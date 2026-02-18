# Update Milestone

This method allows to update a specific milestone.

### Path

`PATCH /milestone/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of milestone. |

### Request Body

## MilestoneUpdate

```json
{
  "title": "Milestone title",
  "description": "Milestone description",
  "status": "active",
  "due_date": "2017-10-21T11:09:40+00:00"
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of milestone update. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```