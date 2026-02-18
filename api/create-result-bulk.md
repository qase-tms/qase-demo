# Create Result Bulk

This method allows to create a lot of test run results at once.

If you try to send more than 2,000 results in a single bulk request, you will receive an error with code 413 - Payload Too Large.

If there is no free space left in your team account, when attempting to upload an attachment, e.g., through reporters, you will receive an error with code 507 - Insufficient Storage.

### Path

`POST /result/{code}/{id}/bulk`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | Identifier of the test run. |

### Request Body

```json
{
  "results": [
    {
      "case_id": 0,
      "case": {
        "title": "string",
        "suite_title": "string",
        "description": "string",
        "preconditions": "string",
        "postconditions": "string",
        "layer": "string",
        "severity": "string",
        "priority": "string"
      },
      "status": "string",
      "start_time": 0,
      "time": 31536000,
      "time_ms": 31536000000,
      "defect": true,
      "attachments": [
        "string"
      ],
      "stacktrace": "string",
      "comment": "string",
      "param": {
        "property1": "string",
        "property2": "string"
      },
      "param_groups": [
        ["string"]
      ],
      "steps": [
        {
          "position": 0,
          "status": "passed",
          "comment": "string",
          "attachments": ["string"],
          "action": "string",
          "expected_result": "string",
          "data": "string",
          "steps": [{}]
        }
      ],
      "author_id": 0
    }
  ]
}
```

### Request Body Parameters

| Name | In | Type | Required | Description |
| ---- | -- | ---- | -------- | ----------- |
| `code` | path | string | true | Code of project, where to search entities. |
| `id` | path | integer | true | Identifier. |
| `results` | body | array | true | Array of test run results to create. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result. |
| `400` | Bad Request. |
| `401` | Unauthorized. |
| `403` | Forbidden. |
| `404` | Not Found. |
| `413` | Payload Too Large. |
| `422` | Unprocessable Entity. |
| `429` | Too Many Requests. |

```json
{
  "status": true
}
```
