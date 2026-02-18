# Get Milestone

This method allows to retrieve a specific milestone.

### Path

`GET /milestone/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of milestone. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single milestone. |

## MilestoneResponse

```json
{
  "status": true,
  "result": {
    "id": 1,
    "title": "Milestone title",
    "description": "Milestone description",
    "status": "active",
    "due_date": "2017-10-21T11:09:40+00:00",
    "created_at": "2017-10-21T11:09:40+00:00",
    "updated_at": "2017-10-21T11:09:40+00:00"
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