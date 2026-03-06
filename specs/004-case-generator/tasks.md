# Tasks: Test Case Generator

**Input**: Design documents from `specs/004-case-generator/`
**Prerequisites**: plan.md ✅ | spec.md ✅ | research.md ✅ | data-model.md ✅ | contracts/ ✅ | quickstart.md ✅

**Tests**: No test tasks generated — not requested in the spec.

**Organization**: Tasks grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different logic units, no blocking dependency between them)
- **[Story]**: Which user story this task belongs to (US1–US4)
- All paths relative to repo root

---

## Phase 1: Setup

**Purpose**: Create the new script file with module-level scaffolding before any logic is added.

- [X] T001 Create `scripts/case_generator.py` with module docstring (step, credentials, usage, design principles in the style of `scripts/suite_generator.py`), module-level constants (`_BASE_URL`, `_RATE_INTERVAL = 1/5`, `_MAX_RETRIES = 3`, `_RETRY_STATUS_CODES`, `IS_FLAKY_MAP = {"no": 0, "yes": 1}`, `_REPO_ROOT`), `_last_req_ts` rate-limiter global, and a stub `def main(): pass` placeholder (T023 will replace it); include `if __name__ == "__main__": main()` guard at the bottom — the stub prevents `NameError` if the script is executed during MVP testing before Phase 6

**Checkpoint**: File exists, imports `sys`, `csv`, `json`, `time`, `argparse`, `urllib.*`, `pathlib.Path`; imports `get_qase_token`, `load_state`, `save_state` from `scripts/qase_seed_utils.py`; and has `if __name__ == "__main__": main()` stub at the bottom

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core helpers that every user story depends on. ALL must be complete before US1 work begins.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T002 Port `_QaseAPIError` class and `_qase_request()` function from `scripts/suite_generator.py` into `scripts/case_generator.py` — identical behaviour: rate-limit (200 ms gap), exponential-backoff retry on `_RETRY_STATUS_CODES`, 30 s timeout, raises `_QaseAPIError` for non-retryable HTTP errors

- [X] T003 [P] Implement `_load_config()` and `_resolve_csv_path()` in `scripts/case_generator.py` — `_load_config(path)` reads `config/workspace.yaml` via PyYAML; `_resolve_csv_path(cli_arg, config)` returns absolute `Path` from `--csv` arg or `config.seed.cases_csv`, exits with descriptive error if neither available

- [X] T004 [P] Implement `_parse_case_rows()` and `_parse_suite_rows_for_lookup()` in `scripts/case_generator.py` — `_parse_case_rows()` returns rows where `suite_without_cases != "1"`, exits if CSV not found or yields zero rows; `_parse_suite_rows_for_lookup()` returns rows where `suite_without_cases == "1"`, used to build the leaf-to-root map

- [X] T005 Implement `_parse_steps()` in `scripts/case_generator.py` — splits `steps_actions`, `steps_result`, `steps_data` on `"\n"`, strips numbered prefix regex `r"^\d+\.\s*"` from each line, zips the three lists by position, drops leading/trailing entries where action is empty after stripping, returns `[{"action": str, "expected_result": str, "data": str, "position": int}]` (1-based)

- [X] T006 Implement `_build_leaf_to_root_map()` in `scripts/case_generator.py` — from suite rows, builds `{csv_suite_id_str: root_suite_title_str}` by walking the parent chain; ShopEase is max 2 levels so: if row has `suite_parent_id` empty → it is a root, title is its own; if row has `suite_parent_id` → root title is the title of the parent row; returns complete map for all 30 suite IDs

- [X] T007 [P] Implement `_build_enum_map()` in `scripts/case_generator.py` — calls `GET /system_field` per `api/get-system-fields.md` (no project code), builds `{field_name_lower: {option_title_lower: option_id_int}}` from `result[].options[].{id, title}`; exits with descriptive error on API failure; returns `enum_map`

- [X] T008 [P] Implement `_build_cf_maps()` in `scripts/case_generator.py` — reads `custom_fields` from `state/workspace_state.json`; for each CF name in `cf_column_map` values, extracts `custom_fields[name]["id"]` into `cf_id_map` and `custom_fields[name]["options"]` into `cf_option_map`; exits with error naming any CF whose `options` key is absent (research.md F-01)

