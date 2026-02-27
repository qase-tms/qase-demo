#!/usr/bin/env python3
"""
scripts/workspace_init.py — Step 1 of 7: Qase workspace foundation
============================================================
Creates (or reconciles) every workspace-level entity required by downstream
pipeline scripts, then writes ``state/workspace_state.json`` atomically.

Entities provisioned
--------------------
- Qase project  (unique 2-letter code; new project each run)
- 5 custom fields  (selectbox / multiselect for cases), with option IDs
- 3 milestones
- 6 environments
- 4 configuration groups + their items
- 50 shared steps  (3 nested-step patterns cycling A/B/C across all titles)

Usage
-----
  .venv/bin/python scripts/workspace_init.py [--dry-run] [--config PATH]

Design principles
-----------------
- Idempotent (GET-before-POST for all entities except the project itself,
  which always gets a fresh unique code as per plan.md Step 3).
- Rate-limited (≤5 req/sec) with exponential-backoff retry (max 3).
- Atomic state write via temp-file rename.
- ``--dry-run`` prints the full plan without touching the API.
"""
from __future__ import annotations

import argparse
import json
import os
import string
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # type: ignore[assignment]

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_BASE_URL      = "https://api.qase.io/v1"
_RATE_INTERVAL = 1.0 / 5    # 200 ms min gap → ≤5 req/sec
_MAX_RETRIES   = 3
_RETRY_CODES   = frozenset({429, 500, 502, 503, 504})
_REPO_ROOT     = Path(__file__).resolve().parents[1]

# Custom-field type integers (per Qase API docs)
_CF_TYPE = {"selectbox": 3, "multiselect": 6}
_CF_ENTITY_CASE = 0   # entity=0 → test case

# ---------------------------------------------------------------------------
# Shared-step content patterns
# ---------------------------------------------------------------------------
# Three reusable structures cycled by title index (i % 3):
#   Pattern A (i%3 == 0): flat — top-level steps only
#   Pattern B (i%3 == 1): 2 levels deep — child steps with grandchild steps
#   Pattern C (i%3 == 2): 1 level deep — top-level steps with one child level
#
# All 50 shared steps share the same structural skeleton; only the title differs.
# The user's curl example confirmed the API accepts nested `steps` arrays.

_STEP_PATTERN_A = [
    {
        "action": "Open the application and navigate to the target feature",
        "expected_result": "Feature page loads without errors",
        "data": "",
    },
    {
        "action": "Verify the initial state of the page",
        "expected_result": "All UI elements are visible and in their default state",
        "data": "",
    },
    {
        "action": "Perform the primary workflow action",
        "expected_result": "System processes the request and responds accordingly",
        "data": "",
    },
    {
        "action": "Assert the expected outcome is achieved",
        "expected_result": "Result matches the defined acceptance criteria",
        "data": "",
    },
]

_STEP_PATTERN_B = [
    {
        "action": "Open the application and navigate to the target feature",
        "expected_result": "Feature page loads without errors",
        "data": "",
        "steps": [
            {
                "action": "Authenticate as a valid user if no active session exists",
                "expected_result": "User is authenticated and redirected to the intended page",
                "data": "credentials: test@example.com / SecurePass123",
                "steps": [
                    {
                        "action": "Enter email address in the login field",
                        "expected_result": "Email field accepts valid input",
                        "data": "test@example.com",
                    },
                    {
                        "action": "Enter password and submit the login form",
                        "expected_result": "Dashboard is displayed after successful login",
                        "data": "SecurePass123",
                    },
                ],
            },
            {
                "action": "Verify the target page is fully rendered",
                "expected_result": "All dynamic content has loaded",
                "data": "",
                "steps": [
                    {
                        "action": "Check page title and primary heading",
                        "expected_result": "Title matches the expected section label",
                        "data": "",
                    },
                    {
                        "action": "Confirm no error banners or alerts are present",
                        "expected_result": "Page is error-free",
                        "data": "",
                    },
                    {
                        "action": "Verify the primary call-to-action button is enabled",
                        "expected_result": "CTA button is interactive and not disabled",
                        "data": "",
                    },
                ],
            },
        ],
    },
    {
        "action": "Perform the primary workflow action",
        "expected_result": "System processes the request and responds accordingly",
        "data": "",
    },
    {
        "action": "Assert the expected outcome is achieved",
        "expected_result": "Result matches the defined acceptance criteria",
        "data": "",
    },
]

