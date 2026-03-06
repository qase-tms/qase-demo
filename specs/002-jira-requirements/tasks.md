# Feature Tasks: Jira Requirement Provisioning

## Phase 1: Setup & Tooling

- [X] T001 Initialize `scripts/jira_requirements.py` with CLI argument parsing, interactive credential prompts, and `--dry-run` support.
- [X] T002 Extend `scripts/qase_seed_utils.py` with reusable `load_state(path)` / `save_state(path, data)` helpers so scripts read/write `state/*.json` atomically.
- [X] T003 Wire the script into `quickstart.md` instructions, documenting dependency installation (`requests`, `PyYAML`) and execution steps.

## Phase 2: Foundational Tasks

- [X] T004 Parse `config/workspace.yaml` (project name + description) and `config/seeds/jira-requirements.seed.yaml` (epics/stories) inside `scripts/jira_requirements.py`, validating slug uniqueness before touching Jira.
- [X] T005 Implement credential acquisition: prompt interactively when no env/CLI values exist, honor `--email`/`--token` overrides, and fall back to `JIRA_EMAIL`/`JIRA_API_TOKEN`, logging each source.
- [X] T006 Add rate limiting/exponential backoff helpers around Jira requests to enforce the constitution’s ≤5 requests/sec rule.
- [X] T007 Configure structured logging of milestones (credential receipt, project selection, issue counts, mapping file path) and ensure HTTP errors abort before persisting state.

## Phase 3 – User Story 1 (P1): Provision Jira artifacts

- [X] T008 [US1] Implement `JiraProject` creation: query `/rest/api/3/project/search`, detect duplicates, append ` (n)` names, and create/reuse the project while capturing `id`/`key`.
- [X] T009 [US1] Bulk-create epics via `/rest/api/3/issue/bulk`, supplying the Epic Name field and capturing slug → Jira key order.
- [X] T010 [US1] Bulk-create stories in a second `/rest/api/3/issue/bulk` call, linking each story to its epic (Epic Link or parent) and validating the response before continuing.
- [X] T011 [US1] After each bulk request, compare the number of returned issues with the requested updates and fail fast (log the Jira response) if Jira reports fewer creations so `state/jira_state.json` stays untouched.
- [X] T012 [US1] Build `SeedMapping`: once the epics/stories calls succeed, write slug → `{jira_key, jira_id, issue_type}` for every epic/story to `state/jira_state.json` via atomic temp-file writes.

## Phase 4 – User Story 2 (P2): Keep duplicate-handling predictable

- [X] T013 [US2] Factor out `select_project_key(existing_keys)` helper that mirrors `scripts/workspace_init.py` (first unused two-letter code) and log when duplicates require a suffix.
- [X] T014 [US2] Add validation that the script refuses to reuse a project name without suffixing when an existing project is detected, then document the strategy in `research.md`.
- [X] T015 [US2] Create lightweight smoke tests (scripts under `scripts/` or pytest) supplying simulated `existing_keys` arrays to prove deterministic suffixing.

## Phase 5 – User Story 3 (P3): Persist mapping for downstream automation

- [X] T016 [US3] Build a mapping builder that merges epic/story slugs into one structure, references `data-model.md`’s `SeedMapping`, and namespaces story slugs (e.g., `auth-reset`) to avoid collisions.
- [X] T017 [US3] Ensure `state/jira_state.json` is only overwritten after successful Jira calls; leave the previous file untouched during retries and log rollback hints when partial failures occur.
- [X] T018 [US3] Document mapping consumption in `contracts/jira-requirements-api.md` so downstream scripts know how to read `jira_state.json` and expect slug-based keys.

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T019 Polish logging/errors: surface guidance for invalid credentials, duplicate slugs, and API failures; ensure quickstart references these error cases.
- [X] T020 Update `.cursor/rules/` context to mention the Jira provisioning workflow and mapping file so agents stay synchronized.
- [X] T021 Review `state/jira_state.json` format and add inline documentation notes so future scripts know how to consume it safely.

## Dependencies & Execution Order

1. Phase 1 → Phase 2 (setup precedes foundational helpers)  
2. Phase 2 → User Story 1 (project + issue creation depends on parsed config/credentials)  
3. User Story 1 → User Story 2 (project creation must exist before deterministic key helpers)  
4. User Story 1/2 → User Story 3 (mapping persistence runs after epics/stories exist)  
5. Final polish tasks can run in parallel once each storyline has delivered its artefact.

## Parallel Execution Opportunities

- Phase 1/T002 (state helpers) and Phase 2/T004 (seed parsing) can proceed concurrently because they touch different modules before Jira calls begin.  
- Within Phase 5, T016 and T018 can run in parallel: the mapping builder and documentation improvements don't block each other as long as the final write waits for T011’s success.

## Implementation Strategy

Follow the MVP-first approach: fully complete User Story 1 (provisioning) before adding deterministic key helpers (US2) and mapping persistence safeguards (US3). Keep changes incremental, rely on `scripts/jira_requirements.py --dry-run` for validation, and only then finalize logging/tests/documentation.
# Feature Tasks: Jira Requirement Provisioning

