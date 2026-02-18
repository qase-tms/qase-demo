# Get Plan

This method allows to retrieve a specific test plan.

### Path

`GET /plan/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test plan. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single test plan. |

## PlanResponse

```json
{
  "status": true,
  "result": {
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
    "cases_count": 10,
    "included_actuals": [
      {
        "case_id": 10,
        "status": "passed"
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

## PlanDetailedAllOfCases

```json
{
  "case_id": 10,
  "status": "passed"
}
```

## PlanDetailed

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
  "cases_count": 10,
  "included_actuals": [
    {
      "case_id": 10,
      "status": "passed"
    }
  ]
}
```