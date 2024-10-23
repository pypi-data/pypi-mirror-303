# V1alphaFinalizeOperationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**V1alphaOperation**](V1alphaOperation.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_finalize_operation_response import V1alphaFinalizeOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaFinalizeOperationResponse from a JSON string
v1alpha_finalize_operation_response_instance = V1alphaFinalizeOperationResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaFinalizeOperationResponse.to_json())

# convert the object into a dict
v1alpha_finalize_operation_response_dict = v1alpha_finalize_operation_response_instance.to_dict()
# create an instance of V1alphaFinalizeOperationResponse from a dict
v1alpha_finalize_operation_response_from_dict = V1alphaFinalizeOperationResponse.from_dict(v1alpha_finalize_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


