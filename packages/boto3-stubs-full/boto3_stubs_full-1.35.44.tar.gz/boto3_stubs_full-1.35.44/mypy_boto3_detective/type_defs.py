"""
Type annotations for detective service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_detective/type_defs/)

Usage::

    ```python
    from mypy_boto3_detective.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    DatasourcePackageIngestStateType,
    DatasourcePackageType,
    EntityTypeType,
    FieldType,
    IndicatorTypeType,
    InvitationTypeType,
    MemberDisabledReasonType,
    MemberStatusType,
    SeverityType,
    SortOrderType,
    StateType,
    StatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceptInvitationRequestRequestTypeDef",
    "AccountTypeDef",
    "AdministratorTypeDef",
    "BatchGetGraphMemberDatasourcesRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UnprocessedAccountTypeDef",
    "BatchGetMembershipDatasourcesRequestRequestTypeDef",
    "UnprocessedGraphTypeDef",
    "CreateGraphRequestRequestTypeDef",
    "TimestampForCollectionTypeDef",
    "DatasourcePackageUsageInfoTypeDef",
    "TimestampTypeDef",
    "DeleteGraphRequestRequestTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    "DisassociateMembershipRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "StringFilterTypeDef",
    "FlaggedIpAddressDetailTypeDef",
    "GetInvestigationRequestRequestTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GraphTypeDef",
    "ImpossibleTravelDetailTypeDef",
    "NewAsoDetailTypeDef",
    "NewGeolocationDetailTypeDef",
    "NewUserAgentDetailTypeDef",
    "RelatedFindingDetailTypeDef",
    "RelatedFindingGroupDetailTypeDef",
    "TTPsObservedDetailTypeDef",
    "InvestigationDetailTypeDef",
    "ListDatasourcePackagesRequestRequestTypeDef",
    "ListGraphsRequestRequestTypeDef",
    "ListIndicatorsRequestRequestTypeDef",
    "SortCriteriaTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RejectInvitationRequestRequestTypeDef",
    "StartMonitoringMemberRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasourcePackagesRequestRequestTypeDef",
    "UpdateInvestigationStateRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateGraphResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetInvestigationResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartInvestigationResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "DatasourcePackageIngestDetailTypeDef",
    "MembershipDatasourcesTypeDef",
    "MemberDetailTypeDef",
    "DateFilterTypeDef",
    "StartInvestigationRequestRequestTypeDef",
    "ListGraphsResponseTypeDef",
    "IndicatorDetailTypeDef",
    "ListInvestigationsResponseTypeDef",
    "ListDatasourcePackagesResponseTypeDef",
    "BatchGetGraphMemberDatasourcesResponseTypeDef",
    "BatchGetMembershipDatasourcesResponseTypeDef",
    "CreateMembersResponseTypeDef",
    "GetMembersResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersResponseTypeDef",
    "FilterCriteriaTypeDef",
    "IndicatorTypeDef",
    "ListInvestigationsRequestRequestTypeDef",
    "ListIndicatorsResponseTypeDef",
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
    },
)
AdministratorTypeDef = TypedDict(
    "AdministratorTypeDef",
    {
        "AccountId": NotRequired[str],
        "GraphArn": NotRequired[str],
        "DelegationTime": NotRequired[datetime],
    },
)
BatchGetGraphMemberDatasourcesRequestRequestTypeDef = TypedDict(
    "BatchGetGraphMemberDatasourcesRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": Sequence[str],
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
UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
BatchGetMembershipDatasourcesRequestRequestTypeDef = TypedDict(
    "BatchGetMembershipDatasourcesRequestRequestTypeDef",
    {
        "GraphArns": Sequence[str],
    },
)
UnprocessedGraphTypeDef = TypedDict(
    "UnprocessedGraphTypeDef",
    {
        "GraphArn": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
CreateGraphRequestRequestTypeDef = TypedDict(
    "CreateGraphRequestRequestTypeDef",
    {
        "Tags": NotRequired[Mapping[str, str]],
    },
)
TimestampForCollectionTypeDef = TypedDict(
    "TimestampForCollectionTypeDef",
    {
        "Timestamp": NotRequired[datetime],
    },
)
DatasourcePackageUsageInfoTypeDef = TypedDict(
    "DatasourcePackageUsageInfoTypeDef",
    {
        "VolumeUsageInBytes": NotRequired[int],
        "VolumeUsageUpdateTime": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]
DeleteGraphRequestRequestTypeDef = TypedDict(
    "DeleteGraphRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": Sequence[str],
    },
)
DescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
DisassociateMembershipRequestRequestTypeDef = TypedDict(
    "DisassociateMembershipRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "Value": str,
    },
)
FlaggedIpAddressDetailTypeDef = TypedDict(
    "FlaggedIpAddressDetailTypeDef",
    {
        "IpAddress": NotRequired[str],
        "Reason": NotRequired[Literal["AWS_THREAT_INTELLIGENCE"]],
    },
)
GetInvestigationRequestRequestTypeDef = TypedDict(
    "GetInvestigationRequestRequestTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
    },
)
GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": Sequence[str],
    },
)
GraphTypeDef = TypedDict(
    "GraphTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
    },
)
ImpossibleTravelDetailTypeDef = TypedDict(
    "ImpossibleTravelDetailTypeDef",
    {
        "StartingIpAddress": NotRequired[str],
        "EndingIpAddress": NotRequired[str],
        "StartingLocation": NotRequired[str],
        "EndingLocation": NotRequired[str],
        "HourlyTimeDelta": NotRequired[int],
    },
)
NewAsoDetailTypeDef = TypedDict(
    "NewAsoDetailTypeDef",
    {
        "Aso": NotRequired[str],
        "IsNewForEntireAccount": NotRequired[bool],
    },
)
NewGeolocationDetailTypeDef = TypedDict(
    "NewGeolocationDetailTypeDef",
    {
        "Location": NotRequired[str],
        "IpAddress": NotRequired[str],
        "IsNewForEntireAccount": NotRequired[bool],
    },
)
NewUserAgentDetailTypeDef = TypedDict(
    "NewUserAgentDetailTypeDef",
    {
        "UserAgent": NotRequired[str],
        "IsNewForEntireAccount": NotRequired[bool],
    },
)
RelatedFindingDetailTypeDef = TypedDict(
    "RelatedFindingDetailTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)
RelatedFindingGroupDetailTypeDef = TypedDict(
    "RelatedFindingGroupDetailTypeDef",
    {
        "Id": NotRequired[str],
    },
)
TTPsObservedDetailTypeDef = TypedDict(
    "TTPsObservedDetailTypeDef",
    {
        "Tactic": NotRequired[str],
        "Technique": NotRequired[str],
        "Procedure": NotRequired[str],
        "IpAddress": NotRequired[str],
        "APIName": NotRequired[str],
        "APISuccessCount": NotRequired[int],
        "APIFailureCount": NotRequired[int],
    },
)
InvestigationDetailTypeDef = TypedDict(
    "InvestigationDetailTypeDef",
    {
        "InvestigationId": NotRequired[str],
        "Severity": NotRequired[SeverityType],
        "Status": NotRequired[StatusType],
        "State": NotRequired[StateType],
        "CreatedTime": NotRequired[datetime],
        "EntityArn": NotRequired[str],
        "EntityType": NotRequired[EntityTypeType],
    },
)
ListDatasourcePackagesRequestRequestTypeDef = TypedDict(
    "ListDatasourcePackagesRequestRequestTypeDef",
    {
        "GraphArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListGraphsRequestRequestTypeDef = TypedDict(
    "ListGraphsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIndicatorsRequestRequestTypeDef = TypedDict(
    "ListIndicatorsRequestRequestTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
        "IndicatorType": NotRequired[IndicatorTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "Field": NotRequired[FieldType],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
RejectInvitationRequestRequestTypeDef = TypedDict(
    "RejectInvitationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
StartMonitoringMemberRequestRequestTypeDef = TypedDict(
    "StartMonitoringMemberRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountId": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDatasourcePackagesRequestRequestTypeDef = TypedDict(
    "UpdateDatasourcePackagesRequestRequestTypeDef",
    {
        "GraphArn": str,
        "DatasourcePackages": Sequence[DatasourcePackageType],
    },
)
UpdateInvestigationStateRequestRequestTypeDef = TypedDict(
    "UpdateInvestigationStateRequestRequestTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
        "State": StateType,
    },
)
UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AutoEnable": NotRequired[bool],
    },
)
CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "Accounts": Sequence[AccountTypeDef],
        "Message": NotRequired[str],
        "DisableEmailNotification": NotRequired[bool],
    },
)
CreateGraphResponseTypeDef = TypedDict(
    "CreateGraphResponseTypeDef",
    {
        "GraphArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInvestigationResponseTypeDef = TypedDict(
    "GetInvestigationResponseTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
        "EntityArn": str,
        "EntityType": EntityTypeType,
        "CreatedTime": datetime,
        "ScopeStartTime": datetime,
        "ScopeEndTime": datetime,
        "Status": StatusType,
        "Severity": SeverityType,
        "State": StateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "Administrators": List[AdministratorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartInvestigationResponseTypeDef = TypedDict(
    "StartInvestigationResponseTypeDef",
    {
        "InvestigationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "AccountIds": List[str],
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasourcePackageIngestDetailTypeDef = TypedDict(
    "DatasourcePackageIngestDetailTypeDef",
    {
        "DatasourcePackageIngestState": NotRequired[DatasourcePackageIngestStateType],
        "LastIngestStateChange": NotRequired[
            Dict[DatasourcePackageIngestStateType, TimestampForCollectionTypeDef]
        ],
    },
)
MembershipDatasourcesTypeDef = TypedDict(
    "MembershipDatasourcesTypeDef",
    {
        "AccountId": NotRequired[str],
        "GraphArn": NotRequired[str],
        "DatasourcePackageIngestHistory": NotRequired[
            Dict[
                DatasourcePackageType,
                Dict[DatasourcePackageIngestStateType, TimestampForCollectionTypeDef],
            ]
        ],
    },
)
MemberDetailTypeDef = TypedDict(
    "MemberDetailTypeDef",
    {
        "AccountId": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "GraphArn": NotRequired[str],
        "MasterId": NotRequired[str],
        "AdministratorId": NotRequired[str],
        "Status": NotRequired[MemberStatusType],
        "DisabledReason": NotRequired[MemberDisabledReasonType],
        "InvitedTime": NotRequired[datetime],
        "UpdatedTime": NotRequired[datetime],
        "VolumeUsageInBytes": NotRequired[int],
        "VolumeUsageUpdatedTime": NotRequired[datetime],
        "PercentOfGraphUtilization": NotRequired[float],
        "PercentOfGraphUtilizationUpdatedTime": NotRequired[datetime],
        "InvitationType": NotRequired[InvitationTypeType],
        "VolumeUsageByDatasourcePackage": NotRequired[
            Dict[DatasourcePackageType, DatasourcePackageUsageInfoTypeDef]
        ],
        "DatasourcePackageIngestStates": NotRequired[
            Dict[DatasourcePackageType, DatasourcePackageIngestStateType]
        ],
    },
)
DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "StartInclusive": TimestampTypeDef,
        "EndInclusive": TimestampTypeDef,
    },
)
StartInvestigationRequestRequestTypeDef = TypedDict(
    "StartInvestigationRequestRequestTypeDef",
    {
        "GraphArn": str,
        "EntityArn": str,
        "ScopeStartTime": TimestampTypeDef,
        "ScopeEndTime": TimestampTypeDef,
    },
)
ListGraphsResponseTypeDef = TypedDict(
    "ListGraphsResponseTypeDef",
    {
        "GraphList": List[GraphTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
IndicatorDetailTypeDef = TypedDict(
    "IndicatorDetailTypeDef",
    {
        "TTPsObservedDetail": NotRequired[TTPsObservedDetailTypeDef],
        "ImpossibleTravelDetail": NotRequired[ImpossibleTravelDetailTypeDef],
        "FlaggedIpAddressDetail": NotRequired[FlaggedIpAddressDetailTypeDef],
        "NewGeolocationDetail": NotRequired[NewGeolocationDetailTypeDef],
        "NewAsoDetail": NotRequired[NewAsoDetailTypeDef],
        "NewUserAgentDetail": NotRequired[NewUserAgentDetailTypeDef],
        "RelatedFindingDetail": NotRequired[RelatedFindingDetailTypeDef],
        "RelatedFindingGroupDetail": NotRequired[RelatedFindingGroupDetailTypeDef],
    },
)
ListInvestigationsResponseTypeDef = TypedDict(
    "ListInvestigationsResponseTypeDef",
    {
        "InvestigationDetails": List[InvestigationDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDatasourcePackagesResponseTypeDef = TypedDict(
    "ListDatasourcePackagesResponseTypeDef",
    {
        "DatasourcePackages": Dict[DatasourcePackageType, DatasourcePackageIngestDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchGetGraphMemberDatasourcesResponseTypeDef = TypedDict(
    "BatchGetGraphMemberDatasourcesResponseTypeDef",
    {
        "MemberDatasources": List[MembershipDatasourcesTypeDef],
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetMembershipDatasourcesResponseTypeDef = TypedDict(
    "BatchGetMembershipDatasourcesResponseTypeDef",
    {
        "MembershipDatasources": List[MembershipDatasourcesTypeDef],
        "UnprocessedGraphs": List[UnprocessedGraphTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "Members": List[MemberDetailTypeDef],
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "MemberDetails": List[MemberDetailTypeDef],
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List[MemberDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "MemberDetails": List[MemberDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "Severity": NotRequired[StringFilterTypeDef],
        "Status": NotRequired[StringFilterTypeDef],
        "State": NotRequired[StringFilterTypeDef],
        "EntityArn": NotRequired[StringFilterTypeDef],
        "CreatedTime": NotRequired[DateFilterTypeDef],
    },
)
IndicatorTypeDef = TypedDict(
    "IndicatorTypeDef",
    {
        "IndicatorType": NotRequired[IndicatorTypeType],
        "IndicatorDetail": NotRequired[IndicatorDetailTypeDef],
    },
)
ListInvestigationsRequestRequestTypeDef = TypedDict(
    "ListInvestigationsRequestRequestTypeDef",
    {
        "GraphArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "FilterCriteria": NotRequired[FilterCriteriaTypeDef],
        "SortCriteria": NotRequired[SortCriteriaTypeDef],
    },
)
ListIndicatorsResponseTypeDef = TypedDict(
    "ListIndicatorsResponseTypeDef",
    {
        "GraphArn": str,
        "InvestigationId": str,
        "Indicators": List[IndicatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
