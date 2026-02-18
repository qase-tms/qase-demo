# Get Custom Field

GET /custom_field/{id}

Get a specific custom field.

This method allows to retrieve a specific custom field.

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
    "title": "string",
    "entity": "string",
    "type": "string",
    "placeholder": "string",
    "default_value": "string",
    "value": "string",
    "is_required": true,
    "is_visible": true,
    "is_filterable": true,
    "is_enabled_for_all_projects": true,
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "projects_codes": [
      "string"
    ]
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Single Custom Field.|[CustomFieldResponse](#schemacustomfieldresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth