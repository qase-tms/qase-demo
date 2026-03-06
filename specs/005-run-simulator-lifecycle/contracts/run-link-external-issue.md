# Contract: Link Run to External Issue

**API doc**: `api/run-update-external-issue.md`  
**Endpoint**: `POST /run/{code}/external-issue`  
**Used in**: Run lifecycle phase 4 (Jira linkage)

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
      "run_id": 145,
      "external_issue": "HY-245"
    }
  ]
}
```

### Constraints

- `run_id` must be the run ID returned by create-run call.
- `external_issue` should be the Jira issue key for the newly created Task.
- Exactly one external issue link is expected per run lifecycle execution.

---

## Response

`200 OK` with success status indicates link is stored.

Run must be linked before completion call.

