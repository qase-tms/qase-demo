# Update Defect Status

This method allows to update a specific defect status.

### Path

`PATCH /defect/{code}/status/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | Identifier of the defect. |

### Request Body

| Parameter | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `status` | `string` | Yes | New status for the defect. Enum: `in_progress`, `resolved`, `invalid`. |

```json
{
  "status": "in_progress"
}
```

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
