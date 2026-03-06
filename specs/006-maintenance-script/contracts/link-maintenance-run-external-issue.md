# Contract: Link Maintenance Run External Issue

**API doc**: `api/link-run-external-issue.md`  
**Endpoint**: `POST /run/{code}/external-issue`  
**Used in**: Maintenance cycle per-run lifecycle (phase 4)

---

## Request

```http
POST /v1/run/{code}/external-issue
Token: {QASE_API_TOKEN}
Content-Type: application/json
```

```json
{
  "type": "jira-cloud",
  "links": [
    {
      "run_id": 245,
      "external_issue": "AI-140"
    }
  ]
}
```

### Constraints

- `run_id` must reference the created maintenance run.
- `external_issue` must be the Jira issue key from maintenance task creation.
- If link fails, run remains incomplete and cycle continues.

---

## Response

```json
{
  "status": true
}
```

Successful link is required before run completion.
