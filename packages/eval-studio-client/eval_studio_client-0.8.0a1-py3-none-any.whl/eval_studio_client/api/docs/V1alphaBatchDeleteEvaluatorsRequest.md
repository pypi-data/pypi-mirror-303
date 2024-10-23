# V1alphaBatchDeleteEvaluatorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Required. The names of the Evaluators to delete. A maximum of 1000 can be specified. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_delete_evaluators_request import V1alphaBatchDeleteEvaluatorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchDeleteEvaluatorsRequest from a JSON string
v1alpha_batch_delete_evaluators_request_instance = V1alphaBatchDeleteEvaluatorsRequest.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchDeleteEvaluatorsRequest.to_json())

# convert the object into a dict
v1alpha_batch_delete_evaluators_request_dict = v1alpha_batch_delete_evaluators_request_instance.to_dict()
# create an instance of V1alphaBatchDeleteEvaluatorsRequest from a dict
v1alpha_batch_delete_evaluators_request_from_dict = V1alphaBatchDeleteEvaluatorsRequest.from_dict(v1alpha_batch_delete_evaluators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


