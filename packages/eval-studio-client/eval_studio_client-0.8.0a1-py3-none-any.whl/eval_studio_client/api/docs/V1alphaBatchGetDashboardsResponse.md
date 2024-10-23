# V1alphaBatchGetDashboardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboards** | [**List[V1alphaDashboard]**](V1alphaDashboard.md) | The requested Dashboards. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_get_dashboards_response import V1alphaBatchGetDashboardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchGetDashboardsResponse from a JSON string
v1alpha_batch_get_dashboards_response_instance = V1alphaBatchGetDashboardsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchGetDashboardsResponse.to_json())

# convert the object into a dict
v1alpha_batch_get_dashboards_response_dict = v1alpha_batch_get_dashboards_response_instance.to_dict()
# create an instance of V1alphaBatchGetDashboardsResponse from a dict
v1alpha_batch_get_dashboards_response_from_dict = V1alphaBatchGetDashboardsResponse.from_dict(v1alpha_batch_get_dashboards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


