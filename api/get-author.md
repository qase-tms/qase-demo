# Get Author

GET /author/{id}

Get author by ID.

This method allows to retrieve author by ID.

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|Identifier.|

### Example responses

```json
{
  "status": true,
  "result": {
    "id": 0,
    "author_id": 0,
    "entity_type": "string",
    "entity_id": 0,
    "email": "string",
    "name": "string",
    "is_active": true
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Single author.|[AuthorResponse](#schemaauthorresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
