# Contract: Jira Create Task

**API doc**: Jira Cloud REST API v3 `POST /rest/api/3/issue`  
**Endpoint**: `POST /rest/api/3/issue`  
**Used in**: `run_simulator.py` and `maintenance.py`

---

## Request

```http
POST /rest/api/3/issue
Authorization: Basic {JIRA_EMAIL:JIRA_API_TOKEN}
Content-Type: application/json
```

Required fields:
- `project.key` resolved from `state/jira_state.json` (`project.key`) with optional `JIRA_PROJECT_KEY` override
- `issuetype.name` (`Task`)
- meaningful `summary`

## Response

```json
{
  "id": "10840",
  "key": "AI-140"
}
```

The `key` value is required for Qase external issue linking.
