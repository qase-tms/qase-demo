# Complete Run

This method allows to complete a specific test run.

### Path

`POST /run/{code}/{id}/complete`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | Identifier of the test run. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result. |
| `400` | Bad Request. |
| `401` | Unauthorized. |
| `403` | Forbidden. |
| `404` | Not Found. |
| `422` | Unprocessable Entity. |
| `429` | Too Many Requests. |

```json
{
  "status": true
}
```
