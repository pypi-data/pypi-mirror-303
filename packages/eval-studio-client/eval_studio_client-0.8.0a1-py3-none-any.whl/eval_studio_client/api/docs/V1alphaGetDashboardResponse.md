# V1alphaGetDashboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | [**V1alphaDashboard**](V1alphaDashboard.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_get_dashboard_response import V1alphaGetDashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaGetDashboardResponse from a JSON string
v1alpha_get_dashboard_response_instance = V1alphaGetDashboardResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaGetDashboardResponse.to_json())

# convert the object into a dict
v1alpha_get_dashboard_response_dict = v1alpha_get_dashboard_response_instance.to_dict()
# create an instance of V1alphaGetDashboardResponse from a dict
v1alpha_get_dashboard_response_from_dict = V1alphaGetDashboardResponse.from_dict(v1alpha_get_dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


