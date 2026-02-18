# Get Result

This method allows to retrieve a specific test result.

### Path

`GET /result/{code}/{hash}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |
| `hash` | `string` | | Hash of test result. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single test result. |

## ResultResponse

```json
{
  "status": true,
  "result": {
    "hash": "235a0f0d4b1a4597402a7853676dfb37",
    "comment": "Test suite run.",
    "status": "passed",
    "start_time": "2017-10-21T11:09:40+00:00",
    "end_time": "2017-10-21T11:09:40+00:00",
    "full_start_time": "2017-10-21T11:09:40+00:00",
    "full_end_time": "2017-10-21T11:09:40+00:00",
    "time_ms": 100,
    "steps": [
      {
        "position": 1,
        "status": "passed",
        "start_time": "2017-10-21T11:09:40+00:00",
        "end_time": "2017-10-21T11:09:40+00:00",
        "full_start_time": "2017-10-21T11:09:40+00:00",
        "full_end_time": "2017-10-21T11:09:40+00:00",
        "time_ms": 100
      }
    ],
    "attachments": [
      {
        "hash": "950a99059f21f1852033c4153b035136",
        "mime": "image/png",
        "size": 100,
        "filename": "test.png",
        "url": "https://image.url"
      }
    ],
    "stacktrace": "stacktrace",
    "case": {
      "id": 1,
      "title": "Case title",
      "position": 1,
      "suite_id": 1,
      "description": "Case description",
      "preconditions": "Case preconditions",
      "postconditions": "Case postconditions",
      "links": [
        {
          "url": "https://example.com",
          "title": "Example Link",
          "type": "other"
        }
      ]
    },
    "run_id": 1,
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
    "url": "https://qase.io/result/1"
  }
}
```

## Attachment

```json
{
  "hash": "950a99059f21f1852033c4153b035136",
  "mime": "image/png",
  "size": 100,
  "filename": "test.png",
  "url": "https://image.url"
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

## CustomFieldValue

```json
{
  "id": 1,
  "value": "Custom field value"
}
```

## TestStepResult

```json
{
  "position": 1,
  "status": "passed",
  "start_time": "2017-10-21T11:09:40+00:00",
  "end_time": "2017-10-21T11:09:40+00:00",
  "full_start_time": "2017-10-21T11:09:40+00:00",
  "full_end_time": "2017-10-21T11:09:40+00:00",
  "time_ms": 100
}
```

## TestCaseExternalIssuesLinksInner

```json
{
  "url": "https://example.com",
  "title": "Example Link",
  "type": "other"
}
```

## TestCase

```json
{
  "id": 1,
  "title": "Case title",
  "position": 1,
  "suite_id": 1,
  "description": "Case description",
  "preconditions": "Case preconditions",
  "postconditions": "Case postconditions",
  "links": [
    {
      "url": "https://example.com",
      "title": "Example Link",
      "type": "other"
    }
  ]
}
```

## Result

```json
{
  "hash": "235a0f0d4b1a4597402a7853676dfb37",
  "comment": "Test suite run.",
  "status": "passed",
  "start_time": "2017-10-21T11:09:40+00:00",
  "end_time": "2017-10-21T11:09:40+00:00",
  "full_start_time": "2017-10-21T11:09:40+00:00",
  "full_end_time": "2017-10-21T11:09:40+00:00",
  "time_ms": 100,
  "steps": [
    {
      "position": 1,
      "status": "passed",
      "start_time": "2017-10-21T11:09:40+00:00",
      "end_time": "2017-10-21T11:09:40+00:00",
      "full_start_time": "2017-10-21T11:09:40+00:00",
      "full_end_time": "2017-10-21T11:09:40+00:00",
      "time_ms": 100
    }
  ],
  "attachments": [
    {
      "hash": "950a99059f21f1852033c4153b035136",
      "mime": "image/png",
      "size": 100,
      "filename": "test.png",
      "url": "https://image.url"
    }
  ],
  "stacktrace": "stacktrace",
  "case": {
    "id": 1,
    "title": "Case title",
    "position": 1,
    "suite_id": 1,
    "description": "Case description",
    "preconditions": "Case preconditions",
    "postconditions": "Case postconditions",
    "links": [
      {
        "url": "https://example.com",
        "title": "Example Link",
        "type": "other"
      }
    ]
  },
  "run_id": 1,
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
  "url": "https://qase.io/result/1"
}
```