# Get All Suites

This method allows to retrieve all test suites stored in selected project.

### Path

`GET /suite/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all test suites. |

## SuiteListResponse

```json
{
  "status": true,
  "result": {
    "total": 100,
    "filtered": 100,
    "count": 20,
    "entities": [
      {
        "id": 1,
        "title": "Test Suite",
        "description": "Description for Test Suite",
        "cases_count": 10,
        "created_at": "2017-10-21T11:09:40+00:00",
        "updated_at": "2017-10-21T11:09:40+00:00"
      }
    ]
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