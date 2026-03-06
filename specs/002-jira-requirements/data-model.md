# Data Model: Jira Requirement Provisioning

| Entity | Attributes | Relationships / Notes |
|--------|------------|-----------------------|
| `JiraProject` | `name` (string, base from `config/workspace.yaml`), `key` (unique 2-letter code), `id` (Jira project ID), `type/template` (Immutable, e.g., "Software") | Created once per run; used as scope for issue creation. |
| `JiraEpic` | `slug` (seed identifier), `summary`, `description`, `labels` (list), `jira_key`, `jira_id`, `issue_type` ("Epic") | Derived from `config/seeds/jira-requirements.seed.yaml`; slug drives linkage to stories and mapping storage. |
| `JiraStory` | `slug` (derived from `summary` or generated stable ID), `epic_slug`, `summary`, `description`, `labels`, `jira_key`, `jira_id`, `issue_type` ("Story") | Validated against known epic slugs before creation. |
| `SeedMapping` | JSON object keyed by slug → `{ jira_key, jira_id, issue_type }` | Written atomically to `state/jira_state.json` after full success; used by case seeding for linking. |
| `JiraCredentials` | `email`, `api_token`, `base_url` | Sourced interactively today with CLI flags/env fallback; used for Authorization headers. |
| `ScriptState` | `mode` (`dry-run` flag), `project_name`, `project_key`, `created_issue_counts` | Tracks progress for logging and validation; never persisted beyond `state/jira_state.json`. |

Validation rules:
- Slug uniqueness: every entry in the seed file must have a unique slug; duplicates abort before any Jira call.
- Mapping completeness: `SeedMapping` must include every epic and story slug exactly once.
- Rate limiting: all Jira calls obey ≤5 requests/sec throttle; repeated retries must not write mapping until success.
