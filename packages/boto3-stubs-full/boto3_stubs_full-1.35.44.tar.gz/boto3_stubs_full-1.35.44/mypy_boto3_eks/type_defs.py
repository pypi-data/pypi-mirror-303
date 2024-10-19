"""
Type annotations for eks service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/type_defs/)

Usage::

    ```python
    from mypy_boto3_eks.type_defs import AccessConfigResponseTypeDef

    data: AccessConfigResponseTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AccessScopeTypeType,
    AddonIssueCodeType,
    AddonStatusType,
    AMITypesType,
    AuthenticationModeType,
    CapacityTypesType,
    ClusterIssueCodeType,
    ClusterStatusType,
    ConfigStatusType,
    ConnectorConfigProviderType,
    EksAnywhereSubscriptionStatusType,
    ErrorCodeType,
    FargateProfileIssueCodeType,
    FargateProfileStatusType,
    InsightStatusValueType,
    IpFamilyType,
    LogTypeType,
    NodegroupIssueCodeType,
    NodegroupStatusType,
    ResolveConflictsType,
    SupportTypeType,
    TaintEffectType,
    UpdateParamTypeType,
    UpdateStatusType,
    UpdateTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AccessConfigResponseTypeDef",
    "AccessEntryTypeDef",
    "AccessPolicyTypeDef",
    "AccessScopeOutputTypeDef",
    "AccessScopeTypeDef",
    "AddonIssueTypeDef",
    "MarketplaceInformationTypeDef",
    "AddonPodIdentityAssociationsTypeDef",
    "AddonPodIdentityConfigurationTypeDef",
    "CompatibilityTypeDef",
    "ResponseMetadataTypeDef",
    "OidcIdentityProviderConfigRequestTypeDef",
    "AutoScalingGroupTypeDef",
    "CertificateTypeDef",
    "ClientStatTypeDef",
    "ClusterIssueTypeDef",
    "ConnectorConfigResponseTypeDef",
    "KubernetesNetworkConfigResponseTypeDef",
    "UpgradePolicyResponseTypeDef",
    "VpcConfigResponseTypeDef",
    "ConnectorConfigRequestTypeDef",
    "ControlPlanePlacementRequestTypeDef",
    "ControlPlanePlacementResponseTypeDef",
    "CreateAccessConfigRequestTypeDef",
    "CreateAccessEntryRequestRequestTypeDef",
    "KubernetesNetworkConfigRequestTypeDef",
    "UpgradePolicyRequestTypeDef",
    "VpcConfigRequestTypeDef",
    "EksAnywhereSubscriptionTermTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "NodegroupScalingConfigTypeDef",
    "NodegroupUpdateConfigTypeDef",
    "RemoteAccessConfigTypeDef",
    "TaintTypeDef",
    "CreatePodIdentityAssociationRequestRequestTypeDef",
    "PodIdentityAssociationTypeDef",
    "DeleteAccessEntryRequestRequestTypeDef",
    "DeleteAddonRequestRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteEksAnywhereSubscriptionRequestRequestTypeDef",
    "DeleteFargateProfileRequestRequestTypeDef",
    "DeleteNodegroupRequestRequestTypeDef",
    "DeletePodIdentityAssociationRequestRequestTypeDef",
    "DeregisterClusterRequestRequestTypeDef",
    "DescribeAccessEntryRequestRequestTypeDef",
    "DescribeAddonConfigurationRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeAddonRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAddonVersionsRequestRequestTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeEksAnywhereSubscriptionRequestRequestTypeDef",
    "DescribeFargateProfileRequestRequestTypeDef",
    "IdentityProviderConfigTypeDef",
    "DescribeInsightRequestRequestTypeDef",
    "DescribeNodegroupRequestRequestTypeDef",
    "DescribePodIdentityAssociationRequestRequestTypeDef",
    "DescribeUpdateRequestRequestTypeDef",
    "DisassociateAccessPolicyRequestRequestTypeDef",
    "ProviderTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileIssueTypeDef",
    "FargateProfileSelectorOutputTypeDef",
    "FargateProfileSelectorTypeDef",
    "OidcIdentityProviderConfigTypeDef",
    "OIDCTypeDef",
    "InsightStatusTypeDef",
    "InsightsFilterTypeDef",
    "IssueTypeDef",
    "ListAccessEntriesRequestRequestTypeDef",
    "ListAccessPoliciesRequestRequestTypeDef",
    "ListAddonsRequestRequestTypeDef",
    "ListAssociatedAccessPoliciesRequestRequestTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListEksAnywhereSubscriptionsRequestRequestTypeDef",
    "ListFargateProfilesRequestRequestTypeDef",
    "ListIdentityProviderConfigsRequestRequestTypeDef",
    "ListNodegroupsRequestRequestTypeDef",
    "ListPodIdentityAssociationsRequestRequestTypeDef",
    "PodIdentityAssociationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListUpdatesRequestRequestTypeDef",
    "LogSetupOutputTypeDef",
    "LogSetupTypeDef",
    "RemoteAccessConfigOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessConfigRequestTypeDef",
    "UpdateAccessEntryRequestRequestTypeDef",
    "UpdateClusterVersionRequestRequestTypeDef",
    "UpdateEksAnywhereSubscriptionRequestRequestTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateParamTypeDef",
    "UpdatePodIdentityAssociationRequestRequestTypeDef",
    "AssociatedAccessPolicyTypeDef",
    "AssociateAccessPolicyRequestRequestTypeDef",
    "AddonHealthTypeDef",
    "CreateAddonRequestRequestTypeDef",
    "UpdateAddonRequestRequestTypeDef",
    "AddonVersionInfoTypeDef",
    "CreateAccessEntryResponseTypeDef",
    "DescribeAccessEntryResponseTypeDef",
    "DescribeAddonConfigurationResponseTypeDef",
    "ListAccessEntriesResponseTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListAddonsResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUpdatesResponseTypeDef",
    "UpdateAccessEntryResponseTypeDef",
    "AssociateIdentityProviderConfigRequestRequestTypeDef",
    "NodegroupResourcesTypeDef",
    "DeprecationDetailTypeDef",
    "ClusterHealthTypeDef",
    "RegisterClusterRequestRequestTypeDef",
    "OutpostConfigRequestTypeDef",
    "OutpostConfigResponseTypeDef",
    "CreateEksAnywhereSubscriptionRequestRequestTypeDef",
    "EksAnywhereSubscriptionTypeDef",
    "UpdateNodegroupVersionRequestRequestTypeDef",
    "CreateNodegroupRequestRequestTypeDef",
    "UpdateTaintsPayloadTypeDef",
    "CreatePodIdentityAssociationResponseTypeDef",
    "DeletePodIdentityAssociationResponseTypeDef",
    "DescribePodIdentityAssociationResponseTypeDef",
    "UpdatePodIdentityAssociationResponseTypeDef",
    "DescribeAddonRequestAddonActiveWaitTypeDef",
    "DescribeAddonRequestAddonDeletedWaitTypeDef",
    "DescribeClusterRequestClusterActiveWaitTypeDef",
    "DescribeClusterRequestClusterDeletedWaitTypeDef",
    "DescribeFargateProfileRequestFargateProfileActiveWaitTypeDef",
    "DescribeFargateProfileRequestFargateProfileDeletedWaitTypeDef",
    "DescribeNodegroupRequestNodegroupActiveWaitTypeDef",
    "DescribeNodegroupRequestNodegroupDeletedWaitTypeDef",
    "DescribeAddonVersionsRequestDescribeAddonVersionsPaginateTypeDef",
    "ListAccessEntriesRequestListAccessEntriesPaginateTypeDef",
    "ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef",
    "ListAddonsRequestListAddonsPaginateTypeDef",
    "ListAssociatedAccessPoliciesRequestListAssociatedAccessPoliciesPaginateTypeDef",
    "ListClustersRequestListClustersPaginateTypeDef",
    "ListEksAnywhereSubscriptionsRequestListEksAnywhereSubscriptionsPaginateTypeDef",
    "ListFargateProfilesRequestListFargateProfilesPaginateTypeDef",
    "ListIdentityProviderConfigsRequestListIdentityProviderConfigsPaginateTypeDef",
    "ListNodegroupsRequestListNodegroupsPaginateTypeDef",
    "ListPodIdentityAssociationsRequestListPodIdentityAssociationsPaginateTypeDef",
    "ListUpdatesRequestListUpdatesPaginateTypeDef",
    "DescribeIdentityProviderConfigRequestRequestTypeDef",
    "DisassociateIdentityProviderConfigRequestRequestTypeDef",
    "ListIdentityProviderConfigsResponseTypeDef",
    "EncryptionConfigOutputTypeDef",
    "EncryptionConfigTypeDef",
    "FargateProfileHealthTypeDef",
    "FargateProfileSelectorUnionTypeDef",
    "IdentityProviderConfigResponseTypeDef",
    "IdentityTypeDef",
    "InsightResourceDetailTypeDef",
    "InsightSummaryTypeDef",
    "ListInsightsRequestListInsightsPaginateTypeDef",
    "ListInsightsRequestRequestTypeDef",
    "NodegroupHealthTypeDef",
    "ListPodIdentityAssociationsResponseTypeDef",
    "LoggingOutputTypeDef",
    "LogSetupUnionTypeDef",
    "UpdateTypeDef",
    "AssociateAccessPolicyResponseTypeDef",
    "ListAssociatedAccessPoliciesResponseTypeDef",
    "AddonTypeDef",
    "AddonInfoTypeDef",
    "InsightCategorySpecificSummaryTypeDef",
    "CreateEksAnywhereSubscriptionResponseTypeDef",
    "DeleteEksAnywhereSubscriptionResponseTypeDef",
    "DescribeEksAnywhereSubscriptionResponseTypeDef",
    "ListEksAnywhereSubscriptionsResponseTypeDef",
    "UpdateEksAnywhereSubscriptionResponseTypeDef",
    "UpdateNodegroupConfigRequestRequestTypeDef",
    "EncryptionConfigUnionTypeDef",
    "FargateProfileTypeDef",
    "CreateFargateProfileRequestRequestTypeDef",
    "DescribeIdentityProviderConfigResponseTypeDef",
    "ListInsightsResponseTypeDef",
    "NodegroupTypeDef",
    "ClusterTypeDef",
    "LoggingTypeDef",
    "AssociateEncryptionConfigResponseTypeDef",
    "AssociateIdentityProviderConfigResponseTypeDef",
    "DescribeUpdateResponseTypeDef",
    "DisassociateIdentityProviderConfigResponseTypeDef",
    "UpdateAddonResponseTypeDef",
    "UpdateClusterConfigResponseTypeDef",
    "UpdateClusterVersionResponseTypeDef",
    "UpdateNodegroupConfigResponseTypeDef",
    "UpdateNodegroupVersionResponseTypeDef",
    "CreateAddonResponseTypeDef",
    "DeleteAddonResponseTypeDef",
    "DescribeAddonResponseTypeDef",
    "DescribeAddonVersionsResponseTypeDef",
    "InsightTypeDef",
    "AssociateEncryptionConfigRequestRequestTypeDef",
    "CreateFargateProfileResponseTypeDef",
    "DeleteFargateProfileResponseTypeDef",
    "DescribeFargateProfileResponseTypeDef",
    "CreateNodegroupResponseTypeDef",
    "DeleteNodegroupResponseTypeDef",
    "DescribeNodegroupResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeregisterClusterResponseTypeDef",
    "DescribeClusterResponseTypeDef",
    "RegisterClusterResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "UpdateClusterConfigRequestRequestTypeDef",
    "DescribeInsightResponseTypeDef",
)

AccessConfigResponseTypeDef = TypedDict(
    "AccessConfigResponseTypeDef",
    {
        "bootstrapClusterCreatorAdminPermissions": NotRequired[bool],
        "authenticationMode": NotRequired[AuthenticationModeType],
    },
)
AccessEntryTypeDef = TypedDict(
    "AccessEntryTypeDef",
    {
        "clusterName": NotRequired[str],
        "principalArn": NotRequired[str],
        "kubernetesGroups": NotRequired[List[str]],
        "accessEntryArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "username": NotRequired[str],
        "type": NotRequired[str],
    },
)
AccessPolicyTypeDef = TypedDict(
    "AccessPolicyTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
    },
)
AccessScopeOutputTypeDef = TypedDict(
    "AccessScopeOutputTypeDef",
    {
        "type": NotRequired[AccessScopeTypeType],
        "namespaces": NotRequired[List[str]],
    },
)
AccessScopeTypeDef = TypedDict(
    "AccessScopeTypeDef",
    {
        "type": NotRequired[AccessScopeTypeType],
        "namespaces": NotRequired[Sequence[str]],
    },
)
AddonIssueTypeDef = TypedDict(
    "AddonIssueTypeDef",
    {
        "code": NotRequired[AddonIssueCodeType],
        "message": NotRequired[str],
        "resourceIds": NotRequired[List[str]],
    },
)
MarketplaceInformationTypeDef = TypedDict(
    "MarketplaceInformationTypeDef",
    {
        "productId": NotRequired[str],
        "productUrl": NotRequired[str],
    },
)
AddonPodIdentityAssociationsTypeDef = TypedDict(
    "AddonPodIdentityAssociationsTypeDef",
    {
        "serviceAccount": str,
        "roleArn": str,
    },
)
AddonPodIdentityConfigurationTypeDef = TypedDict(
    "AddonPodIdentityConfigurationTypeDef",
    {
        "serviceAccount": NotRequired[str],
        "recommendedManagedPolicies": NotRequired[List[str]],
    },
)
CompatibilityTypeDef = TypedDict(
    "CompatibilityTypeDef",
    {
        "clusterVersion": NotRequired[str],
        "platformVersions": NotRequired[List[str]],
        "defaultVersion": NotRequired[bool],
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
OidcIdentityProviderConfigRequestTypeDef = TypedDict(
    "OidcIdentityProviderConfigRequestTypeDef",
    {
        "identityProviderConfigName": str,
        "issuerUrl": str,
        "clientId": str,
        "usernameClaim": NotRequired[str],
        "usernamePrefix": NotRequired[str],
        "groupsClaim": NotRequired[str],
        "groupsPrefix": NotRequired[str],
        "requiredClaims": NotRequired[Mapping[str, str]],
    },
)
AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "name": NotRequired[str],
    },
)
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "data": NotRequired[str],
    },
)
ClientStatTypeDef = TypedDict(
    "ClientStatTypeDef",
    {
        "userAgent": NotRequired[str],
        "numberOfRequestsLast30Days": NotRequired[int],
        "lastRequestTime": NotRequired[datetime],
    },
)
ClusterIssueTypeDef = TypedDict(
    "ClusterIssueTypeDef",
    {
        "code": NotRequired[ClusterIssueCodeType],
        "message": NotRequired[str],
        "resourceIds": NotRequired[List[str]],
    },
)
ConnectorConfigResponseTypeDef = TypedDict(
    "ConnectorConfigResponseTypeDef",
    {
        "activationId": NotRequired[str],
        "activationCode": NotRequired[str],
        "activationExpiry": NotRequired[datetime],
        "provider": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
KubernetesNetworkConfigResponseTypeDef = TypedDict(
    "KubernetesNetworkConfigResponseTypeDef",
    {
        "serviceIpv4Cidr": NotRequired[str],
        "serviceIpv6Cidr": NotRequired[str],
        "ipFamily": NotRequired[IpFamilyType],
    },
)
UpgradePolicyResponseTypeDef = TypedDict(
    "UpgradePolicyResponseTypeDef",
    {
        "supportType": NotRequired[SupportTypeType],
    },
)
VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "subnetIds": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
        "clusterSecurityGroupId": NotRequired[str],
        "vpcId": NotRequired[str],
        "endpointPublicAccess": NotRequired[bool],
        "endpointPrivateAccess": NotRequired[bool],
        "publicAccessCidrs": NotRequired[List[str]],
    },
)
ConnectorConfigRequestTypeDef = TypedDict(
    "ConnectorConfigRequestTypeDef",
    {
        "roleArn": str,
        "provider": ConnectorConfigProviderType,
    },
)
ControlPlanePlacementRequestTypeDef = TypedDict(
    "ControlPlanePlacementRequestTypeDef",
    {
        "groupName": NotRequired[str],
    },
)
ControlPlanePlacementResponseTypeDef = TypedDict(
    "ControlPlanePlacementResponseTypeDef",
    {
        "groupName": NotRequired[str],
    },
)
CreateAccessConfigRequestTypeDef = TypedDict(
    "CreateAccessConfigRequestTypeDef",
    {
        "bootstrapClusterCreatorAdminPermissions": NotRequired[bool],
        "authenticationMode": NotRequired[AuthenticationModeType],
    },
)
CreateAccessEntryRequestRequestTypeDef = TypedDict(
    "CreateAccessEntryRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "kubernetesGroups": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
        "clientRequestToken": NotRequired[str],
        "username": NotRequired[str],
        "type": NotRequired[str],
    },
)
KubernetesNetworkConfigRequestTypeDef = TypedDict(
    "KubernetesNetworkConfigRequestTypeDef",
    {
        "serviceIpv4Cidr": NotRequired[str],
        "ipFamily": NotRequired[IpFamilyType],
    },
)
UpgradePolicyRequestTypeDef = TypedDict(
    "UpgradePolicyRequestTypeDef",
    {
        "supportType": NotRequired[SupportTypeType],
    },
)
VpcConfigRequestTypeDef = TypedDict(
    "VpcConfigRequestTypeDef",
    {
        "subnetIds": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "endpointPublicAccess": NotRequired[bool],
        "endpointPrivateAccess": NotRequired[bool],
        "publicAccessCidrs": NotRequired[Sequence[str]],
    },
)
EksAnywhereSubscriptionTermTypeDef = TypedDict(
    "EksAnywhereSubscriptionTermTypeDef",
    {
        "duration": NotRequired[int],
        "unit": NotRequired[Literal["MONTHS"]],
    },
)
LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "name": NotRequired[str],
        "version": NotRequired[str],
        "id": NotRequired[str],
    },
)
NodegroupScalingConfigTypeDef = TypedDict(
    "NodegroupScalingConfigTypeDef",
    {
        "minSize": NotRequired[int],
        "maxSize": NotRequired[int],
        "desiredSize": NotRequired[int],
    },
)
NodegroupUpdateConfigTypeDef = TypedDict(
    "NodegroupUpdateConfigTypeDef",
    {
        "maxUnavailable": NotRequired[int],
        "maxUnavailablePercentage": NotRequired[int],
    },
)
RemoteAccessConfigTypeDef = TypedDict(
    "RemoteAccessConfigTypeDef",
    {
        "ec2SshKey": NotRequired[str],
        "sourceSecurityGroups": NotRequired[Sequence[str]],
    },
)
TaintTypeDef = TypedDict(
    "TaintTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
        "effect": NotRequired[TaintEffectType],
    },
)
CreatePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "CreatePodIdentityAssociationRequestRequestTypeDef",
    {
        "clusterName": str,
        "namespace": str,
        "serviceAccount": str,
        "roleArn": str,
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
PodIdentityAssociationTypeDef = TypedDict(
    "PodIdentityAssociationTypeDef",
    {
        "clusterName": NotRequired[str],
        "namespace": NotRequired[str],
        "serviceAccount": NotRequired[str],
        "roleArn": NotRequired[str],
        "associationArn": NotRequired[str],
        "associationId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "ownerArn": NotRequired[str],
    },
)
DeleteAccessEntryRequestRequestTypeDef = TypedDict(
    "DeleteAccessEntryRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
    },
)
DeleteAddonRequestRequestTypeDef = TypedDict(
    "DeleteAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
        "preserve": NotRequired[bool],
    },
)
DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteFargateProfileRequestRequestTypeDef = TypedDict(
    "DeleteFargateProfileRequestRequestTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
    },
)
DeleteNodegroupRequestRequestTypeDef = TypedDict(
    "DeleteNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)
DeletePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "DeletePodIdentityAssociationRequestRequestTypeDef",
    {
        "clusterName": str,
        "associationId": str,
    },
)
DeregisterClusterRequestRequestTypeDef = TypedDict(
    "DeregisterClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)
DescribeAccessEntryRequestRequestTypeDef = TypedDict(
    "DescribeAccessEntryRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
    },
)
DescribeAddonConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAddonConfigurationRequestRequestTypeDef",
    {
        "addonName": str,
        "addonVersion": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeAddonRequestRequestTypeDef = TypedDict(
    "DescribeAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
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
DescribeAddonVersionsRequestRequestTypeDef = TypedDict(
    "DescribeAddonVersionsRequestRequestTypeDef",
    {
        "kubernetesVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "addonName": NotRequired[str],
        "types": NotRequired[Sequence[str]],
        "publishers": NotRequired[Sequence[str]],
        "owners": NotRequired[Sequence[str]],
    },
)
DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)
DescribeEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "DescribeEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "id": str,
    },
)
DescribeFargateProfileRequestRequestTypeDef = TypedDict(
    "DescribeFargateProfileRequestRequestTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
    },
)
IdentityProviderConfigTypeDef = TypedDict(
    "IdentityProviderConfigTypeDef",
    {
        "type": str,
        "name": str,
    },
)
DescribeInsightRequestRequestTypeDef = TypedDict(
    "DescribeInsightRequestRequestTypeDef",
    {
        "clusterName": str,
        "id": str,
    },
)
DescribeNodegroupRequestRequestTypeDef = TypedDict(
    "DescribeNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)
DescribePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "DescribePodIdentityAssociationRequestRequestTypeDef",
    {
        "clusterName": str,
        "associationId": str,
    },
)
DescribeUpdateRequestRequestTypeDef = TypedDict(
    "DescribeUpdateRequestRequestTypeDef",
    {
        "name": str,
        "updateId": str,
        "nodegroupName": NotRequired[str],
        "addonName": NotRequired[str],
    },
)
DisassociateAccessPolicyRequestRequestTypeDef = TypedDict(
    "DisassociateAccessPolicyRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "policyArn": str,
    },
)
ProviderTypeDef = TypedDict(
    "ProviderTypeDef",
    {
        "keyArn": NotRequired[str],
    },
)
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
        "resourceIds": NotRequired[List[str]],
    },
)
FargateProfileIssueTypeDef = TypedDict(
    "FargateProfileIssueTypeDef",
    {
        "code": NotRequired[FargateProfileIssueCodeType],
        "message": NotRequired[str],
        "resourceIds": NotRequired[List[str]],
    },
)
FargateProfileSelectorOutputTypeDef = TypedDict(
    "FargateProfileSelectorOutputTypeDef",
    {
        "namespace": NotRequired[str],
        "labels": NotRequired[Dict[str, str]],
    },
)
FargateProfileSelectorTypeDef = TypedDict(
    "FargateProfileSelectorTypeDef",
    {
        "namespace": NotRequired[str],
        "labels": NotRequired[Mapping[str, str]],
    },
)
OidcIdentityProviderConfigTypeDef = TypedDict(
    "OidcIdentityProviderConfigTypeDef",
    {
        "identityProviderConfigName": NotRequired[str],
        "identityProviderConfigArn": NotRequired[str],
        "clusterName": NotRequired[str],
        "issuerUrl": NotRequired[str],
        "clientId": NotRequired[str],
        "usernameClaim": NotRequired[str],
        "usernamePrefix": NotRequired[str],
        "groupsClaim": NotRequired[str],
        "groupsPrefix": NotRequired[str],
        "requiredClaims": NotRequired[Dict[str, str]],
        "tags": NotRequired[Dict[str, str]],
        "status": NotRequired[ConfigStatusType],
    },
)
OIDCTypeDef = TypedDict(
    "OIDCTypeDef",
    {
        "issuer": NotRequired[str],
    },
)
InsightStatusTypeDef = TypedDict(
    "InsightStatusTypeDef",
    {
        "status": NotRequired[InsightStatusValueType],
        "reason": NotRequired[str],
    },
)
InsightsFilterTypeDef = TypedDict(
    "InsightsFilterTypeDef",
    {
        "categories": NotRequired[Sequence[Literal["UPGRADE_READINESS"]]],
        "kubernetesVersions": NotRequired[Sequence[str]],
        "statuses": NotRequired[Sequence[InsightStatusValueType]],
    },
)
IssueTypeDef = TypedDict(
    "IssueTypeDef",
    {
        "code": NotRequired[NodegroupIssueCodeType],
        "message": NotRequired[str],
        "resourceIds": NotRequired[List[str]],
    },
)
ListAccessEntriesRequestRequestTypeDef = TypedDict(
    "ListAccessEntriesRequestRequestTypeDef",
    {
        "clusterName": str,
        "associatedPolicyArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAccessPoliciesRequestRequestTypeDef = TypedDict(
    "ListAccessPoliciesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAddonsRequestRequestTypeDef = TypedDict(
    "ListAddonsRequestRequestTypeDef",
    {
        "clusterName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAssociatedAccessPoliciesRequestRequestTypeDef = TypedDict(
    "ListAssociatedAccessPoliciesRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "include": NotRequired[Sequence[str]],
    },
)
ListEksAnywhereSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListEksAnywhereSubscriptionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "includeStatus": NotRequired[Sequence[EksAnywhereSubscriptionStatusType]],
    },
)
ListFargateProfilesRequestRequestTypeDef = TypedDict(
    "ListFargateProfilesRequestRequestTypeDef",
    {
        "clusterName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListIdentityProviderConfigsRequestRequestTypeDef = TypedDict(
    "ListIdentityProviderConfigsRequestRequestTypeDef",
    {
        "clusterName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListNodegroupsRequestRequestTypeDef = TypedDict(
    "ListNodegroupsRequestRequestTypeDef",
    {
        "clusterName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListPodIdentityAssociationsRequestRequestTypeDef = TypedDict(
    "ListPodIdentityAssociationsRequestRequestTypeDef",
    {
        "clusterName": str,
        "namespace": NotRequired[str],
        "serviceAccount": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
PodIdentityAssociationSummaryTypeDef = TypedDict(
    "PodIdentityAssociationSummaryTypeDef",
    {
        "clusterName": NotRequired[str],
        "namespace": NotRequired[str],
        "serviceAccount": NotRequired[str],
        "associationArn": NotRequired[str],
        "associationId": NotRequired[str],
        "ownerArn": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListUpdatesRequestRequestTypeDef = TypedDict(
    "ListUpdatesRequestRequestTypeDef",
    {
        "name": str,
        "nodegroupName": NotRequired[str],
        "addonName": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
LogSetupOutputTypeDef = TypedDict(
    "LogSetupOutputTypeDef",
    {
        "types": NotRequired[List[LogTypeType]],
        "enabled": NotRequired[bool],
    },
)
LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef",
    {
        "types": NotRequired[Sequence[LogTypeType]],
        "enabled": NotRequired[bool],
    },
)
RemoteAccessConfigOutputTypeDef = TypedDict(
    "RemoteAccessConfigOutputTypeDef",
    {
        "ec2SshKey": NotRequired[str],
        "sourceSecurityGroups": NotRequired[List[str]],
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
UpdateAccessConfigRequestTypeDef = TypedDict(
    "UpdateAccessConfigRequestTypeDef",
    {
        "authenticationMode": NotRequired[AuthenticationModeType],
    },
)
UpdateAccessEntryRequestRequestTypeDef = TypedDict(
    "UpdateAccessEntryRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "kubernetesGroups": NotRequired[Sequence[str]],
        "clientRequestToken": NotRequired[str],
        "username": NotRequired[str],
    },
)
UpdateClusterVersionRequestRequestTypeDef = TypedDict(
    "UpdateClusterVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
        "clientRequestToken": NotRequired[str],
    },
)
UpdateEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "id": str,
        "autoRenew": bool,
        "clientRequestToken": NotRequired[str],
    },
)
UpdateLabelsPayloadTypeDef = TypedDict(
    "UpdateLabelsPayloadTypeDef",
    {
        "addOrUpdateLabels": NotRequired[Mapping[str, str]],
        "removeLabels": NotRequired[Sequence[str]],
    },
)
UpdateParamTypeDef = TypedDict(
    "UpdateParamTypeDef",
    {
        "type": NotRequired[UpdateParamTypeType],
        "value": NotRequired[str],
    },
)
UpdatePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "UpdatePodIdentityAssociationRequestRequestTypeDef",
    {
        "clusterName": str,
        "associationId": str,
        "roleArn": NotRequired[str],
        "clientRequestToken": NotRequired[str],
    },
)
AssociatedAccessPolicyTypeDef = TypedDict(
    "AssociatedAccessPolicyTypeDef",
    {
        "policyArn": NotRequired[str],
        "accessScope": NotRequired[AccessScopeOutputTypeDef],
        "associatedAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
    },
)
AssociateAccessPolicyRequestRequestTypeDef = TypedDict(
    "AssociateAccessPolicyRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "policyArn": str,
        "accessScope": AccessScopeTypeDef,
    },
)
AddonHealthTypeDef = TypedDict(
    "AddonHealthTypeDef",
    {
        "issues": NotRequired[List[AddonIssueTypeDef]],
    },
)
CreateAddonRequestRequestTypeDef = TypedDict(
    "CreateAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
        "addonVersion": NotRequired[str],
        "serviceAccountRoleArn": NotRequired[str],
        "resolveConflicts": NotRequired[ResolveConflictsType],
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "configurationValues": NotRequired[str],
        "podIdentityAssociations": NotRequired[Sequence[AddonPodIdentityAssociationsTypeDef]],
    },
)
UpdateAddonRequestRequestTypeDef = TypedDict(
    "UpdateAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
        "addonVersion": NotRequired[str],
        "serviceAccountRoleArn": NotRequired[str],
        "resolveConflicts": NotRequired[ResolveConflictsType],
        "clientRequestToken": NotRequired[str],
        "configurationValues": NotRequired[str],
        "podIdentityAssociations": NotRequired[Sequence[AddonPodIdentityAssociationsTypeDef]],
    },
)
AddonVersionInfoTypeDef = TypedDict(
    "AddonVersionInfoTypeDef",
    {
        "addonVersion": NotRequired[str],
        "architecture": NotRequired[List[str]],
        "compatibilities": NotRequired[List[CompatibilityTypeDef]],
        "requiresConfiguration": NotRequired[bool],
        "requiresIamPermissions": NotRequired[bool],
    },
)
CreateAccessEntryResponseTypeDef = TypedDict(
    "CreateAccessEntryResponseTypeDef",
    {
        "accessEntry": AccessEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccessEntryResponseTypeDef = TypedDict(
    "DescribeAccessEntryResponseTypeDef",
    {
        "accessEntry": AccessEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddonConfigurationResponseTypeDef = TypedDict(
    "DescribeAddonConfigurationResponseTypeDef",
    {
        "addonName": str,
        "addonVersion": str,
        "configurationSchema": str,
        "podIdentityConfiguration": List[AddonPodIdentityConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessEntriesResponseTypeDef = TypedDict(
    "ListAccessEntriesResponseTypeDef",
    {
        "accessEntries": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessPoliciesResponseTypeDef = TypedDict(
    "ListAccessPoliciesResponseTypeDef",
    {
        "accessPolicies": List[AccessPolicyTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAddonsResponseTypeDef = TypedDict(
    "ListAddonsResponseTypeDef",
    {
        "addons": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "clusters": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFargateProfilesResponseTypeDef = TypedDict(
    "ListFargateProfilesResponseTypeDef",
    {
        "fargateProfileNames": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNodegroupsResponseTypeDef = TypedDict(
    "ListNodegroupsResponseTypeDef",
    {
        "nodegroups": List[str],
        "nextToken": str,
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
ListUpdatesResponseTypeDef = TypedDict(
    "ListUpdatesResponseTypeDef",
    {
        "updateIds": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccessEntryResponseTypeDef = TypedDict(
    "UpdateAccessEntryResponseTypeDef",
    {
        "accessEntry": AccessEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "AssociateIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "oidc": OidcIdentityProviderConfigRequestTypeDef,
        "tags": NotRequired[Mapping[str, str]],
        "clientRequestToken": NotRequired[str],
    },
)
NodegroupResourcesTypeDef = TypedDict(
    "NodegroupResourcesTypeDef",
    {
        "autoScalingGroups": NotRequired[List[AutoScalingGroupTypeDef]],
        "remoteAccessSecurityGroup": NotRequired[str],
    },
)
DeprecationDetailTypeDef = TypedDict(
    "DeprecationDetailTypeDef",
    {
        "usage": NotRequired[str],
        "replacedWith": NotRequired[str],
        "stopServingVersion": NotRequired[str],
        "startServingReplacementVersion": NotRequired[str],
        "clientStats": NotRequired[List[ClientStatTypeDef]],
    },
)
ClusterHealthTypeDef = TypedDict(
    "ClusterHealthTypeDef",
    {
        "issues": NotRequired[List[ClusterIssueTypeDef]],
    },
)
RegisterClusterRequestRequestTypeDef = TypedDict(
    "RegisterClusterRequestRequestTypeDef",
    {
        "name": str,
        "connectorConfig": ConnectorConfigRequestTypeDef,
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
OutpostConfigRequestTypeDef = TypedDict(
    "OutpostConfigRequestTypeDef",
    {
        "outpostArns": Sequence[str],
        "controlPlaneInstanceType": str,
        "controlPlanePlacement": NotRequired[ControlPlanePlacementRequestTypeDef],
    },
)
OutpostConfigResponseTypeDef = TypedDict(
    "OutpostConfigResponseTypeDef",
    {
        "outpostArns": List[str],
        "controlPlaneInstanceType": str,
        "controlPlanePlacement": NotRequired[ControlPlanePlacementResponseTypeDef],
    },
)
CreateEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "name": str,
        "term": EksAnywhereSubscriptionTermTypeDef,
        "licenseQuantity": NotRequired[int],
        "licenseType": NotRequired[Literal["Cluster"]],
        "autoRenew": NotRequired[bool],
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
EksAnywhereSubscriptionTypeDef = TypedDict(
    "EksAnywhereSubscriptionTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "effectiveDate": NotRequired[datetime],
        "expirationDate": NotRequired[datetime],
        "licenseQuantity": NotRequired[int],
        "licenseType": NotRequired[Literal["Cluster"]],
        "term": NotRequired[EksAnywhereSubscriptionTermTypeDef],
        "status": NotRequired[str],
        "autoRenew": NotRequired[bool],
        "licenseArns": NotRequired[List[str]],
        "tags": NotRequired[Dict[str, str]],
    },
)
UpdateNodegroupVersionRequestRequestTypeDef = TypedDict(
    "UpdateNodegroupVersionRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "version": NotRequired[str],
        "releaseVersion": NotRequired[str],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "force": NotRequired[bool],
        "clientRequestToken": NotRequired[str],
    },
)
CreateNodegroupRequestRequestTypeDef = TypedDict(
    "CreateNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "subnets": Sequence[str],
        "nodeRole": str,
        "scalingConfig": NotRequired[NodegroupScalingConfigTypeDef],
        "diskSize": NotRequired[int],
        "instanceTypes": NotRequired[Sequence[str]],
        "amiType": NotRequired[AMITypesType],
        "remoteAccess": NotRequired[RemoteAccessConfigTypeDef],
        "labels": NotRequired[Mapping[str, str]],
        "taints": NotRequired[Sequence[TaintTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "clientRequestToken": NotRequired[str],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "updateConfig": NotRequired[NodegroupUpdateConfigTypeDef],
        "capacityType": NotRequired[CapacityTypesType],
        "version": NotRequired[str],
        "releaseVersion": NotRequired[str],
    },
)
UpdateTaintsPayloadTypeDef = TypedDict(
    "UpdateTaintsPayloadTypeDef",
    {
        "addOrUpdateTaints": NotRequired[Sequence[TaintTypeDef]],
        "removeTaints": NotRequired[Sequence[TaintTypeDef]],
    },
)
CreatePodIdentityAssociationResponseTypeDef = TypedDict(
    "CreatePodIdentityAssociationResponseTypeDef",
    {
        "association": PodIdentityAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePodIdentityAssociationResponseTypeDef = TypedDict(
    "DeletePodIdentityAssociationResponseTypeDef",
    {
        "association": PodIdentityAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePodIdentityAssociationResponseTypeDef = TypedDict(
    "DescribePodIdentityAssociationResponseTypeDef",
    {
        "association": PodIdentityAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePodIdentityAssociationResponseTypeDef = TypedDict(
    "UpdatePodIdentityAssociationResponseTypeDef",
    {
        "association": PodIdentityAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddonRequestAddonActiveWaitTypeDef = TypedDict(
    "DescribeAddonRequestAddonActiveWaitTypeDef",
    {
        "clusterName": str,
        "addonName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeAddonRequestAddonDeletedWaitTypeDef = TypedDict(
    "DescribeAddonRequestAddonDeletedWaitTypeDef",
    {
        "clusterName": str,
        "addonName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeClusterRequestClusterActiveWaitTypeDef = TypedDict(
    "DescribeClusterRequestClusterActiveWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeClusterRequestClusterDeletedWaitTypeDef = TypedDict(
    "DescribeClusterRequestClusterDeletedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeFargateProfileRequestFargateProfileActiveWaitTypeDef = TypedDict(
    "DescribeFargateProfileRequestFargateProfileActiveWaitTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeFargateProfileRequestFargateProfileDeletedWaitTypeDef = TypedDict(
    "DescribeFargateProfileRequestFargateProfileDeletedWaitTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeNodegroupRequestNodegroupActiveWaitTypeDef = TypedDict(
    "DescribeNodegroupRequestNodegroupActiveWaitTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeNodegroupRequestNodegroupDeletedWaitTypeDef = TypedDict(
    "DescribeNodegroupRequestNodegroupDeletedWaitTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeAddonVersionsRequestDescribeAddonVersionsPaginateTypeDef = TypedDict(
    "DescribeAddonVersionsRequestDescribeAddonVersionsPaginateTypeDef",
    {
        "kubernetesVersion": NotRequired[str],
        "addonName": NotRequired[str],
        "types": NotRequired[Sequence[str]],
        "publishers": NotRequired[Sequence[str]],
        "owners": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessEntriesRequestListAccessEntriesPaginateTypeDef = TypedDict(
    "ListAccessEntriesRequestListAccessEntriesPaginateTypeDef",
    {
        "clusterName": str,
        "associatedPolicyArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef = TypedDict(
    "ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAddonsRequestListAddonsPaginateTypeDef = TypedDict(
    "ListAddonsRequestListAddonsPaginateTypeDef",
    {
        "clusterName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssociatedAccessPoliciesRequestListAssociatedAccessPoliciesPaginateTypeDef = TypedDict(
    "ListAssociatedAccessPoliciesRequestListAssociatedAccessPoliciesPaginateTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClustersRequestListClustersPaginateTypeDef = TypedDict(
    "ListClustersRequestListClustersPaginateTypeDef",
    {
        "include": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEksAnywhereSubscriptionsRequestListEksAnywhereSubscriptionsPaginateTypeDef = TypedDict(
    "ListEksAnywhereSubscriptionsRequestListEksAnywhereSubscriptionsPaginateTypeDef",
    {
        "includeStatus": NotRequired[Sequence[EksAnywhereSubscriptionStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFargateProfilesRequestListFargateProfilesPaginateTypeDef = TypedDict(
    "ListFargateProfilesRequestListFargateProfilesPaginateTypeDef",
    {
        "clusterName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIdentityProviderConfigsRequestListIdentityProviderConfigsPaginateTypeDef = TypedDict(
    "ListIdentityProviderConfigsRequestListIdentityProviderConfigsPaginateTypeDef",
    {
        "clusterName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNodegroupsRequestListNodegroupsPaginateTypeDef = TypedDict(
    "ListNodegroupsRequestListNodegroupsPaginateTypeDef",
    {
        "clusterName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPodIdentityAssociationsRequestListPodIdentityAssociationsPaginateTypeDef = TypedDict(
    "ListPodIdentityAssociationsRequestListPodIdentityAssociationsPaginateTypeDef",
    {
        "clusterName": str,
        "namespace": NotRequired[str],
        "serviceAccount": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUpdatesRequestListUpdatesPaginateTypeDef = TypedDict(
    "ListUpdatesRequestListUpdatesPaginateTypeDef",
    {
        "name": str,
        "nodegroupName": NotRequired[str],
        "addonName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "identityProviderConfig": IdentityProviderConfigTypeDef,
    },
)
DisassociateIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "DisassociateIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "identityProviderConfig": IdentityProviderConfigTypeDef,
        "clientRequestToken": NotRequired[str],
    },
)
ListIdentityProviderConfigsResponseTypeDef = TypedDict(
    "ListIdentityProviderConfigsResponseTypeDef",
    {
        "identityProviderConfigs": List[IdentityProviderConfigTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EncryptionConfigOutputTypeDef = TypedDict(
    "EncryptionConfigOutputTypeDef",
    {
        "resources": NotRequired[List[str]],
        "provider": NotRequired[ProviderTypeDef],
    },
)
EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "resources": NotRequired[Sequence[str]],
        "provider": NotRequired[ProviderTypeDef],
    },
)
FargateProfileHealthTypeDef = TypedDict(
    "FargateProfileHealthTypeDef",
    {
        "issues": NotRequired[List[FargateProfileIssueTypeDef]],
    },
)
FargateProfileSelectorUnionTypeDef = Union[
    FargateProfileSelectorTypeDef, FargateProfileSelectorOutputTypeDef
]
IdentityProviderConfigResponseTypeDef = TypedDict(
    "IdentityProviderConfigResponseTypeDef",
    {
        "oidc": NotRequired[OidcIdentityProviderConfigTypeDef],
    },
)
IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "oidc": NotRequired[OIDCTypeDef],
    },
)
InsightResourceDetailTypeDef = TypedDict(
    "InsightResourceDetailTypeDef",
    {
        "insightStatus": NotRequired[InsightStatusTypeDef],
        "kubernetesResourceUri": NotRequired[str],
        "arn": NotRequired[str],
    },
)
InsightSummaryTypeDef = TypedDict(
    "InsightSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "category": NotRequired[Literal["UPGRADE_READINESS"]],
        "kubernetesVersion": NotRequired[str],
        "lastRefreshTime": NotRequired[datetime],
        "lastTransitionTime": NotRequired[datetime],
        "description": NotRequired[str],
        "insightStatus": NotRequired[InsightStatusTypeDef],
    },
)
ListInsightsRequestListInsightsPaginateTypeDef = TypedDict(
    "ListInsightsRequestListInsightsPaginateTypeDef",
    {
        "clusterName": str,
        "filter": NotRequired[InsightsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInsightsRequestRequestTypeDef = TypedDict(
    "ListInsightsRequestRequestTypeDef",
    {
        "clusterName": str,
        "filter": NotRequired[InsightsFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
NodegroupHealthTypeDef = TypedDict(
    "NodegroupHealthTypeDef",
    {
        "issues": NotRequired[List[IssueTypeDef]],
    },
)
ListPodIdentityAssociationsResponseTypeDef = TypedDict(
    "ListPodIdentityAssociationsResponseTypeDef",
    {
        "associations": List[PodIdentityAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingOutputTypeDef = TypedDict(
    "LoggingOutputTypeDef",
    {
        "clusterLogging": NotRequired[List[LogSetupOutputTypeDef]],
    },
)
LogSetupUnionTypeDef = Union[LogSetupTypeDef, LogSetupOutputTypeDef]
UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[UpdateStatusType],
        "type": NotRequired[UpdateTypeType],
        "params": NotRequired[List[UpdateParamTypeDef]],
        "createdAt": NotRequired[datetime],
        "errors": NotRequired[List[ErrorDetailTypeDef]],
    },
)
AssociateAccessPolicyResponseTypeDef = TypedDict(
    "AssociateAccessPolicyResponseTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "associatedAccessPolicy": AssociatedAccessPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssociatedAccessPoliciesResponseTypeDef = TypedDict(
    "ListAssociatedAccessPoliciesResponseTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "nextToken": str,
        "associatedAccessPolicies": List[AssociatedAccessPolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddonTypeDef = TypedDict(
    "AddonTypeDef",
    {
        "addonName": NotRequired[str],
        "clusterName": NotRequired[str],
        "status": NotRequired[AddonStatusType],
        "addonVersion": NotRequired[str],
        "health": NotRequired[AddonHealthTypeDef],
        "addonArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "serviceAccountRoleArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "publisher": NotRequired[str],
        "owner": NotRequired[str],
        "marketplaceInformation": NotRequired[MarketplaceInformationTypeDef],
        "configurationValues": NotRequired[str],
        "podIdentityAssociations": NotRequired[List[str]],
    },
)
AddonInfoTypeDef = TypedDict(
    "AddonInfoTypeDef",
    {
        "addonName": NotRequired[str],
        "type": NotRequired[str],
        "addonVersions": NotRequired[List[AddonVersionInfoTypeDef]],
        "publisher": NotRequired[str],
        "owner": NotRequired[str],
        "marketplaceInformation": NotRequired[MarketplaceInformationTypeDef],
    },
)
InsightCategorySpecificSummaryTypeDef = TypedDict(
    "InsightCategorySpecificSummaryTypeDef",
    {
        "deprecationDetails": NotRequired[List[DeprecationDetailTypeDef]],
    },
)
CreateEksAnywhereSubscriptionResponseTypeDef = TypedDict(
    "CreateEksAnywhereSubscriptionResponseTypeDef",
    {
        "subscription": EksAnywhereSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEksAnywhereSubscriptionResponseTypeDef = TypedDict(
    "DeleteEksAnywhereSubscriptionResponseTypeDef",
    {
        "subscription": EksAnywhereSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEksAnywhereSubscriptionResponseTypeDef = TypedDict(
    "DescribeEksAnywhereSubscriptionResponseTypeDef",
    {
        "subscription": EksAnywhereSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEksAnywhereSubscriptionsResponseTypeDef = TypedDict(
    "ListEksAnywhereSubscriptionsResponseTypeDef",
    {
        "subscriptions": List[EksAnywhereSubscriptionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEksAnywhereSubscriptionResponseTypeDef = TypedDict(
    "UpdateEksAnywhereSubscriptionResponseTypeDef",
    {
        "subscription": EksAnywhereSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNodegroupConfigRequestRequestTypeDef = TypedDict(
    "UpdateNodegroupConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "labels": NotRequired[UpdateLabelsPayloadTypeDef],
        "taints": NotRequired[UpdateTaintsPayloadTypeDef],
        "scalingConfig": NotRequired[NodegroupScalingConfigTypeDef],
        "updateConfig": NotRequired[NodegroupUpdateConfigTypeDef],
        "clientRequestToken": NotRequired[str],
    },
)
EncryptionConfigUnionTypeDef = Union[EncryptionConfigTypeDef, EncryptionConfigOutputTypeDef]
FargateProfileTypeDef = TypedDict(
    "FargateProfileTypeDef",
    {
        "fargateProfileName": NotRequired[str],
        "fargateProfileArn": NotRequired[str],
        "clusterName": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "podExecutionRoleArn": NotRequired[str],
        "subnets": NotRequired[List[str]],
        "selectors": NotRequired[List[FargateProfileSelectorOutputTypeDef]],
        "status": NotRequired[FargateProfileStatusType],
        "tags": NotRequired[Dict[str, str]],
        "health": NotRequired[FargateProfileHealthTypeDef],
    },
)
CreateFargateProfileRequestRequestTypeDef = TypedDict(
    "CreateFargateProfileRequestRequestTypeDef",
    {
        "fargateProfileName": str,
        "clusterName": str,
        "podExecutionRoleArn": str,
        "subnets": NotRequired[Sequence[str]],
        "selectors": NotRequired[Sequence[FargateProfileSelectorUnionTypeDef]],
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DescribeIdentityProviderConfigResponseTypeDef = TypedDict(
    "DescribeIdentityProviderConfigResponseTypeDef",
    {
        "identityProviderConfig": IdentityProviderConfigResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "insights": List[InsightSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NodegroupTypeDef = TypedDict(
    "NodegroupTypeDef",
    {
        "nodegroupName": NotRequired[str],
        "nodegroupArn": NotRequired[str],
        "clusterName": NotRequired[str],
        "version": NotRequired[str],
        "releaseVersion": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "status": NotRequired[NodegroupStatusType],
        "capacityType": NotRequired[CapacityTypesType],
        "scalingConfig": NotRequired[NodegroupScalingConfigTypeDef],
        "instanceTypes": NotRequired[List[str]],
        "subnets": NotRequired[List[str]],
        "remoteAccess": NotRequired[RemoteAccessConfigOutputTypeDef],
        "amiType": NotRequired[AMITypesType],
        "nodeRole": NotRequired[str],
        "labels": NotRequired[Dict[str, str]],
        "taints": NotRequired[List[TaintTypeDef]],
        "resources": NotRequired[NodegroupResourcesTypeDef],
        "diskSize": NotRequired[int],
        "health": NotRequired[NodegroupHealthTypeDef],
        "updateConfig": NotRequired[NodegroupUpdateConfigTypeDef],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "version": NotRequired[str],
        "endpoint": NotRequired[str],
        "roleArn": NotRequired[str],
        "resourcesVpcConfig": NotRequired[VpcConfigResponseTypeDef],
        "kubernetesNetworkConfig": NotRequired[KubernetesNetworkConfigResponseTypeDef],
        "logging": NotRequired[LoggingOutputTypeDef],
        "identity": NotRequired[IdentityTypeDef],
        "status": NotRequired[ClusterStatusType],
        "certificateAuthority": NotRequired[CertificateTypeDef],
        "clientRequestToken": NotRequired[str],
        "platformVersion": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "encryptionConfig": NotRequired[List[EncryptionConfigOutputTypeDef]],
        "connectorConfig": NotRequired[ConnectorConfigResponseTypeDef],
        "id": NotRequired[str],
        "health": NotRequired[ClusterHealthTypeDef],
        "outpostConfig": NotRequired[OutpostConfigResponseTypeDef],
        "accessConfig": NotRequired[AccessConfigResponseTypeDef],
        "upgradePolicy": NotRequired[UpgradePolicyResponseTypeDef],
    },
)
LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "clusterLogging": NotRequired[Sequence[LogSetupUnionTypeDef]],
    },
)
AssociateEncryptionConfigResponseTypeDef = TypedDict(
    "AssociateEncryptionConfigResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateIdentityProviderConfigResponseTypeDef = TypedDict(
    "AssociateIdentityProviderConfigResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUpdateResponseTypeDef = TypedDict(
    "DescribeUpdateResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateIdentityProviderConfigResponseTypeDef = TypedDict(
    "DisassociateIdentityProviderConfigResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAddonResponseTypeDef = TypedDict(
    "UpdateAddonResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateClusterConfigResponseTypeDef = TypedDict(
    "UpdateClusterConfigResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateClusterVersionResponseTypeDef = TypedDict(
    "UpdateClusterVersionResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNodegroupConfigResponseTypeDef = TypedDict(
    "UpdateNodegroupConfigResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNodegroupVersionResponseTypeDef = TypedDict(
    "UpdateNodegroupVersionResponseTypeDef",
    {
        "update": UpdateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAddonResponseTypeDef = TypedDict(
    "CreateAddonResponseTypeDef",
    {
        "addon": AddonTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAddonResponseTypeDef = TypedDict(
    "DeleteAddonResponseTypeDef",
    {
        "addon": AddonTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddonResponseTypeDef = TypedDict(
    "DescribeAddonResponseTypeDef",
    {
        "addon": AddonTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddonVersionsResponseTypeDef = TypedDict(
    "DescribeAddonVersionsResponseTypeDef",
    {
        "addons": List[AddonInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "category": NotRequired[Literal["UPGRADE_READINESS"]],
        "kubernetesVersion": NotRequired[str],
        "lastRefreshTime": NotRequired[datetime],
        "lastTransitionTime": NotRequired[datetime],
        "description": NotRequired[str],
        "insightStatus": NotRequired[InsightStatusTypeDef],
        "recommendation": NotRequired[str],
        "additionalInfo": NotRequired[Dict[str, str]],
        "resources": NotRequired[List[InsightResourceDetailTypeDef]],
        "categorySpecificSummary": NotRequired[InsightCategorySpecificSummaryTypeDef],
    },
)
AssociateEncryptionConfigRequestRequestTypeDef = TypedDict(
    "AssociateEncryptionConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "encryptionConfig": Sequence[EncryptionConfigUnionTypeDef],
        "clientRequestToken": NotRequired[str],
    },
)
CreateFargateProfileResponseTypeDef = TypedDict(
    "CreateFargateProfileResponseTypeDef",
    {
        "fargateProfile": FargateProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFargateProfileResponseTypeDef = TypedDict(
    "DeleteFargateProfileResponseTypeDef",
    {
        "fargateProfile": FargateProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFargateProfileResponseTypeDef = TypedDict(
    "DescribeFargateProfileResponseTypeDef",
    {
        "fargateProfile": FargateProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNodegroupResponseTypeDef = TypedDict(
    "CreateNodegroupResponseTypeDef",
    {
        "nodegroup": NodegroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNodegroupResponseTypeDef = TypedDict(
    "DeleteNodegroupResponseTypeDef",
    {
        "nodegroup": NodegroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNodegroupResponseTypeDef = TypedDict(
    "DescribeNodegroupResponseTypeDef",
    {
        "nodegroup": NodegroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterClusterResponseTypeDef = TypedDict(
    "DeregisterClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterClusterResponseTypeDef = TypedDict(
    "RegisterClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": str,
        "resourcesVpcConfig": VpcConfigRequestTypeDef,
        "version": NotRequired[str],
        "kubernetesNetworkConfig": NotRequired[KubernetesNetworkConfigRequestTypeDef],
        "logging": NotRequired[LoggingTypeDef],
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "encryptionConfig": NotRequired[Sequence[EncryptionConfigTypeDef]],
        "outpostConfig": NotRequired[OutpostConfigRequestTypeDef],
        "accessConfig": NotRequired[CreateAccessConfigRequestTypeDef],
        "bootstrapSelfManagedAddons": NotRequired[bool],
        "upgradePolicy": NotRequired[UpgradePolicyRequestTypeDef],
    },
)
UpdateClusterConfigRequestRequestTypeDef = TypedDict(
    "UpdateClusterConfigRequestRequestTypeDef",
    {
        "name": str,
        "resourcesVpcConfig": NotRequired[VpcConfigRequestTypeDef],
        "logging": NotRequired[LoggingTypeDef],
        "clientRequestToken": NotRequired[str],
        "accessConfig": NotRequired[UpdateAccessConfigRequestTypeDef],
        "upgradePolicy": NotRequired[UpgradePolicyRequestTypeDef],
    },
)
DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {
        "insight": InsightTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
