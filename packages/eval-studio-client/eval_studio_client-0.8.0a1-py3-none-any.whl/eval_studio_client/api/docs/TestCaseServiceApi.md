# eval_studio_client.api.TestCaseServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_case_service_batch_delete_test_cases**](TestCaseServiceApi.md#test_case_service_batch_delete_test_cases) | **POST** /v1alpha/{parent}/testCases:batchDelete | 
[**test_case_service_create_test_case**](TestCaseServiceApi.md#test_case_service_create_test_case) | **POST** /v1alpha/{parent}/testCases | 
[**test_case_service_delete_test_case**](TestCaseServiceApi.md#test_case_service_delete_test_case) | **DELETE** /v1alpha/{name_5} | 
[**test_case_service_find_all_test_cases_by_id**](TestCaseServiceApi.md#test_case_service_find_all_test_cases_by_id) | **GET** /v1alpha/tests/-/testCases:findAllTestCasesByID | 
[**test_case_service_get_test_case**](TestCaseServiceApi.md#test_case_service_get_test_case) | **GET** /v1alpha/{name_7} | 
[**test_case_service_list_test_cases**](TestCaseServiceApi.md#test_case_service_list_test_cases) | **GET** /v1alpha/{parent}/testCases | 
[**test_case_service_update_test_case**](TestCaseServiceApi.md#test_case_service_update_test_case) | **PATCH** /v1alpha/{testCase.name} | 


# **test_case_service_batch_delete_test_cases**
> V1alphaBatchDeleteTestCasesResponse test_case_service_batch_delete_test_cases(parent, body)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.test_case_service_batch_delete_test_cases_request import TestCaseServiceBatchDeleteTestCasesRequest
from eval_studio_client.api.models.v1alpha_batch_delete_test_cases_response import V1alphaBatchDeleteTestCasesResponse
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
    api_instance = eval_studio_client.api.TestCaseServiceApi(api_client)
    parent = 'parent_example' # str | The parent Test whose TestCases will be deleted.  Format: tests/<UUID>  If this is set, the parent of all of the TestCases specified in `names` must match this field.
    body = eval_studio_client.api.TestCaseServiceBatchDeleteTestCasesRequest() # TestCaseServiceBatchDeleteTestCasesRequest | 

    try:
        api_response = api_instance.test_case_service_batch_delete_test_cases(parent, body)
        print("The response of TestCaseServiceApi->test_case_service_batch_delete_test_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseServiceApi->test_case_service_batch_delete_test_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The parent Test whose TestCases will be deleted.  Format: tests/&lt;UUID&gt;  If this is set, the parent of all of the TestCases specified in &#x60;names&#x60; must match this field. | 
 **body** | [**TestCaseServiceBatchDeleteTestCasesRequest**](TestCaseServiceBatchDeleteTestCasesRequest.md)|  | 

### Return type

[**V1alphaBatchDeleteTestCasesResponse**](V1alphaBatchDeleteTestCasesResponse.md)

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

# **test_case_service_create_test_case**
> V1alphaCreateTestCaseResponse test_case_service_create_test_case(parent, test_case)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_create_test_case_response import V1alphaCreateTestCaseResponse
from eval_studio_client.api.models.v1alpha_test_case import V1alphaTestCase
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
    api_instance = eval_studio_client.api.TestCaseServiceApi(api_client)
    parent = 'parent_example' # str | The parent Test where this TestCase will be created. Format: tests/<UUID>
    test_case = eval_studio_client.api.V1alphaTestCase() # V1alphaTestCase | The TestCase to create.

    try:
        api_response = api_instance.test_case_service_create_test_case(parent, test_case)
        print("The response of TestCaseServiceApi->test_case_service_create_test_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseServiceApi->test_case_service_create_test_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The parent Test where this TestCase will be created. Format: tests/&lt;UUID&gt; | 
 **test_case** | [**V1alphaTestCase**](V1alphaTestCase.md)| The TestCase to create. | 

### Return type

[**V1alphaCreateTestCaseResponse**](V1alphaCreateTestCaseResponse.md)

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

# **test_case_service_delete_test_case**
> V1alphaDeleteTestCaseResponse test_case_service_delete_test_case(name_5)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_delete_test_case_response import V1alphaDeleteTestCaseResponse
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
    api_instance = eval_studio_client.api.TestCaseServiceApi(api_client)
    name_5 = 'name_5_example' # str | The name of the TestCase to delete. Format: tests/<UUID>/testCases/<UUID>

    try:
        api_response = api_instance.test_case_service_delete_test_case(name_5)
        print("The response of TestCaseServiceApi->test_case_service_delete_test_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseServiceApi->test_case_service_delete_test_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_5** | **str**| The name of the TestCase to delete. Format: tests/&lt;UUID&gt;/testCases/&lt;UUID&gt; | 

### Return type

[**V1alphaDeleteTestCaseResponse**](V1alphaDeleteTestCaseResponse.md)

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

# **test_case_service_find_all_test_cases_by_id**
> V1alphaFindAllTestCasesByIDResponse test_case_service_find_all_test_cases_by_id(ids=ids)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_find_all_test_cases_by_id_response import V1alphaFindAllTestCasesByIDResponse
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
    api_instance = eval_studio_client.api.TestCaseServiceApi(api_client)
    ids = ['ids_example'] # List[str] | The list of TestCase IDs to retrieve. (optional)

    try:
        api_response = api_instance.test_case_service_find_all_test_cases_by_id(ids=ids)
        print("The response of TestCaseServiceApi->test_case_service_find_all_test_cases_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseServiceApi->test_case_service_find_all_test_cases_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| The list of TestCase IDs to retrieve. | [optional] 

### Return type

[**V1alphaFindAllTestCasesByIDResponse**](V1alphaFindAllTestCasesByIDResponse.md)

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

# **test_case_service_get_test_case**
> V1alphaGetTestCaseResponse test_case_service_get_test_case(name_7)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_get_test_case_response import V1alphaGetTestCaseResponse
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
    api_instance = eval_studio_client.api.TestCaseServiceApi(api_client)
    name_7 = 'name_7_example' # str | The name of the TestCase to retrieve. Format: tests/<UUID>/testCases/<UUID>

    try:
        api_response = api_instance.test_case_service_get_test_case(name_7)
        print("The response of TestCaseServiceApi->test_case_service_get_test_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseServiceApi->test_case_service_get_test_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_7** | **str**| The name of the TestCase to retrieve. Format: tests/&lt;UUID&gt;/testCases/&lt;UUID&gt; | 

### Return type

[**V1alphaGetTestCaseResponse**](V1alphaGetTestCaseResponse.md)

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

# **test_case_service_list_test_cases**
> V1alphaListTestCasesResponse test_case_service_list_test_cases(parent)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_test_cases_response import V1alphaListTestCasesResponse
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
    api_instance = eval_studio_client.api.TestCaseServiceApi(api_client)
    parent = 'parent_example' # str | The parent Test whose TestCases will be listed. Format: tests/<UUID>

    try:
        api_response = api_instance.test_case_service_list_test_cases(parent)
        print("The response of TestCaseServiceApi->test_case_service_list_test_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseServiceApi->test_case_service_list_test_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The parent Test whose TestCases will be listed. Format: tests/&lt;UUID&gt; | 

### Return type

[**V1alphaListTestCasesResponse**](V1alphaListTestCasesResponse.md)

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

# **test_case_service_update_test_case**
> V1alphaUpdateTestCaseResponse test_case_service_update_test_case(test_case_name, test_case)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.required_the_test_case_to_update import RequiredTheTestCaseToUpdate
from eval_studio_client.api.models.v1alpha_update_test_case_response import V1alphaUpdateTestCaseResponse
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
    api_instance = eval_studio_client.api.TestCaseServiceApi(api_client)
    test_case_name = 'test_case_name_example' # str | Output only. Name of the prompt resource. e.g.: \"tests/<UUID>/testCases/<UUID>\"
    test_case = eval_studio_client.api.RequiredTheTestCaseToUpdate() # RequiredTheTestCaseToUpdate | Required. The TestCase to update.

    try:
        api_response = api_instance.test_case_service_update_test_case(test_case_name, test_case)
        print("The response of TestCaseServiceApi->test_case_service_update_test_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestCaseServiceApi->test_case_service_update_test_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_case_name** | **str**| Output only. Name of the prompt resource. e.g.: \&quot;tests/&lt;UUID&gt;/testCases/&lt;UUID&gt;\&quot; | 
 **test_case** | [**RequiredTheTestCaseToUpdate**](RequiredTheTestCaseToUpdate.md)| Required. The TestCase to update. | 

### Return type

[**V1alphaUpdateTestCaseResponse**](V1alphaUpdateTestCaseResponse.md)

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

