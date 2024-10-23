# V1alphaBatchDeleteDashboardsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Required. The names of the Dashboards to delete. A maximum of 1000 can be specified. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_delete_dashboards_request import V1alphaBatchDeleteDashboardsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchDeleteDashboardsRequest from a JSON string
v1alpha_batch_delete_dashboards_request_instance = V1alphaBatchDeleteDashboardsRequest.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchDeleteDashboardsRequest.to_json())

# convert the object into a dict
v1alpha_batch_delete_dashboards_request_dict = v1alpha_batch_delete_dashboards_request_instance.to_dict()
# create an instance of V1alphaBatchDeleteDashboardsRequest from a dict
v1alpha_batch_delete_dashboards_request_from_dict = V1alphaBatchDeleteDashboardsRequest.from_dict(v1alpha_batch_delete_dashboards_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


