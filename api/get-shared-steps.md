# Get All Shared Steps

This method allows to retrieve all shared steps stored in selected project.

### Path

`GET /shared_step/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all shared steps. |

## SharedStepListResponse

```json
{
  "status": true,
  "result": {
    "total": 100,
    "filtered": 100,
    "count": 20,
    "entities": [
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