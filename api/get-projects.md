# Get All Projects

This method allows to retrieve all projects stored in selected project.

### Path

`GET /project`

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A list of all projects. |

## ProjectListResponse

```json
{
  "status": true,
  "result": {
    "total": 100,
    "filtered": 100,
    "count": 20,
    "entities": [
      {
        "title": "Project name",
        "code": "TP",
        "counts": {
          "cases": 10,
          "suites": 10,
          "runs": {
            "total": 10,
            "active": 10
          },
          "defects": {
            "total": 10,
            "open": 10
          }
        },
        "created_at": "2017-10-21T11:09:40+00:00",
        "updated_at": "2017-10-21T11:09:40+00:00"
      }
    ]
  }
}
```

## ProjectCountsDefects

```json
{
  "total": 10,
  "open": 10
}
```

## ProjectCountsRuns

```json
{
  "total": 10,
  "active": 10
}
```

## ProjectCounts

```json
{
  "cases": 10,
  "suites": 10,
  "runs": {
    "total": 10,
    "active": 10
  },
  "defects": {
    "total": 10,
    "open": 10
  }
}
```

## Project

```json
{
  "title": "Project name",
  "code": "TP",
  "counts": {
    "cases": 10,
    "suites": 10,
    "runs": {
      "total": 10,
      "active": 10
    },
    "defects": {
      "total": 10,
      "open": 10
    }
  },
  "created_at": "2017-10-21T11:09:40+00:00",
  "updated_at": "2017-10-21T11:09:40+00:00"
}
```