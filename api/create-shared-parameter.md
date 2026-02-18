# Create Shared Parameter

This method allows to create a new shared parameter in selected project.

### Path

`POST /shared_parameter/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

## SharedParameterCreate

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
| `200` | A result of shared parameter creation. |

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