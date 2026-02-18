# Get All Users

This method allows to retrieve all users.

### Path

`GET /user`

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all users. |

## UserListResponse

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
        "email": "email@example.com",
        "name": "John Doe",
        "created_at": "2017-10-21T11:09:40+00:00",
        "updated_at": "2017-10-21T11:09:40+00:00"
      }
    ]
  }
}
```

## User

```json
{
  "id": 1,
  "email": "email@example.com",
  "name": "John Doe",
  "created_at": "2017-10-21T11:09:40+00:00",
  "updated_at": "2017-10-21T11:09:40+00:00"
}
```