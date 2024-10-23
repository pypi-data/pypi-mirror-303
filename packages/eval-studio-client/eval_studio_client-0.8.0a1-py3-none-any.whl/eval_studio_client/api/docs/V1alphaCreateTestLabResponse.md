# V1alphaCreateTestLabResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_lab** | [**V1alphaTestLab**](V1alphaTestLab.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_create_test_lab_response import V1alphaCreateTestLabResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaCreateTestLabResponse from a JSON string
v1alpha_create_test_lab_response_instance = V1alphaCreateTestLabResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaCreateTestLabResponse.to_json())

# convert the object into a dict
v1alpha_create_test_lab_response_dict = v1alpha_create_test_lab_response_instance.to_dict()
# create an instance of V1alphaCreateTestLabResponse from a dict
v1alpha_create_test_lab_response_from_dict = V1alphaCreateTestLabResponse.from_dict(v1alpha_create_test_lab_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


