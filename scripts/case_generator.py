"""
Qase test case generator (Step 4 of 7).

Reads the 120 test case rows from the CSV configured in
``config/workspace.yaml`` (``seed.cases_csv``) or overridden via ``--csv``,
translates string enum values to Qase API integers using a runtime-queried
system-field map, resolves custom field option IDs from state, assigns each
case a Jira story via deterministic round-robin (per domain, in CSV row order),
bulk-creates cases in batches of 30 via ``POST /case/{code}/bulk``, writes the
``{csv_id: qase_case_id}`` map to state before the Jira link pass, then links
every case to its assigned Jira story via
``POST /case/{code}/external-issue/attach``.

Credential lookup:
  ``QASE_API_TOKEN`` environment variable (via ``qase_seed_utils.get_qase_token``).

Usage:
  .venv/bin/python scripts/case_generator.py [--csv PATH] [--config PATH] [--dry-run]
  .venv/bin/python scripts/case_generator.py --dry-run
  .venv/bin/python scripts/case_generator.py --csv QD-2026-02-18.csv

Design principles:
  - Idempotent: GET /case preflight checks (title, suite_id) before creating;
    GET /case?include=external_issues preflight before linking.
  - Config-driven: CSV path from ``--csv`` then ``config/workspace.yaml``.
  - Rate-limited: ≤5 req/sec with exponential-backoff retry (max 3, 30 s cap).
  - Atomic state write: temp-file rename via ``qase_seed_utils.save_state``;
    written after creates, before Jira links, so link failures are recoverable.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None  # type: ignore[assignment]

# ---------------------------------------------------------------------------
# Bootstrap: ensure scripts/ is on the path for shared helpers
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent))
from qase_seed_utils import get_qase_token, load_state, save_state  # noqa: E402

# ---------------------------------------------------------------------------
# Constants                                                              T001
# ---------------------------------------------------------------------------

_BASE_URL = "https://api.qase.io/v1"
_RATE_INTERVAL: float = 1.0 / 5   # 200 ms minimum gap → ≤5 req/sec
_MAX_RETRIES: int = 3
_RETRY_STATUS_CODES: frozenset = frozenset({429, 500, 502, 503, 504})
_REPO_ROOT = Path(__file__).resolve().parents[1]

# is_flaky uses a fixed map (not from GET /system_field)
IS_FLAKY_MAP: Dict[str, int] = {"no": 0, "yes": 1}

# Maps Qase API system field title (lowercased) → the short key used in _build_case_payload().
# "automation status (deprecated)" is the 3-value field; the non-deprecated one only has 2 values
# (Manual / Automated) and lacks "To be automated", so we prefer the deprecated variant.
# Keys prefixed with "_" are silently skipped.
_SYSTEM_FIELD_KEYS: Dict[str, str] = {
    "automation status (deprecated)": "automation",
    "automation status":              "_automation_current_skip",
}

# Numbered-prefix regex for step lines: strips "1. ", "2. ", etc.
_STEP_PREFIX_RE = re.compile(r"^\d+\.\s*")

# Module-level rate-limit timestamp; reset in tests via _reset_rate().
_last_req_ts: float = 0.0


def _reset_rate() -> None:
    """Allow tests to reset the rate-limiter between runs."""
    global _last_req_ts
    _last_req_ts = 0.0


# ---------------------------------------------------------------------------
# HTTP helper                                                            T002
# ---------------------------------------------------------------------------

class _QaseAPIError(Exception):
    """Carries the HTTP status code and raw body from a Qase API error."""

    def __init__(self, status: int, url: str, body: str) -> None:
        super().__init__(f"Qase API error {status} for {url}")
        self.status = status
        self.url = url
        self.body = body


def _qase_request(
    method: str,
    path: str,
    token: str,
    body: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Issue a rate-limited, retry-safe request to the Qase API v1.

    - Rate limit : ≤5 req/sec (200 ms minimum gap).
    - Retry      : up to ``_MAX_RETRIES`` times on 429/5xx with exponential
                   backoff (1 s, 2 s, 4 s).
    - Timeout    : 30 seconds per attempt.
    - Non-retryable: 400, 401, 403, 404, 422 — raised immediately.
    """
    global _last_req_ts
    url = _BASE_URL + path
    data: Optional[bytes] = None
    headers: Dict[str, str] = {"Token": token}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    for attempt in range(1, _MAX_RETRIES + 2):
        # --- rate limiting ---
        gap = _RATE_INTERVAL - (time.monotonic() - _last_req_ts)
        if gap > 0:
            time.sleep(gap)
        req = urllib.request.Request(url=url, method=method, data=data, headers=headers)
        _last_req_ts = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw) if raw.strip() else {}
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            if exc.code in _RETRY_STATUS_CODES and attempt <= _MAX_RETRIES:
                backoff = 2 ** (attempt - 1)  # 1 s, 2 s, 4 s
                print(
                    f"[WARN] Qase HTTP {exc.code} on {method} {url} — "
                    f"retry {attempt}/{_MAX_RETRIES} in {backoff}s",
                    file=sys.stderr,
                )
                time.sleep(backoff)
                continue
            raise _QaseAPIError(exc.code, url, detail) from exc
        except urllib.error.URLError as exc:
            if attempt <= _MAX_RETRIES:
                backoff = 2 ** (attempt - 1)
                print(
                    f"[WARN] Network error on {method} {url}: {exc.reason} — "
                    f"retry {attempt}/{_MAX_RETRIES} in {backoff}s",
                    file=sys.stderr,
                )
                time.sleep(backoff)
                continue
            raise

    raise _QaseAPIError(-1, url, f"Max retries ({_MAX_RETRIES}) exceeded")


