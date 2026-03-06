# Contract: Create Maintenance Results Bulk

**API doc**: `api/create-result-bulk.md`  
**Endpoint**: `POST /result/{code}/{run_id}/bulk`  
**Used in**: Maintenance cycle per-run lifecycle (phase 2)

---

## Request

```http
POST /v1/result/{code}/{run_id}/bulk
Token: {QASE_API_TOKEN}
Content-Type: application/json
```

```json
{
  "results": [
    {
      "case_id": 201,
      "status": "passed",
      "start_time": 1772172600,
      "time_ms": 5600,
      "defect": false,
      "is_autotest": true,
      "comment": "Maintenance execution completed successfully for checkout regression path.",
      "attachments": ["950a99059f21f1852033c4153b035136"],
      "steps": [
        {
          "position": 1,
          "status": "passed",
          "action": "Execute maintenance scenario step",
          "comment": "Step outcome captured by maintenance cycle."
        }
      ]
    }
  ]
}
```

### Constraints

- Every `results[].case_id` must map to pre-seeded case IDs only.
- At least 90% of generated results must include `attachments`.
- `defect=true` is allowed only when `status=failed`.
- `steps[].action` must be non-empty.
- No case creation/mutation may occur in this flow.

---

## Response

```json
{
  "status": true
}
```

Bulk result submission must complete before Jira linkage and run completion.
