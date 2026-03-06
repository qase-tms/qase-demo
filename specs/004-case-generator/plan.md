# Implementation Plan: Test Case Generator

**Branch**: `004-case-generator` | **Date**: 2026-02-24 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/004-case-generator/spec.md`

## Summary

`case_generator.py` is Step 4 of 7 in the Qase Living Workspace automation pipeline. It reads 120 test case rows from `assets/seed-data/QD-2026-02-18.csv`, translates string enum values to Qase API integers using a runtime-queried system-field map, maps custom field column names to API field IDs and option IDs from state, bulk-creates cases in batches of 30 via `POST /case/{code}/bulk`, writes the `case_ids` map to state before beginning the Jira link pass, and then links every case to its assigned Jira story via `POST /case/{code}/external-issue/attach`. The script is fully idempotent: a `GET /case/{code}` preflight checks for existing cases by `(title, suite_id)`, and a per-case link check (via `include=external_issues`) guards the link pass.

---

## Technical Context

**Language/Version**: Python 3.14 (`.venv/` interpreter — never call `python` or `python3` directly)
**Primary Dependencies**: `PyYAML` (config parsing), `urllib` stdlib (HTTP — no `requests`); all in `.venv/`
**Storage**: `state/workspace_state.json` (read + write), `state/jira_state.json` (read only), `assets/seed-data/QD-2026-02-18.csv` (read only)
**Testing**: `pytest` (`.venv/bin/pytest`)
**Target Platform**: Developer workstation + GitHub Actions (Linux)
**Project Type**: Single script (mirrors `suite_generator.py` architecture)
**Performance Goals**: 120 cases + 120 Jira links in < 5 minutes (excluding network latency); ≤ 5 req/sec
**Constraints**: Batches of ≤ 30 cases per bulk-create call; ≤ 5 API req/sec global; atomic state write; no hardcoded IDs
**Scale/Scope**: Fixed — 120 cases, 30 suites, 5 custom fields, one Jira link per case

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Gate | Principle | Status |
|------|-----------|--------|
| Credentials only in env/secrets | Security | ✅ PASS — `QASE_API_TOKEN` read via `get_qase_token()`; no tokens in code or config |
| No hardcoded project codes or IDs | Security / Reproducibility | ✅ PASS — all IDs from `state/workspace_state.json` or `state/jira_state.json` |
| API calls consult `api-index.md` first | API Reference Guidance | ✅ PASS — see `research.md` for all endpoint decisions |
| Rate limiting enforced | Technical Architecture | ✅ PASS — `_RATE_INTERVAL = 1/5` + `time.sleep()` in `_qase_request()` |
| Idempotent execution | Automation Structure | ✅ PASS — GET-before-POST on cases (FR-013) and links (FR-012) |
| Case count fixed after seeding | Principle VI | ✅ PASS — script only creates; never updates or deletes existing cases |
| Enum values from `constraints.md` | Entity Constraints | ✅ PASS — runtime enum map from `GET /system_field`; no hardcoded integers |

**Post-design re-check**: All gates hold. The two-phase write (state after creates, links after state) and `include=external_issues` link idempotency both reinforce the idempotency gate.

---

## Project Structure

### Documentation (this feature)

```text
specs/004-case-generator/
├── plan.md              ← this file
├── research.md          ← Phase 0 output
├── data-model.md        ← Phase 1 output
├── quickstart.md        ← Phase 1 output
├── contracts/
│   ├── bulk-create-cases.md
│   ├── attach-external-issue.md
│   ├── list-cases.md
│   └── system-fields.md
└── tasks.md             ← Phase 2 output (from /speckit.tasks)
```

### Source Code (repository root)

```text
scripts/
├── case_generator.py          ← NEW (this feature)
├── suite_generator.py         ← reference implementation
├── qase_seed_utils.py         ← shared helpers (get_qase_token, load_state, save_state)
├── jira_utils.py              ← Jira HTTP helpers (reference for Jira calls)
└── scripts/workspace_init.py          ← NEW (spec 001) — must run before case_generator

state/
├── workspace_state.json       ← read (project_code, suite_ids, custom_fields+options) + write (case_ids)
└── jira_state.json            ← read only (epics, stories with jira_id + epic_slug)

config/
└── workspace.yaml             ← read (cf_column_map, suite_domain_map, seed.cases_csv)

