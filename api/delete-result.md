# Delete Result

This method allows to delete a test run result.

### Path

`DELETE /result/{code}/{id}/{hash}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | Identifier of the test run. |
| `hash` | `string` | | Hash of the test run result. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result. |
| `400` | Bad Request. |
| `401` | Unauthorized. |
| `403` | Forbidden. |
| `404` | Not Found. |
| `429` | Too Many Requests. |

## HashResponse

```json
{
  "status": true,
  "result": {
    "hash": "string"
  }
}
```
