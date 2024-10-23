# V1alphaGetEvaluatorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluator** | [**V1alphaEvaluator**](V1alphaEvaluator.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_get_evaluator_response import V1alphaGetEvaluatorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaGetEvaluatorResponse from a JSON string
v1alpha_get_evaluator_response_instance = V1alphaGetEvaluatorResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaGetEvaluatorResponse.to_json())

# convert the object into a dict
v1alpha_get_evaluator_response_dict = v1alpha_get_evaluator_response_instance.to_dict()
# create an instance of V1alphaGetEvaluatorResponse from a dict
v1alpha_get_evaluator_response_from_dict = V1alphaGetEvaluatorResponse.from_dict(v1alpha_get_evaluator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


