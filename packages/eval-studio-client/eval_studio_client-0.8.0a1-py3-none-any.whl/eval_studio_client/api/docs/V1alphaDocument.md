# V1alphaDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**create_time** | **datetime** | Output only. Timestamp when the Document was created. | [optional] [readonly] 
**creator** | **str** | Output only. Name of the user or service that requested creation of the Document. | [optional] [readonly] 
**update_time** | **datetime** | Output only. Optional. Timestamp when the Document was last updated. | [optional] [readonly] 
**updater** | **str** | Output only. Optional. Name of the user or service that requested update of the Document. | [optional] [readonly] 
**delete_time** | **datetime** | Output only. Optional. Set when the Document is deleted. When set Document should be considered as deleted. | [optional] [readonly] 
**deleter** | **str** | Output only. Optional. Name of the user or service that requested deletion of the Document. | [optional] [readonly] 
**display_name** | **str** | Human readable name of the Document. | [optional] 
**description** | **str** | Optional. Arbitrary description of the Document. | [optional] 
**url** | **str** | Required. Immutable. Absolute URL where the document can be downloaded. The format &#39;//eval-studio/documents/&lt;UUID&gt;&#39; is used for documents uploaded to Eval Studio. It is the responsibility of the client to convert this to a valid URL before downloading. | [optional] 

## Example

```python
from eval_studio_client.api.models.v1alpha_document import V1alphaDocument

# TODO update the JSON string below
json = "{}"
# create an instance of V1alphaDocument from a JSON string
v1alpha_document_instance = V1alphaDocument.from_json(json)
# print the JSON string representation of the object
print(V1alphaDocument.to_json())

# convert the object into a dict
v1alpha_document_dict = v1alpha_document_instance.to_dict()
# create an instance of V1alphaDocument from a dict
v1alpha_document_from_dict = V1alphaDocument.from_dict(v1alpha_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


