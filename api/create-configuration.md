# Create Configuration

This method allows to create a new configuration in selected project.

### Path

`POST /configuration/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

## ConfigurationCreate

```json
{
  "title": "Configuration title",
  "group_id": 1,
  "description": "Configuration description"
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of configuration creation. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```