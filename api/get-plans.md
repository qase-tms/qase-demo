# Get All Plans

This method allows to retrieve all test plans stored in selected project.

### Path

`GET /plan/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all test plans. |

## PlanListResponse

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
        "title": "Test Plan",
        "description": "Description for Test Plan",
        "status": 0,
        "created_at": "2017-10-21T11:09:40+00:00",
        "updated_at": "2017-10-21T11:09:40+00:00",
        "milestone": {
          "id": 1,
          "title": "Milestone title"
        },
        "cases_count": 10
      }
    ]
  }
}
```

## Milestone

```json
{
  "id": 1,
  "title": "Milestone title"
}
```

## Plan

```json
{
  "id": 1,
  "title": "Test Plan",
  "description": "Description for Test Plan",
  "status": 0,
  "created_at": "2017-10-21T11:09:40+00:00",
  "updated_at": "2017-10-21T11:09:40+00:00",
  "milestone": {
    "id": 1,
    "title": "Milestone title"
  },
  "cases_count": 10
}
```