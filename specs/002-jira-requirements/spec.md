# Feature Specification: Jira Requirement Provisioning

**Feature Branch**: `002-jira-requirements`  
**Created**: 2026-02-19  
**Status**: Draft  
**Input**: "Create a script that provisions Jira artifacts (project, epics, and stories) from `config/seeds/jira-requirements.seed.yaml`, handles duplicate project names, prompts for Jira email/API token today, but can later accept GitHub Actions workflow inputs, and writes a mapping file for downstream Qase linking."

## Clarifications

### Session 2026-02-19

- Q: What strategy should we use to generate Jira project keys when the base name already exists? → A: Match `scripts/workspace_init.py` and pick the first unused two-letter alphabetic code so duplicate projects stay predictable while keeping the key compact.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Provision Jira artifacts from the seed file (Priority: P1)

As the automation lead,  
I want to run a script that reads `config/seeds/jira-requirements.seed.yaml`, creates or reuses a Jira project, and bulk-creates all epics and user stories with the correct parent-child relationships,  
so that every Jira requirement is available for linking later without manual work.

**Why this priority**: This script unlocks the entire Jira → Qase linkage workflow; nothing down the line can run until the Jira requirements exist.

**Independent Test**: Run the script with a clean Jira workspace, provide interactive credentials, and validate that Jira reports exactly the epics and stories defined in `config/seeds/jira-requirements.seed.yaml`. Confirm the command exits normally, prints the created issue counts, and drops the mapping file under `state/jira_state.json`.

**Acceptance Scenarios**:
1. **Given** no Jira project exists with the intended name, **When** the script runs, **Then** it provisions a new project and creates all epics and stories from the seed without manual steps, logging each creation.
2. **Given** a Jira project already exists with that name, **When** the script runs, **Then** it creates a new project whose name includes a sequential suffix (e.g., `ShopEase Requirements (2)`), logs the suffix strategy, and still creates every issue from the seed.
3. **Given** the seed references a story, **When** issue creation completes, **Then** each story maps back to its epic slug and the final mapping file contains every slug → (key, id, issue type) tuple.

---

### User Story 2 - Keep duplicate-handling predictable (Priority: P2)

As the automation lead,  
I want the script to reuse the same duplicate-handling strategy that `scripts/workspace_init.py` uses (name checking plus suffixing) so that reruns never overwrite the previous Jira project inadvertently,  
so I can re-seed Jira multiple times while keeping every project isolated.

**Why this priority**: Without deterministic duplicate handling, rerunning the script could destroy prior work or confuse stakeholders about which project is authoritative.

**Independent Test**: Execute the script twice using the same credentials and observe that the second run appends an incremented suffix to the project name while leaving the first project intact.

**Acceptance Scenarios**:
1. **Given** a prior project with the base name exists, **When** the script inspects Jira projects, **Then** it reports the existing name, calculates the next suffix, and ensures the new project uses that suffixed name.
2. **Given** many projects already exist with the suffix pattern, **When** suffix generation runs, **Then** it picks the next unused integer and uses it consistently for both the project name and the derived key (if necessary).

---

### User Story 3 - Persist mapping for downstream automation (Priority: P3)

As the automation lead,  
I want the script to record every epic and story slug alongside its Jira key, internal ID, and issue type,  
so later steps (CSV case seeding, Qase linking) can reference the exact Jira issues without re-calling the API.

**Why this priority**: Mapping accuracy is critical for linking Qase cases to the right Jira stories; missing entries would break the next milestone.

**Independent Test**: After a successful run, inspect `state/jira_state.json` and confirm it lists each slug, Jira key, Jira ID, and issue type for both epics and stories exactly once.

**Acceptance Scenarios**:
1. **Given** the seed lists `auth` as an epic slug, **When** the script finishes, **Then** the mapping contains `auth` → `{key, id, issue_type:"Epic"}`.
2. **Given** a story slug appears twice (should be unique), **When** the script runs, **Then** it flags the duplication before calling Jira and exits with an error.
3. **Given** partial failure occurs (e.g., story creation fails after epics), **When** the script exits, **Then** no incomplete mapping is written and the console clearly explains which stage failed.

---

### Edge Cases