## Phase 1: Setup & Tooling

- [X] T001 Initialize `scripts/jira_requirements.py` with CLI argument parsing, interactive credential prompts, and `--dry-run` support based on the plan summary path format.
- [X] T002 Extend `scripts/qase_seed_utils.py` with reusable `load_state(path)` / `save_state(path, data)` helpers so any script can read/write `state/*.json` atomically.
- [X] T003 Wire the script into `quickstart.md` instructions, documenting dependency installation (`requests`, `PyYAML`) and execution steps.

## Phase 2: Foundational Tasks

- [X] T004 Parse `config/workspace.yaml` (project name + description fallback) and `config/seeds/jira-requirements.seed.yaml` (epics/stories) inside `scripts/jira_requirements.py`, validating slug uniqueness before reaching Jira.
- [X] T005 Implement credential acquisition (env vars `JIRA_EMAIL`/`JIRA_API_TOKEN` + CLI `--email`/`--token` overrides) and Jira base URL validation with clear logging.
- [X] T006 Add rate limiting/helper logic (≤5 requests/sec) plus exponential-backoff retry wrappers around `requests` to satisfy the constitution’s throttling rule.
- [X] T007 Configure structured logging of milestones (credential receipt, project selection, issue counts, mapping file path) and ensure HTTP errors abort before persisting state.

## Phase 3 – User Story 1 (P1): Provision Jira artifacts from the seed file

- [X] T008 [US1] Implement `JiraProject` creation: query `/rest/api/3/project/search`, detect duplicates, append ` (n)` names, and create/reuse the project while capturing `id`/`key` inside `scripts/jira_requirements.py`.
- [X] T009 [US1] Bulk-create epics via `/rest/api/3/issue/bulk`, inserting the required Epic Name field (discovered via createmeta) and storing slug → Jira key order.
- [X] T010 [US1] Bulk-create stories in a second `/rest/api/3/issue/bulk` call, linking each story to its epic (Epic Link or parent) and validating the response before proceeding.
- [X] T011 [US1] Build `SeedMapping` output: after both bulk calls succeed, write slug → `{jira_key, jira_id, issue_type}` for every epic and story to `state/jira_state.json` using atomic temp file writes.

## Phase 4 – User Story 2 (P2): Keep duplicate-handling predictable

- [X] T012 [US2] Factor out `select_project_key(existing_keys)` helper that mirrors `scripts/workspace_init.py` (first unused two-letter code) and include detailed logging when duplicates are detected.
- [X] T013 [US2] Add validation that the script refuses to reuse a project name without suffixing when an active project already exists, documenting the decision in `research.md`.
- [X] T014 [US2] Create lightweight smoke checks (can be local Python unit tests or scripts under `scripts/`) that feed fake `existing_keys` arrays to `select_project_key` to prove deterministic suffixing.

## Phase 5 – User Story 3 (P3): Persist mapping for downstream automation

- [X] T015 [US3] Build a mapping builder that merges epic and story slugs into a single structure, references `data-model.md`’s `SeedMapping`, and keeps story slugs namespaced (e.g., `auth-reset`) to avoid collisions.
- [X] T016 [US3] Ensure `state/jira_state.json` is only overwritten after all Jira calls succeed; keep the previous file intact during retries and add rollback logging in case of partial failure.
- [X] T017 [US3] Document mapping usage in `contracts/jira-requirements-api.md` so downstream scripts know how to read `jira_state.json`, linking back to the seed slug expectations.

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T018 Polish logging/errors: add user-facing error guidance (invalid credentials, duplicate slugs, API failures) and ensure the quickstart references the new error cases.
- [X] T019 Update `.cursor/rules` context (already touched by the agent update) to mention the new Jira provisioning workflow and mapping file so agents stay in sync.
- [X] T020 Review `state/jira_state.json` format and add inline comments in documentation to ensure future scripts know how to consume it.

## Dependencies & Execution Order

1. Phase 1 → Phase 2 (setup precedes foundational helpers)
2. Phase 2 → User Story 1 (project + issue creation depends on parsed config/credentials)
3. User Story 1 → User Story 2 (mapping logic builds on the created project; deterministic key selection plugs into creation helper)
4. User Story 1/2 → User Story 3 (mapping persistence runs after epics/stories exist)
5. Final polish tasks can run in parallel once each storyline has delivered its artefact.

## Parallel Execution Opportunities

- Phase 1/T002 (state helpers) and Phase 2/T004 (seed parsing) can be worked on concurrently because they touch different helpers before Jira calls begin.
- Within Phase 5, T015 and T017 can run in parallel: mapping builder and documentation updates do not depend on each other as long as final writing waits for T011’s success.

## Implementation Strategy

Follow the MVP-first approach: complete User Story 1 (provisioning) fully before adding deterministic key helpers (US2) and mapping persistence safeguards (US3). Keep tasks small and verify via local dry runs (`scripts/jira_requirements.py --dry-run`). Once the core script works, incrementally add logging/tests and finalize documentation.
