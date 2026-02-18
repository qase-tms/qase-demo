# Create Case

POST /case/{code}

Create a new test case.

This method allows to create a test case.

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
  },
  "created_at": "string",
  "updated_at": "string"
}
```

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|object|false|none|
|» description|body|string|false|A description of the test case.|
|» preconditions|body|string|false|Preconditions for the test case.|
|» postconditions|body|string|false|Postconditions for the test case.|
|» title|body|string|true|The title of the test case.|
|» severity|body|integer|true|The severity of the test case.|
|» priority|body|integer|true|The priority of the test case.|
|» behavior|body|integer|true|The behavior of the test case.|
|» type|body|integer|true|The type of the test case.|
|» layer|body|integer|true|The layer of the test case.|
|» is_flaky|body|integer|true|Whether the test case is flaky.|
|» suite_id|body|integer|true|The ID of the test suite.|
|» milestone_id|body|integer|true|The ID of the milestone.|
|» automation|body|integer|true|The automation status of the test case.|
|» status|body|integer|true|The status of the test case.|
|» attachments|body|[string]|false|A list of attachment hashes.|
|» steps|body|[object]|false|A list of test steps.|
|» steps[].action|body|string|true|The action of the step.|
|» steps[].expected_result|body|string|false|The expected result of the step.|
|» steps[].data|body|string|false|The test data for the step.|
|» steps[].position|body|integer|false|The position of the step.|
|» steps[].attachments|body|[string]|false|A list of attachment hashes for the step.|
|» steps[].steps|body|[object]|false|Nested steps.|
|» tags|body|[string]|false|A list of tags.|
|» params|body|object|false|Parameters for the test case.|
|» parameters|body|[object]|false|Shared parameters.|
|» parameters[].shared_id|body|string|false|The ID of the shared parameter.|
|» custom_field|body|object|false|Custom fields.|
|» created_at|body|string|false|The creation date of the test case.|
|» updated_at|body|string|false|The last update date of the test case.|

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth