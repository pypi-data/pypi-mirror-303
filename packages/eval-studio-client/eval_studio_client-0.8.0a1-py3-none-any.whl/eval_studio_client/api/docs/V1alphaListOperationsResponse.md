# V1alphaListOperationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[V1alphaOperation]**](V1alphaOperation.md) | The list of Operations. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_list_operations_response import V1alphaListOperationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaListOperationsResponse from a JSON string
v1alpha_list_operations_response_instance = V1alphaListOperationsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaListOperationsResponse.to_json())

# convert the object into a dict
v1alpha_list_operations_response_dict = v1alpha_list_operations_response_instance.to_dict()
# create an instance of V1alphaListOperationsResponse from a dict
v1alpha_list_operations_response_from_dict = V1alphaListOperationsResponse.from_dict(v1alpha_list_operations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


