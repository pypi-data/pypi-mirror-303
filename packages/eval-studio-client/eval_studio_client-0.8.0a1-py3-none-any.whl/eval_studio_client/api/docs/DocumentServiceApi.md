# eval_studio_client.api.DocumentServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_service_batch_delete_documents**](DocumentServiceApi.md#document_service_batch_delete_documents) | **POST** /v1alpha/documents:batchDelete | 
[**document_service_batch_get_documents**](DocumentServiceApi.md#document_service_batch_get_documents) | **GET** /v1alpha/documents:batchGet | 
[**document_service_create_document**](DocumentServiceApi.md#document_service_create_document) | **POST** /v1alpha/documents | 
[**document_service_delete_document**](DocumentServiceApi.md#document_service_delete_document) | **DELETE** /v1alpha/{name_1} | 
[**document_service_get_document**](DocumentServiceApi.md#document_service_get_document) | **GET** /v1alpha/{name_1} | 
[**document_service_list_documents**](DocumentServiceApi.md#document_service_list_documents) | **GET** /v1alpha/documents | 
[**document_service_update_document**](DocumentServiceApi.md#document_service_update_document) | **PATCH** /v1alpha/{document.name} | 


# **document_service_batch_delete_documents**
> V1alphaBatchDeleteDocumentsResponse document_service_batch_delete_documents(body)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_delete_documents_request import V1alphaBatchDeleteDocumentsRequest
from eval_studio_client.api.models.v1alpha_batch_delete_documents_response import V1alphaBatchDeleteDocumentsResponse
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
    api_instance = eval_studio_client.api.DocumentServiceApi(api_client)
    body = eval_studio_client.api.V1alphaBatchDeleteDocumentsRequest() # V1alphaBatchDeleteDocumentsRequest | 

    try:
        api_response = api_instance.document_service_batch_delete_documents(body)
        print("The response of DocumentServiceApi->document_service_batch_delete_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentServiceApi->document_service_batch_delete_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alphaBatchDeleteDocumentsRequest**](V1alphaBatchDeleteDocumentsRequest.md)|  | 

### Return type

[**V1alphaBatchDeleteDocumentsResponse**](V1alphaBatchDeleteDocumentsResponse.md)

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

# **document_service_batch_get_documents**
> V1alphaBatchGetDocumentsResponse document_service_batch_get_documents(names=names)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_batch_get_documents_response import V1alphaBatchGetDocumentsResponse
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
    api_instance = eval_studio_client.api.DocumentServiceApi(api_client)
    names = ['names_example'] # List[str] | The names of the Documents to retrieve. A maximum of 1000 can be specified. (optional)

    try:
        api_response = api_instance.document_service_batch_get_documents(names=names)
        print("The response of DocumentServiceApi->document_service_batch_get_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentServiceApi->document_service_batch_get_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**List[str]**](str.md)| The names of the Documents to retrieve. A maximum of 1000 can be specified. | [optional] 

### Return type

[**V1alphaBatchGetDocumentsResponse**](V1alphaBatchGetDocumentsResponse.md)

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

# **document_service_create_document**
> V1alphaCreateDocumentResponse document_service_create_document(document)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_create_document_response import V1alphaCreateDocumentResponse
from eval_studio_client.api.models.v1alpha_document import V1alphaDocument
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
    api_instance = eval_studio_client.api.DocumentServiceApi(api_client)
    document = eval_studio_client.api.V1alphaDocument() # V1alphaDocument | Required. The Document to create.

    try:
        api_response = api_instance.document_service_create_document(document)
        print("The response of DocumentServiceApi->document_service_create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentServiceApi->document_service_create_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | [**V1alphaDocument**](V1alphaDocument.md)| Required. The Document to create. | 

### Return type

[**V1alphaCreateDocumentResponse**](V1alphaCreateDocumentResponse.md)

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

# **document_service_delete_document**
> V1alphaDeleteDocumentResponse document_service_delete_document(name_1)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_delete_document_response import V1alphaDeleteDocumentResponse
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
    api_instance = eval_studio_client.api.DocumentServiceApi(api_client)
    name_1 = 'name_1_example' # str | Required. The name of the Document to delete.

    try:
        api_response = api_instance.document_service_delete_document(name_1)
        print("The response of DocumentServiceApi->document_service_delete_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentServiceApi->document_service_delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_1** | **str**| Required. The name of the Document to delete. | 

### Return type

[**V1alphaDeleteDocumentResponse**](V1alphaDeleteDocumentResponse.md)

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

# **document_service_get_document**
> V1alphaGetDocumentResponse document_service_get_document(name_1)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_get_document_response import V1alphaGetDocumentResponse
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
    api_instance = eval_studio_client.api.DocumentServiceApi(api_client)
    name_1 = 'name_1_example' # str | Required. The name of the Document to retrieve.

    try:
        api_response = api_instance.document_service_get_document(name_1)
        print("The response of DocumentServiceApi->document_service_get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentServiceApi->document_service_get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_1** | **str**| Required. The name of the Document to retrieve. | 

### Return type

[**V1alphaGetDocumentResponse**](V1alphaGetDocumentResponse.md)

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

# **document_service_list_documents**
> V1alphaListDocumentsResponse document_service_list_documents()



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.v1alpha_list_documents_response import V1alphaListDocumentsResponse
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
    api_instance = eval_studio_client.api.DocumentServiceApi(api_client)

    try:
        api_response = api_instance.document_service_list_documents()
        print("The response of DocumentServiceApi->document_service_list_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentServiceApi->document_service_list_documents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1alphaListDocumentsResponse**](V1alphaListDocumentsResponse.md)

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

# **document_service_update_document**
> V1alphaUpdateDocumentResponse document_service_update_document(document_name, document)



### Example


```python
import eval_studio_client.api
from eval_studio_client.api.models.required_the_document_to_update import RequiredTheDocumentToUpdate
from eval_studio_client.api.models.v1alpha_update_document_response import V1alphaUpdateDocumentResponse
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
    api_instance = eval_studio_client.api.DocumentServiceApi(api_client)
    document_name = 'document_name_example' # str | Output only. Name of the Document resource. e.g.: \"documents/<UUID>\"
    document = eval_studio_client.api.RequiredTheDocumentToUpdate() # RequiredTheDocumentToUpdate | Required. The Document to update.  The Document's name field is used to identify the Document to be updated. Format: documents/{document}

    try:
        api_response = api_instance.document_service_update_document(document_name, document)
        print("The response of DocumentServiceApi->document_service_update_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentServiceApi->document_service_update_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_name** | **str**| Output only. Name of the Document resource. e.g.: \&quot;documents/&lt;UUID&gt;\&quot; | 
 **document** | [**RequiredTheDocumentToUpdate**](RequiredTheDocumentToUpdate.md)| Required. The Document to update.  The Document&#39;s name field is used to identify the Document to be updated. Format: documents/{document} | 

### Return type

[**V1alphaUpdateDocumentResponse**](V1alphaUpdateDocumentResponse.md)

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