# ---------------------------------------------------------------------------
# Config loading                                                         T003
# ---------------------------------------------------------------------------

def _load_config(config_path: Path) -> Dict[str, Any]:
    """
    Load ``config/workspace.yaml``.
    Returns an empty dict if the file does not exist.
    Exits if PyYAML is unavailable.
    """
    if yaml is None:
        sys.exit("Error: PyYAML is not installed. Run: .venv/bin/pip install PyYAML")
    if not config_path.exists():
        return {}
    with config_path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _resolve_csv_path(cli_arg: Optional[str], config: Dict[str, Any]) -> Path:
    """
    Resolve the CSV file path.

    Priority:
      1. ``--csv`` CLI argument
      2. ``config/workspace.yaml`` ``seed.cases_csv``

    Exits with an actionable error if neither source is available.
    """
    if cli_arg:
        p = Path(cli_arg)
        return p if p.is_absolute() else _REPO_ROOT / cli_arg
    seed_csv: Optional[str] = (config.get("seed") or {}).get("cases_csv")
    if seed_csv:
        p = Path(seed_csv)
        return p if p.is_absolute() else _REPO_ROOT / seed_csv
    sys.exit(
        "Error: CSV path not configured. "
        "Provide --csv <path> or set seed.cases_csv in config/workspace.yaml."
    )


# ---------------------------------------------------------------------------
# CSV parsing                                                            T004
# ---------------------------------------------------------------------------

def _parse_case_rows(csv_path: Path) -> List[Dict[str, str]]:
    """
    Return rows where ``suite_without_cases != '1'`` (the 120 test case rows).
    Exits if the file is missing or yields zero case rows.
    """
    if not csv_path.exists():
        sys.exit(f"Error: CSV file not found: {csv_path}")
    rows: List[Dict[str, str]] = []
    with csv_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row.get("suite_without_cases", "").strip() != "1":
                rows.append(row)
    if not rows:
        sys.exit(
            f"Error: No case rows found in {csv_path} "
            "(all rows have suite_without_cases == '1')."
        )
    return rows


def _parse_suite_rows_for_lookup(csv_path: Path) -> List[Dict[str, str]]:
    """
    Return rows where ``suite_without_cases == '1'`` (the 31 suite-definition rows).
    Used to build the leaf-to-root map; does not exit if empty.
    """
    if not csv_path.exists():
        sys.exit(f"Error: CSV file not found: {csv_path}")
    rows: List[Dict[str, str]] = []
    with csv_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row.get("suite_without_cases", "").strip() == "1":
                rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Step parsing                                                           T005
# ---------------------------------------------------------------------------

def _parse_steps(row: Dict[str, str]) -> List[Dict[str, Any]]:
    """
    Parse multi-line step columns into a list of step objects.

    - Splits ``steps_actions``, ``steps_result``, ``steps_data`` on ``\\n``.
    - Strips numbered prefix (e.g. ``"1. "``) from each line.
    - Zips all three lists by position.
    - Drops leading/trailing entries where the action line is empty after strip.
    - Returns ``[{"action": str, "expected_result": str, "data": str, "position": int}]``
      with 1-based ``position``.
    """
    def split_strip(col: str) -> List[str]:
        raw = row.get(col) or ""
        return [_STEP_PREFIX_RE.sub("", line) for line in raw.split("\n")]

    actions = split_strip("steps_actions")
    results = split_strip("steps_result")
    data    = split_strip("steps_data")

    # Pad shorter lists to equal length
    length = max(len(actions), len(results), len(data))
    actions += [""] * (length - len(actions))
    results += [""] * (length - len(results))
    data    += [""] * (length - len(data))

    # Drop leading empty action lines
    triples: List[Tuple[str, str, str]] = list(zip(actions, results, data))
    while triples and not triples[0][0].strip():
        triples.pop(0)
    # Drop trailing empty action lines
    while triples and not triples[-1][0].strip():
        triples.pop()

    return [
        {
            "action":          a,
            "expected_result": r,
            "data":            d,
            "position":        i + 1,
        }
        for i, (a, r, d) in enumerate(triples)
    ]


# ---------------------------------------------------------------------------
# Leaf-to-root map                                                       T006
# ---------------------------------------------------------------------------

def _build_leaf_to_root_map(suite_rows: List[Dict[str, str]]) -> Dict[str, str]:
    """
    Build ``{csv_suite_id: root_suite_title}`` from the suite-definition rows.

    ShopEase uses at most 2 levels:
      - Root rows (no ``suite_parent_id``): root title = own ``suite`` column.
      - Child rows: root title = parent row's ``suite`` column.

    Returns a complete map for all 30 suite IDs.
    """
    id_to_row: Dict[str, Dict[str, str]] = {
        r["suite_id"].strip(): r for r in suite_rows if r.get("suite_id", "").strip()
    }
    result: Dict[str, str] = {}
    for row in suite_rows:
        csv_sid   = row.get("suite_id", "").strip()
        parent_id = row.get("suite_parent_id", "").strip()
        if not csv_sid:
            continue
        if not parent_id:
            result[csv_sid] = row.get("suite", "").strip()
        else:
            parent_row = id_to_row.get(parent_id)
            if parent_row:
                result[csv_sid] = parent_row.get("suite", "").strip()
            else:
                result[csv_sid] = row.get("suite", "").strip()
    return result