- What happens if Jira returns a partial success when bulk-creating issues? (Fail fast, log the API response, and do not write the mapping.)
- How are missing epic slugs handled inside the seed? (Detect before issuing API requests and stop with a descriptive error.)
- What if the user cancels credential input or the provided token/ email fail authentication? (Propagate the HTTP error, keep the state unchanged, and exit non-zero.)
- What if Jira throttles us? (Honor ≤5 req/sec throttling and retry with exponential backoff before failing.)
- How does the script behave if `state/jira_state.json` already exists? (Overwrite only after a successful run; keep it untouched during retries.)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The script MUST treat `config/seeds/jira-requirements.seed.yaml` as the single source of truth for epics and stories, leaving the file untouched, and read every summary, description, label, and slug directly from it.
- **FR-002**: The script MUST prompt interactively for the Jira email and API token today but also accept them via optional `--email`/`--token` CLI flags or `JIRA_EMAIL`/`JIRA_API_TOKEN` environment variables so future GitHub Actions workflows can inject credentials.
- **FR-003**: The script MUST read `config/workspace.yaml` and default to `project.name`/`project.description` for the Jira project metadata, with a fallback name such as "ShopEase Requirements" if those keys are missing.
- **FR-004**: The script MUST query `/rest/api/3/project/search` to enumerate existing projects, compare each name case-insensitively to the desired base name, and, when duplicates exist, append ` (2)`, ` (3)`, … to the new project’s name (matching the `scripts/workspace_init.py` suffix logic) while picking the first unused two-letter alphabetic code for the project key so that both name and key stay predictable.
- **FR-005**: After selecting the final project name/key, the script MUST create the Jira project with a known type and template or reuse an existing project if the computed name already exists, then capture the resulting project ID and key in memory for the issue creation step.
- **FR-006**: The script MUST create epics first, collect their slugs, and then create stories in a second bulk request, always linking each story to the correct epic by slug; missing slugs must trigger a validation error before any Jira API call.
- **FR-007**: The script MUST persist slug → `{jira_key, jira_id, issue_type}` mappings to `state/jira_state.json` exactly once per slug and only after all API calls succeed, writing via a temporary file to preserve consistency.
- **FR-008**: The script MUST log key milestones (credential receipt, selected project name/key, number of epics/stories created, mapping summary) and exit immediately on any Jira API error without mutating `state/jira_state.json`.
- **FR-009**: The script MUST encapsulate its behaviors into modular components (project selection/creation, issue builder, mapping writer) so automation-focused callers can reuse each module if needed.
- **FR-010**: The script MUST obey a global throttle of 5 Jira requests per second and retry transient failures with exponential backoff, matching the rate-limit philosophy used elsewhere in the workspace foundation scripts.

### Key Entities *(include if feature involves data)*

- **JiraProject**: The newly created or deduplicated Jira project (name, key, ID, type); used for every issue creation call.
- **JiraEpic**: Each epic from `config/seeds/jira-requirements.seed.yaml` (slug, summary, description, labels); requires the Jira key/ID for linking later.
- **JiraStory**: Each story that references an epic slug; includes summary, description, labels, and the parent epic key/ID.
- **SeedMapping**: The JSON object stored in `state/jira_state.json` that maps every epic/story slug to its Jira key, internal ID, and issue type so future scripts can look up the correct Jira issue.
- **JiraCredentials**: The provided email/API token pair plus the base URL (from `JIRA_BASE_URL`) that authenticate every API call.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running the script against a clean Jira tenant provisions exactly the project plus all epics/stories defined in `config/seeds/jira-requirements.seed.yaml` within 3 minutes (excluding manual credential entry).
- **SC-002**: Re-running the script when the base project name already exists leaves the original project untouched and creates a new project whose name follows the `(<n>)` suffix pattern while still creating the full issue set.
- **SC-003**: The file `state/jira_state.json` lists one entry per slug with its Jira key, Jira issue ID, and issue type and is only updated after a completely successful run.
- **SC-004**: Every log output from the script clearly states the selected project name/key, the number of epics/stories created, and reports the mapping filename; the script exits non-zero and does not write state when a Jira API error occurs (e.g., authentication failure, validation error, rate limit).
