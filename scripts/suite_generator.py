"""
Qase suite hierarchy generator (Step 3 of 7).

Reads suite-definition rows from the CSV configured in
``config/workspace.yaml`` (``seed.cases_csv``) or overridden via ``--csv``,
creates the full 7-parent / 23-child suite hierarchy in the Qase project using
a two-pass topological approach, and persists the ``csv_suite_id →
qase_suite_id`` mapping into ``state/workspace_state.json``.

Credential lookup:
  ``QASE_API_TOKEN`` environment variable (via ``qase_seed_utils.get_qase_token``).

Usage:
  python scripts/suite_generator.py [--csv PATH] [--config PATH] [--dry-run]

Design principles:
  - Idempotent: pre-fetches existing suites at start; reuses by title; never
    creates duplicates.
  - Config-driven: CSV path resolved from ``--csv`` then
    ``config/workspace.yaml seed.cases_csv``.
  - Rate-limited: ≤5 req/sec with exponential-backoff retry (max 3, 30 s cap).
  - Atomic state write: temp-file rename via ``qase_seed_utils.save_state``;
    ``state/workspace_state.json`` is never modified if any API call fails.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

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
# Constants
# ---------------------------------------------------------------------------

_BASE_URL = "https://api.qase.io/v1"
_RATE_INTERVAL: float = 1.0 / 5   # 200 ms minimum gap → ≤5 req/sec
_MAX_RETRIES: int = 3
_RETRY_STATUS_CODES: frozenset = frozenset({429, 500, 502, 503, 504})
_REPO_ROOT = Path(__file__).resolve().parents[1]

# Module-level rate-limit timestamp; reset in tests via _reset_rate().
_last_req_ts: float = 0.0


def _reset_rate() -> None:
    """Allow tests to reset the rate-limiter between runs."""
    global _last_req_ts
    _last_req_ts = 0.0


# ---------------------------------------------------------------------------
# HTTP helper — T003
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
    - Non-retryable: 400, 401, 403, 404 — raised immediately.
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
# Config loading — T004
# ---------------------------------------------------------------------------

def _load_config(config_path: Path) -> Dict[str, Any]:
    """
    Load ``config/workspace.yaml``.
    Returns an empty dict if the file does not exist.
    Exits if PyYAML is unavailable.
    """
    if yaml is None:
        sys.exit("Error: PyYAML is not installed. Run: pip install PyYAML")
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
# CSV parsing — T005
# ---------------------------------------------------------------------------

def _parse_suite_rows(csv_path: Path) -> List[Dict[str, str]]:
    """
    Open the CSV and return only suite-definition rows
    (``suite_without_cases == '1'``).

    Exits with a descriptive error if the file is missing or contains no
    suite rows.
    """
    if not csv_path.exists():
        sys.exit(f"Error: CSV file not found: {csv_path}")
    rows: List[Dict[str, str]] = []
    with csv_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row.get("suite_without_cases", "").strip() == "1":
                rows.append(row)
    if not rows:
        sys.exit(
            f"Error: No suite rows found in {csv_path} "
            "(no rows with suite_without_cases == '1')."
        )
    return rows


# ---------------------------------------------------------------------------
# CSV structure validation — T006
# ---------------------------------------------------------------------------

def _validate_csv_structure(rows: List[Dict[str, str]]) -> None:
    """
    Verify that every non-empty ``suite_parent_id`` references a
    ``suite_id`` that exists in the same row set.

    Exits with an error naming each orphaned row before any API call is made.
    """
    known_ids = {r["suite_id"].strip() for r in rows if r.get("suite_id", "").strip()}
    orphans: List[str] = []
    for row in rows:
        parent_id = row.get("suite_parent_id", "").strip()
        if parent_id and parent_id not in known_ids:
            orphans.append(
                f"  suite_parent_id={parent_id!r} in row title={row.get('suite', '')!r}"
            )
    if orphans:
        sys.exit(
            "Error: Orphaned suite_parent_id references found in CSV "
            "(no matching suite_id):\n" + "\n".join(orphans)
        )


# ---------------------------------------------------------------------------
# Qase API — T008: fetch existing suites
# ---------------------------------------------------------------------------

def _fetch_existing_suites(project_code: str, token: str) -> Dict[str, int]:
    """
    Bulk-fetch all existing suites from the Qase project.

    Returns ``{title: qase_suite_id}``.

    Strategy:
      - Uses ``?limit=100`` to capture all 30 ShopEase suites in one call.
      - Paginates with ``offset`` if ``count < total`` (safety loop for F-03).
      - Keys on ``title`` alone because the GET response does not include
        ``parent_id`` (research.md F-02).
    """
    existing: Dict[str, int] = {}
    offset = 0
    limit = 100
    total: Optional[int] = None

    while True:
        path = (
            f"/suite/{urllib.parse.quote(project_code)}"
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
                    "Verify state/workspace_state.json was written by scripts/workspace_init.py."
                )
            raise
        result = resp.get("result", {})
        entities: List[Dict[str, Any]] = result.get("entities", [])
        if total is None:
            total = result.get("total", len(entities))
        for suite in entities:
            title = suite.get("title", "").strip()
            qase_id = suite.get("id")
            if title and qase_id is not None:
                existing[title] = int(qase_id)
        offset += len(entities)
        if not entities or offset >= (total or 0):
            break
    return existing


# ---------------------------------------------------------------------------
# Qase API — T009/T010: create a single suite
# ---------------------------------------------------------------------------

def _create_suite(
    project_code: str,
    token: str,
    title: str,
    parent_qase_id: Optional[int],
) -> int:
    """
    POST /suite/{code} to create a single suite.
    Returns the new Qase suite ID.
    """
    body: Dict[str, Any] = {"title": title}
    if parent_qase_id is not None:
        body["parent_id"] = parent_qase_id
    try:
        resp = _qase_request(
            "POST",
            f"/suite/{urllib.parse.quote(project_code)}",
            token,
            body=body,
        )
    except _QaseAPIError as exc:
        if exc.status == 400:
            sys.exit(
                f"Error: Qase rejected suite creation for title={title!r}. "
                f"Response: {exc.body}"
            )
        if exc.status in (401, 403):
            sys.exit("Error: Check QASE_API_TOKEN permissions.")
        if exc.status == 404:
            sys.exit(
                f"Error: project_code {project_code!r} not found in Qase (HTTP 404)."
            )
        raise
    qase_id = resp.get("result", {}).get("id")
    if qase_id is None:
        sys.exit(
            f"Error: Qase returned no suite ID for title={title!r}. "
            f"Response: {resp}"
        )
    return int(qase_id)


# ---------------------------------------------------------------------------
# Dry-run output — T015
# ---------------------------------------------------------------------------

def _dry_run_plan(rows: List[Dict[str, str]]) -> None:
    """
    Print the full ordered creation plan (Pass 1 then Pass 2) and exit 0.
    No API calls are made; ``state/workspace_state.json`` is not modified.
    """
    pass1 = [r for r in rows if not r.get("suite_parent_id", "").strip()]
    pass2 = [r for r in rows if r.get("suite_parent_id", "").strip()]
    id_to_title = {r["suite_id"].strip(): r["suite"].strip() for r in rows}

    print(f"[DRY-RUN] Pass 1 — top-level suites ({len(pass1)} total):")
    for i, row in enumerate(pass1, 1):
        print(
            f"  [{i:2d}] suite_id={row['suite_id'].strip():<4} "
            f"title={row['suite'].strip()!r}  parent=none"
        )
    print()
    print(f"[DRY-RUN] Pass 2 — child suites ({len(pass2)} total):")
    for i, row in enumerate(pass2, 1):
        parent_csv_id = row["suite_parent_id"].strip()
        parent_title = id_to_title.get(parent_csv_id, "?")
        print(
            f"  [{i + len(pass1):2d}] suite_id={row['suite_id'].strip():<4} "
            f"title={row['suite'].strip()!r}  "
            f"parent={parent_title!r} (csv_id={parent_csv_id})"
        )
    total = len(pass1) + len(pass2)
    print()
    print(f"[DRY-RUN] Total: {total} suites. No API calls made.")
    sys.exit(0)


# ---------------------------------------------------------------------------
# Main orchestrator — T007 + T009 + T010 + T011 + T012 + T013 + T014
# ---------------------------------------------------------------------------

def _run(args: argparse.Namespace) -> None:
    # ------------------------------------------------------------------ #
    # 1. Config + CSV path resolution (T004)                               #
    # ------------------------------------------------------------------ #
    config_path = _REPO_ROOT / (args.config or "config/workspace.yaml")
    config = _load_config(config_path)
    csv_path = _resolve_csv_path(args.csv, config)

    # ------------------------------------------------------------------ #
    # 2. CSV parsing + structure validation (T005, T006)                   #
    # ------------------------------------------------------------------ #
    rows = _parse_suite_rows(csv_path)
    _validate_csv_structure(rows)

    # ------------------------------------------------------------------ #
    # 3. Dry-run: print plan and exit — no API calls, no state write (T015)#
    # ------------------------------------------------------------------ #
    if args.dry_run:
        _dry_run_plan(rows)
        return  # unreachable — _dry_run_plan calls sys.exit(0)

    # ------------------------------------------------------------------ #
    # 4. Load workspace state → project_code (T007)                        #
    # ------------------------------------------------------------------ #
    state = load_state("workspace_state")
    project_code: Optional[str] = state.get("project_code")
    if not project_code:
        sys.exit(
            "Error: project_code not found in state/workspace_state.json. "
            "Run scripts/workspace_init.py first."
        )

    token = get_qase_token()

    # ------------------------------------------------------------------ #
    # 5. Pre-flight: fetch existing suites for idempotency (T008)          #
    # ------------------------------------------------------------------ #
    existing_map = _fetch_existing_suites(project_code, token)
    print(
        f"[GET]  Fetched {len(existing_map)} existing suite(s) "
        f"from project {project_code}."
    )

    # ------------------------------------------------------------------ #
    # 6. Split rows into two passes                                        #
    # ------------------------------------------------------------------ #
    pass1 = [r for r in rows if not r.get("suite_parent_id", "").strip()]
    pass2 = [r for r in rows if r.get("suite_parent_id", "").strip()]

    suite_id_map: Dict[str, int] = {}  # csv_suite_id → qase_suite_id
    created = 0
    reused = 0

    # ------------------------------------------------------------------ #
    # 7. Pass 1 — top-level suites (T009, T011)                            #
    # ------------------------------------------------------------------ #
    for row in pass1:
        csv_id = row["suite_id"].strip()
        title = row["suite"].strip()
        if title in existing_map:
            qase_id = existing_map[title]
            suite_id_map[csv_id] = qase_id
            reused += 1
            print(
                f"[PASS1] suite_id={csv_id:<4} → REUSED   "
                f"qase_id={qase_id:<6} title={title!r}"
            )
        else:
            qase_id = _create_suite(project_code, token, title, None)
            suite_id_map[csv_id] = qase_id
            existing_map[title] = qase_id  # keep local cache current
            created += 1
            print(
                f"[PASS1] suite_id={csv_id:<4} → CREATED  "
                f"qase_id={qase_id:<6} title={title!r}"
            )

    # ------------------------------------------------------------------ #
    # 8. Pass 2 — child suites (T010, T011)                                #
    # ------------------------------------------------------------------ #
    for row in pass2:
        csv_id = row["suite_id"].strip()
        title = row["suite"].strip()
        parent_csv_id = row["suite_parent_id"].strip()
        parent_qase_id = suite_id_map.get(parent_csv_id)
        if parent_qase_id is None:
            # This cannot happen after _validate_csv_structure, but guard defensively.
            sys.exit(
                f"Error: parent_csv_id={parent_csv_id!r} for suite {title!r} "
                "was not resolved in Pass 1. Please report a bug."
            )
        if title in existing_map:
            qase_id = existing_map[title]
            suite_id_map[csv_id] = qase_id
            reused += 1
            print(
                f"[PASS2] suite_id={csv_id:<4} → REUSED   "
                f"qase_id={qase_id:<6} title={title!r}"
            )
        else:
            qase_id = _create_suite(project_code, token, title, parent_qase_id)
            suite_id_map[csv_id] = qase_id
            existing_map[title] = qase_id
            created += 1
            print(
                f"[PASS2] suite_id={csv_id:<4} → CREATED  "
                f"qase_id={qase_id:<6} title={title!r}"
            )

    # ------------------------------------------------------------------ #
    # 9. Atomic state write: merge suite_ids; preserve all other keys      #
    #    (T012, T014)                                                       #
    #                                                                       #
    # INVARIANT: Any exception raised before this point (API failure,       #
    # network error, sys.exit) leaves workspace_state.json untouched.       #
    # The write only proceeds when all 30 suites are confirmed.             #
    # ------------------------------------------------------------------ #
    state["suite_ids"] = suite_id_map
    save_state("workspace_state", state)

    # ------------------------------------------------------------------ #
    # 10. Final summary line (T013, SC-001, FR-011)                        #
    # ------------------------------------------------------------------ #
    total = created + reused
    print(f"Suites complete: {created} created, {reused} reused (total {total})")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create Qase suite hierarchy from CSV.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python scripts/suite_generator.py\n"
            "  python scripts/suite_generator.py --dry-run\n"
            "  python scripts/suite_generator.py --csv assets/seed-data/QD-2026-02-18.csv\n"
            "  python scripts/suite_generator.py --config config/workspace.yaml\n"
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
            "Print the ordered creation plan without making any API calls "
            "or modifying state/workspace_state.json."
        ),
    )
    args = parser.parse_args()
    _run(args)


if __name__ == "__main__":
    main()
