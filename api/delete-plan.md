# Delete Plan

This method allows to delete a specific test plan.

### Path

`DELETE /plan/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test plan. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of plan deletion. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```