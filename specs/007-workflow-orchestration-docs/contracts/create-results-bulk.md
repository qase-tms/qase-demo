# Contract: Create Results Bulk

**API doc**: `api/create-result-bulk.md`  
**Endpoint**: `POST /result/{code}/{run_id}/bulk`  
**Used in**: `run_simulator.py` and `maintenance.py`

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
      "time_ms": 5600
    }
  ]
}
```

## Constraints

- `case_id` must reference pre-seeded case IDs.
- `defect=true` is valid only for failed status.
- Dry-run mode must not call this endpoint.

## Response

```json
{
  "status": true
}
```