# ---------------------------------------------------------------------------
# Preflight validation                                                   T010
# ---------------------------------------------------------------------------

def _validate_preflight(
    case_rows: List[Dict[str, str]],
    suite_id_map: Dict[str, int],
    state_custom_fields: Dict[str, Any],
    cf_column_map: Dict[str, str],
    jira_state: Dict[str, Any],
    suite_domain_map: Dict[str, str],
) -> None:
    """
    Run all preflight checks before any API call:

    (a) All ``suite_id`` values in case rows exist in ``suite_id_map``.
    (b) All CF names in ``cf_column_map`` exist in state with an ``options`` sub-key.
    (c) All domain slugs in ``suite_domain_map`` values have matching stories in jira_state.

    Exits with a consolidated error if any check fails.
    """
    errors: List[str] = []

    # (a) Suite IDs
    for row in case_rows:
        csv_sid = row.get("suite_id", "").strip()
        if csv_sid not in suite_id_map:
            errors.append(
                f"  suite_id={csv_sid!r} (case id={row.get('id', '?')!r}) "
                "not found in state/workspace_state.json suite_ids"
            )

    # (b) Custom field options
    for col, cf_name in cf_column_map.items():
        if cf_name not in state_custom_fields:
            errors.append(
                f"  custom_fields['{cf_name}'] not found in state "
                "(expected to be written by workspace_init.py)"
            )
        elif "options" not in state_custom_fields[cf_name]:
            errors.append(
                f"  custom_fields['{cf_name}'].options missing from state "
                "(workspace_init.py must persist option IDs — see plan.md D-01)"
            )

    # (c) Domain slugs → jira stories
    all_stories = jira_state.get("stories", {})
    seen_slugs: Set[str] = set()
    for slug in suite_domain_map.values():
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        matching = [s for s in all_stories.values() if s.get("epic_slug") == slug]
        if not matching:
            errors.append(
                f"  domain slug={slug!r} (from suite_domain_map) has no matching "
                "stories in state/jira_state.json — run jira_requirements.py first"
            )

    if errors:
        sys.exit("Error: Preflight validation failed:\n" + "\n".join(errors))


# ---------------------------------------------------------------------------
# CF maps                                                                T008
# ---------------------------------------------------------------------------

def _build_cf_maps(
    state: Dict[str, Any],
    cf_column_map: Dict[str, str],
) -> Tuple[Dict[str, Any], Dict[str, Dict[str, str]]]:
    """
    Build CF field-ID map and option map from already-loaded workspace state.

    Returns:
      cf_id_map     — ``{cf_name: field_id_int}``
      cf_option_map — ``{cf_name: {option_name: option_id_str}}``

    Exits if any required CF or its options key is absent (should have been
    caught by ``_validate_preflight``, but guard defensively).
    """
    cf_data: Dict[str, Any] = state.get("custom_fields", {})
    cf_id_map: Dict[str, Any] = {}
    cf_option_map: Dict[str, Dict[str, str]] = {}

    for _col, cf_name in cf_column_map.items():
        entry = cf_data.get(cf_name)
        if not entry:
            sys.exit(
                f"Error: custom_fields['{cf_name}'] not found in state. "
                "Run workspace_init.py first."
            )
        if "options" not in entry:
            sys.exit(
                f"Error: custom_fields['{cf_name}'].options missing from state. "
                "workspace_init.py must persist option IDs (see plan.md D-01)."
            )
        cf_id_map[cf_name]     = entry["id"]
        cf_option_map[cf_name] = entry["options"]

    return cf_id_map, cf_option_map


# ---------------------------------------------------------------------------
# Domain stories map                                                     T009
# ---------------------------------------------------------------------------

def _build_domain_stories_map(
    jira_state: Dict[str, Any],
    suite_domain_map: Dict[str, str],
) -> Tuple[Dict[str, List[str]], Dict[str, List[str]], Dict[str, int]]:
    """
    Build domain → story lists from jira_state (no API call).

    Filters ``jira_state["stories"]`` by ``epic_slug`` for each unique domain
    slug in ``suite_domain_map``, preserving dict insertion order (research.md F-02).

    Returns:
      domain_stories_map     — ``{slug: [jira_id_str, ...]}`` (for link calls)
      domain_stories_key_map — ``{slug: [jira_key_str, ...]}`` (for dry-run display)
      domain_cursors         — ``{slug: 0}`` round-robin cursor initialised to 0
    """
    all_stories: Dict[str, Any] = jira_state.get("stories", {})
    domain_stories_map:     Dict[str, List[str]] = {}
    domain_stories_key_map: Dict[str, List[str]] = {}

    # dict.fromkeys preserves first-seen order of unique slugs
    for slug in dict.fromkeys(suite_domain_map.values()):
        matching = [s for s in all_stories.values() if s.get("epic_slug") == slug]
        if not matching:
            sys.exit(
                f"Error: domain slug={slug!r} has no matching stories in "
                "state/jira_state.json (run jira_requirements.py first)"
            )
        # Qase external-issue/attach API requires the Jira issue key (e.g. "AF-7"),
        # not the numeric internal ID. key_map and id_map are identical.
        domain_stories_map[slug]     = [str(s["jira_key"]) for s in matching]
        domain_stories_key_map[slug] = [str(s["jira_key"]) for s in matching]

    domain_cursors: Dict[str, int] = {slug: 0 for slug in domain_stories_map}
    return domain_stories_map, domain_stories_key_map, domain_cursors


