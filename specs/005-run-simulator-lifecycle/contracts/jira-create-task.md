# Contract: Create Jira Task Per Run

**Reference**: Jira Cloud REST API v3 issue creation pattern  
**Endpoint**: `POST /rest/api/3/issue`  
**Used in**: Run lifecycle phase 3 (tracking task creation)

---

## Request

```http
POST /rest/api/3/issue
Authorization: Basic {base64(email:api_token)}
Accept: application/json
Content-Type: application/json
```

```json
{
  "fields": {
    "project": { "key": "HY" },
    "issuetype": { "name": "Task" },
    "summary": "Regression run follow-up: checkout stabilization validation",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "This run validates payment retry changes introduced in Sprint 3 after intermittent checkout declines in production-like traffic."
            }
          ]
        }
      ]
    },
    "labels": ["qa-simulation", "checkout", "regression"]
  }
}
```

### Constraints

- A new Task issue must be created for every simulated run.
- Summary/description must align with run theme and risk narrative.
- Jira response values should capture both issue `id` and `key` for traceability.

---

## Response

```json
{
  "id": "10582",
  "key": "HY-245",
  "self": "https://example.atlassian.net/rest/api/3/issue/10582"
}
```

`key` is used for Qase run external linkage.  
`id` is retained for audit/logging continuity.