- [X] T009 Implement `_build_domain_stories_map()` in `scripts/case_generator.py` — filters `jira_state["stories"]` by `epic_slug` for each domain slug in `suite_domain_map` values; builds two parallel maps in `stories` dict insertion order per research.md F-02: (1) `domain_stories_map = {domain_slug: [jira_id_str, ...]}` (internal IDs for link calls) and (2) `domain_stories_key_map = {domain_slug: [jira_key_str, ...]}` (display keys e.g. `"AF-7"` for dry-run output); initialises `domain_cursors = {slug: 0}` for round-robin; exits with error if a domain slug has no matching stories in jira_state; returns `(domain_stories_map, domain_stories_key_map, domain_cursors)`

- [X] T010 Implement `_validate_preflight()` in `scripts/case_generator.py` — validates: (a) all `suite_id` values from case rows exist in `state["suite_ids"]`, naming any missing; (b) all CF names from `cf_column_map` exist in `custom_fields` with an `options` key; (c) all domain slugs resolved from `suite_domain_map` exist in `domain_stories_map`; exits with consolidated error message before any API call if any check fails

**Checkpoint**: All foundational helpers implemented and importable. All Phase 3+ work can now begin in parallel if desired.

---

## Phase 3: User Story 1 — Seed all 120 test cases (Priority: P1) 🎯 MVP

**Goal**: Run `case_generator.py` against a fresh workspace and create all 120 cases with correct fields, steps, and custom field values. Write `case_ids` to state.

**Independent Test**: `scripts/case_generator.py` with no prior cases → Qase shows 120 cases across 30 suites, each with 5 custom fields and step objects; `state/workspace_state.json` has `case_ids` with 120 entries; final output line reads `"Cases complete: 120 created, 0 reused (total 120)"`.

- [X] T011 [US1] Implement `_build_case_payload()` in `scripts/case_generator.py` — accepts a single case row dict + `enum_map` + `cf_id_map` + `cf_option_map` + `suite_id_map`; returns a Qase case payload dict with: `title`, `description`, `preconditions`, `postconditions`, all system-field integers (via `enum_map`), `is_flaky` as int (via `IS_FLAKY_MAP`), `suite_id` (via `suite_id_map`), `steps` list (via `_parse_steps()`), and `custom_field` dict (keys = str(field_id), values = str(option_id) for selectbox; comma-joined str(option_ids) for multiselect cf_10); omits `milestone_id` since all rows have empty value; **error paths**: (1) if any system-field string value is not found in `enum_map[field_name]`, call `sys.exit()` with message: `"ERROR row {csv_id}: unrecognised {field_name} value '{value}'"` (FR-006); (2) if any CF option string is not found in `cf_option_map[cf_name]`, call `sys.exit()` with message: `"ERROR row {csv_id}: unrecognised {cf_column} ('{cf_name}') option '{value}'"` (spec edge case)

- [X] T012 [P] [US1] Implement `_fetch_existing_cases()` in `scripts/case_generator.py` — paginates `GET /case/{project_code}?limit=100&offset=N` per `contracts/list-cases.md` until `offset >= total`; builds and returns `{(title, suite_id_int): qase_case_id_int}` from response entities; exits on 401/403/404

- [X] T013 [P] [US1] Implement `_bulk_create_batch()` in `scripts/case_generator.py` — accepts `project_code`, `token`, ordered list of `(csv_id, payload)` pairs; posts `{"cases": [payload, ...]}` to `POST /case/{code}/bulk` per `contracts/bulk-create-cases.md`; zips `result["ids"]` with `csv_ids` list by index (D-05) to return `{csv_id: qase_case_id}`; exits with batch range in error message on 400/422

- [X] T014 [US1] Implement `_run_create_pass()` in `scripts/case_generator.py` — iterates all 120 case rows in CSV order; for each row builds the payload via `_build_case_payload()` and assigns a Jira story via `domain_stories_map` + `domain_cursors` round-robin (advancing cursor in CSV row order per clarification Q5); checks `existing_case_map` by `(title, suite_qase_id)` — on hit: adds to `case_id_map`, increments `reused`, logs `"REUSE case {csv_id}: '{title}' → qase_id={N}"`; on miss: batches into groups of ≤30; after each batch POSTs via `_bulk_create_batch()`, logs `"Batch K/T: N created"`, accumulates `case_id_map`; returns `(case_id_map, jira_assignment_map, created_count, reused_count)`

