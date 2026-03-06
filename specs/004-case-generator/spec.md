# Feature Specification: Test Case Generator

**Feature Branch**: `004-case-generator`
**Created**: 2026-02-24
**Status**: Draft
**Input**: "Script 4: case_generator.py — CSV-driven test case creation for Qase. Reads config/workspace.yaml (cf_column_map, suite_domain_map, seed), state/workspace_state.json (project_code, suite_ids, custom_field_ids, custom_field_option_ids), and state/jira_state.json (story_ids, epic_ids). Parses CSV test case rows (skipping suite-only rows), translates string enum values to Qase API integers, parses multi-line steps, maps custom field columns to API field IDs and option IDs, maps CSV suite_ids to Qase suite IDs, assigns Jira stories via round-robin per domain, bulk-creates cases in batches of 30, links each case to its Jira story via Jira internal IDs, writes {csv_case_id: qase_case_id} into state/workspace_state.json, and supports --dry-run flag."

## Clarifications

### Session 2026-02-24

- Q: Which CSV column serves as the `csv_case_id` key in the `case_ids` map? → A: The `id` column value from the CSV row (integer string, as-is).
- Q: When is `case_ids` written to state — after creates only, or after both creates and Jira links succeed? → A: Written after all creates are confirmed, before the Jira link pass begins; link failures can be recovered without re-creating cases.
- Q: How should the Jira link pass handle cases that are already linked on a re-run? → A: GET existing links for the case before each link call; skip if any Jira link is already present (GET-before-POST idempotency).
- Q: What is the per-event log format during case creation? → A: One line per batch of 30 (e.g., `"Batch 1/4: 30 created"`); individual lines only for reused or errored cases. Final summary line always printed.
- Q: What anchors the round-robin story assignment order within a domain? → A: CSV row order within each domain (top-to-bottom through the file); produces a stable, auditable distribution tied to the source of truth.

---

## Assumptions

- All upstream scripts (scripts/workspace_init.py, jira_requirements.py, suite_generator.py) have run successfully and their outputs are present in `state/workspace_state.json` and `state/jira_state.json`.
- The CSV file (`assets/seed-data/QD-2026-02-18.csv`) contains exactly 120 test case rows and 31 suite-only rows; suite-only rows are identified by `suite_without_cases == "1"`.
- System-field enum values (priority, severity, status, behavior, layer, automation, is_flaky) will be queried from the Qase API at runtime rather than hardcoded, to respect any workspace-level customisation.
- Custom field option IDs are already stored in `state/workspace_state.json` by `scripts/workspace_init.py` and are used directly — no additional option-lookup calls are needed.
- Multi-line step fields in the CSV are newline-separated and each line may carry a numbered prefix (e.g., `"1. "`) that must be stripped before submission.
- Each top-level suite domain maps to one or more Jira epic slugs; story assignment within a domain uses a deterministic round-robin that advances in CSV row order (top-to-bottom), producing a stable distribution tied to the CSV source of truth.
- Rate-limit ceiling inherited from the project constitution: ≤ 5 API requests per second.

---

## User Scenarios & Testing

### User Story 1 - Seed all 120 test cases from CSV into Qase (Priority: P1)

As the automation lead,
I want to run a single script that reads the 120 test case rows from the CSV and creates them in the correct Qase suites with all fields, steps, and custom field values populated,
so that the Qase workspace contains the full test suite ready for run simulation.

**Why this priority**: All downstream scripts (run_simulator.py, defect_generator.py, maintenance.py) depend on the case IDs written by this script. Without it, no activity simulation is possible.

**Independent Test**: Run `case_generator.py` against a workspace where Scripts 1–3 have completed successfully. Verify that Qase shows exactly 120 cases distributed across the 30 suites, each with title, steps, priority, severity, and all 5 custom fields populated. Confirm `state/workspace_state.json` contains a `case_ids` map with 120 entries.

**Acceptance Scenarios**:

1. **Given** `state/workspace_state.json` has `project_code`, `suite_ids` (30 entries), `custom_field_ids`, and `custom_field_option_ids`, and `state/jira_state.json` has `story_ids` and `epic_ids`, **When** `case_generator.py` runs, **Then** exactly 120 test cases are created in Qase, each placed in the suite matching its CSV `suite_id`.
2. **Given** the script runs successfully, **When** `state/workspace_state.json` is inspected, **Then** it contains a `case_ids` object mapping every CSV case row identifier to its corresponding Qase case ID, with exactly 120 entries, all non-null.
3. **Given** a CSV row contains multi-line content in `steps_actions`, `steps_result`, or `steps_data`, **When** the script processes that row, **Then** each line is submitted as a separate step object with numbered prefixes stripped, and the steps appear in the correct order in Qase.
4. **Given** a CSV row has custom field values in `cf_6`–`cf_10`, **When** the script creates that case, **Then** every custom field value is translated to its corresponding option ID (stored as a string), and multiselect values are comma-joined into a single string.

---

### User Story 2 - Link every case to its Jira story (Priority: P2)

As the automation lead,
I want each created test case to be linked to the relevant Jira story using the Jira internal ID,
so that the workspace demonstrates traceability between Qase test cases and Jira requirements.

**Why this priority**: Jira traceability is a core feature of the living demo; without links the workspace fails its stated purpose, even if cases exist.

**Independent Test**: After a successful run, inspect a sample of Qase cases across different suites. For each case, verify that a Jira issue link is present and that the linked Jira issue key matches one of the stories assigned to that suite's domain.

**Acceptance Scenarios**:

1. **Given** a test case belongs to a suite in the `auth` domain, **When** the script assigns its Jira story, **Then** the case is linked to one of the Jira stories whose epic slug is `auth`, using that story's Jira internal ID (not display key).
2. **Given** multiple cases belong to the same suite domain, **When** Jira stories are assigned, **Then** the stories are distributed in round-robin order so that no single story holds all cases from that domain.
3. **Given** the script has created all cases, **When** it performs the Jira link step, **Then** every one of the 120 cases has exactly one Jira link attached, and no case is left unlinked.
4. **Given** a domain's story list contains only one story, **When** all cases in that domain are assigned, **Then** all cases link to that single story (round-robin of one is acceptable).

---

### User Story 3 - Support dry-run mode for safe inspection (Priority: P3)

As the automation lead,
I want to run the script with a `--dry-run` flag that shows the full distribution plan — cases per suite, enum translations, custom field mappings, and Jira story assignments — without making any API calls,
so that I can verify correctness before committing 120 creates to Qase.

**Why this priority**: Dry-run prevents irreversible bulk creation against the wrong project and lets the team audit the Jira round-robin and enum mappings before the first live run.

**Independent Test**: Run `case_generator.py --dry-run` and confirm: it exits with code 0, prints one line per case showing suite, title, Jira story key, and custom field values, makes no Qase or Jira API calls, and leaves `state/workspace_state.json` unchanged.

**Acceptance Scenarios**:

1. **Given** `--dry-run` is passed, **When** the script runs, **Then** it prints the planned distribution: for each case, the target suite name, case title, resolved custom field option IDs, and assigned Jira story key — without making any API calls.
2. **Given** `--dry-run` is passed, **When** the script exits, **Then** `state/workspace_state.json` is not modified and no Qase cases or Jira links are created.
3. **Given** `--dry-run` is passed, **When** the output is inspected, **Then** it includes a summary line showing total cases planned, total suites affected, and total unique Jira stories referenced.

---

### User Story 4 - Idempotent re-runs with no duplicate cases (Priority: P4)

As the automation lead,
I want re-running the script against a project that already has all 120 cases to complete without creating duplicates,
so that the script can be safely re-executed if interrupted or re-run for verification.

**Why this priority**: Idempotency prevents data pollution and is a constitution compliance requirement for all create operations.

**Independent Test**: Run `case_generator.py` twice in sequence. After the second run, confirm that Qase still contains exactly 120 cases (not 240), and `state/workspace_state.json` still maps the same 120 CSV IDs to the same Qase case IDs.

