# V1alphaListMostRecentDashboardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboards** | [**List[V1alphaDashboard]**](V1alphaDashboard.md) | The list of Dashboards. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_list_most_recent_dashboards_response import V1alphaListMostRecentDashboardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaListMostRecentDashboardsResponse from a JSON string
v1alpha_list_most_recent_dashboards_response_instance = V1alphaListMostRecentDashboardsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaListMostRecentDashboardsResponse.to_json())

# convert the object into a dict
v1alpha_list_most_recent_dashboards_response_dict = v1alpha_list_most_recent_dashboards_response_instance.to_dict()
# create an instance of V1alphaListMostRecentDashboardsResponse from a dict
v1alpha_list_most_recent_dashboards_response_from_dict = V1alphaListMostRecentDashboardsResponse.from_dict(v1alpha_list_most_recent_dashboards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


