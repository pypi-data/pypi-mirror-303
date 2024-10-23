# eval_studio_client.api.PerturbatorServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perturbator_service_get_perturbator**](PerturbatorServiceApi.md#perturbator_service_get_perturbator) | **GET** /v1alpha/{name_6} | 
[**perturbator_service_list_perturbators**](PerturbatorServiceApi.md#perturbator_service_list_perturbators) | **GET** /v1alpha/perturbators | 


# **perturbator_service_get_perturbator**
> V1alphaGetPerturbatorResponse perturbator_service_get_perturbator(name_6)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_get_perturbator_response import V1alphaGetPerturbatorResponse
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
    api_instance = eval_studio_client.api.PerturbatorServiceApi(api_client)
    name_6 = 'name_6_example' # str | Required. The name of the Perturbator to retrieve.

    try:
        api_response = api_instance.perturbator_service_get_perturbator(name_6)
        print("The response of PerturbatorServiceApi->perturbator_service_get_perturbator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerturbatorServiceApi->perturbator_service_get_perturbator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_6** | **str**| Required. The name of the Perturbator to retrieve. | 

### Return type

[**V1alphaGetPerturbatorResponse**](V1alphaGetPerturbatorResponse.md)

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

# **perturbator_service_list_perturbators**
> V1alphaListPerturbatorsResponse perturbator_service_list_perturbators()



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_perturbators_response import V1alphaListPerturbatorsResponse
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
    api_instance = eval_studio_client.api.PerturbatorServiceApi(api_client)

    try:
        api_response = api_instance.perturbator_service_list_perturbators()
        print("The response of PerturbatorServiceApi->perturbator_service_list_perturbators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerturbatorServiceApi->perturbator_service_list_perturbators: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1alphaListPerturbatorsResponse**](V1alphaListPerturbatorsResponse.md)

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

