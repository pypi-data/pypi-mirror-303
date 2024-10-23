# V1alphaCreateDashboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | [**V1alphaDashboard**](V1alphaDashboard.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_create_dashboard_response import V1alphaCreateDashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaCreateDashboardResponse from a JSON string
v1alpha_create_dashboard_response_instance = V1alphaCreateDashboardResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaCreateDashboardResponse.to_json())

# convert the object into a dict
v1alpha_create_dashboard_response_dict = v1alpha_create_dashboard_response_instance.to_dict()
# create an instance of V1alphaCreateDashboardResponse from a dict
v1alpha_create_dashboard_response_from_dict = V1alphaCreateDashboardResponse.from_dict(v1alpha_create_dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


