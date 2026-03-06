# Feature Tasks: Suite Generator

**Input**: Design documents from `specs/003-suite-generator/`
**Script target**: `scripts/suite_generator.py` (new file)
**Organization**: Tasks grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different logical units, no incomplete-task dependency)
- **[Story]**: User story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup & Tooling

**Purpose**: Create the new script file with all scaffolding in place before any logic is written.

- [x] T001 Initialize `scripts/suite_generator.py` with module docstring, stdlib imports (`argparse`, `csv`, `json`, `sys`, `time`, `urllib.request`, `pathlib`), PyYAML import with graceful fallback, and `main()` / `argparse` wiring for `--csv`, `--config`, and `--dry-run` flags.
- [x] T002 Confirm `scripts/qase_seed_utils.py` already exposes `get_qase_token()`, `load_state(name)`, and `save_state(name, data)` — no changes required; add an import block for these helpers in `scripts/suite_generator.py`.

---

## Phase 2: Foundational Tasks

**Purpose**: Core infrastructure that ALL user stories depend on — must complete before any US phase begins.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T003 Implement `_qase_request(method, path, body=None)` in `scripts/suite_generator.py` — module-level `_last_req_ts` + `_RATE_INTERVAL = 0.20` enforce ≤5 req/sec; retry loop up to `_MAX_RETRIES = 3` on HTTP codes 429/500/502/503/504 with backoff `2^(attempt-1)` seconds; per-request `timeout=30`; raises on non-retryable 400/401/403/404; base URL `https://api.qase.io/v1`, auth header `Token: <QASE_API_TOKEN>`.
- [x] T004 Implement `_load_config(config_path)` and `_resolve_csv_path(cli_arg, config)` in `scripts/suite_generator.py` — reads `config/workspace.yaml` via PyYAML; returns `config["seed"]["cases_csv"]` as fallback when `--csv` is not supplied; exits with a clear configuration error if neither source provides a path.
- [x] T005 Implement `_parse_suite_rows(csv_path)` in `scripts/suite_generator.py` — uses `csv.DictReader` to open the file and return only the rows where `suite_without_cases == "1"` as a list of dicts; exits with a descriptive error if the file is missing or zero suite rows are found.
- [x] T006 Implement `_validate_csv_structure(rows)` in `scripts/suite_generator.py` — collects the set of all `suite_id` values from the filtered rows; then checks every non-empty `suite_parent_id` value against that set; exits with an error naming each orphaned row before any API call is made (FR-008).
- [x] T007 Add startup state loading in `_run(args)` in `scripts/suite_generator.py` — call `load_state("workspace_state")` and assert `project_code` is present; exit with a descriptive error citing the missing key and directing the user to run `scripts/workspace_init.py` first (FR-005).

**Checkpoint**: Foundation complete — user story implementation can now begin.

---

## Phase 3 – User Story 1 (P1): Build the Qase suite hierarchy from the CSV 🎯 MVP

**Goal**: Create all 30 suites in the correct parent-before-child order and log each create/reuse event.

**Independent Test**: Run `python scripts/suite_generator.py` against a project initialised by `scripts/workspace_init.py`. Confirm Qase shows exactly 7 top-level and 23 child suites with the correct titles. Confirm the final output line reads `"Suites complete: 30 created, 0 reused (total 30)"`.

- [x] T008 [US1] Implement `_fetch_existing_suites(project_code)` in `scripts/suite_generator.py` — calls `GET /suite/{project_code}?limit=100` via `_qase_request`; loops with `offset` increments if `result.count < result.total` (pagination safety); returns `{title: qase_id}` dict keyed on title alone (see `research.md` F-02).
- [x] T009 [US1] Implement Pass 1 in `_run()` in `scripts/suite_generator.py` — iterate the 7 top-level suite rows (empty `suite_parent_id`); for each: check `existing_map` by title — if found, reuse the ID; otherwise call `POST /suite/{code}` with `{"title": row["suite"]}`; accumulate `{csv_suite_id: qase_id}` in `suite_id_map`.
- [x] T010 [US1] Implement Pass 2 in `_run()` in `scripts/suite_generator.py` — iterate the 23 child suite rows (non-empty `suite_parent_id`); resolve `parent_qase_id = suite_id_map[row["suite_parent_id"]]`; check `existing_map` by title; if not found call `POST /suite/{code}` with `{"title": ..., "parent_id": parent_qase_id}`; accumulate into `suite_id_map`.
- [x] T011 [US1] Add per-event logging in `_run()` in `scripts/suite_generator.py` — after each create or reuse, print `[PASS1] suite_id=N → CREATED qase_id=M title="..."` (or `REUSED`); track running `created` and `reused` counters for the final summary (FR-011).

**Checkpoint**: User Story 1 is independently functional. Run script and verify Qase hierarchy matches the CSV structure.

---

## Phase 4 – User Story 2 (P2): Persist the suite ID mapping for downstream scripts

**Goal**: Atomically merge the `suite_ids` mapping into `state/workspace_state.json` without disturbing any other keys.

**Independent Test**: After a successful run inspect `state/workspace_state.json`. Confirm `suite_ids` has exactly 30 non-null integer entries. Confirm all keys set by `scripts/workspace_init.py` (e.g., `project_code`, `custom_field_ids`, `milestone_ids`) are still present and unchanged.

