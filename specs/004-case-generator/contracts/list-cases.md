# Contract: List Cases

**API doc**: `api/get-cases.md`
**Endpoint**: `GET /case/{code}`
**Used in**: Phase 3 (create idempotency preflight) + Phase 6 (link idempotency preflight)

---

## Phase 3: Create Preflight (build existing_case_map)

```
GET https://api.qase.io/v1/case/{code}?limit=100&offset=0
GET https://api.qase.io/v1/case/{code}?limit=100&offset=100
(repeat until offset >= total)
```

Extract from each entity: `id` (int), `title` (str), `suite_id` (int).
Build: `existing_case_map = {(title, suite_id): qase_case_id}`.

Before creating any case, check `existing_case_map.get((title, suite_qase_id))`. If found, reuse; log `REUSE case {csv_id}: '{title}' → qase_id={N}`.

---

## Phase 6: Link Preflight (build linked_case_ids)

```
GET https://api.qase.io/v1/case/{code}?limit=100&offset=0&include=external_issues
GET https://api.qase.io/v1/case/{code}?limit=100&offset=100&include=external_issues
(repeat until offset >= total)
```

For each entity, if `external_issues[]` is non-empty, add `entity.id` to `linked_case_ids` set.

---

## Response (200 OK)

```json
{
  "status": true,
  "result": {
    "total": 120,
    "filtered": 120,
    "count": 100,
    "entities": [
      {
        "id": 201,
        "title": "Auth: Negative: Failed Registration...",
        "suite_id": 8,
        "external_issues": [
          { "id": "10443", "type": "jira" }
        ]
      }
    ]
  }
}
```

`external_issues` only present when `include=external_issues` query param is set.

---

## Error Responses

| Status | Action |
|--------|--------|
| 401/403 | Exit with credential error |
| 404 | Exit: project_code not found |
| 429/5xx | Retry with exponential backoff (max 3, 30s cap) |
