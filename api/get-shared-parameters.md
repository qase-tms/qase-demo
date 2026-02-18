# Get All Shared Parameters

This method allows to retrieve all shared parameters stored in selected project.

### Path

`GET /shared_parameter/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all shared parameters. |

## SharedParameterListResponse

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
        "title": "Shared Parameter title",
        "type": "string",
        "entity": "test_case",
        "created_at": "2017-10-21T11:09:40+00:00",
        "updated_at": "2017-10-21T11:09:40+00:00",
        "parameters": [
          {
            "id": "1",
            "value": "Value 1"
          }
        ]
      }
    ]
  }
}
```

## SharedParameterParameter

```json
{
  "id": "1",
  "value": "Value 1"
}
```

## SharedParameter

```json
{
  "id": 1,
  "title": "Shared Parameter title",
  "type": "string",
  "entity": "test_case",
  "created_at": "2017-10-21T11:09:40+00:00",
  "updated_at": "2017-10-21T11:09:40+00:00",
  "parameters": [
    {
      "id": "1",
      "value": "Value 1"
    }
  ]
}
```