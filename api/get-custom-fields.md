# Get Custom Fields

GET /custom_field

Get all custom fields.

This method allows to retrieve all custom fields.

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

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
        "title": "string",
        "entity": "case",
        "type": "string",
        "is_required": true,
        "default_value": "string",
        "is_visible": true,
        "placeholder": "string",
        "created_at": "2026-02-14T06:05:03.957Z",
        "updated_at": "2026-02-14T06:05:03.957Z",
        "projects": [
          "string"
        ]
      }
    ]
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all custom fields.|[CustomFieldListResponse](#schemacustomfieldlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
