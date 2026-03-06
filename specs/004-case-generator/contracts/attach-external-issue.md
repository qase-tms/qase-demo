# Contract: Attach External Issue

**API doc**: `api/case-attach-external-issue.md`
**Endpoint**: `POST /case/{code}/external-issue/attach`
**Used in**: Phase 6 (Jira link pass), batches of ≤ 30 links per call

---

## Request

```
POST https://api.qase.io/v1/case/{code}/external-issue/attach
Headers:
  Token: {QASE_API_TOKEN}
  Content-Type: application/json
```

```json
{
  "type": "jira-cloud",
  "links": [
    { "case_id": 201, "external_issues": ["AF-7"] },
    { "case_id": 202, "external_issues": ["AF-8"] },
    { "case_id": 203, "external_issues": ["AF-7"] }
  ]
}
```

### Field constraints

| Field | Type | Constraint |
|-------|------|------------|
| `type` | string | Always `"jira-cloud"` (fixed constant per F-09) |
| `links[].case_id` | integer | Qase case ID from `CaseIDMap` |
| `links[].external_issues` | array[string] | Exactly one entry: the Jira issue **key** (e.g., `"AF-7"`) — NOT the numeric internal ID (e.g., `"10443"`). Empirically verified: the API returns HTTP 400 "format is invalid" for numeric internal IDs. Read `jira_key` from `jira_state["stories"]`, not `jira_id`. |

---

## Idempotency Guard (Phase 6 Preflight)

Before the link pass, fetch all cases with their external issues:

```
GET /case/{code}?limit=100&offset=0&include=external_issues
GET /case/{code}?limit=100&offset=100&include=external_issues
```

For each case entity in the response, check `external_issues[]`. If non-empty, add the case's Qase ID to `linked_case_ids` set. Skip cases in this set during the link pass.

---

## Response (200 OK)

```json
{
  "status": true,
  "result": { "id": 1 }
}
```

---

## Error Responses

| Status | Action |
|--------|--------|
| 400 | Log batch case IDs + response body; exit |
| 401/403 | Exit with credential error |
| 404 | Exit: project_code or case_id not found |
| 422 | Log batch; exit with validation details |
| 429/5xx | Retry with exponential backoff (max 3, 30s cap) |
