# Contract: Complete Maintenance Run

**API doc**: `api/complete-run.md`  
**Endpoint**: `POST /run/{code}/{id}/complete`  
**Used in**: Maintenance cycle per-run lifecycle (phase 5)

---

## Request

```http
POST /v1/run/{code}/{id}/complete
Token: {QASE_API_TOKEN}
```

No body required.

### Constraints

- Must execute only after successful result submission and successful external issue link.
- Incomplete runs (Jira create/link failure) must not call completion endpoint.

---

## Response

```json
{
  "status": true
}
```

Completed runs are counted toward cycle `run_count_completed`.
