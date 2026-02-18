# Get All Runs

This method allows to retrieve all test runs stored in selected project.

### Path

`GET /run/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all test runs. | 

## RunListResponse

```json
{
  "status": true,
  "result": {
    "total": 100,
    "filtered": 100,
    "count": 20,
    "entities": [
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
        "url": "https://qase.io/run/1"
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
  "url": "https://qase.io/run/1"
}
```