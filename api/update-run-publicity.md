# Update Run Publicity

This method allows to update the publicity of a specific test run.

### Path

`PATCH /run/{code}/{id}/public`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | Identifier of the test run. |

### Request Body

| Parameter | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `status` | `boolean` | Yes | Set to `true` to make the run public, `false` to make it private. |

```json
{
  "status": true
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
| `429` | Too Many Requests. |

## RunPublicResponse

```json
{
  "status": true,
  "result": {
    "url": "http://example.com"
  }
}
```
