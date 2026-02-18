# Create Suite

This method allows to create a new test suite in selected project.

### Path

`POST /suite/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

## SuiteCreate

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
| `200` | A result of test suite creation. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```