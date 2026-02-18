# Delete Shared Step

This method allows to delete a specific shared step.

### Path

`DELETE /shared_step/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of shared step. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of shared step deletion. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```