# Contract: Link Run External Issue

**API doc**: `api/link-run-external-issue.md`  
**Endpoint**: `POST /run/{code}/external-issue`  
**Used in**: `run_simulator.py` and `maintenance.py`

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

## Response

```json
{
  "status": true
}
```

On link failure, run completion must not proceed for that run.
