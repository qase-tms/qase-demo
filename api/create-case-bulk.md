# Create Case Bulk

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