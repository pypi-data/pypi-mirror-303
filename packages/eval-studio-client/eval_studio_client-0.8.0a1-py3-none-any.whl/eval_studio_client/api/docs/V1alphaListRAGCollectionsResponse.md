# V1alphaListRAGCollectionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | [**List[V1alphaCollectionInfo]**](V1alphaCollectionInfo.md) | Required. List of RAG collections available for evaluation. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_list_rag_collections_response import V1alphaListRAGCollectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaListRAGCollectionsResponse from a JSON string
v1alpha_list_rag_collections_response_instance = V1alphaListRAGCollectionsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaListRAGCollectionsResponse.to_json())

# convert the object into a dict
v1alpha_list_rag_collections_response_dict = v1alpha_list_rag_collections_response_instance.to_dict()
# create an instance of V1alphaListRAGCollectionsResponse from a dict
v1alpha_list_rag_collections_response_from_dict = V1alphaListRAGCollectionsResponse.from_dict(v1alpha_list_rag_collections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


