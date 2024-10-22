# polar-sdk

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=polar-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install polar-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add polar-sdk
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.benefits.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from polar_sdk import Polar

async def main():
    s = Polar(
        access_token="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.users.benefits.list_async()
    if res is not None:
        while True:
            # handle items

            res = res.next()
            if res is None:
                break

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [advertisements](https://github.com/polarsource/polar-python/blob/master/docs/sdks/advertisements/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/advertisements/README.md#list) - List Campaigns
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/advertisements/README.md#get) - Get Campaign

### [articles](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#list) - List Articles
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#create) - Create Article
* [export](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#export) - Export Articles
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#get) - Get Article
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#update) - Update Article
* [delete](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#delete) - Delete Article
* [receivers](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#receivers) - Get Article Receivers Count
* [preview](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#preview) - Send Article Preview
* [send](https://github.com/polarsource/polar-python/blob/master/docs/sdks/articles/README.md#send) - Send Article

### [benefits](https://github.com/polarsource/polar-python/blob/master/docs/sdks/benefits/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/benefits/README.md#list) - List Benefits
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/benefits/README.md#create) - Create Benefit
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/benefits/README.md#get) - Get Benefit
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/benefits/README.md#update) - Update Benefit
* [delete](https://github.com/polarsource/polar-python/blob/master/docs/sdks/benefits/README.md#delete) - Delete Benefit
* [grants](https://github.com/polarsource/polar-python/blob/master/docs/sdks/benefits/README.md#grants) - List Benefit Grants

### [checkout_links](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkoutlinks/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkoutlinks/README.md#list) - List Checkout Links
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkoutlinks/README.md#create) - Create Checkout Link
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkoutlinks/README.md#get) - Get Checkout Link
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkoutlinks/README.md#update) - Update Checkout Link
* [delete](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkoutlinks/README.md#delete) - Delete Checkout Link

### [checkouts](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkouts/README.md)

* [~~create~~](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkouts/README.md#create) - Create Checkout :warning: **Deprecated** Use `create` instead.
* [~~get~~](https://github.com/polarsource/polar-python/blob/master/docs/sdks/checkouts/README.md#get) - Get Checkout :warning: **Deprecated**

#### [checkouts.custom](https://github.com/polarsource/polar-python/blob/master/docs/sdks/custom/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/custom/README.md#list) - List Checkout Sessions
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/custom/README.md#create) - Create Checkout Session
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/custom/README.md#get) - Get Checkout Session
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/custom/README.md#update) - Update Checkout Session
* [client_get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/custom/README.md#client_get) - Get Checkout Session from Client
* [client_update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/custom/README.md#client_update) - Update Checkout Session from Client
* [client_confirm](https://github.com/polarsource/polar-python/blob/master/docs/sdks/custom/README.md#client_confirm) - Confirm Checkout Session from Client

### [external_organizations](https://github.com/polarsource/polar-python/blob/master/docs/sdks/externalorganizations/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/externalorganizations/README.md#list) - List External Organizations

### [files](https://github.com/polarsource/polar-python/blob/master/docs/sdks/files/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/files/README.md#list) - List Files
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/files/README.md#create) - Create File
* [uploaded](https://github.com/polarsource/polar-python/blob/master/docs/sdks/files/README.md#uploaded) - Complete File Upload
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/files/README.md#update) - Update File
* [delete](https://github.com/polarsource/polar-python/blob/master/docs/sdks/files/README.md#delete) - Delete File

### [license_keys](https://github.com/polarsource/polar-python/blob/master/docs/sdks/licensekeys/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/licensekeys/README.md#list) - List License Keys
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/licensekeys/README.md#get) - Get License Key
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/licensekeys/README.md#update) - Update License Key
* [get_activation](https://github.com/polarsource/polar-python/blob/master/docs/sdks/licensekeys/README.md#get_activation) - Get Activation

### [metrics](https://github.com/polarsource/polar-python/blob/master/docs/sdks/metricssdk/README.md)

* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/metricssdk/README.md#get) - Get Metrics
* [limits](https://github.com/polarsource/polar-python/blob/master/docs/sdks/metricssdk/README.md#limits) - Get Metrics Limits

### [oauth2](https://github.com/polarsource/polar-python/blob/master/docs/sdks/oauth2/README.md)

* [token](https://github.com/polarsource/polar-python/blob/master/docs/sdks/oauth2/README.md#token) - Request Token
* [revoke](https://github.com/polarsource/polar-python/blob/master/docs/sdks/oauth2/README.md#revoke) - Revoke Token
* [introspect](https://github.com/polarsource/polar-python/blob/master/docs/sdks/oauth2/README.md#introspect) - Introspect Token
* [userinfo](https://github.com/polarsource/polar-python/blob/master/docs/sdks/oauth2/README.md#userinfo) - Get User Info

#### [oauth2.clients](https://github.com/polarsource/polar-python/blob/master/docs/sdks/clients/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/clients/README.md#list) - List Clients
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/clients/README.md#create) - Create Client
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/clients/README.md#get) - Get Client
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/clients/README.md#update) - Update Client
* [delete](https://github.com/polarsource/polar-python/blob/master/docs/sdks/clients/README.md#delete) - Delete Client

### [orders](https://github.com/polarsource/polar-python/blob/master/docs/sdks/orders/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/orders/README.md#list) - List Orders
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/orders/README.md#get) - Get Order
* [invoice](https://github.com/polarsource/polar-python/blob/master/docs/sdks/orders/README.md#invoice) - Get Order Invoice

### [organizations](https://github.com/polarsource/polar-python/blob/master/docs/sdks/organizations/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/organizations/README.md#list) - List Organizations
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/organizations/README.md#create) - Create Organization
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/organizations/README.md#get) - Get Organization
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/organizations/README.md#update) - Update Organization


### [products](https://github.com/polarsource/polar-python/blob/master/docs/sdks/products/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/products/README.md#list) - List Products
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/products/README.md#create) - Create Product
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/products/README.md#get) - Get Product
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/products/README.md#update) - Update Product
* [update_benefits](https://github.com/polarsource/polar-python/blob/master/docs/sdks/products/README.md#update_benefits) - Update Product Benefits

### [repositories](https://github.com/polarsource/polar-python/blob/master/docs/sdks/repositories/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/repositories/README.md#list) - List Repositories
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/repositories/README.md#get) - Get Repository
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/repositories/README.md#update) - Update Repository

### [subscriptions](https://github.com/polarsource/polar-python/blob/master/docs/sdks/subscriptions/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/subscriptions/README.md#list) - List Subscriptions
* [export](https://github.com/polarsource/polar-python/blob/master/docs/sdks/subscriptions/README.md#export) - Export Subscriptions

### [users](https://github.com/polarsource/polar-python/blob/master/docs/sdks/users/README.md)


#### [users.advertisements](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polaradvertisements/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polaradvertisements/README.md#list) - List Advertisements
* [create](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polaradvertisements/README.md#create) - Create Advertisement
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polaradvertisements/README.md#get) - Get Advertisement
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polaradvertisements/README.md#update) - Update Advertisement
* [delete](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polaradvertisements/README.md#delete) - Delete Advertisement
* [enable](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polaradvertisements/README.md#enable) - Enable Advertisement

#### [users.benefits](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarbenefits/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarbenefits/README.md#list) - List Benefits
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarbenefits/README.md#get) - Get Benefit

#### [users.downloadables](https://github.com/polarsource/polar-python/blob/master/docs/sdks/downloadables/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/downloadables/README.md#list) - List Downloadables
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/downloadables/README.md#get) - Get Downloadable

#### [users.license_keys](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarlicensekeys/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarlicensekeys/README.md#list) - List License Keys
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarlicensekeys/README.md#get) - Get License Key
* [validate](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarlicensekeys/README.md#validate) - Validate License Key
* [activate](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarlicensekeys/README.md#activate) - Activate License Key
* [deactivate](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarlicensekeys/README.md#deactivate) - Deactivate License Key

#### [users.orders](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarorders/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarorders/README.md#list) - List Orders
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarorders/README.md#get) - Get Order
* [invoice](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarorders/README.md#invoice) - Get Order Invoice

#### [users.subscriptions](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarsubscriptions/README.md)

* [list](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarsubscriptions/README.md#list) - List Subscriptions
* [get](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarsubscriptions/README.md#get) - Get Subscription
* [update](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarsubscriptions/README.md#update) - Update Subscription
* [cancel](https://github.com/polarsource/polar-python/blob/master/docs/sdks/polarsubscriptions/README.md#cancel) - Cancel Subscription

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from polar.utils import BackoffStrategy, RetryConfig
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.benefits.list(,
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from polar.utils import BackoffStrategy, RetryConfig
from polar_sdk import Polar

s = Polar(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.benefits.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `list_async` method may raise the following exceptions:

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

### Example

```python
from polar_sdk import Polar, models

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.users.benefits.list()

    if res is not None:
        while True:
            # handle items

            res = res.next()
            if res is None:
                break

except models.HTTPValidationError as e:
    # handle e.data: models.HTTPValidationErrorData
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `production` | `https://api.polar.sh` | None |
| `sandbox` | `https://sandbox-api.polar.sh` | None |

#### Example

```python
from polar_sdk import Polar

s = Polar(
    server="sandbox",
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.benefits.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from polar_sdk import Polar

s = Polar(
    server_url="https://api.polar.sh",
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.benefits.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from polar_sdk import Polar
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Polar(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from polar_sdk import Polar
from polar_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Polar(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type           | Scheme         |
| -------------- | -------------- | -------------- |
| `access_token` | http           | HTTP Bearer    |

To authenticate with the API the `access_token` parameter must be set when initializing the SDK client instance. For example:
```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.benefits.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from polar_sdk import Polar
import logging

logging.basicConfig(level=logging.DEBUG)
s = Polar(debug_logger=logging.getLogger("polar_sdk"))
```
<!-- End Debugging [debug] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.benefits.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```
<!-- End Pagination [pagination] -->

<!-- Start Summary [summary] -->
## Summary

Polar API: Polar HTTP and Webhooks API

Read the docs at https://docs.polar.sh/api
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](https://github.com/polarsource/polar-python/blob/master/#sdk-installation)
* [IDE Support](https://github.com/polarsource/polar-python/blob/master/#ide-support)
* [SDK Example Usage](https://github.com/polarsource/polar-python/blob/master/#sdk-example-usage)
* [Available Resources and Operations](https://github.com/polarsource/polar-python/blob/master/#available-resources-and-operations)
* [Pagination](https://github.com/polarsource/polar-python/blob/master/#pagination)
* [Retries](https://github.com/polarsource/polar-python/blob/master/#retries)
* [Error Handling](https://github.com/polarsource/polar-python/blob/master/#error-handling)
* [Server Selection](https://github.com/polarsource/polar-python/blob/master/#server-selection)
* [Custom HTTP Client](https://github.com/polarsource/polar-python/blob/master/#custom-http-client)
* [Authentication](https://github.com/polarsource/polar-python/blob/master/#authentication)
* [Debugging](https://github.com/polarsource/polar-python/blob/master/#debugging)
<!-- End Table of Contents [toc] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=polar-sdk&utm_campaign=python)
