# Contract: Complete Run

**API doc**: `api/complete-run.md`  
**Endpoint**: `POST /run/{code}/{id}/complete`  
**Used in**: `run_simulator.py` and `maintenance.py`

---

## Request

```http
POST /v1/run/{code}/{id}/complete
Token: {QASE_API_TOKEN}
```

No body required.

## Preconditions

- Result submission already succeeded.
- External issue linking already succeeded.

## Response

```json
{
  "status": true
}
```
