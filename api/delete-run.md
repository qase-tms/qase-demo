# Delete Run

This method allows to delete a specific test run.

### Path

`DELETE /run/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test run. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of test run deletion. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```