# ---------------------------------------------------------------------------
# Dry-run plan                                                           T021
# ---------------------------------------------------------------------------

def _dry_run_plan(
    case_rows:              List[Dict[str, str]],
    cf_column_map:          Dict[str, str],
    cf_id_map:              Dict[str, Any],
    cf_option_map:          Dict[str, Dict[str, str]],
    suite_id_map:           Dict[str, int],
    leaf_to_root_map:       Dict[str, str],
    suite_domain_map:       Dict[str, str],
    domain_stories_map:     Dict[str, List[str]],
    domain_stories_key_map: Dict[str, List[str]],
    domain_cursors:         Dict[str, int],
) -> None:
    """
    Print the full distribution plan for all 120 cases and exit 0.

    No API calls are made; state/workspace_state.json is not modified.
    System fields are shown as raw CSV string values (no enum API call).
    CF values are resolved to option IDs from already-loaded state.
    """
    cursors        = dict(domain_cursors)   # local copy — do not mutate original
    suites_touched: Set[str] = set()
    jira_keys_used: Set[str] = set()

    for i, row in enumerate(case_rows, 1):
        csv_id  = row.get("id", "").strip()
        title   = row.get("title", "").strip()
        csv_sid = row.get("suite_id", "").strip()

        root_title = leaf_to_root_map.get(csv_sid, "?")
        slug       = suite_domain_map.get(root_title, "?")

        if slug != "?" and slug in domain_stories_key_map:
            keys      = domain_stories_key_map[slug]
            story_key = keys[cursors[slug] % len(keys)]
            cursors[slug] += 1
        else:
            story_key = "?"

        suites_touched.add(csv_sid)
        jira_keys_used.add(story_key)

        # Build CF option-ID display (from state — no API call)
        cf_parts: List[str] = []
        for col, cf_name in cf_column_map.items():
            raw_val = row.get(col, "").strip()
            if not raw_val:
                continue
            options = cf_option_map.get(cf_name, {})
            if cf_name == "Test Data Profile":
                parts   = [v.strip() for v in raw_val.split(",") if v.strip()]
                opt_ids = [str(options.get(p, f"?{p}")) for p in parts]
                cf_parts.append(f"{col}=[{','.join(opt_ids)}]")
            else:
                cf_parts.append(f"{col}={options.get(raw_val, f'?{raw_val}')}")

        cf_str = "  ".join(cf_parts)
        print(
            f"[DRY-RUN] {i:3d}  suite={root_title!r}  csv_id={csv_id}"
            f"  jira={story_key}  title={title[:60]!r}"
        )
        if cf_str:
            print(f"          {cf_str}")

    print()
    print(
        f"[DRY-RUN] Summary: {len(case_rows)} cases planned, "
        f"{len(suites_touched)} suites affected, "
        f"{len(jira_keys_used)} unique Jira stories referenced."
    )
    sys.exit(0)


# ---------------------------------------------------------------------------
# Enum map                                                               T007
# ---------------------------------------------------------------------------

def _build_enum_map(token: str) -> Dict[str, Dict[str, int]]:
    """
    Build runtime enum map from ``GET /system_field``.

    Returns ``{field_name_lower: {option_title_lower: option_id_int}}``.
    Exits on 401/403.
    """
    try:
        resp = _qase_request("GET", "/system_field", token)
    except _QaseAPIError as exc:
        if exc.status in (401, 403):
            sys.exit(f"Error: Check QASE_API_TOKEN permissions (HTTP {exc.status}).")
        raise

    enum_map: Dict[str, Dict[str, int]] = {}
    for field in resp.get("result", []):
        raw_name   = field.get("title", "").lower()
        mapped_key = _SYSTEM_FIELD_KEYS.get(raw_name, raw_name)
        if mapped_key.startswith("_"):   # silently skip unwanted variants
            continue
        enum_map[mapped_key] = {
            opt["title"].lower(): int(opt["id"])
            for opt in field.get("options", [])
            if "title" in opt and "id" in opt
        }

    # Add CSV-style aliases for the automation field so that the hyphenated CSV values
    # ("is-not-automated", "to-be-automated") round-trip cleanly to the API IDs.
    if "automation" in enum_map:
        am = enum_map["automation"]
        am.setdefault("is-not-automated", am.get("manual", 0))
        am.setdefault("to-be-automated",  am.get("to be automated", 1))

    return enum_map


# ---------------------------------------------------------------------------
# Fetch existing cases (create idempotency preflight)                   T012
# ---------------------------------------------------------------------------

