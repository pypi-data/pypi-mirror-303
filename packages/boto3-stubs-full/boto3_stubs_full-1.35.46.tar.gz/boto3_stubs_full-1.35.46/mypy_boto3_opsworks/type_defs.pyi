"""
Type annotations for opsworks service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/type_defs/)

Usage::

    ```python
    from mypy_boto3_opsworks.type_defs import StackConfigurationManagerTypeDef

    data: StackConfigurationManagerTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AppAttributesKeysType,
    AppTypeType,
    ArchitectureType,
    AutoScalingTypeType,
    CloudWatchLogsEncodingType,
    CloudWatchLogsInitialPositionType,
    CloudWatchLogsTimeZoneType,
    DeploymentCommandNameType,
    LayerAttributesKeysType,
    LayerTypeType,
    RootDeviceTypeType,
    SourceTypeType,
    VirtualizationTypeType,
    VolumeTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "StackConfigurationManagerTypeDef",
    "DataSourceTypeDef",
    "EnvironmentVariableTypeDef",
    "SourceTypeDef",
    "SslConfigurationTypeDef",
    "AssignInstanceRequestRequestTypeDef",
    "AssignVolumeRequestRequestTypeDef",
    "AssociateElasticIpRequestRequestTypeDef",
    "AttachElasticLoadBalancerRequestRequestTypeDef",
    "AutoScalingThresholdsOutputTypeDef",
    "AutoScalingThresholdsTypeDef",
    "EbsBlockDeviceTypeDef",
    "ChefConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "CloudWatchLogsLogStreamTypeDef",
    "CommandTypeDef",
    "DeploymentCommandTypeDef",
    "RecipesTypeDef",
    "VolumeConfigurationTypeDef",
    "CreateUserProfileRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteLayerRequestRequestTypeDef",
    "DeleteStackRequestRequestTypeDef",
    "DeleteUserProfileRequestRequestTypeDef",
    "DeploymentCommandOutputTypeDef",
    "DeregisterEcsClusterRequestRequestTypeDef",
    "DeregisterElasticIpRequestRequestTypeDef",
    "DeregisterInstanceRequestRequestTypeDef",
    "DeregisterRdsDbInstanceRequestRequestTypeDef",
    "DeregisterVolumeRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeAppsRequestRequestTypeDef",
    "DescribeCommandsRequestRequestTypeDef",
    "DescribeDeploymentsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeEcsClustersRequestRequestTypeDef",
    "EcsClusterTypeDef",
    "DescribeElasticIpsRequestRequestTypeDef",
    "ElasticIpTypeDef",
    "DescribeElasticLoadBalancersRequestRequestTypeDef",
    "ElasticLoadBalancerTypeDef",
    "DescribeInstancesRequestRequestTypeDef",
    "DescribeLayersRequestRequestTypeDef",
    "DescribeLoadBasedAutoScalingRequestRequestTypeDef",
    "SelfUserProfileTypeDef",
    "DescribePermissionsRequestRequestTypeDef",
    "PermissionTypeDef",
    "DescribeRaidArraysRequestRequestTypeDef",
    "RaidArrayTypeDef",
    "DescribeRdsDbInstancesRequestRequestTypeDef",
    "RdsDbInstanceTypeDef",
    "DescribeServiceErrorsRequestRequestTypeDef",
    "ServiceErrorTypeDef",
    "DescribeStackProvisioningParametersRequestRequestTypeDef",
    "DescribeStackSummaryRequestRequestTypeDef",
    "DescribeStacksRequestRequestTypeDef",
    "DescribeTimeBasedAutoScalingRequestRequestTypeDef",
    "DescribeUserProfilesRequestRequestTypeDef",
    "UserProfileTypeDef",
    "DescribeVolumesRequestRequestTypeDef",
    "VolumeTypeDef",
    "DetachElasticLoadBalancerRequestRequestTypeDef",
    "DisassociateElasticIpRequestRequestTypeDef",
    "GetHostnameSuggestionRequestRequestTypeDef",
    "GrantAccessRequestRequestTypeDef",
    "TemporaryCredentialTypeDef",
    "InstanceIdentityTypeDef",
    "ReportedOsTypeDef",
    "InstancesCountTypeDef",
    "RecipesOutputTypeDef",
    "ShutdownEventConfigurationTypeDef",
    "ListTagsRequestRequestTypeDef",
    "OperatingSystemConfigurationManagerTypeDef",
    "RebootInstanceRequestRequestTypeDef",
    "RegisterEcsClusterRequestRequestTypeDef",
    "RegisterElasticIpRequestRequestTypeDef",
    "RegisterRdsDbInstanceRequestRequestTypeDef",
    "RegisterVolumeRequestRequestTypeDef",
    "SetPermissionRequestRequestTypeDef",
    "WeeklyAutoScalingScheduleTypeDef",
    "StartInstanceRequestRequestTypeDef",
    "StartStackRequestRequestTypeDef",
    "StopInstanceRequestRequestTypeDef",
    "StopStackRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "WeeklyAutoScalingScheduleOutputTypeDef",
    "UnassignInstanceRequestRequestTypeDef",
    "UnassignVolumeRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateElasticIpRequestRequestTypeDef",
    "UpdateInstanceRequestRequestTypeDef",
    "UpdateMyUserProfileRequestRequestTypeDef",
    "UpdateRdsDbInstanceRequestRequestTypeDef",
    "UpdateUserProfileRequestRequestTypeDef",
    "UpdateVolumeRequestRequestTypeDef",
    "AgentVersionTypeDef",
    "DescribeAgentVersionsRequestRequestTypeDef",
    "AppTypeDef",
    "CreateAppRequestRequestTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "LoadBasedAutoScalingConfigurationTypeDef",
    "SetLoadBasedAutoScalingRequestRequestTypeDef",
    "BlockDeviceMappingTypeDef",
    "CloneStackRequestRequestTypeDef",
    "CreateStackRequestRequestTypeDef",
    "CreateStackRequestServiceResourceCreateStackTypeDef",
    "StackTypeDef",
    "UpdateStackRequestRequestTypeDef",
    "CloneStackResultTypeDef",
    "CreateAppResultTypeDef",
    "CreateDeploymentResultTypeDef",
    "CreateInstanceResultTypeDef",
    "CreateLayerResultTypeDef",
    "CreateStackResultTypeDef",
    "CreateUserProfileResultTypeDef",
    "DescribeStackProvisioningParametersResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetHostnameSuggestionResultTypeDef",
    "ListTagsResultTypeDef",
    "RegisterEcsClusterResultTypeDef",
    "RegisterElasticIpResultTypeDef",
    "RegisterInstanceResultTypeDef",
    "RegisterVolumeResultTypeDef",
    "CloudWatchLogsConfigurationOutputTypeDef",
    "CloudWatchLogsConfigurationTypeDef",
    "DescribeCommandsResultTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "DeploymentTypeDef",
    "DescribeAppsRequestAppExistsWaitTypeDef",
    "DescribeDeploymentsRequestDeploymentSuccessfulWaitTypeDef",
    "DescribeInstancesRequestInstanceOnlineWaitTypeDef",
    "DescribeInstancesRequestInstanceRegisteredWaitTypeDef",
    "DescribeInstancesRequestInstanceStoppedWaitTypeDef",
    "DescribeInstancesRequestInstanceTerminatedWaitTypeDef",
    "DescribeEcsClustersRequestDescribeEcsClustersPaginateTypeDef",
    "DescribeEcsClustersResultTypeDef",
    "DescribeElasticIpsResultTypeDef",
    "DescribeElasticLoadBalancersResultTypeDef",
    "DescribeMyUserProfileResultTypeDef",
    "DescribePermissionsResultTypeDef",
    "DescribeRaidArraysResultTypeDef",
    "DescribeRdsDbInstancesResultTypeDef",
    "DescribeServiceErrorsResultTypeDef",
    "DescribeUserProfilesResultTypeDef",
    "DescribeVolumesResultTypeDef",
    "GrantAccessResultTypeDef",
    "RegisterInstanceRequestRequestTypeDef",
    "StackSummaryTypeDef",
    "LifecycleEventConfigurationTypeDef",
    "OperatingSystemTypeDef",
    "SetTimeBasedAutoScalingRequestRequestTypeDef",
    "TimeBasedAutoScalingConfigurationTypeDef",
    "DescribeAgentVersionsResultTypeDef",
    "DescribeAppsResultTypeDef",
    "DescribeLoadBasedAutoScalingResultTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "InstanceTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeDeploymentsResultTypeDef",
    "DescribeStackSummaryResultTypeDef",
    "CreateLayerRequestRequestTypeDef",
    "CreateLayerRequestStackCreateLayerTypeDef",
    "LayerTypeDef",
    "UpdateLayerRequestRequestTypeDef",
    "DescribeOperatingSystemsResponseTypeDef",
    "DescribeTimeBasedAutoScalingResultTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeLayersResultTypeDef",
)

StackConfigurationManagerTypeDef = TypedDict(
    "StackConfigurationManagerTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Type": NotRequired[str],
        "Arn": NotRequired[str],
        "DatabaseName": NotRequired[str],
    },
)
EnvironmentVariableTypeDef = TypedDict(
    "EnvironmentVariableTypeDef",
    {
        "Key": str,
        "Value": str,
        "Secure": NotRequired[bool],
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Type": NotRequired[SourceTypeType],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "SshKey": NotRequired[str],
        "Revision": NotRequired[str],
    },
)
SslConfigurationTypeDef = TypedDict(
    "SslConfigurationTypeDef",
    {
        "Certificate": str,
        "PrivateKey": str,
        "Chain": NotRequired[str],
    },
)
AssignInstanceRequestRequestTypeDef = TypedDict(
    "AssignInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LayerIds": Sequence[str],
    },
)
AssignVolumeRequestRequestTypeDef = TypedDict(
    "AssignVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "InstanceId": NotRequired[str],
    },
)
AssociateElasticIpRequestRequestTypeDef = TypedDict(
    "AssociateElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
        "InstanceId": NotRequired[str],
    },
)
AttachElasticLoadBalancerRequestRequestTypeDef = TypedDict(
    "AttachElasticLoadBalancerRequestRequestTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "LayerId": str,
    },
)
AutoScalingThresholdsOutputTypeDef = TypedDict(
    "AutoScalingThresholdsOutputTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "ThresholdsWaitTime": NotRequired[int],
        "IgnoreMetricsTime": NotRequired[int],
        "CpuThreshold": NotRequired[float],
        "MemoryThreshold": NotRequired[float],
        "LoadThreshold": NotRequired[float],
        "Alarms": NotRequired[List[str]],
    },
)
AutoScalingThresholdsTypeDef = TypedDict(
    "AutoScalingThresholdsTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "ThresholdsWaitTime": NotRequired[int],
        "IgnoreMetricsTime": NotRequired[int],
        "CpuThreshold": NotRequired[float],
        "MemoryThreshold": NotRequired[float],
        "LoadThreshold": NotRequired[float],
        "Alarms": NotRequired[Sequence[str]],
    },
)
EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "Iops": NotRequired[int],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "DeleteOnTermination": NotRequired[bool],
    },
)
ChefConfigurationTypeDef = TypedDict(
    "ChefConfigurationTypeDef",
    {
        "ManageBerkshelf": NotRequired[bool],
        "BerkshelfVersion": NotRequired[str],
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
CloudWatchLogsLogStreamTypeDef = TypedDict(
    "CloudWatchLogsLogStreamTypeDef",
    {
        "LogGroupName": NotRequired[str],
        "DatetimeFormat": NotRequired[str],
        "TimeZone": NotRequired[CloudWatchLogsTimeZoneType],
        "File": NotRequired[str],
        "FileFingerprintLines": NotRequired[str],
        "MultiLineStartPattern": NotRequired[str],
        "InitialPosition": NotRequired[CloudWatchLogsInitialPositionType],
        "Encoding": NotRequired[CloudWatchLogsEncodingType],
        "BufferDuration": NotRequired[int],
        "BatchCount": NotRequired[int],
        "BatchSize": NotRequired[int],
    },
)
CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "AcknowledgedAt": NotRequired[str],
        "CompletedAt": NotRequired[str],
        "Status": NotRequired[str],
        "ExitCode": NotRequired[int],
        "LogUrl": NotRequired[str],
        "Type": NotRequired[str],
    },
)
DeploymentCommandTypeDef = TypedDict(
    "DeploymentCommandTypeDef",
    {
        "Name": DeploymentCommandNameType,
        "Args": NotRequired[Mapping[str, Sequence[str]]],
    },
)
RecipesTypeDef = TypedDict(
    "RecipesTypeDef",
    {
        "Setup": NotRequired[Sequence[str]],
        "Configure": NotRequired[Sequence[str]],
        "Deploy": NotRequired[Sequence[str]],
        "Undeploy": NotRequired[Sequence[str]],
        "Shutdown": NotRequired[Sequence[str]],
    },
)
VolumeConfigurationTypeDef = TypedDict(
    "VolumeConfigurationTypeDef",
    {
        "MountPoint": str,
        "NumberOfDisks": int,
        "Size": int,
        "RaidLevel": NotRequired[int],
        "VolumeType": NotRequired[str],
        "Iops": NotRequired[int],
        "Encrypted": NotRequired[bool],
    },
)
CreateUserProfileRequestRequestTypeDef = TypedDict(
    "CreateUserProfileRequestRequestTypeDef",
    {
        "IamUserArn": str,
        "SshUsername": NotRequired[str],
        "SshPublicKey": NotRequired[str],
        "AllowSelfManagement": NotRequired[bool],
    },
)
DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "AppId": str,
    },
)
DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DeleteElasticIp": NotRequired[bool],
        "DeleteVolumes": NotRequired[bool],
    },
)
DeleteLayerRequestRequestTypeDef = TypedDict(
    "DeleteLayerRequestRequestTypeDef",
    {
        "LayerId": str,
    },
)
DeleteStackRequestRequestTypeDef = TypedDict(
    "DeleteStackRequestRequestTypeDef",
    {
        "StackId": str,
    },
)
DeleteUserProfileRequestRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestRequestTypeDef",
    {
        "IamUserArn": str,
    },
)
DeploymentCommandOutputTypeDef = TypedDict(
    "DeploymentCommandOutputTypeDef",
    {
        "Name": DeploymentCommandNameType,
        "Args": NotRequired[Dict[str, List[str]]],
    },
)
DeregisterEcsClusterRequestRequestTypeDef = TypedDict(
    "DeregisterEcsClusterRequestRequestTypeDef",
    {
        "EcsClusterArn": str,
    },
)
DeregisterElasticIpRequestRequestTypeDef = TypedDict(
    "DeregisterElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
    },
)
DeregisterInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
DeregisterRdsDbInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterRdsDbInstanceRequestRequestTypeDef",
    {
        "RdsDbInstanceArn": str,
    },
)
DeregisterVolumeRequestRequestTypeDef = TypedDict(
    "DeregisterVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeAppsRequestRequestTypeDef = TypedDict(
    "DescribeAppsRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "AppIds": NotRequired[Sequence[str]],
    },
)
DescribeCommandsRequestRequestTypeDef = TypedDict(
    "DescribeCommandsRequestRequestTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "CommandIds": NotRequired[Sequence[str]],
    },
)
DescribeDeploymentsRequestRequestTypeDef = TypedDict(
    "DescribeDeploymentsRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "AppId": NotRequired[str],
        "DeploymentIds": NotRequired[Sequence[str]],
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
DescribeEcsClustersRequestRequestTypeDef = TypedDict(
    "DescribeEcsClustersRequestRequestTypeDef",
    {
        "EcsClusterArns": NotRequired[Sequence[str]],
        "StackId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
EcsClusterTypeDef = TypedDict(
    "EcsClusterTypeDef",
    {
        "EcsClusterArn": NotRequired[str],
        "EcsClusterName": NotRequired[str],
        "StackId": NotRequired[str],
        "RegisteredAt": NotRequired[str],
    },
)
DescribeElasticIpsRequestRequestTypeDef = TypedDict(
    "DescribeElasticIpsRequestRequestTypeDef",
    {
        "InstanceId": NotRequired[str],
        "StackId": NotRequired[str],
        "Ips": NotRequired[Sequence[str]],
    },
)
ElasticIpTypeDef = TypedDict(
    "ElasticIpTypeDef",
    {
        "Ip": NotRequired[str],
        "Name": NotRequired[str],
        "Domain": NotRequired[str],
        "Region": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)
DescribeElasticLoadBalancersRequestRequestTypeDef = TypedDict(
    "DescribeElasticLoadBalancersRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerIds": NotRequired[Sequence[str]],
    },
)
ElasticLoadBalancerTypeDef = TypedDict(
    "ElasticLoadBalancerTypeDef",
    {
        "ElasticLoadBalancerName": NotRequired[str],
        "Region": NotRequired[str],
        "DnsName": NotRequired[str],
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "Ec2InstanceIds": NotRequired[List[str]],
    },
)
DescribeInstancesRequestRequestTypeDef = TypedDict(
    "DescribeInstancesRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
    },
)
DescribeLayersRequestRequestTypeDef = TypedDict(
    "DescribeLayersRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerIds": NotRequired[Sequence[str]],
    },
)
DescribeLoadBasedAutoScalingRequestRequestTypeDef = TypedDict(
    "DescribeLoadBasedAutoScalingRequestRequestTypeDef",
    {
        "LayerIds": Sequence[str],
    },
)
SelfUserProfileTypeDef = TypedDict(
    "SelfUserProfileTypeDef",
    {
        "IamUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "SshUsername": NotRequired[str],
        "SshPublicKey": NotRequired[str],
    },
)
DescribePermissionsRequestRequestTypeDef = TypedDict(
    "DescribePermissionsRequestRequestTypeDef",
    {
        "IamUserArn": NotRequired[str],
        "StackId": NotRequired[str],
    },
)
PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "StackId": NotRequired[str],
        "IamUserArn": NotRequired[str],
        "AllowSsh": NotRequired[bool],
        "AllowSudo": NotRequired[bool],
        "Level": NotRequired[str],
    },
)
DescribeRaidArraysRequestRequestTypeDef = TypedDict(
    "DescribeRaidArraysRequestRequestTypeDef",
    {
        "InstanceId": NotRequired[str],
        "StackId": NotRequired[str],
        "RaidArrayIds": NotRequired[Sequence[str]],
    },
)
RaidArrayTypeDef = TypedDict(
    "RaidArrayTypeDef",
    {
        "RaidArrayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Name": NotRequired[str],
        "RaidLevel": NotRequired[int],
        "NumberOfDisks": NotRequired[int],
        "Size": NotRequired[int],
        "Device": NotRequired[str],
        "MountPoint": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "StackId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "Iops": NotRequired[int],
    },
)
DescribeRdsDbInstancesRequestRequestTypeDef = TypedDict(
    "DescribeRdsDbInstancesRequestRequestTypeDef",
    {
        "StackId": str,
        "RdsDbInstanceArns": NotRequired[Sequence[str]],
    },
)
RdsDbInstanceTypeDef = TypedDict(
    "RdsDbInstanceTypeDef",
    {
        "RdsDbInstanceArn": NotRequired[str],
        "DbInstanceIdentifier": NotRequired[str],
        "DbUser": NotRequired[str],
        "DbPassword": NotRequired[str],
        "Region": NotRequired[str],
        "Address": NotRequired[str],
        "Engine": NotRequired[str],
        "StackId": NotRequired[str],
        "MissingOnRds": NotRequired[bool],
    },
)
DescribeServiceErrorsRequestRequestTypeDef = TypedDict(
    "DescribeServiceErrorsRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "ServiceErrorIds": NotRequired[Sequence[str]],
    },
)
ServiceErrorTypeDef = TypedDict(
    "ServiceErrorTypeDef",
    {
        "ServiceErrorId": NotRequired[str],
        "StackId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Type": NotRequired[str],
        "Message": NotRequired[str],
        "CreatedAt": NotRequired[str],
    },
)
DescribeStackProvisioningParametersRequestRequestTypeDef = TypedDict(
    "DescribeStackProvisioningParametersRequestRequestTypeDef",
    {
        "StackId": str,
    },
)
DescribeStackSummaryRequestRequestTypeDef = TypedDict(
    "DescribeStackSummaryRequestRequestTypeDef",
    {
        "StackId": str,
    },
)
DescribeStacksRequestRequestTypeDef = TypedDict(
    "DescribeStacksRequestRequestTypeDef",
    {
        "StackIds": NotRequired[Sequence[str]],
    },
)
DescribeTimeBasedAutoScalingRequestRequestTypeDef = TypedDict(
    "DescribeTimeBasedAutoScalingRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
    },
)
DescribeUserProfilesRequestRequestTypeDef = TypedDict(
    "DescribeUserProfilesRequestRequestTypeDef",
    {
        "IamUserArns": NotRequired[Sequence[str]],
    },
)
UserProfileTypeDef = TypedDict(
    "UserProfileTypeDef",
    {
        "IamUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "SshUsername": NotRequired[str],
        "SshPublicKey": NotRequired[str],
        "AllowSelfManagement": NotRequired[bool],
    },
)
DescribeVolumesRequestRequestTypeDef = TypedDict(
    "DescribeVolumesRequestRequestTypeDef",
    {
        "InstanceId": NotRequired[str],
        "StackId": NotRequired[str],
        "RaidArrayId": NotRequired[str],
        "VolumeIds": NotRequired[Sequence[str]],
    },
)
VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "VolumeId": NotRequired[str],
        "Ec2VolumeId": NotRequired[str],
        "Name": NotRequired[str],
        "RaidArrayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Status": NotRequired[str],
        "Size": NotRequired[int],
        "Device": NotRequired[str],
        "MountPoint": NotRequired[str],
        "Region": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "VolumeType": NotRequired[str],
        "Iops": NotRequired[int],
        "Encrypted": NotRequired[bool],
    },
)
DetachElasticLoadBalancerRequestRequestTypeDef = TypedDict(
    "DetachElasticLoadBalancerRequestRequestTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "LayerId": str,
    },
)
DisassociateElasticIpRequestRequestTypeDef = TypedDict(
    "DisassociateElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
    },
)
GetHostnameSuggestionRequestRequestTypeDef = TypedDict(
    "GetHostnameSuggestionRequestRequestTypeDef",
    {
        "LayerId": str,
    },
)
GrantAccessRequestRequestTypeDef = TypedDict(
    "GrantAccessRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ValidForInMinutes": NotRequired[int],
    },
)
TemporaryCredentialTypeDef = TypedDict(
    "TemporaryCredentialTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ValidForInMinutes": NotRequired[int],
        "InstanceId": NotRequired[str],
    },
)
InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef",
    {
        "Document": NotRequired[str],
        "Signature": NotRequired[str],
    },
)
ReportedOsTypeDef = TypedDict(
    "ReportedOsTypeDef",
    {
        "Family": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
InstancesCountTypeDef = TypedDict(
    "InstancesCountTypeDef",
    {
        "Assigning": NotRequired[int],
        "Booting": NotRequired[int],
        "ConnectionLost": NotRequired[int],
        "Deregistering": NotRequired[int],
        "Online": NotRequired[int],
        "Pending": NotRequired[int],
        "Rebooting": NotRequired[int],
        "Registered": NotRequired[int],
        "Registering": NotRequired[int],
        "Requested": NotRequired[int],
        "RunningSetup": NotRequired[int],
        "SetupFailed": NotRequired[int],
        "ShuttingDown": NotRequired[int],
        "StartFailed": NotRequired[int],
        "StopFailed": NotRequired[int],
        "Stopped": NotRequired[int],
        "Stopping": NotRequired[int],
        "Terminated": NotRequired[int],
        "Terminating": NotRequired[int],
        "Unassigning": NotRequired[int],
    },
)
RecipesOutputTypeDef = TypedDict(
    "RecipesOutputTypeDef",
    {
        "Setup": NotRequired[List[str]],
        "Configure": NotRequired[List[str]],
        "Deploy": NotRequired[List[str]],
        "Undeploy": NotRequired[List[str]],
        "Shutdown": NotRequired[List[str]],
    },
)
ShutdownEventConfigurationTypeDef = TypedDict(
    "ShutdownEventConfigurationTypeDef",
    {
        "ExecutionTimeout": NotRequired[int],
        "DelayUntilElbConnectionsDrained": NotRequired[bool],
    },
)
ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
OperatingSystemConfigurationManagerTypeDef = TypedDict(
    "OperatingSystemConfigurationManagerTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
RebootInstanceRequestRequestTypeDef = TypedDict(
    "RebootInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
RegisterEcsClusterRequestRequestTypeDef = TypedDict(
    "RegisterEcsClusterRequestRequestTypeDef",
    {
        "EcsClusterArn": str,
        "StackId": str,
    },
)
RegisterElasticIpRequestRequestTypeDef = TypedDict(
    "RegisterElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
        "StackId": str,
    },
)
RegisterRdsDbInstanceRequestRequestTypeDef = TypedDict(
    "RegisterRdsDbInstanceRequestRequestTypeDef",
    {
        "StackId": str,
        "RdsDbInstanceArn": str,
        "DbUser": str,
        "DbPassword": str,
    },
)
RegisterVolumeRequestRequestTypeDef = TypedDict(
    "RegisterVolumeRequestRequestTypeDef",
    {
        "StackId": str,
        "Ec2VolumeId": NotRequired[str],
    },
)
SetPermissionRequestRequestTypeDef = TypedDict(
    "SetPermissionRequestRequestTypeDef",
    {
        "StackId": str,
        "IamUserArn": str,
        "AllowSsh": NotRequired[bool],
        "AllowSudo": NotRequired[bool],
        "Level": NotRequired[str],
    },
)
WeeklyAutoScalingScheduleTypeDef = TypedDict(
    "WeeklyAutoScalingScheduleTypeDef",
    {
        "Monday": NotRequired[Mapping[str, str]],
        "Tuesday": NotRequired[Mapping[str, str]],
        "Wednesday": NotRequired[Mapping[str, str]],
        "Thursday": NotRequired[Mapping[str, str]],
        "Friday": NotRequired[Mapping[str, str]],
        "Saturday": NotRequired[Mapping[str, str]],
        "Sunday": NotRequired[Mapping[str, str]],
    },
)
StartInstanceRequestRequestTypeDef = TypedDict(
    "StartInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
StartStackRequestRequestTypeDef = TypedDict(
    "StartStackRequestRequestTypeDef",
    {
        "StackId": str,
    },
)
StopInstanceRequestRequestTypeDef = TypedDict(
    "StopInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Force": NotRequired[bool],
    },
)
StopStackRequestRequestTypeDef = TypedDict(
    "StopStackRequestRequestTypeDef",
    {
        "StackId": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
WeeklyAutoScalingScheduleOutputTypeDef = TypedDict(
    "WeeklyAutoScalingScheduleOutputTypeDef",
    {
        "Monday": NotRequired[Dict[str, str]],
        "Tuesday": NotRequired[Dict[str, str]],
        "Wednesday": NotRequired[Dict[str, str]],
        "Thursday": NotRequired[Dict[str, str]],
        "Friday": NotRequired[Dict[str, str]],
        "Saturday": NotRequired[Dict[str, str]],
        "Sunday": NotRequired[Dict[str, str]],
    },
)
UnassignInstanceRequestRequestTypeDef = TypedDict(
    "UnassignInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
UnassignVolumeRequestRequestTypeDef = TypedDict(
    "UnassignVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateElasticIpRequestRequestTypeDef = TypedDict(
    "UpdateElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
        "Name": NotRequired[str],
    },
)
UpdateInstanceRequestRequestTypeDef = TypedDict(
    "UpdateInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LayerIds": NotRequired[Sequence[str]],
        "InstanceType": NotRequired[str],
        "AutoScalingType": NotRequired[AutoScalingTypeType],
        "Hostname": NotRequired[str],
        "Os": NotRequired[str],
        "AmiId": NotRequired[str],
        "SshKeyName": NotRequired[str],
        "Architecture": NotRequired[ArchitectureType],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "AgentVersion": NotRequired[str],
    },
)
UpdateMyUserProfileRequestRequestTypeDef = TypedDict(
    "UpdateMyUserProfileRequestRequestTypeDef",
    {
        "SshPublicKey": NotRequired[str],
    },
)
UpdateRdsDbInstanceRequestRequestTypeDef = TypedDict(
    "UpdateRdsDbInstanceRequestRequestTypeDef",
    {
        "RdsDbInstanceArn": str,
        "DbUser": NotRequired[str],
        "DbPassword": NotRequired[str],
    },
)
UpdateUserProfileRequestRequestTypeDef = TypedDict(
    "UpdateUserProfileRequestRequestTypeDef",
    {
        "IamUserArn": str,
        "SshUsername": NotRequired[str],
        "SshPublicKey": NotRequired[str],
        "AllowSelfManagement": NotRequired[bool],
    },
)
UpdateVolumeRequestRequestTypeDef = TypedDict(
    "UpdateVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "Name": NotRequired[str],
        "MountPoint": NotRequired[str],
    },
)
AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {
        "Version": NotRequired[str],
        "ConfigurationManager": NotRequired[StackConfigurationManagerTypeDef],
    },
)
DescribeAgentVersionsRequestRequestTypeDef = TypedDict(
    "DescribeAgentVersionsRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "ConfigurationManager": NotRequired[StackConfigurationManagerTypeDef],
    },
)
AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppId": NotRequired[str],
        "StackId": NotRequired[str],
        "Shortname": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[List[DataSourceTypeDef]],
        "Type": NotRequired[AppTypeType],
        "AppSource": NotRequired[SourceTypeDef],
        "Domains": NotRequired[List[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired[SslConfigurationTypeDef],
        "Attributes": NotRequired[Dict[AppAttributesKeysType, str]],
        "CreatedAt": NotRequired[str],
        "Environment": NotRequired[List[EnvironmentVariableTypeDef]],
    },
)
CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Type": AppTypeType,
        "Shortname": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[Sequence[DataSourceTypeDef]],
        "AppSource": NotRequired[SourceTypeDef],
        "Domains": NotRequired[Sequence[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired[SslConfigurationTypeDef],
        "Attributes": NotRequired[Mapping[AppAttributesKeysType, str]],
        "Environment": NotRequired[Sequence[EnvironmentVariableTypeDef]],
    },
)
UpdateAppRequestRequestTypeDef = TypedDict(
    "UpdateAppRequestRequestTypeDef",
    {
        "AppId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[Sequence[DataSourceTypeDef]],
        "Type": NotRequired[AppTypeType],
        "AppSource": NotRequired[SourceTypeDef],
        "Domains": NotRequired[Sequence[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired[SslConfigurationTypeDef],
        "Attributes": NotRequired[Mapping[AppAttributesKeysType, str]],
        "Environment": NotRequired[Sequence[EnvironmentVariableTypeDef]],
    },
)
LoadBasedAutoScalingConfigurationTypeDef = TypedDict(
    "LoadBasedAutoScalingConfigurationTypeDef",
    {
        "LayerId": NotRequired[str],
        "Enable": NotRequired[bool],
        "UpScaling": NotRequired[AutoScalingThresholdsOutputTypeDef],
        "DownScaling": NotRequired[AutoScalingThresholdsOutputTypeDef],
    },
)
SetLoadBasedAutoScalingRequestRequestTypeDef = TypedDict(
    "SetLoadBasedAutoScalingRequestRequestTypeDef",
    {
        "LayerId": str,
        "Enable": NotRequired[bool],
        "UpScaling": NotRequired[AutoScalingThresholdsTypeDef],
        "DownScaling": NotRequired[AutoScalingThresholdsTypeDef],
    },
)
BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "NoDevice": NotRequired[str],
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired[EbsBlockDeviceTypeDef],
    },
)
CloneStackRequestRequestTypeDef = TypedDict(
    "CloneStackRequestRequestTypeDef",
    {
        "SourceStackId": str,
        "ServiceRoleArn": str,
        "Name": NotRequired[str],
        "Region": NotRequired[str],
        "VpcId": NotRequired[str],
        "Attributes": NotRequired[Mapping[Literal["Color"], str]],
        "DefaultInstanceProfileArn": NotRequired[str],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired[StackConfigurationManagerTypeDef],
        "ChefConfiguration": NotRequired[ChefConfigurationTypeDef],
        "UseCustomCookbooks": NotRequired[bool],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "CustomCookbooksSource": NotRequired[SourceTypeDef],
        "DefaultSshKeyName": NotRequired[str],
        "ClonePermissions": NotRequired[bool],
        "CloneAppIds": NotRequired[Sequence[str]],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "AgentVersion": NotRequired[str],
    },
)
CreateStackRequestRequestTypeDef = TypedDict(
    "CreateStackRequestRequestTypeDef",
    {
        "Name": str,
        "Region": str,
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "VpcId": NotRequired[str],
        "Attributes": NotRequired[Mapping[Literal["Color"], str]],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired[StackConfigurationManagerTypeDef],
        "ChefConfiguration": NotRequired[ChefConfigurationTypeDef],
        "UseCustomCookbooks": NotRequired[bool],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "CustomCookbooksSource": NotRequired[SourceTypeDef],
        "DefaultSshKeyName": NotRequired[str],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "AgentVersion": NotRequired[str],
    },
)
CreateStackRequestServiceResourceCreateStackTypeDef = TypedDict(
    "CreateStackRequestServiceResourceCreateStackTypeDef",
    {
        "Name": str,
        "Region": str,
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "VpcId": NotRequired[str],
        "Attributes": NotRequired[Mapping[Literal["Color"], str]],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired[StackConfigurationManagerTypeDef],
        "ChefConfiguration": NotRequired[ChefConfigurationTypeDef],
        "UseCustomCookbooks": NotRequired[bool],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "CustomCookbooksSource": NotRequired[SourceTypeDef],
        "DefaultSshKeyName": NotRequired[str],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "AgentVersion": NotRequired[str],
    },
)
StackTypeDef = TypedDict(
    "StackTypeDef",
    {
        "StackId": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Region": NotRequired[str],
        "VpcId": NotRequired[str],
        "Attributes": NotRequired[Dict[Literal["Color"], str]],
        "ServiceRoleArn": NotRequired[str],
        "DefaultInstanceProfileArn": NotRequired[str],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired[StackConfigurationManagerTypeDef],
        "ChefConfiguration": NotRequired[ChefConfigurationTypeDef],
        "UseCustomCookbooks": NotRequired[bool],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "CustomCookbooksSource": NotRequired[SourceTypeDef],
        "DefaultSshKeyName": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "AgentVersion": NotRequired[str],
    },
)
UpdateStackRequestRequestTypeDef = TypedDict(
    "UpdateStackRequestRequestTypeDef",
    {
        "StackId": str,
        "Name": NotRequired[str],
        "Attributes": NotRequired[Mapping[Literal["Color"], str]],
        "ServiceRoleArn": NotRequired[str],
        "DefaultInstanceProfileArn": NotRequired[str],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired[StackConfigurationManagerTypeDef],
        "ChefConfiguration": NotRequired[ChefConfigurationTypeDef],
        "UseCustomCookbooks": NotRequired[bool],
        "CustomCookbooksSource": NotRequired[SourceTypeDef],
        "DefaultSshKeyName": NotRequired[str],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "AgentVersion": NotRequired[str],
    },
)
CloneStackResultTypeDef = TypedDict(
    "CloneStackResultTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppResultTypeDef = TypedDict(
    "CreateAppResultTypeDef",
    {
        "AppId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentResultTypeDef = TypedDict(
    "CreateDeploymentResultTypeDef",
    {
        "DeploymentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceResultTypeDef = TypedDict(
    "CreateInstanceResultTypeDef",
    {
        "InstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLayerResultTypeDef = TypedDict(
    "CreateLayerResultTypeDef",
    {
        "LayerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStackResultTypeDef = TypedDict(
    "CreateStackResultTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserProfileResultTypeDef = TypedDict(
    "CreateUserProfileResultTypeDef",
    {
        "IamUserArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStackProvisioningParametersResultTypeDef = TypedDict(
    "DescribeStackProvisioningParametersResultTypeDef",
    {
        "AgentInstallerUrl": str,
        "Parameters": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHostnameSuggestionResultTypeDef = TypedDict(
    "GetHostnameSuggestionResultTypeDef",
    {
        "LayerId": str,
        "Hostname": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsResultTypeDef = TypedDict(
    "ListTagsResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RegisterEcsClusterResultTypeDef = TypedDict(
    "RegisterEcsClusterResultTypeDef",
    {
        "EcsClusterArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterElasticIpResultTypeDef = TypedDict(
    "RegisterElasticIpResultTypeDef",
    {
        "ElasticIp": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterInstanceResultTypeDef = TypedDict(
    "RegisterInstanceResultTypeDef",
    {
        "InstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterVolumeResultTypeDef = TypedDict(
    "RegisterVolumeResultTypeDef",
    {
        "VolumeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CloudWatchLogsConfigurationOutputTypeDef = TypedDict(
    "CloudWatchLogsConfigurationOutputTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LogStreams": NotRequired[List[CloudWatchLogsLogStreamTypeDef]],
    },
)
CloudWatchLogsConfigurationTypeDef = TypedDict(
    "CloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LogStreams": NotRequired[Sequence[CloudWatchLogsLogStreamTypeDef]],
    },
)
DescribeCommandsResultTypeDef = TypedDict(
    "DescribeCommandsResultTypeDef",
    {
        "Commands": List[CommandTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "StackId": str,
        "Command": DeploymentCommandTypeDef,
        "AppId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "LayerIds": NotRequired[Sequence[str]],
        "Comment": NotRequired[str],
        "CustomJson": NotRequired[str],
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "StackId": NotRequired[str],
        "AppId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "CompletedAt": NotRequired[str],
        "Duration": NotRequired[int],
        "IamUserArn": NotRequired[str],
        "Comment": NotRequired[str],
        "Command": NotRequired[DeploymentCommandOutputTypeDef],
        "Status": NotRequired[str],
        "CustomJson": NotRequired[str],
        "InstanceIds": NotRequired[List[str]],
    },
)
DescribeAppsRequestAppExistsWaitTypeDef = TypedDict(
    "DescribeAppsRequestAppExistsWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "AppIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDeploymentsRequestDeploymentSuccessfulWaitTypeDef = TypedDict(
    "DescribeDeploymentsRequestDeploymentSuccessfulWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "AppId": NotRequired[str],
        "DeploymentIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstancesRequestInstanceOnlineWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceOnlineWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstancesRequestInstanceRegisteredWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceRegisteredWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstancesRequestInstanceStoppedWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceStoppedWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeInstancesRequestInstanceTerminatedWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceTerminatedWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEcsClustersRequestDescribeEcsClustersPaginateTypeDef = TypedDict(
    "DescribeEcsClustersRequestDescribeEcsClustersPaginateTypeDef",
    {
        "EcsClusterArns": NotRequired[Sequence[str]],
        "StackId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEcsClustersResultTypeDef = TypedDict(
    "DescribeEcsClustersResultTypeDef",
    {
        "EcsClusters": List[EcsClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeElasticIpsResultTypeDef = TypedDict(
    "DescribeElasticIpsResultTypeDef",
    {
        "ElasticIps": List[ElasticIpTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeElasticLoadBalancersResultTypeDef = TypedDict(
    "DescribeElasticLoadBalancersResultTypeDef",
    {
        "ElasticLoadBalancers": List[ElasticLoadBalancerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMyUserProfileResultTypeDef = TypedDict(
    "DescribeMyUserProfileResultTypeDef",
    {
        "UserProfile": SelfUserProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePermissionsResultTypeDef = TypedDict(
    "DescribePermissionsResultTypeDef",
    {
        "Permissions": List[PermissionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRaidArraysResultTypeDef = TypedDict(
    "DescribeRaidArraysResultTypeDef",
    {
        "RaidArrays": List[RaidArrayTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRdsDbInstancesResultTypeDef = TypedDict(
    "DescribeRdsDbInstancesResultTypeDef",
    {
        "RdsDbInstances": List[RdsDbInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeServiceErrorsResultTypeDef = TypedDict(
    "DescribeServiceErrorsResultTypeDef",
    {
        "ServiceErrors": List[ServiceErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUserProfilesResultTypeDef = TypedDict(
    "DescribeUserProfilesResultTypeDef",
    {
        "UserProfiles": List[UserProfileTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVolumesResultTypeDef = TypedDict(
    "DescribeVolumesResultTypeDef",
    {
        "Volumes": List[VolumeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GrantAccessResultTypeDef = TypedDict(
    "GrantAccessResultTypeDef",
    {
        "TemporaryCredential": TemporaryCredentialTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterInstanceRequestRequestTypeDef = TypedDict(
    "RegisterInstanceRequestRequestTypeDef",
    {
        "StackId": str,
        "Hostname": NotRequired[str],
        "PublicIp": NotRequired[str],
        "PrivateIp": NotRequired[str],
        "RsaPublicKey": NotRequired[str],
        "RsaPublicKeyFingerprint": NotRequired[str],
        "InstanceIdentity": NotRequired[InstanceIdentityTypeDef],
    },
)
StackSummaryTypeDef = TypedDict(
    "StackSummaryTypeDef",
    {
        "StackId": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "LayersCount": NotRequired[int],
        "AppsCount": NotRequired[int],
        "InstancesCount": NotRequired[InstancesCountTypeDef],
    },
)
LifecycleEventConfigurationTypeDef = TypedDict(
    "LifecycleEventConfigurationTypeDef",
    {
        "Shutdown": NotRequired[ShutdownEventConfigurationTypeDef],
    },
)
OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[str],
        "ConfigurationManagers": NotRequired[List[OperatingSystemConfigurationManagerTypeDef]],
        "ReportedName": NotRequired[str],
        "ReportedVersion": NotRequired[str],
        "Supported": NotRequired[bool],
    },
)
SetTimeBasedAutoScalingRequestRequestTypeDef = TypedDict(
    "SetTimeBasedAutoScalingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AutoScalingSchedule": NotRequired[WeeklyAutoScalingScheduleTypeDef],
    },
)
TimeBasedAutoScalingConfigurationTypeDef = TypedDict(
    "TimeBasedAutoScalingConfigurationTypeDef",
    {
        "InstanceId": NotRequired[str],
        "AutoScalingSchedule": NotRequired[WeeklyAutoScalingScheduleOutputTypeDef],
    },
)
DescribeAgentVersionsResultTypeDef = TypedDict(
    "DescribeAgentVersionsResultTypeDef",
    {
        "AgentVersions": List[AgentVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAppsResultTypeDef = TypedDict(
    "DescribeAppsResultTypeDef",
    {
        "Apps": List[AppTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLoadBasedAutoScalingResultTypeDef = TypedDict(
    "DescribeLoadBasedAutoScalingResultTypeDef",
    {
        "LoadBasedAutoScalingConfigurations": List[LoadBasedAutoScalingConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceRequestRequestTypeDef = TypedDict(
    "CreateInstanceRequestRequestTypeDef",
    {
        "StackId": str,
        "LayerIds": Sequence[str],
        "InstanceType": str,
        "AutoScalingType": NotRequired[AutoScalingTypeType],
        "Hostname": NotRequired[str],
        "Os": NotRequired[str],
        "AmiId": NotRequired[str],
        "SshKeyName": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "VirtualizationType": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Architecture": NotRequired[ArchitectureType],
        "RootDeviceType": NotRequired[RootDeviceTypeType],
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "AgentVersion": NotRequired[str],
        "Tenancy": NotRequired[str],
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AgentVersion": NotRequired[str],
        "AmiId": NotRequired[str],
        "Architecture": NotRequired[ArchitectureType],
        "Arn": NotRequired[str],
        "AutoScalingType": NotRequired[AutoScalingTypeType],
        "AvailabilityZone": NotRequired[str],
        "BlockDeviceMappings": NotRequired[List[BlockDeviceMappingTypeDef]],
        "CreatedAt": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "Ec2InstanceId": NotRequired[str],
        "EcsClusterArn": NotRequired[str],
        "EcsContainerInstanceArn": NotRequired[str],
        "ElasticIp": NotRequired[str],
        "Hostname": NotRequired[str],
        "InfrastructureClass": NotRequired[str],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "InstanceProfileArn": NotRequired[str],
        "InstanceType": NotRequired[str],
        "LastServiceErrorId": NotRequired[str],
        "LayerIds": NotRequired[List[str]],
        "Os": NotRequired[str],
        "Platform": NotRequired[str],
        "PrivateDns": NotRequired[str],
        "PrivateIp": NotRequired[str],
        "PublicDns": NotRequired[str],
        "PublicIp": NotRequired[str],
        "RegisteredBy": NotRequired[str],
        "ReportedAgentVersion": NotRequired[str],
        "ReportedOs": NotRequired[ReportedOsTypeDef],
        "RootDeviceType": NotRequired[RootDeviceTypeType],
        "RootDeviceVolumeId": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "SshHostDsaKeyFingerprint": NotRequired[str],
        "SshHostRsaKeyFingerprint": NotRequired[str],
        "SshKeyName": NotRequired[str],
        "StackId": NotRequired[str],
        "Status": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Tenancy": NotRequired[str],
        "VirtualizationType": NotRequired[VirtualizationTypeType],
    },
)
DescribeStacksResultTypeDef = TypedDict(
    "DescribeStacksResultTypeDef",
    {
        "Stacks": List[StackTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDeploymentsResultTypeDef = TypedDict(
    "DescribeDeploymentsResultTypeDef",
    {
        "Deployments": List[DeploymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStackSummaryResultTypeDef = TypedDict(
    "DescribeStackSummaryResultTypeDef",
    {
        "StackSummary": StackSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLayerRequestRequestTypeDef = TypedDict(
    "CreateLayerRequestRequestTypeDef",
    {
        "StackId": str,
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
        "Attributes": NotRequired[Mapping[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired[CloudWatchLogsConfigurationTypeDef],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[Sequence[str]],
        "Packages": NotRequired[Sequence[str]],
        "VolumeConfigurations": NotRequired[Sequence[VolumeConfigurationTypeDef]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "CustomRecipes": NotRequired[RecipesTypeDef],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired[LifecycleEventConfigurationTypeDef],
    },
)
CreateLayerRequestStackCreateLayerTypeDef = TypedDict(
    "CreateLayerRequestStackCreateLayerTypeDef",
    {
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
        "Attributes": NotRequired[Mapping[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired[CloudWatchLogsConfigurationTypeDef],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[Sequence[str]],
        "Packages": NotRequired[Sequence[str]],
        "VolumeConfigurations": NotRequired[Sequence[VolumeConfigurationTypeDef]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "CustomRecipes": NotRequired[RecipesTypeDef],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired[LifecycleEventConfigurationTypeDef],
    },
)
LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": NotRequired[str],
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "Type": NotRequired[LayerTypeType],
        "Name": NotRequired[str],
        "Shortname": NotRequired[str],
        "Attributes": NotRequired[Dict[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired[CloudWatchLogsConfigurationOutputTypeDef],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[List[str]],
        "DefaultSecurityGroupNames": NotRequired[List[str]],
        "Packages": NotRequired[List[str]],
        "VolumeConfigurations": NotRequired[List[VolumeConfigurationTypeDef]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "DefaultRecipes": NotRequired[RecipesOutputTypeDef],
        "CustomRecipes": NotRequired[RecipesOutputTypeDef],
        "CreatedAt": NotRequired[str],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired[LifecycleEventConfigurationTypeDef],
    },
)
UpdateLayerRequestRequestTypeDef = TypedDict(
    "UpdateLayerRequestRequestTypeDef",
    {
        "LayerId": str,
        "Name": NotRequired[str],
        "Shortname": NotRequired[str],
        "Attributes": NotRequired[Mapping[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired[CloudWatchLogsConfigurationTypeDef],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[Sequence[str]],
        "Packages": NotRequired[Sequence[str]],
        "VolumeConfigurations": NotRequired[Sequence[VolumeConfigurationTypeDef]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "CustomRecipes": NotRequired[RecipesTypeDef],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired[LifecycleEventConfigurationTypeDef],
    },
)
DescribeOperatingSystemsResponseTypeDef = TypedDict(
    "DescribeOperatingSystemsResponseTypeDef",
    {
        "OperatingSystems": List[OperatingSystemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTimeBasedAutoScalingResultTypeDef = TypedDict(
    "DescribeTimeBasedAutoScalingResultTypeDef",
    {
        "TimeBasedAutoScalingConfigurations": List[TimeBasedAutoScalingConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstancesResultTypeDef = TypedDict(
    "DescribeInstancesResultTypeDef",
    {
        "Instances": List[InstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLayersResultTypeDef = TypedDict(
    "DescribeLayersResultTypeDef",
    {
        "Layers": List[LayerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
