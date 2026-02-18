# Create Shared Step

This method allows to create a new shared step in selected project.

### Path

`POST /shared_step/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

## SharedStepCreate

```json
{
  "title": "Shared Step title",
  "steps": [
    {
      "position": 1,
      "action": "Action",
      "expected_result": "Expected Result",
      "data": "Data"
    }
  ]
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of shared step creation. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```

## SharedStepContentCreate

```json
{
  "position": 1,
  "action": "Action",
  "expected_result": "Expected Result",
  "data": "Data"
}
```