_STEP_PATTERN_C = [
    {
        "action": "Open the application and navigate to the target feature",
        "expected_result": "Feature page loads without errors",
        "data": "",
        "steps": [
            {
                "action": "Verify navigation breadcrumbs are correct",
                "expected_result": "Breadcrumbs reflect the current page location",
                "data": "",
            },
            {
                "action": "Confirm the page URL matches the expected path",
                "expected_result": "URL is correct and no unexpected redirect occurred",
                "data": "",
            },
        ],
    },
    {
        "action": "Perform the primary workflow action",
        "expected_result": "System processes the request and responds accordingly",
        "data": "",
    },
    {
        "action": "Assert the expected outcome is achieved",
        "expected_result": "Result matches the defined acceptance criteria",
        "data": "",
    },
]

# Cycle index → pattern
_STEP_PATTERNS = [_STEP_PATTERN_A, _STEP_PATTERN_B, _STEP_PATTERN_C]

# ---------------------------------------------------------------------------
# Rate limiter
# ---------------------------------------------------------------------------

_last_req_ts: float = 0.0


def _throttle() -> None:
    global _last_req_ts
    gap = time.monotonic() - _last_req_ts
    if gap < _RATE_INTERVAL:
        time.sleep(_RATE_INTERVAL - gap)
    _last_req_ts = time.monotonic()


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

class _APIError(Exception):
    def __init__(self, status: int, body: str) -> None:
        self.status = status
        self.body   = body
        super().__init__(f"HTTP {status}: {body[:200]}")


def _request(
    method: str,
    path: str,
    token: str,
    body: Optional[Dict[str, Any]] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Any:
    url = _BASE_URL + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    data = json.dumps(body).encode() if body is not None else None
    headers: Dict[str, str] = {"Token": token, "Accept": "application/json"}
    if data:
        headers["Content-Type"] = "application/json"

    for attempt in range(_MAX_RETRIES + 1):
        _throttle()
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode(errors="replace")
            if exc.code in _RETRY_CODES and attempt < _MAX_RETRIES:
                wait = min(2 ** attempt, 30)
                print(f"  [RETRY {attempt+1}] HTTP {exc.code} — sleeping {wait}s")
                time.sleep(wait)
                continue
            raise _APIError(exc.code, raw) from exc
    raise RuntimeError("unreachable")


# ---------------------------------------------------------------------------
# Config + state helpers
# ---------------------------------------------------------------------------

def _load_config(config_path: Path) -> Dict[str, Any]:
    if yaml is None:
        sys.exit("Error: PyYAML not installed. Run: .venv/bin/pip install pyyaml")
    if not config_path.exists():
        sys.exit(f"Error: config not found at {config_path}")
    with config_path.open() as fh:
        cfg = yaml.safe_load(fh)
    if not isinstance(cfg, dict):
        sys.exit(f"Error: {config_path} did not parse as a YAML dict")
    return cfg


def _load_token() -> str:
    token = os.environ.get("QASE_API_TOKEN", "").strip()
    if not token:
        sys.exit("Error: QASE_API_TOKEN environment variable is not set.")
    return token


# ---------------------------------------------------------------------------
# Project selection + creation
# ---------------------------------------------------------------------------

def _get_existing_project_codes(token: str) -> Set[str]:
    codes: Set[str] = set()
    offset = 0
    limit  = 100
    while True:
        resp = _request("GET", "/project", token, params={"limit": limit, "offset": offset})
        entities = resp.get("result", {}).get("entities", [])
        for p in entities:
            if p.get("code"):
                codes.add(p["code"].upper())
        total = resp.get("result", {}).get("total", 0)
        offset += len(entities)
        if offset >= total or not entities:
            break
    return codes


def _next_code(existing: Set[str]) -> str:
    """Return the first unused 2-letter uppercase code in alphabetical order."""
    letters = string.ascii_uppercase
    for a in letters:
        for b in letters:
            code = a + b
            if code not in existing:
                return code
    sys.exit("Error: all 2-letter project codes are exhausted.")


def _create_project(token: str, title: str, description: str, code: str) -> str:
    resp = _request("POST", "/project", token, body={
        "title":       title,
        "code":        code,
        "description": description,
        "access":      "none",
    })
    returned_code: str = resp.get("result", {}).get("code", code)
    return returned_code


# ---------------------------------------------------------------------------
# Custom fields
# ---------------------------------------------------------------------------

def _list_custom_fields(token: str) -> List[Dict[str, Any]]:
    fields: List[Dict[str, Any]] = []
    offset = 0
    while True:
        resp = _request("GET", "/custom_field", token, params={"limit": 50, "offset": offset})
        batch = resp.get("result", {}).get("entities", [])
        fields.extend(batch)
        total = resp.get("result", {}).get("total", 0)
        offset += len(batch)
        if offset >= total or not batch:
            break
    return fields


def _get_cf_detail(token: str, cf_id: int) -> Dict[str, Any]:
    resp = _request("GET", f"/custom_field/{cf_id}", token)
    return resp.get("result", {})


def _parse_cf_options(detail: Dict[str, Any]) -> Dict[str, str]:
    """Return {option_title: str(option_id)} from the 'value' JSON string."""
    raw = detail.get("value", "[]") or "[]"
    try:
        opts = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return {o["title"]: str(o["id"]) for o in opts if "title" in o and "id" in o}


def _create_custom_field(
    token: str,
    name: str,
    cf_type: str,
    options: List[str],
) -> Tuple[int, Dict[str, str]]:
    """Create a CF and return (id, {option_title: str(option_id)}).
    Note: the CREATE endpoint does not return option IDs; we fetch them back.
    """
    type_int = _CF_TYPE.get(cf_type)
    if type_int is None:
        sys.exit(f"Error: unknown CF type {cf_type!r} (supported: {list(_CF_TYPE)})")

    body: Dict[str, Any] = {
        "title":                    name,
        "entity":                   _CF_ENTITY_CASE,
        "type":                     type_int,
        "is_filterable":            True,
        "is_visible":               True,
        "is_required":              False,
        "is_enabled_for_all_projects": True,
    }
    if options:
        body["value"] = [{"id": i, "title": opt} for i, opt in enumerate(options, 1)]

    resp   = _request("POST", "/custom_field", token, body=body)
    cf_id  = resp.get("result", {}).get("id")
    if not cf_id:
        sys.exit(f"Error: POST /custom_field returned no id for {name!r}")

    # Fetch back to read assigned option IDs
    detail  = _get_cf_detail(token, cf_id)
    opt_map = _parse_cf_options(detail)
    return int(cf_id), opt_map


def _reconcile_custom_fields(
    token: str,
    cf_configs: List[Dict[str, Any]],
    dry_run: bool,
) -> Dict[str, Dict[str, Any]]:
    """
    For each CF in config: find by name among existing fields → reuse + capture
    option IDs. If not found → create. Returns {cf_name: {id, options}}.
    """
    existing = _list_custom_fields(token)
    existing_by_name = {f["title"].lower(): f for f in existing}

    result: Dict[str, Dict[str, Any]] = {}
    for cf in cf_configs:
        name    = cf["name"]
        cf_type = cf["type"]
        options = cf.get("options", [])

        match = existing_by_name.get(name.lower())
        if match:
            cf_id  = int(match["id"])
            detail = _get_cf_detail(token, cf_id)
            opt_map = _parse_cf_options(detail)
            action = "REUSE"
        else:
            if dry_run:
                print(f"  [DRY-RUN] Would CREATE custom field {name!r} (type={cf_type})")
                result[name] = {"id": 0, "options": {o: "?" for o in options}}
                continue
            cf_id, opt_map = _create_custom_field(token, name, cf_type, options)
            action = "CREATE"

        result[name] = {"id": cf_id, "options": opt_map}
        print(f"  {action:6s}  CF {name!r}  id={cf_id}  options({len(opt_map)}): {opt_map}")

    return result


# ---------------------------------------------------------------------------
# Milestones
# ---------------------------------------------------------------------------

def _reconcile_milestones(
    token: str,
    code: str,
    milestone_configs: List[Dict[str, Any]],
    dry_run: bool,
) -> Dict[str, int]:
    resp     = _request("GET", f"/milestone/{code}", token, params={"limit": 100})
    existing = {m["title"].lower(): m["id"] for m in resp.get("result", {}).get("entities", [])}

    result: Dict[str, int] = {}
    for m in milestone_configs:
        title = m["title"]
        match = existing.get(title.lower())
        if match:
            result[title] = int(match)
            print(f"  REUSE   milestone {title!r}  id={match}")
        else:
            if dry_run:
                print(f"  [DRY-RUN] Would CREATE milestone {title!r}")
                result[title] = 0
                continue
            resp2  = _request("POST", f"/milestone/{code}", token, body={"title": title})
            new_id = resp2.get("result", {}).get("id")
            result[title] = int(new_id)
            print(f"  CREATE  milestone {title!r}  id={new_id}")

    return result


# ---------------------------------------------------------------------------
# Environments
# ---------------------------------------------------------------------------

def _reconcile_environments(
    token: str,
    code: str,
    env_configs: List[Dict[str, Any]],
    dry_run: bool,
) -> Dict[str, int]:
    resp     = _request("GET", f"/environment/{code}", token, params={"limit": 100})
    existing = {e["slug"].lower(): e for e in resp.get("result", {}).get("entities", [])}

    result: Dict[str, int] = {}
    for env in env_configs:
        title = env["title"]
        slug  = env["slug"]
        host  = env.get("host", "")
        match = existing.get(slug.lower())
        if match:
            result[title] = int(match["id"])
            print(f"  REUSE   environment {title!r}  slug={slug}  id={match['id']}")
        else:
            if dry_run:
                print(f"  [DRY-RUN] Would CREATE environment {title!r}  slug={slug}")
                result[title] = 0
                continue
            resp2  = _request("POST", f"/environment/{code}", token, body={
                "title": title, "slug": slug, "host": host,
            })
            new_id = resp2.get("result", {}).get("id")
            result[title] = int(new_id)
            print(f"  CREATE  environment {title!r}  slug={slug}  id={new_id}")

    return result


# ---------------------------------------------------------------------------
# Configurations
# ---------------------------------------------------------------------------

def _reconcile_configurations(
    token: str,
    code: str,
    cfg_groups: List[Dict[str, Any]],
    dry_run: bool,
) -> Dict[str, Any]:
    resp     = _request("GET", f"/configuration/{code}", token, params={"limit": 100})
    entities = resp.get("result", {}).get("entities", [])

    # Build existing maps: {group_title_lower: group_id} and
    # {group_id: {item_title_lower: item_id}}
    existing_groups: Dict[str, int]             = {}
    existing_items:  Dict[int, Dict[str, int]]  = {}
    for item in entities:
        grp      = item.get("group", {})
        gid      = int(grp.get("id", 0))
        gtitle   = grp.get("title", "").lower()
        existing_groups.setdefault(gtitle, gid)
        existing_items.setdefault(gid, {})[item["title"].lower()] = int(item["id"])

    result: Dict[str, Any] = {}
    for grp_cfg in cfg_groups:
        grp_title = grp_cfg["group"]
        items     = grp_cfg.get("items", [])
        gid = existing_groups.get(grp_title.lower())

        if gid:
            print(f"  REUSE   config group {grp_title!r}  id={gid}")
        else:
            if dry_run:
                print(f"  [DRY-RUN] Would CREATE config group {grp_title!r}")
                result[grp_title] = {"group_id": 0, "items": {}}
                continue
            gresp = _request("POST", f"/configuration/{code}/group", token,
                             body={"title": grp_title})
            gid   = int(gresp.get("result", {}).get("id", 0))
            existing_items[gid] = {}
            print(f"  CREATE  config group {grp_title!r}  id={gid}")

        item_ids: Dict[str, int] = {}
        grp_items = existing_items.get(gid, {})
        for item_title in items:
            iid = grp_items.get(item_title.lower())
            if iid:
                item_ids[item_title] = iid
                print(f"    REUSE   config item {item_title!r}  id={iid}")
            else:
                if dry_run:
                    print(f"    [DRY-RUN] Would CREATE config item {item_title!r}")
                    item_ids[item_title] = 0
                    continue
                iresp = _request("POST", f"/configuration/{code}", token,
                                 body={"title": item_title, "group_id": gid})
                iid   = int(iresp.get("result", {}).get("id", 0))
                item_ids[item_title] = iid
                print(f"    CREATE  config item {item_title!r}  id={iid}")

        result[grp_title] = {"group_id": gid, "items": item_ids}

    return result


# ---------------------------------------------------------------------------
# Shared steps
# ---------------------------------------------------------------------------

def _reconcile_shared_steps(
    token: str,
    code: str,
    titles: List[str],
    dry_run: bool,
) -> Dict[str, str]:
    """
    Idempotently create 50 shared steps in ``code``.

    ``titles`` is a list of strings (from workspace.yaml ``shared_steps``).
    Step content is generated by cycling _STEP_PATTERNS[i % 3]:
      - i%3 == 0  →  Pattern A: flat (4 top-level steps, no children)
      - i%3 == 1  →  Pattern B: 2 levels deep (children + grandchildren)
      - i%3 == 2  →  Pattern C: 1 level deep (top-level steps with children)

    Returns ``{title: hash}`` for state persistence.
    Idempotency: match by title — if a shared step with that exact title already
    exists in the project, reuse it and capture its hash.
    """
    # Fetch all existing shared steps (skip in dry-run: project may not exist yet)
    existing: Dict[str, str] = {}   # {title_lower: hash}
    if not dry_run:
        offset = 0
        while True:
            resp   = _request("GET", f"/shared_step/{code}", token,
                              params={"limit": 100, "offset": offset})
            result = resp.get("result", {})
            batch  = result.get("entities", [])
            for ss in batch:
                existing[ss["title"].lower()] = ss.get("hash", "")
            total  = result.get("total", 0)
            offset += len(batch)
            if offset >= total or not batch:
                break

    state_hashes: Dict[str, str] = {}
    created = reused = 0

    for idx, title in enumerate(titles):
        pattern = _STEP_PATTERNS[idx % 3]
        key     = title.lower()

        if key in existing:
            state_hashes[title] = existing[key]
            reused += 1
            pattern_name = ["A (flat)", "B (2-level)", "C (1-level)"][idx % 3]
            print(f"  REUSE   [{idx+1:02d}] {title!r}  pattern={pattern_name}  hash={existing[key][:12]}…")
            continue

        if dry_run:
            pattern_name = ["A (flat)", "B (2-level)", "C (1-level)"][idx % 3]
            print(f"  [DRY-RUN] Would CREATE [{idx+1:02d}] {title!r}  pattern={pattern_name}")
            state_hashes[title] = ""
            continue

        resp2  = _request("POST", f"/shared_step/{code}", token,
                          body={"title": title, "steps": pattern})
        pattern_name = ["A (flat)", "B (2-level)", "C (1-level)"][idx % 3]
        print(f"  CREATE  [{idx+1:02d}] {title!r}  pattern={pattern_name}")
        state_hashes[title] = ""   # hash captured in bulk-fetch pass below
        created += 1

    if not dry_run:
        print(f"  → Shared steps: {created} created, {reused} reused (total {len(titles)})")
        # Bulk-fetch to capture hashes for any steps we just created
        if created > 0:
            all_ss: Dict[str, str] = {}
            offset2 = 0
            while True:
                r2     = _request("GET", f"/shared_step/{code}", token,
                                  params={"limit": 100, "offset": offset2})
                batch2 = r2.get("result", {}).get("entities", [])
                for ss in batch2:
                    all_ss[ss["title"]] = ss.get("hash", "")
                total2  = r2.get("result", {}).get("total", 0)
                offset2 += len(batch2)
                if offset2 >= total2 or not batch2:
                    break
            for t in state_hashes:
                if not state_hashes[t] and t in all_ss:
                    state_hashes[t] = all_ss[t]
    return state_hashes


# ---------------------------------------------------------------------------
# Post-execution validation
# ---------------------------------------------------------------------------

def _validate(token: str, code: str, cfg: Dict[str, Any], state: Dict[str, Any]) -> None:
    print("\n[VALIDATE] Re-querying entities...")
    ok = True

    # Project
    try:
        _request("GET", f"/project/{code}", token)
        print(f"  OK  project {code!r}")
    except _APIError as exc:
        print(f"  FAIL project {code!r}: {exc}")
        ok = False

    # Custom fields
    expected_cfs = {cf["name"] for cf in cfg.get("custom_fields", [])}
    actual_cfs   = set(state.get("custom_fields", {}).keys())
    if expected_cfs <= actual_cfs:
        print(f"  OK  custom_fields ({len(expected_cfs)} found)")
    else:
        missing = expected_cfs - actual_cfs
        print(f"  FAIL custom_fields missing: {missing}")
        ok = False

    # Milestones
    resp      = _request("GET", f"/milestone/{code}", token, params={"limit": 100})
    n_miles   = len(resp.get("result", {}).get("entities", []))
    exp_miles = len(cfg.get("milestones", []))
    if n_miles >= exp_miles:
        print(f"  OK  milestones ({n_miles} found, expected ≥{exp_miles})")
    else:
        print(f"  FAIL milestones: found {n_miles}, expected {exp_miles}")
        ok = False

    # Environments
    resp    = _request("GET", f"/environment/{code}", token, params={"limit": 100})
    n_envs  = len(resp.get("result", {}).get("entities", []))
    exp_env = len(cfg.get("environments", []))
    if n_envs >= exp_env:
        print(f"  OK  environments ({n_envs} found, expected ≥{exp_env})")
    else:
        print(f"  FAIL environments: found {n_envs}, expected {exp_env}")
        ok = False

    # Shared steps
    resp    = _request("GET", f"/shared_step/{code}", token, params={"limit": 100})
    n_ss    = resp.get("result", {}).get("total", 0)
    exp_ss  = len(cfg.get("shared_steps", []))
    if n_ss >= exp_ss:
        print(f"  OK  shared_steps ({n_ss} found, expected ≥{exp_ss})")
    else:
        print(f"  FAIL shared_steps: found {n_ss}, expected {exp_ss}")
        ok = False

    if not ok:
        sys.exit("Error: post-execution validation failed.")
    print("[VALIDATE] All checks passed.")


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

def _run(args: argparse.Namespace) -> None:
    dry_run = getattr(args, "dry_run", False)
    config_path = Path(getattr(args, "config", None) or (_REPO_ROOT / "config" / "workspace.yaml"))
    state_path  = _REPO_ROOT / "state" / "workspace_state.json"

    # ── load config ──────────────────────────────────────────────────────────
    cfg   = _load_config(config_path)
    token = _load_token()

    proj_cfg  = cfg.get("project", {})
    proj_name = proj_cfg.get("name", "ShopEase Web App")
    proj_desc = proj_cfg.get("description", "")

    print(f"=== scripts/workspace_init.py {'(DRY-RUN) ' if dry_run else ''}===")
    print(f"Config: {config_path}")
    print(f"Target project: {proj_name!r}\n")

    # ── pre-execution validation ──────────────────────────────────────────────
    print("[PREFLIGHT] Verifying API token...")
    try:
        _request("GET", "/project", token, params={"limit": 1})
        print("  OK  API token valid")
    except _APIError as exc:
        sys.exit(f"Error: API token rejected (HTTP {exc.status}). Check QASE_API_TOKEN.")

    # ── project ───────────────────────────────────────────────────────────────
    print("\n[PROJECT] Selecting unique project code...")
    existing_codes = _get_existing_project_codes(token)
    code           = _next_code(existing_codes)
    print(f"  Existing codes ({len(existing_codes)}): {sorted(existing_codes)}")
    print(f"  Selected code: {code!r}")

    if dry_run:
        print(f"  [DRY-RUN] Would CREATE project {proj_name!r} with code={code!r}")
    else:
        code = _create_project(token, proj_name, proj_desc, code)
        print(f"  CREATE  project {proj_name!r}  code={code}")

    # ── custom fields ─────────────────────────────────────────────────────────
    print("\n[CUSTOM FIELDS]")
    cf_result = _reconcile_custom_fields(
        token, cfg.get("custom_fields", []), dry_run
    )

    # ── milestones ────────────────────────────────────────────────────────────
    print(f"\n[MILESTONES] (project={code})")
    if not dry_run:
        milestone_ids = _reconcile_milestones(
            token, code, cfg.get("milestones", []), dry_run
        )
    else:
        for m in cfg.get("milestones", []):
            print(f"  [DRY-RUN] Would CREATE milestone {m['title']!r}")
        milestone_ids = {m["title"]: 0 for m in cfg.get("milestones", [])}

    # ── environments ──────────────────────────────────────────────────────────
    print(f"\n[ENVIRONMENTS] (project={code})")
    if not dry_run:
        environment_ids = _reconcile_environments(
            token, code, cfg.get("environments", []), dry_run
        )
    else:
        for e in cfg.get("environments", []):
            print(f"  [DRY-RUN] Would CREATE environment {e['title']!r}")
        environment_ids = {e["title"]: 0 for e in cfg.get("environments", [])}

    # ── configurations ────────────────────────────────────────────────────────
    print(f"\n[CONFIGURATIONS] (project={code})")
    if not dry_run:
        configuration_ids = _reconcile_configurations(
            token, code, cfg.get("configurations", []), dry_run
        )
    else:
        for grp in cfg.get("configurations", []):
            print(f"  [DRY-RUN] Would CREATE config group {grp['group']!r} "
                  f"with {len(grp.get('items', []))} items")
        configuration_ids = {}

    # ── shared steps ──────────────────────────────────────────────────────────
    ss_titles = cfg.get("shared_steps", [])
    print(f"\n[SHARED STEPS] (project={code})  —  {len(ss_titles)} title(s), patterns A/B/C cycling")
    shared_step_hashes = _reconcile_shared_steps(
        token, code, ss_titles, dry_run
    )

    # ── build state ───────────────────────────────────────────────────────────
    state: Dict[str, Any] = {
        "project_code":        code,
        "custom_fields":       cf_result,
        "milestone_ids":       milestone_ids,
        "environment_ids":     environment_ids,
        "configuration_ids":   configuration_ids,
        "shared_step_hashes":  shared_step_hashes,
        "suite_ids":           {},
        "case_ids":            {},
    }

    if dry_run:
        print("\n[DRY-RUN] State that would be written:")
        print(json.dumps(state, indent=2))
        print("\n[DRY-RUN] No API calls made, no state written.")
        return

    # ── post-execution validation ─────────────────────────────────────────────
    _validate(token, code, cfg, state)

    # ── atomic state write ────────────────────────────────────────────────────
    state_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = state_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2))
    tmp.replace(state_path)
    print(f"\n[STATE] Written → {state_path.relative_to(_REPO_ROOT)}")

    # ── summary ───────────────────────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"scripts/workspace_init.py complete")
    print(f"  project_code:    {code}")
    print(f"  custom_fields:   {len(cf_result)}")
    print(f"  milestones:      {len(milestone_ids)}")
    print(f"  environments:    {len(environment_ids)}")
    print(f"  config groups:   {len(configuration_ids)}")
    print(f"  shared steps:    {len(shared_step_hashes)}")
    print(f"{'='*50}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Initialize Qase workspace: project, CFs, milestones, environments, configs."
    )
    parser.add_argument("--dry-run",  action="store_true",
                        help="Print plan without making API calls.")
    parser.add_argument("--config",   default=None,
                        help="Path to workspace.yaml (default: config/workspace.yaml).")
    args = parser.parse_args()
    _run(args)


if __name__ == "__main__":
    main()
