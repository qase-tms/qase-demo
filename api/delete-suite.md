# Delete Suite

This method allows to delete a specific test suite.

### Path

`DELETE /suite/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test suite. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of test suite deletion. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```