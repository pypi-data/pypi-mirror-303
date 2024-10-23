# V1alphaCreateTestCaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_case** | [**V1alphaTestCase**](V1alphaTestCase.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_create_test_case_response import V1alphaCreateTestCaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaCreateTestCaseResponse from a JSON string
v1alpha_create_test_case_response_instance = V1alphaCreateTestCaseResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaCreateTestCaseResponse.to_json())

# convert the object into a dict
v1alpha_create_test_case_response_dict = v1alpha_create_test_case_response_instance.to_dict()
# create an instance of V1alphaCreateTestCaseResponse from a dict
v1alpha_create_test_case_response_from_dict = V1alphaCreateTestCaseResponse.from_dict(v1alpha_create_test_case_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


