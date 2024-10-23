# V1alphaBatchDeleteLeaderboardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaderboards** | [**List[V1alphaLeaderboard]**](V1alphaLeaderboard.md) | The deleted Leaderboards. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_batch_delete_leaderboards_response import V1alphaBatchDeleteLeaderboardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaBatchDeleteLeaderboardsResponse from a JSON string
v1alpha_batch_delete_leaderboards_response_instance = V1alphaBatchDeleteLeaderboardsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaBatchDeleteLeaderboardsResponse.to_json())

# convert the object into a dict
v1alpha_batch_delete_leaderboards_response_dict = v1alpha_batch_delete_leaderboards_response_instance.to_dict()
# create an instance of V1alphaBatchDeleteLeaderboardsResponse from a dict
v1alpha_batch_delete_leaderboards_response_from_dict = V1alphaBatchDeleteLeaderboardsResponse.from_dict(v1alpha_batch_delete_leaderboards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


