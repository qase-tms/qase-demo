# Contract: Create Run

**API doc**: `api/create-run.md`  
**Endpoint**: `POST /run/{code}`  
**Used in**: `run_simulator.py` and `maintenance.py`

---

## Request

```http
POST /v1/run/{code}
Token: {QASE_API_TOKEN}
Content-Type: application/json
```

Required payload fields include:
- `title`
- `description`
- `environment_id`
- `milestone_id`

## Response

```json
{
  "status": true,
  "result": {
    "id": 245
  }
}
```

`result.id` is required for results submission, external linking, and completion.
