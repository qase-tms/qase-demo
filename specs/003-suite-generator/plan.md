# Implementation Plan: Suite Generator

**Branch**: `003-suite-generator` | **Date**: 2026-02-20 | **Spec**: [`specs/003-suite-generator/spec.md`](spec.md)
**Input**: Feature specification describing CSV-driven Qase suite hierarchy creation with two-pass topological ordering, bulk pre-fetch idempotency, atomic state persistence, and dry-run support.

## Summary

Script `scripts/suite_generator.py` reads suite-only rows from the CSV (path resolved from `--csv` CLI arg or `config/workspace.yaml seed.cases_csv`), performs a pre-flight bulk `GET /suite/{code}` to seed the idempotency map, creates 7 top-level suites in Pass 1 and 23 child suites in Pass 2, and atomically writes the `{csv_suite_id: qase_suite_id}` mapping into the `suite_ids` key of `state/workspace_state.json`. All 30 Qase API `POST` calls are guarded by rate limiting (≤5 req/sec), exponential backoff (max 3 retries, 30-second cap), and pre-flight CSV structure validation. The script is the third step in the canonical execution sequence, after `scripts/workspace_init.py` and `jira_requirements.py`.

## Technical Context

**Language/Version**: Python 3.11 (matches the full workspace automation suite).
**Primary Dependencies**: `csv` (stdlib), `urllib.request` (stdlib), `PyYAML` (≥5.4), `pathlib` (stdlib); shared helpers from `scripts/qase_seed_utils.py` (`get_qase_token`, `load_state`, `save_state`).
**Storage**: `state/workspace_state.json` — read for `project_code`, merged with `suite_ids` on write. Atomic write via temp-file rename (provided by `save_state`).
**Testing**: `pytest` with `unittest.mock` for HTTP call patching; no live API required.
**Target Platform**: Linux/macOS developer workstations + GitHub Actions runners (Python 3.11).
**Project Type**: Single CLI script; no web server or package structure needed.
**Performance Goals**: Full 30-suite creation completes within 60 seconds excluding API latency; ≤5 req/sec enforced at all times.
**Constraints**: `QASE_API_TOKEN` read exclusively from environment; no hardcoded IDs; state written only after all 30 suites confirmed; 3 retries max with 30-second total cap per request.
**Scale/Scope**: 30 suites (7 top-level, 23 child); 1 GET + up to 30 POSTs = 31 Qase API calls maximum per run.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Gate | Principle | Status |
|------|-----------|--------|
| Credentials only in env/secrets | Security | ✅ `QASE_API_TOKEN` via `get_qase_token()` — never in code or config |
| No hardcoded project codes or IDs | Security / Reproducibility | ✅ `project_code` read from `state/workspace_state.json`; parent IDs resolved in memory from the CSV-to-Qase map |
| API calls consult `api-index.md` first | API Reference Guidance | ✅ Consulted `get-suites.md` and `create-suite.md` before design; see `research.md` |
| Rate limiting enforced | Technical Architecture | ✅ ≤5 req/sec with `time.sleep()` between calls; shared rate-limiter from `jira_requirements.py` pattern |
| Idempotent execution | Automation Structure | ✅ Bulk pre-fetch builds `title → qase_id` map; suites already present are reused, never re-POSTed |
| Case count fixed after seeding | Principle VI | ✅ This script only creates suites, not cases; no case mutations |
| Enum values from `constraints.md` | Entity Constraints | ✅ Suites have no enum fields; only `title` (string) and `parent_id` (integer) |

All gates pass. No violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/003-suite-generator/
├── plan.md              ← this file
├── research.md          ← Phase 0 output
├── data-model.md        ← Phase 1 output
├── quickstart.md        ← Phase 1 output
├── contracts/
│   └── qase-suite-api.md  ← Phase 1 output
└── tasks.md             ← Phase 2 output (via /speckit.tasks)
```

### Source Code (repository root)

```text
scripts/
├── suite_generator.py      ← NEW — main entry point for this feature
├── qase_seed_utils.py      ← SHARED — get_qase_token(), load_state(), save_state()
└── ...

state/
├── workspace_state.json    ← Read: project_code; Updated: suite_ids key added
└── jira_state.json         ← Not touched by this script

config/
└── workspace.yaml          ← Read: seed.cases_csv (fallback for CSV path)

