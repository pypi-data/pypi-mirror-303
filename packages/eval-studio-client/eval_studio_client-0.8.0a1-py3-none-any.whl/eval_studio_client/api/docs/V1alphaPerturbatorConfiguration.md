# V1alphaPerturbatorConfiguration

PerturbatorConfiguration represents the configuration of a perturbator to use during the perturbation process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**intensity** | [**V1alphaPerturbatorIntensity**](V1alphaPerturbatorIntensity.md) |  | [optional] 
**params** | **str** | Optional. The parameters to pass to the perturbator. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_perturbator_configuration import V1alphaPerturbatorConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaPerturbatorConfiguration from a JSON string
v1alpha_perturbator_configuration_instance = V1alphaPerturbatorConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1alphaPerturbatorConfiguration.to_json())

# convert the object into a dict
v1alpha_perturbator_configuration_dict = v1alpha_perturbator_configuration_instance.to_dict()
# create an instance of V1alphaPerturbatorConfiguration from a dict
v1alpha_perturbator_configuration_from_dict = V1alphaPerturbatorConfiguration.from_dict(v1alpha_perturbator_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


