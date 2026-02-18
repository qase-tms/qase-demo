# Delete Milestone

This method allows to delete a specific milestone.

### Path

`DELETE /milestone/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of milestone. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of milestone deletion. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```