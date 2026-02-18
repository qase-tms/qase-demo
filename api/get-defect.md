# Get Defect

GET /defect/{code}/{id}

Get a specific defect.

This method allows to retrieve a specific defect.

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

### Example responses

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "actual_result": "string",
    "severity": "string",
    "status": "string",
    "milestone_id": 0,
    "custom_fields": [
      {
        "id": 0,
        "value": "string"
      }
    ],
    "attachments": [
      {
        "size": 0,
        "mime": "string",
        "filename": "string",
        "url": "http://example.com"
      }
    ],
    "resolved_at": "2021-12-30T19:23:59+00:00",
    "member_id": 0,
    "author_id": 0,
    "external_data": "string",
    "runs": [
      0
    ],
    "results": [
      "string"
    ],
    "tags": [
      {
        "title": "string",
        "internal_id": 0
      }
    ],
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Defect.|[DefectResponse](#schemadefectresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth