# Get Run

This method allows to retrieve a specific test run.

### Path

`GET /run/{code}/{id}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `id` | `integer` | | ID of test run. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single test run. |

## RunResponse

```json
{
  "status": true,
  "result": {
    "id": 1,
    "title": "Test Run",
    "description": "Description for Test Run",
    "status": 0,
    "start_time": "2017-10-21T11:09:40+00:00",
    "end_time": "2017-10-21T11:09:40+00:00",
    "public": true,
    "author": {
      "id": 1,
      "title": "Author title",
      "email": "email@example.com"
    },
    "milestone": {
      "id": 1,
      "title": "Milestone title"
    },
    "environment": {
      "id": 1,
      "title": "Environment title",
      "description": "Environment description",
      "slug": "ENV"
    },
    "custom_fields": [
      {
        "id": 1,
        "value": "Custom field value"
      }
    ],
    "stats": {
      "total": 10,
      "untested": 10,
      "passed": 10,
      "failed": 10,
      "blocked": 10,
      "skipped": 10,
      "retest": 10,
      "in_progress": 10
    },
    "cases": [
      {
        "case_id": 10,
        "status": "passed"
      }
    ],
    "url": "https://qase.io/run/1",
    "external_issues": [
      {
        "url": "https://external.issue",
        "issues": [
          {
            "id": "JIRA-1",
            "external_id": "123"
          }
        ]
      }
    ]
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

## Environment

```json
{
  "id": 1,
  "title": "Environment title",
  "description": "Environment description",
  "slug": "ENV"
}
```

## RunMilestone

```json
{
  "id": 1,
  "title": "Milestone title"
}
```

## RunexternalIssues

```json
{
  "url": "https://external.issue",
  "issues": [
    {
      "id": "JIRA-1",
      "external_id": "123"
    }
  ]
}
```

## RunStats

```json
{
  "total": 10,
  "untested": 10,
  "passed": 10,
  "failed": 10,
  "blocked": 10,
  "skipped": 10,
  "retest": 10,
  "in_progress": 10
}
```

## Author

```json
{
  "id": 1,
  "title": "Author title",
  "email": "email@example.com"
}
```

## PlanDetailedAllOfCases

```json
{
  "case_id": 10,
  "status": "passed"
}
```

## Run

```json
{
  "id": 1,
  "title": "Test Run",
  "description": "Description for Test Run",
  "status": 0,
  "start_time": "2017-10-21T11:09:40+00:00",
  "end_time": "2017-10-21T11:09:40+00:00",
  "public": true,
  "author": {
    "id": 1,
    "title": "Author title",
    "email": "email@example.com"
  },
  "milestone": {
    "id": 1,
    "title": "Milestone title"
  },
  "environment": {
    "id": 1,
    "title": "Environment title",
    "description": "Environment description",
    "slug": "ENV"
  },
  "custom_fields": [
    {
      "id": 1,
      "value": "Custom field value"
    }
  ],
  "stats": {
    "total": 10,
    "untested": 10,
    "passed": 10,
    "failed": 10,
    "blocked": 10,
    "skipped": 10,
    "retest": 10,
    "in_progress": 10
  },
  "cases": [
    {
      "case_id": 10,
      "status": "passed"
    }
  ],
  "url": "https://qase.io/run/1",
  "external_issues": [
    {
      "url": "https://external.issue",
      "issues": [
        {
          "id": "JIRA-1",
          "external_id": "123"
        }
      ]
    }
  ]
}
```