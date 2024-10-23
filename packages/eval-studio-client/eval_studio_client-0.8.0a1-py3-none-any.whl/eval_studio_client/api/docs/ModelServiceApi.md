# eval_studio_client.api.ModelServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_service_batch_delete_models**](ModelServiceApi.md#model_service_batch_delete_models) | **POST** /v1alpha/models:batchDelete | 
[**model_service_batch_get_models**](ModelServiceApi.md#model_service_batch_get_models) | **GET** /v1alpha/models:batchGet | 
[**model_service_check_base_models**](ModelServiceApi.md#model_service_check_base_models) | **GET** /v1alpha/models:check_base_models | 
[**model_service_create_model**](ModelServiceApi.md#model_service_create_model) | **POST** /v1alpha/models | 
[**model_service_delete_model**](ModelServiceApi.md#model_service_delete_model) | **DELETE** /v1alpha/{name_4} | 
[**model_service_get_model**](ModelServiceApi.md#model_service_get_model) | **GET** /v1alpha/{name_4} | 
[**model_service_list_base_models**](ModelServiceApi.md#model_service_list_base_models) | **GET** /v1alpha/models:base_models | 
[**model_service_list_model_collections**](ModelServiceApi.md#model_service_list_model_collections) | **GET** /v1alpha/models:collections | 
[**model_service_list_models**](ModelServiceApi.md#model_service_list_models) | **GET** /v1alpha/models | 
[**model_service_list_most_recent_models**](ModelServiceApi.md#model_service_list_most_recent_models) | **GET** /v1alpha/models:mostRecent | 
[**model_service_update_model**](ModelServiceApi.md#model_service_update_model) | **PATCH** /v1alpha/{model.name} | 


# **model_service_batch_delete_models**
> V1alphaBatchDeleteModelsResponse model_service_batch_delete_models(body)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_delete_models_request import V1alphaBatchDeleteModelsRequest
from eval_studio_client.api.models.v1alpha_batch_delete_models_response import V1alphaBatchDeleteModelsResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    body = eval_studio_client.api.V1alphaBatchDeleteModelsRequest() # V1alphaBatchDeleteModelsRequest | 

    try:
        api_response = api_instance.model_service_batch_delete_models(body)
        print("The response of ModelServiceApi->model_service_batch_delete_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_batch_delete_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alphaBatchDeleteModelsRequest**](V1alphaBatchDeleteModelsRequest.md)|  | 

### Return type

[**V1alphaBatchDeleteModelsResponse**](V1alphaBatchDeleteModelsResponse.md)

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

# **model_service_batch_get_models**
> V1alphaBatchGetModelsResponse model_service_batch_get_models(names=names)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_get_models_response import V1alphaBatchGetModelsResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    names = ['names_example'] # List[str] | The names of the Models to retrieve. A maximum of 1000 can be specified. (optional)

    try:
        api_response = api_instance.model_service_batch_get_models(names=names)
        print("The response of ModelServiceApi->model_service_batch_get_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_batch_get_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**List[str]**](str.md)| The names of the Models to retrieve. A maximum of 1000 can be specified. | [optional] 

### Return type

[**V1alphaBatchGetModelsResponse**](V1alphaBatchGetModelsResponse.md)

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

# **model_service_check_base_models**
> V1alphaCheckBaseModelsResponse model_service_check_base_models(model=model)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_check_base_models_response import V1alphaCheckBaseModelsResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    model = 'model_example' # str | Required. The resource name of the model to list base models for. (optional)

    try:
        api_response = api_instance.model_service_check_base_models(model=model)
        print("The response of ModelServiceApi->model_service_check_base_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_check_base_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Required. The resource name of the model to list base models for. | [optional] 

### Return type

[**V1alphaCheckBaseModelsResponse**](V1alphaCheckBaseModelsResponse.md)

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

# **model_service_create_model**
> V1alphaCreateModelResponse model_service_create_model(model)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_create_model_response import V1alphaCreateModelResponse
from eval_studio_client.api.models.v1alpha_model import V1alphaModel
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    model = eval_studio_client.api.V1alphaModel() # V1alphaModel | Required. The Model to create.

    try:
        api_response = api_instance.model_service_create_model(model)
        print("The response of ModelServiceApi->model_service_create_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_create_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**V1alphaModel**](V1alphaModel.md)| Required. The Model to create. | 

### Return type

[**V1alphaCreateModelResponse**](V1alphaCreateModelResponse.md)

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

# **model_service_delete_model**
> V1alphaDeleteModelResponse model_service_delete_model(name_4)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_delete_model_response import V1alphaDeleteModelResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    name_4 = 'name_4_example' # str | Required. The name of the Model to delete.

    try:
        api_response = api_instance.model_service_delete_model(name_4)
        print("The response of ModelServiceApi->model_service_delete_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_delete_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_4** | **str**| Required. The name of the Model to delete. | 

### Return type

[**V1alphaDeleteModelResponse**](V1alphaDeleteModelResponse.md)

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

# **model_service_get_model**
> V1alphaGetModelResponse model_service_get_model(name_4)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_get_model_response import V1alphaGetModelResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    name_4 = 'name_4_example' # str | Required. The name of the Model to retrieve.

    try:
        api_response = api_instance.model_service_get_model(name_4)
        print("The response of ModelServiceApi->model_service_get_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_get_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_4** | **str**| Required. The name of the Model to retrieve. | 

### Return type

[**V1alphaGetModelResponse**](V1alphaGetModelResponse.md)

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

# **model_service_list_base_models**
> V1alphaListBaseModelsResponse model_service_list_base_models(model=model)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_base_models_response import V1alphaListBaseModelsResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    model = 'model_example' # str | Required. The resource name of the model to list base models for. (optional)

    try:
        api_response = api_instance.model_service_list_base_models(model=model)
        print("The response of ModelServiceApi->model_service_list_base_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_list_base_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Required. The resource name of the model to list base models for. | [optional] 

### Return type

[**V1alphaListBaseModelsResponse**](V1alphaListBaseModelsResponse.md)

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

# **model_service_list_model_collections**
> V1alphaListModelCollectionsResponse model_service_list_model_collections(model=model)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_model_collections_response import V1alphaListModelCollectionsResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    model = 'model_example' # str | Required. The resource name of the model to list collections for. (optional)

    try:
        api_response = api_instance.model_service_list_model_collections(model=model)
        print("The response of ModelServiceApi->model_service_list_model_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_list_model_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Required. The resource name of the model to list collections for. | [optional] 

### Return type

[**V1alphaListModelCollectionsResponse**](V1alphaListModelCollectionsResponse.md)

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

# **model_service_list_models**
> V1alphaListModelsResponse model_service_list_models(order_by=order_by)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_models_response import V1alphaListModelsResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    order_by = 'order_by_example' # str | If specified, the returned models will be ordered by the specified field. Attempts to implement AIP-130 (https://google.aip.dev/132#ordering), although not all features are supported yet.  Supported fields: - create_time - update_time (optional)

    try:
        api_response = api_instance.model_service_list_models(order_by=order_by)
        print("The response of ModelServiceApi->model_service_list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_list_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| If specified, the returned models will be ordered by the specified field. Attempts to implement AIP-130 (https://google.aip.dev/132#ordering), although not all features are supported yet.  Supported fields: - create_time - update_time | [optional] 

### Return type

[**V1alphaListModelsResponse**](V1alphaListModelsResponse.md)

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

# **model_service_list_most_recent_models**
> V1alphaListMostRecentModelsResponse model_service_list_most_recent_models(limit=limit)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_most_recent_models_response import V1alphaListMostRecentModelsResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    limit = 56 # int | Optional. The max number of the most recent Models to retrieve. Use -1 to retrieve all. Defaults to 3. (optional)

    try:
        api_response = api_instance.model_service_list_most_recent_models(limit=limit)
        print("The response of ModelServiceApi->model_service_list_most_recent_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_list_most_recent_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. The max number of the most recent Models to retrieve. Use -1 to retrieve all. Defaults to 3. | [optional] 

### Return type

[**V1alphaListMostRecentModelsResponse**](V1alphaListMostRecentModelsResponse.md)

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

# **model_service_update_model**
> V1alphaUpdateModelResponse model_service_update_model(model_name, model)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.required_the_model_to_update import RequiredTheModelToUpdate
from eval_studio_client.api.models.v1alpha_update_model_response import V1alphaUpdateModelResponse
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
    api_instance = eval_studio_client.api.ModelServiceApi(api_client)
    model_name = 'model_name_example' # str | Output only. Name of the Model resource. e.g.: \"models/<UUID>\"
    model = eval_studio_client.api.RequiredTheModelToUpdate() # RequiredTheModelToUpdate | Required. The Model to update.

    try:
        api_response = api_instance.model_service_update_model(model_name, model)
        print("The response of ModelServiceApi->model_service_update_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelServiceApi->model_service_update_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Output only. Name of the Model resource. e.g.: \&quot;models/&lt;UUID&gt;\&quot; | 
 **model** | [**RequiredTheModelToUpdate**](RequiredTheModelToUpdate.md)| Required. The Model to update. | 

### Return type

[**V1alphaUpdateModelResponse**](V1alphaUpdateModelResponse.md)

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

