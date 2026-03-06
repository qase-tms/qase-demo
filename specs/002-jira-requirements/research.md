# Research Log: Jira Requirement Provisioning

## Decision: Python 3.11 script with `requests` + `PyYAML`

- **Decision**: Implement the provisioning script in Python 3.11, relying on `requests` for Jira REST interactions and `PyYAML` to read `config/seeds/jira-requirements.seed.yaml`.
- **Rationale**: The existing workspace foundation tooling is Python-based, so staying in the same language keeps onboarding friction low, reuses shared helpers (`qase_seed_utils.py`), and avoids shipping a new runtime. `requests` is already part of earlier scripts, and `PyYAML` matches the seed file format.
- **Alternatives considered**: Using the Qase-API SDK was rejected because it focuses on Qase, not Jira, and a separate JavaScript-based CLI would fragment tooling.

## Decision: Map slug → Jira issues in `state/jira_state.json` after bulk success

- **Decision**: Only write the slug-to-issue mapping once all Jira API calls succeed, using an atomic write to `state/jira_state.json`.
- **Rationale**: Later milestones depend strictly on this mapping, so a partial write would corrupt automation. Atomic writes mirror the workspace state handling in `scripts/workspace_init.py`.
- **Alternatives considered**: Writing incrementally per issue was rejected due to the risk of partial failures and inconsistent downstream linking.

## Decision: Deduplicated project key selection follows `scripts/workspace_init.py`

- **Decision**: When the base project name already exists, append ` (n)` to the name and choose the first unused two-letter alphabetic project key, matching the existing initializer logic.
- **Rationale**: Keeps deduplication predictable for operators and prevents collisions with the limited alphabetic key space. Documented as clarified requirement FR-004.
- **Alternatives considered**: Spinning up random/timestamped keys or reusing the base key both felt riskier for long-term maintenance and dashboard clarity.

## Decision: Script always creates a new project; it never silently reuses an existing one

- **Decision**: `_select_project_name` enforces that the final name is **always** distinct from every existing project name (case-insensitive comparison). There is no "reuse" path: every invocation creates an isolated project so reruns are non-destructive.
- **Rationale**: Silently reusing an existing project would append new epics/stories to a project that may already have them, making deduplication of issues ambiguous. The mapping file would also overwrite the previous run's keys, breaking any downstream scripts that already consumed the old `jira_state.json`.
- **Implementation note**: `provision_project()` calls `_select_project_name` before `_create_jira_project`; the helper only returns a name that is absent from `existing_names`, ensuring the guard is always active.
- **Alternatives considered**: A `--reuse` flag was considered but rejected: it would require extra logic to detect whether all seed issues already exist in the project, and the existing state file from a previous run already satisfies that use-case.

## Decision: urllib-only HTTP (no `requests` dependency)

- **Decision**: Use Python's built-in `urllib.request` for all Jira API calls rather than the `requests` third-party library.
- **Rationale**: Keeps the dependency footprint minimal (only `PyYAML` required). The Jira REST API v3 calls made by this script (GET project/search, POST project, GET createmeta, POST issue/bulk) are straightforward JSON exchanges that do not need `requests`-specific features like sessions or streaming.
- **Alternatives considered**: `requests` would simplify timeouts and retries but adds an extra install step that is avoidable given the small call surface.
