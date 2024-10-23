# V1alphaBatchDeleteLeaderboardsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Required. The names of the Leaderboards to delete. A maximum of 1000 can be specified. | [optional] 
**view** | [**V1alphaLeaderboardView**](V1alphaLeaderboardView.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_delete_leaderboards_request import V1alphaBatchDeleteLeaderboardsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchDeleteLeaderboardsRequest from a JSON string
v1alpha_batch_delete_leaderboards_request_instance = V1alphaBatchDeleteLeaderboardsRequest.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchDeleteLeaderboardsRequest.to_json())

# convert the object into a dict
v1alpha_batch_delete_leaderboards_request_dict = v1alpha_batch_delete_leaderboards_request_instance.to_dict()
# create an instance of V1alphaBatchDeleteLeaderboardsRequest from a dict
v1alpha_batch_delete_leaderboards_request_from_dict = V1alphaBatchDeleteLeaderboardsRequest.from_dict(v1alpha_batch_delete_leaderboards_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


