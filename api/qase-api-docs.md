---
title: Qase.io TestOps API v1 v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="qase-io-testops-api-v1">Qase.io TestOps API v1 v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Qase TestOps API v1 Specification.

Base URLs:

* <a href="https://api.qase.io/v1">https://api.qase.io/v1</a>

<a href="https://qase.io/terms">Terms of service</a>
Email: <a href="mailto:support@qase.io">Qase.io</a> Web: <a href="https://qase.io">Qase.io</a> 
License: <a href="https://github.com/qase-tms/specs/blob/master/LICENSE">Apache 2.0</a>

# Authentication

* API Key (TokenAuth)
    - Parameter Name: **Token**, in: header. 

<h1 id="qase-io-testops-api-v1-attachments">attachments</h1>

## get-attachments

<a id="opIdget-attachments"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/attachment \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/attachment HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/attachment',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/attachment',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/attachment', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/attachment', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/attachment");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/attachment", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /attachment`

*Get all attachments*

This method allows to retrieve attachments.

<h3 id="get-attachments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "hash": "string",
        "file": "string",
        "mime": "string",
        "size": 0,
        "extension": "string",
        "full_path": "http://example.com",
        "url": "string"
      }
    ]
  }
}
```

<h3 id="get-attachments-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all attachments.|[AttachmentListResponse](#schemaattachmentlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|413|[Payload Too Large](https://tools.ietf.org/html/rfc7231#section-6.5.11)|Payload Too Large.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## upload-attachment

<a id="opIdupload-attachment"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/attachment/{code} \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/attachment/{code} HTTP/1.1
Host: api.qase.io
Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "file[]": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/attachment/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/attachment/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/attachment/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/attachment/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/attachment/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/attachment/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /attachment/{code}`

*Upload attachment*

This method allows to upload attachment to Qase.
Max upload size:
* Up to 32 Mb per file
* Up to 128 Mb per single request
* Up to 20 files per single request

If there is no free space left in your team account,
you will receive an error with code 507 - Insufficient Storage.

> Body parameter

```yaml
"file[]":
  - string

```

<h3 id="upload-attachment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|object|false|none|
|» file[]|body|[string]|false|none|

> Example responses

> 200 Response

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

<h3 id="upload-attachment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|An attachments.|[AttachmentUploadsResponse](#schemaattachmentuploadsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|413|[Payload Too Large](https://tools.ietf.org/html/rfc7231#section-6.5.11)|Payload Too Large.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-attachment

<a id="opIdget-attachment"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/attachment/{hash} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/attachment/{hash} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/attachment/{hash}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/attachment/{hash}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/attachment/{hash}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/attachment/{hash}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/attachment/{hash}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/attachment/{hash}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /attachment/{hash}`

*Get attachment by Hash*

This method allows to retrieve attachment by Hash.

<h3 id="get-attachment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hash|path|string|true|Hash.|

> Example responses

> 200 Response

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

<h3 id="get-attachment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Single attachment.|[AttachmentResponse](#schemaattachmentresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-attachment

<a id="opIddelete-attachment"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/attachment/{hash} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/attachment/{hash} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/attachment/{hash}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/attachment/{hash}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/attachment/{hash}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/attachment/{hash}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/attachment/{hash}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/attachment/{hash}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /attachment/{hash}`

*Remove attachment by Hash*

This method allows to remove attachment by Hash.

<h3 id="delete-attachment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hash|path|string|true|Hash.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "hash": "string"
  }
}
```

<h3 id="delete-attachment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[HashResponse](#schemahashresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-authors">authors</h1>

## get-authors

<a id="opIdget-authors"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/author \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/author HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/author',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/author',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/author', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/author', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/author");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/author", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /author`

*Get all authors*

This method allows to retrieve all authors in selected project.

<h3 id="get-authors-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|search|query|string|false|Provide a string that will be used to search by name.|
|type|query|string|false|none|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|type|app|
|type|user|

> Example responses

> 200 Response

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
        "author_id": 0,
        "entity_type": "string",
        "entity_id": 0,
        "email": "string",
        "name": "string",
        "is_active": true
      }
    ]
  }
}
```

<h3 id="get-authors-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Author list.|[AuthorListResponse](#schemaauthorlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-author

<a id="opIdget-author"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/author/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/author/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/author/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/author/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/author/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/author/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/author/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/author/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /author/{id}`

*Get a specific author*

This method allows to retrieve a specific author.

<h3 id="get-author-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "author_id": 0,
    "entity_type": "string",
    "entity_id": 0,
    "email": "string",
    "name": "string",
    "is_active": true
  }
}
```

<h3 id="get-author-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|An author.|[AuthorResponse](#schemaauthorresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-cases">cases</h1>

## get-cases

<a id="opIdget-cases"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/case/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/case/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/case/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/case/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/case/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/case/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/case/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/case/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /case/{code}`

*Get all test cases*

This method allows to retrieve all test cases stored in selected project.

<h3 id="get-cases-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|search|query|string|false|Provide a string that will be used to search by name.|
|milestone_id|query|integer|false|ID of milestone.|
|suite_id|query|integer|false|ID of test suite.|
|severity|query|string|false|A list of severity values separated by comma.|
|priority|query|string|false|A list of priority values separated by comma.|
|type|query|string|false|A list of type values separated by comma.|
|behavior|query|string|false|A list of behavior values separated by comma.|
|automation|query|string|false|A list of values separated by comma.|
|status|query|string|false|A list of values separated by comma. Possible values: actual, draft deprecated|
|external_issues[type]|query|string|false|An integration type.|
|external_issues[ids][]|query|array[string]|false|A list of issue IDs.|
|include|query|string|false|A list of entities to include in response separated by comma. Possible values: external_issues.|
|code|path|string|true|Code of project, where to search entities.|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

#### Detailed descriptions

**severity**: A list of severity values separated by comma.
Possible values: undefined, blocker, critical,
major, normal, minor, trivial

**priority**: A list of priority values separated by comma.
Possible values: undefined, high, medium, low

**type**: A list of type values separated by comma.
Possible values: other, functional smoke, regression,
security, usability, performance, acceptance

**behavior**: A list of behavior values separated by comma.
Possible values: undefined, positive negative, destructive

**automation**: A list of values separated by comma.
Possible values: is-not-automated, automated to-be-automated

**status**: A list of values separated by comma. Possible values: actual, draft deprecated

**external_issues[type]**: An integration type.

**include**: A list of entities to include in response separated by comma. Possible values: external_issues.

#### Enumerated Values

|Parameter|Value|
|---|---|
|external_issues[type]|asana|
|external_issues[type]|azure-devops|
|external_issues[type]|clickup-app|
|external_issues[type]|github-app|
|external_issues[type]|gitlab-app|
|external_issues[type]|jira-cloud|
|external_issues[type]|jira-server|
|external_issues[type]|linear|
|external_issues[type]|monday|
|external_issues[type]|redmine-app|
|external_issues[type]|trello-app|
|external_issues[type]|youtrack-app|

> Example responses

> 200 Response

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
        "position": 0,
        "title": "string",
        "description": "string",
        "preconditions": "string",
        "postconditions": "string",
        "severity": 0,
        "priority": 0,
        "type": 0,
        "layer": 0,
        "is_flaky": 0,
        "behavior": 0,
        "automation": 0,
        "status": 0,
        "milestone_id": 0,
        "suite_id": 0,
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "steps_type": "string",
        "steps": [
          {
            "hash": "string",
            "shared_step_hash": "string",
            "shared_step_nested_hash": "string",
            "position": 0,
            "action": "string",
            "expected_result": "string",
            "data": "string",
            "attachments": [
              {
                "size": 0,
                "mime": "string",
                "filename": "string",
                "url": "http://example.com"
              }
            ],
            "steps": [
              {}
            ]
          }
        ],
        "params": [
          null
        ],
        "parameters": [
          {
            "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a",
            "type": "single",
            "item": {
              "title": "string",
              "values": [
                "string"
              ]
            }
          }
        ],
        "tags": [
          {
            "title": "string",
            "internal_id": 0
          }
        ],
        "member_id": 0,
        "author_id": 0,
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00",
        "deleted": "2021-12-30T19:23:59.000000Z",
        "created": "2021-12-30T19:23:59.000000Z",
        "updated": "2021-12-30T19:23:59.000000Z",
        "external_issues": [
          {
            "type": "string",
            "issues": [
              {
                "id": "string",
                "link": "string"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

<h3 id="get-cases-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all cases.|[TestCaseListResponse](#schematestcaselistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Required.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-case

<a id="opIdcreate-case"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/case/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/case/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "title": "string",
  "severity": 0,
  "priority": 0,
  "behavior": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "suite_id": 0,
  "milestone_id": 0,
  "automation": 0,
  "status": 0,
  "attachments": [
    "string"
  ],
  "steps": [
    {
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "position": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {}
      ]
    }
  ],
  "tags": [
    "string"
  ],
  "params": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  },
  "parameters": [
    {
      "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
    }
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "created_at": "string",
  "updated_at": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/case/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/case/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/case/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/case/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/case/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/case/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /case/{code}`

*Create a new test case*

This method allows to create a new test case in selected project.

> Body parameter

```json
{
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "title": "string",
  "severity": 0,
  "priority": 0,
  "behavior": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "suite_id": 0,
  "milestone_id": 0,
  "automation": 0,
  "status": 0,
  "attachments": [
    "string"
  ],
  "steps": [
    {
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "position": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {}
      ]
    }
  ],
  "tags": [
    "string"
  ],
  "params": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  },
  "parameters": [
    {
      "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
    }
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "created_at": "string",
  "updated_at": "string"
}
```

<h3 id="create-case-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[TestCaseCreate](#schematestcasecreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-case-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-case

<a id="opIdget-case"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/case/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/case/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/case/{code}/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/case/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/case/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/case/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/case/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/case/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /case/{code}/{id}`

*Get a specific test case*

This method allows to retrieve a specific test case.

<h3 id="get-case-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|include|query|string|false|A list of entities to include in response separated by comma. Possible values: external_issues.|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

#### Detailed descriptions

**include**: A list of entities to include in response separated by comma. Possible values: external_issues.

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "position": 0,
    "title": "string",
    "description": "string",
    "preconditions": "string",
    "postconditions": "string",
    "severity": 0,
    "priority": 0,
    "type": 0,
    "layer": 0,
    "is_flaky": 0,
    "behavior": 0,
    "automation": 0,
    "status": 0,
    "milestone_id": 0,
    "suite_id": 0,
    "custom_fields": [
      {
        "id": 0,
        "value": "string"
      }
    ],
    "attachments": [
      {
        "size": 0,
        "mime": "string",
        "filename": "string",
        "url": "http://example.com"
      }
    ],
    "steps_type": "string",
    "steps": [
      {
        "hash": "string",
        "shared_step_hash": "string",
        "shared_step_nested_hash": "string",
        "position": 0,
        "action": "string",
        "expected_result": "string",
        "data": "string",
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "steps": [
          {}
        ]
      }
    ],
    "params": [
      null
    ],
    "parameters": [
      {
        "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a",
        "type": "single",
        "item": {
          "title": "string",
          "values": [
            "string"
          ]
        }
      }
    ],
    "tags": [
      {
        "title": "string",
        "internal_id": 0
      }
    ],
    "member_id": 0,
    "author_id": 0,
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "deleted": "2021-12-30T19:23:59.000000Z",
    "created": "2021-12-30T19:23:59.000000Z",
    "updated": "2021-12-30T19:23:59.000000Z",
    "external_issues": [
      {
        "type": "string",
        "issues": [
          {
            "id": "string",
            "link": "string"
          }
        ]
      }
    ]
  }
}
```

<h3 id="get-case-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Test Case.|[TestCaseResponse](#schematestcaseresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-case

<a id="opIddelete-case"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/case/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/case/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/case/{code}/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/case/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/case/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/case/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/case/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/case/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /case/{code}/{id}`

*Delete test case*

This method completely deletes a test case from repository.

<h3 id="delete-case-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="delete-case-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Test Case.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-case

<a id="opIdupdate-case"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/case/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/case/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "title": "string",
  "severity": 0,
  "priority": 0,
  "behavior": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "suite_id": 0,
  "milestone_id": 0,
  "automation": 0,
  "status": 0,
  "attachments": [
    "string"
  ],
  "steps": [
    {
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "position": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {}
      ]
    }
  ],
  "tags": [
    "string"
  ],
  "params": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  },
  "parameters": [
    {
      "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
    }
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/case/{code}/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/case/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/case/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/case/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/case/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/case/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /case/{code}/{id}`

*Update test case*

This method updates a test case.

> Body parameter

```json
{
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "title": "string",
  "severity": 0,
  "priority": 0,
  "behavior": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "suite_id": 0,
  "milestone_id": 0,
  "automation": 0,
  "status": 0,
  "attachments": [
    "string"
  ],
  "steps": [
    {
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "position": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {}
      ]
    }
  ],
  "tags": [
    "string"
  ],
  "params": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  },
  "parameters": [
    {
      "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
    }
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  }
}
```

<h3 id="update-case-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[TestCaseUpdate](#schematestcaseupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="update-case-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Test Case.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## bulk

<a id="opIdbulk"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/case/{code}/bulk \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/case/{code}/bulk HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "cases": [
    {
      "description": "string",
      "preconditions": "string",
      "postconditions": "string",
      "title": "string",
      "severity": 0,
      "priority": 0,
      "behavior": 0,
      "type": 0,
      "layer": 0,
      "is_flaky": 0,
      "suite_id": 0,
      "milestone_id": 0,
      "automation": 0,
      "status": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {
          "action": "string",
          "expected_result": "string",
          "data": "string",
          "position": 0,
          "attachments": [
            "string"
          ],
          "steps": [
            {}
          ]
        }
      ],
      "tags": [
        "string"
      ],
      "params": {
        "property1": [
          "string"
        ],
        "property2": [
          "string"
        ]
      },
      "parameters": [
        {
          "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
        }
      ],
      "custom_field": {
        "property1": "string",
        "property2": "string"
      },
      "created_at": "string",
      "updated_at": "string",
      "id": 0
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/case/{code}/bulk',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/case/{code}/bulk',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/case/{code}/bulk', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/case/{code}/bulk', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/case/{code}/bulk");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/case/{code}/bulk", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /case/{code}/bulk`

*Create test cases in bulk*

This method allows to bulk create new test cases in a project.

> Body parameter

```json
{
  "cases": [
    {
      "description": "string",
      "preconditions": "string",
      "postconditions": "string",
      "title": "string",
      "severity": 0,
      "priority": 0,
      "behavior": 0,
      "type": 0,
      "layer": 0,
      "is_flaky": 0,
      "suite_id": 0,
      "milestone_id": 0,
      "automation": 0,
      "status": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {
          "action": "string",
          "expected_result": "string",
          "data": "string",
          "position": 0,
          "attachments": [
            "string"
          ],
          "steps": [
            {}
          ]
        }
      ],
      "tags": [
        "string"
      ],
      "params": {
        "property1": [
          "string"
        ],
        "property2": [
          "string"
        ]
      },
      "parameters": [
        {
          "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
        }
      ],
      "custom_field": {
        "property1": "string",
        "property2": "string"
      },
      "created_at": "string",
      "updated_at": "string",
      "id": 0
    }
  ]
}
```

<h3 id="bulk-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|object|true|none|
|» cases|body|[allOf]|true|none|
|»» *anonymous*|body|[TestCaseCreate](#schematestcasecreate)|false|none|
|»»» description|body|string|false|none|
|»»» preconditions|body|string|false|none|
|»»» postconditions|body|string|false|none|
|»»» title|body|string|true|none|
|»»» severity|body|integer|false|none|
|»»» priority|body|integer|false|none|
|»»» behavior|body|integer|false|none|
|»»» type|body|integer|false|none|
|»»» layer|body|integer|false|none|
|»»» is_flaky|body|integer|false|none|
|»»» suite_id|body|integer(int64)|false|none|
|»»» milestone_id|body|integer(int64)|false|none|
|»»» automation|body|integer|false|none|
|»»» status|body|integer|false|none|
|»»» attachments|body|[string]|false|A list of Attachment hashes.|
|»»» steps|body|[[TestStepCreate](#schemateststepcreate)]|false|none|
|»»»» action|body|string|false|none|
|»»»» expected_result|body|string|false|none|
|»»»» data|body|string|false|none|
|»»»» position|body|integer|false|none|
|»»»» attachments|body|[string]|false|A list of Attachment hashes.|
|»»»» steps|body|[object]|false|Nested steps may be passed here. Use same structure for them.|
|»»» tags|body|[string]|false|none|
|»»» params|body|object¦null|false|Deprecated, use `parameters` instead.|
|»»»» **additionalProperties**|body|[string]|false|none|
|»»» parameters|body|[oneOf]¦null|false|none|
|»»»» *anonymous*|body|object|false|Shared parameter|
|»»»»» shared_id|body|string(uuid)|true|none|
|»»»» *anonymous*|body|[TestCaseCreate/properties/parameters/items/oneOf/1](#schematestcasecreate/properties/parameters/items/oneof/1)|false|Single parameter|
|»»»»» title|body|string|true|none|
|»»»»» values|body|[string]|true|none|
|»»»» *anonymous*|body|object|false|Group parameter|
|»»»»» items|body|[[TestCaseCreate/properties/parameters/items/oneOf/1](#schematestcasecreate/properties/parameters/items/oneof/1)]|true|[Single parameter]|
|»»» custom_field|body|object|false|A map of custom fields values (id => value)|
|»»»» **additionalProperties**|body|string|false|none|
|»»» created_at|body|string|false|none|
|»»» updated_at|body|string|false|none|
|»» *anonymous*|body|object|false|none|
|»»» id|body|integer¦null|false|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "ids": [
      0
    ]
  }
}
```

<h3 id="bulk-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of IDs of the created cases.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<h3 id="bulk-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## case-attach-external-issue

