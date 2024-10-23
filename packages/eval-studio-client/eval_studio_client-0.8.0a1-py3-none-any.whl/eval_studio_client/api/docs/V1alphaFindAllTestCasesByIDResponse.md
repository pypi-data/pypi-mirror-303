# V1alphaFindAllTestCasesByIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_cases** | [**List[V1alphaTestCase]**](V1alphaTestCase.md) | The list of TestCases. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_find_all_test_cases_by_id_response import V1alphaFindAllTestCasesByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaFindAllTestCasesByIDResponse from a JSON string
v1alpha_find_all_test_cases_by_id_response_instance = V1alphaFindAllTestCasesByIDResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaFindAllTestCasesByIDResponse.to_json())

# convert the object into a dict
v1alpha_find_all_test_cases_by_id_response_dict = v1alpha_find_all_test_cases_by_id_response_instance.to_dict()
# create an instance of V1alphaFindAllTestCasesByIDResponse from a dict
v1alpha_find_all_test_cases_by_id_response_from_dict = V1alphaFindAllTestCasesByIDResponse.from_dict(v1alpha_find_all_test_cases_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


