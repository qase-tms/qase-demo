# Get Shared Step

This method allows to retrieve a specific shared step.

### Path

`GET /shared_step/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of shared step. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single shared step. |

## SharedStepResponse

```json
{
  "status": true,
  "result": {
    "id": 1,
    "title": "Shared Step title",
    "hash": "950a99059f21f1852033c4153b035136",
    "created_at": "2017-10-21T11:09:40+00:00",
    "updated_at": "2017-10-21T11:09:40+00:00",
    "steps": [
      {
        "position": 1,
        "action": "Action",
        "expected_result": "Expected Result",
        "data": "Data"
      }
    ]
  }
}
```

## SharedStepContent

```json
{
  "position": 1,
  "action": "Action",
  "expected_result": "Expected Result",
  "data": "Data"
}
```

## SharedStep

```json
{
  "id": 1,
  "title": "Shared Step title",
  "hash": "950a99059f21f1852033c4153b035136",
  "created_at": "2017-10-21T11:09:40+00:00",
  "updated_at": "2017-10-21T11:09:40+00:00",
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