**Acceptance Scenarios**:

1. **Given** all 120 cases already exist in Qase, **When** `case_generator.py` runs again, **Then** it detects the existing cases by title and suite, reuses their IDs, creates no new cases, and the final line reads `"Cases complete: 0 created, 120 reused (total 120)"`.
2. **Given** the script detects existing cases, **When** it completes, **Then** `state/workspace_state.json` contains the same 120-entry `case_ids` map as after the initial run, with no values changed.
3. **Given** a partial run (e.g., 60 of 120 cases created before failure), **When** the script is re-run, **Then** it creates only the remaining 60 cases, producing a final `case_ids` map with all 120 entries.
4. **Given** all 120 cases exist and `case_ids` is already written but the Jira link pass failed mid-way, **When** the script is re-run, **Then** it skips all creates, GETs existing links per case, skips already-linked cases, and issues link calls only for cases not yet linked.

---

### Edge Cases

- What happens if `state/workspace_state.json` is missing or lacks `project_code`, `suite_ids`, `custom_field_ids`, or `custom_field_option_ids`? (Script exits with a descriptive error before any API call, naming the missing key.)
- What happens if `state/jira_state.json` is missing or lacks `story_ids` or `epic_ids`? (Script exits with a descriptive error before any API call.)
- What if a CSV case row references a `suite_id` not present in the state's `suite_ids` map? (Script exits with an error naming the unmapped suite ID before issuing any creates.)
- What if a suite's domain key in `suite_domain_map` has no matching epic slug in `state/jira_state.json`? (Script exits with a descriptive error identifying the unresolvable domain mapping.)
- What if a custom field value in the CSV cannot be mapped to any known option ID? (Script exits with an error identifying the row, field name, and unrecognised value.)
- What if the Qase bulk-create endpoint rejects a batch due to a validation error on one case? (Script logs the error with the batch range and exits without partial state writes; the operator must fix the data and re-run.)
- What if the Jira link pass fails mid-way (e.g., after linking 60 of 120 cases)? (Since `case_ids` was already written after the create pass, a re-run skips all creates. The link pass then GETs existing links per case and skips the 60 already linked, issuing calls only for the remaining 60.)
- What if an enum string value in the CSV (priority, severity, etc.) is not in the runtime-queried enum map? (Script exits with an error identifying the row, field name, and unrecognised value; it does not silently default.)
- What if the Qase API returns a rate-limit or transient error? (Script retries with exponential backoff, up to 3 retries with a 30-second total cap per request, then propagates the error.)
- What if `is_flaky` in the CSV is `"yes"` or `"no"` rather than `1` or `0`? (Script converts via the enum map to integer `1` or `0` before sending; boolean `True`/`False` is never submitted.)
- What if `--csv` is not provided and `config/workspace.yaml` does not define `seed.cases_csv`? (Script exits with a clear configuration error before reading any file.)

---

## Requirements

### Functional Requirements