<a id="opIdcase-attach-external-issue"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/case/{code}/external-issue/attach \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/case/{code}/external-issue/attach HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "type": "jira-cloud",
  "links": [
    {
      "case_id": 0,
      "external_issues": [
        "string"
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/case/{code}/external-issue/attach',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/case/{code}/external-issue/attach',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/case/{code}/external-issue/attach', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/case/{code}/external-issue/attach', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/case/{code}/external-issue/attach");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/case/{code}/external-issue/attach", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /case/{code}/external-issue/attach`

*Attach the external issues to the test cases*

> Body parameter

```json
{
  "type": "jira-cloud",
  "links": [
    {
      "case_id": 0,
      "external_issues": [
        "string"
      ]
    }
  ]
}
```

<h3 id="case-attach-external-issue-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[TestCaseExternalIssues](#schematestcaseexternalissues)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="case-attach-external-issue-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Required.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## case-detach-external-issue

<a id="opIdcase-detach-external-issue"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/case/{code}/external-issue/detach \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/case/{code}/external-issue/detach HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "type": "jira-cloud",
  "links": [
    {
      "case_id": 0,
      "external_issues": [
        "string"
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/case/{code}/external-issue/detach',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/case/{code}/external-issue/detach',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/case/{code}/external-issue/detach', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/case/{code}/external-issue/detach', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/case/{code}/external-issue/detach");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/case/{code}/external-issue/detach", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /case/{code}/external-issue/detach`

*Detach the external issues from the test cases*

> Body parameter

```json
{
  "type": "jira-cloud",
  "links": [
    {
      "case_id": 0,
      "external_issues": [
        "string"
      ]
    }
  ]
}
```

<h3 id="case-detach-external-issue-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[TestCaseExternalIssues](#schematestcaseexternalissues)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="case-detach-external-issue-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|Payment Required.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-custom-fields">custom-fields</h1>

## get-custom-fields

<a id="opIdget-custom-fields"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/custom_field \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/custom_field HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/custom_field',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/custom_field',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/custom_field', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/custom_field', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/custom_field");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/custom_field", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /custom_field`

*Get all Custom Fields*

This method allows to retrieve and filter custom fields.

<h3 id="get-custom-fields-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entity|query|string|false|none|
|type|query|string|false|none|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|entity|case|
|entity|run|
|entity|defect|
|type|string|
|type|text|
|type|number|
|type|checkbox|
|type|selectbox|
|type|radio|
|type|multiselect|
|type|url|
|type|user|
|type|datetime|

> Example responses

> 200 Response

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
        "entity": "string",
        "type": "string",
        "placeholder": "string",
        "default_value": "string",
        "value": "string",
        "is_required": true,
        "is_visible": true,
        "is_filterable": true,
        "is_enabled_for_all_projects": true,
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59",
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00",
        "projects_codes": [
          "string"
        ]
      }
    ]
  }
}
```

<h3 id="get-custom-fields-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Custom Field list.|[CustomFieldsResponse](#schemacustomfieldsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-custom-field

<a id="opIdcreate-custom-field"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/custom_field \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/custom_field HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "value": [
    {
      "id": 0,
      "title": "string"
    }
  ],
  "entity": 2,
  "type": 9,
  "placeholder": "string",
  "default_value": "string",
  "is_filterable": true,
  "is_visible": true,
  "is_required": true,
  "is_enabled_for_all_projects": true,
  "projects_codes": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/custom_field',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/custom_field',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/custom_field', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/custom_field', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/custom_field");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/custom_field", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /custom_field`

*Create new Custom Field*

This method allows to create custom field.

> Body parameter

```json
{
  "title": "string",
  "value": [
    {
      "id": 0,
      "title": "string"
    }
  ],
  "entity": 2,
  "type": 9,
  "placeholder": "string",
  "default_value": "string",
  "is_filterable": true,
  "is_visible": true,
  "is_required": true,
  "is_enabled_for_all_projects": true,
  "projects_codes": [
    "string"
  ]
}
```

<h3 id="create-custom-field-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CustomFieldCreate](#schemacustomfieldcreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-custom-field-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Created Custom Field id.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-custom-field

<a id="opIdget-custom-field"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/custom_field/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/custom_field/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/custom_field/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/custom_field/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/custom_field/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/custom_field/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/custom_field/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/custom_field/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /custom_field/{id}`

*Get Custom Field*

This method allows to retrieve custom field.

<h3 id="get-custom-field-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "entity": "string",
    "type": "string",
    "placeholder": "string",
    "default_value": "string",
    "value": "string",
    "is_required": true,
    "is_visible": true,
    "is_filterable": true,
    "is_enabled_for_all_projects": true,
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "projects_codes": [
      "string"
    ]
  }
}
```

<h3 id="get-custom-field-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Custom Field.|[CustomFieldResponse](#schemacustomfieldresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-custom-field

<a id="opIddelete-custom-field"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/custom_field/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/custom_field/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/custom_field/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/custom_field/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/custom_field/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/custom_field/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/custom_field/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/custom_field/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /custom_field/{id}`

*Delete Custom Field*

This method allows to delete custom field.

<h3 id="delete-custom-field-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="delete-custom-field-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Custom Field removal result.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-custom-field

<a id="opIdupdate-custom-field"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/custom_field/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/custom_field/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "value": [
    {
      "id": 0,
      "title": "string"
    }
  ],
  "replace_values": {
    "property1": "string",
    "property2": "string"
  },
  "placeholder": "string",
  "default_value": "string",
  "is_filterable": true,
  "is_visible": true,
  "is_required": true,
  "is_enabled_for_all_projects": true,
  "projects_codes": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/custom_field/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/custom_field/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/custom_field/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/custom_field/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/custom_field/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/custom_field/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /custom_field/{id}`

*Update Custom Field*

This method allows to update custom field.

> Body parameter

```json
{
  "title": "string",
  "value": [
    {
      "id": 0,
      "title": "string"
    }
  ],
  "replace_values": {
    "property1": "string",
    "property2": "string"
  },
  "placeholder": "string",
  "default_value": "string",
  "is_filterable": true,
  "is_visible": true,
  "is_required": true,
  "is_enabled_for_all_projects": true,
  "projects_codes": [
    "string"
  ]
}
```

<h3 id="update-custom-field-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|Identifier.|
|body|body|[CustomFieldUpdate](#schemacustomfieldupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="update-custom-field-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Custom Field update result.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-environments">environments</h1>

## get-environments

<a id="opIdget-environments"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/environment/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/environment/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/environment/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/environment/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/environment/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/environment/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/environment/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/environment/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /environment/{code}`

*Get all environments*

This method allows to retrieve all environments stored in selected project.

<h3 id="get-environments-parameters">Parameters</h3>

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

> Example responses

> 200 Response

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

<h3 id="get-environments-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all environments.|[EnvironmentListResponse](#schemaenvironmentlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-environment

<a id="opIdcreate-environment"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/environment/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/environment/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "slug": "string",
  "host": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/environment/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/environment/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/environment/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/environment/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/environment/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/environment/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /environment/{code}`

*Create a new environment*

This method allows to create an environment in selected project.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "slug": "string",
  "host": "string"
}
```

<h3 id="create-environment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[EnvironmentCreate](#schemaenvironmentcreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-environment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-environment

<a id="opIdget-environment"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/environment/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/environment/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/environment/{code}/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/environment/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/environment/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/environment/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/environment/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/environment/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /environment/{code}/{id}`

*Get a specific environment*

This method allows to retrieve a specific environment.

<h3 id="get-environment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "description": "string",
    "slug": "string",
    "host": "string"
  }
}
```

<h3 id="get-environment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|An environment.|[EnvironmentResponse](#schemaenvironmentresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-environment

<a id="opIddelete-environment"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/environment/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/environment/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/environment/{code}/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/environment/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/environment/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/environment/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/environment/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/environment/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /environment/{code}/{id}`

*Delete environment*

This method completely deletes an environment from repository.

<h3 id="delete-environment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="delete-environment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-environment

<a id="opIdupdate-environment"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/environment/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/environment/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "slug": "string",
  "host": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/environment/{code}/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/environment/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/environment/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/environment/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/environment/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/environment/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /environment/{code}/{id}`

*Update environment*

This method updates an environment.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "slug": "string",
  "host": "string"
}
```

<h3 id="update-environment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[EnvironmentUpdate](#schemaenvironmentupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="update-environment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-defects">defects</h1>

## get-defects

<a id="opIdget-defects"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/defect/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/defect/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/defect/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/defect/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/defect/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/defect/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/defect/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/defect/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /defect/{code}`

*Get all defects*

This method allows to retrieve all defects stored in selected project.

<h3 id="get-defects-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|status|query|string|false|none|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|status|open|
|status|resolved|
|status|in_progress|
|status|invalid|

> Example responses

> 200 Response

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
        "actual_result": "string",
        "severity": "string",
        "status": "string",
        "milestone_id": 0,
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "resolved_at": "2021-12-30T19:23:59+00:00",
        "member_id": 0,
        "author_id": 0,
        "external_data": "string",
        "runs": [
          0
        ],
        "results": [
          "string"
        ],
        "tags": [
          {
            "title": "string",
            "internal_id": 0
          }
        ],
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00",
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59"
      }
    ]
  }
}
```

<h3 id="get-defects-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all defects.|[DefectListResponse](#schemadefectlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-defect

<a id="opIdcreate-defect"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/defect/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/defect/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "actual_result": "string",
  "severity": 0,
  "milestone_id": 0,
  "attachments": [
    "string"
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "tags": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/defect/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/defect/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/defect/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/defect/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/defect/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/defect/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /defect/{code}`

*Create a new defect*

This method allows to create a defect in selected project.

> Body parameter

```json
{
  "title": "string",
  "actual_result": "string",
  "severity": 0,
  "milestone_id": 0,
  "attachments": [
    "string"
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "tags": [
    "string"
  ]
}
```

<h3 id="create-defect-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[DefectCreate](#schemadefectcreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-defect-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-defect

<a id="opIdget-defect"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/defect/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/defect/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/defect/{code}/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/defect/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/defect/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/defect/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/defect/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/defect/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /defect/{code}/{id}`

*Get a specific defect*

This method allows to retrieve a specific defect.

<h3 id="get-defect-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "actual_result": "string",
    "severity": "string",
    "status": "string",
    "milestone_id": 0,
    "custom_fields": [
      {
        "id": 0,
        "value": "string"
      }
    ],
    "attachments": [
      {
        "size": 0,
        "mime": "string",
        "filename": "string",
        "url": "http://example.com"
      }
    ],
    "resolved_at": "2021-12-30T19:23:59+00:00",
    "member_id": 0,
    "author_id": 0,
    "external_data": "string",
    "runs": [
      0
    ],
    "results": [
      "string"
    ],
    "tags": [
      {
        "title": "string",
        "internal_id": 0
      }
    ],
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59"
  }
}
```

<h3 id="get-defect-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A defect.|[DefectResponse](#schemadefectresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-defect

<a id="opIddelete-defect"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/defect/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/defect/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/defect/{code}/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/defect/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/defect/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/defect/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/defect/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/defect/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /defect/{code}/{id}`

*Delete defect*

This method completely deletes a defect from repository.

<h3 id="delete-defect-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="delete-defect-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-defect

<a id="opIdupdate-defect"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/defect/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/defect/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "actual_result": "string",
  "severity": 0,
  "milestone_id": 0,
  "attachments": [
    "string"
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "tags": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/defect/{code}/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/defect/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/defect/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/defect/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/defect/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/defect/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /defect/{code}/{id}`

*Update defect*

This method updates a defect.

> Body parameter

```json
{
  "title": "string",
  "actual_result": "string",
  "severity": 0,
  "milestone_id": 0,
  "attachments": [
    "string"
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "tags": [
    "string"
  ]
}
```

<h3 id="update-defect-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[DefectUpdate](#schemadefectupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="update-defect-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## resolve-defect

<a id="opIdresolve-defect"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/defect/{code}/resolve/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/defect/{code}/resolve/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/defect/{code}/resolve/{id}',
{
  method: 'PATCH',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/defect/{code}/resolve/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/defect/{code}/resolve/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/defect/{code}/resolve/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/defect/{code}/resolve/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/defect/{code}/resolve/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /defect/{code}/resolve/{id}`

*Resolve a specific defect*

This method allows to resolve a specific defect.

<h3 id="resolve-defect-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="resolve-defect-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-defect-status

<a id="opIdupdate-defect-status"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/defect/{code}/status/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/defect/{code}/status/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "status": "in_progress"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/defect/{code}/status/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/defect/{code}/status/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/defect/{code}/status/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/defect/{code}/status/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/defect/{code}/status/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/defect/{code}/status/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /defect/{code}/status/{id}`

*Update a specific defect status*

This method allows to update a specific defect status.

> Body parameter

```json
{
  "status": "in_progress"
}
```

<h3 id="update-defect-status-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[DefectStatus](#schemadefectstatus)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="update-defect-status-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-plans">plans</h1>

## get-plans

<a id="opIdget-plans"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/plan/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/plan/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/plan/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/plan/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/plan/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/plan/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/plan/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/plan/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /plan/{code}`

*Get all plans*

This method allows to retrieve all plans stored in selected project.

<h3 id="get-plans-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

> Example responses

> 200 Response

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
        "cases_count": 0,
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00",
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59"
      }
    ]
  }
}
```

<h3 id="get-plans-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all plans.|[PlanListResponse](#schemaplanlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-plan

<a id="opIdcreate-plan"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/plan/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/plan/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "cases": [
    0
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/plan/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/plan/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/plan/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/plan/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/plan/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/plan/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /plan/{code}`

*Create a new plan*

This method allows to create a plan in selected project.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cases": [
    0
  ]
}
```

<h3 id="create-plan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[PlanCreate](#schemaplancreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-plan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-plan

<a id="opIdget-plan"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/plan/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/plan/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/plan/{code}/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/plan/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/plan/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/plan/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/plan/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/plan/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /plan/{code}/{id}`

*Get a specific plan*

This method allows to retrieve a specific plan.

<h3 id="get-plan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "description": "string",
    "cases_count": 0,
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "average_time": 0,
    "cases": [
      {
        "case_id": 0,
        "assignee_id": 0
      }
    ]
  }
}
```

<h3 id="get-plan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A plan.|[PlanResponse](#schemaplanresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-plan

<a id="opIddelete-plan"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/plan/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/plan/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/plan/{code}/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/plan/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/plan/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/plan/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/plan/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/plan/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /plan/{code}/{id}`

*Delete plan*

This method completely deletes a plan from repository.

<h3 id="delete-plan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="delete-plan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-plan

<a id="opIdupdate-plan"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/plan/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/plan/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "cases": [
    0
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/plan/{code}/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/plan/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/plan/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/plan/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/plan/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/plan/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /plan/{code}/{id}`

*Update plan*

This method updates a plan.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cases": [
    0
  ]
}
```

<h3 id="update-plan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[PlanUpdate](#schemaplanupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="update-plan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-projects">projects</h1>

## get-projects

<a id="opIdget-projects"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/project \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/project HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/project',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/project',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/project', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/project', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/project");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/project", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /project`

*Get All Projects*

This method allows to retrieve all projects available
for your account. You can limit and offset params
to paginate.

<h3 id="get-projects-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "title": "string",
        "code": "string",
        "counts": {
          "cases": 0,
          "suites": 0,
          "milestones": 0,
          "runs": {
            "total": 0,
            "active": 0
          },
          "defects": {
            "total": 0,
            "open": 0
          }
        }
      }
    ]
  }
}
```

<h3 id="get-projects-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all projects.|[ProjectListResponse](#schemaprojectlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-project

<a id="opIdcreate-project"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/project \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/project HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "code": "string",
  "description": "string",
  "access": "all",
  "group": "string",
  "settings": {}
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/project',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/project',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/project', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/project', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/project");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/project", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /project`

*Create new project*

This method is used to create a new project through API.

> Body parameter

```json
{
  "title": "string",
  "code": "string",
  "description": "string",
  "access": "all",
  "group": "string",
  "settings": {}
}
```

<h3 id="create-project-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ProjectCreate](#schemaprojectcreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "code": "string"
  }
}
```

<h3 id="create-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result of project creation.|[ProjectCodeResponse](#schemaprojectcoderesponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-project

<a id="opIdget-project"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/project/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/project/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/project/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/project/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/project/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/project/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/project/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/project/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /project/{code}`

*Get Project by code*

This method allows to retrieve a specific project.

<h3 id="get-project-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "title": "string",
    "code": "string",
    "counts": {
      "cases": 0,
      "suites": 0,
      "milestones": 0,
      "runs": {
        "total": 0,
        "active": 0
      },
      "defects": {
        "total": 0,
        "open": 0
      }
    }
  }
}
```

<h3 id="get-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Project.|[ProjectResponse](#schemaprojectresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-project

<a id="opIddelete-project"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/project/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/project/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/project/{code}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/project/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/project/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/project/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/project/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/project/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /project/{code}`

*Delete Project by code*

This method allows to delete a specific project.

<h3 id="delete-project-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="delete-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result of project removal.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## grant-access-to-project

<a id="opIdgrant-access-to-project"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/project/{code}/access \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/project/{code}/access HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "member_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/project/{code}/access',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/project/{code}/access',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/project/{code}/access', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/project/{code}/access', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/project/{code}/access");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/project/{code}/access", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /project/{code}/access`

*Grant access to project by code*

This method allows to grant access to a specific project.

> Body parameter

```json
{
  "member_id": 0
}
```

<h3 id="grant-access-to-project-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[ProjectAccess](#schemaprojectaccess)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="grant-access-to-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Result of operation.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## revoke-access-to-project

<a id="opIdrevoke-access-to-project"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/project/{code}/access \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/project/{code}/access HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "member_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/project/{code}/access',
{
  method: 'DELETE',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/project/{code}/access',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/project/{code}/access', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/project/{code}/access', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/project/{code}/access");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/project/{code}/access", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /project/{code}/access`

*Revoke access to project by code*

This method allows to revoke access to a specific project.

> Body parameter

```json
{
  "member_id": 0
}
```

<h3 id="revoke-access-to-project-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[ProjectAccess](#schemaprojectaccess)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="revoke-access-to-project-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Result of operation.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-results">results</h1>

## get-results

<a id="opIdget-results"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/result/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/result/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/result/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/result/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/result/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/result/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/result/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/result/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /result/{code}`

*Get all test run results*

This method allows to retrieve all test run
results stored in selected project.

<h3 id="get-results-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|status|query|string|false|A single test run result status.|
|run|query|string|false|A list of run IDs separated by comma.|
|case_id|query|string|false|A list of case IDs separated by comma.|
|member|query|string|false|A list of member IDs separated by comma.|
|api|query|boolean|false|none|
|from_end_time|query|string|false|Will return all results created after provided datetime.|
|to_end_time|query|string|false|Will return all results created before provided datetime.|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

#### Detailed descriptions

**status**: A single test run result status.
Possible values: in_progress, passed, failed, blocked, skipped, invalid.

**from_end_time**: Will return all results created after provided datetime.
Allowed format: `Y-m-d H:i:s`.

**to_end_time**: Will return all results created before provided datetime.
Allowed format: `Y-m-d H:i:s`.

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "hash": "string",
        "result_hash": "string",
        "comment": "string",
        "stacktrace": "string",
        "run_id": 0,
        "case_id": 0,
        "steps": [
          {
            "status": 0,
            "position": 0,
            "attachments": [
              {
                "size": 0,
                "mime": "string",
                "filename": "string",
                "url": "http://example.com"
              }
            ],
            "steps": [
              {}
            ]
          }
        ],
        "status": "string",
        "is_api_result": true,
        "time_spent_ms": 0,
        "end_time": "2021-12-30T19:23:59+00:00",
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ]
      }
    ]
  }
}
```

<h3 id="get-results-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all test run results.|[ResultListResponse](#schemaresultlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-result

<a id="opIdcreate-result"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/result/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/result/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "case_id": 0,
  "case": {
    "title": "string",
    "suite_title": "string",
    "description": "string",
    "preconditions": "string",
    "postconditions": "string",
    "layer": "string",
    "severity": "string",
    "priority": "string"
  },
  "status": "string",
  "start_time": 0,
  "time": 31536000,
  "time_ms": 31536000000,
  "defect": true,
  "attachments": [
    "string"
  ],
  "stacktrace": "string",
  "comment": "string",
  "param": {
    "property1": "string",
    "property2": "string"
  },
  "param_groups": [
    [
      "string"
    ]
  ],
  "steps": [
    {
      "position": 0,
      "status": "passed",
      "comment": "string",
      "attachments": [
        "string"
      ],
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "steps": [
        {}
      ]
    }
  ],
  "author_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/result/{code}/{id}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/result/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/result/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/result/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/result/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/result/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /result/{code}/{id}`

*Create test run result*

This method allows to create test run result by Run Id.

> Body parameter

```json
{
  "case_id": 0,
  "case": {
    "title": "string",
    "suite_title": "string",
    "description": "string",
    "preconditions": "string",
    "postconditions": "string",
    "layer": "string",
    "severity": "string",
    "priority": "string"
  },
  "status": "string",
  "start_time": 0,
  "time": 31536000,
  "time_ms": 31536000000,
  "defect": true,
  "attachments": [
    "string"
  ],
  "stacktrace": "string",
  "comment": "string",
  "param": {
    "property1": "string",
    "property2": "string"
  },
  "param_groups": [
    [
      "string"
    ]
  ],
  "steps": [
    {
      "position": 0,
      "status": "passed",
      "comment": "string",
      "attachments": [
        "string"
      ],
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "steps": [
        {}
      ]
    }
  ],
  "author_id": 0
}
```

<h3 id="create-result-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[ResultCreate](#schemaresultcreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "case_id": 0,
    "hash": "string"
  }
}
```

<h3 id="create-result-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<h3 id="create-result-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-result

<a id="opIdget-result"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/result/{code}/{hash} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/result/{code}/{hash} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/result/{code}/{hash}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/result/{code}/{hash}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/result/{code}/{hash}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/result/{code}/{hash}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/result/{code}/{hash}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/result/{code}/{hash}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /result/{code}/{hash}`

*Get test run result by code*

This method allows to retrieve a specific test run result by Hash.

