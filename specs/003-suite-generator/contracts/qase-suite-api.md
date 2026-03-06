# API Contract: Qase Suite Endpoints

**Feature**: `003-suite-generator`
**Date**: 2026-02-20
**Source**: `api/get-suites.md`, `api/create-suite.md`
**Base URL**: `https://api.qase.io/v1`
**Auth header**: `Token: <QASE_API_TOKEN>`

---

## 1. List All Suites

Used at script start to build the `ExistingSuitesMap` for idempotency.

```
GET /suite/{code}?limit=100
```

### Path parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `code` | string | Qase project code (from `state/workspace_state.json`) |

### Query parameters

| Parameter | Type | Default | Used value |
|-----------|------|---------|------------|
| `limit` | integer | ~20 (estimated) | `100` — ensures all 30 suites are returned in one call |

### Request headers

```
Token: <QASE_API_TOKEN>
```

### Success response — `200 OK`

```json
{
  "status": true,
  "result": {
    "total": 30,
    "filtered": 30,
    "count": 30,
    "entities": [
      {
        "id": 101,
        "title": "01 Authentication",
        "description": "",
        "cases_count": 0,
        "created_at": "2026-02-20T10:00:00+00:00",
        "updated_at": "2026-02-20T10:00:00+00:00"
      }
    ]
  }
}
```

### Fields used by this script

| Field | Path | Used for |
|-------|------|----------|
| Suite ID | `result.entities[].id` | Value in `ExistingSuitesMap` |
| Suite title | `result.entities[].title` | Key in `ExistingSuitesMap` |
| Total count | `result.total` | Pagination safety check |
| Page count | `result.count` | Detect if `count < total` → need additional pages |

**Important**: `parent_id` is **not** present in the documented response. See research F-02. The implementation keys the map on `title` only.

### Pagination handling

If `result.count < result.total`, repeat with `offset=result.count` until all entities are fetched:
```
GET /suite/{code}?limit=100&offset=100
GET /suite/{code}?limit=100&offset=200
...
```
For the ShopEase workspace (30 suites, limit=100) a single call is always sufficient; the loop is included as a safety measure.

### Error responses

| Status | Meaning | Script action |
|--------|---------|---------------|
| `401` | Invalid token | Exit with auth error, no state change |
| `403` | Token lacks project access | Exit with permission error, no state change |
| `404` | Project code not found | Exit with descriptive error, no state change |
| `429`, `5xx` | Rate limit / server error | Retry up to 3 times with backoff |

---

## 2. Create Suite

Used in Pass 1 (top-level suites) and Pass 2 (child suites) when a suite title is not already in `ExistingSuitesMap`.

```
POST /suite/{code}
```

### Path parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `code` | string | Qase project code |

### Request headers

```
Token: <QASE_API_TOKEN>
Content-Type: application/json
```

### Request body

**Pass 1 (top-level suite)**:
```json
{
  "title": "01 Authentication"
}
```

**Pass 2 (child suite)**:
```json
{
  "title": "Registration",
  "parent_id": 101
}
```

### Fields sent

| Field | Type | Required | Source |
|-------|------|----------|--------|
| `title` | string | Yes | `SuiteRow.title` from CSV `suite` column |
| `parent_id` | integer | No (omit for top-level) | Resolved from `SuiteIDMap` using `SuiteRow.parent_csv_id` |

Fields **not** sent: `description` (empty by default — suites get their context from their title and the cases within them).

### Success response — `200 OK`

```json
{
  "status": true,
  "result": {
    "id": 102
  }
}
```

The `id` value is stored in `SuiteIDMap` under the row's `csv_suite_id` key.

### Error responses

| Status | Meaning | Script action |
|--------|---------|---------------|
| `400` | Validation error (e.g., duplicate title, invalid parent_id) | Log full response body; exit non-zero without state write |
| `401` | Invalid token | Exit with auth error |
| `403` | Insufficient permissions | Exit with permission error |
| `404` | Project not found | Exit with descriptive error |
| `429`, `5xx` | Rate limit / server error | Retry up to 3 times with exponential backoff (1 s, 2 s, 4 s); fail after 3 retries |

---

## Rate Limiting

Both endpoints are subject to the global rate limit:

```
≤ 5 requests/second
```

Implementation: module-level `_last_req_ts` + `time.sleep(max(0, _RATE_INTERVAL - elapsed))` before each request, where `_RATE_INTERVAL = 0.20` seconds.

Maximum API calls for a full clean run: **31** (1 GET + 30 POST). At 5 req/sec this takes at minimum 6.2 seconds of enforced sleep, well within the 60-second SC-001 target.

---

## Retry Policy

```
Max retries:      3
Backoff schedule: 1 s → 2 s → 4 s (exponential, 2^(attempt-1))
Per-request cap:  30 seconds (urllib timeout parameter)
Retryable codes:  429, 500, 502, 503, 504
Non-retryable:    400, 401, 403, 404 (fail immediately)
```
