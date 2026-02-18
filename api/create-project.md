# Create Project

This method allows to create a new project.

### Path

`POST /project`

### Request Body

## ProjectCreate

```json
{
  "title": "Project name",
  "code": "TP",
  "description": "Project description",
  "access": "private",
  "group": "0a103c14-2396-4161-b1e9-74112046427b",
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
  }
}
```

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of project creation. |

## ProjectCodeResponse

```json
{
  "status": true,
  "result": {
    "code": "TP" 
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

## ProjectAccess

```json
"private"
```