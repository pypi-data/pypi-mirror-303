# V1alphaWhoAmIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** | The caller&#39;s identity. | [optional] 
**preferred_username** | **str** | The caller&#39;s preferred username. Might be empty. | [optional] 
**email** | **str** | The caller&#39;s email address. Might be empty. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_who_am_i_response import V1alphaWhoAmIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaWhoAmIResponse from a JSON string
v1alpha_who_am_i_response_instance = V1alphaWhoAmIResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaWhoAmIResponse.to_json())

# convert the object into a dict
v1alpha_who_am_i_response_dict = v1alpha_who_am_i_response_instance.to_dict()
# create an instance of V1alphaWhoAmIResponse from a dict
v1alpha_who_am_i_response_from_dict = V1alphaWhoAmIResponse.from_dict(v1alpha_who_am_i_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


