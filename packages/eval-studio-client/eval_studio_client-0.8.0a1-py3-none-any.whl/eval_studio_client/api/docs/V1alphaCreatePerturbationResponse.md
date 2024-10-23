# V1alphaCreatePerturbationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_suite** | **str** | Perturbated test suite in JSON format. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_create_perturbation_response import V1alphaCreatePerturbationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaCreatePerturbationResponse from a JSON string
v1alpha_create_perturbation_response_instance = V1alphaCreatePerturbationResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaCreatePerturbationResponse.to_json())

# convert the object into a dict
v1alpha_create_perturbation_response_dict = v1alpha_create_perturbation_response_instance.to_dict()
# create an instance of V1alphaCreatePerturbationResponse from a dict
v1alpha_create_perturbation_response_from_dict = V1alphaCreatePerturbationResponse.from_dict(v1alpha_create_perturbation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


