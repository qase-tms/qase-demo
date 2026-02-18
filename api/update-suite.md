# Update Suite

This method allows to update a specific test suite.

### Path

`PATCH /suite/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test suite. |

### Request Body

## SuiteUpdate

```json
{
  "title": "Test Suite",
  "description": "Description for Test Suite",
  "parent_id": 1
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of test suite update. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```