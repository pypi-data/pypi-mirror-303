# V1alphaCheckBaseModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_availability** | **bool** | The model availability check. | [optional] 
**reason** | **str** | Optional. Information on why the model isn&#39;t available. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_check_base_models_response import V1alphaCheckBaseModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaCheckBaseModelsResponse from a JSON string
v1alpha_check_base_models_response_instance = V1alphaCheckBaseModelsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaCheckBaseModelsResponse.to_json())

# convert the object into a dict
v1alpha_check_base_models_response_dict = v1alpha_check_base_models_response_instance.to_dict()
# create an instance of V1alphaCheckBaseModelsResponse from a dict
v1alpha_check_base_models_response_from_dict = V1alphaCheckBaseModelsResponse.from_dict(v1alpha_check_base_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