- [X] T015 [US1] Implement `_write_case_ids_to_state()` in `scripts/case_generator.py` — accepts the in-memory state dict already loaded in `_run()` (no redundant re-read from disk); merges `{"case_ids": case_id_map}` into it in-place (preserving all existing keys), then calls `save_state("workspace_state", merged_state)` for atomic write (temp file + rename via `qase_seed_utils`) per FR-014 (clarification Q2: written before link pass)

- [X] T016 [US1] Implement `_run()` skeleton (phases 0–5) in `scripts/case_generator.py` — calls in this exact order: `_load_config()`, `_resolve_csv_path()`, `load_state("workspace_state")`, `load_state("jira_state")`, `_parse_case_rows()`, `_parse_suite_rows_for_lookup()`, `_build_leaf_to_root_map()`, `_validate_preflight()`, `_build_cf_maps()`, `(domain_stories_map, domain_stories_key_map, domain_cursors) = _build_domain_stories_map()`, **[dry-run gate — see T022]**, `get_qase_token()`, `_build_enum_map()`, `_fetch_existing_cases()`, `_run_create_pass()`, `_write_case_ids_to_state()`; prints final summary `"Cases complete: N created, M reused (total 120)"`; `_build_cf_maps()` and `_build_domain_stories_map()` are placed before `get_qase_token()` because they read only from already-loaded state/jira_state (no API calls)

**Checkpoint**: `_run()` (phases 0–5) is callable end-to-end. US1 acceptance scenarios 1–4 are satisfiable.

---

## Phase 4: User Story 2 — Link every case to its Jira story (Priority: P2)

**Goal**: After cases are created and state is written, link all 120 cases to their assigned Jira stories via batched `POST /case/{code}/external-issue/attach`. Skip cases already linked on re-run.

**Independent Test**: After a full run, spot-check Qase cases across domains — each has exactly one Jira link; the linked story's `epic_slug` matches the case's suite domain. Re-running produces `"Links batch K/T: 0 linked, 30 skipped"` for all batches.

- [X] T017 [US2] Implement `_fetch_linked_cases()` in `scripts/case_generator.py` — paginates `GET /case/{code}?limit=100&offset=N&include=external_issues` per `contracts/list-cases.md`; builds and returns `linked_case_ids` set of Qase case IDs where `entity["external_issues"]` is non-empty (D-04)

- [X] T018 [US2] Implement `_attach_links_batch()` in `scripts/case_generator.py` — accepts list of `(qase_case_id, jira_id_str)` pairs (≤30); posts `{"type": "jira-cloud", "links": [{"case_id": int, "external_issues": [str]}, ...]}` to `POST /case/{code}/external-issue/attach` per `contracts/attach-external-issue.md`; returns number of links sent; exits with batch case IDs in error message on 400/422

- [X] T019 [US2] Implement `_run_link_pass()` in `scripts/case_generator.py` — receives `case_id_map` (csv_id → qase_id) and `jira_assignment_map` (csv_id → jira_id_str); fetches `linked_case_ids` via `_fetch_linked_cases()`; iterates `case_id_map` values, skips those in `linked_case_ids`; batches remaining into groups of ≤30; after each batch calls `_attach_links_batch()`, logs `"Links batch K/T: N linked, M skipped"`; returns `(linked_count, skipped_count)`

- [X] T020 [US2] Extend `_run()` in `scripts/case_generator.py` to include phase 6 — after `_write_case_ids_to_state()`, call `_run_link_pass(case_id_map, jira_assignment_map)` and log its result; full execution now covers all phases 0–6

**Checkpoint**: Full pipeline runs end-to-end. US2 acceptance scenarios 1–4 are satisfiable. The script is feature-complete for a first live run.

---

## Phase 5: User Story 3 — Dry-run mode (Priority: P3)

**Goal**: `--dry-run` prints the full 120-case distribution plan (suite, title, CF values, Jira story key) and exits cleanly with no API calls and no state mutation.

