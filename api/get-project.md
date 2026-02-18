# Get Project

This method allows to retrieve a specific project.

### Path

`GET /project/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A single project. |

## ProjectResponse

```json
{
  "status": true,
  "result": {
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