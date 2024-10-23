# V1alphaEvaluatorParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Output only. Parameter name. | [optional] [readonly] 
**type** | [**V1alphaEvaluatorParamType**](V1alphaEvaluatorParamType.md) |  | [optional] 
**description** | **str** | Output only. Parameter description. | [optional] [readonly] 
**comment** | **str** | Output only. Parameter comment. | [optional] [readonly] 
**string_val** | **str** |  | [optional] 
**float_val** | **float** |  | [optional] 
**bool_val** | **bool** |  | [optional] 
**min** | **float** | Output only. Minimum value. | [optional] [readonly] 
**max** | **float** | Output only. Maximum value. | [optional] [readonly] 
**predefined** | **List[str]** | Output only. Optional. Predefined values. | [optional] [readonly] 
**tags** | **List[str]** | Output only. Optional. Tags or other identifiers of the parameter. | [optional] [readonly] 
**category** | **List[str]** | Output only. Category of the parameter. | [optional] [readonly] 

## Example

```python
from eval_studio_client.api.models.v1alpha_evaluator_parameter import V1alphaEvaluatorParameter

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaEvaluatorParameter from a JSON string
v1alpha_evaluator_parameter_instance = V1alphaEvaluatorParameter.from_json(json)
# print the JSON string representation of the object
print(V1alphaEvaluatorParameter.to_json())

# convert the object into a dict
v1alpha_evaluator_parameter_dict = v1alpha_evaluator_parameter_instance.to_dict()
# create an instance of V1alphaEvaluatorParameter from a dict
v1alpha_evaluator_parameter_from_dict = V1alphaEvaluatorParameter.from_dict(v1alpha_evaluator_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