**Independent Test**: `scripts/case_generator.py --dry-run` exits 0; prints 120 plan lines + summary; `state/workspace_state.json` is unchanged; zero network calls visible in output.

- [X] T021 [US3] Implement `_dry_run_plan()` in `scripts/case_generator.py` — accepts case rows, `cf_id_map`, `cf_option_map`, `suite_id_map`, `leaf_to_root_map`, `suite_domain_map`, `domain_stories_map`, `domain_stories_key_map`, `domain_cursors`; for each row prints one line: `"[DRY-RUN]  {i:3d}  suite={suite_name}  csv_id={id}  jira={story_key}  title={title[:60]}"` plus **raw CSV string values** for system fields (priority, severity, etc. — not translated to integers, since no enum API call is made in dry-run); CF values shown as resolved option IDs from `cf_option_map`; after all rows prints `"[DRY-RUN] Summary: 120 cases planned, N suites affected, M unique Jira stories referenced."`; calls `sys.exit(0)`; note: `enum_map` is NOT a parameter — dry-run mode does not call `GET /system_field`

- [X] T022 [US3] Add `--dry-run` gate in `_run()` in `scripts/case_generator.py` — positioned immediately after `_build_domain_stories_map()` and **before** `get_qase_token()` (per corrected call order in T016); if `args.dry_run` is true, call `_dry_run_plan()` and return; this placement guarantees zero API calls (FR-017): `_build_cf_maps()` and `_build_domain_stories_map()` use only already-loaded state/jira_state, `get_qase_token()`/`_build_enum_map()`/`_fetch_existing_cases()` are never reached; state file is never touched in this path

**Checkpoint**: `--dry-run` works independently. US3 acceptance scenarios 1–3 are satisfiable.

---

## Phase 6: User Story 4 — Idempotent re-runs & CLI entry point (Priority: P4)

**Goal**: Wire the `argparse` CLI entry point and confirm the two-phase recovery path (creates done, links interrupted) works correctly across re-runs.

**Independent Test**: Run `case_generator.py` twice — second run produces `"Cases complete: 0 created, 120 reused (total 120)"` and all link batches show `"0 linked, 30 skipped"`. Run with only half the cases existing — second run creates only the remaining 60.

- [X] T023 [US4] Implement `main()` in `scripts/case_generator.py` — `argparse.ArgumentParser` with `--csv PATH`, `--config PATH`, `--dry-run` flags and epilog showing 3 usage examples matching `quickstart.md`; calls `_run(args)` and passes `args` namespace through the call chain; add `if __name__ == "__main__": main()` guard

- [X] T024 [US4] Verify two-phase recovery in `_run()` in `scripts/case_generator.py` — confirm that when `_write_case_ids_to_state()` succeeds but `_run_link_pass()` is interrupted (e.g., raises midway), a subsequent run correctly re-builds `case_id_map` via the create pass (all 120 reused from Qase), re-writes state, then calls `_run_link_pass()` which skips already-linked cases and links only the remainder; no code changes should be needed if phases 3–6 are correctly wired — this task is an implementation review + any fixes needed

**Checkpoint**: All 4 user stories are independently satisfiable. Full pipeline passes all acceptance scenarios.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Hardening, log-format compliance, and documentation finishes.

- [X] T025 [P] Audit all error exits in `scripts/case_generator.py` — verify every `sys.exit()` call includes a descriptive human-readable message; check all API paths: 401/403 → credential error, 404 → project/resource not found with name, 400/422 → batch range + response body, network error → URL + reason; compare against `contracts/` error tables

- [X] T026 [P] Audit log format in `scripts/case_generator.py` — verify batch lines match `"Batch K/T: N created"`, REUSE lines match `"REUSE case {csv_id}: '{title}' → qase_id={N}"`, ERROR lines match `"ERROR batch K: {reason}"`, link batch lines match `"Links batch K/T: N linked, M skipped"`, summary line matches `"Cases complete: N created, M reused (total 120)"` — all per FR-018 and clarification Q4

- [X] T027 [P] Complete module docstring in `scripts/case_generator.py` top-of-file — add Credential lookup section, Usage section (3 examples), and Design principles section (idempotent, config-driven, rate-limited, atomic state write) mirroring `scripts/suite_generator.py` style

