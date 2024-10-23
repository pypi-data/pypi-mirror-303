# V1alphaGetInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**V1alphaInfo**](V1alphaInfo.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_get_info_response import V1alphaGetInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaGetInfoResponse from a JSON string
v1alpha_get_info_response_instance = V1alphaGetInfoResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaGetInfoResponse.to_json())

# convert the object into a dict
v1alpha_get_info_response_dict = v1alpha_get_info_response_instance.to_dict()
# create an instance of V1alphaGetInfoResponse from a dict
v1alpha_get_info_response_from_dict = V1alphaGetInfoResponse.from_dict(v1alpha_get_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


