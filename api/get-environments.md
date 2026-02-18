# Get Environments

GET /environment/{code}

Get all environments.

This method allows to retrieve all environments stored in selected project.

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|search|query|string|false|A search string.|
|slug|query|string|false|A search string. |
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

#### Detailed descriptions

**search**: A search string.
Will return all environments with titles containing provided string.

**slug**: A search string. 
Will return all environments with slugs equal to provided string.

### Example responses

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "id": 0,
        "title": "string",
        "description": "string",
        "slug": "string",
        "host": "string"
      }
    ]
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all environments.|[EnvironmentListResponse](#schemaenvironmentlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth