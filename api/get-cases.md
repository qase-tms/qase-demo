# Get Cases

GET /case/{code}

Get all test cases.

This method allows to retrieve all test cases stored in selected project.

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|search|query|string|false|Provide a string that will be used to search by name.|
|milestone_id|query|integer|false|ID of milestone.|
|suite_id|query|integer|false|ID of test suite.|
|severity|query|string|false|A list of severity values separated by comma.|
|priority|query|string|false|A list of priority values separated by comma.|
|type|query|string|false|A list of type values separated by comma.|
|behavior|query|string|false|A list of behavior values separated by comma.|
|automation|query|string|false|A list of values separated by comma.|
|status|query|string|false|A list of values separated by comma. Possible values: actual, draft deprecated|
|external_issues[type]|query|string|false|An integration type.|
|external_issues[ids][]|query|array[string]|false|A list of issue IDs.|
|include|query|string|false|A list of entities to include in response separated by comma. Possible values: external_issues.|
|code|path|string|true|Code of project, where to search entities.|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

#### Detailed descriptions

**severity**: A list of severity values separated by comma.
Possible values: undefined, blocker, critical,
major, normal, minor, trivial

**priority**: A list of priority values separated by comma.
Possible values: undefined, high, medium, low

**type**: A list of type values separated by comma.
Possible values: other, functional smoke, regression,
security, usability, performance, acceptance

**behavior**: A list of behavior values separated by comma.
Possible values: undefined, positive negative, destructive

**automation**: A list of values separated by comma.
Possible values: is-not-automated, automated to-be-automated

**status**: A list of values separated by comma. Possible values: actual, draft deprecated

**external_issues[type]**: An integration type.

**include**: A list of entities to include in response separated by comma. Possible values: external_issues.

#### Enumerated Values

|Parameter|Value|
|---|---|
|external_issues[type]|asana|
|external_issues[type]|azure-devops|
|external_issues[type]|clickup-app|
|external_issues[type]|github-app|
|external_issues[type]|gitlab-app|
|external_issues[type]|jira-cloud|
|external_issues[type]|jira-server|
|external_issues[type]|linear|
|external_issues[type]|monday|
|external_issues[type]|redmine-app|
|external_issues[type]|trello-app|
|external_issues[type]|youtrack-app|

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
        "description": "string",
        "preconditions": "string",
        "postconditions": "string",
        "severity": "blocker",
        "priority": "high",
        "type": "other",
        "milestone_id": 0,
        "suite_id": 0,
        "layer": "e2e",
        "is_flaky": true,
        "behavior": "positive",
        "automation": "is_not_automated",
        "status": "actual",
        "created_at": "2026-02-14T06:05:03.957Z",
        "updated_at": "2026-02-14T06:05:03.957Z",
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "extension": "string",
            "hash": "string",
            "url": "string"
          }
        ],
        "steps": [
          {
            "position": 0,
            "action": "string",
            "expected_result": "string",
            "data": "string",
            "attachments": [
              {
                "size": 0,
                "mime": "string",
                "filename": "string",
                "extension": "string",
                "hash": "string",
                "url": "string"
              }
            ]
          }
        ],
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "tags": [
          {
            "id": 0,
            "title": "string"
          }
        ],
        "external_issues": [
          {
            "id": "string",
            "type": "jira"
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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all test cases.|[TestCaseListResponse](#schematestcaselistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Required.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth