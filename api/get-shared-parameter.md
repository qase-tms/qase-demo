# Get Shared Parameter

This method allows to retrieve a specific shared parameter.

### Path

`GET /shared_parameter/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of shared parameter. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single shared parameter. |

## SharedParameterResponse

```json
{
  "status": true,
  "result": {
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