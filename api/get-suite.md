# Get Suite

This method allows to retrieve a specific test suite.

### Path

`GET /suite/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test suite. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single test suite. |

## SuiteResponse

```json
{
  "status": true,
  "result": {
    "id": 1,
    "title": "Test Suite",
    "description": "Description for Test Suite",
    "cases_count": 10,
    "created_at": "2017-10-21T11:09:40+00:00",
    "updated_at": "2017-10-21T11:09:40+00:00"
  }
}
```

## Suite

```json
{
  "id": 1,
  "title": "Test Suite",
  "description": "Description for Test Suite",
  "cases_count": 10,
  "created_at": "2017-10-21T11:09:40+00:00",
  "updated_at": "2017-10-21T11:09:40+00:00"
}
```