def _fetch_existing_cases(
    project_code: str,
    token: str,
) -> Dict[Tuple[str, int], int]:
    """
    Paginate ``GET /case/{code}`` and return ``{(title, suite_id): qase_case_id}``.
    Used to detect cases that already exist before the create pass.
    """
    existing: Dict[Tuple[str, int], int] = {}
    offset = 0
    limit  = 100
    total: Optional[int] = None

    while True:
        path = (
            f"/case/{urllib.parse.quote(project_code)}"
            f"?limit={limit}&offset={offset}"
        )
        try:
            resp = _qase_request("GET", path, token)
        except _QaseAPIError as exc:
            if exc.status == 401:
                sys.exit("Error: Check QASE_API_TOKEN permissions (HTTP 401).")
            if exc.status == 403:
                sys.exit("Error: Check QASE_API_TOKEN permissions (HTTP 403).")
            if exc.status == 404:
                sys.exit(
                    f"Error: project_code {project_code!r} not found in Qase (HTTP 404). "
                    "Verify state/workspace_state.json was written by workspace_init.py."
                )
            raise

        result   = resp.get("result", {})
        entities: List[Dict[str, Any]] = result.get("entities", [])
        if total is None:
            total = result.get("total", 0)

        for entity in entities:
            title    = entity.get("title", "").strip()
            suite_id = entity.get("suite_id")
            qase_id  = entity.get("id")
            if title and suite_id is not None and qase_id is not None:
                existing[(title, int(suite_id))] = int(qase_id)

        offset += len(entities)
        if not entities or offset >= (total or 0):
            break

    return existing


# ---------------------------------------------------------------------------
# Case payload builder                                                   T011
# ---------------------------------------------------------------------------

def _build_case_payload(
    row:           Dict[str, str],
    enum_map:      Dict[str, Dict[str, int]],
    cf_id_map:     Dict[str, Any],
    cf_option_map: Dict[str, Dict[str, str]],
    suite_id_map:  Dict[str, int],
    cf_column_map: Dict[str, str],
) -> Dict[str, Any]:
    """
    Convert a single CSV case row into a Qase bulk-create payload dict.

    Exits with a descriptive error if any enum or CF option value is not found
    in the runtime maps (FR-006 + spec edge cases).
    """
    csv_id  = row.get("id", "?").strip()
    csv_sid = row.get("suite_id", "").strip()
    qase_sid = suite_id_map[csv_sid]   # validated in preflight

    def _translate(field_name: str, raw: str) -> int:
        val = raw.strip().lower()
        field_map = enum_map.get(field_name, {})
        if val not in field_map:
            sys.exit(
                f"ERROR row {csv_id}: unrecognised {field_name} value '{raw.strip()}'"
            )
        return field_map[val]

    # is_flaky
    is_flaky_raw = (row.get("is_flaky") or "no").strip().lower()
    if is_flaky_raw not in IS_FLAKY_MAP:
        sys.exit(
            f"ERROR row {csv_id}: unrecognised is_flaky value "
            f"'{row.get('is_flaky', '').strip()}'"
        )

    # Custom fields: str(field_id) → str(option_id) or comma-joined str(option_ids)
    custom_field: Dict[str, str] = {}
    for col, cf_name in cf_column_map.items():
        raw_val = (row.get(col) or "").strip()
        if not raw_val:
            continue
        options  = cf_option_map.get(cf_name, {})
        field_id = cf_id_map.get(cf_name)
        if field_id is None:
            continue
        if cf_name == "Test Data Profile":
            parts = [v.strip() for v in raw_val.split(",") if v.strip()]
            opt_ids: List[str] = []
            for part in parts:
                if part not in options:
                    sys.exit(
                        f"ERROR row {csv_id}: unrecognised {col} ('{cf_name}') "
                        f"option '{part}'"
                    )
                opt_ids.append(str(options[part]))
            custom_field[str(field_id)] = ",".join(opt_ids)
        else:
            if raw_val not in options:
                sys.exit(
                    f"ERROR row {csv_id}: unrecognised {col} ('{cf_name}') "
                    f"option '{raw_val}'"
                )
            custom_field[str(field_id)] = str(options[raw_val])

    payload: Dict[str, Any] = {
        "title":      row.get("title", "").strip(),
        "suite_id":   qase_sid,
        "priority":   _translate("priority",   row.get("priority",   "") or ""),
        "severity":   _translate("severity",   row.get("severity",   "") or ""),
        "behavior":   _translate("behavior",   row.get("behavior",   "") or ""),
        "type":       _translate("type",       row.get("type",       "") or ""),
        "layer":      _translate("layer",      row.get("layer",      "") or ""),
        "automation": _translate("automation", row.get("automation", "") or ""),
        "status":     _translate("status",     row.get("status",     "") or ""),
        "is_flaky":   IS_FLAKY_MAP[is_flaky_raw],
        "steps":      _parse_steps(row),
    }

    # Optional text fields — only include if non-empty
    for field in ("description", "preconditions", "postconditions"):
        val = (row.get(field) or "").strip()
        if val:
            payload[field] = val

    if custom_field:
        payload["custom_field"] = custom_field

    return payload


# ---------------------------------------------------------------------------
# Bulk create batch                                                      T013
# ---------------------------------------------------------------------------

