# V1alphaCreateLeaderboardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaderboard** | [**V1alphaLeaderboard**](V1alphaLeaderboard.md) |  | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_create_leaderboard_request import V1alphaCreateLeaderboardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaCreateLeaderboardRequest from a JSON string
v1alpha_create_leaderboard_request_instance = V1alphaCreateLeaderboardRequest.from_json(json)
# print the JSON string representation of the object
print(V1alphaCreateLeaderboardRequest.to_json())

# convert the object into a dict
v1alpha_create_leaderboard_request_dict = v1alpha_create_leaderboard_request_instance.to_dict()
# create an instance of V1alphaCreateLeaderboardRequest from a dict
v1alpha_create_leaderboard_request_from_dict = V1alphaCreateLeaderboardRequest.from_dict(v1alpha_create_leaderboard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


