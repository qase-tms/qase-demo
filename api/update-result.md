# Update Result

This method allows to update a specific test result.

### Path

`PATCH /result/{code}/{hash}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `hash` | `string` | | Hash of test result. |

### Request Body

## ResultUpdate

```json
{
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
  "custom_fields": [
    {
      "id": 1,
      "value": "Custom field value"
    }
  ]
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of test run result update. |

## HashResponse

```json
{
  "status": true,
  "result": {
    "hash": "950a99059f21f1852033c4153b035136"
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