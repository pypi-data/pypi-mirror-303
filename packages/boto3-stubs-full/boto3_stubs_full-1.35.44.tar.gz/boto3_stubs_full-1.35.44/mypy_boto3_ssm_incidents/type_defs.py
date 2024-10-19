"""
Type annotations for ssm-incidents service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/type_defs/)

Usage::

    ```python
    from mypy_boto3_ssm_incidents.type_defs import AddRegionActionTypeDef

    data: AddRegionActionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    IncidentRecordStatusType,
    ItemTypeType,
    RegionStatusType,
    ReplicationSetStatusType,
    SortOrderType,
    SsmTargetAccountType,
    VariableTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AddRegionActionTypeDef",
    "AttributeValueListTypeDef",
    "AutomationExecutionTypeDef",
    "BatchGetIncidentFindingsErrorTypeDef",
    "BatchGetIncidentFindingsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ChatChannelOutputTypeDef",
    "ChatChannelTypeDef",
    "CloudFormationStackUpdateTypeDef",
    "CodeDeployDeploymentTypeDef",
    "TimestampTypeDef",
    "RegionMapInputValueTypeDef",
    "EventReferenceTypeDef",
    "DeleteIncidentRecordInputRequestTypeDef",
    "DeleteRegionActionTypeDef",
    "DeleteReplicationSetInputRequestTypeDef",
    "DeleteResourcePolicyInputRequestTypeDef",
    "DeleteResponsePlanInputRequestTypeDef",
    "DeleteTimelineEventInputRequestTypeDef",
    "DynamicSsmParameterValueTypeDef",
    "FindingSummaryTypeDef",
    "GetIncidentRecordInputRequestTypeDef",
    "GetReplicationSetInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "PaginatorConfigTypeDef",
    "GetResourcePoliciesInputRequestTypeDef",
    "ResourcePolicyTypeDef",
    "GetResponsePlanInputRequestTypeDef",
    "GetTimelineEventInputRequestTypeDef",
    "IncidentRecordSourceTypeDef",
    "NotificationTargetItemTypeDef",
    "PagerDutyIncidentDetailTypeDef",
    "ListIncidentFindingsInputRequestTypeDef",
    "ListRelatedItemsInputRequestTypeDef",
    "ListReplicationSetsInputRequestTypeDef",
    "ListResponsePlansInputRequestTypeDef",
    "ResponsePlanSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PagerDutyIncidentConfigurationTypeDef",
    "PutResourcePolicyInputRequestTypeDef",
    "RegionInfoTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeletionProtectionInputRequestTypeDef",
    "CreateReplicationSetOutputTypeDef",
    "CreateResponsePlanOutputTypeDef",
    "CreateTimelineEventOutputTypeDef",
    "ListReplicationSetsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "StartIncidentOutputTypeDef",
    "FindingDetailsTypeDef",
    "ConditionTypeDef",
    "TriggerDetailsTypeDef",
    "CreateReplicationSetInputRequestTypeDef",
    "CreateTimelineEventInputRequestTypeDef",
    "EventSummaryTypeDef",
    "TimelineEventTypeDef",
    "UpdateTimelineEventInputRequestTypeDef",
    "UpdateReplicationSetActionTypeDef",
    "SsmAutomationOutputTypeDef",
    "SsmAutomationTypeDef",
    "ListIncidentFindingsOutputTypeDef",
    "GetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef",
    "GetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef",
    "GetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef",
    "ListIncidentFindingsInputListIncidentFindingsPaginateTypeDef",
    "ListRelatedItemsInputListRelatedItemsPaginateTypeDef",
    "ListReplicationSetsInputListReplicationSetsPaginateTypeDef",
    "ListResponsePlansInputListResponsePlansPaginateTypeDef",
    "GetResourcePoliciesOutputTypeDef",
    "IncidentRecordSummaryTypeDef",
    "IncidentRecordTypeDef",
    "IncidentTemplateOutputTypeDef",
    "IncidentTemplateTypeDef",
    "UpdateIncidentRecordInputRequestTypeDef",
    "ItemValueTypeDef",
    "ListResponsePlansOutputTypeDef",
    "PagerDutyConfigurationTypeDef",
    "ReplicationSetTypeDef",
    "FindingTypeDef",
    "FilterTypeDef",
    "ListTimelineEventsOutputTypeDef",
    "GetTimelineEventOutputTypeDef",
    "UpdateReplicationSetInputRequestTypeDef",
    "ActionOutputTypeDef",
    "SsmAutomationUnionTypeDef",
    "ListIncidentRecordsOutputTypeDef",
    "GetIncidentRecordOutputTypeDef",
    "ItemIdentifierTypeDef",
    "IntegrationTypeDef",
    "GetReplicationSetOutputTypeDef",
    "BatchGetIncidentFindingsOutputTypeDef",
    "ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef",
    "ListIncidentRecordsInputRequestTypeDef",
    "ListTimelineEventsInputListTimelineEventsPaginateTypeDef",
    "ListTimelineEventsInputRequestTypeDef",
    "ActionTypeDef",
    "RelatedItemTypeDef",
    "GetResponsePlanOutputTypeDef",
    "ActionUnionTypeDef",
    "UpdateResponsePlanInputRequestTypeDef",
    "ListRelatedItemsOutputTypeDef",
    "RelatedItemsUpdateTypeDef",
    "StartIncidentInputRequestTypeDef",
    "CreateResponsePlanInputRequestTypeDef",
    "UpdateRelatedItemsInputRequestTypeDef",
)

AddRegionActionTypeDef = TypedDict(
    "AddRegionActionTypeDef",
    {
        "regionName": str,
        "sseKmsKeyId": NotRequired[str],
    },
)
AttributeValueListTypeDef = TypedDict(
    "AttributeValueListTypeDef",
    {
        "integerValues": NotRequired[Sequence[int]],
        "stringValues": NotRequired[Sequence[str]],
    },
)
AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "ssmExecutionArn": NotRequired[str],
    },
)
BatchGetIncidentFindingsErrorTypeDef = TypedDict(
    "BatchGetIncidentFindingsErrorTypeDef",
    {
        "code": str,
        "findingId": str,
        "message": str,
    },
)
BatchGetIncidentFindingsInputRequestTypeDef = TypedDict(
    "BatchGetIncidentFindingsInputRequestTypeDef",
    {
        "findingIds": Sequence[str],
        "incidentRecordArn": str,
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
        "HostId": NotRequired[str],
    },
)
ChatChannelOutputTypeDef = TypedDict(
    "ChatChannelOutputTypeDef",
    {
        "chatbotSns": NotRequired[List[str]],
        "empty": NotRequired[Dict[str, Any]],
    },
)
ChatChannelTypeDef = TypedDict(
    "ChatChannelTypeDef",
    {
        "chatbotSns": NotRequired[Sequence[str]],
        "empty": NotRequired[Mapping[str, Any]],
    },
)
CloudFormationStackUpdateTypeDef = TypedDict(
    "CloudFormationStackUpdateTypeDef",
    {
        "stackArn": str,
        "startTime": datetime,
        "endTime": NotRequired[datetime],
    },
)
CodeDeployDeploymentTypeDef = TypedDict(
    "CodeDeployDeploymentTypeDef",
    {
        "deploymentGroupArn": str,
        "deploymentId": str,
        "startTime": datetime,
        "endTime": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]
RegionMapInputValueTypeDef = TypedDict(
    "RegionMapInputValueTypeDef",
    {
        "sseKmsKeyId": NotRequired[str],
    },
)
EventReferenceTypeDef = TypedDict(
    "EventReferenceTypeDef",
    {
        "relatedItemId": NotRequired[str],
        "resource": NotRequired[str],
    },
)
DeleteIncidentRecordInputRequestTypeDef = TypedDict(
    "DeleteIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteRegionActionTypeDef = TypedDict(
    "DeleteRegionActionTypeDef",
    {
        "regionName": str,
    },
)
DeleteReplicationSetInputRequestTypeDef = TypedDict(
    "DeleteReplicationSetInputRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteResourcePolicyInputRequestTypeDef = TypedDict(
    "DeleteResourcePolicyInputRequestTypeDef",
    {
        "policyId": str,
        "resourceArn": str,
    },
)
DeleteResponsePlanInputRequestTypeDef = TypedDict(
    "DeleteResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteTimelineEventInputRequestTypeDef = TypedDict(
    "DeleteTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)
DynamicSsmParameterValueTypeDef = TypedDict(
    "DynamicSsmParameterValueTypeDef",
    {
        "variable": NotRequired[VariableTypeType],
    },
)
FindingSummaryTypeDef = TypedDict(
    "FindingSummaryTypeDef",
    {
        "id": str,
        "lastModifiedTime": datetime,
    },
)
GetIncidentRecordInputRequestTypeDef = TypedDict(
    "GetIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)
GetReplicationSetInputRequestTypeDef = TypedDict(
    "GetReplicationSetInputRequestTypeDef",
    {
        "arn": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
GetResourcePoliciesInputRequestTypeDef = TypedDict(
    "GetResourcePoliciesInputRequestTypeDef",
    {
        "resourceArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policyDocument": str,
        "policyId": str,
        "ramResourceShareRegion": str,
    },
)
GetResponsePlanInputRequestTypeDef = TypedDict(
    "GetResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)
GetTimelineEventInputRequestTypeDef = TypedDict(
    "GetTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)
IncidentRecordSourceTypeDef = TypedDict(
    "IncidentRecordSourceTypeDef",
    {
        "createdBy": str,
        "source": str,
        "invokedBy": NotRequired[str],
        "resourceArn": NotRequired[str],
    },
)
NotificationTargetItemTypeDef = TypedDict(
    "NotificationTargetItemTypeDef",
    {
        "snsTopicArn": NotRequired[str],
    },
)
PagerDutyIncidentDetailTypeDef = TypedDict(
    "PagerDutyIncidentDetailTypeDef",
    {
        "id": str,
        "autoResolve": NotRequired[bool],
        "secretId": NotRequired[str],
    },
)
ListIncidentFindingsInputRequestTypeDef = TypedDict(
    "ListIncidentFindingsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListRelatedItemsInputRequestTypeDef = TypedDict(
    "ListRelatedItemsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListReplicationSetsInputRequestTypeDef = TypedDict(
    "ListReplicationSetsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListResponsePlansInputRequestTypeDef = TypedDict(
    "ListResponsePlansInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ResponsePlanSummaryTypeDef = TypedDict(
    "ResponsePlanSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "displayName": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
PagerDutyIncidentConfigurationTypeDef = TypedDict(
    "PagerDutyIncidentConfigurationTypeDef",
    {
        "serviceId": str,
    },
)
PutResourcePolicyInputRequestTypeDef = TypedDict(
    "PutResourcePolicyInputRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)
RegionInfoTypeDef = TypedDict(
    "RegionInfoTypeDef",
    {
        "status": RegionStatusType,
        "statusUpdateDateTime": datetime,
        "sseKmsKeyId": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateDeletionProtectionInputRequestTypeDef = TypedDict(
    "UpdateDeletionProtectionInputRequestTypeDef",
    {
        "arn": str,
        "deletionProtected": bool,
        "clientToken": NotRequired[str],
    },
)
CreateReplicationSetOutputTypeDef = TypedDict(
    "CreateReplicationSetOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResponsePlanOutputTypeDef = TypedDict(
    "CreateResponsePlanOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTimelineEventOutputTypeDef = TypedDict(
    "CreateTimelineEventOutputTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReplicationSetsOutputTypeDef = TypedDict(
    "ListReplicationSetsOutputTypeDef",
    {
        "nextToken": str,
        "replicationSetArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
    {
        "policyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartIncidentOutputTypeDef = TypedDict(
    "StartIncidentOutputTypeDef",
    {
        "incidentRecordArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FindingDetailsTypeDef = TypedDict(
    "FindingDetailsTypeDef",
    {
        "cloudFormationStackUpdate": NotRequired[CloudFormationStackUpdateTypeDef],
        "codeDeployDeployment": NotRequired[CodeDeployDeploymentTypeDef],
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "after": NotRequired[TimestampTypeDef],
        "before": NotRequired[TimestampTypeDef],
        "equals": NotRequired[AttributeValueListTypeDef],
    },
)
TriggerDetailsTypeDef = TypedDict(
    "TriggerDetailsTypeDef",
    {
        "source": str,
        "timestamp": TimestampTypeDef,
        "rawData": NotRequired[str],
        "triggerArn": NotRequired[str],
    },
)
CreateReplicationSetInputRequestTypeDef = TypedDict(
    "CreateReplicationSetInputRequestTypeDef",
    {
        "regions": Mapping[str, RegionMapInputValueTypeDef],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateTimelineEventInputRequestTypeDef = TypedDict(
    "CreateTimelineEventInputRequestTypeDef",
    {
        "eventData": str,
        "eventTime": TimestampTypeDef,
        "eventType": str,
        "incidentRecordArn": str,
        "clientToken": NotRequired[str],
        "eventReferences": NotRequired[Sequence[EventReferenceTypeDef]],
    },
)
EventSummaryTypeDef = TypedDict(
    "EventSummaryTypeDef",
    {
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
        "eventReferences": NotRequired[List[EventReferenceTypeDef]],
    },
)
TimelineEventTypeDef = TypedDict(
    "TimelineEventTypeDef",
    {
        "eventData": str,
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
        "eventReferences": NotRequired[List[EventReferenceTypeDef]],
    },
)
UpdateTimelineEventInputRequestTypeDef = TypedDict(
    "UpdateTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
        "clientToken": NotRequired[str],
        "eventData": NotRequired[str],
        "eventReferences": NotRequired[Sequence[EventReferenceTypeDef]],
        "eventTime": NotRequired[TimestampTypeDef],
        "eventType": NotRequired[str],
    },
)
UpdateReplicationSetActionTypeDef = TypedDict(
    "UpdateReplicationSetActionTypeDef",
    {
        "addRegionAction": NotRequired[AddRegionActionTypeDef],
        "deleteRegionAction": NotRequired[DeleteRegionActionTypeDef],
    },
)
SsmAutomationOutputTypeDef = TypedDict(
    "SsmAutomationOutputTypeDef",
    {
        "documentName": str,
        "roleArn": str,
        "documentVersion": NotRequired[str],
        "dynamicParameters": NotRequired[Dict[str, DynamicSsmParameterValueTypeDef]],
        "parameters": NotRequired[Dict[str, List[str]]],
        "targetAccount": NotRequired[SsmTargetAccountType],
    },
)
SsmAutomationTypeDef = TypedDict(
    "SsmAutomationTypeDef",
    {
        "documentName": str,
        "roleArn": str,
        "documentVersion": NotRequired[str],
        "dynamicParameters": NotRequired[Mapping[str, DynamicSsmParameterValueTypeDef]],
        "parameters": NotRequired[Mapping[str, Sequence[str]]],
        "targetAccount": NotRequired[SsmTargetAccountType],
    },
)
ListIncidentFindingsOutputTypeDef = TypedDict(
    "ListIncidentFindingsOutputTypeDef",
    {
        "findings": List[FindingSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef = TypedDict(
    "GetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef",
    {
        "arn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef = TypedDict(
    "GetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef",
    {
        "arn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef = TypedDict(
    "GetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef",
    {
        "resourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIncidentFindingsInputListIncidentFindingsPaginateTypeDef = TypedDict(
    "ListIncidentFindingsInputListIncidentFindingsPaginateTypeDef",
    {
        "incidentRecordArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRelatedItemsInputListRelatedItemsPaginateTypeDef = TypedDict(
    "ListRelatedItemsInputListRelatedItemsPaginateTypeDef",
    {
        "incidentRecordArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReplicationSetsInputListReplicationSetsPaginateTypeDef = TypedDict(
    "ListReplicationSetsInputListReplicationSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResponsePlansInputListResponsePlansPaginateTypeDef = TypedDict(
    "ListResponsePlansInputListResponsePlansPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourcePoliciesOutputTypeDef = TypedDict(
    "GetResourcePoliciesOutputTypeDef",
    {
        "nextToken": str,
        "resourcePolicies": List[ResourcePolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IncidentRecordSummaryTypeDef = TypedDict(
    "IncidentRecordSummaryTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "impact": int,
        "incidentRecordSource": IncidentRecordSourceTypeDef,
        "status": IncidentRecordStatusType,
        "title": str,
        "resolvedTime": NotRequired[datetime],
    },
)
IncidentRecordTypeDef = TypedDict(
    "IncidentRecordTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "dedupeString": str,
        "impact": int,
        "incidentRecordSource": IncidentRecordSourceTypeDef,
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "status": IncidentRecordStatusType,
        "title": str,
        "automationExecutions": NotRequired[List[AutomationExecutionTypeDef]],
        "chatChannel": NotRequired[ChatChannelOutputTypeDef],
        "notificationTargets": NotRequired[List[NotificationTargetItemTypeDef]],
        "resolvedTime": NotRequired[datetime],
        "summary": NotRequired[str],
    },
)
IncidentTemplateOutputTypeDef = TypedDict(
    "IncidentTemplateOutputTypeDef",
    {
        "impact": int,
        "title": str,
        "dedupeString": NotRequired[str],
        "incidentTags": NotRequired[Dict[str, str]],
        "notificationTargets": NotRequired[List[NotificationTargetItemTypeDef]],
        "summary": NotRequired[str],
    },
)
IncidentTemplateTypeDef = TypedDict(
    "IncidentTemplateTypeDef",
    {
        "impact": int,
        "title": str,
        "dedupeString": NotRequired[str],
        "incidentTags": NotRequired[Mapping[str, str]],
        "notificationTargets": NotRequired[Sequence[NotificationTargetItemTypeDef]],
        "summary": NotRequired[str],
    },
)
UpdateIncidentRecordInputRequestTypeDef = TypedDict(
    "UpdateIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
        "chatChannel": NotRequired[ChatChannelTypeDef],
        "clientToken": NotRequired[str],
        "impact": NotRequired[int],
        "notificationTargets": NotRequired[Sequence[NotificationTargetItemTypeDef]],
        "status": NotRequired[IncidentRecordStatusType],
        "summary": NotRequired[str],
        "title": NotRequired[str],
    },
)
ItemValueTypeDef = TypedDict(
    "ItemValueTypeDef",
    {
        "arn": NotRequired[str],
        "metricDefinition": NotRequired[str],
        "pagerDutyIncidentDetail": NotRequired[PagerDutyIncidentDetailTypeDef],
        "url": NotRequired[str],
    },
)
ListResponsePlansOutputTypeDef = TypedDict(
    "ListResponsePlansOutputTypeDef",
    {
        "nextToken": str,
        "responsePlanSummaries": List[ResponsePlanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PagerDutyConfigurationTypeDef = TypedDict(
    "PagerDutyConfigurationTypeDef",
    {
        "name": str,
        "pagerDutyIncidentConfiguration": PagerDutyIncidentConfigurationTypeDef,
        "secretId": str,
    },
)
ReplicationSetTypeDef = TypedDict(
    "ReplicationSetTypeDef",
    {
        "createdBy": str,
        "createdTime": datetime,
        "deletionProtected": bool,
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "regionMap": Dict[str, RegionInfoTypeDef],
        "status": ReplicationSetStatusType,
        "arn": NotRequired[str],
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "creationTime": datetime,
        "id": str,
        "lastModifiedTime": datetime,
        "details": NotRequired[FindingDetailsTypeDef],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "condition": ConditionTypeDef,
        "key": str,
    },
)
ListTimelineEventsOutputTypeDef = TypedDict(
    "ListTimelineEventsOutputTypeDef",
    {
        "eventSummaries": List[EventSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTimelineEventOutputTypeDef = TypedDict(
    "GetTimelineEventOutputTypeDef",
    {
        "event": TimelineEventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateReplicationSetInputRequestTypeDef = TypedDict(
    "UpdateReplicationSetInputRequestTypeDef",
    {
        "actions": Sequence[UpdateReplicationSetActionTypeDef],
        "arn": str,
        "clientToken": NotRequired[str],
    },
)
ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "ssmAutomation": NotRequired[SsmAutomationOutputTypeDef],
    },
)
SsmAutomationUnionTypeDef = Union[SsmAutomationTypeDef, SsmAutomationOutputTypeDef]
ListIncidentRecordsOutputTypeDef = TypedDict(
    "ListIncidentRecordsOutputTypeDef",
    {
        "incidentRecordSummaries": List[IncidentRecordSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIncidentRecordOutputTypeDef = TypedDict(
    "GetIncidentRecordOutputTypeDef",
    {
        "incidentRecord": IncidentRecordTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ItemIdentifierTypeDef = TypedDict(
    "ItemIdentifierTypeDef",
    {
        "type": ItemTypeType,
        "value": ItemValueTypeDef,
    },
)
IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "pagerDutyConfiguration": NotRequired[PagerDutyConfigurationTypeDef],
    },
)
GetReplicationSetOutputTypeDef = TypedDict(
    "GetReplicationSetOutputTypeDef",
    {
        "replicationSet": ReplicationSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetIncidentFindingsOutputTypeDef = TypedDict(
    "BatchGetIncidentFindingsOutputTypeDef",
    {
        "errors": List[BatchGetIncidentFindingsErrorTypeDef],
        "findings": List[FindingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef = TypedDict(
    "ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIncidentRecordsInputRequestTypeDef = TypedDict(
    "ListIncidentRecordsInputRequestTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTimelineEventsInputListTimelineEventsPaginateTypeDef = TypedDict(
    "ListTimelineEventsInputListTimelineEventsPaginateTypeDef",
    {
        "incidentRecordArn": str,
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "sortBy": NotRequired[Literal["EVENT_TIME"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTimelineEventsInputRequestTypeDef = TypedDict(
    "ListTimelineEventsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["EVENT_TIME"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ssmAutomation": NotRequired[SsmAutomationUnionTypeDef],
    },
)
RelatedItemTypeDef = TypedDict(
    "RelatedItemTypeDef",
    {
        "identifier": ItemIdentifierTypeDef,
        "generatedId": NotRequired[str],
        "title": NotRequired[str],
    },
)
GetResponsePlanOutputTypeDef = TypedDict(
    "GetResponsePlanOutputTypeDef",
    {
        "actions": List[ActionOutputTypeDef],
        "arn": str,
        "chatChannel": ChatChannelOutputTypeDef,
        "displayName": str,
        "engagements": List[str],
        "incidentTemplate": IncidentTemplateOutputTypeDef,
        "integrations": List[IntegrationTypeDef],
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActionUnionTypeDef = Union[ActionTypeDef, ActionOutputTypeDef]
UpdateResponsePlanInputRequestTypeDef = TypedDict(
    "UpdateResponsePlanInputRequestTypeDef",
    {
        "arn": str,
        "actions": NotRequired[Sequence[ActionTypeDef]],
        "chatChannel": NotRequired[ChatChannelTypeDef],
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "engagements": NotRequired[Sequence[str]],
        "incidentTemplateDedupeString": NotRequired[str],
        "incidentTemplateImpact": NotRequired[int],
        "incidentTemplateNotificationTargets": NotRequired[Sequence[NotificationTargetItemTypeDef]],
        "incidentTemplateSummary": NotRequired[str],
        "incidentTemplateTags": NotRequired[Mapping[str, str]],
        "incidentTemplateTitle": NotRequired[str],
        "integrations": NotRequired[Sequence[IntegrationTypeDef]],
    },
)
ListRelatedItemsOutputTypeDef = TypedDict(
    "ListRelatedItemsOutputTypeDef",
    {
        "nextToken": str,
        "relatedItems": List[RelatedItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RelatedItemsUpdateTypeDef = TypedDict(
    "RelatedItemsUpdateTypeDef",
    {
        "itemToAdd": NotRequired[RelatedItemTypeDef],
        "itemToRemove": NotRequired[ItemIdentifierTypeDef],
    },
)
StartIncidentInputRequestTypeDef = TypedDict(
    "StartIncidentInputRequestTypeDef",
    {
        "responsePlanArn": str,
        "clientToken": NotRequired[str],
        "impact": NotRequired[int],
        "relatedItems": NotRequired[Sequence[RelatedItemTypeDef]],
        "title": NotRequired[str],
        "triggerDetails": NotRequired[TriggerDetailsTypeDef],
    },
)
CreateResponsePlanInputRequestTypeDef = TypedDict(
    "CreateResponsePlanInputRequestTypeDef",
    {
        "incidentTemplate": IncidentTemplateTypeDef,
        "name": str,
        "actions": NotRequired[Sequence[ActionUnionTypeDef]],
        "chatChannel": NotRequired[ChatChannelTypeDef],
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "engagements": NotRequired[Sequence[str]],
        "integrations": NotRequired[Sequence[IntegrationTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateRelatedItemsInputRequestTypeDef = TypedDict(
    "UpdateRelatedItemsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "relatedItemsUpdate": RelatedItemsUpdateTypeDef,
        "clientToken": NotRequired[str],
    },
)
