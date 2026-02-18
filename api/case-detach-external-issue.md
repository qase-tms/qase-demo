# Case Detach External Issue

POST /case/{code}/external-issue/detach

Detach external issues from test cases.

This method allows to detach the external issues from the test cases.

### Body parameter

```json
{
  "type": "jira-cloud",
  "links": [
    {
      "case_id": 0,
      "external_issues": [
        "string"
      ]
    }
  ]
}
```

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|object|true|none|
|» type|body|string|true|The type of the external issue.|
|» links|body|[object]|true|A list of links.|
|» links[].case_id|body|integer|true|The ID of the test case.|
|» links[].external_issues|body|[string]|true|A list of external issue IDs.|

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.etf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth