# Feature Specification: Suite Generator

**Feature Branch**: `003-suite-generator`
**Created**: 2026-02-20
**Status**: Draft
**Input**: "Script 3: suite_generator.py - CSV-driven Qase suite creation, reads suite rows from the shared CSV, creates parent suites before children using a two-pass topological approach, and persists the csv_suite_id → qase_suite_id mapping back into state/workspace_state.json."

## Clarifications

### Session 2026-02-20

- Q: How should the script locate the CSV file? → A: Accept as a `--csv` CLI argument with fallback to `config/workspace.yaml` `seed.cases_csv` key.
- Q: What should the retry ceiling be for transient API failures? → A: 3 retries maximum with a 30-second total cap per request.
- Q: How should the script enumerate existing suites for the idempotency check? → A: Single bulk GET of all existing suites at script start; match by title and parent in memory.
- Q: What should the script output on successful completion? → A: Per-event log lines (one per suite create/reuse) plus a final summary line showing created and reused counts.
- Analysis I1: FR-004 map key corrected from `(title, parent_qase_id)` to `title` alone — Qase `GET /suite/{code}` does not return `parent_id`; title uniqueness across all 30 ShopEase suites makes this safe.
- Analysis I2: SC-001 summary format aligned to FR-011 exact string `"Suites complete: N created, M reused (total 30)"`.

## User Scenarios & Testing

### User Story 1 - Build the Qase suite hierarchy from the CSV (Priority: P1)

As the automation lead,
I want to run a script that reads the suite-only rows from the configured CSV file and creates the full 7-parent / 23-child suite hierarchy in Qase,
so that the correct folder structure is in place before any test cases are seeded.

**Why this priority**: The suite tree must exist before `case_generator.py` runs; without it, every case would be created at the root level and the entire downstream workflow would break.

**Independent Test**: Run `suite_generator.py --dry-run` against a workspace that already has `state/workspace_state.json` populated by `scripts/workspace_init.py`. Verify that the console output lists exactly 7 parent suites followed by 23 child suites in the correct creation order. Then run without `--dry-run` and confirm that Qase reflects the expected hierarchy and that `state/workspace_state.json` contains a `suite_ids` map with 30 entries.

**Acceptance Scenarios**:

1. **Given** `state/workspace_state.json` exists with a valid `project_code` and the CSV file (from `--csv` or `config/workspace.yaml seed.cases_csv`) is present, **When** `suite_generator.py` runs, **Then** it creates 7 top-level suites and 23 child suites in Qase, all named exactly as specified in the CSV.
2. **Given** the script runs successfully, **When** `state/workspace_state.json` is inspected, **Then** it contains a `suite_ids` object mapping every CSV `suite_id` value to its corresponding Qase suite ID.
3. **Given** a child suite's parent has not yet been created, **When** the script processes that row, **Then** it defers creation of the child until the parent's Qase ID is known, never attempting a create with a missing `parent_id`.
4. **Given** the script is run a second time, **When** it checks Qase for existing suites by name under the project, **Then** it reuses already-created suites rather than creating duplicates, and the final `suite_ids` map still contains all 30 entries.

---

### User Story 2 - Persist the suite ID mapping for downstream scripts (Priority: P2)

As the automation lead,
I want the script to write the `csv_suite_id → qase_suite_id` mapping into `state/workspace_state.json`,
so that `case_generator.py` can resolve the correct Qase suite ID for each test case without any hardcoded values.

**Why this priority**: `case_generator.py` relies entirely on this mapping; if it is missing or incomplete, case creation fails for every row in the CSV.

**Independent Test**: After a successful run, inspect `state/workspace_state.json` and confirm that `suite_ids` contains exactly 30 keys (one per CSV `suite_id`), each mapping to a non-null integer Qase suite ID.

**Acceptance Scenarios**:

1. **Given** the script creates all 30 suites, **When** it writes state, **Then** `suite_ids` in `state/workspace_state.json` maps every CSV `suite_id` to a Qase integer ID and no entry is null.
2. **Given** the state file already contains keys for `project_code`, `custom_field_ids`, and `milestone_ids` from prior steps, **When** the script writes `suite_ids`, **Then** those existing keys are preserved and only `suite_ids` is added or updated.
3. **Given** a partial run that fails mid-way (e.g., network error after 5 suites), **When** the script is re-run, **Then** it resumes from the first un-created suite (idempotent re-entry) and the final state contains all 30 mappings.

---

### User Story 3 - Support dry-run mode for safe pre-flight inspection (Priority: P3)

As the automation lead,
I want to run the script with a `--dry-run` flag that lists all planned suite creations in order without making any API calls,
so I can verify the creation plan before committing to Qase changes.

**Why this priority**: Dry-run prevents accidental suite creation in a wrong project and lets the team review the two-pass ordering before the first real run.

**Independent Test**: Run `suite_generator.py --dry-run` and confirm it exits with code 0, prints all 30 suite names in parent-before-child order, and shows no Qase API calls in the network logs.

**Acceptance Scenarios**:

1. **Given** `--dry-run` is passed, **When** the script runs, **Then** it prints the ordered list of suites (pass 1 parents, then pass 2 children) with their intended `parent_id` references and exits without making any API calls.
2. **Given** `--dry-run` is passed, **When** the script exits, **Then** `state/workspace_state.json` is not modified.

---

### Edge Cases

- What happens if the resolved CSV file contains no rows where `suite_without_cases == "1"`? (Script exits immediately with a descriptive error; no Qase calls are made.)
- What if neither `--csv` is provided nor `seed.cases_csv` is defined in `config/workspace.yaml`? (Script exits with a clear configuration error before any file read or API call.)
- What if `state/workspace_state.json` is missing or does not contain `project_code`? (Script exits with a clear error before any API call.)
- What if a child suite's `suite_parent_id` value refers to a CSV `suite_id` that was never created? (Detected before API calls begin; script exits with an error naming the orphaned row.)
- What if Qase returns a rate-limit or transient error during suite creation? (Script retries with backoff, honouring the ≤5 req/sec global limit, and reports failure only after exhausting retries.)
- What if the project identified by `project_code` is not accessible with the current API token? (Script detects a 403/404 on the first API call and exits with a clear authentication/permission error without modifying state.)

## Requirements

### Functional Requirements

- **FR-001**: The script MUST accept an optional `--csv` CLI argument specifying the path to the CSV file; if omitted, it MUST fall back to the path defined in `config/workspace.yaml` under `seed.cases_csv`. It MUST extract only the rows where `suite_without_cases` equals `"1"` as the authoritative list of suites to create.
- **FR-002**: The script MUST perform suite creation in two passes: Pass 1 creates rows with no `suite_parent_id` (7 top-level suites); Pass 2 creates rows whose `suite_parent_id` refers to a suite created in Pass 1.
- **FR-003**: The script MUST resolve `parent_id` values at creation time using the in-memory mapping built from already-created suites; it MUST NOT hardcode any Qase suite IDs.
- **FR-004**: At script start, the script MUST perform a bulk `GET` of all existing suites in the project (paginated if needed) and build an in-memory map of `title → qase_suite_id`. Before creating any suite, it MUST check this map by title; if a match is found, it MUST reuse that suite's ID rather than issuing a `POST`. Note: the Qase `GET /suite/{code}` response does not include `parent_id`, so title alone is used as the deduplication key. This is safe because all 30 ShopEase suite titles are globally unique within the project (see `research.md` F-02).
- **FR-005**: The script MUST read `state/workspace_state.json` to obtain the `project_code` and MUST exit with a descriptive error if the file is missing or `project_code` is absent.
- **FR-006**: The script MUST write the accumulated `{csv_suite_id: qase_suite_id}` mapping into the `suite_ids` key of `state/workspace_state.json` only after all 30 suites are confirmed created or reused, using an atomic write (write to a temp file, then rename).
- **FR-007**: The script MUST preserve all existing keys in `state/workspace_state.json` when updating the file; it MUST only add or overwrite the `suite_ids` key.
- **FR-008**: The script MUST validate before any API calls that all `suite_parent_id` values in Pass 2 rows reference a `suite_id` present in Pass 1; if any orphaned reference is found, it MUST exit with a descriptive error.
- **FR-009**: The script MUST enforce a global API rate limit of no more than 5 requests per second.
- **FR-010**: The script MUST include a `--dry-run` flag that prints the full ordered creation plan (suite name, intended parent reference) without making any API calls or modifying `state/workspace_state.json`.
- **FR-011**: The script MUST log each suite creation or reuse event with its CSV `suite_id`, Qase suite ID, and title. On successful completion it MUST print a final summary line in the form `"Suites complete: N created, M reused (total 30)"`.
- **FR-012**: The script MUST implement retry with exponential backoff for transient API failures (e.g., rate-limit responses, network timeouts), with a maximum of 3 retries and a 30-second total cap per request, before propagating an error.

### Key Entities

- **SuiteRow**: A row from `assets/seed-data/QD-2026-02-18.csv` where `suite_without_cases == "1"`. Key fields: `suite_id`, `suite_parent_id`, `suite` (display title).
- **QaseSuite**: The suite object created in (or fetched from) Qase. Key attributes: Qase integer ID, title, parent suite ID.
- **SuiteIDMap**: The `{csv_suite_id: qase_suite_id}` dictionary held in memory during the run and persisted to `state/workspace_state.json` under the `suite_ids` key.
- **WorkspaceState**: The JSON file at `state/workspace_state.json`. Read for `project_code`; updated with `suite_ids` after successful completion.

## Success Criteria

### Measurable Outcomes

- **SC-001**: A clean run against a fresh Qase project creates exactly 30 suites (7 top-level, 23 children) in the correct parent-child hierarchy within 60 seconds (excluding API latency), and the final output line reads exactly `"Suites complete: 30 created, 0 reused (total 30)"`.
- **SC-002**: Re-running the script against a project that already has all 30 suites completes without creating any duplicates, and `state/workspace_state.json` contains the same 30-entry `suite_ids` map as after the initial run.
- **SC-003**: `state/workspace_state.json` is updated with a `suite_ids` map containing exactly 30 entries, all non-null, and all other pre-existing keys are preserved intact.
- **SC-004**: The `--dry-run` mode outputs all 30 suite names in parent-before-child order with no API calls made, completing in under 5 seconds.
- **SC-005**: If the script is interrupted and re-run, it resumes idempotently, making only the API calls needed to create the remaining suites, with no duplicates and a complete final `suite_ids` map.
