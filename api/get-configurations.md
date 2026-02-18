# Get All Configurations

This method allows to retrieve all configurations stored in selected project. 

### Path

`GET /configuration/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all configurations. |

## ConfigurationListResponse

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
        "title": "Confuguration title",
        "description": "Configuration description",
        "group": {
          "id": 1,
          "title": "Group title"
        },
        "created_at": "2017-10-21T11:09:40+00:00",
        "updated_at": "2017-10-21T11:09:40+00:00"
      }
    ]
  }
}
```

## ConfigurationGroup

```json
{
  "id": 1,
  "title": "Group title"
}
```

## Configuration

```json
{
  "id": 1,
  "title": "Confuguration title",
  "description": "Configuration description",
  "group": {
    "id": 1,
    "title": "Group title"
  },
  "created_at": "2017-10-21T11:09:40+00:00",
  "updated_at": "2017-10-21T11:09:40+00:00"
}
```