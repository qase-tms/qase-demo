# Contract: System Fields

**API doc**: `api/get-system-fields.md`
**Endpoint**: `GET /system_field`
**Used in**: Phase 1 (build runtime EnumMap), called once at script start

---

## Request

```
GET https://api.qase.io/v1/system_field
Headers:
  Token: {QASE_API_TOKEN}
```

No path parameters. No pagination — returns all system fields in a single response.

---

## Response (200 OK)

```json
{
  "status": true,
  "result": [
    {
      "id": 1,
      "title": "severity",
      "type": "string",
      "options": [
        { "id": 1, "title": "blocker" },
        { "id": 2, "title": "critical" },
        { "id": 3, "title": "major" },
        { "id": 4, "title": "normal" },
        { "id": 5, "title": "minor" },
        { "id": 6, "title": "trivial" }
      ]
    },
    {
      "id": 2,
      "title": "priority",
      "options": [
        { "id": 1, "title": "high" },
        { "id": 2, "title": "medium" },
        { "id": 3, "title": "low" }
      ]
    }
  ]
}
```

---

## EnumMap construction

```python
enum_map = {}
for field in result:
    field_name = field["title"].lower()
    enum_map[field_name] = {
        opt["title"].lower(): opt["id"]
        for opt in field.get("options", [])
    }
```

Fields covered: `severity`, `priority`, `behavior`, `type`, `layer`, `automation`, `status`.

`is_flaky` uses a hardcoded map `{"no": 0, "yes": 1}` (not from system_field).

---

## Error Responses

| Status | Action |
|--------|--------|
| 401/403 | Exit with credential error |
| 429/5xx | Retry with exponential backoff (max 3, 30s cap) |
