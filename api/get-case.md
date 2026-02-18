# Get Case

GET /case/{code}/{id}

Get a specific test case.

This method allows to retrieve a specific test case.

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|include|query|string|false|A list of entities to include in response separated by comma. Possible values: external_issues.|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

#### Detailed descriptions

**include**: A list of entities to include in response separated by comma. Possible values: external_issues.

### Example responses

```json
{
  "status": true,
  "result": {
    "id": 0,
    "position": 0,
    "title": "string",
    "description": "string",
    "preconditions": "string",
    "postconditions": "string",
    "severity": 0,
    "priority": 0,
    "type": 0,
    "layer": 0,
    "is_flaky": 0,
    "behavior": 0,
    "automation": 0,
    "status": 0,
    "milestone_id": 0,
    "suite_id": 0,
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
    "steps_type": "string",
    "steps": [
      {
        "hash": "string",
        "shared_step_hash": "string",
        "shared_step_nested_hash": "string",
        "position": 0,
        "action": "string",
        "expected_result": "string",
        "data": "string",
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "steps": [
          {}
        ]
      }
    ],
    "params": [
      null
    ],
    "parameters": [
      {
        "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a",
        "type": "single",
        "item": {
          "title": "string",
          "values": [
            "string"
          ]
        }
      }
    ],
    "tags": [
      {
        "title": "string",
        "internal_id": 0
      }
    ],
    "member_id": 0,
    "author_id": 0,
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "deleted": "2021-12-30T19:23:59.000000Z",
    "created": "2021-12-30T19:23:59.000000Z",
    "updated": "2021-12-30T19:23:59.000000Z",
    "external_issues": [
      {
        "type": "string",
        "issues": [
          {
            "id": "string",
            "link": "string"
          }
        ]
      }
    ]
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Test Case.|[TestCaseResponse](#schematestcaseresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth