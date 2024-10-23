# V1alphaBatchDeleteModelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | The names of the Models to delete. A maximum of 1000 can be specified. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_delete_models_request import V1alphaBatchDeleteModelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchDeleteModelsRequest from a JSON string
v1alpha_batch_delete_models_request_instance = V1alphaBatchDeleteModelsRequest.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchDeleteModelsRequest.to_json())

# convert the object into a dict
v1alpha_batch_delete_models_request_dict = v1alpha_batch_delete_models_request_instance.to_dict()
# create an instance of V1alphaBatchDeleteModelsRequest from a dict
v1alpha_batch_delete_models_request_from_dict = V1alphaBatchDeleteModelsRequest.from_dict(v1alpha_batch_delete_models_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


