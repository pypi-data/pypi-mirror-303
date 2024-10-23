# V1alphaBatchDeleteDocumentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Required. The names of the Documents to delete. A maximum of 1000 can be specified. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_delete_documents_request import V1alphaBatchDeleteDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchDeleteDocumentsRequest from a JSON string
v1alpha_batch_delete_documents_request_instance = V1alphaBatchDeleteDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchDeleteDocumentsRequest.to_json())

# convert the object into a dict
v1alpha_batch_delete_documents_request_dict = v1alpha_batch_delete_documents_request_instance.to_dict()
# create an instance of V1alphaBatchDeleteDocumentsRequest from a dict
v1alpha_batch_delete_documents_request_from_dict = V1alphaBatchDeleteDocumentsRequest.from_dict(v1alpha_batch_delete_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


