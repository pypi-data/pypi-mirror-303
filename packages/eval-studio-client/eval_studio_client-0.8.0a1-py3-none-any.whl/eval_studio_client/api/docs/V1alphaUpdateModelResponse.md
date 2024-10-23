# V1alphaUpdateModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**V1alphaModel**](V1alphaModel.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_update_model_response import V1alphaUpdateModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaUpdateModelResponse from a JSON string
v1alpha_update_model_response_instance = V1alphaUpdateModelResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaUpdateModelResponse.to_json())

# convert the object into a dict
v1alpha_update_model_response_dict = v1alpha_update_model_response_instance.to_dict()
# create an instance of V1alphaUpdateModelResponse from a dict
v1alpha_update_model_response_from_dict = V1alphaUpdateModelResponse.from_dict(v1alpha_update_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