assets/seed-data/QD-2026-02-18.csv              ← read only (120 case rows + 31 suite rows)
```

**Structure Decision**: Single script following the established `suite_generator.py` pattern. No submodules — all logic in `scripts/case_generator.py` with imports from `qase_seed_utils`. The script is the unit of deployment and testing.

---

## Complexity Tracking

No constitution violations. No justified exceptions required.

---

## Implementation Design

### Execution Flow

```
case_generator.py
│
├─ Phase 0: Preflight validation
│   ├─ Load config/workspace.yaml (cf_column_map, suite_domain_map, seed.cases_csv)
│   ├─ Resolve CSV path (--csv arg → config fallback → error)
│   ├─ Load state/workspace_state.json (project_code, suite_ids, custom_fields)
│   ├─ Load state/jira_state.json (stories filtered by epic_slug)
│   ├─ Validate all suite_ids in CSV case rows exist in state suite_ids map
│   ├─ Validate all suite domain keys resolve to known epic slugs in jira_state
│   └─ Validate all custom field names in cf_column_map exist in state custom_fields
│
├─ Phase 1: Build runtime maps (API calls)
│   ├─ GET /system_field → build enum_map {field_name: {csv_string: int_value}}
│   └─ GET /custom_field/{id} per CF (or derive from state option IDs) → build cf_option_map
│
├─ Phase 2: Build Jira story assignment map
│   └─ For each domain slug, collect stories from jira_state filtered by epic_slug
│       → domain_stories {slug: [jira_key, ...]} in CSV row order
│
├─ (--dry-run exits here after printing plan)
│
├─ Phase 3: Idempotency preflight
│   └─ GET /case/{code}?limit=100&offset=N (paginated) → build existing_case_map
│       {(title, suite_qase_id): qase_case_id}
│
├─ Phase 4: Bulk create pass (batches of 30)
│   ├─ For each batch: build case payload list, POST /case/{code}/bulk
│   ├─ Map result.ids[] back to csv case IDs (preserve batch ordering)
│   └─ Accumulate case_id_map {csv_id: qase_case_id}
│
├─ Phase 5: Atomic state write
│   └─ save_state("workspace_state", state | {case_ids: case_id_map})
│
└─ Phase 6: Jira link pass
    ├─ GET /case/{code}?include=external_issues (paginated) → build linked_case_ids set
    └─ For each unlinked case: POST /case/{code}/external-issue/attach
        (batch up to 30 links per request via links[] array)
```

### Key Design Decisions

**D-01: Custom field option IDs source**
`scripts/workspace_init.py` (spec 001) MUST write `custom_fields.{name}.options: {option_name: option_id}` into `workspace_state.json`. `case_generator.py` reads these at runtime. If the options key is absent for any CF, the script exits with a descriptive error naming the missing field. See `research.md F-01`.

**D-02: jira_state.json story lookup**
The actual `jira_state.json` structure uses `stories.{slug-N}.{jira_id, jira_key, epic_slug}` — not the flat `story_ids`/`epic_ids` shape shown in plan.md. The script filters `stories` by `epic_slug` to build the domain story list. See `research.md F-02`.

**D-03: Attach external issue — batch links per call**
`POST /case/{code}/external-issue/attach` accepts a `links[]` array — multiple `{case_id, external_issues[]}` pairs per request. The script batches up to 30 link objects per call (matching the create batch size) to minimise API calls while staying within rate limits. See `research.md F-03`.

**D-04: Link idempotency detection**
`GET /case/{code}?include=external_issues` returns `external_issues[]` per case entity. Cases already linked (non-empty `external_issues`) are added to `linked_case_ids` set and skipped in the link pass. See `research.md F-04`.

**D-05: Bulk create response ordering**
`POST /case/{code}/bulk` returns `result.ids[]` in the same order as the input `cases[]` array. The script zips the input batch's `[csv_id, ...]` list against `result.ids` to build the case_id_map. Batch ordering MUST be preserved.

**D-06: Steps alignment**
All three step columns (`steps_actions`, `steps_result`, `steps_data`) are split on `"\n"` and numbered-prefix-stripped together. Lines are zipped by position: `[{action: line_i_actions, expected_result: line_i_result, data: line_i_data, position: i+1}]`. Empty lines produce step objects with empty string values (valid per API). Leading and trailing empty lines are dropped.

**D-07: Suite domain lookup for leaf suites**
The `suite_domain_map` keys are top-level suite names (e.g., `"01 Authentication"`). CSV case rows have `suite_id` pointing to a leaf suite (e.g., `9` = Registration). The script builds a parent-chain lookup from the CSV suite rows: `csv_suite_id → root_suite_title`. This is computed once from the CSV during preflight.

**D-08: is_flaky encoding**
CSV values are `"yes"` / `"no"` strings. The enum map converts these to `1` / `0` integers. The integer is submitted directly in the bulk create payload — never as a Python bool. See `constraints.md`.

**D-09: External issue type**
The Jira integration type is `"jira-cloud"`. This is the only type compatible with the Atlassian Cloud API used in this project. It is treated as a constant (not configurable) since the constitution mandates Jira Cloud REST API v3.

**D-10: Batch size for link pass**
The link pass uses batches of 30 (same as create pass). Each batch produces one `POST /case/{code}/external-issue/attach` call with 30 `links[]` entries, each `{case_id, external_issues: [jira_key_string]}`. Note: `jira_key` (e.g. `"AF-7"`) is the required format — numeric internal IDs are rejected by the API (empirically verified).
