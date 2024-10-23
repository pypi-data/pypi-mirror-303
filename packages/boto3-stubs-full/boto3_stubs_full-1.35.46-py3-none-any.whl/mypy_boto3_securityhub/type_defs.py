"""
Type annotations for securityhub service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/type_defs/)

Usage::

    ```python
    from mypy_boto3_securityhub.type_defs import AcceptAdministratorInvitationRequestRequestTypeDef

    data: AcceptAdministratorInvitationRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AdminStatusType,
    AssociationStatusType,
    AssociationTypeType,
    AutoEnableStandardsType,
    AwsIamAccessKeyStatusType,
    AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType,
    ComplianceStatusType,
    ConfigurationPolicyAssociationStatusType,
    ControlFindingGeneratorType,
    ControlStatusType,
    FindingHistoryUpdateSourceTypeType,
    IntegrationTypeType,
    MalwareStateType,
    MalwareTypeType,
    MapFilterComparisonType,
    NetworkDirectionType,
    OrganizationConfigurationConfigurationTypeType,
    OrganizationConfigurationStatusType,
    ParameterValueTypeType,
    PartitionType,
    RecordStateType,
    RegionAvailabilityStatusType,
    RuleStatusType,
    SeverityLabelType,
    SeverityRatingType,
    SortOrderType,
    StandardsStatusType,
    StatusReasonCodeType,
    StringFilterComparisonType,
    TargetTypeType,
    ThreatIntelIndicatorCategoryType,
    ThreatIntelIndicatorTypeType,
    UnprocessedErrorCodeType,
    UpdateStatusType,
    VerificationStateType,
    VulnerabilityExploitAvailableType,
    VulnerabilityFixAvailableType,
    WorkflowStateType,
    WorkflowStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    "AcceptInvitationRequestRequestTypeDef",
    "AccountDetailsTypeDef",
    "ActionLocalIpDetailsTypeDef",
    "ActionLocalPortDetailsTypeDef",
    "DnsRequestActionTypeDef",
    "CityTypeDef",
    "CountryTypeDef",
    "GeoLocationTypeDef",
    "IpOrganizationDetailsTypeDef",
    "ActionRemotePortDetailsTypeDef",
    "ActionTargetTypeDef",
    "AdjustmentTypeDef",
    "AdminAccountTypeDef",
    "AssociatedStandardTypeDef",
    "AssociationFiltersTypeDef",
    "AssociationStateDetailsTypeDef",
    "NoteUpdateTypeDef",
    "RelatedFindingTypeDef",
    "SeverityUpdateTypeDef",
    "WorkflowUpdateTypeDef",
    "MapFilterTypeDef",
    "NumberFilterTypeDef",
    "StringFilterTypeDef",
    "AutomationRulesMetadataTypeDef",
    "AvailabilityZoneTypeDef",
    "AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef",
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef",
    "AwsAmazonMqBrokerUsersDetailsTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef",
    "AwsAmazonMqBrokerLogsPendingDetailsTypeDef",
    "AwsApiCallActionDomainDetailsTypeDef",
    "AwsApiGatewayAccessLogSettingsTypeDef",
    "AwsApiGatewayCanarySettingsOutputTypeDef",
    "AwsApiGatewayCanarySettingsTypeDef",
    "AwsApiGatewayEndpointConfigurationOutputTypeDef",
    "AwsApiGatewayEndpointConfigurationTypeDef",
    "AwsApiGatewayMethodSettingsTypeDef",
    "AwsCorsConfigurationOutputTypeDef",
    "AwsApiGatewayV2RouteSettingsTypeDef",
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiLogConfigDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef",
    "AwsBackupBackupPlanLifecycleDetailsTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsOutputTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsTypeDef",
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef",
    "AwsBackupRecoveryPointCreatedByDetailsTypeDef",
    "AwsBackupRecoveryPointLifecycleDetailsTypeDef",
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    "AwsCertificateManagerCertificateOptionsTypeDef",
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    "AwsCloudFormationStackDriftInformationDetailsTypeDef",
    "AwsCloudFormationStackOutputsDetailsTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionLoggingTypeDef",
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsTypeDef",
    "AwsCloudTrailTrailDetailsTypeDef",
    "AwsCloudWatchAlarmDimensionsDetailsTypeDef",
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    "AwsCodeBuildProjectSourceTypeDef",
    "AwsCodeBuildProjectVpcConfigOutputTypeDef",
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    "AwsCodeBuildProjectVpcConfigTypeDef",
    "AwsCorsConfigurationTypeDef",
    "AwsDmsEndpointDetailsTypeDef",
    "AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef",
    "AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef",
    "AwsDmsReplicationTaskDetailsTypeDef",
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    "AwsDynamoDbTableKeySchemaTypeDef",
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    "AwsDynamoDbTableSseDescriptionTypeDef",
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    "AwsDynamoDbTableProjectionOutputTypeDef",
    "AwsDynamoDbTableProjectionTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef",
    "AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef",
    "AwsEc2EipDetailsTypeDef",
    "AwsEc2InstanceMetadataOptionsTypeDef",
    "AwsEc2InstanceMonitoringDetailsTypeDef",
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef",
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef",
    "AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef",
    "AwsEc2LaunchTemplateDataPlacementDetailsTypeDef",
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef",
    "AwsEc2NetworkAclAssociationTypeDef",
    "IcmpTypeCodeTypeDef",
    "PortRangeFromToTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "PropagatingVgwSetDetailsTypeDef",
    "RouteSetDetailsTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "Ipv6CidrBlockAssociationTypeDef",
    "AwsEc2TransitGatewayDetailsOutputTypeDef",
    "AwsEc2TransitGatewayDetailsTypeDef",
    "AwsEc2VolumeAttachmentTypeDef",
    "CidrBlockAssociationTypeDef",
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionStatusDetailsTypeDef",
    "VpcInfoCidrBlockSetDetailsTypeDef",
    "VpcInfoIpv6CidrBlockSetDetailsTypeDef",
    "VpcInfoPeeringOptionsDetailsTypeDef",
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    "AwsEcrContainerImageDetailsOutputTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    "AwsMountPointTypeDef",
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    "AwsEcsTaskVolumeHostDetailsTypeDef",
    "AwsEfsAccessPointPosixUserDetailsOutputTypeDef",
    "AwsEfsAccessPointPosixUserDetailsTypeDef",
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsOutputTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    "AwsElbAppCookieStickinessPolicyTypeDef",
    "AwsElbLbCookieStickinessPolicyTypeDef",
    "AwsElbLoadBalancerAccessLogTypeDef",
    "AwsElbLoadBalancerAdditionalAttributeTypeDef",
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    "AwsElbLoadBalancerHealthCheckTypeDef",
    "AwsElbLoadBalancerInstanceTypeDef",
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    "AwsElbLoadBalancerListenerTypeDef",
    "AwsElbv2LoadBalancerAttributeTypeDef",
    "LoadBalancerStateTypeDef",
    "AwsEventSchemasRegistryDetailsTypeDef",
    "AwsEventsEndpointEventBusesDetailsTypeDef",
    "AwsEventsEndpointReplicationConfigDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef",
    "AwsEventsEventbusDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef",
    "AwsGuardDutyDetectorFeaturesDetailsTypeDef",
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    "AwsIamAttachedManagedPolicyTypeDef",
    "AwsIamGroupPolicyTypeDef",
    "AwsIamInstanceProfileRoleTypeDef",
    "AwsIamPermissionsBoundaryTypeDef",
    "AwsIamPolicyVersionTypeDef",
    "AwsIamRolePolicyTypeDef",
    "AwsIamUserPolicyTypeDef",
    "AwsKinesisStreamStreamEncryptionDetailsTypeDef",
    "AwsKmsKeyDetailsTypeDef",
    "AwsLambdaFunctionCodeTypeDef",
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    "AwsLambdaFunctionLayerTypeDef",
    "AwsLambdaFunctionTracingConfigTypeDef",
    "AwsLambdaFunctionVpcConfigOutputTypeDef",
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    "AwsLambdaFunctionVpcConfigTypeDef",
    "AwsLambdaLayerVersionDetailsOutputTypeDef",
    "AwsLambdaLayerVersionDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef",
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    "AwsRdsDbClusterMemberTypeDef",
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    "AwsRdsDbDomainMembershipTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef",
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    "AwsRdsDbInstanceEndpointTypeDef",
    "AwsRdsDbOptionGroupMembershipTypeDef",
    "AwsRdsDbParameterGroupTypeDef",
    "AwsRdsDbProcessorFeatureTypeDef",
    "AwsRdsDbStatusInfoTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsOutputTypeDef",
    "AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef",
    "AwsRdsDbSecurityGroupIpRangeTypeDef",
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    "AwsRdsEventSubscriptionDetailsOutputTypeDef",
    "AwsRdsEventSubscriptionDetailsTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    "AwsRedshiftClusterClusterNodeTypeDef",
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    "AwsRedshiftClusterEndpointTypeDef",
    "AwsRedshiftClusterHsmStatusTypeDef",
    "AwsRedshiftClusterIamRoleTypeDef",
    "AwsRedshiftClusterLoggingStatusTypeDef",
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    "AwsRedshiftClusterResizeInfoTypeDef",
    "AwsRedshiftClusterRestoreStatusTypeDef",
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    "AwsRoute53HostedZoneConfigDetailsTypeDef",
    "AwsRoute53HostedZoneVpcDetailsTypeDef",
    "CloudWatchLogsLogGroupArnConfigDetailsTypeDef",
    "AwsS3AccessPointVpcConfigurationDetailsTypeDef",
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    "AwsS3BucketLoggingConfigurationTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef",
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    "AwsS3ObjectDetailsTypeDef",
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef",
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    "BooleanFilterTypeDef",
    "IpFilterTypeDef",
    "KeywordFilterTypeDef",
    "AwsSecurityFindingIdentifierTypeDef",
    "GeneratorDetailsOutputTypeDef",
    "MalwareTypeDef",
    "NoteTypeDef",
    "PatchSummaryTypeDef",
    "ProcessDetailsTypeDef",
    "SeverityTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "WorkflowTypeDef",
    "AwsSnsTopicSubscriptionTypeDef",
    "AwsSqsQueueDetailsTypeDef",
    "AwsSsmComplianceSummaryTypeDef",
    "AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef",
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRulePredicateListDetailsTypeDef",
    "AwsWafRegionalRuleGroupRulesActionDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListActionDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef",
    "AwsWafRulePredicateListDetailsTypeDef",
    "AwsWafRuleGroupRulesActionDetailsTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "AwsWafv2CustomHttpHeaderTypeDef",
    "AwsWafv2VisibilityConfigDetailsTypeDef",
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef",
    "AwsXrayEncryptionConfigDetailsTypeDef",
    "BatchDeleteAutomationRulesRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UnprocessedAutomationRuleTypeDef",
    "BatchDisableStandardsRequestRequestTypeDef",
    "StandardsSubscriptionRequestTypeDef",
    "BatchGetAutomationRulesRequestRequestTypeDef",
    "ConfigurationPolicyAssociationSummaryTypeDef",
    "BatchGetSecurityControlsRequestRequestTypeDef",
    "UnprocessedSecurityControlTypeDef",
    "StandardsControlAssociationIdTypeDef",
    "StandardsControlAssociationDetailTypeDef",
    "ImportFindingsErrorTypeDef",
    "StandardsControlAssociationUpdateTypeDef",
    "BooleanConfigurationOptionsTypeDef",
    "CellTypeDef",
    "ClassificationStatusTypeDef",
    "CodeVulnerabilitiesFilePathTypeDef",
    "SecurityControlParameterOutputTypeDef",
    "StatusReasonTypeDef",
    "DoubleConfigurationOptionsTypeDef",
    "EnumConfigurationOptionsTypeDef",
    "EnumListConfigurationOptionsTypeDef",
    "IntegerConfigurationOptionsTypeDef",
    "IntegerListConfigurationOptionsTypeDef",
    "StringConfigurationOptionsTypeDef",
    "StringListConfigurationOptionsTypeDef",
    "TargetTypeDef",
    "ConfigurationPolicySummaryTypeDef",
    "VolumeMountTypeDef",
    "CreateActionTargetRequestRequestTypeDef",
    "CreateFindingAggregatorRequestRequestTypeDef",
    "ResultTypeDef",
    "DateRangeTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeleteActionTargetRequestRequestTypeDef",
    "DeleteConfigurationPolicyRequestRequestTypeDef",
    "DeleteFindingAggregatorRequestRequestTypeDef",
    "DeleteInsightRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeActionTargetsRequestRequestTypeDef",
    "DescribeHubRequestRequestTypeDef",
    "OrganizationConfigurationTypeDef",
    "DescribeProductsRequestRequestTypeDef",
    "ProductTypeDef",
    "DescribeStandardsControlsRequestRequestTypeDef",
    "StandardsControlTypeDef",
    "DescribeStandardsRequestRequestTypeDef",
    "DisableImportFindingsForProductRequestRequestTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "EnableImportFindingsForProductRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "EnableSecurityHubRequestRequestTypeDef",
    "FilePathsTypeDef",
    "FindingAggregatorTypeDef",
    "FindingHistoryUpdateSourceTypeDef",
    "FindingHistoryUpdateTypeDef",
    "FindingProviderSeverityTypeDef",
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    "GeneratorDetailsTypeDef",
    "InvitationTypeDef",
    "GetConfigurationPolicyRequestRequestTypeDef",
    "GetEnabledStandardsRequestRequestTypeDef",
    "GetFindingAggregatorRequestRequestTypeDef",
    "TimestampTypeDef",
    "SortCriterionTypeDef",
    "GetInsightResultsRequestRequestTypeDef",
    "GetInsightsRequestRequestTypeDef",
    "GetMembersRequestRequestTypeDef",
    "MemberTypeDef",
    "GetSecurityControlDefinitionRequestRequestTypeDef",
    "InsightResultValueTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "ListAutomationRulesRequestRequestTypeDef",
    "ListConfigurationPoliciesRequestRequestTypeDef",
    "ListEnabledProductsForImportRequestRequestTypeDef",
    "ListFindingAggregatorsRequestRequestTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListSecurityControlDefinitionsRequestRequestTypeDef",
    "ListStandardsControlAssociationsRequestRequestTypeDef",
    "StandardsControlAssociationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PortRangeTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "ParameterValueOutputTypeDef",
    "ParameterValueTypeDef",
    "RecommendationTypeDef",
    "RuleGroupSourceListDetailsOutputTypeDef",
    "RuleGroupSourceListDetailsTypeDef",
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    "RuleGroupVariablesIpSetsDetailsOutputTypeDef",
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    "RuleGroupVariablesPortSetsDetailsOutputTypeDef",
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    "SecurityControlParameterTypeDef",
    "SoftwarePackageTypeDef",
    "StandardsManagedByTypeDef",
    "StandardsStatusReasonTypeDef",
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateActionTargetRequestRequestTypeDef",
    "UpdateFindingAggregatorRequestRequestTypeDef",
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    "UpdateStandardsControlRequestRequestTypeDef",
    "VulnerabilityVendorTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "ActionRemoteIpDetailsTypeDef",
    "CvssOutputTypeDef",
    "CvssTypeDef",
    "ListConfigurationPolicyAssociationsRequestRequestTypeDef",
    "AssociationSetDetailsTypeDef",
    "AutomationRulesFindingFieldsUpdateOutputTypeDef",
    "AutomationRulesFindingFieldsUpdateTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsUnionTypeDef",
    "AwsAmazonMqBrokerLogsDetailsTypeDef",
    "AwsApiGatewayCanarySettingsUnionTypeDef",
    "AwsApiGatewayRestApiDetailsOutputTypeDef",
    "AwsApiGatewayEndpointConfigurationUnionTypeDef",
    "AwsApiGatewayStageDetailsOutputTypeDef",
    "AwsApiGatewayV2ApiDetailsOutputTypeDef",
    "AwsApiGatewayV2StageDetailsOutputTypeDef",
    "AwsApiGatewayV2StageDetailsTypeDef",
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnionTypeDef",
    "AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef",
    "AwsBackupBackupVaultDetailsOutputTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsUnionTypeDef",
    "AwsBackupRecoveryPointDetailsTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    "AwsCloudFormationStackDetailsOutputTypeDef",
    "AwsCloudFormationStackDetailsTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnionTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsUnionTypeDef",
    "AwsCloudWatchAlarmDetailsOutputTypeDef",
    "AwsCloudWatchAlarmDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentOutputTypeDef",
    "AwsCodeBuildProjectEnvironmentTypeDef",
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    "AwsCodeBuildProjectVpcConfigUnionTypeDef",
    "AwsCorsConfigurationUnionTypeDef",
    "AwsDmsReplicationInstanceDetailsOutputTypeDef",
    "AwsDmsReplicationInstanceDetailsTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef",
    "AwsDynamoDbTableProjectionUnionTypeDef",
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef",
    "AwsEc2InstanceDetailsOutputTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef",
    "AwsEc2NetworkAclEntryTypeDef",
    "AwsEc2NetworkInterfaceDetailsOutputTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2SecurityGroupIpPermissionOutputTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SubnetDetailsOutputTypeDef",
    "AwsEc2SubnetDetailsTypeDef",
    "AwsEc2TransitGatewayDetailsUnionTypeDef",
    "AwsEc2VolumeDetailsOutputTypeDef",
    "AwsEc2VolumeDetailsTypeDef",
    "AwsEc2VpcDetailsOutputTypeDef",
    "AwsEc2VpcDetailsTypeDef",
    "AwsEc2VpcEndpointServiceDetailsOutputTypeDef",
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsOutputTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnionTypeDef",
    "AwsEcrContainerImageDetailsUnionTypeDef",
    "AwsEcrRepositoryDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    "AwsEcsContainerDetailsOutputTypeDef",
    "AwsEcsContainerDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskVolumeDetailsTypeDef",
    "AwsEfsAccessPointPosixUserDetailsUnionTypeDef",
    "AwsEfsAccessPointRootDirectoryDetailsTypeDef",
    "AwsEksClusterLoggingDetailsOutputTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsUnionTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsUnionTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsUnionTypeDef",
    "AwsElbLoadBalancerPoliciesOutputTypeDef",
    "AwsElbLoadBalancerPoliciesTypeDef",
    "AwsElbLoadBalancerAttributesOutputTypeDef",
    "AwsElbLoadBalancerAttributesTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionUnionTypeDef",
    "AwsElbLoadBalancerListenerDescriptionOutputTypeDef",
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    "AwsElbv2LoadBalancerDetailsOutputTypeDef",
    "AwsElbv2LoadBalancerDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef",
    "AwsIamAccessKeySessionContextTypeDef",
    "AwsIamGroupDetailsOutputTypeDef",
    "AwsIamGroupDetailsTypeDef",
    "AwsIamInstanceProfileOutputTypeDef",
    "AwsIamInstanceProfileTypeDef",
    "AwsIamPolicyDetailsOutputTypeDef",
    "AwsIamPolicyDetailsTypeDef",
    "AwsIamUserDetailsOutputTypeDef",
    "AwsIamUserDetailsTypeDef",
    "AwsKinesisStreamDetailsTypeDef",
    "AwsLambdaFunctionEnvironmentOutputTypeDef",
    "AwsLambdaFunctionEnvironmentTypeDef",
    "AwsLambdaFunctionVpcConfigUnionTypeDef",
    "AwsLambdaLayerVersionDetailsUnionTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnionTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef",
    "AwsNetworkFirewallFirewallDetailsOutputTypeDef",
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsUnionTypeDef",
    "AwsRdsDbClusterDetailsOutputTypeDef",
    "AwsRdsDbClusterDetailsTypeDef",
    "AwsRdsDbClusterSnapshotDetailsOutputTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnionTypeDef",
    "AwsRdsDbSnapshotDetailsOutputTypeDef",
    "AwsRdsDbSnapshotDetailsTypeDef",
    "AwsRdsDbPendingModifiedValuesOutputTypeDef",
    "AwsRdsDbSecurityGroupDetailsOutputTypeDef",
    "AwsRdsDbSecurityGroupDetailsTypeDef",
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    "AwsRdsEventSubscriptionDetailsUnionTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsUnionTypeDef",
    "AwsRedshiftClusterClusterParameterGroupOutputTypeDef",
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    "AwsRoute53HostedZoneObjectDetailsTypeDef",
    "AwsRoute53QueryLoggingConfigDetailsTypeDef",
    "AwsS3AccessPointDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef",
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    "AwsSageMakerNotebookInstanceDetailsOutputTypeDef",
    "AwsSageMakerNotebookInstanceDetailsTypeDef",
    "AwsSecretsManagerSecretDetailsTypeDef",
    "BatchUpdateFindingsRequestRequestTypeDef",
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    "AwsSnsTopicDetailsOutputTypeDef",
    "AwsSnsTopicDetailsTypeDef",
    "AwsSsmPatchTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef",
    "AwsWafRateBasedRuleDetailsOutputTypeDef",
    "AwsWafRateBasedRuleDetailsTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsOutputTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    "AwsWafRegionalRuleDetailsOutputTypeDef",
    "AwsWafRegionalRuleDetailsTypeDef",
    "AwsWafRegionalRuleGroupRulesDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListDetailsTypeDef",
    "AwsWafRuleDetailsOutputTypeDef",
    "AwsWafRuleDetailsTypeDef",
    "AwsWafRuleGroupRulesDetailsTypeDef",
    "AwsWafWebAclRuleOutputTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsOutputTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsTypeDef",
    "AwsWafv2CustomResponseDetailsOutputTypeDef",
    "AwsWafv2CustomResponseDetailsTypeDef",
    "AwsWafv2WebAclCaptchaConfigDetailsTypeDef",
    "CreateActionTargetResponseTypeDef",
    "CreateAutomationRuleResponseTypeDef",
    "CreateFindingAggregatorResponseTypeDef",
    "CreateInsightResponseTypeDef",
    "DeleteActionTargetResponseTypeDef",
    "DeleteInsightResponseTypeDef",
    "DescribeActionTargetsResponseTypeDef",
    "DescribeHubResponseTypeDef",
    "EnableImportFindingsForProductResponseTypeDef",
    "GetConfigurationPolicyAssociationResponseTypeDef",
    "GetFindingAggregatorResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "ListAutomationRulesResponseTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartConfigurationPolicyAssociationResponseTypeDef",
    "UpdateFindingAggregatorResponseTypeDef",
    "BatchDeleteAutomationRulesResponseTypeDef",
    "BatchUpdateAutomationRulesResponseTypeDef",
    "BatchEnableStandardsRequestRequestTypeDef",
    "ListConfigurationPolicyAssociationsResponseTypeDef",
    "BatchGetStandardsControlAssociationsRequestRequestTypeDef",
    "UnprocessedStandardsControlAssociationTypeDef",
    "BatchImportFindingsResponseTypeDef",
    "BatchUpdateStandardsControlAssociationsRequestRequestTypeDef",
    "UnprocessedStandardsControlAssociationUpdateTypeDef",
    "VulnerabilityCodeVulnerabilitiesOutputTypeDef",
    "VulnerabilityCodeVulnerabilitiesTypeDef",
    "ComplianceOutputTypeDef",
    "ConfigurationOptionsTypeDef",
    "ConfigurationPolicyAssociationTypeDef",
    "GetConfigurationPolicyAssociationRequestRequestTypeDef",
    "StartConfigurationPolicyAssociationRequestRequestTypeDef",
    "StartConfigurationPolicyDisassociationRequestRequestTypeDef",
    "ListConfigurationPoliciesResponseTypeDef",
    "ContainerDetailsOutputTypeDef",
    "ContainerDetailsTypeDef",
    "CreateMembersResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "InviteMembersResponseTypeDef",
    "DateFilterTypeDef",
    "DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef",
    "DescribeProductsRequestDescribeProductsPaginateTypeDef",
    "DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef",
    "DescribeStandardsRequestDescribeStandardsPaginateTypeDef",
    "GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef",
    "GetInsightsRequestGetInsightsPaginateTypeDef",
    "ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef",
    "ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef",
    "ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef",
    "ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef",
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    "ListMembersRequestListMembersPaginateTypeDef",
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    "ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef",
    "ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "DescribeProductsResponseTypeDef",
    "DescribeStandardsControlsResponseTypeDef",
    "ThreatOutputTypeDef",
    "ThreatTypeDef",
    "ListFindingAggregatorsResponseTypeDef",
    "FindingHistoryRecordTypeDef",
    "FindingProviderFieldsOutputTypeDef",
    "FindingProviderFieldsTypeDef",
    "GeneratorDetailsUnionTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef",
    "GetFindingHistoryRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "ListMembersResponseTypeDef",
    "InsightResultsTypeDef",
    "ListStandardsControlAssociationsResponseTypeDef",
    "NetworkPathComponentDetailsOutputTypeDef",
    "NetworkPathComponentDetailsTypeDef",
    "NetworkTypeDef",
    "PageTypeDef",
    "ParameterConfigurationOutputTypeDef",
    "ParameterValueUnionTypeDef",
    "RemediationTypeDef",
    "RuleGroupSourceListDetailsUnionTypeDef",
    "RuleGroupSourceStatefulRulesDetailsOutputTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsUnionTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnionTypeDef",
    "RuleGroupVariablesIpSetsDetailsUnionTypeDef",
    "RuleGroupVariablesOutputTypeDef",
    "RuleGroupVariablesPortSetsDetailsUnionTypeDef",
    "SecurityControlParameterUnionTypeDef",
    "StandardTypeDef",
    "StandardsSubscriptionTypeDef",
    "StatelessCustomPublishMetricActionOutputTypeDef",
    "StatelessCustomPublishMetricActionTypeDef",
    "AwsApiCallActionOutputTypeDef",
    "AwsApiCallActionTypeDef",
    "NetworkConnectionActionTypeDef",
    "PortProbeDetailTypeDef",
    "CvssUnionTypeDef",
    "AwsEc2RouteTableDetailsOutputTypeDef",
    "AwsEc2RouteTableDetailsTypeDef",
    "AutomationRulesActionOutputTypeDef",
    "AutomationRulesFindingFieldsUpdateUnionTypeDef",
    "AwsAmazonMqBrokerDetailsOutputTypeDef",
    "AwsAmazonMqBrokerDetailsTypeDef",
    "AwsApiGatewayStageDetailsTypeDef",
    "AwsApiGatewayRestApiDetailsTypeDef",
    "AwsApiGatewayV2StageDetailsUnionTypeDef",
    "AwsAppSyncGraphQlApiDetailsOutputTypeDef",
    "AwsAppSyncGraphQlApiDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnionTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    "AwsBackupBackupPlanRuleDetailsOutputTypeDef",
    "AwsBackupBackupPlanRuleDetailsTypeDef",
    "AwsBackupBackupVaultDetailsTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionUnionTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    "AwsCloudFormationStackDetailsUnionTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsUnionTypeDef",
    "AwsCloudFrontDistributionOriginItemOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef",
    "AwsCloudWatchAlarmDetailsUnionTypeDef",
    "AwsCodeBuildProjectEnvironmentUnionTypeDef",
    "AwsCodeBuildProjectDetailsOutputTypeDef",
    "AwsApiGatewayV2ApiDetailsTypeDef",
    "AwsDmsReplicationInstanceDetailsUnionTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    "AwsDynamoDbTableReplicaOutputTypeDef",
    "AwsDynamoDbTableReplicaTypeDef",
    "AwsEc2ClientVpnEndpointDetailsOutputTypeDef",
    "AwsEc2ClientVpnEndpointDetailsTypeDef",
    "AwsEc2InstanceDetailsUnionTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnionTypeDef",
    "AwsEc2LaunchTemplateDataDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnionTypeDef",
    "AwsEc2NetworkAclDetailsOutputTypeDef",
    "AwsEc2NetworkAclDetailsTypeDef",
    "AwsEc2NetworkInterfaceDetailsUnionTypeDef",
    "AwsEc2SecurityGroupDetailsOutputTypeDef",
    "AwsEc2SecurityGroupIpPermissionUnionTypeDef",
    "AwsEc2SubnetDetailsUnionTypeDef",
    "AwsEc2VolumeDetailsUnionTypeDef",
    "AwsEc2VpcDetailsUnionTypeDef",
    "AwsEc2VpcEndpointServiceDetailsUnionTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsOutputTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsUnionTypeDef",
    "AwsEc2VpnConnectionDetailsOutputTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    "AwsEcsClusterConfigurationDetailsTypeDef",
    "AwsEcsContainerDetailsUnionTypeDef",
    "AwsEcsServiceDetailsOutputTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    "AwsEcsTaskDetailsOutputTypeDef",
    "AwsEfsAccessPointDetailsOutputTypeDef",
    "AwsEfsAccessPointDetailsTypeDef",
    "AwsEksClusterDetailsOutputTypeDef",
    "AwsEksClusterLoggingDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsUnionTypeDef",
    "AwsElasticsearchDomainDetailsOutputTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AwsElbLoadBalancerPoliciesUnionTypeDef",
    "AwsElbLoadBalancerAttributesUnionTypeDef",
    "AwsElbLoadBalancerDetailsOutputTypeDef",
    "AwsElbLoadBalancerListenerDescriptionUnionTypeDef",
    "AwsElbv2LoadBalancerDetailsUnionTypeDef",
    "AwsEventsEndpointRoutingConfigDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef",
    "AwsIamAccessKeyDetailsTypeDef",
    "AwsIamGroupDetailsUnionTypeDef",
    "AwsIamRoleDetailsOutputTypeDef",
    "AwsIamInstanceProfileUnionTypeDef",
    "AwsIamPolicyDetailsUnionTypeDef",
    "AwsIamUserDetailsUnionTypeDef",
    "AwsLambdaFunctionDetailsOutputTypeDef",
    "AwsLambdaFunctionEnvironmentUnionTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef",
    "AwsNetworkFirewallFirewallDetailsUnionTypeDef",
    "AwsOpenSearchServiceDomainDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    "AwsRdsDbClusterDetailsUnionTypeDef",
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    "AwsRdsDbSnapshotDetailsUnionTypeDef",
    "AwsRdsDbSecurityGroupDetailsUnionTypeDef",
    "AwsRdsDbSubnetGroupOutputTypeDef",
    "AwsRdsDbSubnetGroupTypeDef",
    "AwsRdsDbPendingModifiedValuesTypeDef",
    "AwsRedshiftClusterDetailsOutputTypeDef",
    "AwsRedshiftClusterClusterParameterGroupUnionTypeDef",
    "AwsRoute53HostedZoneDetailsOutputTypeDef",
    "AwsRoute53HostedZoneDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationFilterOutputTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterUnionTypeDef",
    "AwsS3BucketObjectLockConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    "AwsS3BucketWebsiteConfigurationOutputTypeDef",
    "AwsS3BucketWebsiteConfigurationTypeDef",
    "AwsSageMakerNotebookInstanceDetailsUnionTypeDef",
    "BatchUpdateFindingsResponseTypeDef",
    "AwsSnsTopicDetailsUnionTypeDef",
    "AwsSsmPatchComplianceDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef",
    "AwsWafRateBasedRuleDetailsUnionTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsUnionTypeDef",
    "AwsWafRegionalRuleDetailsUnionTypeDef",
    "AwsWafRegionalRuleGroupDetailsOutputTypeDef",
    "AwsWafRegionalRuleGroupDetailsTypeDef",
    "AwsWafRegionalWebAclDetailsOutputTypeDef",
    "AwsWafRegionalWebAclDetailsTypeDef",
    "AwsWafRuleDetailsUnionTypeDef",
    "AwsWafRuleGroupDetailsOutputTypeDef",
    "AwsWafRuleGroupDetailsTypeDef",
    "AwsWafWebAclDetailsOutputTypeDef",
    "AwsWafWebAclRuleUnionTypeDef",
    "AwsWafv2ActionAllowDetailsOutputTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsOutputTypeDef",
    "AwsWafv2RulesActionCountDetailsOutputTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsUnionTypeDef",
    "AwsWafv2ActionBlockDetailsOutputTypeDef",
    "AwsWafv2CustomResponseDetailsUnionTypeDef",
    "BatchGetStandardsControlAssociationsResponseTypeDef",
    "BatchUpdateStandardsControlAssociationsResponseTypeDef",
    "VulnerabilityOutputTypeDef",
    "VulnerabilityCodeVulnerabilitiesUnionTypeDef",
    "ParameterDefinitionTypeDef",
    "BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef",
    "UnprocessedConfigurationPolicyAssociationTypeDef",
    "ContainerDetailsUnionTypeDef",
    "AutomationRulesFindingFiltersOutputTypeDef",
    "AutomationRulesFindingFiltersTypeDef",
    "AwsSecurityFindingFiltersOutputTypeDef",
    "AwsSecurityFindingFiltersTypeDef",
    "ThreatUnionTypeDef",
    "GetFindingHistoryResponseTypeDef",
    "FindingProviderFieldsUnionTypeDef",
    "GetInsightResultsResponseTypeDef",
    "NetworkHeaderOutputTypeDef",
    "NetworkPathComponentDetailsUnionTypeDef",
    "OccurrencesOutputTypeDef",
    "OccurrencesTypeDef",
    "SecurityControlCustomParameterOutputTypeDef",
    "SecurityControlTypeDef",
    "ParameterConfigurationTypeDef",
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    "RuleGroupVariablesTypeDef",
    "ComplianceTypeDef",
    "DescribeStandardsResponseTypeDef",
    "BatchDisableStandardsResponseTypeDef",
    "BatchEnableStandardsResponseTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "StatelessCustomActionDefinitionOutputTypeDef",
    "StatelessCustomPublishMetricActionUnionTypeDef",
    "AwsApiCallActionUnionTypeDef",
    "PortProbeActionOutputTypeDef",
    "PortProbeActionTypeDef",
    "AwsEc2RouteTableDetailsUnionTypeDef",
    "AutomationRulesActionTypeDef",
    "AwsAmazonMqBrokerDetailsUnionTypeDef",
    "AwsApiGatewayStageDetailsUnionTypeDef",
    "AwsApiGatewayRestApiDetailsUnionTypeDef",
    "AwsAppSyncGraphQlApiDetailsUnionTypeDef",
    "AwsAthenaWorkGroupDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsUnionTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef",
    "AwsBackupBackupPlanRuleDetailsUnionTypeDef",
    "AwsBackupBackupVaultDetailsUnionTypeDef",
    "AwsCertificateManagerCertificateDetailsOutputTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryUnionTypeDef",
    "AwsCloudFrontDistributionOriginsOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupsOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverUnionTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigUnionTypeDef",
    "AwsCodeBuildProjectDetailsTypeDef",
    "AwsApiGatewayV2ApiDetailsUnionTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexUnionTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexUnionTypeDef",
    "AwsDynamoDbTableDetailsOutputTypeDef",
    "AwsDynamoDbTableReplicaUnionTypeDef",
    "AwsEc2ClientVpnEndpointDetailsUnionTypeDef",
    "AwsEc2LaunchTemplateDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataDetailsTypeDef",
    "AwsEc2NetworkAclDetailsUnionTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsUnionTypeDef",
    "AwsEcsClusterDetailsOutputTypeDef",
    "AwsEcsClusterDetailsTypeDef",
    "AwsEcsTaskDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsUnionTypeDef",
    "AwsEfsAccessPointDetailsUnionTypeDef",
    "AwsEksClusterLoggingDetailsUnionTypeDef",
    "AwsElasticsearchDomainDetailsUnionTypeDef",
    "AwsElbLoadBalancerDetailsTypeDef",
    "AwsEventsEndpointDetailsOutputTypeDef",
    "AwsEventsEndpointDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesDetailsTypeDef",
    "AwsIamRoleDetailsTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "AwsMskClusterClusterInfoDetailsOutputTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationDetailsUnionTypeDef",
    "AwsOpenSearchServiceDomainDetailsUnionTypeDef",
    "AwsRdsDbClusterSnapshotDetailsUnionTypeDef",
    "AwsRdsDbInstanceDetailsOutputTypeDef",
    "AwsRdsDbSubnetGroupUnionTypeDef",
    "AwsRdsDbPendingModifiedValuesUnionTypeDef",
    "AwsRedshiftClusterDetailsTypeDef",
    "AwsRoute53HostedZoneDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnionTypeDef",
    "AwsS3BucketNotificationConfigurationDetailOutputTypeDef",
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationUnionTypeDef",
    "AwsS3BucketWebsiteConfigurationUnionTypeDef",
    "AwsStepFunctionStateMachineDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsUnionTypeDef",
    "AwsWafRegionalRuleGroupDetailsUnionTypeDef",
    "AwsWafRegionalWebAclDetailsUnionTypeDef",
    "AwsWafRuleGroupDetailsUnionTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "AwsWafv2ActionAllowDetailsTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsTypeDef",
    "AwsWafv2RulesActionCountDetailsTypeDef",
    "AwsWafv2RulesActionDetailsOutputTypeDef",
    "AwsWafv2WebAclActionDetailsOutputTypeDef",
    "AwsWafv2ActionBlockDetailsTypeDef",
    "VulnerabilityTypeDef",
    "SecurityControlDefinitionTypeDef",
    "BatchGetConfigurationPolicyAssociationsResponseTypeDef",
    "AutomationRulesConfigTypeDef",
    "AutomationRulesFindingFiltersUnionTypeDef",
    "InsightTypeDef",
    "CreateInsightRequestRequestTypeDef",
    "GetFindingsRequestGetFindingsPaginateTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "UpdateInsightRequestRequestTypeDef",
    "NetworkPathComponentOutputTypeDef",
    "NetworkHeaderTypeDef",
    "CustomDataIdentifiersDetectionsOutputTypeDef",
    "SensitiveDataDetectionsOutputTypeDef",
    "OccurrencesUnionTypeDef",
    "SecurityControlsConfigurationOutputTypeDef",
    "BatchGetSecurityControlsResponseTypeDef",
    "ParameterConfigurationUnionTypeDef",
    "RuleGroupSourceStatefulRulesDetailsUnionTypeDef",
    "RuleGroupSourceStatelessRulesDetailsOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesUnionTypeDef",
    "RuleGroupVariablesUnionTypeDef",
    "ComplianceUnionTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef",
    "RuleGroupSourceCustomActionsDetailsOutputTypeDef",
    "StatelessCustomActionDefinitionTypeDef",
    "ActionOutputTypeDef",
    "PortProbeActionUnionTypeDef",
    "AutomationRulesActionUnionTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnionTypeDef",
    "AwsBackupBackupPlanDetailsOutputTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsTypeDef",
    "AwsCertificateManagerCertificateDetailsTypeDef",
    "AwsCloudFrontDistributionDetailsOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    "AwsCloudFrontDistributionOriginItemTypeDef",
    "AwsCodeBuildProjectDetailsUnionTypeDef",
    "AwsDynamoDbTableDetailsTypeDef",
    "AwsEc2LaunchTemplateDataDetailsUnionTypeDef",
    "AwsEc2SecurityGroupDetailsUnionTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsUnionTypeDef",
    "AwsEc2VpnConnectionDetailsTypeDef",
    "AwsEcsClusterDetailsUnionTypeDef",
    "AwsEcsTaskDetailsUnionTypeDef",
    "AwsEcsServiceDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    "AwsEksClusterDetailsTypeDef",
    "AwsElbLoadBalancerDetailsUnionTypeDef",
    "AwsEventsEndpointDetailsUnionTypeDef",
    "AwsGuardDutyDetectorDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDetailsTypeDef",
    "AwsIamRoleDetailsUnionTypeDef",
    "AwsLambdaFunctionDetailsUnionTypeDef",
    "AwsMskClusterDetailsOutputTypeDef",
    "AwsMskClusterClusterInfoDetailsTypeDef",
    "AwsRdsDbInstanceDetailsTypeDef",
    "AwsRedshiftClusterDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationOutputTypeDef",
    "AwsS3BucketNotificationConfigurationFilterUnionTypeDef",
    "AwsStepFunctionStateMachineDetailsTypeDef",
    "AwsWafWebAclDetailsUnionTypeDef",
    "AwsWafv2ActionAllowDetailsUnionTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsUnionTypeDef",
    "AwsWafv2RulesActionCountDetailsUnionTypeDef",
    "AwsWafv2RulesDetailsOutputTypeDef",
    "AwsWafv2ActionBlockDetailsUnionTypeDef",
    "VulnerabilityUnionTypeDef",
    "GetSecurityControlDefinitionResponseTypeDef",
    "ListSecurityControlDefinitionsResponseTypeDef",
    "BatchGetAutomationRulesResponseTypeDef",
    "GetInsightsResponseTypeDef",
    "NetworkHeaderUnionTypeDef",
    "CustomDataIdentifiersResultOutputTypeDef",
    "SensitiveDataResultOutputTypeDef",
    "CustomDataIdentifiersDetectionsTypeDef",
    "SensitiveDataDetectionsTypeDef",
    "SecurityHubPolicyOutputTypeDef",
    "SecurityControlCustomParameterTypeDef",
    "UpdateSecurityControlRequestRequestTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    "FirewallPolicyDetailsOutputTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef",
    "StatelessCustomActionDefinitionUnionTypeDef",
    "ActionTypeDef",
    "CreateAutomationRuleRequestRequestTypeDef",
    "UpdateAutomationRulesRequestItemTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsUnionTypeDef",
    "AwsCertificateManagerCertificateDetailsUnionTypeDef",
    "AwsCloudFrontDistributionOriginGroupUnionTypeDef",
    "AwsCloudFrontDistributionOriginItemUnionTypeDef",
    "AwsDynamoDbTableDetailsUnionTypeDef",
    "AwsEc2LaunchTemplateDetailsTypeDef",
    "AwsEc2VpnConnectionDetailsUnionTypeDef",
    "AwsEcsServiceDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsUnionTypeDef",
    "AwsEksClusterDetailsUnionTypeDef",
    "AwsGuardDutyDetectorDetailsUnionTypeDef",
    "AwsMskClusterClusterInfoDetailsUnionTypeDef",
    "AwsRdsDbInstanceDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnionTypeDef",
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    "AwsStepFunctionStateMachineDetailsUnionTypeDef",
    "AwsWafv2RuleGroupDetailsOutputTypeDef",
    "AwsWafv2WebAclDetailsOutputTypeDef",
    "AwsWafv2RulesActionDetailsTypeDef",
    "AwsWafv2WebAclActionDetailsTypeDef",
    "NetworkPathComponentTypeDef",
    "ClassificationResultOutputTypeDef",
    "CustomDataIdentifiersDetectionsUnionTypeDef",
    "SensitiveDataDetectionsUnionTypeDef",
    "PolicyOutputTypeDef",
    "SecurityControlCustomParameterUnionTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionUnionTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef",
    "RuleGroupSourceOutputTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    "ActionUnionTypeDef",
    "BatchUpdateAutomationRulesRequestRequestTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsUnionTypeDef",
    "AwsBackupBackupPlanDetailsTypeDef",
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    "AwsCloudFrontDistributionOriginsTypeDef",
    "AwsEc2LaunchTemplateDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionDetailsTypeDef",
    "AwsMskClusterDetailsTypeDef",
    "AwsS3BucketDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationDetailUnionTypeDef",
    "AwsWafv2RulesActionDetailsUnionTypeDef",
    "AwsWafv2WebAclActionDetailsUnionTypeDef",
    "NetworkPathComponentUnionTypeDef",
    "DataClassificationDetailsOutputTypeDef",
    "CustomDataIdentifiersResultTypeDef",
    "SensitiveDataResultTypeDef",
    "CreateConfigurationPolicyResponseTypeDef",
    "GetConfigurationPolicyResponseTypeDef",
    "UpdateConfigurationPolicyResponseTypeDef",
    "SecurityControlsConfigurationTypeDef",
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    "RuleGroupDetailsOutputTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsUnionTypeDef",
    "RuleGroupSourceCustomActionsDetailsUnionTypeDef",
    "AwsBackupBackupPlanDetailsUnionTypeDef",
    "AwsCloudFrontDistributionOriginGroupsUnionTypeDef",
    "AwsCloudFrontDistributionOriginsUnionTypeDef",
    "AwsEcsTaskDefinitionDetailsUnionTypeDef",
    "AwsMskClusterDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnionTypeDef",
    "AwsS3BucketNotificationConfigurationTypeDef",
    "AwsWafv2RulesDetailsTypeDef",
    "CustomDataIdentifiersResultUnionTypeDef",
    "SensitiveDataResultUnionTypeDef",
    "SecurityControlsConfigurationUnionTypeDef",
    "RuleGroupSourceStatelessRulesDetailsUnionTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsOutputTypeDef",
    "FirewallPolicyDetailsTypeDef",
    "AwsCloudFrontDistributionDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationUnionTypeDef",
    "AwsWafv2RuleGroupDetailsTypeDef",
    "AwsWafv2RulesDetailsUnionTypeDef",
    "ClassificationResultTypeDef",
    "SecurityHubPolicyTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    "ResourceDetailsOutputTypeDef",
    "FirewallPolicyDetailsUnionTypeDef",
    "AwsCloudFrontDistributionDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsUnionTypeDef",
    "AwsWafv2RuleGroupDetailsUnionTypeDef",
    "AwsWafv2WebAclDetailsTypeDef",
    "ClassificationResultUnionTypeDef",
    "SecurityHubPolicyUnionTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnionTypeDef",
    "ResourceOutputTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    "AwsS3BucketDetailsTypeDef",
    "AwsWafv2WebAclDetailsUnionTypeDef",
    "DataClassificationDetailsTypeDef",
    "PolicyTypeDef",
    "RuleGroupSourceTypeDef",
    "AwsSecurityFindingOutputTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsUnionTypeDef",
    "AwsS3BucketDetailsUnionTypeDef",
    "DataClassificationDetailsUnionTypeDef",
    "CreateConfigurationPolicyRequestRequestTypeDef",
    "UpdateConfigurationPolicyRequestRequestTypeDef",
    "RuleGroupSourceUnionTypeDef",
    "GetFindingsResponseTypeDef",
    "RuleGroupDetailsTypeDef",
    "RuleGroupDetailsUnionTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsUnionTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceDetailsUnionTypeDef",
    "ResourceTypeDef",
    "ResourceUnionTypeDef",
    "AwsSecurityFindingTypeDef",
    "AwsSecurityFindingUnionTypeDef",
    "BatchImportFindingsRequestRequestTypeDef",
)

AcceptAdministratorInvitationRequestRequestTypeDef = TypedDict(
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    {
        "AdministratorId": str,
        "InvitationId": str,
    },
)
AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "MasterId": str,
        "InvitationId": str,
    },
)
AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "AccountId": str,
        "Email": NotRequired[str],
    },
)
ActionLocalIpDetailsTypeDef = TypedDict(
    "ActionLocalIpDetailsTypeDef",
    {
        "IpAddressV4": NotRequired[str],
    },
)
ActionLocalPortDetailsTypeDef = TypedDict(
    "ActionLocalPortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)
DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": NotRequired[str],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
    },
)
CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": NotRequired[str],
    },
)
CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": NotRequired[str],
        "CountryName": NotRequired[str],
    },
)
GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lon": NotRequired[float],
        "Lat": NotRequired[float],
    },
)
IpOrganizationDetailsTypeDef = TypedDict(
    "IpOrganizationDetailsTypeDef",
    {
        "Asn": NotRequired[int],
        "AsnOrg": NotRequired[str],
        "Isp": NotRequired[str],
        "Org": NotRequired[str],
    },
)
ActionRemotePortDetailsTypeDef = TypedDict(
    "ActionRemotePortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)
ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ActionTargetArn": str,
        "Name": str,
        "Description": str,
    },
)
AdjustmentTypeDef = TypedDict(
    "AdjustmentTypeDef",
    {
        "Metric": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AccountId": NotRequired[str],
        "Status": NotRequired[AdminStatusType],
    },
)
AssociatedStandardTypeDef = TypedDict(
    "AssociatedStandardTypeDef",
    {
        "StandardsId": NotRequired[str],
    },
)
AssociationFiltersTypeDef = TypedDict(
    "AssociationFiltersTypeDef",
    {
        "ConfigurationPolicyId": NotRequired[str],
        "AssociationType": NotRequired[AssociationTypeType],
        "AssociationStatus": NotRequired[ConfigurationPolicyAssociationStatusType],
    },
)
AssociationStateDetailsTypeDef = TypedDict(
    "AssociationStateDetailsTypeDef",
    {
        "State": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)
NoteUpdateTypeDef = TypedDict(
    "NoteUpdateTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
    },
)
RelatedFindingTypeDef = TypedDict(
    "RelatedFindingTypeDef",
    {
        "ProductArn": str,
        "Id": str,
    },
)
SeverityUpdateTypeDef = TypedDict(
    "SeverityUpdateTypeDef",
    {
        "Normalized": NotRequired[int],
        "Product": NotRequired[float],
        "Label": NotRequired[SeverityLabelType],
    },
)
WorkflowUpdateTypeDef = TypedDict(
    "WorkflowUpdateTypeDef",
    {
        "Status": NotRequired[WorkflowStatusType],
    },
)
MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Comparison": NotRequired[MapFilterComparisonType],
    },
)
NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef",
    {
        "Gte": NotRequired[float],
        "Lte": NotRequired[float],
        "Eq": NotRequired[float],
        "Gt": NotRequired[float],
        "Lt": NotRequired[float],
    },
)
StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "Value": NotRequired[str],
        "Comparison": NotRequired[StringFilterComparisonType],
    },
)
AutomationRulesMetadataTypeDef = TypedDict(
    "AutomationRulesMetadataTypeDef",
    {
        "RuleArn": NotRequired[str],
        "RuleStatus": NotRequired[RuleStatusType],
        "RuleOrder": NotRequired[int],
        "RuleName": NotRequired[str],
        "Description": NotRequired[str],
        "IsTerminal": NotRequired[bool],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)
AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef",
    {
        "KmsKeyId": NotRequired[str],
        "UseAwsOwnedKey": NotRequired[bool],
    },
)
AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef",
    {
        "Hosts": NotRequired[List[str]],
        "RoleBase": NotRequired[str],
        "RoleName": NotRequired[str],
        "RoleSearchMatching": NotRequired[str],
        "RoleSearchSubtree": NotRequired[bool],
        "ServiceAccountUsername": NotRequired[str],
        "UserBase": NotRequired[str],
        "UserRoleName": NotRequired[str],
        "UserSearchMatching": NotRequired[str],
        "UserSearchSubtree": NotRequired[bool],
    },
)
AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef",
    {
        "DayOfWeek": NotRequired[str],
        "TimeOfDay": NotRequired[str],
        "TimeZone": NotRequired[str],
    },
)
AwsAmazonMqBrokerUsersDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerUsersDetailsTypeDef",
    {
        "PendingChange": NotRequired[str],
        "Username": NotRequired[str],
    },
)
AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef",
    {
        "Hosts": NotRequired[Sequence[str]],
        "RoleBase": NotRequired[str],
        "RoleName": NotRequired[str],
        "RoleSearchMatching": NotRequired[str],
        "RoleSearchSubtree": NotRequired[bool],
        "ServiceAccountUsername": NotRequired[str],
        "UserBase": NotRequired[str],
        "UserRoleName": NotRequired[str],
        "UserSearchMatching": NotRequired[str],
        "UserSearchSubtree": NotRequired[bool],
    },
)
AwsAmazonMqBrokerLogsPendingDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLogsPendingDetailsTypeDef",
    {
        "Audit": NotRequired[bool],
        "General": NotRequired[bool],
    },
)
AwsApiCallActionDomainDetailsTypeDef = TypedDict(
    "AwsApiCallActionDomainDetailsTypeDef",
    {
        "Domain": NotRequired[str],
    },
)
AwsApiGatewayAccessLogSettingsTypeDef = TypedDict(
    "AwsApiGatewayAccessLogSettingsTypeDef",
    {
        "Format": NotRequired[str],
        "DestinationArn": NotRequired[str],
    },
)
AwsApiGatewayCanarySettingsOutputTypeDef = TypedDict(
    "AwsApiGatewayCanarySettingsOutputTypeDef",
    {
        "PercentTraffic": NotRequired[float],
        "DeploymentId": NotRequired[str],
        "StageVariableOverrides": NotRequired[Dict[str, str]],
        "UseStageCache": NotRequired[bool],
    },
)
AwsApiGatewayCanarySettingsTypeDef = TypedDict(
    "AwsApiGatewayCanarySettingsTypeDef",
    {
        "PercentTraffic": NotRequired[float],
        "DeploymentId": NotRequired[str],
        "StageVariableOverrides": NotRequired[Mapping[str, str]],
        "UseStageCache": NotRequired[bool],
    },
)
AwsApiGatewayEndpointConfigurationOutputTypeDef = TypedDict(
    "AwsApiGatewayEndpointConfigurationOutputTypeDef",
    {
        "Types": NotRequired[List[str]],
    },
)
AwsApiGatewayEndpointConfigurationTypeDef = TypedDict(
    "AwsApiGatewayEndpointConfigurationTypeDef",
    {
        "Types": NotRequired[Sequence[str]],
    },
)
AwsApiGatewayMethodSettingsTypeDef = TypedDict(
    "AwsApiGatewayMethodSettingsTypeDef",
    {
        "MetricsEnabled": NotRequired[bool],
        "LoggingLevel": NotRequired[str],
        "DataTraceEnabled": NotRequired[bool],
        "ThrottlingBurstLimit": NotRequired[int],
        "ThrottlingRateLimit": NotRequired[float],
        "CachingEnabled": NotRequired[bool],
        "CacheTtlInSeconds": NotRequired[int],
        "CacheDataEncrypted": NotRequired[bool],
        "RequireAuthorizationForCacheControl": NotRequired[bool],
        "UnauthorizedCacheControlHeaderStrategy": NotRequired[str],
        "HttpMethod": NotRequired[str],
        "ResourcePath": NotRequired[str],
    },
)
AwsCorsConfigurationOutputTypeDef = TypedDict(
    "AwsCorsConfigurationOutputTypeDef",
    {
        "AllowOrigins": NotRequired[List[str]],
        "AllowCredentials": NotRequired[bool],
        "ExposeHeaders": NotRequired[List[str]],
        "MaxAge": NotRequired[int],
        "AllowMethods": NotRequired[List[str]],
        "AllowHeaders": NotRequired[List[str]],
    },
)
AwsApiGatewayV2RouteSettingsTypeDef = TypedDict(
    "AwsApiGatewayV2RouteSettingsTypeDef",
    {
        "DetailedMetricsEnabled": NotRequired[bool],
        "LoggingLevel": NotRequired[str],
        "DataTraceEnabled": NotRequired[bool],
        "ThrottlingBurstLimit": NotRequired[int],
        "ThrottlingRateLimit": NotRequired[float],
    },
)
AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef",
    {
        "AuthorizerResultTtlInSeconds": NotRequired[int],
        "AuthorizerUri": NotRequired[str],
        "IdentityValidationExpression": NotRequired[str],
    },
)
AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef",
    {
        "AuthTtL": NotRequired[int],
        "ClientId": NotRequired[str],
        "IatTtL": NotRequired[int],
        "Issuer": NotRequired[str],
    },
)
AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef",
    {
        "AppIdClientRegex": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "DefaultAction": NotRequired[str],
        "UserPoolId": NotRequired[str],
    },
)
AwsAppSyncGraphQlApiLogConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiLogConfigDetailsTypeDef",
    {
        "CloudWatchLogsRoleArn": NotRequired[str],
        "ExcludeVerboseContent": NotRequired[bool],
        "FieldLogLevel": NotRequired[str],
    },
)
AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef",
    {
        "EncryptionOption": NotRequired[str],
        "KmsKey": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    {
        "Value": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    {
        "OnDemandAllocationStrategy": NotRequired[str],
        "OnDemandBaseCapacity": NotRequired[int],
        "OnDemandPercentageAboveBaseCapacity": NotRequired[int],
        "SpotAllocationStrategy": NotRequired[str],
        "SpotInstancePools": NotRequired[int],
        "SpotMaxPrice": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[str],
    },
)
AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
    },
)
AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpTokens": NotRequired[str],
    },
)
AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef",
    {
        "BackupOptions": NotRequired[Dict[str, str]],
        "ResourceType": NotRequired[str],
    },
)
AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef",
    {
        "BackupOptions": NotRequired[Mapping[str, str]],
        "ResourceType": NotRequired[str],
    },
)
AwsBackupBackupPlanLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanLifecycleDetailsTypeDef",
    {
        "DeleteAfterDays": NotRequired[int],
        "MoveToColdStorageAfterDays": NotRequired[int],
    },
)
AwsBackupBackupVaultNotificationsDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupVaultNotificationsDetailsOutputTypeDef",
    {
        "BackupVaultEvents": NotRequired[List[str]],
        "SnsTopicArn": NotRequired[str],
    },
)
AwsBackupBackupVaultNotificationsDetailsTypeDef = TypedDict(
    "AwsBackupBackupVaultNotificationsDetailsTypeDef",
    {
        "BackupVaultEvents": NotRequired[Sequence[str]],
        "SnsTopicArn": NotRequired[str],
    },
)
AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef",
    {
        "DeleteAt": NotRequired[str],
        "MoveToColdStorageAt": NotRequired[str],
    },
)
AwsBackupRecoveryPointCreatedByDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointCreatedByDetailsTypeDef",
    {
        "BackupPlanArn": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "BackupPlanVersion": NotRequired[str],
        "BackupRuleId": NotRequired[str],
    },
)
AwsBackupRecoveryPointLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointLifecycleDetailsTypeDef",
    {
        "DeleteAfterDays": NotRequired[int],
        "MoveToColdStorageAfterDays": NotRequired[int],
    },
)
AwsCertificateManagerCertificateExtendedKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    {
        "Name": NotRequired[str],
        "OId": NotRequired[str],
    },
)
AwsCertificateManagerCertificateKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    {
        "Name": NotRequired[str],
    },
)
AwsCertificateManagerCertificateOptionsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateOptionsTypeDef",
    {
        "CertificateTransparencyLoggingPreference": NotRequired[str],
    },
)
AwsCertificateManagerCertificateResourceRecordTypeDef = TypedDict(
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsCloudFormationStackDriftInformationDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackDriftInformationDetailsTypeDef",
    {
        "StackDriftStatus": NotRequired[str],
    },
)
AwsCloudFormationStackOutputsDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackOutputsDetailsTypeDef",
    {
        "Description": NotRequired[str],
        "OutputKey": NotRequired[str],
        "OutputValue": NotRequired[str],
    },
)
AwsCloudFrontDistributionCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": NotRequired[str],
    },
)
AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": NotRequired[str],
    },
)
AwsCloudFrontDistributionLoggingTypeDef = TypedDict(
    "AwsCloudFrontDistributionLoggingTypeDef",
    {
        "Bucket": NotRequired[str],
        "Enabled": NotRequired[bool],
        "IncludeCookies": NotRequired[bool],
        "Prefix": NotRequired[str],
    },
)
AwsCloudFrontDistributionViewerCertificateTypeDef = TypedDict(
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    {
        "AcmCertificateArn": NotRequired[str],
        "Certificate": NotRequired[str],
        "CertificateSource": NotRequired[str],
        "CloudFrontDefaultCertificate": NotRequired[bool],
        "IamCertificateId": NotRequired[str],
        "MinimumProtocolVersion": NotRequired[str],
        "SslSupportMethod": NotRequired[str],
    },
)
AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef",
    {
        "Items": NotRequired[List[str]],
        "Quantity": NotRequired[int],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef",
    {
        "Items": NotRequired[List[int]],
        "Quantity": NotRequired[int],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    {
        "Items": NotRequired[Sequence[int]],
        "Quantity": NotRequired[int],
    },
)
AwsCloudFrontDistributionOriginS3OriginConfigTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    {
        "OriginAccessIdentity": NotRequired[str],
    },
)
AwsCloudFrontDistributionOriginSslProtocolsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginSslProtocolsTypeDef",
    {
        "Items": NotRequired[Sequence[str]],
        "Quantity": NotRequired[int],
    },
)
AwsCloudTrailTrailDetailsTypeDef = TypedDict(
    "AwsCloudTrailTrailDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "HasCustomEventSelectors": NotRequired[bool],
        "HomeRegion": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "IsOrganizationTrail": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "LogFileValidationEnabled": NotRequired[bool],
        "Name": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "TrailArn": NotRequired[str],
    },
)
AwsCloudWatchAlarmDimensionsDetailsTypeDef = TypedDict(
    "AwsCloudWatchAlarmDimensionsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsCodeBuildProjectArtifactsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    {
        "ArtifactIdentifier": NotRequired[str],
        "EncryptionDisabled": NotRequired[bool],
        "Location": NotRequired[str],
        "Name": NotRequired[str],
        "NamespaceType": NotRequired[str],
        "OverrideArtifactName": NotRequired[bool],
        "Packaging": NotRequired[str],
        "Path": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsCodeBuildProjectSourceTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceTypeDef",
    {
        "Type": NotRequired[str],
        "Location": NotRequired[str],
        "GitCloneDepth": NotRequired[int],
        "InsecureSsl": NotRequired[bool],
    },
)
AwsCodeBuildProjectVpcConfigOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigOutputTypeDef",
    {
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
    },
)
AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    {
        "Credential": NotRequired[str],
        "CredentialProvider": NotRequired[str],
    },
)
AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    {
        "GroupName": NotRequired[str],
        "Status": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)
AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    {
        "EncryptionDisabled": NotRequired[bool],
        "Location": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigTypeDef",
    {
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)
AwsCorsConfigurationTypeDef = TypedDict(
    "AwsCorsConfigurationTypeDef",
    {
        "AllowOrigins": NotRequired[Sequence[str]],
        "AllowCredentials": NotRequired[bool],
        "ExposeHeaders": NotRequired[Sequence[str]],
        "MaxAge": NotRequired[int],
        "AllowMethods": NotRequired[Sequence[str]],
        "AllowHeaders": NotRequired[Sequence[str]],
    },
)
AwsDmsEndpointDetailsTypeDef = TypedDict(
    "AwsDmsEndpointDetailsTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "EndpointArn": NotRequired[str],
        "EndpointIdentifier": NotRequired[str],
        "EndpointType": NotRequired[str],
        "EngineName": NotRequired[str],
        "ExternalId": NotRequired[str],
        "ExtraConnectionAttributes": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "SslMode": NotRequired[str],
        "Username": NotRequired[str],
    },
)
AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef = TypedDict(
    "AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": NotRequired[str],
    },
)
AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef = TypedDict(
    "AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
    },
)
AwsDmsReplicationTaskDetailsTypeDef = TypedDict(
    "AwsDmsReplicationTaskDetailsTypeDef",
    {
        "CdcStartPosition": NotRequired[str],
        "CdcStartTime": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "MigrationType": NotRequired[str],
        "Id": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "ReplicationTaskIdentifier": NotRequired[str],
        "ReplicationTaskSettings": NotRequired[str],
        "SourceEndpointArn": NotRequired[str],
        "TableMappings": NotRequired[str],
        "TargetEndpointArn": NotRequired[str],
        "TaskData": NotRequired[str],
    },
)
AwsDynamoDbTableAttributeDefinitionTypeDef = TypedDict(
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeType": NotRequired[str],
    },
)
AwsDynamoDbTableBillingModeSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    {
        "BillingMode": NotRequired[str],
        "LastUpdateToPayPerRequestDateTime": NotRequired[str],
    },
)
AwsDynamoDbTableKeySchemaTypeDef = TypedDict(
    "AwsDynamoDbTableKeySchemaTypeDef",
    {
        "AttributeName": NotRequired[str],
        "KeyType": NotRequired[str],
    },
)
AwsDynamoDbTableProvisionedThroughputTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    {
        "LastDecreaseDateTime": NotRequired[str],
        "LastIncreaseDateTime": NotRequired[str],
        "NumberOfDecreasesToday": NotRequired[int],
        "ReadCapacityUnits": NotRequired[int],
        "WriteCapacityUnits": NotRequired[int],
    },
)
AwsDynamoDbTableRestoreSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    {
        "SourceBackupArn": NotRequired[str],
        "SourceTableArn": NotRequired[str],
        "RestoreDateTime": NotRequired[str],
        "RestoreInProgress": NotRequired[bool],
    },
)
AwsDynamoDbTableSseDescriptionTypeDef = TypedDict(
    "AwsDynamoDbTableSseDescriptionTypeDef",
    {
        "InaccessibleEncryptionDateTime": NotRequired[str],
        "Status": NotRequired[str],
        "SseType": NotRequired[str],
        "KmsMasterKeyArn": NotRequired[str],
    },
)
AwsDynamoDbTableStreamSpecificationTypeDef = TypedDict(
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": NotRequired[bool],
        "StreamViewType": NotRequired[str],
    },
)
AwsDynamoDbTableProjectionOutputTypeDef = TypedDict(
    "AwsDynamoDbTableProjectionOutputTypeDef",
    {
        "NonKeyAttributes": NotRequired[List[str]],
        "ProjectionType": NotRequired[str],
    },
)
AwsDynamoDbTableProjectionTypeDef = TypedDict(
    "AwsDynamoDbTableProjectionTypeDef",
    {
        "NonKeyAttributes": NotRequired[Sequence[str]],
        "ProjectionType": NotRequired[str],
    },
)
AwsDynamoDbTableProvisionedThroughputOverrideTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": NotRequired[int],
    },
)
AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef",
    {
        "DirectoryId": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef",
    {
        "SamlProviderArn": NotRequired[str],
        "SelfServiceSamlProviderArn": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef",
    {
        "ClientRootCertificateChain": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "BannerText": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "CloudwatchLogGroup": NotRequired[str],
        "CloudwatchLogStream": NotRequired[str],
    },
)
AwsEc2EipDetailsTypeDef = TypedDict(
    "AwsEc2EipDetailsTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllocationId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "Domain": NotRequired[str],
        "PublicIpv4Pool": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfaceOwnerId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)
AwsEc2InstanceMetadataOptionsTypeDef = TypedDict(
    "AwsEc2InstanceMetadataOptionsTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "HttpProtocolIpv6": NotRequired[str],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpTokens": NotRequired[str],
        "InstanceMetadataTags": NotRequired[str],
    },
)
AwsEc2InstanceMonitoringDetailsTypeDef = TypedDict(
    "AwsEc2InstanceMonitoringDetailsTypeDef",
    {
        "State": NotRequired[str],
    },
)
AwsEc2InstanceNetworkInterfacesDetailsTypeDef = TypedDict(
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Throughput": NotRequired[int],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "CapacityReservationResourceGroupArn": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef",
    {
        "CpuCredits": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)
AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef",
    {
        "AutoRecovery": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "HttpProtocolIpv6": NotRequired[str],
        "HttpTokens": NotRequired[str],
        "HttpPutResponseHopLimit": NotRequired[int],
        "InstanceMetadataTags": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsEc2LaunchTemplateDataPlacementDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataPlacementDetailsTypeDef",
    {
        "Affinity": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "GroupName": NotRequired[str],
        "HostId": NotRequired[str],
        "HostResourceGroupArn": NotRequired[str],
        "PartitionNumber": NotRequired[int],
        "SpreadDomain": NotRequired[str],
        "Tenancy": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef",
    {
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "HostnameType": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef",
    {
        "BlockDurationMinutes": NotRequired[int],
        "InstanceInterruptionBehavior": NotRequired[str],
        "MaxPrice": NotRequired[str],
        "SpotInstanceType": NotRequired[str],
        "ValidUntil": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef",
    {
        "Max": NotRequired[float],
        "Min": NotRequired[float],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef",
    {
        "Max": NotRequired[float],
        "Min": NotRequired[float],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef",
    {
        "Ipv6Address": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef",
    {
        "Primary": NotRequired[bool],
        "PrivateIpAddress": NotRequired[str],
    },
)
AwsEc2NetworkAclAssociationTypeDef = TypedDict(
    "AwsEc2NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": NotRequired[str],
        "NetworkAclId": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)
IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": NotRequired[int],
        "Type": NotRequired[int],
    },
)
PortRangeFromToTypeDef = TypedDict(
    "PortRangeFromToTypeDef",
    {
        "From": NotRequired[int],
        "To": NotRequired[int],
    },
)
AwsEc2NetworkInterfaceAttachmentTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "DeviceIndex": NotRequired[int],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    {
        "IpV6Address": NotRequired[str],
    },
)
AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    {
        "PrivateIpAddress": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
    },
)
AwsEc2NetworkInterfaceSecurityGroupTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)
PropagatingVgwSetDetailsTypeDef = TypedDict(
    "PropagatingVgwSetDetailsTypeDef",
    {
        "GatewayId": NotRequired[str],
    },
)
RouteSetDetailsTypeDef = TypedDict(
    "RouteSetDetailsTypeDef",
    {
        "CarrierGatewayId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "Origin": NotRequired[str],
        "State": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
AwsEc2SecurityGroupIpRangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpRangeTypeDef",
    {
        "CidrIp": NotRequired[str],
    },
)
AwsEc2SecurityGroupIpv6RangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    {
        "CidrIpv6": NotRequired[str],
    },
)
AwsEc2SecurityGroupPrefixListIdTypeDef = TypedDict(
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    {
        "PrefixListId": NotRequired[str],
    },
)
AwsEc2SecurityGroupUserIdGroupPairTypeDef = TypedDict(
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "PeeringStatus": NotRequired[str],
        "UserId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
Ipv6CidrBlockAssociationTypeDef = TypedDict(
    "Ipv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "CidrBlockState": NotRequired[str],
    },
)
AwsEc2TransitGatewayDetailsOutputTypeDef = TypedDict(
    "AwsEc2TransitGatewayDetailsOutputTypeDef",
    {
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteTablePropagation": NotRequired[str],
        "AutoAcceptSharedAttachments": NotRequired[str],
        "DefaultRouteTableAssociation": NotRequired[str],
        "TransitGatewayCidrBlocks": NotRequired[List[str]],
        "AssociationDefaultRouteTableId": NotRequired[str],
        "PropagationDefaultRouteTableId": NotRequired[str],
        "VpnEcmpSupport": NotRequired[str],
        "DnsSupport": NotRequired[str],
        "MulticastSupport": NotRequired[str],
        "AmazonSideAsn": NotRequired[int],
    },
)
AwsEc2TransitGatewayDetailsTypeDef = TypedDict(
    "AwsEc2TransitGatewayDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteTablePropagation": NotRequired[str],
        "AutoAcceptSharedAttachments": NotRequired[str],
        "DefaultRouteTableAssociation": NotRequired[str],
        "TransitGatewayCidrBlocks": NotRequired[Sequence[str]],
        "AssociationDefaultRouteTableId": NotRequired[str],
        "PropagationDefaultRouteTableId": NotRequired[str],
        "VpnEcmpSupport": NotRequired[str],
        "DnsSupport": NotRequired[str],
        "MulticastSupport": NotRequired[str],
        "AmazonSideAsn": NotRequired[int],
    },
)
AwsEc2VolumeAttachmentTypeDef = TypedDict(
    "AwsEc2VolumeAttachmentTypeDef",
    {
        "AttachTime": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
CidrBlockAssociationTypeDef = TypedDict(
    "CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "CidrBlockState": NotRequired[str],
    },
)
AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    {
        "ServiceType": NotRequired[str],
    },
)
AwsEc2VpcPeeringConnectionStatusDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionStatusDetailsTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
VpcInfoCidrBlockSetDetailsTypeDef = TypedDict(
    "VpcInfoCidrBlockSetDetailsTypeDef",
    {
        "CidrBlock": NotRequired[str],
    },
)
VpcInfoIpv6CidrBlockSetDetailsTypeDef = TypedDict(
    "VpcInfoIpv6CidrBlockSetDetailsTypeDef",
    {
        "Ipv6CidrBlock": NotRequired[str],
    },
)
VpcInfoPeeringOptionsDetailsTypeDef = TypedDict(
    "VpcInfoPeeringOptionsDetailsTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalClassicLinkToRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalVpcToRemoteClassicLink": NotRequired[bool],
    },
)
AwsEc2VpnConnectionRoutesDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "State": NotRequired[str],
    },
)
AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    {
        "AcceptedRouteCount": NotRequired[int],
        "CertificateArn": NotRequired[str],
        "LastStatusChange": NotRequired[str],
        "OutsideIpAddress": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)
AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef",
    {
        "DpdTimeoutSeconds": NotRequired[int],
        "IkeVersions": NotRequired[List[str]],
        "OutsideIpAddress": NotRequired[str],
        "Phase1DhGroupNumbers": NotRequired[List[int]],
        "Phase1EncryptionAlgorithms": NotRequired[List[str]],
        "Phase1IntegrityAlgorithms": NotRequired[List[str]],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2DhGroupNumbers": NotRequired[List[int]],
        "Phase2EncryptionAlgorithms": NotRequired[List[str]],
        "Phase2IntegrityAlgorithms": NotRequired[List[str]],
        "Phase2LifetimeSeconds": NotRequired[int],
        "PreSharedKey": NotRequired[str],
        "RekeyFuzzPercentage": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "TunnelInsideCidr": NotRequired[str],
    },
)
AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    {
        "DpdTimeoutSeconds": NotRequired[int],
        "IkeVersions": NotRequired[Sequence[str]],
        "OutsideIpAddress": NotRequired[str],
        "Phase1DhGroupNumbers": NotRequired[Sequence[int]],
        "Phase1EncryptionAlgorithms": NotRequired[Sequence[str]],
        "Phase1IntegrityAlgorithms": NotRequired[Sequence[str]],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2DhGroupNumbers": NotRequired[Sequence[int]],
        "Phase2EncryptionAlgorithms": NotRequired[Sequence[str]],
        "Phase2IntegrityAlgorithms": NotRequired[Sequence[str]],
        "Phase2LifetimeSeconds": NotRequired[int],
        "PreSharedKey": NotRequired[str],
        "RekeyFuzzPercentage": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "TunnelInsideCidr": NotRequired[str],
    },
)
AwsEcrContainerImageDetailsOutputTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsOutputTypeDef",
    {
        "RegistryId": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Architecture": NotRequired[str],
        "ImageDigest": NotRequired[str],
        "ImageTags": NotRequired[List[str]],
        "ImagePublishedAt": NotRequired[str],
    },
)
AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "RegistryId": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Architecture": NotRequired[str],
        "ImageDigest": NotRequired[str],
        "ImageTags": NotRequired[Sequence[str]],
        "ImagePublishedAt": NotRequired[str],
    },
)
AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    {
        "ScanOnPush": NotRequired[bool],
    },
)
AwsEcrRepositoryLifecyclePolicyDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    {
        "LifecyclePolicyText": NotRequired[str],
        "RegistryId": NotRequired[str],
    },
)
AwsEcsClusterClusterSettingsDetailsTypeDef = TypedDict(
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    {
        "CloudWatchEncryptionEnabled": NotRequired[bool],
        "CloudWatchLogGroupName": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3EncryptionEnabled": NotRequired[bool],
        "S3KeyPrefix": NotRequired[str],
    },
)
AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": NotRequired[int],
        "CapacityProvider": NotRequired[str],
        "Weight": NotRequired[int],
    },
)
AwsMountPointTypeDef = TypedDict(
    "AwsMountPointTypeDef",
    {
        "SourceVolume": NotRequired[str],
        "ContainerPath": NotRequired[str],
    },
)
AwsEcsServiceCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": NotRequired[int],
        "CapacityProvider": NotRequired[str],
        "Weight": NotRequired[int],
    },
)
AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    {
        "Enable": NotRequired[bool],
        "Rollback": NotRequired[bool],
    },
)
AwsEcsServiceDeploymentControllerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsEcsServiceLoadBalancersDetailsTypeDef = TypedDict(
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ContainerPort": NotRequired[int],
        "LoadBalancerName": NotRequired[str],
        "TargetGroupArn": NotRequired[str],
    },
)
AwsEcsServicePlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    {
        "Expression": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsEcsServicePlacementStrategiesDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    {
        "Field": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsEcsServiceServiceRegistriesDetailsTypeDef = TypedDict(
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ContainerPort": NotRequired[int],
        "Port": NotRequired[int],
        "RegistryArn": NotRequired[str],
    },
)
AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef",
    {
        "AssignPublicIp": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "Subnets": NotRequired[List[str]],
    },
)
AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    {
        "AssignPublicIp": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Subnets": NotRequired[Sequence[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    {
        "Condition": NotRequired[str],
        "ContainerName": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    {
        "Hostname": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef",
    {
        "Options": NotRequired[Dict[str, str]],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef",
    {
        "Command": NotRequired[List[str]],
        "Interval": NotRequired[int],
        "Retries": NotRequired[int],
        "StartPeriod": NotRequired[int],
        "Timeout": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "SourceVolume": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    {
        "ContainerPort": NotRequired[int],
        "HostPort": NotRequired[int],
        "Protocol": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    {
        "CredentialsParameter": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "ValueFrom": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    {
        "Namespace": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    {
        "HardLimit": NotRequired[int],
        "Name": NotRequired[str],
        "SoftLimit": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    {
        "ReadOnly": NotRequired[bool],
        "SourceContainer": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    {
        "Options": NotRequired[Mapping[str, str]],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Interval": NotRequired[int],
        "Retries": NotRequired[int],
        "StartPeriod": NotRequired[int],
        "Timeout": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef",
    {
        "Add": NotRequired[List[str]],
        "Drop": NotRequired[List[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    {
        "Add": NotRequired[Sequence[str]],
        "Drop": NotRequired[Sequence[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "HostPath": NotRequired[str],
        "Permissions": NotRequired[List[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "MountOptions": NotRequired[List[str]],
        "Size": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "HostPath": NotRequired[str],
        "Permissions": NotRequired[Sequence[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "MountOptions": NotRequired[Sequence[str]],
        "Size": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "ValueFrom": NotRequired[str],
    },
)
AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    {
        "DeviceName": NotRequired[str],
        "DeviceType": NotRequired[str],
    },
)
AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    {
        "Expression": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef",
    {
        "Autoprovision": NotRequired[bool],
        "Driver": NotRequired[str],
        "DriverOpts": NotRequired[Dict[str, str]],
        "Labels": NotRequired[Dict[str, str]],
        "Scope": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesHostDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    {
        "SourcePath": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    {
        "Autoprovision": NotRequired[bool],
        "Driver": NotRequired[str],
        "DriverOpts": NotRequired[Mapping[str, str]],
        "Labels": NotRequired[Mapping[str, str]],
        "Scope": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    {
        "AccessPointId": NotRequired[str],
        "Iam": NotRequired[str],
    },
)
AwsEcsTaskVolumeHostDetailsTypeDef = TypedDict(
    "AwsEcsTaskVolumeHostDetailsTypeDef",
    {
        "SourcePath": NotRequired[str],
    },
)
AwsEfsAccessPointPosixUserDetailsOutputTypeDef = TypedDict(
    "AwsEfsAccessPointPosixUserDetailsOutputTypeDef",
    {
        "Gid": NotRequired[str],
        "SecondaryGids": NotRequired[List[str]],
        "Uid": NotRequired[str],
    },
)
AwsEfsAccessPointPosixUserDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointPosixUserDetailsTypeDef",
    {
        "Gid": NotRequired[str],
        "SecondaryGids": NotRequired[Sequence[str]],
        "Uid": NotRequired[str],
    },
)
AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef",
    {
        "OwnerGid": NotRequired[str],
        "OwnerUid": NotRequired[str],
        "Permissions": NotRequired[str],
    },
)
AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef = TypedDict(
    "AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef",
    {
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "EndpointPublicAccess": NotRequired[bool],
    },
)
AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef = TypedDict(
    "AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Types": NotRequired[List[str]],
    },
)
AwsEksClusterLoggingClusterLoggingDetailsTypeDef = TypedDict(
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Types": NotRequired[Sequence[str]],
    },
)
AwsEksClusterResourcesVpcConfigDetailsTypeDef = TypedDict(
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "EndpointPublicAccess": NotRequired[bool],
    },
)
AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    {
        "EnvironmentName": NotRequired[str],
        "LinkName": NotRequired[str],
    },
)
AwsElasticBeanstalkEnvironmentOptionSettingTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    {
        "Namespace": NotRequired[str],
        "OptionName": NotRequired[str],
        "ResourceName": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsElasticBeanstalkEnvironmentTierTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Version": NotRequired[str],
    },
)
AwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": NotRequired[bool],
        "TLSSecurityPolicy": NotRequired[str],
    },
)
AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
    },
)
AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsElasticsearchDomainServiceSoftwareOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    {
        "AutomatedUpdateDate": NotRequired[str],
        "Cancellable": NotRequired[bool],
        "CurrentVersion": NotRequired[str],
        "Description": NotRequired[str],
        "NewVersion": NotRequired[str],
        "UpdateAvailable": NotRequired[bool],
        "UpdateStatus": NotRequired[str],
    },
)
AwsElasticsearchDomainVPCOptionsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsOutputTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "VPCId": NotRequired[str],
    },
)
AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": NotRequired[int],
    },
)
AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
    },
)
AwsElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "VPCId": NotRequired[str],
    },
)
AwsElbAppCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbAppCookieStickinessPolicyTypeDef",
    {
        "CookieName": NotRequired[str],
        "PolicyName": NotRequired[str],
    },
)
AwsElbLbCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbLbCookieStickinessPolicyTypeDef",
    {
        "CookieExpirationPeriod": NotRequired[int],
        "PolicyName": NotRequired[str],
    },
)
AwsElbLoadBalancerAccessLogTypeDef = TypedDict(
    "AwsElbLoadBalancerAccessLogTypeDef",
    {
        "EmitInterval": NotRequired[int],
        "Enabled": NotRequired[bool],
        "S3BucketName": NotRequired[str],
        "S3BucketPrefix": NotRequired[str],
    },
)
AwsElbLoadBalancerAdditionalAttributeTypeDef = TypedDict(
    "AwsElbLoadBalancerAdditionalAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsElbLoadBalancerConnectionDrainingTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Timeout": NotRequired[int],
    },
)
AwsElbLoadBalancerConnectionSettingsTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    {
        "IdleTimeout": NotRequired[int],
    },
)
AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef = TypedDict(
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef",
    {
        "InstancePort": NotRequired[int],
        "PolicyNames": NotRequired[List[str]],
    },
)
AwsElbLoadBalancerBackendServerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    {
        "InstancePort": NotRequired[int],
        "PolicyNames": NotRequired[Sequence[str]],
    },
)
AwsElbLoadBalancerHealthCheckTypeDef = TypedDict(
    "AwsElbLoadBalancerHealthCheckTypeDef",
    {
        "HealthyThreshold": NotRequired[int],
        "Interval": NotRequired[int],
        "Target": NotRequired[str],
        "Timeout": NotRequired[int],
        "UnhealthyThreshold": NotRequired[int],
    },
)
AwsElbLoadBalancerInstanceTypeDef = TypedDict(
    "AwsElbLoadBalancerInstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
    },
)
AwsElbLoadBalancerSourceSecurityGroupTypeDef = TypedDict(
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "OwnerAlias": NotRequired[str],
    },
)
AwsElbLoadBalancerListenerTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerTypeDef",
    {
        "InstancePort": NotRequired[int],
        "InstanceProtocol": NotRequired[str],
        "LoadBalancerPort": NotRequired[int],
        "Protocol": NotRequired[str],
        "SslCertificateId": NotRequired[str],
    },
)
AwsElbv2LoadBalancerAttributeTypeDef = TypedDict(
    "AwsElbv2LoadBalancerAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
AwsEventSchemasRegistryDetailsTypeDef = TypedDict(
    "AwsEventSchemasRegistryDetailsTypeDef",
    {
        "Description": NotRequired[str],
        "RegistryArn": NotRequired[str],
        "RegistryName": NotRequired[str],
    },
)
AwsEventsEndpointEventBusesDetailsTypeDef = TypedDict(
    "AwsEventsEndpointEventBusesDetailsTypeDef",
    {
        "EventBusArn": NotRequired[str],
    },
)
AwsEventsEndpointReplicationConfigDetailsTypeDef = TypedDict(
    "AwsEventsEndpointReplicationConfigDetailsTypeDef",
    {
        "State": NotRequired[str],
    },
)
AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef = TypedDict(
    "AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef",
    {
        "HealthCheck": NotRequired[str],
    },
)
AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef = TypedDict(
    "AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef",
    {
        "Route": NotRequired[str],
    },
)
AwsEventsEventbusDetailsTypeDef = TypedDict(
    "AwsEventsEventbusDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Policy": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef",
    {
        "Reason": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorFeaturesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorFeaturesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsIamAccessKeySessionContextAttributesTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    {
        "MfaAuthenticated": NotRequired[bool],
        "CreationDate": NotRequired[str],
    },
)
AwsIamAccessKeySessionContextSessionIssuerTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    {
        "Type": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "Arn": NotRequired[str],
        "AccountId": NotRequired[str],
        "UserName": NotRequired[str],
    },
)
AwsIamAttachedManagedPolicyTypeDef = TypedDict(
    "AwsIamAttachedManagedPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyArn": NotRequired[str],
    },
)
AwsIamGroupPolicyTypeDef = TypedDict(
    "AwsIamGroupPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)
AwsIamInstanceProfileRoleTypeDef = TypedDict(
    "AwsIamInstanceProfileRoleTypeDef",
    {
        "Arn": NotRequired[str],
        "AssumeRolePolicyDocument": NotRequired[str],
        "CreateDate": NotRequired[str],
        "Path": NotRequired[str],
        "RoleId": NotRequired[str],
        "RoleName": NotRequired[str],
    },
)
AwsIamPermissionsBoundaryTypeDef = TypedDict(
    "AwsIamPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryArn": NotRequired[str],
        "PermissionsBoundaryType": NotRequired[str],
    },
)
AwsIamPolicyVersionTypeDef = TypedDict(
    "AwsIamPolicyVersionTypeDef",
    {
        "VersionId": NotRequired[str],
        "IsDefaultVersion": NotRequired[bool],
        "CreateDate": NotRequired[str],
    },
)
AwsIamRolePolicyTypeDef = TypedDict(
    "AwsIamRolePolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)
AwsIamUserPolicyTypeDef = TypedDict(
    "AwsIamUserPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)
AwsKinesisStreamStreamEncryptionDetailsTypeDef = TypedDict(
    "AwsKinesisStreamStreamEncryptionDetailsTypeDef",
    {
        "EncryptionType": NotRequired[str],
        "KeyId": NotRequired[str],
    },
)
AwsKmsKeyDetailsTypeDef = TypedDict(
    "AwsKmsKeyDetailsTypeDef",
    {
        "AWSAccountId": NotRequired[str],
        "CreationDate": NotRequired[float],
        "KeyId": NotRequired[str],
        "KeyManager": NotRequired[str],
        "KeyState": NotRequired[str],
        "Origin": NotRequired[str],
        "Description": NotRequired[str],
        "KeyRotationStatus": NotRequired[bool],
    },
)
AwsLambdaFunctionCodeTypeDef = TypedDict(
    "AwsLambdaFunctionCodeTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3ObjectVersion": NotRequired[str],
        "ZipFile": NotRequired[str],
    },
)
AwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    {
        "TargetArn": NotRequired[str],
    },
)
AwsLambdaFunctionLayerTypeDef = TypedDict(
    "AwsLambdaFunctionLayerTypeDef",
    {
        "Arn": NotRequired[str],
        "CodeSize": NotRequired[int],
    },
)
AwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "AwsLambdaFunctionTracingConfigTypeDef",
    {
        "Mode": NotRequired[str],
    },
)
AwsLambdaFunctionVpcConfigOutputTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigOutputTypeDef",
    {
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "VpcId": NotRequired[str],
    },
)
AwsLambdaFunctionEnvironmentErrorTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
    },
)
AwsLambdaLayerVersionDetailsOutputTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsOutputTypeDef",
    {
        "Version": NotRequired[int],
        "CompatibleRuntimes": NotRequired[List[str]],
        "CreatedDate": NotRequired[str],
    },
)
AwsLambdaLayerVersionDetailsTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsTypeDef",
    {
        "Version": NotRequired[int],
        "CompatibleRuntimes": NotRequired[Sequence[str]],
        "CreatedDate": NotRequired[str],
    },
)
AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef",
    {
        "CertificateAuthorityArnList": NotRequired[List[str]],
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef",
    {
        "CertificateAuthorityArnList": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef",
    {
        "DataVolumeKMSKeyId": NotRequired[str],
    },
)
AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef",
    {
        "InCluster": NotRequired[bool],
        "ClientBroker": NotRequired[str],
    },
)
AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    {
        "SubnetId": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef",
    {
        "MasterUserArn": NotRequired[str],
        "MasterUserName": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": NotRequired[int],
    },
)
AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    {
        "CustomEndpointCertificateArn": NotRequired[str],
        "CustomEndpointEnabled": NotRequired[bool],
        "EnforceHTTPS": NotRequired[bool],
        "CustomEndpoint": NotRequired[str],
        "TLSSecurityPolicy": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    {
        "AutomatedUpdateDate": NotRequired[str],
        "Cancellable": NotRequired[bool],
        "CurrentVersion": NotRequired[str],
        "Description": NotRequired[str],
        "NewVersion": NotRequired[str],
        "UpdateAvailable": NotRequired[bool],
        "UpdateStatus": NotRequired[str],
        "OptionalDeployment": NotRequired[bool],
    },
)
AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef",
    {
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
    },
)
AwsOpenSearchServiceDomainLogPublishingOptionTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
    },
)
AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)
AwsRdsDbClusterAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbClusterMemberTypeDef = TypedDict(
    "AwsRdsDbClusterMemberTypeDef",
    {
        "IsClusterWriter": NotRequired[bool],
        "PromotionTier": NotRequired[int],
        "DbInstanceIdentifier": NotRequired[str],
        "DbClusterParameterGroupStatus": NotRequired[str],
    },
)
AwsRdsDbClusterOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    {
        "DbClusterOptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbDomainMembershipTypeDef = TypedDict(
    "AwsRdsDbDomainMembershipTypeDef",
    {
        "Domain": NotRequired[str],
        "Status": NotRequired[str],
        "Fqdn": NotRequired[str],
        "IamRoleName": NotRequired[str],
    },
)
AwsRdsDbInstanceVpcSecurityGroupTypeDef = TypedDict(
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List[str]],
    },
)
AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[Sequence[str]],
    },
)
AwsRdsDbInstanceAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "FeatureName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbInstanceEndpointTypeDef = TypedDict(
    "AwsRdsDbInstanceEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
        "HostedZoneId": NotRequired[str],
    },
)
AwsRdsDbOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbOptionGroupMembershipTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbParameterGroupTypeDef = TypedDict(
    "AwsRdsDbParameterGroupTypeDef",
    {
        "DbParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
    },
)
AwsRdsDbProcessorFeatureTypeDef = TypedDict(
    "AwsRdsDbProcessorFeatureTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsRdsDbStatusInfoTypeDef = TypedDict(
    "AwsRdsDbStatusInfoTypeDef",
    {
        "StatusType": NotRequired[str],
        "Normal": NotRequired[bool],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AwsRdsPendingCloudWatchLogsExportsOutputTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsOutputTypeDef",
    {
        "LogTypesToEnable": NotRequired[List[str]],
        "LogTypesToDisable": NotRequired[List[str]],
    },
)
AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef",
    {
        "Ec2SecurityGroupId": NotRequired[str],
        "Ec2SecurityGroupName": NotRequired[str],
        "Ec2SecurityGroupOwnerId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbSecurityGroupIpRangeTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupIpRangeTypeDef",
    {
        "CidrIp": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)
AwsRdsEventSubscriptionDetailsOutputTypeDef = TypedDict(
    "AwsRdsEventSubscriptionDetailsOutputTypeDef",
    {
        "CustSubscriptionId": NotRequired[str],
        "CustomerAwsId": NotRequired[str],
        "Enabled": NotRequired[bool],
        "EventCategoriesList": NotRequired[List[str]],
        "EventSubscriptionArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SourceIdsList": NotRequired[List[str]],
        "SourceType": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
    },
)
AwsRdsEventSubscriptionDetailsTypeDef = TypedDict(
    "AwsRdsEventSubscriptionDetailsTypeDef",
    {
        "CustSubscriptionId": NotRequired[str],
        "CustomerAwsId": NotRequired[str],
        "Enabled": NotRequired[bool],
        "EventCategoriesList": NotRequired[Sequence[str]],
        "EventSubscriptionArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SourceIdsList": NotRequired[Sequence[str]],
        "SourceType": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
    },
)
AwsRdsPendingCloudWatchLogsExportsTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": NotRequired[Sequence[str]],
        "LogTypesToDisable": NotRequired[Sequence[str]],
    },
)
AwsRedshiftClusterClusterNodeTypeDef = TypedDict(
    "AwsRedshiftClusterClusterNodeTypeDef",
    {
        "NodeRole": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PublicIpAddress": NotRequired[str],
    },
)
AwsRedshiftClusterClusterParameterStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterApplyErrorDescription": NotRequired[str],
    },
)
AwsRedshiftClusterClusterSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "RetentionPeriod": NotRequired[int],
        "SnapshotCopyGrantName": NotRequired[str],
    },
)
AwsRedshiftClusterDeferredMaintenanceWindowTypeDef = TypedDict(
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceEndTime": NotRequired[str],
        "DeferMaintenanceIdentifier": NotRequired[str],
        "DeferMaintenanceStartTime": NotRequired[str],
    },
)
AwsRedshiftClusterElasticIpStatusTypeDef = TypedDict(
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    {
        "ElasticIp": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRedshiftClusterEndpointTypeDef = TypedDict(
    "AwsRedshiftClusterEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)
AwsRedshiftClusterHsmStatusTypeDef = TypedDict(
    "AwsRedshiftClusterHsmStatusTypeDef",
    {
        "HsmClientCertificateIdentifier": NotRequired[str],
        "HsmConfigurationIdentifier": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRedshiftClusterIamRoleTypeDef = TypedDict(
    "AwsRedshiftClusterIamRoleTypeDef",
    {
        "ApplyStatus": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)
AwsRedshiftClusterLoggingStatusTypeDef = TypedDict(
    "AwsRedshiftClusterLoggingStatusTypeDef",
    {
        "BucketName": NotRequired[str],
        "LastFailureMessage": NotRequired[str],
        "LastFailureTime": NotRequired[str],
        "LastSuccessfulDeliveryTime": NotRequired[str],
        "LoggingEnabled": NotRequired[bool],
        "S3KeyPrefix": NotRequired[str],
    },
)
AwsRedshiftClusterPendingModifiedValuesTypeDef = TypedDict(
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    {
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "ClusterIdentifier": NotRequired[str],
        "ClusterType": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "EncryptionType": NotRequired[str],
        "EnhancedVpcRouting": NotRequired[bool],
        "MaintenanceTrackName": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
    },
)
AwsRedshiftClusterResizeInfoTypeDef = TypedDict(
    "AwsRedshiftClusterResizeInfoTypeDef",
    {
        "AllowCancelResize": NotRequired[bool],
        "ResizeType": NotRequired[str],
    },
)
AwsRedshiftClusterRestoreStatusTypeDef = TypedDict(
    "AwsRedshiftClusterRestoreStatusTypeDef",
    {
        "CurrentRestoreRateInMegaBytesPerSecond": NotRequired[float],
        "ElapsedTimeInSeconds": NotRequired[int],
        "EstimatedTimeToCompletionInSeconds": NotRequired[int],
        "ProgressInMegaBytes": NotRequired[int],
        "SnapshotSizeInMegaBytes": NotRequired[int],
        "Status": NotRequired[str],
    },
)
AwsRedshiftClusterVpcSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    {
        "Status": NotRequired[str],
        "VpcSecurityGroupId": NotRequired[str],
    },
)
AwsRoute53HostedZoneConfigDetailsTypeDef = TypedDict(
    "AwsRoute53HostedZoneConfigDetailsTypeDef",
    {
        "Comment": NotRequired[str],
    },
)
AwsRoute53HostedZoneVpcDetailsTypeDef = TypedDict(
    "AwsRoute53HostedZoneVpcDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Region": NotRequired[str],
    },
)
CloudWatchLogsLogGroupArnConfigDetailsTypeDef = TypedDict(
    "CloudWatchLogsLogGroupArnConfigDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "HostedZoneId": NotRequired[str],
        "Id": NotRequired[str],
    },
)
AwsS3AccessPointVpcConfigurationDetailsTypeDef = TypedDict(
    "AwsS3AccessPointVpcConfigurationDetailsTypeDef",
    {
        "VpcId": NotRequired[str],
    },
)
AwsS3AccountPublicAccessBlockDetailsTypeDef = TypedDict(
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    {
        "BlockPublicAcls": NotRequired[bool],
        "BlockPublicPolicy": NotRequired[bool],
        "IgnorePublicAcls": NotRequired[bool],
        "RestrictPublicBuckets": NotRequired[bool],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef = (
    TypedDict(
        "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
        {
            "DaysAfterInitiation": NotRequired[int],
        },
    )
)
AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    {
        "Days": NotRequired[int],
        "StorageClass": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    {
        "Date": NotRequired[str],
        "Days": NotRequired[int],
        "StorageClass": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsS3BucketBucketVersioningConfigurationTypeDef = TypedDict(
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    {
        "IsMfaDeleteEnabled": NotRequired[bool],
        "Status": NotRequired[str],
    },
)
AwsS3BucketLoggingConfigurationTypeDef = TypedDict(
    "AwsS3BucketLoggingConfigurationTypeDef",
    {
        "DestinationBucketName": NotRequired[str],
        "LogFilePrefix": NotRequired[str],
    },
)
AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    {
        "Name": NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType],
        "Value": NotRequired[str],
    },
)
AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef",
    {
        "Days": NotRequired[int],
        "Mode": NotRequired[str],
        "Years": NotRequired[int],
    },
)
AwsS3BucketServerSideEncryptionByDefaultTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    {
        "SSEAlgorithm": NotRequired[str],
        "KMSMasterKeyID": NotRequired[str],
    },
)
AwsS3BucketWebsiteConfigurationRedirectToTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    {
        "Hostname": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)
AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    {
        "HttpErrorCodeReturnedEquals": NotRequired[str],
        "KeyPrefixEquals": NotRequired[str],
    },
)
AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    {
        "Hostname": NotRequired[str],
        "HttpRedirectCode": NotRequired[str],
        "Protocol": NotRequired[str],
        "ReplaceKeyPrefixWith": NotRequired[str],
        "ReplaceKeyWith": NotRequired[str],
    },
)
AwsS3ObjectDetailsTypeDef = TypedDict(
    "AwsS3ObjectDetailsTypeDef",
    {
        "LastModified": NotRequired[str],
        "ETag": NotRequired[str],
        "VersionId": NotRequired[str],
        "ContentType": NotRequired[str],
        "ServerSideEncryption": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
    },
)
AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef",
    {
        "MinimumInstanceMetadataServiceVersion": NotRequired[str],
    },
)
AwsSecretsManagerSecretRotationRulesTypeDef = TypedDict(
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    {
        "AutomaticallyAfterDays": NotRequired[int],
    },
)
BooleanFilterTypeDef = TypedDict(
    "BooleanFilterTypeDef",
    {
        "Value": NotRequired[bool],
    },
)
IpFilterTypeDef = TypedDict(
    "IpFilterTypeDef",
    {
        "Cidr": NotRequired[str],
    },
)
KeywordFilterTypeDef = TypedDict(
    "KeywordFilterTypeDef",
    {
        "Value": NotRequired[str],
    },
)
AwsSecurityFindingIdentifierTypeDef = TypedDict(
    "AwsSecurityFindingIdentifierTypeDef",
    {
        "Id": str,
        "ProductArn": str,
    },
)
GeneratorDetailsOutputTypeDef = TypedDict(
    "GeneratorDetailsOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Labels": NotRequired[List[str]],
    },
)
MalwareTypeDef = TypedDict(
    "MalwareTypeDef",
    {
        "Name": str,
        "Type": NotRequired[MalwareTypeType],
        "Path": NotRequired[str],
        "State": NotRequired[MalwareStateType],
    },
)
NoteTypeDef = TypedDict(
    "NoteTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
        "UpdatedAt": str,
    },
)
PatchSummaryTypeDef = TypedDict(
    "PatchSummaryTypeDef",
    {
        "Id": str,
        "InstalledCount": NotRequired[int],
        "MissingCount": NotRequired[int],
        "FailedCount": NotRequired[int],
        "InstalledOtherCount": NotRequired[int],
        "InstalledRejectedCount": NotRequired[int],
        "InstalledPendingReboot": NotRequired[int],
        "OperationStartTime": NotRequired[str],
        "OperationEndTime": NotRequired[str],
        "RebootOption": NotRequired[str],
        "Operation": NotRequired[str],
    },
)
ProcessDetailsTypeDef = TypedDict(
    "ProcessDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Path": NotRequired[str],
        "Pid": NotRequired[int],
        "ParentPid": NotRequired[int],
        "LaunchedAt": NotRequired[str],
        "TerminatedAt": NotRequired[str],
    },
)
SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "Product": NotRequired[float],
        "Label": NotRequired[SeverityLabelType],
        "Normalized": NotRequired[int],
        "Original": NotRequired[str],
    },
)
ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": NotRequired[ThreatIntelIndicatorTypeType],
        "Value": NotRequired[str],
        "Category": NotRequired[ThreatIntelIndicatorCategoryType],
        "LastObservedAt": NotRequired[str],
        "Source": NotRequired[str],
        "SourceUrl": NotRequired[str],
    },
)
WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Status": NotRequired[WorkflowStatusType],
    },
)
AwsSnsTopicSubscriptionTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionTypeDef",
    {
        "Endpoint": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)
AwsSqsQueueDetailsTypeDef = TypedDict(
    "AwsSqsQueueDetailsTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": NotRequired[int],
        "KmsMasterKeyId": NotRequired[str],
        "QueueName": NotRequired[str],
        "DeadLetterTargetArn": NotRequired[str],
    },
)
AwsSsmComplianceSummaryTypeDef = TypedDict(
    "AwsSsmComplianceSummaryTypeDef",
    {
        "Status": NotRequired[str],
        "CompliantCriticalCount": NotRequired[int],
        "CompliantHighCount": NotRequired[int],
        "CompliantMediumCount": NotRequired[int],
        "ExecutionType": NotRequired[str],
        "NonCompliantCriticalCount": NotRequired[int],
        "CompliantInformationalCount": NotRequired[int],
        "NonCompliantInformationalCount": NotRequired[int],
        "CompliantUnspecifiedCount": NotRequired[int],
        "NonCompliantLowCount": NotRequired[int],
        "NonCompliantHighCount": NotRequired[int],
        "CompliantLowCount": NotRequired[int],
        "ComplianceType": NotRequired[str],
        "PatchBaselineId": NotRequired[str],
        "OverallSeverity": NotRequired[str],
        "NonCompliantMediumCount": NotRequired[int],
        "NonCompliantUnspecifiedCount": NotRequired[int],
        "PatchGroup": NotRequired[str],
    },
)
AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef",
    {
        "LogGroupArn": NotRequired[str],
    },
)
AwsWafRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRulePredicateListDetailsTypeDef = TypedDict(
    "AwsWafRegionalRulePredicateListDetailsTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRuleGroupRulesActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRulePredicateListDetailsTypeDef = TypedDict(
    "AwsWafRulePredicateListDetailsTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRuleGroupRulesActionDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupRulesActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": NotRequired[str],
    },
)
WafExcludedRuleTypeDef = TypedDict(
    "WafExcludedRuleTypeDef",
    {
        "RuleId": NotRequired[str],
    },
)
WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafv2CustomHttpHeaderTypeDef = TypedDict(
    "AwsWafv2CustomHttpHeaderTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsWafv2VisibilityConfigDetailsTypeDef = TypedDict(
    "AwsWafv2VisibilityConfigDetailsTypeDef",
    {
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "MetricName": NotRequired[str],
        "SampledRequestsEnabled": NotRequired[bool],
    },
)
AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef",
    {
        "ImmunityTime": NotRequired[int],
    },
)
AwsXrayEncryptionConfigDetailsTypeDef = TypedDict(
    "AwsXrayEncryptionConfigDetailsTypeDef",
    {
        "KeyId": NotRequired[str],
        "Status": NotRequired[str],
        "Type": NotRequired[str],
    },
)
BatchDeleteAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchDeleteAutomationRulesRequestRequestTypeDef",
    {
        "AutomationRulesArns": Sequence[str],
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
UnprocessedAutomationRuleTypeDef = TypedDict(
    "UnprocessedAutomationRuleTypeDef",
    {
        "RuleArn": NotRequired[str],
        "ErrorCode": NotRequired[int],
        "ErrorMessage": NotRequired[str],
    },
)
BatchDisableStandardsRequestRequestTypeDef = TypedDict(
    "BatchDisableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": Sequence[str],
    },
)
StandardsSubscriptionRequestTypeDef = TypedDict(
    "StandardsSubscriptionRequestTypeDef",
    {
        "StandardsArn": str,
        "StandardsInput": NotRequired[Mapping[str, str]],
    },
)
BatchGetAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchGetAutomationRulesRequestRequestTypeDef",
    {
        "AutomationRulesArns": Sequence[str],
    },
)
ConfigurationPolicyAssociationSummaryTypeDef = TypedDict(
    "ConfigurationPolicyAssociationSummaryTypeDef",
    {
        "ConfigurationPolicyId": NotRequired[str],
        "TargetId": NotRequired[str],
        "TargetType": NotRequired[TargetTypeType],
        "AssociationType": NotRequired[AssociationTypeType],
        "UpdatedAt": NotRequired[datetime],
        "AssociationStatus": NotRequired[ConfigurationPolicyAssociationStatusType],
        "AssociationStatusMessage": NotRequired[str],
    },
)
BatchGetSecurityControlsRequestRequestTypeDef = TypedDict(
    "BatchGetSecurityControlsRequestRequestTypeDef",
    {
        "SecurityControlIds": Sequence[str],
    },
)
UnprocessedSecurityControlTypeDef = TypedDict(
    "UnprocessedSecurityControlTypeDef",
    {
        "SecurityControlId": str,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": NotRequired[str],
    },
)
StandardsControlAssociationIdTypeDef = TypedDict(
    "StandardsControlAssociationIdTypeDef",
    {
        "SecurityControlId": str,
        "StandardsArn": str,
    },
)
StandardsControlAssociationDetailTypeDef = TypedDict(
    "StandardsControlAssociationDetailTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "AssociationStatus": AssociationStatusType,
        "RelatedRequirements": NotRequired[List[str]],
        "UpdatedAt": NotRequired[datetime],
        "UpdatedReason": NotRequired[str],
        "StandardsControlTitle": NotRequired[str],
        "StandardsControlDescription": NotRequired[str],
        "StandardsControlArns": NotRequired[List[str]],
    },
)
ImportFindingsErrorTypeDef = TypedDict(
    "ImportFindingsErrorTypeDef",
    {
        "Id": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)
StandardsControlAssociationUpdateTypeDef = TypedDict(
    "StandardsControlAssociationUpdateTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "AssociationStatus": AssociationStatusType,
        "UpdatedReason": NotRequired[str],
    },
)
BooleanConfigurationOptionsTypeDef = TypedDict(
    "BooleanConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[bool],
    },
)
CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "Column": NotRequired[int],
        "Row": NotRequired[int],
        "ColumnName": NotRequired[str],
        "CellReference": NotRequired[str],
    },
)
ClassificationStatusTypeDef = TypedDict(
    "ClassificationStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
CodeVulnerabilitiesFilePathTypeDef = TypedDict(
    "CodeVulnerabilitiesFilePathTypeDef",
    {
        "EndLine": NotRequired[int],
        "FileName": NotRequired[str],
        "FilePath": NotRequired[str],
        "StartLine": NotRequired[int],
    },
)
SecurityControlParameterOutputTypeDef = TypedDict(
    "SecurityControlParameterOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[List[str]],
    },
)
StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "ReasonCode": str,
        "Description": NotRequired[str],
    },
)
DoubleConfigurationOptionsTypeDef = TypedDict(
    "DoubleConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[float],
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
EnumConfigurationOptionsTypeDef = TypedDict(
    "EnumConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "AllowedValues": NotRequired[List[str]],
    },
)
EnumListConfigurationOptionsTypeDef = TypedDict(
    "EnumListConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[List[str]],
        "MaxItems": NotRequired[int],
        "AllowedValues": NotRequired[List[str]],
    },
)
IntegerConfigurationOptionsTypeDef = TypedDict(
    "IntegerConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[int],
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
IntegerListConfigurationOptionsTypeDef = TypedDict(
    "IntegerListConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[List[int]],
        "Min": NotRequired[int],
        "Max": NotRequired[int],
        "MaxItems": NotRequired[int],
    },
)
StringConfigurationOptionsTypeDef = TypedDict(
    "StringConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "Re2Expression": NotRequired[str],
        "ExpressionDescription": NotRequired[str],
    },
)
StringListConfigurationOptionsTypeDef = TypedDict(
    "StringListConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[List[str]],
        "Re2Expression": NotRequired[str],
        "MaxItems": NotRequired[int],
        "ExpressionDescription": NotRequired[str],
    },
)
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "AccountId": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "RootId": NotRequired[str],
    },
)
ConfigurationPolicySummaryTypeDef = TypedDict(
    "ConfigurationPolicySummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "ServiceEnabled": NotRequired[bool],
    },
)
VolumeMountTypeDef = TypedDict(
    "VolumeMountTypeDef",
    {
        "Name": NotRequired[str],
        "MountPath": NotRequired[str],
    },
)
CreateActionTargetRequestRequestTypeDef = TypedDict(
    "CreateActionTargetRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Id": str,
    },
)
CreateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "CreateFindingAggregatorRequestRequestTypeDef",
    {
        "RegionLinkingMode": str,
        "Regions": NotRequired[Sequence[str]],
    },
)
ResultTypeDef = TypedDict(
    "ResultTypeDef",
    {
        "AccountId": NotRequired[str],
        "ProcessingResult": NotRequired[str],
    },
)
DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef",
    {
        "Value": NotRequired[int],
        "Unit": NotRequired[Literal["DAYS"]],
    },
)
DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
DeleteActionTargetRequestRequestTypeDef = TypedDict(
    "DeleteActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
    },
)
DeleteConfigurationPolicyRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationPolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
DeleteFindingAggregatorRequestRequestTypeDef = TypedDict(
    "DeleteFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)
DeleteInsightRequestRequestTypeDef = TypedDict(
    "DeleteInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)
DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
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
DescribeActionTargetsRequestRequestTypeDef = TypedDict(
    "DescribeActionTargetsRequestRequestTypeDef",
    {
        "ActionTargetArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeHubRequestRequestTypeDef = TypedDict(
    "DescribeHubRequestRequestTypeDef",
    {
        "HubArn": NotRequired[str],
    },
)
OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef",
    {
        "ConfigurationType": NotRequired[OrganizationConfigurationConfigurationTypeType],
        "Status": NotRequired[OrganizationConfigurationStatusType],
        "StatusMessage": NotRequired[str],
    },
)
DescribeProductsRequestRequestTypeDef = TypedDict(
    "DescribeProductsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ProductArn": NotRequired[str],
    },
)
ProductTypeDef = TypedDict(
    "ProductTypeDef",
    {
        "ProductArn": str,
        "ProductName": NotRequired[str],
        "CompanyName": NotRequired[str],
        "Description": NotRequired[str],
        "Categories": NotRequired[List[str]],
        "IntegrationTypes": NotRequired[List[IntegrationTypeType]],
        "MarketplaceUrl": NotRequired[str],
        "ActivationUrl": NotRequired[str],
        "ProductSubscriptionResourcePolicy": NotRequired[str],
    },
)
DescribeStandardsControlsRequestRequestTypeDef = TypedDict(
    "DescribeStandardsControlsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
StandardsControlTypeDef = TypedDict(
    "StandardsControlTypeDef",
    {
        "StandardsControlArn": NotRequired[str],
        "ControlStatus": NotRequired[ControlStatusType],
        "DisabledReason": NotRequired[str],
        "ControlStatusUpdatedAt": NotRequired[datetime],
        "ControlId": NotRequired[str],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "RemediationUrl": NotRequired[str],
        "SeverityRating": NotRequired[SeverityRatingType],
        "RelatedRequirements": NotRequired[List[str]],
    },
)
DescribeStandardsRequestRequestTypeDef = TypedDict(
    "DescribeStandardsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DisableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "DisableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductSubscriptionArn": str,
    },
)
DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)
DisassociateMembersRequestRequestTypeDef = TypedDict(
    "DisassociateMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
EnableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "EnableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductArn": str,
    },
)
EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)
EnableSecurityHubRequestRequestTypeDef = TypedDict(
    "EnableSecurityHubRequestRequestTypeDef",
    {
        "Tags": NotRequired[Mapping[str, str]],
        "EnableDefaultStandards": NotRequired[bool],
        "ControlFindingGenerator": NotRequired[ControlFindingGeneratorType],
    },
)
FilePathsTypeDef = TypedDict(
    "FilePathsTypeDef",
    {
        "FilePath": NotRequired[str],
        "FileName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Hash": NotRequired[str],
    },
)
FindingAggregatorTypeDef = TypedDict(
    "FindingAggregatorTypeDef",
    {
        "FindingAggregatorArn": NotRequired[str],
    },
)
FindingHistoryUpdateSourceTypeDef = TypedDict(
    "FindingHistoryUpdateSourceTypeDef",
    {
        "Type": NotRequired[FindingHistoryUpdateSourceTypeType],
        "Identity": NotRequired[str],
    },
)
FindingHistoryUpdateTypeDef = TypedDict(
    "FindingHistoryUpdateTypeDef",
    {
        "UpdatedField": NotRequired[str],
        "OldValue": NotRequired[str],
        "NewValue": NotRequired[str],
    },
)
FindingProviderSeverityTypeDef = TypedDict(
    "FindingProviderSeverityTypeDef",
    {
        "Label": NotRequired[SeverityLabelType],
        "Original": NotRequired[str],
    },
)
FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef = TypedDict(
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    {
        "ResourceArn": NotRequired[str],
    },
)
FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef = TypedDict(
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    {
        "Priority": NotRequired[int],
        "ResourceArn": NotRequired[str],
    },
)
GeneratorDetailsTypeDef = TypedDict(
    "GeneratorDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Labels": NotRequired[Sequence[str]],
    },
)
InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "AccountId": NotRequired[str],
        "InvitationId": NotRequired[str],
        "InvitedAt": NotRequired[datetime],
        "MemberStatus": NotRequired[str],
    },
)
GetConfigurationPolicyRequestRequestTypeDef = TypedDict(
    "GetConfigurationPolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetEnabledStandardsRequestRequestTypeDef = TypedDict(
    "GetEnabledStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetFindingAggregatorRequestRequestTypeDef = TypedDict(
    "GetFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)
TimestampTypeDef = Union[datetime, str]
SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "Field": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)
GetInsightResultsRequestRequestTypeDef = TypedDict(
    "GetInsightResultsRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)
GetInsightsRequestRequestTypeDef = TypedDict(
    "GetInsightsRequestRequestTypeDef",
    {
        "InsightArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": NotRequired[str],
        "Email": NotRequired[str],
        "MasterId": NotRequired[str],
        "AdministratorId": NotRequired[str],
        "MemberStatus": NotRequired[str],
        "InvitedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
GetSecurityControlDefinitionRequestRequestTypeDef = TypedDict(
    "GetSecurityControlDefinitionRequestRequestTypeDef",
    {
        "SecurityControlId": str,
    },
)
InsightResultValueTypeDef = TypedDict(
    "InsightResultValueTypeDef",
    {
        "GroupByAttributeValue": str,
        "Count": int,
    },
)
InviteMembersRequestRequestTypeDef = TypedDict(
    "InviteMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
ListAutomationRulesRequestRequestTypeDef = TypedDict(
    "ListAutomationRulesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListConfigurationPoliciesRequestRequestTypeDef = TypedDict(
    "ListConfigurationPoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEnabledProductsForImportRequestRequestTypeDef = TypedDict(
    "ListEnabledProductsForImportRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFindingAggregatorsRequestRequestTypeDef = TypedDict(
    "ListFindingAggregatorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "OnlyAssociated": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSecurityControlDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSecurityControlDefinitionsRequestRequestTypeDef",
    {
        "StandardsArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "ListStandardsControlAssociationsRequestRequestTypeDef",
    {
        "SecurityControlId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
StandardsControlAssociationSummaryTypeDef = TypedDict(
    "StandardsControlAssociationSummaryTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "AssociationStatus": AssociationStatusType,
        "RelatedRequirements": NotRequired[List[str]],
        "UpdatedAt": NotRequired[datetime],
        "UpdatedReason": NotRequired[str],
        "StandardsControlTitle": NotRequired[str],
        "StandardsControlDescription": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "Begin": NotRequired[int],
        "End": NotRequired[int],
    },
)
RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "Start": NotRequired[int],
        "End": NotRequired[int],
        "StartColumn": NotRequired[int],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "JsonPath": NotRequired[str],
        "RecordIndex": NotRequired[int],
    },
)
ParameterValueOutputTypeDef = TypedDict(
    "ParameterValueOutputTypeDef",
    {
        "Integer": NotRequired[int],
        "IntegerList": NotRequired[List[int]],
        "Double": NotRequired[float],
        "String": NotRequired[str],
        "StringList": NotRequired[List[str]],
        "Boolean": NotRequired[bool],
        "Enum": NotRequired[str],
        "EnumList": NotRequired[List[str]],
    },
)
ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "Integer": NotRequired[int],
        "IntegerList": NotRequired[Sequence[int]],
        "Double": NotRequired[float],
        "String": NotRequired[str],
        "StringList": NotRequired[Sequence[str]],
        "Boolean": NotRequired[bool],
        "Enum": NotRequired[str],
        "EnumList": NotRequired[Sequence[str]],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Text": NotRequired[str],
        "Url": NotRequired[str],
    },
)
RuleGroupSourceListDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceListDetailsOutputTypeDef",
    {
        "GeneratedRulesType": NotRequired[str],
        "TargetTypes": NotRequired[List[str]],
        "Targets": NotRequired[List[str]],
    },
)
RuleGroupSourceListDetailsTypeDef = TypedDict(
    "RuleGroupSourceListDetailsTypeDef",
    {
        "GeneratedRulesType": NotRequired[str],
        "TargetTypes": NotRequired[Sequence[str]],
        "Targets": NotRequired[Sequence[str]],
    },
)
RuleGroupSourceStatefulRulesHeaderDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    {
        "Destination": NotRequired[str],
        "DestinationPort": NotRequired[str],
        "Direction": NotRequired[str],
        "Protocol": NotRequired[str],
        "Source": NotRequired[str],
        "SourcePort": NotRequired[str],
    },
)
RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef",
    {
        "Keyword": NotRequired[str],
        "Settings": NotRequired[List[str]],
    },
)
RuleGroupSourceStatefulRulesOptionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    {
        "Keyword": NotRequired[str],
        "Settings": NotRequired[Sequence[str]],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    {
        "AddressDefinition": NotRequired[str],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    {
        "AddressDefinition": NotRequired[str],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef",
    {
        "Flags": NotRequired[List[str]],
        "Masks": NotRequired[List[str]],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    {
        "Flags": NotRequired[Sequence[str]],
        "Masks": NotRequired[Sequence[str]],
    },
)
RuleGroupVariablesIpSetsDetailsOutputTypeDef = TypedDict(
    "RuleGroupVariablesIpSetsDetailsOutputTypeDef",
    {
        "Definition": NotRequired[List[str]],
    },
)
RuleGroupVariablesIpSetsDetailsTypeDef = TypedDict(
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    {
        "Definition": NotRequired[Sequence[str]],
    },
)
RuleGroupVariablesPortSetsDetailsOutputTypeDef = TypedDict(
    "RuleGroupVariablesPortSetsDetailsOutputTypeDef",
    {
        "Definition": NotRequired[List[str]],
    },
)
RuleGroupVariablesPortSetsDetailsTypeDef = TypedDict(
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    {
        "Definition": NotRequired[Sequence[str]],
    },
)
SecurityControlParameterTypeDef = TypedDict(
    "SecurityControlParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[Sequence[str]],
    },
)
SoftwarePackageTypeDef = TypedDict(
    "SoftwarePackageTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "Epoch": NotRequired[str],
        "Release": NotRequired[str],
        "Architecture": NotRequired[str],
        "PackageManager": NotRequired[str],
        "FilePath": NotRequired[str],
        "FixedInVersion": NotRequired[str],
        "Remediation": NotRequired[str],
        "SourceLayerHash": NotRequired[str],
        "SourceLayerArn": NotRequired[str],
    },
)
StandardsManagedByTypeDef = TypedDict(
    "StandardsManagedByTypeDef",
    {
        "Company": NotRequired[str],
        "Product": NotRequired[str],
    },
)
StandardsStatusReasonTypeDef = TypedDict(
    "StandardsStatusReasonTypeDef",
    {
        "StatusReasonCode": StatusReasonCodeType,
    },
)
StatelessCustomPublishMetricActionDimensionTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    {
        "Value": NotRequired[str],
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
UpdateActionTargetRequestRequestTypeDef = TypedDict(
    "UpdateActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "UpdateFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
        "RegionLinkingMode": str,
        "Regions": NotRequired[Sequence[str]],
    },
)
UpdateSecurityHubConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    {
        "AutoEnableControls": NotRequired[bool],
        "ControlFindingGenerator": NotRequired[ControlFindingGeneratorType],
    },
)
UpdateStandardsControlRequestRequestTypeDef = TypedDict(
    "UpdateStandardsControlRequestRequestTypeDef",
    {
        "StandardsControlArn": str,
        "ControlStatus": NotRequired[ControlStatusType],
        "DisabledReason": NotRequired[str],
    },
)
VulnerabilityVendorTypeDef = TypedDict(
    "VulnerabilityVendorTypeDef",
    {
        "Name": str,
        "Url": NotRequired[str],
        "VendorSeverity": NotRequired[str],
        "VendorCreatedAt": NotRequired[str],
        "VendorUpdatedAt": NotRequired[str],
    },
)
CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "AccountDetails": Sequence[AccountDetailsTypeDef],
    },
)
ActionRemoteIpDetailsTypeDef = TypedDict(
    "ActionRemoteIpDetailsTypeDef",
    {
        "IpAddressV4": NotRequired[str],
        "Organization": NotRequired[IpOrganizationDetailsTypeDef],
        "Country": NotRequired[CountryTypeDef],
        "City": NotRequired[CityTypeDef],
        "GeoLocation": NotRequired[GeoLocationTypeDef],
    },
)
CvssOutputTypeDef = TypedDict(
    "CvssOutputTypeDef",
    {
        "Version": NotRequired[str],
        "BaseScore": NotRequired[float],
        "BaseVector": NotRequired[str],
        "Source": NotRequired[str],
        "Adjustments": NotRequired[List[AdjustmentTypeDef]],
    },
)
CvssTypeDef = TypedDict(
    "CvssTypeDef",
    {
        "Version": NotRequired[str],
        "BaseScore": NotRequired[float],
        "BaseVector": NotRequired[str],
        "Source": NotRequired[str],
        "Adjustments": NotRequired[Sequence[AdjustmentTypeDef]],
    },
)
ListConfigurationPolicyAssociationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationPolicyAssociationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[AssociationFiltersTypeDef],
    },
)
AssociationSetDetailsTypeDef = TypedDict(
    "AssociationSetDetailsTypeDef",
    {
        "AssociationState": NotRequired[AssociationStateDetailsTypeDef],
        "GatewayId": NotRequired[str],
        "Main": NotRequired[bool],
        "RouteTableAssociationId": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)
AutomationRulesFindingFieldsUpdateOutputTypeDef = TypedDict(
    "AutomationRulesFindingFieldsUpdateOutputTypeDef",
    {
        "Note": NotRequired[NoteUpdateTypeDef],
        "Severity": NotRequired[SeverityUpdateTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Types": NotRequired[List[str]],
        "UserDefinedFields": NotRequired[Dict[str, str]],
        "Workflow": NotRequired[WorkflowUpdateTypeDef],
        "RelatedFindings": NotRequired[List[RelatedFindingTypeDef]],
    },
)
AutomationRulesFindingFieldsUpdateTypeDef = TypedDict(
    "AutomationRulesFindingFieldsUpdateTypeDef",
    {
        "Note": NotRequired[NoteUpdateTypeDef],
        "Severity": NotRequired[SeverityUpdateTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Types": NotRequired[Sequence[str]],
        "UserDefinedFields": NotRequired[Mapping[str, str]],
        "Workflow": NotRequired[WorkflowUpdateTypeDef],
        "RelatedFindings": NotRequired[Sequence[RelatedFindingTypeDef]],
    },
)
AwsAmazonMqBrokerLdapServerMetadataDetailsUnionTypeDef = Union[
    AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef,
    AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef,
]
AwsAmazonMqBrokerLogsDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLogsDetailsTypeDef",
    {
        "Audit": NotRequired[bool],
        "General": NotRequired[bool],
        "AuditLogGroup": NotRequired[str],
        "GeneralLogGroup": NotRequired[str],
        "Pending": NotRequired[AwsAmazonMqBrokerLogsPendingDetailsTypeDef],
    },
)
AwsApiGatewayCanarySettingsUnionTypeDef = Union[
    AwsApiGatewayCanarySettingsTypeDef, AwsApiGatewayCanarySettingsOutputTypeDef
]
AwsApiGatewayRestApiDetailsOutputTypeDef = TypedDict(
    "AwsApiGatewayRestApiDetailsOutputTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Version": NotRequired[str],
        "BinaryMediaTypes": NotRequired[List[str]],
        "MinimumCompressionSize": NotRequired[int],
        "ApiKeySource": NotRequired[str],
        "EndpointConfiguration": NotRequired[AwsApiGatewayEndpointConfigurationOutputTypeDef],
    },
)
AwsApiGatewayEndpointConfigurationUnionTypeDef = Union[
    AwsApiGatewayEndpointConfigurationTypeDef, AwsApiGatewayEndpointConfigurationOutputTypeDef
]
AwsApiGatewayStageDetailsOutputTypeDef = TypedDict(
    "AwsApiGatewayStageDetailsOutputTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "ClientCertificateId": NotRequired[str],
        "StageName": NotRequired[str],
        "Description": NotRequired[str],
        "CacheClusterEnabled": NotRequired[bool],
        "CacheClusterSize": NotRequired[str],
        "CacheClusterStatus": NotRequired[str],
        "MethodSettings": NotRequired[List[AwsApiGatewayMethodSettingsTypeDef]],
        "Variables": NotRequired[Dict[str, str]],
        "DocumentationVersion": NotRequired[str],
        "AccessLogSettings": NotRequired[AwsApiGatewayAccessLogSettingsTypeDef],
        "CanarySettings": NotRequired[AwsApiGatewayCanarySettingsOutputTypeDef],
        "TracingEnabled": NotRequired[bool],
        "CreatedDate": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "WebAclArn": NotRequired[str],
    },
)
AwsApiGatewayV2ApiDetailsOutputTypeDef = TypedDict(
    "AwsApiGatewayV2ApiDetailsOutputTypeDef",
    {
        "ApiEndpoint": NotRequired[str],
        "ApiId": NotRequired[str],
        "ApiKeySelectionExpression": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "Version": NotRequired[str],
        "Name": NotRequired[str],
        "ProtocolType": NotRequired[str],
        "RouteSelectionExpression": NotRequired[str],
        "CorsConfiguration": NotRequired[AwsCorsConfigurationOutputTypeDef],
    },
)
AwsApiGatewayV2StageDetailsOutputTypeDef = TypedDict(
    "AwsApiGatewayV2StageDetailsOutputTypeDef",
    {
        "ClientCertificateId": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteSettings": NotRequired[AwsApiGatewayV2RouteSettingsTypeDef],
        "DeploymentId": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "RouteSettings": NotRequired[AwsApiGatewayV2RouteSettingsTypeDef],
        "StageName": NotRequired[str],
        "StageVariables": NotRequired[Dict[str, str]],
        "AccessLogSettings": NotRequired[AwsApiGatewayAccessLogSettingsTypeDef],
        "AutoDeploy": NotRequired[bool],
        "LastDeploymentStatusMessage": NotRequired[str],
        "ApiGatewayManaged": NotRequired[bool],
    },
)
AwsApiGatewayV2StageDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2StageDetailsTypeDef",
    {
        "ClientCertificateId": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteSettings": NotRequired[AwsApiGatewayV2RouteSettingsTypeDef],
        "DeploymentId": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "RouteSettings": NotRequired[AwsApiGatewayV2RouteSettingsTypeDef],
        "StageName": NotRequired[str],
        "StageVariables": NotRequired[Mapping[str, str]],
        "AccessLogSettings": NotRequired[AwsApiGatewayAccessLogSettingsTypeDef],
        "AutoDeploy": NotRequired[bool],
        "LastDeploymentStatusMessage": NotRequired[str],
        "ApiGatewayManaged": NotRequired[bool],
    },
)
AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef",
    {
        "AuthenticationType": NotRequired[str],
        "LambdaAuthorizerConfig": NotRequired[
            AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef
        ],
        "OpenIdConnectConfig": NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef],
        "UserPoolConfig": NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef],
    },
)
AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef",
    {
        "EncryptionConfiguration": NotRequired[
            AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef
        ],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
        ],
        "Overrides": NotRequired[
            List[
                AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef
            ]
        ],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
        ],
        "Overrides": NotRequired[
            Sequence[
                AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef
            ]
        ],
    },
)
AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef],
        "NoDevice": NotRequired[bool],
        "VirtualName": NotRequired[str],
    },
)
AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnionTypeDef = Union[
    AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef,
    AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef,
]
AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef",
    {
        "DestinationBackupVaultArn": NotRequired[str],
        "Lifecycle": NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef],
    },
)
AwsBackupBackupVaultDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupVaultDetailsOutputTypeDef",
    {
        "BackupVaultArn": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "Notifications": NotRequired[AwsBackupBackupVaultNotificationsDetailsOutputTypeDef],
        "AccessPolicy": NotRequired[str],
    },
)
AwsBackupBackupVaultNotificationsDetailsUnionTypeDef = Union[
    AwsBackupBackupVaultNotificationsDetailsTypeDef,
    AwsBackupBackupVaultNotificationsDetailsOutputTypeDef,
]
AwsBackupRecoveryPointDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointDetailsTypeDef",
    {
        "BackupSizeInBytes": NotRequired[int],
        "BackupVaultArn": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "CalculatedLifecycle": NotRequired[AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef],
        "CompletionDate": NotRequired[str],
        "CreatedBy": NotRequired[AwsBackupRecoveryPointCreatedByDetailsTypeDef],
        "CreationDate": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "IamRoleArn": NotRequired[str],
        "IsEncrypted": NotRequired[bool],
        "LastRestoreTime": NotRequired[str],
        "Lifecycle": NotRequired[AwsBackupRecoveryPointLifecycleDetailsTypeDef],
        "RecoveryPointArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "SourceBackupVaultArn": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "StorageClass": NotRequired[str],
    },
)
AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef",
    {
        "DomainName": NotRequired[str],
        "ResourceRecord": NotRequired[AwsCertificateManagerCertificateResourceRecordTypeDef],
        "ValidationDomain": NotRequired[str],
        "ValidationEmails": NotRequired[List[str]],
        "ValidationMethod": NotRequired[str],
        "ValidationStatus": NotRequired[str],
    },
)
AwsCertificateManagerCertificateDomainValidationOptionTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    {
        "DomainName": NotRequired[str],
        "ResourceRecord": NotRequired[AwsCertificateManagerCertificateResourceRecordTypeDef],
        "ValidationDomain": NotRequired[str],
        "ValidationEmails": NotRequired[Sequence[str]],
        "ValidationMethod": NotRequired[str],
        "ValidationStatus": NotRequired[str],
    },
)
AwsCloudFormationStackDetailsOutputTypeDef = TypedDict(
    "AwsCloudFormationStackDetailsOutputTypeDef",
    {
        "Capabilities": NotRequired[List[str]],
        "CreationTime": NotRequired[str],
        "Description": NotRequired[str],
        "DisableRollback": NotRequired[bool],
        "DriftInformation": NotRequired[AwsCloudFormationStackDriftInformationDetailsTypeDef],
        "EnableTerminationProtection": NotRequired[bool],
        "LastUpdatedTime": NotRequired[str],
        "NotificationArns": NotRequired[List[str]],
        "Outputs": NotRequired[List[AwsCloudFormationStackOutputsDetailsTypeDef]],
        "RoleArn": NotRequired[str],
        "StackId": NotRequired[str],
        "StackName": NotRequired[str],
        "StackStatus": NotRequired[str],
        "StackStatusReason": NotRequired[str],
        "TimeoutInMinutes": NotRequired[int],
    },
)
AwsCloudFormationStackDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackDetailsTypeDef",
    {
        "Capabilities": NotRequired[Sequence[str]],
        "CreationTime": NotRequired[str],
        "Description": NotRequired[str],
        "DisableRollback": NotRequired[bool],
        "DriftInformation": NotRequired[AwsCloudFormationStackDriftInformationDetailsTypeDef],
        "EnableTerminationProtection": NotRequired[bool],
        "LastUpdatedTime": NotRequired[str],
        "NotificationArns": NotRequired[Sequence[str]],
        "Outputs": NotRequired[Sequence[AwsCloudFormationStackOutputsDetailsTypeDef]],
        "RoleArn": NotRequired[str],
        "StackId": NotRequired[str],
        "StackName": NotRequired[str],
        "StackStatus": NotRequired[str],
        "StackStatusReason": NotRequired[str],
        "TimeoutInMinutes": NotRequired[int],
    },
)
AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef",
    {
        "Items": NotRequired[List[AwsCloudFrontDistributionCacheBehaviorTypeDef]],
    },
)
AwsCloudFrontDistributionCacheBehaviorsTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    {
        "Items": NotRequired[Sequence[AwsCloudFrontDistributionCacheBehaviorTypeDef]],
    },
)
AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef",
    {
        "HttpPort": NotRequired[int],
        "HttpsPort": NotRequired[int],
        "OriginKeepaliveTimeout": NotRequired[int],
        "OriginProtocolPolicy": NotRequired[str],
        "OriginReadTimeout": NotRequired[int],
        "OriginSslProtocols": NotRequired[AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef",
    {
        "StatusCodes": NotRequired[
            AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef
        ],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef,
    AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef,
]
AwsCloudFrontDistributionOriginSslProtocolsUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginSslProtocolsTypeDef,
    AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef,
]
AwsCloudWatchAlarmDetailsOutputTypeDef = TypedDict(
    "AwsCloudWatchAlarmDetailsOutputTypeDef",
    {
        "ActionsEnabled": NotRequired[bool],
        "AlarmActions": NotRequired[List[str]],
        "AlarmArn": NotRequired[str],
        "AlarmConfigurationUpdatedTimestamp": NotRequired[str],
        "AlarmDescription": NotRequired[str],
        "AlarmName": NotRequired[str],
        "ComparisonOperator": NotRequired[str],
        "DatapointsToAlarm": NotRequired[int],
        "Dimensions": NotRequired[List[AwsCloudWatchAlarmDimensionsDetailsTypeDef]],
        "EvaluateLowSampleCountPercentile": NotRequired[str],
        "EvaluationPeriods": NotRequired[int],
        "ExtendedStatistic": NotRequired[str],
        "InsufficientDataActions": NotRequired[List[str]],
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "OkActions": NotRequired[List[str]],
        "Period": NotRequired[int],
        "Statistic": NotRequired[str],
        "Threshold": NotRequired[float],
        "ThresholdMetricId": NotRequired[str],
        "TreatMissingData": NotRequired[str],
        "Unit": NotRequired[str],
    },
)
AwsCloudWatchAlarmDetailsTypeDef = TypedDict(
    "AwsCloudWatchAlarmDetailsTypeDef",
    {
        "ActionsEnabled": NotRequired[bool],
        "AlarmActions": NotRequired[Sequence[str]],
        "AlarmArn": NotRequired[str],
        "AlarmConfigurationUpdatedTimestamp": NotRequired[str],
        "AlarmDescription": NotRequired[str],
        "AlarmName": NotRequired[str],
        "ComparisonOperator": NotRequired[str],
        "DatapointsToAlarm": NotRequired[int],
        "Dimensions": NotRequired[Sequence[AwsCloudWatchAlarmDimensionsDetailsTypeDef]],
        "EvaluateLowSampleCountPercentile": NotRequired[str],
        "EvaluationPeriods": NotRequired[int],
        "ExtendedStatistic": NotRequired[str],
        "InsufficientDataActions": NotRequired[Sequence[str]],
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "OkActions": NotRequired[Sequence[str]],
        "Period": NotRequired[int],
        "Statistic": NotRequired[str],
        "Threshold": NotRequired[float],
        "ThresholdMetricId": NotRequired[str],
        "TreatMissingData": NotRequired[str],
        "Unit": NotRequired[str],
    },
)
AwsCodeBuildProjectEnvironmentOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentOutputTypeDef",
    {
        "Certificate": NotRequired[str],
        "EnvironmentVariables": NotRequired[
            List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]
        ],
        "PrivilegedMode": NotRequired[bool],
        "ImagePullCredentialsType": NotRequired[str],
        "RegistryCredential": NotRequired[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef],
        "Type": NotRequired[str],
    },
)
AwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": NotRequired[str],
        "EnvironmentVariables": NotRequired[
            Sequence[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]
        ],
        "PrivilegedMode": NotRequired[bool],
        "ImagePullCredentialsType": NotRequired[str],
        "RegistryCredential": NotRequired[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef],
        "Type": NotRequired[str],
    },
)
AwsCodeBuildProjectLogsConfigDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    {
        "CloudWatchLogs": NotRequired[AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef],
        "S3Logs": NotRequired[AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef],
    },
)
AwsCodeBuildProjectVpcConfigUnionTypeDef = Union[
    AwsCodeBuildProjectVpcConfigTypeDef, AwsCodeBuildProjectVpcConfigOutputTypeDef
]
AwsCorsConfigurationUnionTypeDef = Union[
    AwsCorsConfigurationTypeDef, AwsCorsConfigurationOutputTypeDef
]
AwsDmsReplicationInstanceDetailsOutputTypeDef = TypedDict(
    "AwsDmsReplicationInstanceDetailsOutputTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ReplicationInstanceClass": NotRequired[str],
        "ReplicationInstanceIdentifier": NotRequired[str],
        "ReplicationSubnetGroup": NotRequired[
            AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef
        ],
        "VpcSecurityGroups": NotRequired[
            List[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]
        ],
    },
)
AwsDmsReplicationInstanceDetailsTypeDef = TypedDict(
    "AwsDmsReplicationInstanceDetailsTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ReplicationInstanceClass": NotRequired[str],
        "ReplicationInstanceIdentifier": NotRequired[str],
        "ReplicationSubnetGroup": NotRequired[
            AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef
        ],
        "VpcSecurityGroups": NotRequired[
            Sequence[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]
        ],
    },
)
AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef = TypedDict(
    "AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef",
    {
        "Backfilling": NotRequired[bool],
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "IndexSizeBytes": NotRequired[int],
        "IndexStatus": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]],
        "Projection": NotRequired[AwsDynamoDbTableProjectionOutputTypeDef],
        "ProvisionedThroughput": NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef],
    },
)
AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef = TypedDict(
    "AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef",
    {
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]],
        "Projection": NotRequired[AwsDynamoDbTableProjectionOutputTypeDef],
    },
)
AwsDynamoDbTableProjectionUnionTypeDef = Union[
    AwsDynamoDbTableProjectionTypeDef, AwsDynamoDbTableProjectionOutputTypeDef
]
AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
        ],
    },
)
AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "ActiveDirectory": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef
        ],
        "MutualAuthentication": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef
        ],
        "FederatedAuthentication": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef
        ],
    },
)
AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LambdaFunctionArn": NotRequired[str],
        "Status": NotRequired[AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef],
    },
)
AwsEc2InstanceDetailsOutputTypeDef = TypedDict(
    "AwsEc2InstanceDetailsOutputTypeDef",
    {
        "Type": NotRequired[str],
        "ImageId": NotRequired[str],
        "IpV4Addresses": NotRequired[List[str]],
        "IpV6Addresses": NotRequired[List[str]],
        "KeyName": NotRequired[str],
        "IamInstanceProfileArn": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "NetworkInterfaces": NotRequired[List[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]],
        "VirtualizationType": NotRequired[str],
        "MetadataOptions": NotRequired[AwsEc2InstanceMetadataOptionsTypeDef],
        "Monitoring": NotRequired[AwsEc2InstanceMonitoringDetailsTypeDef],
    },
)
AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "ImageId": NotRequired[str],
        "IpV4Addresses": NotRequired[Sequence[str]],
        "IpV6Addresses": NotRequired[Sequence[str]],
        "KeyName": NotRequired[str],
        "IamInstanceProfileArn": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "NetworkInterfaces": NotRequired[Sequence[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]],
        "VirtualizationType": NotRequired[str],
        "MetadataOptions": NotRequired[AwsEc2InstanceMetadataOptionsTypeDef],
        "Monitoring": NotRequired[AwsEc2InstanceMonitoringDetailsTypeDef],
    },
)
AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired[AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef],
        "NoDevice": NotRequired[str],
        "VirtualName": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef",
    {
        "CapacityReservationPreference": NotRequired[str],
        "CapacityReservationTarget": NotRequired[
            AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef",
    {
        "MarketType": NotRequired[str],
        "SpotOptions": NotRequired[
            AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef",
    {
        "AcceleratorCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef
        ],
        "AcceleratorManufacturers": NotRequired[List[str]],
        "AcceleratorNames": NotRequired[List[str]],
        "AcceleratorTotalMemoryMiB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef
        ],
        "AcceleratorTypes": NotRequired[List[str]],
        "BareMetal": NotRequired[str],
        "BaselineEbsBandwidthMbps": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef
        ],
        "BurstablePerformance": NotRequired[str],
        "CpuManufacturers": NotRequired[List[str]],
        "ExcludedInstanceTypes": NotRequired[List[str]],
        "InstanceGenerations": NotRequired[List[str]],
        "LocalStorage": NotRequired[str],
        "LocalStorageTypes": NotRequired[List[str]],
        "MemoryGiBPerVCpu": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef
        ],
        "MemoryMiB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef
        ],
        "NetworkInterfaceCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef
        ],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "RequireHibernateSupport": NotRequired[bool],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "TotalLocalStorageGB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef
        ],
        "VCpuCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef",
    {
        "AcceleratorCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef
        ],
        "AcceleratorManufacturers": NotRequired[Sequence[str]],
        "AcceleratorNames": NotRequired[Sequence[str]],
        "AcceleratorTotalMemoryMiB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef
        ],
        "AcceleratorTypes": NotRequired[Sequence[str]],
        "BareMetal": NotRequired[str],
        "BaselineEbsBandwidthMbps": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef
        ],
        "BurstablePerformance": NotRequired[str],
        "CpuManufacturers": NotRequired[Sequence[str]],
        "ExcludedInstanceTypes": NotRequired[Sequence[str]],
        "InstanceGenerations": NotRequired[Sequence[str]],
        "LocalStorage": NotRequired[str],
        "LocalStorageTypes": NotRequired[Sequence[str]],
        "MemoryGiBPerVCpu": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef
        ],
        "MemoryMiB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef
        ],
        "NetworkInterfaceCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef
        ],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "RequireHibernateSupport": NotRequired[bool],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "TotalLocalStorageGB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef
        ],
        "VCpuCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef",
    {
        "AssociateCarrierIpAddress": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[List[str]],
        "InterfaceType": NotRequired[str],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]
        ],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]
        ],
        "Ipv6PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]
        ],
        "NetworkCardIndex": NotRequired[int],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]
        ],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef",
    {
        "AssociateCarrierIpAddress": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[Sequence[str]],
        "InterfaceType": NotRequired[str],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]
        ],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]
        ],
        "Ipv6PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]
        ],
        "NetworkCardIndex": NotRequired[int],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]
        ],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
    },
)
AwsEc2NetworkAclEntryTypeDef = TypedDict(
    "AwsEc2NetworkAclEntryTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "Egress": NotRequired[bool],
        "IcmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired[PortRangeFromToTypeDef],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[str],
        "RuleNumber": NotRequired[int],
    },
)
AwsEc2NetworkInterfaceDetailsOutputTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsOutputTypeDef",
    {
        "Attachment": NotRequired[AwsEc2NetworkInterfaceAttachmentTypeDef],
        "NetworkInterfaceId": NotRequired[str],
        "SecurityGroups": NotRequired[List[AwsEc2NetworkInterfaceSecurityGroupTypeDef]],
        "SourceDestCheck": NotRequired[bool],
        "IpV6Addresses": NotRequired[List[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]],
        "PrivateIpAddresses": NotRequired[
            List[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]
        ],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
    },
)
AwsEc2NetworkInterfaceDetailsTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    {
        "Attachment": NotRequired[AwsEc2NetworkInterfaceAttachmentTypeDef],
        "NetworkInterfaceId": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[AwsEc2NetworkInterfaceSecurityGroupTypeDef]],
        "SourceDestCheck": NotRequired[bool],
        "IpV6Addresses": NotRequired[Sequence[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]],
        "PrivateIpAddresses": NotRequired[
            Sequence[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]
        ],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
    },
)
AwsEc2SecurityGroupIpPermissionOutputTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionOutputTypeDef",
    {
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[List[AwsEc2SecurityGroupUserIdGroupPairTypeDef]],
        "IpRanges": NotRequired[List[AwsEc2SecurityGroupIpRangeTypeDef]],
        "Ipv6Ranges": NotRequired[List[AwsEc2SecurityGroupIpv6RangeTypeDef]],
        "PrefixListIds": NotRequired[List[AwsEc2SecurityGroupPrefixListIdTypeDef]],
    },
)
AwsEc2SecurityGroupIpPermissionTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    {
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[Sequence[AwsEc2SecurityGroupUserIdGroupPairTypeDef]],
        "IpRanges": NotRequired[Sequence[AwsEc2SecurityGroupIpRangeTypeDef]],
        "Ipv6Ranges": NotRequired[Sequence[AwsEc2SecurityGroupIpv6RangeTypeDef]],
        "PrefixListIds": NotRequired[Sequence[AwsEc2SecurityGroupPrefixListIdTypeDef]],
    },
)
AwsEc2SubnetDetailsOutputTypeDef = TypedDict(
    "AwsEc2SubnetDetailsOutputTypeDef",
    {
        "AssignIpv6AddressOnCreation": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailableIpAddressCount": NotRequired[int],
        "CidrBlock": NotRequired[str],
        "DefaultForAz": NotRequired[bool],
        "MapPublicIpOnLaunch": NotRequired[bool],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "SubnetArn": NotRequired[str],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Ipv6CidrBlockAssociationSet": NotRequired[List[Ipv6CidrBlockAssociationTypeDef]],
    },
)
AwsEc2SubnetDetailsTypeDef = TypedDict(
    "AwsEc2SubnetDetailsTypeDef",
    {
        "AssignIpv6AddressOnCreation": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailableIpAddressCount": NotRequired[int],
        "CidrBlock": NotRequired[str],
        "DefaultForAz": NotRequired[bool],
        "MapPublicIpOnLaunch": NotRequired[bool],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "SubnetArn": NotRequired[str],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Ipv6CidrBlockAssociationSet": NotRequired[Sequence[Ipv6CidrBlockAssociationTypeDef]],
    },
)
AwsEc2TransitGatewayDetailsUnionTypeDef = Union[
    AwsEc2TransitGatewayDetailsTypeDef, AwsEc2TransitGatewayDetailsOutputTypeDef
]
AwsEc2VolumeDetailsOutputTypeDef = TypedDict(
    "AwsEc2VolumeDetailsOutputTypeDef",
    {
        "CreateTime": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Attachments": NotRequired[List[AwsEc2VolumeAttachmentTypeDef]],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeScanStatus": NotRequired[str],
    },
)
AwsEc2VolumeDetailsTypeDef = TypedDict(
    "AwsEc2VolumeDetailsTypeDef",
    {
        "CreateTime": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Attachments": NotRequired[Sequence[AwsEc2VolumeAttachmentTypeDef]],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeScanStatus": NotRequired[str],
    },
)
AwsEc2VpcDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcDetailsOutputTypeDef",
    {
        "CidrBlockAssociationSet": NotRequired[List[CidrBlockAssociationTypeDef]],
        "Ipv6CidrBlockAssociationSet": NotRequired[List[Ipv6CidrBlockAssociationTypeDef]],
        "DhcpOptionsId": NotRequired[str],
        "State": NotRequired[str],
    },
)
AwsEc2VpcDetailsTypeDef = TypedDict(
    "AwsEc2VpcDetailsTypeDef",
    {
        "CidrBlockAssociationSet": NotRequired[Sequence[CidrBlockAssociationTypeDef]],
        "Ipv6CidrBlockAssociationSet": NotRequired[Sequence[Ipv6CidrBlockAssociationTypeDef]],
        "DhcpOptionsId": NotRequired[str],
        "State": NotRequired[str],
    },
)
AwsEc2VpcEndpointServiceDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsOutputTypeDef",
    {
        "AcceptanceRequired": NotRequired[bool],
        "AvailabilityZones": NotRequired[List[str]],
        "BaseEndpointDnsNames": NotRequired[List[str]],
        "ManagesVpcEndpoints": NotRequired[bool],
        "GatewayLoadBalancerArns": NotRequired[List[str]],
        "NetworkLoadBalancerArns": NotRequired[List[str]],
        "PrivateDnsName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[str],
        "ServiceType": NotRequired[List[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]],
    },
)
AwsEc2VpcEndpointServiceDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    {
        "AcceptanceRequired": NotRequired[bool],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BaseEndpointDnsNames": NotRequired[Sequence[str]],
        "ManagesVpcEndpoints": NotRequired[bool],
        "GatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "NetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "PrivateDnsName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[str],
        "ServiceType": NotRequired[Sequence[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]],
    },
)
AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "CidrBlockSet": NotRequired[List[VpcInfoCidrBlockSetDetailsTypeDef]],
        "Ipv6CidrBlockSet": NotRequired[List[VpcInfoIpv6CidrBlockSetDetailsTypeDef]],
        "OwnerId": NotRequired[str],
        "PeeringOptions": NotRequired[VpcInfoPeeringOptionsDetailsTypeDef],
        "Region": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "CidrBlockSet": NotRequired[Sequence[VpcInfoCidrBlockSetDetailsTypeDef]],
        "Ipv6CidrBlockSet": NotRequired[Sequence[VpcInfoIpv6CidrBlockSetDetailsTypeDef]],
        "OwnerId": NotRequired[str],
        "PeeringOptions": NotRequired[VpcInfoPeeringOptionsDetailsTypeDef],
        "Region": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
AwsEc2VpnConnectionOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsDetailsOutputTypeDef",
    {
        "StaticRoutesOnly": NotRequired[bool],
        "TunnelOptions": NotRequired[
            List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef]
        ],
    },
)
AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnionTypeDef = Union[
    AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef,
    AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef,
]
AwsEcrContainerImageDetailsUnionTypeDef = Union[
    AwsEcrContainerImageDetailsTypeDef, AwsEcrContainerImageDetailsOutputTypeDef
]
AwsEcrRepositoryDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "ImageScanningConfiguration": NotRequired[
            AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef
        ],
        "ImageTagMutability": NotRequired[str],
        "LifecyclePolicy": NotRequired[AwsEcrRepositoryLifecyclePolicyDetailsTypeDef],
        "RepositoryName": NotRequired[str],
        "RepositoryPolicyText": NotRequired[str],
    },
)
AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    {
        "KmsKeyId": NotRequired[str],
        "LogConfiguration": NotRequired[
            AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef
        ],
        "Logging": NotRequired[str],
    },
)
AwsEcsContainerDetailsOutputTypeDef = TypedDict(
    "AwsEcsContainerDetailsOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Image": NotRequired[str],
        "MountPoints": NotRequired[List[AwsMountPointTypeDef]],
        "Privileged": NotRequired[bool],
    },
)
AwsEcsContainerDetailsTypeDef = TypedDict(
    "AwsEcsContainerDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Image": NotRequired[str],
        "MountPoints": NotRequired[Sequence[AwsMountPointTypeDef]],
        "Privileged": NotRequired[bool],
    },
)
AwsEcsServiceDeploymentConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    {
        "DeploymentCircuitBreaker": NotRequired[
            AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef
        ],
        "MaximumPercent": NotRequired[int],
        "MinimumHealthyPercent": NotRequired[int],
    },
)
AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef",
    {
        "AwsVpcConfiguration": NotRequired[
            AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef
        ],
    },
)
AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnionTypeDef = Union[
    AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef,
    AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef",
    {
        "Capabilities": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef
        ],
        "Devices": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef]
        ],
        "InitProcessEnabled": NotRequired[bool],
        "MaxSwap": NotRequired[int],
        "SharedMemorySize": NotRequired[int],
        "Swappiness": NotRequired[int],
        "Tmpfs": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef]
        ],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef",
    {
        "LogDriver": NotRequired[str],
        "Options": NotRequired[Dict[str, str]],
        "SecretOptions": NotRequired[
            List[
                AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef
            ]
        ],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    {
        "LogDriver": NotRequired[str],
        "Options": NotRequired[Mapping[str, str]],
        "SecretOptions": NotRequired[
            Sequence[
                AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef
            ]
        ],
    },
)
AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ProxyConfigurationProperties": NotRequired[
            List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]
        ],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ProxyConfigurationProperties": NotRequired[
            Sequence[
                AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef
            ]
        ],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef,
    AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    {
        "AuthorizationConfig": NotRequired[
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef
        ],
        "FilesystemId": NotRequired[str],
        "RootDirectory": NotRequired[str],
        "TransitEncryption": NotRequired[str],
        "TransitEncryptionPort": NotRequired[int],
    },
)
AwsEcsTaskVolumeDetailsTypeDef = TypedDict(
    "AwsEcsTaskVolumeDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Host": NotRequired[AwsEcsTaskVolumeHostDetailsTypeDef],
    },
)
AwsEfsAccessPointPosixUserDetailsUnionTypeDef = Union[
    AwsEfsAccessPointPosixUserDetailsTypeDef, AwsEfsAccessPointPosixUserDetailsOutputTypeDef
]
AwsEfsAccessPointRootDirectoryDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointRootDirectoryDetailsTypeDef",
    {
        "CreationInfo": NotRequired[AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef],
        "Path": NotRequired[str],
    },
)
AwsEksClusterLoggingDetailsOutputTypeDef = TypedDict(
    "AwsEksClusterLoggingDetailsOutputTypeDef",
    {
        "ClusterLogging": NotRequired[List[AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef]],
    },
)
AwsEksClusterLoggingClusterLoggingDetailsUnionTypeDef = Union[
    AwsEksClusterLoggingClusterLoggingDetailsTypeDef,
    AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef,
]
AwsEksClusterResourcesVpcConfigDetailsUnionTypeDef = Union[
    AwsEksClusterResourcesVpcConfigDetailsTypeDef,
    AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef,
]
AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "Cname": NotRequired[str],
        "DateCreated": NotRequired[str],
        "DateUpdated": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EnvironmentArn": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "EnvironmentLinks": NotRequired[List[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]],
        "EnvironmentName": NotRequired[str],
        "OptionSettings": NotRequired[List[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]],
        "PlatformArn": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "Status": NotRequired[str],
        "Tier": NotRequired[AwsElasticBeanstalkEnvironmentTierTypeDef],
        "VersionLabel": NotRequired[str],
    },
)
AwsElasticBeanstalkEnvironmentDetailsTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "Cname": NotRequired[str],
        "DateCreated": NotRequired[str],
        "DateUpdated": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EnvironmentArn": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "EnvironmentLinks": NotRequired[
            Sequence[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]
        ],
        "EnvironmentName": NotRequired[str],
        "OptionSettings": NotRequired[Sequence[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]],
        "PlatformArn": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "Status": NotRequired[str],
        "Tier": NotRequired[AwsElasticBeanstalkEnvironmentTierTypeDef],
        "VersionLabel": NotRequired[str],
    },
)
AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    {
        "DedicatedMasterCount": NotRequired[int],
        "DedicatedMasterEnabled": NotRequired[bool],
        "DedicatedMasterType": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[str],
        "ZoneAwarenessConfig": NotRequired[
            AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef
        ],
        "ZoneAwarenessEnabled": NotRequired[bool],
    },
)
AwsElasticsearchDomainLogPublishingOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    {
        "IndexSlowLogs": NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef],
        "SearchSlowLogs": NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef],
        "AuditLogs": NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef],
    },
)
AwsElasticsearchDomainVPCOptionsUnionTypeDef = Union[
    AwsElasticsearchDomainVPCOptionsTypeDef, AwsElasticsearchDomainVPCOptionsOutputTypeDef
]
AwsElbLoadBalancerPoliciesOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerPoliciesOutputTypeDef",
    {
        "AppCookieStickinessPolicies": NotRequired[List[AwsElbAppCookieStickinessPolicyTypeDef]],
        "LbCookieStickinessPolicies": NotRequired[List[AwsElbLbCookieStickinessPolicyTypeDef]],
        "OtherPolicies": NotRequired[List[str]],
    },
)
AwsElbLoadBalancerPoliciesTypeDef = TypedDict(
    "AwsElbLoadBalancerPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": NotRequired[
            Sequence[AwsElbAppCookieStickinessPolicyTypeDef]
        ],
        "LbCookieStickinessPolicies": NotRequired[Sequence[AwsElbLbCookieStickinessPolicyTypeDef]],
        "OtherPolicies": NotRequired[Sequence[str]],
    },
)
AwsElbLoadBalancerAttributesOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerAttributesOutputTypeDef",
    {
        "AccessLog": NotRequired[AwsElbLoadBalancerAccessLogTypeDef],
        "ConnectionDraining": NotRequired[AwsElbLoadBalancerConnectionDrainingTypeDef],
        "ConnectionSettings": NotRequired[AwsElbLoadBalancerConnectionSettingsTypeDef],
        "CrossZoneLoadBalancing": NotRequired[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef],
        "AdditionalAttributes": NotRequired[List[AwsElbLoadBalancerAdditionalAttributeTypeDef]],
    },
)
AwsElbLoadBalancerAttributesTypeDef = TypedDict(
    "AwsElbLoadBalancerAttributesTypeDef",
    {
        "AccessLog": NotRequired[AwsElbLoadBalancerAccessLogTypeDef],
        "ConnectionDraining": NotRequired[AwsElbLoadBalancerConnectionDrainingTypeDef],
        "ConnectionSettings": NotRequired[AwsElbLoadBalancerConnectionSettingsTypeDef],
        "CrossZoneLoadBalancing": NotRequired[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef],
        "AdditionalAttributes": NotRequired[Sequence[AwsElbLoadBalancerAdditionalAttributeTypeDef]],
    },
)
AwsElbLoadBalancerBackendServerDescriptionUnionTypeDef = Union[
    AwsElbLoadBalancerBackendServerDescriptionTypeDef,
    AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef,
]
AwsElbLoadBalancerListenerDescriptionOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionOutputTypeDef",
    {
        "Listener": NotRequired[AwsElbLoadBalancerListenerTypeDef],
        "PolicyNames": NotRequired[List[str]],
    },
)
AwsElbLoadBalancerListenerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    {
        "Listener": NotRequired[AwsElbLoadBalancerListenerTypeDef],
        "PolicyNames": NotRequired[Sequence[str]],
    },
)
AwsElbv2LoadBalancerDetailsOutputTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsOutputTypeDef",
    {
        "AvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DNSName": NotRequired[str],
        "IpAddressType": NotRequired[str],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "State": NotRequired[LoadBalancerStateTypeDef],
        "Type": NotRequired[str],
        "VpcId": NotRequired[str],
        "LoadBalancerAttributes": NotRequired[List[AwsElbv2LoadBalancerAttributeTypeDef]],
    },
)
AwsElbv2LoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[AvailabilityZoneTypeDef]],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DNSName": NotRequired[str],
        "IpAddressType": NotRequired[str],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "State": NotRequired[LoadBalancerStateTypeDef],
        "Type": NotRequired[str],
        "VpcId": NotRequired[str],
        "LoadBalancerAttributes": NotRequired[Sequence[AwsElbv2LoadBalancerAttributeTypeDef]],
    },
)
AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef = TypedDict(
    "AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef",
    {
        "Primary": NotRequired[AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef],
        "Secondary": NotRequired[
            AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef
        ],
    },
)
AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef",
    {
        "AuditLogs": NotRequired[AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef],
    },
)
AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef",
    {
        "EbsVolumes": NotRequired[
            AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef
        ],
    },
)
AwsIamAccessKeySessionContextTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextTypeDef",
    {
        "Attributes": NotRequired[AwsIamAccessKeySessionContextAttributesTypeDef],
        "SessionIssuer": NotRequired[AwsIamAccessKeySessionContextSessionIssuerTypeDef],
    },
)
AwsIamGroupDetailsOutputTypeDef = TypedDict(
    "AwsIamGroupDetailsOutputTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "GroupPolicyList": NotRequired[List[AwsIamGroupPolicyTypeDef]],
        "Path": NotRequired[str],
    },
)
AwsIamGroupDetailsTypeDef = TypedDict(
    "AwsIamGroupDetailsTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "GroupPolicyList": NotRequired[Sequence[AwsIamGroupPolicyTypeDef]],
        "Path": NotRequired[str],
    },
)
AwsIamInstanceProfileOutputTypeDef = TypedDict(
    "AwsIamInstanceProfileOutputTypeDef",
    {
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[str],
        "InstanceProfileId": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "Path": NotRequired[str],
        "Roles": NotRequired[List[AwsIamInstanceProfileRoleTypeDef]],
    },
)
AwsIamInstanceProfileTypeDef = TypedDict(
    "AwsIamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[str],
        "InstanceProfileId": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "Path": NotRequired[str],
        "Roles": NotRequired[Sequence[AwsIamInstanceProfileRoleTypeDef]],
    },
)
AwsIamPolicyDetailsOutputTypeDef = TypedDict(
    "AwsIamPolicyDetailsOutputTypeDef",
    {
        "AttachmentCount": NotRequired[int],
        "CreateDate": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "Description": NotRequired[str],
        "IsAttachable": NotRequired[bool],
        "Path": NotRequired[str],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "PolicyVersionList": NotRequired[List[AwsIamPolicyVersionTypeDef]],
        "UpdateDate": NotRequired[str],
    },
)
AwsIamPolicyDetailsTypeDef = TypedDict(
    "AwsIamPolicyDetailsTypeDef",
    {
        "AttachmentCount": NotRequired[int],
        "CreateDate": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "Description": NotRequired[str],
        "IsAttachable": NotRequired[bool],
        "Path": NotRequired[str],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "PolicyVersionList": NotRequired[Sequence[AwsIamPolicyVersionTypeDef]],
        "UpdateDate": NotRequired[str],
    },
)
AwsIamUserDetailsOutputTypeDef = TypedDict(
    "AwsIamUserDetailsOutputTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "GroupList": NotRequired[List[str]],
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[AwsIamPermissionsBoundaryTypeDef],
        "UserId": NotRequired[str],
        "UserName": NotRequired[str],
        "UserPolicyList": NotRequired[List[AwsIamUserPolicyTypeDef]],
    },
)
AwsIamUserDetailsTypeDef = TypedDict(
    "AwsIamUserDetailsTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "GroupList": NotRequired[Sequence[str]],
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[AwsIamPermissionsBoundaryTypeDef],
        "UserId": NotRequired[str],
        "UserName": NotRequired[str],
        "UserPolicyList": NotRequired[Sequence[AwsIamUserPolicyTypeDef]],
    },
)
AwsKinesisStreamDetailsTypeDef = TypedDict(
    "AwsKinesisStreamDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "StreamEncryption": NotRequired[AwsKinesisStreamStreamEncryptionDetailsTypeDef],
        "ShardCount": NotRequired[int],
        "RetentionPeriodHours": NotRequired[int],
    },
)
AwsLambdaFunctionEnvironmentOutputTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentOutputTypeDef",
    {
        "Variables": NotRequired[Dict[str, str]],
        "Error": NotRequired[AwsLambdaFunctionEnvironmentErrorTypeDef],
    },
)
AwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentTypeDef",
    {
        "Variables": NotRequired[Mapping[str, str]],
        "Error": NotRequired[AwsLambdaFunctionEnvironmentErrorTypeDef],
    },
)
AwsLambdaFunctionVpcConfigUnionTypeDef = Union[
    AwsLambdaFunctionVpcConfigTypeDef, AwsLambdaFunctionVpcConfigOutputTypeDef
]
AwsLambdaLayerVersionDetailsUnionTypeDef = Union[
    AwsLambdaLayerVersionDetailsTypeDef, AwsLambdaLayerVersionDetailsOutputTypeDef
]
AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef",
    {
        "Iam": NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef],
        "Scram": NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef],
    },
)
AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnionTypeDef = Union[
    AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef,
    AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef,
]
AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef",
    {
        "EncryptionInTransit": NotRequired[
            AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef
        ],
        "EncryptionAtRest": NotRequired[
            AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef
        ],
    },
)
AwsNetworkFirewallFirewallDetailsOutputTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallDetailsOutputTypeDef",
    {
        "DeleteProtection": NotRequired[bool],
        "Description": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallId": NotRequired[str],
        "FirewallName": NotRequired[str],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyChangeProtection": NotRequired[bool],
        "SubnetChangeProtection": NotRequired[bool],
        "SubnetMappings": NotRequired[List[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]],
        "VpcId": NotRequired[str],
    },
)
AwsNetworkFirewallFirewallDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    {
        "DeleteProtection": NotRequired[bool],
        "Description": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallId": NotRequired[str],
        "FirewallName": NotRequired[str],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyChangeProtection": NotRequired[bool],
        "SubnetChangeProtection": NotRequired[bool],
        "SubnetMappings": NotRequired[
            Sequence[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]
        ],
        "VpcId": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "InternalUserDatabaseEnabled": NotRequired[bool],
        "MasterUserOptions": NotRequired[AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef],
    },
)
AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "WarmEnabled": NotRequired[bool],
        "WarmCount": NotRequired[int],
        "DedicatedMasterEnabled": NotRequired[bool],
        "ZoneAwarenessConfig": NotRequired[
            AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef
        ],
        "DedicatedMasterCount": NotRequired[int],
        "InstanceType": NotRequired[str],
        "WarmType": NotRequired[str],
        "ZoneAwarenessEnabled": NotRequired[bool],
        "DedicatedMasterType": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    {
        "IndexSlowLogs": NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef],
        "SearchSlowLogs": NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef],
        "AuditLogs": NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef],
    },
)
AwsOpenSearchServiceDomainVpcOptionsDetailsUnionTypeDef = Union[
    AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef,
    AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef,
]
AwsRdsDbClusterDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbClusterDetailsOutputTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[List[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "Status": NotRequired[str],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "CustomEndpoints": NotRequired[List[str]],
        "MultiAz": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReadReplicaIdentifiers": NotRequired[List[str]],
        "VpcSecurityGroups": NotRequired[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]],
        "HostedZoneId": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "AssociatedRoles": NotRequired[List[AwsRdsDbClusterAssociatedRoleTypeDef]],
        "ClusterCreateTime": NotRequired[str],
        "EnabledCloudWatchLogsExports": NotRequired[List[str]],
        "EngineMode": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "HttpEndpointEnabled": NotRequired[bool],
        "ActivityStreamStatus": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "CrossAccountClone": NotRequired[bool],
        "DomainMemberships": NotRequired[List[AwsRdsDbDomainMembershipTypeDef]],
        "DbClusterParameterGroup": NotRequired[str],
        "DbSubnetGroup": NotRequired[str],
        "DbClusterOptionGroupMemberships": NotRequired[
            List[AwsRdsDbClusterOptionGroupMembershipTypeDef]
        ],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterMembers": NotRequired[List[AwsRdsDbClusterMemberTypeDef]],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
    },
)
AwsRdsDbClusterDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterDetailsTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "Status": NotRequired[str],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "CustomEndpoints": NotRequired[Sequence[str]],
        "MultiAz": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReadReplicaIdentifiers": NotRequired[Sequence[str]],
        "VpcSecurityGroups": NotRequired[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]],
        "HostedZoneId": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "AssociatedRoles": NotRequired[Sequence[AwsRdsDbClusterAssociatedRoleTypeDef]],
        "ClusterCreateTime": NotRequired[str],
        "EnabledCloudWatchLogsExports": NotRequired[Sequence[str]],
        "EngineMode": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "HttpEndpointEnabled": NotRequired[bool],
        "ActivityStreamStatus": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "CrossAccountClone": NotRequired[bool],
        "DomainMemberships": NotRequired[Sequence[AwsRdsDbDomainMembershipTypeDef]],
        "DbClusterParameterGroup": NotRequired[str],
        "DbSubnetGroup": NotRequired[str],
        "DbClusterOptionGroupMemberships": NotRequired[
            Sequence[AwsRdsDbClusterOptionGroupMembershipTypeDef]
        ],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterMembers": NotRequired[Sequence[AwsRdsDbClusterMemberTypeDef]],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
    },
)
AwsRdsDbClusterSnapshotDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDetailsOutputTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterSnapshotIdentifier": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "DbClusterSnapshotAttributes": NotRequired[
            List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef]
        ],
    },
)
AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnionTypeDef = Union[
    AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef,
    AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef,
]
AwsRdsDbSnapshotDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbSnapshotDetailsOutputTypeDef",
    {
        "DbSnapshotIdentifier": NotRequired[str],
        "DbInstanceIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "SourceRegion": NotRequired[str],
        "SourceDbSnapshotIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "Timezone": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "ProcessorFeatures": NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]],
        "DbiResourceId": NotRequired[str],
    },
)
AwsRdsDbSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbSnapshotDetailsTypeDef",
    {
        "DbSnapshotIdentifier": NotRequired[str],
        "DbInstanceIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "SourceRegion": NotRequired[str],
        "SourceDbSnapshotIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "Timezone": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "ProcessorFeatures": NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]],
        "DbiResourceId": NotRequired[str],
    },
)
AwsRdsDbPendingModifiedValuesOutputTypeDef = TypedDict(
    "AwsRdsDbPendingModifiedValuesOutputTypeDef",
    {
        "DbInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "Port": NotRequired[int],
        "BackupRetentionPeriod": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "DbInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "CaCertificateIdentifier": NotRequired[str],
        "DbSubnetGroupName": NotRequired[str],
        "PendingCloudWatchLogsExports": NotRequired[
            AwsRdsPendingCloudWatchLogsExportsOutputTypeDef
        ],
        "ProcessorFeatures": NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]],
    },
)
AwsRdsDbSecurityGroupDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupDetailsOutputTypeDef",
    {
        "DbSecurityGroupArn": NotRequired[str],
        "DbSecurityGroupDescription": NotRequired[str],
        "DbSecurityGroupName": NotRequired[str],
        "Ec2SecurityGroups": NotRequired[List[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]],
        "IpRanges": NotRequired[List[AwsRdsDbSecurityGroupIpRangeTypeDef]],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
AwsRdsDbSecurityGroupDetailsTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupDetailsTypeDef",
    {
        "DbSecurityGroupArn": NotRequired[str],
        "DbSecurityGroupDescription": NotRequired[str],
        "DbSecurityGroupName": NotRequired[str],
        "Ec2SecurityGroups": NotRequired[Sequence[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]],
        "IpRanges": NotRequired[Sequence[AwsRdsDbSecurityGroupIpRangeTypeDef]],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
AwsRdsDbSubnetGroupSubnetTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef],
        "SubnetStatus": NotRequired[str],
    },
)
AwsRdsEventSubscriptionDetailsUnionTypeDef = Union[
    AwsRdsEventSubscriptionDetailsTypeDef, AwsRdsEventSubscriptionDetailsOutputTypeDef
]
AwsRdsPendingCloudWatchLogsExportsUnionTypeDef = Union[
    AwsRdsPendingCloudWatchLogsExportsTypeDef, AwsRdsPendingCloudWatchLogsExportsOutputTypeDef
]
AwsRedshiftClusterClusterParameterGroupOutputTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterGroupOutputTypeDef",
    {
        "ClusterParameterStatusList": NotRequired[
            List[AwsRedshiftClusterClusterParameterStatusTypeDef]
        ],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
    },
)
AwsRedshiftClusterClusterParameterGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    {
        "ClusterParameterStatusList": NotRequired[
            Sequence[AwsRedshiftClusterClusterParameterStatusTypeDef]
        ],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
    },
)
AwsRoute53HostedZoneObjectDetailsTypeDef = TypedDict(
    "AwsRoute53HostedZoneObjectDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Config": NotRequired[AwsRoute53HostedZoneConfigDetailsTypeDef],
    },
)
AwsRoute53QueryLoggingConfigDetailsTypeDef = TypedDict(
    "AwsRoute53QueryLoggingConfigDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[CloudWatchLogsLogGroupArnConfigDetailsTypeDef],
    },
)
AwsS3AccessPointDetailsTypeDef = TypedDict(
    "AwsS3AccessPointDetailsTypeDef",
    {
        "AccessPointArn": NotRequired[str],
        "Alias": NotRequired[str],
        "Bucket": NotRequired[str],
        "BucketAccountId": NotRequired[str],
        "Name": NotRequired[str],
        "NetworkOrigin": NotRequired[str],
        "PublicAccessBlockConfiguration": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "VpcConfiguration": NotRequired[AwsS3AccessPointVpcConfigurationDetailsTypeDef],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef",
    {
        "FilterRules": NotRequired[
            List[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]
        ],
    },
)
AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    {
        "FilterRules": NotRequired[
            Sequence[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]
        ],
    },
)
AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef",
    {
        "DefaultRetention": NotRequired[
            AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef
        ],
    },
)
AwsS3BucketServerSideEncryptionRuleTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": NotRequired[
            AwsS3BucketServerSideEncryptionByDefaultTypeDef
        ],
    },
)
AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    {
        "Condition": NotRequired[AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef],
        "Redirect": NotRequired[AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef],
    },
)
AwsSageMakerNotebookInstanceDetailsOutputTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceDetailsOutputTypeDef",
    {
        "AcceleratorTypes": NotRequired[List[str]],
        "AdditionalCodeRepositories": NotRequired[List[str]],
        "DefaultCodeRepository": NotRequired[str],
        "DirectInternetAccess": NotRequired[str],
        "FailureReason": NotRequired[str],
        "InstanceMetadataServiceConfiguration": NotRequired[
            AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NotebookInstanceArn": NotRequired[str],
        "NotebookInstanceLifecycleConfigName": NotRequired[str],
        "NotebookInstanceName": NotRequired[str],
        "NotebookInstanceStatus": NotRequired[str],
        "PlatformIdentifier": NotRequired[str],
        "RoleArn": NotRequired[str],
        "RootAccess": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "SubnetId": NotRequired[str],
        "Url": NotRequired[str],
        "VolumeSizeInGB": NotRequired[int],
    },
)
AwsSageMakerNotebookInstanceDetailsTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceDetailsTypeDef",
    {
        "AcceleratorTypes": NotRequired[Sequence[str]],
        "AdditionalCodeRepositories": NotRequired[Sequence[str]],
        "DefaultCodeRepository": NotRequired[str],
        "DirectInternetAccess": NotRequired[str],
        "FailureReason": NotRequired[str],
        "InstanceMetadataServiceConfiguration": NotRequired[
            AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NotebookInstanceArn": NotRequired[str],
        "NotebookInstanceLifecycleConfigName": NotRequired[str],
        "NotebookInstanceName": NotRequired[str],
        "NotebookInstanceStatus": NotRequired[str],
        "PlatformIdentifier": NotRequired[str],
        "RoleArn": NotRequired[str],
        "RootAccess": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "Url": NotRequired[str],
        "VolumeSizeInGB": NotRequired[int],
    },
)
AwsSecretsManagerSecretDetailsTypeDef = TypedDict(
    "AwsSecretsManagerSecretDetailsTypeDef",
    {
        "RotationRules": NotRequired[AwsSecretsManagerSecretRotationRulesTypeDef],
        "RotationOccurredWithinFrequency": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "RotationEnabled": NotRequired[bool],
        "RotationLambdaArn": NotRequired[str],
        "Deleted": NotRequired[bool],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
BatchUpdateFindingsRequestRequestTypeDef = TypedDict(
    "BatchUpdateFindingsRequestRequestTypeDef",
    {
        "FindingIdentifiers": Sequence[AwsSecurityFindingIdentifierTypeDef],
        "Note": NotRequired[NoteUpdateTypeDef],
        "Severity": NotRequired[SeverityUpdateTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Types": NotRequired[Sequence[str]],
        "UserDefinedFields": NotRequired[Mapping[str, str]],
        "Workflow": NotRequired[WorkflowUpdateTypeDef],
        "RelatedFindings": NotRequired[Sequence[RelatedFindingTypeDef]],
    },
)
BatchUpdateFindingsUnprocessedFindingTypeDef = TypedDict(
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierTypeDef,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)
AwsSnsTopicDetailsOutputTypeDef = TypedDict(
    "AwsSnsTopicDetailsOutputTypeDef",
    {
        "KmsMasterKeyId": NotRequired[str],
        "Subscription": NotRequired[List[AwsSnsTopicSubscriptionTypeDef]],
        "TopicName": NotRequired[str],
        "Owner": NotRequired[str],
        "SqsSuccessFeedbackRoleArn": NotRequired[str],
        "SqsFailureFeedbackRoleArn": NotRequired[str],
        "ApplicationSuccessFeedbackRoleArn": NotRequired[str],
        "FirehoseSuccessFeedbackRoleArn": NotRequired[str],
        "FirehoseFailureFeedbackRoleArn": NotRequired[str],
        "HttpSuccessFeedbackRoleArn": NotRequired[str],
        "HttpFailureFeedbackRoleArn": NotRequired[str],
    },
)
AwsSnsTopicDetailsTypeDef = TypedDict(
    "AwsSnsTopicDetailsTypeDef",
    {
        "KmsMasterKeyId": NotRequired[str],
        "Subscription": NotRequired[Sequence[AwsSnsTopicSubscriptionTypeDef]],
        "TopicName": NotRequired[str],
        "Owner": NotRequired[str],
        "SqsSuccessFeedbackRoleArn": NotRequired[str],
        "SqsFailureFeedbackRoleArn": NotRequired[str],
        "ApplicationSuccessFeedbackRoleArn": NotRequired[str],
        "FirehoseSuccessFeedbackRoleArn": NotRequired[str],
        "FirehoseFailureFeedbackRoleArn": NotRequired[str],
        "HttpSuccessFeedbackRoleArn": NotRequired[str],
        "HttpFailureFeedbackRoleArn": NotRequired[str],
    },
)
AwsSsmPatchTypeDef = TypedDict(
    "AwsSsmPatchTypeDef",
    {
        "ComplianceSummary": NotRequired[AwsSsmComplianceSummaryTypeDef],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef",
    {
        "CloudWatchLogsLogGroup": NotRequired[
            AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef
        ],
    },
)
AwsWafRateBasedRuleDetailsOutputTypeDef = TypedDict(
    "AwsWafRateBasedRuleDetailsOutputTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[List[AwsWafRateBasedRuleMatchPredicateTypeDef]],
    },
)
AwsWafRateBasedRuleDetailsTypeDef = TypedDict(
    "AwsWafRateBasedRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[Sequence[AwsWafRateBasedRuleMatchPredicateTypeDef]],
    },
)
AwsWafRegionalRateBasedRuleDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleDetailsOutputTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[List[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]],
    },
)
AwsWafRegionalRateBasedRuleDetailsTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[Sequence[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]],
    },
)
AwsWafRegionalRuleDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRuleDetailsOutputTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "PredicateList": NotRequired[List[AwsWafRegionalRulePredicateListDetailsTypeDef]],
        "RuleId": NotRequired[str],
    },
)
AwsWafRegionalRuleDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "PredicateList": NotRequired[Sequence[AwsWafRegionalRulePredicateListDetailsTypeDef]],
        "RuleId": NotRequired[str],
    },
)
AwsWafRegionalRuleGroupRulesDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRegionalRuleGroupRulesActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRegionalWebAclRulesListActionDetailsTypeDef],
        "OverrideAction": NotRequired[AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafRuleDetailsOutputTypeDef = TypedDict(
    "AwsWafRuleDetailsOutputTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "PredicateList": NotRequired[List[AwsWafRulePredicateListDetailsTypeDef]],
        "RuleId": NotRequired[str],
    },
)
AwsWafRuleDetailsTypeDef = TypedDict(
    "AwsWafRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "PredicateList": NotRequired[Sequence[AwsWafRulePredicateListDetailsTypeDef]],
        "RuleId": NotRequired[str],
    },
)
AwsWafRuleGroupRulesDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupRulesDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRuleGroupRulesActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafWebAclRuleOutputTypeDef = TypedDict(
    "AwsWafWebAclRuleOutputTypeDef",
    {
        "Action": NotRequired[WafActionTypeDef],
        "ExcludedRules": NotRequired[List[WafExcludedRuleTypeDef]],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafWebAclRuleTypeDef = TypedDict(
    "AwsWafWebAclRuleTypeDef",
    {
        "Action": NotRequired[WafActionTypeDef],
        "ExcludedRules": NotRequired[Sequence[WafExcludedRuleTypeDef]],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafv2CustomRequestHandlingDetailsOutputTypeDef = TypedDict(
    "AwsWafv2CustomRequestHandlingDetailsOutputTypeDef",
    {
        "InsertHeaders": NotRequired[List[AwsWafv2CustomHttpHeaderTypeDef]],
    },
)
AwsWafv2CustomRequestHandlingDetailsTypeDef = TypedDict(
    "AwsWafv2CustomRequestHandlingDetailsTypeDef",
    {
        "InsertHeaders": NotRequired[Sequence[AwsWafv2CustomHttpHeaderTypeDef]],
    },
)
AwsWafv2CustomResponseDetailsOutputTypeDef = TypedDict(
    "AwsWafv2CustomResponseDetailsOutputTypeDef",
    {
        "CustomResponseBodyKey": NotRequired[str],
        "ResponseCode": NotRequired[int],
        "ResponseHeaders": NotRequired[List[AwsWafv2CustomHttpHeaderTypeDef]],
    },
)
AwsWafv2CustomResponseDetailsTypeDef = TypedDict(
    "AwsWafv2CustomResponseDetailsTypeDef",
    {
        "CustomResponseBodyKey": NotRequired[str],
        "ResponseCode": NotRequired[int],
        "ResponseHeaders": NotRequired[Sequence[AwsWafv2CustomHttpHeaderTypeDef]],
    },
)
AwsWafv2WebAclCaptchaConfigDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclCaptchaConfigDetailsTypeDef",
    {
        "ImmunityTimeProperty": NotRequired[
            AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef
        ],
    },
)
CreateActionTargetResponseTypeDef = TypedDict(
    "CreateActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAutomationRuleResponseTypeDef = TypedDict(
    "CreateAutomationRuleResponseTypeDef",
    {
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFindingAggregatorResponseTypeDef = TypedDict(
    "CreateFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInsightResponseTypeDef = TypedDict(
    "CreateInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteActionTargetResponseTypeDef = TypedDict(
    "DeleteActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInsightResponseTypeDef = TypedDict(
    "DeleteInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeActionTargetsResponseTypeDef = TypedDict(
    "DescribeActionTargetsResponseTypeDef",
    {
        "ActionTargets": List[ActionTargetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeHubResponseTypeDef = TypedDict(
    "DescribeHubResponseTypeDef",
    {
        "HubArn": str,
        "SubscribedAt": str,
        "AutoEnableControls": bool,
        "ControlFindingGenerator": ControlFindingGeneratorType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableImportFindingsForProductResponseTypeDef = TypedDict(
    "EnableImportFindingsForProductResponseTypeDef",
    {
        "ProductSubscriptionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfigurationPolicyAssociationResponseTypeDef = TypedDict(
    "GetConfigurationPolicyAssociationResponseTypeDef",
    {
        "ConfigurationPolicyId": str,
        "TargetId": str,
        "TargetType": TargetTypeType,
        "AssociationType": AssociationTypeType,
        "UpdatedAt": datetime,
        "AssociationStatus": ConfigurationPolicyAssociationStatusType,
        "AssociationStatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingAggregatorResponseTypeDef = TypedDict(
    "GetFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
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
ListAutomationRulesResponseTypeDef = TypedDict(
    "ListAutomationRulesResponseTypeDef",
    {
        "AutomationRulesMetadata": List[AutomationRulesMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ListEnabledProductsForImportResponseTypeDef",
    {
        "ProductSubscriptions": List[str],
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
StartConfigurationPolicyAssociationResponseTypeDef = TypedDict(
    "StartConfigurationPolicyAssociationResponseTypeDef",
    {
        "ConfigurationPolicyId": str,
        "TargetId": str,
        "TargetType": TargetTypeType,
        "AssociationType": AssociationTypeType,
        "UpdatedAt": datetime,
        "AssociationStatus": ConfigurationPolicyAssociationStatusType,
        "AssociationStatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFindingAggregatorResponseTypeDef = TypedDict(
    "UpdateFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteAutomationRulesResponseTypeDef = TypedDict(
    "BatchDeleteAutomationRulesResponseTypeDef",
    {
        "ProcessedAutomationRules": List[str],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateAutomationRulesResponseTypeDef = TypedDict(
    "BatchUpdateAutomationRulesResponseTypeDef",
    {
        "ProcessedAutomationRules": List[str],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchEnableStandardsRequestRequestTypeDef = TypedDict(
    "BatchEnableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionRequests": Sequence[StandardsSubscriptionRequestTypeDef],
    },
)
ListConfigurationPolicyAssociationsResponseTypeDef = TypedDict(
    "ListConfigurationPolicyAssociationsResponseTypeDef",
    {
        "ConfigurationPolicyAssociationSummaries": List[
            ConfigurationPolicyAssociationSummaryTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchGetStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "BatchGetStandardsControlAssociationsRequestRequestTypeDef",
    {
        "StandardsControlAssociationIds": Sequence[StandardsControlAssociationIdTypeDef],
    },
)
UnprocessedStandardsControlAssociationTypeDef = TypedDict(
    "UnprocessedStandardsControlAssociationTypeDef",
    {
        "StandardsControlAssociationId": StandardsControlAssociationIdTypeDef,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": NotRequired[str],
    },
)
BatchImportFindingsResponseTypeDef = TypedDict(
    "BatchImportFindingsResponseTypeDef",
    {
        "FailedCount": int,
        "SuccessCount": int,
        "FailedFindings": List[ImportFindingsErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "BatchUpdateStandardsControlAssociationsRequestRequestTypeDef",
    {
        "StandardsControlAssociationUpdates": Sequence[StandardsControlAssociationUpdateTypeDef],
    },
)
UnprocessedStandardsControlAssociationUpdateTypeDef = TypedDict(
    "UnprocessedStandardsControlAssociationUpdateTypeDef",
    {
        "StandardsControlAssociationUpdate": StandardsControlAssociationUpdateTypeDef,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": NotRequired[str],
    },
)
VulnerabilityCodeVulnerabilitiesOutputTypeDef = TypedDict(
    "VulnerabilityCodeVulnerabilitiesOutputTypeDef",
    {
        "Cwes": NotRequired[List[str]],
        "FilePath": NotRequired[CodeVulnerabilitiesFilePathTypeDef],
        "SourceArn": NotRequired[str],
    },
)
VulnerabilityCodeVulnerabilitiesTypeDef = TypedDict(
    "VulnerabilityCodeVulnerabilitiesTypeDef",
    {
        "Cwes": NotRequired[Sequence[str]],
        "FilePath": NotRequired[CodeVulnerabilitiesFilePathTypeDef],
        "SourceArn": NotRequired[str],
    },
)
ComplianceOutputTypeDef = TypedDict(
    "ComplianceOutputTypeDef",
    {
        "Status": NotRequired[ComplianceStatusType],
        "RelatedRequirements": NotRequired[List[str]],
        "StatusReasons": NotRequired[List[StatusReasonTypeDef]],
        "SecurityControlId": NotRequired[str],
        "AssociatedStandards": NotRequired[List[AssociatedStandardTypeDef]],
        "SecurityControlParameters": NotRequired[List[SecurityControlParameterOutputTypeDef]],
    },
)
ConfigurationOptionsTypeDef = TypedDict(
    "ConfigurationOptionsTypeDef",
    {
        "Integer": NotRequired[IntegerConfigurationOptionsTypeDef],
        "IntegerList": NotRequired[IntegerListConfigurationOptionsTypeDef],
        "Double": NotRequired[DoubleConfigurationOptionsTypeDef],
        "String": NotRequired[StringConfigurationOptionsTypeDef],
        "StringList": NotRequired[StringListConfigurationOptionsTypeDef],
        "Boolean": NotRequired[BooleanConfigurationOptionsTypeDef],
        "Enum": NotRequired[EnumConfigurationOptionsTypeDef],
        "EnumList": NotRequired[EnumListConfigurationOptionsTypeDef],
    },
)
ConfigurationPolicyAssociationTypeDef = TypedDict(
    "ConfigurationPolicyAssociationTypeDef",
    {
        "Target": NotRequired[TargetTypeDef],
    },
)
GetConfigurationPolicyAssociationRequestRequestTypeDef = TypedDict(
    "GetConfigurationPolicyAssociationRequestRequestTypeDef",
    {
        "Target": TargetTypeDef,
    },
)
StartConfigurationPolicyAssociationRequestRequestTypeDef = TypedDict(
    "StartConfigurationPolicyAssociationRequestRequestTypeDef",
    {
        "ConfigurationPolicyIdentifier": str,
        "Target": TargetTypeDef,
    },
)
StartConfigurationPolicyDisassociationRequestRequestTypeDef = TypedDict(
    "StartConfigurationPolicyDisassociationRequestRequestTypeDef",
    {
        "ConfigurationPolicyIdentifier": str,
        "Target": NotRequired[TargetTypeDef],
    },
)
ListConfigurationPoliciesResponseTypeDef = TypedDict(
    "ListConfigurationPoliciesResponseTypeDef",
    {
        "ConfigurationPolicySummaries": List[ConfigurationPolicySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ContainerDetailsOutputTypeDef = TypedDict(
    "ContainerDetailsOutputTypeDef",
    {
        "ContainerRuntime": NotRequired[str],
        "Name": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImageName": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "VolumeMounts": NotRequired[List[VolumeMountTypeDef]],
        "Privileged": NotRequired[bool],
    },
)
ContainerDetailsTypeDef = TypedDict(
    "ContainerDetailsTypeDef",
    {
        "ContainerRuntime": NotRequired[str],
        "Name": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImageName": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "VolumeMounts": NotRequired[Sequence[VolumeMountTypeDef]],
        "Privileged": NotRequired[bool],
    },
)
CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "Start": NotRequired[str],
        "End": NotRequired[str],
        "DateRange": NotRequired[DateRangeTypeDef],
    },
)
DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef = TypedDict(
    "DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef",
    {
        "ActionTargetArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeProductsRequestDescribeProductsPaginateTypeDef = TypedDict(
    "DescribeProductsRequestDescribeProductsPaginateTypeDef",
    {
        "ProductArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef = TypedDict(
    "DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStandardsRequestDescribeStandardsPaginateTypeDef = TypedDict(
    "DescribeStandardsRequestDescribeStandardsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef = TypedDict(
    "GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef",
    {
        "StandardsSubscriptionArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetInsightsRequestGetInsightsPaginateTypeDef = TypedDict(
    "GetInsightsRequestGetInsightsPaginateTypeDef",
    {
        "InsightArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef = TypedDict(
    "ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef = TypedDict(
    "ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef",
    {
        "Filters": NotRequired[AssociationFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef = TypedDict(
    "ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef = TypedDict(
    "ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef",
    {
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
        "OnlyAssociated": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef = TypedDict(
    "ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef",
    {
        "StandardsArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef = TypedDict(
    "ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef",
    {
        "SecurityControlId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "AutoEnableStandards": AutoEnableStandardsType,
        "OrganizationConfiguration": OrganizationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnable": bool,
        "AutoEnableStandards": NotRequired[AutoEnableStandardsType],
        "OrganizationConfiguration": NotRequired[OrganizationConfigurationTypeDef],
    },
)
DescribeProductsResponseTypeDef = TypedDict(
    "DescribeProductsResponseTypeDef",
    {
        "Products": List[ProductTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeStandardsControlsResponseTypeDef = TypedDict(
    "DescribeStandardsControlsResponseTypeDef",
    {
        "Controls": List[StandardsControlTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ThreatOutputTypeDef = TypedDict(
    "ThreatOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Severity": NotRequired[str],
        "ItemCount": NotRequired[int],
        "FilePaths": NotRequired[List[FilePathsTypeDef]],
    },
)
ThreatTypeDef = TypedDict(
    "ThreatTypeDef",
    {
        "Name": NotRequired[str],
        "Severity": NotRequired[str],
        "ItemCount": NotRequired[int],
        "FilePaths": NotRequired[Sequence[FilePathsTypeDef]],
    },
)
ListFindingAggregatorsResponseTypeDef = TypedDict(
    "ListFindingAggregatorsResponseTypeDef",
    {
        "FindingAggregators": List[FindingAggregatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FindingHistoryRecordTypeDef = TypedDict(
    "FindingHistoryRecordTypeDef",
    {
        "FindingIdentifier": NotRequired[AwsSecurityFindingIdentifierTypeDef],
        "UpdateTime": NotRequired[datetime],
        "FindingCreated": NotRequired[bool],
        "UpdateSource": NotRequired[FindingHistoryUpdateSourceTypeDef],
        "Updates": NotRequired[List[FindingHistoryUpdateTypeDef]],
        "NextToken": NotRequired[str],
    },
)
FindingProviderFieldsOutputTypeDef = TypedDict(
    "FindingProviderFieldsOutputTypeDef",
    {
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "RelatedFindings": NotRequired[List[RelatedFindingTypeDef]],
        "Severity": NotRequired[FindingProviderSeverityTypeDef],
        "Types": NotRequired[List[str]],
    },
)
FindingProviderFieldsTypeDef = TypedDict(
    "FindingProviderFieldsTypeDef",
    {
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "RelatedFindings": NotRequired[Sequence[RelatedFindingTypeDef]],
        "Severity": NotRequired[FindingProviderSeverityTypeDef],
        "Types": NotRequired[Sequence[str]],
    },
)
GeneratorDetailsUnionTypeDef = Union[GeneratorDetailsTypeDef, GeneratorDetailsOutputTypeDef]
GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "Administrator": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef = TypedDict(
    "GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierTypeDef,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFindingHistoryRequestRequestTypeDef = TypedDict(
    "GetFindingHistoryRequestRequestTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierTypeDef,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List[MemberTypeDef],
        "UnprocessedAccounts": List[ResultTypeDef],
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
InsightResultsTypeDef = TypedDict(
    "InsightResultsTypeDef",
    {
        "InsightArn": str,
        "GroupByAttribute": str,
        "ResultValues": List[InsightResultValueTypeDef],
    },
)
ListStandardsControlAssociationsResponseTypeDef = TypedDict(
    "ListStandardsControlAssociationsResponseTypeDef",
    {
        "StandardsControlAssociationSummaries": List[StandardsControlAssociationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
NetworkPathComponentDetailsOutputTypeDef = TypedDict(
    "NetworkPathComponentDetailsOutputTypeDef",
    {
        "Address": NotRequired[List[str]],
        "PortRanges": NotRequired[List[PortRangeTypeDef]],
    },
)
NetworkPathComponentDetailsTypeDef = TypedDict(
    "NetworkPathComponentDetailsTypeDef",
    {
        "Address": NotRequired[Sequence[str]],
        "PortRanges": NotRequired[Sequence[PortRangeTypeDef]],
    },
)
NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Direction": NotRequired[NetworkDirectionType],
        "Protocol": NotRequired[str],
        "OpenPortRange": NotRequired[PortRangeTypeDef],
        "SourceIpV4": NotRequired[str],
        "SourceIpV6": NotRequired[str],
        "SourcePort": NotRequired[int],
        "SourceDomain": NotRequired[str],
        "SourceMac": NotRequired[str],
        "DestinationIpV4": NotRequired[str],
        "DestinationIpV6": NotRequired[str],
        "DestinationPort": NotRequired[int],
        "DestinationDomain": NotRequired[str],
    },
)
PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "PageNumber": NotRequired[int],
        "LineRange": NotRequired[RangeTypeDef],
        "OffsetRange": NotRequired[RangeTypeDef],
    },
)
ParameterConfigurationOutputTypeDef = TypedDict(
    "ParameterConfigurationOutputTypeDef",
    {
        "ValueType": ParameterValueTypeType,
        "Value": NotRequired[ParameterValueOutputTypeDef],
    },
)
ParameterValueUnionTypeDef = Union[ParameterValueTypeDef, ParameterValueOutputTypeDef]
RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "Recommendation": NotRequired[RecommendationTypeDef],
    },
)
RuleGroupSourceListDetailsUnionTypeDef = Union[
    RuleGroupSourceListDetailsTypeDef, RuleGroupSourceListDetailsOutputTypeDef
]
RuleGroupSourceStatefulRulesDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesDetailsOutputTypeDef",
    {
        "Action": NotRequired[str],
        "Header": NotRequired[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef],
        "RuleOptions": NotRequired[List[RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef]],
    },
)
RuleGroupSourceStatefulRulesOptionsDetailsUnionTypeDef = Union[
    RuleGroupSourceStatefulRulesOptionsDetailsTypeDef,
    RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef,
]
RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef",
    {
        "DestinationPorts": NotRequired[
            List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]
        ],
        "Destinations": NotRequired[
            List[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]
        ],
        "Protocols": NotRequired[List[int]],
        "SourcePorts": NotRequired[
            List[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]
        ],
        "Sources": NotRequired[List[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]],
        "TcpFlags": NotRequired[
            List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef]
        ],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnionTypeDef = Union[
    RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef,
    RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef,
]
RuleGroupVariablesIpSetsDetailsUnionTypeDef = Union[
    RuleGroupVariablesIpSetsDetailsTypeDef, RuleGroupVariablesIpSetsDetailsOutputTypeDef
]
RuleGroupVariablesOutputTypeDef = TypedDict(
    "RuleGroupVariablesOutputTypeDef",
    {
        "IpSets": NotRequired[RuleGroupVariablesIpSetsDetailsOutputTypeDef],
        "PortSets": NotRequired[RuleGroupVariablesPortSetsDetailsOutputTypeDef],
    },
)
RuleGroupVariablesPortSetsDetailsUnionTypeDef = Union[
    RuleGroupVariablesPortSetsDetailsTypeDef, RuleGroupVariablesPortSetsDetailsOutputTypeDef
]
SecurityControlParameterUnionTypeDef = Union[
    SecurityControlParameterTypeDef, SecurityControlParameterOutputTypeDef
]
StandardTypeDef = TypedDict(
    "StandardTypeDef",
    {
        "StandardsArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EnabledByDefault": NotRequired[bool],
        "StandardsManagedBy": NotRequired[StandardsManagedByTypeDef],
    },
)
StandardsSubscriptionTypeDef = TypedDict(
    "StandardsSubscriptionTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": StandardsStatusType,
        "StandardsStatusReason": NotRequired[StandardsStatusReasonTypeDef],
    },
)
StatelessCustomPublishMetricActionOutputTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionOutputTypeDef",
    {
        "Dimensions": NotRequired[List[StatelessCustomPublishMetricActionDimensionTypeDef]],
    },
)
StatelessCustomPublishMetricActionTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionTypeDef",
    {
        "Dimensions": NotRequired[Sequence[StatelessCustomPublishMetricActionDimensionTypeDef]],
    },
)
AwsApiCallActionOutputTypeDef = TypedDict(
    "AwsApiCallActionOutputTypeDef",
    {
        "Api": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CallerType": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "DomainDetails": NotRequired[AwsApiCallActionDomainDetailsTypeDef],
        "AffectedResources": NotRequired[Dict[str, str]],
        "FirstSeen": NotRequired[str],
        "LastSeen": NotRequired[str],
    },
)
AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CallerType": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "DomainDetails": NotRequired[AwsApiCallActionDomainDetailsTypeDef],
        "AffectedResources": NotRequired[Mapping[str, str]],
        "FirstSeen": NotRequired[str],
        "LastSeen": NotRequired[str],
    },
)
NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "ConnectionDirection": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "RemotePortDetails": NotRequired[ActionRemotePortDetailsTypeDef],
        "LocalPortDetails": NotRequired[ActionLocalPortDetailsTypeDef],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
    },
)
PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": NotRequired[ActionLocalPortDetailsTypeDef],
        "LocalIpDetails": NotRequired[ActionLocalIpDetailsTypeDef],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
    },
)
CvssUnionTypeDef = Union[CvssTypeDef, CvssOutputTypeDef]
AwsEc2RouteTableDetailsOutputTypeDef = TypedDict(
    "AwsEc2RouteTableDetailsOutputTypeDef",
    {
        "AssociationSet": NotRequired[List[AssociationSetDetailsTypeDef]],
        "OwnerId": NotRequired[str],
        "PropagatingVgwSet": NotRequired[List[PropagatingVgwSetDetailsTypeDef]],
        "RouteTableId": NotRequired[str],
        "RouteSet": NotRequired[List[RouteSetDetailsTypeDef]],
        "VpcId": NotRequired[str],
    },
)
AwsEc2RouteTableDetailsTypeDef = TypedDict(
    "AwsEc2RouteTableDetailsTypeDef",
    {
        "AssociationSet": NotRequired[Sequence[AssociationSetDetailsTypeDef]],
        "OwnerId": NotRequired[str],
        "PropagatingVgwSet": NotRequired[Sequence[PropagatingVgwSetDetailsTypeDef]],
        "RouteTableId": NotRequired[str],
        "RouteSet": NotRequired[Sequence[RouteSetDetailsTypeDef]],
        "VpcId": NotRequired[str],
    },
)
AutomationRulesActionOutputTypeDef = TypedDict(
    "AutomationRulesActionOutputTypeDef",
    {
        "Type": NotRequired[Literal["FINDING_FIELDS_UPDATE"]],
        "FindingFieldsUpdate": NotRequired[AutomationRulesFindingFieldsUpdateOutputTypeDef],
    },
)
AutomationRulesFindingFieldsUpdateUnionTypeDef = Union[
    AutomationRulesFindingFieldsUpdateTypeDef, AutomationRulesFindingFieldsUpdateOutputTypeDef
]
AwsAmazonMqBrokerDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerDetailsOutputTypeDef",
    {
        "AuthenticationStrategy": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "BrokerArn": NotRequired[str],
        "BrokerName": NotRequired[str],
        "DeploymentMode": NotRequired[str],
        "EncryptionOptions": NotRequired[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef],
        "EngineType": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "HostInstanceType": NotRequired[str],
        "BrokerId": NotRequired[str],
        "LdapServerMetadata": NotRequired[AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef],
        "Logs": NotRequired[AwsAmazonMqBrokerLogsDetailsTypeDef],
        "MaintenanceWindowStartTime": NotRequired[
            AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef
        ],
        "PubliclyAccessible": NotRequired[bool],
        "SecurityGroups": NotRequired[List[str]],
        "StorageType": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "Users": NotRequired[List[AwsAmazonMqBrokerUsersDetailsTypeDef]],
    },
)
AwsAmazonMqBrokerDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerDetailsTypeDef",
    {
        "AuthenticationStrategy": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "BrokerArn": NotRequired[str],
        "BrokerName": NotRequired[str],
        "DeploymentMode": NotRequired[str],
        "EncryptionOptions": NotRequired[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef],
        "EngineType": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "HostInstanceType": NotRequired[str],
        "BrokerId": NotRequired[str],
        "LdapServerMetadata": NotRequired[AwsAmazonMqBrokerLdapServerMetadataDetailsUnionTypeDef],
        "Logs": NotRequired[AwsAmazonMqBrokerLogsDetailsTypeDef],
        "MaintenanceWindowStartTime": NotRequired[
            AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef
        ],
        "PubliclyAccessible": NotRequired[bool],
        "SecurityGroups": NotRequired[Sequence[str]],
        "StorageType": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "Users": NotRequired[Sequence[AwsAmazonMqBrokerUsersDetailsTypeDef]],
    },
)
AwsApiGatewayStageDetailsTypeDef = TypedDict(
    "AwsApiGatewayStageDetailsTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "ClientCertificateId": NotRequired[str],
        "StageName": NotRequired[str],
        "Description": NotRequired[str],
        "CacheClusterEnabled": NotRequired[bool],
        "CacheClusterSize": NotRequired[str],
        "CacheClusterStatus": NotRequired[str],
        "MethodSettings": NotRequired[Sequence[AwsApiGatewayMethodSettingsTypeDef]],
        "Variables": NotRequired[Mapping[str, str]],
        "DocumentationVersion": NotRequired[str],
        "AccessLogSettings": NotRequired[AwsApiGatewayAccessLogSettingsTypeDef],
        "CanarySettings": NotRequired[AwsApiGatewayCanarySettingsUnionTypeDef],
        "TracingEnabled": NotRequired[bool],
        "CreatedDate": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "WebAclArn": NotRequired[str],
    },
)
AwsApiGatewayRestApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayRestApiDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Version": NotRequired[str],
        "BinaryMediaTypes": NotRequired[Sequence[str]],
        "MinimumCompressionSize": NotRequired[int],
        "ApiKeySource": NotRequired[str],
        "EndpointConfiguration": NotRequired[AwsApiGatewayEndpointConfigurationUnionTypeDef],
    },
)
AwsApiGatewayV2StageDetailsUnionTypeDef = Union[
    AwsApiGatewayV2StageDetailsTypeDef, AwsApiGatewayV2StageDetailsOutputTypeDef
]
AwsAppSyncGraphQlApiDetailsOutputTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiDetailsOutputTypeDef",
    {
        "ApiId": NotRequired[str],
        "Id": NotRequired[str],
        "OpenIdConnectConfig": NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef],
        "Name": NotRequired[str],
        "LambdaAuthorizerConfig": NotRequired[
            AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef
        ],
        "XrayEnabled": NotRequired[bool],
        "Arn": NotRequired[str],
        "UserPoolConfig": NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef],
        "AuthenticationType": NotRequired[str],
        "LogConfig": NotRequired[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef],
        "AdditionalAuthenticationProviders": NotRequired[
            List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]
        ],
        "WafWebAclArn": NotRequired[str],
    },
)
AwsAppSyncGraphQlApiDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiDetailsTypeDef",
    {
        "ApiId": NotRequired[str],
        "Id": NotRequired[str],
        "OpenIdConnectConfig": NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef],
        "Name": NotRequired[str],
        "LambdaAuthorizerConfig": NotRequired[
            AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef
        ],
        "XrayEnabled": NotRequired[bool],
        "Arn": NotRequired[str],
        "UserPoolConfig": NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef],
        "AuthenticationType": NotRequired[str],
        "LogConfig": NotRequired[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef],
        "AdditionalAuthenticationProviders": NotRequired[
            Sequence[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]
        ],
        "WafWebAclArn": NotRequired[str],
    },
)
AwsAthenaWorkGroupConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationDetailsTypeDef",
    {
        "ResultConfiguration": NotRequired[
            AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef
        ],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef",
    {
        "InstancesDistribution": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef
        ],
        "LaunchTemplate": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef
        ],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnionTypeDef = Union[
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef,
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef,
]
AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "BlockDeviceMappings": NotRequired[
            List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]
        ],
        "ClassicLinkVpcId": NotRequired[str],
        "ClassicLinkVpcSecurityGroups": NotRequired[List[str]],
        "CreatedTime": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[str],
        "ImageId": NotRequired[str],
        "InstanceMonitoring": NotRequired[
            AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "PlacementTenancy": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "SpotPrice": NotRequired[str],
        "UserData": NotRequired[str],
        "MetadataOptions": NotRequired[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef],
    },
)
AwsAutoScalingLaunchConfigurationDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "BlockDeviceMappings": NotRequired[
            Sequence[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]
        ],
        "ClassicLinkVpcId": NotRequired[str],
        "ClassicLinkVpcSecurityGroups": NotRequired[Sequence[str]],
        "CreatedTime": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[str],
        "ImageId": NotRequired[str],
        "InstanceMonitoring": NotRequired[
            AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "PlacementTenancy": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SpotPrice": NotRequired[str],
        "UserData": NotRequired[str],
        "MetadataOptions": NotRequired[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef],
    },
)
AwsBackupBackupPlanRuleDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleDetailsOutputTypeDef",
    {
        "TargetBackupVault": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "ScheduleExpression": NotRequired[str],
        "RuleName": NotRequired[str],
        "RuleId": NotRequired[str],
        "EnableContinuousBackup": NotRequired[bool],
        "CompletionWindowMinutes": NotRequired[int],
        "CopyActions": NotRequired[List[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]],
        "Lifecycle": NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef],
    },
)
AwsBackupBackupPlanRuleDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleDetailsTypeDef",
    {
        "TargetBackupVault": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "ScheduleExpression": NotRequired[str],
        "RuleName": NotRequired[str],
        "RuleId": NotRequired[str],
        "EnableContinuousBackup": NotRequired[bool],
        "CompletionWindowMinutes": NotRequired[int],
        "CopyActions": NotRequired[Sequence[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]],
        "Lifecycle": NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef],
    },
)
AwsBackupBackupVaultDetailsTypeDef = TypedDict(
    "AwsBackupBackupVaultDetailsTypeDef",
    {
        "BackupVaultArn": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "Notifications": NotRequired[AwsBackupBackupVaultNotificationsDetailsUnionTypeDef],
        "AccessPolicy": NotRequired[str],
    },
)
AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef",
    {
        "DomainValidationOptions": NotRequired[
            List[AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]
        ],
        "RenewalStatus": NotRequired[str],
        "RenewalStatusReason": NotRequired[str],
        "UpdatedAt": NotRequired[str],
    },
)
AwsCertificateManagerCertificateDomainValidationOptionUnionTypeDef = Union[
    AwsCertificateManagerCertificateDomainValidationOptionTypeDef,
    AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef,
]
AwsCertificateManagerCertificateRenewalSummaryTypeDef = TypedDict(
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    {
        "DomainValidationOptions": NotRequired[
            Sequence[AwsCertificateManagerCertificateDomainValidationOptionTypeDef]
        ],
        "RenewalStatus": NotRequired[str],
        "RenewalStatusReason": NotRequired[str],
        "UpdatedAt": NotRequired[str],
    },
)
AwsCloudFormationStackDetailsUnionTypeDef = Union[
    AwsCloudFormationStackDetailsTypeDef, AwsCloudFormationStackDetailsOutputTypeDef
]
AwsCloudFrontDistributionCacheBehaviorsUnionTypeDef = Union[
    AwsCloudFrontDistributionCacheBehaviorsTypeDef,
    AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef,
]
AwsCloudFrontDistributionOriginItemOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemOutputTypeDef",
    {
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "OriginPath": NotRequired[str],
        "S3OriginConfig": NotRequired[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef],
        "CustomOriginConfig": NotRequired[
            AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef
        ],
    },
)
AwsCloudFrontDistributionOriginGroupOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupOutputTypeDef",
    {
        "FailoverCriteria": NotRequired[AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    {
        "StatusCodes": NotRequired[
            AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnionTypeDef
        ],
    },
)
AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef",
    {
        "HttpPort": NotRequired[int],
        "HttpsPort": NotRequired[int],
        "OriginKeepaliveTimeout": NotRequired[int],
        "OriginProtocolPolicy": NotRequired[str],
        "OriginReadTimeout": NotRequired[int],
        "OriginSslProtocols": NotRequired[AwsCloudFrontDistributionOriginSslProtocolsUnionTypeDef],
    },
)
AwsCloudWatchAlarmDetailsUnionTypeDef = Union[
    AwsCloudWatchAlarmDetailsTypeDef, AwsCloudWatchAlarmDetailsOutputTypeDef
]
AwsCodeBuildProjectEnvironmentUnionTypeDef = Union[
    AwsCodeBuildProjectEnvironmentTypeDef, AwsCodeBuildProjectEnvironmentOutputTypeDef
]
AwsCodeBuildProjectDetailsOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsOutputTypeDef",
    {
        "EncryptionKey": NotRequired[str],
        "Artifacts": NotRequired[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]],
        "Environment": NotRequired[AwsCodeBuildProjectEnvironmentOutputTypeDef],
        "Name": NotRequired[str],
        "Source": NotRequired[AwsCodeBuildProjectSourceTypeDef],
        "ServiceRole": NotRequired[str],
        "LogsConfig": NotRequired[AwsCodeBuildProjectLogsConfigDetailsTypeDef],
        "VpcConfig": NotRequired[AwsCodeBuildProjectVpcConfigOutputTypeDef],
        "SecondaryArtifacts": NotRequired[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]],
    },
)
AwsApiGatewayV2ApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2ApiDetailsTypeDef",
    {
        "ApiEndpoint": NotRequired[str],
        "ApiId": NotRequired[str],
        "ApiKeySelectionExpression": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "Version": NotRequired[str],
        "Name": NotRequired[str],
        "ProtocolType": NotRequired[str],
        "RouteSelectionExpression": NotRequired[str],
        "CorsConfiguration": NotRequired[AwsCorsConfigurationUnionTypeDef],
    },
)
AwsDmsReplicationInstanceDetailsUnionTypeDef = Union[
    AwsDmsReplicationInstanceDetailsTypeDef, AwsDmsReplicationInstanceDetailsOutputTypeDef
]
AwsDynamoDbTableGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    {
        "Backfilling": NotRequired[bool],
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "IndexSizeBytes": NotRequired[int],
        "IndexStatus": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]],
        "Projection": NotRequired[AwsDynamoDbTableProjectionUnionTypeDef],
        "ProvisionedThroughput": NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef],
    },
)
AwsDynamoDbTableLocalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    {
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]],
        "Projection": NotRequired[AwsDynamoDbTableProjectionUnionTypeDef],
    },
)
AwsDynamoDbTableReplicaOutputTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaOutputTypeDef",
    {
        "GlobalSecondaryIndexes": NotRequired[
            List[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]
        ],
        "KmsMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
        ],
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[str],
        "ReplicaStatusDescription": NotRequired[str],
    },
)
AwsDynamoDbTableReplicaTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaTypeDef",
    {
        "GlobalSecondaryIndexes": NotRequired[
            Sequence[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]
        ],
        "KmsMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
        ],
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[str],
        "ReplicaStatusDescription": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointDetailsOutputTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointDetailsOutputTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Description": NotRequired[str],
        "ClientCidrBlock": NotRequired[str],
        "DnsServer": NotRequired[List[str]],
        "SplitTunnel": NotRequired[bool],
        "TransportProtocol": NotRequired[str],
        "VpnPort": NotRequired[int],
        "ServerCertificateArn": NotRequired[str],
        "AuthenticationOptions": NotRequired[
            List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]
        ],
        "ConnectionLogOptions": NotRequired[
            AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef
        ],
        "SecurityGroupIdSet": NotRequired[List[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortalUrl": NotRequired[str],
        "ClientConnectOptions": NotRequired[
            AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef
        ],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired[
            AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef
        ],
    },
)
AwsEc2ClientVpnEndpointDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointDetailsTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Description": NotRequired[str],
        "ClientCidrBlock": NotRequired[str],
        "DnsServer": NotRequired[Sequence[str]],
        "SplitTunnel": NotRequired[bool],
        "TransportProtocol": NotRequired[str],
        "VpnPort": NotRequired[int],
        "ServerCertificateArn": NotRequired[str],
        "AuthenticationOptions": NotRequired[
            Sequence[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]
        ],
        "ConnectionLogOptions": NotRequired[
            AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef
        ],
        "SecurityGroupIdSet": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortalUrl": NotRequired[str],
        "ClientConnectOptions": NotRequired[
            AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef
        ],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired[
            AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef
        ],
    },
)
AwsEc2InstanceDetailsUnionTypeDef = Union[
    AwsEc2InstanceDetailsTypeDef, AwsEc2InstanceDetailsOutputTypeDef
]
AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnionTypeDef = Union[
    AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef,
    AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef,
]
AwsEc2LaunchTemplateDataDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataDetailsOutputTypeDef",
    {
        "BlockDeviceMappingSet": NotRequired[
            List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]
        ],
        "CapacityReservationSpecification": NotRequired[
            AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef
        ],
        "CpuOptions": NotRequired[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef],
        "CreditSpecification": NotRequired[
            AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef
        ],
        "DisableApiStop": NotRequired[bool],
        "DisableApiTermination": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "ElasticGpuSpecificationSet": NotRequired[
            List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]
        ],
        "ElasticInferenceAcceleratorSet": NotRequired[
            List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]
        ],
        "EnclaveOptions": NotRequired[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef],
        "HibernationOptions": NotRequired[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef],
        "IamInstanceProfile": NotRequired[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef],
        "ImageId": NotRequired[str],
        "InstanceInitiatedShutdownBehavior": NotRequired[str],
        "InstanceMarketOptions": NotRequired[
            AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef
        ],
        "InstanceRequirements": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LicenseSet": NotRequired[List[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]],
        "MaintenanceOptions": NotRequired[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef],
        "MetadataOptions": NotRequired[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef],
        "Monitoring": NotRequired[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef],
        "NetworkInterfaceSet": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef]
        ],
        "Placement": NotRequired[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef],
        "PrivateDnsNameOptions": NotRequired[
            AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef
        ],
        "RamDiskId": NotRequired[str],
        "SecurityGroupIdSet": NotRequired[List[str]],
        "SecurityGroupSet": NotRequired[List[str]],
        "UserData": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnionTypeDef = Union[
    AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef,
    AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef,
]
AwsEc2NetworkAclDetailsOutputTypeDef = TypedDict(
    "AwsEc2NetworkAclDetailsOutputTypeDef",
    {
        "IsDefault": NotRequired[bool],
        "NetworkAclId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Associations": NotRequired[List[AwsEc2NetworkAclAssociationTypeDef]],
        "Entries": NotRequired[List[AwsEc2NetworkAclEntryTypeDef]],
    },
)
AwsEc2NetworkAclDetailsTypeDef = TypedDict(
    "AwsEc2NetworkAclDetailsTypeDef",
    {
        "IsDefault": NotRequired[bool],
        "NetworkAclId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Associations": NotRequired[Sequence[AwsEc2NetworkAclAssociationTypeDef]],
        "Entries": NotRequired[Sequence[AwsEc2NetworkAclEntryTypeDef]],
    },
)
AwsEc2NetworkInterfaceDetailsUnionTypeDef = Union[
    AwsEc2NetworkInterfaceDetailsTypeDef, AwsEc2NetworkInterfaceDetailsOutputTypeDef
]
AwsEc2SecurityGroupDetailsOutputTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsOutputTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "IpPermissions": NotRequired[List[AwsEc2SecurityGroupIpPermissionOutputTypeDef]],
        "IpPermissionsEgress": NotRequired[List[AwsEc2SecurityGroupIpPermissionOutputTypeDef]],
    },
)
AwsEc2SecurityGroupIpPermissionUnionTypeDef = Union[
    AwsEc2SecurityGroupIpPermissionTypeDef, AwsEc2SecurityGroupIpPermissionOutputTypeDef
]
AwsEc2SubnetDetailsUnionTypeDef = Union[
    AwsEc2SubnetDetailsTypeDef, AwsEc2SubnetDetailsOutputTypeDef
]
AwsEc2VolumeDetailsUnionTypeDef = Union[
    AwsEc2VolumeDetailsTypeDef, AwsEc2VolumeDetailsOutputTypeDef
]
AwsEc2VpcDetailsUnionTypeDef = Union[AwsEc2VpcDetailsTypeDef, AwsEc2VpcDetailsOutputTypeDef]
AwsEc2VpcEndpointServiceDetailsUnionTypeDef = Union[
    AwsEc2VpcEndpointServiceDetailsTypeDef, AwsEc2VpcEndpointServiceDetailsOutputTypeDef
]
AwsEc2VpcPeeringConnectionDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionDetailsOutputTypeDef",
    {
        "AccepterVpcInfo": NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef],
        "ExpirationTime": NotRequired[str],
        "RequesterVpcInfo": NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef],
        "Status": NotRequired[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
AwsEc2VpcPeeringConnectionVpcInfoDetailsUnionTypeDef = Union[
    AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef,
    AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef,
]
AwsEc2VpnConnectionDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsOutputTypeDef",
    {
        "VpnConnectionId": NotRequired[str],
        "State": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "CustomerGatewayConfiguration": NotRequired[str],
        "Type": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "VgwTelemetry": NotRequired[List[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]],
        "Options": NotRequired[AwsEc2VpnConnectionOptionsDetailsOutputTypeDef],
        "Routes": NotRequired[List[AwsEc2VpnConnectionRoutesDetailsTypeDef]],
        "TransitGatewayId": NotRequired[str],
    },
)
AwsEc2VpnConnectionOptionsDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    {
        "StaticRoutesOnly": NotRequired[bool],
        "TunnelOptions": NotRequired[
            Sequence[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnionTypeDef]
        ],
    },
)
AwsEcsClusterConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationDetailsTypeDef",
    {
        "ExecuteCommandConfiguration": NotRequired[
            AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef
        ],
    },
)
AwsEcsContainerDetailsUnionTypeDef = Union[
    AwsEcsContainerDetailsTypeDef, AwsEcsContainerDetailsOutputTypeDef
]
AwsEcsServiceDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceDetailsOutputTypeDef",
    {
        "CapacityProviderStrategy": NotRequired[
            List[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]
        ],
        "Cluster": NotRequired[str],
        "DeploymentConfiguration": NotRequired[AwsEcsServiceDeploymentConfigurationDetailsTypeDef],
        "DeploymentController": NotRequired[AwsEcsServiceDeploymentControllerDetailsTypeDef],
        "DesiredCount": NotRequired[int],
        "EnableEcsManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "HealthCheckGracePeriodSeconds": NotRequired[int],
        "LaunchType": NotRequired[str],
        "LoadBalancers": NotRequired[List[AwsEcsServiceLoadBalancersDetailsTypeDef]],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired[AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef],
        "PlacementConstraints": NotRequired[List[AwsEcsServicePlacementConstraintsDetailsTypeDef]],
        "PlacementStrategies": NotRequired[List[AwsEcsServicePlacementStrategiesDetailsTypeDef]],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[str],
        "Role": NotRequired[str],
        "SchedulingStrategy": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceRegistries": NotRequired[List[AwsEcsServiceServiceRegistriesDetailsTypeDef]],
        "TaskDefinition": NotRequired[str],
    },
)
AwsEcsServiceNetworkConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    {
        "AwsVpcConfiguration": NotRequired[
            AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnionTypeDef
        ],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    {
        "Capabilities": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnionTypeDef
        ],
        "Devices": NotRequired[
            Sequence[
                AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnionTypeDef
            ]
        ],
        "InitProcessEnabled": NotRequired[bool],
        "MaxSwap": NotRequired[int],
        "SharedMemorySize": NotRequired[int],
        "Swappiness": NotRequired[int],
        "Tmpfs": NotRequired[
            Sequence[
                AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnionTypeDef
            ]
        ],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef",
    {
        "Command": NotRequired[List[str]],
        "Cpu": NotRequired[int],
        "DependsOn": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]
        ],
        "DisableNetworking": NotRequired[bool],
        "DnsSearchDomains": NotRequired[List[str]],
        "DnsServers": NotRequired[List[str]],
        "DockerLabels": NotRequired[Dict[str, str]],
        "DockerSecurityOptions": NotRequired[List[str]],
        "EntryPoint": NotRequired[List[str]],
        "Environment": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]
        ],
        "EnvironmentFiles": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]
        ],
        "Essential": NotRequired[bool],
        "ExtraHosts": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]
        ],
        "FirelensConfiguration": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef
        ],
        "HealthCheck": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef
        ],
        "Hostname": NotRequired[str],
        "Image": NotRequired[str],
        "Interactive": NotRequired[bool],
        "Links": NotRequired[List[str]],
        "LinuxParameters": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef
        ],
        "LogConfiguration": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef
        ],
        "Memory": NotRequired[int],
        "MemoryReservation": NotRequired[int],
        "MountPoints": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]
        ],
        "Name": NotRequired[str],
        "PortMappings": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]
        ],
        "Privileged": NotRequired[bool],
        "PseudoTerminal": NotRequired[bool],
        "ReadonlyRootFilesystem": NotRequired[bool],
        "RepositoryCredentials": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef
        ],
        "ResourceRequirements": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]
        ],
        "Secrets": NotRequired[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]],
        "StartTimeout": NotRequired[int],
        "StopTimeout": NotRequired[int],
        "SystemControls": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]
        ],
        "Ulimits": NotRequired[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]],
        "User": NotRequired[str],
        "VolumesFrom": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]
        ],
        "WorkingDirectory": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionProxyConfigurationDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef,
    AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef",
    {
        "DockerVolumeConfiguration": NotRequired[
            AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef
        ],
        "EfsVolumeConfiguration": NotRequired[
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef
        ],
        "Host": NotRequired[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef],
        "Name": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    {
        "DockerVolumeConfiguration": NotRequired[
            AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnionTypeDef
        ],
        "EfsVolumeConfiguration": NotRequired[
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef
        ],
        "Host": NotRequired[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef],
        "Name": NotRequired[str],
    },
)
AwsEcsTaskDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDetailsOutputTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "TaskDefinitionArn": NotRequired[str],
        "Version": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "StartedAt": NotRequired[str],
        "StartedBy": NotRequired[str],
        "Group": NotRequired[str],
        "Volumes": NotRequired[List[AwsEcsTaskVolumeDetailsTypeDef]],
        "Containers": NotRequired[List[AwsEcsContainerDetailsOutputTypeDef]],
    },
)
AwsEfsAccessPointDetailsOutputTypeDef = TypedDict(
    "AwsEfsAccessPointDetailsOutputTypeDef",
    {
        "AccessPointId": NotRequired[str],
        "Arn": NotRequired[str],
        "ClientToken": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "PosixUser": NotRequired[AwsEfsAccessPointPosixUserDetailsOutputTypeDef],
        "RootDirectory": NotRequired[AwsEfsAccessPointRootDirectoryDetailsTypeDef],
    },
)
AwsEfsAccessPointDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointDetailsTypeDef",
    {
        "AccessPointId": NotRequired[str],
        "Arn": NotRequired[str],
        "ClientToken": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "PosixUser": NotRequired[AwsEfsAccessPointPosixUserDetailsUnionTypeDef],
        "RootDirectory": NotRequired[AwsEfsAccessPointRootDirectoryDetailsTypeDef],
    },
)
AwsEksClusterDetailsOutputTypeDef = TypedDict(
    "AwsEksClusterDetailsOutputTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityData": NotRequired[str],
        "ClusterStatus": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Name": NotRequired[str],
        "ResourcesVpcConfig": NotRequired[AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef],
        "RoleArn": NotRequired[str],
        "Version": NotRequired[str],
        "Logging": NotRequired[AwsEksClusterLoggingDetailsOutputTypeDef],
    },
)
AwsEksClusterLoggingDetailsTypeDef = TypedDict(
    "AwsEksClusterLoggingDetailsTypeDef",
    {
        "ClusterLogging": NotRequired[
            Sequence[AwsEksClusterLoggingClusterLoggingDetailsUnionTypeDef]
        ],
    },
)
AwsElasticBeanstalkEnvironmentDetailsUnionTypeDef = Union[
    AwsElasticBeanstalkEnvironmentDetailsTypeDef, AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef
]
AwsElasticsearchDomainDetailsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsOutputTypeDef",
    {
        "AccessPolicies": NotRequired[str],
        "DomainEndpointOptions": NotRequired[AwsElasticsearchDomainDomainEndpointOptionsTypeDef],
        "DomainId": NotRequired[str],
        "DomainName": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Endpoints": NotRequired[Dict[str, str]],
        "ElasticsearchVersion": NotRequired[str],
        "ElasticsearchClusterConfig": NotRequired[
            AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef
        ],
        "EncryptionAtRestOptions": NotRequired[
            AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef
        ],
        "LogPublishingOptions": NotRequired[AwsElasticsearchDomainLogPublishingOptionsTypeDef],
        "NodeToNodeEncryptionOptions": NotRequired[
            AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
        ],
        "ServiceSoftwareOptions": NotRequired[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef],
        "VPCOptions": NotRequired[AwsElasticsearchDomainVPCOptionsOutputTypeDef],
    },
)
AwsElasticsearchDomainDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsTypeDef",
    {
        "AccessPolicies": NotRequired[str],
        "DomainEndpointOptions": NotRequired[AwsElasticsearchDomainDomainEndpointOptionsTypeDef],
        "DomainId": NotRequired[str],
        "DomainName": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Endpoints": NotRequired[Mapping[str, str]],
        "ElasticsearchVersion": NotRequired[str],
        "ElasticsearchClusterConfig": NotRequired[
            AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef
        ],
        "EncryptionAtRestOptions": NotRequired[
            AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef
        ],
        "LogPublishingOptions": NotRequired[AwsElasticsearchDomainLogPublishingOptionsTypeDef],
        "NodeToNodeEncryptionOptions": NotRequired[
            AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
        ],
        "ServiceSoftwareOptions": NotRequired[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef],
        "VPCOptions": NotRequired[AwsElasticsearchDomainVPCOptionsUnionTypeDef],
    },
)
AwsElbLoadBalancerPoliciesUnionTypeDef = Union[
    AwsElbLoadBalancerPoliciesTypeDef, AwsElbLoadBalancerPoliciesOutputTypeDef
]
AwsElbLoadBalancerAttributesUnionTypeDef = Union[
    AwsElbLoadBalancerAttributesTypeDef, AwsElbLoadBalancerAttributesOutputTypeDef
]
AwsElbLoadBalancerDetailsOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerDetailsOutputTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "BackendServerDescriptions": NotRequired[
            List[AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef]
        ],
        "CanonicalHostedZoneName": NotRequired[str],
        "CanonicalHostedZoneNameID": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DnsName": NotRequired[str],
        "HealthCheck": NotRequired[AwsElbLoadBalancerHealthCheckTypeDef],
        "Instances": NotRequired[List[AwsElbLoadBalancerInstanceTypeDef]],
        "ListenerDescriptions": NotRequired[
            List[AwsElbLoadBalancerListenerDescriptionOutputTypeDef]
        ],
        "LoadBalancerAttributes": NotRequired[AwsElbLoadBalancerAttributesOutputTypeDef],
        "LoadBalancerName": NotRequired[str],
        "Policies": NotRequired[AwsElbLoadBalancerPoliciesOutputTypeDef],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "SourceSecurityGroup": NotRequired[AwsElbLoadBalancerSourceSecurityGroupTypeDef],
        "Subnets": NotRequired[List[str]],
        "VpcId": NotRequired[str],
    },
)
AwsElbLoadBalancerListenerDescriptionUnionTypeDef = Union[
    AwsElbLoadBalancerListenerDescriptionTypeDef, AwsElbLoadBalancerListenerDescriptionOutputTypeDef
]
AwsElbv2LoadBalancerDetailsUnionTypeDef = Union[
    AwsElbv2LoadBalancerDetailsTypeDef, AwsElbv2LoadBalancerDetailsOutputTypeDef
]
AwsEventsEndpointRoutingConfigDetailsTypeDef = TypedDict(
    "AwsEventsEndpointRoutingConfigDetailsTypeDef",
    {
        "FailoverConfig": NotRequired[AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef],
    },
)
AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef",
    {
        "ScanEc2InstanceWithFindings": NotRequired[
            AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef
        ],
        "ServiceRole": NotRequired[str],
    },
)
AwsIamAccessKeyDetailsTypeDef = TypedDict(
    "AwsIamAccessKeyDetailsTypeDef",
    {
        "UserName": NotRequired[str],
        "Status": NotRequired[AwsIamAccessKeyStatusType],
        "CreatedAt": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "PrincipalType": NotRequired[str],
        "PrincipalName": NotRequired[str],
        "AccountId": NotRequired[str],
        "AccessKeyId": NotRequired[str],
        "SessionContext": NotRequired[AwsIamAccessKeySessionContextTypeDef],
    },
)
AwsIamGroupDetailsUnionTypeDef = Union[AwsIamGroupDetailsTypeDef, AwsIamGroupDetailsOutputTypeDef]
AwsIamRoleDetailsOutputTypeDef = TypedDict(
    "AwsIamRoleDetailsOutputTypeDef",
    {
        "AssumeRolePolicyDocument": NotRequired[str],
        "AttachedManagedPolicies": NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "InstanceProfileList": NotRequired[List[AwsIamInstanceProfileOutputTypeDef]],
        "PermissionsBoundary": NotRequired[AwsIamPermissionsBoundaryTypeDef],
        "RoleId": NotRequired[str],
        "RoleName": NotRequired[str],
        "RolePolicyList": NotRequired[List[AwsIamRolePolicyTypeDef]],
        "MaxSessionDuration": NotRequired[int],
        "Path": NotRequired[str],
    },
)
AwsIamInstanceProfileUnionTypeDef = Union[
    AwsIamInstanceProfileTypeDef, AwsIamInstanceProfileOutputTypeDef
]
AwsIamPolicyDetailsUnionTypeDef = Union[
    AwsIamPolicyDetailsTypeDef, AwsIamPolicyDetailsOutputTypeDef
]
AwsIamUserDetailsUnionTypeDef = Union[AwsIamUserDetailsTypeDef, AwsIamUserDetailsOutputTypeDef]
AwsLambdaFunctionDetailsOutputTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsOutputTypeDef",
    {
        "Code": NotRequired[AwsLambdaFunctionCodeTypeDef],
        "CodeSha256": NotRequired[str],
        "DeadLetterConfig": NotRequired[AwsLambdaFunctionDeadLetterConfigTypeDef],
        "Environment": NotRequired[AwsLambdaFunctionEnvironmentOutputTypeDef],
        "FunctionName": NotRequired[str],
        "Handler": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "LastModified": NotRequired[str],
        "Layers": NotRequired[List[AwsLambdaFunctionLayerTypeDef]],
        "MasterArn": NotRequired[str],
        "MemorySize": NotRequired[int],
        "RevisionId": NotRequired[str],
        "Role": NotRequired[str],
        "Runtime": NotRequired[str],
        "Timeout": NotRequired[int],
        "TracingConfig": NotRequired[AwsLambdaFunctionTracingConfigTypeDef],
        "VpcConfig": NotRequired[AwsLambdaFunctionVpcConfigOutputTypeDef],
        "Version": NotRequired[str],
        "Architectures": NotRequired[List[str]],
        "PackageType": NotRequired[str],
    },
)
AwsLambdaFunctionEnvironmentUnionTypeDef = Union[
    AwsLambdaFunctionEnvironmentTypeDef, AwsLambdaFunctionEnvironmentOutputTypeDef
]
AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef",
    {
        "Sasl": NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef],
        "Unauthenticated": NotRequired[
            AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef
        ],
        "Tls": NotRequired[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef],
    },
)
AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef",
    {
        "Sasl": NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef],
        "Unauthenticated": NotRequired[
            AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef
        ],
        "Tls": NotRequired[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnionTypeDef],
    },
)
AwsNetworkFirewallFirewallDetailsUnionTypeDef = Union[
    AwsNetworkFirewallFirewallDetailsTypeDef, AwsNetworkFirewallFirewallDetailsOutputTypeDef
]
AwsOpenSearchServiceDomainDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDetailsOutputTypeDef",
    {
        "Arn": NotRequired[str],
        "AccessPolicies": NotRequired[str],
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "DomainEndpoint": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EncryptionAtRestOptions": NotRequired[
            AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef
        ],
        "NodeToNodeEncryptionOptions": NotRequired[
            AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef
        ],
        "ServiceSoftwareOptions": NotRequired[
            AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef
        ],
        "ClusterConfig": NotRequired[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef],
        "DomainEndpointOptions": NotRequired[
            AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef
        ],
        "VpcOptions": NotRequired[AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef],
        "LogPublishingOptions": NotRequired[
            AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef
        ],
        "DomainEndpoints": NotRequired[Dict[str, str]],
        "AdvancedSecurityOptions": NotRequired[
            AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef
        ],
    },
)
AwsOpenSearchServiceDomainDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "AccessPolicies": NotRequired[str],
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "DomainEndpoint": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EncryptionAtRestOptions": NotRequired[
            AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef
        ],
        "NodeToNodeEncryptionOptions": NotRequired[
            AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef
        ],
        "ServiceSoftwareOptions": NotRequired[
            AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef
        ],
        "ClusterConfig": NotRequired[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef],
        "DomainEndpointOptions": NotRequired[
            AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef
        ],
        "VpcOptions": NotRequired[AwsOpenSearchServiceDomainVpcOptionsDetailsUnionTypeDef],
        "LogPublishingOptions": NotRequired[
            AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef
        ],
        "DomainEndpoints": NotRequired[Mapping[str, str]],
        "AdvancedSecurityOptions": NotRequired[
            AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef
        ],
    },
)
AwsRdsDbClusterDetailsUnionTypeDef = Union[
    AwsRdsDbClusterDetailsTypeDef, AwsRdsDbClusterDetailsOutputTypeDef
]
AwsRdsDbClusterSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterSnapshotIdentifier": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "DbClusterSnapshotAttributes": NotRequired[
            Sequence[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnionTypeDef]
        ],
    },
)
AwsRdsDbSnapshotDetailsUnionTypeDef = Union[
    AwsRdsDbSnapshotDetailsTypeDef, AwsRdsDbSnapshotDetailsOutputTypeDef
]
AwsRdsDbSecurityGroupDetailsUnionTypeDef = Union[
    AwsRdsDbSecurityGroupDetailsTypeDef, AwsRdsDbSecurityGroupDetailsOutputTypeDef
]
AwsRdsDbSubnetGroupOutputTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupOutputTypeDef",
    {
        "DbSubnetGroupName": NotRequired[str],
        "DbSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[List[AwsRdsDbSubnetGroupSubnetTypeDef]],
        "DbSubnetGroupArn": NotRequired[str],
    },
)
AwsRdsDbSubnetGroupTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupTypeDef",
    {
        "DbSubnetGroupName": NotRequired[str],
        "DbSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[Sequence[AwsRdsDbSubnetGroupSubnetTypeDef]],
        "DbSubnetGroupArn": NotRequired[str],
    },
)
AwsRdsDbPendingModifiedValuesTypeDef = TypedDict(
    "AwsRdsDbPendingModifiedValuesTypeDef",
    {
        "DbInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "Port": NotRequired[int],
        "BackupRetentionPeriod": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "DbInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "CaCertificateIdentifier": NotRequired[str],
        "DbSubnetGroupName": NotRequired[str],
        "PendingCloudWatchLogsExports": NotRequired[AwsRdsPendingCloudWatchLogsExportsUnionTypeDef],
        "ProcessorFeatures": NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]],
    },
)
AwsRedshiftClusterDetailsOutputTypeDef = TypedDict(
    "AwsRedshiftClusterDetailsOutputTypeDef",
    {
        "AllowVersionUpgrade": NotRequired[bool],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "ClusterAvailabilityStatus": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "ClusterNodes": NotRequired[List[AwsRedshiftClusterClusterNodeTypeDef]],
        "ClusterParameterGroups": NotRequired[
            List[AwsRedshiftClusterClusterParameterGroupOutputTypeDef]
        ],
        "ClusterPublicKey": NotRequired[str],
        "ClusterRevisionNumber": NotRequired[str],
        "ClusterSecurityGroups": NotRequired[List[AwsRedshiftClusterClusterSecurityGroupTypeDef]],
        "ClusterSnapshotCopyStatus": NotRequired[
            AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef
        ],
        "ClusterStatus": NotRequired[str],
        "ClusterSubnetGroupName": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "DBName": NotRequired[str],
        "DeferredMaintenanceWindows": NotRequired[
            List[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]
        ],
        "ElasticIpStatus": NotRequired[AwsRedshiftClusterElasticIpStatusTypeDef],
        "ElasticResizeNumberOfNodeOptions": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Endpoint": NotRequired[AwsRedshiftClusterEndpointTypeDef],
        "EnhancedVpcRouting": NotRequired[bool],
        "ExpectedNextSnapshotScheduleTime": NotRequired[str],
        "ExpectedNextSnapshotScheduleTimeStatus": NotRequired[str],
        "HsmStatus": NotRequired[AwsRedshiftClusterHsmStatusTypeDef],
        "IamRoles": NotRequired[List[AwsRedshiftClusterIamRoleTypeDef]],
        "KmsKeyId": NotRequired[str],
        "MaintenanceTrackName": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "NextMaintenanceWindowStartTime": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "PendingActions": NotRequired[List[str]],
        "PendingModifiedValues": NotRequired[AwsRedshiftClusterPendingModifiedValuesTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ResizeInfo": NotRequired[AwsRedshiftClusterResizeInfoTypeDef],
        "RestoreStatus": NotRequired[AwsRedshiftClusterRestoreStatusTypeDef],
        "SnapshotScheduleIdentifier": NotRequired[str],
        "SnapshotScheduleState": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcSecurityGroups": NotRequired[List[AwsRedshiftClusterVpcSecurityGroupTypeDef]],
        "LoggingStatus": NotRequired[AwsRedshiftClusterLoggingStatusTypeDef],
    },
)
AwsRedshiftClusterClusterParameterGroupUnionTypeDef = Union[
    AwsRedshiftClusterClusterParameterGroupTypeDef,
    AwsRedshiftClusterClusterParameterGroupOutputTypeDef,
]
AwsRoute53HostedZoneDetailsOutputTypeDef = TypedDict(
    "AwsRoute53HostedZoneDetailsOutputTypeDef",
    {
        "HostedZone": NotRequired[AwsRoute53HostedZoneObjectDetailsTypeDef],
        "Vpcs": NotRequired[List[AwsRoute53HostedZoneVpcDetailsTypeDef]],
        "NameServers": NotRequired[List[str]],
        "QueryLoggingConfig": NotRequired[AwsRoute53QueryLoggingConfigDetailsTypeDef],
    },
)
AwsRoute53HostedZoneDetailsTypeDef = TypedDict(
    "AwsRoute53HostedZoneDetailsTypeDef",
    {
        "HostedZone": NotRequired[AwsRoute53HostedZoneObjectDetailsTypeDef],
        "Vpcs": NotRequired[Sequence[AwsRoute53HostedZoneVpcDetailsTypeDef]],
        "NameServers": NotRequired[Sequence[str]],
        "QueryLoggingConfig": NotRequired[AwsRoute53QueryLoggingConfigDetailsTypeDef],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef",
    {
        "Operands": NotRequired[
            List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]
        ],
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    {
        "Operands": NotRequired[
            Sequence[
                AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef
            ]
        ],
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsS3BucketNotificationConfigurationFilterOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationFilterOutputTypeDef",
    {
        "S3KeyFilter": NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef],
    },
)
AwsS3BucketNotificationConfigurationS3KeyFilterUnionTypeDef = Union[
    AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef,
    AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef,
]
AwsS3BucketObjectLockConfigurationTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": NotRequired[str],
        "Rule": NotRequired[AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef],
    },
)
AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef",
    {
        "Rules": NotRequired[List[AwsS3BucketServerSideEncryptionRuleTypeDef]],
    },
)
AwsS3BucketServerSideEncryptionConfigurationTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": NotRequired[Sequence[AwsS3BucketServerSideEncryptionRuleTypeDef]],
    },
)
AwsS3BucketWebsiteConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationOutputTypeDef",
    {
        "ErrorDocument": NotRequired[str],
        "IndexDocumentSuffix": NotRequired[str],
        "RedirectAllRequestsTo": NotRequired[AwsS3BucketWebsiteConfigurationRedirectToTypeDef],
        "RoutingRules": NotRequired[List[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]],
    },
)
AwsS3BucketWebsiteConfigurationTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": NotRequired[str],
        "IndexDocumentSuffix": NotRequired[str],
        "RedirectAllRequestsTo": NotRequired[AwsS3BucketWebsiteConfigurationRedirectToTypeDef],
        "RoutingRules": NotRequired[Sequence[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]],
    },
)
AwsSageMakerNotebookInstanceDetailsUnionTypeDef = Union[
    AwsSageMakerNotebookInstanceDetailsTypeDef, AwsSageMakerNotebookInstanceDetailsOutputTypeDef
]
BatchUpdateFindingsResponseTypeDef = TypedDict(
    "BatchUpdateFindingsResponseTypeDef",
    {
        "ProcessedFindings": List[AwsSecurityFindingIdentifierTypeDef],
        "UnprocessedFindings": List[BatchUpdateFindingsUnprocessedFindingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AwsSnsTopicDetailsUnionTypeDef = Union[AwsSnsTopicDetailsTypeDef, AwsSnsTopicDetailsOutputTypeDef]
AwsSsmPatchComplianceDetailsTypeDef = TypedDict(
    "AwsSsmPatchComplianceDetailsTypeDef",
    {
        "Patch": NotRequired[AwsSsmPatchTypeDef],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef",
    {
        "Destinations": NotRequired[
            List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]
        ],
        "IncludeExecutionData": NotRequired[bool],
        "Level": NotRequired[str],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef",
    {
        "Destinations": NotRequired[
            Sequence[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]
        ],
        "IncludeExecutionData": NotRequired[bool],
        "Level": NotRequired[str],
    },
)
AwsWafRateBasedRuleDetailsUnionTypeDef = Union[
    AwsWafRateBasedRuleDetailsTypeDef, AwsWafRateBasedRuleDetailsOutputTypeDef
]
AwsWafRegionalRateBasedRuleDetailsUnionTypeDef = Union[
    AwsWafRegionalRateBasedRuleDetailsTypeDef, AwsWafRegionalRateBasedRuleDetailsOutputTypeDef
]
AwsWafRegionalRuleDetailsUnionTypeDef = Union[
    AwsWafRegionalRuleDetailsTypeDef, AwsWafRegionalRuleDetailsOutputTypeDef
]
AwsWafRegionalRuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupDetailsOutputTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "Rules": NotRequired[List[AwsWafRegionalRuleGroupRulesDetailsTypeDef]],
    },
)
AwsWafRegionalRuleGroupDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafRegionalRuleGroupRulesDetailsTypeDef]],
    },
)
AwsWafRegionalWebAclDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalWebAclDetailsOutputTypeDef",
    {
        "DefaultAction": NotRequired[str],
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RulesList": NotRequired[List[AwsWafRegionalWebAclRulesListDetailsTypeDef]],
        "WebAclId": NotRequired[str],
    },
)
AwsWafRegionalWebAclDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclDetailsTypeDef",
    {
        "DefaultAction": NotRequired[str],
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RulesList": NotRequired[Sequence[AwsWafRegionalWebAclRulesListDetailsTypeDef]],
        "WebAclId": NotRequired[str],
    },
)
AwsWafRuleDetailsUnionTypeDef = Union[AwsWafRuleDetailsTypeDef, AwsWafRuleDetailsOutputTypeDef]
AwsWafRuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsWafRuleGroupDetailsOutputTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "Rules": NotRequired[List[AwsWafRuleGroupRulesDetailsTypeDef]],
    },
)
AwsWafRuleGroupDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafRuleGroupRulesDetailsTypeDef]],
    },
)
AwsWafWebAclDetailsOutputTypeDef = TypedDict(
    "AwsWafWebAclDetailsOutputTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultAction": NotRequired[str],
        "Rules": NotRequired[List[AwsWafWebAclRuleOutputTypeDef]],
        "WebAclId": NotRequired[str],
    },
)
AwsWafWebAclRuleUnionTypeDef = Union[AwsWafWebAclRuleTypeDef, AwsWafWebAclRuleOutputTypeDef]
AwsWafv2ActionAllowDetailsOutputTypeDef = TypedDict(
    "AwsWafv2ActionAllowDetailsOutputTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef],
    },
)
AwsWafv2RulesActionCaptchaDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RulesActionCaptchaDetailsOutputTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef],
    },
)
AwsWafv2RulesActionCountDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RulesActionCountDetailsOutputTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef],
    },
)
AwsWafv2CustomRequestHandlingDetailsUnionTypeDef = Union[
    AwsWafv2CustomRequestHandlingDetailsTypeDef, AwsWafv2CustomRequestHandlingDetailsOutputTypeDef
]
AwsWafv2ActionBlockDetailsOutputTypeDef = TypedDict(
    "AwsWafv2ActionBlockDetailsOutputTypeDef",
    {
        "CustomResponse": NotRequired[AwsWafv2CustomResponseDetailsOutputTypeDef],
    },
)
AwsWafv2CustomResponseDetailsUnionTypeDef = Union[
    AwsWafv2CustomResponseDetailsTypeDef, AwsWafv2CustomResponseDetailsOutputTypeDef
]
BatchGetStandardsControlAssociationsResponseTypeDef = TypedDict(
    "BatchGetStandardsControlAssociationsResponseTypeDef",
    {
        "StandardsControlAssociationDetails": List[StandardsControlAssociationDetailTypeDef],
        "UnprocessedAssociations": List[UnprocessedStandardsControlAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateStandardsControlAssociationsResponseTypeDef = TypedDict(
    "BatchUpdateStandardsControlAssociationsResponseTypeDef",
    {
        "UnprocessedAssociationUpdates": List[UnprocessedStandardsControlAssociationUpdateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VulnerabilityOutputTypeDef = TypedDict(
    "VulnerabilityOutputTypeDef",
    {
        "Id": str,
        "VulnerablePackages": NotRequired[List[SoftwarePackageTypeDef]],
        "Cvss": NotRequired[List[CvssOutputTypeDef]],
        "RelatedVulnerabilities": NotRequired[List[str]],
        "Vendor": NotRequired[VulnerabilityVendorTypeDef],
        "ReferenceUrls": NotRequired[List[str]],
        "FixAvailable": NotRequired[VulnerabilityFixAvailableType],
        "EpssScore": NotRequired[float],
        "ExploitAvailable": NotRequired[VulnerabilityExploitAvailableType],
        "LastKnownExploitAt": NotRequired[str],
        "CodeVulnerabilities": NotRequired[List[VulnerabilityCodeVulnerabilitiesOutputTypeDef]],
    },
)
VulnerabilityCodeVulnerabilitiesUnionTypeDef = Union[
    VulnerabilityCodeVulnerabilitiesTypeDef, VulnerabilityCodeVulnerabilitiesOutputTypeDef
]
ParameterDefinitionTypeDef = TypedDict(
    "ParameterDefinitionTypeDef",
    {
        "Description": str,
        "ConfigurationOptions": ConfigurationOptionsTypeDef,
    },
)
BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef = TypedDict(
    "BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef",
    {
        "ConfigurationPolicyAssociationIdentifiers": Sequence[
            ConfigurationPolicyAssociationTypeDef
        ],
    },
)
UnprocessedConfigurationPolicyAssociationTypeDef = TypedDict(
    "UnprocessedConfigurationPolicyAssociationTypeDef",
    {
        "ConfigurationPolicyAssociationIdentifiers": NotRequired[
            ConfigurationPolicyAssociationTypeDef
        ],
        "ErrorCode": NotRequired[str],
        "ErrorReason": NotRequired[str],
    },
)
ContainerDetailsUnionTypeDef = Union[ContainerDetailsTypeDef, ContainerDetailsOutputTypeDef]
AutomationRulesFindingFiltersOutputTypeDef = TypedDict(
    "AutomationRulesFindingFiltersOutputTypeDef",
    {
        "ProductArn": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[List[StringFilterTypeDef]],
        "Id": NotRequired[List[StringFilterTypeDef]],
        "GeneratorId": NotRequired[List[StringFilterTypeDef]],
        "Type": NotRequired[List[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[List[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[List[DateFilterTypeDef]],
        "CreatedAt": NotRequired[List[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "Confidence": NotRequired[List[NumberFilterTypeDef]],
        "Criticality": NotRequired[List[NumberFilterTypeDef]],
        "Title": NotRequired[List[StringFilterTypeDef]],
        "Description": NotRequired[List[StringFilterTypeDef]],
        "SourceUrl": NotRequired[List[StringFilterTypeDef]],
        "ProductName": NotRequired[List[StringFilterTypeDef]],
        "CompanyName": NotRequired[List[StringFilterTypeDef]],
        "SeverityLabel": NotRequired[List[StringFilterTypeDef]],
        "ResourceType": NotRequired[List[StringFilterTypeDef]],
        "ResourceId": NotRequired[List[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[List[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[List[StringFilterTypeDef]],
        "ResourceTags": NotRequired[List[MapFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[List[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[List[StringFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[List[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[List[StringFilterTypeDef]],
        "VerificationState": NotRequired[List[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[List[StringFilterTypeDef]],
        "RecordState": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[List[StringFilterTypeDef]],
        "NoteText": NotRequired[List[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[List[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[List[MapFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[List[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[List[StringFilterTypeDef]],
    },
)
AutomationRulesFindingFiltersTypeDef = TypedDict(
    "AutomationRulesFindingFiltersTypeDef",
    {
        "ProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[Sequence[StringFilterTypeDef]],
        "Id": NotRequired[Sequence[StringFilterTypeDef]],
        "GeneratorId": NotRequired[Sequence[StringFilterTypeDef]],
        "Type": NotRequired[Sequence[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "CreatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "Confidence": NotRequired[Sequence[NumberFilterTypeDef]],
        "Criticality": NotRequired[Sequence[NumberFilterTypeDef]],
        "Title": NotRequired[Sequence[StringFilterTypeDef]],
        "Description": NotRequired[Sequence[StringFilterTypeDef]],
        "SourceUrl": NotRequired[Sequence[StringFilterTypeDef]],
        "ProductName": NotRequired[Sequence[StringFilterTypeDef]],
        "CompanyName": NotRequired[Sequence[StringFilterTypeDef]],
        "SeverityLabel": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceType": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceTags": NotRequired[Sequence[MapFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[Sequence[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[Sequence[StringFilterTypeDef]],
        "VerificationState": NotRequired[Sequence[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "RecordState": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteText": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[Sequence[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[Sequence[MapFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[Sequence[StringFilterTypeDef]],
    },
)
AwsSecurityFindingFiltersOutputTypeDef = TypedDict(
    "AwsSecurityFindingFiltersOutputTypeDef",
    {
        "ProductArn": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[List[StringFilterTypeDef]],
        "Id": NotRequired[List[StringFilterTypeDef]],
        "GeneratorId": NotRequired[List[StringFilterTypeDef]],
        "Region": NotRequired[List[StringFilterTypeDef]],
        "Type": NotRequired[List[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[List[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[List[DateFilterTypeDef]],
        "CreatedAt": NotRequired[List[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "SeverityProduct": NotRequired[List[NumberFilterTypeDef]],
        "SeverityNormalized": NotRequired[List[NumberFilterTypeDef]],
        "SeverityLabel": NotRequired[List[StringFilterTypeDef]],
        "Confidence": NotRequired[List[NumberFilterTypeDef]],
        "Criticality": NotRequired[List[NumberFilterTypeDef]],
        "Title": NotRequired[List[StringFilterTypeDef]],
        "Description": NotRequired[List[StringFilterTypeDef]],
        "RecommendationText": NotRequired[List[StringFilterTypeDef]],
        "SourceUrl": NotRequired[List[StringFilterTypeDef]],
        "ProductFields": NotRequired[List[MapFilterTypeDef]],
        "ProductName": NotRequired[List[StringFilterTypeDef]],
        "CompanyName": NotRequired[List[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[List[MapFilterTypeDef]],
        "MalwareName": NotRequired[List[StringFilterTypeDef]],
        "MalwareType": NotRequired[List[StringFilterTypeDef]],
        "MalwarePath": NotRequired[List[StringFilterTypeDef]],
        "MalwareState": NotRequired[List[StringFilterTypeDef]],
        "NetworkDirection": NotRequired[List[StringFilterTypeDef]],
        "NetworkProtocol": NotRequired[List[StringFilterTypeDef]],
        "NetworkSourceIpV4": NotRequired[List[IpFilterTypeDef]],
        "NetworkSourceIpV6": NotRequired[List[IpFilterTypeDef]],
        "NetworkSourcePort": NotRequired[List[NumberFilterTypeDef]],
        "NetworkSourceDomain": NotRequired[List[StringFilterTypeDef]],
        "NetworkSourceMac": NotRequired[List[StringFilterTypeDef]],
        "NetworkDestinationIpV4": NotRequired[List[IpFilterTypeDef]],
        "NetworkDestinationIpV6": NotRequired[List[IpFilterTypeDef]],
        "NetworkDestinationPort": NotRequired[List[NumberFilterTypeDef]],
        "NetworkDestinationDomain": NotRequired[List[StringFilterTypeDef]],
        "ProcessName": NotRequired[List[StringFilterTypeDef]],
        "ProcessPath": NotRequired[List[StringFilterTypeDef]],
        "ProcessPid": NotRequired[List[NumberFilterTypeDef]],
        "ProcessParentPid": NotRequired[List[NumberFilterTypeDef]],
        "ProcessLaunchedAt": NotRequired[List[DateFilterTypeDef]],
        "ProcessTerminatedAt": NotRequired[List[DateFilterTypeDef]],
        "ThreatIntelIndicatorType": NotRequired[List[StringFilterTypeDef]],
        "ThreatIntelIndicatorValue": NotRequired[List[StringFilterTypeDef]],
        "ThreatIntelIndicatorCategory": NotRequired[List[StringFilterTypeDef]],
        "ThreatIntelIndicatorLastObservedAt": NotRequired[List[DateFilterTypeDef]],
        "ThreatIntelIndicatorSource": NotRequired[List[StringFilterTypeDef]],
        "ThreatIntelIndicatorSourceUrl": NotRequired[List[StringFilterTypeDef]],
        "ResourceType": NotRequired[List[StringFilterTypeDef]],
        "ResourceId": NotRequired[List[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[List[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[List[StringFilterTypeDef]],
        "ResourceTags": NotRequired[List[MapFilterTypeDef]],
        "ResourceAwsEc2InstanceType": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceImageId": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV4Addresses": NotRequired[List[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV6Addresses": NotRequired[List[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceKeyName": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceVpcId": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceSubnetId": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceLaunchedAt": NotRequired[List[DateFilterTypeDef]],
        "ResourceAwsS3BucketOwnerId": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsS3BucketOwnerName": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyUserName": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyPrincipalName": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyStatus": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyCreatedAt": NotRequired[List[DateFilterTypeDef]],
        "ResourceAwsIamUserUserName": NotRequired[List[StringFilterTypeDef]],
        "ResourceContainerName": NotRequired[List[StringFilterTypeDef]],
        "ResourceContainerImageId": NotRequired[List[StringFilterTypeDef]],
        "ResourceContainerImageName": NotRequired[List[StringFilterTypeDef]],
        "ResourceContainerLaunchedAt": NotRequired[List[DateFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[List[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[List[StringFilterTypeDef]],
        "VerificationState": NotRequired[List[StringFilterTypeDef]],
        "WorkflowState": NotRequired[List[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[List[StringFilterTypeDef]],
        "RecordState": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[List[StringFilterTypeDef]],
        "NoteText": NotRequired[List[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[List[StringFilterTypeDef]],
        "Keyword": NotRequired[List[KeywordFilterTypeDef]],
        "FindingProviderFieldsConfidence": NotRequired[List[NumberFilterTypeDef]],
        "FindingProviderFieldsCriticality": NotRequired[List[NumberFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsId": NotRequired[List[StringFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsProductArn": NotRequired[List[StringFilterTypeDef]],
        "FindingProviderFieldsSeverityLabel": NotRequired[List[StringFilterTypeDef]],
        "FindingProviderFieldsSeverityOriginal": NotRequired[List[StringFilterTypeDef]],
        "FindingProviderFieldsTypes": NotRequired[List[StringFilterTypeDef]],
        "Sample": NotRequired[List[BooleanFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[List[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[List[StringFilterTypeDef]],
        "VulnerabilitiesExploitAvailable": NotRequired[List[StringFilterTypeDef]],
        "VulnerabilitiesFixAvailable": NotRequired[List[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersName": NotRequired[List[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersValue": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[List[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[List[StringFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[List[StringFilterTypeDef]],
    },
)
AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[Sequence[StringFilterTypeDef]],
        "Id": NotRequired[Sequence[StringFilterTypeDef]],
        "GeneratorId": NotRequired[Sequence[StringFilterTypeDef]],
        "Region": NotRequired[Sequence[StringFilterTypeDef]],
        "Type": NotRequired[Sequence[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "CreatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "SeverityProduct": NotRequired[Sequence[NumberFilterTypeDef]],
        "SeverityNormalized": NotRequired[Sequence[NumberFilterTypeDef]],
        "SeverityLabel": NotRequired[Sequence[StringFilterTypeDef]],
        "Confidence": NotRequired[Sequence[NumberFilterTypeDef]],
        "Criticality": NotRequired[Sequence[NumberFilterTypeDef]],
        "Title": NotRequired[Sequence[StringFilterTypeDef]],
        "Description": NotRequired[Sequence[StringFilterTypeDef]],
        "RecommendationText": NotRequired[Sequence[StringFilterTypeDef]],
        "SourceUrl": NotRequired[Sequence[StringFilterTypeDef]],
        "ProductFields": NotRequired[Sequence[MapFilterTypeDef]],
        "ProductName": NotRequired[Sequence[StringFilterTypeDef]],
        "CompanyName": NotRequired[Sequence[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[Sequence[MapFilterTypeDef]],
        "MalwareName": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwareType": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwarePath": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwareState": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkDirection": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkProtocol": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkSourceIpV4": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkSourceIpV6": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkSourcePort": NotRequired[Sequence[NumberFilterTypeDef]],
        "NetworkSourceDomain": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkSourceMac": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkDestinationIpV4": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkDestinationIpV6": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkDestinationPort": NotRequired[Sequence[NumberFilterTypeDef]],
        "NetworkDestinationDomain": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessName": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessPath": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessPid": NotRequired[Sequence[NumberFilterTypeDef]],
        "ProcessParentPid": NotRequired[Sequence[NumberFilterTypeDef]],
        "ProcessLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ProcessTerminatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ThreatIntelIndicatorType": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorValue": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorCategory": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorLastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ThreatIntelIndicatorSource": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorSourceUrl": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceType": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceTags": NotRequired[Sequence[MapFilterTypeDef]],
        "ResourceAwsEc2InstanceType": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceImageId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV4Addresses": NotRequired[Sequence[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV6Addresses": NotRequired[Sequence[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceKeyName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceVpcId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceSubnetId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceAwsS3BucketOwnerId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsS3BucketOwnerName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyUserName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyPrincipalName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyCreatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceAwsIamUserUserName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerImageId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerImageName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[Sequence[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "VerificationState": NotRequired[Sequence[StringFilterTypeDef]],
        "WorkflowState": NotRequired[Sequence[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "RecordState": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteText": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[Sequence[StringFilterTypeDef]],
        "Keyword": NotRequired[Sequence[KeywordFilterTypeDef]],
        "FindingProviderFieldsConfidence": NotRequired[Sequence[NumberFilterTypeDef]],
        "FindingProviderFieldsCriticality": NotRequired[Sequence[NumberFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsId": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsProductArn": NotRequired[
            Sequence[StringFilterTypeDef]
        ],
        "FindingProviderFieldsSeverityLabel": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsSeverityOriginal": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsTypes": NotRequired[Sequence[StringFilterTypeDef]],
        "Sample": NotRequired[Sequence[BooleanFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[Sequence[StringFilterTypeDef]],
        "VulnerabilitiesExploitAvailable": NotRequired[Sequence[StringFilterTypeDef]],
        "VulnerabilitiesFixAvailable": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersName": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersValue": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[Sequence[StringFilterTypeDef]],
    },
)
ThreatUnionTypeDef = Union[ThreatTypeDef, ThreatOutputTypeDef]
GetFindingHistoryResponseTypeDef = TypedDict(
    "GetFindingHistoryResponseTypeDef",
    {
        "Records": List[FindingHistoryRecordTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FindingProviderFieldsUnionTypeDef = Union[
    FindingProviderFieldsTypeDef, FindingProviderFieldsOutputTypeDef
]
GetInsightResultsResponseTypeDef = TypedDict(
    "GetInsightResultsResponseTypeDef",
    {
        "InsightResults": InsightResultsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkHeaderOutputTypeDef = TypedDict(
    "NetworkHeaderOutputTypeDef",
    {
        "Protocol": NotRequired[str],
        "Destination": NotRequired[NetworkPathComponentDetailsOutputTypeDef],
        "Source": NotRequired[NetworkPathComponentDetailsOutputTypeDef],
    },
)
NetworkPathComponentDetailsUnionTypeDef = Union[
    NetworkPathComponentDetailsTypeDef, NetworkPathComponentDetailsOutputTypeDef
]
OccurrencesOutputTypeDef = TypedDict(
    "OccurrencesOutputTypeDef",
    {
        "LineRanges": NotRequired[List[RangeTypeDef]],
        "OffsetRanges": NotRequired[List[RangeTypeDef]],
        "Pages": NotRequired[List[PageTypeDef]],
        "Records": NotRequired[List[RecordTypeDef]],
        "Cells": NotRequired[List[CellTypeDef]],
    },
)
OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "LineRanges": NotRequired[Sequence[RangeTypeDef]],
        "OffsetRanges": NotRequired[Sequence[RangeTypeDef]],
        "Pages": NotRequired[Sequence[PageTypeDef]],
        "Records": NotRequired[Sequence[RecordTypeDef]],
        "Cells": NotRequired[Sequence[CellTypeDef]],
    },
)
SecurityControlCustomParameterOutputTypeDef = TypedDict(
    "SecurityControlCustomParameterOutputTypeDef",
    {
        "SecurityControlId": NotRequired[str],
        "Parameters": NotRequired[Dict[str, ParameterConfigurationOutputTypeDef]],
    },
)
SecurityControlTypeDef = TypedDict(
    "SecurityControlTypeDef",
    {
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": SeverityRatingType,
        "SecurityControlStatus": ControlStatusType,
        "UpdateStatus": NotRequired[UpdateStatusType],
        "Parameters": NotRequired[Dict[str, ParameterConfigurationOutputTypeDef]],
        "LastUpdateReason": NotRequired[str],
    },
)
ParameterConfigurationTypeDef = TypedDict(
    "ParameterConfigurationTypeDef",
    {
        "ValueType": ParameterValueTypeType,
        "Value": NotRequired[ParameterValueUnionTypeDef],
    },
)
RuleGroupSourceStatefulRulesDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    {
        "Action": NotRequired[str],
        "Header": NotRequired[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef],
        "RuleOptions": NotRequired[
            Sequence[RuleGroupSourceStatefulRulesOptionsDetailsUnionTypeDef]
        ],
    },
)
RuleGroupSourceStatelessRuleDefinitionOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleDefinitionOutputTypeDef",
    {
        "Actions": NotRequired[List[str]],
        "MatchAttributes": NotRequired[RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    {
        "DestinationPorts": NotRequired[
            Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]
        ],
        "Destinations": NotRequired[
            Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]
        ],
        "Protocols": NotRequired[Sequence[int]],
        "SourcePorts": NotRequired[
            Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]
        ],
        "Sources": NotRequired[Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]],
        "TcpFlags": NotRequired[
            Sequence[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnionTypeDef]
        ],
    },
)
RuleGroupVariablesTypeDef = TypedDict(
    "RuleGroupVariablesTypeDef",
    {
        "IpSets": NotRequired[RuleGroupVariablesIpSetsDetailsUnionTypeDef],
        "PortSets": NotRequired[RuleGroupVariablesPortSetsDetailsUnionTypeDef],
    },
)
ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "Status": NotRequired[ComplianceStatusType],
        "RelatedRequirements": NotRequired[Sequence[str]],
        "StatusReasons": NotRequired[Sequence[StatusReasonTypeDef]],
        "SecurityControlId": NotRequired[str],
        "AssociatedStandards": NotRequired[Sequence[AssociatedStandardTypeDef]],
        "SecurityControlParameters": NotRequired[Sequence[SecurityControlParameterUnionTypeDef]],
    },
)
DescribeStandardsResponseTypeDef = TypedDict(
    "DescribeStandardsResponseTypeDef",
    {
        "Standards": List[StandardTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchDisableStandardsResponseTypeDef = TypedDict(
    "BatchDisableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchEnableStandardsResponseTypeDef = TypedDict(
    "BatchEnableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnabledStandardsResponseTypeDef = TypedDict(
    "GetEnabledStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StatelessCustomActionDefinitionOutputTypeDef = TypedDict(
    "StatelessCustomActionDefinitionOutputTypeDef",
    {
        "PublishMetricAction": NotRequired[StatelessCustomPublishMetricActionOutputTypeDef],
    },
)
StatelessCustomPublishMetricActionUnionTypeDef = Union[
    StatelessCustomPublishMetricActionTypeDef, StatelessCustomPublishMetricActionOutputTypeDef
]
AwsApiCallActionUnionTypeDef = Union[AwsApiCallActionTypeDef, AwsApiCallActionOutputTypeDef]
PortProbeActionOutputTypeDef = TypedDict(
    "PortProbeActionOutputTypeDef",
    {
        "PortProbeDetails": NotRequired[List[PortProbeDetailTypeDef]],
        "Blocked": NotRequired[bool],
    },
)
PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "PortProbeDetails": NotRequired[Sequence[PortProbeDetailTypeDef]],
        "Blocked": NotRequired[bool],
    },
)
AwsEc2RouteTableDetailsUnionTypeDef = Union[
    AwsEc2RouteTableDetailsTypeDef, AwsEc2RouteTableDetailsOutputTypeDef
]
AutomationRulesActionTypeDef = TypedDict(
    "AutomationRulesActionTypeDef",
    {
        "Type": NotRequired[Literal["FINDING_FIELDS_UPDATE"]],
        "FindingFieldsUpdate": NotRequired[AutomationRulesFindingFieldsUpdateUnionTypeDef],
    },
)
AwsAmazonMqBrokerDetailsUnionTypeDef = Union[
    AwsAmazonMqBrokerDetailsTypeDef, AwsAmazonMqBrokerDetailsOutputTypeDef
]
AwsApiGatewayStageDetailsUnionTypeDef = Union[
    AwsApiGatewayStageDetailsTypeDef, AwsApiGatewayStageDetailsOutputTypeDef
]
AwsApiGatewayRestApiDetailsUnionTypeDef = Union[
    AwsApiGatewayRestApiDetailsTypeDef, AwsApiGatewayRestApiDetailsOutputTypeDef
]
AwsAppSyncGraphQlApiDetailsUnionTypeDef = Union[
    AwsAppSyncGraphQlApiDetailsTypeDef, AwsAppSyncGraphQlApiDetailsOutputTypeDef
]
AwsAthenaWorkGroupDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[str],
        "Configuration": NotRequired[AwsAthenaWorkGroupConfigurationDetailsTypeDef],
    },
)
AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef",
    {
        "LaunchConfigurationName": NotRequired[str],
        "LoadBalancerNames": NotRequired[List[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "CreatedTime": NotRequired[str],
        "MixedInstancesPolicy": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef
        ],
        "AvailabilityZones": NotRequired[
            List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]
        ],
        "LaunchTemplate": NotRequired[
            AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef
        ],
        "CapacityRebalance": NotRequired[bool],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    {
        "InstancesDistribution": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef
        ],
        "LaunchTemplate": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnionTypeDef
        ],
    },
)
AwsAutoScalingLaunchConfigurationDetailsUnionTypeDef = Union[
    AwsAutoScalingLaunchConfigurationDetailsTypeDef,
    AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef,
]
AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef",
    {
        "BackupPlanName": NotRequired[str],
        "AdvancedBackupSettings": NotRequired[
            List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef]
        ],
        "BackupPlanRule": NotRequired[List[AwsBackupBackupPlanRuleDetailsOutputTypeDef]],
    },
)
AwsBackupBackupPlanRuleDetailsUnionTypeDef = Union[
    AwsBackupBackupPlanRuleDetailsTypeDef, AwsBackupBackupPlanRuleDetailsOutputTypeDef
]
AwsBackupBackupVaultDetailsUnionTypeDef = Union[
    AwsBackupBackupVaultDetailsTypeDef, AwsBackupBackupVaultDetailsOutputTypeDef
]
AwsCertificateManagerCertificateDetailsOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsOutputTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "DomainValidationOptions": NotRequired[
            List[AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]
        ],
        "ExtendedKeyUsages": NotRequired[
            List[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]
        ],
        "FailureReason": NotRequired[str],
        "ImportedAt": NotRequired[str],
        "InUseBy": NotRequired[List[str]],
        "IssuedAt": NotRequired[str],
        "Issuer": NotRequired[str],
        "KeyAlgorithm": NotRequired[str],
        "KeyUsages": NotRequired[List[AwsCertificateManagerCertificateKeyUsageTypeDef]],
        "NotAfter": NotRequired[str],
        "NotBefore": NotRequired[str],
        "Options": NotRequired[AwsCertificateManagerCertificateOptionsTypeDef],
        "RenewalEligibility": NotRequired[str],
        "RenewalSummary": NotRequired[AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef],
        "Serial": NotRequired[str],
        "SignatureAlgorithm": NotRequired[str],
        "Status": NotRequired[str],
        "Subject": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[List[str]],
        "Type": NotRequired[str],
    },
)
AwsCertificateManagerCertificateRenewalSummaryUnionTypeDef = Union[
    AwsCertificateManagerCertificateRenewalSummaryTypeDef,
    AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef,
]
AwsCloudFrontDistributionOriginsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsOutputTypeDef",
    {
        "Items": NotRequired[List[AwsCloudFrontDistributionOriginItemOutputTypeDef]],
    },
)
AwsCloudFrontDistributionOriginGroupsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsOutputTypeDef",
    {
        "Items": NotRequired[List[AwsCloudFrontDistributionOriginGroupOutputTypeDef]],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginGroupFailoverTypeDef,
    AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef,
]
AwsCloudFrontDistributionOriginCustomOriginConfigUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef,
    AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef,
]
AwsCodeBuildProjectDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsTypeDef",
    {
        "EncryptionKey": NotRequired[str],
        "Artifacts": NotRequired[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]],
        "Environment": NotRequired[AwsCodeBuildProjectEnvironmentUnionTypeDef],
        "Name": NotRequired[str],
        "Source": NotRequired[AwsCodeBuildProjectSourceTypeDef],
        "ServiceRole": NotRequired[str],
        "LogsConfig": NotRequired[AwsCodeBuildProjectLogsConfigDetailsTypeDef],
        "VpcConfig": NotRequired[AwsCodeBuildProjectVpcConfigUnionTypeDef],
        "SecondaryArtifacts": NotRequired[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]],
    },
)
AwsApiGatewayV2ApiDetailsUnionTypeDef = Union[
    AwsApiGatewayV2ApiDetailsTypeDef, AwsApiGatewayV2ApiDetailsOutputTypeDef
]
AwsDynamoDbTableGlobalSecondaryIndexUnionTypeDef = Union[
    AwsDynamoDbTableGlobalSecondaryIndexTypeDef, AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef
]
AwsDynamoDbTableLocalSecondaryIndexUnionTypeDef = Union[
    AwsDynamoDbTableLocalSecondaryIndexTypeDef, AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef
]
AwsDynamoDbTableDetailsOutputTypeDef = TypedDict(
    "AwsDynamoDbTableDetailsOutputTypeDef",
    {
        "AttributeDefinitions": NotRequired[List[AwsDynamoDbTableAttributeDefinitionTypeDef]],
        "BillingModeSummary": NotRequired[AwsDynamoDbTableBillingModeSummaryTypeDef],
        "CreationDateTime": NotRequired[str],
        "GlobalSecondaryIndexes": NotRequired[
            List[AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef]
        ],
        "GlobalTableVersion": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]],
        "LatestStreamArn": NotRequired[str],
        "LatestStreamLabel": NotRequired[str],
        "LocalSecondaryIndexes": NotRequired[
            List[AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef]
        ],
        "ProvisionedThroughput": NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef],
        "Replicas": NotRequired[List[AwsDynamoDbTableReplicaOutputTypeDef]],
        "RestoreSummary": NotRequired[AwsDynamoDbTableRestoreSummaryTypeDef],
        "SseDescription": NotRequired[AwsDynamoDbTableSseDescriptionTypeDef],
        "StreamSpecification": NotRequired[AwsDynamoDbTableStreamSpecificationTypeDef],
        "TableId": NotRequired[str],
        "TableName": NotRequired[str],
        "TableSizeBytes": NotRequired[int],
        "TableStatus": NotRequired[str],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
AwsDynamoDbTableReplicaUnionTypeDef = Union[
    AwsDynamoDbTableReplicaTypeDef, AwsDynamoDbTableReplicaOutputTypeDef
]
AwsEc2ClientVpnEndpointDetailsUnionTypeDef = Union[
    AwsEc2ClientVpnEndpointDetailsTypeDef, AwsEc2ClientVpnEndpointDetailsOutputTypeDef
]
AwsEc2LaunchTemplateDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDetailsOutputTypeDef",
    {
        "LaunchTemplateName": NotRequired[str],
        "Id": NotRequired[str],
        "LaunchTemplateData": NotRequired[AwsEc2LaunchTemplateDataDetailsOutputTypeDef],
        "DefaultVersionNumber": NotRequired[int],
        "LatestVersionNumber": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataDetailsTypeDef",
    {
        "BlockDeviceMappingSet": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]
        ],
        "CapacityReservationSpecification": NotRequired[
            AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef
        ],
        "CpuOptions": NotRequired[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef],
        "CreditSpecification": NotRequired[
            AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef
        ],
        "DisableApiStop": NotRequired[bool],
        "DisableApiTermination": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "ElasticGpuSpecificationSet": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]
        ],
        "ElasticInferenceAcceleratorSet": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]
        ],
        "EnclaveOptions": NotRequired[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef],
        "HibernationOptions": NotRequired[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef],
        "IamInstanceProfile": NotRequired[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef],
        "ImageId": NotRequired[str],
        "InstanceInitiatedShutdownBehavior": NotRequired[str],
        "InstanceMarketOptions": NotRequired[
            AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef
        ],
        "InstanceRequirements": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnionTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LicenseSet": NotRequired[Sequence[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]],
        "MaintenanceOptions": NotRequired[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef],
        "MetadataOptions": NotRequired[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef],
        "Monitoring": NotRequired[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef],
        "NetworkInterfaceSet": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnionTypeDef]
        ],
        "Placement": NotRequired[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef],
        "PrivateDnsNameOptions": NotRequired[
            AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef
        ],
        "RamDiskId": NotRequired[str],
        "SecurityGroupIdSet": NotRequired[Sequence[str]],
        "SecurityGroupSet": NotRequired[Sequence[str]],
        "UserData": NotRequired[str],
    },
)
AwsEc2NetworkAclDetailsUnionTypeDef = Union[
    AwsEc2NetworkAclDetailsTypeDef, AwsEc2NetworkAclDetailsOutputTypeDef
]
AwsEc2SecurityGroupDetailsTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "IpPermissions": NotRequired[Sequence[AwsEc2SecurityGroupIpPermissionUnionTypeDef]],
        "IpPermissionsEgress": NotRequired[Sequence[AwsEc2SecurityGroupIpPermissionTypeDef]],
    },
)
AwsEc2VpcPeeringConnectionDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionDetailsTypeDef",
    {
        "AccepterVpcInfo": NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsUnionTypeDef],
        "ExpirationTime": NotRequired[str],
        "RequesterVpcInfo": NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsUnionTypeDef],
        "Status": NotRequired[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
AwsEc2VpnConnectionOptionsDetailsUnionTypeDef = Union[
    AwsEc2VpnConnectionOptionsDetailsTypeDef, AwsEc2VpnConnectionOptionsDetailsOutputTypeDef
]
AwsEcsClusterDetailsOutputTypeDef = TypedDict(
    "AwsEcsClusterDetailsOutputTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "ActiveServicesCount": NotRequired[int],
        "CapacityProviders": NotRequired[List[str]],
        "ClusterSettings": NotRequired[List[AwsEcsClusterClusterSettingsDetailsTypeDef]],
        "Configuration": NotRequired[AwsEcsClusterConfigurationDetailsTypeDef],
        "DefaultCapacityProviderStrategy": NotRequired[
            List[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]
        ],
        "ClusterName": NotRequired[str],
        "RegisteredContainerInstancesCount": NotRequired[int],
        "RunningTasksCount": NotRequired[int],
        "Status": NotRequired[str],
    },
)
AwsEcsClusterDetailsTypeDef = TypedDict(
    "AwsEcsClusterDetailsTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "ActiveServicesCount": NotRequired[int],
        "CapacityProviders": NotRequired[Sequence[str]],
        "ClusterSettings": NotRequired[Sequence[AwsEcsClusterClusterSettingsDetailsTypeDef]],
        "Configuration": NotRequired[AwsEcsClusterConfigurationDetailsTypeDef],
        "DefaultCapacityProviderStrategy": NotRequired[
            Sequence[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]
        ],
        "ClusterName": NotRequired[str],
        "RegisteredContainerInstancesCount": NotRequired[int],
        "RunningTasksCount": NotRequired[int],
        "Status": NotRequired[str],
    },
)
AwsEcsTaskDetailsTypeDef = TypedDict(
    "AwsEcsTaskDetailsTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "TaskDefinitionArn": NotRequired[str],
        "Version": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "StartedAt": NotRequired[str],
        "StartedBy": NotRequired[str],
        "Group": NotRequired[str],
        "Volumes": NotRequired[Sequence[AwsEcsTaskVolumeDetailsTypeDef]],
        "Containers": NotRequired[Sequence[AwsEcsContainerDetailsUnionTypeDef]],
    },
)
AwsEcsServiceNetworkConfigurationDetailsUnionTypeDef = Union[
    AwsEcsServiceNetworkConfigurationDetailsTypeDef,
    AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionDetailsOutputTypeDef",
    {
        "ContainerDefinitions": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef]
        ],
        "Cpu": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "Family": NotRequired[str],
        "InferenceAccelerators": NotRequired[
            List[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]
        ],
        "IpcMode": NotRequired[str],
        "Memory": NotRequired[str],
        "NetworkMode": NotRequired[str],
        "PidMode": NotRequired[str],
        "PlacementConstraints": NotRequired[
            List[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]
        ],
        "ProxyConfiguration": NotRequired[
            AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef
        ],
        "RequiresCompatibilities": NotRequired[List[str]],
        "TaskRoleArn": NotRequired[str],
        "Volumes": NotRequired[List[AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef]],
        "Status": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionVolumesDetailsTypeDef, AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef
]
AwsEfsAccessPointDetailsUnionTypeDef = Union[
    AwsEfsAccessPointDetailsTypeDef, AwsEfsAccessPointDetailsOutputTypeDef
]
AwsEksClusterLoggingDetailsUnionTypeDef = Union[
    AwsEksClusterLoggingDetailsTypeDef, AwsEksClusterLoggingDetailsOutputTypeDef
]
AwsElasticsearchDomainDetailsUnionTypeDef = Union[
    AwsElasticsearchDomainDetailsTypeDef, AwsElasticsearchDomainDetailsOutputTypeDef
]
AwsElbLoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbLoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackendServerDescriptions": NotRequired[
            Sequence[AwsElbLoadBalancerBackendServerDescriptionUnionTypeDef]
        ],
        "CanonicalHostedZoneName": NotRequired[str],
        "CanonicalHostedZoneNameID": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DnsName": NotRequired[str],
        "HealthCheck": NotRequired[AwsElbLoadBalancerHealthCheckTypeDef],
        "Instances": NotRequired[Sequence[AwsElbLoadBalancerInstanceTypeDef]],
        "ListenerDescriptions": NotRequired[
            Sequence[AwsElbLoadBalancerListenerDescriptionUnionTypeDef]
        ],
        "LoadBalancerAttributes": NotRequired[AwsElbLoadBalancerAttributesUnionTypeDef],
        "LoadBalancerName": NotRequired[str],
        "Policies": NotRequired[AwsElbLoadBalancerPoliciesUnionTypeDef],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SourceSecurityGroup": NotRequired[AwsElbLoadBalancerSourceSecurityGroupTypeDef],
        "Subnets": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
    },
)
AwsEventsEndpointDetailsOutputTypeDef = TypedDict(
    "AwsEventsEndpointDetailsOutputTypeDef",
    {
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointId": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EventBuses": NotRequired[List[AwsEventsEndpointEventBusesDetailsTypeDef]],
        "Name": NotRequired[str],
        "ReplicationConfig": NotRequired[AwsEventsEndpointReplicationConfigDetailsTypeDef],
        "RoleArn": NotRequired[str],
        "RoutingConfig": NotRequired[AwsEventsEndpointRoutingConfigDetailsTypeDef],
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
    },
)
AwsEventsEndpointDetailsTypeDef = TypedDict(
    "AwsEventsEndpointDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointId": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EventBuses": NotRequired[Sequence[AwsEventsEndpointEventBusesDetailsTypeDef]],
        "Name": NotRequired[str],
        "ReplicationConfig": NotRequired[AwsEventsEndpointReplicationConfigDetailsTypeDef],
        "RoleArn": NotRequired[str],
        "RoutingConfig": NotRequired[AwsEventsEndpointRoutingConfigDetailsTypeDef],
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesDetailsTypeDef",
    {
        "CloudTrail": NotRequired[AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef],
        "DnsLogs": NotRequired[AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef],
        "FlowLogs": NotRequired[AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef],
        "Kubernetes": NotRequired[AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef],
        "MalwareProtection": NotRequired[
            AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef
        ],
        "S3Logs": NotRequired[AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef],
    },
)
AwsIamRoleDetailsTypeDef = TypedDict(
    "AwsIamRoleDetailsTypeDef",
    {
        "AssumeRolePolicyDocument": NotRequired[str],
        "AttachedManagedPolicies": NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "InstanceProfileList": NotRequired[Sequence[AwsIamInstanceProfileUnionTypeDef]],
        "PermissionsBoundary": NotRequired[AwsIamPermissionsBoundaryTypeDef],
        "RoleId": NotRequired[str],
        "RoleName": NotRequired[str],
        "RolePolicyList": NotRequired[Sequence[AwsIamRolePolicyTypeDef]],
        "MaxSessionDuration": NotRequired[int],
        "Path": NotRequired[str],
    },
)
AwsLambdaFunctionDetailsTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsTypeDef",
    {
        "Code": NotRequired[AwsLambdaFunctionCodeTypeDef],
        "CodeSha256": NotRequired[str],
        "DeadLetterConfig": NotRequired[AwsLambdaFunctionDeadLetterConfigTypeDef],
        "Environment": NotRequired[AwsLambdaFunctionEnvironmentUnionTypeDef],
        "FunctionName": NotRequired[str],
        "Handler": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "LastModified": NotRequired[str],
        "Layers": NotRequired[Sequence[AwsLambdaFunctionLayerTypeDef]],
        "MasterArn": NotRequired[str],
        "MemorySize": NotRequired[int],
        "RevisionId": NotRequired[str],
        "Role": NotRequired[str],
        "Runtime": NotRequired[str],
        "Timeout": NotRequired[int],
        "TracingConfig": NotRequired[AwsLambdaFunctionTracingConfigTypeDef],
        "VpcConfig": NotRequired[AwsLambdaFunctionVpcConfigUnionTypeDef],
        "Version": NotRequired[str],
        "Architectures": NotRequired[Sequence[str]],
        "PackageType": NotRequired[str],
    },
)
AwsMskClusterClusterInfoDetailsOutputTypeDef = TypedDict(
    "AwsMskClusterClusterInfoDetailsOutputTypeDef",
    {
        "EncryptionInfo": NotRequired[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef],
        "CurrentVersion": NotRequired[str],
        "NumberOfBrokerNodes": NotRequired[int],
        "ClusterName": NotRequired[str],
        "ClientAuthentication": NotRequired[
            AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef
        ],
        "EnhancedMonitoring": NotRequired[str],
    },
)
AwsMskClusterClusterInfoClientAuthenticationDetailsUnionTypeDef = Union[
    AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef,
    AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef,
]
AwsOpenSearchServiceDomainDetailsUnionTypeDef = Union[
    AwsOpenSearchServiceDomainDetailsTypeDef, AwsOpenSearchServiceDomainDetailsOutputTypeDef
]
AwsRdsDbClusterSnapshotDetailsUnionTypeDef = Union[
    AwsRdsDbClusterSnapshotDetailsTypeDef, AwsRdsDbClusterSnapshotDetailsOutputTypeDef
]
AwsRdsDbInstanceDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsOutputTypeDef",
    {
        "AssociatedRoles": NotRequired[List[AwsRdsDbInstanceAssociatedRoleTypeDef]],
        "CACertificateIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "DbInstancePort": NotRequired[int],
        "DbiResourceId": NotRequired[str],
        "DBName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "Endpoint": NotRequired[AwsRdsDbInstanceEndpointTypeDef],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "InstanceCreateTime": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "StorageEncrypted": NotRequired[bool],
        "TdeCredentialArn": NotRequired[str],
        "VpcSecurityGroups": NotRequired[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]],
        "MultiAz": NotRequired[bool],
        "EnhancedMonitoringResourceArn": NotRequired[str],
        "DbInstanceStatus": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "DbSecurityGroups": NotRequired[List[str]],
        "DbParameterGroups": NotRequired[List[AwsRdsDbParameterGroupTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "DbSubnetGroup": NotRequired[AwsRdsDbSubnetGroupOutputTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired[AwsRdsDbPendingModifiedValuesOutputTypeDef],
        "LatestRestorableTime": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReadReplicaSourceDBInstanceIdentifier": NotRequired[str],
        "ReadReplicaDBInstanceIdentifiers": NotRequired[List[str]],
        "ReadReplicaDBClusterIdentifiers": NotRequired[List[str]],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupMemberships": NotRequired[List[AwsRdsDbOptionGroupMembershipTypeDef]],
        "CharacterSetName": NotRequired[str],
        "SecondaryAvailabilityZone": NotRequired[str],
        "StatusInfos": NotRequired[List[AwsRdsDbStatusInfoTypeDef]],
        "StorageType": NotRequired[str],
        "DomainMemberships": NotRequired[List[AwsRdsDbDomainMembershipTypeDef]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "Timezone": NotRequired[str],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKmsKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnabledCloudWatchLogsExports": NotRequired[List[str]],
        "ProcessorFeatures": NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]],
        "ListenerEndpoint": NotRequired[AwsRdsDbInstanceEndpointTypeDef],
        "MaxAllocatedStorage": NotRequired[int],
    },
)
AwsRdsDbSubnetGroupUnionTypeDef = Union[
    AwsRdsDbSubnetGroupTypeDef, AwsRdsDbSubnetGroupOutputTypeDef
]
AwsRdsDbPendingModifiedValuesUnionTypeDef = Union[
    AwsRdsDbPendingModifiedValuesTypeDef, AwsRdsDbPendingModifiedValuesOutputTypeDef
]
AwsRedshiftClusterDetailsTypeDef = TypedDict(
    "AwsRedshiftClusterDetailsTypeDef",
    {
        "AllowVersionUpgrade": NotRequired[bool],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "ClusterAvailabilityStatus": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "ClusterNodes": NotRequired[Sequence[AwsRedshiftClusterClusterNodeTypeDef]],
        "ClusterParameterGroups": NotRequired[
            Sequence[AwsRedshiftClusterClusterParameterGroupUnionTypeDef]
        ],
        "ClusterPublicKey": NotRequired[str],
        "ClusterRevisionNumber": NotRequired[str],
        "ClusterSecurityGroups": NotRequired[
            Sequence[AwsRedshiftClusterClusterSecurityGroupTypeDef]
        ],
        "ClusterSnapshotCopyStatus": NotRequired[
            AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef
        ],
        "ClusterStatus": NotRequired[str],
        "ClusterSubnetGroupName": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "DBName": NotRequired[str],
        "DeferredMaintenanceWindows": NotRequired[
            Sequence[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]
        ],
        "ElasticIpStatus": NotRequired[AwsRedshiftClusterElasticIpStatusTypeDef],
        "ElasticResizeNumberOfNodeOptions": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Endpoint": NotRequired[AwsRedshiftClusterEndpointTypeDef],
        "EnhancedVpcRouting": NotRequired[bool],
        "ExpectedNextSnapshotScheduleTime": NotRequired[str],
        "ExpectedNextSnapshotScheduleTimeStatus": NotRequired[str],
        "HsmStatus": NotRequired[AwsRedshiftClusterHsmStatusTypeDef],
        "IamRoles": NotRequired[Sequence[AwsRedshiftClusterIamRoleTypeDef]],
        "KmsKeyId": NotRequired[str],
        "MaintenanceTrackName": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "NextMaintenanceWindowStartTime": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "PendingActions": NotRequired[Sequence[str]],
        "PendingModifiedValues": NotRequired[AwsRedshiftClusterPendingModifiedValuesTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ResizeInfo": NotRequired[AwsRedshiftClusterResizeInfoTypeDef],
        "RestoreStatus": NotRequired[AwsRedshiftClusterRestoreStatusTypeDef],
        "SnapshotScheduleIdentifier": NotRequired[str],
        "SnapshotScheduleState": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcSecurityGroups": NotRequired[Sequence[AwsRedshiftClusterVpcSecurityGroupTypeDef]],
        "LoggingStatus": NotRequired[AwsRedshiftClusterLoggingStatusTypeDef],
    },
)
AwsRoute53HostedZoneDetailsUnionTypeDef = Union[
    AwsRoute53HostedZoneDetailsTypeDef, AwsRoute53HostedZoneDetailsOutputTypeDef
]
AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef",
    {
        "Predicate": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef
        ],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnionTypeDef = Union[
    AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef,
    AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef,
]
AwsS3BucketNotificationConfigurationDetailOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailOutputTypeDef",
    {
        "Events": NotRequired[List[str]],
        "Filter": NotRequired[AwsS3BucketNotificationConfigurationFilterOutputTypeDef],
        "Destination": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsS3BucketNotificationConfigurationFilterTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    {
        "S3KeyFilter": NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterUnionTypeDef],
    },
)
AwsS3BucketServerSideEncryptionConfigurationUnionTypeDef = Union[
    AwsS3BucketServerSideEncryptionConfigurationTypeDef,
    AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef,
]
AwsS3BucketWebsiteConfigurationUnionTypeDef = Union[
    AwsS3BucketWebsiteConfigurationTypeDef, AwsS3BucketWebsiteConfigurationOutputTypeDef
]
AwsStepFunctionStateMachineDetailsOutputTypeDef = TypedDict(
    "AwsStepFunctionStateMachineDetailsOutputTypeDef",
    {
        "Label": NotRequired[str],
        "LoggingConfiguration": NotRequired[
            AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef
        ],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "StateMachineArn": NotRequired[str],
        "Status": NotRequired[str],
        "TracingConfiguration": NotRequired[
            AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDetailsUnionTypeDef = Union[
    AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef,
    AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef,
]
AwsWafRegionalRuleGroupDetailsUnionTypeDef = Union[
    AwsWafRegionalRuleGroupDetailsTypeDef, AwsWafRegionalRuleGroupDetailsOutputTypeDef
]
AwsWafRegionalWebAclDetailsUnionTypeDef = Union[
    AwsWafRegionalWebAclDetailsTypeDef, AwsWafRegionalWebAclDetailsOutputTypeDef
]
AwsWafRuleGroupDetailsUnionTypeDef = Union[
    AwsWafRuleGroupDetailsTypeDef, AwsWafRuleGroupDetailsOutputTypeDef
]
AwsWafWebAclDetailsTypeDef = TypedDict(
    "AwsWafWebAclDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultAction": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafWebAclRuleUnionTypeDef]],
        "WebAclId": NotRequired[str],
    },
)
AwsWafv2ActionAllowDetailsTypeDef = TypedDict(
    "AwsWafv2ActionAllowDetailsTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsUnionTypeDef],
    },
)
AwsWafv2RulesActionCaptchaDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionCaptchaDetailsTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsUnionTypeDef],
    },
)
AwsWafv2RulesActionCountDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionCountDetailsTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsUnionTypeDef],
    },
)
AwsWafv2RulesActionDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RulesActionDetailsOutputTypeDef",
    {
        "Allow": NotRequired[AwsWafv2ActionAllowDetailsOutputTypeDef],
        "Block": NotRequired[AwsWafv2ActionBlockDetailsOutputTypeDef],
        "Captcha": NotRequired[AwsWafv2RulesActionCaptchaDetailsOutputTypeDef],
        "Count": NotRequired[AwsWafv2RulesActionCountDetailsOutputTypeDef],
    },
)
AwsWafv2WebAclActionDetailsOutputTypeDef = TypedDict(
    "AwsWafv2WebAclActionDetailsOutputTypeDef",
    {
        "Allow": NotRequired[AwsWafv2ActionAllowDetailsOutputTypeDef],
        "Block": NotRequired[AwsWafv2ActionBlockDetailsOutputTypeDef],
    },
)
AwsWafv2ActionBlockDetailsTypeDef = TypedDict(
    "AwsWafv2ActionBlockDetailsTypeDef",
    {
        "CustomResponse": NotRequired[AwsWafv2CustomResponseDetailsUnionTypeDef],
    },
)
VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "Id": str,
        "VulnerablePackages": NotRequired[Sequence[SoftwarePackageTypeDef]],
        "Cvss": NotRequired[Sequence[CvssUnionTypeDef]],
        "RelatedVulnerabilities": NotRequired[Sequence[str]],
        "Vendor": NotRequired[VulnerabilityVendorTypeDef],
        "ReferenceUrls": NotRequired[Sequence[str]],
        "FixAvailable": NotRequired[VulnerabilityFixAvailableType],
        "EpssScore": NotRequired[float],
        "ExploitAvailable": NotRequired[VulnerabilityExploitAvailableType],
        "LastKnownExploitAt": NotRequired[str],
        "CodeVulnerabilities": NotRequired[Sequence[VulnerabilityCodeVulnerabilitiesUnionTypeDef]],
    },
)
SecurityControlDefinitionTypeDef = TypedDict(
    "SecurityControlDefinitionTypeDef",
    {
        "SecurityControlId": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": SeverityRatingType,
        "CurrentRegionAvailability": RegionAvailabilityStatusType,
        "CustomizableProperties": NotRequired[List[Literal["Parameters"]]],
        "ParameterDefinitions": NotRequired[Dict[str, ParameterDefinitionTypeDef]],
    },
)
BatchGetConfigurationPolicyAssociationsResponseTypeDef = TypedDict(
    "BatchGetConfigurationPolicyAssociationsResponseTypeDef",
    {
        "ConfigurationPolicyAssociations": List[ConfigurationPolicyAssociationSummaryTypeDef],
        "UnprocessedConfigurationPolicyAssociations": List[
            UnprocessedConfigurationPolicyAssociationTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutomationRulesConfigTypeDef = TypedDict(
    "AutomationRulesConfigTypeDef",
    {
        "RuleArn": NotRequired[str],
        "RuleStatus": NotRequired[RuleStatusType],
        "RuleOrder": NotRequired[int],
        "RuleName": NotRequired[str],
        "Description": NotRequired[str],
        "IsTerminal": NotRequired[bool],
        "Criteria": NotRequired[AutomationRulesFindingFiltersOutputTypeDef],
        "Actions": NotRequired[List[AutomationRulesActionOutputTypeDef]],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
    },
)
AutomationRulesFindingFiltersUnionTypeDef = Union[
    AutomationRulesFindingFiltersTypeDef, AutomationRulesFindingFiltersOutputTypeDef
]
InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": AwsSecurityFindingFiltersOutputTypeDef,
        "GroupByAttribute": str,
    },
)
CreateInsightRequestRequestTypeDef = TypedDict(
    "CreateInsightRequestRequestTypeDef",
    {
        "Name": str,
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "GroupByAttribute": str,
    },
)
GetFindingsRequestGetFindingsPaginateTypeDef = TypedDict(
    "GetFindingsRequestGetFindingsPaginateTypeDef",
    {
        "Filters": NotRequired[AwsSecurityFindingFiltersTypeDef],
        "SortCriteria": NotRequired[Sequence[SortCriterionTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "Filters": NotRequired[AwsSecurityFindingFiltersTypeDef],
        "SortCriteria": NotRequired[Sequence[SortCriterionTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
UpdateFindingsRequestRequestTypeDef = TypedDict(
    "UpdateFindingsRequestRequestTypeDef",
    {
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "Note": NotRequired[NoteUpdateTypeDef],
        "RecordState": NotRequired[RecordStateType],
    },
)
UpdateInsightRequestRequestTypeDef = TypedDict(
    "UpdateInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
        "Name": NotRequired[str],
        "Filters": NotRequired[AwsSecurityFindingFiltersTypeDef],
        "GroupByAttribute": NotRequired[str],
    },
)
NetworkPathComponentOutputTypeDef = TypedDict(
    "NetworkPathComponentOutputTypeDef",
    {
        "ComponentId": NotRequired[str],
        "ComponentType": NotRequired[str],
        "Egress": NotRequired[NetworkHeaderOutputTypeDef],
        "Ingress": NotRequired[NetworkHeaderOutputTypeDef],
    },
)
NetworkHeaderTypeDef = TypedDict(
    "NetworkHeaderTypeDef",
    {
        "Protocol": NotRequired[str],
        "Destination": NotRequired[NetworkPathComponentDetailsUnionTypeDef],
        "Source": NotRequired[NetworkPathComponentDetailsUnionTypeDef],
    },
)
CustomDataIdentifiersDetectionsOutputTypeDef = TypedDict(
    "CustomDataIdentifiersDetectionsOutputTypeDef",
    {
        "Count": NotRequired[int],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesOutputTypeDef],
    },
)
SensitiveDataDetectionsOutputTypeDef = TypedDict(
    "SensitiveDataDetectionsOutputTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesOutputTypeDef],
    },
)
OccurrencesUnionTypeDef = Union[OccurrencesTypeDef, OccurrencesOutputTypeDef]
SecurityControlsConfigurationOutputTypeDef = TypedDict(
    "SecurityControlsConfigurationOutputTypeDef",
    {
        "EnabledSecurityControlIdentifiers": NotRequired[List[str]],
        "DisabledSecurityControlIdentifiers": NotRequired[List[str]],
        "SecurityControlCustomParameters": NotRequired[
            List[SecurityControlCustomParameterOutputTypeDef]
        ],
    },
)
BatchGetSecurityControlsResponseTypeDef = TypedDict(
    "BatchGetSecurityControlsResponseTypeDef",
    {
        "SecurityControls": List[SecurityControlTypeDef],
        "UnprocessedIds": List[UnprocessedSecurityControlTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ParameterConfigurationUnionTypeDef = Union[
    ParameterConfigurationTypeDef, ParameterConfigurationOutputTypeDef
]
RuleGroupSourceStatefulRulesDetailsUnionTypeDef = Union[
    RuleGroupSourceStatefulRulesDetailsTypeDef, RuleGroupSourceStatefulRulesDetailsOutputTypeDef
]
RuleGroupSourceStatelessRulesDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesDetailsOutputTypeDef",
    {
        "Priority": NotRequired[int],
        "RuleDefinition": NotRequired[RuleGroupSourceStatelessRuleDefinitionOutputTypeDef],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesUnionTypeDef = Union[
    RuleGroupSourceStatelessRuleMatchAttributesTypeDef,
    RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef,
]
RuleGroupVariablesUnionTypeDef = Union[RuleGroupVariablesTypeDef, RuleGroupVariablesOutputTypeDef]
ComplianceUnionTypeDef = Union[ComplianceTypeDef, ComplianceOutputTypeDef]
FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef = TypedDict(
    "FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef",
    {
        "ActionDefinition": NotRequired[StatelessCustomActionDefinitionOutputTypeDef],
        "ActionName": NotRequired[str],
    },
)
RuleGroupSourceCustomActionsDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceCustomActionsDetailsOutputTypeDef",
    {
        "ActionDefinition": NotRequired[StatelessCustomActionDefinitionOutputTypeDef],
        "ActionName": NotRequired[str],
    },
)
StatelessCustomActionDefinitionTypeDef = TypedDict(
    "StatelessCustomActionDefinitionTypeDef",
    {
        "PublishMetricAction": NotRequired[StatelessCustomPublishMetricActionUnionTypeDef],
    },
)
ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "ActionType": NotRequired[str],
        "NetworkConnectionAction": NotRequired[NetworkConnectionActionTypeDef],
        "AwsApiCallAction": NotRequired[AwsApiCallActionOutputTypeDef],
        "DnsRequestAction": NotRequired[DnsRequestActionTypeDef],
        "PortProbeAction": NotRequired[PortProbeActionOutputTypeDef],
    },
)
PortProbeActionUnionTypeDef = Union[PortProbeActionTypeDef, PortProbeActionOutputTypeDef]
AutomationRulesActionUnionTypeDef = Union[
    AutomationRulesActionTypeDef, AutomationRulesActionOutputTypeDef
]
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnionTypeDef = Union[
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef,
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef,
]
AwsBackupBackupPlanDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanDetailsOutputTypeDef",
    {
        "BackupPlan": NotRequired[AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef],
        "BackupPlanArn": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)
AwsBackupBackupPlanBackupPlanDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanBackupPlanDetailsTypeDef",
    {
        "BackupPlanName": NotRequired[str],
        "AdvancedBackupSettings": NotRequired[
            Sequence[AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnionTypeDef]
        ],
        "BackupPlanRule": NotRequired[Sequence[AwsBackupBackupPlanRuleDetailsUnionTypeDef]],
    },
)
AwsCertificateManagerCertificateDetailsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "DomainValidationOptions": NotRequired[
            Sequence[AwsCertificateManagerCertificateDomainValidationOptionUnionTypeDef]
        ],
        "ExtendedKeyUsages": NotRequired[
            Sequence[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]
        ],
        "FailureReason": NotRequired[str],
        "ImportedAt": NotRequired[str],
        "InUseBy": NotRequired[Sequence[str]],
        "IssuedAt": NotRequired[str],
        "Issuer": NotRequired[str],
        "KeyAlgorithm": NotRequired[str],
        "KeyUsages": NotRequired[Sequence[AwsCertificateManagerCertificateKeyUsageTypeDef]],
        "NotAfter": NotRequired[str],
        "NotBefore": NotRequired[str],
        "Options": NotRequired[AwsCertificateManagerCertificateOptionsTypeDef],
        "RenewalEligibility": NotRequired[str],
        "RenewalSummary": NotRequired[AwsCertificateManagerCertificateRenewalSummaryUnionTypeDef],
        "Serial": NotRequired[str],
        "SignatureAlgorithm": NotRequired[str],
        "Status": NotRequired[str],
        "Subject": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[Sequence[str]],
        "Type": NotRequired[str],
    },
)
AwsCloudFrontDistributionDetailsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsOutputTypeDef",
    {
        "CacheBehaviors": NotRequired[AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef],
        "DefaultCacheBehavior": NotRequired[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef],
        "DefaultRootObject": NotRequired[str],
        "DomainName": NotRequired[str],
        "ETag": NotRequired[str],
        "LastModifiedTime": NotRequired[str],
        "Logging": NotRequired[AwsCloudFrontDistributionLoggingTypeDef],
        "Origins": NotRequired[AwsCloudFrontDistributionOriginsOutputTypeDef],
        "OriginGroups": NotRequired[AwsCloudFrontDistributionOriginGroupsOutputTypeDef],
        "ViewerCertificate": NotRequired[AwsCloudFrontDistributionViewerCertificateTypeDef],
        "Status": NotRequired[str],
        "WebAclId": NotRequired[str],
    },
)
AwsCloudFrontDistributionOriginGroupTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    {
        "FailoverCriteria": NotRequired[AwsCloudFrontDistributionOriginGroupFailoverUnionTypeDef],
    },
)
AwsCloudFrontDistributionOriginItemTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemTypeDef",
    {
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "OriginPath": NotRequired[str],
        "S3OriginConfig": NotRequired[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef],
        "CustomOriginConfig": NotRequired[
            AwsCloudFrontDistributionOriginCustomOriginConfigUnionTypeDef
        ],
    },
)
AwsCodeBuildProjectDetailsUnionTypeDef = Union[
    AwsCodeBuildProjectDetailsTypeDef, AwsCodeBuildProjectDetailsOutputTypeDef
]
AwsDynamoDbTableDetailsTypeDef = TypedDict(
    "AwsDynamoDbTableDetailsTypeDef",
    {
        "AttributeDefinitions": NotRequired[Sequence[AwsDynamoDbTableAttributeDefinitionTypeDef]],
        "BillingModeSummary": NotRequired[AwsDynamoDbTableBillingModeSummaryTypeDef],
        "CreationDateTime": NotRequired[str],
        "GlobalSecondaryIndexes": NotRequired[
            Sequence[AwsDynamoDbTableGlobalSecondaryIndexUnionTypeDef]
        ],
        "GlobalTableVersion": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]],
        "LatestStreamArn": NotRequired[str],
        "LatestStreamLabel": NotRequired[str],
        "LocalSecondaryIndexes": NotRequired[
            Sequence[AwsDynamoDbTableLocalSecondaryIndexUnionTypeDef]
        ],
        "ProvisionedThroughput": NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef],
        "Replicas": NotRequired[Sequence[AwsDynamoDbTableReplicaUnionTypeDef]],
        "RestoreSummary": NotRequired[AwsDynamoDbTableRestoreSummaryTypeDef],
        "SseDescription": NotRequired[AwsDynamoDbTableSseDescriptionTypeDef],
        "StreamSpecification": NotRequired[AwsDynamoDbTableStreamSpecificationTypeDef],
        "TableId": NotRequired[str],
        "TableName": NotRequired[str],
        "TableSizeBytes": NotRequired[int],
        "TableStatus": NotRequired[str],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
AwsEc2LaunchTemplateDataDetailsUnionTypeDef = Union[
    AwsEc2LaunchTemplateDataDetailsTypeDef, AwsEc2LaunchTemplateDataDetailsOutputTypeDef
]
AwsEc2SecurityGroupDetailsUnionTypeDef = Union[
    AwsEc2SecurityGroupDetailsTypeDef, AwsEc2SecurityGroupDetailsOutputTypeDef
]
AwsEc2VpcPeeringConnectionDetailsUnionTypeDef = Union[
    AwsEc2VpcPeeringConnectionDetailsTypeDef, AwsEc2VpcPeeringConnectionDetailsOutputTypeDef
]
AwsEc2VpnConnectionDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsTypeDef",
    {
        "VpnConnectionId": NotRequired[str],
        "State": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "CustomerGatewayConfiguration": NotRequired[str],
        "Type": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "VgwTelemetry": NotRequired[Sequence[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]],
        "Options": NotRequired[AwsEc2VpnConnectionOptionsDetailsUnionTypeDef],
        "Routes": NotRequired[Sequence[AwsEc2VpnConnectionRoutesDetailsTypeDef]],
        "TransitGatewayId": NotRequired[str],
    },
)
AwsEcsClusterDetailsUnionTypeDef = Union[
    AwsEcsClusterDetailsTypeDef, AwsEcsClusterDetailsOutputTypeDef
]
AwsEcsTaskDetailsUnionTypeDef = Union[AwsEcsTaskDetailsTypeDef, AwsEcsTaskDetailsOutputTypeDef]
AwsEcsServiceDetailsTypeDef = TypedDict(
    "AwsEcsServiceDetailsTypeDef",
    {
        "CapacityProviderStrategy": NotRequired[
            Sequence[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]
        ],
        "Cluster": NotRequired[str],
        "DeploymentConfiguration": NotRequired[AwsEcsServiceDeploymentConfigurationDetailsTypeDef],
        "DeploymentController": NotRequired[AwsEcsServiceDeploymentControllerDetailsTypeDef],
        "DesiredCount": NotRequired[int],
        "EnableEcsManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "HealthCheckGracePeriodSeconds": NotRequired[int],
        "LaunchType": NotRequired[str],
        "LoadBalancers": NotRequired[Sequence[AwsEcsServiceLoadBalancersDetailsTypeDef]],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired[AwsEcsServiceNetworkConfigurationDetailsUnionTypeDef],
        "PlacementConstraints": NotRequired[
            Sequence[AwsEcsServicePlacementConstraintsDetailsTypeDef]
        ],
        "PlacementStrategies": NotRequired[
            Sequence[AwsEcsServicePlacementStrategiesDetailsTypeDef]
        ],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[str],
        "Role": NotRequired[str],
        "SchedulingStrategy": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceRegistries": NotRequired[Sequence[AwsEcsServiceServiceRegistriesDetailsTypeDef]],
        "TaskDefinition": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Cpu": NotRequired[int],
        "DependsOn": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]
        ],
        "DisableNetworking": NotRequired[bool],
        "DnsSearchDomains": NotRequired[Sequence[str]],
        "DnsServers": NotRequired[Sequence[str]],
        "DockerLabels": NotRequired[Mapping[str, str]],
        "DockerSecurityOptions": NotRequired[Sequence[str]],
        "EntryPoint": NotRequired[Sequence[str]],
        "Environment": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]
        ],
        "EnvironmentFiles": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]
        ],
        "Essential": NotRequired[bool],
        "ExtraHosts": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]
        ],
        "FirelensConfiguration": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnionTypeDef
        ],
        "HealthCheck": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnionTypeDef
        ],
        "Hostname": NotRequired[str],
        "Image": NotRequired[str],
        "Interactive": NotRequired[bool],
        "Links": NotRequired[Sequence[str]],
        "LinuxParameters": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnionTypeDef
        ],
        "LogConfiguration": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnionTypeDef
        ],
        "Memory": NotRequired[int],
        "MemoryReservation": NotRequired[int],
        "MountPoints": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]
        ],
        "Name": NotRequired[str],
        "PortMappings": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]
        ],
        "Privileged": NotRequired[bool],
        "PseudoTerminal": NotRequired[bool],
        "ReadonlyRootFilesystem": NotRequired[bool],
        "RepositoryCredentials": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef
        ],
        "ResourceRequirements": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]
        ],
        "Secrets": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]
        ],
        "StartTimeout": NotRequired[int],
        "StopTimeout": NotRequired[int],
        "SystemControls": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]
        ],
        "Ulimits": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]
        ],
        "User": NotRequired[str],
        "VolumesFrom": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]
        ],
        "WorkingDirectory": NotRequired[str],
    },
)
AwsEksClusterDetailsTypeDef = TypedDict(
    "AwsEksClusterDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityData": NotRequired[str],
        "ClusterStatus": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Name": NotRequired[str],
        "ResourcesVpcConfig": NotRequired[AwsEksClusterResourcesVpcConfigDetailsUnionTypeDef],
        "RoleArn": NotRequired[str],
        "Version": NotRequired[str],
        "Logging": NotRequired[AwsEksClusterLoggingDetailsUnionTypeDef],
    },
)
AwsElbLoadBalancerDetailsUnionTypeDef = Union[
    AwsElbLoadBalancerDetailsTypeDef, AwsElbLoadBalancerDetailsOutputTypeDef
]
AwsEventsEndpointDetailsUnionTypeDef = Union[
    AwsEventsEndpointDetailsTypeDef, AwsEventsEndpointDetailsOutputTypeDef
]
AwsGuardDutyDetectorDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDetailsOutputTypeDef",
    {
        "DataSources": NotRequired[AwsGuardDutyDetectorDataSourcesDetailsTypeDef],
        "Features": NotRequired[List[AwsGuardDutyDetectorFeaturesDetailsTypeDef]],
        "FindingPublishingFrequency": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDetailsTypeDef",
    {
        "DataSources": NotRequired[AwsGuardDutyDetectorDataSourcesDetailsTypeDef],
        "Features": NotRequired[Sequence[AwsGuardDutyDetectorFeaturesDetailsTypeDef]],
        "FindingPublishingFrequency": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsIamRoleDetailsUnionTypeDef = Union[AwsIamRoleDetailsTypeDef, AwsIamRoleDetailsOutputTypeDef]
AwsLambdaFunctionDetailsUnionTypeDef = Union[
    AwsLambdaFunctionDetailsTypeDef, AwsLambdaFunctionDetailsOutputTypeDef
]
AwsMskClusterDetailsOutputTypeDef = TypedDict(
    "AwsMskClusterDetailsOutputTypeDef",
    {
        "ClusterInfo": NotRequired[AwsMskClusterClusterInfoDetailsOutputTypeDef],
    },
)
AwsMskClusterClusterInfoDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoDetailsTypeDef",
    {
        "EncryptionInfo": NotRequired[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef],
        "CurrentVersion": NotRequired[str],
        "NumberOfBrokerNodes": NotRequired[int],
        "ClusterName": NotRequired[str],
        "ClientAuthentication": NotRequired[
            AwsMskClusterClusterInfoClientAuthenticationDetailsUnionTypeDef
        ],
        "EnhancedMonitoring": NotRequired[str],
    },
)
AwsRdsDbInstanceDetailsTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsTypeDef",
    {
        "AssociatedRoles": NotRequired[Sequence[AwsRdsDbInstanceAssociatedRoleTypeDef]],
        "CACertificateIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "DbInstancePort": NotRequired[int],
        "DbiResourceId": NotRequired[str],
        "DBName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "Endpoint": NotRequired[AwsRdsDbInstanceEndpointTypeDef],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "InstanceCreateTime": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "StorageEncrypted": NotRequired[bool],
        "TdeCredentialArn": NotRequired[str],
        "VpcSecurityGroups": NotRequired[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]],
        "MultiAz": NotRequired[bool],
        "EnhancedMonitoringResourceArn": NotRequired[str],
        "DbInstanceStatus": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "DbSecurityGroups": NotRequired[Sequence[str]],
        "DbParameterGroups": NotRequired[Sequence[AwsRdsDbParameterGroupTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "DbSubnetGroup": NotRequired[AwsRdsDbSubnetGroupUnionTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired[AwsRdsDbPendingModifiedValuesUnionTypeDef],
        "LatestRestorableTime": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReadReplicaSourceDBInstanceIdentifier": NotRequired[str],
        "ReadReplicaDBInstanceIdentifiers": NotRequired[Sequence[str]],
        "ReadReplicaDBClusterIdentifiers": NotRequired[Sequence[str]],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupMemberships": NotRequired[Sequence[AwsRdsDbOptionGroupMembershipTypeDef]],
        "CharacterSetName": NotRequired[str],
        "SecondaryAvailabilityZone": NotRequired[str],
        "StatusInfos": NotRequired[Sequence[AwsRdsDbStatusInfoTypeDef]],
        "StorageType": NotRequired[str],
        "DomainMemberships": NotRequired[Sequence[AwsRdsDbDomainMembershipTypeDef]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "Timezone": NotRequired[str],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKmsKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnabledCloudWatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]],
        "ListenerEndpoint": NotRequired[AwsRdsDbInstanceEndpointTypeDef],
        "MaxAllocatedStorage": NotRequired[int],
    },
)
AwsRedshiftClusterDetailsUnionTypeDef = Union[
    AwsRedshiftClusterDetailsTypeDef, AwsRedshiftClusterDetailsOutputTypeDef
]
AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef",
    {
        "AbortIncompleteMultipartUpload": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef
        ],
        "ExpirationDate": NotRequired[str],
        "ExpirationInDays": NotRequired[int],
        "ExpiredObjectDeleteMarker": NotRequired[bool],
        "Filter": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef
        ],
        "ID": NotRequired[str],
        "NoncurrentVersionExpirationInDays": NotRequired[int],
        "NoncurrentVersionTransitions": NotRequired[
            List[
                AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef
            ]
        ],
        "Prefix": NotRequired[str],
        "Status": NotRequired[str],
        "Transitions": NotRequired[
            List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]
        ],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    {
        "Predicate": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnionTypeDef
        ],
    },
)
AwsS3BucketNotificationConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationOutputTypeDef",
    {
        "Configurations": NotRequired[
            List[AwsS3BucketNotificationConfigurationDetailOutputTypeDef]
        ],
    },
)
AwsS3BucketNotificationConfigurationFilterUnionTypeDef = Union[
    AwsS3BucketNotificationConfigurationFilterTypeDef,
    AwsS3BucketNotificationConfigurationFilterOutputTypeDef,
]
AwsStepFunctionStateMachineDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineDetailsTypeDef",
    {
        "Label": NotRequired[str],
        "LoggingConfiguration": NotRequired[
            AwsStepFunctionStateMachineLoggingConfigurationDetailsUnionTypeDef
        ],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "StateMachineArn": NotRequired[str],
        "Status": NotRequired[str],
        "TracingConfiguration": NotRequired[
            AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsWafWebAclDetailsUnionTypeDef = Union[
    AwsWafWebAclDetailsTypeDef, AwsWafWebAclDetailsOutputTypeDef
]
AwsWafv2ActionAllowDetailsUnionTypeDef = Union[
    AwsWafv2ActionAllowDetailsTypeDef, AwsWafv2ActionAllowDetailsOutputTypeDef
]
AwsWafv2RulesActionCaptchaDetailsUnionTypeDef = Union[
    AwsWafv2RulesActionCaptchaDetailsTypeDef, AwsWafv2RulesActionCaptchaDetailsOutputTypeDef
]
AwsWafv2RulesActionCountDetailsUnionTypeDef = Union[
    AwsWafv2RulesActionCountDetailsTypeDef, AwsWafv2RulesActionCountDetailsOutputTypeDef
]
AwsWafv2RulesDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RulesDetailsOutputTypeDef",
    {
        "Action": NotRequired[AwsWafv2RulesActionDetailsOutputTypeDef],
        "Name": NotRequired[str],
        "OverrideAction": NotRequired[str],
        "Priority": NotRequired[int],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
AwsWafv2ActionBlockDetailsUnionTypeDef = Union[
    AwsWafv2ActionBlockDetailsTypeDef, AwsWafv2ActionBlockDetailsOutputTypeDef
]
VulnerabilityUnionTypeDef = Union[VulnerabilityTypeDef, VulnerabilityOutputTypeDef]
GetSecurityControlDefinitionResponseTypeDef = TypedDict(
    "GetSecurityControlDefinitionResponseTypeDef",
    {
        "SecurityControlDefinition": SecurityControlDefinitionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSecurityControlDefinitionsResponseTypeDef = TypedDict(
    "ListSecurityControlDefinitionsResponseTypeDef",
    {
        "SecurityControlDefinitions": List[SecurityControlDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchGetAutomationRulesResponseTypeDef = TypedDict(
    "BatchGetAutomationRulesResponseTypeDef",
    {
        "Rules": List[AutomationRulesConfigTypeDef],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInsightsResponseTypeDef = TypedDict(
    "GetInsightsResponseTypeDef",
    {
        "Insights": List[InsightTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
NetworkHeaderUnionTypeDef = Union[NetworkHeaderTypeDef, NetworkHeaderOutputTypeDef]
CustomDataIdentifiersResultOutputTypeDef = TypedDict(
    "CustomDataIdentifiersResultOutputTypeDef",
    {
        "Detections": NotRequired[List[CustomDataIdentifiersDetectionsOutputTypeDef]],
        "TotalCount": NotRequired[int],
    },
)
SensitiveDataResultOutputTypeDef = TypedDict(
    "SensitiveDataResultOutputTypeDef",
    {
        "Category": NotRequired[str],
        "Detections": NotRequired[List[SensitiveDataDetectionsOutputTypeDef]],
        "TotalCount": NotRequired[int],
    },
)
CustomDataIdentifiersDetectionsTypeDef = TypedDict(
    "CustomDataIdentifiersDetectionsTypeDef",
    {
        "Count": NotRequired[int],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesUnionTypeDef],
    },
)
SensitiveDataDetectionsTypeDef = TypedDict(
    "SensitiveDataDetectionsTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesUnionTypeDef],
    },
)
SecurityHubPolicyOutputTypeDef = TypedDict(
    "SecurityHubPolicyOutputTypeDef",
    {
        "ServiceEnabled": NotRequired[bool],
        "EnabledStandardIdentifiers": NotRequired[List[str]],
        "SecurityControlsConfiguration": NotRequired[SecurityControlsConfigurationOutputTypeDef],
    },
)
SecurityControlCustomParameterTypeDef = TypedDict(
    "SecurityControlCustomParameterTypeDef",
    {
        "SecurityControlId": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, ParameterConfigurationUnionTypeDef]],
    },
)
UpdateSecurityControlRequestRequestTypeDef = TypedDict(
    "UpdateSecurityControlRequestRequestTypeDef",
    {
        "SecurityControlId": str,
        "Parameters": Mapping[str, ParameterConfigurationUnionTypeDef],
        "LastUpdateReason": NotRequired[str],
    },
)
RuleGroupSourceStatelessRuleDefinitionTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    {
        "Actions": NotRequired[Sequence[str]],
        "MatchAttributes": NotRequired[RuleGroupSourceStatelessRuleMatchAttributesUnionTypeDef],
    },
)
FirewallPolicyDetailsOutputTypeDef = TypedDict(
    "FirewallPolicyDetailsOutputTypeDef",
    {
        "StatefulRuleGroupReferences": NotRequired[
            List[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]
        ],
        "StatelessCustomActions": NotRequired[
            List[FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef]
        ],
        "StatelessDefaultActions": NotRequired[List[str]],
        "StatelessFragmentDefaultActions": NotRequired[List[str]],
        "StatelessRuleGroupReferences": NotRequired[
            List[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]
        ],
    },
)
RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef",
    {
        "CustomActions": NotRequired[List[RuleGroupSourceCustomActionsDetailsOutputTypeDef]],
        "StatelessRules": NotRequired[List[RuleGroupSourceStatelessRulesDetailsOutputTypeDef]],
    },
)
StatelessCustomActionDefinitionUnionTypeDef = Union[
    StatelessCustomActionDefinitionTypeDef, StatelessCustomActionDefinitionOutputTypeDef
]
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": NotRequired[str],
        "NetworkConnectionAction": NotRequired[NetworkConnectionActionTypeDef],
        "AwsApiCallAction": NotRequired[AwsApiCallActionUnionTypeDef],
        "DnsRequestAction": NotRequired[DnsRequestActionTypeDef],
        "PortProbeAction": NotRequired[PortProbeActionUnionTypeDef],
    },
)
CreateAutomationRuleRequestRequestTypeDef = TypedDict(
    "CreateAutomationRuleRequestRequestTypeDef",
    {
        "RuleOrder": int,
        "RuleName": str,
        "Description": str,
        "Criteria": AutomationRulesFindingFiltersTypeDef,
        "Actions": Sequence[AutomationRulesActionUnionTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "RuleStatus": NotRequired[RuleStatusType],
        "IsTerminal": NotRequired[bool],
    },
)
UpdateAutomationRulesRequestItemTypeDef = TypedDict(
    "UpdateAutomationRulesRequestItemTypeDef",
    {
        "RuleArn": str,
        "RuleStatus": NotRequired[RuleStatusType],
        "RuleOrder": NotRequired[int],
        "Description": NotRequired[str],
        "RuleName": NotRequired[str],
        "IsTerminal": NotRequired[bool],
        "Criteria": NotRequired[AutomationRulesFindingFiltersUnionTypeDef],
        "Actions": NotRequired[Sequence[AutomationRulesActionUnionTypeDef]],
    },
)
AwsAutoScalingAutoScalingGroupDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    {
        "LaunchConfigurationName": NotRequired[str],
        "LoadBalancerNames": NotRequired[Sequence[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "CreatedTime": NotRequired[str],
        "MixedInstancesPolicy": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnionTypeDef
        ],
        "AvailabilityZones": NotRequired[
            Sequence[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]
        ],
        "LaunchTemplate": NotRequired[
            AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef
        ],
        "CapacityRebalance": NotRequired[bool],
    },
)
AwsBackupBackupPlanBackupPlanDetailsUnionTypeDef = Union[
    AwsBackupBackupPlanBackupPlanDetailsTypeDef, AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef
]
AwsCertificateManagerCertificateDetailsUnionTypeDef = Union[
    AwsCertificateManagerCertificateDetailsTypeDef,
    AwsCertificateManagerCertificateDetailsOutputTypeDef,
]
AwsCloudFrontDistributionOriginGroupUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginGroupTypeDef, AwsCloudFrontDistributionOriginGroupOutputTypeDef
]
AwsCloudFrontDistributionOriginItemUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginItemTypeDef, AwsCloudFrontDistributionOriginItemOutputTypeDef
]
AwsDynamoDbTableDetailsUnionTypeDef = Union[
    AwsDynamoDbTableDetailsTypeDef, AwsDynamoDbTableDetailsOutputTypeDef
]
AwsEc2LaunchTemplateDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDetailsTypeDef",
    {
        "LaunchTemplateName": NotRequired[str],
        "Id": NotRequired[str],
        "LaunchTemplateData": NotRequired[AwsEc2LaunchTemplateDataDetailsUnionTypeDef],
        "DefaultVersionNumber": NotRequired[int],
        "LatestVersionNumber": NotRequired[int],
    },
)
AwsEc2VpnConnectionDetailsUnionTypeDef = Union[
    AwsEc2VpnConnectionDetailsTypeDef, AwsEc2VpnConnectionDetailsOutputTypeDef
]
AwsEcsServiceDetailsUnionTypeDef = Union[
    AwsEcsServiceDetailsTypeDef, AwsEcsServiceDetailsOutputTypeDef
]
AwsEcsTaskDefinitionContainerDefinitionsDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef,
]
AwsEksClusterDetailsUnionTypeDef = Union[
    AwsEksClusterDetailsTypeDef, AwsEksClusterDetailsOutputTypeDef
]
AwsGuardDutyDetectorDetailsUnionTypeDef = Union[
    AwsGuardDutyDetectorDetailsTypeDef, AwsGuardDutyDetectorDetailsOutputTypeDef
]
AwsMskClusterClusterInfoDetailsUnionTypeDef = Union[
    AwsMskClusterClusterInfoDetailsTypeDef, AwsMskClusterClusterInfoDetailsOutputTypeDef
]
AwsRdsDbInstanceDetailsUnionTypeDef = Union[
    AwsRdsDbInstanceDetailsTypeDef, AwsRdsDbInstanceDetailsOutputTypeDef
]
AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef",
    {
        "Rules": NotRequired[
            List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef]
        ],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnionTypeDef = Union[
    AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef,
    AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef,
]
AwsS3BucketNotificationConfigurationDetailTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    {
        "Events": NotRequired[Sequence[str]],
        "Filter": NotRequired[AwsS3BucketNotificationConfigurationFilterUnionTypeDef],
        "Destination": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsStepFunctionStateMachineDetailsUnionTypeDef = Union[
    AwsStepFunctionStateMachineDetailsTypeDef, AwsStepFunctionStateMachineDetailsOutputTypeDef
]
AwsWafv2RuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RuleGroupDetailsOutputTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Rules": NotRequired[List[AwsWafv2RulesDetailsOutputTypeDef]],
        "Scope": NotRequired[str],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
AwsWafv2WebAclDetailsOutputTypeDef = TypedDict(
    "AwsWafv2WebAclDetailsOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "ManagedbyFirewallManager": NotRequired[bool],
        "Id": NotRequired[str],
        "Capacity": NotRequired[int],
        "CaptchaConfig": NotRequired[AwsWafv2WebAclCaptchaConfigDetailsTypeDef],
        "DefaultAction": NotRequired[AwsWafv2WebAclActionDetailsOutputTypeDef],
        "Description": NotRequired[str],
        "Rules": NotRequired[List[AwsWafv2RulesDetailsOutputTypeDef]],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
AwsWafv2RulesActionDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionDetailsTypeDef",
    {
        "Allow": NotRequired[AwsWafv2ActionAllowDetailsUnionTypeDef],
        "Block": NotRequired[AwsWafv2ActionBlockDetailsUnionTypeDef],
        "Captcha": NotRequired[AwsWafv2RulesActionCaptchaDetailsUnionTypeDef],
        "Count": NotRequired[AwsWafv2RulesActionCountDetailsUnionTypeDef],
    },
)
AwsWafv2WebAclActionDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclActionDetailsTypeDef",
    {
        "Allow": NotRequired[AwsWafv2ActionAllowDetailsUnionTypeDef],
        "Block": NotRequired[AwsWafv2ActionBlockDetailsUnionTypeDef],
    },
)
NetworkPathComponentTypeDef = TypedDict(
    "NetworkPathComponentTypeDef",
    {
        "ComponentId": NotRequired[str],
        "ComponentType": NotRequired[str],
        "Egress": NotRequired[NetworkHeaderUnionTypeDef],
        "Ingress": NotRequired[NetworkHeaderUnionTypeDef],
    },
)
ClassificationResultOutputTypeDef = TypedDict(
    "ClassificationResultOutputTypeDef",
    {
        "MimeType": NotRequired[str],
        "SizeClassified": NotRequired[int],
        "AdditionalOccurrences": NotRequired[bool],
        "Status": NotRequired[ClassificationStatusTypeDef],
        "SensitiveData": NotRequired[List[SensitiveDataResultOutputTypeDef]],
        "CustomDataIdentifiers": NotRequired[CustomDataIdentifiersResultOutputTypeDef],
    },
)
CustomDataIdentifiersDetectionsUnionTypeDef = Union[
    CustomDataIdentifiersDetectionsTypeDef, CustomDataIdentifiersDetectionsOutputTypeDef
]
SensitiveDataDetectionsUnionTypeDef = Union[
    SensitiveDataDetectionsTypeDef, SensitiveDataDetectionsOutputTypeDef
]
PolicyOutputTypeDef = TypedDict(
    "PolicyOutputTypeDef",
    {
        "SecurityHub": NotRequired[SecurityHubPolicyOutputTypeDef],
    },
)
SecurityControlCustomParameterUnionTypeDef = Union[
    SecurityControlCustomParameterTypeDef, SecurityControlCustomParameterOutputTypeDef
]
RuleGroupSourceStatelessRuleDefinitionUnionTypeDef = Union[
    RuleGroupSourceStatelessRuleDefinitionTypeDef,
    RuleGroupSourceStatelessRuleDefinitionOutputTypeDef,
]
AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef",
    {
        "FirewallPolicy": NotRequired[FirewallPolicyDetailsOutputTypeDef],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyId": NotRequired[str],
        "FirewallPolicyName": NotRequired[str],
        "Description": NotRequired[str],
    },
)
RuleGroupSourceOutputTypeDef = TypedDict(
    "RuleGroupSourceOutputTypeDef",
    {
        "RulesSourceList": NotRequired[RuleGroupSourceListDetailsOutputTypeDef],
        "RulesString": NotRequired[str],
        "StatefulRules": NotRequired[List[RuleGroupSourceStatefulRulesDetailsOutputTypeDef]],
        "StatelessRulesAndCustomActions": NotRequired[
            RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef
        ],
    },
)
FirewallPolicyStatelessCustomActionsDetailsTypeDef = TypedDict(
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    {
        "ActionDefinition": NotRequired[StatelessCustomActionDefinitionUnionTypeDef],
        "ActionName": NotRequired[str],
    },
)
RuleGroupSourceCustomActionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    {
        "ActionDefinition": NotRequired[StatelessCustomActionDefinitionUnionTypeDef],
        "ActionName": NotRequired[str],
    },
)
ActionUnionTypeDef = Union[ActionTypeDef, ActionOutputTypeDef]
BatchUpdateAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchUpdateAutomationRulesRequestRequestTypeDef",
    {
        "UpdateAutomationRulesRequestItems": Sequence[UpdateAutomationRulesRequestItemTypeDef],
    },
)
AwsAutoScalingAutoScalingGroupDetailsUnionTypeDef = Union[
    AwsAutoScalingAutoScalingGroupDetailsTypeDef, AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef
]
AwsBackupBackupPlanDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanDetailsTypeDef",
    {
        "BackupPlan": NotRequired[AwsBackupBackupPlanBackupPlanDetailsUnionTypeDef],
        "BackupPlanArn": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)
AwsCloudFrontDistributionOriginGroupsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    {
        "Items": NotRequired[Sequence[AwsCloudFrontDistributionOriginGroupUnionTypeDef]],
    },
)
AwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsTypeDef",
    {
        "Items": NotRequired[Sequence[AwsCloudFrontDistributionOriginItemUnionTypeDef]],
    },
)
AwsEc2LaunchTemplateDetailsUnionTypeDef = Union[
    AwsEc2LaunchTemplateDetailsTypeDef, AwsEc2LaunchTemplateDetailsOutputTypeDef
]
AwsEcsTaskDefinitionDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionDetailsTypeDef",
    {
        "ContainerDefinitions": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsDetailsUnionTypeDef]
        ],
        "Cpu": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "Family": NotRequired[str],
        "InferenceAccelerators": NotRequired[
            Sequence[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]
        ],
        "IpcMode": NotRequired[str],
        "Memory": NotRequired[str],
        "NetworkMode": NotRequired[str],
        "PidMode": NotRequired[str],
        "PlacementConstraints": NotRequired[
            Sequence[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]
        ],
        "ProxyConfiguration": NotRequired[
            AwsEcsTaskDefinitionProxyConfigurationDetailsUnionTypeDef
        ],
        "RequiresCompatibilities": NotRequired[Sequence[str]],
        "TaskRoleArn": NotRequired[str],
        "Volumes": NotRequired[Sequence[AwsEcsTaskDefinitionVolumesDetailsUnionTypeDef]],
        "Status": NotRequired[str],
    },
)
AwsMskClusterDetailsTypeDef = TypedDict(
    "AwsMskClusterDetailsTypeDef",
    {
        "ClusterInfo": NotRequired[AwsMskClusterClusterInfoDetailsUnionTypeDef],
    },
)
AwsS3BucketDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketDetailsOutputTypeDef",
    {
        "OwnerId": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[
            AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef
        ],
        "BucketLifecycleConfiguration": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef
        ],
        "PublicAccessBlockConfiguration": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AccessControlList": NotRequired[str],
        "BucketLoggingConfiguration": NotRequired[AwsS3BucketLoggingConfigurationTypeDef],
        "BucketWebsiteConfiguration": NotRequired[AwsS3BucketWebsiteConfigurationOutputTypeDef],
        "BucketNotificationConfiguration": NotRequired[
            AwsS3BucketNotificationConfigurationOutputTypeDef
        ],
        "BucketVersioningConfiguration": NotRequired[
            AwsS3BucketBucketVersioningConfigurationTypeDef
        ],
        "ObjectLockConfiguration": NotRequired[AwsS3BucketObjectLockConfigurationTypeDef],
        "Name": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    {
        "AbortIncompleteMultipartUpload": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef
        ],
        "ExpirationDate": NotRequired[str],
        "ExpirationInDays": NotRequired[int],
        "ExpiredObjectDeleteMarker": NotRequired[bool],
        "Filter": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnionTypeDef
        ],
        "ID": NotRequired[str],
        "NoncurrentVersionExpirationInDays": NotRequired[int],
        "NoncurrentVersionTransitions": NotRequired[
            Sequence[
                AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef
            ]
        ],
        "Prefix": NotRequired[str],
        "Status": NotRequired[str],
        "Transitions": NotRequired[
            Sequence[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]
        ],
    },
)
AwsS3BucketNotificationConfigurationDetailUnionTypeDef = Union[
    AwsS3BucketNotificationConfigurationDetailTypeDef,
    AwsS3BucketNotificationConfigurationDetailOutputTypeDef,
]
AwsWafv2RulesActionDetailsUnionTypeDef = Union[
    AwsWafv2RulesActionDetailsTypeDef, AwsWafv2RulesActionDetailsOutputTypeDef
]
AwsWafv2WebAclActionDetailsUnionTypeDef = Union[
    AwsWafv2WebAclActionDetailsTypeDef, AwsWafv2WebAclActionDetailsOutputTypeDef
]
NetworkPathComponentUnionTypeDef = Union[
    NetworkPathComponentTypeDef, NetworkPathComponentOutputTypeDef
]
DataClassificationDetailsOutputTypeDef = TypedDict(
    "DataClassificationDetailsOutputTypeDef",
    {
        "DetailedResultsLocation": NotRequired[str],
        "Result": NotRequired[ClassificationResultOutputTypeDef],
    },
)
CustomDataIdentifiersResultTypeDef = TypedDict(
    "CustomDataIdentifiersResultTypeDef",
    {
        "Detections": NotRequired[Sequence[CustomDataIdentifiersDetectionsUnionTypeDef]],
        "TotalCount": NotRequired[int],
    },
)
SensitiveDataResultTypeDef = TypedDict(
    "SensitiveDataResultTypeDef",
    {
        "Category": NotRequired[str],
        "Detections": NotRequired[Sequence[SensitiveDataDetectionsUnionTypeDef]],
        "TotalCount": NotRequired[int],
    },
)
CreateConfigurationPolicyResponseTypeDef = TypedDict(
    "CreateConfigurationPolicyResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "UpdatedAt": datetime,
        "CreatedAt": datetime,
        "ConfigurationPolicy": PolicyOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfigurationPolicyResponseTypeDef = TypedDict(
    "GetConfigurationPolicyResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "UpdatedAt": datetime,
        "CreatedAt": datetime,
        "ConfigurationPolicy": PolicyOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfigurationPolicyResponseTypeDef = TypedDict(
    "UpdateConfigurationPolicyResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "UpdatedAt": datetime,
        "CreatedAt": datetime,
        "ConfigurationPolicy": PolicyOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SecurityControlsConfigurationTypeDef = TypedDict(
    "SecurityControlsConfigurationTypeDef",
    {
        "EnabledSecurityControlIdentifiers": NotRequired[Sequence[str]],
        "DisabledSecurityControlIdentifiers": NotRequired[Sequence[str]],
        "SecurityControlCustomParameters": NotRequired[
            Sequence[SecurityControlCustomParameterUnionTypeDef]
        ],
    },
)
RuleGroupSourceStatelessRulesDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    {
        "Priority": NotRequired[int],
        "RuleDefinition": NotRequired[RuleGroupSourceStatelessRuleDefinitionUnionTypeDef],
    },
)
RuleGroupDetailsOutputTypeDef = TypedDict(
    "RuleGroupDetailsOutputTypeDef",
    {
        "RuleVariables": NotRequired[RuleGroupVariablesOutputTypeDef],
        "RulesSource": NotRequired[RuleGroupSourceOutputTypeDef],
    },
)
FirewallPolicyStatelessCustomActionsDetailsUnionTypeDef = Union[
    FirewallPolicyStatelessCustomActionsDetailsTypeDef,
    FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef,
]
RuleGroupSourceCustomActionsDetailsUnionTypeDef = Union[
    RuleGroupSourceCustomActionsDetailsTypeDef, RuleGroupSourceCustomActionsDetailsOutputTypeDef
]
AwsBackupBackupPlanDetailsUnionTypeDef = Union[
    AwsBackupBackupPlanDetailsTypeDef, AwsBackupBackupPlanDetailsOutputTypeDef
]
AwsCloudFrontDistributionOriginGroupsUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginGroupsTypeDef, AwsCloudFrontDistributionOriginGroupsOutputTypeDef
]
AwsCloudFrontDistributionOriginsUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginsTypeDef, AwsCloudFrontDistributionOriginsOutputTypeDef
]
AwsEcsTaskDefinitionDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionDetailsTypeDef, AwsEcsTaskDefinitionDetailsOutputTypeDef
]
AwsMskClusterDetailsUnionTypeDef = Union[
    AwsMskClusterDetailsTypeDef, AwsMskClusterDetailsOutputTypeDef
]
AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnionTypeDef = Union[
    AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef,
    AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef,
]
AwsS3BucketNotificationConfigurationTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationTypeDef",
    {
        "Configurations": NotRequired[
            Sequence[AwsS3BucketNotificationConfigurationDetailUnionTypeDef]
        ],
    },
)
AwsWafv2RulesDetailsTypeDef = TypedDict(
    "AwsWafv2RulesDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafv2RulesActionDetailsUnionTypeDef],
        "Name": NotRequired[str],
        "OverrideAction": NotRequired[str],
        "Priority": NotRequired[int],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
CustomDataIdentifiersResultUnionTypeDef = Union[
    CustomDataIdentifiersResultTypeDef, CustomDataIdentifiersResultOutputTypeDef
]
SensitiveDataResultUnionTypeDef = Union[
    SensitiveDataResultTypeDef, SensitiveDataResultOutputTypeDef
]
SecurityControlsConfigurationUnionTypeDef = Union[
    SecurityControlsConfigurationTypeDef, SecurityControlsConfigurationOutputTypeDef
]
RuleGroupSourceStatelessRulesDetailsUnionTypeDef = Union[
    RuleGroupSourceStatelessRulesDetailsTypeDef, RuleGroupSourceStatelessRulesDetailsOutputTypeDef
]
AwsNetworkFirewallRuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsOutputTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "RuleGroup": NotRequired[RuleGroupDetailsOutputTypeDef],
        "RuleGroupArn": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "RuleGroupName": NotRequired[str],
        "Type": NotRequired[str],
    },
)
FirewallPolicyDetailsTypeDef = TypedDict(
    "FirewallPolicyDetailsTypeDef",
    {
        "StatefulRuleGroupReferences": NotRequired[
            Sequence[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]
        ],
        "StatelessCustomActions": NotRequired[
            Sequence[FirewallPolicyStatelessCustomActionsDetailsUnionTypeDef]
        ],
        "StatelessDefaultActions": NotRequired[Sequence[str]],
        "StatelessFragmentDefaultActions": NotRequired[Sequence[str]],
        "StatelessRuleGroupReferences": NotRequired[
            Sequence[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]
        ],
    },
)
AwsCloudFrontDistributionDetailsTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsTypeDef",
    {
        "CacheBehaviors": NotRequired[AwsCloudFrontDistributionCacheBehaviorsUnionTypeDef],
        "DefaultCacheBehavior": NotRequired[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef],
        "DefaultRootObject": NotRequired[str],
        "DomainName": NotRequired[str],
        "ETag": NotRequired[str],
        "LastModifiedTime": NotRequired[str],
        "Logging": NotRequired[AwsCloudFrontDistributionLoggingTypeDef],
        "Origins": NotRequired[AwsCloudFrontDistributionOriginsUnionTypeDef],
        "OriginGroups": NotRequired[AwsCloudFrontDistributionOriginGroupsUnionTypeDef],
        "ViewerCertificate": NotRequired[AwsCloudFrontDistributionViewerCertificateTypeDef],
        "Status": NotRequired[str],
        "WebAclId": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    {
        "Rules": NotRequired[
            Sequence[AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnionTypeDef]
        ],
    },
)
AwsS3BucketNotificationConfigurationUnionTypeDef = Union[
    AwsS3BucketNotificationConfigurationTypeDef, AwsS3BucketNotificationConfigurationOutputTypeDef
]
AwsWafv2RuleGroupDetailsTypeDef = TypedDict(
    "AwsWafv2RuleGroupDetailsTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafv2RulesDetailsTypeDef]],
        "Scope": NotRequired[str],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
AwsWafv2RulesDetailsUnionTypeDef = Union[
    AwsWafv2RulesDetailsTypeDef, AwsWafv2RulesDetailsOutputTypeDef
]
ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "MimeType": NotRequired[str],
        "SizeClassified": NotRequired[int],
        "AdditionalOccurrences": NotRequired[bool],
        "Status": NotRequired[ClassificationStatusTypeDef],
        "SensitiveData": NotRequired[Sequence[SensitiveDataResultUnionTypeDef]],
        "CustomDataIdentifiers": NotRequired[CustomDataIdentifiersResultUnionTypeDef],
    },
)
SecurityHubPolicyTypeDef = TypedDict(
    "SecurityHubPolicyTypeDef",
    {
        "ServiceEnabled": NotRequired[bool],
        "EnabledStandardIdentifiers": NotRequired[Sequence[str]],
        "SecurityControlsConfiguration": NotRequired[SecurityControlsConfigurationUnionTypeDef],
    },
)
RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    {
        "CustomActions": NotRequired[Sequence[RuleGroupSourceCustomActionsDetailsUnionTypeDef]],
        "StatelessRules": NotRequired[Sequence[RuleGroupSourceStatelessRulesDetailsUnionTypeDef]],
    },
)
ResourceDetailsOutputTypeDef = TypedDict(
    "ResourceDetailsOutputTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": NotRequired[
            AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef
        ],
        "AwsCodeBuildProject": NotRequired[AwsCodeBuildProjectDetailsOutputTypeDef],
        "AwsCloudFrontDistribution": NotRequired[AwsCloudFrontDistributionDetailsOutputTypeDef],
        "AwsEc2Instance": NotRequired[AwsEc2InstanceDetailsOutputTypeDef],
        "AwsEc2NetworkInterface": NotRequired[AwsEc2NetworkInterfaceDetailsOutputTypeDef],
        "AwsEc2SecurityGroup": NotRequired[AwsEc2SecurityGroupDetailsOutputTypeDef],
        "AwsEc2Volume": NotRequired[AwsEc2VolumeDetailsOutputTypeDef],
        "AwsEc2Vpc": NotRequired[AwsEc2VpcDetailsOutputTypeDef],
        "AwsEc2Eip": NotRequired[AwsEc2EipDetailsTypeDef],
        "AwsEc2Subnet": NotRequired[AwsEc2SubnetDetailsOutputTypeDef],
        "AwsEc2NetworkAcl": NotRequired[AwsEc2NetworkAclDetailsOutputTypeDef],
        "AwsElbv2LoadBalancer": NotRequired[AwsElbv2LoadBalancerDetailsOutputTypeDef],
        "AwsElasticBeanstalkEnvironment": NotRequired[
            AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef
        ],
        "AwsElasticsearchDomain": NotRequired[AwsElasticsearchDomainDetailsOutputTypeDef],
        "AwsS3Bucket": NotRequired[AwsS3BucketDetailsOutputTypeDef],
        "AwsS3AccountPublicAccessBlock": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AwsS3Object": NotRequired[AwsS3ObjectDetailsTypeDef],
        "AwsSecretsManagerSecret": NotRequired[AwsSecretsManagerSecretDetailsTypeDef],
        "AwsIamAccessKey": NotRequired[AwsIamAccessKeyDetailsTypeDef],
        "AwsIamUser": NotRequired[AwsIamUserDetailsOutputTypeDef],
        "AwsIamPolicy": NotRequired[AwsIamPolicyDetailsOutputTypeDef],
        "AwsApiGatewayV2Stage": NotRequired[AwsApiGatewayV2StageDetailsOutputTypeDef],
        "AwsApiGatewayV2Api": NotRequired[AwsApiGatewayV2ApiDetailsOutputTypeDef],
        "AwsDynamoDbTable": NotRequired[AwsDynamoDbTableDetailsOutputTypeDef],
        "AwsApiGatewayStage": NotRequired[AwsApiGatewayStageDetailsOutputTypeDef],
        "AwsApiGatewayRestApi": NotRequired[AwsApiGatewayRestApiDetailsOutputTypeDef],
        "AwsCloudTrailTrail": NotRequired[AwsCloudTrailTrailDetailsTypeDef],
        "AwsSsmPatchCompliance": NotRequired[AwsSsmPatchComplianceDetailsTypeDef],
        "AwsCertificateManagerCertificate": NotRequired[
            AwsCertificateManagerCertificateDetailsOutputTypeDef
        ],
        "AwsRedshiftCluster": NotRequired[AwsRedshiftClusterDetailsOutputTypeDef],
        "AwsElbLoadBalancer": NotRequired[AwsElbLoadBalancerDetailsOutputTypeDef],
        "AwsIamGroup": NotRequired[AwsIamGroupDetailsOutputTypeDef],
        "AwsIamRole": NotRequired[AwsIamRoleDetailsOutputTypeDef],
        "AwsKmsKey": NotRequired[AwsKmsKeyDetailsTypeDef],
        "AwsLambdaFunction": NotRequired[AwsLambdaFunctionDetailsOutputTypeDef],
        "AwsLambdaLayerVersion": NotRequired[AwsLambdaLayerVersionDetailsOutputTypeDef],
        "AwsRdsDbInstance": NotRequired[AwsRdsDbInstanceDetailsOutputTypeDef],
        "AwsSnsTopic": NotRequired[AwsSnsTopicDetailsOutputTypeDef],
        "AwsSqsQueue": NotRequired[AwsSqsQueueDetailsTypeDef],
        "AwsWafWebAcl": NotRequired[AwsWafWebAclDetailsOutputTypeDef],
        "AwsRdsDbSnapshot": NotRequired[AwsRdsDbSnapshotDetailsOutputTypeDef],
        "AwsRdsDbClusterSnapshot": NotRequired[AwsRdsDbClusterSnapshotDetailsOutputTypeDef],
        "AwsRdsDbCluster": NotRequired[AwsRdsDbClusterDetailsOutputTypeDef],
        "AwsEcsCluster": NotRequired[AwsEcsClusterDetailsOutputTypeDef],
        "AwsEcsContainer": NotRequired[AwsEcsContainerDetailsOutputTypeDef],
        "AwsEcsTaskDefinition": NotRequired[AwsEcsTaskDefinitionDetailsOutputTypeDef],
        "Container": NotRequired[ContainerDetailsOutputTypeDef],
        "Other": NotRequired[Dict[str, str]],
        "AwsRdsEventSubscription": NotRequired[AwsRdsEventSubscriptionDetailsOutputTypeDef],
        "AwsEcsService": NotRequired[AwsEcsServiceDetailsOutputTypeDef],
        "AwsAutoScalingLaunchConfiguration": NotRequired[
            AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef
        ],
        "AwsEc2VpnConnection": NotRequired[AwsEc2VpnConnectionDetailsOutputTypeDef],
        "AwsEcrContainerImage": NotRequired[AwsEcrContainerImageDetailsOutputTypeDef],
        "AwsOpenSearchServiceDomain": NotRequired[AwsOpenSearchServiceDomainDetailsOutputTypeDef],
        "AwsEc2VpcEndpointService": NotRequired[AwsEc2VpcEndpointServiceDetailsOutputTypeDef],
        "AwsXrayEncryptionConfig": NotRequired[AwsXrayEncryptionConfigDetailsTypeDef],
        "AwsWafRateBasedRule": NotRequired[AwsWafRateBasedRuleDetailsOutputTypeDef],
        "AwsWafRegionalRateBasedRule": NotRequired[AwsWafRegionalRateBasedRuleDetailsOutputTypeDef],
        "AwsEcrRepository": NotRequired[AwsEcrRepositoryDetailsTypeDef],
        "AwsEksCluster": NotRequired[AwsEksClusterDetailsOutputTypeDef],
        "AwsNetworkFirewallFirewallPolicy": NotRequired[
            AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef
        ],
        "AwsNetworkFirewallFirewall": NotRequired[AwsNetworkFirewallFirewallDetailsOutputTypeDef],
        "AwsNetworkFirewallRuleGroup": NotRequired[AwsNetworkFirewallRuleGroupDetailsOutputTypeDef],
        "AwsRdsDbSecurityGroup": NotRequired[AwsRdsDbSecurityGroupDetailsOutputTypeDef],
        "AwsKinesisStream": NotRequired[AwsKinesisStreamDetailsTypeDef],
        "AwsEc2TransitGateway": NotRequired[AwsEc2TransitGatewayDetailsOutputTypeDef],
        "AwsEfsAccessPoint": NotRequired[AwsEfsAccessPointDetailsOutputTypeDef],
        "AwsCloudFormationStack": NotRequired[AwsCloudFormationStackDetailsOutputTypeDef],
        "AwsCloudWatchAlarm": NotRequired[AwsCloudWatchAlarmDetailsOutputTypeDef],
        "AwsEc2VpcPeeringConnection": NotRequired[AwsEc2VpcPeeringConnectionDetailsOutputTypeDef],
        "AwsWafRegionalRuleGroup": NotRequired[AwsWafRegionalRuleGroupDetailsOutputTypeDef],
        "AwsWafRegionalRule": NotRequired[AwsWafRegionalRuleDetailsOutputTypeDef],
        "AwsWafRegionalWebAcl": NotRequired[AwsWafRegionalWebAclDetailsOutputTypeDef],
        "AwsWafRule": NotRequired[AwsWafRuleDetailsOutputTypeDef],
        "AwsWafRuleGroup": NotRequired[AwsWafRuleGroupDetailsOutputTypeDef],
        "AwsEcsTask": NotRequired[AwsEcsTaskDetailsOutputTypeDef],
        "AwsBackupBackupVault": NotRequired[AwsBackupBackupVaultDetailsOutputTypeDef],
        "AwsBackupBackupPlan": NotRequired[AwsBackupBackupPlanDetailsOutputTypeDef],
        "AwsBackupRecoveryPoint": NotRequired[AwsBackupRecoveryPointDetailsTypeDef],
        "AwsEc2LaunchTemplate": NotRequired[AwsEc2LaunchTemplateDetailsOutputTypeDef],
        "AwsSageMakerNotebookInstance": NotRequired[
            AwsSageMakerNotebookInstanceDetailsOutputTypeDef
        ],
        "AwsWafv2WebAcl": NotRequired[AwsWafv2WebAclDetailsOutputTypeDef],
        "AwsWafv2RuleGroup": NotRequired[AwsWafv2RuleGroupDetailsOutputTypeDef],
        "AwsEc2RouteTable": NotRequired[AwsEc2RouteTableDetailsOutputTypeDef],
        "AwsAmazonMqBroker": NotRequired[AwsAmazonMqBrokerDetailsOutputTypeDef],
        "AwsAppSyncGraphQlApi": NotRequired[AwsAppSyncGraphQlApiDetailsOutputTypeDef],
        "AwsEventSchemasRegistry": NotRequired[AwsEventSchemasRegistryDetailsTypeDef],
        "AwsGuardDutyDetector": NotRequired[AwsGuardDutyDetectorDetailsOutputTypeDef],
        "AwsStepFunctionStateMachine": NotRequired[AwsStepFunctionStateMachineDetailsOutputTypeDef],
        "AwsAthenaWorkGroup": NotRequired[AwsAthenaWorkGroupDetailsTypeDef],
        "AwsEventsEventbus": NotRequired[AwsEventsEventbusDetailsTypeDef],
        "AwsDmsEndpoint": NotRequired[AwsDmsEndpointDetailsTypeDef],
        "AwsEventsEndpoint": NotRequired[AwsEventsEndpointDetailsOutputTypeDef],
        "AwsDmsReplicationTask": NotRequired[AwsDmsReplicationTaskDetailsTypeDef],
        "AwsDmsReplicationInstance": NotRequired[AwsDmsReplicationInstanceDetailsOutputTypeDef],
        "AwsRoute53HostedZone": NotRequired[AwsRoute53HostedZoneDetailsOutputTypeDef],
        "AwsMskCluster": NotRequired[AwsMskClusterDetailsOutputTypeDef],
        "AwsS3AccessPoint": NotRequired[AwsS3AccessPointDetailsTypeDef],
        "AwsEc2ClientVpnEndpoint": NotRequired[AwsEc2ClientVpnEndpointDetailsOutputTypeDef],
    },
)
FirewallPolicyDetailsUnionTypeDef = Union[
    FirewallPolicyDetailsTypeDef, FirewallPolicyDetailsOutputTypeDef
]
AwsCloudFrontDistributionDetailsUnionTypeDef = Union[
    AwsCloudFrontDistributionDetailsTypeDef, AwsCloudFrontDistributionDetailsOutputTypeDef
]
AwsS3BucketBucketLifecycleConfigurationDetailsUnionTypeDef = Union[
    AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef,
    AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef,
]
AwsWafv2RuleGroupDetailsUnionTypeDef = Union[
    AwsWafv2RuleGroupDetailsTypeDef, AwsWafv2RuleGroupDetailsOutputTypeDef
]
AwsWafv2WebAclDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "ManagedbyFirewallManager": NotRequired[bool],
        "Id": NotRequired[str],
        "Capacity": NotRequired[int],
        "CaptchaConfig": NotRequired[AwsWafv2WebAclCaptchaConfigDetailsTypeDef],
        "DefaultAction": NotRequired[AwsWafv2WebAclActionDetailsUnionTypeDef],
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafv2RulesDetailsUnionTypeDef]],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
ClassificationResultUnionTypeDef = Union[
    ClassificationResultTypeDef, ClassificationResultOutputTypeDef
]
SecurityHubPolicyUnionTypeDef = Union[SecurityHubPolicyTypeDef, SecurityHubPolicyOutputTypeDef]
RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnionTypeDef = Union[
    RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef,
    RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef,
]
ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": NotRequired[PartitionType],
        "Region": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "DataClassification": NotRequired[DataClassificationDetailsOutputTypeDef],
        "Details": NotRequired[ResourceDetailsOutputTypeDef],
        "ApplicationName": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)
AwsNetworkFirewallFirewallPolicyDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    {
        "FirewallPolicy": NotRequired[FirewallPolicyDetailsUnionTypeDef],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyId": NotRequired[str],
        "FirewallPolicyName": NotRequired[str],
        "Description": NotRequired[str],
    },
)
AwsS3BucketDetailsTypeDef = TypedDict(
    "AwsS3BucketDetailsTypeDef",
    {
        "OwnerId": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[
            AwsS3BucketServerSideEncryptionConfigurationUnionTypeDef
        ],
        "BucketLifecycleConfiguration": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationDetailsUnionTypeDef
        ],
        "PublicAccessBlockConfiguration": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AccessControlList": NotRequired[str],
        "BucketLoggingConfiguration": NotRequired[AwsS3BucketLoggingConfigurationTypeDef],
        "BucketWebsiteConfiguration": NotRequired[AwsS3BucketWebsiteConfigurationUnionTypeDef],
        "BucketNotificationConfiguration": NotRequired[
            AwsS3BucketNotificationConfigurationUnionTypeDef
        ],
        "BucketVersioningConfiguration": NotRequired[
            AwsS3BucketBucketVersioningConfigurationTypeDef
        ],
        "ObjectLockConfiguration": NotRequired[AwsS3BucketObjectLockConfigurationTypeDef],
        "Name": NotRequired[str],
    },
)
AwsWafv2WebAclDetailsUnionTypeDef = Union[
    AwsWafv2WebAclDetailsTypeDef, AwsWafv2WebAclDetailsOutputTypeDef
]
DataClassificationDetailsTypeDef = TypedDict(
    "DataClassificationDetailsTypeDef",
    {
        "DetailedResultsLocation": NotRequired[str],
        "Result": NotRequired[ClassificationResultUnionTypeDef],
    },
)
PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "SecurityHub": NotRequired[SecurityHubPolicyUnionTypeDef],
    },
)
RuleGroupSourceTypeDef = TypedDict(
    "RuleGroupSourceTypeDef",
    {
        "RulesSourceList": NotRequired[RuleGroupSourceListDetailsUnionTypeDef],
        "RulesString": NotRequired[str],
        "StatefulRules": NotRequired[Sequence[RuleGroupSourceStatefulRulesDetailsUnionTypeDef]],
        "StatelessRulesAndCustomActions": NotRequired[
            RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnionTypeDef
        ],
    },
)
AwsSecurityFindingOutputTypeDef = TypedDict(
    "AwsSecurityFindingOutputTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Title": str,
        "Description": str,
        "Resources": List[ResourceOutputTypeDef],
        "ProductName": NotRequired[str],
        "CompanyName": NotRequired[str],
        "Region": NotRequired[str],
        "Types": NotRequired[List[str]],
        "FirstObservedAt": NotRequired[str],
        "LastObservedAt": NotRequired[str],
        "Severity": NotRequired[SeverityTypeDef],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Remediation": NotRequired[RemediationTypeDef],
        "SourceUrl": NotRequired[str],
        "ProductFields": NotRequired[Dict[str, str]],
        "UserDefinedFields": NotRequired[Dict[str, str]],
        "Malware": NotRequired[List[MalwareTypeDef]],
        "Network": NotRequired[NetworkTypeDef],
        "NetworkPath": NotRequired[List[NetworkPathComponentOutputTypeDef]],
        "Process": NotRequired[ProcessDetailsTypeDef],
        "Threats": NotRequired[List[ThreatOutputTypeDef]],
        "ThreatIntelIndicators": NotRequired[List[ThreatIntelIndicatorTypeDef]],
        "Compliance": NotRequired[ComplianceOutputTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "WorkflowState": NotRequired[WorkflowStateType],
        "Workflow": NotRequired[WorkflowTypeDef],
        "RecordState": NotRequired[RecordStateType],
        "RelatedFindings": NotRequired[List[RelatedFindingTypeDef]],
        "Note": NotRequired[NoteTypeDef],
        "Vulnerabilities": NotRequired[List[VulnerabilityOutputTypeDef]],
        "PatchSummary": NotRequired[PatchSummaryTypeDef],
        "Action": NotRequired[ActionOutputTypeDef],
        "FindingProviderFields": NotRequired[FindingProviderFieldsOutputTypeDef],
        "Sample": NotRequired[bool],
        "GeneratorDetails": NotRequired[GeneratorDetailsOutputTypeDef],
        "ProcessedAt": NotRequired[str],
        "AwsAccountName": NotRequired[str],
    },
)
AwsNetworkFirewallFirewallPolicyDetailsUnionTypeDef = Union[
    AwsNetworkFirewallFirewallPolicyDetailsTypeDef,
    AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef,
]
AwsS3BucketDetailsUnionTypeDef = Union[AwsS3BucketDetailsTypeDef, AwsS3BucketDetailsOutputTypeDef]
DataClassificationDetailsUnionTypeDef = Union[
    DataClassificationDetailsTypeDef, DataClassificationDetailsOutputTypeDef
]
CreateConfigurationPolicyRequestRequestTypeDef = TypedDict(
    "CreateConfigurationPolicyRequestRequestTypeDef",
    {
        "Name": str,
        "ConfigurationPolicy": PolicyTypeDef,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateConfigurationPolicyRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationPolicyRequestRequestTypeDef",
    {
        "Identifier": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "UpdatedReason": NotRequired[str],
        "ConfigurationPolicy": NotRequired[PolicyTypeDef],
    },
)
RuleGroupSourceUnionTypeDef = Union[RuleGroupSourceTypeDef, RuleGroupSourceOutputTypeDef]
GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List[AwsSecurityFindingOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RuleGroupDetailsTypeDef = TypedDict(
    "RuleGroupDetailsTypeDef",
    {
        "RuleVariables": NotRequired[RuleGroupVariablesUnionTypeDef],
        "RulesSource": NotRequired[RuleGroupSourceUnionTypeDef],
    },
)
RuleGroupDetailsUnionTypeDef = Union[RuleGroupDetailsTypeDef, RuleGroupDetailsOutputTypeDef]
AwsNetworkFirewallRuleGroupDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "RuleGroup": NotRequired[RuleGroupDetailsUnionTypeDef],
        "RuleGroupArn": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "RuleGroupName": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsNetworkFirewallRuleGroupDetailsUnionTypeDef = Union[
    AwsNetworkFirewallRuleGroupDetailsTypeDef, AwsNetworkFirewallRuleGroupDetailsOutputTypeDef
]
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": NotRequired[
            AwsAutoScalingAutoScalingGroupDetailsUnionTypeDef
        ],
        "AwsCodeBuildProject": NotRequired[AwsCodeBuildProjectDetailsUnionTypeDef],
        "AwsCloudFrontDistribution": NotRequired[AwsCloudFrontDistributionDetailsUnionTypeDef],
        "AwsEc2Instance": NotRequired[AwsEc2InstanceDetailsUnionTypeDef],
        "AwsEc2NetworkInterface": NotRequired[AwsEc2NetworkInterfaceDetailsUnionTypeDef],
        "AwsEc2SecurityGroup": NotRequired[AwsEc2SecurityGroupDetailsUnionTypeDef],
        "AwsEc2Volume": NotRequired[AwsEc2VolumeDetailsUnionTypeDef],
        "AwsEc2Vpc": NotRequired[AwsEc2VpcDetailsUnionTypeDef],
        "AwsEc2Eip": NotRequired[AwsEc2EipDetailsTypeDef],
        "AwsEc2Subnet": NotRequired[AwsEc2SubnetDetailsUnionTypeDef],
        "AwsEc2NetworkAcl": NotRequired[AwsEc2NetworkAclDetailsUnionTypeDef],
        "AwsElbv2LoadBalancer": NotRequired[AwsElbv2LoadBalancerDetailsUnionTypeDef],
        "AwsElasticBeanstalkEnvironment": NotRequired[
            AwsElasticBeanstalkEnvironmentDetailsUnionTypeDef
        ],
        "AwsElasticsearchDomain": NotRequired[AwsElasticsearchDomainDetailsUnionTypeDef],
        "AwsS3Bucket": NotRequired[AwsS3BucketDetailsUnionTypeDef],
        "AwsS3AccountPublicAccessBlock": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AwsS3Object": NotRequired[AwsS3ObjectDetailsTypeDef],
        "AwsSecretsManagerSecret": NotRequired[AwsSecretsManagerSecretDetailsTypeDef],
        "AwsIamAccessKey": NotRequired[AwsIamAccessKeyDetailsTypeDef],
        "AwsIamUser": NotRequired[AwsIamUserDetailsUnionTypeDef],
        "AwsIamPolicy": NotRequired[AwsIamPolicyDetailsUnionTypeDef],
        "AwsApiGatewayV2Stage": NotRequired[AwsApiGatewayV2StageDetailsUnionTypeDef],
        "AwsApiGatewayV2Api": NotRequired[AwsApiGatewayV2ApiDetailsUnionTypeDef],
        "AwsDynamoDbTable": NotRequired[AwsDynamoDbTableDetailsUnionTypeDef],
        "AwsApiGatewayStage": NotRequired[AwsApiGatewayStageDetailsUnionTypeDef],
        "AwsApiGatewayRestApi": NotRequired[AwsApiGatewayRestApiDetailsUnionTypeDef],
        "AwsCloudTrailTrail": NotRequired[AwsCloudTrailTrailDetailsTypeDef],
        "AwsSsmPatchCompliance": NotRequired[AwsSsmPatchComplianceDetailsTypeDef],
        "AwsCertificateManagerCertificate": NotRequired[
            AwsCertificateManagerCertificateDetailsUnionTypeDef
        ],
        "AwsRedshiftCluster": NotRequired[AwsRedshiftClusterDetailsUnionTypeDef],
        "AwsElbLoadBalancer": NotRequired[AwsElbLoadBalancerDetailsUnionTypeDef],
        "AwsIamGroup": NotRequired[AwsIamGroupDetailsUnionTypeDef],
        "AwsIamRole": NotRequired[AwsIamRoleDetailsUnionTypeDef],
        "AwsKmsKey": NotRequired[AwsKmsKeyDetailsTypeDef],
        "AwsLambdaFunction": NotRequired[AwsLambdaFunctionDetailsUnionTypeDef],
        "AwsLambdaLayerVersion": NotRequired[AwsLambdaLayerVersionDetailsUnionTypeDef],
        "AwsRdsDbInstance": NotRequired[AwsRdsDbInstanceDetailsUnionTypeDef],
        "AwsSnsTopic": NotRequired[AwsSnsTopicDetailsUnionTypeDef],
        "AwsSqsQueue": NotRequired[AwsSqsQueueDetailsTypeDef],
        "AwsWafWebAcl": NotRequired[AwsWafWebAclDetailsUnionTypeDef],
        "AwsRdsDbSnapshot": NotRequired[AwsRdsDbSnapshotDetailsUnionTypeDef],
        "AwsRdsDbClusterSnapshot": NotRequired[AwsRdsDbClusterSnapshotDetailsUnionTypeDef],
        "AwsRdsDbCluster": NotRequired[AwsRdsDbClusterDetailsUnionTypeDef],
        "AwsEcsCluster": NotRequired[AwsEcsClusterDetailsUnionTypeDef],
        "AwsEcsContainer": NotRequired[AwsEcsContainerDetailsUnionTypeDef],
        "AwsEcsTaskDefinition": NotRequired[AwsEcsTaskDefinitionDetailsUnionTypeDef],
        "Container": NotRequired[ContainerDetailsUnionTypeDef],
        "Other": NotRequired[Mapping[str, str]],
        "AwsRdsEventSubscription": NotRequired[AwsRdsEventSubscriptionDetailsUnionTypeDef],
        "AwsEcsService": NotRequired[AwsEcsServiceDetailsUnionTypeDef],
        "AwsAutoScalingLaunchConfiguration": NotRequired[
            AwsAutoScalingLaunchConfigurationDetailsUnionTypeDef
        ],
        "AwsEc2VpnConnection": NotRequired[AwsEc2VpnConnectionDetailsUnionTypeDef],
        "AwsEcrContainerImage": NotRequired[AwsEcrContainerImageDetailsUnionTypeDef],
        "AwsOpenSearchServiceDomain": NotRequired[AwsOpenSearchServiceDomainDetailsUnionTypeDef],
        "AwsEc2VpcEndpointService": NotRequired[AwsEc2VpcEndpointServiceDetailsUnionTypeDef],
        "AwsXrayEncryptionConfig": NotRequired[AwsXrayEncryptionConfigDetailsTypeDef],
        "AwsWafRateBasedRule": NotRequired[AwsWafRateBasedRuleDetailsUnionTypeDef],
        "AwsWafRegionalRateBasedRule": NotRequired[AwsWafRegionalRateBasedRuleDetailsUnionTypeDef],
        "AwsEcrRepository": NotRequired[AwsEcrRepositoryDetailsTypeDef],
        "AwsEksCluster": NotRequired[AwsEksClusterDetailsUnionTypeDef],
        "AwsNetworkFirewallFirewallPolicy": NotRequired[
            AwsNetworkFirewallFirewallPolicyDetailsUnionTypeDef
        ],
        "AwsNetworkFirewallFirewall": NotRequired[AwsNetworkFirewallFirewallDetailsUnionTypeDef],
        "AwsNetworkFirewallRuleGroup": NotRequired[AwsNetworkFirewallRuleGroupDetailsUnionTypeDef],
        "AwsRdsDbSecurityGroup": NotRequired[AwsRdsDbSecurityGroupDetailsUnionTypeDef],
        "AwsKinesisStream": NotRequired[AwsKinesisStreamDetailsTypeDef],
        "AwsEc2TransitGateway": NotRequired[AwsEc2TransitGatewayDetailsUnionTypeDef],
        "AwsEfsAccessPoint": NotRequired[AwsEfsAccessPointDetailsUnionTypeDef],
        "AwsCloudFormationStack": NotRequired[AwsCloudFormationStackDetailsUnionTypeDef],
        "AwsCloudWatchAlarm": NotRequired[AwsCloudWatchAlarmDetailsUnionTypeDef],
        "AwsEc2VpcPeeringConnection": NotRequired[AwsEc2VpcPeeringConnectionDetailsUnionTypeDef],
        "AwsWafRegionalRuleGroup": NotRequired[AwsWafRegionalRuleGroupDetailsUnionTypeDef],
        "AwsWafRegionalRule": NotRequired[AwsWafRegionalRuleDetailsUnionTypeDef],
        "AwsWafRegionalWebAcl": NotRequired[AwsWafRegionalWebAclDetailsUnionTypeDef],
        "AwsWafRule": NotRequired[AwsWafRuleDetailsUnionTypeDef],
        "AwsWafRuleGroup": NotRequired[AwsWafRuleGroupDetailsUnionTypeDef],
        "AwsEcsTask": NotRequired[AwsEcsTaskDetailsUnionTypeDef],
        "AwsBackupBackupVault": NotRequired[AwsBackupBackupVaultDetailsUnionTypeDef],
        "AwsBackupBackupPlan": NotRequired[AwsBackupBackupPlanDetailsUnionTypeDef],
        "AwsBackupRecoveryPoint": NotRequired[AwsBackupRecoveryPointDetailsTypeDef],
        "AwsEc2LaunchTemplate": NotRequired[AwsEc2LaunchTemplateDetailsUnionTypeDef],
        "AwsSageMakerNotebookInstance": NotRequired[
            AwsSageMakerNotebookInstanceDetailsUnionTypeDef
        ],
        "AwsWafv2WebAcl": NotRequired[AwsWafv2WebAclDetailsUnionTypeDef],
        "AwsWafv2RuleGroup": NotRequired[AwsWafv2RuleGroupDetailsUnionTypeDef],
        "AwsEc2RouteTable": NotRequired[AwsEc2RouteTableDetailsUnionTypeDef],
        "AwsAmazonMqBroker": NotRequired[AwsAmazonMqBrokerDetailsUnionTypeDef],
        "AwsAppSyncGraphQlApi": NotRequired[AwsAppSyncGraphQlApiDetailsUnionTypeDef],
        "AwsEventSchemasRegistry": NotRequired[AwsEventSchemasRegistryDetailsTypeDef],
        "AwsGuardDutyDetector": NotRequired[AwsGuardDutyDetectorDetailsUnionTypeDef],
        "AwsStepFunctionStateMachine": NotRequired[AwsStepFunctionStateMachineDetailsUnionTypeDef],
        "AwsAthenaWorkGroup": NotRequired[AwsAthenaWorkGroupDetailsTypeDef],
        "AwsEventsEventbus": NotRequired[AwsEventsEventbusDetailsTypeDef],
        "AwsDmsEndpoint": NotRequired[AwsDmsEndpointDetailsTypeDef],
        "AwsEventsEndpoint": NotRequired[AwsEventsEndpointDetailsUnionTypeDef],
        "AwsDmsReplicationTask": NotRequired[AwsDmsReplicationTaskDetailsTypeDef],
        "AwsDmsReplicationInstance": NotRequired[AwsDmsReplicationInstanceDetailsUnionTypeDef],
        "AwsRoute53HostedZone": NotRequired[AwsRoute53HostedZoneDetailsUnionTypeDef],
        "AwsMskCluster": NotRequired[AwsMskClusterDetailsUnionTypeDef],
        "AwsS3AccessPoint": NotRequired[AwsS3AccessPointDetailsTypeDef],
        "AwsEc2ClientVpnEndpoint": NotRequired[AwsEc2ClientVpnEndpointDetailsUnionTypeDef],
    },
)
ResourceDetailsUnionTypeDef = Union[ResourceDetailsTypeDef, ResourceDetailsOutputTypeDef]
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": NotRequired[PartitionType],
        "Region": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "DataClassification": NotRequired[DataClassificationDetailsUnionTypeDef],
        "Details": NotRequired[ResourceDetailsUnionTypeDef],
        "ApplicationName": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)
ResourceUnionTypeDef = Union[ResourceTypeDef, ResourceOutputTypeDef]
AwsSecurityFindingTypeDef = TypedDict(
    "AwsSecurityFindingTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Title": str,
        "Description": str,
        "Resources": Sequence[ResourceUnionTypeDef],
        "ProductName": NotRequired[str],
        "CompanyName": NotRequired[str],
        "Region": NotRequired[str],
        "Types": NotRequired[Sequence[str]],
        "FirstObservedAt": NotRequired[str],
        "LastObservedAt": NotRequired[str],
        "Severity": NotRequired[SeverityTypeDef],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Remediation": NotRequired[RemediationTypeDef],
        "SourceUrl": NotRequired[str],
        "ProductFields": NotRequired[Mapping[str, str]],
        "UserDefinedFields": NotRequired[Mapping[str, str]],
        "Malware": NotRequired[Sequence[MalwareTypeDef]],
        "Network": NotRequired[NetworkTypeDef],
        "NetworkPath": NotRequired[Sequence[NetworkPathComponentUnionTypeDef]],
        "Process": NotRequired[ProcessDetailsTypeDef],
        "Threats": NotRequired[Sequence[ThreatUnionTypeDef]],
        "ThreatIntelIndicators": NotRequired[Sequence[ThreatIntelIndicatorTypeDef]],
        "Compliance": NotRequired[ComplianceUnionTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "WorkflowState": NotRequired[WorkflowStateType],
        "Workflow": NotRequired[WorkflowTypeDef],
        "RecordState": NotRequired[RecordStateType],
        "RelatedFindings": NotRequired[Sequence[RelatedFindingTypeDef]],
        "Note": NotRequired[NoteTypeDef],
        "Vulnerabilities": NotRequired[Sequence[VulnerabilityUnionTypeDef]],
        "PatchSummary": NotRequired[PatchSummaryTypeDef],
        "Action": NotRequired[ActionUnionTypeDef],
        "FindingProviderFields": NotRequired[FindingProviderFieldsUnionTypeDef],
        "Sample": NotRequired[bool],
        "GeneratorDetails": NotRequired[GeneratorDetailsUnionTypeDef],
        "ProcessedAt": NotRequired[str],
        "AwsAccountName": NotRequired[str],
    },
)
AwsSecurityFindingUnionTypeDef = Union[AwsSecurityFindingTypeDef, AwsSecurityFindingOutputTypeDef]
BatchImportFindingsRequestRequestTypeDef = TypedDict(
    "BatchImportFindingsRequestRequestTypeDef",
    {
        "Findings": Sequence[AwsSecurityFindingUnionTypeDef],
    },
)
