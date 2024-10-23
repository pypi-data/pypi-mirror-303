# eval_studio_client.api.TestClassServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_class_service_get_test_class**](TestClassServiceApi.md#test_class_service_get_test_class) | **GET** /v1alpha/{name_8} | 
[**test_class_service_list_test_classes**](TestClassServiceApi.md#test_class_service_list_test_classes) | **GET** /v1alpha/testClasses | 


# **test_class_service_get_test_class**
> V1alphaGetTestClassResponse test_class_service_get_test_class(name_8)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_get_test_class_response import V1alphaGetTestClassResponse
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
    api_instance = eval_studio_client.api.TestClassServiceApi(api_client)
    name_8 = 'name_8_example' # str | The name of the TestClass to retrieve. Format: testClasses/<UUID>

    try:
        api_response = api_instance.test_class_service_get_test_class(name_8)
        print("The response of TestClassServiceApi->test_class_service_get_test_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestClassServiceApi->test_class_service_get_test_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_8** | **str**| The name of the TestClass to retrieve. Format: testClasses/&lt;UUID&gt; | 

### Return type

[**V1alphaGetTestClassResponse**](V1alphaGetTestClassResponse.md)

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

# **test_class_service_list_test_classes**
> V1alphaListTestClassesResponse test_class_service_list_test_classes()



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_test_classes_response import V1alphaListTestClassesResponse
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
    api_instance = eval_studio_client.api.TestClassServiceApi(api_client)

    try:
        api_response = api_instance.test_class_service_list_test_classes()
        print("The response of TestClassServiceApi->test_class_service_list_test_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestClassServiceApi->test_class_service_list_test_classes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1alphaListTestClassesResponse**](V1alphaListTestClassesResponse.md)

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

