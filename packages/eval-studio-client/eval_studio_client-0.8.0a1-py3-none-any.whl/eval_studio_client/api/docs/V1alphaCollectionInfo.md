# V1alphaCollectionInfo

CollectionInfo represents the information about a collection in the H2OGPTE.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Required. Collection ID. | [optional] 
**display_name** | **str** | Required. Collection display name. | [optional] 
**description** | **str** | Required. Collection description. | [optional] 
**document_count** | **int** | Required.The number of documents in the collection. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_collection_info import V1alphaCollectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaCollectionInfo from a JSON string
v1alpha_collection_info_instance = V1alphaCollectionInfo.from_json(json)
# print the JSON string representation of the object
print(V1alphaCollectionInfo.to_json())

# convert the object into a dict
v1alpha_collection_info_dict = v1alpha_collection_info_instance.to_dict()
# create an instance of V1alphaCollectionInfo from a dict
v1alpha_collection_info_from_dict = V1alphaCollectionInfo.from_dict(v1alpha_collection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


