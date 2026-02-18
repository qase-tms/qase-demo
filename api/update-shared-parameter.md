# Update Shared Parameter

This method allows to update a specific shared parameter.

### Path

`PATCH /shared_parameter/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of shared parameter. |

### Request Body

## SharedParameterUpdate

```json
{
  "title": "Shared Parameter title",
  "type": "string",
  "entity": "test_case",
  "parameters": [
    {
      "id": "1",
      "value": "Value 1"
    }
  ]
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of shared parameter update. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
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