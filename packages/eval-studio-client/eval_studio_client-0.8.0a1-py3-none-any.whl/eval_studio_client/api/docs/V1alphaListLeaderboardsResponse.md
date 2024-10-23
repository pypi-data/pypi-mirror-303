# V1alphaListLeaderboardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaderboards** | [**List[V1alphaLeaderboard]**](V1alphaLeaderboard.md) | The list of Leaderboards. | [optional] 
**next_page_token** | **str** | A token that can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is empty/omitted, there are no subsequent pages. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_list_leaderboards_response import V1alphaListLeaderboardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaListLeaderboardsResponse from a JSON string
v1alpha_list_leaderboards_response_instance = V1alphaListLeaderboardsResponse.from_json(json)
# print the JSON string representation of the object
print(V1alphaListLeaderboardsResponse.to_json())

# convert the object into a dict
v1alpha_list_leaderboards_response_dict = v1alpha_list_leaderboards_response_instance.to_dict()
# create an instance of V1alphaListLeaderboardsResponse from a dict
v1alpha_list_leaderboards_response_from_dict = V1alphaListLeaderboardsResponse.from_dict(v1alpha_list_leaderboards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


