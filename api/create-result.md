# Create Result

This method allows to create a new test result in selected project.

### Path

`POST /result/{code}/{id}/results`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test run. |

### Request Body

## ResultCreate

```json
{
  "case_id": 10,
  "hash": "235a0f0d4b1a4597402a7853676dfb37",
  "status": "passed",
  "time": 100,
  "comment": "Test suite run.",
  "stacktrace": "stacktrace",
  "steps": [
    {
      "position": 1,
      "status": "passed",
      "time": 100,
      "comment": "Step comment"
    }
  ],
  "attachments": [
    "950a99059f21f1852033c4153b035136"
  ],
  "before_run_hook": "before_run_hook",
  "after_run_hook": "after_run_hook",
  "custom_fields": [
    {
      "id": 1,
      "value": "Custom field value"
    }
  ],
  "defects": [
    "jira-123",
    "bug-456"
  ]
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of test run result creation. |

## ResultCreateResponse

```json
{
  "status": true,
  "result": {
    "hash": "235a0f0d4b1a4597402a7853676dfb37"
  }
}
```

## CustomFieldValue

```json
{
  "id": 1,
  "value": "Custom field value"
}
```

## TestStepCreate

```json
{
  "position": 1,
  "status": "passed",
  "time": 100,
  "comment": "Step comment"
}
```

## ResultCreateCase

```json
{
  "case_id": 10,
  "hash": "235a0f0d4b1a4597402a7853676dfb37",
  "status": "passed",
  "time": 100,
  "comment": "Test suite run.",
  "stacktrace": "stacktrace",
  "steps": [
    {
      "position": 1,
      "status": "passed",
      "time": 100,
      "comment": "Step comment"
    }
  ],
  "attachments": [
    "950a99059f21f1852033c4153b035136"
  ],
  "before_run_hook": "before_run_hook",
  "after_run_hook": "after_run_hook",
  "custom_fields": [
    {
      "id": 1,
      "value": "Custom field value"
    }
  ],
  "defects": [
    "jira-123",
    "bug-456"
  ]
}
```

## ResultCreate

```json
{
  "case_id": 10,
  "hash": "235a0f0d4b1a4597402a7853676dfb37",
  "status": "passed",
  "time": 100,
  "comment": "Test suite run.",
  "stacktrace": "stacktrace",
  "steps": [
    {
      "position": 1,
      "status": "passed",
      "time": 100,
      "comment": "Step comment"
    }
  ],
  "attachments": [
    "950a99059f21f1852033c4153b035136"
  ],
  "before_run_hook": "before_run_hook",
  "after_run_hook": "after_run_hook",
  "custom_fields": [
    {
      "id": 1,
      "value": "Custom field value"
    }
  ],
  "defects": [
    "jira-123",
    "bug-456"
  ]
}
```