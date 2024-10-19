"""
Type annotations for organizations service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/type_defs/)

Usage::

    ```python
    from mypy_boto3_organizations.type_defs import AcceptHandshakeRequestRequestTypeDef

    data: AcceptHandshakeRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Sequence

from .literals import (
    AccountJoinedMethodType,
    AccountStatusType,
    ActionTypeType,
    ChildTypeType,
    CreateAccountFailureReasonType,
    CreateAccountStateType,
    EffectivePolicyTypeType,
    HandshakePartyTypeType,
    HandshakeResourceTypeType,
    HandshakeStateType,
    IAMUserAccessToBillingType,
    OrganizationFeatureSetType,
    ParentTypeType,
    PolicyTypeStatusType,
    PolicyTypeType,
    TargetTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptHandshakeRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AccountTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "CancelHandshakeRequestRequestTypeDef",
    "ChildTypeDef",
    "CloseAccountRequestRequestTypeDef",
    "TagTypeDef",
    "CreateAccountStatusTypeDef",
    "CreateOrganizationRequestRequestTypeDef",
    "OrganizationalUnitTypeDef",
    "DeclineHandshakeRequestRequestTypeDef",
    "DelegatedAdministratorTypeDef",
    "DelegatedServiceTypeDef",
    "DeleteOrganizationalUnitRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeregisterDelegatedAdministratorRequestRequestTypeDef",
    "DescribeAccountRequestRequestTypeDef",
    "DescribeCreateAccountStatusRequestRequestTypeDef",
    "DescribeEffectivePolicyRequestRequestTypeDef",
    "EffectivePolicyTypeDef",
    "DescribeHandshakeRequestRequestTypeDef",
    "DescribeOrganizationalUnitRequestRequestTypeDef",
    "DescribePolicyRequestRequestTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "DisableAWSServiceAccessRequestRequestTypeDef",
    "DisablePolicyTypeRequestRequestTypeDef",
    "EnableAWSServiceAccessRequestRequestTypeDef",
    "EnablePolicyTypeRequestRequestTypeDef",
    "EnabledServicePrincipalTypeDef",
    "HandshakeFilterTypeDef",
    "HandshakePartyTypeDef",
    "HandshakeResourcePaginatorTypeDef",
    "HandshakeResourceTypeDef",
    "PaginatorConfigTypeDef",
    "ListAWSServiceAccessForOrganizationRequestRequestTypeDef",
    "ListAccountsForParentRequestRequestTypeDef",
    "ListAccountsRequestRequestTypeDef",
    "ListChildrenRequestRequestTypeDef",
    "ListCreateAccountStatusRequestRequestTypeDef",
    "ListDelegatedAdministratorsRequestRequestTypeDef",
    "ListDelegatedServicesForAccountRequestRequestTypeDef",
    "ListOrganizationalUnitsForParentRequestRequestTypeDef",
    "ListParentsRequestRequestTypeDef",
    "ParentTypeDef",
    "ListPoliciesForTargetRequestRequestTypeDef",
    "PolicySummaryTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListRootsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTargetsForPolicyRequestRequestTypeDef",
    "PolicyTargetSummaryTypeDef",
    "MoveAccountRequestRequestTypeDef",
    "PolicyTypeSummaryTypeDef",
    "RegisterDelegatedAdministratorRequestRequestTypeDef",
    "RemoveAccountFromOrganizationRequestRequestTypeDef",
    "ResourcePolicySummaryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateOrganizationalUnitRequestRequestTypeDef",
    "UpdatePolicyRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "DescribeAccountResponseTypeDef",
    "ListAccountsForParentResponseTypeDef",
    "ListAccountsResponseTypeDef",
    "ListChildrenResponseTypeDef",
    "CreateAccountRequestRequestTypeDef",
    "CreateGovCloudAccountRequestRequestTypeDef",
    "CreateOrganizationalUnitRequestRequestTypeDef",
    "CreatePolicyRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateGovCloudAccountResponseTypeDef",
    "DescribeCreateAccountStatusResponseTypeDef",
    "ListCreateAccountStatusResponseTypeDef",
    "CreateOrganizationalUnitResponseTypeDef",
    "DescribeOrganizationalUnitResponseTypeDef",
    "ListOrganizationalUnitsForParentResponseTypeDef",
    "UpdateOrganizationalUnitResponseTypeDef",
    "ListDelegatedAdministratorsResponseTypeDef",
    "ListDelegatedServicesForAccountResponseTypeDef",
    "DescribeEffectivePolicyResponseTypeDef",
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    "ListHandshakesForAccountRequestRequestTypeDef",
    "ListHandshakesForOrganizationRequestRequestTypeDef",
    "InviteAccountToOrganizationRequestRequestTypeDef",
    "HandshakePaginatorTypeDef",
    "HandshakeTypeDef",
    "ListAWSServiceAccessForOrganizationRequestListAWSServiceAccessForOrganizationPaginateTypeDef",
    "ListAccountsForParentRequestListAccountsForParentPaginateTypeDef",
    "ListAccountsRequestListAccountsPaginateTypeDef",
    "ListChildrenRequestListChildrenPaginateTypeDef",
    "ListCreateAccountStatusRequestListCreateAccountStatusPaginateTypeDef",
    "ListDelegatedAdministratorsRequestListDelegatedAdministratorsPaginateTypeDef",
    "ListDelegatedServicesForAccountRequestListDelegatedServicesForAccountPaginateTypeDef",
    "ListHandshakesForAccountRequestListHandshakesForAccountPaginateTypeDef",
    "ListHandshakesForOrganizationRequestListHandshakesForOrganizationPaginateTypeDef",
    "ListOrganizationalUnitsForParentRequestListOrganizationalUnitsForParentPaginateTypeDef",
    "ListParentsRequestListParentsPaginateTypeDef",
    "ListPoliciesForTargetRequestListPoliciesForTargetPaginateTypeDef",
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    "ListRootsRequestListRootsPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef",
    "ListParentsResponseTypeDef",
    "ListPoliciesForTargetResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "PolicyTypeDef",
    "ListTargetsForPolicyResponseTypeDef",
    "OrganizationTypeDef",
    "RootTypeDef",
    "ResourcePolicyTypeDef",
    "ListHandshakesForAccountResponsePaginatorTypeDef",
    "ListHandshakesForOrganizationResponsePaginatorTypeDef",
    "AcceptHandshakeResponseTypeDef",
    "CancelHandshakeResponseTypeDef",
    "DeclineHandshakeResponseTypeDef",
    "DescribeHandshakeResponseTypeDef",
    "EnableAllFeaturesResponseTypeDef",
    "InviteAccountToOrganizationResponseTypeDef",
    "ListHandshakesForAccountResponseTypeDef",
    "ListHandshakesForOrganizationResponseTypeDef",
    "CreatePolicyResponseTypeDef",
    "DescribePolicyResponseTypeDef",
    "UpdatePolicyResponseTypeDef",
    "CreateOrganizationResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DisablePolicyTypeResponseTypeDef",
    "EnablePolicyTypeResponseTypeDef",
    "ListRootsResponseTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
)

AcceptHandshakeRequestRequestTypeDef = TypedDict(
    "AcceptHandshakeRequestRequestTypeDef",
    {
        "HandshakeId": str,
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
AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[AccountStatusType],
        "JoinedMethod": NotRequired[AccountJoinedMethodType],
        "JoinedTimestamp": NotRequired[datetime],
    },
)
AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "TargetId": str,
    },
)
CancelHandshakeRequestRequestTypeDef = TypedDict(
    "CancelHandshakeRequestRequestTypeDef",
    {
        "HandshakeId": str,
    },
)
ChildTypeDef = TypedDict(
    "ChildTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[ChildTypeType],
    },
)
CloseAccountRequestRequestTypeDef = TypedDict(
    "CloseAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreateAccountStatusTypeDef = TypedDict(
    "CreateAccountStatusTypeDef",
    {
        "Id": NotRequired[str],
        "AccountName": NotRequired[str],
        "State": NotRequired[CreateAccountStateType],
        "RequestedTimestamp": NotRequired[datetime],
        "CompletedTimestamp": NotRequired[datetime],
        "AccountId": NotRequired[str],
        "GovCloudAccountId": NotRequired[str],
        "FailureReason": NotRequired[CreateAccountFailureReasonType],
    },
)
CreateOrganizationRequestRequestTypeDef = TypedDict(
    "CreateOrganizationRequestRequestTypeDef",
    {
        "FeatureSet": NotRequired[OrganizationFeatureSetType],
    },
)
OrganizationalUnitTypeDef = TypedDict(
    "OrganizationalUnitTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DeclineHandshakeRequestRequestTypeDef = TypedDict(
    "DeclineHandshakeRequestRequestTypeDef",
    {
        "HandshakeId": str,
    },
)
DelegatedAdministratorTypeDef = TypedDict(
    "DelegatedAdministratorTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[AccountStatusType],
        "JoinedMethod": NotRequired[AccountJoinedMethodType],
        "JoinedTimestamp": NotRequired[datetime],
        "DelegationEnabledDate": NotRequired[datetime],
    },
)
DelegatedServiceTypeDef = TypedDict(
    "DelegatedServiceTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "DelegationEnabledDate": NotRequired[datetime],
    },
)
DeleteOrganizationalUnitRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationalUnitRequestRequestTypeDef",
    {
        "OrganizationalUnitId": str,
    },
)
DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
DeregisterDelegatedAdministratorRequestRequestTypeDef = TypedDict(
    "DeregisterDelegatedAdministratorRequestRequestTypeDef",
    {
        "AccountId": str,
        "ServicePrincipal": str,
    },
)
DescribeAccountRequestRequestTypeDef = TypedDict(
    "DescribeAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
DescribeCreateAccountStatusRequestRequestTypeDef = TypedDict(
    "DescribeCreateAccountStatusRequestRequestTypeDef",
    {
        "CreateAccountRequestId": str,
    },
)
DescribeEffectivePolicyRequestRequestTypeDef = TypedDict(
    "DescribeEffectivePolicyRequestRequestTypeDef",
    {
        "PolicyType": EffectivePolicyTypeType,
        "TargetId": NotRequired[str],
    },
)
EffectivePolicyTypeDef = TypedDict(
    "EffectivePolicyTypeDef",
    {
        "PolicyContent": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "TargetId": NotRequired[str],
        "PolicyType": NotRequired[EffectivePolicyTypeType],
    },
)
DescribeHandshakeRequestRequestTypeDef = TypedDict(
    "DescribeHandshakeRequestRequestTypeDef",
    {
        "HandshakeId": str,
    },
)
DescribeOrganizationalUnitRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationalUnitRequestRequestTypeDef",
    {
        "OrganizationalUnitId": str,
    },
)
DescribePolicyRequestRequestTypeDef = TypedDict(
    "DescribePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "TargetId": str,
    },
)
DisableAWSServiceAccessRequestRequestTypeDef = TypedDict(
    "DisableAWSServiceAccessRequestRequestTypeDef",
    {
        "ServicePrincipal": str,
    },
)
DisablePolicyTypeRequestRequestTypeDef = TypedDict(
    "DisablePolicyTypeRequestRequestTypeDef",
    {
        "RootId": str,
        "PolicyType": PolicyTypeType,
    },
)
EnableAWSServiceAccessRequestRequestTypeDef = TypedDict(
    "EnableAWSServiceAccessRequestRequestTypeDef",
    {
        "ServicePrincipal": str,
    },
)
EnablePolicyTypeRequestRequestTypeDef = TypedDict(
    "EnablePolicyTypeRequestRequestTypeDef",
    {
        "RootId": str,
        "PolicyType": PolicyTypeType,
    },
)
EnabledServicePrincipalTypeDef = TypedDict(
    "EnabledServicePrincipalTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "DateEnabled": NotRequired[datetime],
    },
)
HandshakeFilterTypeDef = TypedDict(
    "HandshakeFilterTypeDef",
    {
        "ActionType": NotRequired[ActionTypeType],
        "ParentHandshakeId": NotRequired[str],
    },
)
HandshakePartyTypeDef = TypedDict(
    "HandshakePartyTypeDef",
    {
        "Id": str,
        "Type": HandshakePartyTypeType,
    },
)
HandshakeResourcePaginatorTypeDef = TypedDict(
    "HandshakeResourcePaginatorTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[HandshakeResourceTypeType],
        "Resources": NotRequired[List[Dict[str, Any]]],
    },
)
HandshakeResourceTypeDef = TypedDict(
    "HandshakeResourceTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[HandshakeResourceTypeType],
        "Resources": NotRequired[List[Dict[str, Any]]],
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
ListAWSServiceAccessForOrganizationRequestRequestTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAccountsForParentRequestRequestTypeDef = TypedDict(
    "ListAccountsForParentRequestRequestTypeDef",
    {
        "ParentId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAccountsRequestRequestTypeDef = TypedDict(
    "ListAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListChildrenRequestRequestTypeDef = TypedDict(
    "ListChildrenRequestRequestTypeDef",
    {
        "ParentId": str,
        "ChildType": ChildTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCreateAccountStatusRequestRequestTypeDef = TypedDict(
    "ListCreateAccountStatusRequestRequestTypeDef",
    {
        "States": NotRequired[Sequence[CreateAccountStateType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDelegatedAdministratorsRequestRequestTypeDef = TypedDict(
    "ListDelegatedAdministratorsRequestRequestTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDelegatedServicesForAccountRequestRequestTypeDef = TypedDict(
    "ListDelegatedServicesForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListOrganizationalUnitsForParentRequestRequestTypeDef = TypedDict(
    "ListOrganizationalUnitsForParentRequestRequestTypeDef",
    {
        "ParentId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListParentsRequestRequestTypeDef = TypedDict(
    "ListParentsRequestRequestTypeDef",
    {
        "ChildId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[ParentTypeType],
    },
)
ListPoliciesForTargetRequestRequestTypeDef = TypedDict(
    "ListPoliciesForTargetRequestRequestTypeDef",
    {
        "TargetId": str,
        "Filter": PolicyTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[PolicyTypeType],
        "AwsManaged": NotRequired[bool],
    },
)
ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "Filter": PolicyTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRootsRequestRequestTypeDef = TypedDict(
    "ListRootsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
    },
)
ListTargetsForPolicyRequestRequestTypeDef = TypedDict(
    "ListTargetsForPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PolicyTargetSummaryTypeDef = TypedDict(
    "PolicyTargetSummaryTypeDef",
    {
        "TargetId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[TargetTypeType],
    },
)
MoveAccountRequestRequestTypeDef = TypedDict(
    "MoveAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "SourceParentId": str,
        "DestinationParentId": str,
    },
)
PolicyTypeSummaryTypeDef = TypedDict(
    "PolicyTypeSummaryTypeDef",
    {
        "Type": NotRequired[PolicyTypeType],
        "Status": NotRequired[PolicyTypeStatusType],
    },
)
RegisterDelegatedAdministratorRequestRequestTypeDef = TypedDict(
    "RegisterDelegatedAdministratorRequestRequestTypeDef",
    {
        "AccountId": str,
        "ServicePrincipal": str,
    },
)
RemoveAccountFromOrganizationRequestRequestTypeDef = TypedDict(
    "RemoveAccountFromOrganizationRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
ResourcePolicySummaryTypeDef = TypedDict(
    "ResourcePolicySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)
UpdateOrganizationalUnitRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationalUnitRequestRequestTypeDef",
    {
        "OrganizationalUnitId": str,
        "Name": NotRequired[str],
    },
)
UpdatePolicyRequestRequestTypeDef = TypedDict(
    "UpdatePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Content": NotRequired[str],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountResponseTypeDef = TypedDict(
    "DescribeAccountResponseTypeDef",
    {
        "Account": AccountTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountsForParentResponseTypeDef = TypedDict(
    "ListAccountsForParentResponseTypeDef",
    {
        "Accounts": List[AccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {
        "Accounts": List[AccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListChildrenResponseTypeDef = TypedDict(
    "ListChildrenResponseTypeDef",
    {
        "Children": List[ChildTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateAccountRequestRequestTypeDef = TypedDict(
    "CreateAccountRequestRequestTypeDef",
    {
        "Email": str,
        "AccountName": str,
        "RoleName": NotRequired[str],
        "IamUserAccessToBilling": NotRequired[IAMUserAccessToBillingType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateGovCloudAccountRequestRequestTypeDef = TypedDict(
    "CreateGovCloudAccountRequestRequestTypeDef",
    {
        "Email": str,
        "AccountName": str,
        "RoleName": NotRequired[str],
        "IamUserAccessToBilling": NotRequired[IAMUserAccessToBillingType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateOrganizationalUnitRequestRequestTypeDef = TypedDict(
    "CreateOrganizationalUnitRequestRequestTypeDef",
    {
        "ParentId": str,
        "Name": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreatePolicyRequestRequestTypeDef = TypedDict(
    "CreatePolicyRequestRequestTypeDef",
    {
        "Content": str,
        "Description": str,
        "Name": str,
        "Type": PolicyTypeType,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "Content": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateAccountResponseTypeDef = TypedDict(
    "CreateAccountResponseTypeDef",
    {
        "CreateAccountStatus": CreateAccountStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGovCloudAccountResponseTypeDef = TypedDict(
    "CreateGovCloudAccountResponseTypeDef",
    {
        "CreateAccountStatus": CreateAccountStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCreateAccountStatusResponseTypeDef = TypedDict(
    "DescribeCreateAccountStatusResponseTypeDef",
    {
        "CreateAccountStatus": CreateAccountStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCreateAccountStatusResponseTypeDef = TypedDict(
    "ListCreateAccountStatusResponseTypeDef",
    {
        "CreateAccountStatuses": List[CreateAccountStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateOrganizationalUnitResponseTypeDef = TypedDict(
    "CreateOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": OrganizationalUnitTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationalUnitResponseTypeDef = TypedDict(
    "DescribeOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": OrganizationalUnitTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationalUnitsForParentResponseTypeDef = TypedDict(
    "ListOrganizationalUnitsForParentResponseTypeDef",
    {
        "OrganizationalUnits": List[OrganizationalUnitTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateOrganizationalUnitResponseTypeDef = TypedDict(
    "UpdateOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": OrganizationalUnitTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDelegatedAdministratorsResponseTypeDef = TypedDict(
    "ListDelegatedAdministratorsResponseTypeDef",
    {
        "DelegatedAdministrators": List[DelegatedAdministratorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDelegatedServicesForAccountResponseTypeDef = TypedDict(
    "ListDelegatedServicesForAccountResponseTypeDef",
    {
        "DelegatedServices": List[DelegatedServiceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeEffectivePolicyResponseTypeDef = TypedDict(
    "DescribeEffectivePolicyResponseTypeDef",
    {
        "EffectivePolicy": EffectivePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAWSServiceAccessForOrganizationResponseTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    {
        "EnabledServicePrincipals": List[EnabledServicePrincipalTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListHandshakesForAccountRequestRequestTypeDef = TypedDict(
    "ListHandshakesForAccountRequestRequestTypeDef",
    {
        "Filter": NotRequired[HandshakeFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListHandshakesForOrganizationRequestRequestTypeDef = TypedDict(
    "ListHandshakesForOrganizationRequestRequestTypeDef",
    {
        "Filter": NotRequired[HandshakeFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
InviteAccountToOrganizationRequestRequestTypeDef = TypedDict(
    "InviteAccountToOrganizationRequestRequestTypeDef",
    {
        "Target": HandshakePartyTypeDef,
        "Notes": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
HandshakePaginatorTypeDef = TypedDict(
    "HandshakePaginatorTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Parties": NotRequired[List[HandshakePartyTypeDef]],
        "State": NotRequired[HandshakeStateType],
        "RequestedTimestamp": NotRequired[datetime],
        "ExpirationTimestamp": NotRequired[datetime],
        "Action": NotRequired[ActionTypeType],
        "Resources": NotRequired[List[HandshakeResourcePaginatorTypeDef]],
    },
)
HandshakeTypeDef = TypedDict(
    "HandshakeTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Parties": NotRequired[List[HandshakePartyTypeDef]],
        "State": NotRequired[HandshakeStateType],
        "RequestedTimestamp": NotRequired[datetime],
        "ExpirationTimestamp": NotRequired[datetime],
        "Action": NotRequired[ActionTypeType],
        "Resources": NotRequired[List[HandshakeResourceTypeDef]],
    },
)
ListAWSServiceAccessForOrganizationRequestListAWSServiceAccessForOrganizationPaginateTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationRequestListAWSServiceAccessForOrganizationPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountsForParentRequestListAccountsForParentPaginateTypeDef = TypedDict(
    "ListAccountsForParentRequestListAccountsForParentPaginateTypeDef",
    {
        "ParentId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountsRequestListAccountsPaginateTypeDef = TypedDict(
    "ListAccountsRequestListAccountsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListChildrenRequestListChildrenPaginateTypeDef = TypedDict(
    "ListChildrenRequestListChildrenPaginateTypeDef",
    {
        "ParentId": str,
        "ChildType": ChildTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCreateAccountStatusRequestListCreateAccountStatusPaginateTypeDef = TypedDict(
    "ListCreateAccountStatusRequestListCreateAccountStatusPaginateTypeDef",
    {
        "States": NotRequired[Sequence[CreateAccountStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDelegatedAdministratorsRequestListDelegatedAdministratorsPaginateTypeDef = TypedDict(
    "ListDelegatedAdministratorsRequestListDelegatedAdministratorsPaginateTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDelegatedServicesForAccountRequestListDelegatedServicesForAccountPaginateTypeDef = TypedDict(
    "ListDelegatedServicesForAccountRequestListDelegatedServicesForAccountPaginateTypeDef",
    {
        "AccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHandshakesForAccountRequestListHandshakesForAccountPaginateTypeDef = TypedDict(
    "ListHandshakesForAccountRequestListHandshakesForAccountPaginateTypeDef",
    {
        "Filter": NotRequired[HandshakeFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHandshakesForOrganizationRequestListHandshakesForOrganizationPaginateTypeDef = TypedDict(
    "ListHandshakesForOrganizationRequestListHandshakesForOrganizationPaginateTypeDef",
    {
        "Filter": NotRequired[HandshakeFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationalUnitsForParentRequestListOrganizationalUnitsForParentPaginateTypeDef = TypedDict(
    "ListOrganizationalUnitsForParentRequestListOrganizationalUnitsForParentPaginateTypeDef",
    {
        "ParentId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListParentsRequestListParentsPaginateTypeDef = TypedDict(
    "ListParentsRequestListParentsPaginateTypeDef",
    {
        "ChildId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoliciesForTargetRequestListPoliciesForTargetPaginateTypeDef = TypedDict(
    "ListPoliciesForTargetRequestListPoliciesForTargetPaginateTypeDef",
    {
        "TargetId": str,
        "Filter": PolicyTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoliciesRequestListPoliciesPaginateTypeDef = TypedDict(
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    {
        "Filter": PolicyTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRootsRequestListRootsPaginateTypeDef = TypedDict(
    "ListRootsRequestListRootsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef = TypedDict(
    "ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef",
    {
        "PolicyId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListParentsResponseTypeDef = TypedDict(
    "ListParentsResponseTypeDef",
    {
        "Parents": List[ParentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPoliciesForTargetResponseTypeDef = TypedDict(
    "ListPoliciesForTargetResponseTypeDef",
    {
        "Policies": List[PolicySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "Policies": List[PolicySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicySummary": NotRequired[PolicySummaryTypeDef],
        "Content": NotRequired[str],
    },
)
ListTargetsForPolicyResponseTypeDef = TypedDict(
    "ListTargetsForPolicyResponseTypeDef",
    {
        "Targets": List[PolicyTargetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
OrganizationTypeDef = TypedDict(
    "OrganizationTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "FeatureSet": NotRequired[OrganizationFeatureSetType],
        "MasterAccountArn": NotRequired[str],
        "MasterAccountId": NotRequired[str],
        "MasterAccountEmail": NotRequired[str],
        "AvailablePolicyTypes": NotRequired[List[PolicyTypeSummaryTypeDef]],
    },
)
RootTypeDef = TypedDict(
    "RootTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "PolicyTypes": NotRequired[List[PolicyTypeSummaryTypeDef]],
    },
)
ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "ResourcePolicySummary": NotRequired[ResourcePolicySummaryTypeDef],
        "Content": NotRequired[str],
    },
)
ListHandshakesForAccountResponsePaginatorTypeDef = TypedDict(
    "ListHandshakesForAccountResponsePaginatorTypeDef",
    {
        "Handshakes": List[HandshakePaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListHandshakesForOrganizationResponsePaginatorTypeDef = TypedDict(
    "ListHandshakesForOrganizationResponsePaginatorTypeDef",
    {
        "Handshakes": List[HandshakePaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AcceptHandshakeResponseTypeDef = TypedDict(
    "AcceptHandshakeResponseTypeDef",
    {
        "Handshake": HandshakeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelHandshakeResponseTypeDef = TypedDict(
    "CancelHandshakeResponseTypeDef",
    {
        "Handshake": HandshakeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeclineHandshakeResponseTypeDef = TypedDict(
    "DeclineHandshakeResponseTypeDef",
    {
        "Handshake": HandshakeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHandshakeResponseTypeDef = TypedDict(
    "DescribeHandshakeResponseTypeDef",
    {
        "Handshake": HandshakeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableAllFeaturesResponseTypeDef = TypedDict(
    "EnableAllFeaturesResponseTypeDef",
    {
        "Handshake": HandshakeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InviteAccountToOrganizationResponseTypeDef = TypedDict(
    "InviteAccountToOrganizationResponseTypeDef",
    {
        "Handshake": HandshakeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHandshakesForAccountResponseTypeDef = TypedDict(
    "ListHandshakesForAccountResponseTypeDef",
    {
        "Handshakes": List[HandshakeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListHandshakesForOrganizationResponseTypeDef = TypedDict(
    "ListHandshakesForOrganizationResponseTypeDef",
    {
        "Handshakes": List[HandshakeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreatePolicyResponseTypeDef = TypedDict(
    "CreatePolicyResponseTypeDef",
    {
        "Policy": PolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePolicyResponseTypeDef = TypedDict(
    "DescribePolicyResponseTypeDef",
    {
        "Policy": PolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePolicyResponseTypeDef = TypedDict(
    "UpdatePolicyResponseTypeDef",
    {
        "Policy": PolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOrganizationResponseTypeDef = TypedDict(
    "CreateOrganizationResponseTypeDef",
    {
        "Organization": OrganizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationResponseTypeDef = TypedDict(
    "DescribeOrganizationResponseTypeDef",
    {
        "Organization": OrganizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisablePolicyTypeResponseTypeDef = TypedDict(
    "DisablePolicyTypeResponseTypeDef",
    {
        "Root": RootTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnablePolicyTypeResponseTypeDef = TypedDict(
    "EnablePolicyTypeResponseTypeDef",
    {
        "Root": RootTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRootsResponseTypeDef = TypedDict(
    "ListRootsResponseTypeDef",
    {
        "Roots": List[RootTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "ResourcePolicy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "ResourcePolicy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
