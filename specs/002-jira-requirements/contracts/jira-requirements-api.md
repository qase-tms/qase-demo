# Jira Requirement Provisioning API Contracts

## Authorization
- Header: `Authorization: Basic <base64(email:api_token)>`
- Header: `Accept: application/json`
- Content-Type: `application/json` for mutation requests

## `/rest/api/3/project/search`
- **Purpose**: Detect existing projects with the target name and collect used two-letter keys.
- **Method**: `GET`
- **Query Params**: `query=<base project name>`, optional pagination.
- **Response Notes**: Inspect `values[].name`, `values[].key`, `values[].id`.
- **Idempotency**: Only read; used to decide whether to create a new project and which key to reuse.

## `/rest/api/3/project`
- **Purpose**: Create a new Jira project when the name/key combination is unused.
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "key": "AB",
    "name": "ShopEase Requirements (2)",
    "projectTypeKey": "software",
    "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-project-management",
    "description": "Requirements store for ShopEase automation",
    "leadAccountId": "<derived if required>"
  }
  ```
- **Success**: captures `id` and `key` for the new project.
- **Failure Handling**: if `name` already exists, increment suffix and retry; log API detail before failure.

## `/rest/api/3/issue/bulk`
- **Purpose**: Create epics and stories in batches (one request per type).
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "issueUpdates": [
      {
        "fields": {
          "project": { "key": "<project_key>" },
          "issuetype": { "name": "Epic" },
          "summary": "User can ...",
          "description": { "type": "doc", "version": 1, "content": [...] },
          "<epic-name-field>": "User can ...",
          "labels": ["demo"]
        }
      },
      ...
    ]
  }
  ```
- **Linking**: Stories require `Epic Link` field or `parent` object referencing created epic key.
- **Partial Success**: fail fast if returned issue count mismatches request count; log `issues` array detail.

## Logging & Mapping
- All requests log start/end timestamp, request path, and response summary.
- `state/jira_state.json` holds:
  ```json
  {
    "project": { "name": "ShopEase Web App", "key": "AA", "id": 12345 },
    "epics": {
      "auth":     { "jira_key": "AA-1", "jira_id": 10001, "issue_type": "Epic" },
      "search":   { "jira_key": "AA-2", "jira_id": 10002, "issue_type": "Epic" }
    },
    "stories": {
      "auth-1":   { "jira_key": "AA-3", "jira_id": 10003, "issue_type": "Story",
                    "epic_slug": "auth", "summary": "User can sign up …" },
      "auth-2":   { "jira_key": "AA-4", "jira_id": 10004, "issue_type": "Story",
                    "epic_slug": "auth", "summary": "User can log in …" }
    }
  }
  ```

## Mapping Consumption (for downstream scripts)

Downstream automation (CSV case seeding, Qase linking) **must** read
`state/jira_state.json` as follows:

1. Load the file as JSON.
2. Resolve an epic by its seed slug via `state["epics"][slug]`.
3. Resolve a story by its namespaced slug via `state["stories"]["<epic_slug>-<n>"]`
   where `<n>` is the 1-based position of that story within its epic in the
   seed file order.
4. Story entries include `"epic_slug"` and `"summary"` fields to allow fuzzy
   matching when the exact index is unknown.
5. **Never hardcode Jira keys or IDs**: always look up from this file so a
   fresh provisioning run (which produces new keys) does not break downstream
   scripts.

## Error Guidance

| Scenario | Console signal | State file outcome |
|---|---|---|
| Invalid credentials | `[ERROR] Jira API error 401` | Unchanged |
| Duplicate epic slug in seed | `[ERROR] Duplicate epic slugs` | Unchanged |
| Bulk create partial success | `[ERROR] … creation mismatch` | Unchanged |
| Rate limit (429) | `[WARN] … retry N/3` → up to 3 retries | Unchanged until success |
| All retries exhausted | `[ERROR] Max retries exceeded` | Unchanged |
