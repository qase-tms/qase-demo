# Update Run

This method allows to update a specific test run.

### Path

`PATCH /run/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test run. |

### Request Body

## Runupdate

```json
{
  "title": "Test Run",
  "description": "Description for Test Run",
  "cases": [
    1,
    2,
    3
  ],
  "environment_id": 1,
  "milestone_id": 1,
  "plan_id": 1,
  "tags": [
    "tag1",
    "tag2"
  ],
  "preconditions": "preconditions",
  "postconditions": "postconditions",
  "start_time": "2017-10-21T11:09:40+00:00",
  "end_time": "2017-10-21T11:09:40+00:00",
  "block_until_end": true,
  "custom_fields": [
    {
      "id": 1,
      "value": "Custom field value"
    }
  ],
  "external_issues": [
    {
      "id": "JIRA-1",
      "external_id": "123"
    }
  ]
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of test run update. |

## IdResponse

```json
{
  "status": true,
  "result": {
    "id": 1
  }
}
```

## CustomFieldValue

```json
{
  "id": 1,
  "value": "Custom field value"
}
```

## RunExternalIssueIssuesInner

```json
{
  "id": "JIRA-1",
  "external_id": "123"
}
```