# V1alphaGetModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**V1alphaModel**](V1alphaModel.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_get_model_response import V1alphaGetModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaGetModelResponse from a JSON string
v1alpha_get_model_response_instance = V1alphaGetModelResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaGetModelResponse.to_json())

# convert the object into a dict
v1alpha_get_model_response_dict = v1alpha_get_model_response_instance.to_dict()
# create an instance of V1alphaGetModelResponse from a dict
v1alpha_get_model_response_from_dict = V1alphaGetModelResponse.from_dict(v1alpha_get_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


