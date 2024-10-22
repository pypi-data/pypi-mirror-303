"""
Type annotations for shield service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/type_defs/)

Usage::

    ```python
    from mypy_boto3_shield.type_defs import ResponseActionOutputTypeDef

    data: ResponseActionOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    ApplicationLayerAutomaticResponseStatusType,
    AttackLayerType,
    AttackPropertyIdentifierType,
    AutoRenewType,
    ProactiveEngagementStatusType,
    ProtectedResourceTypeType,
    ProtectionGroupAggregationType,
    ProtectionGroupPatternType,
    SubResourceTypeType,
    SubscriptionStateType,
    UnitType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ResponseActionOutputTypeDef",
    "AssociateDRTLogBucketRequestRequestTypeDef",
    "AssociateDRTRoleRequestRequestTypeDef",
    "AssociateHealthCheckRequestRequestTypeDef",
    "EmergencyContactTypeDef",
    "MitigationTypeDef",
    "SummarizedCounterTypeDef",
    "ContributorTypeDef",
    "AttackVectorDescriptionTypeDef",
    "AttackVolumeStatisticsTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteProtectionGroupRequestRequestTypeDef",
    "DeleteProtectionRequestRequestTypeDef",
    "DescribeAttackRequestRequestTypeDef",
    "TimeRangeOutputTypeDef",
    "DescribeProtectionGroupRequestRequestTypeDef",
    "ProtectionGroupTypeDef",
    "DescribeProtectionRequestRequestTypeDef",
    "DisableApplicationLayerAutomaticResponseRequestRequestTypeDef",
    "DisassociateDRTLogBucketRequestRequestTypeDef",
    "DisassociateHealthCheckRequestRequestTypeDef",
    "ResponseActionTypeDef",
    "InclusionProtectionFiltersTypeDef",
    "InclusionProtectionGroupFiltersTypeDef",
    "LimitTypeDef",
    "PaginatorConfigTypeDef",
    "ListResourcesInProtectionGroupRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProtectionGroupRequestRequestTypeDef",
    "UpdateSubscriptionRequestRequestTypeDef",
    "ApplicationLayerAutomaticResponseConfigurationTypeDef",
    "AssociateProactiveEngagementDetailsRequestRequestTypeDef",
    "UpdateEmergencyContactSettingsRequestRequestTypeDef",
    "SummarizedAttackVectorTypeDef",
    "AttackPropertyTypeDef",
    "AttackSummaryTypeDef",
    "AttackVolumeTypeDef",
    "CreateProtectionGroupRequestRequestTypeDef",
    "CreateProtectionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateProtectionResponseTypeDef",
    "DescribeDRTAccessResponseTypeDef",
    "DescribeEmergencyContactSettingsResponseTypeDef",
    "GetSubscriptionStateResponseTypeDef",
    "ListResourcesInProtectionGroupResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "DescribeProtectionGroupResponseTypeDef",
    "ListProtectionGroupsResponseTypeDef",
    "EnableApplicationLayerAutomaticResponseRequestRequestTypeDef",
    "UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef",
    "ListProtectionsRequestRequestTypeDef",
    "ListProtectionGroupsRequestRequestTypeDef",
    "ProtectionLimitsTypeDef",
    "ListProtectionsRequestListProtectionsPaginateTypeDef",
    "ProtectionGroupPatternTypeLimitsTypeDef",
    "TimeRangeTypeDef",
    "ProtectionTypeDef",
    "SubResourceSummaryTypeDef",
    "ListAttacksResponseTypeDef",
    "AttackStatisticsDataItemTypeDef",
    "ProtectionGroupLimitsTypeDef",
    "ListAttacksRequestListAttacksPaginateTypeDef",
    "ListAttacksRequestRequestTypeDef",
    "DescribeProtectionResponseTypeDef",
    "ListProtectionsResponseTypeDef",
    "AttackDetailTypeDef",
    "DescribeAttackStatisticsResponseTypeDef",
    "SubscriptionLimitsTypeDef",
    "DescribeAttackResponseTypeDef",
    "SubscriptionTypeDef",
    "DescribeSubscriptionResponseTypeDef",
)

ResponseActionOutputTypeDef = TypedDict(
    "ResponseActionOutputTypeDef",
    {
        "Block": NotRequired[Dict[str, Any]],
        "Count": NotRequired[Dict[str, Any]],
    },
)
AssociateDRTLogBucketRequestRequestTypeDef = TypedDict(
    "AssociateDRTLogBucketRequestRequestTypeDef",
    {
        "LogBucket": str,
    },
)
AssociateDRTRoleRequestRequestTypeDef = TypedDict(
    "AssociateDRTRoleRequestRequestTypeDef",
    {
        "RoleArn": str,
    },
)
AssociateHealthCheckRequestRequestTypeDef = TypedDict(
    "AssociateHealthCheckRequestRequestTypeDef",
    {
        "ProtectionId": str,
        "HealthCheckArn": str,
    },
)
EmergencyContactTypeDef = TypedDict(
    "EmergencyContactTypeDef",
    {
        "EmailAddress": str,
        "PhoneNumber": NotRequired[str],
        "ContactNotes": NotRequired[str],
    },
)
MitigationTypeDef = TypedDict(
    "MitigationTypeDef",
    {
        "MitigationName": NotRequired[str],
    },
)
SummarizedCounterTypeDef = TypedDict(
    "SummarizedCounterTypeDef",
    {
        "Name": NotRequired[str],
        "Max": NotRequired[float],
        "Average": NotRequired[float],
        "Sum": NotRequired[float],
        "N": NotRequired[int],
        "Unit": NotRequired[str],
    },
)
ContributorTypeDef = TypedDict(
    "ContributorTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[int],
    },
)
AttackVectorDescriptionTypeDef = TypedDict(
    "AttackVectorDescriptionTypeDef",
    {
        "VectorType": str,
    },
)
AttackVolumeStatisticsTypeDef = TypedDict(
    "AttackVolumeStatisticsTypeDef",
    {
        "Max": float,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
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
DeleteProtectionGroupRequestRequestTypeDef = TypedDict(
    "DeleteProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)
DeleteProtectionRequestRequestTypeDef = TypedDict(
    "DeleteProtectionRequestRequestTypeDef",
    {
        "ProtectionId": str,
    },
)
DescribeAttackRequestRequestTypeDef = TypedDict(
    "DescribeAttackRequestRequestTypeDef",
    {
        "AttackId": str,
    },
)
TimeRangeOutputTypeDef = TypedDict(
    "TimeRangeOutputTypeDef",
    {
        "FromInclusive": NotRequired[datetime],
        "ToExclusive": NotRequired[datetime],
    },
)
DescribeProtectionGroupRequestRequestTypeDef = TypedDict(
    "DescribeProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)
ProtectionGroupTypeDef = TypedDict(
    "ProtectionGroupTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "Members": List[str],
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "ProtectionGroupArn": NotRequired[str],
    },
)
DescribeProtectionRequestRequestTypeDef = TypedDict(
    "DescribeProtectionRequestRequestTypeDef",
    {
        "ProtectionId": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)
DisableApplicationLayerAutomaticResponseRequestRequestTypeDef = TypedDict(
    "DisableApplicationLayerAutomaticResponseRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DisassociateDRTLogBucketRequestRequestTypeDef = TypedDict(
    "DisassociateDRTLogBucketRequestRequestTypeDef",
    {
        "LogBucket": str,
    },
)
DisassociateHealthCheckRequestRequestTypeDef = TypedDict(
    "DisassociateHealthCheckRequestRequestTypeDef",
    {
        "ProtectionId": str,
        "HealthCheckArn": str,
    },
)
ResponseActionTypeDef = TypedDict(
    "ResponseActionTypeDef",
    {
        "Block": NotRequired[Mapping[str, Any]],
        "Count": NotRequired[Mapping[str, Any]],
    },
)
InclusionProtectionFiltersTypeDef = TypedDict(
    "InclusionProtectionFiltersTypeDef",
    {
        "ResourceArns": NotRequired[Sequence[str]],
        "ProtectionNames": NotRequired[Sequence[str]],
        "ResourceTypes": NotRequired[Sequence[ProtectedResourceTypeType]],
    },
)
InclusionProtectionGroupFiltersTypeDef = TypedDict(
    "InclusionProtectionGroupFiltersTypeDef",
    {
        "ProtectionGroupIds": NotRequired[Sequence[str]],
        "Patterns": NotRequired[Sequence[ProtectionGroupPatternType]],
        "ResourceTypes": NotRequired[Sequence[ProtectedResourceTypeType]],
        "Aggregations": NotRequired[Sequence[ProtectionGroupAggregationType]],
    },
)
LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Type": NotRequired[str],
        "Max": NotRequired[int],
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
ListResourcesInProtectionGroupRequestRequestTypeDef = TypedDict(
    "ListResourcesInProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
ProtectionGroupArbitraryPatternLimitsTypeDef = TypedDict(
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    {
        "MaxMembers": int,
    },
)
TimestampTypeDef = Union[datetime, str]
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateProtectionGroupRequestRequestTypeDef = TypedDict(
    "UpdateProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "Members": NotRequired[Sequence[str]],
    },
)
UpdateSubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateSubscriptionRequestRequestTypeDef",
    {
        "AutoRenew": NotRequired[AutoRenewType],
    },
)
ApplicationLayerAutomaticResponseConfigurationTypeDef = TypedDict(
    "ApplicationLayerAutomaticResponseConfigurationTypeDef",
    {
        "Status": ApplicationLayerAutomaticResponseStatusType,
        "Action": ResponseActionOutputTypeDef,
    },
)
AssociateProactiveEngagementDetailsRequestRequestTypeDef = TypedDict(
    "AssociateProactiveEngagementDetailsRequestRequestTypeDef",
    {
        "EmergencyContactList": Sequence[EmergencyContactTypeDef],
    },
)
UpdateEmergencyContactSettingsRequestRequestTypeDef = TypedDict(
    "UpdateEmergencyContactSettingsRequestRequestTypeDef",
    {
        "EmergencyContactList": NotRequired[Sequence[EmergencyContactTypeDef]],
    },
)
SummarizedAttackVectorTypeDef = TypedDict(
    "SummarizedAttackVectorTypeDef",
    {
        "VectorType": str,
        "VectorCounters": NotRequired[List[SummarizedCounterTypeDef]],
    },
)
AttackPropertyTypeDef = TypedDict(
    "AttackPropertyTypeDef",
    {
        "AttackLayer": NotRequired[AttackLayerType],
        "AttackPropertyIdentifier": NotRequired[AttackPropertyIdentifierType],
        "TopContributors": NotRequired[List[ContributorTypeDef]],
        "Unit": NotRequired[UnitType],
        "Total": NotRequired[int],
    },
)
AttackSummaryTypeDef = TypedDict(
    "AttackSummaryTypeDef",
    {
        "AttackId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "AttackVectors": NotRequired[List[AttackVectorDescriptionTypeDef]],
    },
)
AttackVolumeTypeDef = TypedDict(
    "AttackVolumeTypeDef",
    {
        "BitsPerSecond": NotRequired[AttackVolumeStatisticsTypeDef],
        "PacketsPerSecond": NotRequired[AttackVolumeStatisticsTypeDef],
        "RequestsPerSecond": NotRequired[AttackVolumeStatisticsTypeDef],
    },
)
CreateProtectionGroupRequestRequestTypeDef = TypedDict(
    "CreateProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "Members": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateProtectionRequestRequestTypeDef = TypedDict(
    "CreateProtectionRequestRequestTypeDef",
    {
        "Name": str,
        "ResourceArn": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateProtectionResponseTypeDef = TypedDict(
    "CreateProtectionResponseTypeDef",
    {
        "ProtectionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDRTAccessResponseTypeDef = TypedDict(
    "DescribeDRTAccessResponseTypeDef",
    {
        "RoleArn": str,
        "LogBucketList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEmergencyContactSettingsResponseTypeDef = TypedDict(
    "DescribeEmergencyContactSettingsResponseTypeDef",
    {
        "EmergencyContactList": List[EmergencyContactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionStateResponseTypeDef = TypedDict(
    "GetSubscriptionStateResponseTypeDef",
    {
        "SubscriptionState": SubscriptionStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesInProtectionGroupResponseTypeDef = TypedDict(
    "ListResourcesInProtectionGroupResponseTypeDef",
    {
        "ResourceArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProtectionGroupResponseTypeDef = TypedDict(
    "DescribeProtectionGroupResponseTypeDef",
    {
        "ProtectionGroup": ProtectionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProtectionGroupsResponseTypeDef = TypedDict(
    "ListProtectionGroupsResponseTypeDef",
    {
        "ProtectionGroups": List[ProtectionGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EnableApplicationLayerAutomaticResponseRequestRequestTypeDef = TypedDict(
    "EnableApplicationLayerAutomaticResponseRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Action": ResponseActionTypeDef,
    },
)
UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef = TypedDict(
    "UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Action": ResponseActionTypeDef,
    },
)
ListProtectionsRequestRequestTypeDef = TypedDict(
    "ListProtectionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "InclusionFilters": NotRequired[InclusionProtectionFiltersTypeDef],
    },
)
ListProtectionGroupsRequestRequestTypeDef = TypedDict(
    "ListProtectionGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "InclusionFilters": NotRequired[InclusionProtectionGroupFiltersTypeDef],
    },
)
ProtectionLimitsTypeDef = TypedDict(
    "ProtectionLimitsTypeDef",
    {
        "ProtectedResourceTypeLimits": List[LimitTypeDef],
    },
)
ListProtectionsRequestListProtectionsPaginateTypeDef = TypedDict(
    "ListProtectionsRequestListProtectionsPaginateTypeDef",
    {
        "InclusionFilters": NotRequired[InclusionProtectionFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ProtectionGroupPatternTypeLimitsTypeDef = TypedDict(
    "ProtectionGroupPatternTypeLimitsTypeDef",
    {
        "ArbitraryPatternLimits": ProtectionGroupArbitraryPatternLimitsTypeDef,
    },
)
TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "FromInclusive": NotRequired[TimestampTypeDef],
        "ToExclusive": NotRequired[TimestampTypeDef],
    },
)
ProtectionTypeDef = TypedDict(
    "ProtectionTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "HealthCheckIds": NotRequired[List[str]],
        "ProtectionArn": NotRequired[str],
        "ApplicationLayerAutomaticResponseConfiguration": NotRequired[
            ApplicationLayerAutomaticResponseConfigurationTypeDef
        ],
    },
)
SubResourceSummaryTypeDef = TypedDict(
    "SubResourceSummaryTypeDef",
    {
        "Type": NotRequired[SubResourceTypeType],
        "Id": NotRequired[str],
        "AttackVectors": NotRequired[List[SummarizedAttackVectorTypeDef]],
        "Counters": NotRequired[List[SummarizedCounterTypeDef]],
    },
)
ListAttacksResponseTypeDef = TypedDict(
    "ListAttacksResponseTypeDef",
    {
        "AttackSummaries": List[AttackSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AttackStatisticsDataItemTypeDef = TypedDict(
    "AttackStatisticsDataItemTypeDef",
    {
        "AttackCount": int,
        "AttackVolume": NotRequired[AttackVolumeTypeDef],
    },
)
ProtectionGroupLimitsTypeDef = TypedDict(
    "ProtectionGroupLimitsTypeDef",
    {
        "MaxProtectionGroups": int,
        "PatternTypeLimits": ProtectionGroupPatternTypeLimitsTypeDef,
    },
)
ListAttacksRequestListAttacksPaginateTypeDef = TypedDict(
    "ListAttacksRequestListAttacksPaginateTypeDef",
    {
        "ResourceArns": NotRequired[Sequence[str]],
        "StartTime": NotRequired[TimeRangeTypeDef],
        "EndTime": NotRequired[TimeRangeTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttacksRequestRequestTypeDef = TypedDict(
    "ListAttacksRequestRequestTypeDef",
    {
        "ResourceArns": NotRequired[Sequence[str]],
        "StartTime": NotRequired[TimeRangeTypeDef],
        "EndTime": NotRequired[TimeRangeTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeProtectionResponseTypeDef = TypedDict(
    "DescribeProtectionResponseTypeDef",
    {
        "Protection": ProtectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProtectionsResponseTypeDef = TypedDict(
    "ListProtectionsResponseTypeDef",
    {
        "Protections": List[ProtectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AttackDetailTypeDef = TypedDict(
    "AttackDetailTypeDef",
    {
        "AttackId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "SubResources": NotRequired[List[SubResourceSummaryTypeDef]],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "AttackCounters": NotRequired[List[SummarizedCounterTypeDef]],
        "AttackProperties": NotRequired[List[AttackPropertyTypeDef]],
        "Mitigations": NotRequired[List[MitigationTypeDef]],
    },
)
DescribeAttackStatisticsResponseTypeDef = TypedDict(
    "DescribeAttackStatisticsResponseTypeDef",
    {
        "TimeRange": TimeRangeOutputTypeDef,
        "DataItems": List[AttackStatisticsDataItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionLimitsTypeDef = TypedDict(
    "SubscriptionLimitsTypeDef",
    {
        "ProtectionLimits": ProtectionLimitsTypeDef,
        "ProtectionGroupLimits": ProtectionGroupLimitsTypeDef,
    },
)
DescribeAttackResponseTypeDef = TypedDict(
    "DescribeAttackResponseTypeDef",
    {
        "Attack": AttackDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionLimits": SubscriptionLimitsTypeDef,
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TimeCommitmentInSeconds": NotRequired[int],
        "AutoRenew": NotRequired[AutoRenewType],
        "Limits": NotRequired[List[LimitTypeDef]],
        "ProactiveEngagementStatus": NotRequired[ProactiveEngagementStatusType],
        "SubscriptionArn": NotRequired[str],
    },
)
DescribeSubscriptionResponseTypeDef = TypedDict(
    "DescribeSubscriptionResponseTypeDef",
    {
        "Subscription": SubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
