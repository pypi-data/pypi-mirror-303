"""
Type annotations for guardduty service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/type_defs/)

Usage::

    ```python
    from mypy_boto3_guardduty.type_defs import AcceptAdministratorInvitationRequestRequestTypeDef

    data: AcceptAdministratorInvitationRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AdminStatusType,
    AutoEnableMembersType,
    CoverageFilterCriterionKeyType,
    CoverageSortKeyType,
    CoverageStatisticsTypeType,
    CoverageStatusType,
    CriterionKeyType,
    DataSourceStatusType,
    DataSourceType,
    DetectorFeatureResultType,
    DetectorFeatureType,
    DetectorStatusType,
    EbsSnapshotPreservationType,
    FeatureAdditionalConfigurationType,
    FeatureStatusType,
    FeedbackType,
    FilterActionType,
    FindingPublishingFrequencyType,
    FreeTrialFeatureResultType,
    GroupByTypeType,
    IpSetFormatType,
    IpSetStatusType,
    MalwareProtectionPlanStatusType,
    MalwareProtectionPlanTaggingActionStatusType,
    ManagementTypeType,
    OrderByType,
    OrgFeatureAdditionalConfigurationType,
    OrgFeatureStatusType,
    OrgFeatureType,
    ProfileSubtypeType,
    PublishingStatusType,
    ResourceTypeType,
    ScanResultType,
    ScanStatusType,
    ScanTypeType,
    ThreatIntelSetFormatType,
    ThreatIntelSetStatusType,
    UsageFeatureType,
    UsageStatisticTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    "AcceptInvitationRequestRequestTypeDef",
    "AccessControlListTypeDef",
    "AccessKeyDetailsTypeDef",
    "AccountDetailTypeDef",
    "FreeTrialFeatureConfigurationResultTypeDef",
    "BlockPublicAccessTypeDef",
    "AccountStatisticsTypeDef",
    "DnsRequestActionTypeDef",
    "KubernetesPermissionCheckedDetailsTypeDef",
    "KubernetesRoleBindingDetailsTypeDef",
    "KubernetesRoleDetailsTypeDef",
    "AddonDetailsTypeDef",
    "AdminAccountTypeDef",
    "AdministratorTypeDef",
    "AgentDetailsTypeDef",
    "ObservationsTypeDef",
    "ArchiveFindingsRequestRequestTypeDef",
    "DomainDetailsTypeDef",
    "RemoteAccountDetailsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
    "ConditionOutputTypeDef",
    "ConditionTypeDef",
    "ContainerInstanceDetailsTypeDef",
    "SecurityContextTypeDef",
    "VolumeMountTypeDef",
    "CountryTypeDef",
    "FargateDetailsTypeDef",
    "CoverageFilterConditionTypeDef",
    "CoverageSortCriteriaTypeDef",
    "CoverageStatisticsTypeDef",
    "ResponseMetadataTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "CreateS3BucketResourceOutputTypeDef",
    "DestinationPropertiesTypeDef",
    "CreateS3BucketResourceTypeDef",
    "CreateSampleFindingsRequestRequestTypeDef",
    "CreateThreatIntelSetRequestRequestTypeDef",
    "DNSLogsConfigurationResultTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "DataSourceFreeTrialTypeDef",
    "DateStatisticsTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DefaultServerSideEncryptionTypeDef",
    "DeleteDetectorRequestRequestTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteMalwareProtectionPlanRequestRequestTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DeletePublishingDestinationRequestRequestTypeDef",
    "DeleteThreatIntelSetRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "SortCriteriaTypeDef",
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    "DescribePublishingDestinationRequestRequestTypeDef",
    "DestinationTypeDef",
    "DetectorAdditionalConfigurationResultTypeDef",
    "DetectorAdditionalConfigurationTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateFromAdministratorAccountRequestRequestTypeDef",
    "DisassociateFromMasterAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "VolumeDetailTypeDef",
    "EbsVolumesResultTypeDef",
    "TagTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "FilterConditionTypeDef",
    "FindingTypeStatisticsTypeDef",
    "ResourceStatisticsTypeDef",
    "SeverityStatisticsTypeDef",
    "GeoLocationTypeDef",
    "GetAdministratorAccountRequestRequestTypeDef",
    "GetDetectorRequestRequestTypeDef",
    "GetFilterRequestRequestTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "GetMalwareProtectionPlanRequestRequestTypeDef",
    "MalwareProtectionPlanStatusReasonTypeDef",
    "GetMalwareScanSettingsRequestRequestTypeDef",
    "GetMasterAccountRequestRequestTypeDef",
    "MasterTypeDef",
    "GetMemberDetectorsRequestRequestTypeDef",
    "GetMembersRequestRequestTypeDef",
    "MemberTypeDef",
    "GetRemainingFreeTrialDaysRequestRequestTypeDef",
    "GetThreatIntelSetRequestRequestTypeDef",
    "UsageCriteriaTypeDef",
    "HighestSeverityThreatDetailsTypeDef",
    "HostPathTypeDef",
    "IamInstanceProfileTypeDef",
    "ImpersonatedUserTypeDef",
    "ProductCodeTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "ItemPathTypeDef",
    "KubernetesAuditLogsConfigurationResultTypeDef",
    "KubernetesAuditLogsConfigurationTypeDef",
    "LineageObjectTypeDef",
    "ListDetectorsRequestRequestTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListMalwareProtectionPlansRequestRequestTypeDef",
    "MalwareProtectionPlanSummaryTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListPublishingDestinationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListThreatIntelSetsRequestRequestTypeDef",
    "LocalIpDetailsTypeDef",
    "LocalPortDetailsTypeDef",
    "LoginAttributeTypeDef",
    "ScanEc2InstanceWithFindingsTypeDef",
    "MalwareProtectionPlanTaggingActionTypeDef",
    "MemberAdditionalConfigurationResultTypeDef",
    "MemberAdditionalConfigurationTypeDef",
    "RemotePortDetailsTypeDef",
    "PrivateIpAddressDetailsTypeDef",
    "SecurityGroupTypeDef",
    "OrganizationAdditionalConfigurationResultTypeDef",
    "OrganizationAdditionalConfigurationTypeDef",
    "OrganizationS3LogsConfigurationResultTypeDef",
    "OrganizationS3LogsConfigurationTypeDef",
    "OrganizationEbsVolumesResultTypeDef",
    "OrganizationEbsVolumesTypeDef",
    "OrganizationFeatureStatisticsAdditionalConfigurationTypeDef",
    "OrganizationKubernetesAuditLogsConfigurationResultTypeDef",
    "OrganizationKubernetesAuditLogsConfigurationTypeDef",
    "OrganizationTypeDef",
    "OwnerTypeDef",
    "RdsDbUserDetailsTypeDef",
    "ResourceDetailsTypeDef",
    "S3ObjectDetailTypeDef",
    "ScanConditionPairTypeDef",
    "ScannedItemCountTypeDef",
    "ThreatsDetectedItemCountTypeDef",
    "ScanFilePathTypeDef",
    "ScanResultDetailsTypeDef",
    "TriggerDetailsTypeDef",
    "ServiceAdditionalInfoTypeDef",
    "StartMalwareScanRequestRequestTypeDef",
    "StartMonitoringMembersRequestRequestTypeDef",
    "StopMonitoringMembersRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TotalTypeDef",
    "UnarchiveFindingsRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFindingsFeedbackRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateS3BucketResourceTypeDef",
    "UpdateThreatIntelSetRequestRequestTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "AccountLevelPermissionsTypeDef",
    "CoverageEksClusterDetailsTypeDef",
    "CoverageEc2InstanceDetailsTypeDef",
    "AnomalyObjectTypeDef",
    "BucketLevelPermissionsTypeDef",
    "FindingCriteriaOutputTypeDef",
    "ConditionUnionTypeDef",
    "ContainerTypeDef",
    "CoverageEcsClusterDetailsTypeDef",
    "CoverageFilterCriterionTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateMalwareProtectionPlanResponseTypeDef",
    "CreatePublishingDestinationResponseTypeDef",
    "CreateThreatIntelSetResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetCoverageStatisticsResponseTypeDef",
    "GetIPSetResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetThreatIntelSetResponseTypeDef",
    "ListDetectorsResponseTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThreatIntelSetsResponseTypeDef",
    "StartMalwareScanResponseTypeDef",
    "UpdateFilterResponseTypeDef",
    "CreateMembersResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "DisassociateMembersResponseTypeDef",
    "InviteMembersResponseTypeDef",
    "StartMonitoringMembersResponseTypeDef",
    "StopMonitoringMembersResponseTypeDef",
    "UpdateMemberDetectorsResponseTypeDef",
    "CreateProtectedResourceOutputTypeDef",
    "CreatePublishingDestinationRequestRequestTypeDef",
    "DescribePublishingDestinationResponseTypeDef",
    "UpdatePublishingDestinationRequestRequestTypeDef",
    "CreateS3BucketResourceUnionTypeDef",
    "KubernetesDataSourceFreeTrialTypeDef",
    "MalwareProtectionDataSourceFreeTrialTypeDef",
    "ListDetectorsRequestListDetectorsPaginateTypeDef",
    "ListFiltersRequestListFiltersPaginateTypeDef",
    "ListIPSetsRequestListIPSetsPaginateTypeDef",
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    "ListMembersRequestListMembersPaginateTypeDef",
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    "ListThreatIntelSetsRequestListThreatIntelSetsPaginateTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "ListPublishingDestinationsResponseTypeDef",
    "DetectorFeatureConfigurationResultTypeDef",
    "DetectorFeatureConfigurationTypeDef",
    "EbsVolumeDetailsTypeDef",
    "ScanEc2InstanceWithFindingsResultTypeDef",
    "EksClusterDetailsTypeDef",
    "RdsDbInstanceDetailsTypeDef",
    "EvidenceTypeDef",
    "FilterCriterionTypeDef",
    "FindingStatisticsTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMembersResponseTypeDef",
    "ListMembersResponseTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "VolumeTypeDef",
    "KubernetesUserDetailsTypeDef",
    "ListInvitationsResponseTypeDef",
    "ThreatTypeDef",
    "KubernetesConfigurationResultTypeDef",
    "KubernetesConfigurationTypeDef",
    "ProcessDetailsTypeDef",
    "ListMalwareProtectionPlansResponseTypeDef",
    "MalwareProtectionConfigurationTypeDef",
    "MalwareProtectionPlanActionsTypeDef",
    "MemberFeaturesConfigurationResultTypeDef",
    "MemberFeaturesConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "VpcConfigTypeDef",
    "OrganizationFeatureConfigurationResultTypeDef",
    "OrganizationFeatureConfigurationTypeDef",
    "OrganizationScanEc2InstanceWithFindingsResultTypeDef",
    "OrganizationScanEc2InstanceWithFindingsTypeDef",
    "OrganizationFeatureStatisticsTypeDef",
    "OrganizationKubernetesConfigurationResultTypeDef",
    "OrganizationKubernetesConfigurationTypeDef",
    "RemoteIpDetailsTypeDef",
    "ScanConditionOutputTypeDef",
    "ScanConditionTypeDef",
    "ScanThreatNameTypeDef",
    "ScanTypeDef",
    "UsageAccountResultTypeDef",
    "UsageDataSourceResultTypeDef",
    "UsageFeatureResultTypeDef",
    "UsageResourceResultTypeDef",
    "UsageTopAccountResultTypeDef",
    "UpdateProtectedResourceTypeDef",
    "AnomalyUnusualTypeDef",
    "PermissionConfigurationTypeDef",
    "GetFilterResponseTypeDef",
    "FindingCriteriaTypeDef",
    "CoverageResourceDetailsTypeDef",
    "CoverageFilterCriteriaTypeDef",
    "CreateProtectedResourceTypeDef",
    "DataSourcesFreeTrialTypeDef",
    "MalwareProtectionConfigurationResultTypeDef",
    "FilterCriteriaTypeDef",
    "GetFindingsStatisticsResponseTypeDef",
    "EcsTaskDetailsTypeDef",
    "KubernetesWorkloadDetailsTypeDef",
    "MalwareScanDetailsTypeDef",
    "RuntimeContextTypeDef",
    "DataSourceConfigurationsTypeDef",
    "GetMalwareProtectionPlanResponseTypeDef",
    "InstanceDetailsTypeDef",
    "LambdaDetailsTypeDef",
    "OrganizationMalwareProtectionConfigurationResultTypeDef",
    "OrganizationMalwareProtectionConfigurationTypeDef",
    "OrganizationStatisticsTypeDef",
    "AwsApiCallActionTypeDef",
    "KubernetesApiCallActionTypeDef",
    "NetworkConnectionActionTypeDef",
    "PortProbeDetailTypeDef",
    "RdsLoginAttemptActionTypeDef",
    "ScanResourceCriteriaOutputTypeDef",
    "ScanConditionUnionTypeDef",
    "ThreatDetectedByNameTypeDef",
    "DescribeMalwareScansResponseTypeDef",
    "UsageTopAccountsResultTypeDef",
    "UpdateMalwareProtectionPlanRequestRequestTypeDef",
    "AnomalyTypeDef",
    "PublicAccessTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "GetFindingsStatisticsRequestRequestTypeDef",
    "ListFindingsRequestListFindingsPaginateTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "UpdateFilterRequestRequestTypeDef",
    "CoverageResourceTypeDef",
    "GetCoverageStatisticsRequestRequestTypeDef",
    "ListCoverageRequestListCoveragePaginateTypeDef",
    "ListCoverageRequestRequestTypeDef",
    "CreateMalwareProtectionPlanRequestRequestTypeDef",
    "AccountFreeTrialInfoTypeDef",
    "DataSourceConfigurationsResultTypeDef",
    "UnprocessedDataSourcesResultTypeDef",
    "DescribeMalwareScansRequestDescribeMalwareScansPaginateTypeDef",
    "DescribeMalwareScansRequestRequestTypeDef",
    "EcsClusterDetailsTypeDef",
    "KubernetesDetailsTypeDef",
    "RuntimeDetailsTypeDef",
    "CreateDetectorRequestRequestTypeDef",
    "UpdateDetectorRequestRequestTypeDef",
    "UpdateMemberDetectorsRequestRequestTypeDef",
    "OrganizationDataSourceConfigurationsResultTypeDef",
    "OrganizationDataSourceConfigurationsTypeDef",
    "OrganizationDetailsTypeDef",
    "PortProbeActionTypeDef",
    "GetMalwareScanSettingsResponseTypeDef",
    "ScanResourceCriteriaTypeDef",
    "ScanDetectionsTypeDef",
    "UsageStatisticsTypeDef",
    "DetectionTypeDef",
    "S3BucketDetailTypeDef",
    "ListCoverageResponseTypeDef",
    "GetRemainingFreeTrialDaysResponseTypeDef",
    "GetDetectorResponseTypeDef",
    "MemberDataSourceConfigurationTypeDef",
    "CreateDetectorResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "GetOrganizationStatisticsResponseTypeDef",
    "ActionTypeDef",
    "UpdateMalwareScanSettingsRequestRequestTypeDef",
    "EbsVolumeScanDetailsTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "ResourceTypeDef",
    "GetMemberDetectorsResponseTypeDef",
    "ServiceTypeDef",
    "FindingTypeDef",
    "GetFindingsResponseTypeDef",
)

AcceptAdministratorInvitationRequestRequestTypeDef = TypedDict(
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AdministratorId": str,
        "InvitationId": str,
    },
)
AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MasterId": str,
        "InvitationId": str,
    },
)
AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "AllowsPublicReadAccess": NotRequired[bool],
        "AllowsPublicWriteAccess": NotRequired[bool],
    },
)
AccessKeyDetailsTypeDef = TypedDict(
    "AccessKeyDetailsTypeDef",
    {
        "AccessKeyId": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "UserName": NotRequired[str],
        "UserType": NotRequired[str],
    },
)
AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "AccountId": str,
        "Email": str,
    },
)
FreeTrialFeatureConfigurationResultTypeDef = TypedDict(
    "FreeTrialFeatureConfigurationResultTypeDef",
    {
        "Name": NotRequired[FreeTrialFeatureResultType],
        "FreeTrialDaysRemaining": NotRequired[int],
    },
)
BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "IgnorePublicAcls": NotRequired[bool],
        "RestrictPublicBuckets": NotRequired[bool],
        "BlockPublicAcls": NotRequired[bool],
        "BlockPublicPolicy": NotRequired[bool],
    },
)
AccountStatisticsTypeDef = TypedDict(
    "AccountStatisticsTypeDef",
    {
        "AccountId": NotRequired[str],
        "LastGeneratedAt": NotRequired[datetime],
        "TotalFindings": NotRequired[int],
    },
)
DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": NotRequired[str],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
        "DomainWithSuffix": NotRequired[str],
    },
)
KubernetesPermissionCheckedDetailsTypeDef = TypedDict(
    "KubernetesPermissionCheckedDetailsTypeDef",
    {
        "Verb": NotRequired[str],
        "Resource": NotRequired[str],
        "Namespace": NotRequired[str],
        "Allowed": NotRequired[bool],
    },
)
KubernetesRoleBindingDetailsTypeDef = TypedDict(
    "KubernetesRoleBindingDetailsTypeDef",
    {
        "Kind": NotRequired[str],
        "Name": NotRequired[str],
        "Uid": NotRequired[str],
        "RoleRefName": NotRequired[str],
        "RoleRefKind": NotRequired[str],
    },
)
KubernetesRoleDetailsTypeDef = TypedDict(
    "KubernetesRoleDetailsTypeDef",
    {
        "Kind": NotRequired[str],
        "Name": NotRequired[str],
        "Uid": NotRequired[str],
    },
)
AddonDetailsTypeDef = TypedDict(
    "AddonDetailsTypeDef",
    {
        "AddonVersion": NotRequired[str],
        "AddonStatus": NotRequired[str],
    },
)
AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AdminAccountId": NotRequired[str],
        "AdminStatus": NotRequired[AdminStatusType],
    },
)
AdministratorTypeDef = TypedDict(
    "AdministratorTypeDef",
    {
        "AccountId": NotRequired[str],
        "InvitationId": NotRequired[str],
        "RelationshipStatus": NotRequired[str],
        "InvitedAt": NotRequired[str],
    },
)
AgentDetailsTypeDef = TypedDict(
    "AgentDetailsTypeDef",
    {
        "Version": NotRequired[str],
    },
)
ObservationsTypeDef = TypedDict(
    "ObservationsTypeDef",
    {
        "Text": NotRequired[List[str]],
    },
)
ArchiveFindingsRequestRequestTypeDef = TypedDict(
    "ArchiveFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": Sequence[str],
    },
)
DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "Domain": NotRequired[str],
    },
)
RemoteAccountDetailsTypeDef = TypedDict(
    "RemoteAccountDetailsTypeDef",
    {
        "AccountId": NotRequired[str],
        "Affiliated": NotRequired[bool],
    },
)
BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "AllowsPublicReadAccess": NotRequired[bool],
        "AllowsPublicWriteAccess": NotRequired[bool],
    },
)
CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": NotRequired[str],
    },
)
CloudTrailConfigurationResultTypeDef = TypedDict(
    "CloudTrailConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)
ConditionOutputTypeDef = TypedDict(
    "ConditionOutputTypeDef",
    {
        "Eq": NotRequired[List[str]],
        "Neq": NotRequired[List[str]],
        "Gt": NotRequired[int],
        "Gte": NotRequired[int],
        "Lt": NotRequired[int],
        "Lte": NotRequired[int],
        "Equals": NotRequired[List[str]],
        "NotEquals": NotRequired[List[str]],
        "GreaterThan": NotRequired[int],
        "GreaterThanOrEqual": NotRequired[int],
        "LessThan": NotRequired[int],
        "LessThanOrEqual": NotRequired[int],
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Eq": NotRequired[Sequence[str]],
        "Neq": NotRequired[Sequence[str]],
        "Gt": NotRequired[int],
        "Gte": NotRequired[int],
        "Lt": NotRequired[int],
        "Lte": NotRequired[int],
        "Equals": NotRequired[Sequence[str]],
        "NotEquals": NotRequired[Sequence[str]],
        "GreaterThan": NotRequired[int],
        "GreaterThanOrEqual": NotRequired[int],
        "LessThan": NotRequired[int],
        "LessThanOrEqual": NotRequired[int],
    },
)
ContainerInstanceDetailsTypeDef = TypedDict(
    "ContainerInstanceDetailsTypeDef",
    {
        "CoveredContainerInstances": NotRequired[int],
        "CompatibleContainerInstances": NotRequired[int],
    },
)
SecurityContextTypeDef = TypedDict(
    "SecurityContextTypeDef",
    {
        "Privileged": NotRequired[bool],
        "AllowPrivilegeEscalation": NotRequired[bool],
    },
)
VolumeMountTypeDef = TypedDict(
    "VolumeMountTypeDef",
    {
        "Name": NotRequired[str],
        "MountPath": NotRequired[str],
    },
)
CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": NotRequired[str],
        "CountryName": NotRequired[str],
    },
)
FargateDetailsTypeDef = TypedDict(
    "FargateDetailsTypeDef",
    {
        "Issues": NotRequired[List[str]],
        "ManagementType": NotRequired[ManagementTypeType],
    },
)
CoverageFilterConditionTypeDef = TypedDict(
    "CoverageFilterConditionTypeDef",
    {
        "Equals": NotRequired[Sequence[str]],
        "NotEquals": NotRequired[Sequence[str]],
    },
)
CoverageSortCriteriaTypeDef = TypedDict(
    "CoverageSortCriteriaTypeDef",
    {
        "AttributeName": NotRequired[CoverageSortKeyType],
        "OrderBy": NotRequired[OrderByType],
    },
)
CoverageStatisticsTypeDef = TypedDict(
    "CoverageStatisticsTypeDef",
    {
        "CountByResourceType": NotRequired[Dict[ResourceTypeType, int]],
        "CountByCoverageStatus": NotRequired[Dict[CoverageStatusType, int]],
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
CreateIPSetRequestRequestTypeDef = TypedDict(
    "CreateIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Activate": bool,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": str,
        "Result": str,
    },
)
CreateS3BucketResourceOutputTypeDef = TypedDict(
    "CreateS3BucketResourceOutputTypeDef",
    {
        "BucketName": NotRequired[str],
        "ObjectPrefixes": NotRequired[List[str]],
    },
)
DestinationPropertiesTypeDef = TypedDict(
    "DestinationPropertiesTypeDef",
    {
        "DestinationArn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
    },
)
CreateS3BucketResourceTypeDef = TypedDict(
    "CreateS3BucketResourceTypeDef",
    {
        "BucketName": NotRequired[str],
        "ObjectPrefixes": NotRequired[Sequence[str]],
    },
)
CreateSampleFindingsRequestRequestTypeDef = TypedDict(
    "CreateSampleFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingTypes": NotRequired[Sequence[str]],
    },
)
CreateThreatIntelSetRequestRequestTypeDef = TypedDict(
    "CreateThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Activate": bool,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DNSLogsConfigurationResultTypeDef = TypedDict(
    "DNSLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)
FlowLogsConfigurationResultTypeDef = TypedDict(
    "FlowLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)
S3LogsConfigurationResultTypeDef = TypedDict(
    "S3LogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)
S3LogsConfigurationTypeDef = TypedDict(
    "S3LogsConfigurationTypeDef",
    {
        "Enable": bool,
    },
)
DataSourceFreeTrialTypeDef = TypedDict(
    "DataSourceFreeTrialTypeDef",
    {
        "FreeTrialDaysRemaining": NotRequired[int],
    },
)
DateStatisticsTypeDef = TypedDict(
    "DateStatisticsTypeDef",
    {
        "Date": NotRequired[datetime],
        "LastGeneratedAt": NotRequired[datetime],
        "Severity": NotRequired[float],
        "TotalFindings": NotRequired[int],
    },
)
DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
DefaultServerSideEncryptionTypeDef = TypedDict(
    "DefaultServerSideEncryptionTypeDef",
    {
        "EncryptionType": NotRequired[str],
        "KmsMasterKeyArn": NotRequired[str],
    },
)
DeleteDetectorRequestRequestTypeDef = TypedDict(
    "DeleteDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)
DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)
DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
DeleteMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "DeleteMalwareProtectionPlanRequestRequestTypeDef",
    {
        "MalwareProtectionPlanId": str,
    },
)
DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)
DeletePublishingDestinationRequestRequestTypeDef = TypedDict(
    "DeletePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)
DeleteThreatIntelSetRequestRequestTypeDef = TypedDict(
    "DeleteThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
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
SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "AttributeName": NotRequired[str],
        "OrderBy": NotRequired[OrderByType],
    },
)
DescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribePublishingDestinationRequestRequestTypeDef = TypedDict(
    "DescribePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
    },
)
DetectorAdditionalConfigurationResultTypeDef = TypedDict(
    "DetectorAdditionalConfigurationResultTypeDef",
    {
        "Name": NotRequired[FeatureAdditionalConfigurationType],
        "Status": NotRequired[FeatureStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)
DetectorAdditionalConfigurationTypeDef = TypedDict(
    "DetectorAdditionalConfigurationTypeDef",
    {
        "Name": NotRequired[FeatureAdditionalConfigurationType],
        "Status": NotRequired[FeatureStatusType],
    },
)
DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)
DisassociateFromAdministratorAccountRequestRequestTypeDef = TypedDict(
    "DisassociateFromAdministratorAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
DisassociateFromMasterAccountRequestRequestTypeDef = TypedDict(
    "DisassociateFromMasterAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
DisassociateMembersRequestRequestTypeDef = TypedDict(
    "DisassociateMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)
VolumeDetailTypeDef = TypedDict(
    "VolumeDetailTypeDef",
    {
        "VolumeArn": NotRequired[str],
        "VolumeType": NotRequired[str],
        "DeviceName": NotRequired[str],
        "VolumeSizeInGB": NotRequired[int],
        "EncryptionType": NotRequired[str],
        "SnapshotArn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
    },
)
EbsVolumesResultTypeDef = TypedDict(
    "EbsVolumesResultTypeDef",
    {
        "Status": NotRequired[DataSourceStatusType],
        "Reason": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)
ThreatIntelligenceDetailTypeDef = TypedDict(
    "ThreatIntelligenceDetailTypeDef",
    {
        "ThreatListName": NotRequired[str],
        "ThreatNames": NotRequired[List[str]],
        "ThreatFileSha256": NotRequired[str],
    },
)
FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "EqualsValue": NotRequired[str],
        "GreaterThan": NotRequired[int],
        "LessThan": NotRequired[int],
    },
)
FindingTypeStatisticsTypeDef = TypedDict(
    "FindingTypeStatisticsTypeDef",
    {
        "FindingType": NotRequired[str],
        "LastGeneratedAt": NotRequired[datetime],
        "TotalFindings": NotRequired[int],
    },
)
ResourceStatisticsTypeDef = TypedDict(
    "ResourceStatisticsTypeDef",
    {
        "AccountId": NotRequired[str],
        "LastGeneratedAt": NotRequired[datetime],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "TotalFindings": NotRequired[int],
    },
)
SeverityStatisticsTypeDef = TypedDict(
    "SeverityStatisticsTypeDef",
    {
        "LastGeneratedAt": NotRequired[datetime],
        "Severity": NotRequired[float],
        "TotalFindings": NotRequired[int],
    },
)
GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lat": NotRequired[float],
        "Lon": NotRequired[float],
    },
)
GetAdministratorAccountRequestRequestTypeDef = TypedDict(
    "GetAdministratorAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
GetDetectorRequestRequestTypeDef = TypedDict(
    "GetDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
GetFilterRequestRequestTypeDef = TypedDict(
    "GetFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)
GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)
GetMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "GetMalwareProtectionPlanRequestRequestTypeDef",
    {
        "MalwareProtectionPlanId": str,
    },
)
MalwareProtectionPlanStatusReasonTypeDef = TypedDict(
    "MalwareProtectionPlanStatusReasonTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
GetMalwareScanSettingsRequestRequestTypeDef = TypedDict(
    "GetMalwareScanSettingsRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
GetMasterAccountRequestRequestTypeDef = TypedDict(
    "GetMasterAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
MasterTypeDef = TypedDict(
    "MasterTypeDef",
    {
        "AccountId": NotRequired[str],
        "InvitationId": NotRequired[str],
        "RelationshipStatus": NotRequired[str],
        "InvitedAt": NotRequired[str],
    },
)
GetMemberDetectorsRequestRequestTypeDef = TypedDict(
    "GetMemberDetectorsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)
GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "UpdatedAt": str,
        "DetectorId": NotRequired[str],
        "InvitedAt": NotRequired[str],
        "AdministratorId": NotRequired[str],
    },
)
GetRemainingFreeTrialDaysRequestRequestTypeDef = TypedDict(
    "GetRemainingFreeTrialDaysRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": NotRequired[Sequence[str]],
    },
)
GetThreatIntelSetRequestRequestTypeDef = TypedDict(
    "GetThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)
UsageCriteriaTypeDef = TypedDict(
    "UsageCriteriaTypeDef",
    {
        "AccountIds": NotRequired[Sequence[str]],
        "DataSources": NotRequired[Sequence[DataSourceType]],
        "Resources": NotRequired[Sequence[str]],
        "Features": NotRequired[Sequence[UsageFeatureType]],
    },
)
HighestSeverityThreatDetailsTypeDef = TypedDict(
    "HighestSeverityThreatDetailsTypeDef",
    {
        "Severity": NotRequired[str],
        "ThreatName": NotRequired[str],
        "Count": NotRequired[int],
    },
)
HostPathTypeDef = TypedDict(
    "HostPathTypeDef",
    {
        "Path": NotRequired[str],
    },
)
IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
    },
)
ImpersonatedUserTypeDef = TypedDict(
    "ImpersonatedUserTypeDef",
    {
        "Username": NotRequired[str],
        "Groups": NotRequired[List[str]],
    },
)
ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "Code": NotRequired[str],
        "ProductType": NotRequired[str],
    },
)
InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "AccountId": NotRequired[str],
        "InvitationId": NotRequired[str],
        "RelationshipStatus": NotRequired[str],
        "InvitedAt": NotRequired[str],
    },
)
InviteMembersRequestRequestTypeDef = TypedDict(
    "InviteMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
        "DisableEmailNotification": NotRequired[bool],
        "Message": NotRequired[str],
    },
)
ItemPathTypeDef = TypedDict(
    "ItemPathTypeDef",
    {
        "NestedItemPath": NotRequired[str],
        "Hash": NotRequired[str],
    },
)
KubernetesAuditLogsConfigurationResultTypeDef = TypedDict(
    "KubernetesAuditLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)
KubernetesAuditLogsConfigurationTypeDef = TypedDict(
    "KubernetesAuditLogsConfigurationTypeDef",
    {
        "Enable": bool,
    },
)
LineageObjectTypeDef = TypedDict(
    "LineageObjectTypeDef",
    {
        "StartTime": NotRequired[datetime],
        "NamespacePid": NotRequired[int],
        "UserId": NotRequired[int],
        "Name": NotRequired[str],
        "Pid": NotRequired[int],
        "Uuid": NotRequired[str],
        "ExecutablePath": NotRequired[str],
        "Euid": NotRequired[int],
        "ParentUuid": NotRequired[str],
    },
)
ListDetectorsRequestRequestTypeDef = TypedDict(
    "ListDetectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFiltersRequestRequestTypeDef = TypedDict(
    "ListFiltersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListIPSetsRequestRequestTypeDef = TypedDict(
    "ListIPSetsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMalwareProtectionPlansRequestRequestTypeDef = TypedDict(
    "ListMalwareProtectionPlansRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
MalwareProtectionPlanSummaryTypeDef = TypedDict(
    "MalwareProtectionPlanSummaryTypeDef",
    {
        "MalwareProtectionPlanId": NotRequired[str],
    },
)
ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OnlyAssociated": NotRequired[str],
    },
)
ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPublishingDestinationsRequestRequestTypeDef = TypedDict(
    "ListPublishingDestinationsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListThreatIntelSetsRequestRequestTypeDef = TypedDict(
    "ListThreatIntelSetsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
LocalIpDetailsTypeDef = TypedDict(
    "LocalIpDetailsTypeDef",
    {
        "IpAddressV4": NotRequired[str],
        "IpAddressV6": NotRequired[str],
    },
)
LocalPortDetailsTypeDef = TypedDict(
    "LocalPortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)
LoginAttributeTypeDef = TypedDict(
    "LoginAttributeTypeDef",
    {
        "User": NotRequired[str],
        "Application": NotRequired[str],
        "FailedLoginAttempts": NotRequired[int],
        "SuccessfulLoginAttempts": NotRequired[int],
    },
)
ScanEc2InstanceWithFindingsTypeDef = TypedDict(
    "ScanEc2InstanceWithFindingsTypeDef",
    {
        "EbsVolumes": NotRequired[bool],
    },
)
MalwareProtectionPlanTaggingActionTypeDef = TypedDict(
    "MalwareProtectionPlanTaggingActionTypeDef",
    {
        "Status": NotRequired[MalwareProtectionPlanTaggingActionStatusType],
    },
)
MemberAdditionalConfigurationResultTypeDef = TypedDict(
    "MemberAdditionalConfigurationResultTypeDef",
    {
        "Name": NotRequired[OrgFeatureAdditionalConfigurationType],
        "Status": NotRequired[FeatureStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)
MemberAdditionalConfigurationTypeDef = TypedDict(
    "MemberAdditionalConfigurationTypeDef",
    {
        "Name": NotRequired[OrgFeatureAdditionalConfigurationType],
        "Status": NotRequired[FeatureStatusType],
    },
)
RemotePortDetailsTypeDef = TypedDict(
    "RemotePortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)
PrivateIpAddressDetailsTypeDef = TypedDict(
    "PrivateIpAddressDetailsTypeDef",
    {
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)
SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)
OrganizationAdditionalConfigurationResultTypeDef = TypedDict(
    "OrganizationAdditionalConfigurationResultTypeDef",
    {
        "Name": NotRequired[OrgFeatureAdditionalConfigurationType],
        "AutoEnable": NotRequired[OrgFeatureStatusType],
    },
)
OrganizationAdditionalConfigurationTypeDef = TypedDict(
    "OrganizationAdditionalConfigurationTypeDef",
    {
        "Name": NotRequired[OrgFeatureAdditionalConfigurationType],
        "AutoEnable": NotRequired[OrgFeatureStatusType],
    },
)
OrganizationS3LogsConfigurationResultTypeDef = TypedDict(
    "OrganizationS3LogsConfigurationResultTypeDef",
    {
        "AutoEnable": bool,
    },
)
OrganizationS3LogsConfigurationTypeDef = TypedDict(
    "OrganizationS3LogsConfigurationTypeDef",
    {
        "AutoEnable": bool,
    },
)
OrganizationEbsVolumesResultTypeDef = TypedDict(
    "OrganizationEbsVolumesResultTypeDef",
    {
        "AutoEnable": NotRequired[bool],
    },
)
OrganizationEbsVolumesTypeDef = TypedDict(
    "OrganizationEbsVolumesTypeDef",
    {
        "AutoEnable": NotRequired[bool],
    },
)
OrganizationFeatureStatisticsAdditionalConfigurationTypeDef = TypedDict(
    "OrganizationFeatureStatisticsAdditionalConfigurationTypeDef",
    {
        "Name": NotRequired[OrgFeatureAdditionalConfigurationType],
        "EnabledAccountsCount": NotRequired[int],
    },
)
OrganizationKubernetesAuditLogsConfigurationResultTypeDef = TypedDict(
    "OrganizationKubernetesAuditLogsConfigurationResultTypeDef",
    {
        "AutoEnable": bool,
    },
)
OrganizationKubernetesAuditLogsConfigurationTypeDef = TypedDict(
    "OrganizationKubernetesAuditLogsConfigurationTypeDef",
    {
        "AutoEnable": bool,
    },
)
OrganizationTypeDef = TypedDict(
    "OrganizationTypeDef",
    {
        "Asn": NotRequired[str],
        "AsnOrg": NotRequired[str],
        "Isp": NotRequired[str],
        "Org": NotRequired[str],
    },
)
OwnerTypeDef = TypedDict(
    "OwnerTypeDef",
    {
        "Id": NotRequired[str],
    },
)
RdsDbUserDetailsTypeDef = TypedDict(
    "RdsDbUserDetailsTypeDef",
    {
        "User": NotRequired[str],
        "Application": NotRequired[str],
        "Database": NotRequired[str],
        "Ssl": NotRequired[str],
        "AuthMethod": NotRequired[str],
    },
)
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "InstanceArn": NotRequired[str],
    },
)
S3ObjectDetailTypeDef = TypedDict(
    "S3ObjectDetailTypeDef",
    {
        "ObjectArn": NotRequired[str],
        "Key": NotRequired[str],
        "ETag": NotRequired[str],
        "Hash": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)
ScanConditionPairTypeDef = TypedDict(
    "ScanConditionPairTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
ScannedItemCountTypeDef = TypedDict(
    "ScannedItemCountTypeDef",
    {
        "TotalGb": NotRequired[int],
        "Files": NotRequired[int],
        "Volumes": NotRequired[int],
    },
)
ThreatsDetectedItemCountTypeDef = TypedDict(
    "ThreatsDetectedItemCountTypeDef",
    {
        "Files": NotRequired[int],
    },
)
ScanFilePathTypeDef = TypedDict(
    "ScanFilePathTypeDef",
    {
        "FilePath": NotRequired[str],
        "VolumeArn": NotRequired[str],
        "Hash": NotRequired[str],
        "FileName": NotRequired[str],
    },
)
ScanResultDetailsTypeDef = TypedDict(
    "ScanResultDetailsTypeDef",
    {
        "ScanResult": NotRequired[ScanResultType],
    },
)
TriggerDetailsTypeDef = TypedDict(
    "TriggerDetailsTypeDef",
    {
        "GuardDutyFindingId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ServiceAdditionalInfoTypeDef = TypedDict(
    "ServiceAdditionalInfoTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[str],
    },
)
StartMalwareScanRequestRequestTypeDef = TypedDict(
    "StartMalwareScanRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
StartMonitoringMembersRequestRequestTypeDef = TypedDict(
    "StartMonitoringMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)
StopMonitoringMembersRequestRequestTypeDef = TypedDict(
    "StopMonitoringMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
TotalTypeDef = TypedDict(
    "TotalTypeDef",
    {
        "Amount": NotRequired[str],
        "Unit": NotRequired[str],
    },
)
UnarchiveFindingsRequestRequestTypeDef = TypedDict(
    "UnarchiveFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": Sequence[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateFindingsFeedbackRequestRequestTypeDef = TypedDict(
    "UpdateFindingsFeedbackRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": Sequence[str],
        "Feedback": FeedbackType,
        "Comments": NotRequired[str],
    },
)
UpdateIPSetRequestRequestTypeDef = TypedDict(
    "UpdateIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
        "Name": NotRequired[str],
        "Location": NotRequired[str],
        "Activate": NotRequired[bool],
    },
)
UpdateS3BucketResourceTypeDef = TypedDict(
    "UpdateS3BucketResourceTypeDef",
    {
        "ObjectPrefixes": NotRequired[Sequence[str]],
    },
)
UpdateThreatIntelSetRequestRequestTypeDef = TypedDict(
    "UpdateThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
        "Name": NotRequired[str],
        "Location": NotRequired[str],
        "Activate": NotRequired[bool],
    },
)
CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountDetails": Sequence[AccountDetailTypeDef],
    },
)
AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "BlockPublicAccess": NotRequired[BlockPublicAccessTypeDef],
    },
)
CoverageEksClusterDetailsTypeDef = TypedDict(
    "CoverageEksClusterDetailsTypeDef",
    {
        "ClusterName": NotRequired[str],
        "CoveredNodes": NotRequired[int],
        "CompatibleNodes": NotRequired[int],
        "AddonDetails": NotRequired[AddonDetailsTypeDef],
        "ManagementType": NotRequired[ManagementTypeType],
    },
)
CoverageEc2InstanceDetailsTypeDef = TypedDict(
    "CoverageEc2InstanceDetailsTypeDef",
    {
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "ClusterArn": NotRequired[str],
        "AgentDetails": NotRequired[AgentDetailsTypeDef],
        "ManagementType": NotRequired[ManagementTypeType],
    },
)
AnomalyObjectTypeDef = TypedDict(
    "AnomalyObjectTypeDef",
    {
        "ProfileType": NotRequired[Literal["FREQUENCY"]],
        "ProfileSubtype": NotRequired[ProfileSubtypeType],
        "Observations": NotRequired[ObservationsTypeDef],
    },
)
BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "AccessControlList": NotRequired[AccessControlListTypeDef],
        "BucketPolicy": NotRequired[BucketPolicyTypeDef],
        "BlockPublicAccess": NotRequired[BlockPublicAccessTypeDef],
    },
)
FindingCriteriaOutputTypeDef = TypedDict(
    "FindingCriteriaOutputTypeDef",
    {
        "Criterion": NotRequired[Dict[str, ConditionOutputTypeDef]],
    },
)
ConditionUnionTypeDef = Union[ConditionTypeDef, ConditionOutputTypeDef]
ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "ContainerRuntime": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Image": NotRequired[str],
        "ImagePrefix": NotRequired[str],
        "VolumeMounts": NotRequired[List[VolumeMountTypeDef]],
        "SecurityContext": NotRequired[SecurityContextTypeDef],
    },
)
CoverageEcsClusterDetailsTypeDef = TypedDict(
    "CoverageEcsClusterDetailsTypeDef",
    {
        "ClusterName": NotRequired[str],
        "FargateDetails": NotRequired[FargateDetailsTypeDef],
        "ContainerInstanceDetails": NotRequired[ContainerInstanceDetailsTypeDef],
    },
)
CoverageFilterCriterionTypeDef = TypedDict(
    "CoverageFilterCriterionTypeDef",
    {
        "CriterionKey": NotRequired[CoverageFilterCriterionKeyType],
        "FilterCondition": NotRequired[CoverageFilterConditionTypeDef],
    },
)
CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "IpSetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMalwareProtectionPlanResponseTypeDef = TypedDict(
    "CreateMalwareProtectionPlanResponseTypeDef",
    {
        "MalwareProtectionPlanId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePublishingDestinationResponseTypeDef = TypedDict(
    "CreatePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateThreatIntelSetResponseTypeDef = TypedDict(
    "CreateThreatIntelSetResponseTypeDef",
    {
        "ThreatIntelSetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "Administrator": AdministratorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCoverageStatisticsResponseTypeDef = TypedDict(
    "GetCoverageStatisticsResponseTypeDef",
    {
        "CoverageStatistics": CoverageStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Status": IpSetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "InvitationsCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetThreatIntelSetResponseTypeDef = TypedDict(
    "GetThreatIntelSetResponseTypeDef",
    {
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Status": ThreatIntelSetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDetectorsResponseTypeDef = TypedDict(
    "ListDetectorsResponseTypeDef",
    {
        "DetectorIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "FilterNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "FindingIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "IpSetIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "AdminAccounts": List[AdminAccountTypeDef],
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
ListThreatIntelSetsResponseTypeDef = TypedDict(
    "ListThreatIntelSetsResponseTypeDef",
    {
        "ThreatIntelSetIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartMalwareScanResponseTypeDef = TypedDict(
    "StartMalwareScanResponseTypeDef",
    {
        "ScanId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFilterResponseTypeDef = TypedDict(
    "UpdateFilterResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateMembersResponseTypeDef = TypedDict(
    "DisassociateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMonitoringMembersResponseTypeDef = TypedDict(
    "StartMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopMonitoringMembersResponseTypeDef = TypedDict(
    "StopMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMemberDetectorsResponseTypeDef = TypedDict(
    "UpdateMemberDetectorsResponseTypeDef",
    {
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProtectedResourceOutputTypeDef = TypedDict(
    "CreateProtectedResourceOutputTypeDef",
    {
        "S3Bucket": NotRequired[CreateS3BucketResourceOutputTypeDef],
    },
)
CreatePublishingDestinationRequestRequestTypeDef = TypedDict(
    "CreatePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationType": Literal["S3"],
        "DestinationProperties": DestinationPropertiesTypeDef,
        "ClientToken": NotRequired[str],
    },
)
DescribePublishingDestinationResponseTypeDef = TypedDict(
    "DescribePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
        "PublishingFailureStartTimestamp": int,
        "DestinationProperties": DestinationPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePublishingDestinationRequestRequestTypeDef = TypedDict(
    "UpdatePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
        "DestinationProperties": NotRequired[DestinationPropertiesTypeDef],
    },
)
CreateS3BucketResourceUnionTypeDef = Union[
    CreateS3BucketResourceTypeDef, CreateS3BucketResourceOutputTypeDef
]
KubernetesDataSourceFreeTrialTypeDef = TypedDict(
    "KubernetesDataSourceFreeTrialTypeDef",
    {
        "AuditLogs": NotRequired[DataSourceFreeTrialTypeDef],
    },
)
MalwareProtectionDataSourceFreeTrialTypeDef = TypedDict(
    "MalwareProtectionDataSourceFreeTrialTypeDef",
    {
        "ScanEc2InstanceWithFindings": NotRequired[DataSourceFreeTrialTypeDef],
    },
)
ListDetectorsRequestListDetectorsPaginateTypeDef = TypedDict(
    "ListDetectorsRequestListDetectorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFiltersRequestListFiltersPaginateTypeDef = TypedDict(
    "ListFiltersRequestListFiltersPaginateTypeDef",
    {
        "DetectorId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIPSetsRequestListIPSetsPaginateTypeDef = TypedDict(
    "ListIPSetsRequestListIPSetsPaginateTypeDef",
    {
        "DetectorId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInvitationsRequestListInvitationsPaginateTypeDef = TypedDict(
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMembersRequestListMembersPaginateTypeDef = TypedDict(
    "ListMembersRequestListMembersPaginateTypeDef",
    {
        "DetectorId": str,
        "OnlyAssociated": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListThreatIntelSetsRequestListThreatIntelSetsPaginateTypeDef = TypedDict(
    "ListThreatIntelSetsRequestListThreatIntelSetsPaginateTypeDef",
    {
        "DetectorId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": Sequence[str],
        "SortCriteria": NotRequired[SortCriteriaTypeDef],
    },
)
ListPublishingDestinationsResponseTypeDef = TypedDict(
    "ListPublishingDestinationsResponseTypeDef",
    {
        "Destinations": List[DestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DetectorFeatureConfigurationResultTypeDef = TypedDict(
    "DetectorFeatureConfigurationResultTypeDef",
    {
        "Name": NotRequired[DetectorFeatureResultType],
        "Status": NotRequired[FeatureStatusType],
        "UpdatedAt": NotRequired[datetime],
        "AdditionalConfiguration": NotRequired[List[DetectorAdditionalConfigurationResultTypeDef]],
    },
)
DetectorFeatureConfigurationTypeDef = TypedDict(
    "DetectorFeatureConfigurationTypeDef",
    {
        "Name": NotRequired[DetectorFeatureType],
        "Status": NotRequired[FeatureStatusType],
        "AdditionalConfiguration": NotRequired[Sequence[DetectorAdditionalConfigurationTypeDef]],
    },
)
EbsVolumeDetailsTypeDef = TypedDict(
    "EbsVolumeDetailsTypeDef",
    {
        "ScannedVolumeDetails": NotRequired[List[VolumeDetailTypeDef]],
        "SkippedVolumeDetails": NotRequired[List[VolumeDetailTypeDef]],
    },
)
ScanEc2InstanceWithFindingsResultTypeDef = TypedDict(
    "ScanEc2InstanceWithFindingsResultTypeDef",
    {
        "EbsVolumes": NotRequired[EbsVolumesResultTypeDef],
    },
)
EksClusterDetailsTypeDef = TypedDict(
    "EksClusterDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "VpcId": NotRequired[str],
        "Status": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "CreatedAt": NotRequired[datetime],
    },
)
RdsDbInstanceDetailsTypeDef = TypedDict(
    "RdsDbInstanceDetailsTypeDef",
    {
        "DbInstanceIdentifier": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DbClusterIdentifier": NotRequired[str],
        "DbInstanceArn": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "ThreatIntelligenceDetails": NotRequired[List[ThreatIntelligenceDetailTypeDef]],
    },
)
FilterCriterionTypeDef = TypedDict(
    "FilterCriterionTypeDef",
    {
        "CriterionKey": NotRequired[CriterionKeyType],
        "FilterCondition": NotRequired[FilterConditionTypeDef],
    },
)
FindingStatisticsTypeDef = TypedDict(
    "FindingStatisticsTypeDef",
    {
        "CountBySeverity": NotRequired[Dict[str, int]],
        "GroupedByAccount": NotRequired[List[AccountStatisticsTypeDef]],
        "GroupedByDate": NotRequired[List[DateStatisticsTypeDef]],
        "GroupedByFindingType": NotRequired[List[FindingTypeStatisticsTypeDef]],
        "GroupedByResource": NotRequired[List[ResourceStatisticsTypeDef]],
        "GroupedBySeverity": NotRequired[List[SeverityStatisticsTypeDef]],
    },
)
GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": MasterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List[MemberTypeDef],
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "Members": List[MemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetUsageStatisticsRequestRequestTypeDef = TypedDict(
    "GetUsageStatisticsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "UsageStatisticType": UsageStatisticTypeType,
        "UsageCriteria": UsageCriteriaTypeDef,
        "Unit": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "Name": NotRequired[str],
        "HostPath": NotRequired[HostPathTypeDef],
    },
)
KubernetesUserDetailsTypeDef = TypedDict(
    "KubernetesUserDetailsTypeDef",
    {
        "Username": NotRequired[str],
        "Uid": NotRequired[str],
        "Groups": NotRequired[List[str]],
        "SessionName": NotRequired[List[str]],
        "ImpersonatedUser": NotRequired[ImpersonatedUserTypeDef],
    },
)
ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List[InvitationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ThreatTypeDef = TypedDict(
    "ThreatTypeDef",
    {
        "Name": NotRequired[str],
        "Source": NotRequired[str],
        "ItemPaths": NotRequired[List[ItemPathTypeDef]],
    },
)
KubernetesConfigurationResultTypeDef = TypedDict(
    "KubernetesConfigurationResultTypeDef",
    {
        "AuditLogs": KubernetesAuditLogsConfigurationResultTypeDef,
    },
)
KubernetesConfigurationTypeDef = TypedDict(
    "KubernetesConfigurationTypeDef",
    {
        "AuditLogs": KubernetesAuditLogsConfigurationTypeDef,
    },
)
ProcessDetailsTypeDef = TypedDict(
    "ProcessDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "ExecutablePath": NotRequired[str],
        "ExecutableSha256": NotRequired[str],
        "NamespacePid": NotRequired[int],
        "Pwd": NotRequired[str],
        "Pid": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "Uuid": NotRequired[str],
        "ParentUuid": NotRequired[str],
        "User": NotRequired[str],
        "UserId": NotRequired[int],
        "Euid": NotRequired[int],
        "Lineage": NotRequired[List[LineageObjectTypeDef]],
    },
)
ListMalwareProtectionPlansResponseTypeDef = TypedDict(
    "ListMalwareProtectionPlansResponseTypeDef",
    {
        "MalwareProtectionPlans": List[MalwareProtectionPlanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MalwareProtectionConfigurationTypeDef = TypedDict(
    "MalwareProtectionConfigurationTypeDef",
    {
        "ScanEc2InstanceWithFindings": NotRequired[ScanEc2InstanceWithFindingsTypeDef],
    },
)
MalwareProtectionPlanActionsTypeDef = TypedDict(
    "MalwareProtectionPlanActionsTypeDef",
    {
        "Tagging": NotRequired[MalwareProtectionPlanTaggingActionTypeDef],
    },
)
MemberFeaturesConfigurationResultTypeDef = TypedDict(
    "MemberFeaturesConfigurationResultTypeDef",
    {
        "Name": NotRequired[OrgFeatureType],
        "Status": NotRequired[FeatureStatusType],
        "UpdatedAt": NotRequired[datetime],
        "AdditionalConfiguration": NotRequired[List[MemberAdditionalConfigurationResultTypeDef]],
    },
)
MemberFeaturesConfigurationTypeDef = TypedDict(
    "MemberFeaturesConfigurationTypeDef",
    {
        "Name": NotRequired[OrgFeatureType],
        "Status": NotRequired[FeatureStatusType],
        "AdditionalConfiguration": NotRequired[Sequence[MemberAdditionalConfigurationTypeDef]],
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Ipv6Addresses": NotRequired[List[str]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List[PrivateIpAddressDetailsTypeDef]],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
        "SecurityGroups": NotRequired[List[SecurityGroupTypeDef]],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": NotRequired[List[str]],
        "VpcId": NotRequired[str],
        "SecurityGroups": NotRequired[List[SecurityGroupTypeDef]],
    },
)
OrganizationFeatureConfigurationResultTypeDef = TypedDict(
    "OrganizationFeatureConfigurationResultTypeDef",
    {
        "Name": NotRequired[OrgFeatureType],
        "AutoEnable": NotRequired[OrgFeatureStatusType],
        "AdditionalConfiguration": NotRequired[
            List[OrganizationAdditionalConfigurationResultTypeDef]
        ],
    },
)
OrganizationFeatureConfigurationTypeDef = TypedDict(
    "OrganizationFeatureConfigurationTypeDef",
    {
        "Name": NotRequired[OrgFeatureType],
        "AutoEnable": NotRequired[OrgFeatureStatusType],
        "AdditionalConfiguration": NotRequired[
            Sequence[OrganizationAdditionalConfigurationTypeDef]
        ],
    },
)
OrganizationScanEc2InstanceWithFindingsResultTypeDef = TypedDict(
    "OrganizationScanEc2InstanceWithFindingsResultTypeDef",
    {
        "EbsVolumes": NotRequired[OrganizationEbsVolumesResultTypeDef],
    },
)
OrganizationScanEc2InstanceWithFindingsTypeDef = TypedDict(
    "OrganizationScanEc2InstanceWithFindingsTypeDef",
    {
        "EbsVolumes": NotRequired[OrganizationEbsVolumesTypeDef],
    },
)
OrganizationFeatureStatisticsTypeDef = TypedDict(
    "OrganizationFeatureStatisticsTypeDef",
    {
        "Name": NotRequired[OrgFeatureType],
        "EnabledAccountsCount": NotRequired[int],
        "AdditionalConfiguration": NotRequired[
            List[OrganizationFeatureStatisticsAdditionalConfigurationTypeDef]
        ],
    },
)
OrganizationKubernetesConfigurationResultTypeDef = TypedDict(
    "OrganizationKubernetesConfigurationResultTypeDef",
    {
        "AuditLogs": OrganizationKubernetesAuditLogsConfigurationResultTypeDef,
    },
)
OrganizationKubernetesConfigurationTypeDef = TypedDict(
    "OrganizationKubernetesConfigurationTypeDef",
    {
        "AuditLogs": OrganizationKubernetesAuditLogsConfigurationTypeDef,
    },
)
RemoteIpDetailsTypeDef = TypedDict(
    "RemoteIpDetailsTypeDef",
    {
        "City": NotRequired[CityTypeDef],
        "Country": NotRequired[CountryTypeDef],
        "GeoLocation": NotRequired[GeoLocationTypeDef],
        "IpAddressV4": NotRequired[str],
        "IpAddressV6": NotRequired[str],
        "Organization": NotRequired[OrganizationTypeDef],
    },
)
ScanConditionOutputTypeDef = TypedDict(
    "ScanConditionOutputTypeDef",
    {
        "MapEquals": List[ScanConditionPairTypeDef],
    },
)
ScanConditionTypeDef = TypedDict(
    "ScanConditionTypeDef",
    {
        "MapEquals": Sequence[ScanConditionPairTypeDef],
    },
)
ScanThreatNameTypeDef = TypedDict(
    "ScanThreatNameTypeDef",
    {
        "Name": NotRequired[str],
        "Severity": NotRequired[str],
        "ItemCount": NotRequired[int],
        "FilePaths": NotRequired[List[ScanFilePathTypeDef]],
    },
)
ScanTypeDef = TypedDict(
    "ScanTypeDef",
    {
        "DetectorId": NotRequired[str],
        "AdminDetectorId": NotRequired[str],
        "ScanId": NotRequired[str],
        "ScanStatus": NotRequired[ScanStatusType],
        "FailureReason": NotRequired[str],
        "ScanStartTime": NotRequired[datetime],
        "ScanEndTime": NotRequired[datetime],
        "TriggerDetails": NotRequired[TriggerDetailsTypeDef],
        "ResourceDetails": NotRequired[ResourceDetailsTypeDef],
        "ScanResultDetails": NotRequired[ScanResultDetailsTypeDef],
        "AccountId": NotRequired[str],
        "TotalBytes": NotRequired[int],
        "FileCount": NotRequired[int],
        "AttachedVolumes": NotRequired[List[VolumeDetailTypeDef]],
        "ScanType": NotRequired[ScanTypeType],
    },
)
UsageAccountResultTypeDef = TypedDict(
    "UsageAccountResultTypeDef",
    {
        "AccountId": NotRequired[str],
        "Total": NotRequired[TotalTypeDef],
    },
)
UsageDataSourceResultTypeDef = TypedDict(
    "UsageDataSourceResultTypeDef",
    {
        "DataSource": NotRequired[DataSourceType],
        "Total": NotRequired[TotalTypeDef],
    },
)
UsageFeatureResultTypeDef = TypedDict(
    "UsageFeatureResultTypeDef",
    {
        "Feature": NotRequired[UsageFeatureType],
        "Total": NotRequired[TotalTypeDef],
    },
)
UsageResourceResultTypeDef = TypedDict(
    "UsageResourceResultTypeDef",
    {
        "Resource": NotRequired[str],
        "Total": NotRequired[TotalTypeDef],
    },
)
UsageTopAccountResultTypeDef = TypedDict(
    "UsageTopAccountResultTypeDef",
    {
        "AccountId": NotRequired[str],
        "Total": NotRequired[TotalTypeDef],
    },
)
UpdateProtectedResourceTypeDef = TypedDict(
    "UpdateProtectedResourceTypeDef",
    {
        "S3Bucket": NotRequired[UpdateS3BucketResourceTypeDef],
    },
)
AnomalyUnusualTypeDef = TypedDict(
    "AnomalyUnusualTypeDef",
    {
        "Behavior": NotRequired[Dict[str, Dict[str, AnomalyObjectTypeDef]]],
    },
)
PermissionConfigurationTypeDef = TypedDict(
    "PermissionConfigurationTypeDef",
    {
        "BucketLevelPermissions": NotRequired[BucketLevelPermissionsTypeDef],
        "AccountLevelPermissions": NotRequired[AccountLevelPermissionsTypeDef],
    },
)
GetFilterResponseTypeDef = TypedDict(
    "GetFilterResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": FilterActionType,
        "Rank": int,
        "FindingCriteria": FindingCriteriaOutputTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "Criterion": NotRequired[Mapping[str, ConditionUnionTypeDef]],
    },
)
CoverageResourceDetailsTypeDef = TypedDict(
    "CoverageResourceDetailsTypeDef",
    {
        "EksClusterDetails": NotRequired[CoverageEksClusterDetailsTypeDef],
        "ResourceType": NotRequired[ResourceTypeType],
        "EcsClusterDetails": NotRequired[CoverageEcsClusterDetailsTypeDef],
        "Ec2InstanceDetails": NotRequired[CoverageEc2InstanceDetailsTypeDef],
    },
)
CoverageFilterCriteriaTypeDef = TypedDict(
    "CoverageFilterCriteriaTypeDef",
    {
        "FilterCriterion": NotRequired[Sequence[CoverageFilterCriterionTypeDef]],
    },
)
CreateProtectedResourceTypeDef = TypedDict(
    "CreateProtectedResourceTypeDef",
    {
        "S3Bucket": NotRequired[CreateS3BucketResourceUnionTypeDef],
    },
)
DataSourcesFreeTrialTypeDef = TypedDict(
    "DataSourcesFreeTrialTypeDef",
    {
        "CloudTrail": NotRequired[DataSourceFreeTrialTypeDef],
        "DnsLogs": NotRequired[DataSourceFreeTrialTypeDef],
        "FlowLogs": NotRequired[DataSourceFreeTrialTypeDef],
        "S3Logs": NotRequired[DataSourceFreeTrialTypeDef],
        "Kubernetes": NotRequired[KubernetesDataSourceFreeTrialTypeDef],
        "MalwareProtection": NotRequired[MalwareProtectionDataSourceFreeTrialTypeDef],
    },
)
MalwareProtectionConfigurationResultTypeDef = TypedDict(
    "MalwareProtectionConfigurationResultTypeDef",
    {
        "ScanEc2InstanceWithFindings": NotRequired[ScanEc2InstanceWithFindingsResultTypeDef],
        "ServiceRole": NotRequired[str],
    },
)
FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "FilterCriterion": NotRequired[Sequence[FilterCriterionTypeDef]],
    },
)
GetFindingsStatisticsResponseTypeDef = TypedDict(
    "GetFindingsStatisticsResponseTypeDef",
    {
        "FindingStatistics": FindingStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EcsTaskDetailsTypeDef = TypedDict(
    "EcsTaskDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "DefinitionArn": NotRequired[str],
        "Version": NotRequired[str],
        "TaskCreatedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
        "StartedBy": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "Volumes": NotRequired[List[VolumeTypeDef]],
        "Containers": NotRequired[List[ContainerTypeDef]],
        "Group": NotRequired[str],
        "LaunchType": NotRequired[str],
    },
)
KubernetesWorkloadDetailsTypeDef = TypedDict(
    "KubernetesWorkloadDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Uid": NotRequired[str],
        "Namespace": NotRequired[str],
        "HostNetwork": NotRequired[bool],
        "Containers": NotRequired[List[ContainerTypeDef]],
        "Volumes": NotRequired[List[VolumeTypeDef]],
        "ServiceAccountName": NotRequired[str],
        "HostIPC": NotRequired[bool],
        "HostPID": NotRequired[bool],
    },
)
MalwareScanDetailsTypeDef = TypedDict(
    "MalwareScanDetailsTypeDef",
    {
        "Threats": NotRequired[List[ThreatTypeDef]],
    },
)
RuntimeContextTypeDef = TypedDict(
    "RuntimeContextTypeDef",
    {
        "ModifyingProcess": NotRequired[ProcessDetailsTypeDef],
        "ModifiedAt": NotRequired[datetime],
        "ScriptPath": NotRequired[str],
        "LibraryPath": NotRequired[str],
        "LdPreloadValue": NotRequired[str],
        "SocketPath": NotRequired[str],
        "RuncBinaryPath": NotRequired[str],
        "ReleaseAgentPath": NotRequired[str],
        "MountSource": NotRequired[str],
        "MountTarget": NotRequired[str],
        "FileSystemType": NotRequired[str],
        "Flags": NotRequired[List[str]],
        "ModuleName": NotRequired[str],
        "ModuleFilePath": NotRequired[str],
        "ModuleSha256": NotRequired[str],
        "ShellHistoryFilePath": NotRequired[str],
        "TargetProcess": NotRequired[ProcessDetailsTypeDef],
        "AddressFamily": NotRequired[str],
        "IanaProtocolNumber": NotRequired[int],
        "MemoryRegions": NotRequired[List[str]],
        "ToolName": NotRequired[str],
        "ToolCategory": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CommandLineExample": NotRequired[str],
        "ThreatFilePath": NotRequired[str],
    },
)
DataSourceConfigurationsTypeDef = TypedDict(
    "DataSourceConfigurationsTypeDef",
    {
        "S3Logs": NotRequired[S3LogsConfigurationTypeDef],
        "Kubernetes": NotRequired[KubernetesConfigurationTypeDef],
        "MalwareProtection": NotRequired[MalwareProtectionConfigurationTypeDef],
    },
)
GetMalwareProtectionPlanResponseTypeDef = TypedDict(
    "GetMalwareProtectionPlanResponseTypeDef",
    {
        "Arn": str,
        "Role": str,
        "ProtectedResource": CreateProtectedResourceOutputTypeDef,
        "Actions": MalwareProtectionPlanActionsTypeDef,
        "CreatedAt": datetime,
        "Status": MalwareProtectionPlanStatusType,
        "StatusReasons": List[MalwareProtectionPlanStatusReasonTypeDef],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "IamInstanceProfile": NotRequired[IamInstanceProfileTypeDef],
        "ImageDescription": NotRequired[str],
        "ImageId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceState": NotRequired[str],
        "InstanceType": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "LaunchTime": NotRequired[str],
        "NetworkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
        "Platform": NotRequired[str],
        "ProductCodes": NotRequired[List[ProductCodeTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
LambdaDetailsTypeDef = TypedDict(
    "LambdaDetailsTypeDef",
    {
        "FunctionArn": NotRequired[str],
        "FunctionName": NotRequired[str],
        "Description": NotRequired[str],
        "LastModifiedAt": NotRequired[datetime],
        "RevisionId": NotRequired[str],
        "FunctionVersion": NotRequired[str],
        "Role": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
OrganizationMalwareProtectionConfigurationResultTypeDef = TypedDict(
    "OrganizationMalwareProtectionConfigurationResultTypeDef",
    {
        "ScanEc2InstanceWithFindings": NotRequired[
            OrganizationScanEc2InstanceWithFindingsResultTypeDef
        ],
    },
)
OrganizationMalwareProtectionConfigurationTypeDef = TypedDict(
    "OrganizationMalwareProtectionConfigurationTypeDef",
    {
        "ScanEc2InstanceWithFindings": NotRequired[OrganizationScanEc2InstanceWithFindingsTypeDef],
    },
)
OrganizationStatisticsTypeDef = TypedDict(
    "OrganizationStatisticsTypeDef",
    {
        "TotalAccountsCount": NotRequired[int],
        "MemberAccountsCount": NotRequired[int],
        "ActiveAccountsCount": NotRequired[int],
        "EnabledAccountsCount": NotRequired[int],
        "CountByFeature": NotRequired[List[OrganizationFeatureStatisticsTypeDef]],
    },
)
AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": NotRequired[str],
        "CallerType": NotRequired[str],
        "DomainDetails": NotRequired[DomainDetailsTypeDef],
        "ErrorCode": NotRequired[str],
        "UserAgent": NotRequired[str],
        "RemoteIpDetails": NotRequired[RemoteIpDetailsTypeDef],
        "ServiceName": NotRequired[str],
        "RemoteAccountDetails": NotRequired[RemoteAccountDetailsTypeDef],
        "AffectedResources": NotRequired[Dict[str, str]],
    },
)
KubernetesApiCallActionTypeDef = TypedDict(
    "KubernetesApiCallActionTypeDef",
    {
        "RequestUri": NotRequired[str],
        "Verb": NotRequired[str],
        "SourceIps": NotRequired[List[str]],
        "UserAgent": NotRequired[str],
        "RemoteIpDetails": NotRequired[RemoteIpDetailsTypeDef],
        "StatusCode": NotRequired[int],
        "Parameters": NotRequired[str],
        "Resource": NotRequired[str],
        "Subresource": NotRequired[str],
        "Namespace": NotRequired[str],
        "ResourceName": NotRequired[str],
    },
)
NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "Blocked": NotRequired[bool],
        "ConnectionDirection": NotRequired[str],
        "LocalPortDetails": NotRequired[LocalPortDetailsTypeDef],
        "Protocol": NotRequired[str],
        "LocalIpDetails": NotRequired[LocalIpDetailsTypeDef],
        "LocalNetworkInterface": NotRequired[str],
        "RemoteIpDetails": NotRequired[RemoteIpDetailsTypeDef],
        "RemotePortDetails": NotRequired[RemotePortDetailsTypeDef],
    },
)
PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": NotRequired[LocalPortDetailsTypeDef],
        "LocalIpDetails": NotRequired[LocalIpDetailsTypeDef],
        "RemoteIpDetails": NotRequired[RemoteIpDetailsTypeDef],
    },
)
RdsLoginAttemptActionTypeDef = TypedDict(
    "RdsLoginAttemptActionTypeDef",
    {
        "RemoteIpDetails": NotRequired[RemoteIpDetailsTypeDef],
        "LoginAttributes": NotRequired[List[LoginAttributeTypeDef]],
    },
)
ScanResourceCriteriaOutputTypeDef = TypedDict(
    "ScanResourceCriteriaOutputTypeDef",
    {
        "Include": NotRequired[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionOutputTypeDef]],
        "Exclude": NotRequired[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionOutputTypeDef]],
    },
)
ScanConditionUnionTypeDef = Union[ScanConditionTypeDef, ScanConditionOutputTypeDef]
ThreatDetectedByNameTypeDef = TypedDict(
    "ThreatDetectedByNameTypeDef",
    {
        "ItemCount": NotRequired[int],
        "UniqueThreatNameCount": NotRequired[int],
        "Shortened": NotRequired[bool],
        "ThreatNames": NotRequired[List[ScanThreatNameTypeDef]],
    },
)
DescribeMalwareScansResponseTypeDef = TypedDict(
    "DescribeMalwareScansResponseTypeDef",
    {
        "Scans": List[ScanTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UsageTopAccountsResultTypeDef = TypedDict(
    "UsageTopAccountsResultTypeDef",
    {
        "Feature": NotRequired[UsageFeatureType],
        "Accounts": NotRequired[List[UsageTopAccountResultTypeDef]],
    },
)
UpdateMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "UpdateMalwareProtectionPlanRequestRequestTypeDef",
    {
        "MalwareProtectionPlanId": str,
        "Role": NotRequired[str],
        "Actions": NotRequired[MalwareProtectionPlanActionsTypeDef],
        "ProtectedResource": NotRequired[UpdateProtectedResourceTypeDef],
    },
)
AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "Profiles": NotRequired[Dict[str, Dict[str, List[AnomalyObjectTypeDef]]]],
        "Unusual": NotRequired[AnomalyUnusualTypeDef],
    },
)
PublicAccessTypeDef = TypedDict(
    "PublicAccessTypeDef",
    {
        "PermissionConfiguration": NotRequired[PermissionConfigurationTypeDef],
        "EffectivePermission": NotRequired[str],
    },
)
CreateFilterRequestRequestTypeDef = TypedDict(
    "CreateFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "FindingCriteria": FindingCriteriaTypeDef,
        "Description": NotRequired[str],
        "Action": NotRequired[FilterActionType],
        "Rank": NotRequired[int],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
GetFindingsStatisticsRequestRequestTypeDef = TypedDict(
    "GetFindingsStatisticsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingStatisticTypes": NotRequired[Sequence[Literal["COUNT_BY_SEVERITY"]]],
        "FindingCriteria": NotRequired[FindingCriteriaTypeDef],
        "GroupBy": NotRequired[GroupByTypeType],
        "OrderBy": NotRequired[OrderByType],
        "MaxResults": NotRequired[int],
    },
)
ListFindingsRequestListFindingsPaginateTypeDef = TypedDict(
    "ListFindingsRequestListFindingsPaginateTypeDef",
    {
        "DetectorId": str,
        "FindingCriteria": NotRequired[FindingCriteriaTypeDef],
        "SortCriteria": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingCriteria": NotRequired[FindingCriteriaTypeDef],
        "SortCriteria": NotRequired[SortCriteriaTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
UpdateFilterRequestRequestTypeDef = TypedDict(
    "UpdateFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
        "Description": NotRequired[str],
        "Action": NotRequired[FilterActionType],
        "Rank": NotRequired[int],
        "FindingCriteria": NotRequired[FindingCriteriaTypeDef],
    },
)
CoverageResourceTypeDef = TypedDict(
    "CoverageResourceTypeDef",
    {
        "ResourceId": NotRequired[str],
        "DetectorId": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceDetails": NotRequired[CoverageResourceDetailsTypeDef],
        "CoverageStatus": NotRequired[CoverageStatusType],
        "Issue": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
    },
)
GetCoverageStatisticsRequestRequestTypeDef = TypedDict(
    "GetCoverageStatisticsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "StatisticsType": Sequence[CoverageStatisticsTypeType],
        "FilterCriteria": NotRequired[CoverageFilterCriteriaTypeDef],
    },
)
ListCoverageRequestListCoveragePaginateTypeDef = TypedDict(
    "ListCoverageRequestListCoveragePaginateTypeDef",
    {
        "DetectorId": str,
        "FilterCriteria": NotRequired[CoverageFilterCriteriaTypeDef],
        "SortCriteria": NotRequired[CoverageSortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCoverageRequestRequestTypeDef = TypedDict(
    "ListCoverageRequestRequestTypeDef",
    {
        "DetectorId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "FilterCriteria": NotRequired[CoverageFilterCriteriaTypeDef],
        "SortCriteria": NotRequired[CoverageSortCriteriaTypeDef],
    },
)
CreateMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "CreateMalwareProtectionPlanRequestRequestTypeDef",
    {
        "Role": str,
        "ProtectedResource": CreateProtectedResourceTypeDef,
        "ClientToken": NotRequired[str],
        "Actions": NotRequired[MalwareProtectionPlanActionsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
AccountFreeTrialInfoTypeDef = TypedDict(
    "AccountFreeTrialInfoTypeDef",
    {
        "AccountId": NotRequired[str],
        "DataSources": NotRequired[DataSourcesFreeTrialTypeDef],
        "Features": NotRequired[List[FreeTrialFeatureConfigurationResultTypeDef]],
    },
)
DataSourceConfigurationsResultTypeDef = TypedDict(
    "DataSourceConfigurationsResultTypeDef",
    {
        "CloudTrail": CloudTrailConfigurationResultTypeDef,
        "DNSLogs": DNSLogsConfigurationResultTypeDef,
        "FlowLogs": FlowLogsConfigurationResultTypeDef,
        "S3Logs": S3LogsConfigurationResultTypeDef,
        "Kubernetes": NotRequired[KubernetesConfigurationResultTypeDef],
        "MalwareProtection": NotRequired[MalwareProtectionConfigurationResultTypeDef],
    },
)
UnprocessedDataSourcesResultTypeDef = TypedDict(
    "UnprocessedDataSourcesResultTypeDef",
    {
        "MalwareProtection": NotRequired[MalwareProtectionConfigurationResultTypeDef],
    },
)
DescribeMalwareScansRequestDescribeMalwareScansPaginateTypeDef = TypedDict(
    "DescribeMalwareScansRequestDescribeMalwareScansPaginateTypeDef",
    {
        "DetectorId": str,
        "FilterCriteria": NotRequired[FilterCriteriaTypeDef],
        "SortCriteria": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMalwareScansRequestRequestTypeDef = TypedDict(
    "DescribeMalwareScansRequestRequestTypeDef",
    {
        "DetectorId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "FilterCriteria": NotRequired[FilterCriteriaTypeDef],
        "SortCriteria": NotRequired[SortCriteriaTypeDef],
    },
)
EcsClusterDetailsTypeDef = TypedDict(
    "EcsClusterDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Status": NotRequired[str],
        "ActiveServicesCount": NotRequired[int],
        "RegisteredContainerInstancesCount": NotRequired[int],
        "RunningTasksCount": NotRequired[int],
        "Tags": NotRequired[List[TagTypeDef]],
        "TaskDetails": NotRequired[EcsTaskDetailsTypeDef],
    },
)
KubernetesDetailsTypeDef = TypedDict(
    "KubernetesDetailsTypeDef",
    {
        "KubernetesUserDetails": NotRequired[KubernetesUserDetailsTypeDef],
        "KubernetesWorkloadDetails": NotRequired[KubernetesWorkloadDetailsTypeDef],
    },
)
RuntimeDetailsTypeDef = TypedDict(
    "RuntimeDetailsTypeDef",
    {
        "Process": NotRequired[ProcessDetailsTypeDef],
        "Context": NotRequired[RuntimeContextTypeDef],
    },
)
CreateDetectorRequestRequestTypeDef = TypedDict(
    "CreateDetectorRequestRequestTypeDef",
    {
        "Enable": bool,
        "ClientToken": NotRequired[str],
        "FindingPublishingFrequency": NotRequired[FindingPublishingFrequencyType],
        "DataSources": NotRequired[DataSourceConfigurationsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "Features": NotRequired[Sequence[DetectorFeatureConfigurationTypeDef]],
    },
)
UpdateDetectorRequestRequestTypeDef = TypedDict(
    "UpdateDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Enable": NotRequired[bool],
        "FindingPublishingFrequency": NotRequired[FindingPublishingFrequencyType],
        "DataSources": NotRequired[DataSourceConfigurationsTypeDef],
        "Features": NotRequired[Sequence[DetectorFeatureConfigurationTypeDef]],
    },
)
UpdateMemberDetectorsRequestRequestTypeDef = TypedDict(
    "UpdateMemberDetectorsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
        "DataSources": NotRequired[DataSourceConfigurationsTypeDef],
        "Features": NotRequired[Sequence[MemberFeaturesConfigurationTypeDef]],
    },
)
OrganizationDataSourceConfigurationsResultTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsResultTypeDef",
    {
        "S3Logs": OrganizationS3LogsConfigurationResultTypeDef,
        "Kubernetes": NotRequired[OrganizationKubernetesConfigurationResultTypeDef],
        "MalwareProtection": NotRequired[OrganizationMalwareProtectionConfigurationResultTypeDef],
    },
)
OrganizationDataSourceConfigurationsTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsTypeDef",
    {
        "S3Logs": NotRequired[OrganizationS3LogsConfigurationTypeDef],
        "Kubernetes": NotRequired[OrganizationKubernetesConfigurationTypeDef],
        "MalwareProtection": NotRequired[OrganizationMalwareProtectionConfigurationTypeDef],
    },
)
OrganizationDetailsTypeDef = TypedDict(
    "OrganizationDetailsTypeDef",
    {
        "UpdatedAt": NotRequired[datetime],
        "OrganizationStatistics": NotRequired[OrganizationStatisticsTypeDef],
    },
)
PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "Blocked": NotRequired[bool],
        "PortProbeDetails": NotRequired[List[PortProbeDetailTypeDef]],
    },
)
GetMalwareScanSettingsResponseTypeDef = TypedDict(
    "GetMalwareScanSettingsResponseTypeDef",
    {
        "ScanResourceCriteria": ScanResourceCriteriaOutputTypeDef,
        "EbsSnapshotPreservation": EbsSnapshotPreservationType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScanResourceCriteriaTypeDef = TypedDict(
    "ScanResourceCriteriaTypeDef",
    {
        "Include": NotRequired[Mapping[Literal["EC2_INSTANCE_TAG"], ScanConditionUnionTypeDef]],
        "Exclude": NotRequired[Mapping[Literal["EC2_INSTANCE_TAG"], ScanConditionTypeDef]],
    },
)
ScanDetectionsTypeDef = TypedDict(
    "ScanDetectionsTypeDef",
    {
        "ScannedItemCount": NotRequired[ScannedItemCountTypeDef],
        "ThreatsDetectedItemCount": NotRequired[ThreatsDetectedItemCountTypeDef],
        "HighestSeverityThreatDetails": NotRequired[HighestSeverityThreatDetailsTypeDef],
        "ThreatDetectedByName": NotRequired[ThreatDetectedByNameTypeDef],
    },
)
UsageStatisticsTypeDef = TypedDict(
    "UsageStatisticsTypeDef",
    {
        "SumByAccount": NotRequired[List[UsageAccountResultTypeDef]],
        "TopAccountsByFeature": NotRequired[List[UsageTopAccountsResultTypeDef]],
        "SumByDataSource": NotRequired[List[UsageDataSourceResultTypeDef]],
        "SumByResource": NotRequired[List[UsageResourceResultTypeDef]],
        "TopResources": NotRequired[List[UsageResourceResultTypeDef]],
        "SumByFeature": NotRequired[List[UsageFeatureResultTypeDef]],
    },
)
DetectionTypeDef = TypedDict(
    "DetectionTypeDef",
    {
        "Anomaly": NotRequired[AnomalyTypeDef],
    },
)
S3BucketDetailTypeDef = TypedDict(
    "S3BucketDetailTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Owner": NotRequired[OwnerTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "DefaultServerSideEncryption": NotRequired[DefaultServerSideEncryptionTypeDef],
        "PublicAccess": NotRequired[PublicAccessTypeDef],
        "S3ObjectDetails": NotRequired[List[S3ObjectDetailTypeDef]],
    },
)
ListCoverageResponseTypeDef = TypedDict(
    "ListCoverageResponseTypeDef",
    {
        "Resources": List[CoverageResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetRemainingFreeTrialDaysResponseTypeDef = TypedDict(
    "GetRemainingFreeTrialDaysResponseTypeDef",
    {
        "Accounts": List[AccountFreeTrialInfoTypeDef],
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDetectorResponseTypeDef = TypedDict(
    "GetDetectorResponseTypeDef",
    {
        "CreatedAt": str,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "ServiceRole": str,
        "Status": DetectorStatusType,
        "UpdatedAt": str,
        "DataSources": DataSourceConfigurationsResultTypeDef,
        "Tags": Dict[str, str],
        "Features": List[DetectorFeatureConfigurationResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MemberDataSourceConfigurationTypeDef = TypedDict(
    "MemberDataSourceConfigurationTypeDef",
    {
        "AccountId": str,
        "DataSources": NotRequired[DataSourceConfigurationsResultTypeDef],
        "Features": NotRequired[List[MemberFeaturesConfigurationResultTypeDef]],
    },
)
CreateDetectorResponseTypeDef = TypedDict(
    "CreateDetectorResponseTypeDef",
    {
        "DetectorId": str,
        "UnprocessedDataSources": UnprocessedDataSourcesResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "DataSources": OrganizationDataSourceConfigurationsResultTypeDef,
        "Features": List[OrganizationFeatureConfigurationResultTypeDef],
        "AutoEnableOrganizationMembers": AutoEnableMembersType,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AutoEnable": NotRequired[bool],
        "DataSources": NotRequired[OrganizationDataSourceConfigurationsTypeDef],
        "Features": NotRequired[Sequence[OrganizationFeatureConfigurationTypeDef]],
        "AutoEnableOrganizationMembers": NotRequired[AutoEnableMembersType],
    },
)
GetOrganizationStatisticsResponseTypeDef = TypedDict(
    "GetOrganizationStatisticsResponseTypeDef",
    {
        "OrganizationDetails": OrganizationDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": NotRequired[str],
        "AwsApiCallAction": NotRequired[AwsApiCallActionTypeDef],
        "DnsRequestAction": NotRequired[DnsRequestActionTypeDef],
        "NetworkConnectionAction": NotRequired[NetworkConnectionActionTypeDef],
        "PortProbeAction": NotRequired[PortProbeActionTypeDef],
        "KubernetesApiCallAction": NotRequired[KubernetesApiCallActionTypeDef],
        "RdsLoginAttemptAction": NotRequired[RdsLoginAttemptActionTypeDef],
        "KubernetesPermissionCheckedDetails": NotRequired[
            KubernetesPermissionCheckedDetailsTypeDef
        ],
        "KubernetesRoleBindingDetails": NotRequired[KubernetesRoleBindingDetailsTypeDef],
        "KubernetesRoleDetails": NotRequired[KubernetesRoleDetailsTypeDef],
    },
)
UpdateMalwareScanSettingsRequestRequestTypeDef = TypedDict(
    "UpdateMalwareScanSettingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ScanResourceCriteria": NotRequired[ScanResourceCriteriaTypeDef],
        "EbsSnapshotPreservation": NotRequired[EbsSnapshotPreservationType],
    },
)
EbsVolumeScanDetailsTypeDef = TypedDict(
    "EbsVolumeScanDetailsTypeDef",
    {
        "ScanId": NotRequired[str],
        "ScanStartedAt": NotRequired[datetime],
        "ScanCompletedAt": NotRequired[datetime],
        "TriggerFindingId": NotRequired[str],
        "Sources": NotRequired[List[str]],
        "ScanDetections": NotRequired[ScanDetectionsTypeDef],
        "ScanType": NotRequired[ScanTypeType],
    },
)
GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {
        "UsageStatistics": UsageStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "AccessKeyDetails": NotRequired[AccessKeyDetailsTypeDef],
        "S3BucketDetails": NotRequired[List[S3BucketDetailTypeDef]],
        "InstanceDetails": NotRequired[InstanceDetailsTypeDef],
        "EksClusterDetails": NotRequired[EksClusterDetailsTypeDef],
        "KubernetesDetails": NotRequired[KubernetesDetailsTypeDef],
        "ResourceType": NotRequired[str],
        "EbsVolumeDetails": NotRequired[EbsVolumeDetailsTypeDef],
        "EcsClusterDetails": NotRequired[EcsClusterDetailsTypeDef],
        "ContainerDetails": NotRequired[ContainerTypeDef],
        "RdsDbInstanceDetails": NotRequired[RdsDbInstanceDetailsTypeDef],
        "RdsDbUserDetails": NotRequired[RdsDbUserDetailsTypeDef],
        "LambdaDetails": NotRequired[LambdaDetailsTypeDef],
    },
)
GetMemberDetectorsResponseTypeDef = TypedDict(
    "GetMemberDetectorsResponseTypeDef",
    {
        "MemberDataSourceConfigurations": List[MemberDataSourceConfigurationTypeDef],
        "UnprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Action": NotRequired[ActionTypeDef],
        "Evidence": NotRequired[EvidenceTypeDef],
        "Archived": NotRequired[bool],
        "Count": NotRequired[int],
        "DetectorId": NotRequired[str],
        "EventFirstSeen": NotRequired[str],
        "EventLastSeen": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "ServiceName": NotRequired[str],
        "UserFeedback": NotRequired[str],
        "AdditionalInfo": NotRequired[ServiceAdditionalInfoTypeDef],
        "FeatureName": NotRequired[str],
        "EbsVolumeScanDetails": NotRequired[EbsVolumeScanDetailsTypeDef],
        "RuntimeDetails": NotRequired[RuntimeDetailsTypeDef],
        "Detection": NotRequired[DetectionTypeDef],
        "MalwareScanDetails": NotRequired[MalwareScanDetailsTypeDef],
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "Region": str,
        "Resource": ResourceTypeDef,
        "SchemaVersion": str,
        "Severity": float,
        "Type": str,
        "UpdatedAt": str,
        "Confidence": NotRequired[float],
        "Description": NotRequired[str],
        "Partition": NotRequired[str],
        "Service": NotRequired[ServiceTypeDef],
        "Title": NotRequired[str],
    },
)
GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List[FindingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