<h3 id="get-result-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|hash|path|string|true|Hash.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "hash": "string",
    "result_hash": "string",
    "comment": "string",
    "stacktrace": "string",
    "run_id": 0,
    "case_id": 0,
    "steps": [
      {
        "status": 0,
        "position": 0,
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "steps": [
          {}
        ]
      }
    ],
    "status": "string",
    "is_api_result": true,
    "time_spent_ms": 0,
    "end_time": "2021-12-30T19:23:59+00:00",
    "attachments": [
      {
        "size": 0,
        "mime": "string",
        "filename": "string",
        "url": "http://example.com"
      }
    ]
  }
}
```

<h3 id="get-result-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A test run result.|[ResultResponse](#schemaresultresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-result-bulk

<a id="opIdcreate-result-bulk"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/result/{code}/{id}/bulk \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/result/{code}/{id}/bulk HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "results": [
    {
      "case_id": 0,
      "case": {
        "title": "string",
        "suite_title": "string",
        "description": "string",
        "preconditions": "string",
        "postconditions": "string",
        "layer": "string",
        "severity": "string",
        "priority": "string"
      },
      "status": "string",
      "start_time": 0,
      "time": 31536000,
      "time_ms": 31536000000,
      "defect": true,
      "attachments": [
        "string"
      ],
      "stacktrace": "string",
      "comment": "string",
      "param": {
        "property1": "string",
        "property2": "string"
      },
      "param_groups": [
        [
          "string"
        ]
      ],
      "steps": [
        {
          "position": 0,
          "status": "passed",
          "comment": "string",
          "attachments": [
            "string"
          ],
          "action": "string",
          "expected_result": "string",
          "data": "string",
          "steps": [
            {}
          ]
        }
      ],
      "author_id": 0
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/result/{code}/{id}/bulk',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/result/{code}/{id}/bulk',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/result/{code}/{id}/bulk', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/result/{code}/{id}/bulk', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/result/{code}/{id}/bulk");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/result/{code}/{id}/bulk", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /result/{code}/{id}/bulk`

*Bulk create test run result*

This method allows to create a lot of test run result at once.

If you try to send more than 2,000 results in a single bulk request, you will receive an error with code 413 - Payload Too Large.

If there is no free space left in your team account, when attempting to upload an attachment, e.g., through reporters, you will receive an error with code 507 - Insufficient Storage.

> Body parameter

```json
{
  "results": [
    {
      "case_id": 0,
      "case": {
        "title": "string",
        "suite_title": "string",
        "description": "string",
        "preconditions": "string",
        "postconditions": "string",
        "layer": "string",
        "severity": "string",
        "priority": "string"
      },
      "status": "string",
      "start_time": 0,
      "time": 31536000,
      "time_ms": 31536000000,
      "defect": true,
      "attachments": [
        "string"
      ],
      "stacktrace": "string",
      "comment": "string",
      "param": {
        "property1": "string",
        "property2": "string"
      },
      "param_groups": [
        [
          "string"
        ]
      ],
      "steps": [
        {
          "position": 0,
          "status": "passed",
          "comment": "string",
          "attachments": [
            "string"
          ],
          "action": "string",
          "expected_result": "string",
          "data": "string",
          "steps": [
            {}
          ]
        }
      ],
      "author_id": 0
    }
  ]
}
```

<h3 id="create-result-bulk-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[ResultCreateBulk](#schemaresultcreatebulk)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="create-result-bulk-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|413|[Payload Too Large](https://tools.ietf.org/html/rfc7231#section-6.5.11)|Payload Too Large.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-result

<a id="opIdupdate-result"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/result/{code}/{id}/{hash} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/result/{code}/{id}/{hash} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "status": "in_progress",
  "time_ms": 31536000000,
  "defect": true,
  "attachments": [
    "string"
  ],
  "stacktrace": "string",
  "comment": "string",
  "steps": [
    {
      "position": 0,
      "status": "passed",
      "comment": "string",
      "attachments": [
        "string"
      ],
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "steps": [
        {}
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/result/{code}/{id}/{hash}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/result/{code}/{id}/{hash}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/result/{code}/{id}/{hash}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/result/{code}/{id}/{hash}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/result/{code}/{id}/{hash}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/result/{code}/{id}/{hash}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /result/{code}/{id}/{hash}`

*Update test run result*

This method allows to update test run result.

> Body parameter

```json
{
  "status": "in_progress",
  "time_ms": 31536000000,
  "defect": true,
  "attachments": [
    "string"
  ],
  "stacktrace": "string",
  "comment": "string",
  "steps": [
    {
      "position": 0,
      "status": "passed",
      "comment": "string",
      "attachments": [
        "string"
      ],
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "steps": [
        {}
      ]
    }
  ]
}
```

<h3 id="update-result-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|hash|path|string|true|Hash.|
|body|body|[ResultUpdate](#schemaresultupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "hash": "string"
  }
}
```

<h3 id="update-result-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[HashResponse](#schemahashresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-result

<a id="opIddelete-result"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/result/{code}/{id}/{hash} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/result/{code}/{id}/{hash} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/result/{code}/{id}/{hash}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/result/{code}/{id}/{hash}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/result/{code}/{id}/{hash}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/result/{code}/{id}/{hash}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/result/{code}/{id}/{hash}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/result/{code}/{id}/{hash}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /result/{code}/{id}/{hash}`

*Delete test run result*

This method allows to delete test run result.

<h3 id="delete-result-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|hash|path|string|true|Hash.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "hash": "string"
  }
}
```

<h3 id="delete-result-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[HashResponse](#schemahashresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-milestones">milestones</h1>

## get-milestones

<a id="opIdget-milestones"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/milestone/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/milestone/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/milestone/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/milestone/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/milestone/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/milestone/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/milestone/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/milestone/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /milestone/{code}`

*Get all milestones*

This method allows to retrieve all milestones stored in selected project.

<h3 id="get-milestones-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|search|query|string|false|Provide a string that will be used to search by name.|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

> Example responses

> 200 Response

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
        "status": "completed",
        "due_date": "2021-12-30T19:23:59+00:00",
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59",
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00"
      }
    ]
  }
}
```

<h3 id="get-milestones-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all milestones.|[MilestoneListResponse](#schemamilestonelistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-milestone

<a id="opIdcreate-milestone"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/milestone/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/milestone/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "status": "completed",
  "due_date": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/milestone/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/milestone/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/milestone/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/milestone/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/milestone/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/milestone/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /milestone/{code}`

*Create a new milestone*

This method allows to create a milestone in selected project.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "status": "completed",
  "due_date": 0
}
```

<h3 id="create-milestone-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[MilestoneCreate](#schemamilestonecreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-milestone-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-milestone

<a id="opIdget-milestone"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/milestone/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/milestone/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/milestone/{code}/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/milestone/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/milestone/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/milestone/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/milestone/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/milestone/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /milestone/{code}/{id}`

*Get a specific milestone*

This method allows to retrieve a specific milestone.

<h3 id="get-milestone-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "description": "string",
    "status": "completed",
    "due_date": "2021-12-30T19:23:59+00:00",
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00"
  }
}
```

<h3 id="get-milestone-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Milestone.|[MilestoneResponse](#schemamilestoneresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-milestone

<a id="opIddelete-milestone"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/milestone/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/milestone/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/milestone/{code}/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/milestone/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/milestone/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/milestone/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/milestone/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/milestone/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /milestone/{code}/{id}`

*Delete milestone*

This method completely deletes a milestone from repository.

<h3 id="delete-milestone-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="delete-milestone-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-milestone

<a id="opIdupdate-milestone"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/milestone/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/milestone/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "status": "completed"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/milestone/{code}/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/milestone/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/milestone/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/milestone/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/milestone/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/milestone/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /milestone/{code}/{id}`

*Update milestone*

This method updates a milestone.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "status": "completed"
}
```

<h3 id="update-milestone-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[MilestoneUpdate](#schemamilestoneupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="update-milestone-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-runs">runs</h1>

## get-runs

<a id="opIdget-runs"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/run/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/run/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/run/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/run/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/run/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/run/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/run/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/run/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /run/{code}`

*Get all runs*

This method allows to retrieve all runs stored in selected project.

<h3 id="get-runs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|search|query|string|false|none|
|status|query|string|false|A list of status values separated by comma.|
|milestone|query|integer|false|none|
|environment|query|integer|false|none|
|from_start_time|query|integer(int64)|false|none|
|to_start_time|query|integer(int64)|false|none|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|
|include|query|string|false|Include a list of related entities IDs into response. Should be separated by comma. Possible values: cases, defects, external_issue|

#### Detailed descriptions

**status**: A list of status values separated by comma.
Possible values: in_progress, passed, failed, aborted, active (deprecated), complete (deprecated), abort (deprecated).

**include**: Include a list of related entities IDs into response. Should be separated by comma. Possible values: cases, defects, external_issue

> Example responses

> 200 Response

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
        "run_id": 0,
        "title": "string",
        "description": "string",
        "status": 0,
        "status_text": "string",
        "start_time": "2021-12-30T19:23:59+00:00",
        "end_time": "2021-12-30T19:23:59+00:00",
        "public": true,
        "stats": {
          "total": 0,
          "statuses": {
            "property1": 0,
            "property2": 0
          },
          "untested": 0,
          "passed": 0,
          "failed": 0,
          "blocked": 0,
          "skipped": 0,
          "retest": 0,
          "in_progress": 0,
          "invalid": 0
        },
        "time_spent": 0,
        "elapsed_time": 0,
        "environment": {
          "title": "string",
          "description": "string",
          "slug": "string",
          "host": "string"
        },
        "milestone": {
          "title": "string",
          "description": "string"
        },
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "tags": [
          {
            "title": "string",
            "internal_id": 0
          }
        ],
        "cases": [
          0
        ],
        "plan_id": 0,
        "configurations": [
          0
        ],
        "external_issue": {
          "id": "string",
          "type": "string",
          "link": "http://example.com"
        }
      }
    ]
  }
}
```

<h3 id="get-runs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all runs.|[RunListResponse](#schemarunlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-run

<a id="opIdcreate-run"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/run/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/run/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "include_all_cases": true,
  "cases": [
    0
  ],
  "is_autotest": true,
  "environment_id": 1,
  "environment_slug": "string",
  "milestone_id": 1,
  "plan_id": 1,
  "author_id": 1,
  "tags": [
    "string"
  ],
  "configurations": [
    0
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "start_time": "string",
  "end_time": "string",
  "is_cloud": true,
  "cloud_run_config": {
    "browser": "chromium"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/run/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/run/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/run/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/run/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/run/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/run/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /run/{code}`

*Create a new run*

This method allows to create a run in selected project.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "include_all_cases": true,
  "cases": [
    0
  ],
  "is_autotest": true,
  "environment_id": 1,
  "environment_slug": "string",
  "milestone_id": 1,
  "plan_id": 1,
  "author_id": 1,
  "tags": [
    "string"
  ],
  "configurations": [
    0
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "start_time": "string",
  "end_time": "string",
  "is_cloud": true,
  "cloud_run_config": {
    "browser": "chromium"
  }
}
```

<h3 id="create-run-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[RunCreate](#schemaruncreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-run-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## run-update-external-issue

<a id="opIdrun-update-external-issue"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/run/{code}/external-issue \
  -H 'Content-Type: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/run/{code}/external-issue HTTP/1.1
Host: api.qase.io
Content-Type: application/json

```

```javascript
const inputBody = '{
  "type": "jira-cloud",
  "links": [
    {
      "run_id": 0,
      "external_issue": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/run/{code}/external-issue',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/run/{code}/external-issue',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/run/{code}/external-issue', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/run/{code}/external-issue', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/run/{code}/external-issue");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/run/{code}/external-issue", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /run/{code}/external-issue`

*Update external issues for runs*

This method allows you to update links between test runs and external issues (such as Jira tickets).

You can use this endpoint to:
- Link test runs to external issues by providing the external issue identifier (e.g., "PROJ-1234")
- Update existing links by providing a new external issue identifier
- Remove existing links by setting the external_issue field to null

**Important**: Each test run can have only one link with an external issue. If a test run already has an external issue link, providing a new external_issue value will replace the existing link.

The endpoint supports both Jira Cloud and Jira Server integrations. Each request can update multiple test run links in a single operation.

> Body parameter

```json
{
  "type": "jira-cloud",
  "links": [
    {
      "run_id": 0,
      "external_issue": "string"
    }
  ]
}
```

<h3 id="run-update-external-issue-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|object|true|none|
|» type|body|string|true|none|
|» links|body|[object]|true|Array of external issue links. Each test run (run_id) can have only one external issue link.|
|»» run_id|body|integer(int64)|true|none|
|»» external_issue|body|string¦null|false|An external issue identifier, e.g. "PROJ-1234". Or null if you want to remove the link.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» type|jira-cloud|
|» type|jira-server|

<h3 id="run-update-external-issue-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-run

<a id="opIdget-run"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/run/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/run/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/run/{code}/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/run/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/run/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/run/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/run/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/run/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /run/{code}/{id}`

*Get a specific run*

This method allows to retrieve a specific run.

<h3 id="get-run-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|include|query|string|false|Include a list of related entities IDs into response. Should be separated by comma. Possible values: cases, defects, external_issue|

#### Detailed descriptions

**include**: Include a list of related entities IDs into response. Should be separated by comma. Possible values: cases, defects, external_issue

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "run_id": 0,
    "title": "string",
    "description": "string",
    "status": 0,
    "status_text": "string",
    "start_time": "2021-12-30T19:23:59+00:00",
    "end_time": "2021-12-30T19:23:59+00:00",
    "public": true,
    "stats": {
      "total": 0,
      "statuses": {
        "property1": 0,
        "property2": 0
      },
      "untested": 0,
      "passed": 0,
      "failed": 0,
      "blocked": 0,
      "skipped": 0,
      "retest": 0,
      "in_progress": 0,
      "invalid": 0
    },
    "time_spent": 0,
    "elapsed_time": 0,
    "environment": {
      "title": "string",
      "description": "string",
      "slug": "string",
      "host": "string"
    },
    "milestone": {
      "title": "string",
      "description": "string"
    },
    "custom_fields": [
      {
        "id": 0,
        "value": "string"
      }
    ],
    "tags": [
      {
        "title": "string",
        "internal_id": 0
      }
    ],
    "cases": [
      0
    ],
    "plan_id": 0,
    "configurations": [
      0
    ],
    "external_issue": {
      "id": "string",
      "type": "string",
      "link": "http://example.com"
    }
  }
}
```

<h3 id="get-run-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A run.|[RunResponse](#schemarunresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-run

<a id="opIdupdate-run"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/run/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/run/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "environment_id": 1,
  "environment_slug": "string",
  "milestone_id": 1,
  "tags": [
    "string"
  ],
  "configurations": [
    0
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/run/{code}/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/run/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/run/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/run/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/run/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/run/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /run/{code}/{id}`

*Update a specific run*

This method allows to update a specific run.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "environment_id": 1,
  "environment_slug": "string",
  "milestone_id": 1,
  "tags": [
    "string"
  ],
  "configurations": [
    0
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  }
}
```

<h3 id="update-run-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|object|true|none|
|» title|body|string|false|none|
|» description|body|string¦null|false|none|
|» environment_id|body|integer(int64)¦null|false|none|
|» environment_slug|body|string¦null|false|none|
|» milestone_id|body|integer(int64)¦null|false|none|
|» tags|body|[string]¦null|false|none|
|» configurations|body|[integer]¦null|false|none|
|» custom_field|body|object¦null|false|A map of custom fields values (id => value)|
|»» **additionalProperties**|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="update-run-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-run

<a id="opIddelete-run"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/run/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/run/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/run/{code}/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/run/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/run/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/run/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/run/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/run/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /run/{code}/{id}`

*Delete run*

This method completely deletes a run from repository.

<h3 id="delete-run-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="delete-run-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-run-publicity

<a id="opIdupdate-run-publicity"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/run/{code}/{id}/public \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/run/{code}/{id}/public HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "status": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/run/{code}/{id}/public',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/run/{code}/{id}/public',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/run/{code}/{id}/public', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/run/{code}/{id}/public', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/run/{code}/{id}/public");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/run/{code}/{id}/public", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /run/{code}/{id}/public`

*Update publicity of a specific run*

This method allows to update a publicity of specific run.

> Body parameter

```json
{
  "status": true
}
```

<h3 id="update-run-publicity-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[RunPublic](#schemarunpublic)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "url": "http://example.com"
  }
}
```

<h3 id="update-run-publicity-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[RunPublicResponse](#schemarunpublicresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## complete-run

<a id="opIdcomplete-run"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/run/{code}/{id}/complete \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/run/{code}/{id}/complete HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/run/{code}/{id}/complete',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/run/{code}/{id}/complete',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/run/{code}/{id}/complete', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/run/{code}/{id}/complete', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/run/{code}/{id}/complete");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/run/{code}/{id}/complete", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /run/{code}/{id}/complete`

*Complete a specific run*

This method allows to complete a specific run.

<h3 id="complete-run-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true
}
```

<h3 id="complete-run-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[Response](#schemaresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-search">search</h1>

## search

<a id="opIdsearch"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/search?query=string \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/search?query=string HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/search?query=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/search',
  params: {
  'query' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/search', params={
  'query': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/search?query=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /search`

*Search entities by Qase Query Language (QQL)*

This method allows to retrieve data sets for various
entities using expressions with conditions.

<h3 id="search-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|
|query|query|string|true|Expression in Qase Query Language.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "entities": [
      {
        "id": 0,
        "run_id": 0,
        "title": "string",
        "description": "string",
        "status": 0,
        "status_text": "string",
        "start_time": "2021-12-30T19:23:59+00:00",
        "end_time": "2021-12-30T19:23:59+00:00",
        "public": true,
        "stats": {
          "total": 0,
          "statuses": {
            "property1": 0,
            "property2": 0
          },
          "untested": 0,
          "passed": 0,
          "failed": 0,
          "blocked": 0,
          "skipped": 0,
          "retest": 0,
          "in_progress": 0,
          "invalid": 0
        },
        "time_spent": 0,
        "elapsed_time": 0,
        "environment": {
          "title": "string",
          "description": "string",
          "slug": "string",
          "host": "string"
        },
        "milestone": {
          "title": "string",
          "description": "string"
        },
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "tags": [
          {
            "title": "string",
            "internal_id": 0
          }
        ],
        "cases": [
          0
        ],
        "plan_id": 0
      }
    ],
    "total": 0
  }
}
```

<h3 id="search-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of found entities.|[SearchResponse](#schemasearchresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-shared-parameters">shared-parameters</h1>

## get-shared-parameters

<a id="opIdget-shared-parameters"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/shared_parameter \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/shared_parameter HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_parameter',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/shared_parameter',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/shared_parameter', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/shared_parameter', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_parameter");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/shared_parameter", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /shared_parameter`

*Get all shared parameters*

<h3 id="get-shared-parameters-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|
|filters[search]|query|string|false|none|
|filters[type]|query|string|false|none|
|filters[project_codes][]|query|array[string]|false|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|filters[type]|single|
|filters[type]|group|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "total": 0,
    "entities": [
      {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "title": "string",
        "type": "single",
        "project_codes": [
          "string"
        ],
        "is_enabled_for_all_projects": true,
        "parameters": [
          {
            "title": "string",
            "values": [
              "string"
            ]
          }
        ]
      }
    ]
  }
}
```

<h3 id="get-shared-parameters-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all shared parameters.|[SharedParameterListResponse](#schemasharedparameterlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-shared-parameter

<a id="opIdcreate-shared-parameter"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/shared_parameter \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/shared_parameter HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "type": "single",
  "project_codes": [
    "string"
  ],
  "is_enabled_for_all_projects": true,
  "parameters": [
    {
      "title": "string",
      "values": [
        "string"
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_parameter',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/shared_parameter',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/shared_parameter', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/shared_parameter', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_parameter");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/shared_parameter", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /shared_parameter`

*Create a new shared parameter*

> Body parameter

```json
{
  "title": "string",
  "type": "single",
  "project_codes": [
    "string"
  ],
  "is_enabled_for_all_projects": true,
  "parameters": [
    {
      "title": "string",
      "values": [
        "string"
      ]
    }
  ]
}
```

<h3 id="create-shared-parameter-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SharedParameterCreate](#schemasharedparametercreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  }
}
```

<h3 id="create-shared-parameter-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A shared parameter.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<h3 id="create-shared-parameter-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-shared-parameter

<a id="opIdget-shared-parameter"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/shared_parameter/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/shared_parameter/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_parameter/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/shared_parameter/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/shared_parameter/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/shared_parameter/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_parameter/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/shared_parameter/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /shared_parameter/{id}`

