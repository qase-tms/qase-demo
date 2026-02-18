# Run Update External Issue

This method allows you to update links between test runs and external issues (such as Jira tickets).

You can use this endpoint to:
- Link test runs to external issues by providing the external issue identifier (e.g., "PROJ-1234")
- Update existing links by providing a new external issue identifier
- Remove existing links by setting the `external_issue` field to null

**Important**: Each test run can have only one link with an external issue. If a test run already has an external issue link, providing a new `external_issue` value will replace the existing link.

The endpoint supports both Jira Cloud and Jira Server integrations. Each request can update multiple test run links in a single operation.

### Path

`POST /run/{code}/external-issue`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Request Body

```json
{
  "type": "jira-cloud",
  "links": [
    {
      "run_id": 0,
      "external_issue": "string"
    }
  ]
}
```

### Request Body Parameters

| Name | In | Type | Required | Description |
| ---- | -- | ---- | -------- | ----------- |
| `type` | body | string | true | Integration type. Enum: `jira-cloud`, `jira-server`. |
| `links` | body | array | true | Array of external issue links. Each test run (`run_id`) can have only one external issue link. |
| `links[].run_id` | body | integer | true | ID of the test run. |
| `links[].external_issue` | body | string or null | false | An external issue identifier, e.g. "PROJ-1234". Set to null to remove the link. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | OK. |
| `400` | Bad Request. |
| `401` | Unauthorized. |
| `403` | Forbidden. |
| `404` | Not Found. |
| `429` | Too Many Requests. |
