# Update Case

PATCH /case/{code}/{id}

Update test case.

This method updates a test case.

### Body parameter

```json
{
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "title": "string",
  "severity": 0,
  "priority": 0,
  "behavior": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "suite_id": 0,
  "milestone_id": 0,
  "automation": 0,
  "status": 0,
  "attachments": [
    "string"
  ],
  "steps": [
    {
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "position": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {}
      ]
    }
  ],
  "tags": [
    "string"
  ],
  "params": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  },
  "parameters": [
    {
      "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
    }
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  }
}
```

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[TestCaseUpdate](#schematestcaseupdate)|true|none|

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth