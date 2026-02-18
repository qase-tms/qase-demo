"""
workspace_init.py – Idempotent Qase workspace initialisation script.

Usage:
    python workspace_init.py [--dry-run]

Requirements:
    QASE_API_TOKEN env var must be set.
    config/workspace.yaml must exist.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import random
import string
import sys
import time
from pathlib import Path
from typing import Any

import requests
import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
CONFIG_PATH = Path("config/workspace.yaml")
STATE_PATH = Path("state/workspace_state.json")
QASE_BASE_URL = "https://api.qase.io/v1"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("workspace_init")

# ---------------------------------------------------------------------------
# T001 – Argument parsing
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialise a Qase demo workspace idempotently."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print intended actions without making API mutations.",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# T004 – Config loader
# ---------------------------------------------------------------------------
def load_config(path: Path) -> dict:
    if not path.exists():
        logger.error("Config file not found: %s", path)
        sys.exit(1)
    with path.open("r") as fh:
        cfg = yaml.safe_load(fh)
    if not cfg:
        logger.error("Config file is empty: %s", path)
        sys.exit(1)
    return cfg


# ---------------------------------------------------------------------------
# T005 – State manager
# ---------------------------------------------------------------------------
def load_state(path: Path) -> dict:
    if path.exists():
        text = path.read_text(encoding="utf-8").strip()
        if text:
            return json.loads(text)
    return {}


def save_state(path: Path, state: dict) -> None:
    """T018 – Atomic write via rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with tmp.open("w") as fh:
        json.dump(state, fh, indent=2)
    os.replace(tmp, path)


# ---------------------------------------------------------------------------
# T006 – Rate limiter (≤5 req/s)
# ---------------------------------------------------------------------------
_last_call: float = 0.0
_MIN_INTERVAL = 1.0 / 5  # 200 ms between calls


def _rate_limit() -> None:
    global _last_call
    elapsed = time.monotonic() - _last_call
    if elapsed < _MIN_INTERVAL:
        time.sleep(_MIN_INTERVAL - elapsed)
    _last_call = time.monotonic()


# ---------------------------------------------------------------------------
# T007 – HTTP client with retry + error handling
# ---------------------------------------------------------------------------
def _call(
    method: str,
    path: str,
    token: str,
    *,
    params: dict | None = None,
    body: dict | None = None,
    max_retries: int = 3,
) -> dict | None:
    """
    Make an authenticated Qase API call with exponential-backoff retries.
    Returns parsed JSON body on success, None on unrecoverable error.
    """
    url = f"{QASE_BASE_URL}{path}"
    headers = {"Token": token, "Content-Type": "application/json", "Accept": "application/json"}
    backoff = 1.0

    for attempt in range(1, max_retries + 1):
        _rate_limit()
        try:
            resp = requests.request(
                method.upper(),
                url,
                headers=headers,
                params=params,
                json=body,
                timeout=30,
            )
        except requests.RequestException as exc:
            logger.warning("Network error (attempt %d/%d): %s", attempt, max_retries, exc)
            if attempt < max_retries:
                time.sleep(backoff)
                backoff *= 2
                continue
            logger.error("Giving up on %s %s after %d attempts.", method, path, max_retries)
            return None

        if resp.status_code == 429:
            retry_after = float(resp.headers.get("Retry-After", backoff))
            logger.warning("Rate-limited; sleeping %.1fs (attempt %d/%d).", retry_after, attempt, max_retries)
            time.sleep(retry_after)
            backoff = retry_after * 2
            continue

        if resp.status_code >= 500:
            logger.warning("Server error %d (attempt %d/%d): %s", resp.status_code, attempt, max_retries, resp.text[:200])
            if attempt < max_retries:
                time.sleep(backoff)
                backoff *= 2
                continue
            logger.error("Giving up on %s %s after %d attempts (5xx).", method, path, max_retries)
            return None

        if not resp.ok:
            logger.error("API error %d for %s %s: %s", resp.status_code, method, path, resp.text[:300])
            return None

        try:
            return resp.json()
        except ValueError:
            return {"status": True}

    return None


# ---------------------------------------------------------------------------
# T008 – Pre-execution validation
# ---------------------------------------------------------------------------
def validate_pre_execution(token: str, dry_run: bool) -> bool:
    """Verify API key, connectivity, and config schema."""
    if not token:
        logger.error("QASE_API_TOKEN is not set.")
        return False

    if dry_run:
        logger.info("[DRY-RUN] Skipping live API connectivity check.")
        return True

    logger.info("Verifying API token and connectivity …")
    resp = _call("GET", "/project", token, params={"limit": 1})
    if resp is None:
        logger.error("Pre-execution check failed: cannot reach Qase API.")
        return False
    logger.info("API token valid. Connection OK.")
    return True


# ---------------------------------------------------------------------------
# T009 – Config schema validation
# ---------------------------------------------------------------------------
def validate_config(cfg: dict) -> bool:
    required = ["project", "custom_fields", "environments", "milestones",
                "configurations", "shared_steps", "shared_parameters"]
    for key in required:
        if key not in cfg:
            logger.error("Config missing required key: '%s'", key)
            return False
    if "name" not in cfg["project"]:
        logger.error("Config 'project' section missing 'name'.")
        return False
    return True


# ---------------------------------------------------------------------------
# Helper: paginate a list endpoint
# ---------------------------------------------------------------------------
def _paginate(path: str, token: str, params: dict | None = None) -> list[dict]:
    entities: list[dict] = []
    offset = 0
    limit = 100
    base_params = dict(params or {})
    while True:
        resp = _call("GET", path, token, params={**base_params, "limit": limit, "offset": offset})
        if not resp or not resp.get("result"):
            break
        result = resp["result"]
        batch = result.get("entities") or []
        entities.extend(batch)
        total = result.get("total", 0)
        offset += limit
        if offset >= total:
            break
    return entities


# ---------------------------------------------------------------------------
# T010 – Project creation / reconciliation
# ---------------------------------------------------------------------------
def _generate_unique_code(existing: set[str], length: int = 2) -> str:
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        if code not in existing:
            return code


def reconcile_project(cfg: dict, state: dict, token: str, dry_run: bool) -> bool:
    name = cfg["project"]["name"]
    description = cfg["project"].get("description", "")
    access = cfg["project"].get("access", "none")

    logger.info("=== Project ===")

    if dry_run:
        logger.info("[DRY-RUN] Would query projects and create/reuse '%s'.", name)
        state.setdefault("project_code", "DR")
        return True

    # Fast path: if we already have a saved project code, verify it still exists and
    # belongs to this project. This avoids full-list pagination when the workspace
    # has accumulated many projects from previous runs.
    saved_code = state.get("project_code", "")
    if saved_code and saved_code not in ("DR",):
        probe = _call("GET", f"/project/{saved_code}", token)
        if probe and probe.get("result", {}).get("title") == name:
            logger.info("Reused project '%s' (code=%s, from state).", name, saved_code)
            return True

    # Fall back to full list search (handles first run or code mismatch)
    projects = _paginate("/project", token)
    existing_codes = {p["code"] for p in projects}
    match = next((p for p in projects if p["title"] == name), None)

    if match:
        state["project_code"] = match["code"]
        logger.info("Reused project '%s' (code=%s).", name, match["code"])
    else:
        code = _generate_unique_code(existing_codes)
        body = {"title": name, "code": code, "description": description, "access": access}
        resp = _call("POST", "/project", token, body=body)
        if not resp:
            logger.error("Failed to create project '%s'.", name)
            return False
        # Project create returns {"result": {"code": "XY"}}, no numeric id
        state["project_code"] = resp.get("result", {}).get("code", code)
        logger.info("Created project '%s' (code=%s).", name, state["project_code"])

    return True


# ---------------------------------------------------------------------------
# T011 – Custom fields creation / reconciliation
# ---------------------------------------------------------------------------
_CF_TYPE_MAP = {
    "number": 0,
    "string": 1,
    "text": 2,
    "selectbox": 3,
    "checkbox": 4,
    "radio": 5,
    "multiselect": 6,
    "url": 7,
    "user": 8,
    "datetime": 9,
}


def reconcile_custom_fields(cfg: dict, state: dict, token: str, dry_run: bool) -> bool:
    fields_cfg = cfg.get("custom_fields", [])
    logger.info("=== Custom Fields (%d) ===", len(fields_cfg))
    state.setdefault("custom_fields", {})

    if dry_run:
        for f in fields_cfg:
            logger.info("[DRY-RUN] Would create/reuse custom field '%s'.", f["name"])
        return True

    existing_fields = _paginate("/custom_field", token)
    existing_by_name = {f["title"]: f for f in existing_fields}

    for field_def in fields_cfg:
        fname = field_def["name"]
        ftype_str = field_def.get("type", "string")
        ftype_int = _CF_TYPE_MAP.get(ftype_str, 1)
        options = field_def.get("options", [])
        # API rejects id=0; valid IDs start at 1
        value_list = [{"id": i + 1, "title": opt} for i, opt in enumerate(options)]

        if fname in existing_by_name:
            # The list endpoint returns full field data including `value` (array)
            # and `is_enabled_for_all_projects` — use directly, no extra GET needed.
            existing = existing_by_name[fname]
            fid = existing["id"]
            state["custom_fields"][fname] = {"id": fid}

            already_enabled = existing.get("is_enabled_for_all_projects", False)
            raw_value = existing.get("value")
            parsed_values: list[dict] = raw_value if isinstance(raw_value, list) else []

            needs_patch = False
            # Always include is_enabled_for_all_projects=True in every PATCH.
            # Qase resets omitted boolean flags on write, so we re-assert every time.
            patch_body: dict[str, Any] = {
                "title": fname,
                "is_enabled_for_all_projects": True,
            }

            if not already_enabled:
                needs_patch = True

            # Reconcile options for selectbox/radio/multiselect fields
            missing_opts: list[dict] = []
            if value_list:
                existing_titles = {v["title"] for v in parsed_values}
                missing_opts = [v for v in value_list if v["title"] not in existing_titles]
                if missing_opts:
                    merged = parsed_values + missing_opts
                    patch_body["value"] = [
                        {"id": i + 1, "title": v["title"]} for i, v in enumerate(merged)
                    ]
                    needs_patch = True
                elif needs_patch:
                    # Patching for another reason; must supply non-empty value or API returns 400
                    patch_body["value"] = (
                        [{"id": i + 1, "title": v["title"]} for i, v in enumerate(parsed_values)]
                        if parsed_values else value_list
                    )

            if needs_patch:
                _call("PATCH", f"/custom_field/{fid}", token, body=patch_body)
                updates = []
                if not already_enabled:
                    updates.append("enabled for all projects")
                if missing_opts:
                    updates.append(f"added {len(missing_opts)} option(s)")
                logger.info("Updated custom field '%s': %s.", fname,
                            ", ".join(updates) if updates else "reinforced settings")
            else:
                logger.info("Reused custom field '%s' (id=%d, up to date).", fname, fid)
        else:
            body: dict[str, Any] = {
                "title": fname,
                "entity": 0,  # 0 = case
                "type": ftype_int,
                "is_enabled_for_all_projects": True,
                "is_visible": True,
            }
            if value_list:
                body["value"] = value_list
            resp = _call("POST", "/custom_field", token, body=body)
            if resp:
                fid = resp.get("result", {}).get("id")
                state["custom_fields"][fname] = {"id": fid}
                logger.info("Created custom field '%s' (id=%s).", fname, fid)
            else:
                logger.error("Failed to create custom field '%s'.", fname)

    return True


# ---------------------------------------------------------------------------
# T012 – Environments creation / reconciliation
# ---------------------------------------------------------------------------
def reconcile_environments(cfg: dict, state: dict, token: str, dry_run: bool) -> bool:
    envs_cfg = cfg.get("environments", [])
    project_code = state.get("project_code", "")
    logger.info("=== Environments (%d) ===", len(envs_cfg))
    state.setdefault("environments", {})

    if dry_run:
        for e in envs_cfg:
            logger.info("[DRY-RUN] Would create/reuse environment '%s'.", e["title"])
        return True

    existing = _paginate(f"/environment/{project_code}", token)
    existing_by_slug = {e["slug"]: e for e in existing}

    for env_def in envs_cfg:
        title = env_def["title"]
        slug = env_def["slug"]
        host = env_def.get("host", "")

        if slug in existing_by_slug:
            ex = existing_by_slug[slug]
            eid = ex["id"]
            state["environments"][title] = eid
            if ex.get("host") != host:
                _call("PATCH", f"/environment/{project_code}/{eid}", token,
                      body={"title": title, "slug": slug, "host": host})
                logger.info("Updated environment '%s' host.", title)
            else:
                logger.info("Reused environment '%s' (id=%d).", title, eid)
        else:
            resp = _call("POST", f"/environment/{project_code}", token,
                         body={"title": title, "slug": slug, "host": host})
            if resp:
                eid = resp.get("result", {}).get("id")
                state["environments"][title] = eid
                logger.info("Created environment '%s' (id=%s).", title, eid)
            else:
                logger.error("Failed to create environment '%s'.", title)

    return True


# ---------------------------------------------------------------------------
# T013 – Milestones creation / reconciliation
# ---------------------------------------------------------------------------
def reconcile_milestones(cfg: dict, state: dict, token: str, dry_run: bool) -> bool:
    milestones_cfg = cfg.get("milestones", [])
    project_code = state.get("project_code", "")
    logger.info("=== Milestones (%d) ===", len(milestones_cfg))
    state.setdefault("milestones", {})

    if dry_run:
        for m in milestones_cfg:
            logger.info("[DRY-RUN] Would create/reuse milestone '%s'.", m["title"])
        return True

    existing = _paginate(f"/milestone/{project_code}", token)
    existing_by_title = {m["title"]: m for m in existing}

    for ms_def in milestones_cfg:
        title = ms_def["title"]
        if title in existing_by_title:
            mid = existing_by_title[title]["id"]
            state["milestones"][title] = mid
            logger.info("Reused milestone '%s' (id=%d).", title, mid)
        else:
            resp = _call("POST", f"/milestone/{project_code}", token, body={"title": title})
            if resp:
                mid = resp.get("result", {}).get("id")
                state["milestones"][title] = mid
                logger.info("Created milestone '%s' (id=%s).", title, mid)
            else:
                logger.error("Failed to create milestone '%s'.", title)

    return True


# ---------------------------------------------------------------------------
# T014 – Configurations creation / reconciliation
# ---------------------------------------------------------------------------
def reconcile_configurations(cfg: dict, state: dict, token: str, dry_run: bool) -> bool:
    configs_cfg = cfg.get("configurations", [])
    project_code = state.get("project_code", "")
    logger.info("=== Configurations (%d groups) ===", len(configs_cfg))
    state.setdefault("configurations", {})

    if dry_run:
        for g in configs_cfg:
            logger.info("[DRY-RUN] Would create/reuse configuration group '%s'.", g["group"])
        return True

    # GET /configuration/{code} returns a list of GROUP objects, each with:
    #   {"id": N, "title": "Browser", "configurations": [{"id": M, "title": "Chrome"}, ...]}
    existing_groups_raw = _paginate(f"/configuration/{project_code}", token)

    # Build map: normalized group title -> {group_id, items: {title -> item_id}}
    groups_map: dict[str, dict] = {}
    for grp_entity in existing_groups_raw:
        grp_title = grp_entity.get("title", "")
        norm = grp_title.strip().lower()
        gid = grp_entity.get("id")
        items: dict[str, int] = {}
        for sub in (grp_entity.get("configurations") or []):
            items[sub["title"]] = sub["id"]
        groups_map[norm] = {"id": gid, "title": grp_title, "items": items}

    for grp_def in configs_cfg:
        group_title = grp_def["group"]
        items = grp_def.get("items", [])
        norm = group_title.strip().lower()

        if norm in groups_map:
            gid = groups_map[norm]["id"]
            state["configurations"][group_title] = {"id": gid, "items": dict(groups_map[norm]["items"])}
            existing_item_titles = set(groups_map[norm]["items"].keys())
            missing = [i for i in items if i not in existing_item_titles]
            if missing:
                for item_title in missing:
                    r = _call("POST", f"/configuration/{project_code}", token,
                              body={"title": item_title, "group_id": gid})
                    if r:
                        iid = r.get("result", {}).get("id")
                        state["configurations"][group_title]["items"][item_title] = iid
                        logger.info("Added config item '%s' to group '%s'.", item_title, group_title)
                    else:
                        logger.error("Failed to add config item '%s'.", item_title)
            else:
                logger.info("Reused configuration group '%s' (id=%d, %d items).",
                            group_title, gid, len(existing_item_titles))
        else:
            # Create the group first, then each item individually
            r_grp = _call("POST", f"/configuration/{project_code}/group", token,
                          body={"title": group_title})
            if not r_grp:
                logger.error("Failed to create configuration group '%s'.", group_title)
                continue
            gid = r_grp.get("result", {}).get("id")
            state["configurations"][group_title] = {"id": gid, "items": {}}
            logger.info("Created configuration group '%s' (id=%s).", group_title, gid)
            for item_title in items:
                r_item = _call("POST", f"/configuration/{project_code}", token,
                               body={"title": item_title, "group_id": gid})
                if r_item:
                    iid = r_item.get("result", {}).get("id")
                    state["configurations"][group_title]["items"][item_title] = iid
                    logger.info("  + config item '%s' (id=%s).", item_title, iid)
                else:
                    logger.error("Failed to create config item '%s'.", item_title)

    return True


# ---------------------------------------------------------------------------
# T015 – Shared steps creation / reconciliation
# ---------------------------------------------------------------------------
def _step_hash(steps: list[dict]) -> str:
    canonical = json.dumps(steps, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]


def reconcile_shared_steps(cfg: dict, state: dict, token: str, dry_run: bool) -> bool:
    steps_cfg = cfg.get("shared_steps", [])
    project_code = state.get("project_code", "")
    logger.info("=== Shared Steps (%d) ===", len(steps_cfg))
    state.setdefault("shared_steps", {})

    if dry_run:
        for s in steps_cfg:
            logger.info("[DRY-RUN] Would create/reuse shared step '%s'.", s["title"])
        return True

    # Correct endpoint: /shared_step/{code}
    existing = _paginate(f"/shared_step/{project_code}", token)
    existing_by_title = {s["title"]: s for s in existing}

    for step_def in steps_cfg:
        title = step_def["title"]
        steps = step_def.get("steps", [])

        if title in existing_by_title:
            ex = existing_by_title[title]
            shash = ex.get("hash", "")
            sid = ex.get("id")
            state["shared_steps"][title] = {"id": sid, "hash": shash}
            logger.info("Reused shared step '%s' (id=%s, hash=%s).", title, sid, shash)
        else:
            step_bodies = []
            for pos, st in enumerate(steps, start=1):
                step_bodies.append({
                    "position": pos,
                    "action": st.get("action", ""),
                    "expected_result": st.get("expected_result", ""),
                    "data": st.get("data", ""),
                })
            resp = _call("POST", f"/shared_step/{project_code}", token,
                         body={"title": title, "steps": step_bodies})
            if resp:
                result = resp.get("result") or {}
                # API may return {"id": N} or {"hash": "..."} depending on version
                sid = result.get("id") if isinstance(result, dict) else None
                shash = result.get("hash") if isinstance(result, dict) else str(result)
                logger.debug("Shared step create raw result: %s", result)
                state["shared_steps"][title] = {"id": sid, "hash": shash or _step_hash(steps)}
                logger.info("Created shared step '%s' (id=%s, hash=%s).", title, sid, shash)
            else:
                logger.error("Failed to create shared step '%s'.", title)

    return True


# ---------------------------------------------------------------------------
# T016 – Shared parameters creation / reconciliation
# ---------------------------------------------------------------------------
def reconcile_shared_parameters(cfg: dict, state: dict, token: str, dry_run: bool) -> bool:
    params_cfg = cfg.get("shared_parameters", [])
    project_code = state.get("project_code", "")
    logger.info("=== Shared Parameters (%d) ===", len(params_cfg))
    state.setdefault("shared_parameters", {})

    if dry_run:
        for p in params_cfg:
            logger.info("[DRY-RUN] Would create/reuse shared parameter '%s'.", p["name"])
        return True

    # Shared parameters are workspace-level: GET/POST /shared_parameter (no project code).
    # IDs are UUIDs. Filter by project_codes for scoping.
    existing = _paginate("/shared_parameter", token,
                         params={"filters[project_codes][]": project_code})
    existing_by_name = {p["title"]: p for p in existing}

    for param_def in params_cfg:
        name = param_def["name"]
        value = param_def.get("value", "")

        if name in existing_by_name:
            ex = existing_by_name[name]
            pid = ex["id"]
            state["shared_parameters"][name] = pid
            logger.info("Reused shared parameter '%s' (id=%s).", name, pid)
        else:
            resp = _call("POST", "/shared_parameter", token,
                         body={
                             "title": name,
                             "type": "single",
                             "project_codes": [project_code],
                             "is_enabled_for_all_projects": False,
                             "parameters": [{"title": name, "values": [value]}],
                         })
            if resp:
                result = resp.get("result") or {}
                pid = result.get("id") if isinstance(result, dict) else str(result)
                state["shared_parameters"][name] = pid
                logger.info("Created shared parameter '%s' (id=%s).", name, pid)
            else:
                logger.error("Failed to create shared parameter '%s'.", name)

    return True


