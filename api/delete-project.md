# Delete Project

This method allows to delete a specific project.

### Path

`DELETE /project/{code}`

### Path Parameters

| Parameter | Type | Default | Description |
| --------- | ---- | ------- | ----------- |
| `code` | `string` | | Code of project. |

### Responses

| Status | Description |
| ------ | ----------- |
| `200` | A result of project deletion. |

## ProjectCodeResponse

```json
{
  "status": true,
  "result": {
    "code": "TP" 
  }
}
```