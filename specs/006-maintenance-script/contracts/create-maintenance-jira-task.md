# Contract: Create Maintenance Jira Task

**API doc**: Jira Cloud REST API v3 `POST /rest/api/3/issue`  
**Endpoint**: `POST /rest/api/3/issue`  
**Used in**: Maintenance cycle per-run lifecycle (phase 3)

---

## Request

```http
POST /rest/api/3/issue
Authorization: Basic {JIRA_EMAIL:JIRA_API_TOKEN}
Content-Type: application/json
```

```json
{
  "fields": {
    "project": { "key": "AI" },
    "issuetype": { "name": "Task" },
    "summary": "Maintenance run follow-up: Smoke - Weekday Health Sweep",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            { "type": "text", "text": "Follow-up task for weekday maintenance run traceability." }
          ]
        }
      ]
    },
    "labels": ["qa-maintenance", "qase-run", "weekday"]
  }
}
```

### Constraints

- `project.key` must be sourced from `JIRA_PROJECT_KEY`.
- Exactly one Jira task is created per maintenance run.
- Returned issue key must be captured for external run linking.

---

## Response

```json
{
  "id": "10840",
  "key": "AI-140",
  "self": "https://example.atlassian.net/rest/api/3/issue/10840"
}
```

Both `id` and `key` must be parsed; `key` is used for Qase external issue link.
