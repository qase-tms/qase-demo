# Case Attach External Issue

This method allows to attach external issues to test cases.

### Path

`POST /case/{code}/external-issue/attach`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

| Name | Type | Required | Description |
| ---- | ---- | -------- | ----------- |
| `type` | `string` | Yes | The type of the external issue (e.g. `jira-cloud`, `jira-server`). |
| `links` | `array` | Yes | A list of links. |
| `links[].case_id` | `integer` | Yes | The ID of the test case. |
| `links[].external_issues` | `array` | Yes | A list of external issue IDs. |

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

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result. |
| `400` | Bad Request. |
| `401` | Unauthorized. |
| `403` | Forbidden. |
| `404` | Not Found. |
| `422` | Unprocessable Entity. |
| `429` | Too Many Requests. |

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```