# ---------------------------------------------------------------------------
# T017 – Post-execution validation
# ---------------------------------------------------------------------------
def validate_post_execution(cfg: dict, state: dict, token: str, dry_run: bool) -> bool:
    if dry_run:
        logger.info("[DRY-RUN] Skipping post-execution validation.")
        return True

    project_code = state.get("project_code", "")
    ok = True

    def check(label: str, actual: int, expected: int) -> None:
        nonlocal ok
        if actual < expected:
            logger.warning("POST-VALIDATION: %s – expected ≥%d, found %d.", label, expected, actual)
            ok = False
        else:
            logger.info("POST-VALIDATION: %s – OK (%d).", label, actual)

    # Custom fields
    cf_resp = _paginate("/custom_field", token)
    cf_names = {f["title"] for f in cf_resp}
    expected_cf = [f["name"] for f in cfg.get("custom_fields", [])]
    found_cf = sum(1 for n in expected_cf if n in cf_names)
    check("custom_fields", found_cf, len(expected_cf))

    # Environments
    env_resp = _paginate(f"/environment/{project_code}", token)
    env_titles = {e["title"] for e in env_resp}
    expected_envs = [e["title"] for e in cfg.get("environments", [])]
    found_envs = sum(1 for t in expected_envs if t in env_titles)
    check("environments", found_envs, len(expected_envs))

    # Milestones
    ms_resp = _paginate(f"/milestone/{project_code}", token)
    ms_titles = {m["title"] for m in ms_resp}
    expected_ms = [m["title"] for m in cfg.get("milestones", [])]
    found_ms = sum(1 for t in expected_ms if t in ms_titles)
    check("milestones", found_ms, len(expected_ms))

    # Shared steps
    ss_resp = _paginate(f"/shared_step/{project_code}", token)
    ss_titles = {s["title"] for s in ss_resp}
    expected_ss = [s["title"] for s in cfg.get("shared_steps", [])]
    found_ss = sum(1 for t in expected_ss if t in ss_titles)
    check("shared_steps", found_ss, len(expected_ss))

    # Shared parameters (workspace-level, filter by project code)
    sp_resp = _paginate("/shared_parameter", token,
                        params={"filters[project_codes][]": project_code})
    sp_titles = {p["title"] for p in sp_resp}
    expected_sp = [p["name"] for p in cfg.get("shared_parameters", [])]
    found_sp = sum(1 for t in expected_sp if t in sp_titles)
    check("shared_parameters", found_sp, len(expected_sp))

    if ok:
        logger.info("Post-execution validation passed.")
    else:
        logger.warning("Post-execution validation found discrepancies (see above).")

    return ok


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------
def main() -> int:
    # T001
    args = parse_args()
    dry_run: bool = args.dry_run
    logger.info("=== Qase Workspace Init (dry_run=%s) ===", dry_run)

    # T002
    token = os.environ.get("QASE_API_TOKEN", "").strip()

    # T009
    cfg = load_config(CONFIG_PATH)
    if not validate_config(cfg):
        return 1

    # T005
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    state = load_state(STATE_PATH)

    # T008
    if not validate_pre_execution(token, dry_run):
        return 1

    # T010
    if not reconcile_project(cfg, state, token, dry_run):
        return 1

    # T011
    reconcile_custom_fields(cfg, state, token, dry_run)

    # T012
    reconcile_environments(cfg, state, token, dry_run)

    # T013
    reconcile_milestones(cfg, state, token, dry_run)

    # T014
    reconcile_configurations(cfg, state, token, dry_run)

    # T015
    reconcile_shared_steps(cfg, state, token, dry_run)

    # T016
    reconcile_shared_parameters(cfg, state, token, dry_run)

    # T017
    validate_post_execution(cfg, state, token, dry_run)

    # T018 – atomic state write
    if not dry_run:
        save_state(STATE_PATH, state)
        logger.info("State saved to %s.", STATE_PATH)
    else:
        logger.info("[DRY-RUN] State NOT written (dry-run mode).")

    logger.info("=== Workspace init complete. ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
