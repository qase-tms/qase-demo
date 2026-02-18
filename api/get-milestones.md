# Get All Milestones

This method allows to retrieve all milestones stored in selected project.

### Path

`GET /milestone/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all milestones. |

## MilestoneListResponse

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
        "title": "Milestone title",
        "description": "Milestone description",
        "status": "active",
        "due_date": "2017-10-21T11:09:40+00:00",
        "created_at": "2017-10-21T11:09:40+00:00",
        "updated_at": "2017-10-21T11:09:40+00:00"
      }
    ]
  }
}
```

## Milestone

```json
{
  "id": 1,
  "title": "Milestone title",
  "description": "Milestone description",
  "status": "active",
  "due_date": "2017-10-21T11:09:40+00:00",
  "created_at": "2017-10-21T11:09:40+00:00",
  "updated_at": "2017-10-21T11:09:40+00:00"
}
```