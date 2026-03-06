# Contract: Complete Run

**API doc**: `api/complete-run.md`  
**Endpoint**: `POST /run/{code}/{run_id}/complete`  
**Used in**: Run lifecycle phase 5 (finalization)

---

## Request

```http
POST /v1/run/{code}/{run_id}/complete
Token: {QASE_API_TOKEN}
```

No request body.

### Preconditions

- All intended results for the run have already been submitted.
- External Jira issue link has already been set for the run.

---

## Response

```json
{
  "status": true
}
```

After this call, the run is considered closed for the simulation lifecycle.