def _bulk_create_batch(
    project_code: str,
    token: str,
    batch: List[Tuple[str, Dict[str, Any]]],
) -> Dict[str, int]:
    """
    POST a single bulk-create batch (≤30 cases) to ``POST /case/{code}/bulk``.

    ``batch`` is an ordered list of ``(csv_id, payload)`` pairs.
    Returns ``{csv_id: qase_case_id}`` by zipping ``result.ids`` with csv_ids
    in order (D-05 — response order matches input order).
    """
    csv_ids  = [item[0] for item in batch]
    payloads = [item[1] for item in batch]

    try:
        resp = _qase_request(
            "POST",
            f"/case/{urllib.parse.quote(project_code)}/bulk",
            token,
            body={"cases": payloads},
        )
    except _QaseAPIError as exc:
        if exc.status in (400, 422):
            sys.exit(
                f"ERROR batch (csv_ids {csv_ids[0]}–{csv_ids[-1]}): "
                f"HTTP {exc.status} — {exc.body}"
            )
        if exc.status in (401, 403):
            sys.exit("Error: Check QASE_API_TOKEN permissions.")
        if exc.status == 404:
            sys.exit(
                f"Error: project_code {project_code!r} not found in Qase (HTTP 404)."
            )
        raise

    ids: List[int] = resp.get("result", {}).get("ids", [])
    if len(ids) != len(csv_ids):
        sys.exit(
            f"ERROR batch (csv_ids {csv_ids[0]}–{csv_ids[-1]}): "
            f"expected {len(csv_ids)} IDs back, got {len(ids)}"
        )
    return {csv_id: int(qase_id) for csv_id, qase_id in zip(csv_ids, ids)}


# ---------------------------------------------------------------------------
# Create pass orchestrator                                               T014
# ---------------------------------------------------------------------------

def _run_create_pass(
    case_rows:          List[Dict[str, str]],
    existing_case_map:  Dict[Tuple[str, int], int],
    suite_id_map:       Dict[str, int],
    enum_map:           Dict[str, Dict[str, int]],
    cf_id_map:          Dict[str, Any],
    cf_option_map:      Dict[str, Dict[str, str]],
    cf_column_map:      Dict[str, str],
    leaf_to_root_map:   Dict[str, str],
    suite_domain_map:   Dict[str, str],
    domain_stories_map: Dict[str, List[str]],
    domain_cursors:     Dict[str, int],
    project_code:       str,
    token:              str,
) -> Tuple[Dict[str, int], Dict[str, str], int, int]:
    """
    Two-pass create orchestrator:

    Pass A — iterate all 120 rows in CSV order:
      - Assign Jira story via round-robin (mutates ``domain_cursors`` in place).
      - Check ``existing_case_map``; on hit, log REUSE and add to case_id_map.
      - On miss, build payload and queue for batch creation.

    Pass B — bulk-create all queued new cases in batches of ≤30.

    Returns ``(case_id_map, jira_assignment_map, created_count, reused_count)``.
    """
    case_id_map:        Dict[str, int] = {}
    jira_assignment_map: Dict[str, str] = {}
    new_cases: List[Tuple[str, Dict[str, Any]]] = []
    reused_total = 0

    # Pass A: scan rows, assign stories, separate reused vs new
    for row in case_rows:
        csv_id  = row.get("id", "").strip()
        title   = row.get("title", "").strip()
        csv_sid = row.get("suite_id", "").strip()
        qase_sid = suite_id_map[csv_sid]

        # Round-robin story assignment (must advance for ALL rows in CSV order)
        root_title = leaf_to_root_map.get(csv_sid, "")
        slug       = suite_domain_map.get(root_title, "")
        stories    = domain_stories_map.get(slug, [])
        if stories:
            jira_id = stories[domain_cursors[slug] % len(stories)]
            domain_cursors[slug] += 1
        else:
            jira_id = ""
        jira_assignment_map[csv_id] = jira_id

        if (title, qase_sid) in existing_case_map:
            case_id_map[csv_id] = existing_case_map[(title, qase_sid)]
            reused_total += 1
            print(
                f"REUSE case {csv_id}: '{title}' → qase_id={case_id_map[csv_id]}"
            )
        else:
            payload = _build_case_payload(
                row, enum_map, cf_id_map, cf_option_map, suite_id_map, cf_column_map
            )
            new_cases.append((csv_id, payload))

    # Pass B: batch-create new cases (batches of ≤30)
    total_batches = math.ceil(len(new_cases) / 30) if new_cases else 0
    created_total = 0

    for batch_num, start in enumerate(range(0, len(new_cases), 30), 1):
        batch = new_cases[start:start + 30]
        result_map = _bulk_create_batch(project_code, token, batch)
        for csv_id, qase_id in result_map.items():
            case_id_map[csv_id] = qase_id
        created_total += len(result_map)
        print(f"Batch {batch_num}/{total_batches}: {len(result_map)} created")

    return case_id_map, jira_assignment_map, created_total, reused_total


# ---------------------------------------------------------------------------
# State write                                                            T015
# ---------------------------------------------------------------------------

def _write_case_ids_to_state(
    state: Dict[str, Any],
    case_id_map: Dict[str, int],
) -> None:
    """
    Merge ``case_ids`` into the in-memory state dict, then atomically write to
    ``state/workspace_state.json`` via ``save_state()`` (temp-file + rename).

    Uses the already-loaded in-memory state (no redundant disk re-read).
    All pre-existing keys (project_code, suite_ids, custom_fields, etc.) are
    preserved intact.
    """
    state["case_ids"] = case_id_map
    save_state("workspace_state", state)


