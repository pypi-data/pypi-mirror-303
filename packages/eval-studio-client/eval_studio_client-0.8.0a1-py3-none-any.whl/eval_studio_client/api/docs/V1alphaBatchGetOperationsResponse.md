# V1alphaBatchGetOperationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[V1alphaOperation]**](V1alphaOperation.md) | The Operations that were requested. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_get_operations_response import V1alphaBatchGetOperationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchGetOperationsResponse from a JSON string
v1alpha_batch_get_operations_response_instance = V1alphaBatchGetOperationsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchGetOperationsResponse.to_json())

# convert the object into a dict
v1alpha_batch_get_operations_response_dict = v1alpha_batch_get_operations_response_instance.to_dict()
# create an instance of V1alphaBatchGetOperationsResponse from a dict
v1alpha_batch_get_operations_response_from_dict = V1alphaBatchGetOperationsResponse.from_dict(v1alpha_batch_get_operations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


