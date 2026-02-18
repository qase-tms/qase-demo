# Create Plan

This method allows to create a new test plan in selected project.

### Path

`POST /plan/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

## PlanCreate

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
| `200` | A result of plan creation. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```