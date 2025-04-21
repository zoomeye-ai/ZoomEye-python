<h1 class="zoomeye-references">ZoomEye API v2 参考手册</h1>

- [Introduction](#introduction)
- [Search Description](#Search Description)
- [Authentication](#authentication)
  - [User](#user)
    - [Code samples](#code-samples)
    - [Example responses](#example-responses)
    - [Response field description](#response-field-description)
  - [Asset Search](#asset-search)
    - [Code samples](#code-samples-1)
    - [Parameters](#parameters)
    - [Example responses](#example-responses-1)
    - [Response field description](#response-field-description-1)
    - [Related references](#related-references)
        - [base64 encoding conversion](#base64-encoding-conversion)

# Introduction

**Update time**：2024-12-04

ZoomEye provides a powerful and flexible RESTful API for network research enthusiasts, developers, and security geeks, enabling seamless access to platform resources, automating network exploration, and building a wide range of application scenarios, With the ZoomEye API, you can:

① **Automate Asset Discovery**

Perform bulk searches of global network devices, services, and systems to create a comprehensive map of network assets.

② **Manage and Integrate Attack Surfaces**

Leverage the API to seamlessly integrate network asset data into existing attack surface management platform, enabling precise identification and reduction of exposure risks.

③ **Real-time Monitoring and Threat Alerts**

Continuously track sensitive assets exposed on the internet and detect potential risks in real-time.

④ **Customized Data Analysis and Tool Development**

Use ZoomEye’s rich dataset to develop custom tools, such as IoT security validation utilities, vulnerability scanning plugins, and threat intelligence analysis systems.

⑤ **Generate Visualized Reports**

Automatically extract data to generate asset or risk reports, empowering informed and effective security decision-making.

Base URLs: <a href="https://api.zoomeye.ai">https://api.zoomeye.ai</a>

Email: <a href="mailto:support@zoomeye.ai">API Support</a>

# Search Description

● Search scope covers devices (IPv4, IPv6) and websites (domain names)

● When entering a search string, the system will match the keywords in "global" mode, covering content from various protocols such as HTTP, SSH, FTP, etc. (e.g., HTTP/HTTPS protocol headers, body, SSL, title, and other protocol banners)

● The search string is case-insensitive and will be matched after segmentation (the search results page provides a "segmentation" test function). Use == for precise matching and strict restriction of search syntax case sensitivity.

● Please use quotation marks for search strings (e.g., "Cisco System" or 'Cisco System'). If there are quotation marks in the search string, use \ for escape, e.g., "a\"b". If there are brackets in the search string, use \ for escape, e.g., portinfo\(\)

**Search Logic Operations**

| **SearchLogic** | **Description**                                              | **Example**                                                  |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| =               | Search for assets containing keywords                        | [title="knownsec"](https://www.zoomeye.ai/searchResult?q=dGl0bGU9Imtub3duc2VjIg%3D%3D)Search for websites with titles containing Knowsec's assets |
| ==              | Accurate search, indicating a complete match of keywords (case sensitive), can search for data with empty values | [title=="knownsec"](https://www.zoomeye.ai/searchResult?q=dGl0bGU9PSJrbm93bnNlYyI%3D)Precise search, which means exact match of keywords (case sensitive), and can search for data with empty values Search for assets with the website title "Knownsec" |
| \|\|            | Enter "\|\|" in the search box to indicate the logical operation of "or" | [service="ssh" \|\| service="http"](https://www.zoomeye.ai/searchResult?q=c2VydmljZT0ic3NoIiB8fCBzZXJ2aWNlPSJodHRwIg%3D%3D)Search for SSH or HTTP data |
| &&              | Enter "&&" in the search box to indicate the logical operation of "and" | [device="router" && after="2020-01-01"](https://www.zoomeye.ai/searchResult?q=ZGV2aWNlPSJyb3V0ZXIiICYmIGFmdGVyPSIyMDIwLTAxLTAxIg%3D%3D)Search for routers after Jan 1, 2020 |
| !=              | Enter "!=" in the search box to indicate the logical operation of "not" | [country="US" && subdivisions!="new york"](https://www.zoomeye.ai/searchResult?q=Y291bnRyeT0iVVMiICYmIHN1YmRpdmlzaW9ucyE9Im5ldyB5b3JrIg%3D%3D)Search for data in united states excluding new york |
| ()              | Enter "()" in the search box to indicate the logical operation of "priority processing" | [(country="US" && port!=80) \|\| (country="US" && title!="404 Not Found")](https://www.zoomeye.ai/searchResult?q=KGNvdW50cnk9IlVTIiAmJiBwb3J0IT04MCkgfHwgKGNvdW50cnk9IlVTIiAmJiB0aXRsZSE9IjQwNCBOb3QgRm91bmQiKQ%3D%3D)Search excluding port 80 in US or "404 not found" in the US |
| *               | Fuzzy search, use * for search                               | [title="google*"](https://www.zoomeye.ai/searchResult?q=dGl0bGU9Imdvb2dsZSoi)Fuzzy search, use * to search Search for assets containing google in the website title, and the title can end with any character |

**Geographical Location Search**

| **Filter**                                                   | **Description**                                          | **Tips**                                                     |
| ------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------ |
| [country="CN"](https://www.zoomeye.ai/searchResult?q=Y291bnRyeT0iQ04i) | Search for country assets                                | Input country abbreviations or names, e.g.[country="china"](https://www.zoomeye.ai/searchResult?q=Y291bnRyeT0iY2hpbmEi) |
| [subdivisions="beijing"](https://www.zoomeye.ai/searchResult?q=c3ViZGl2aXNpb25zPSJiZWlqaW5nIg%3D%3D) | Search for assets in the specified administrative region | Input in English, e.g.[subdivisions="beijing"](https://www.zoomeye.ai/searchResult?q=c3ViZGl2aXNpb25zPSJiZWlqaW5nIg%3D%3D) |
| [city="changsha"](https://www.zoomeye.ai/searchResult?q=Y2l0eT0iY2hhbmdzaGEi) | Search for city assets                                   | Input in English, e.g.[city="changsha"](https://www.zoomeye.ai/searchResult?q=Y2l0eT0iY2hhbmdzaGEi) |

**Certificate Search**

| **Filter**                                                   | **Description**                                              | **Tips**                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ssl="google"](https://www.zoomeye.ai/searchResult?q=c3NsPSJnb29nbGUi) | Search for assets with "google" string in ssl certificate    | Often used to search for corresponding targets by product name and company name |
| [ssl.cert.fingerprint="F3C98F223D82CC41CF83D94671CCC6C69873FABF"](https://www.zoomeye.ai/searchResult?q=c3NsLmNlcnQuZmluZ2VycHJpbnQ9IkYzQzk4RjIyM0Q4MkNDNDFDRjgzRDk0NjcxQ0NDNkM2OTg3M0ZBQkYi) | Search for certificate-related fingerprint assets            |                                                              |
| [ssl.chain_count=3](https://www.zoomeye.ai/searchResult?q=c3NsLmNoYWluX2NvdW50PTM%3D) | Search for SSL chain count assets                            |                                                              |
| [ssl.cert.alg="SHA256-RSA"](https://www.zoomeye.ai/searchResult?q=c3NsLmNlcnQuYWxnPSJTSEEyNTYtUlNBIg%3D%3D) | Search for signature algorithms supported by certificates    |                                                              |
| [ssl.cert.issuer.cn="pbx.wildix.com"](https://www.zoomeye.ai/searchResult?q=c3NsLmNlcnQuaXNzdWVyLmNuPSJwYngud2lsZGl4LmNvbSI%3D) | Search for the common domain name of the user certificate issuer |                                                              |
| [ssl.cert.pubkey.rsa.bits=2048](https://www.zoomeye.ai/searchResult?q=c3NsLmNlcnQucHVia2V5LnJzYS5iaXRzPTIwNDg%3D) | Search for rsa_bits certificate public key bit number        |                                                              |
| [ssl.cert.pubkey.ecdsa.bits=256](https://www.zoomeye.ai/searchResult?q=c3NsLmNlcnQucHVia2V5LmVjZHNhLmJpdHM9MjU2) | Search for ecdsa_bits certificate public key bit number      |                                                              |
| [ssl.cert.pubkey.type="RSA"](https://www.zoomeye.ai/searchResult?q=c3NsLmNlcnQucHVia2V5LnR5cGU9IlJTQSI%3D) | Search for the public key type of the certificate            |                                                              |
| [ssl.cert.serial="18460192207935675900910674501"](https://www.zoomeye.ai/searchResult?q=c3NsLmNlcnQuc2VyaWFsPSIxODQ2MDE5MjIwNzkzNTY3NTkwMDkxMDY3NDUwMSI%3D) | Search for certificate serial number                         |                                                              |
| [ssl.cipher.bits="128"](https://www.zoomeye.ai/searchResult?q=c3NsLmNpcGhlci5iaXRzPSIxMjgi) | Search for encryption suite bit number                       |                                                              |
| [ssl.cipher.name="TLS_AES_128_GCM_SHA256"](https://www.zoomeye.ai/searchResult?q=c3NsLmNpcGhlci5uYW1lPSJUTFNfQUVTXzEyOF9HQ01fU0hBMjU2Ig%3D%3D) | Search for encryption suite name                             |                                                              |
| [ssl.cipher.version="TLSv1.3"](https://www.zoomeye.ai/searchResult?q=c3NsLmNpcGhlci52ZXJzaW9uPSJUTFN2MS4zIg%3D%3D) | Search for encryption suite version                          |                                                              |
| [ssl.version="TLSv1.3"](https://www.zoomeye.ai/searchResult?q=c3NsLnZlcnNpb249IlRMU3YxLjMi) | Search for the SSL version of the certificate                |                                                              |
| [ssl.cert.subject.cn="example.com"](https://www.zoomeye.ai/searchResult?q=c3NsLmNlcnQuc3ViamVjdC5jbj0iZXhhbXBsZS5jb20i) | Search for the common domain name of the user certificate holder |                                                              |
| [ssl.jarm="29d29d15d29d29d00029d29d29d29dea0f89a2e5fb09e4d8e099befed92cfa"](https://www.zoomeye.ai/searchResult?q=c3NsLmphcm09IjI5ZDI5ZDE1ZDI5ZDI5ZDAwMDI5ZDI5ZDI5ZDI5ZGVhMGY4OWEyZTVmYjA5ZTRkOGUwOTliZWZlZDkyY2ZhIg%3D%3D) | Search for assets related to Jarm Fingerprint content        |                                                              |
| [ssl.ja3s=45094d08156d110d8ee97b204143db14](https://www.zoomeye.ai/searchResult?q=c3NsLmphM3M9NDUwOTRkMDgxNTZkMTEwZDhlZTk3YjIwNDE0M2RiMTQ%3D) | Find assets related to specific JA3S fingerprints            |                                                              |

**IP or Domain Name Related Information Search**

| **Filter**                                                   | **Description**                                              | **Tips**                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ip="8.8.8.8"](https://www.zoomeye.ai/searchResult?q=aXA9IjguOC44Ljgi) | Search for assets related to the specified IPv4 address      |                                                              |
| [ip="2600:3c00::f03c:91ff:fefc:574a"](https://www.zoomeye.ai/searchResult?q=aXA9IjI2MDA6M2MwMDo6ZjAzYzo5MWZmOmZlZmM6NTc0YSI%3D) | Search for assets related to specified IPv6 address          |                                                              |
| [cidr="52.2.254.36/24"](https://www.zoomeye.ai/searchResult?q=Y2lkcj0iNTIuMi4yNTQuMzYvMjQi) | Search for C-class assets of IP                              | cidr="52.2.254.36/16"is the B class of the IP, cidr="52.2.254.36/8"is the A class of the IP, e.g.[cidr="52.2.254.36/16"](https://www.zoomeye.ai/searchResult?q=Y2lkcj0iNTIuMi4yNTQuMzYvMTYi)[cidr="52.2.254.36/8"](https://www.zoomeye.ai/searchResult?q=Y2lkcj0iNTIuMi4yNTQuMzYvOCI%3D) |
| [org="Stanford University"](https://www.zoomeye.ai/searchResult?q=b3JnPSJTdGFuZm9yZCBVbml2ZXJzaXR5Ig%3D%3D) | Search for assets of related organizations                   | Used to locate IP assets corresponding to universities, structures, and large Internet companies |
| [isp="China Mobile"](https://www.zoomeye.ai/searchResult?q=aXNwPSJDaGluYSBNb2JpbGUi) | Search for assets of related network service providers       | Can be supplemented with org data                            |
| [asn=42893](https://www.zoomeye.ai/searchResult?q=YXNuPTQyODkz) | Search for IP assets related to corresponding ASN (Autonomous system number) |                                                              |
| [port=80](https://www.zoomeye.ai/searchResult?q=cG9ydD04MA%3D%3D) | Search for related port assets                               | Currently does not support simultaneous open multi-port target search |
| [hostname="google.com"](https://www.zoomeye.ai/searchResult?q=aG9zdG5hbWU9Imdvb2dsZS5jb20i) |                                                              | Search for assets of related IP "hostname"                   |
| [domain="baidu.com"](https://www.zoomeye.ai/searchResult?q=ZG9tYWluPSJiYWlkdS5jb20i) | Search for domain-related assets                             | Used to search domain and subdomain data                     |
| [banner="FTP"](https://www.zoomeye.ai/searchResult?q=YmFubmVyPSJGVFAi) | Search by protocol messages                                  | Used for searching HTTP response header data                 |
| [http.header="http"](https://www.zoomeye.ai/searchResult?q=aHR0cC5oZWFkZXI9Imh0dHAi) | Search by HTTP response header                               | Used for searching HTTP response header data                 |
| [http.header_hash="27f9973fe57298c3b63919259877a84d"](https://www.zoomeye.ai/searchResult?q=aHR0cC5oZWFkZXJfaGFzaD0iMjdmOTk3M2ZlNTcyOThjM2I2MzkxOTI1OTg3N2E4NGQi) | Search by the hash values calculated from HTTP header.       |                                                              |
| [http.header.server="Nginx"](https://www.zoomeye.ai/searchResult?q=aHR0cC5oZWFkZXIuc2VydmVyPSJOZ2lueCIJ) | Search by server of the HTTP header                          | Used for searching the server data in HTTP response headers  |
| [http.header.version="1.2"](https://www.zoomeye.ai/searchResult?q=aHR0cC5oZWFkZXIudmVyc2lvbj0iMS4yIg%3D%3D) | Search by version number in the HTTP header                  |                                                              |
| [http.header.status_code="200"](https://www.zoomeye.ai/searchResult?q=aHR0cC5oZWFkZXIuc3RhdHVzX2NvZGU9IjIwMCI%3D) | Search by HTTP response status code                          | Search for assets with HTTP response status code 200 or other status codes, such as 302, 404, etc. |
| [http.body="document"](https://www.zoomeye.ai/searchResult?q=aHR0cC5ib2R5PSJkb2N1bWVudCI%3D) | Search by HTML body                                          |                                                              |
| [http.body_hash="84a18166fde3ee7e7c974b8d1e7e21b4"](https://www.zoomeye.ai/searchResult?q=aHR0cC5ib2R5X2hhc2g9Ijg0YTE4MTY2ZmRlM2VlN2U3Yzk3NGI4ZDFlN2UyMWI0Igk%3D) | Search by hash value calculated from HTML body               |                                                              |

**Fingerprint Search**

| **Filter**                                                   | **Description**                                              | **Tips**                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [app="Cisco ASA SSL VPN"](https://www.zoomeye.ai/searchResult?q=YXBwPSJDaXNjbyBBU0EgU1NMIFZQTiI%3D) | Search for Cisco ASA-SSL-VPN devices                         | For more app rules, please refer to [object Object]. Entering keywords such as "Cisco" in the search box will display related app prompts |
| [service="ssh"](https://www.zoomeye.ai/searchResult?q=c2VydmljZT0ic3NoIg%3D%3D) | Search for assets related to the specified service protocol  | Common service protocols include: http, ftp, ssh, telnet, etc. (other services can be found in the domain name sidebar aggregation display of search results) |
| [device="router"](https://www.zoomeye.ai/searchResult?q=ZGV2aWNlPSJyb3V0ZXIi) | Search for router-related device types                       | Common types include router, switch, storage-misc, etc. (other types can be found in the domain name sidebar aggregation display of search results) |
| [os="RouterOS"](https://www.zoomeye.ai/searchResult?q=b3M9IlJvdXRlck9TIg%3D%3D) | Search for related operating systems                         | Common systems include Linux, Windows, RouterOS, IOS, JUNOS, etc. (other systems can be found in the domain name sidebar aggregation display of search results) |
| [title="Cisco"](https://www.zoomeye.ai/searchResult?q=dGl0bGU9IkNpc2NvIg%3D%3D) | Search for data with "Cisco" in the title of the HTML content |                                                              |
| [industry="government"](https://www.zoomeye.ai/searchResult?q=aW5kdXN0cnk9ImdvdmVybm1lbnQi) | Search for assets related to the specified industry type     | Common industry types include technology, energy, finance, manufacturing, etc. (other types can be supplemented with org data) |
| [product="Cisco"](https://www.zoomeye.ai/searchResult?q=cHJvZHVjdD0iQ2lzY28i) | Search for assets with "Cisco" in the component information  | Support mainstream asset component search                    |
| [protocol="TCP"](https://www.zoomeye.ai/searchResult?q=cHJvdG9jb2w9IlRDUCI%3D) | Search for assets with the transmission protocol as TCP      | Common transmission protocols include TCP, UDP, TCP6, SCTP   |
| [is_honeypot="True"](https://www.zoomeye.ai/searchResult?q=aXNfaG9uZXlwb3Q9IlRydWUi) | Filter for honeypot assets                                   |                                                              |

**Time Node or Interval Related Search**

| **Filter**                                                   | **Description**                                              | **Tips**                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------- |
| [after="2020-01-01" && port="50050"](https://www.zoomeye.ai/searchResult?q=YWZ0ZXI9IjIwMjAtMDEtMDEiICYmIHBvcnQ9IjUwMDUwIg%3D%3D) | Search for assets with an update time after Jan 1, 2020 and a port 50050 | Time filters need to be combined with other filters |
| [before="2020-01-01" && port="50050"](https://www.zoomeye.ai/searchResult?q=YmVmb3JlPSIyMDIwLTAxLTAxIiAmJiBwb3J0PSI1MDA1MCI%3D) | Search for assets with an update time before Jan 1, 2020 and a port 50050 | Time filters need to be combined with other filters |

**Dig**

| **Filter**                                                   | **Description**                            | **Tips** |
| ------------------------------------------------------------ | ------------------------------------------ | -------- |
| [dig="baidu.com 220.181.38.148"](https://www.zoomeye.ai/searchResult?q=ZGlnPSJiYWlkdS5jb20gMjIwLjE4MS4zOC4xNDgi) | Search for assets with related dig content |          |

**Iconhash**

| **Filter**                                                   | **Description**                                              | **Tips**                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------- |
| [iconhash="f3418a443e7d841097c714d69ec4bcb8"](https://www.zoomeye.ai/searchResult?q=aWNvbmhhc2g9ImYzNDE4YTQ0M2U3ZDg0MTA5N2M3MTRkNjllYzRiY2I4Ig%3D%3D) | Analyze the target data by MD5 and search for assets with related content based on the icon | Search for assets with the "google" icon |
| [iconhash="1941681276"](https://www.zoomeye.ai/searchResult?q=aWNvbmhhc2g9IjE5NDE2ODEyNzYi) | Analyze the target data by MMH3 and search for assets with related content based on the icon | Search for assets with the "amazon" icon |

**Filehash**

| **Filter**                                                   | **Description**                                              | **Tips**                               |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------- |
| [filehash="0b5ce08db7fb8fffe4e14d05588d49d9"](https://www.zoomeye.ai/searchResult?q=ZmlsZWhhc2g9IjBiNWNlMDhkYjdmYjhmZmZlNGUxNGQwNTU4OGQ0OWQ5Ig%3D%3D) | Search for assets with related content based on the parsed file data | Search for assets parsed with "Gitlab" |



# Authentication

* ZoomEye-API supports API-KEY authentication, Each account will find the `API-KEY` string at the bottom of its profile page. Just fill in the string into the `API-KEY` field of ZoomEye-API. You can get the API-KEY from. [here](https://www.zoomeye.ai/profile)

<img style="max-width: 100%" src="/v2/static/images/doc-api-key-en.png" >

## User

Get user information, subscription details and current points.

`POST /v2/userinfo`

### Code samples

```bash
# Bash
curl -X POST https://api.zoomeye.ai/v2/userinfo -H "API-KEY: $YOUR_API_KEY"
```

### Example responses

```json
{
  "code": 60000,
  "message": "success",
  "data": {
    "username": "abc",
    "email": "user@example.com",
    "phone": "+1234567890",
    "created_at": "2023-01-15T08:00:00Z",
    "subscription": {
      "plan": "Premium",
      "end_date": "2024-01-20T00:00:00Z",
      "points": "30000",
      "zoomeye_points": "10000000"
    }
  }
}
```

### Response field description

|Name|Type| Description                                                                                      |
|---|---|--------------------------------------------------------------------------------------------------|
|code|integer| Response code                                                                                    |
|message|string| Response message                                                                                 |
|data|object| User information and subscription details                                                        |
|username|string| Username                                                                                         |
|email|string| User email                                                                                       |
|phone|string| User phone number                                                                                |
|created_at|string(date-time)| user creation time                                                                               |
|subscription|object| subscription information                                                                         |
|plan|string| subscription plan                                                                                |
|end_date|string(date-time)| subscription end date                                                                            |
|points|string| Available General Points, You can also see it from [here](https://www.zoomeye.ai/profile/record) |
|zoomeye_points|string| Available ZoomEye-Points, You can also see it from [here](https://www.zoomeye.ai/profile/record) |


## Asset Search

Get network asset information based on query conditions.

`POST /v2/search`

### Code samples

```bash
# Bash
curl -X POST 'https://api.zoomeye.ai/v2/search' -H "API-KEY: $YOUR_API_KEY" \
-H 'content-type: application/json' \
-d '{
  "qbase64": "dGl0bGU9ImNpc2NvIHZwbiIK",
  "page": 1
}'
```

### Parameters

|Field Name|Type|Required|Description|
|---|---|---|---|
|qbase64|string|true|Base64 encoded query string. For more, refer to  **Related references**.|
|fields|string|false|The fields to return, separated by commas. Default: ip, port, domain, update_time. For more, refer to **Response field description**|
|sub_type|string|false|Data type, supports v4, v6, and web. Default is v4.|
|page|integer|false|View asset page number|
|pagesize|integer|false|Number of records per page, default is 10, maximum is 10,000.|
|facets|string|false|Statistical items, separated by commas if there are multiple. Supports country, subdivisions, city, product, service, device, OS, and port.|
|ignore_cache|boolean|false|Whether to ignore the cache. false, supported by Business plan and above.|

### Example responses

```json
{
  "code": 60000,
  "message": "success",
  "total": 163139107,
  "query": "title=\"cisco vpn\"",
  "data": [
    {
      "url": "https://1.1.1.1:443",
      "ssl.jarm": "29d29d15d29d29d00029d29d29d29dea0f89a2e5fb09e4d8e099befed92cfa",
      "ssl.ja3s": "45094d08156d110d8ee97b204143db14",
      "iconhash_md5": "f3418a443e7d841097c714d69ec4bcb8",
      "robots_md5": "0b5ce08db7fb8fffe4e14d05588d49d9",
      "security_md5": "0b5ce08db7fb8fffe4e14d05588d49d9",
      "ip": "1.1.1.1",
      "domain": "www.google.com",
      "hostname": "SPACEX",
      "os": "windows",
      "port": 443,
      "service": "https",
      "title": ["GoogleGoogle appsGoogle Search"],
      "version": "1.1.0",
      "device": "webcam",
      "rdns": "c01031-001.cust.wallcloud.ch",
      "product": "OpenSSD",
      "header": "HTTP/1.1 302 Found Location: https://www.google.com/?gws_rd=ssl Cache-Control: private...",
      "header_hash": "27f9973fe57298c3b63919259877a84d",
      "body": "HTTP/1.1 302 Found Location: https://www.google.com/?gws_rd=ssl Cache-Control: private...",
      "body_hash": "84a18166fde3ee7e7c974b8d1e7e21b4",
      "banner": "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3",
      "update_time": "2024-07-03T14:34:10",
      "header.server.name": "nginx",
      "header.server.version": "1.8.1",
      "continent.name": "Europe",
      "country.name": "Germany",
      "province.name": "Hesse",
      "city.name": "Frankfurt",
      "lon": "118.753262",
      "lat": "32.064838",
      "isp.name": "aviel.ru",
      "organization.name": "SERVISFIRST BANK",
      "zipcode": "210003",
      "idc": 0,
      "honeypot": 0,
      "asn": 4837,
      "protocol": "tcp",
      "ssl": "SSL Certificate Version: TLS 1.2 CipherSuit: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256...",
      "primary_industry": "Finance",
      "sub_industry": "bank",
      "rank": 60
    }
  ]
}
```

### Response field description

The query interface supports a large number of fields, such as ip, port, domain, update_time, etc.

| Field Name         | Type    | Description                                                  | Permission                  |
| ------------------ | ------- | ------------------------------------------------------------ | --------------------------- |
| ip                 | string  | IP address (used when the web asset is incomplete)           | All users                   |
| domain             | string  | Domain                                                       | All users                   |
| url                | string  | Full URL of the asset (for web assets)                       | All users                   |
| ssl.jarm           | string  | SSL JARM fingerprint                                         | All users                   |
| ssl.ja3s           | string  | SSL JA3S fingerprint                                         | All users                   |
| iconhash_md5       | string  | MD5 value of the icon image                                  | Professional plan and above |
| robots_md5         | string  | MD5 value of the robots.txt file                             | Business plan and above     |
| security_md5       | string  | MD5 value of the security settings file                      | Business plan and above     |
| hostname           | string  | Hostname information                                         | All users                   |
| os                 | string  | Operating system information                                 | All users                   |
| port               | integer | Port number                                                  | All users                   |
| service            | string  | Provided application protocol (e.g., HTTP, SSH)              | All users                   |
| title              | list    | Webpage title                                                | All users                   |
| version            | string  | Component version information                                | All users                   |
| device             | string  | Device name                                                  | All users                   |
| rdns               | string  | Reverse DNS information                                      | All users                   |
| product            | string  | Product component information                                | All users                   |
| header             | string  | HTTP response header information                             | All users                   |
| header_hash        | string  | Hash calculated from HTTP response header                    | Professional plan and above |
| banner             | string  | Service banner information                                   | All users                   |
| body               | string  | HTML Body content                                            | Business plan and above     |
| body_hash          | string  | Hash calculated from the HTML body                           | Professional plan and above |
| update_time        | string  | Asset update time                                            | All users                   |
| header.server.name | string  | Server name in the HTTP response header                      | All users                   |
| continent.name     | string  | Name of the continent                                        | All users                   |
| country.name       | string  | Name of the country                                          | All users                   |
| province.name      | string  | Name of the province                                         | All users                   |
| city.name          | string  | Name of the city                                             | All users                   |
| isp.name           | string  | ISP name                                                     | All users                   |
| organization.name  | string  | Organization name                                            | All users                   |
| zipcode            | integer | Postal code                                                  | All users                   |
| idc                | string  | Is it an IDC (0 for no, 1 for yes)                           | All users                   |
| lon                | string  | Geolocation longitude                                        | All users                   |
| lat                | string  | Geolocation latitude                                         | All users                   |
| asn                | string  | Autonomous System Number                                     | All users                   |
| protocol           | string  | Transport layer protocol (e.g., TCP, UDP)                    | All users                   |
| honeypot           | integer | Is it a honeypot (0 for no, 1 for yes)                       | All users                   |
| ssl                | string  | SSL x509 certificate information                             | All users                   |
| primary_industry   | string  | Primary industry information                                 | Business plan and above     |
| sub_industry       | string  | Sub-industry information                                     | Business plan and above     |
| rank               | integer | Asset importance ranking, the higher the score, the more important. | Business plan and above     |

### Related references

##### base64 encoding conversion

Convert the query condition to base64 encoding and pass it to the API as a qbase64 parameter.

```bash
#bash
 echo 'title="knownsec"' | base64
```
