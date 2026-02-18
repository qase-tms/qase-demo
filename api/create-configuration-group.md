# Create Configuration Group

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