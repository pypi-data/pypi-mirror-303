# V1alphaBatchDeleteModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[V1alphaModel]**](V1alphaModel.md) | The Models that were deleted. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_delete_models_response import V1alphaBatchDeleteModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchDeleteModelsResponse from a JSON string
v1alpha_batch_delete_models_response_instance = V1alphaBatchDeleteModelsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchDeleteModelsResponse.to_json())

# convert the object into a dict
v1alpha_batch_delete_models_response_dict = v1alpha_batch_delete_models_response_instance.to_dict()
# create an instance of V1alphaBatchDeleteModelsResponse from a dict
v1alpha_batch_delete_models_response_from_dict = V1alphaBatchDeleteModelsResponse.from_dict(v1alpha_batch_delete_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