# ---------------------------------------------------------------------------
# Fetch linked cases (link idempotency preflight)                       T017
# ---------------------------------------------------------------------------

def _fetch_linked_cases(
    project_code: str,
    token: str,
) -> Set[int]:
    """
    Paginate ``GET /case/{code}?include=external_issues`` and return the set
    of Qase case IDs that already have at least one external issue linked (D-04).
    """
    linked: Set[int] = set()
    offset = 0
    limit  = 100
    total: Optional[int] = None

    while True:
        path = (
            f"/case/{urllib.parse.quote(project_code)}"
            f"?limit={limit}&offset={offset}&include=external_issues"
        )
        try:
            resp = _qase_request("GET", path, token)
        except _QaseAPIError as exc:
            if exc.status == 401:
                sys.exit("Error: Check QASE_API_TOKEN permissions (HTTP 401).")
            if exc.status == 403:
                sys.exit("Error: Check QASE_API_TOKEN permissions (HTTP 403).")
            if exc.status == 404:
                sys.exit(
                    f"Error: project_code {project_code!r} not found in Qase (HTTP 404)."
                )
            raise

        result   = resp.get("result", {})
        entities: List[Dict[str, Any]] = result.get("entities", [])
        if total is None:
            total = result.get("total", 0)

        for entity in entities:
            qase_id         = entity.get("id")
            external_issues = entity.get("external_issues") or []
            if qase_id is not None and external_issues:
                linked.add(int(qase_id))

        offset += len(entities)
        if not entities or offset >= (total or 0):
            break

    return linked


# ---------------------------------------------------------------------------
# Attach links batch                                                     T018
# ---------------------------------------------------------------------------

def _attach_links_batch(
    project_code: str,
    token: str,
    link_pairs: List[Tuple[int, str]],
) -> None:
    """
    POST a single link batch (≤30 pairs) to
    ``POST /case/{code}/external-issue/attach`` (D-03, D-09).

    ``link_pairs`` is a list of ``(qase_case_id_int, jira_id_str)`` pairs.
    """
    links = [
        {"case_id": qase_id, "external_issues": [jira_id]}
        for qase_id, jira_id in link_pairs
    ]
    try:
        _qase_request(
            "POST",
            f"/case/{urllib.parse.quote(project_code)}/external-issue/attach",
            token,
            body={"type": "jira-cloud", "links": links},
        )
    except _QaseAPIError as exc:
        case_ids_str = ", ".join(str(q) for q, _ in link_pairs[:5])
        if exc.status in (400, 422):
            sys.exit(
                f"ERROR link batch (qase_case_ids: {case_ids_str}...): "
                f"HTTP {exc.status} — {exc.body}"
            )
        if exc.status in (401, 403):
            sys.exit("Error: Check QASE_API_TOKEN permissions.")
        if exc.status == 404:
            sys.exit(
                f"Error: project_code {project_code!r} or case_id not found "
                f"in Qase (HTTP 404)."
            )
        raise


# ---------------------------------------------------------------------------
# Link pass orchestrator                                                 T019
# ---------------------------------------------------------------------------

def _run_link_pass(
    case_id_map:         Dict[str, int],
    jira_assignment_map: Dict[str, str],
    project_code:        str,
    token:               str,
) -> Tuple[int, int]:
    """
    Idempotent Jira link pass:

    1. GET existing links via ``_fetch_linked_cases()`` → ``linked_case_ids``.
    2. Iterate all case_id_map entries in groups of 30 (matching create batch size).
       Per group: skip cases already in ``linked_case_ids``, link the rest.
    3. Log ``"Links batch K/T: N linked, M skipped"`` per group.

    Returns ``(linked_count, skipped_count)``.
    """
    linked_case_ids = _fetch_linked_cases(project_code, token)

    all_items = list(case_id_map.items())   # [(csv_id, qase_case_id), ...]
    total_batches = math.ceil(len(all_items) / 30) if all_items else 0
    linked_total  = 0
    skipped_total = 0

    for batch_num, start in enumerate(range(0, len(all_items), 30), 1):
        group = all_items[start:start + 30]
        to_link:     List[Tuple[int, str]] = []
        batch_skipped = 0

        for csv_id, qase_case_id in group:
            if qase_case_id in linked_case_ids:
                batch_skipped += 1
            else:
                jira_id = jira_assignment_map.get(csv_id, "")
                if jira_id:
                    to_link.append((qase_case_id, jira_id))

        if to_link:
            _attach_links_batch(project_code, token, to_link)

        linked_total  += len(to_link)
        skipped_total += batch_skipped
        print(
            f"Links batch {batch_num}/{total_batches}: "
            f"{len(to_link)} linked, {batch_skipped} skipped"
        )

    return linked_total, skipped_total


# ---------------------------------------------------------------------------
# Main orchestrator                                                      T016 + T020 + T022 + T024
# ---------------------------------------------------------------------------

