"""
Type annotations for lightsail service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/type_defs/)

Usage::

    ```python
    from mypy_boto3_lightsail.type_defs import AccessKeyLastUsedTypeDef

    data: AccessKeyLastUsedTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AccessDirectionType,
    AccessTypeType,
    AccountLevelBpaSyncStatusType,
    AddOnTypeType,
    AlarmStateType,
    AutoMountStatusType,
    AutoSnapshotStatusType,
    BehaviorEnumType,
    BlueprintTypeType,
    BPAStatusMessageType,
    BucketMetricNameType,
    CertificateDomainValidationStatusType,
    CertificateStatusType,
    ComparisonOperatorType,
    ContactMethodStatusType,
    ContactProtocolType,
    ContainerServiceDeploymentStateType,
    ContainerServiceMetricNameType,
    ContainerServicePowerNameType,
    ContainerServiceProtocolType,
    ContainerServiceStateDetailCodeType,
    ContainerServiceStateType,
    DiskSnapshotStateType,
    DiskStateType,
    DistributionMetricNameType,
    DnsRecordCreationStateCodeType,
    ExportSnapshotRecordSourceTypeType,
    ForwardValuesType,
    HeaderEnumType,
    HttpEndpointType,
    HttpProtocolIpv6Type,
    HttpTokensType,
    InstanceAccessProtocolType,
    InstanceHealthReasonType,
    InstanceHealthStateType,
    InstanceMetadataStateType,
    InstanceMetricNameType,
    InstancePlatformType,
    InstanceSnapshotStateType,
    IpAddressTypeType,
    LoadBalancerAttributeNameType,
    LoadBalancerMetricNameType,
    LoadBalancerProtocolType,
    LoadBalancerStateType,
    LoadBalancerTlsCertificateDnsRecordCreationStateCodeType,
    LoadBalancerTlsCertificateDomainStatusType,
    LoadBalancerTlsCertificateFailureReasonType,
    LoadBalancerTlsCertificateRenewalStatusType,
    LoadBalancerTlsCertificateRevocationReasonType,
    LoadBalancerTlsCertificateStatusType,
    MetricNameType,
    MetricStatisticType,
    MetricUnitType,
    NameServersUpdateStateCodeType,
    NetworkProtocolType,
    OperationStatusType,
    OperationTypeType,
    OriginProtocolPolicyEnumType,
    PortAccessTypeType,
    PortInfoSourceTypeType,
    PortStateType,
    PricingUnitType,
    R53HostedZoneDeletionStateCodeType,
    RecordStateType,
    RegionNameType,
    RelationalDatabaseMetricNameType,
    RelationalDatabasePasswordVersionType,
    RenewalStatusType,
    ResourceBucketAccessType,
    ResourceTypeType,
    SetupStatusType,
    StatusType,
    StatusTypeType,
    TreatMissingDataType,
    ViewerMinimumTlsProtocolVersionEnumType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AccessKeyLastUsedTypeDef",
    "AccessRulesTypeDef",
    "AccountLevelBpaSyncTypeDef",
    "AutoSnapshotAddOnRequestTypeDef",
    "StopInstanceOnIdleRequestTypeDef",
    "AddOnTypeDef",
    "MonitoredResourceInfoTypeDef",
    "ResourceLocationTypeDef",
    "AllocateStaticIpRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AttachCertificateToDistributionRequestRequestTypeDef",
    "AttachDiskRequestRequestTypeDef",
    "AttachInstancesToLoadBalancerRequestRequestTypeDef",
    "AttachLoadBalancerTlsCertificateRequestRequestTypeDef",
    "AttachStaticIpRequestRequestTypeDef",
    "AttachedDiskTypeDef",
    "AvailabilityZoneTypeDef",
    "BlueprintTypeDef",
    "BucketAccessLogConfigTypeDef",
    "BucketBundleTypeDef",
    "BucketStateTypeDef",
    "ResourceReceivingAccessTypeDef",
    "TagTypeDef",
    "BundleTypeDef",
    "CacheBehaviorPerPathTypeDef",
    "CacheBehaviorTypeDef",
    "CookieObjectOutputTypeDef",
    "HeaderObjectOutputTypeDef",
    "QueryStringObjectOutputTypeDef",
    "PortInfoTypeDef",
    "CloudFormationStackRecordSourceInfoTypeDef",
    "DestinationInfoTypeDef",
    "ContainerImageTypeDef",
    "ContainerOutputTypeDef",
    "ContainerServiceECRImagePullerRoleRequestTypeDef",
    "ContainerServiceECRImagePullerRoleTypeDef",
    "ContainerServiceHealthCheckConfigTypeDef",
    "ContainerServiceLogEventTypeDef",
    "ContainerServicePowerTypeDef",
    "ContainerServiceRegistryLoginTypeDef",
    "ContainerServiceStateDetailTypeDef",
    "ContainerTypeDef",
    "CookieObjectTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CreateBucketAccessKeyRequestRequestTypeDef",
    "InstanceEntryTypeDef",
    "CreateContactMethodRequestRequestTypeDef",
    "InputOriginTypeDef",
    "DomainEntryTypeDef",
    "CreateGUISessionAccessDetailsRequestRequestTypeDef",
    "SessionTypeDef",
    "DiskMapTypeDef",
    "TimestampTypeDef",
    "DeleteAlarmRequestRequestTypeDef",
    "DeleteAutoSnapshotRequestRequestTypeDef",
    "DeleteBucketAccessKeyRequestRequestTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "DeleteContactMethodRequestRequestTypeDef",
    "DeleteContainerImageRequestRequestTypeDef",
    "DeleteContainerServiceRequestRequestTypeDef",
    "DeleteDiskRequestRequestTypeDef",
    "DeleteDiskSnapshotRequestRequestTypeDef",
    "DeleteDistributionRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteInstanceSnapshotRequestRequestTypeDef",
    "DeleteKeyPairRequestRequestTypeDef",
    "DeleteKnownHostKeysRequestRequestTypeDef",
    "DeleteLoadBalancerRequestRequestTypeDef",
    "DeleteLoadBalancerTlsCertificateRequestRequestTypeDef",
    "DeleteRelationalDatabaseRequestRequestTypeDef",
    "DeleteRelationalDatabaseSnapshotRequestRequestTypeDef",
    "DetachCertificateFromDistributionRequestRequestTypeDef",
    "DetachDiskRequestRequestTypeDef",
    "DetachInstancesFromLoadBalancerRequestRequestTypeDef",
    "DetachStaticIpRequestRequestTypeDef",
    "DisableAddOnRequestRequestTypeDef",
    "DiskInfoTypeDef",
    "DiskSnapshotInfoTypeDef",
    "DistributionBundleTypeDef",
    "DnsRecordCreationStateTypeDef",
    "DomainEntryOutputTypeDef",
    "ResourceRecordTypeDef",
    "TimePeriodTypeDef",
    "ExportSnapshotRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetActiveNamesRequestRequestTypeDef",
    "GetAlarmsRequestRequestTypeDef",
    "GetAutoSnapshotsRequestRequestTypeDef",
    "GetBlueprintsRequestRequestTypeDef",
    "GetBucketAccessKeysRequestRequestTypeDef",
    "GetBucketBundlesRequestRequestTypeDef",
    "MetricDatapointTypeDef",
    "GetBucketsRequestRequestTypeDef",
    "GetBundlesRequestRequestTypeDef",
    "GetCertificatesRequestRequestTypeDef",
    "GetCloudFormationStackRecordsRequestRequestTypeDef",
    "GetContactMethodsRequestRequestTypeDef",
    "GetContainerImagesRequestRequestTypeDef",
    "GetContainerServiceDeploymentsRequestRequestTypeDef",
    "GetContainerServicesRequestRequestTypeDef",
    "GetDiskRequestRequestTypeDef",
    "GetDiskSnapshotRequestRequestTypeDef",
    "GetDiskSnapshotsRequestRequestTypeDef",
    "GetDisksRequestRequestTypeDef",
    "GetDistributionLatestCacheResetRequestRequestTypeDef",
    "GetDistributionsRequestRequestTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetDomainsRequestRequestTypeDef",
    "GetExportSnapshotRecordsRequestRequestTypeDef",
    "GetInstanceAccessDetailsRequestRequestTypeDef",
    "GetInstancePortStatesRequestRequestTypeDef",
    "InstancePortStateTypeDef",
    "GetInstanceRequestRequestTypeDef",
    "GetInstanceSnapshotRequestRequestTypeDef",
    "GetInstanceSnapshotsRequestRequestTypeDef",
    "GetInstanceStateRequestRequestTypeDef",
    "InstanceStateTypeDef",
    "GetInstancesRequestRequestTypeDef",
    "GetKeyPairRequestRequestTypeDef",
    "GetKeyPairsRequestRequestTypeDef",
    "GetLoadBalancerRequestRequestTypeDef",
    "GetLoadBalancerTlsCertificatesRequestRequestTypeDef",
    "GetLoadBalancerTlsPoliciesRequestRequestTypeDef",
    "LoadBalancerTlsPolicyTypeDef",
    "GetLoadBalancersRequestRequestTypeDef",
    "GetOperationRequestRequestTypeDef",
    "GetOperationsForResourceRequestRequestTypeDef",
    "GetOperationsRequestRequestTypeDef",
    "GetRegionsRequestRequestTypeDef",
    "GetRelationalDatabaseBlueprintsRequestRequestTypeDef",
    "RelationalDatabaseBlueprintTypeDef",
    "GetRelationalDatabaseBundlesRequestRequestTypeDef",
    "RelationalDatabaseBundleTypeDef",
    "GetRelationalDatabaseEventsRequestRequestTypeDef",
    "RelationalDatabaseEventTypeDef",
    "LogEventTypeDef",
    "GetRelationalDatabaseLogStreamsRequestRequestTypeDef",
    "GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef",
    "GetRelationalDatabaseParametersRequestRequestTypeDef",
    "RelationalDatabaseParameterTypeDef",
    "GetRelationalDatabaseRequestRequestTypeDef",
    "GetRelationalDatabaseSnapshotRequestRequestTypeDef",
    "GetRelationalDatabaseSnapshotsRequestRequestTypeDef",
    "GetRelationalDatabasesRequestRequestTypeDef",
    "GetSetupHistoryRequestRequestTypeDef",
    "GetStaticIpRequestRequestTypeDef",
    "GetStaticIpsRequestRequestTypeDef",
    "HeaderObjectTypeDef",
    "HostKeyAttributesTypeDef",
    "ImportKeyPairRequestRequestTypeDef",
    "PasswordDataTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "InstancePortInfoTypeDef",
    "MonthlyTransferTypeDef",
    "OriginTypeDef",
    "LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef",
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    "LoadBalancerTlsCertificateSummaryTypeDef",
    "NameServersUpdateStateTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    "PutAlarmRequestRequestTypeDef",
    "QueryStringObjectTypeDef",
    "R53HostedZoneDeletionStateTypeDef",
    "RebootInstanceRequestRequestTypeDef",
    "RebootRelationalDatabaseRequestRequestTypeDef",
    "RegisterContainerImageRequestRequestTypeDef",
    "RelationalDatabaseEndpointTypeDef",
    "RelationalDatabaseHardwareTypeDef",
    "ReleaseStaticIpRequestRequestTypeDef",
    "ResetDistributionCacheRequestRequestTypeDef",
    "SendContactMethodVerificationRequestRequestTypeDef",
    "SetIpAddressTypeRequestRequestTypeDef",
    "SetResourceAccessForBucketRequestRequestTypeDef",
    "SetupExecutionDetailsTypeDef",
    "SetupRequestTypeDef",
    "SetupInstanceHttpsRequestRequestTypeDef",
    "StartGUISessionRequestRequestTypeDef",
    "StartInstanceRequestRequestTypeDef",
    "StartRelationalDatabaseRequestRequestTypeDef",
    "StopGUISessionRequestRequestTypeDef",
    "StopInstanceRequestRequestTypeDef",
    "StopRelationalDatabaseRequestRequestTypeDef",
    "TestAlarmRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBucketBundleRequestRequestTypeDef",
    "UpdateDistributionBundleRequestRequestTypeDef",
    "UpdateInstanceMetadataOptionsRequestRequestTypeDef",
    "UpdateLoadBalancerAttributeRequestRequestTypeDef",
    "UpdateRelationalDatabaseRequestRequestTypeDef",
    "AccessKeyTypeDef",
    "AddOnRequestTypeDef",
    "AlarmTypeDef",
    "ContactMethodTypeDef",
    "OperationTypeDef",
    "SetupHistoryResourceTypeDef",
    "StaticIpTypeDef",
    "DownloadDefaultKeyPairResultTypeDef",
    "GetActiveNamesResultTypeDef",
    "GetContainerAPIMetadataResultTypeDef",
    "GetDistributionLatestCacheResetResultTypeDef",
    "GetRelationalDatabaseLogStreamsResultTypeDef",
    "GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    "IsVpcPeeredResultTypeDef",
    "AutoSnapshotDetailsTypeDef",
    "RegionTypeDef",
    "GetBlueprintsResultTypeDef",
    "UpdateBucketRequestRequestTypeDef",
    "GetBucketBundlesResultTypeDef",
    "BucketTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "CreateCertificateRequestRequestTypeDef",
    "CreateDiskSnapshotRequestRequestTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateInstanceSnapshotRequestRequestTypeDef",
    "CreateKeyPairRequestRequestTypeDef",
    "CreateLoadBalancerRequestRequestTypeDef",
    "CreateLoadBalancerTlsCertificateRequestRequestTypeDef",
    "CreateRelationalDatabaseRequestRequestTypeDef",
    "CreateRelationalDatabaseSnapshotRequestRequestTypeDef",
    "DiskSnapshotTypeDef",
    "DiskTypeDef",
    "KeyPairTypeDef",
    "RelationalDatabaseSnapshotTypeDef",
    "TagResourceRequestRequestTypeDef",
    "GetBundlesResultTypeDef",
    "CacheSettingsOutputTypeDef",
    "CloseInstancePublicPortsRequestRequestTypeDef",
    "OpenInstancePublicPortsRequestRequestTypeDef",
    "PutInstancePublicPortsRequestRequestTypeDef",
    "CloudFormationStackRecordTypeDef",
    "GetContainerImagesResultTypeDef",
    "RegisterContainerImageResultTypeDef",
    "PrivateRegistryAccessRequestTypeDef",
    "PrivateRegistryAccessTypeDef",
    "ContainerServiceEndpointTypeDef",
    "EndpointRequestTypeDef",
    "GetContainerLogResultTypeDef",
    "GetContainerServicePowersResultTypeDef",
    "CreateContainerServiceRegistryLoginResultTypeDef",
    "ContainerUnionTypeDef",
    "CookieObjectUnionTypeDef",
    "CreateCloudFormationStackRequestRequestTypeDef",
    "CreateDomainEntryRequestRequestTypeDef",
    "DeleteDomainEntryRequestRequestTypeDef",
    "UpdateDomainEntryRequestRequestTypeDef",
    "CreateGUISessionAccessDetailsResultTypeDef",
    "CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef",
    "GetBucketMetricDataRequestRequestTypeDef",
    "GetContainerLogRequestRequestTypeDef",
    "GetContainerServiceMetricDataRequestRequestTypeDef",
    "GetCostEstimateRequestRequestTypeDef",
    "GetDistributionMetricDataRequestRequestTypeDef",
    "GetInstanceMetricDataRequestRequestTypeDef",
    "GetLoadBalancerMetricDataRequestRequestTypeDef",
    "GetRelationalDatabaseLogEventsRequestRequestTypeDef",
    "GetRelationalDatabaseMetricDataRequestRequestTypeDef",
    "InstanceSnapshotInfoTypeDef",
    "GetDistributionBundlesResultTypeDef",
    "DomainValidationRecordTypeDef",
    "EstimateByTimeTypeDef",
    "GetActiveNamesRequestGetActiveNamesPaginateTypeDef",
    "GetBlueprintsRequestGetBlueprintsPaginateTypeDef",
    "GetBundlesRequestGetBundlesPaginateTypeDef",
    "GetCloudFormationStackRecordsRequestGetCloudFormationStackRecordsPaginateTypeDef",
    "GetDiskSnapshotsRequestGetDiskSnapshotsPaginateTypeDef",
    "GetDisksRequestGetDisksPaginateTypeDef",
    "GetDomainsRequestGetDomainsPaginateTypeDef",
    "GetExportSnapshotRecordsRequestGetExportSnapshotRecordsPaginateTypeDef",
    "GetInstanceSnapshotsRequestGetInstanceSnapshotsPaginateTypeDef",
    "GetInstancesRequestGetInstancesPaginateTypeDef",
    "GetKeyPairsRequestGetKeyPairsPaginateTypeDef",
    "GetLoadBalancersRequestGetLoadBalancersPaginateTypeDef",
    "GetOperationsRequestGetOperationsPaginateTypeDef",
    "GetRelationalDatabaseBlueprintsRequestGetRelationalDatabaseBlueprintsPaginateTypeDef",
    "GetRelationalDatabaseBundlesRequestGetRelationalDatabaseBundlesPaginateTypeDef",
    "GetRelationalDatabaseEventsRequestGetRelationalDatabaseEventsPaginateTypeDef",
    "GetRelationalDatabaseParametersRequestGetRelationalDatabaseParametersPaginateTypeDef",
    "GetRelationalDatabaseSnapshotsRequestGetRelationalDatabaseSnapshotsPaginateTypeDef",
    "GetRelationalDatabasesRequestGetRelationalDatabasesPaginateTypeDef",
    "GetStaticIpsRequestGetStaticIpsPaginateTypeDef",
    "GetBucketMetricDataResultTypeDef",
    "GetContainerServiceMetricDataResultTypeDef",
    "GetDistributionMetricDataResultTypeDef",
    "GetInstanceMetricDataResultTypeDef",
    "GetLoadBalancerMetricDataResultTypeDef",
    "GetRelationalDatabaseMetricDataResultTypeDef",
    "GetInstancePortStatesResultTypeDef",
    "GetInstanceStateResultTypeDef",
    "GetLoadBalancerTlsPoliciesResultTypeDef",
    "GetRelationalDatabaseBlueprintsResultTypeDef",
    "GetRelationalDatabaseBundlesResultTypeDef",
    "GetRelationalDatabaseEventsResultTypeDef",
    "GetRelationalDatabaseLogEventsResultTypeDef",
    "GetRelationalDatabaseParametersResultTypeDef",
    "UpdateRelationalDatabaseParametersRequestRequestTypeDef",
    "HeaderObjectUnionTypeDef",
    "InstanceAccessDetailsTypeDef",
    "InstanceNetworkingTypeDef",
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    "LoadBalancerTypeDef",
    "QueryStringObjectUnionTypeDef",
    "RegisteredDomainDelegationInfoTypeDef",
    "RelationalDatabaseTypeDef",
    "GetBucketAccessKeysResultTypeDef",
    "CreateDiskFromSnapshotRequestRequestTypeDef",
    "CreateDiskRequestRequestTypeDef",
    "CreateInstancesFromSnapshotRequestRequestTypeDef",
    "CreateInstancesRequestRequestTypeDef",
    "EnableAddOnRequestRequestTypeDef",
    "GetAlarmsResultTypeDef",
    "GetContactMethodsResultTypeDef",
    "AllocateStaticIpResultTypeDef",
    "AttachCertificateToDistributionResultTypeDef",
    "AttachDiskResultTypeDef",
    "AttachInstancesToLoadBalancerResultTypeDef",
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    "AttachStaticIpResultTypeDef",
    "CloseInstancePublicPortsResultTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateBucketAccessKeyResultTypeDef",
    "CreateCloudFormationStackResultTypeDef",
    "CreateContactMethodResultTypeDef",
    "CreateDiskFromSnapshotResultTypeDef",
    "CreateDiskResultTypeDef",
    "CreateDiskSnapshotResultTypeDef",
    "CreateDomainEntryResultTypeDef",
    "CreateDomainResultTypeDef",
    "CreateInstanceSnapshotResultTypeDef",
    "CreateInstancesFromSnapshotResultTypeDef",
    "CreateInstancesResultTypeDef",
    "CreateLoadBalancerResultTypeDef",
    "CreateLoadBalancerTlsCertificateResultTypeDef",
    "CreateRelationalDatabaseFromSnapshotResultTypeDef",
    "CreateRelationalDatabaseResultTypeDef",
    "CreateRelationalDatabaseSnapshotResultTypeDef",
    "DeleteAlarmResultTypeDef",
    "DeleteAutoSnapshotResultTypeDef",
    "DeleteBucketAccessKeyResultTypeDef",
    "DeleteBucketResultTypeDef",
    "DeleteCertificateResultTypeDef",
    "DeleteContactMethodResultTypeDef",
    "DeleteDiskResultTypeDef",
    "DeleteDiskSnapshotResultTypeDef",
    "DeleteDistributionResultTypeDef",
    "DeleteDomainEntryResultTypeDef",
    "DeleteDomainResultTypeDef",
    "DeleteInstanceResultTypeDef",
    "DeleteInstanceSnapshotResultTypeDef",
    "DeleteKeyPairResultTypeDef",
    "DeleteKnownHostKeysResultTypeDef",
    "DeleteLoadBalancerResultTypeDef",
    "DeleteLoadBalancerTlsCertificateResultTypeDef",
    "DeleteRelationalDatabaseResultTypeDef",
    "DeleteRelationalDatabaseSnapshotResultTypeDef",
    "DetachCertificateFromDistributionResultTypeDef",
    "DetachDiskResultTypeDef",
    "DetachInstancesFromLoadBalancerResultTypeDef",
    "DetachStaticIpResultTypeDef",
    "DisableAddOnResultTypeDef",
    "EnableAddOnResultTypeDef",
    "ExportSnapshotResultTypeDef",
    "GetOperationResultTypeDef",
    "GetOperationsForResourceResultTypeDef",
    "GetOperationsResultTypeDef",
    "ImportKeyPairResultTypeDef",
    "OpenInstancePublicPortsResultTypeDef",
    "PeerVpcResultTypeDef",
    "PutAlarmResultTypeDef",
    "PutInstancePublicPortsResultTypeDef",
    "RebootInstanceResultTypeDef",
    "RebootRelationalDatabaseResultTypeDef",
    "ReleaseStaticIpResultTypeDef",
    "ResetDistributionCacheResultTypeDef",
    "SendContactMethodVerificationResultTypeDef",
    "SetIpAddressTypeResultTypeDef",
    "SetResourceAccessForBucketResultTypeDef",
    "SetupInstanceHttpsResultTypeDef",
    "StartGUISessionResultTypeDef",
    "StartInstanceResultTypeDef",
    "StartRelationalDatabaseResultTypeDef",
    "StopGUISessionResultTypeDef",
    "StopInstanceResultTypeDef",
    "StopRelationalDatabaseResultTypeDef",
    "TagResourceResultTypeDef",
    "TestAlarmResultTypeDef",
    "UnpeerVpcResultTypeDef",
    "UntagResourceResultTypeDef",
    "UpdateBucketBundleResultTypeDef",
    "UpdateDistributionBundleResultTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateDomainEntryResultTypeDef",
    "UpdateInstanceMetadataOptionsResultTypeDef",
    "UpdateLoadBalancerAttributeResultTypeDef",
    "UpdateRelationalDatabaseParametersResultTypeDef",
    "UpdateRelationalDatabaseResultTypeDef",
    "SetupHistoryTypeDef",
    "GetStaticIpResultTypeDef",
    "GetStaticIpsResultTypeDef",
    "GetAutoSnapshotsResultTypeDef",
    "GetRegionsResultTypeDef",
    "CreateBucketResultTypeDef",
    "GetBucketsResultTypeDef",
    "UpdateBucketResultTypeDef",
    "GetDiskSnapshotResultTypeDef",
    "GetDiskSnapshotsResultTypeDef",
    "GetDiskResultTypeDef",
    "GetDisksResultTypeDef",
    "InstanceHardwareTypeDef",
    "InstanceSnapshotTypeDef",
    "CreateKeyPairResultTypeDef",
    "GetKeyPairResultTypeDef",
    "GetKeyPairsResultTypeDef",
    "GetRelationalDatabaseSnapshotResultTypeDef",
    "GetRelationalDatabaseSnapshotsResultTypeDef",
    "LightsailDistributionTypeDef",
    "GetCloudFormationStackRecordsResultTypeDef",
    "UpdateContainerServiceRequestRequestTypeDef",
    "ContainerServiceDeploymentTypeDef",
    "ContainerServiceDeploymentRequestTypeDef",
    "CreateContainerServiceDeploymentRequestRequestTypeDef",
    "ExportSnapshotRecordSourceInfoTypeDef",
    "RenewalSummaryTypeDef",
    "CostEstimateTypeDef",
    "GetInstanceAccessDetailsResultTypeDef",
    "LoadBalancerTlsCertificateTypeDef",
    "GetLoadBalancerResultTypeDef",
    "GetLoadBalancersResultTypeDef",
    "CacheSettingsTypeDef",
    "DomainTypeDef",
    "GetRelationalDatabaseResultTypeDef",
    "GetRelationalDatabasesResultTypeDef",
    "GetSetupHistoryResultTypeDef",
    "InstanceTypeDef",
    "GetInstanceSnapshotResultTypeDef",
    "GetInstanceSnapshotsResultTypeDef",
    "CreateDistributionResultTypeDef",
    "GetDistributionsResultTypeDef",
    "ContainerServiceTypeDef",
    "GetContainerServiceDeploymentsResultTypeDef",
    "CreateContainerServiceRequestRequestTypeDef",
    "ExportSnapshotRecordTypeDef",
    "CertificateTypeDef",
    "ResourceBudgetEstimateTypeDef",
    "GetLoadBalancerTlsCertificatesResultTypeDef",
    "CreateDistributionRequestRequestTypeDef",
    "UpdateDistributionRequestRequestTypeDef",
    "GetDomainResultTypeDef",
    "GetDomainsResultTypeDef",
    "GetInstanceResultTypeDef",
    "GetInstancesResultTypeDef",
    "ContainerServicesListResultTypeDef",
    "CreateContainerServiceDeploymentResultTypeDef",
    "CreateContainerServiceResultTypeDef",
    "UpdateContainerServiceResultTypeDef",
    "GetExportSnapshotRecordsResultTypeDef",
    "CertificateSummaryTypeDef",
    "GetCostEstimateResultTypeDef",
    "CreateCertificateResultTypeDef",
    "GetCertificatesResultTypeDef",
)

AccessKeyLastUsedTypeDef = TypedDict(
    "AccessKeyLastUsedTypeDef",
    {
        "lastUsedDate": NotRequired[datetime],
        "region": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)
AccessRulesTypeDef = TypedDict(
    "AccessRulesTypeDef",
    {
        "getObject": NotRequired[AccessTypeType],
        "allowPublicOverrides": NotRequired[bool],
    },
)
AccountLevelBpaSyncTypeDef = TypedDict(
    "AccountLevelBpaSyncTypeDef",
    {
        "status": NotRequired[AccountLevelBpaSyncStatusType],
        "lastSyncedAt": NotRequired[datetime],
        "message": NotRequired[BPAStatusMessageType],
        "bpaImpactsLightsail": NotRequired[bool],
    },
)
AutoSnapshotAddOnRequestTypeDef = TypedDict(
    "AutoSnapshotAddOnRequestTypeDef",
    {
        "snapshotTimeOfDay": NotRequired[str],
    },
)
StopInstanceOnIdleRequestTypeDef = TypedDict(
    "StopInstanceOnIdleRequestTypeDef",
    {
        "threshold": NotRequired[str],
        "duration": NotRequired[str],
    },
)
AddOnTypeDef = TypedDict(
    "AddOnTypeDef",
    {
        "name": NotRequired[str],
        "status": NotRequired[str],
        "snapshotTimeOfDay": NotRequired[str],
        "nextSnapshotTimeOfDay": NotRequired[str],
        "threshold": NotRequired[str],
        "duration": NotRequired[str],
    },
)
MonitoredResourceInfoTypeDef = TypedDict(
    "MonitoredResourceInfoTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
    },
)
ResourceLocationTypeDef = TypedDict(
    "ResourceLocationTypeDef",
    {
        "availabilityZone": NotRequired[str],
        "regionName": NotRequired[RegionNameType],
    },
)
AllocateStaticIpRequestRequestTypeDef = TypedDict(
    "AllocateStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
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
AttachCertificateToDistributionRequestRequestTypeDef = TypedDict(
    "AttachCertificateToDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
        "certificateName": str,
    },
)
AttachDiskRequestRequestTypeDef = TypedDict(
    "AttachDiskRequestRequestTypeDef",
    {
        "diskName": str,
        "instanceName": str,
        "diskPath": str,
        "autoMounting": NotRequired[bool],
    },
)
AttachInstancesToLoadBalancerRequestRequestTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instanceNames": Sequence[str],
    },
)
AttachLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
    },
)
AttachStaticIpRequestRequestTypeDef = TypedDict(
    "AttachStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
        "instanceName": str,
    },
)
AttachedDiskTypeDef = TypedDict(
    "AttachedDiskTypeDef",
    {
        "path": NotRequired[str],
        "sizeInGb": NotRequired[int],
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "zoneName": NotRequired[str],
        "state": NotRequired[str],
    },
)
BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "blueprintId": NotRequired[str],
        "name": NotRequired[str],
        "group": NotRequired[str],
        "type": NotRequired[BlueprintTypeType],
        "description": NotRequired[str],
        "isActive": NotRequired[bool],
        "minPower": NotRequired[int],
        "version": NotRequired[str],
        "versionCode": NotRequired[str],
        "productUrl": NotRequired[str],
        "licenseUrl": NotRequired[str],
        "platform": NotRequired[InstancePlatformType],
        "appCategory": NotRequired[Literal["LfR"]],
    },
)
BucketAccessLogConfigTypeDef = TypedDict(
    "BucketAccessLogConfigTypeDef",
    {
        "enabled": bool,
        "destination": NotRequired[str],
        "prefix": NotRequired[str],
    },
)
BucketBundleTypeDef = TypedDict(
    "BucketBundleTypeDef",
    {
        "bundleId": NotRequired[str],
        "name": NotRequired[str],
        "price": NotRequired[float],
        "storagePerMonthInGb": NotRequired[int],
        "transferPerMonthInGb": NotRequired[int],
        "isActive": NotRequired[bool],
    },
)
BucketStateTypeDef = TypedDict(
    "BucketStateTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
ResourceReceivingAccessTypeDef = TypedDict(
    "ResourceReceivingAccessTypeDef",
    {
        "name": NotRequired[str],
        "resourceType": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
BundleTypeDef = TypedDict(
    "BundleTypeDef",
    {
        "price": NotRequired[float],
        "cpuCount": NotRequired[int],
        "diskSizeInGb": NotRequired[int],
        "bundleId": NotRequired[str],
        "instanceType": NotRequired[str],
        "isActive": NotRequired[bool],
        "name": NotRequired[str],
        "power": NotRequired[int],
        "ramSizeInGb": NotRequired[float],
        "transferPerMonthInGb": NotRequired[int],
        "supportedPlatforms": NotRequired[List[InstancePlatformType]],
        "supportedAppCategories": NotRequired[List[Literal["LfR"]]],
        "publicIpv4AddressCount": NotRequired[int],
    },
)
CacheBehaviorPerPathTypeDef = TypedDict(
    "CacheBehaviorPerPathTypeDef",
    {
        "path": NotRequired[str],
        "behavior": NotRequired[BehaviorEnumType],
    },
)
CacheBehaviorTypeDef = TypedDict(
    "CacheBehaviorTypeDef",
    {
        "behavior": NotRequired[BehaviorEnumType],
    },
)
CookieObjectOutputTypeDef = TypedDict(
    "CookieObjectOutputTypeDef",
    {
        "option": NotRequired[ForwardValuesType],
        "cookiesAllowList": NotRequired[List[str]],
    },
)
HeaderObjectOutputTypeDef = TypedDict(
    "HeaderObjectOutputTypeDef",
    {
        "option": NotRequired[ForwardValuesType],
        "headersAllowList": NotRequired[List[HeaderEnumType]],
    },
)
QueryStringObjectOutputTypeDef = TypedDict(
    "QueryStringObjectOutputTypeDef",
    {
        "option": NotRequired[bool],
        "queryStringsAllowList": NotRequired[List[str]],
    },
)
PortInfoTypeDef = TypedDict(
    "PortInfoTypeDef",
    {
        "fromPort": NotRequired[int],
        "toPort": NotRequired[int],
        "protocol": NotRequired[NetworkProtocolType],
        "cidrs": NotRequired[Sequence[str]],
        "ipv6Cidrs": NotRequired[Sequence[str]],
        "cidrListAliases": NotRequired[Sequence[str]],
    },
)
CloudFormationStackRecordSourceInfoTypeDef = TypedDict(
    "CloudFormationStackRecordSourceInfoTypeDef",
    {
        "resourceType": NotRequired[Literal["ExportSnapshotRecord"]],
        "name": NotRequired[str],
        "arn": NotRequired[str],
    },
)
DestinationInfoTypeDef = TypedDict(
    "DestinationInfoTypeDef",
    {
        "id": NotRequired[str],
        "service": NotRequired[str],
    },
)
ContainerImageTypeDef = TypedDict(
    "ContainerImageTypeDef",
    {
        "image": NotRequired[str],
        "digest": NotRequired[str],
        "createdAt": NotRequired[datetime],
    },
)
ContainerOutputTypeDef = TypedDict(
    "ContainerOutputTypeDef",
    {
        "image": NotRequired[str],
        "command": NotRequired[List[str]],
        "environment": NotRequired[Dict[str, str]],
        "ports": NotRequired[Dict[str, ContainerServiceProtocolType]],
    },
)
ContainerServiceECRImagePullerRoleRequestTypeDef = TypedDict(
    "ContainerServiceECRImagePullerRoleRequestTypeDef",
    {
        "isActive": NotRequired[bool],
    },
)
ContainerServiceECRImagePullerRoleTypeDef = TypedDict(
    "ContainerServiceECRImagePullerRoleTypeDef",
    {
        "isActive": NotRequired[bool],
        "principalArn": NotRequired[str],
    },
)
ContainerServiceHealthCheckConfigTypeDef = TypedDict(
    "ContainerServiceHealthCheckConfigTypeDef",
    {
        "healthyThreshold": NotRequired[int],
        "unhealthyThreshold": NotRequired[int],
        "timeoutSeconds": NotRequired[int],
        "intervalSeconds": NotRequired[int],
        "path": NotRequired[str],
        "successCodes": NotRequired[str],
    },
)
ContainerServiceLogEventTypeDef = TypedDict(
    "ContainerServiceLogEventTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)
ContainerServicePowerTypeDef = TypedDict(
    "ContainerServicePowerTypeDef",
    {
        "powerId": NotRequired[str],
        "price": NotRequired[float],
        "cpuCount": NotRequired[float],
        "ramSizeInGb": NotRequired[float],
        "name": NotRequired[str],
        "isActive": NotRequired[bool],
    },
)
ContainerServiceRegistryLoginTypeDef = TypedDict(
    "ContainerServiceRegistryLoginTypeDef",
    {
        "username": NotRequired[str],
        "password": NotRequired[str],
        "expiresAt": NotRequired[datetime],
        "registry": NotRequired[str],
    },
)
ContainerServiceStateDetailTypeDef = TypedDict(
    "ContainerServiceStateDetailTypeDef",
    {
        "code": NotRequired[ContainerServiceStateDetailCodeType],
        "message": NotRequired[str],
    },
)
ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "image": NotRequired[str],
        "command": NotRequired[Sequence[str]],
        "environment": NotRequired[Mapping[str, str]],
        "ports": NotRequired[Mapping[str, ContainerServiceProtocolType]],
    },
)
CookieObjectTypeDef = TypedDict(
    "CookieObjectTypeDef",
    {
        "option": NotRequired[ForwardValuesType],
        "cookiesAllowList": NotRequired[Sequence[str]],
    },
)
CopySnapshotRequestRequestTypeDef = TypedDict(
    "CopySnapshotRequestRequestTypeDef",
    {
        "targetSnapshotName": str,
        "sourceRegion": RegionNameType,
        "sourceSnapshotName": NotRequired[str],
        "sourceResourceName": NotRequired[str],
        "restoreDate": NotRequired[str],
        "useLatestRestorableAutoSnapshot": NotRequired[bool],
    },
)
CreateBucketAccessKeyRequestRequestTypeDef = TypedDict(
    "CreateBucketAccessKeyRequestRequestTypeDef",
    {
        "bucketName": str,
    },
)
InstanceEntryTypeDef = TypedDict(
    "InstanceEntryTypeDef",
    {
        "sourceName": str,
        "instanceType": str,
        "portInfoSource": PortInfoSourceTypeType,
        "availabilityZone": str,
        "userData": NotRequired[str],
    },
)
CreateContactMethodRequestRequestTypeDef = TypedDict(
    "CreateContactMethodRequestRequestTypeDef",
    {
        "protocol": ContactProtocolType,
        "contactEndpoint": str,
    },
)
InputOriginTypeDef = TypedDict(
    "InputOriginTypeDef",
    {
        "name": NotRequired[str],
        "regionName": NotRequired[RegionNameType],
        "protocolPolicy": NotRequired[OriginProtocolPolicyEnumType],
        "responseTimeout": NotRequired[int],
    },
)
DomainEntryTypeDef = TypedDict(
    "DomainEntryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "target": NotRequired[str],
        "isAlias": NotRequired[bool],
        "type": NotRequired[str],
        "options": NotRequired[Mapping[str, str]],
    },
)
CreateGUISessionAccessDetailsRequestRequestTypeDef = TypedDict(
    "CreateGUISessionAccessDetailsRequestRequestTypeDef",
    {
        "resourceName": str,
    },
)
SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "name": NotRequired[str],
        "url": NotRequired[str],
        "isPrimary": NotRequired[bool],
    },
)
DiskMapTypeDef = TypedDict(
    "DiskMapTypeDef",
    {
        "originalDiskPath": NotRequired[str],
        "newDiskName": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
DeleteAlarmRequestRequestTypeDef = TypedDict(
    "DeleteAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
    },
)
DeleteAutoSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteAutoSnapshotRequestRequestTypeDef",
    {
        "resourceName": str,
        "date": str,
    },
)
DeleteBucketAccessKeyRequestRequestTypeDef = TypedDict(
    "DeleteBucketAccessKeyRequestRequestTypeDef",
    {
        "bucketName": str,
        "accessKeyId": str,
    },
)
DeleteBucketRequestRequestTypeDef = TypedDict(
    "DeleteBucketRequestRequestTypeDef",
    {
        "bucketName": str,
        "forceDelete": NotRequired[bool],
    },
)
DeleteCertificateRequestRequestTypeDef = TypedDict(
    "DeleteCertificateRequestRequestTypeDef",
    {
        "certificateName": str,
    },
)
DeleteContactMethodRequestRequestTypeDef = TypedDict(
    "DeleteContactMethodRequestRequestTypeDef",
    {
        "protocol": ContactProtocolType,
    },
)
DeleteContainerImageRequestRequestTypeDef = TypedDict(
    "DeleteContainerImageRequestRequestTypeDef",
    {
        "serviceName": str,
        "image": str,
    },
)
DeleteContainerServiceRequestRequestTypeDef = TypedDict(
    "DeleteContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)
DeleteDiskRequestRequestTypeDef = TypedDict(
    "DeleteDiskRequestRequestTypeDef",
    {
        "diskName": str,
        "forceDeleteAddOns": NotRequired[bool],
    },
)
DeleteDiskSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)
DeleteDistributionRequestRequestTypeDef = TypedDict(
    "DeleteDistributionRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
        "forceDeleteAddOns": NotRequired[bool],
    },
)
DeleteInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
    },
)
DeleteKeyPairRequestRequestTypeDef = TypedDict(
    "DeleteKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
        "expectedFingerprint": NotRequired[str],
    },
)
DeleteKnownHostKeysRequestRequestTypeDef = TypedDict(
    "DeleteKnownHostKeysRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
DeleteLoadBalancerRequestRequestTypeDef = TypedDict(
    "DeleteLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)
DeleteLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "DeleteLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
        "force": NotRequired[bool],
    },
)
DeleteRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "skipFinalSnapshot": NotRequired[bool],
        "finalRelationalDatabaseSnapshotName": NotRequired[str],
    },
)
DeleteRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
)
DetachCertificateFromDistributionRequestRequestTypeDef = TypedDict(
    "DetachCertificateFromDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
    },
)
DetachDiskRequestRequestTypeDef = TypedDict(
    "DetachDiskRequestRequestTypeDef",
    {
        "diskName": str,
    },
)
DetachInstancesFromLoadBalancerRequestRequestTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instanceNames": Sequence[str],
    },
)
DetachStaticIpRequestRequestTypeDef = TypedDict(
    "DetachStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)
DisableAddOnRequestRequestTypeDef = TypedDict(
    "DisableAddOnRequestRequestTypeDef",
    {
        "addOnType": AddOnTypeType,
        "resourceName": str,
    },
)
DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {
        "name": NotRequired[str],
        "path": NotRequired[str],
        "sizeInGb": NotRequired[int],
        "isSystemDisk": NotRequired[bool],
    },
)
DiskSnapshotInfoTypeDef = TypedDict(
    "DiskSnapshotInfoTypeDef",
    {
        "sizeInGb": NotRequired[int],
    },
)
DistributionBundleTypeDef = TypedDict(
    "DistributionBundleTypeDef",
    {
        "bundleId": NotRequired[str],
        "name": NotRequired[str],
        "price": NotRequired[float],
        "transferPerMonthInGb": NotRequired[int],
        "isActive": NotRequired[bool],
    },
)
DnsRecordCreationStateTypeDef = TypedDict(
    "DnsRecordCreationStateTypeDef",
    {
        "code": NotRequired[DnsRecordCreationStateCodeType],
        "message": NotRequired[str],
    },
)
DomainEntryOutputTypeDef = TypedDict(
    "DomainEntryOutputTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "target": NotRequired[str],
        "isAlias": NotRequired[bool],
        "type": NotRequired[str],
        "options": NotRequired[Dict[str, str]],
    },
)
ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[str],
        "value": NotRequired[str],
    },
)
TimePeriodTypeDef = TypedDict(
    "TimePeriodTypeDef",
    {
        "start": NotRequired[datetime],
        "end": NotRequired[datetime],
    },
)
ExportSnapshotRequestRequestTypeDef = TypedDict(
    "ExportSnapshotRequestRequestTypeDef",
    {
        "sourceSnapshotName": str,
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
GetActiveNamesRequestRequestTypeDef = TypedDict(
    "GetActiveNamesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetAlarmsRequestRequestTypeDef = TypedDict(
    "GetAlarmsRequestRequestTypeDef",
    {
        "alarmName": NotRequired[str],
        "pageToken": NotRequired[str],
        "monitoredResourceName": NotRequired[str],
    },
)
GetAutoSnapshotsRequestRequestTypeDef = TypedDict(
    "GetAutoSnapshotsRequestRequestTypeDef",
    {
        "resourceName": str,
    },
)
GetBlueprintsRequestRequestTypeDef = TypedDict(
    "GetBlueprintsRequestRequestTypeDef",
    {
        "includeInactive": NotRequired[bool],
        "pageToken": NotRequired[str],
        "appCategory": NotRequired[Literal["LfR"]],
    },
)
GetBucketAccessKeysRequestRequestTypeDef = TypedDict(
    "GetBucketAccessKeysRequestRequestTypeDef",
    {
        "bucketName": str,
    },
)
GetBucketBundlesRequestRequestTypeDef = TypedDict(
    "GetBucketBundlesRequestRequestTypeDef",
    {
        "includeInactive": NotRequired[bool],
    },
)
MetricDatapointTypeDef = TypedDict(
    "MetricDatapointTypeDef",
    {
        "average": NotRequired[float],
        "maximum": NotRequired[float],
        "minimum": NotRequired[float],
        "sampleCount": NotRequired[float],
        "sum": NotRequired[float],
        "timestamp": NotRequired[datetime],
        "unit": NotRequired[MetricUnitType],
    },
)
GetBucketsRequestRequestTypeDef = TypedDict(
    "GetBucketsRequestRequestTypeDef",
    {
        "bucketName": NotRequired[str],
        "pageToken": NotRequired[str],
        "includeConnectedResources": NotRequired[bool],
    },
)
GetBundlesRequestRequestTypeDef = TypedDict(
    "GetBundlesRequestRequestTypeDef",
    {
        "includeInactive": NotRequired[bool],
        "pageToken": NotRequired[str],
        "appCategory": NotRequired[Literal["LfR"]],
    },
)
GetCertificatesRequestRequestTypeDef = TypedDict(
    "GetCertificatesRequestRequestTypeDef",
    {
        "certificateStatuses": NotRequired[Sequence[CertificateStatusType]],
        "includeCertificateDetails": NotRequired[bool],
        "certificateName": NotRequired[str],
        "pageToken": NotRequired[str],
    },
)
GetCloudFormationStackRecordsRequestRequestTypeDef = TypedDict(
    "GetCloudFormationStackRecordsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetContactMethodsRequestRequestTypeDef = TypedDict(
    "GetContactMethodsRequestRequestTypeDef",
    {
        "protocols": NotRequired[Sequence[ContactProtocolType]],
    },
)
GetContainerImagesRequestRequestTypeDef = TypedDict(
    "GetContainerImagesRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)
GetContainerServiceDeploymentsRequestRequestTypeDef = TypedDict(
    "GetContainerServiceDeploymentsRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)
GetContainerServicesRequestRequestTypeDef = TypedDict(
    "GetContainerServicesRequestRequestTypeDef",
    {
        "serviceName": NotRequired[str],
    },
)
GetDiskRequestRequestTypeDef = TypedDict(
    "GetDiskRequestRequestTypeDef",
    {
        "diskName": str,
    },
)
GetDiskSnapshotRequestRequestTypeDef = TypedDict(
    "GetDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)
GetDiskSnapshotsRequestRequestTypeDef = TypedDict(
    "GetDiskSnapshotsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetDisksRequestRequestTypeDef = TypedDict(
    "GetDisksRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetDistributionLatestCacheResetRequestRequestTypeDef = TypedDict(
    "GetDistributionLatestCacheResetRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
    },
)
GetDistributionsRequestRequestTypeDef = TypedDict(
    "GetDistributionsRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
        "pageToken": NotRequired[str],
    },
)
GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
GetDomainsRequestRequestTypeDef = TypedDict(
    "GetDomainsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetExportSnapshotRecordsRequestRequestTypeDef = TypedDict(
    "GetExportSnapshotRecordsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetInstanceAccessDetailsRequestRequestTypeDef = TypedDict(
    "GetInstanceAccessDetailsRequestRequestTypeDef",
    {
        "instanceName": str,
        "protocol": NotRequired[InstanceAccessProtocolType],
    },
)
GetInstancePortStatesRequestRequestTypeDef = TypedDict(
    "GetInstancePortStatesRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
InstancePortStateTypeDef = TypedDict(
    "InstancePortStateTypeDef",
    {
        "fromPort": NotRequired[int],
        "toPort": NotRequired[int],
        "protocol": NotRequired[NetworkProtocolType],
        "state": NotRequired[PortStateType],
        "cidrs": NotRequired[List[str]],
        "ipv6Cidrs": NotRequired[List[str]],
        "cidrListAliases": NotRequired[List[str]],
    },
)
GetInstanceRequestRequestTypeDef = TypedDict(
    "GetInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
GetInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "GetInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
    },
)
GetInstanceSnapshotsRequestRequestTypeDef = TypedDict(
    "GetInstanceSnapshotsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetInstanceStateRequestRequestTypeDef = TypedDict(
    "GetInstanceStateRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "code": NotRequired[int],
        "name": NotRequired[str],
    },
)
GetInstancesRequestRequestTypeDef = TypedDict(
    "GetInstancesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetKeyPairRequestRequestTypeDef = TypedDict(
    "GetKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
    },
)
GetKeyPairsRequestRequestTypeDef = TypedDict(
    "GetKeyPairsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
        "includeDefaultKeyPair": NotRequired[bool],
    },
)
GetLoadBalancerRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)
GetLoadBalancerTlsCertificatesRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)
GetLoadBalancerTlsPoliciesRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerTlsPoliciesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
LoadBalancerTlsPolicyTypeDef = TypedDict(
    "LoadBalancerTlsPolicyTypeDef",
    {
        "name": NotRequired[str],
        "isDefault": NotRequired[bool],
        "description": NotRequired[str],
        "protocols": NotRequired[List[str]],
        "ciphers": NotRequired[List[str]],
    },
)
GetLoadBalancersRequestRequestTypeDef = TypedDict(
    "GetLoadBalancersRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetOperationRequestRequestTypeDef = TypedDict(
    "GetOperationRequestRequestTypeDef",
    {
        "operationId": str,
    },
)
GetOperationsForResourceRequestRequestTypeDef = TypedDict(
    "GetOperationsForResourceRequestRequestTypeDef",
    {
        "resourceName": str,
        "pageToken": NotRequired[str],
    },
)
GetOperationsRequestRequestTypeDef = TypedDict(
    "GetOperationsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetRegionsRequestRequestTypeDef = TypedDict(
    "GetRegionsRequestRequestTypeDef",
    {
        "includeAvailabilityZones": NotRequired[bool],
        "includeRelationalDatabaseAvailabilityZones": NotRequired[bool],
    },
)
GetRelationalDatabaseBlueprintsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
RelationalDatabaseBlueprintTypeDef = TypedDict(
    "RelationalDatabaseBlueprintTypeDef",
    {
        "blueprintId": NotRequired[str],
        "engine": NotRequired[Literal["mysql"]],
        "engineVersion": NotRequired[str],
        "engineDescription": NotRequired[str],
        "engineVersionDescription": NotRequired[str],
        "isEngineDefault": NotRequired[bool],
    },
)
GetRelationalDatabaseBundlesRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
        "includeInactive": NotRequired[bool],
    },
)
RelationalDatabaseBundleTypeDef = TypedDict(
    "RelationalDatabaseBundleTypeDef",
    {
        "bundleId": NotRequired[str],
        "name": NotRequired[str],
        "price": NotRequired[float],
        "ramSizeInGb": NotRequired[float],
        "diskSizeInGb": NotRequired[int],
        "transferPerMonthInGb": NotRequired[int],
        "cpuCount": NotRequired[int],
        "isEncrypted": NotRequired[bool],
        "isActive": NotRequired[bool],
    },
)
GetRelationalDatabaseEventsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseEventsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "durationInMinutes": NotRequired[int],
        "pageToken": NotRequired[str],
    },
)
RelationalDatabaseEventTypeDef = TypedDict(
    "RelationalDatabaseEventTypeDef",
    {
        "resource": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "message": NotRequired[str],
        "eventCategories": NotRequired[List[str]],
    },
)
LogEventTypeDef = TypedDict(
    "LogEventTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)
GetRelationalDatabaseLogStreamsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "passwordVersion": NotRequired[RelationalDatabasePasswordVersionType],
    },
)
GetRelationalDatabaseParametersRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseParametersRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "pageToken": NotRequired[str],
    },
)
RelationalDatabaseParameterTypeDef = TypedDict(
    "RelationalDatabaseParameterTypeDef",
    {
        "allowedValues": NotRequired[str],
        "applyMethod": NotRequired[str],
        "applyType": NotRequired[str],
        "dataType": NotRequired[str],
        "description": NotRequired[str],
        "isModifiable": NotRequired[bool],
        "parameterName": NotRequired[str],
        "parameterValue": NotRequired[str],
    },
)
GetRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
GetRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
)
GetRelationalDatabaseSnapshotsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetRelationalDatabasesRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabasesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
GetSetupHistoryRequestRequestTypeDef = TypedDict(
    "GetSetupHistoryRequestRequestTypeDef",
    {
        "resourceName": str,
        "pageToken": NotRequired[str],
    },
)
GetStaticIpRequestRequestTypeDef = TypedDict(
    "GetStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)
GetStaticIpsRequestRequestTypeDef = TypedDict(
    "GetStaticIpsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)
HeaderObjectTypeDef = TypedDict(
    "HeaderObjectTypeDef",
    {
        "option": NotRequired[ForwardValuesType],
        "headersAllowList": NotRequired[Sequence[HeaderEnumType]],
    },
)
HostKeyAttributesTypeDef = TypedDict(
    "HostKeyAttributesTypeDef",
    {
        "algorithm": NotRequired[str],
        "publicKey": NotRequired[str],
        "witnessedAt": NotRequired[datetime],
        "fingerprintSHA1": NotRequired[str],
        "fingerprintSHA256": NotRequired[str],
        "notValidBefore": NotRequired[datetime],
        "notValidAfter": NotRequired[datetime],
    },
)
ImportKeyPairRequestRequestTypeDef = TypedDict(
    "ImportKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
        "publicKeyBase64": str,
    },
)
PasswordDataTypeDef = TypedDict(
    "PasswordDataTypeDef",
    {
        "ciphertext": NotRequired[str],
        "keyPairName": NotRequired[str],
    },
)
InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "instanceName": NotRequired[str],
        "instanceHealth": NotRequired[InstanceHealthStateType],
        "instanceHealthReason": NotRequired[InstanceHealthReasonType],
    },
)
InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "state": NotRequired[InstanceMetadataStateType],
        "httpTokens": NotRequired[HttpTokensType],
        "httpEndpoint": NotRequired[HttpEndpointType],
        "httpPutResponseHopLimit": NotRequired[int],
        "httpProtocolIpv6": NotRequired[HttpProtocolIpv6Type],
    },
)
InstancePortInfoTypeDef = TypedDict(
    "InstancePortInfoTypeDef",
    {
        "fromPort": NotRequired[int],
        "toPort": NotRequired[int],
        "protocol": NotRequired[NetworkProtocolType],
        "accessFrom": NotRequired[str],
        "accessType": NotRequired[PortAccessTypeType],
        "commonName": NotRequired[str],
        "accessDirection": NotRequired[AccessDirectionType],
        "cidrs": NotRequired[List[str]],
        "ipv6Cidrs": NotRequired[List[str]],
        "cidrListAliases": NotRequired[List[str]],
    },
)
MonthlyTransferTypeDef = TypedDict(
    "MonthlyTransferTypeDef",
    {
        "gbPerMonthAllocated": NotRequired[int],
    },
)
OriginTypeDef = TypedDict(
    "OriginTypeDef",
    {
        "name": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "regionName": NotRequired[RegionNameType],
        "protocolPolicy": NotRequired[OriginProtocolPolicyEnumType],
        "responseTimeout": NotRequired[int],
    },
)
LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef",
    {
        "code": NotRequired[LoadBalancerTlsCertificateDnsRecordCreationStateCodeType],
        "message": NotRequired[str],
    },
)
LoadBalancerTlsCertificateDomainValidationOptionTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    {
        "domainName": NotRequired[str],
        "validationStatus": NotRequired[LoadBalancerTlsCertificateDomainStatusType],
    },
)
LoadBalancerTlsCertificateSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateSummaryTypeDef",
    {
        "name": NotRequired[str],
        "isAttached": NotRequired[bool],
    },
)
NameServersUpdateStateTypeDef = TypedDict(
    "NameServersUpdateStateTypeDef",
    {
        "code": NotRequired[NameServersUpdateStateCodeType],
        "message": NotRequired[str],
    },
)
PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "action": NotRequired[str],
        "description": NotRequired[str],
        "currentApplyDate": NotRequired[datetime],
    },
)
PendingModifiedRelationalDatabaseValuesTypeDef = TypedDict(
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    {
        "masterUserPassword": NotRequired[str],
        "engineVersion": NotRequired[str],
        "backupRetentionEnabled": NotRequired[bool],
    },
)
PutAlarmRequestRequestTypeDef = TypedDict(
    "PutAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
        "metricName": MetricNameType,
        "monitoredResourceName": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": float,
        "evaluationPeriods": int,
        "datapointsToAlarm": NotRequired[int],
        "treatMissingData": NotRequired[TreatMissingDataType],
        "contactProtocols": NotRequired[Sequence[ContactProtocolType]],
        "notificationTriggers": NotRequired[Sequence[AlarmStateType]],
        "notificationEnabled": NotRequired[bool],
    },
)
QueryStringObjectTypeDef = TypedDict(
    "QueryStringObjectTypeDef",
    {
        "option": NotRequired[bool],
        "queryStringsAllowList": NotRequired[Sequence[str]],
    },
)
R53HostedZoneDeletionStateTypeDef = TypedDict(
    "R53HostedZoneDeletionStateTypeDef",
    {
        "code": NotRequired[R53HostedZoneDeletionStateCodeType],
        "message": NotRequired[str],
    },
)
RebootInstanceRequestRequestTypeDef = TypedDict(
    "RebootInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
RebootRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "RebootRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
RegisterContainerImageRequestRequestTypeDef = TypedDict(
    "RegisterContainerImageRequestRequestTypeDef",
    {
        "serviceName": str,
        "label": str,
        "digest": str,
    },
)
RelationalDatabaseEndpointTypeDef = TypedDict(
    "RelationalDatabaseEndpointTypeDef",
    {
        "port": NotRequired[int],
        "address": NotRequired[str],
    },
)
RelationalDatabaseHardwareTypeDef = TypedDict(
    "RelationalDatabaseHardwareTypeDef",
    {
        "cpuCount": NotRequired[int],
        "diskSizeInGb": NotRequired[int],
        "ramSizeInGb": NotRequired[float],
    },
)
ReleaseStaticIpRequestRequestTypeDef = TypedDict(
    "ReleaseStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)
ResetDistributionCacheRequestRequestTypeDef = TypedDict(
    "ResetDistributionCacheRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
    },
)
SendContactMethodVerificationRequestRequestTypeDef = TypedDict(
    "SendContactMethodVerificationRequestRequestTypeDef",
    {
        "protocol": Literal["Email"],
    },
)
SetIpAddressTypeRequestRequestTypeDef = TypedDict(
    "SetIpAddressTypeRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceName": str,
        "ipAddressType": IpAddressTypeType,
        "acceptBundleUpdate": NotRequired[bool],
    },
)
SetResourceAccessForBucketRequestRequestTypeDef = TypedDict(
    "SetResourceAccessForBucketRequestRequestTypeDef",
    {
        "resourceName": str,
        "bucketName": str,
        "access": ResourceBucketAccessType,
    },
)
SetupExecutionDetailsTypeDef = TypedDict(
    "SetupExecutionDetailsTypeDef",
    {
        "command": NotRequired[str],
        "dateTime": NotRequired[datetime],
        "name": NotRequired[str],
        "status": NotRequired[SetupStatusType],
        "standardError": NotRequired[str],
        "standardOutput": NotRequired[str],
        "version": NotRequired[str],
    },
)
SetupRequestTypeDef = TypedDict(
    "SetupRequestTypeDef",
    {
        "instanceName": NotRequired[str],
        "domainNames": NotRequired[List[str]],
        "certificateProvider": NotRequired[Literal["LetsEncrypt"]],
    },
)
SetupInstanceHttpsRequestRequestTypeDef = TypedDict(
    "SetupInstanceHttpsRequestRequestTypeDef",
    {
        "instanceName": str,
        "emailAddress": str,
        "domainNames": Sequence[str],
        "certificateProvider": Literal["LetsEncrypt"],
    },
)
StartGUISessionRequestRequestTypeDef = TypedDict(
    "StartGUISessionRequestRequestTypeDef",
    {
        "resourceName": str,
    },
)
StartInstanceRequestRequestTypeDef = TypedDict(
    "StartInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
StartRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "StartRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
StopGUISessionRequestRequestTypeDef = TypedDict(
    "StopGUISessionRequestRequestTypeDef",
    {
        "resourceName": str,
    },
)
StopInstanceRequestRequestTypeDef = TypedDict(
    "StopInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
        "force": NotRequired[bool],
    },
)
StopRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "StopRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseSnapshotName": NotRequired[str],
    },
)
TestAlarmRequestRequestTypeDef = TypedDict(
    "TestAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
        "state": AlarmStateType,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceName": str,
        "tagKeys": Sequence[str],
        "resourceArn": NotRequired[str],
    },
)
UpdateBucketBundleRequestRequestTypeDef = TypedDict(
    "UpdateBucketBundleRequestRequestTypeDef",
    {
        "bucketName": str,
        "bundleId": str,
    },
)
UpdateDistributionBundleRequestRequestTypeDef = TypedDict(
    "UpdateDistributionBundleRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
        "bundleId": NotRequired[str],
    },
)
UpdateInstanceMetadataOptionsRequestRequestTypeDef = TypedDict(
    "UpdateInstanceMetadataOptionsRequestRequestTypeDef",
    {
        "instanceName": str,
        "httpTokens": NotRequired[HttpTokensType],
        "httpEndpoint": NotRequired[HttpEndpointType],
        "httpPutResponseHopLimit": NotRequired[int],
        "httpProtocolIpv6": NotRequired[HttpProtocolIpv6Type],
    },
)
UpdateLoadBalancerAttributeRequestRequestTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "attributeName": LoadBalancerAttributeNameType,
        "attributeValue": str,
    },
)
UpdateRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "UpdateRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "masterUserPassword": NotRequired[str],
        "rotateMasterUserPassword": NotRequired[bool],
        "preferredBackupWindow": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "enableBackupRetention": NotRequired[bool],
        "disableBackupRetention": NotRequired[bool],
        "publiclyAccessible": NotRequired[bool],
        "applyImmediately": NotRequired[bool],
        "caCertificateIdentifier": NotRequired[str],
        "relationalDatabaseBlueprintId": NotRequired[str],
    },
)
AccessKeyTypeDef = TypedDict(
    "AccessKeyTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "secretAccessKey": NotRequired[str],
        "status": NotRequired[StatusTypeType],
        "createdAt": NotRequired[datetime],
        "lastUsed": NotRequired[AccessKeyLastUsedTypeDef],
    },
)
AddOnRequestTypeDef = TypedDict(
    "AddOnRequestTypeDef",
    {
        "addOnType": AddOnTypeType,
        "autoSnapshotAddOnRequest": NotRequired[AutoSnapshotAddOnRequestTypeDef],
        "stopInstanceOnIdleRequest": NotRequired[StopInstanceOnIdleRequestTypeDef],
    },
)
AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "supportCode": NotRequired[str],
        "monitoredResourceInfo": NotRequired[MonitoredResourceInfoTypeDef],
        "comparisonOperator": NotRequired[ComparisonOperatorType],
        "evaluationPeriods": NotRequired[int],
        "period": NotRequired[int],
        "threshold": NotRequired[float],
        "datapointsToAlarm": NotRequired[int],
        "treatMissingData": NotRequired[TreatMissingDataType],
        "statistic": NotRequired[MetricStatisticType],
        "metricName": NotRequired[MetricNameType],
        "state": NotRequired[AlarmStateType],
        "unit": NotRequired[MetricUnitType],
        "contactProtocols": NotRequired[List[ContactProtocolType]],
        "notificationTriggers": NotRequired[List[AlarmStateType]],
        "notificationEnabled": NotRequired[bool],
    },
)
ContactMethodTypeDef = TypedDict(
    "ContactMethodTypeDef",
    {
        "contactEndpoint": NotRequired[str],
        "status": NotRequired[ContactMethodStatusType],
        "protocol": NotRequired[ContactProtocolType],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "supportCode": NotRequired[str],
    },
)
OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "id": NotRequired[str],
        "resourceName": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "isTerminal": NotRequired[bool],
        "operationDetails": NotRequired[str],
        "operationType": NotRequired[OperationTypeType],
        "status": NotRequired[OperationStatusType],
        "statusChangedAt": NotRequired[datetime],
        "errorCode": NotRequired[str],
        "errorDetails": NotRequired[str],
    },
)
SetupHistoryResourceTypeDef = TypedDict(
    "SetupHistoryResourceTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
    },
)
StaticIpTypeDef = TypedDict(
    "StaticIpTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "ipAddress": NotRequired[str],
        "attachedTo": NotRequired[str],
        "isAttached": NotRequired[bool],
    },
)
DownloadDefaultKeyPairResultTypeDef = TypedDict(
    "DownloadDefaultKeyPairResultTypeDef",
    {
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetActiveNamesResultTypeDef = TypedDict(
    "GetActiveNamesResultTypeDef",
    {
        "activeNames": List[str],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContainerAPIMetadataResultTypeDef = TypedDict(
    "GetContainerAPIMetadataResultTypeDef",
    {
        "metadata": List[Dict[str, str]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDistributionLatestCacheResetResultTypeDef = TypedDict(
    "GetDistributionLatestCacheResetResultTypeDef",
    {
        "status": str,
        "createTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseLogStreamsResultTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsResultTypeDef",
    {
        "logStreams": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseMasterUserPasswordResultTypeDef = TypedDict(
    "GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    {
        "masterUserPassword": str,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IsVpcPeeredResultTypeDef = TypedDict(
    "IsVpcPeeredResultTypeDef",
    {
        "isPeered": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutoSnapshotDetailsTypeDef = TypedDict(
    "AutoSnapshotDetailsTypeDef",
    {
        "date": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "status": NotRequired[AutoSnapshotStatusType],
        "fromAttachedDisks": NotRequired[List[AttachedDiskTypeDef]],
    },
)
RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "continentCode": NotRequired[str],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "name": NotRequired[RegionNameType],
        "availabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "relationalDatabaseAvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
    },
)
GetBlueprintsResultTypeDef = TypedDict(
    "GetBlueprintsResultTypeDef",
    {
        "blueprints": List[BlueprintTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBucketRequestRequestTypeDef = TypedDict(
    "UpdateBucketRequestRequestTypeDef",
    {
        "bucketName": str,
        "accessRules": NotRequired[AccessRulesTypeDef],
        "versioning": NotRequired[str],
        "readonlyAccessAccounts": NotRequired[Sequence[str]],
        "accessLogConfig": NotRequired[BucketAccessLogConfigTypeDef],
    },
)
GetBucketBundlesResultTypeDef = TypedDict(
    "GetBucketBundlesResultTypeDef",
    {
        "bundles": List[BucketBundleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "resourceType": NotRequired[str],
        "accessRules": NotRequired[AccessRulesTypeDef],
        "arn": NotRequired[str],
        "bundleId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "url": NotRequired[str],
        "location": NotRequired[ResourceLocationTypeDef],
        "name": NotRequired[str],
        "supportCode": NotRequired[str],
        "tags": NotRequired[List[TagTypeDef]],
        "objectVersioning": NotRequired[str],
        "ableToUpdateBundle": NotRequired[bool],
        "readonlyAccessAccounts": NotRequired[List[str]],
        "resourcesReceivingAccess": NotRequired[List[ResourceReceivingAccessTypeDef]],
        "state": NotRequired[BucketStateTypeDef],
        "accessLogConfig": NotRequired[BucketAccessLogConfigTypeDef],
    },
)
CreateBucketRequestRequestTypeDef = TypedDict(
    "CreateBucketRequestRequestTypeDef",
    {
        "bucketName": str,
        "bundleId": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
        "enableObjectVersioning": NotRequired[bool],
    },
)
CreateCertificateRequestRequestTypeDef = TypedDict(
    "CreateCertificateRequestRequestTypeDef",
    {
        "certificateName": str,
        "domainName": str,
        "subjectAlternativeNames": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDiskSnapshotRequestRequestTypeDef = TypedDict(
    "CreateDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
        "diskName": NotRequired[str],
        "instanceName": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "domainName": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "CreateInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
        "instanceName": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateKeyPairRequestRequestTypeDef = TypedDict(
    "CreateKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateLoadBalancerRequestRequestTypeDef = TypedDict(
    "CreateLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instancePort": int,
        "healthCheckPath": NotRequired[str],
        "certificateName": NotRequired[str],
        "certificateDomainName": NotRequired[str],
        "certificateAlternativeNames": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "tlsPolicyName": NotRequired[str],
    },
)
CreateLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "CreateLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
        "certificateDomainName": str,
        "certificateAlternativeNames": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "CreateRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "masterUsername": str,
        "availabilityZone": NotRequired[str],
        "masterUserPassword": NotRequired[str],
        "preferredBackupWindow": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "publiclyAccessible": NotRequired[bool],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "CreateRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseSnapshotName": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DiskSnapshotTypeDef = TypedDict(
    "DiskSnapshotTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "sizeInGb": NotRequired[int],
        "state": NotRequired[DiskSnapshotStateType],
        "progress": NotRequired[str],
        "fromDiskName": NotRequired[str],
        "fromDiskArn": NotRequired[str],
        "fromInstanceName": NotRequired[str],
        "fromInstanceArn": NotRequired[str],
        "isFromAutoSnapshot": NotRequired[bool],
    },
)
DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "addOns": NotRequired[List[AddOnTypeDef]],
        "sizeInGb": NotRequired[int],
        "isSystemDisk": NotRequired[bool],
        "iops": NotRequired[int],
        "path": NotRequired[str],
        "state": NotRequired[DiskStateType],
        "attachedTo": NotRequired[str],
        "isAttached": NotRequired[bool],
        "attachmentState": NotRequired[str],
        "gbInUse": NotRequired[int],
        "autoMountStatus": NotRequired[AutoMountStatusType],
    },
)
KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "fingerprint": NotRequired[str],
    },
)
RelationalDatabaseSnapshotTypeDef = TypedDict(
    "RelationalDatabaseSnapshotTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "engine": NotRequired[str],
        "engineVersion": NotRequired[str],
        "sizeInGb": NotRequired[int],
        "state": NotRequired[str],
        "fromRelationalDatabaseName": NotRequired[str],
        "fromRelationalDatabaseArn": NotRequired[str],
        "fromRelationalDatabaseBundleId": NotRequired[str],
        "fromRelationalDatabaseBlueprintId": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceName": str,
        "tags": Sequence[TagTypeDef],
        "resourceArn": NotRequired[str],
    },
)
GetBundlesResultTypeDef = TypedDict(
    "GetBundlesResultTypeDef",
    {
        "bundles": List[BundleTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheSettingsOutputTypeDef = TypedDict(
    "CacheSettingsOutputTypeDef",
    {
        "defaultTTL": NotRequired[int],
        "minimumTTL": NotRequired[int],
        "maximumTTL": NotRequired[int],
        "allowedHTTPMethods": NotRequired[str],
        "cachedHTTPMethods": NotRequired[str],
        "forwardedCookies": NotRequired[CookieObjectOutputTypeDef],
        "forwardedHeaders": NotRequired[HeaderObjectOutputTypeDef],
        "forwardedQueryStrings": NotRequired[QueryStringObjectOutputTypeDef],
    },
)
CloseInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "CloseInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfo": PortInfoTypeDef,
        "instanceName": str,
    },
)
OpenInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "OpenInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfo": PortInfoTypeDef,
        "instanceName": str,
    },
)
PutInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "PutInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfos": Sequence[PortInfoTypeDef],
        "instanceName": str,
    },
)
CloudFormationStackRecordTypeDef = TypedDict(
    "CloudFormationStackRecordTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "state": NotRequired[RecordStateType],
        "sourceInfo": NotRequired[List[CloudFormationStackRecordSourceInfoTypeDef]],
        "destinationInfo": NotRequired[DestinationInfoTypeDef],
    },
)
GetContainerImagesResultTypeDef = TypedDict(
    "GetContainerImagesResultTypeDef",
    {
        "containerImages": List[ContainerImageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterContainerImageResultTypeDef = TypedDict(
    "RegisterContainerImageResultTypeDef",
    {
        "containerImage": ContainerImageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PrivateRegistryAccessRequestTypeDef = TypedDict(
    "PrivateRegistryAccessRequestTypeDef",
    {
        "ecrImagePullerRole": NotRequired[ContainerServiceECRImagePullerRoleRequestTypeDef],
    },
)
PrivateRegistryAccessTypeDef = TypedDict(
    "PrivateRegistryAccessTypeDef",
    {
        "ecrImagePullerRole": NotRequired[ContainerServiceECRImagePullerRoleTypeDef],
    },
)
ContainerServiceEndpointTypeDef = TypedDict(
    "ContainerServiceEndpointTypeDef",
    {
        "containerName": NotRequired[str],
        "containerPort": NotRequired[int],
        "healthCheck": NotRequired[ContainerServiceHealthCheckConfigTypeDef],
    },
)
EndpointRequestTypeDef = TypedDict(
    "EndpointRequestTypeDef",
    {
        "containerName": str,
        "containerPort": int,
        "healthCheck": NotRequired[ContainerServiceHealthCheckConfigTypeDef],
    },
)
GetContainerLogResultTypeDef = TypedDict(
    "GetContainerLogResultTypeDef",
    {
        "logEvents": List[ContainerServiceLogEventTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContainerServicePowersResultTypeDef = TypedDict(
    "GetContainerServicePowersResultTypeDef",
    {
        "powers": List[ContainerServicePowerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContainerServiceRegistryLoginResultTypeDef = TypedDict(
    "CreateContainerServiceRegistryLoginResultTypeDef",
    {
        "registryLogin": ContainerServiceRegistryLoginTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContainerUnionTypeDef = Union[ContainerTypeDef, ContainerOutputTypeDef]
CookieObjectUnionTypeDef = Union[CookieObjectTypeDef, CookieObjectOutputTypeDef]
CreateCloudFormationStackRequestRequestTypeDef = TypedDict(
    "CreateCloudFormationStackRequestRequestTypeDef",
    {
        "instances": Sequence[InstanceEntryTypeDef],
    },
)
CreateDomainEntryRequestRequestTypeDef = TypedDict(
    "CreateDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": DomainEntryTypeDef,
    },
)
DeleteDomainEntryRequestRequestTypeDef = TypedDict(
    "DeleteDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": DomainEntryTypeDef,
    },
)
UpdateDomainEntryRequestRequestTypeDef = TypedDict(
    "UpdateDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": DomainEntryTypeDef,
    },
)
CreateGUISessionAccessDetailsResultTypeDef = TypedDict(
    "CreateGUISessionAccessDetailsResultTypeDef",
    {
        "resourceName": str,
        "status": StatusType,
        "percentageComplete": int,
        "failureReason": str,
        "sessions": List[SessionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef = TypedDict(
    "CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "availabilityZone": NotRequired[str],
        "publiclyAccessible": NotRequired[bool],
        "relationalDatabaseSnapshotName": NotRequired[str],
        "relationalDatabaseBundleId": NotRequired[str],
        "sourceRelationalDatabaseName": NotRequired[str],
        "restoreTime": NotRequired[TimestampTypeDef],
        "useLatestRestorableTime": NotRequired[bool],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetBucketMetricDataRequestRequestTypeDef = TypedDict(
    "GetBucketMetricDataRequestRequestTypeDef",
    {
        "bucketName": str,
        "metricName": BucketMetricNameType,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "period": int,
        "statistics": Sequence[MetricStatisticType],
        "unit": MetricUnitType,
    },
)
GetContainerLogRequestRequestTypeDef = TypedDict(
    "GetContainerLogRequestRequestTypeDef",
    {
        "serviceName": str,
        "containerName": str,
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
        "filterPattern": NotRequired[str],
        "pageToken": NotRequired[str],
    },
)
GetContainerServiceMetricDataRequestRequestTypeDef = TypedDict(
    "GetContainerServiceMetricDataRequestRequestTypeDef",
    {
        "serviceName": str,
        "metricName": ContainerServiceMetricNameType,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "period": int,
        "statistics": Sequence[MetricStatisticType],
    },
)
GetCostEstimateRequestRequestTypeDef = TypedDict(
    "GetCostEstimateRequestRequestTypeDef",
    {
        "resourceName": str,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
    },
)
GetDistributionMetricDataRequestRequestTypeDef = TypedDict(
    "GetDistributionMetricDataRequestRequestTypeDef",
    {
        "distributionName": str,
        "metricName": DistributionMetricNameType,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "period": int,
        "unit": MetricUnitType,
        "statistics": Sequence[MetricStatisticType],
    },
)
GetInstanceMetricDataRequestRequestTypeDef = TypedDict(
    "GetInstanceMetricDataRequestRequestTypeDef",
    {
        "instanceName": str,
        "metricName": InstanceMetricNameType,
        "period": int,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "unit": MetricUnitType,
        "statistics": Sequence[MetricStatisticType],
    },
)
GetLoadBalancerMetricDataRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerMetricDataRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "metricName": LoadBalancerMetricNameType,
        "period": int,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "unit": MetricUnitType,
        "statistics": Sequence[MetricStatisticType],
    },
)
GetRelationalDatabaseLogEventsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseLogEventsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "logStreamName": str,
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
        "startFromHead": NotRequired[bool],
        "pageToken": NotRequired[str],
    },
)
GetRelationalDatabaseMetricDataRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "metricName": RelationalDatabaseMetricNameType,
        "period": int,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "unit": MetricUnitType,
        "statistics": Sequence[MetricStatisticType],
    },
)
InstanceSnapshotInfoTypeDef = TypedDict(
    "InstanceSnapshotInfoTypeDef",
    {
        "fromBundleId": NotRequired[str],
        "fromBlueprintId": NotRequired[str],
        "fromDiskInfo": NotRequired[List[DiskInfoTypeDef]],
    },
)
GetDistributionBundlesResultTypeDef = TypedDict(
    "GetDistributionBundlesResultTypeDef",
    {
        "bundles": List[DistributionBundleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DomainValidationRecordTypeDef = TypedDict(
    "DomainValidationRecordTypeDef",
    {
        "domainName": NotRequired[str],
        "resourceRecord": NotRequired[ResourceRecordTypeDef],
        "dnsRecordCreationState": NotRequired[DnsRecordCreationStateTypeDef],
        "validationStatus": NotRequired[CertificateDomainValidationStatusType],
    },
)
EstimateByTimeTypeDef = TypedDict(
    "EstimateByTimeTypeDef",
    {
        "usageCost": NotRequired[float],
        "pricingUnit": NotRequired[PricingUnitType],
        "unit": NotRequired[float],
        "currency": NotRequired[Literal["USD"]],
        "timePeriod": NotRequired[TimePeriodTypeDef],
    },
)
GetActiveNamesRequestGetActiveNamesPaginateTypeDef = TypedDict(
    "GetActiveNamesRequestGetActiveNamesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBlueprintsRequestGetBlueprintsPaginateTypeDef = TypedDict(
    "GetBlueprintsRequestGetBlueprintsPaginateTypeDef",
    {
        "includeInactive": NotRequired[bool],
        "appCategory": NotRequired[Literal["LfR"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBundlesRequestGetBundlesPaginateTypeDef = TypedDict(
    "GetBundlesRequestGetBundlesPaginateTypeDef",
    {
        "includeInactive": NotRequired[bool],
        "appCategory": NotRequired[Literal["LfR"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCloudFormationStackRecordsRequestGetCloudFormationStackRecordsPaginateTypeDef = TypedDict(
    "GetCloudFormationStackRecordsRequestGetCloudFormationStackRecordsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDiskSnapshotsRequestGetDiskSnapshotsPaginateTypeDef = TypedDict(
    "GetDiskSnapshotsRequestGetDiskSnapshotsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDisksRequestGetDisksPaginateTypeDef = TypedDict(
    "GetDisksRequestGetDisksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDomainsRequestGetDomainsPaginateTypeDef = TypedDict(
    "GetDomainsRequestGetDomainsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetExportSnapshotRecordsRequestGetExportSnapshotRecordsPaginateTypeDef = TypedDict(
    "GetExportSnapshotRecordsRequestGetExportSnapshotRecordsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetInstanceSnapshotsRequestGetInstanceSnapshotsPaginateTypeDef = TypedDict(
    "GetInstanceSnapshotsRequestGetInstanceSnapshotsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetInstancesRequestGetInstancesPaginateTypeDef = TypedDict(
    "GetInstancesRequestGetInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetKeyPairsRequestGetKeyPairsPaginateTypeDef = TypedDict(
    "GetKeyPairsRequestGetKeyPairsPaginateTypeDef",
    {
        "includeDefaultKeyPair": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetLoadBalancersRequestGetLoadBalancersPaginateTypeDef = TypedDict(
    "GetLoadBalancersRequestGetLoadBalancersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetOperationsRequestGetOperationsPaginateTypeDef = TypedDict(
    "GetOperationsRequestGetOperationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRelationalDatabaseBlueprintsRequestGetRelationalDatabaseBlueprintsPaginateTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsRequestGetRelationalDatabaseBlueprintsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRelationalDatabaseBundlesRequestGetRelationalDatabaseBundlesPaginateTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesRequestGetRelationalDatabaseBundlesPaginateTypeDef",
    {
        "includeInactive": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRelationalDatabaseEventsRequestGetRelationalDatabaseEventsPaginateTypeDef = TypedDict(
    "GetRelationalDatabaseEventsRequestGetRelationalDatabaseEventsPaginateTypeDef",
    {
        "relationalDatabaseName": str,
        "durationInMinutes": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRelationalDatabaseParametersRequestGetRelationalDatabaseParametersPaginateTypeDef = TypedDict(
    "GetRelationalDatabaseParametersRequestGetRelationalDatabaseParametersPaginateTypeDef",
    {
        "relationalDatabaseName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRelationalDatabaseSnapshotsRequestGetRelationalDatabaseSnapshotsPaginateTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsRequestGetRelationalDatabaseSnapshotsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRelationalDatabasesRequestGetRelationalDatabasesPaginateTypeDef = TypedDict(
    "GetRelationalDatabasesRequestGetRelationalDatabasesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetStaticIpsRequestGetStaticIpsPaginateTypeDef = TypedDict(
    "GetStaticIpsRequestGetStaticIpsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBucketMetricDataResultTypeDef = TypedDict(
    "GetBucketMetricDataResultTypeDef",
    {
        "metricName": BucketMetricNameType,
        "metricData": List[MetricDatapointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContainerServiceMetricDataResultTypeDef = TypedDict(
    "GetContainerServiceMetricDataResultTypeDef",
    {
        "metricName": ContainerServiceMetricNameType,
        "metricData": List[MetricDatapointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDistributionMetricDataResultTypeDef = TypedDict(
    "GetDistributionMetricDataResultTypeDef",
    {
        "metricName": DistributionMetricNameType,
        "metricData": List[MetricDatapointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceMetricDataResultTypeDef = TypedDict(
    "GetInstanceMetricDataResultTypeDef",
    {
        "metricName": InstanceMetricNameType,
        "metricData": List[MetricDatapointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLoadBalancerMetricDataResultTypeDef = TypedDict(
    "GetLoadBalancerMetricDataResultTypeDef",
    {
        "metricName": LoadBalancerMetricNameType,
        "metricData": List[MetricDatapointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseMetricDataResultTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataResultTypeDef",
    {
        "metricName": RelationalDatabaseMetricNameType,
        "metricData": List[MetricDatapointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstancePortStatesResultTypeDef = TypedDict(
    "GetInstancePortStatesResultTypeDef",
    {
        "portStates": List[InstancePortStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceStateResultTypeDef = TypedDict(
    "GetInstanceStateResultTypeDef",
    {
        "state": InstanceStateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLoadBalancerTlsPoliciesResultTypeDef = TypedDict(
    "GetLoadBalancerTlsPoliciesResultTypeDef",
    {
        "tlsPolicies": List[LoadBalancerTlsPolicyTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseBlueprintsResultTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsResultTypeDef",
    {
        "blueprints": List[RelationalDatabaseBlueprintTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseBundlesResultTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesResultTypeDef",
    {
        "bundles": List[RelationalDatabaseBundleTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseEventsResultTypeDef = TypedDict(
    "GetRelationalDatabaseEventsResultTypeDef",
    {
        "relationalDatabaseEvents": List[RelationalDatabaseEventTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseLogEventsResultTypeDef = TypedDict(
    "GetRelationalDatabaseLogEventsResultTypeDef",
    {
        "resourceLogEvents": List[LogEventTypeDef],
        "nextBackwardToken": str,
        "nextForwardToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseParametersResultTypeDef = TypedDict(
    "GetRelationalDatabaseParametersResultTypeDef",
    {
        "parameters": List[RelationalDatabaseParameterTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRelationalDatabaseParametersRequestRequestTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "parameters": Sequence[RelationalDatabaseParameterTypeDef],
    },
)
HeaderObjectUnionTypeDef = Union[HeaderObjectTypeDef, HeaderObjectOutputTypeDef]
InstanceAccessDetailsTypeDef = TypedDict(
    "InstanceAccessDetailsTypeDef",
    {
        "certKey": NotRequired[str],
        "expiresAt": NotRequired[datetime],
        "ipAddress": NotRequired[str],
        "ipv6Addresses": NotRequired[List[str]],
        "password": NotRequired[str],
        "passwordData": NotRequired[PasswordDataTypeDef],
        "privateKey": NotRequired[str],
        "protocol": NotRequired[InstanceAccessProtocolType],
        "instanceName": NotRequired[str],
        "username": NotRequired[str],
        "hostKeys": NotRequired[List[HostKeyAttributesTypeDef]],
    },
)
InstanceNetworkingTypeDef = TypedDict(
    "InstanceNetworkingTypeDef",
    {
        "monthlyTransfer": NotRequired[MonthlyTransferTypeDef],
        "ports": NotRequired[List[InstancePortInfoTypeDef]],
    },
)
LoadBalancerTlsCertificateDomainValidationRecordTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[str],
        "value": NotRequired[str],
        "validationStatus": NotRequired[LoadBalancerTlsCertificateDomainStatusType],
        "domainName": NotRequired[str],
        "dnsRecordCreationState": NotRequired[
            LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef
        ],
    },
)
LoadBalancerTlsCertificateRenewalSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    {
        "renewalStatus": NotRequired[LoadBalancerTlsCertificateRenewalStatusType],
        "domainValidationOptions": NotRequired[
            List[LoadBalancerTlsCertificateDomainValidationOptionTypeDef]
        ],
    },
)
LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "dnsName": NotRequired[str],
        "state": NotRequired[LoadBalancerStateType],
        "protocol": NotRequired[LoadBalancerProtocolType],
        "publicPorts": NotRequired[List[int]],
        "healthCheckPath": NotRequired[str],
        "instancePort": NotRequired[int],
        "instanceHealthSummary": NotRequired[List[InstanceHealthSummaryTypeDef]],
        "tlsCertificateSummaries": NotRequired[List[LoadBalancerTlsCertificateSummaryTypeDef]],
        "configurationOptions": NotRequired[Dict[LoadBalancerAttributeNameType, str]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "httpsRedirectionEnabled": NotRequired[bool],
        "tlsPolicyName": NotRequired[str],
    },
)
QueryStringObjectUnionTypeDef = Union[QueryStringObjectTypeDef, QueryStringObjectOutputTypeDef]
RegisteredDomainDelegationInfoTypeDef = TypedDict(
    "RegisteredDomainDelegationInfoTypeDef",
    {
        "nameServersUpdateState": NotRequired[NameServersUpdateStateTypeDef],
        "r53HostedZoneDeletionState": NotRequired[R53HostedZoneDeletionStateTypeDef],
    },
)
RelationalDatabaseTypeDef = TypedDict(
    "RelationalDatabaseTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "relationalDatabaseBlueprintId": NotRequired[str],
        "relationalDatabaseBundleId": NotRequired[str],
        "masterDatabaseName": NotRequired[str],
        "hardware": NotRequired[RelationalDatabaseHardwareTypeDef],
        "state": NotRequired[str],
        "secondaryAvailabilityZone": NotRequired[str],
        "backupRetentionEnabled": NotRequired[bool],
        "pendingModifiedValues": NotRequired[PendingModifiedRelationalDatabaseValuesTypeDef],
        "engine": NotRequired[str],
        "engineVersion": NotRequired[str],
        "latestRestorableTime": NotRequired[datetime],
        "masterUsername": NotRequired[str],
        "parameterApplyStatus": NotRequired[str],
        "preferredBackupWindow": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "publiclyAccessible": NotRequired[bool],
        "masterEndpoint": NotRequired[RelationalDatabaseEndpointTypeDef],
        "pendingMaintenanceActions": NotRequired[List[PendingMaintenanceActionTypeDef]],
        "caCertificateIdentifier": NotRequired[str],
    },
)
GetBucketAccessKeysResultTypeDef = TypedDict(
    "GetBucketAccessKeysResultTypeDef",
    {
        "accessKeys": List[AccessKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDiskFromSnapshotRequestRequestTypeDef = TypedDict(
    "CreateDiskFromSnapshotRequestRequestTypeDef",
    {
        "diskName": str,
        "availabilityZone": str,
        "sizeInGb": int,
        "diskSnapshotName": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "addOns": NotRequired[Sequence[AddOnRequestTypeDef]],
        "sourceDiskName": NotRequired[str],
        "restoreDate": NotRequired[str],
        "useLatestRestorableAutoSnapshot": NotRequired[bool],
    },
)
CreateDiskRequestRequestTypeDef = TypedDict(
    "CreateDiskRequestRequestTypeDef",
    {
        "diskName": str,
        "availabilityZone": str,
        "sizeInGb": int,
        "tags": NotRequired[Sequence[TagTypeDef]],
        "addOns": NotRequired[Sequence[AddOnRequestTypeDef]],
    },
)
CreateInstancesFromSnapshotRequestRequestTypeDef = TypedDict(
    "CreateInstancesFromSnapshotRequestRequestTypeDef",
    {
        "instanceNames": Sequence[str],
        "availabilityZone": str,
        "bundleId": str,
        "attachedDiskMapping": NotRequired[Mapping[str, Sequence[DiskMapTypeDef]]],
        "instanceSnapshotName": NotRequired[str],
        "userData": NotRequired[str],
        "keyPairName": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "addOns": NotRequired[Sequence[AddOnRequestTypeDef]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "sourceInstanceName": NotRequired[str],
        "restoreDate": NotRequired[str],
        "useLatestRestorableAutoSnapshot": NotRequired[bool],
    },
)
CreateInstancesRequestRequestTypeDef = TypedDict(
    "CreateInstancesRequestRequestTypeDef",
    {
        "instanceNames": Sequence[str],
        "availabilityZone": str,
        "blueprintId": str,
        "bundleId": str,
        "customImageName": NotRequired[str],
        "userData": NotRequired[str],
        "keyPairName": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "addOns": NotRequired[Sequence[AddOnRequestTypeDef]],
        "ipAddressType": NotRequired[IpAddressTypeType],
    },
)
EnableAddOnRequestRequestTypeDef = TypedDict(
    "EnableAddOnRequestRequestTypeDef",
    {
        "resourceName": str,
        "addOnRequest": AddOnRequestTypeDef,
    },
)
GetAlarmsResultTypeDef = TypedDict(
    "GetAlarmsResultTypeDef",
    {
        "alarms": List[AlarmTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContactMethodsResultTypeDef = TypedDict(
    "GetContactMethodsResultTypeDef",
    {
        "contactMethods": List[ContactMethodTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AllocateStaticIpResultTypeDef = TypedDict(
    "AllocateStaticIpResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachCertificateToDistributionResultTypeDef = TypedDict(
    "AttachCertificateToDistributionResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachDiskResultTypeDef = TypedDict(
    "AttachDiskResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachInstancesToLoadBalancerResultTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachStaticIpResultTypeDef = TypedDict(
    "AttachStaticIpResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CloseInstancePublicPortsResultTypeDef = TypedDict(
    "CloseInstancePublicPortsResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBucketAccessKeyResultTypeDef = TypedDict(
    "CreateBucketAccessKeyResultTypeDef",
    {
        "accessKey": AccessKeyTypeDef,
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCloudFormationStackResultTypeDef = TypedDict(
    "CreateCloudFormationStackResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContactMethodResultTypeDef = TypedDict(
    "CreateContactMethodResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDiskFromSnapshotResultTypeDef = TypedDict(
    "CreateDiskFromSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDiskResultTypeDef = TypedDict(
    "CreateDiskResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDiskSnapshotResultTypeDef = TypedDict(
    "CreateDiskSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDomainEntryResultTypeDef = TypedDict(
    "CreateDomainEntryResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceSnapshotResultTypeDef = TypedDict(
    "CreateInstanceSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstancesFromSnapshotResultTypeDef = TypedDict(
    "CreateInstancesFromSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstancesResultTypeDef = TypedDict(
    "CreateInstancesResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLoadBalancerResultTypeDef = TypedDict(
    "CreateLoadBalancerResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "CreateLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRelationalDatabaseFromSnapshotResultTypeDef = TypedDict(
    "CreateRelationalDatabaseFromSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRelationalDatabaseResultTypeDef = TypedDict(
    "CreateRelationalDatabaseResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "CreateRelationalDatabaseSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAlarmResultTypeDef = TypedDict(
    "DeleteAlarmResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAutoSnapshotResultTypeDef = TypedDict(
    "DeleteAutoSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBucketAccessKeyResultTypeDef = TypedDict(
    "DeleteBucketAccessKeyResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBucketResultTypeDef = TypedDict(
    "DeleteBucketResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCertificateResultTypeDef = TypedDict(
    "DeleteCertificateResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteContactMethodResultTypeDef = TypedDict(
    "DeleteContactMethodResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDiskResultTypeDef = TypedDict(
    "DeleteDiskResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDiskSnapshotResultTypeDef = TypedDict(
    "DeleteDiskSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDistributionResultTypeDef = TypedDict(
    "DeleteDistributionResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainEntryResultTypeDef = TypedDict(
    "DeleteDomainEntryResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInstanceResultTypeDef = TypedDict(
    "DeleteInstanceResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInstanceSnapshotResultTypeDef = TypedDict(
    "DeleteInstanceSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteKeyPairResultTypeDef = TypedDict(
    "DeleteKeyPairResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteKnownHostKeysResultTypeDef = TypedDict(
    "DeleteKnownHostKeysResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLoadBalancerResultTypeDef = TypedDict(
    "DeleteLoadBalancerResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "DeleteLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRelationalDatabaseResultTypeDef = TypedDict(
    "DeleteRelationalDatabaseResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachCertificateFromDistributionResultTypeDef = TypedDict(
    "DetachCertificateFromDistributionResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachDiskResultTypeDef = TypedDict(
    "DetachDiskResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachInstancesFromLoadBalancerResultTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachStaticIpResultTypeDef = TypedDict(
    "DetachStaticIpResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableAddOnResultTypeDef = TypedDict(
    "DisableAddOnResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableAddOnResultTypeDef = TypedDict(
    "EnableAddOnResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportSnapshotResultTypeDef = TypedDict(
    "ExportSnapshotResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOperationResultTypeDef = TypedDict(
    "GetOperationResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOperationsForResourceResultTypeDef = TypedDict(
    "GetOperationsForResourceResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "nextPageCount": str,
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOperationsResultTypeDef = TypedDict(
    "GetOperationsResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportKeyPairResultTypeDef = TypedDict(
    "ImportKeyPairResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OpenInstancePublicPortsResultTypeDef = TypedDict(
    "OpenInstancePublicPortsResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PeerVpcResultTypeDef = TypedDict(
    "PeerVpcResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAlarmResultTypeDef = TypedDict(
    "PutAlarmResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutInstancePublicPortsResultTypeDef = TypedDict(
    "PutInstancePublicPortsResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebootInstanceResultTypeDef = TypedDict(
    "RebootInstanceResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebootRelationalDatabaseResultTypeDef = TypedDict(
    "RebootRelationalDatabaseResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReleaseStaticIpResultTypeDef = TypedDict(
    "ReleaseStaticIpResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetDistributionCacheResultTypeDef = TypedDict(
    "ResetDistributionCacheResultTypeDef",
    {
        "status": str,
        "createTime": datetime,
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendContactMethodVerificationResultTypeDef = TypedDict(
    "SendContactMethodVerificationResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetIpAddressTypeResultTypeDef = TypedDict(
    "SetIpAddressTypeResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetResourceAccessForBucketResultTypeDef = TypedDict(
    "SetResourceAccessForBucketResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetupInstanceHttpsResultTypeDef = TypedDict(
    "SetupInstanceHttpsResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartGUISessionResultTypeDef = TypedDict(
    "StartGUISessionResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartInstanceResultTypeDef = TypedDict(
    "StartInstanceResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRelationalDatabaseResultTypeDef = TypedDict(
    "StartRelationalDatabaseResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopGUISessionResultTypeDef = TypedDict(
    "StopGUISessionResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopInstanceResultTypeDef = TypedDict(
    "StopInstanceResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopRelationalDatabaseResultTypeDef = TypedDict(
    "StopRelationalDatabaseResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceResultTypeDef = TypedDict(
    "TagResourceResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestAlarmResultTypeDef = TypedDict(
    "TestAlarmResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnpeerVpcResultTypeDef = TypedDict(
    "UnpeerVpcResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UntagResourceResultTypeDef = TypedDict(
    "UntagResourceResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBucketBundleResultTypeDef = TypedDict(
    "UpdateBucketBundleResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDistributionBundleResultTypeDef = TypedDict(
    "UpdateDistributionBundleResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainEntryResultTypeDef = TypedDict(
    "UpdateDomainEntryResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateInstanceMetadataOptionsResultTypeDef = TypedDict(
    "UpdateInstanceMetadataOptionsResultTypeDef",
    {
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLoadBalancerAttributeResultTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRelationalDatabaseParametersResultTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRelationalDatabaseResultTypeDef = TypedDict(
    "UpdateRelationalDatabaseResultTypeDef",
    {
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetupHistoryTypeDef = TypedDict(
    "SetupHistoryTypeDef",
    {
        "operationId": NotRequired[str],
        "request": NotRequired[SetupRequestTypeDef],
        "resource": NotRequired[SetupHistoryResourceTypeDef],
        "executionDetails": NotRequired[List[SetupExecutionDetailsTypeDef]],
        "status": NotRequired[SetupStatusType],
    },
)
GetStaticIpResultTypeDef = TypedDict(
    "GetStaticIpResultTypeDef",
    {
        "staticIp": StaticIpTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStaticIpsResultTypeDef = TypedDict(
    "GetStaticIpsResultTypeDef",
    {
        "staticIps": List[StaticIpTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAutoSnapshotsResultTypeDef = TypedDict(
    "GetAutoSnapshotsResultTypeDef",
    {
        "resourceName": str,
        "resourceType": ResourceTypeType,
        "autoSnapshots": List[AutoSnapshotDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegionsResultTypeDef = TypedDict(
    "GetRegionsResultTypeDef",
    {
        "regions": List[RegionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBucketResultTypeDef = TypedDict(
    "CreateBucketResultTypeDef",
    {
        "bucket": BucketTypeDef,
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBucketsResultTypeDef = TypedDict(
    "GetBucketsResultTypeDef",
    {
        "buckets": List[BucketTypeDef],
        "nextPageToken": str,
        "accountLevelBpaSync": AccountLevelBpaSyncTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBucketResultTypeDef = TypedDict(
    "UpdateBucketResultTypeDef",
    {
        "bucket": BucketTypeDef,
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDiskSnapshotResultTypeDef = TypedDict(
    "GetDiskSnapshotResultTypeDef",
    {
        "diskSnapshot": DiskSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDiskSnapshotsResultTypeDef = TypedDict(
    "GetDiskSnapshotsResultTypeDef",
    {
        "diskSnapshots": List[DiskSnapshotTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDiskResultTypeDef = TypedDict(
    "GetDiskResultTypeDef",
    {
        "disk": DiskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDisksResultTypeDef = TypedDict(
    "GetDisksResultTypeDef",
    {
        "disks": List[DiskTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceHardwareTypeDef = TypedDict(
    "InstanceHardwareTypeDef",
    {
        "cpuCount": NotRequired[int],
        "disks": NotRequired[List[DiskTypeDef]],
        "ramSizeInGb": NotRequired[float],
    },
)
InstanceSnapshotTypeDef = TypedDict(
    "InstanceSnapshotTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "state": NotRequired[InstanceSnapshotStateType],
        "progress": NotRequired[str],
        "fromAttachedDisks": NotRequired[List[DiskTypeDef]],
        "fromInstanceName": NotRequired[str],
        "fromInstanceArn": NotRequired[str],
        "fromBlueprintId": NotRequired[str],
        "fromBundleId": NotRequired[str],
        "isFromAutoSnapshot": NotRequired[bool],
        "sizeInGb": NotRequired[int],
    },
)
CreateKeyPairResultTypeDef = TypedDict(
    "CreateKeyPairResultTypeDef",
    {
        "keyPair": KeyPairTypeDef,
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyPairResultTypeDef = TypedDict(
    "GetKeyPairResultTypeDef",
    {
        "keyPair": KeyPairTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyPairsResultTypeDef = TypedDict(
    "GetKeyPairsResultTypeDef",
    {
        "keyPairs": List[KeyPairTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotResultTypeDef",
    {
        "relationalDatabaseSnapshot": RelationalDatabaseSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabaseSnapshotsResultTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsResultTypeDef",
    {
        "relationalDatabaseSnapshots": List[RelationalDatabaseSnapshotTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LightsailDistributionTypeDef = TypedDict(
    "LightsailDistributionTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "alternativeDomainNames": NotRequired[List[str]],
        "status": NotRequired[str],
        "isEnabled": NotRequired[bool],
        "domainName": NotRequired[str],
        "bundleId": NotRequired[str],
        "certificateName": NotRequired[str],
        "origin": NotRequired[OriginTypeDef],
        "originPublicDNS": NotRequired[str],
        "defaultCacheBehavior": NotRequired[CacheBehaviorTypeDef],
        "cacheBehaviorSettings": NotRequired[CacheSettingsOutputTypeDef],
        "cacheBehaviors": NotRequired[List[CacheBehaviorPerPathTypeDef]],
        "ableToUpdateBundle": NotRequired[bool],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "viewerMinimumTlsProtocolVersion": NotRequired[str],
    },
)
GetCloudFormationStackRecordsResultTypeDef = TypedDict(
    "GetCloudFormationStackRecordsResultTypeDef",
    {
        "cloudFormationStackRecords": List[CloudFormationStackRecordTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContainerServiceRequestRequestTypeDef = TypedDict(
    "UpdateContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
        "power": NotRequired[ContainerServicePowerNameType],
        "scale": NotRequired[int],
        "isDisabled": NotRequired[bool],
        "publicDomainNames": NotRequired[Mapping[str, Sequence[str]]],
        "privateRegistryAccess": NotRequired[PrivateRegistryAccessRequestTypeDef],
    },
)
ContainerServiceDeploymentTypeDef = TypedDict(
    "ContainerServiceDeploymentTypeDef",
    {
        "version": NotRequired[int],
        "state": NotRequired[ContainerServiceDeploymentStateType],
        "containers": NotRequired[Dict[str, ContainerOutputTypeDef]],
        "publicEndpoint": NotRequired[ContainerServiceEndpointTypeDef],
        "createdAt": NotRequired[datetime],
    },
)
ContainerServiceDeploymentRequestTypeDef = TypedDict(
    "ContainerServiceDeploymentRequestTypeDef",
    {
        "containers": NotRequired[Mapping[str, ContainerUnionTypeDef]],
        "publicEndpoint": NotRequired[EndpointRequestTypeDef],
    },
)
CreateContainerServiceDeploymentRequestRequestTypeDef = TypedDict(
    "CreateContainerServiceDeploymentRequestRequestTypeDef",
    {
        "serviceName": str,
        "containers": NotRequired[Mapping[str, ContainerUnionTypeDef]],
        "publicEndpoint": NotRequired[EndpointRequestTypeDef],
    },
)
ExportSnapshotRecordSourceInfoTypeDef = TypedDict(
    "ExportSnapshotRecordSourceInfoTypeDef",
    {
        "resourceType": NotRequired[ExportSnapshotRecordSourceTypeType],
        "createdAt": NotRequired[datetime],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "fromResourceName": NotRequired[str],
        "fromResourceArn": NotRequired[str],
        "instanceSnapshotInfo": NotRequired[InstanceSnapshotInfoTypeDef],
        "diskSnapshotInfo": NotRequired[DiskSnapshotInfoTypeDef],
    },
)
RenewalSummaryTypeDef = TypedDict(
    "RenewalSummaryTypeDef",
    {
        "domainValidationRecords": NotRequired[List[DomainValidationRecordTypeDef]],
        "renewalStatus": NotRequired[RenewalStatusType],
        "renewalStatusReason": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
CostEstimateTypeDef = TypedDict(
    "CostEstimateTypeDef",
    {
        "usageType": NotRequired[str],
        "resultsByTime": NotRequired[List[EstimateByTimeTypeDef]],
    },
)
GetInstanceAccessDetailsResultTypeDef = TypedDict(
    "GetInstanceAccessDetailsResultTypeDef",
    {
        "accessDetails": InstanceAccessDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoadBalancerTlsCertificateTypeDef = TypedDict(
    "LoadBalancerTlsCertificateTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "loadBalancerName": NotRequired[str],
        "isAttached": NotRequired[bool],
        "status": NotRequired[LoadBalancerTlsCertificateStatusType],
        "domainName": NotRequired[str],
        "domainValidationRecords": NotRequired[
            List[LoadBalancerTlsCertificateDomainValidationRecordTypeDef]
        ],
        "failureReason": NotRequired[LoadBalancerTlsCertificateFailureReasonType],
        "issuedAt": NotRequired[datetime],
        "issuer": NotRequired[str],
        "keyAlgorithm": NotRequired[str],
        "notAfter": NotRequired[datetime],
        "notBefore": NotRequired[datetime],
        "renewalSummary": NotRequired[LoadBalancerTlsCertificateRenewalSummaryTypeDef],
        "revocationReason": NotRequired[LoadBalancerTlsCertificateRevocationReasonType],
        "revokedAt": NotRequired[datetime],
        "serial": NotRequired[str],
        "signatureAlgorithm": NotRequired[str],
        "subject": NotRequired[str],
        "subjectAlternativeNames": NotRequired[List[str]],
    },
)
GetLoadBalancerResultTypeDef = TypedDict(
    "GetLoadBalancerResultTypeDef",
    {
        "loadBalancer": LoadBalancerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLoadBalancersResultTypeDef = TypedDict(
    "GetLoadBalancersResultTypeDef",
    {
        "loadBalancers": List[LoadBalancerTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheSettingsTypeDef = TypedDict(
    "CacheSettingsTypeDef",
    {
        "defaultTTL": NotRequired[int],
        "minimumTTL": NotRequired[int],
        "maximumTTL": NotRequired[int],
        "allowedHTTPMethods": NotRequired[str],
        "cachedHTTPMethods": NotRequired[str],
        "forwardedCookies": NotRequired[CookieObjectUnionTypeDef],
        "forwardedHeaders": NotRequired[HeaderObjectUnionTypeDef],
        "forwardedQueryStrings": NotRequired[QueryStringObjectUnionTypeDef],
    },
)
DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "domainEntries": NotRequired[List[DomainEntryOutputTypeDef]],
        "registeredDomainDelegationInfo": NotRequired[RegisteredDomainDelegationInfoTypeDef],
    },
)
GetRelationalDatabaseResultTypeDef = TypedDict(
    "GetRelationalDatabaseResultTypeDef",
    {
        "relationalDatabase": RelationalDatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRelationalDatabasesResultTypeDef = TypedDict(
    "GetRelationalDatabasesResultTypeDef",
    {
        "relationalDatabases": List[RelationalDatabaseTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSetupHistoryResultTypeDef = TypedDict(
    "GetSetupHistoryResultTypeDef",
    {
        "setupHistory": List[SetupHistoryTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "blueprintId": NotRequired[str],
        "blueprintName": NotRequired[str],
        "bundleId": NotRequired[str],
        "addOns": NotRequired[List[AddOnTypeDef]],
        "isStaticIp": NotRequired[bool],
        "privateIpAddress": NotRequired[str],
        "publicIpAddress": NotRequired[str],
        "ipv6Addresses": NotRequired[List[str]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "hardware": NotRequired[InstanceHardwareTypeDef],
        "networking": NotRequired[InstanceNetworkingTypeDef],
        "state": NotRequired[InstanceStateTypeDef],
        "username": NotRequired[str],
        "sshKeyName": NotRequired[str],
        "metadataOptions": NotRequired[InstanceMetadataOptionsTypeDef],
    },
)
GetInstanceSnapshotResultTypeDef = TypedDict(
    "GetInstanceSnapshotResultTypeDef",
    {
        "instanceSnapshot": InstanceSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceSnapshotsResultTypeDef = TypedDict(
    "GetInstanceSnapshotsResultTypeDef",
    {
        "instanceSnapshots": List[InstanceSnapshotTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {
        "distribution": LightsailDistributionTypeDef,
        "operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDistributionsResultTypeDef = TypedDict(
    "GetDistributionsResultTypeDef",
    {
        "distributions": List[LightsailDistributionTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContainerServiceTypeDef = TypedDict(
    "ContainerServiceTypeDef",
    {
        "containerServiceName": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List[TagTypeDef]],
        "power": NotRequired[ContainerServicePowerNameType],
        "powerId": NotRequired[str],
        "state": NotRequired[ContainerServiceStateType],
        "stateDetail": NotRequired[ContainerServiceStateDetailTypeDef],
        "scale": NotRequired[int],
        "currentDeployment": NotRequired[ContainerServiceDeploymentTypeDef],
        "nextDeployment": NotRequired[ContainerServiceDeploymentTypeDef],
        "isDisabled": NotRequired[bool],
        "principalArn": NotRequired[str],
        "privateDomainName": NotRequired[str],
        "publicDomainNames": NotRequired[Dict[str, List[str]]],
        "url": NotRequired[str],
        "privateRegistryAccess": NotRequired[PrivateRegistryAccessTypeDef],
    },
)
GetContainerServiceDeploymentsResultTypeDef = TypedDict(
    "GetContainerServiceDeploymentsResultTypeDef",
    {
        "deployments": List[ContainerServiceDeploymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContainerServiceRequestRequestTypeDef = TypedDict(
    "CreateContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
        "power": ContainerServicePowerNameType,
        "scale": int,
        "tags": NotRequired[Sequence[TagTypeDef]],
        "publicDomainNames": NotRequired[Mapping[str, Sequence[str]]],
        "deployment": NotRequired[ContainerServiceDeploymentRequestTypeDef],
        "privateRegistryAccess": NotRequired[PrivateRegistryAccessRequestTypeDef],
    },
)
ExportSnapshotRecordTypeDef = TypedDict(
    "ExportSnapshotRecordTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired[ResourceLocationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "state": NotRequired[RecordStateType],
        "sourceInfo": NotRequired[ExportSnapshotRecordSourceInfoTypeDef],
        "destinationInfo": NotRequired[DestinationInfoTypeDef],
    },
)
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "domainName": NotRequired[str],
        "status": NotRequired[CertificateStatusType],
        "serialNumber": NotRequired[str],
        "subjectAlternativeNames": NotRequired[List[str]],
        "domainValidationRecords": NotRequired[List[DomainValidationRecordTypeDef]],
        "requestFailureReason": NotRequired[str],
        "inUseResourceCount": NotRequired[int],
        "keyAlgorithm": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "issuedAt": NotRequired[datetime],
        "issuerCA": NotRequired[str],
        "notBefore": NotRequired[datetime],
        "notAfter": NotRequired[datetime],
        "eligibleToRenew": NotRequired[str],
        "renewalSummary": NotRequired[RenewalSummaryTypeDef],
        "revokedAt": NotRequired[datetime],
        "revocationReason": NotRequired[str],
        "tags": NotRequired[List[TagTypeDef]],
        "supportCode": NotRequired[str],
    },
)
ResourceBudgetEstimateTypeDef = TypedDict(
    "ResourceBudgetEstimateTypeDef",
    {
        "resourceName": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "costEstimates": NotRequired[List[CostEstimateTypeDef]],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
GetLoadBalancerTlsCertificatesResultTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesResultTypeDef",
    {
        "tlsCertificates": List[LoadBalancerTlsCertificateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDistributionRequestRequestTypeDef = TypedDict(
    "CreateDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
        "origin": InputOriginTypeDef,
        "defaultCacheBehavior": CacheBehaviorTypeDef,
        "bundleId": str,
        "cacheBehaviorSettings": NotRequired[CacheSettingsTypeDef],
        "cacheBehaviors": NotRequired[Sequence[CacheBehaviorPerPathTypeDef]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "certificateName": NotRequired[str],
        "viewerMinimumTlsProtocolVersion": NotRequired[ViewerMinimumTlsProtocolVersionEnumType],
    },
)
UpdateDistributionRequestRequestTypeDef = TypedDict(
    "UpdateDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
        "origin": NotRequired[InputOriginTypeDef],
        "defaultCacheBehavior": NotRequired[CacheBehaviorTypeDef],
        "cacheBehaviorSettings": NotRequired[CacheSettingsTypeDef],
        "cacheBehaviors": NotRequired[Sequence[CacheBehaviorPerPathTypeDef]],
        "isEnabled": NotRequired[bool],
        "viewerMinimumTlsProtocolVersion": NotRequired[ViewerMinimumTlsProtocolVersionEnumType],
        "certificateName": NotRequired[str],
        "useDefaultCertificate": NotRequired[bool],
    },
)
GetDomainResultTypeDef = TypedDict(
    "GetDomainResultTypeDef",
    {
        "domain": DomainTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainsResultTypeDef = TypedDict(
    "GetDomainsResultTypeDef",
    {
        "domains": List[DomainTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceResultTypeDef = TypedDict(
    "GetInstanceResultTypeDef",
    {
        "instance": InstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstancesResultTypeDef = TypedDict(
    "GetInstancesResultTypeDef",
    {
        "instances": List[InstanceTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContainerServicesListResultTypeDef = TypedDict(
    "ContainerServicesListResultTypeDef",
    {
        "containerServices": List[ContainerServiceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContainerServiceDeploymentResultTypeDef = TypedDict(
    "CreateContainerServiceDeploymentResultTypeDef",
    {
        "containerService": ContainerServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContainerServiceResultTypeDef = TypedDict(
    "CreateContainerServiceResultTypeDef",
    {
        "containerService": ContainerServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContainerServiceResultTypeDef = TypedDict(
    "UpdateContainerServiceResultTypeDef",
    {
        "containerService": ContainerServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExportSnapshotRecordsResultTypeDef = TypedDict(
    "GetExportSnapshotRecordsResultTypeDef",
    {
        "exportSnapshotRecords": List[ExportSnapshotRecordTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "certificateArn": NotRequired[str],
        "certificateName": NotRequired[str],
        "domainName": NotRequired[str],
        "certificateDetail": NotRequired[CertificateTypeDef],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
GetCostEstimateResultTypeDef = TypedDict(
    "GetCostEstimateResultTypeDef",
    {
        "resourcesBudgetEstimate": List[ResourceBudgetEstimateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCertificateResultTypeDef = TypedDict(
    "CreateCertificateResultTypeDef",
    {
        "certificate": CertificateSummaryTypeDef,
        "operations": List[OperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCertificatesResultTypeDef = TypedDict(
    "GetCertificatesResultTypeDef",
    {
        "certificates": List[CertificateSummaryTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