- **FR-001**: The script MUST accept an optional `--csv` CLI argument specifying the path to the CSV file; if omitted, it MUST fall back to the path defined in `config/workspace.yaml` under `seed.cases_csv`. It MUST exit with a descriptive error if neither source is available.
- **FR-002**: The script MUST read `state/workspace_state.json` to obtain `project_code`, `suite_ids`, and `custom_fields` (a map of CF name → `{id, options}`). It MUST exit with a descriptive error if the file is missing, if `project_code` or `suite_ids` are absent, or if any CF named in `config/workspace.yaml`'s `cf_column_map` is missing its `options` sub-key. The `options` sub-key is written by `scripts/workspace_init.py` (spec 001) and MUST be present before this script runs. (The original spec input referenced `custom_field_ids`/`custom_field_option_ids` as flat keys; the actual schema uses `custom_fields.{name}.{id, options}` per plan.md D-01.)
- **FR-003**: The script MUST read `state/jira_state.json` to obtain `stories` (a map of slug → `{jira_key, jira_id, epic_slug, summary}`) and `epics` (a map of slug → `{jira_key, jira_id}`). It MUST exit with a descriptive error if the file is missing or the `stories` key is absent or empty. (The original spec input referenced flat `story_ids`/`epic_ids` keys; the actual schema uses nested `stories`/`epics` objects per plan.md D-02.)
- **FR-004**: The script MUST filter the CSV to test case rows only, identified by `suite_without_cases != "1"`. It MUST process all 120 case rows and skip the 31 suite-only rows.
- **FR-005**: Before creating any cases, the script MUST query the Qase API to retrieve the current integer values for system-field enums (priority, severity, status, behavior, layer, automation) and build a runtime enum map. It MUST NOT hardcode integer values for these fields.
- **FR-006**: The script MUST translate each CSV row's string enum values (priority, severity, status, behavior, layer, automation, is_flaky) to API integers using the runtime enum map. It MUST exit with a descriptive error identifying the row, field name, and unrecognised value if any translation fails.
- **FR-007**: The script MUST parse multi-line step content from `steps_actions`, `steps_result`, and `steps_data` CSV columns by splitting on newline and stripping any leading numbered prefix (e.g., `"1. "`, `"2. "`). Each resulting line MUST be submitted as a separate step object, preserving order.
- **FR-008**: The script MUST translate each CSV `cf_6`–`cf_10` value to its corresponding custom field ID and option ID using the mappings in `config/workspace.yaml` (`cf_column_map`) and `state/workspace_state.json` (`custom_field_ids`, `custom_field_option_ids`). Custom field values MUST be stored as strings. Multiselect field (cf_10) values MUST be comma-joined option IDs in a single string.
- **FR-009**: The script MUST map each CSV case row's `suite_id` to the corresponding Qase suite ID using `suite_ids` from state. It MUST exit with an error naming any unmapped suite ID before issuing any creates.
- **FR-010**: The script MUST assign a Jira story to each case by: (a) looking up the case's suite name in `suite_domain_map` from `config/workspace.yaml` to get the epic slug, (b) resolving the epic slug to an ordered list of stories by filtering `jira_state["stories"]` where `epic_slug` matches (per plan.md D-02), and (c) selecting a story using a round-robin cursor that advances in CSV row order (top-to-bottom) within each domain — so the first case row in a domain gets story[0], the second gets story[1], and so on, wrapping when the list is exhausted. The Jira issue key (`jira_key` field, e.g. `"AF-7"`) MUST be used for the link call — NOT the numeric internal ID (`jira_id`). Empirically verified during production run: the Qase API returns HTTP 400 "format is invalid" for numeric internal IDs; only the display key is accepted. The `jira_key` is also used for dry-run output (FR-017).
- **FR-011**: The script MUST bulk-create cases in batches of no more than 30 per request using the Qase bulk case creation endpoint.
- **FR-012**: After all 120 cases are created and `case_ids` has been written to state (FR-014), the script MUST link each case to its assigned Jira story using the Jira internal ID. Before issuing any link call, the script MUST GET the existing external links for that case; if a Jira link is already present, it MUST skip the link call. This GET-before-POST pattern ensures the link pass is fully idempotent on re-run.
- **FR-013**: At the start of the create pass, the script MUST perform a bulk GET of all existing cases in the project and build an in-memory map of `(title, suite_id) → qase_case_id`. Before creating any case, it MUST check this map; if a match is found, it MUST reuse the existing case ID and skip the create call.
- **FR-014**: Once all 120 cases are created or confirmed reused, the script MUST immediately write the accumulated `{csv_id_value: qase_case_id}` mapping into the `case_ids` key of `state/workspace_state.json` — before beginning the Jira link pass. The write MUST be atomic (write to a temp file, then rename) and MUST preserve all existing keys in the state file. This ordering ensures that a Jira link failure can be recovered without re-running case creation.
- **FR-015**: The script MUST enforce a global API rate limit of no more than 5 requests per second across all Qase and Jira API calls.
- **FR-016**: The script MUST implement retry with exponential backoff for transient API failures (rate-limit responses, network timeouts), with a maximum of 3 retries and a 30-second total cap per request.
- **FR-017**: The script MUST include a `--dry-run` flag that prints the full planned distribution (case title, target suite name, resolved custom field option IDs, assigned Jira story key) for all 120 cases, followed by a summary line, without making any API calls or modifying `state/workspace_state.json`.
- **FR-018**: During the create pass, the script MUST print one log line per batch in the form `"Batch K/T: N created"` (where K is the current batch number and T is the total batch count). Individual log lines MUST be printed only for reused cases (format: `"REUSE case {csv_id}: '{title}' → qase_id={N}"`) and for errored cases (format: `"ERROR batch K: {reason}"`). The Jira link pass MUST similarly log one line per batch: `"Links batch K/T: N linked, M skipped"`. On successful completion the script MUST print a final summary line in the form `"Cases complete: N created, M reused (total 120)"`.
- **FR-019**: The `is_flaky` field MUST be submitted as integer `0` or `1`; boolean values MUST NOT be sent.