def _run(args: argparse.Namespace) -> None:
    # ------------------------------------------------------------------ #
    # Phase 0a: Config + CSV path resolution                               #
    # ------------------------------------------------------------------ #
    config_path = _REPO_ROOT / (getattr(args, "config", None) or "config/workspace.yaml")
    config      = _load_config(config_path)
    csv_path    = _resolve_csv_path(getattr(args, "csv", None), config)

    # ------------------------------------------------------------------ #
    # Phase 0b: State loading                                              #
    # ------------------------------------------------------------------ #
    state      = load_state("workspace_state")
    jira_state = load_state("jira_state")

    project_code: Optional[str] = state.get("project_code")
    if not project_code:
        sys.exit(
            "Error: project_code not found in state/workspace_state.json. "
            "Run workspace_init.py first."
        )

    # ------------------------------------------------------------------ #
    # Phase 0c: CSV parsing                                                #
    # ------------------------------------------------------------------ #
    case_rows   = _parse_case_rows(csv_path)
    suite_rows  = _parse_suite_rows_for_lookup(csv_path)

    # ------------------------------------------------------------------ #
    # Phase 0d: Build helper maps (all no-API, from CSV + state + config)  #
    # ------------------------------------------------------------------ #
    cf_column_map:  Dict[str, str] = dict(config.get("cf_column_map")   or {})
    suite_domain_map: Dict[str, str] = dict(config.get("suite_domain_map") or {})
    suite_id_map: Dict[str, int] = {
        str(k): int(v)
        for k, v in (state.get("suite_ids") or {}).items()
    }
    leaf_to_root_map = _build_leaf_to_root_map(suite_rows)

    # ------------------------------------------------------------------ #
    # Phase 0e: Preflight validation                                       #
    # ------------------------------------------------------------------ #
    _validate_preflight(
        case_rows,
        suite_id_map,
        state.get("custom_fields") or {},
        cf_column_map,
        jira_state,
        suite_domain_map,
    )

    # ------------------------------------------------------------------ #
    # Phase 1: Build CF and domain story maps (no API calls)               #
    # ------------------------------------------------------------------ #
    cf_id_map, cf_option_map = _build_cf_maps(state, cf_column_map)
    domain_stories_map, domain_stories_key_map, domain_cursors = (
        _build_domain_stories_map(jira_state, suite_domain_map)
    )

    # ------------------------------------------------------------------ #
    # Dry-run gate — exits here; zero API calls made (FR-017, T022)        #
    # ------------------------------------------------------------------ #
    if getattr(args, "dry_run", False):
        _dry_run_plan(
            case_rows,
            cf_column_map,
            cf_id_map,
            cf_option_map,
            suite_id_map,
            leaf_to_root_map,
            suite_domain_map,
            domain_stories_map,
            domain_stories_key_map,
            domain_cursors,
        )
        return   # unreachable — _dry_run_plan calls sys.exit(0)

    # ------------------------------------------------------------------ #
    # Phase 1b: Build enum map (first API call)                            #
    # ------------------------------------------------------------------ #
    token = get_qase_token()
    enum_map = _build_enum_map(token)

    # ------------------------------------------------------------------ #
    # Phase 3: Create idempotency preflight                                #
    # ------------------------------------------------------------------ #
    print(f"[GET]  Fetching existing cases for idempotency check (project: {project_code})...")
    existing_case_map = _fetch_existing_cases(project_code, token)
    print(f"[GET]  Found {len(existing_case_map)} existing case(s).")

    # ------------------------------------------------------------------ #
    # Phase 4: Bulk create pass                                            #
    # ------------------------------------------------------------------ #
    case_id_map, jira_assignment_map, created_count, reused_count = _run_create_pass(
        case_rows,
        existing_case_map,
        suite_id_map,
        enum_map,
        cf_id_map,
        cf_option_map,
        cf_column_map,
        leaf_to_root_map,
        suite_domain_map,
        domain_stories_map,
        domain_cursors,
        project_code,
        token,
    )
    total_cases = created_count + reused_count
    print(f"Cases complete: {created_count} created, {reused_count} reused (total {total_cases})")

    # ------------------------------------------------------------------ #
    # Phase 5: Atomic state write (before Jira links — FR-014)             #
    # ------------------------------------------------------------------ #
    _write_case_ids_to_state(state, case_id_map)

    # ------------------------------------------------------------------ #
    # Phase 6: Jira link pass                                              #
    # ------------------------------------------------------------------ #
    linked_count, skipped_count = _run_link_pass(
        case_id_map,
        jira_assignment_map,
        project_code,
        token,
    )
    link_total = linked_count + skipped_count
    print(f"Links complete: {linked_count} linked, {skipped_count} skipped (total {link_total})")


# ---------------------------------------------------------------------------
# Entry point                                                            T023
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bulk-create 120 Qase test cases from CSV and link each to its Jira story.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  .venv/bin/python scripts/case_generator.py\n"
            "  .venv/bin/python scripts/case_generator.py --dry-run\n"
            "  .venv/bin/python scripts/case_generator.py --csv QD-2026-02-18.csv\n"
        ),
    )
    parser.add_argument(
        "--csv",
        metavar="PATH",
        default=None,
        help=(
            "Path to the CSV file. "
            "Overrides config/workspace.yaml seed.cases_csv."
        ),
    )
    parser.add_argument(
        "--config",
        metavar="PATH",
        default=None,
        help="Path to workspace config YAML (default: config/workspace.yaml).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Print the full distribution plan (suite, title, CF values, Jira story) "
            "for all 120 cases without making any API calls or modifying state."
        ),
    )
    args = parser.parse_args()
    _run(args)


if __name__ == "__main__":
    main()