- [X] T028 Run quickstart.md dry-run and live scenarios against the current workspace to confirm expected output lines, state file shape, and Jira link presence; fix any discrepancies found in `scripts/case_generator.py`; verify total elapsed time for 120 creates + 120 links is within SC-001's 5-minute ceiling (log start/end timestamps, exclude API latency)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — **BLOCKS all user story phases**
- **US1 (Phase 3)**: Depends on Phase 2 — creates the `case_ids` map that US2 consumes
- **US2 (Phase 4)**: Depends on US1 (needs `case_id_map` + `jira_assignment_map` from `_run_create_pass()`)
- **US3 (Phase 5)**: Depends on Phase 2 only — dry-run path exits before US1/US2 code runs
- **US4 (Phase 6)**: Depends on US1 + US2 + US3 being complete (wires `main()` and recovery logic)
- **Polish (Phase 7)**: Depends on all user story phases complete

### User Story Dependencies

- **US1 (P1)**: Starts after Phase 2 — no dependency on US2/US3/US4
- **US2 (P2)**: Starts after US1 — `jira_assignment_map` is produced by `_run_create_pass()`
- **US3 (P3)**: Starts after Phase 2 — entirely independent of US1/US2
- **US4 (P4)**: Starts after US1 + US2 + US3

### Within Each User Story

- Models/helpers before orchestrators
- `_build_case_payload()` (T011) before `_run_create_pass()` (T014)
- `_bulk_create_batch()` (T013) before `_run_create_pass()` (T014)
- `_fetch_existing_cases()` (T012) and `_bulk_create_batch()` (T013) can run in parallel [P]
- `_write_case_ids_to_state()` (T015) before `_run()` wiring (T016)

### Parallel Opportunities

- T003, T004 in Phase 2 can run in parallel (different parsing concerns)
- T007, T008 in Phase 2 can run in parallel (different map sources)
- T012, T013 in Phase 3 can run in parallel (different API calls, no dependency)
- T017, T018 in Phase 4 can run in parallel (preflight GET vs batch POST)
- T021, T022 can run in parallel (different functions)
- T025, T026, T027 in Phase 7 can all run in parallel (audit of different concerns)

---

## Parallel Example: User Story 1

```bash
# These Phase 2 tasks can be dispatched together:
Task T003: Implement _load_config() + _resolve_csv_path()
Task T004: Implement _parse_case_rows() + _parse_suite_rows_for_lookup()
Task T007: Implement _build_enum_map()
Task T008: Implement _build_cf_maps()

# After T003/T004/T005/T006 complete, these US1 tasks can run in parallel:
Task T012: Implement _fetch_existing_cases()
Task T013: Implement _bulk_create_batch()
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002–T010) — CRITICAL, blocks all stories
3. Complete Phase 3: User Story 1 (T011–T016)
4. **STOP and VALIDATE**: `_run()` creates 120 cases, writes state, exits with summary — no links yet
5. Proceed to US2 once US1 is confirmed working

### Incremental Delivery

1. T001 → T002–T010 → Foundation complete
2. T011–T016 → US1 complete → 120 cases in Qase, `case_ids` in state
3. T017–T020 → US2 complete → all 120 cases linked to Jira
4. T021–T022 → US3 complete → `--dry-run` works
5. T023–T024 → US4 complete → CLI entry point + recovery verified
6. T025–T028 → Polish complete → script is production-ready

### Reference Implementation

Use `scripts/suite_generator.py` as the architectural reference throughout:
- `_QaseAPIError` + `_qase_request()` — copy verbatim (T002)
- `_load_config()` + `_resolve_csv_path()` — copy and extend (T003)
- Module docstring structure — mirror (T027)
- `save_state()` atomic write pattern — reuse from `qase_seed_utils` (T015)

---

## Notes

- `[P]` tasks = independent logic units, safe to implement in parallel
- `[Story]` label provides full traceability from task → user story → acceptance scenario
- **Never** use `python` or `python3` directly — always `.venv/bin/python`
- **Never** call `pip install` — all dependencies already in `.venv/`
- Read `api-index.md` before implementing any API call; open only the mapped file
- Commit after each completed phase or logical group (T001, T002–T010, T011–T016, etc.)
- Run `scripts/case_generator.py --dry-run` as a sanity check after every Phase 2 task
