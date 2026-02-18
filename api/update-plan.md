# Update Plan

This method allows to update a specific test plan.

### Path

`PATCH /plan/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test plan. |

### Request Body

## PlanUpdate

```json
{
  "title": "Test Plan",
  "description": "Description for Test Plan",
  "milestone_id": 1,
  "cases": [
    1,
    2,
    3
  ]
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of plan update. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```