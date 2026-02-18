# Get User

This method allows to retrieve a specific user.

### Path

`GET /user/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `id` | `integer` | | ID of user. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single user. |

## UserResponse

```json
{
  "status": true,
  "result": {
    "id": 1,
    "email": "email@example.com",
    "name": "John Doe",
    "created_at": "2017-10-21T11:09:40+00:00",
    "updated_at": "2017-10-21T11:09:40+00:00"
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