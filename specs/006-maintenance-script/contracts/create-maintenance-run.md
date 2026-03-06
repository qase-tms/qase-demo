# Contract: Create Maintenance Run

**API doc**: `api/create-run.md`  
**Endpoint**: `POST /run/{code}`  
**Used in**: Maintenance cycle per-run lifecycle (phase 1)

---

## Request

```http
POST /v1/run/{code}
Token: {QASE_API_TOKEN}
Content-Type: application/json
```

```json
{
  "title": "Smoke - Weekday Health Sweep",
  "description": "Daily tactical maintenance run to keep workspace execution trends active.",
  "environment_id": 1,
  "milestone_id": 3,
  "tags": ["maintenance", "smoke", "weekday"],
  "start_time": "2026-02-27 06:10:00"
}
```

### Constraints

- Do not seed run with full `cases[]`; results are posted via bulk result endpoint.
- `environment_id` and `milestone_id` must come from workspace state mappings.
- Title/description must be realistic and non-empty.

---

## Response

```json
{
  "status": true,
  "result": {
    "id": 245
  }
}
```

`result.id` is required for result submission, issue linking, and completion.
