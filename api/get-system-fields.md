# Get System Fields

This method allows to retrieve all system fields.

### Path

`GET /system_field`

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all system fields. |

## SystemFieldListResponse

```json
{
  "status": true,
  "result": [
    {
      "id": 1,
      "title": "System field title",
      "type": "string",
      "options": [
        {
          "id": 1,
          "title": "Option title"
        }
      ]
    }
  ]
}
```

## SystemFieldOption

```json
{
  "id": 1,
  "title": "Option title"
}
```

## SystemField

```json
{
  "id": 1,
  "title": "System field title",
  "type": "string",
  "options": [
    {
      "id": 1,
      "title": "Option title"
    }
  ]
}
```