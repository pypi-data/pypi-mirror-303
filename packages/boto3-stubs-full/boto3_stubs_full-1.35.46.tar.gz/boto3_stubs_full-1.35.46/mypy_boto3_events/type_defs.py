"""
Type annotations for events service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/type_defs/)

Usage::

    ```python
    from mypy_boto3_events.type_defs import ActivateEventSourceRequestRequestTypeDef

    data: ActivateEventSourceRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ApiDestinationHttpMethodType,
    ApiDestinationStateType,
    ArchiveStateType,
    AssignPublicIpType,
    ConnectionAuthorizationTypeType,
    ConnectionOAuthHttpMethodType,
    ConnectionStateType,
    EndpointStateType,
    EventSourceStateType,
    LaunchTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    ReplayStateType,
    ReplicationStateType,
    RuleStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ActivateEventSourceRequestRequestTypeDef",
    "ApiDestinationTypeDef",
    "AppSyncParametersTypeDef",
    "ArchiveTypeDef",
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchRetryStrategyTypeDef",
    "CancelReplayRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "ConditionTypeDef",
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    "ConnectionBasicAuthResponseParametersTypeDef",
    "ConnectionBodyParameterTypeDef",
    "ConnectionHeaderParameterTypeDef",
    "ConnectionQueryStringParameterTypeDef",
    "ConnectionOAuthClientResponseParametersTypeDef",
    "ConnectionTypeDef",
    "CreateApiDestinationRequestRequestTypeDef",
    "CreateArchiveRequestRequestTypeDef",
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    "EndpointEventBusTypeDef",
    "ReplicationConfigTypeDef",
    "DeadLetterConfigTypeDef",
    "TagTypeDef",
    "CreatePartnerEventSourceRequestRequestTypeDef",
    "DeactivateEventSourceRequestRequestTypeDef",
    "DeauthorizeConnectionRequestRequestTypeDef",
    "DeleteApiDestinationRequestRequestTypeDef",
    "DeleteArchiveRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "DeleteEventBusRequestRequestTypeDef",
    "DeletePartnerEventSourceRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DescribeApiDestinationRequestRequestTypeDef",
    "DescribeArchiveRequestRequestTypeDef",
    "DescribeConnectionRequestRequestTypeDef",
    "DescribeEndpointRequestRequestTypeDef",
    "DescribeEventBusRequestRequestTypeDef",
    "DescribeEventSourceRequestRequestTypeDef",
    "DescribePartnerEventSourceRequestRequestTypeDef",
    "DescribeReplayRequestRequestTypeDef",
    "ReplayDestinationOutputTypeDef",
    "DescribeRuleRequestRequestTypeDef",
    "DisableRuleRequestRequestTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "EnableRuleRequestRequestTypeDef",
    "EventBusTypeDef",
    "EventSourceTypeDef",
    "PrimaryTypeDef",
    "SecondaryTypeDef",
    "HttpParametersOutputTypeDef",
    "HttpParametersTypeDef",
    "InputTransformerOutputTypeDef",
    "InputTransformerTypeDef",
    "KinesisParametersTypeDef",
    "ListApiDestinationsRequestRequestTypeDef",
    "ListArchivesRequestRequestTypeDef",
    "ListConnectionsRequestRequestTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEventBusesRequestRequestTypeDef",
    "ListEventSourcesRequestRequestTypeDef",
    "ListPartnerEventSourceAccountsRequestRequestTypeDef",
    "PartnerEventSourceAccountTypeDef",
    "ListPartnerEventSourcesRequestRequestTypeDef",
    "PartnerEventSourceTypeDef",
    "ListReplaysRequestRequestTypeDef",
    "ReplayTypeDef",
    "PaginatorConfigTypeDef",
    "ListRuleNamesByTargetRequestRequestTypeDef",
    "ListRulesRequestRequestTypeDef",
    "RuleTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTargetsByRuleRequestRequestTypeDef",
    "TimestampTypeDef",
    "PutEventsResultEntryTypeDef",
    "PutPartnerEventsResultEntryTypeDef",
    "PutTargetsResultEntryTypeDef",
    "RedshiftDataParametersOutputTypeDef",
    "RedshiftDataParametersTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "RemoveTargetsRequestRequestTypeDef",
    "RemoveTargetsResultEntryTypeDef",
    "ReplayDestinationTypeDef",
    "RetryPolicyTypeDef",
    "RunCommandTargetOutputTypeDef",
    "RunCommandTargetTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SqsParametersTypeDef",
    "TestEventPatternRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiDestinationRequestRequestTypeDef",
    "UpdateArchiveRequestRequestTypeDef",
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "AwsVpcConfigurationUnionTypeDef",
    "BatchParametersTypeDef",
    "CancelReplayResponseTypeDef",
    "CreateApiDestinationResponseTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreatePartnerEventSourceResponseTypeDef",
    "DeauthorizeConnectionResponseTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DescribeApiDestinationResponseTypeDef",
    "DescribeArchiveResponseTypeDef",
    "DescribeEventSourceResponseTypeDef",
    "DescribePartnerEventSourceResponseTypeDef",
    "DescribeRuleResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListApiDestinationsResponseTypeDef",
    "ListArchivesResponseTypeDef",
    "ListRuleNamesByTargetResponseTypeDef",
    "PutRuleResponseTypeDef",
    "StartReplayResponseTypeDef",
    "TestEventPatternResponseTypeDef",
    "UpdateApiDestinationResponseTypeDef",
    "UpdateArchiveResponseTypeDef",
    "UpdateConnectionResponseTypeDef",
    "PutPermissionRequestRequestTypeDef",
    "ConnectionHttpParametersOutputTypeDef",
    "ConnectionHttpParametersTypeDef",
    "ListConnectionsResponseTypeDef",
    "CreateEventBusResponseTypeDef",
    "DescribeEventBusResponseTypeDef",
    "UpdateEventBusRequestRequestTypeDef",
    "UpdateEventBusResponseTypeDef",
    "CreateEventBusRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutRuleRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DescribeReplayResponseTypeDef",
    "ListEventBusesResponseTypeDef",
    "ListEventSourcesResponseTypeDef",
    "FailoverConfigTypeDef",
    "HttpParametersUnionTypeDef",
    "InputTransformerUnionTypeDef",
    "ListPartnerEventSourceAccountsResponseTypeDef",
    "ListPartnerEventSourcesResponseTypeDef",
    "ListReplaysResponseTypeDef",
    "ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef",
    "ListRulesRequestListRulesPaginateTypeDef",
    "ListTargetsByRuleRequestListTargetsByRulePaginateTypeDef",
    "ListRulesResponseTypeDef",
    "PutEventsRequestEntryTypeDef",
    "PutPartnerEventsRequestEntryTypeDef",
    "PutEventsResponseTypeDef",
    "PutPartnerEventsResponseTypeDef",
    "PutTargetsResponseTypeDef",
    "RedshiftDataParametersUnionTypeDef",
    "RemoveTargetsResponseTypeDef",
    "StartReplayRequestRequestTypeDef",
    "RunCommandParametersOutputTypeDef",
    "RunCommandTargetUnionTypeDef",
    "SageMakerPipelineParametersOutputTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "EcsParametersOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "ConnectionOAuthResponseParametersTypeDef",
    "ConnectionHttpParametersUnionTypeDef",
    "RoutingConfigTypeDef",
    "PutEventsRequestRequestTypeDef",
    "PutPartnerEventsRequestRequestTypeDef",
    "RunCommandParametersTypeDef",
    "SageMakerPipelineParametersUnionTypeDef",
    "TargetOutputTypeDef",
    "NetworkConfigurationUnionTypeDef",
    "ConnectionAuthResponseParametersTypeDef",
    "CreateConnectionOAuthRequestParametersTypeDef",
    "UpdateConnectionOAuthRequestParametersTypeDef",
    "CreateEndpointRequestRequestTypeDef",
    "CreateEndpointResponseTypeDef",
    "DescribeEndpointResponseTypeDef",
    "EndpointTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "UpdateEndpointResponseTypeDef",
    "RunCommandParametersUnionTypeDef",
    "ListTargetsByRuleResponseTypeDef",
    "EcsParametersTypeDef",
    "DescribeConnectionResponseTypeDef",
    "CreateConnectionAuthRequestParametersTypeDef",
    "UpdateConnectionAuthRequestParametersTypeDef",
    "ListEndpointsResponseTypeDef",
    "EcsParametersUnionTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "TargetTypeDef",
    "TargetUnionTypeDef",
    "PutTargetsRequestRequestTypeDef",
)

ActivateEventSourceRequestRequestTypeDef = TypedDict(
    "ActivateEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
ApiDestinationTypeDef = TypedDict(
    "ApiDestinationTypeDef",
    {
        "ApiDestinationArn": NotRequired[str],
        "Name": NotRequired[str],
        "ApiDestinationState": NotRequired[ApiDestinationStateType],
        "ConnectionArn": NotRequired[str],
        "InvocationEndpoint": NotRequired[str],
        "HttpMethod": NotRequired[ApiDestinationHttpMethodType],
        "InvocationRateLimitPerSecond": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)
AppSyncParametersTypeDef = TypedDict(
    "AppSyncParametersTypeDef",
    {
        "GraphQLOperation": NotRequired[str],
    },
)
ArchiveTypeDef = TypedDict(
    "ArchiveTypeDef",
    {
        "ArchiveName": NotRequired[str],
        "EventSourceArn": NotRequired[str],
        "State": NotRequired[ArchiveStateType],
        "StateReason": NotRequired[str],
        "RetentionDays": NotRequired[int],
        "SizeBytes": NotRequired[int],
        "EventCount": NotRequired[int],
        "CreationTime": NotRequired[datetime],
    },
)
AwsVpcConfigurationOutputTypeDef = TypedDict(
    "AwsVpcConfigurationOutputTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": NotRequired[List[str]],
        "AssignPublicIp": NotRequired[AssignPublicIpType],
    },
)
AwsVpcConfigurationTypeDef = TypedDict(
    "AwsVpcConfigurationTypeDef",
    {
        "Subnets": Sequence[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "AssignPublicIp": NotRequired[AssignPublicIpType],
    },
)
BatchArrayPropertiesTypeDef = TypedDict(
    "BatchArrayPropertiesTypeDef",
    {
        "Size": NotRequired[int],
    },
)
BatchRetryStrategyTypeDef = TypedDict(
    "BatchRetryStrategyTypeDef",
    {
        "Attempts": NotRequired[int],
    },
)
CancelReplayRequestRequestTypeDef = TypedDict(
    "CancelReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
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
CapacityProviderStrategyItemTypeDef = TypedDict(
    "CapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
        "weight": NotRequired[int],
        "base": NotRequired[int],
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Type": str,
        "Key": str,
        "Value": str,
    },
)
ConnectionApiKeyAuthResponseParametersTypeDef = TypedDict(
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    {
        "ApiKeyName": NotRequired[str],
    },
)
ConnectionBasicAuthResponseParametersTypeDef = TypedDict(
    "ConnectionBasicAuthResponseParametersTypeDef",
    {
        "Username": NotRequired[str],
    },
)
ConnectionBodyParameterTypeDef = TypedDict(
    "ConnectionBodyParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "IsValueSecret": NotRequired[bool],
    },
)
ConnectionHeaderParameterTypeDef = TypedDict(
    "ConnectionHeaderParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "IsValueSecret": NotRequired[bool],
    },
)
ConnectionQueryStringParameterTypeDef = TypedDict(
    "ConnectionQueryStringParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "IsValueSecret": NotRequired[bool],
    },
)
ConnectionOAuthClientResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthClientResponseParametersTypeDef",
    {
        "ClientID": NotRequired[str],
    },
)
ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionArn": NotRequired[str],
        "Name": NotRequired[str],
        "ConnectionState": NotRequired[ConnectionStateType],
        "StateReason": NotRequired[str],
        "AuthorizationType": NotRequired[ConnectionAuthorizationTypeType],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "LastAuthorizedTime": NotRequired[datetime],
    },
)
CreateApiDestinationRequestRequestTypeDef = TypedDict(
    "CreateApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "Description": NotRequired[str],
        "InvocationRateLimitPerSecond": NotRequired[int],
    },
)
CreateArchiveRequestRequestTypeDef = TypedDict(
    "CreateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
        "Description": NotRequired[str],
        "EventPattern": NotRequired[str],
        "RetentionDays": NotRequired[int],
    },
)
CreateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": str,
        "ApiKeyValue": str,
    },
)
CreateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)
CreateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": str,
        "ClientSecret": str,
    },
)
EndpointEventBusTypeDef = TypedDict(
    "EndpointEventBusTypeDef",
    {
        "EventBusArn": str,
    },
)
ReplicationConfigTypeDef = TypedDict(
    "ReplicationConfigTypeDef",
    {
        "State": NotRequired[ReplicationStateType],
    },
)
DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreatePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "CreatePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)
DeactivateEventSourceRequestRequestTypeDef = TypedDict(
    "DeactivateEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeauthorizeConnectionRequestRequestTypeDef = TypedDict(
    "DeauthorizeConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteApiDestinationRequestRequestTypeDef = TypedDict(
    "DeleteApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteArchiveRequestRequestTypeDef = TypedDict(
    "DeleteArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)
DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteEventBusRequestRequestTypeDef = TypedDict(
    "DeleteEventBusRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeletePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "DeletePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)
DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventBusName": NotRequired[str],
        "Force": NotRequired[bool],
    },
)
DescribeApiDestinationRequestRequestTypeDef = TypedDict(
    "DescribeApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeArchiveRequestRequestTypeDef = TypedDict(
    "DescribeArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)
DescribeConnectionRequestRequestTypeDef = TypedDict(
    "DescribeConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeEndpointRequestRequestTypeDef = TypedDict(
    "DescribeEndpointRequestRequestTypeDef",
    {
        "Name": str,
        "HomeRegion": NotRequired[str],
    },
)
DescribeEventBusRequestRequestTypeDef = TypedDict(
    "DescribeEventBusRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
    },
)
DescribeEventSourceRequestRequestTypeDef = TypedDict(
    "DescribeEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "DescribePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeReplayRequestRequestTypeDef = TypedDict(
    "DescribeReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
    },
)
ReplayDestinationOutputTypeDef = TypedDict(
    "ReplayDestinationOutputTypeDef",
    {
        "Arn": str,
        "FilterArns": NotRequired[List[str]],
    },
)
DescribeRuleRequestRequestTypeDef = TypedDict(
    "DescribeRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventBusName": NotRequired[str],
    },
)
DisableRuleRequestRequestTypeDef = TypedDict(
    "DisableRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventBusName": NotRequired[str],
    },
)
PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": NotRequired[PlacementConstraintTypeType],
        "expression": NotRequired[str],
    },
)
PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": NotRequired[PlacementStrategyTypeType],
        "field": NotRequired[str],
    },
)
EnableRuleRequestRequestTypeDef = TypedDict(
    "EnableRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventBusName": NotRequired[str],
    },
)
EventBusTypeDef = TypedDict(
    "EventBusTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "Policy": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)
EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "ExpirationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "State": NotRequired[EventSourceStateType],
    },
)
PrimaryTypeDef = TypedDict(
    "PrimaryTypeDef",
    {
        "HealthCheck": str,
    },
)
SecondaryTypeDef = TypedDict(
    "SecondaryTypeDef",
    {
        "Route": str,
    },
)
HttpParametersOutputTypeDef = TypedDict(
    "HttpParametersOutputTypeDef",
    {
        "PathParameterValues": NotRequired[List[str]],
        "HeaderParameters": NotRequired[Dict[str, str]],
        "QueryStringParameters": NotRequired[Dict[str, str]],
    },
)
HttpParametersTypeDef = TypedDict(
    "HttpParametersTypeDef",
    {
        "PathParameterValues": NotRequired[Sequence[str]],
        "HeaderParameters": NotRequired[Mapping[str, str]],
        "QueryStringParameters": NotRequired[Mapping[str, str]],
    },
)
InputTransformerOutputTypeDef = TypedDict(
    "InputTransformerOutputTypeDef",
    {
        "InputTemplate": str,
        "InputPathsMap": NotRequired[Dict[str, str]],
    },
)
InputTransformerTypeDef = TypedDict(
    "InputTransformerTypeDef",
    {
        "InputTemplate": str,
        "InputPathsMap": NotRequired[Mapping[str, str]],
    },
)
KinesisParametersTypeDef = TypedDict(
    "KinesisParametersTypeDef",
    {
        "PartitionKeyPath": str,
    },
)
ListApiDestinationsRequestRequestTypeDef = TypedDict(
    "ListApiDestinationsRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListArchivesRequestRequestTypeDef = TypedDict(
    "ListArchivesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "EventSourceArn": NotRequired[str],
        "State": NotRequired[ArchiveStateType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListConnectionsRequestRequestTypeDef = TypedDict(
    "ListConnectionsRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "ConnectionState": NotRequired[ConnectionStateType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListEndpointsRequestRequestTypeDef = TypedDict(
    "ListEndpointsRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "HomeRegion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEventBusesRequestRequestTypeDef = TypedDict(
    "ListEventBusesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListEventSourcesRequestRequestTypeDef = TypedDict(
    "ListEventSourcesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListPartnerEventSourceAccountsRequestRequestTypeDef = TypedDict(
    "ListPartnerEventSourceAccountsRequestRequestTypeDef",
    {
        "EventSourceName": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
PartnerEventSourceAccountTypeDef = TypedDict(
    "PartnerEventSourceAccountTypeDef",
    {
        "Account": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "ExpirationTime": NotRequired[datetime],
        "State": NotRequired[EventSourceStateType],
    },
)
ListPartnerEventSourcesRequestRequestTypeDef = TypedDict(
    "ListPartnerEventSourcesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
PartnerEventSourceTypeDef = TypedDict(
    "PartnerEventSourceTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ListReplaysRequestRequestTypeDef = TypedDict(
    "ListReplaysRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "State": NotRequired[ReplayStateType],
        "EventSourceArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ReplayTypeDef = TypedDict(
    "ReplayTypeDef",
    {
        "ReplayName": NotRequired[str],
        "EventSourceArn": NotRequired[str],
        "State": NotRequired[ReplayStateType],
        "StateReason": NotRequired[str],
        "EventStartTime": NotRequired[datetime],
        "EventEndTime": NotRequired[datetime],
        "EventLastReplayedTime": NotRequired[datetime],
        "ReplayStartTime": NotRequired[datetime],
        "ReplayEndTime": NotRequired[datetime],
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
ListRuleNamesByTargetRequestRequestTypeDef = TypedDict(
    "ListRuleNamesByTargetRequestRequestTypeDef",
    {
        "TargetArn": str,
        "EventBusName": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "EventBusName": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "EventPattern": NotRequired[str],
        "State": NotRequired[RuleStateType],
        "Description": NotRequired[str],
        "ScheduleExpression": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ManagedBy": NotRequired[str],
        "EventBusName": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
ListTargetsByRuleRequestRequestTypeDef = TypedDict(
    "ListTargetsByRuleRequestRequestTypeDef",
    {
        "Rule": str,
        "EventBusName": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
PutEventsResultEntryTypeDef = TypedDict(
    "PutEventsResultEntryTypeDef",
    {
        "EventId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
PutPartnerEventsResultEntryTypeDef = TypedDict(
    "PutPartnerEventsResultEntryTypeDef",
    {
        "EventId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
PutTargetsResultEntryTypeDef = TypedDict(
    "PutTargetsResultEntryTypeDef",
    {
        "TargetId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
RedshiftDataParametersOutputTypeDef = TypedDict(
    "RedshiftDataParametersOutputTypeDef",
    {
        "Database": str,
        "SecretManagerArn": NotRequired[str],
        "DbUser": NotRequired[str],
        "Sql": NotRequired[str],
        "StatementName": NotRequired[str],
        "WithEvent": NotRequired[bool],
        "Sqls": NotRequired[List[str]],
    },
)
RedshiftDataParametersTypeDef = TypedDict(
    "RedshiftDataParametersTypeDef",
    {
        "Database": str,
        "SecretManagerArn": NotRequired[str],
        "DbUser": NotRequired[str],
        "Sql": NotRequired[str],
        "StatementName": NotRequired[str],
        "WithEvent": NotRequired[bool],
        "Sqls": NotRequired[Sequence[str]],
    },
)
RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "StatementId": NotRequired[str],
        "RemoveAllPermissions": NotRequired[bool],
        "EventBusName": NotRequired[str],
    },
)
RemoveTargetsRequestRequestTypeDef = TypedDict(
    "RemoveTargetsRequestRequestTypeDef",
    {
        "Rule": str,
        "Ids": Sequence[str],
        "EventBusName": NotRequired[str],
        "Force": NotRequired[bool],
    },
)
RemoveTargetsResultEntryTypeDef = TypedDict(
    "RemoveTargetsResultEntryTypeDef",
    {
        "TargetId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
ReplayDestinationTypeDef = TypedDict(
    "ReplayDestinationTypeDef",
    {
        "Arn": str,
        "FilterArns": NotRequired[Sequence[str]],
    },
)
RetryPolicyTypeDef = TypedDict(
    "RetryPolicyTypeDef",
    {
        "MaximumRetryAttempts": NotRequired[int],
        "MaximumEventAgeInSeconds": NotRequired[int],
    },
)
RunCommandTargetOutputTypeDef = TypedDict(
    "RunCommandTargetOutputTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)
RunCommandTargetTypeDef = TypedDict(
    "RunCommandTargetTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
)
SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
SqsParametersTypeDef = TypedDict(
    "SqsParametersTypeDef",
    {
        "MessageGroupId": NotRequired[str],
    },
)
TestEventPatternRequestRequestTypeDef = TypedDict(
    "TestEventPatternRequestRequestTypeDef",
    {
        "EventPattern": str,
        "Event": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateApiDestinationRequestRequestTypeDef = TypedDict(
    "UpdateApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "InvocationEndpoint": NotRequired[str],
        "HttpMethod": NotRequired[ApiDestinationHttpMethodType],
        "InvocationRateLimitPerSecond": NotRequired[int],
    },
)
UpdateArchiveRequestRequestTypeDef = TypedDict(
    "UpdateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
        "Description": NotRequired[str],
        "EventPattern": NotRequired[str],
        "RetentionDays": NotRequired[int],
    },
)
UpdateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": NotRequired[str],
        "ApiKeyValue": NotRequired[str],
    },
)
UpdateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
    },
)
UpdateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": NotRequired[str],
        "ClientSecret": NotRequired[str],
    },
)
NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "awsvpcConfiguration": NotRequired[AwsVpcConfigurationOutputTypeDef],
    },
)
AwsVpcConfigurationUnionTypeDef = Union[
    AwsVpcConfigurationTypeDef, AwsVpcConfigurationOutputTypeDef
]
BatchParametersTypeDef = TypedDict(
    "BatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": NotRequired[BatchArrayPropertiesTypeDef],
        "RetryStrategy": NotRequired[BatchRetryStrategyTypeDef],
    },
)
CancelReplayResponseTypeDef = TypedDict(
    "CancelReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApiDestinationResponseTypeDef = TypedDict(
    "CreateApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateArchiveResponseTypeDef = TypedDict(
    "CreateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePartnerEventSourceResponseTypeDef = TypedDict(
    "CreatePartnerEventSourceResponseTypeDef",
    {
        "EventSourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeauthorizeConnectionResponseTypeDef = TypedDict(
    "DeauthorizeConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeApiDestinationResponseTypeDef = TypedDict(
    "DescribeApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "Name": str,
        "Description": str,
        "ApiDestinationState": ApiDestinationStateType,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeArchiveResponseTypeDef = TypedDict(
    "DescribeArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "ArchiveName": str,
        "EventSourceArn": str,
        "Description": str,
        "EventPattern": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventSourceResponseTypeDef = TypedDict(
    "DescribeEventSourceResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": EventSourceStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePartnerEventSourceResponseTypeDef = TypedDict(
    "DescribePartnerEventSourceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRuleResponseTypeDef = TypedDict(
    "DescribeRuleResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": RuleStateType,
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
        "CreatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApiDestinationsResponseTypeDef = TypedDict(
    "ListApiDestinationsResponseTypeDef",
    {
        "ApiDestinations": List[ApiDestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListArchivesResponseTypeDef = TypedDict(
    "ListArchivesResponseTypeDef",
    {
        "Archives": List[ArchiveTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRuleNamesByTargetResponseTypeDef = TypedDict(
    "ListRuleNamesByTargetResponseTypeDef",
    {
        "RuleNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutRuleResponseTypeDef = TypedDict(
    "PutRuleResponseTypeDef",
    {
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReplayResponseTypeDef = TypedDict(
    "StartReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ReplayStartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestEventPatternResponseTypeDef = TypedDict(
    "TestEventPatternResponseTypeDef",
    {
        "Result": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApiDestinationResponseTypeDef = TypedDict(
    "UpdateApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateArchiveResponseTypeDef = TypedDict(
    "UpdateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConnectionResponseTypeDef = TypedDict(
    "UpdateConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPermissionRequestRequestTypeDef = TypedDict(
    "PutPermissionRequestRequestTypeDef",
    {
        "EventBusName": NotRequired[str],
        "Action": NotRequired[str],
        "Principal": NotRequired[str],
        "StatementId": NotRequired[str],
        "Condition": NotRequired[ConditionTypeDef],
        "Policy": NotRequired[str],
    },
)
ConnectionHttpParametersOutputTypeDef = TypedDict(
    "ConnectionHttpParametersOutputTypeDef",
    {
        "HeaderParameters": NotRequired[List[ConnectionHeaderParameterTypeDef]],
        "QueryStringParameters": NotRequired[List[ConnectionQueryStringParameterTypeDef]],
        "BodyParameters": NotRequired[List[ConnectionBodyParameterTypeDef]],
    },
)
ConnectionHttpParametersTypeDef = TypedDict(
    "ConnectionHttpParametersTypeDef",
    {
        "HeaderParameters": NotRequired[Sequence[ConnectionHeaderParameterTypeDef]],
        "QueryStringParameters": NotRequired[Sequence[ConnectionQueryStringParameterTypeDef]],
        "BodyParameters": NotRequired[Sequence[ConnectionBodyParameterTypeDef]],
    },
)
ListConnectionsResponseTypeDef = TypedDict(
    "ListConnectionsResponseTypeDef",
    {
        "Connections": List[ConnectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateEventBusResponseTypeDef = TypedDict(
    "CreateEventBusResponseTypeDef",
    {
        "EventBusArn": str,
        "Description": str,
        "KmsKeyIdentifier": str,
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventBusResponseTypeDef = TypedDict(
    "DescribeEventBusResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "KmsKeyIdentifier": str,
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "Policy": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEventBusRequestRequestTypeDef = TypedDict(
    "UpdateEventBusRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "KmsKeyIdentifier": NotRequired[str],
        "Description": NotRequired[str],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
    },
)
UpdateEventBusResponseTypeDef = TypedDict(
    "UpdateEventBusResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "KmsKeyIdentifier": str,
        "Description": str,
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventBusRequestRequestTypeDef = TypedDict(
    "CreateEventBusRequestRequestTypeDef",
    {
        "Name": str,
        "EventSourceName": NotRequired[str],
        "Description": NotRequired[str],
        "KmsKeyIdentifier": NotRequired[str],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRuleRequestRequestTypeDef = TypedDict(
    "PutRuleRequestRequestTypeDef",
    {
        "Name": str,
        "ScheduleExpression": NotRequired[str],
        "EventPattern": NotRequired[str],
        "State": NotRequired[RuleStateType],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "EventBusName": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
DescribeReplayResponseTypeDef = TypedDict(
    "DescribeReplayResponseTypeDef",
    {
        "ReplayName": str,
        "ReplayArn": str,
        "Description": str,
        "State": ReplayStateType,
        "StateReason": str,
        "EventSourceArn": str,
        "Destination": ReplayDestinationOutputTypeDef,
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventBusesResponseTypeDef = TypedDict(
    "ListEventBusesResponseTypeDef",
    {
        "EventBuses": List[EventBusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEventSourcesResponseTypeDef = TypedDict(
    "ListEventSourcesResponseTypeDef",
    {
        "EventSources": List[EventSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FailoverConfigTypeDef = TypedDict(
    "FailoverConfigTypeDef",
    {
        "Primary": PrimaryTypeDef,
        "Secondary": SecondaryTypeDef,
    },
)
HttpParametersUnionTypeDef = Union[HttpParametersTypeDef, HttpParametersOutputTypeDef]
InputTransformerUnionTypeDef = Union[InputTransformerTypeDef, InputTransformerOutputTypeDef]
ListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "ListPartnerEventSourceAccountsResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List[PartnerEventSourceAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPartnerEventSourcesResponseTypeDef = TypedDict(
    "ListPartnerEventSourcesResponseTypeDef",
    {
        "PartnerEventSources": List[PartnerEventSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListReplaysResponseTypeDef = TypedDict(
    "ListReplaysResponseTypeDef",
    {
        "Replays": List[ReplayTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef = TypedDict(
    "ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef",
    {
        "TargetArn": str,
        "EventBusName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "ListRulesRequestListRulesPaginateTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "EventBusName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTargetsByRuleRequestListTargetsByRulePaginateTypeDef = TypedDict(
    "ListTargetsByRuleRequestListTargetsByRulePaginateTypeDef",
    {
        "Rule": str,
        "EventBusName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutEventsRequestEntryTypeDef = TypedDict(
    "PutEventsRequestEntryTypeDef",
    {
        "Time": NotRequired[TimestampTypeDef],
        "Source": NotRequired[str],
        "Resources": NotRequired[Sequence[str]],
        "DetailType": NotRequired[str],
        "Detail": NotRequired[str],
        "EventBusName": NotRequired[str],
        "TraceHeader": NotRequired[str],
    },
)
PutPartnerEventsRequestEntryTypeDef = TypedDict(
    "PutPartnerEventsRequestEntryTypeDef",
    {
        "Time": NotRequired[TimestampTypeDef],
        "Source": NotRequired[str],
        "Resources": NotRequired[Sequence[str]],
        "DetailType": NotRequired[str],
        "Detail": NotRequired[str],
    },
)
PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List[PutEventsResultEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPartnerEventsResponseTypeDef = TypedDict(
    "PutPartnerEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List[PutPartnerEventsResultEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutTargetsResponseTypeDef = TypedDict(
    "PutTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[PutTargetsResultEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RedshiftDataParametersUnionTypeDef = Union[
    RedshiftDataParametersTypeDef, RedshiftDataParametersOutputTypeDef
]
RemoveTargetsResponseTypeDef = TypedDict(
    "RemoveTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[RemoveTargetsResultEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReplayRequestRequestTypeDef = TypedDict(
    "StartReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
        "EventSourceArn": str,
        "EventStartTime": TimestampTypeDef,
        "EventEndTime": TimestampTypeDef,
        "Destination": ReplayDestinationTypeDef,
        "Description": NotRequired[str],
    },
)
RunCommandParametersOutputTypeDef = TypedDict(
    "RunCommandParametersOutputTypeDef",
    {
        "RunCommandTargets": List[RunCommandTargetOutputTypeDef],
    },
)
RunCommandTargetUnionTypeDef = Union[RunCommandTargetTypeDef, RunCommandTargetOutputTypeDef]
SageMakerPipelineParametersOutputTypeDef = TypedDict(
    "SageMakerPipelineParametersOutputTypeDef",
    {
        "PipelineParameterList": NotRequired[List[SageMakerPipelineParameterTypeDef]],
    },
)
SageMakerPipelineParametersTypeDef = TypedDict(
    "SageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": NotRequired[Sequence[SageMakerPipelineParameterTypeDef]],
    },
)
EcsParametersOutputTypeDef = TypedDict(
    "EcsParametersOutputTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": NotRequired[int],
        "LaunchType": NotRequired[LaunchTypeType],
        "NetworkConfiguration": NotRequired[NetworkConfigurationOutputTypeDef],
        "PlatformVersion": NotRequired[str],
        "Group": NotRequired[str],
        "CapacityProviderStrategy": NotRequired[List[CapacityProviderStrategyItemTypeDef]],
        "EnableECSManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "PlacementConstraints": NotRequired[List[PlacementConstraintTypeDef]],
        "PlacementStrategy": NotRequired[List[PlacementStrategyTypeDef]],
        "PropagateTags": NotRequired[Literal["TASK_DEFINITION"]],
        "ReferenceId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": NotRequired[AwsVpcConfigurationUnionTypeDef],
    },
)
ConnectionOAuthResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthResponseParametersTypeDef",
    {
        "ClientParameters": NotRequired[ConnectionOAuthClientResponseParametersTypeDef],
        "AuthorizationEndpoint": NotRequired[str],
        "HttpMethod": NotRequired[ConnectionOAuthHttpMethodType],
        "OAuthHttpParameters": NotRequired[ConnectionHttpParametersOutputTypeDef],
    },
)
ConnectionHttpParametersUnionTypeDef = Union[
    ConnectionHttpParametersTypeDef, ConnectionHttpParametersOutputTypeDef
]
RoutingConfigTypeDef = TypedDict(
    "RoutingConfigTypeDef",
    {
        "FailoverConfig": FailoverConfigTypeDef,
    },
)
PutEventsRequestRequestTypeDef = TypedDict(
    "PutEventsRequestRequestTypeDef",
    {
        "Entries": Sequence[PutEventsRequestEntryTypeDef],
        "EndpointId": NotRequired[str],
    },
)
PutPartnerEventsRequestRequestTypeDef = TypedDict(
    "PutPartnerEventsRequestRequestTypeDef",
    {
        "Entries": Sequence[PutPartnerEventsRequestEntryTypeDef],
    },
)
RunCommandParametersTypeDef = TypedDict(
    "RunCommandParametersTypeDef",
    {
        "RunCommandTargets": Sequence[RunCommandTargetUnionTypeDef],
    },
)
SageMakerPipelineParametersUnionTypeDef = Union[
    SageMakerPipelineParametersTypeDef, SageMakerPipelineParametersOutputTypeDef
]
TargetOutputTypeDef = TypedDict(
    "TargetOutputTypeDef",
    {
        "Id": str,
        "Arn": str,
        "RoleArn": NotRequired[str],
        "Input": NotRequired[str],
        "InputPath": NotRequired[str],
        "InputTransformer": NotRequired[InputTransformerOutputTypeDef],
        "KinesisParameters": NotRequired[KinesisParametersTypeDef],
        "RunCommandParameters": NotRequired[RunCommandParametersOutputTypeDef],
        "EcsParameters": NotRequired[EcsParametersOutputTypeDef],
        "BatchParameters": NotRequired[BatchParametersTypeDef],
        "SqsParameters": NotRequired[SqsParametersTypeDef],
        "HttpParameters": NotRequired[HttpParametersOutputTypeDef],
        "RedshiftDataParameters": NotRequired[RedshiftDataParametersOutputTypeDef],
        "SageMakerPipelineParameters": NotRequired[SageMakerPipelineParametersOutputTypeDef],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "RetryPolicy": NotRequired[RetryPolicyTypeDef],
        "AppSyncParameters": NotRequired[AppSyncParametersTypeDef],
    },
)
NetworkConfigurationUnionTypeDef = Union[
    NetworkConfigurationTypeDef, NetworkConfigurationOutputTypeDef
]
ConnectionAuthResponseParametersTypeDef = TypedDict(
    "ConnectionAuthResponseParametersTypeDef",
    {
        "BasicAuthParameters": NotRequired[ConnectionBasicAuthResponseParametersTypeDef],
        "OAuthParameters": NotRequired[ConnectionOAuthResponseParametersTypeDef],
        "ApiKeyAuthParameters": NotRequired[ConnectionApiKeyAuthResponseParametersTypeDef],
        "InvocationHttpParameters": NotRequired[ConnectionHttpParametersOutputTypeDef],
    },
)
CreateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": CreateConnectionOAuthClientRequestParametersTypeDef,
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
        "OAuthHttpParameters": NotRequired[ConnectionHttpParametersUnionTypeDef],
    },
)
UpdateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": NotRequired[UpdateConnectionOAuthClientRequestParametersTypeDef],
        "AuthorizationEndpoint": NotRequired[str],
        "HttpMethod": NotRequired[ConnectionOAuthHttpMethodType],
        "OAuthHttpParameters": NotRequired[ConnectionHttpParametersUnionTypeDef],
    },
)
CreateEndpointRequestRequestTypeDef = TypedDict(
    "CreateEndpointRequestRequestTypeDef",
    {
        "Name": str,
        "RoutingConfig": RoutingConfigTypeDef,
        "EventBuses": Sequence[EndpointEventBusTypeDef],
        "Description": NotRequired[str],
        "ReplicationConfig": NotRequired[ReplicationConfigTypeDef],
        "RoleArn": NotRequired[str],
    },
)
CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "RoutingConfig": RoutingConfigTypeDef,
        "ReplicationConfig": ReplicationConfigTypeDef,
        "EventBuses": List[EndpointEventBusTypeDef],
        "RoleArn": str,
        "State": EndpointStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEndpointResponseTypeDef = TypedDict(
    "DescribeEndpointResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "RoutingConfig": RoutingConfigTypeDef,
        "ReplicationConfig": ReplicationConfigTypeDef,
        "EventBuses": List[EndpointEventBusTypeDef],
        "RoleArn": str,
        "EndpointId": str,
        "EndpointUrl": str,
        "State": EndpointStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Arn": NotRequired[str],
        "RoutingConfig": NotRequired[RoutingConfigTypeDef],
        "ReplicationConfig": NotRequired[ReplicationConfigTypeDef],
        "EventBuses": NotRequired[List[EndpointEventBusTypeDef]],
        "RoleArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "State": NotRequired[EndpointStateType],
        "StateReason": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)
UpdateEndpointRequestRequestTypeDef = TypedDict(
    "UpdateEndpointRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "RoutingConfig": NotRequired[RoutingConfigTypeDef],
        "ReplicationConfig": NotRequired[ReplicationConfigTypeDef],
        "EventBuses": NotRequired[Sequence[EndpointEventBusTypeDef]],
        "RoleArn": NotRequired[str],
    },
)
UpdateEndpointResponseTypeDef = TypedDict(
    "UpdateEndpointResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "RoutingConfig": RoutingConfigTypeDef,
        "ReplicationConfig": ReplicationConfigTypeDef,
        "EventBuses": List[EndpointEventBusTypeDef],
        "RoleArn": str,
        "EndpointId": str,
        "EndpointUrl": str,
        "State": EndpointStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RunCommandParametersUnionTypeDef = Union[
    RunCommandParametersTypeDef, RunCommandParametersOutputTypeDef
]
ListTargetsByRuleResponseTypeDef = TypedDict(
    "ListTargetsByRuleResponseTypeDef",
    {
        "Targets": List[TargetOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EcsParametersTypeDef = TypedDict(
    "EcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": NotRequired[int],
        "LaunchType": NotRequired[LaunchTypeType],
        "NetworkConfiguration": NotRequired[NetworkConfigurationUnionTypeDef],
        "PlatformVersion": NotRequired[str],
        "Group": NotRequired[str],
        "CapacityProviderStrategy": NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]],
        "EnableECSManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "PlacementConstraints": NotRequired[Sequence[PlacementConstraintTypeDef]],
        "PlacementStrategy": NotRequired[Sequence[PlacementStrategyTypeDef]],
        "PropagateTags": NotRequired[Literal["TASK_DEFINITION"]],
        "ReferenceId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeConnectionResponseTypeDef = TypedDict(
    "DescribeConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "Name": str,
        "Description": str,
        "ConnectionState": ConnectionStateType,
        "StateReason": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "SecretArn": str,
        "AuthParameters": ConnectionAuthResponseParametersTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectionAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": NotRequired[CreateConnectionBasicAuthRequestParametersTypeDef],
        "OAuthParameters": NotRequired[CreateConnectionOAuthRequestParametersTypeDef],
        "ApiKeyAuthParameters": NotRequired[CreateConnectionApiKeyAuthRequestParametersTypeDef],
        "InvocationHttpParameters": NotRequired[ConnectionHttpParametersUnionTypeDef],
    },
)
UpdateConnectionAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": NotRequired[UpdateConnectionBasicAuthRequestParametersTypeDef],
        "OAuthParameters": NotRequired[UpdateConnectionOAuthRequestParametersTypeDef],
        "ApiKeyAuthParameters": NotRequired[UpdateConnectionApiKeyAuthRequestParametersTypeDef],
        "InvocationHttpParameters": NotRequired[ConnectionHttpParametersUnionTypeDef],
    },
)
ListEndpointsResponseTypeDef = TypedDict(
    "ListEndpointsResponseTypeDef",
    {
        "Endpoints": List[EndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EcsParametersUnionTypeDef = Union[EcsParametersTypeDef, EcsParametersOutputTypeDef]
CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "AuthParameters": CreateConnectionAuthRequestParametersTypeDef,
        "Description": NotRequired[str],
    },
)
UpdateConnectionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "AuthorizationType": NotRequired[ConnectionAuthorizationTypeType],
        "AuthParameters": NotRequired[UpdateConnectionAuthRequestParametersTypeDef],
    },
)
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Id": str,
        "Arn": str,
        "RoleArn": NotRequired[str],
        "Input": NotRequired[str],
        "InputPath": NotRequired[str],
        "InputTransformer": NotRequired[InputTransformerUnionTypeDef],
        "KinesisParameters": NotRequired[KinesisParametersTypeDef],
        "RunCommandParameters": NotRequired[RunCommandParametersUnionTypeDef],
        "EcsParameters": NotRequired[EcsParametersUnionTypeDef],
        "BatchParameters": NotRequired[BatchParametersTypeDef],
        "SqsParameters": NotRequired[SqsParametersTypeDef],
        "HttpParameters": NotRequired[HttpParametersUnionTypeDef],
        "RedshiftDataParameters": NotRequired[RedshiftDataParametersUnionTypeDef],
        "SageMakerPipelineParameters": NotRequired[SageMakerPipelineParametersUnionTypeDef],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "RetryPolicy": NotRequired[RetryPolicyTypeDef],
        "AppSyncParameters": NotRequired[AppSyncParametersTypeDef],
    },
)
TargetUnionTypeDef = Union[TargetTypeDef, TargetOutputTypeDef]
PutTargetsRequestRequestTypeDef = TypedDict(
    "PutTargetsRequestRequestTypeDef",
    {
        "Rule": str,
        "Targets": Sequence[TargetUnionTypeDef],
        "EventBusName": NotRequired[str],
    },
)