### Key Entities

- **CaseRow**: A row from `assets/seed-data/QD-2026-02-18.csv` where `suite_without_cases != "1"`. Key fields: `id` column value (used as `csv_case_id` — integer string, non-null for all 120 case rows), `title`, `suite_id`, `priority`, `severity`, `status`, `behavior`, `layer`, `automation`, `is_flaky`, `steps_actions`, `steps_result`, `steps_data`, `cf_6`–`cf_10`.
- **QaseCase**: The case object created in (or fetched from) Qase. Key attributes: Qase integer case ID, title, suite ID, system-field integer values, step objects, custom field value objects.
- **CaseIDMap**: The `{csv_case_id: qase_case_id}` dictionary held in memory during the run and persisted to `state/workspace_state.json` under the `case_ids` key.
- **EnumMap**: A runtime-built map of system field names to `{string_value: integer}` dictionaries, populated by querying the Qase API before any case processing.
- **CustomFieldValueSet**: The set of custom field ID + option ID pairs (as strings) derived from a single CSV row's `cf_6`–`cf_10` values via the `cf_column_map` and state option ID lookups.
- **JiraStoryAssignment**: The mapping of a case to its Jira story, derived from the suite's domain slug and the round-robin cursor for that domain. Stores both the Jira display key and Jira internal ID.
- **WorkspaceState**: The JSON file at `state/workspace_state.json`. Read for `project_code`, `suite_ids`, `custom_field_ids`, `custom_field_option_ids`; updated with `case_ids` after successful completion.
- **JiraState**: The JSON file at `state/jira_state.json`. Read for `story_ids` and `epic_ids`; never written by this script.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: A clean run against a project where Scripts 1–3 have completed creates exactly 120 test cases across 30 suites within 5 minutes (excluding API latency), and the final output line reads `"Cases complete: 120 created, 0 reused (total 120)"`.
- **SC-002**: Every created case has all 5 custom fields populated with non-null, correctly mapped option IDs (stored as strings), and no case is missing a step object if the source CSV row contained step content.
- **SC-003**: Every created case has exactly one Jira story link using the Jira internal ID; no case is unlinked and no case has more than one link.
- **SC-004**: Re-running the script against a project that already has all 120 cases completes without creating duplicates, and `state/workspace_state.json` retains the same `case_ids` map, with the final line reading `"Cases complete: 0 created, 120 reused (total 120)"`.
- **SC-005**: `state/workspace_state.json` is updated with a `case_ids` map containing exactly 120 entries, all non-null integers, and all pre-existing keys (project_code, suite_ids, custom_field_ids, etc.) are preserved intact.
- **SC-006**: The `--dry-run` mode prints all 120 planned cases with suite name, title, custom field values, and Jira story key, followed by a summary line, and exits in under 10 seconds with no API calls made and no state file changes.
- **SC-007**: If the script is interrupted after partial case creation and re-run, it creates only the remaining cases, resulting in a complete 120-entry `case_ids` map with no duplicates.