- [x] T012 [US2] Implement the atomic state write at the end of `_run()` in `scripts/suite_generator.py` — call `load_state("workspace_state")` to get the current dict, set `state["suite_ids"] = suite_id_map`, then call `save_state("workspace_state", state)`; this write runs only after all 30 suites are confirmed created or reused (FR-006, FR-007).
- [x] T013 [US2] Print the final summary line in `_run()` in `scripts/suite_generator.py` — `f"Suites complete: {created} created, {reused} reused (total {created + reused})"` immediately after the state write succeeds (FR-011, SC-001).
- [x] T014 [US2] Verify the failure-before-write guarantee in `scripts/suite_generator.py` — confirm that any exception raised by `_qase_request()` (including after 3 retries) propagates out of `_run()` before `save_state` is called, so `state/workspace_state.json` remains untouched on partial runs; add a brief comment in the code documenting this invariant.

**Checkpoint**: User Stories 1 and 2 are both independently functional. State file is correct; downstream `case_generator.py` can consume `suite_ids`.

---

## Phase 5 – User Story 3 (P3): Dry-run mode for safe pre-flight inspection

**Goal**: `--dry-run` prints the full ordered creation plan and exits cleanly without touching Qase or state.

**Independent Test**: Run `python scripts/suite_generator.py --dry-run`. Confirm exit code 0, output lists exactly 30 suite names (7 Pass-1 entries then 23 Pass-2 entries with their intended parent references), and `state/workspace_state.json` is unchanged (SC-004).

- [x] T015 [US3] Implement the `--dry-run` branch in `_run()` in `scripts/suite_generator.py` — after CSV parsing and structure validation but before any API call, if `args.dry_run` is set: print a `[DRY-RUN]` header, then iterate Pass 1 rows printing `suite_id`, `title`, and `parent=none`, then iterate Pass 2 rows printing `suite_id`, `title`, and `parent="<parent title>" (csv_id=N)`, then print `"[DRY-RUN] Total: 30 suites. No API calls made."` and call `sys.exit(0)` (FR-010, SC-004).
- [x] T016 [US3] Cross-check the dry-run output format against the sample shown in `specs/003-suite-generator/quickstart.md` and update either the code or the quickstart if they diverge; confirm state file is never opened for writing in dry-run path.

**Checkpoint**: All three user stories independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Error surfaces, documentation consistency, and index hygiene.

- [x] T017 Polish error messages throughout `scripts/suite_generator.py` — each `sys.exit` call must include a one-sentence actionable message: missing token → "Set QASE_API_TOKEN environment variable"; missing project_code → "Run scripts/workspace_init.py first"; missing CSV → "Provide --csv or set seed.cases_csv in config/workspace.yaml"; orphaned parent reference → "suite_parent_id <N> in row '<title>' has no matching suite_id"; API 401/403 → "Check QASE_API_TOKEN permissions"; API 404 → "project_code <X> not found in Qase".
- [x] T018 Update `api-index.md` to add the two suite endpoints used by this script: `suites.list → api/get-suites.md` and `suites.create → api/create-suite.md` under a new `## Suites` section, so they are discoverable for future scripts.
- [x] T019 Do a final read-through of `specs/003-suite-generator/quickstart.md` against the implemented CLI to confirm all flag names, expected output samples, and troubleshooting rows are accurate; update any discrepancies in-place.

---

## Dependencies & Execution Order

1. **Phase 1 → Phase 2**: Script scaffold must exist before any functions are added.
2. **Phase 2 → User Story Phases**: All foundational helpers (`_qase_request`, `_load_config`, `_parse_suite_rows`, `_validate_csv_structure`, state load) must work before suite creation logic can be written.
3. **Phase 3 (US1) → Phase 4 (US2)**: The `suite_id_map` built in US1 is the input to the state write in US2; US2 wraps the completion of US1.
4. **Phase 2 → Phase 5 (US3)** (independent of US1/US2): Dry-run depends only on CSV parsing + validation, not on the API-call logic; can be implemented in parallel with US1 by a second developer.
5. **Phase 6**: Can proceed once all user stories are functional; T017–T019 have no interdependencies.

### User story dependencies at a glance

| Story | Depends on | Can run in parallel with |
|-------|-----------|--------------------------|
| US1 (P1) | Phase 2 complete | US3 (dry-run path is independent) |
| US2 (P2) | US1 complete (needs `suite_id_map`) | — |
| US3 (P3) | Phase 2 complete | US1 |

---

## Parallel Execution Opportunities

- **T003–T007** (Phase 2): each function is self-contained; two developers could split T003/T004 vs T005/T006/T007 and merge into the same file without conflicts.
- **T008 and T015** can be developed in parallel: `_fetch_existing_suites()` (T008) and the dry-run print loop (T015) operate in different branches of `_run()` and do not share mutable state.
- **T017, T018, T019** (Phase 6 polish) have no interdependencies and can all run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 only)

1. Complete Phase 1 (scaffold) and Phase 2 (foundational helpers).
2. Complete Phase 3 (US1) — suite hierarchy created in Qase.
3. **Stop and validate**: `python scripts/suite_generator.py` creates 30 suites; verify in Qase UI and via `state/workspace_state.json`.
4. Proceed to Phase 4 (US2) to persist state, then Phase 5 (US3) for dry-run.

### Incremental Delivery

1. **Setup + Foundation** → script runs without crashing.
2. **US1** → 30 suites visible in Qase.
3. **US2** → `suite_ids` persisted; `case_generator.py` can now be developed.
4. **US3** → dry-run works; safe to re-run in CI pre-flight.
5. **Polish** → clean errors, updated index, consistent docs.
