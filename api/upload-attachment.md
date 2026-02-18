# Upload Attachment

POST /attachment/{code}

Upload attachment.

This method allows to upload attachment to Qase.
Max upload size:
* Up to 32 Mb per file
* Up to 128 Mb per single request
* Up to 20 files per single request

If there is no free space left in your team account,
you will receive an error with code 507 - Insufficient Storage.

### Body parameter

```yaml
"file[]":
  - string

```

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|object|false|none|
|» file[]|body|[string]|false|none|

### Example responses

```json
{
  "status": true,
  "result": [
    {
      "hash": "string",
      "filename": "string",
      "mime": "string",
      "extension": "string",
      "url": "string",
      "team": "string"
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|An attachments.|[AttachmentUploadsResponse](#schemaattachmentuploadsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|413|[Payload Too Large](https://tools.ietf.org/html/rfc7231#section-6.5.11)|Payload Too Large.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth