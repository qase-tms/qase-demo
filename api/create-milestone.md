# Create Milestone

This method allows to create a new milestone in selected project.

### Path

`POST /milestone/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

## MilestoneCreate

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
| `200` | A result of milestone creation. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```