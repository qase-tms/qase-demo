# Contract: Create Results Bulk

**API doc**: `api/create-result-bulk.md`  
**Endpoint**: `POST /result/{code}/{run_id}/bulk`  
**Used in**: Run lifecycle phase 2 (result submission)

---

## Request

```http
POST /v1/result/{code}/{run_id}/bulk
Token: {QASE_API_TOKEN}
Content-Type: application/json
```

```json
{
  "results": [
    {
      "case_id": 201,
      "status": "failed",
      "start_time": 1740651300,
      "time_ms": 12400,
      "defect": true,
      "is_autotest": true,
      "comment": "Checkout retry exceeded expected latency under concurrent payment requests.",
      "stacktrace": "Error: locator.click: Timeout 5000ms exceeded.\n  at CheckoutPage.submitPayment (checkout.page.ts:118:15)\n  at tests/checkout.spec.ts:42:9",
      "attachments": ["950a99059f21f1852033c4153b035136"],
      "param": {"browser": "Chrome", "currency": "USD"},
      "steps": [
        {
          "position": 1,
          "status": "passed",
          "action": "Open checkout page and load payment section",
          "comment": "Checkout page rendered with expected cart totals."
        },
        {
          "position": 2,
          "status": "failed",
          "action": "Submit payment and await confirmation response",
          "comment": "Payment confirmation did not return within timeout.",
          "attachments": ["950a99059f21f1852033c4153b035136"]
        }
      ]
    }
  ]
}
```

### Constraints

- `results[].case_id` must reference existing seeded case IDs only.
- `defect=true` is valid only for failed results.
- `time_ms` must be positive and match timeline distribution policy.
- `steps[]` must always include non-empty `action` fields.
- Manual failures should rely on `comment`; automated failures include stack trace details.
- Parameter map may be included only when parameters exist in source case definitions.

---

## Response

```json
{
  "status": true
}
```

Bulk submission must succeed before run Jira linking and completion.

