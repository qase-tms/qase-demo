# Search

This method allows to search for entities.

### Path

`GET /search/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Query Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `query` | `string` | | Search query. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of found entities. |

## SearchResponse

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
        "title": "Test Case 1",
        "entity_type": "test_case"
      }
    ]
  }
}
```

## SearchResponseAllOfResultEntities

```json
{
  "id": 1,
  "title": "Test Case 1",
  "entity_type": "test_case"
}
```