# Contract: Create Run

**API doc**: `api/create-run.md`  
**Endpoint**: `POST /run/{code}`  
**Used in**: Run lifecycle phase 1 (run creation)

---

## Request

```http
POST /v1/run/{code}
Token: {QASE_API_TOKEN}
Content-Type: application/json
```

```json
{
  "title": "Regression - Sprint 3 Checkout Stabilization",
  "description": "Validates checkout stability after payment retry refactor and 3DS guardrail updates.",
  "cases": [201, 202, 205, 214, 229],
  "environment_id": 1,
  "milestone_id": 3,
  "tags": ["regression", "checkout", "stability"],
  "start_time": "2026-02-27T10:15:00+00:00"
}
```

### Constraints

- `cases[]` must contain only known existing case IDs from state.
- `environment_id` and `milestone_id` must come from state maps.
- Tags should contain 1-3 meaningful labels.
- Title and description must align with selected run theme.

---

## Response

```json
{
  "status": true,
  "result": {
    "id": 145
  }
}
```

`result.id` is required for all subsequent lifecycle calls.

