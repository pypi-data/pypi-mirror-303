"""
Type annotations for inspector service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/type_defs/)

Usage::

    ```python
    from mypy_boto3_inspector.type_defs import AttributeTypeDef

    data: AttributeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AgentHealthCodeType,
    AgentHealthType,
    AssessmentRunNotificationSnsStatusCodeType,
    AssessmentRunStateType,
    FailedItemErrorCodeType,
    InspectorEventType,
    PreviewStatusType,
    ReportFileFormatType,
    ReportStatusType,
    ReportTypeType,
    ScopeTypeType,
    SeverityType,
    StopActionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AttributeTypeDef",
    "FailedItemDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "AgentFilterTypeDef",
    "AgentPreviewTypeDef",
    "TelemetryMetadataTypeDef",
    "DurationRangeTypeDef",
    "AssessmentRunNotificationTypeDef",
    "AssessmentRunStateChangeTypeDef",
    "AssessmentTargetFilterTypeDef",
    "AssessmentTargetTypeDef",
    "TagTypeDef",
    "CreateAssessmentTargetRequestRequestTypeDef",
    "CreateExclusionsPreviewRequestRequestTypeDef",
    "ResourceGroupTagTypeDef",
    "DeleteAssessmentRunRequestRequestTypeDef",
    "DeleteAssessmentTargetRequestRequestTypeDef",
    "DeleteAssessmentTemplateRequestRequestTypeDef",
    "DescribeAssessmentRunsRequestRequestTypeDef",
    "DescribeAssessmentTargetsRequestRequestTypeDef",
    "DescribeAssessmentTemplatesRequestRequestTypeDef",
    "DescribeExclusionsRequestRequestTypeDef",
    "DescribeFindingsRequestRequestTypeDef",
    "DescribeResourceGroupsRequestRequestTypeDef",
    "DescribeRulesPackagesRequestRequestTypeDef",
    "RulesPackageTypeDef",
    "EventSubscriptionTypeDef",
    "ScopeTypeDef",
    "InspectorServiceAttributesTypeDef",
    "GetAssessmentReportRequestRequestTypeDef",
    "GetExclusionsPreviewRequestRequestTypeDef",
    "GetTelemetryMetadataRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListEventSubscriptionsRequestRequestTypeDef",
    "ListExclusionsRequestRequestTypeDef",
    "ListRulesPackagesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PrivateIpTypeDef",
    "SecurityGroupTypeDef",
    "PreviewAgentsRequestRequestTypeDef",
    "RegisterCrossAccountAccessRoleRequestRequestTypeDef",
    "RemoveAttributesFromFindingsRequestRequestTypeDef",
    "StartAssessmentRunRequestRequestTypeDef",
    "StopAssessmentRunRequestRequestTypeDef",
    "SubscribeToEventRequestRequestTypeDef",
    "TimestampTypeDef",
    "UnsubscribeFromEventRequestRequestTypeDef",
    "UpdateAssessmentTargetRequestRequestTypeDef",
    "AddAttributesToFindingsRequestRequestTypeDef",
    "AssessmentTemplateTypeDef",
    "CreateAssessmentTemplateRequestRequestTypeDef",
    "AddAttributesToFindingsResponseTypeDef",
    "CreateAssessmentTargetResponseTypeDef",
    "CreateAssessmentTemplateResponseTypeDef",
    "CreateExclusionsPreviewResponseTypeDef",
    "CreateResourceGroupResponseTypeDef",
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAssessmentReportResponseTypeDef",
    "ListAssessmentRunsResponseTypeDef",
    "ListAssessmentTargetsResponseTypeDef",
    "ListAssessmentTemplatesResponseTypeDef",
    "ListExclusionsResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListRulesPackagesResponseTypeDef",
    "RemoveAttributesFromFindingsResponseTypeDef",
    "StartAssessmentRunResponseTypeDef",
    "ListAssessmentRunAgentsRequestRequestTypeDef",
    "PreviewAgentsResponseTypeDef",
    "AssessmentRunAgentTypeDef",
    "GetTelemetryMetadataResponseTypeDef",
    "AssessmentTemplateFilterTypeDef",
    "AssessmentRunTypeDef",
    "ListAssessmentTargetsRequestRequestTypeDef",
    "DescribeAssessmentTargetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SetTagsForResourceRequestRequestTypeDef",
    "CreateResourceGroupRequestRequestTypeDef",
    "ResourceGroupTypeDef",
    "DescribeRulesPackagesResponseTypeDef",
    "SubscriptionTypeDef",
    "ExclusionPreviewTypeDef",
    "ExclusionTypeDef",
    "ListAssessmentRunAgentsRequestListAssessmentRunAgentsPaginateTypeDef",
    "ListAssessmentTargetsRequestListAssessmentTargetsPaginateTypeDef",
    "ListEventSubscriptionsRequestListEventSubscriptionsPaginateTypeDef",
    "ListExclusionsRequestListExclusionsPaginateTypeDef",
    "ListRulesPackagesRequestListRulesPackagesPaginateTypeDef",
    "PreviewAgentsRequestPreviewAgentsPaginateTypeDef",
    "NetworkInterfaceTypeDef",
    "TimestampRangeTypeDef",
    "DescribeAssessmentTemplatesResponseTypeDef",
    "ListAssessmentRunAgentsResponseTypeDef",
    "ListAssessmentTemplatesRequestListAssessmentTemplatesPaginateTypeDef",
    "ListAssessmentTemplatesRequestRequestTypeDef",
    "DescribeAssessmentRunsResponseTypeDef",
    "DescribeResourceGroupsResponseTypeDef",
    "ListEventSubscriptionsResponseTypeDef",
    "GetExclusionsPreviewResponseTypeDef",
    "DescribeExclusionsResponseTypeDef",
    "AssetAttributesTypeDef",
    "AssessmentRunFilterTypeDef",
    "FindingFilterTypeDef",
    "FindingTypeDef",
    "ListAssessmentRunsRequestListAssessmentRunsPaginateTypeDef",
    "ListAssessmentRunsRequestRequestTypeDef",
    "ListFindingsRequestListFindingsPaginateTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "DescribeFindingsResponseTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)
FailedItemDetailsTypeDef = TypedDict(
    "FailedItemDetailsTypeDef",
    {
        "failureCode": FailedItemErrorCodeType,
        "retryable": bool,
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
AgentFilterTypeDef = TypedDict(
    "AgentFilterTypeDef",
    {
        "agentHealths": Sequence[AgentHealthType],
        "agentHealthCodes": Sequence[AgentHealthCodeType],
    },
)
AgentPreviewTypeDef = TypedDict(
    "AgentPreviewTypeDef",
    {
        "agentId": str,
        "hostname": NotRequired[str],
        "autoScalingGroup": NotRequired[str],
        "agentHealth": NotRequired[AgentHealthType],
        "agentVersion": NotRequired[str],
        "operatingSystem": NotRequired[str],
        "kernelVersion": NotRequired[str],
        "ipv4Address": NotRequired[str],
    },
)
TelemetryMetadataTypeDef = TypedDict(
    "TelemetryMetadataTypeDef",
    {
        "messageType": str,
        "count": int,
        "dataSize": NotRequired[int],
    },
)
DurationRangeTypeDef = TypedDict(
    "DurationRangeTypeDef",
    {
        "minSeconds": NotRequired[int],
        "maxSeconds": NotRequired[int],
    },
)
AssessmentRunNotificationTypeDef = TypedDict(
    "AssessmentRunNotificationTypeDef",
    {
        "date": datetime,
        "event": InspectorEventType,
        "error": bool,
        "message": NotRequired[str],
        "snsTopicArn": NotRequired[str],
        "snsPublishStatusCode": NotRequired[AssessmentRunNotificationSnsStatusCodeType],
    },
)
AssessmentRunStateChangeTypeDef = TypedDict(
    "AssessmentRunStateChangeTypeDef",
    {
        "stateChangedAt": datetime,
        "state": AssessmentRunStateType,
    },
)
AssessmentTargetFilterTypeDef = TypedDict(
    "AssessmentTargetFilterTypeDef",
    {
        "assessmentTargetNamePattern": NotRequired[str],
    },
)
AssessmentTargetTypeDef = TypedDict(
    "AssessmentTargetTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "resourceGroupArn": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)
CreateAssessmentTargetRequestRequestTypeDef = TypedDict(
    "CreateAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetName": str,
        "resourceGroupArn": NotRequired[str],
    },
)
CreateExclusionsPreviewRequestRequestTypeDef = TypedDict(
    "CreateExclusionsPreviewRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)
ResourceGroupTagTypeDef = TypedDict(
    "ResourceGroupTagTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)
DeleteAssessmentRunRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentRunRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)
DeleteAssessmentTargetRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
    },
)
DeleteAssessmentTemplateRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentTemplateRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)
DescribeAssessmentRunsRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentRunsRequestRequestTypeDef",
    {
        "assessmentRunArns": Sequence[str],
    },
)
DescribeAssessmentTargetsRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentTargetsRequestRequestTypeDef",
    {
        "assessmentTargetArns": Sequence[str],
    },
)
DescribeAssessmentTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentTemplatesRequestRequestTypeDef",
    {
        "assessmentTemplateArns": Sequence[str],
    },
)
DescribeExclusionsRequestRequestTypeDef = TypedDict(
    "DescribeExclusionsRequestRequestTypeDef",
    {
        "exclusionArns": Sequence[str],
        "locale": NotRequired[Literal["EN_US"]],
    },
)
DescribeFindingsRequestRequestTypeDef = TypedDict(
    "DescribeFindingsRequestRequestTypeDef",
    {
        "findingArns": Sequence[str],
        "locale": NotRequired[Literal["EN_US"]],
    },
)
DescribeResourceGroupsRequestRequestTypeDef = TypedDict(
    "DescribeResourceGroupsRequestRequestTypeDef",
    {
        "resourceGroupArns": Sequence[str],
    },
)
DescribeRulesPackagesRequestRequestTypeDef = TypedDict(
    "DescribeRulesPackagesRequestRequestTypeDef",
    {
        "rulesPackageArns": Sequence[str],
        "locale": NotRequired[Literal["EN_US"]],
    },
)
RulesPackageTypeDef = TypedDict(
    "RulesPackageTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "provider": str,
        "description": NotRequired[str],
    },
)
EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "event": InspectorEventType,
        "subscribedAt": datetime,
    },
)
ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "key": NotRequired[ScopeTypeType],
        "value": NotRequired[str],
    },
)
InspectorServiceAttributesTypeDef = TypedDict(
    "InspectorServiceAttributesTypeDef",
    {
        "schemaVersion": int,
        "assessmentRunArn": NotRequired[str],
        "rulesPackageArn": NotRequired[str],
    },
)
GetAssessmentReportRequestRequestTypeDef = TypedDict(
    "GetAssessmentReportRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "reportFileFormat": ReportFileFormatType,
        "reportType": ReportTypeType,
    },
)
GetExclusionsPreviewRequestRequestTypeDef = TypedDict(
    "GetExclusionsPreviewRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
        "previewToken": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "locale": NotRequired[Literal["EN_US"]],
    },
)
GetTelemetryMetadataRequestRequestTypeDef = TypedDict(
    "GetTelemetryMetadataRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
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
ListEventSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListEventSubscriptionsRequestRequestTypeDef",
    {
        "resourceArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListExclusionsRequestRequestTypeDef = TypedDict(
    "ListExclusionsRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListRulesPackagesRequestRequestTypeDef = TypedDict(
    "ListRulesPackagesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
PrivateIpTypeDef = TypedDict(
    "PrivateIpTypeDef",
    {
        "privateDnsName": NotRequired[str],
        "privateIpAddress": NotRequired[str],
    },
)
SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "groupName": NotRequired[str],
        "groupId": NotRequired[str],
    },
)
PreviewAgentsRequestRequestTypeDef = TypedDict(
    "PreviewAgentsRequestRequestTypeDef",
    {
        "previewAgentsArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RegisterCrossAccountAccessRoleRequestRequestTypeDef = TypedDict(
    "RegisterCrossAccountAccessRoleRequestRequestTypeDef",
    {
        "roleArn": str,
    },
)
RemoveAttributesFromFindingsRequestRequestTypeDef = TypedDict(
    "RemoveAttributesFromFindingsRequestRequestTypeDef",
    {
        "findingArns": Sequence[str],
        "attributeKeys": Sequence[str],
    },
)
StartAssessmentRunRequestRequestTypeDef = TypedDict(
    "StartAssessmentRunRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
        "assessmentRunName": NotRequired[str],
    },
)
StopAssessmentRunRequestRequestTypeDef = TypedDict(
    "StopAssessmentRunRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "stopAction": NotRequired[StopActionType],
    },
)
SubscribeToEventRequestRequestTypeDef = TypedDict(
    "SubscribeToEventRequestRequestTypeDef",
    {
        "resourceArn": str,
        "event": InspectorEventType,
        "topicArn": str,
    },
)
TimestampTypeDef = Union[datetime, str]
UnsubscribeFromEventRequestRequestTypeDef = TypedDict(
    "UnsubscribeFromEventRequestRequestTypeDef",
    {
        "resourceArn": str,
        "event": InspectorEventType,
        "topicArn": str,
    },
)
UpdateAssessmentTargetRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
        "assessmentTargetName": str,
        "resourceGroupArn": NotRequired[str],
    },
)
AddAttributesToFindingsRequestRequestTypeDef = TypedDict(
    "AddAttributesToFindingsRequestRequestTypeDef",
    {
        "findingArns": Sequence[str],
        "attributes": Sequence[AttributeTypeDef],
    },
)
AssessmentTemplateTypeDef = TypedDict(
    "AssessmentTemplateTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTargetArn": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List[AttributeTypeDef],
        "assessmentRunCount": int,
        "createdAt": datetime,
        "lastAssessmentRunArn": NotRequired[str],
    },
)
CreateAssessmentTemplateRequestRequestTypeDef = TypedDict(
    "CreateAssessmentTemplateRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
        "assessmentTemplateName": str,
        "durationInSeconds": int,
        "rulesPackageArns": Sequence[str],
        "userAttributesForFindings": NotRequired[Sequence[AttributeTypeDef]],
    },
)
AddAttributesToFindingsResponseTypeDef = TypedDict(
    "AddAttributesToFindingsResponseTypeDef",
    {
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssessmentTargetResponseTypeDef = TypedDict(
    "CreateAssessmentTargetResponseTypeDef",
    {
        "assessmentTargetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssessmentTemplateResponseTypeDef = TypedDict(
    "CreateAssessmentTemplateResponseTypeDef",
    {
        "assessmentTemplateArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExclusionsPreviewResponseTypeDef = TypedDict(
    "CreateExclusionsPreviewResponseTypeDef",
    {
        "previewToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceGroupResponseTypeDef = TypedDict(
    "CreateResourceGroupResponseTypeDef",
    {
        "resourceGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCrossAccountAccessRoleResponseTypeDef = TypedDict(
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    {
        "roleArn": str,
        "valid": bool,
        "registeredAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssessmentReportResponseTypeDef = TypedDict(
    "GetAssessmentReportResponseTypeDef",
    {
        "status": ReportStatusType,
        "url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentRunsResponseTypeDef = TypedDict(
    "ListAssessmentRunsResponseTypeDef",
    {
        "assessmentRunArns": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentTargetsResponseTypeDef = TypedDict(
    "ListAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargetArns": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentTemplatesResponseTypeDef = TypedDict(
    "ListAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplateArns": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListExclusionsResponseTypeDef = TypedDict(
    "ListExclusionsResponseTypeDef",
    {
        "exclusionArns": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findingArns": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRulesPackagesResponseTypeDef = TypedDict(
    "ListRulesPackagesResponseTypeDef",
    {
        "rulesPackageArns": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveAttributesFromFindingsResponseTypeDef = TypedDict(
    "RemoveAttributesFromFindingsResponseTypeDef",
    {
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAssessmentRunResponseTypeDef = TypedDict(
    "StartAssessmentRunResponseTypeDef",
    {
        "assessmentRunArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentRunAgentsRequestRequestTypeDef = TypedDict(
    "ListAssessmentRunAgentsRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "filter": NotRequired[AgentFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PreviewAgentsResponseTypeDef = TypedDict(
    "PreviewAgentsResponseTypeDef",
    {
        "agentPreviews": List[AgentPreviewTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssessmentRunAgentTypeDef = TypedDict(
    "AssessmentRunAgentTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": AgentHealthType,
        "agentHealthCode": AgentHealthCodeType,
        "telemetryMetadata": List[TelemetryMetadataTypeDef],
        "agentHealthDetails": NotRequired[str],
        "autoScalingGroup": NotRequired[str],
    },
)
GetTelemetryMetadataResponseTypeDef = TypedDict(
    "GetTelemetryMetadataResponseTypeDef",
    {
        "telemetryMetadata": List[TelemetryMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssessmentTemplateFilterTypeDef = TypedDict(
    "AssessmentTemplateFilterTypeDef",
    {
        "namePattern": NotRequired[str],
        "durationRange": NotRequired[DurationRangeTypeDef],
        "rulesPackageArns": NotRequired[Sequence[str]],
    },
)
AssessmentRunTypeDef = TypedDict(
    "AssessmentRunTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTemplateArn": str,
        "state": AssessmentRunStateType,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List[AttributeTypeDef],
        "createdAt": datetime,
        "stateChangedAt": datetime,
        "dataCollected": bool,
        "stateChanges": List[AssessmentRunStateChangeTypeDef],
        "notifications": List[AssessmentRunNotificationTypeDef],
        "findingCounts": Dict[SeverityType, int],
        "startedAt": NotRequired[datetime],
        "completedAt": NotRequired[datetime],
    },
)
ListAssessmentTargetsRequestRequestTypeDef = TypedDict(
    "ListAssessmentTargetsRequestRequestTypeDef",
    {
        "filter": NotRequired[AssessmentTargetFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeAssessmentTargetsResponseTypeDef = TypedDict(
    "DescribeAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargets": List[AssessmentTargetTypeDef],
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetTagsForResourceRequestRequestTypeDef = TypedDict(
    "SetTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateResourceGroupRequestRequestTypeDef = TypedDict(
    "CreateResourceGroupRequestRequestTypeDef",
    {
        "resourceGroupTags": Sequence[ResourceGroupTagTypeDef],
    },
)
ResourceGroupTypeDef = TypedDict(
    "ResourceGroupTypeDef",
    {
        "arn": str,
        "tags": List[ResourceGroupTagTypeDef],
        "createdAt": datetime,
    },
)
DescribeRulesPackagesResponseTypeDef = TypedDict(
    "DescribeRulesPackagesResponseTypeDef",
    {
        "rulesPackages": List[RulesPackageTypeDef],
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List[EventSubscriptionTypeDef],
    },
)
ExclusionPreviewTypeDef = TypedDict(
    "ExclusionPreviewTypeDef",
    {
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List[ScopeTypeDef],
        "attributes": NotRequired[List[AttributeTypeDef]],
    },
)
ExclusionTypeDef = TypedDict(
    "ExclusionTypeDef",
    {
        "arn": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List[ScopeTypeDef],
        "attributes": NotRequired[List[AttributeTypeDef]],
    },
)
ListAssessmentRunAgentsRequestListAssessmentRunAgentsPaginateTypeDef = TypedDict(
    "ListAssessmentRunAgentsRequestListAssessmentRunAgentsPaginateTypeDef",
    {
        "assessmentRunArn": str,
        "filter": NotRequired[AgentFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssessmentTargetsRequestListAssessmentTargetsPaginateTypeDef = TypedDict(
    "ListAssessmentTargetsRequestListAssessmentTargetsPaginateTypeDef",
    {
        "filter": NotRequired[AssessmentTargetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventSubscriptionsRequestListEventSubscriptionsPaginateTypeDef = TypedDict(
    "ListEventSubscriptionsRequestListEventSubscriptionsPaginateTypeDef",
    {
        "resourceArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExclusionsRequestListExclusionsPaginateTypeDef = TypedDict(
    "ListExclusionsRequestListExclusionsPaginateTypeDef",
    {
        "assessmentRunArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesPackagesRequestListRulesPackagesPaginateTypeDef = TypedDict(
    "ListRulesPackagesRequestListRulesPackagesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
PreviewAgentsRequestPreviewAgentsPaginateTypeDef = TypedDict(
    "PreviewAgentsRequestPreviewAgentsPaginateTypeDef",
    {
        "previewAgentsArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": NotRequired[str],
        "subnetId": NotRequired[str],
        "vpcId": NotRequired[str],
        "privateDnsName": NotRequired[str],
        "privateIpAddress": NotRequired[str],
        "privateIpAddresses": NotRequired[List[PrivateIpTypeDef]],
        "publicDnsName": NotRequired[str],
        "publicIp": NotRequired[str],
        "ipv6Addresses": NotRequired[List[str]],
        "securityGroups": NotRequired[List[SecurityGroupTypeDef]],
    },
)
TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "beginDate": NotRequired[TimestampTypeDef],
        "endDate": NotRequired[TimestampTypeDef],
    },
)
DescribeAssessmentTemplatesResponseTypeDef = TypedDict(
    "DescribeAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplates": List[AssessmentTemplateTypeDef],
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentRunAgentsResponseTypeDef = TypedDict(
    "ListAssessmentRunAgentsResponseTypeDef",
    {
        "assessmentRunAgents": List[AssessmentRunAgentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentTemplatesRequestListAssessmentTemplatesPaginateTypeDef = TypedDict(
    "ListAssessmentTemplatesRequestListAssessmentTemplatesPaginateTypeDef",
    {
        "assessmentTargetArns": NotRequired[Sequence[str]],
        "filter": NotRequired[AssessmentTemplateFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssessmentTemplatesRequestRequestTypeDef = TypedDict(
    "ListAssessmentTemplatesRequestRequestTypeDef",
    {
        "assessmentTargetArns": NotRequired[Sequence[str]],
        "filter": NotRequired[AssessmentTemplateFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeAssessmentRunsResponseTypeDef",
    {
        "assessmentRuns": List[AssessmentRunTypeDef],
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeResourceGroupsResponseTypeDef = TypedDict(
    "DescribeResourceGroupsResponseTypeDef",
    {
        "resourceGroups": List[ResourceGroupTypeDef],
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventSubscriptionsResponseTypeDef = TypedDict(
    "ListEventSubscriptionsResponseTypeDef",
    {
        "subscriptions": List[SubscriptionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExclusionsPreviewResponseTypeDef = TypedDict(
    "GetExclusionsPreviewResponseTypeDef",
    {
        "previewStatus": PreviewStatusType,
        "exclusionPreviews": List[ExclusionPreviewTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExclusionsResponseTypeDef = TypedDict(
    "DescribeExclusionsResponseTypeDef",
    {
        "exclusions": Dict[str, ExclusionTypeDef],
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetAttributesTypeDef = TypedDict(
    "AssetAttributesTypeDef",
    {
        "schemaVersion": int,
        "agentId": NotRequired[str],
        "autoScalingGroup": NotRequired[str],
        "amiId": NotRequired[str],
        "hostname": NotRequired[str],
        "ipv4Addresses": NotRequired[List[str]],
        "tags": NotRequired[List[TagTypeDef]],
        "networkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
    },
)
AssessmentRunFilterTypeDef = TypedDict(
    "AssessmentRunFilterTypeDef",
    {
        "namePattern": NotRequired[str],
        "states": NotRequired[Sequence[AssessmentRunStateType]],
        "durationRange": NotRequired[DurationRangeTypeDef],
        "rulesPackageArns": NotRequired[Sequence[str]],
        "startTimeRange": NotRequired[TimestampRangeTypeDef],
        "completionTimeRange": NotRequired[TimestampRangeTypeDef],
        "stateChangeTimeRange": NotRequired[TimestampRangeTypeDef],
    },
)
FindingFilterTypeDef = TypedDict(
    "FindingFilterTypeDef",
    {
        "agentIds": NotRequired[Sequence[str]],
        "autoScalingGroups": NotRequired[Sequence[str]],
        "ruleNames": NotRequired[Sequence[str]],
        "severities": NotRequired[Sequence[SeverityType]],
        "rulesPackageArns": NotRequired[Sequence[str]],
        "attributes": NotRequired[Sequence[AttributeTypeDef]],
        "userAttributes": NotRequired[Sequence[AttributeTypeDef]],
        "creationTimeRange": NotRequired[TimestampRangeTypeDef],
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "arn": str,
        "attributes": List[AttributeTypeDef],
        "userAttributes": List[AttributeTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
        "schemaVersion": NotRequired[int],
        "service": NotRequired[str],
        "serviceAttributes": NotRequired[InspectorServiceAttributesTypeDef],
        "assetType": NotRequired[Literal["ec2-instance"]],
        "assetAttributes": NotRequired[AssetAttributesTypeDef],
        "id": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
        "recommendation": NotRequired[str],
        "severity": NotRequired[SeverityType],
        "numericSeverity": NotRequired[float],
        "confidence": NotRequired[int],
        "indicatorOfCompromise": NotRequired[bool],
    },
)
ListAssessmentRunsRequestListAssessmentRunsPaginateTypeDef = TypedDict(
    "ListAssessmentRunsRequestListAssessmentRunsPaginateTypeDef",
    {
        "assessmentTemplateArns": NotRequired[Sequence[str]],
        "filter": NotRequired[AssessmentRunFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssessmentRunsRequestRequestTypeDef = TypedDict(
    "ListAssessmentRunsRequestRequestTypeDef",
    {
        "assessmentTemplateArns": NotRequired[Sequence[str]],
        "filter": NotRequired[AssessmentRunFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFindingsRequestListFindingsPaginateTypeDef = TypedDict(
    "ListFindingsRequestListFindingsPaginateTypeDef",
    {
        "assessmentRunArns": NotRequired[Sequence[str]],
        "filter": NotRequired[FindingFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "assessmentRunArns": NotRequired[Sequence[str]],
        "filter": NotRequired[FindingFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeFindingsResponseTypeDef = TypedDict(
    "DescribeFindingsResponseTypeDef",
    {
        "findings": List[FindingTypeDef],
        "failedItems": Dict[str, FailedItemDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
