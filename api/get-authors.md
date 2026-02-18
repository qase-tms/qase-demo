# Get Authors

GET /author

Get all authors.

This method allows to retrieve all authors in selected project.

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|search|query|string|false|Provide a string that will be used to search by name.|
|type|query|string|false|none|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|type|app|
|type|user|

### Example responses

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "id": 0,
        "author_id": 0,
        "entity_type": "string",
        "entity_id": 0,
        "email": "string",
        "name": "string",
        "is_active": true
      }
    ]
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Author list.|[AuthorListResponse](#schemaauthorlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
