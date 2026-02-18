# Get Attachment

GET /attachment/{hash}

Get attachment by Hash.

This method allows to retrieve attachment by Hash.

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hash|path|string|true|Hash.|

### Example responses

```json
{
  "status": true,
  "result": {
    "hash": "string",
    "file": "string",
    "mime": "string",
    "size": 0,
    "extension": "string",
    "full_path": "http://example.com",
    "url": "string"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Single attachment.|[AttachmentResponse](#schemaattachmentresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth