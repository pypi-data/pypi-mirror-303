# eval_studio_client.api.DashboardServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_service_batch_delete_dashboards**](DashboardServiceApi.md#dashboard_service_batch_delete_dashboards) | **POST** /v1alpha/dashboards:batchDelete | 
[**dashboard_service_batch_get_dashboards**](DashboardServiceApi.md#dashboard_service_batch_get_dashboards) | **GET** /v1alpha/dashboards:batchGet | 
[**dashboard_service_create_dashboard**](DashboardServiceApi.md#dashboard_service_create_dashboard) | **POST** /v1alpha/dashboards | 
[**dashboard_service_delete_dashboard**](DashboardServiceApi.md#dashboard_service_delete_dashboard) | **DELETE** /v1alpha/{name} | 
[**dashboard_service_get_dashboard**](DashboardServiceApi.md#dashboard_service_get_dashboard) | **GET** /v1alpha/{name} | 
[**dashboard_service_list_dashboards**](DashboardServiceApi.md#dashboard_service_list_dashboards) | **GET** /v1alpha/dashboards | 
[**dashboard_service_list_most_recent_dashboards**](DashboardServiceApi.md#dashboard_service_list_most_recent_dashboards) | **GET** /v1alpha/dashboards:mostRecent | 
[**dashboard_service_update_dashboard**](DashboardServiceApi.md#dashboard_service_update_dashboard) | **PATCH** /v1alpha/{dashboard.name} | 


# **dashboard_service_batch_delete_dashboards**
> V1alphaBatchDeleteDashboardsResponse dashboard_service_batch_delete_dashboards(body)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_delete_dashboards_request import V1alphaBatchDeleteDashboardsRequest
from eval_studio_client.api.models.v1alpha_batch_delete_dashboards_response import V1alphaBatchDeleteDashboardsResponse
from eval_studio_client.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = eval_studio_client.api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with eval_studio_client.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eval_studio_client.api.DashboardServiceApi(api_client)
    body = eval_studio_client.api.V1alphaBatchDeleteDashboardsRequest() # V1alphaBatchDeleteDashboardsRequest | 

    try:
        api_response = api_instance.dashboard_service_batch_delete_dashboards(body)
        print("The response of DashboardServiceApi->dashboard_service_batch_delete_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardServiceApi->dashboard_service_batch_delete_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alphaBatchDeleteDashboardsRequest**](V1alphaBatchDeleteDashboardsRequest.md)|  | 

### Return type

[**V1alphaBatchDeleteDashboardsResponse**](V1alphaBatchDeleteDashboardsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_batch_get_dashboards**
> V1alphaBatchGetDashboardsResponse dashboard_service_batch_get_dashboards(names=names)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_get_dashboards_response import V1alphaBatchGetDashboardsResponse
from eval_studio_client.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = eval_studio_client.api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with eval_studio_client.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eval_studio_client.api.DashboardServiceApi(api_client)
    names = ['names_example'] # List[str] | Required. The names of the Dashboards to retrieve. A maximum of 1000 can be specified. (optional)

    try:
        api_response = api_instance.dashboard_service_batch_get_dashboards(names=names)
        print("The response of DashboardServiceApi->dashboard_service_batch_get_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardServiceApi->dashboard_service_batch_get_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**List[str]**](str.md)| Required. The names of the Dashboards to retrieve. A maximum of 1000 can be specified. | [optional] 

### Return type

[**V1alphaBatchGetDashboardsResponse**](V1alphaBatchGetDashboardsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_create_dashboard**
> V1alphaCreateDashboardResponse dashboard_service_create_dashboard(dashboard)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_create_dashboard_response import V1alphaCreateDashboardResponse
from eval_studio_client.api.models.v1alpha_dashboard import V1alphaDashboard
from eval_studio_client.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = eval_studio_client.api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with eval_studio_client.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eval_studio_client.api.DashboardServiceApi(api_client)
    dashboard = eval_studio_client.api.V1alphaDashboard() # V1alphaDashboard | Required. The Dashboard to create.

    try:
        api_response = api_instance.dashboard_service_create_dashboard(dashboard)
        print("The response of DashboardServiceApi->dashboard_service_create_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardServiceApi->dashboard_service_create_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard** | [**V1alphaDashboard**](V1alphaDashboard.md)| Required. The Dashboard to create. | 

### Return type

[**V1alphaCreateDashboardResponse**](V1alphaCreateDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_delete_dashboard**
> V1alphaDeleteDashboardResponse dashboard_service_delete_dashboard(name)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_delete_dashboard_response import V1alphaDeleteDashboardResponse
from eval_studio_client.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = eval_studio_client.api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with eval_studio_client.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eval_studio_client.api.DashboardServiceApi(api_client)
    name = 'name_example' # str | Required. The name of the Dashboard to delete.

    try:
        api_response = api_instance.dashboard_service_delete_dashboard(name)
        print("The response of DashboardServiceApi->dashboard_service_delete_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardServiceApi->dashboard_service_delete_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. The name of the Dashboard to delete. | 

### Return type

[**V1alphaDeleteDashboardResponse**](V1alphaDeleteDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_get_dashboard**
> V1alphaGetDashboardResponse dashboard_service_get_dashboard(name)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_get_dashboard_response import V1alphaGetDashboardResponse
from eval_studio_client.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = eval_studio_client.api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with eval_studio_client.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eval_studio_client.api.DashboardServiceApi(api_client)
    name = 'name_example' # str | Required. The name of the Dashboard to retrieve.

    try:
        api_response = api_instance.dashboard_service_get_dashboard(name)
        print("The response of DashboardServiceApi->dashboard_service_get_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardServiceApi->dashboard_service_get_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. The name of the Dashboard to retrieve. | 

### Return type

[**V1alphaGetDashboardResponse**](V1alphaGetDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_list_dashboards**
> V1alphaListDashboardsResponse dashboard_service_list_dashboards(filter=filter)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_dashboards_response import V1alphaListDashboardsResponse
from eval_studio_client.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = eval_studio_client.api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with eval_studio_client.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eval_studio_client.api.DashboardServiceApi(api_client)
    filter = 'filter_example' # str | Optional. If specified, only dashboards matching the filter will be returned. Attempts to implement AIP-160 (https://aip.dev/160), although not all fields, operators and features are supported.  Supported fields: - models   - only ':' operator (has) is supported (no wildcards), e.g. \"models:\\\"models/<UUID>\\\"\" (optional)

    try:
        api_response = api_instance.dashboard_service_list_dashboards(filter=filter)
        print("The response of DashboardServiceApi->dashboard_service_list_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardServiceApi->dashboard_service_list_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Optional. If specified, only dashboards matching the filter will be returned. Attempts to implement AIP-160 (https://aip.dev/160), although not all fields, operators and features are supported.  Supported fields: - models   - only &#39;:&#39; operator (has) is supported (no wildcards), e.g. \&quot;models:\\\&quot;models/&lt;UUID&gt;\\\&quot;\&quot; | [optional] 

### Return type

[**V1alphaListDashboardsResponse**](V1alphaListDashboardsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_list_most_recent_dashboards**
> V1alphaListMostRecentDashboardsResponse dashboard_service_list_most_recent_dashboards(limit=limit)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_most_recent_dashboards_response import V1alphaListMostRecentDashboardsResponse
from eval_studio_client.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = eval_studio_client.api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with eval_studio_client.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eval_studio_client.api.DashboardServiceApi(api_client)
    limit = 56 # int | Optional. The max number of the most recent Dashboards to retrieve. Use -1 to retrieve all. Defaults to 3. (optional)

    try:
        api_response = api_instance.dashboard_service_list_most_recent_dashboards(limit=limit)
        print("The response of DashboardServiceApi->dashboard_service_list_most_recent_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardServiceApi->dashboard_service_list_most_recent_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. The max number of the most recent Dashboards to retrieve. Use -1 to retrieve all. Defaults to 3. | [optional] 

### Return type

[**V1alphaListMostRecentDashboardsResponse**](V1alphaListMostRecentDashboardsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_service_update_dashboard**
> V1alphaUpdateDashboardResponse dashboard_service_update_dashboard(dashboard_name, dashboard)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.required_the_dashboard_to_update import RequiredTheDashboardToUpdate
from eval_studio_client.api.models.v1alpha_update_dashboard_response import V1alphaUpdateDashboardResponse
from eval_studio_client.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = eval_studio_client.api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with eval_studio_client.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eval_studio_client.api.DashboardServiceApi(api_client)
    dashboard_name = 'dashboard_name_example' # str | Output only. Name of the Dashboard resource. e.g.: \"dashboards/<UUID>\"
    dashboard = eval_studio_client.api.RequiredTheDashboardToUpdate() # RequiredTheDashboardToUpdate | Required. The Dashboard to update.  The Dashboard's `name` field is used to identify the Dashboard to update. Format: dashboards/{dashboard}

    try:
        api_response = api_instance.dashboard_service_update_dashboard(dashboard_name, dashboard)
        print("The response of DashboardServiceApi->dashboard_service_update_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardServiceApi->dashboard_service_update_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_name** | **str**| Output only. Name of the Dashboard resource. e.g.: \&quot;dashboards/&lt;UUID&gt;\&quot; | 
 **dashboard** | [**RequiredTheDashboardToUpdate**](RequiredTheDashboardToUpdate.md)| Required. The Dashboard to update.  The Dashboard&#39;s &#x60;name&#x60; field is used to identify the Dashboard to update. Format: dashboards/{dashboard} | 

### Return type

[**V1alphaUpdateDashboardResponse**](V1alphaUpdateDashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

