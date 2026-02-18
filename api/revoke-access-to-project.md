# Revoke Access to Project

This method allows to revoke access to a specific project.

### Path

`DELETE /project/{code}/access`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

| Parameter | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `member_id` | `integer` | Yes | ID of the user to revoke access from. |

```json
{
  "member_id": 0
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | Result of operation. |
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
