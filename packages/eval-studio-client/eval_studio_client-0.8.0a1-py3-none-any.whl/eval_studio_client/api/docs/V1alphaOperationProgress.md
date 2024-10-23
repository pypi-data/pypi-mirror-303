# V1alphaOperationProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**parent** | **str** | Parent Operation resource name. e.g.: \&quot;operations/&lt;UUID&gt;\&quot;. | [optional] 
**progress** | **float** | Output only. Progress in range [0,1]. | [optional] [readonly] 
**message** | **str** | Output only. Progress message. | [optional] [readonly] 

## Example

```python
from eval_studio_client.api.models.v1alpha_operation_progress import V1alphaOperationProgress

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaOperationProgress from a JSON string
v1alpha_operation_progress_instance = V1alphaOperationProgress.from_json(json)
# print the JSON string representation of the object
print(V1alphaOperationProgress.to_json())

# convert the object into a dict
v1alpha_operation_progress_dict = v1alpha_operation_progress_instance.to_dict()
# create an instance of V1alphaOperationProgress from a dict
v1alpha_operation_progress_from_dict = V1alphaOperationProgress.from_dict(v1alpha_operation_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