assets/seed-data/QD-2026-02-18.csv           ← Source of truth for suite hierarchy
```

**Structure Decision**: Single-script structure. All logic lives in `scripts/suite_generator.py`. Shared state I/O and token helpers are imported from `scripts/qase_seed_utils.py`. No new packages or directories are introduced.

## Implementation Design

### Module layout (`suite_generator.py`)

```text
suite_generator.py
├── Constants & rate-limiter state
├── _qase_request(method, path, body)     — rate-limited HTTP with retry/backoff
├── _load_config(config_path)             — parse config/workspace.yaml
├── _resolve_csv_path(cli_arg, config)    — --csv arg vs config fallback
├── _parse_suite_rows(csv_path)           — extract suite_without_cases == "1" rows
├── _validate_csv_structure(rows)         — orphan reference check (FR-008)
├── _fetch_existing_suites(project_code)  — GET /suite/{code}, return title→id map
├── _create_or_reuse_suite(project_code, title, parent_qase_id, existing_map)
├── _run(args)                            — orchestrator: passes 1 + 2, state write
└── main() / argparse
```

### Execution flow

```
startup
  ├── parse args (--csv, --dry-run, --config)
  ├── load config/workspace.yaml  → resolve CSV path (FR-001)
  ├── load state/workspace_state.json → project_code (FR-005)
  ├── parse CSV → suite rows (FR-001)
  └── validate: all Pass-2 suite_parent_ids reference a Pass-1 suite_id (FR-008)

if dry-run
  └── print ordered plan (Pass 1 then Pass 2) and exit 0 — no API calls (FR-010)

if not dry-run
  ├── GET /suite/{code}?limit=100 → build title→qase_id in-memory map (FR-004)
  ├── Pass 1 — top-level suites (suite_parent_id is empty/null)
  │     for each row:
  │       if title in existing_map → reuse qase_id (log "reused")
  │       else → POST /suite/{code} → capture new qase_id (log "created")
  │       accumulate csv_suite_id → qase_id in suite_id_map
  ├── Pass 2 — child suites (suite_parent_id != empty)
  │     for each row:
  │       resolve parent_qase_id from suite_id_map
  │       if title in existing_map → reuse qase_id (log "reused")
  │       else → POST /suite/{code} with parent_id → capture qase_id (log "created")
  │       accumulate csv_suite_id → qase_id in suite_id_map
  ├── atomic write: merge suite_ids into workspace_state.json (FR-006, FR-007)
  └── print summary: "Suites complete: N created, M reused (total 30)" (FR-011)
```

### Rate-limiter & retry pattern

Mirrors `jira_requirements.py` exactly:
- Module-level `_last_req_ts` tracks last request time
- `_RATE_INTERVAL = 1.0 / 5` (200 ms minimum gap)
- Retry loop: max 3 attempts; backoff `2^(attempt-1)` seconds (1 s, 2 s, 4 s)
- Retryable HTTP codes: 429, 500, 502, 503, 504
- Per-request `timeout=30` seconds (FR-012)

### Idempotency: title-matching design decision

`GET /suite/{code}` documented response does **not** include `parent_id` (see `research.md` Finding F-02). The in-memory existing-suites map is therefore keyed on `title` alone. This is safe for the ShopEase workspace because all 30 suite titles are globally unique within the project (confirmed by CSV inspection). If `parent_id` becomes available in the API response in future, the key can be upgraded to `(title, parent_id)` without changing any other logic.

### CSV column references

| CSV column | Usage |
|---|---|
| `suite_without_cases` | Filter: keep only rows where value == `"1"` |
| `suite_id` | Becomes the key in `suite_id_map` (string, used as dict key) |
| `suite_parent_id` | Empty = Pass 1 (top-level); non-empty = Pass 2 (child) |
| `suite` | `title` sent to `POST /suite/{code}` |

### State merge strategy

`save_state` from `qase_seed_utils` overwrites the full file. To preserve existing keys (FR-007), the script:
1. Calls `load_state("workspace_state")` to get the current dict
2. Merges: `state["suite_ids"] = suite_id_map`
3. Calls `save_state("workspace_state", state)` atomically

## Complexity Tracking

No constitution violations were introduced. The script stays within the step-based sequential execution model and satisfies all constitutional gates.
