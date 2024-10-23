# V1alphaListModelCollectionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | [**List[V1alphaCollectionInfo]**](V1alphaCollectionInfo.md) | The list of collections. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_list_model_collections_response import V1alphaListModelCollectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaListModelCollectionsResponse from a JSON string
v1alpha_list_model_collections_response_instance = V1alphaListModelCollectionsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaListModelCollectionsResponse.to_json())

# convert the object into a dict
v1alpha_list_model_collections_response_dict = v1alpha_list_model_collections_response_instance.to_dict()
# create an instance of V1alphaListModelCollectionsResponse from a dict
v1alpha_list_model_collections_response_from_dict = V1alphaListModelCollectionsResponse.from_dict(v1alpha_list_model_collections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


