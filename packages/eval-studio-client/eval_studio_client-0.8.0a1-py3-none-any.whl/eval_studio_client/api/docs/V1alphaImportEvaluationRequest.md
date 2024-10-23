# V1alphaImportEvaluationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluator_identifiers** | **List[str]** | Required. Evaluator identifiers to use, not the resource names. | [optional] 
**model** | [**V1alphaModel**](V1alphaModel.md) |  | [optional] 
**test_lab** | **str** | Required. The JSON representation of the pre-built test-lab. | [optional] 
**operation** | **str** | Required. Resource name of the long-running operation. | [optional] 
**evaluators_parameters** | **Dict[str, str]** | Optional. Additional evaluators configuration, for all the evaluators used in the evaluation. Key is the evaluator identifier, and the value is a JSON string containing the configuration dictionary. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_import_evaluation_request import V1alphaImportEvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaImportEvaluationRequest from a JSON string
v1alpha_import_evaluation_request_instance = V1alphaImportEvaluationRequest.from_json(json)
# print the JSON string representation of the object
print(V1alphaImportEvaluationRequest.to_json())

# convert the object into a dict
v1alpha_import_evaluation_request_dict = v1alpha_import_evaluation_request_instance.to_dict()
# create an instance of V1alphaImportEvaluationRequest from a dict
v1alpha_import_evaluation_request_from_dict = V1alphaImportEvaluationRequest.from_dict(v1alpha_import_evaluation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