*Get a specific shared parameter*

<h3 id="get-shared-parameter-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "title": "string",
    "type": "single",
    "project_codes": [
      "string"
    ],
    "is_enabled_for_all_projects": true,
    "parameters": [
      {
        "title": "string",
        "values": [
          "string"
        ]
      }
    ]
  }
}
```

<h3 id="get-shared-parameter-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A shared parameter.|[SharedParameterResponse](#schemasharedparameterresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-shared-parameter

<a id="opIdupdate-shared-parameter"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/shared_parameter/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/shared_parameter/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "project_codes": [
    "string"
  ],
  "is_enabled_for_all_projects": true,
  "parameters": [
    {
      "title": "string",
      "values": [
        "string"
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_parameter/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/shared_parameter/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/shared_parameter/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/shared_parameter/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_parameter/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/shared_parameter/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /shared_parameter/{id}`

*Update shared parameter*

> Body parameter

```json
{
  "title": "string",
  "project_codes": [
    "string"
  ],
  "is_enabled_for_all_projects": true,
  "parameters": [
    {
      "title": "string",
      "values": [
        "string"
      ]
    }
  ]
}
```

<h3 id="update-shared-parameter-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|Identifier.|
|body|body|[SharedParameterUpdate](#schemasharedparameterupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  }
}
```

<h3 id="update-shared-parameter-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<h3 id="update-shared-parameter-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-shared-parameter

<a id="opIddelete-shared-parameter"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/shared_parameter/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/shared_parameter/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_parameter/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/shared_parameter/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/shared_parameter/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/shared_parameter/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_parameter/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/shared_parameter/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /shared_parameter/{id}`

*Delete shared parameter*

Delete shared parameter along with all its usages in test cases and reviews.

<h3 id="delete-shared-parameter-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  }
}
```

<h3 id="delete-shared-parameter-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<h3 id="delete-shared-parameter-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-shared-steps">shared-steps</h1>

## get-shared-steps

<a id="opIdget-shared-steps"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/shared_step/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/shared_step/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_step/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/shared_step/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/shared_step/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/shared_step/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_step/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/shared_step/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /shared_step/{code}`

*Get all shared steps*

This method allows to retrieve all shared steps stored in selected project.

<h3 id="get-shared-steps-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|search|query|string|false|Provide a string that will be used to search by name.|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "hash": "string",
        "title": "string",
        "action": "string",
        "expected_result": "string",
        "steps": [
          {
            "data": "string",
            "hash": "string",
            "action": "string",
            "expected_result": "string",
            "attachments": [
              {
                "size": 0,
                "mime": "string",
                "filename": "string",
                "url": "http://example.com",
                "hash": "string"
              }
            ]
          }
        ],
        "data": "string",
        "cases": [
          0
        ],
        "cases_count": 0,
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59",
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00"
      }
    ]
  }
}
```

<h3 id="get-shared-steps-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all shared steps.|[SharedStepListResponse](#schemasharedsteplistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-shared-step

<a id="opIdcreate-shared-step"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/shared_step/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/shared_step/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "steps": [
    {
      "hash": "string",
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "attachments": [
        "string"
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_step/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/shared_step/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/shared_step/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/shared_step/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_step/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/shared_step/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /shared_step/{code}`

*Create a new shared step*

This method allows to create a shared step in selected project.

> Body parameter

```json
{
  "title": "string",
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "steps": [
    {
      "hash": "string",
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "attachments": [
        "string"
      ]
    }
  ]
}
```

<h3 id="create-shared-step-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[SharedStepCreate](#schemasharedstepcreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "hash": "string"
  }
}
```

<h3 id="create-shared-step-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[HashResponse](#schemahashresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-shared-step

<a id="opIdget-shared-step"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/shared_step/{code}/{hash} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/shared_step/{code}/{hash} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_step/{code}/{hash}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/shared_step/{code}/{hash}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/shared_step/{code}/{hash}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/shared_step/{code}/{hash}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_step/{code}/{hash}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/shared_step/{code}/{hash}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /shared_step/{code}/{hash}`

*Get a specific shared step*

This method allows to retrieve a specific shared step.

<h3 id="get-shared-step-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|hash|path|string|true|Hash.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "hash": "string",
    "title": "string",
    "action": "string",
    "expected_result": "string",
    "steps": [
      {
        "data": "string",
        "hash": "string",
        "action": "string",
        "expected_result": "string",
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com",
            "hash": "string"
          }
        ]
      }
    ],
    "data": "string",
    "cases": [
      0
    ],
    "cases_count": 0,
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00"
  }
}
```

<h3 id="get-shared-step-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A shared step.|[SharedStepResponse](#schemasharedstepresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-shared-step

<a id="opIddelete-shared-step"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/shared_step/{code}/{hash} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/shared_step/{code}/{hash} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_step/{code}/{hash}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/shared_step/{code}/{hash}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/shared_step/{code}/{hash}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/shared_step/{code}/{hash}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_step/{code}/{hash}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/shared_step/{code}/{hash}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /shared_step/{code}/{hash}`

*Delete shared step*

This method completely deletes a shared step from repository.

<h3 id="delete-shared-step-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|hash|path|string|true|Hash.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "hash": "string"
  }
}
```

<h3 id="delete-shared-step-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Result.|[HashResponse](#schemahashresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-shared-step

<a id="opIdupdate-shared-step"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/shared_step/{code}/{hash} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/shared_step/{code}/{hash} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "steps": [
    {
      "hash": "string",
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "attachments": [
        "string"
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/shared_step/{code}/{hash}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/shared_step/{code}/{hash}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/shared_step/{code}/{hash}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/shared_step/{code}/{hash}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/shared_step/{code}/{hash}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/shared_step/{code}/{hash}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /shared_step/{code}/{hash}`

*Update shared step*

This method updates a shared step.

> Body parameter

```json
{
  "title": "string",
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "steps": [
    {
      "hash": "string",
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "attachments": [
        "string"
      ]
    }
  ]
}
```

<h3 id="update-shared-step-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|hash|path|string|true|Hash.|
|body|body|[SharedStepUpdate](#schemasharedstepupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "hash": "string"
  }
}
```

<h3 id="update-shared-step-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[HashResponse](#schemahashresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-suites">suites</h1>

## get-suites

<a id="opIdget-suites"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/suite/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/suite/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/suite/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/suite/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/suite/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/suite/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/suite/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/suite/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /suite/{code}`

*Get all test suites*

This method allows to retrieve all test suites stored in selected project.

<h3 id="get-suites-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|search|query|string|false|Provide a string that will be used to search by name.|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

> Example responses

> 200 Response

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
        "preconditions": "string",
        "position": 0,
        "cases_count": 0,
        "parent_id": 0,
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59",
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00"
      }
    ]
  }
}
```

<h3 id="get-suites-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all suites of project.|[SuiteListResponse](#schemasuitelistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-suite

<a id="opIdcreate-suite"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/suite/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/suite/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "parent_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/suite/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/suite/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/suite/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/suite/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/suite/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/suite/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /suite/{code}`

*Create a new test suite*

This method is used to create a new test suite through API.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "parent_id": 0
}
```

<h3 id="create-suite-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[SuiteCreate](#schemasuitecreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-suite-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-suite

<a id="opIdget-suite"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/suite/{code}/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/suite/{code}/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/suite/{code}/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/suite/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/suite/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/suite/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/suite/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/suite/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /suite/{code}/{id}`

*Get a specific test suite*

This method allows to retrieve a specific test suite.

<h3 id="get-suite-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "description": "string",
    "preconditions": "string",
    "position": 0,
    "cases_count": 0,
    "parent_id": 0,
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00"
  }
}
```

<h3 id="get-suite-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A Test Case.|[SuiteResponse](#schemasuiteresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## delete-suite

<a id="opIddelete-suite"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://api.qase.io/v1/suite/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
DELETE https://api.qase.io/v1/suite/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "destination_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/suite/{code}/{id}',
{
  method: 'DELETE',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.delete 'https://api.qase.io/v1/suite/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.delete('https://api.qase.io/v1/suite/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://api.qase.io/v1/suite/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/suite/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://api.qase.io/v1/suite/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /suite/{code}/{id}`

*Delete test suite*

This method completely deletes a test suite with test cases from repository.

> Body parameter

```json
{
  "destination_id": 0
}
```

<h3 id="delete-suite-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[SuiteDelete](#schemasuitedelete)|false|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="delete-suite-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result of operation.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## update-suite

<a id="opIdupdate-suite"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH https://api.qase.io/v1/suite/{code}/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
PATCH https://api.qase.io/v1/suite/{code}/{id} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "parent_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/suite/{code}/{id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.patch 'https://api.qase.io/v1/suite/{code}/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.patch('https://api.qase.io/v1/suite/{code}/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','https://api.qase.io/v1/suite/{code}/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/suite/{code}/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "https://api.qase.io/v1/suite/{code}/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /suite/{code}/{id}`

*Update test suite*

This method is used to update a test suite through API.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "parent_id": 0
}
```

<h3 id="update-suite-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|id|path|integer|true|Identifier.|
|body|body|[SuiteUpdate](#schemasuiteupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="update-suite-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result of operation.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-system-fields">system-fields</h1>

## get-system-fields

<a id="opIdget-system-fields"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/system_field \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/system_field HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/system_field',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/system_field',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/system_field', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/system_field', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/system_field");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/system_field", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /system_field`

*Get all System Fields*

This method allows to retrieve all system fields.

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": [
    {
      "title": "string",
      "slug": "string",
      "default_value": "string",
      "is_required": true,
      "entity": 0,
      "type": 0,
      "options": [
        {
          "id": 0,
          "title": "string",
          "slug": "string",
          "color": "string",
          "icon": "string",
          "is_default": true,
          "read_only": true
        }
      ]
    }
  ]
}
```

<h3 id="get-system-fields-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|System Field list.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<h3 id="get-system-fields-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-configurations">configurations</h1>

## get-configurations

<a id="opIdget-configurations"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/configuration/{code} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/configuration/{code} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/configuration/{code}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/configuration/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/configuration/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/configuration/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/configuration/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/configuration/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /configuration/{code}`

*Get all configuration groups with configurations.*

This method allows to retrieve all configurations groups with configurations

<h3 id="get-configurations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|

> Example responses

> 200 Response

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
        "configurations": [
          {
            "id": 0,
            "title": "string"
          }
        ]
      }
    ]
  }
}
```

<h3 id="get-configurations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all configurations.|[ConfigurationListResponse](#schemaconfigurationlistresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-configuration

<a id="opIdcreate-configuration"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/configuration/{code} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/configuration/{code} HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "group_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/configuration/{code}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/configuration/{code}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/configuration/{code}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/configuration/{code}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/configuration/{code}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/configuration/{code}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /configuration/{code}`

*Create a new configuration in a particular group.*

This method allows to create a configuration in selected project.

> Body parameter

```json
{
  "title": "string",
  "group_id": 0
}
```

<h3 id="create-configuration-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[ConfigurationCreate](#schemaconfigurationcreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-configuration-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## create-configuration-group

<a id="opIdcreate-configuration-group"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://api.qase.io/v1/configuration/{code}/group \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
POST https://api.qase.io/v1/configuration/{code}/group HTTP/1.1
Host: api.qase.io
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/configuration/{code}/group',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.post 'https://api.qase.io/v1/configuration/{code}/group',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.post('https://api.qase.io/v1/configuration/{code}/group', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://api.qase.io/v1/configuration/{code}/group', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/configuration/{code}/group");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://api.qase.io/v1/configuration/{code}/group", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /configuration/{code}/group`

*Create a new configuration group.*

This method allows to create a configuration group in selected project.

> Body parameter

```json
{
  "title": "string"
}
```

<h3 id="create-configuration-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|code|path|string|true|Code of project, where to search entities.|
|body|body|[ConfigurationGroupCreate](#schemaconfigurationgroupcreate)|true|none|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}
```

<h3 id="create-configuration-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A result.|[IdResponse](#schemaidresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request.|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized.|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden.|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found.|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unprocessable Entity.|None|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|Too Many Requests.|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

<h1 id="qase-io-testops-api-v1-users">users</h1>

## get-users

<a id="opIdget-users"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/user \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/user HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/user',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/user',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/user', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/user', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/user");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/user", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /user`

*Get all users.*

This method allows to retrieve all users.

<h3 id="get-users-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer|false|A number of entities in result set.|
|offset|query|integer|false|How many entities should be skipped.|

> Example responses

> 200 Response

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
        "name": "string",
        "email": "string",
        "title": "string",
        "status": 0
      }
    ]
  }
}
```

<h3 id="get-users-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all users.|[UserListResponse](#schemauserlistresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

## get-user

<a id="opIdget-user"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://api.qase.io/v1/user/{id} \
  -H 'Accept: application/json' \
  -H 'Token: API_KEY'

```

```http
GET https://api.qase.io/v1/user/{id} HTTP/1.1
Host: api.qase.io
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Token':'API_KEY'
};

fetch('https://api.qase.io/v1/user/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Token' => 'API_KEY'
}

result = RestClient.get 'https://api.qase.io/v1/user/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Token': 'API_KEY'
}

r = requests.get('https://api.qase.io/v1/user/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Token' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://api.qase.io/v1/user/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://api.qase.io/v1/user/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Token": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://api.qase.io/v1/user/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /user/{id}`

*Get a specific user.*

This method allows to retrieve a specific user.

<h3 id="get-user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|Identifier.|

> Example responses

> 200 Response

```json
{
  "status": true,
  "result": {
    "id": 0,
    "name": "string",
    "email": "string",
    "title": "string",
    "status": 0
  }
}
```

<h3 id="get-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A user.|[UserResponse](#schemauserresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
TokenAuth
</aside>

# Schemas

<h2 id="tocS_Attachment">Attachment</h2>
<!-- backwards compatibility -->
<a id="schemaattachment"></a>
<a id="schema_Attachment"></a>
<a id="tocSattachment"></a>
<a id="tocsattachment"></a>

