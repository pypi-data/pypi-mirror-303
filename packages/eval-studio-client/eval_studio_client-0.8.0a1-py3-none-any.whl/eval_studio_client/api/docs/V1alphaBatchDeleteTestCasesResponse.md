# V1alphaBatchDeleteTestCasesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_cases** | [**List[V1alphaTestCase]**](V1alphaTestCase.md) | The list of deleted TestCases. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_delete_test_cases_response import V1alphaBatchDeleteTestCasesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchDeleteTestCasesResponse from a JSON string
v1alpha_batch_delete_test_cases_response_instance = V1alphaBatchDeleteTestCasesResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchDeleteTestCasesResponse.to_json())

# convert the object into a dict
v1alpha_batch_delete_test_cases_response_dict = v1alpha_batch_delete_test_cases_response_instance.to_dict()
# create an instance of V1alphaBatchDeleteTestCasesResponse from a dict
v1alpha_batch_delete_test_cases_response_from_dict = V1alphaBatchDeleteTestCasesResponse.from_dict(v1alpha_batch_delete_test_cases_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


