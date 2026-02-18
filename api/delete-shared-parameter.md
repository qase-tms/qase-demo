# Delete Shared Parameter

This method allows to delete a specific shared parameter.

### Path

`DELETE /shared_parameter/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of shared parameter. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of shared parameter deletion. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```