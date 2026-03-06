# Contract: Bulk Create Cases

**API doc**: `api/create-case-bulk.md`
**Endpoint**: `POST /case/{code}/bulk`
**Used in**: Phase 4 (create pass), batches of ≤ 30

---

## Request

```
POST https://api.qase.io/v1/case/{code}/bulk
Headers:
  Token: {QASE_API_TOKEN}
  Content-Type: application/json
```

```json
{
  "cases": [
    {
      "title": "Auth: Negative: Failed Registration with Invalid Email Format",
      "description": "Validates Web UI behavior for new user scenarios.",
      "preconditions": "Seeded demo users exist and API is reachable.",
      "postconditions": "No persistent side effects.",
      "priority": 3,
      "severity": 5,
      "behavior": 3,
      "type": 2,
      "layer": 1,
      "automation": 2,
      "status": 0,
      "is_flaky": 0,
      "suite_id": 8,
      "steps": [
        { "action": "Open ShopEase and go to Sign up", "expected_result": "", "data": "", "position": 1 },
        { "action": "Enter a new email and a strong password", "expected_result": "", "data": "", "position": 2 }
      ],
      "custom_field": {
        "221": "3",
        "222": "6",
        "11":  "12",
        "12":  "14",
        "225": "20,19"
      }
    }
  ]
}
```

### Field constraints

| Field | Type | Constraint |
|-------|------|------------|
| `title` | string | Required; max 255 chars |
| `suite_id` | int64 | From `SuiteIDMap`; not null |
| `is_flaky` | integer | `0` or `1`; never boolean |
| `custom_field` | object | Keys = field ID as string; values = option ID as string (selectbox) or comma-joined option IDs (multiselect) |
| `steps[].position` | integer | 1-based; must be sequential |
| `milestone_id` | int64 | Omitted — all 120 CSV rows have empty `milestone_id` |

---

## Response (200 OK)

```json
{
  "status": true,
  "result": {
    "ids": [201, 202, 203]
  }
}
```

`result.ids[]` is ordered identically to the input `cases[]` array. Zip against the batch's `[csv_id, ...]` list to build `case_id_map` entries.

## Error Responses

| Status | Action |
|--------|--------|
| 400 | Log batch range + response body; exit without partial state write |
| 401/403 | Exit with credential error |
| 404 | Exit: project_code not found in Qase |
| 422 | Log batch range; exit with validation details |
| 429/5xx | Retry with exponential backoff (max 3, 30s cap) |
