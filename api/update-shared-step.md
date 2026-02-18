# Update Shared Step

This method allows to update a specific shared step.

### Path

`PATCH /shared_step/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of shared step. |

### Request Body

## SharedStepUpdate

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
| `200` | A result of shared step update. |

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