```json
{
  "size": 0,
  "mime": "string",
  "filename": "string",
  "url": "http://example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|size|integer|false|none|none|
|mime|string|false|none|none|
|filename|string|false|none|none|
|url|string(uri)|false|none|none|

<h2 id="tocS_AttachmentGet">AttachmentGet</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentget"></a>
<a id="schema_AttachmentGet"></a>
<a id="tocSattachmentget"></a>
<a id="tocsattachmentget"></a>

```json
{
  "hash": "string",
  "file": "string",
  "mime": "string",
  "size": 0,
  "extension": "string",
  "full_path": "http://example.com",
  "url": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hash|string|false|none|none|
|file|string|false|none|none|
|mime|string|false|none|none|
|size|integer|false|none|none|
|extension|string|false|none|none|
|full_path|string(uri)|false|none|none|
|url|string|false|none|none|

<h2 id="tocS_AttachmentHash">AttachmentHash</h2>
<!-- backwards compatibility -->
<a id="schemaattachmenthash"></a>
<a id="schema_AttachmentHash"></a>
<a id="tocSattachmenthash"></a>
<a id="tocsattachmenthash"></a>

```json
{
  "size": 0,
  "mime": "string",
  "filename": "string",
  "url": "http://example.com",
  "hash": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|size|integer|false|none|none|
|mime|string|false|none|none|
|filename|string|false|none|none|
|url|string(uri)|false|none|none|
|hash|string|false|none|none|

<h2 id="tocS_AttachmentHashList">AttachmentHashList</h2>
<!-- backwards compatibility -->
<a id="schemaattachmenthashlist"></a>
<a id="schema_AttachmentHashList"></a>
<a id="tocSattachmenthashlist"></a>
<a id="tocsattachmenthashlist"></a>

```json
[
  "string"
]

```

A list of Attachment hashes.

### Properties

*None*

<h2 id="tocS_Author">Author</h2>
<!-- backwards compatibility -->
<a id="schemaauthor"></a>
<a id="schema_Author"></a>
<a id="tocSauthor"></a>
<a id="tocsauthor"></a>

```json
{
  "id": 0,
  "author_id": 0,
  "entity_type": "string",
  "entity_id": 0,
  "email": "string",
  "name": "string",
  "is_active": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|author_id|integer(int64)|false|none|none|
|entity_type|string|false|none|none|
|entity_id|integer(int64)|false|none|none|
|email|string|false|none|none|
|name|string|false|none|none|
|is_active|boolean|false|none|none|

<h2 id="tocS_CustomField">CustomField</h2>
<!-- backwards compatibility -->
<a id="schemacustomfield"></a>
<a id="schema_CustomField"></a>
<a id="tocScustomfield"></a>
<a id="tocscustomfield"></a>

```json
{
  "id": 0,
  "title": "string",
  "entity": "string",
  "type": "string",
  "placeholder": "string",
  "default_value": "string",
  "value": "string",
  "is_required": true,
  "is_visible": true,
  "is_filterable": true,
  "is_enabled_for_all_projects": true,
  "created": "2021-12-30 19:23:59",
  "updated": "2021-12-30 19:23:59",
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00",
  "projects_codes": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|title|string|false|none|none|
|entity|string|false|none|none|
|type|string|false|none|none|
|placeholder|string¦null|false|none|none|
|default_value|string¦null|false|none|none|
|value|string¦null|false|none|none|
|is_required|boolean|false|none|none|
|is_visible|boolean|false|none|none|
|is_filterable|boolean|false|none|none|
|is_enabled_for_all_projects|boolean|false|none|none|
|created|string|false|none|Deprecated, use the `created_at` property instead.|
|updated|string¦null|false|none|Deprecated, use the `updated_at` property instead.|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|
|projects_codes|[string]|false|none|none|

<h2 id="tocS_CustomFieldCreate">CustomFieldCreate</h2>
<!-- backwards compatibility -->
<a id="schemacustomfieldcreate"></a>
<a id="schema_CustomFieldCreate"></a>
<a id="tocScustomfieldcreate"></a>
<a id="tocscustomfieldcreate"></a>

```json
{
  "title": "string",
  "value": [
    {
      "id": 0,
      "title": "string"
    }
  ],
  "entity": 2,
  "type": 9,
  "placeholder": "string",
  "default_value": "string",
  "is_filterable": true,
  "is_visible": true,
  "is_required": true,
  "is_enabled_for_all_projects": true,
  "projects_codes": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|value|[object]¦null|false|none|Required if type one of:<br>3 - selectbox;<br>5 - radio;<br>6 - multiselect;|
|» id|integer(int64)|false|none|none|
|» title|string|false|none|none|
|entity|integer|true|none|Possible values:<br>0 - case;<br>1 - run;<br>2 - defect;|
|type|integer|true|none|Possible values:<br>0 - number;<br>1 - string;<br>2 - text;<br>3 - selectbox;<br>4 - checkbox;<br>5 - radio;<br>6 - multiselect;<br>7 - url;<br>8 - user;<br>9 - datetime;|
|placeholder|string¦null|false|none|none|
|default_value|string¦null|false|none|none|
|is_filterable|boolean|false|none|none|
|is_visible|boolean|false|none|none|
|is_required|boolean|false|none|none|
|is_enabled_for_all_projects|boolean|false|none|none|
|projects_codes|[string]|false|none|none|

<h2 id="tocS_CustomFieldUpdate">CustomFieldUpdate</h2>
<!-- backwards compatibility -->
<a id="schemacustomfieldupdate"></a>
<a id="schema_CustomFieldUpdate"></a>
<a id="tocScustomfieldupdate"></a>
<a id="tocscustomfieldupdate"></a>

```json
{
  "title": "string",
  "value": [
    {
      "id": 0,
      "title": "string"
    }
  ],
  "replace_values": {
    "property1": "string",
    "property2": "string"
  },
  "placeholder": "string",
  "default_value": "string",
  "is_filterable": true,
  "is_visible": true,
  "is_required": true,
  "is_enabled_for_all_projects": true,
  "projects_codes": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|value|[object]¦null|false|none|none|
|» id|integer(int64)|false|none|none|
|» title|string|false|none|none|
|replace_values|object¦null|false|none|Dictionary of old values and their replacemants|
|» **additionalProperties**|string|false|none|none|
|placeholder|string¦null|false|none|none|
|default_value|string¦null|false|none|none|
|is_filterable|boolean|false|none|none|
|is_visible|boolean|false|none|none|
|is_required|boolean|false|none|none|
|is_enabled_for_all_projects|boolean|false|none|none|
|projects_codes|[string]|false|none|none|

<h2 id="tocS_CustomFieldValue">CustomFieldValue</h2>
<!-- backwards compatibility -->
<a id="schemacustomfieldvalue"></a>
<a id="schema_CustomFieldValue"></a>
<a id="tocScustomfieldvalue"></a>
<a id="tocscustomfieldvalue"></a>

```json
{
  "id": 0,
  "value": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|value|string|false|none|none|

<h2 id="tocS_Defect">Defect</h2>
<!-- backwards compatibility -->
<a id="schemadefect"></a>
<a id="schema_Defect"></a>
<a id="tocSdefect"></a>
<a id="tocsdefect"></a>

```json
{
  "id": 0,
  "title": "string",
  "actual_result": "string",
  "severity": "string",
  "status": "string",
  "milestone_id": 0,
  "custom_fields": [
    {
      "id": 0,
      "value": "string"
    }
  ],
  "attachments": [
    {
      "size": 0,
      "mime": "string",
      "filename": "string",
      "url": "http://example.com"
    }
  ],
  "resolved_at": "2021-12-30T19:23:59+00:00",
  "member_id": 0,
  "author_id": 0,
  "external_data": "string",
  "runs": [
    0
  ],
  "results": [
    "string"
  ],
  "tags": [
    {
      "title": "string",
      "internal_id": 0
    }
  ],
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00",
  "created": "2021-12-30 19:23:59",
  "updated": "2021-12-30 19:23:59"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|title|string|false|none|none|
|actual_result|string|false|none|none|
|severity|string|false|none|none|
|status|string|false|none|none|
|milestone_id|integer(int64)¦null|false|none|none|
|custom_fields|[[CustomFieldValue](#schemacustomfieldvalue)]|false|none|none|
|attachments|[[Attachment](#schemaattachment)]|false|none|none|
|resolved_at|string(date-time)¦null|false|none|none|
|member_id|integer(int64)|false|none|Deprecated, use `author_id` instead.|
|author_id|integer(int64)|false|none|none|
|external_data|string|false|none|none|
|runs|[integer]|false|none|none|
|results|[string]|false|none|none|
|tags|[[TagValue](#schematagvalue)]|false|none|none|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|
|created|string|false|none|Deprecated, use the `created_at` property instead.|
|updated|string|false|none|Deprecated, use the `updated_at` property instead.|

<h2 id="tocS_DefectCreate">DefectCreate</h2>
<!-- backwards compatibility -->
<a id="schemadefectcreate"></a>
<a id="schema_DefectCreate"></a>
<a id="tocSdefectcreate"></a>
<a id="tocsdefectcreate"></a>

```json
{
  "title": "string",
  "actual_result": "string",
  "severity": 0,
  "milestone_id": 0,
  "attachments": [
    "string"
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "tags": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|actual_result|string|true|none|none|
|severity|integer|true|none|none|
|milestone_id|integer(int64)¦null|false|none|none|
|attachments|[string]|false|none|none|
|custom_field|object|false|none|A map of custom fields values (id => value)|
|» **additionalProperties**|string|false|none|none|
|tags|[string]|false|none|none|

<h2 id="tocS_DefectStatus">DefectStatus</h2>
<!-- backwards compatibility -->
<a id="schemadefectstatus"></a>
<a id="schema_DefectStatus"></a>
<a id="tocSdefectstatus"></a>
<a id="tocsdefectstatus"></a>

```json
{
  "status": "in_progress"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|in_progress|
|status|resolved|
|status|invalid|

<h2 id="tocS_DefectUpdate">DefectUpdate</h2>
<!-- backwards compatibility -->
<a id="schemadefectupdate"></a>
<a id="schema_DefectUpdate"></a>
<a id="tocSdefectupdate"></a>
<a id="tocsdefectupdate"></a>

```json
{
  "title": "string",
  "actual_result": "string",
  "severity": 0,
  "milestone_id": 0,
  "attachments": [
    "string"
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "tags": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|false|none|none|
|actual_result|string|false|none|none|
|severity|integer|false|none|none|
|milestone_id|integer(int64)¦null|false|none|none|
|attachments|[string]|false|none|none|
|custom_field|object|false|none|A map of custom fields values (id => value)|
|» **additionalProperties**|string|false|none|none|
|tags|[string]|false|none|none|

<h2 id="tocS_Environment">Environment</h2>
<!-- backwards compatibility -->
<a id="schemaenvironment"></a>
<a id="schema_Environment"></a>
<a id="tocSenvironment"></a>
<a id="tocsenvironment"></a>

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "slug": "string",
  "host": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|slug|string|false|none|none|
|host|string¦null|false|none|none|

<h2 id="tocS_EnvironmentCreate">EnvironmentCreate</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentcreate"></a>
<a id="schema_EnvironmentCreate"></a>
<a id="tocSenvironmentcreate"></a>
<a id="tocsenvironmentcreate"></a>

```json
{
  "title": "string",
  "description": "string",
  "slug": "string",
  "host": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string|false|none|none|
|slug|string|true|none|none|
|host|string|false|none|none|

<h2 id="tocS_EnvironmentUpdate">EnvironmentUpdate</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentupdate"></a>
<a id="schema_EnvironmentUpdate"></a>
<a id="tocSenvironmentupdate"></a>
<a id="tocsenvironmentupdate"></a>

```json
{
  "title": "string",
  "description": "string",
  "slug": "string",
  "host": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|false|none|none|
|description|string|false|none|none|
|slug|string|false|none|none|
|host|string|false|none|none|

<h2 id="tocS_Milestone">Milestone</h2>
<!-- backwards compatibility -->
<a id="schemamilestone"></a>
<a id="schema_Milestone"></a>
<a id="tocSmilestone"></a>
<a id="tocsmilestone"></a>

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "status": "completed",
  "due_date": "2021-12-30T19:23:59+00:00",
  "created": "2021-12-30 19:23:59",
  "updated": "2021-12-30 19:23:59",
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|status|string|false|none|none|
|due_date|string(date-time)¦null|false|none|none|
|created|string|false|none|Deprecated, use the `created_at` property instead.|
|updated|string¦null|false|none|Deprecated, use the `updated_at` property instead.|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|completed|
|status|active|

<h2 id="tocS_MilestoneCreate">MilestoneCreate</h2>
<!-- backwards compatibility -->
<a id="schemamilestonecreate"></a>
<a id="schema_MilestoneCreate"></a>
<a id="tocSmilestonecreate"></a>
<a id="tocsmilestonecreate"></a>

```json
{
  "title": "string",
  "description": "string",
  "status": "completed",
  "due_date": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string|false|none|none|
|status|string|false|none|none|
|due_date|integer(int64)|false|none|unix timestamp|

#### Enumerated Values

|Property|Value|
|---|---|
|status|completed|
|status|active|

<h2 id="tocS_MilestoneUpdate">MilestoneUpdate</h2>
<!-- backwards compatibility -->
<a id="schemamilestoneupdate"></a>
<a id="schema_MilestoneUpdate"></a>
<a id="tocSmilestoneupdate"></a>
<a id="tocsmilestoneupdate"></a>

```json
{
  "title": "string",
  "description": "string",
  "status": "completed"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|false|none|none|
|description|string|false|none|none|
|status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|completed|
|status|active|

<h2 id="tocS_Plan">Plan</h2>
<!-- backwards compatibility -->
<a id="schemaplan"></a>
<a id="schema_Plan"></a>
<a id="tocSplan"></a>
<a id="tocsplan"></a>

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "cases_count": 0,
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00",
  "created": "2021-12-30 19:23:59",
  "updated": "2021-12-30 19:23:59"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|cases_count|integer|false|none|none|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|
|created|string|false|none|Deprecated, use the `created_at` property instead.|
|updated|string|false|none|Deprecated, use the `updated_at` property instead.|

<h2 id="tocS_PlanCreate">PlanCreate</h2>
<!-- backwards compatibility -->
<a id="schemaplancreate"></a>
<a id="schema_PlanCreate"></a>
<a id="tocSplancreate"></a>
<a id="tocsplancreate"></a>

```json
{
  "title": "string",
  "description": "string",
  "cases": [
    0
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string¦null|false|none|none|
|cases|[integer]|true|none|none|

<h2 id="tocS_PlanDetailed">PlanDetailed</h2>
<!-- backwards compatibility -->
<a id="schemaplandetailed"></a>
<a id="schema_PlanDetailed"></a>
<a id="tocSplandetailed"></a>
<a id="tocsplandetailed"></a>

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "cases_count": 0,
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00",
  "created": "2021-12-30 19:23:59",
  "updated": "2021-12-30 19:23:59",
  "average_time": 0,
  "cases": [
    {
      "case_id": 0,
      "assignee_id": 0
    }
  ]
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Plan](#schemaplan)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» average_time|number|false|none|none|
|» cases|[object]|false|none|none|
|»» case_id|integer(int64)|false|none|none|
|»» assignee_id|integer(int64)¦null|false|none|none|

<h2 id="tocS_PlanUpdate">PlanUpdate</h2>
<!-- backwards compatibility -->
<a id="schemaplanupdate"></a>
<a id="schema_PlanUpdate"></a>
<a id="tocSplanupdate"></a>
<a id="tocsplanupdate"></a>

```json
{
  "title": "string",
  "description": "string",
  "cases": [
    0
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|cases|[integer]|false|none|none|

<h2 id="tocS_Project">Project</h2>
<!-- backwards compatibility -->
<a id="schemaproject"></a>
<a id="schema_Project"></a>
<a id="tocSproject"></a>
<a id="tocsproject"></a>

```json
{
  "title": "string",
  "code": "string",
  "counts": {
    "cases": 0,
    "suites": 0,
    "milestones": 0,
    "runs": {
      "total": 0,
      "active": 0
    },
    "defects": {
      "total": 0,
      "open": 0
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|false|none|none|
|code|string|false|none|none|
|counts|object|false|none|none|
|» cases|integer|false|none|none|
|» suites|integer|false|none|none|
|» milestones|integer|false|none|none|
|» runs|object|false|none|none|
|»» total|integer|false|none|none|
|»» active|integer|false|none|none|
|» defects|object|false|none|none|
|»» total|integer|false|none|none|
|»» open|integer|false|none|none|

<h2 id="tocS_ProjectAccess">ProjectAccess</h2>
<!-- backwards compatibility -->
<a id="schemaprojectaccess"></a>
<a id="schema_ProjectAccess"></a>
<a id="tocSprojectaccess"></a>
<a id="tocsprojectaccess"></a>

```json
{
  "member_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|member_id|integer(int64)|false|none|Team member id title.|

<h2 id="tocS_ProjectCreate">ProjectCreate</h2>
<!-- backwards compatibility -->
<a id="schemaprojectcreate"></a>
<a id="schema_ProjectCreate"></a>
<a id="tocSprojectcreate"></a>
<a id="tocsprojectcreate"></a>

```json
{
  "title": "string",
  "code": "string",
  "description": "string",
  "access": "all",
  "group": "string",
  "settings": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|Project title.|
|code|string|true|none|Project code. Unique for team. Digits and special characters are not allowed.|
|description|string|false|none|Project description.|
|access|string|false|none|none|
|group|string|false|none|Team group hash. Required if access param is set to group.|
|settings|object|false|none|Additional project settings.|

#### Enumerated Values

|Property|Value|
|---|---|
|access|all|
|access|group|
|access|none|

<h2 id="tocS_Result">Result</h2>
<!-- backwards compatibility -->
<a id="schemaresult"></a>
<a id="schema_Result"></a>
<a id="tocSresult"></a>
<a id="tocsresult"></a>

```json
{
  "hash": "string",
  "result_hash": "string",
  "comment": "string",
  "stacktrace": "string",
  "run_id": 0,
  "case_id": 0,
  "steps": [
    {
      "status": 0,
      "position": 0,
      "attachments": [
        {
          "size": 0,
          "mime": "string",
          "filename": "string",
          "url": "http://example.com"
        }
      ],
      "steps": [
        {}
      ]
    }
  ],
  "status": "string",
  "is_api_result": true,
  "time_spent_ms": 0,
  "end_time": "2021-12-30T19:23:59+00:00",
  "attachments": [
    {
      "size": 0,
      "mime": "string",
      "filename": "string",
      "url": "http://example.com"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hash|string|false|none|none|
|result_hash|string|false|none|none|
|comment|string¦null|false|none|none|
|stacktrace|string¦null|false|none|none|
|run_id|integer(int64)|false|none|none|
|case_id|integer(int64)|false|none|none|
|steps|[[TestStepResult](#schemateststepresult)]¦null|false|none|none|
|status|string|false|none|none|
|is_api_result|boolean|false|none|none|
|time_spent_ms|integer(int64)|false|none|none|
|end_time|string(date-time)¦null|false|none|none|
|attachments|[[Attachment](#schemaattachment)]|false|none|none|

<h2 id="tocS_ResultCreate">ResultCreate</h2>
<!-- backwards compatibility -->
<a id="schemaresultcreate"></a>
<a id="schema_ResultCreate"></a>
<a id="tocSresultcreate"></a>
<a id="tocsresultcreate"></a>

```json
{
  "case_id": 0,
  "case": {
    "title": "string",
    "suite_title": "string",
    "description": "string",
    "preconditions": "string",
    "postconditions": "string",
    "layer": "string",
    "severity": "string",
    "priority": "string"
  },
  "status": "string",
  "start_time": 0,
  "time": 31536000,
  "time_ms": 31536000000,
  "defect": true,
  "attachments": [
    "string"
  ],
  "stacktrace": "string",
  "comment": "string",
  "param": {
    "property1": "string",
    "property2": "string"
  },
  "param_groups": [
    [
      "string"
    ]
  ],
  "steps": [
    {
      "position": 0,
      "status": "passed",
      "comment": "string",
      "attachments": [
        "string"
      ],
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "steps": [
        {}
      ]
    }
  ],
  "author_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|case_id|integer(int64)|false|none|none|
|case|object|false|none|Could be used instead of `case_id`.|
|» title|string|false|none|none|
|» suite_title|string¦null|false|none|Nested suites should be separated with `TAB` symbol.|
|» description|string¦null|false|none|none|
|» preconditions|string¦null|false|none|none|
|» postconditions|string¦null|false|none|none|
|» layer|string|false|none|Slug of the layer. You can get it in the System Field settings.|
|» severity|string|false|none|Slug of the severity. You can get it in the System Field settings.|
|» priority|string|false|none|Slug of the priority. You can get it in the System Field settings.|
|status|string|true|none|Can have the following values `passed`, `failed`, `blocked`, `skipped`, `invalid` + custom statuses|
|start_time|integer¦null|false|none|none|
|time|integer(int64)¦null|false|none|none|
|time_ms|integer(int64)¦null|false|none|none|
|defect|boolean¦null|false|none|none|
|attachments|[string]¦null|false|none|none|
|stacktrace|string¦null|false|none|none|
|comment|string¦null|false|none|none|
|param|object¦null|false|none|A map of parameters (name => value)|
|» **additionalProperties**|string|false|none|none|
|param_groups|[array]¦null|false|none|List parameter groups by name only. Add their values in the 'param' field|
|steps|[[TestStepResultCreate](#schemateststepresultcreate)]¦null|false|none|none|
|author_id|integer(int64)¦null|false|none|none|

<h2 id="tocS_ResultCreateBulk">ResultCreateBulk</h2>
<!-- backwards compatibility -->
<a id="schemaresultcreatebulk"></a>
<a id="schema_ResultCreateBulk"></a>
<a id="tocSresultcreatebulk"></a>
<a id="tocsresultcreatebulk"></a>

```json
{
  "results": [
    {
      "case_id": 0,
      "case": {
        "title": "string",
        "suite_title": "string",
        "description": "string",
        "preconditions": "string",
        "postconditions": "string",
        "layer": "string",
        "severity": "string",
        "priority": "string"
      },
      "status": "string",
      "start_time": 0,
      "time": 31536000,
      "time_ms": 31536000000,
      "defect": true,
      "attachments": [
        "string"
      ],
      "stacktrace": "string",
      "comment": "string",
      "param": {
        "property1": "string",
        "property2": "string"
      },
      "param_groups": [
        [
          "string"
        ]
      ],
      "steps": [
        {
          "position": 0,
          "status": "passed",
          "comment": "string",
          "attachments": [
            "string"
          ],
          "action": "string",
          "expected_result": "string",
          "data": "string",
          "steps": [
            {}
          ]
        }
      ],
      "author_id": 0
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|results|[[ResultCreate](#schemaresultcreate)]|true|none|none|

<h2 id="tocS_ResultUpdate">ResultUpdate</h2>
<!-- backwards compatibility -->
<a id="schemaresultupdate"></a>
<a id="schema_ResultUpdate"></a>
<a id="tocSresultupdate"></a>
<a id="tocsresultupdate"></a>

```json
{
  "status": "in_progress",
  "time_ms": 31536000000,
  "defect": true,
  "attachments": [
    "string"
  ],
  "stacktrace": "string",
  "comment": "string",
  "steps": [
    {
      "position": 0,
      "status": "passed",
      "comment": "string",
      "attachments": [
        "string"
      ],
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "steps": [
        {}
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|string|false|none|none|
|time_ms|integer(int64)¦null|false|none|none|
|defect|boolean¦null|false|none|none|
|attachments|[string]¦null|false|none|none|
|stacktrace|string¦null|false|none|none|
|comment|string¦null|false|none|none|
|steps|[[TestStepResultCreate](#schemateststepresultcreate)]¦null|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|in_progress|
|status|passed|
|status|failed|
|status|blocked|
|status|skipped|

<h2 id="tocS_Run">Run</h2>
<!-- backwards compatibility -->
<a id="schemarun"></a>
<a id="schema_Run"></a>
<a id="tocSrun"></a>
<a id="tocsrun"></a>

```json
{
  "id": 0,
  "run_id": 0,
  "title": "string",
  "description": "string",
  "status": 0,
  "status_text": "string",
  "start_time": "2021-12-30T19:23:59+00:00",
  "end_time": "2021-12-30T19:23:59+00:00",
  "public": true,
  "stats": {
    "total": 0,
    "statuses": {
      "property1": 0,
      "property2": 0
    },
    "untested": 0,
    "passed": 0,
    "failed": 0,
    "blocked": 0,
    "skipped": 0,
    "retest": 0,
    "in_progress": 0,
    "invalid": 0
  },
  "time_spent": 0,
  "elapsed_time": 0,
  "environment": {
    "title": "string",
    "description": "string",
    "slug": "string",
    "host": "string"
  },
  "milestone": {
    "title": "string",
    "description": "string"
  },
  "custom_fields": [
    {
      "id": 0,
      "value": "string"
    }
  ],
  "tags": [
    {
      "title": "string",
      "internal_id": 0
    }
  ],
  "cases": [
    0
  ],
  "plan_id": 0,
  "configurations": [
    0
  ],
  "external_issue": {
    "id": "string",
    "type": "string",
    "link": "http://example.com"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|run_id|integer(int64)|false|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|status|integer|false|none|none|
|status_text|string|false|none|none|
|start_time|string(date-time)¦null|false|none|none|
|end_time|string(date-time)¦null|false|none|none|
|public|boolean|false|none|none|
|stats|object|false|none|none|
|» total|integer|false|none|none|
|» statuses|object|false|none|none|
|»» **additionalProperties**|integer|false|none|none|
|» untested|integer|false|none|none|
|» passed|integer|false|none|none|
|» failed|integer|false|none|none|
|» blocked|integer|false|none|none|
|» skipped|integer|false|none|none|
|» retest|integer|false|none|none|
|» in_progress|integer|false|none|none|
|» invalid|integer|false|none|none|
|time_spent|integer(int64)|false|none|Time in ms.|
|elapsed_time|integer(int64)|false|none|Time in ms.|
|environment|object¦null|false|none|none|
|» title|string|false|none|none|
|» description|string|false|none|none|
|» slug|string|false|none|none|
|» host|string|false|none|none|
|milestone|object¦null|false|none|none|
|» title|string|false|none|none|
|» description|string|false|none|none|
|custom_fields|[[CustomFieldValue](#schemacustomfieldvalue)]|false|none|none|
|tags|[[TagValue](#schematagvalue)]|false|none|none|
|cases|[integer]|false|none|none|
|plan_id|integer(int64)¦null|false|none|none|
|configurations|[integer]|false|none|none|
|external_issue|object¦null|false|none|none|
|» id|string|false|none|none|
|» type|string|false|none|none|
|» link|string(uri)|false|none|none|

<h2 id="tocS_RunCreate">RunCreate</h2>
<!-- backwards compatibility -->
<a id="schemaruncreate"></a>
<a id="schema_RunCreate"></a>
<a id="tocSruncreate"></a>
<a id="tocsruncreate"></a>

```json
{
  "title": "string",
  "description": "string",
  "include_all_cases": true,
  "cases": [
    0
  ],
  "is_autotest": true,
  "environment_id": 1,
  "environment_slug": "string",
  "milestone_id": 1,
  "plan_id": 1,
  "author_id": 1,
  "tags": [
    "string"
  ],
  "configurations": [
    0
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "start_time": "string",
  "end_time": "string",
  "is_cloud": true,
  "cloud_run_config": {
    "browser": "chromium"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string|false|none|none|
|include_all_cases|boolean|false|none|none|
|cases|[integer]|false|none|none|
|is_autotest|boolean|false|none|none|
|environment_id|integer(int64)|false|none|none|
|environment_slug|string|false|none|none|
|milestone_id|integer(int64)|false|none|none|
|plan_id|integer(int64)|false|none|none|
|author_id|integer(int64)|false|none|none|
|tags|[string]|false|none|none|
|configurations|[integer]|false|none|none|
|custom_field|object|false|none|A map of custom fields values (id => value)|
|» **additionalProperties**|string|false|none|none|
|start_time|string|false|none|none|
|end_time|string|false|none|none|
|is_cloud|boolean|false|none|Indicates if the run is created for the Test Cases produced by AIDEN|
|cloud_run_config|object|false|none|Configuration for the cloud run, if applicable|
|» browser|string|false|none|The browser to be used for the cloud run|

#### Enumerated Values

|Property|Value|
|---|---|
|browser|chromium|
|browser|firefox|
|browser|webkit|

<h2 id="tocS_RunPublic">RunPublic</h2>
<!-- backwards compatibility -->
<a id="schemarunpublic"></a>
<a id="schema_RunPublic"></a>
<a id="tocSrunpublic"></a>
<a id="tocsrunpublic"></a>

```json
{
  "status": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|boolean|true|none|none|

<h2 id="tocS_Requirement">Requirement</h2>
<!-- backwards compatibility -->
<a id="schemarequirement"></a>
<a id="schema_Requirement"></a>
<a id="tocSrequirement"></a>
<a id="tocsrequirement"></a>

```json
{
  "id": 0,
  "requirement_id": 0,
  "parent_id": 0,
  "member_id": 0,
  "title": "string",
  "description": "string",
  "status": "valid",
  "type": "epic",
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|requirement_id|integer(int64)|false|none|none|
|parent_id|integer(int64)¦null|false|none|none|
|member_id|integer(int64)|false|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|status|string|false|none|none|
|type|string|false|none|none|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)¦null|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|valid|
|status|draft|
|status|review|
|status|rework|
|status|finish|
|status|implemented|
|status|not-testable|
|status|obsolete|
|type|epic|
|type|user-story|
|type|feature|

<h2 id="tocS_SharedParameter">SharedParameter</h2>
<!-- backwards compatibility -->
<a id="schemasharedparameter"></a>
<a id="schema_SharedParameter"></a>
<a id="tocSsharedparameter"></a>
<a id="tocssharedparameter"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "title": "string",
  "type": "single",
  "project_codes": [
    "string"
  ],
  "is_enabled_for_all_projects": true,
  "parameters": [
    {
      "title": "string",
      "values": [
        "string"
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|title|string|true|none|none|
|type|string|true|none|none|
|project_codes|[string]|true|none|none|
|is_enabled_for_all_projects|boolean|true|none|none|
|parameters|any|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[TestCaseCreate/properties/parameters/items/oneOf/1](#schematestcasecreate/properties/parameters/items/oneof/1)]|false|none|Single parameter|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[TestCaseCreate/properties/parameters/items/oneOf/1](#schematestcasecreate/properties/parameters/items/oneof/1)]|false|none|Group parameter|

#### Enumerated Values

|Property|Value|
|---|---|
|type|single|
|type|group|

<h2 id="tocS_SharedParameterCreate">SharedParameterCreate</h2>
<!-- backwards compatibility -->
<a id="schemasharedparametercreate"></a>
<a id="schema_SharedParameterCreate"></a>
<a id="tocSsharedparametercreate"></a>
<a id="tocssharedparametercreate"></a>

```json
{
  "title": "string",
  "type": "single",
  "project_codes": [
    "string"
  ],
  "is_enabled_for_all_projects": true,
  "parameters": [
    {
      "title": "string",
      "values": [
        "string"
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|type|string|true|none|none|
|project_codes|[string]|false|none|List of project codes to associate with this shared parameter|
|is_enabled_for_all_projects|boolean|true|none|none|
|parameters|[SharedParameter/properties/parameters](#schemasharedparameter/properties/parameters)|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|single|
|type|group|

<h2 id="tocS_SharedParameterUpdate">SharedParameterUpdate</h2>
<!-- backwards compatibility -->
<a id="schemasharedparameterupdate"></a>
<a id="schema_SharedParameterUpdate"></a>
<a id="tocSsharedparameterupdate"></a>
<a id="tocssharedparameterupdate"></a>

```json
{
  "title": "string",
  "project_codes": [
    "string"
  ],
  "is_enabled_for_all_projects": true,
  "parameters": [
    {
      "title": "string",
      "values": [
        "string"
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|false|none|none|
|project_codes|[string]|false|none|List of project codes to associate with this shared parameter|
|is_enabled_for_all_projects|boolean|false|none|none|
|parameters|[SharedParameter/properties/parameters](#schemasharedparameter/properties/parameters)|false|none|none|

<h2 id="tocS_SharedStep">SharedStep</h2>
<!-- backwards compatibility -->
<a id="schemasharedstep"></a>
<a id="schema_SharedStep"></a>
<a id="tocSsharedstep"></a>
<a id="tocssharedstep"></a>

```json
{
  "hash": "string",
  "title": "string",
  "action": "string",
  "expected_result": "string",
  "steps": [
    {
      "data": "string",
      "hash": "string",
      "action": "string",
      "expected_result": "string",
      "attachments": [
        {
          "size": 0,
          "mime": "string",
          "filename": "string",
          "url": "http://example.com",
          "hash": "string"
        }
      ]
    }
  ],
  "data": "string",
  "cases": [
    0
  ],
  "cases_count": 0,
  "created": "2021-12-30 19:23:59",
  "updated": "2021-12-30 19:23:59",
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hash|string|false|none|none|
|title|string|false|none|none|
|action|string|false|none|none|
|expected_result|string|false|none|none|
|steps|[[SharedStepContent](#schemasharedstepcontent)]|false|none|none|
|data|string|false|none|none|
|cases|[integer]|false|none|none|
|cases_count|integer|false|none|none|
|created|string|false|none|Deprecated, use the `created_at` property instead.|
|updated|string|false|none|Deprecated, use the `updated_at` property instead.|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|

<h2 id="tocS_SharedStepCreate">SharedStepCreate</h2>
<!-- backwards compatibility -->
<a id="schemasharedstepcreate"></a>
<a id="schema_SharedStepCreate"></a>
<a id="tocSsharedstepcreate"></a>
<a id="tocssharedstepcreate"></a>

```json
{
  "title": "string",
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "steps": [
    {
      "hash": "string",
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "attachments": [
        "string"
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|action|string|false|none|Deprecated, use the `steps` property instead.|
|expected_result|string|false|none|Deprecated, use the `steps` property instead.|
|data|string|false|none|Deprecated, use the `steps` property instead.|
|steps|[[SharedStepContentCreate](#schemasharedstepcontentcreate)]|false|none|none|

<h2 id="tocS_SharedStepUpdate">SharedStepUpdate</h2>
<!-- backwards compatibility -->
<a id="schemasharedstepupdate"></a>
<a id="schema_SharedStepUpdate"></a>
<a id="tocSsharedstepupdate"></a>
<a id="tocssharedstepupdate"></a>

```json
{
  "title": "string",
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "steps": [
    {
      "hash": "string",
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "attachments": [
        "string"
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|action|string|false|none|Deprecated, use the `steps` property instead.|
|expected_result|string|false|none|Deprecated, use the `steps` property instead.|
|data|string|false|none|Deprecated, use the `steps` property instead.|
|steps|[[SharedStepContentCreate](#schemasharedstepcontentcreate)]|false|none|none|

<h2 id="tocS_SharedStepContentCreate">SharedStepContentCreate</h2>
<!-- backwards compatibility -->
<a id="schemasharedstepcontentcreate"></a>
<a id="schema_SharedStepContentCreate"></a>
<a id="tocSsharedstepcontentcreate"></a>
<a id="tocssharedstepcontentcreate"></a>

```json
{
  "hash": "string",
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "attachments": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hash|string|false|none|none|
|action|string|true|none|none|
|expected_result|string|false|none|none|
|data|string|false|none|none|
|attachments|[AttachmentHashList](#schemaattachmenthashlist)|false|none|A list of Attachment hashes.|

<h2 id="tocS_SharedStepContent">SharedStepContent</h2>
<!-- backwards compatibility -->
<a id="schemasharedstepcontent"></a>
<a id="schema_SharedStepContent"></a>
<a id="tocSsharedstepcontent"></a>
<a id="tocssharedstepcontent"></a>

```json
{
  "data": "string",
  "hash": "string",
  "action": "string",
  "expected_result": "string",
  "attachments": [
    {
      "size": 0,
      "mime": "string",
      "filename": "string",
      "url": "http://example.com",
      "hash": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|string|false|none|none|
|hash|string|false|none|none|
|action|string|false|none|none|
|expected_result|string|false|none|none|
|attachments|[[AttachmentHash](#schemaattachmenthash)]|false|none|none|

<h2 id="tocS_Suite">Suite</h2>
<!-- backwards compatibility -->
<a id="schemasuite"></a>
<a id="schema_Suite"></a>
<a id="tocSsuite"></a>
<a id="tocssuite"></a>

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "position": 0,
  "cases_count": 0,
  "parent_id": 0,
  "created": "2021-12-30 19:23:59",
  "updated": "2021-12-30 19:23:59",
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|preconditions|string¦null|false|none|none|
|position|integer|false|none|none|
|cases_count|integer|false|none|none|
|parent_id|integer(int64)¦null|false|none|none|
|created|string|false|none|Deprecated, use the `created_at` property instead.|
|updated|string¦null|false|none|Deprecated, use the `updated_at` property instead.|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|

<h2 id="tocS_SuiteCreate">SuiteCreate</h2>
<!-- backwards compatibility -->
<a id="schemasuitecreate"></a>
<a id="schema_SuiteCreate"></a>
<a id="tocSsuitecreate"></a>
<a id="tocssuitecreate"></a>

```json
{
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "parent_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|Test suite title.|
|description|string|false|none|Test suite description.|
|preconditions|string|false|none|Test suite preconditions|
|parent_id|integer(int64)¦null|false|none|Parent suite ID|

<h2 id="tocS_SuiteUpdate">SuiteUpdate</h2>
<!-- backwards compatibility -->
<a id="schemasuiteupdate"></a>
<a id="schema_SuiteUpdate"></a>
<a id="tocSsuiteupdate"></a>
<a id="tocssuiteupdate"></a>

```json
{
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "parent_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|false|none|Test suite title.|
|description|string|false|none|Test suite description.|
|preconditions|string|false|none|Test suite preconditions|
|parent_id|integer(int64)¦null|false|none|Parent suite ID|

<h2 id="tocS_SuiteDelete">SuiteDelete</h2>
<!-- backwards compatibility -->
<a id="schemasuitedelete"></a>
<a id="schema_SuiteDelete"></a>
<a id="tocSsuitedelete"></a>
<a id="tocssuitedelete"></a>

```json
{
  "destination_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|destination_id|integer(int64)|false|none|If provided, child test cases would be moved to suite with such ID.|

<h2 id="tocS_TagValue">TagValue</h2>
<!-- backwards compatibility -->
<a id="schematagvalue"></a>
<a id="schema_TagValue"></a>
<a id="tocStagvalue"></a>
<a id="tocstagvalue"></a>

```json
{
  "title": "string",
  "internal_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|false|none|none|
|internal_id|integer(int64)|false|none|none|

<h2 id="tocS_TestCase">TestCase</h2>
<!-- backwards compatibility -->
<a id="schematestcase"></a>
<a id="schema_TestCase"></a>
<a id="tocStestcase"></a>
<a id="tocstestcase"></a>

```json
{
  "id": 0,
  "position": 0,
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "severity": 0,
  "priority": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "behavior": 0,
  "automation": 0,
  "status": 0,
  "milestone_id": 0,
  "suite_id": 0,
  "custom_fields": [
    {
      "id": 0,
      "value": "string"
    }
  ],
  "attachments": [
    {
      "size": 0,
      "mime": "string",
      "filename": "string",
      "url": "http://example.com"
    }
  ],
  "steps_type": "string",
  "steps": [
    {
      "hash": "string",
      "shared_step_hash": "string",
      "shared_step_nested_hash": "string",
      "position": 0,
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "attachments": [
        {
          "size": 0,
          "mime": "string",
          "filename": "string",
          "url": "http://example.com"
        }
      ],
      "steps": [
        {}
      ]
    }
  ],
  "params": [
    null
  ],
  "parameters": [
    {
      "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a",
      "type": "single",
      "item": {
        "title": "string",
        "values": [
          "string"
        ]
      }
    }
  ],
  "tags": [
    {
      "title": "string",
      "internal_id": 0
    }
  ],
  "member_id": 0,
  "author_id": 0,
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00",
  "deleted": "2021-12-30T19:23:59.000000Z",
  "created": "2021-12-30T19:23:59.000000Z",
  "updated": "2021-12-30T19:23:59.000000Z",
  "external_issues": [
    {
      "type": "string",
      "issues": [
        {
          "id": "string",
          "link": "string"
        }
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|position|integer|false|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|preconditions|string¦null|false|none|none|
|postconditions|string¦null|false|none|none|
|severity|integer|false|none|none|
|priority|integer|false|none|none|
|type|integer|false|none|none|
|layer|integer|false|none|none|
|is_flaky|integer|false|none|none|
|behavior|integer|false|none|none|
|automation|integer|false|none|none|
|status|integer|false|none|none|
|milestone_id|integer(int64)¦null|false|none|none|
|suite_id|integer(int64)¦null|false|none|none|
|custom_fields|[[CustomFieldValue](#schemacustomfieldvalue)]|false|none|none|
|attachments|[[Attachment](#schemaattachment)]|false|none|none|
|steps_type|string¦null|false|none|none|
|steps|[[TestStep](#schemateststep)]|false|none|none|
|params|any|false|none|Deprecated, use `parameters` instead.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|parameters|[oneOf]|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|none|
|»»» shared_id|string(uuid)¦null|false|none|none|
|»»» type|string|true|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Single parameter|
|»»» type|string|false|none|none|
|»»» item|[TestCaseCreate/properties/parameters/items/oneOf/1](#schematestcasecreate/properties/parameters/items/oneof/1)|true|none|Single parameter|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|[TestCase/properties/parameters/items/oneOf/0/allOf/0](#schematestcase/properties/parameters/items/oneof/0/allof/0)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Group parameter|
|»»» type|string|false|none|none|
|»»» items|[[TestCaseCreate/properties/parameters/items/oneOf/1](#schematestcasecreate/properties/parameters/items/oneof/1)]|true|none|[Single parameter]|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tags|[[TagValue](#schematagvalue)]|false|none|none|
|member_id|integer(int64)|false|none|Deprecated, use `author_id` instead.|
|author_id|integer(int64)|false|none|none|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|
|deleted|string¦null|false|none|none|
|created|string|false|none|Deprecated, use the `created_at` property instead.|
|updated|string|false|none|Deprecated, use the `updated_at` property instead.|
|external_issues|[object]|false|none|none|
|» type|string|false|none|none|
|» issues|[object]|false|none|none|
|»» id|string|false|none|none|
|»» link|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|single|
|type|group|

<h2 id="tocS_TestCaseCreate">TestCaseCreate</h2>
<!-- backwards compatibility -->
<a id="schematestcasecreate"></a>
<a id="schema_TestCaseCreate"></a>
<a id="tocStestcasecreate"></a>
<a id="tocstestcasecreate"></a>

```json
{
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "title": "string",
  "severity": 0,
  "priority": 0,
  "behavior": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "suite_id": 0,
  "milestone_id": 0,
  "automation": 0,
  "status": 0,
  "attachments": [
    "string"
  ],
  "steps": [
    {
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "position": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {}
      ]
    }
  ],
  "tags": [
    "string"
  ],
  "params": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  },
  "parameters": [
    {
      "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
    }
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  },
  "created_at": "string",
  "updated_at": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string|false|none|none|
|preconditions|string|false|none|none|
|postconditions|string|false|none|none|
|title|string|true|none|none|
|severity|integer|false|none|none|
|priority|integer|false|none|none|
|behavior|integer|false|none|none|
|type|integer|false|none|none|
|layer|integer|false|none|none|
|is_flaky|integer|false|none|none|
|suite_id|integer(int64)|false|none|none|
|milestone_id|integer(int64)|false|none|none|
|automation|integer|false|none|none|
|status|integer|false|none|none|
|attachments|[AttachmentHashList](#schemaattachmenthashlist)|false|none|A list of Attachment hashes.|
|steps|[[TestStepCreate](#schemateststepcreate)]|false|none|none|
|tags|[string]|false|none|none|
|params|object¦null|false|none|Deprecated, use `parameters` instead.|
|» **additionalProperties**|[string]|false|none|none|
|parameters|[oneOf]¦null|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|Shared parameter|
|»» shared_id|string(uuid)|true|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|Single parameter|
|»» title|string|true|none|none|
|»» values|[string]|true|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|Group parameter|
|»» items|[[TestCaseCreate/properties/parameters/items/oneOf/1](#schematestcasecreate/properties/parameters/items/oneof/1)]|true|none|[Single parameter]|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|custom_field|object|false|none|A map of custom fields values (id => value)|
|» **additionalProperties**|string|false|none|none|
|created_at|string|false|none|none|
|updated_at|string|false|none|none|

<h2 id="tocS_TestCaseExternalIssues">TestCaseExternalIssues</h2>
<!-- backwards compatibility -->
<a id="schematestcaseexternalissues"></a>
<a id="schema_TestCaseExternalIssues"></a>
<a id="tocStestcaseexternalissues"></a>
<a id="tocstestcaseexternalissues"></a>

```json
{
  "type": "jira-cloud",
  "links": [
    {
      "case_id": 0,
      "external_issues": [
        "string"
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|true|none|none|
|links|[object]|true|none|none|
|» case_id|integer(int64)|true|none|none|
|» external_issues|[string]|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|jira-cloud|
|type|jira-server|

<h2 id="tocS_TestCaseUpdate">TestCaseUpdate</h2>
<!-- backwards compatibility -->
<a id="schematestcaseupdate"></a>
<a id="schema_TestCaseUpdate"></a>
<a id="tocStestcaseupdate"></a>
<a id="tocstestcaseupdate"></a>

```json
{
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "title": "string",
  "severity": 0,
  "priority": 0,
  "behavior": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "suite_id": 0,
  "milestone_id": 0,
  "automation": 0,
  "status": 0,
  "attachments": [
    "string"
  ],
  "steps": [
    {
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "position": 0,
      "attachments": [
        "string"
      ],
      "steps": [
        {}
      ]
    }
  ],
  "tags": [
    "string"
  ],
  "params": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  },
  "parameters": [
    {
      "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a"
    }
  ],
  "custom_field": {
    "property1": "string",
    "property2": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string|false|none|none|
|preconditions|string|false|none|none|
|postconditions|string|false|none|none|
|title|string|false|none|none|
|severity|integer|false|none|none|
|priority|integer|false|none|none|
|behavior|integer|false|none|none|
|type|integer|false|none|none|
|layer|integer|false|none|none|
|is_flaky|integer|false|none|none|
|suite_id|integer(int64)|false|none|none|
|milestone_id|integer(int64)|false|none|none|
|automation|integer|false|none|none|
|status|integer|false|none|none|
|attachments|[AttachmentHashList](#schemaattachmenthashlist)|false|none|A list of Attachment hashes.|
|steps|[[TestStepCreate](#schemateststepcreate)]|false|none|none|
|tags|[string]|false|none|none|
|params|object¦null|false|none|Deprecated, use `parameters` instead.|
|» **additionalProperties**|[string]|false|none|none|
|parameters|[[TestCaseCreate/properties/parameters/items](#schematestcasecreate/properties/parameters/items)]¦null|false|none|none|
|custom_field|object|false|none|A map of custom fields values (id => value)|
|» **additionalProperties**|string|false|none|none|

<h2 id="tocS_TestStep">TestStep</h2>
<!-- backwards compatibility -->
<a id="schemateststep"></a>
<a id="schema_TestStep"></a>
<a id="tocSteststep"></a>
<a id="tocsteststep"></a>

```json
{
  "hash": "string",
  "shared_step_hash": "string",
  "shared_step_nested_hash": "string",
  "position": 0,
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "attachments": [
    {
      "size": 0,
      "mime": "string",
      "filename": "string",
      "url": "http://example.com"
    }
  ],
  "steps": [
    {}
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hash|string|false|none|none|
|shared_step_hash|string¦null|false|none|none|
|shared_step_nested_hash|string¦null|false|none|none|
|position|integer|false|none|none|
|action|string|false|none|none|
|expected_result|string¦null|false|none|none|
|data|string¦null|false|none|none|
|attachments|[[Attachment](#schemaattachment)]|false|none|none|
|steps|[object]|false|none|Nested steps will be here. The same structure is used for them.|

<h2 id="tocS_TestStepCreate">TestStepCreate</h2>
<!-- backwards compatibility -->
<a id="schemateststepcreate"></a>
<a id="schema_TestStepCreate"></a>
<a id="tocSteststepcreate"></a>
<a id="tocsteststepcreate"></a>

```json
{
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "position": 0,
  "attachments": [
    "string"
  ],
  "steps": [
    {}
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|action|string|false|none|none|
|expected_result|string|false|none|none|
|data|string|false|none|none|
|position|integer|false|none|none|
|attachments|[AttachmentHashList](#schemaattachmenthashlist)|false|none|A list of Attachment hashes.|
|steps|[object]|false|none|Nested steps may be passed here. Use same structure for them.|

<h2 id="tocS_TestStepResultCreate">TestStepResultCreate</h2>
<!-- backwards compatibility -->
<a id="schemateststepresultcreate"></a>
<a id="schema_TestStepResultCreate"></a>
<a id="tocSteststepresultcreate"></a>
<a id="tocsteststepresultcreate"></a>

```json
{
  "position": 0,
  "status": "passed",
  "comment": "string",
  "attachments": [
    "string"
  ],
  "action": "string",
  "expected_result": "string",
  "data": "string",
  "steps": [
    {}
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|position|integer|false|none|none|
|status|string|true|none|none|
|comment|string¦null|false|none|none|
|attachments|[string]¦null|false|none|none|
|action|string|false|none|none|
|expected_result|string¦null|false|none|none|
|data|string¦null|false|none|none|
|steps|[object]|false|none|Nested steps results may be passed here. Use same structure for them.|

#### Enumerated Values

|Property|Value|
|---|---|
|status|passed|
|status|failed|
|status|blocked|
|status|in_progress|

<h2 id="tocS_TestStepResult">TestStepResult</h2>
<!-- backwards compatibility -->
<a id="schemateststepresult"></a>
<a id="schema_TestStepResult"></a>
<a id="tocSteststepresult"></a>
<a id="tocsteststepresult"></a>

```json
{
  "status": 0,
  "position": 0,
  "attachments": [
    {
      "size": 0,
      "mime": "string",
      "filename": "string",
      "url": "http://example.com"
    }
  ],
  "steps": [
    {}
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|integer|false|none|1 - passed, 2 - failed, 3 - blocked, 5 - skipped, 7 - in_progress|
|position|integer|false|none|none|
|attachments|[[Attachment](#schemaattachment)]|false|none|none|
|steps|[object]|false|none|Nested steps results will be here. The same structure is used for them for them.|

<h2 id="tocS_qql.Defect">qql.Defect</h2>
<!-- backwards compatibility -->
<a id="schemaqql.defect"></a>
<a id="schema_qql.Defect"></a>
<a id="tocSqql.defect"></a>
<a id="tocsqql.defect"></a>

```json
{
  "id": 0,
  "defect_id": 0,
  "title": "string",
  "actual_result": "string",
  "severity": "string",
  "status": "string",
  "milestone_id": 0,
  "custom_fields": [
    {
      "id": 0,
      "value": "string"
    }
  ],
  "attachments": [
    {
      "size": 0,
      "mime": "string",
      "filename": "string",
      "url": "http://example.com"
    }
  ],
  "resolved": "2019-08-24T14:15:22Z",
  "member_id": 0,
  "author_id": 0,
  "external_data": "string",
  "tags": [
    {
      "title": "string",
      "internal_id": 0
    }
  ],
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|defect_id|integer(int64)|true|none|none|
|title|string|false|none|none|
|actual_result|string|false|none|none|
|severity|string|false|none|none|
|status|string|false|none|none|
|milestone_id|integer(int64)¦null|false|none|none|
|custom_fields|[[CustomFieldValue](#schemacustomfieldvalue)]|false|none|none|
|attachments|[[Attachment](#schemaattachment)]|false|none|none|
|resolved|string(date-time)¦null|false|none|none|
|member_id|integer(int64)|false|none|Deprecated, use `author_id` instead.|
|author_id|integer(int64)|false|none|none|
|external_data|string|false|none|none|
|tags|[[TagValue](#schematagvalue)]|false|none|none|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|

<h2 id="tocS_qql.TestCase">qql.TestCase</h2>
<!-- backwards compatibility -->
<a id="schemaqql.testcase"></a>
<a id="schema_qql.TestCase"></a>
<a id="tocSqql.testcase"></a>
<a id="tocsqql.testcase"></a>

```json
{
  "id": 0,
  "test_case_id": 0,
  "position": 0,
  "title": "string",
  "description": "string",
  "preconditions": "string",
  "postconditions": "string",
  "severity": 0,
  "priority": 0,
  "type": 0,
  "layer": 0,
  "is_flaky": 0,
  "behavior": 0,
  "automation": 0,
  "status": 0,
  "milestone_id": 0,
  "suite_id": 0,
  "custom_fields": [
    {
      "id": 0,
      "value": "string"
    }
  ],
  "attachments": [
    {
      "size": 0,
      "mime": "string",
      "filename": "string",
      "url": "http://example.com"
    }
  ],
  "steps_type": "string",
  "steps": [
    {
      "hash": "string",
      "shared_step_hash": "string",
      "shared_step_nested_hash": "string",
      "position": 0,
      "action": "string",
      "expected_result": "string",
      "data": "string",
      "attachments": [
        {
          "size": 0,
          "mime": "string",
          "filename": "string",
          "url": "http://example.com"
        }
      ],
      "steps": [
        {}
      ]
    }
  ],
  "params": [
    null
  ],
  "tags": [
    {
      "title": "string",
      "internal_id": 0
    }
  ],
  "member_id": 0,
  "author_id": 0,
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00",
  "updated_by": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|test_case_id|integer(int64)|true|none|none|
|position|integer|false|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|preconditions|string¦null|false|none|none|
|postconditions|string¦null|false|none|none|
|severity|integer|false|none|none|
|priority|integer|false|none|none|
|type|integer|false|none|none|
|layer|integer|false|none|none|
|is_flaky|integer|false|none|none|
|behavior|integer|false|none|none|
|automation|integer|false|none|none|
|status|integer|false|none|none|
|milestone_id|integer(int64)¦null|false|none|none|
|suite_id|integer(int64)¦null|false|none|none|
|custom_fields|[[CustomFieldValue](#schemacustomfieldvalue)]|false|none|none|
|attachments|[[Attachment](#schemaattachment)]|false|none|none|
|steps_type|string¦null|false|none|none|
|steps|[[TestStep](#schemateststep)]|false|none|none|
|params|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tags|[[TagValue](#schematagvalue)]|false|none|none|
|member_id|integer(int64)|false|none|Deprecated, use `author_id` instead.|
|author_id|integer(int64)|false|none|none|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|
|updated_by|integer(int64)|false|none|Author ID of the last update.|

<h2 id="tocS_qql.Plan">qql.Plan</h2>
<!-- backwards compatibility -->
<a id="schemaqql.plan"></a>
<a id="schema_qql.Plan"></a>
<a id="tocSqql.plan"></a>
<a id="tocsqql.plan"></a>

```json
{
  "id": 0,
  "plan_id": 0,
  "title": "string",
  "description": "string",
  "cases_count": 0,
  "created_at": "2021-12-30T19:23:59+00:00",
  "updated_at": "2021-12-30T19:23:59+00:00"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|plan_id|integer(int64)|true|none|none|
|title|string|false|none|none|
|description|string¦null|false|none|none|
|cases_count|integer|false|none|none|
|created_at|string(date-time)|false|none|none|
|updated_at|string(date-time)|false|none|none|

<h2 id="tocS_Configuration">Configuration</h2>
<!-- backwards compatibility -->
<a id="schemaconfiguration"></a>
<a id="schema_Configuration"></a>
<a id="tocSconfiguration"></a>
<a id="tocsconfiguration"></a>

```json
{
  "id": 0,
  "title": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|title|string|false|none|none|

<h2 id="tocS_ConfigurationCreate">ConfigurationCreate</h2>
<!-- backwards compatibility -->
<a id="schemaconfigurationcreate"></a>
<a id="schema_ConfigurationCreate"></a>
<a id="tocSconfigurationcreate"></a>
<a id="tocsconfigurationcreate"></a>

```json
{
  "title": "string",
  "group_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|group_id|integer|true|none|none|

<h2 id="tocS_ConfigurationGroupCreate">ConfigurationGroupCreate</h2>
<!-- backwards compatibility -->
<a id="schemaconfigurationgroupcreate"></a>
<a id="schema_ConfigurationGroupCreate"></a>
<a id="tocSconfigurationgroupcreate"></a>
<a id="tocsconfigurationgroupcreate"></a>

```json
{
  "title": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|

<h2 id="tocS_User">User</h2>
<!-- backwards compatibility -->
<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "id": 0,
  "name": "string",
  "email": "string",
  "title": "string",
  "status": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|none|
|name|string|false|none|none|
|email|string|false|none|none|
|title|string|false|none|none|
|status|integer|false|none|none|

<h2 id="tocS_AttachmentResponse">AttachmentResponse</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentresponse"></a>
<a id="schema_AttachmentResponse"></a>
<a id="tocSattachmentresponse"></a>
<a id="tocsattachmentresponse"></a>

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

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[AttachmentGet](#schemaattachmentget)|false|none|none|

<h2 id="tocS_AttachmentListResponse">AttachmentListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentlistresponse"></a>
<a id="schema_AttachmentListResponse"></a>
<a id="tocSattachmentlistresponse"></a>
<a id="tocsattachmentlistresponse"></a>

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "hash": "string",
        "file": "string",
        "mime": "string",
        "size": 0,
        "extension": "string",
        "full_path": "http://example.com",
        "url": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[AttachmentGet](#schemaattachmentget)]|false|none|none|

<h2 id="tocS_AttachmentUploadsResponse">AttachmentUploadsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentuploadsresponse"></a>
<a id="schema_AttachmentUploadsResponse"></a>
<a id="tocSattachmentuploadsresponse"></a>
<a id="tocsattachmentuploadsresponse"></a>

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

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[object]|false|none|none|
|»» hash|string|false|none|none|
|»» filename|string|false|none|none|
|»» mime|string|false|none|none|
|»» extension|string|false|none|none|
|»» url|string|false|none|none|
|»» team|string|false|none|none|

<h2 id="tocS_AuthorResponse">AuthorResponse</h2>
<!-- backwards compatibility -->
<a id="schemaauthorresponse"></a>
<a id="schema_AuthorResponse"></a>
<a id="tocSauthorresponse"></a>
<a id="tocsauthorresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "author_id": 0,
    "entity_type": "string",
    "entity_id": 0,
    "email": "string",
    "name": "string",
    "is_active": true
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[Author](#schemaauthor)|false|none|none|

<h2 id="tocS_AuthorListResponse">AuthorListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaauthorlistresponse"></a>
<a id="schema_AuthorListResponse"></a>
<a id="tocSauthorlistresponse"></a>
<a id="tocsauthorlistresponse"></a>

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
        "author_id": 0,
        "entity_type": "string",
        "entity_id": 0,
        "email": "string",
        "name": "string",
        "is_active": true
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Author](#schemaauthor)]|false|none|none|

<h2 id="tocS_CustomFieldResponse">CustomFieldResponse</h2>
<!-- backwards compatibility -->
<a id="schemacustomfieldresponse"></a>
<a id="schema_CustomFieldResponse"></a>
<a id="tocScustomfieldresponse"></a>
<a id="tocscustomfieldresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "entity": "string",
    "type": "string",
    "placeholder": "string",
    "default_value": "string",
    "value": "string",
    "is_required": true,
    "is_visible": true,
    "is_filterable": true,
    "is_enabled_for_all_projects": true,
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "projects_codes": [
      "string"
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[CustomField](#schemacustomfield)|false|none|none|

<h2 id="tocS_CustomFieldsResponse">CustomFieldsResponse</h2>
<!-- backwards compatibility -->
<a id="schemacustomfieldsresponse"></a>
<a id="schema_CustomFieldsResponse"></a>
<a id="tocScustomfieldsresponse"></a>
<a id="tocscustomfieldsresponse"></a>

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
        "entity": "string",
        "type": "string",
        "placeholder": "string",
        "default_value": "string",
        "value": "string",
        "is_required": true,
        "is_visible": true,
        "is_filterable": true,
        "is_enabled_for_all_projects": true,
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59",
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00",
        "projects_codes": [
          "string"
        ]
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[CustomField](#schemacustomfield)]|false|none|none|

<h2 id="tocS_DefectResponse">DefectResponse</h2>
<!-- backwards compatibility -->
<a id="schemadefectresponse"></a>
<a id="schema_DefectResponse"></a>
<a id="tocSdefectresponse"></a>
<a id="tocsdefectresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "actual_result": "string",
    "severity": "string",
    "status": "string",
    "milestone_id": 0,
    "custom_fields": [
      {
        "id": 0,
        "value": "string"
      }
    ],
    "attachments": [
      {
        "size": 0,
        "mime": "string",
        "filename": "string",
        "url": "http://example.com"
      }
    ],
    "resolved_at": "2021-12-30T19:23:59+00:00",
    "member_id": 0,
    "author_id": 0,
    "external_data": "string",
    "runs": [
      0
    ],
    "results": [
      "string"
    ],
    "tags": [
      {
        "title": "string",
        "internal_id": 0
      }
    ],
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[Defect](#schemadefect)|false|none|none|

<h2 id="tocS_DefectListResponse">DefectListResponse</h2>
<!-- backwards compatibility -->
<a id="schemadefectlistresponse"></a>
<a id="schema_DefectListResponse"></a>
<a id="tocSdefectlistresponse"></a>
<a id="tocsdefectlistresponse"></a>

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
        "actual_result": "string",
        "severity": "string",
        "status": "string",
        "milestone_id": 0,
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "resolved_at": "2021-12-30T19:23:59+00:00",
        "member_id": 0,
        "author_id": 0,
        "external_data": "string",
        "runs": [
          0
        ],
        "results": [
          "string"
        ],
        "tags": [
          {
            "title": "string",
            "internal_id": 0
          }
        ],
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00",
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Defect](#schemadefect)]|false|none|none|

<h2 id="tocS_EnvironmentResponse">EnvironmentResponse</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentresponse"></a>
<a id="schema_EnvironmentResponse"></a>
<a id="tocSenvironmentresponse"></a>
<a id="tocsenvironmentresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "description": "string",
    "slug": "string",
    "host": "string"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[Environment](#schemaenvironment)|false|none|none|

<h2 id="tocS_EnvironmentListResponse">EnvironmentListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentlistresponse"></a>
<a id="schema_EnvironmentListResponse"></a>
<a id="tocSenvironmentlistresponse"></a>
<a id="tocsenvironmentlistresponse"></a>

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

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Environment](#schemaenvironment)]|false|none|none|

<h2 id="tocS_IdResponse">IdResponse</h2>
<!-- backwards compatibility -->
<a id="schemaidresponse"></a>
<a id="schema_IdResponse"></a>
<a id="tocSidresponse"></a>
<a id="tocsidresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» id|integer(int64)|false|none|none|

<h2 id="tocS_HashResponse">HashResponse</h2>
<!-- backwards compatibility -->
<a id="schemahashresponse"></a>
<a id="schema_HashResponse"></a>
<a id="tocShashresponse"></a>
<a id="tocshashresponse"></a>

```json
{
  "status": true,
  "result": {
    "hash": "string"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» hash|string|false|none|none|

<h2 id="tocS_MilestoneResponse">MilestoneResponse</h2>
<!-- backwards compatibility -->
<a id="schemamilestoneresponse"></a>
<a id="schema_MilestoneResponse"></a>
<a id="tocSmilestoneresponse"></a>
<a id="tocsmilestoneresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "description": "string",
    "status": "completed",
    "due_date": "2021-12-30T19:23:59+00:00",
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[Milestone](#schemamilestone)|false|none|none|

<h2 id="tocS_MilestoneListResponse">MilestoneListResponse</h2>
<!-- backwards compatibility -->
<a id="schemamilestonelistresponse"></a>
<a id="schema_MilestoneListResponse"></a>
<a id="tocSmilestonelistresponse"></a>
<a id="tocsmilestonelistresponse"></a>

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
        "status": "completed",
        "due_date": "2021-12-30T19:23:59+00:00",
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59",
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Milestone](#schemamilestone)]|false|none|none|

<h2 id="tocS_PlanResponse">PlanResponse</h2>
<!-- backwards compatibility -->
<a id="schemaplanresponse"></a>
<a id="schema_PlanResponse"></a>
<a id="tocSplanresponse"></a>
<a id="tocsplanresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "description": "string",
    "cases_count": 0,
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "average_time": 0,
    "cases": [
      {
        "case_id": 0,
        "assignee_id": 0
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[PlanDetailed](#schemaplandetailed)|false|none|none|

<h2 id="tocS_PlanListResponse">PlanListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaplanlistresponse"></a>
<a id="schema_PlanListResponse"></a>
<a id="tocSplanlistresponse"></a>
<a id="tocsplanlistresponse"></a>

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
        "cases_count": 0,
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00",
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Plan](#schemaplan)]|false|none|none|

<h2 id="tocS_ProjectResponse">ProjectResponse</h2>
<!-- backwards compatibility -->
<a id="schemaprojectresponse"></a>
<a id="schema_ProjectResponse"></a>
<a id="tocSprojectresponse"></a>
<a id="tocsprojectresponse"></a>

```json
{
  "status": true,
  "result": {
    "title": "string",
    "code": "string",
    "counts": {
      "cases": 0,
      "suites": 0,
      "milestones": 0,
      "runs": {
        "total": 0,
        "active": 0
      },
      "defects": {
        "total": 0,
        "open": 0
      }
    }
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[Project](#schemaproject)|false|none|none|

<h2 id="tocS_ProjectCodeResponse">ProjectCodeResponse</h2>
<!-- backwards compatibility -->
<a id="schemaprojectcoderesponse"></a>
<a id="schema_ProjectCodeResponse"></a>
<a id="tocSprojectcoderesponse"></a>
<a id="tocsprojectcoderesponse"></a>

```json
{
  "status": true,
  "result": {
    "code": "string"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» code|string|false|none|none|

<h2 id="tocS_ProjectListResponse">ProjectListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaprojectlistresponse"></a>
<a id="schema_ProjectListResponse"></a>
<a id="tocSprojectlistresponse"></a>
<a id="tocsprojectlistresponse"></a>

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "title": "string",
        "code": "string",
        "counts": {
          "cases": 0,
          "suites": 0,
          "milestones": 0,
          "runs": {
            "total": 0,
            "active": 0
          },
          "defects": {
            "total": 0,
            "open": 0
          }
        }
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Project](#schemaproject)]|false|none|none|

<h2 id="tocS_Response">Response</h2>
<!-- backwards compatibility -->
<a id="schemaresponse"></a>
<a id="schema_Response"></a>
<a id="tocSresponse"></a>
<a id="tocsresponse"></a>

```json
{
  "status": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|boolean|false|none|none|

<h2 id="tocS_ResultResponse">ResultResponse</h2>
<!-- backwards compatibility -->
<a id="schemaresultresponse"></a>
<a id="schema_ResultResponse"></a>
<a id="tocSresultresponse"></a>
<a id="tocsresultresponse"></a>

```json
{
  "status": true,
  "result": {
    "hash": "string",
    "result_hash": "string",
    "comment": "string",
    "stacktrace": "string",
    "run_id": 0,
    "case_id": 0,
    "steps": [
      {
        "status": 0,
        "position": 0,
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "steps": [
          {}
        ]
      }
    ],
    "status": "string",
    "is_api_result": true,
    "time_spent_ms": 0,
    "end_time": "2021-12-30T19:23:59+00:00",
    "attachments": [
      {
        "size": 0,
        "mime": "string",
        "filename": "string",
        "url": "http://example.com"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[Result](#schemaresult)|false|none|none|

<h2 id="tocS_ResultListResponse">ResultListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaresultlistresponse"></a>
<a id="schema_ResultListResponse"></a>
<a id="tocSresultlistresponse"></a>
<a id="tocsresultlistresponse"></a>

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "hash": "string",
        "result_hash": "string",
        "comment": "string",
        "stacktrace": "string",
        "run_id": 0,
        "case_id": 0,
        "steps": [
          {
            "status": 0,
            "position": 0,
            "attachments": [
              {
                "size": 0,
                "mime": "string",
                "filename": "string",
                "url": "http://example.com"
              }
            ],
            "steps": [
              {}
            ]
          }
        ],
        "status": "string",
        "is_api_result": true,
        "time_spent_ms": 0,
        "end_time": "2021-12-30T19:23:59+00:00",
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ]
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Result](#schemaresult)]|false|none|none|

<h2 id="tocS_RunResponse">RunResponse</h2>
<!-- backwards compatibility -->
<a id="schemarunresponse"></a>
<a id="schema_RunResponse"></a>
<a id="tocSrunresponse"></a>
<a id="tocsrunresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "run_id": 0,
    "title": "string",
    "description": "string",
    "status": 0,
    "status_text": "string",
    "start_time": "2021-12-30T19:23:59+00:00",
    "end_time": "2021-12-30T19:23:59+00:00",
    "public": true,
    "stats": {
      "total": 0,
      "statuses": {
        "property1": 0,
        "property2": 0
      },
      "untested": 0,
      "passed": 0,
      "failed": 0,
      "blocked": 0,
      "skipped": 0,
      "retest": 0,
      "in_progress": 0,
      "invalid": 0
    },
    "time_spent": 0,
    "elapsed_time": 0,
    "environment": {
      "title": "string",
      "description": "string",
      "slug": "string",
      "host": "string"
    },
    "milestone": {
      "title": "string",
      "description": "string"
    },
    "custom_fields": [
      {
        "id": 0,
        "value": "string"
      }
    ],
    "tags": [
      {
        "title": "string",
        "internal_id": 0
      }
    ],
    "cases": [
      0
    ],
    "plan_id": 0,
    "configurations": [
      0
    ],
    "external_issue": {
      "id": "string",
      "type": "string",
      "link": "http://example.com"
    }
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[Run](#schemarun)|false|none|none|

<h2 id="tocS_RunListResponse">RunListResponse</h2>
<!-- backwards compatibility -->
<a id="schemarunlistresponse"></a>
<a id="schema_RunListResponse"></a>
<a id="tocSrunlistresponse"></a>
<a id="tocsrunlistresponse"></a>

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
        "run_id": 0,
        "title": "string",
        "description": "string",
        "status": 0,
        "status_text": "string",
        "start_time": "2021-12-30T19:23:59+00:00",
        "end_time": "2021-12-30T19:23:59+00:00",
        "public": true,
        "stats": {
          "total": 0,
          "statuses": {
            "property1": 0,
            "property2": 0
          },
          "untested": 0,
          "passed": 0,
          "failed": 0,
          "blocked": 0,
          "skipped": 0,
          "retest": 0,
          "in_progress": 0,
          "invalid": 0
        },
        "time_spent": 0,
        "elapsed_time": 0,
        "environment": {
          "title": "string",
          "description": "string",
          "slug": "string",
          "host": "string"
        },
        "milestone": {
          "title": "string",
          "description": "string"
        },
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "tags": [
          {
            "title": "string",
            "internal_id": 0
          }
        ],
        "cases": [
          0
        ],
        "plan_id": 0,
        "configurations": [
          0
        ],
        "external_issue": {
          "id": "string",
          "type": "string",
          "link": "http://example.com"
        }
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Run](#schemarun)]|false|none|none|

<h2 id="tocS_RunPublicResponse">RunPublicResponse</h2>
<!-- backwards compatibility -->
<a id="schemarunpublicresponse"></a>
<a id="schema_RunPublicResponse"></a>
<a id="tocSrunpublicresponse"></a>
<a id="tocsrunpublicresponse"></a>

```json
{
  "status": true,
  "result": {
    "url": "http://example.com"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» url|string(uri)|false|none|none|

<h2 id="tocS_SearchResponse">SearchResponse</h2>
<!-- backwards compatibility -->
<a id="schemasearchresponse"></a>
<a id="schema_SearchResponse"></a>
<a id="tocSsearchresponse"></a>
<a id="tocssearchresponse"></a>

```json
{
  "status": true,
  "result": {
    "entities": [
      {
        "id": 0,
        "run_id": 0,
        "title": "string",
        "description": "string",
        "status": 0,
        "status_text": "string",
        "start_time": "2021-12-30T19:23:59+00:00",
        "end_time": "2021-12-30T19:23:59+00:00",
        "public": true,
        "stats": {
          "total": 0,
          "statuses": {
            "property1": 0,
            "property2": 0
          },
          "untested": 0,
          "passed": 0,
          "failed": 0,
          "blocked": 0,
          "skipped": 0,
          "retest": 0,
          "in_progress": 0,
          "invalid": 0
        },
        "time_spent": 0,
        "elapsed_time": 0,
        "environment": {
          "title": "string",
          "description": "string",
          "slug": "string",
          "host": "string"
        },
        "milestone": {
          "title": "string",
          "description": "string"
        },
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "tags": [
          {
            "title": "string",
            "internal_id": 0
          }
        ],
        "cases": [
          0
        ],
        "plan_id": 0
      }
    ],
    "total": 0
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» entities|[oneOf]|true|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|object|false|none|none|
|»»»» id|integer(int64)|false|none|none|
|»»»» run_id|integer(int64)|true|none|none|
|»»»» title|string|false|none|none|
|»»»» description|string¦null|false|none|none|
|»»»» status|integer|false|none|none|
|»»»» status_text|string|false|none|none|
|»»»» start_time|string(date-time)¦null|false|none|none|
|»»»» end_time|string(date-time)¦null|false|none|none|
|»»»» public|boolean|false|none|none|
|»»»» stats|object|false|none|none|
|»»»»» total|integer|false|none|none|
|»»»»» statuses|object|false|none|none|
|»»»»»» **additionalProperties**|integer|false|none|none|
|»»»»» untested|integer|false|none|none|
|»»»»» passed|integer|false|none|none|
|»»»»» failed|integer|false|none|none|
|»»»»» blocked|integer|false|none|none|
|»»»»» skipped|integer|false|none|none|
|»»»»» retest|integer|false|none|none|
|»»»»» in_progress|integer|false|none|none|
|»»»»» invalid|integer|false|none|none|
|»»»» time_spent|integer(int64)|false|none|Time in ms.|
|»»»» elapsed_time|integer(int64)|false|none|Time in ms.|
|»»»» environment|object¦null|false|none|none|
|»»»»» title|string|false|none|none|
|»»»»» description|string|false|none|none|
|»»»»» slug|string|false|none|none|
|»»»»» host|string|false|none|none|
|»»»» milestone|object¦null|false|none|none|
|»»»»» title|string|false|none|none|
|»»»»» description|string|false|none|none|
|»»»» custom_fields|[[CustomFieldValue](#schemacustomfieldvalue)]|false|none|none|
|»»»» tags|[[TagValue](#schematagvalue)]|false|none|none|
|»»»» cases|[integer]|false|none|none|
|»»»» plan_id|integer(int64)¦null|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|object|false|none|none|
|»»»» hash|string|false|none|none|
|»»»» result_hash|string|true|none|none|
|»»»» comment|string¦null|false|none|none|
|»»»» stacktrace|string¦null|false|none|none|
|»»»» run_id|integer(int64)|false|none|none|
|»»»» case_id|integer(int64)|false|none|none|
|»»»» steps|[[TestStepResult](#schemateststepresult)]¦null|false|none|none|
|»»»» status|string|false|none|none|
|»»»» is_api_result|boolean|false|none|none|
|»»»» time_spent_ms|integer(int64)|false|none|none|
|»»»» end_time|string(date-time)¦null|false|none|none|
|»»»» attachments|[[Attachment](#schemaattachment)]|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|object|false|none|none|
|»»»» id|integer(int64)|false|none|none|
|»»»» requirement_id|integer(int64)|true|none|none|
|»»»» parent_id|integer(int64)¦null|false|none|none|
|»»»» member_id|integer(int64)|false|none|none|
|»»»» title|string|false|none|none|
|»»»» description|string¦null|false|none|none|
|»»»» status|string|false|none|none|
|»»»» type|string|false|none|none|
|»»»» created_at|string(date-time)|false|none|none|
|»»»» updated_at|string(date-time)¦null|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|[qql.TestCase](#schemaqql.testcase)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|[qql.Defect](#schemaqql.defect)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|[qql.Plan](#schemaqql.plan)|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» total|integer|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|valid|
|status|draft|
|status|review|
|status|rework|
|status|finish|
|status|implemented|
|status|not-testable|
|status|obsolete|
|type|epic|
|type|user-story|
|type|feature|

<h2 id="tocS_SharedParameterResponse">SharedParameterResponse</h2>
<!-- backwards compatibility -->
<a id="schemasharedparameterresponse"></a>
<a id="schema_SharedParameterResponse"></a>
<a id="tocSsharedparameterresponse"></a>
<a id="tocssharedparameterresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "title": "string",
    "type": "single",
    "project_codes": [
      "string"
    ],
    "is_enabled_for_all_projects": true,
    "parameters": [
      {
        "title": "string",
        "values": [
          "string"
        ]
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[SharedParameter](#schemasharedparameter)|false|none|none|

<h2 id="tocS_SharedParameterListResponse">SharedParameterListResponse</h2>
<!-- backwards compatibility -->
<a id="schemasharedparameterlistresponse"></a>
<a id="schema_SharedParameterListResponse"></a>
<a id="tocSsharedparameterlistresponse"></a>
<a id="tocssharedparameterlistresponse"></a>

```json
{
  "status": true,
  "result": {
    "total": 0,
    "entities": [
      {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "title": "string",
        "type": "single",
        "project_codes": [
          "string"
        ],
        "is_enabled_for_all_projects": true,
        "parameters": [
          {
            "title": "string",
            "values": [
              "string"
            ]
          }
        ]
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|true|none|none|
|»» entities|[[SharedParameter](#schemasharedparameter)]|true|none|none|

<h2 id="tocS_SharedStepResponse">SharedStepResponse</h2>
<!-- backwards compatibility -->
<a id="schemasharedstepresponse"></a>
<a id="schema_SharedStepResponse"></a>
<a id="tocSsharedstepresponse"></a>
<a id="tocssharedstepresponse"></a>

```json
{
  "status": true,
  "result": {
    "hash": "string",
    "title": "string",
    "action": "string",
    "expected_result": "string",
    "steps": [
      {
        "data": "string",
        "hash": "string",
        "action": "string",
        "expected_result": "string",
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com",
            "hash": "string"
          }
        ]
      }
    ],
    "data": "string",
    "cases": [
      0
    ],
    "cases_count": 0,
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[SharedStep](#schemasharedstep)|false|none|none|

<h2 id="tocS_SharedStepListResponse">SharedStepListResponse</h2>
<!-- backwards compatibility -->
<a id="schemasharedsteplistresponse"></a>
<a id="schema_SharedStepListResponse"></a>
<a id="tocSsharedsteplistresponse"></a>
<a id="tocssharedsteplistresponse"></a>

```json
{
  "status": true,
  "result": {
    "total": 0,
    "filtered": 0,
    "count": 0,
    "entities": [
      {
        "hash": "string",
        "title": "string",
        "action": "string",
        "expected_result": "string",
        "steps": [
          {
            "data": "string",
            "hash": "string",
            "action": "string",
            "expected_result": "string",
            "attachments": [
              {
                "size": 0,
                "mime": "string",
                "filename": "string",
                "url": "http://example.com",
                "hash": "string"
              }
            ]
          }
        ],
        "data": "string",
        "cases": [
          0
        ],
        "cases_count": 0,
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59",
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[SharedStep](#schemasharedstep)]|false|none|none|

<h2 id="tocS_SuiteResponse">SuiteResponse</h2>
<!-- backwards compatibility -->
<a id="schemasuiteresponse"></a>
<a id="schema_SuiteResponse"></a>
<a id="tocSsuiteresponse"></a>
<a id="tocssuiteresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "title": "string",
    "description": "string",
    "preconditions": "string",
    "position": 0,
    "cases_count": 0,
    "parent_id": 0,
    "created": "2021-12-30 19:23:59",
    "updated": "2021-12-30 19:23:59",
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[Suite](#schemasuite)|false|none|none|

<h2 id="tocS_SuiteListResponse">SuiteListResponse</h2>
<!-- backwards compatibility -->
<a id="schemasuitelistresponse"></a>
<a id="schema_SuiteListResponse"></a>
<a id="tocSsuitelistresponse"></a>
<a id="tocssuitelistresponse"></a>

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
        "preconditions": "string",
        "position": 0,
        "cases_count": 0,
        "parent_id": 0,
        "created": "2021-12-30 19:23:59",
        "updated": "2021-12-30 19:23:59",
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[Suite](#schemasuite)]|false|none|none|

<h2 id="tocS_TestCaseResponse">TestCaseResponse</h2>
<!-- backwards compatibility -->
<a id="schematestcaseresponse"></a>
<a id="schema_TestCaseResponse"></a>
<a id="tocStestcaseresponse"></a>
<a id="tocstestcaseresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "position": 0,
    "title": "string",
    "description": "string",
    "preconditions": "string",
    "postconditions": "string",
    "severity": 0,
    "priority": 0,
    "type": 0,
    "layer": 0,
    "is_flaky": 0,
    "behavior": 0,
    "automation": 0,
    "status": 0,
    "milestone_id": 0,
    "suite_id": 0,
    "custom_fields": [
      {
        "id": 0,
        "value": "string"
      }
    ],
    "attachments": [
      {
        "size": 0,
        "mime": "string",
        "filename": "string",
        "url": "http://example.com"
      }
    ],
    "steps_type": "string",
    "steps": [
      {
        "hash": "string",
        "shared_step_hash": "string",
        "shared_step_nested_hash": "string",
        "position": 0,
        "action": "string",
        "expected_result": "string",
        "data": "string",
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "steps": [
          {}
        ]
      }
    ],
    "params": [
      null
    ],
    "parameters": [
      {
        "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a",
        "type": "single",
        "item": {
          "title": "string",
          "values": [
            "string"
          ]
        }
      }
    ],
    "tags": [
      {
        "title": "string",
        "internal_id": 0
      }
    ],
    "member_id": 0,
    "author_id": 0,
    "created_at": "2021-12-30T19:23:59+00:00",
    "updated_at": "2021-12-30T19:23:59+00:00",
    "deleted": "2021-12-30T19:23:59.000000Z",
    "created": "2021-12-30T19:23:59.000000Z",
    "updated": "2021-12-30T19:23:59.000000Z",
    "external_issues": [
      {
        "type": "string",
        "issues": [
          {
            "id": "string",
            "link": "string"
          }
        ]
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[TestCase](#schematestcase)|false|none|none|

<h2 id="tocS_TestCaseListResponse">TestCaseListResponse</h2>
<!-- backwards compatibility -->
<a id="schematestcaselistresponse"></a>
<a id="schema_TestCaseListResponse"></a>
<a id="tocStestcaselistresponse"></a>
<a id="tocstestcaselistresponse"></a>

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
        "position": 0,
        "title": "string",
        "description": "string",
        "preconditions": "string",
        "postconditions": "string",
        "severity": 0,
        "priority": 0,
        "type": 0,
        "layer": 0,
        "is_flaky": 0,
        "behavior": 0,
        "automation": 0,
        "status": 0,
        "milestone_id": 0,
        "suite_id": 0,
        "custom_fields": [
          {
            "id": 0,
            "value": "string"
          }
        ],
        "attachments": [
          {
            "size": 0,
            "mime": "string",
            "filename": "string",
            "url": "http://example.com"
          }
        ],
        "steps_type": "string",
        "steps": [
          {
            "hash": "string",
            "shared_step_hash": "string",
            "shared_step_nested_hash": "string",
            "position": 0,
            "action": "string",
            "expected_result": "string",
            "data": "string",
            "attachments": [
              {
                "size": 0,
                "mime": "string",
                "filename": "string",
                "url": "http://example.com"
              }
            ],
            "steps": [
              {}
            ]
          }
        ],
        "params": [
          null
        ],
        "parameters": [
          {
            "shared_id": "ff4ec820-e78c-460e-95db-6a3c1e8cdd1a",
            "type": "single",
            "item": {
              "title": "string",
              "values": [
                "string"
              ]
            }
          }
        ],
        "tags": [
          {
            "title": "string",
            "internal_id": 0
          }
        ],
        "member_id": 0,
        "author_id": 0,
        "created_at": "2021-12-30T19:23:59+00:00",
        "updated_at": "2021-12-30T19:23:59+00:00",
        "deleted": "2021-12-30T19:23:59.000000Z",
        "created": "2021-12-30T19:23:59.000000Z",
        "updated": "2021-12-30T19:23:59.000000Z",
        "external_issues": [
          {
            "type": "string",
            "issues": [
              {
                "id": "string",
                "link": "string"
              }
            ]
          }
        ]
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[TestCase](#schematestcase)]|false|none|none|

<h2 id="tocS_ConfigurationListResponse">ConfigurationListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaconfigurationlistresponse"></a>
<a id="schema_ConfigurationListResponse"></a>
<a id="tocSconfigurationlistresponse"></a>
<a id="tocsconfigurationlistresponse"></a>

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
        "configurations": [
          {
            "id": 0,
            "title": "string"
          }
        ]
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[object]|false|none|none|
|»»» id|integer(int64)|false|none|none|
|»»» title|string|false|none|none|
|»»» configurations|[[Configuration](#schemaconfiguration)]|false|none|none|

<h2 id="tocS_UserResponse">UserResponse</h2>
<!-- backwards compatibility -->
<a id="schemauserresponse"></a>
<a id="schema_UserResponse"></a>
<a id="tocSuserresponse"></a>
<a id="tocsuserresponse"></a>

```json
{
  "status": true,
  "result": {
    "id": 0,
    "name": "string",
    "email": "string",
    "title": "string",
    "status": 0
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|[User](#schemauser)|false|none|none|

<h2 id="tocS_UserListResponse">UserListResponse</h2>
<!-- backwards compatibility -->
<a id="schemauserlistresponse"></a>
<a id="schema_UserListResponse"></a>
<a id="tocSuserlistresponse"></a>
<a id="tocsuserlistresponse"></a>

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
        "name": "string",
        "email": "string",
        "title": "string",
        "status": 0
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Response](#schemaresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» result|object|false|none|none|
|»» total|integer|false|none|none|
|»» filtered|integer|false|none|none|
|»» count|integer|false|none|none|
|»» entities|[[User](#schemauser)]|false|none|none|
