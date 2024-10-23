# V1alphaBatchGetDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[V1alphaDocument]**](V1alphaDocument.md) | The Documents that were requested. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_get_documents_response import V1alphaBatchGetDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchGetDocumentsResponse from a JSON string
v1alpha_batch_get_documents_response_instance = V1alphaBatchGetDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchGetDocumentsResponse.to_json())

# convert the object into a dict
v1alpha_batch_get_documents_response_dict = v1alpha_batch_get_documents_response_instance.to_dict()
# create an instance of V1alphaBatchGetDocumentsResponse from a dict
v1alpha_batch_get_documents_response_from_dict = V1alphaBatchGetDocumentsResponse.from_dict(v1alpha_batch_get_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


