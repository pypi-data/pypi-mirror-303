# eval_studio_client.api.TestServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_service_batch_delete_tests**](TestServiceApi.md#test_service_batch_delete_tests) | **POST** /v1alpha/tests:batchDelete | 
[**test_service_batch_get_tests**](TestServiceApi.md#test_service_batch_get_tests) | **GET** /v1alpha/tests:batchGet | 
[**test_service_batch_import_tests**](TestServiceApi.md#test_service_batch_import_tests) | **POST** /v1alpha/tests:batchImport | 
[**test_service_create_test**](TestServiceApi.md#test_service_create_test) | **POST** /v1alpha/tests | 
[**test_service_delete_test**](TestServiceApi.md#test_service_delete_test) | **DELETE** /v1alpha/{name_6} | 
[**test_service_get_test**](TestServiceApi.md#test_service_get_test) | **GET** /v1alpha/{name_9} | 
[**test_service_list_most_recent_tests**](TestServiceApi.md#test_service_list_most_recent_tests) | **GET** /v1alpha/tests:mostRecent | 
[**test_service_list_tests**](TestServiceApi.md#test_service_list_tests) | **GET** /v1alpha/tests | 
[**test_service_perturb_test**](TestServiceApi.md#test_service_perturb_test) | **POST** /v1alpha/{name}:perturb | 
[**test_service_update_test**](TestServiceApi.md#test_service_update_test) | **PATCH** /v1alpha/{test.name} | 


# **test_service_batch_delete_tests**
> V1alphaBatchDeleteTestsResponse test_service_batch_delete_tests(body)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_delete_tests_request import V1alphaBatchDeleteTestsRequest
from eval_studio_client.api.models.v1alpha_batch_delete_tests_response import V1alphaBatchDeleteTestsResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    body = eval_studio_client.api.V1alphaBatchDeleteTestsRequest() # V1alphaBatchDeleteTestsRequest | 

    try:
        api_response = api_instance.test_service_batch_delete_tests(body)
        print("The response of TestServiceApi->test_service_batch_delete_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_batch_delete_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alphaBatchDeleteTestsRequest**](V1alphaBatchDeleteTestsRequest.md)|  | 

### Return type

[**V1alphaBatchDeleteTestsResponse**](V1alphaBatchDeleteTestsResponse.md)

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

# **test_service_batch_get_tests**
> V1alphaBatchGetTestsResponse test_service_batch_get_tests(names=names)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_get_tests_response import V1alphaBatchGetTestsResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    names = ['names_example'] # List[str] | The names of the Tests to retrieve. A maximum of 1000 can be specified. (optional)

    try:
        api_response = api_instance.test_service_batch_get_tests(names=names)
        print("The response of TestServiceApi->test_service_batch_get_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_batch_get_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**List[str]**](str.md)| The names of the Tests to retrieve. A maximum of 1000 can be specified. | [optional] 

### Return type

[**V1alphaBatchGetTestsResponse**](V1alphaBatchGetTestsResponse.md)

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

# **test_service_batch_import_tests**
> V1alphaBatchImportTestsResponse test_service_batch_import_tests(body)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_import_tests_request import V1alphaBatchImportTestsRequest
from eval_studio_client.api.models.v1alpha_batch_import_tests_response import V1alphaBatchImportTestsResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    body = eval_studio_client.api.V1alphaBatchImportTestsRequest() # V1alphaBatchImportTestsRequest | 

    try:
        api_response = api_instance.test_service_batch_import_tests(body)
        print("The response of TestServiceApi->test_service_batch_import_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_batch_import_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alphaBatchImportTestsRequest**](V1alphaBatchImportTestsRequest.md)|  | 

### Return type

[**V1alphaBatchImportTestsResponse**](V1alphaBatchImportTestsResponse.md)

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

# **test_service_create_test**
> V1alphaCreateTestResponse test_service_create_test(test)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_create_test_response import V1alphaCreateTestResponse
from eval_studio_client.api.models.v1alpha_test import V1alphaTest
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    test = eval_studio_client.api.V1alphaTest() # V1alphaTest | The Test to create.

    try:
        api_response = api_instance.test_service_create_test(test)
        print("The response of TestServiceApi->test_service_create_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_create_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test** | [**V1alphaTest**](V1alphaTest.md)| The Test to create. | 

### Return type

[**V1alphaCreateTestResponse**](V1alphaCreateTestResponse.md)

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

# **test_service_delete_test**
> V1alphaDeleteTestResponse test_service_delete_test(name_6, force=force)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_delete_test_response import V1alphaDeleteTestResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    name_6 = 'name_6_example' # str | Required. The name of the Test to delete.
    force = True # bool | If set to true, any TestCases associated with this Test will also be deleted. Otherwise, if any TestCases are associated with this Test, the request will fail. (optional)

    try:
        api_response = api_instance.test_service_delete_test(name_6, force=force)
        print("The response of TestServiceApi->test_service_delete_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_delete_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_6** | **str**| Required. The name of the Test to delete. | 
 **force** | **bool**| If set to true, any TestCases associated with this Test will also be deleted. Otherwise, if any TestCases are associated with this Test, the request will fail. | [optional] 

### Return type

[**V1alphaDeleteTestResponse**](V1alphaDeleteTestResponse.md)

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

# **test_service_get_test**
> V1alphaGetTestResponse test_service_get_test(name_9)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_get_test_response import V1alphaGetTestResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    name_9 = 'name_9_example' # str | Required. The name of the Test to retrieve.

    try:
        api_response = api_instance.test_service_get_test(name_9)
        print("The response of TestServiceApi->test_service_get_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_get_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_9** | **str**| Required. The name of the Test to retrieve. | 

### Return type

[**V1alphaGetTestResponse**](V1alphaGetTestResponse.md)

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

# **test_service_list_most_recent_tests**
> V1alphaListMostRecentTestsResponse test_service_list_most_recent_tests(limit=limit)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_most_recent_tests_response import V1alphaListMostRecentTestsResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    limit = 56 # int | Optional. The max number of the most recent Tests to retrieve. Use -1 to retrieve all. Defaults to 3. (optional)

    try:
        api_response = api_instance.test_service_list_most_recent_tests(limit=limit)
        print("The response of TestServiceApi->test_service_list_most_recent_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_list_most_recent_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. The max number of the most recent Tests to retrieve. Use -1 to retrieve all. Defaults to 3. | [optional] 

### Return type

[**V1alphaListMostRecentTestsResponse**](V1alphaListMostRecentTestsResponse.md)

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

# **test_service_list_tests**
> V1alphaListTestsResponse test_service_list_tests(order_by=order_by)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_tests_response import V1alphaListTestsResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    order_by = 'order_by_example' # str | If specified, the returned tests will be ordered by the specified field. Attempts to implement AIP-130 (https://google.aip.dev/132#ordering), although not all features are supported yet.  Supported fields: - create_time - update_time (optional)

    try:
        api_response = api_instance.test_service_list_tests(order_by=order_by)
        print("The response of TestServiceApi->test_service_list_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_list_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| If specified, the returned tests will be ordered by the specified field. Attempts to implement AIP-130 (https://google.aip.dev/132#ordering), although not all features are supported yet.  Supported fields: - create_time - update_time | [optional] 

### Return type

[**V1alphaListTestsResponse**](V1alphaListTestsResponse.md)

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

# **test_service_perturb_test**
> V1alphaPerturbTestResponse test_service_perturb_test(name, body)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.test_service_perturb_test_request import TestServicePerturbTestRequest
from eval_studio_client.api.models.v1alpha_perturb_test_response import V1alphaPerturbTestResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    name = 'name_example' # str | Required. The name of the Test to perturb.
    body = eval_studio_client.api.TestServicePerturbTestRequest() # TestServicePerturbTestRequest | 

    try:
        api_response = api_instance.test_service_perturb_test(name, body)
        print("The response of TestServiceApi->test_service_perturb_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_perturb_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. The name of the Test to perturb. | 
 **body** | [**TestServicePerturbTestRequest**](TestServicePerturbTestRequest.md)|  | 

### Return type

[**V1alphaPerturbTestResponse**](V1alphaPerturbTestResponse.md)

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

# **test_service_update_test**
> V1alphaUpdateTestResponse test_service_update_test(test_name, test)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.required_the_test_to_update import RequiredTheTestToUpdate
from eval_studio_client.api.models.v1alpha_update_test_response import V1alphaUpdateTestResponse
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
    api_instance = eval_studio_client.api.TestServiceApi(api_client)
    test_name = 'test_name_example' # str | Output only. Name of the prompt resource. e.g.: \"tests/<UUID>\"
    test = eval_studio_client.api.RequiredTheTestToUpdate() # RequiredTheTestToUpdate | Required. The Test to update.

    try:
        api_response = api_instance.test_service_update_test(test_name, test)
        print("The response of TestServiceApi->test_service_update_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestServiceApi->test_service_update_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_name** | **str**| Output only. Name of the prompt resource. e.g.: \&quot;tests/&lt;UUID&gt;\&quot; | 
 **test** | [**RequiredTheTestToUpdate**](RequiredTheTestToUpdate.md)| Required. The Test to update. | 

### Return type

[**V1alphaUpdateTestResponse**](V1alphaUpdateTestResponse.md)

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

