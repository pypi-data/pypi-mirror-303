# V1alphaListDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[V1alphaDocument]**](V1alphaDocument.md) | The list of Documents. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_list_documents_response import V1alphaListDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaListDocumentsResponse from a JSON string
v1alpha_list_documents_response_instance = V1alphaListDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaListDocumentsResponse.to_json())

# convert the object into a dict
v1alpha_list_documents_response_dict = v1alpha_list_documents_response_instance.to_dict()
# create an instance of V1alphaListDocumentsResponse from a dict
v1alpha_list_documents_response_from_dict = V1alphaListDocumentsResponse.from_dict(v1alpha_list_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


