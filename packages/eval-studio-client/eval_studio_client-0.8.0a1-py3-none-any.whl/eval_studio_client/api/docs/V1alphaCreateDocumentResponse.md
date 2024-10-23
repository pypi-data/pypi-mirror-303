# V1alphaCreateDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**V1alphaDocument**](V1alphaDocument.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_create_document_response import V1alphaCreateDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaCreateDocumentResponse from a JSON string
v1alpha_create_document_response_instance = V1alphaCreateDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaCreateDocumentResponse.to_json())

# convert the object into a dict
v1alpha_create_document_response_dict = v1alpha_create_document_response_instance.to_dict()
# create an instance of V1alphaCreateDocumentResponse from a dict
v1alpha_create_document_response_from_dict = V1alphaCreateDocumentResponse.from_dict(v1alpha_create_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


