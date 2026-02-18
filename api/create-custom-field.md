# Create Custom Field

POST /custom_field

Create new Custom Field.

This method allows to create custom field.

### Body parameter

```json
{
  "title": "string",
  "value": [
    {
      "id": 0,
      "title": "string"
    }
  ],
  "entity": 2,
  "type": 9,
  "placeholder": "string",
  "default_value": "string",
  "is_filterable": true,
  "is_visible": true,
  "is_required": true,
  "is_enabled_for_all_projects": true,
  "projects_codes": [
    "string"
  ]
}
```

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CustomFieldCreate](#schemacustomfieldcreate)|true|none|

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Created Custom Field id.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth