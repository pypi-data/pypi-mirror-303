# V1alphaUpdateLeaderboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaderboard** | [**V1alphaLeaderboard**](V1alphaLeaderboard.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_update_leaderboard_response import V1alphaUpdateLeaderboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaUpdateLeaderboardResponse from a JSON string
v1alpha_update_leaderboard_response_instance = V1alphaUpdateLeaderboardResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaUpdateLeaderboardResponse.to_json())

# convert the object into a dict
v1alpha_update_leaderboard_response_dict = v1alpha_update_leaderboard_response_instance.to_dict()
# create an instance of V1alphaUpdateLeaderboardResponse from a dict
v1alpha_update_leaderboard_response_from_dict = V1alphaUpdateLeaderboardResponse.from_dict(v1alpha_update_leaderboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


