# V1alphaBatchImportTestsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[V1alphaTest]**](V1alphaTest.md) | The imported Tests. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_import_tests_response import V1alphaBatchImportTestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchImportTestsResponse from a JSON string
v1alpha_batch_import_tests_response_instance = V1alphaBatchImportTestsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchImportTestsResponse.to_json())

# convert the object into a dict
v1alpha_batch_import_tests_response_dict = v1alpha_batch_import_tests_response_instance.to_dict()
# create an instance of V1alphaBatchImportTestsResponse from a dict
v1alpha_batch_import_tests_response_from_dict = V1alphaBatchImportTestsResponse.from_dict(v1alpha_batch_import_tests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


