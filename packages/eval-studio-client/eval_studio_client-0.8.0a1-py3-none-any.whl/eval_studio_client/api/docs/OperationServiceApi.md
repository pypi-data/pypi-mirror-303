# eval_studio_client.api.OperationServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operation_service_batch_get_operations**](OperationServiceApi.md#operation_service_batch_get_operations) | **GET** /v1alpha/operations:batchGet | 
[**operation_service_finalize_operation**](OperationServiceApi.md#operation_service_finalize_operation) | **PATCH** /v1alpha/{operation.name}:finalize | 
[**operation_service_get_operation**](OperationServiceApi.md#operation_service_get_operation) | **GET** /v1alpha/{name_5} | 
[**operation_service_list_operations**](OperationServiceApi.md#operation_service_list_operations) | **GET** /v1alpha/operations | 
[**operation_service_update_operation**](OperationServiceApi.md#operation_service_update_operation) | **PATCH** /v1alpha/{operation.name} | 


# **operation_service_batch_get_operations**
> V1alphaBatchGetOperationsResponse operation_service_batch_get_operations(names=names)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_get_operations_response import V1alphaBatchGetOperationsResponse
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
    api_instance = eval_studio_client.api.OperationServiceApi(api_client)
    names = ['names_example'] # List[str] | The names of the Operations to retrieve. A maximum of 1000 can be specified. (optional)

    try:
        api_response = api_instance.operation_service_batch_get_operations(names=names)
        print("The response of OperationServiceApi->operation_service_batch_get_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationServiceApi->operation_service_batch_get_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**List[str]**](str.md)| The names of the Operations to retrieve. A maximum of 1000 can be specified. | [optional] 

### Return type

[**V1alphaBatchGetOperationsResponse**](V1alphaBatchGetOperationsResponse.md)

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

# **operation_service_finalize_operation**
> V1alphaFinalizeOperationResponse operation_service_finalize_operation(operation_name, operation)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.required_the_operation_to_finalize import RequiredTheOperationToFinalize
from eval_studio_client.api.models.v1alpha_finalize_operation_response import V1alphaFinalizeOperationResponse
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
    api_instance = eval_studio_client.api.OperationServiceApi(api_client)
    operation_name = 'operation_name_example' # str | Output only. Name of the Operation resource. e.g.: \"operations/<UUID>\"
    operation = eval_studio_client.api.RequiredTheOperationToFinalize() # RequiredTheOperationToFinalize | Required. The Operation to finalize.  The Operation's `name` field is used to identify the Operation to finalize. Format: operations/{operation}

    try:
        api_response = api_instance.operation_service_finalize_operation(operation_name, operation)
        print("The response of OperationServiceApi->operation_service_finalize_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationServiceApi->operation_service_finalize_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_name** | **str**| Output only. Name of the Operation resource. e.g.: \&quot;operations/&lt;UUID&gt;\&quot; | 
 **operation** | [**RequiredTheOperationToFinalize**](RequiredTheOperationToFinalize.md)| Required. The Operation to finalize.  The Operation&#39;s &#x60;name&#x60; field is used to identify the Operation to finalize. Format: operations/{operation} | 

### Return type

[**V1alphaFinalizeOperationResponse**](V1alphaFinalizeOperationResponse.md)

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

# **operation_service_get_operation**
> V1alphaGetOperationResponse operation_service_get_operation(name_5)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_get_operation_response import V1alphaGetOperationResponse
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
    api_instance = eval_studio_client.api.OperationServiceApi(api_client)
    name_5 = 'name_5_example' # str | Required. The name of the Operation to retrieve.

    try:
        api_response = api_instance.operation_service_get_operation(name_5)
        print("The response of OperationServiceApi->operation_service_get_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationServiceApi->operation_service_get_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_5** | **str**| Required. The name of the Operation to retrieve. | 

### Return type

[**V1alphaGetOperationResponse**](V1alphaGetOperationResponse.md)

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

# **operation_service_list_operations**
> V1alphaListOperationsResponse operation_service_list_operations()



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_operations_response import V1alphaListOperationsResponse
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
    api_instance = eval_studio_client.api.OperationServiceApi(api_client)

    try:
        api_response = api_instance.operation_service_list_operations()
        print("The response of OperationServiceApi->operation_service_list_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationServiceApi->operation_service_list_operations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1alphaListOperationsResponse**](V1alphaListOperationsResponse.md)

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

# **operation_service_update_operation**
> V1alphaUpdateOperationResponse operation_service_update_operation(operation_name, operation)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.required_the_operation_to_update import RequiredTheOperationToUpdate
from eval_studio_client.api.models.v1alpha_update_operation_response import V1alphaUpdateOperationResponse
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
    api_instance = eval_studio_client.api.OperationServiceApi(api_client)
    operation_name = 'operation_name_example' # str | Output only. Name of the Operation resource. e.g.: \"operations/<UUID>\"
    operation = eval_studio_client.api.RequiredTheOperationToUpdate() # RequiredTheOperationToUpdate | Required. The Operation to update.  The Operation's `name` field is used to identify the Operation to update. Format: operations/{operation}

    try:
        api_response = api_instance.operation_service_update_operation(operation_name, operation)
        print("The response of OperationServiceApi->operation_service_update_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationServiceApi->operation_service_update_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_name** | **str**| Output only. Name of the Operation resource. e.g.: \&quot;operations/&lt;UUID&gt;\&quot; | 
 **operation** | [**RequiredTheOperationToUpdate**](RequiredTheOperationToUpdate.md)| Required. The Operation to update.  The Operation&#39;s &#x60;name&#x60; field is used to identify the Operation to update. Format: operations/{operation} | 

### Return type

[**V1alphaUpdateOperationResponse**](V1alphaUpdateOperationResponse.md)

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

