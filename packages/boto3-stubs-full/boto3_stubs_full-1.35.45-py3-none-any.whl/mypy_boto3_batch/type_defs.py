"""
Type annotations for batch service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/type_defs/)

Usage::

    ```python
    from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef

    data: ArrayPropertiesDetailTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ArrayJobDependencyType,
    AssignPublicIpType,
    CEStateType,
    CEStatusType,
    CETypeType,
    CRAllocationStrategyType,
    CRTypeType,
    CRUpdateAllocationStrategyType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    JobDefinitionTypeType,
    JobStatusType,
    JQStateType,
    JQStatusType,
    LogDriverType,
    OrchestrationTypeType,
    PlatformCapabilityType,
    ResourceTypeType,
    RetryActionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ArrayPropertiesDetailTypeDef",
    "ArrayPropertiesSummaryTypeDef",
    "ArrayPropertiesTypeDef",
    "NetworkInterfaceTypeDef",
    "CancelJobRequestRequestTypeDef",
    "EksConfigurationTypeDef",
    "UpdatePolicyTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "Ec2ConfigurationTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "EphemeralStorageTypeDef",
    "FargatePlatformConfigurationTypeDef",
    "KeyValuePairTypeDef",
    "MountPointTypeDef",
    "NetworkConfigurationTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "RuntimePlatformTypeDef",
    "SecretTypeDef",
    "UlimitTypeDef",
    "ContainerSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "JobStateTimeLimitActionTypeDef",
    "DeleteComputeEnvironmentRequestRequestTypeDef",
    "DeleteJobQueueRequestRequestTypeDef",
    "DeleteSchedulingPolicyRequestRequestTypeDef",
    "DeregisterJobDefinitionRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeComputeEnvironmentsRequestRequestTypeDef",
    "DescribeJobDefinitionsRequestRequestTypeDef",
    "DescribeJobQueuesRequestRequestTypeDef",
    "DescribeJobsRequestRequestTypeDef",
    "DescribeSchedulingPoliciesRequestRequestTypeDef",
    "DeviceOutputTypeDef",
    "DeviceTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EksAttemptContainerDetailTypeDef",
    "EksContainerEnvironmentVariableTypeDef",
    "EksContainerResourceRequirementsOutputTypeDef",
    "EksContainerSecurityContextTypeDef",
    "EksContainerVolumeMountTypeDef",
    "EksContainerResourceRequirementsTypeDef",
    "EksEmptyDirTypeDef",
    "EksHostPathTypeDef",
    "EksMetadataOutputTypeDef",
    "EksMetadataTypeDef",
    "ImagePullSecretTypeDef",
    "EksSecretTypeDef",
    "EvaluateOnExitTypeDef",
    "ShareAttributesTypeDef",
    "FrontOfQueueJobSummaryTypeDef",
    "GetJobQueueSnapshotRequestRequestTypeDef",
    "HostTypeDef",
    "JobTimeoutTypeDef",
    "JobDependencyTypeDef",
    "NodeDetailsTypeDef",
    "NodePropertiesSummaryTypeDef",
    "KeyValuesPairTypeDef",
    "TmpfsOutputTypeDef",
    "ListSchedulingPoliciesRequestRequestTypeDef",
    "SchedulingPolicyListingDetailTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskContainerDependencyTypeDef",
    "TerminateJobRequestRequestTypeDef",
    "TmpfsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AttemptContainerDetailTypeDef",
    "AttemptTaskContainerDetailsTypeDef",
    "ComputeResourceOutputTypeDef",
    "ComputeResourceTypeDef",
    "ComputeResourceUpdateTypeDef",
    "ContainerOverridesTypeDef",
    "TaskContainerOverridesTypeDef",
    "LogConfigurationOutputTypeDef",
    "LogConfigurationTypeDef",
    "CreateComputeEnvironmentResponseTypeDef",
    "CreateJobQueueResponseTypeDef",
    "CreateSchedulingPolicyResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RegisterJobDefinitionResponseTypeDef",
    "SubmitJobResponseTypeDef",
    "UpdateComputeEnvironmentResponseTypeDef",
    "UpdateJobQueueResponseTypeDef",
    "CreateJobQueueRequestRequestTypeDef",
    "JobQueueDetailTypeDef",
    "UpdateJobQueueRequestRequestTypeDef",
    "DescribeComputeEnvironmentsRequestDescribeComputeEnvironmentsPaginateTypeDef",
    "DescribeJobDefinitionsRequestDescribeJobDefinitionsPaginateTypeDef",
    "DescribeJobQueuesRequestDescribeJobQueuesPaginateTypeDef",
    "ListSchedulingPoliciesRequestListSchedulingPoliciesPaginateTypeDef",
    "DeviceUnionTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EksAttemptDetailTypeDef",
    "EksContainerDetailTypeDef",
    "EksContainerOutputTypeDef",
    "EksContainerResourceRequirementsUnionTypeDef",
    "EksMetadataUnionTypeDef",
    "EksVolumeTypeDef",
    "RetryStrategyOutputTypeDef",
    "RetryStrategyTypeDef",
    "FairsharePolicyOutputTypeDef",
    "FairsharePolicyTypeDef",
    "FrontOfQueueDetailTypeDef",
    "JobSummaryTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListJobsRequestRequestTypeDef",
    "LinuxParametersOutputTypeDef",
    "ListSchedulingPoliciesResponseTypeDef",
    "TmpfsUnionTypeDef",
    "AttemptEcsTaskDetailsTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "CreateComputeEnvironmentRequestRequestTypeDef",
    "UpdateComputeEnvironmentRequestRequestTypeDef",
    "TaskPropertiesOverrideTypeDef",
    "LogConfigurationUnionTypeDef",
    "DescribeJobQueuesResponseTypeDef",
    "VolumeTypeDef",
    "EksContainerOverrideTypeDef",
    "EksContainerTypeDef",
    "EksPodPropertiesDetailTypeDef",
    "EksPodPropertiesOutputTypeDef",
    "SchedulingPolicyDetailTypeDef",
    "CreateSchedulingPolicyRequestRequestTypeDef",
    "UpdateSchedulingPolicyRequestRequestTypeDef",
    "GetJobQueueSnapshotResponseTypeDef",
    "ListJobsResponseTypeDef",
    "TaskContainerDetailsTypeDef",
    "TaskContainerPropertiesOutputTypeDef",
    "LinuxParametersTypeDef",
    "AttemptDetailTypeDef",
    "DescribeComputeEnvironmentsResponseTypeDef",
    "EcsPropertiesOverrideTypeDef",
    "ContainerDetailTypeDef",
    "ContainerPropertiesOutputTypeDef",
    "EksPodPropertiesOverrideTypeDef",
    "EksContainerUnionTypeDef",
    "EksPropertiesDetailTypeDef",
    "EksPropertiesOutputTypeDef",
    "DescribeSchedulingPoliciesResponseTypeDef",
    "EcsTaskDetailsTypeDef",
    "EcsTaskPropertiesOutputTypeDef",
    "LinuxParametersUnionTypeDef",
    "EksPropertiesOverrideTypeDef",
    "EksPodPropertiesTypeDef",
    "EcsPropertiesDetailTypeDef",
    "EcsPropertiesOutputTypeDef",
    "ContainerPropertiesTypeDef",
    "TaskContainerPropertiesTypeDef",
    "NodePropertyOverrideTypeDef",
    "EksPodPropertiesUnionTypeDef",
    "NodeRangePropertyOutputTypeDef",
    "ContainerPropertiesUnionTypeDef",
    "TaskContainerPropertiesUnionTypeDef",
    "NodeOverridesTypeDef",
    "EksPropertiesTypeDef",
    "NodePropertiesOutputTypeDef",
    "EcsTaskPropertiesTypeDef",
    "SubmitJobRequestRequestTypeDef",
    "EksPropertiesUnionTypeDef",
    "JobDefinitionTypeDef",
    "JobDetailTypeDef",
    "EcsTaskPropertiesUnionTypeDef",
    "DescribeJobDefinitionsResponseTypeDef",
    "DescribeJobsResponseTypeDef",
    "EcsPropertiesTypeDef",
    "EcsPropertiesUnionTypeDef",
    "NodeRangePropertyTypeDef",
    "NodeRangePropertyUnionTypeDef",
    "NodePropertiesTypeDef",
    "RegisterJobDefinitionRequestRequestTypeDef",
)

ArrayPropertiesDetailTypeDef = TypedDict(
    "ArrayPropertiesDetailTypeDef",
    {
        "statusSummary": NotRequired[Dict[str, int]],
        "size": NotRequired[int],
        "index": NotRequired[int],
    },
)
ArrayPropertiesSummaryTypeDef = TypedDict(
    "ArrayPropertiesSummaryTypeDef",
    {
        "size": NotRequired[int],
        "index": NotRequired[int],
    },
)
ArrayPropertiesTypeDef = TypedDict(
    "ArrayPropertiesTypeDef",
    {
        "size": NotRequired[int],
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": NotRequired[str],
        "ipv6Address": NotRequired[str],
        "privateIpv4Address": NotRequired[str],
    },
)
CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)
EksConfigurationTypeDef = TypedDict(
    "EksConfigurationTypeDef",
    {
        "eksClusterArn": str,
        "kubernetesNamespace": str,
    },
)
UpdatePolicyTypeDef = TypedDict(
    "UpdatePolicyTypeDef",
    {
        "terminateJobsOnUpdate": NotRequired[bool],
        "jobExecutionTimeoutMinutes": NotRequired[int],
    },
)
ComputeEnvironmentOrderTypeDef = TypedDict(
    "ComputeEnvironmentOrderTypeDef",
    {
        "order": int,
        "computeEnvironment": str,
    },
)
Ec2ConfigurationTypeDef = TypedDict(
    "Ec2ConfigurationTypeDef",
    {
        "imageType": str,
        "imageIdOverride": NotRequired[str],
        "imageKubernetesVersion": NotRequired[str],
    },
)
LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": NotRequired[str],
        "launchTemplateName": NotRequired[str],
        "version": NotRequired[str],
    },
)
EphemeralStorageTypeDef = TypedDict(
    "EphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)
FargatePlatformConfigurationTypeDef = TypedDict(
    "FargatePlatformConfigurationTypeDef",
    {
        "platformVersion": NotRequired[str],
    },
)
KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)
MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "containerPath": NotRequired[str],
        "readOnly": NotRequired[bool],
        "sourceVolume": NotRequired[str],
    },
)
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "assignPublicIp": NotRequired[AssignPublicIpType],
    },
)
RepositoryCredentialsTypeDef = TypedDict(
    "RepositoryCredentialsTypeDef",
    {
        "credentialsParameter": str,
    },
)
ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)
RuntimePlatformTypeDef = TypedDict(
    "RuntimePlatformTypeDef",
    {
        "operatingSystemFamily": NotRequired[str],
        "cpuArchitecture": NotRequired[str],
    },
)
SecretTypeDef = TypedDict(
    "SecretTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)
UlimitTypeDef = TypedDict(
    "UlimitTypeDef",
    {
        "hardLimit": int,
        "name": str,
        "softLimit": int,
    },
)
ContainerSummaryTypeDef = TypedDict(
    "ContainerSummaryTypeDef",
    {
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
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
JobStateTimeLimitActionTypeDef = TypedDict(
    "JobStateTimeLimitActionTypeDef",
    {
        "reason": str,
        "state": Literal["RUNNABLE"],
        "maxTimeSeconds": int,
        "action": Literal["CANCEL"],
    },
)
DeleteComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironment": str,
    },
)
DeleteJobQueueRequestRequestTypeDef = TypedDict(
    "DeleteJobQueueRequestRequestTypeDef",
    {
        "jobQueue": str,
    },
)
DeleteSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "DeleteSchedulingPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeregisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeregisterJobDefinitionRequestRequestTypeDef",
    {
        "jobDefinition": str,
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
DescribeComputeEnvironmentsRequestRequestTypeDef = TypedDict(
    "DescribeComputeEnvironmentsRequestRequestTypeDef",
    {
        "computeEnvironments": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeJobDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeJobDefinitionsRequestRequestTypeDef",
    {
        "jobDefinitions": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "jobDefinitionName": NotRequired[str],
        "status": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
DescribeJobQueuesRequestRequestTypeDef = TypedDict(
    "DescribeJobQueuesRequestRequestTypeDef",
    {
        "jobQueues": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeJobsRequestRequestTypeDef = TypedDict(
    "DescribeJobsRequestRequestTypeDef",
    {
        "jobs": Sequence[str],
    },
)
DescribeSchedulingPoliciesRequestRequestTypeDef = TypedDict(
    "DescribeSchedulingPoliciesRequestRequestTypeDef",
    {
        "arns": Sequence[str],
    },
)
DeviceOutputTypeDef = TypedDict(
    "DeviceOutputTypeDef",
    {
        "hostPath": str,
        "containerPath": NotRequired[str],
        "permissions": NotRequired[List[DeviceCgroupPermissionType]],
    },
)
DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "hostPath": str,
        "containerPath": NotRequired[str],
        "permissions": NotRequired[Sequence[DeviceCgroupPermissionType]],
    },
)
EFSAuthorizationConfigTypeDef = TypedDict(
    "EFSAuthorizationConfigTypeDef",
    {
        "accessPointId": NotRequired[str],
        "iam": NotRequired[EFSAuthorizationConfigIAMType],
    },
)
EksAttemptContainerDetailTypeDef = TypedDict(
    "EksAttemptContainerDetailTypeDef",
    {
        "name": NotRequired[str],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
    },
)
EksContainerEnvironmentVariableTypeDef = TypedDict(
    "EksContainerEnvironmentVariableTypeDef",
    {
        "name": str,
        "value": NotRequired[str],
    },
)
EksContainerResourceRequirementsOutputTypeDef = TypedDict(
    "EksContainerResourceRequirementsOutputTypeDef",
    {
        "limits": NotRequired[Dict[str, str]],
        "requests": NotRequired[Dict[str, str]],
    },
)
EksContainerSecurityContextTypeDef = TypedDict(
    "EksContainerSecurityContextTypeDef",
    {
        "runAsUser": NotRequired[int],
        "runAsGroup": NotRequired[int],
        "privileged": NotRequired[bool],
        "allowPrivilegeEscalation": NotRequired[bool],
        "readOnlyRootFilesystem": NotRequired[bool],
        "runAsNonRoot": NotRequired[bool],
    },
)
EksContainerVolumeMountTypeDef = TypedDict(
    "EksContainerVolumeMountTypeDef",
    {
        "name": NotRequired[str],
        "mountPath": NotRequired[str],
        "readOnly": NotRequired[bool],
    },
)
EksContainerResourceRequirementsTypeDef = TypedDict(
    "EksContainerResourceRequirementsTypeDef",
    {
        "limits": NotRequired[Mapping[str, str]],
        "requests": NotRequired[Mapping[str, str]],
    },
)
EksEmptyDirTypeDef = TypedDict(
    "EksEmptyDirTypeDef",
    {
        "medium": NotRequired[str],
        "sizeLimit": NotRequired[str],
    },
)
EksHostPathTypeDef = TypedDict(
    "EksHostPathTypeDef",
    {
        "path": NotRequired[str],
    },
)
EksMetadataOutputTypeDef = TypedDict(
    "EksMetadataOutputTypeDef",
    {
        "labels": NotRequired[Dict[str, str]],
    },
)
EksMetadataTypeDef = TypedDict(
    "EksMetadataTypeDef",
    {
        "labels": NotRequired[Mapping[str, str]],
    },
)
ImagePullSecretTypeDef = TypedDict(
    "ImagePullSecretTypeDef",
    {
        "name": str,
    },
)
EksSecretTypeDef = TypedDict(
    "EksSecretTypeDef",
    {
        "secretName": str,
        "optional": NotRequired[bool],
    },
)
EvaluateOnExitTypeDef = TypedDict(
    "EvaluateOnExitTypeDef",
    {
        "action": RetryActionType,
        "onStatusReason": NotRequired[str],
        "onReason": NotRequired[str],
        "onExitCode": NotRequired[str],
    },
)
ShareAttributesTypeDef = TypedDict(
    "ShareAttributesTypeDef",
    {
        "shareIdentifier": str,
        "weightFactor": NotRequired[float],
    },
)
FrontOfQueueJobSummaryTypeDef = TypedDict(
    "FrontOfQueueJobSummaryTypeDef",
    {
        "jobArn": NotRequired[str],
        "earliestTimeAtPosition": NotRequired[int],
    },
)
GetJobQueueSnapshotRequestRequestTypeDef = TypedDict(
    "GetJobQueueSnapshotRequestRequestTypeDef",
    {
        "jobQueue": str,
    },
)
HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "sourcePath": NotRequired[str],
    },
)
JobTimeoutTypeDef = TypedDict(
    "JobTimeoutTypeDef",
    {
        "attemptDurationSeconds": NotRequired[int],
    },
)
JobDependencyTypeDef = TypedDict(
    "JobDependencyTypeDef",
    {
        "jobId": NotRequired[str],
        "type": NotRequired[ArrayJobDependencyType],
    },
)
NodeDetailsTypeDef = TypedDict(
    "NodeDetailsTypeDef",
    {
        "nodeIndex": NotRequired[int],
        "isMainNode": NotRequired[bool],
    },
)
NodePropertiesSummaryTypeDef = TypedDict(
    "NodePropertiesSummaryTypeDef",
    {
        "isMainNode": NotRequired[bool],
        "numNodes": NotRequired[int],
        "nodeIndex": NotRequired[int],
    },
)
KeyValuesPairTypeDef = TypedDict(
    "KeyValuesPairTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
TmpfsOutputTypeDef = TypedDict(
    "TmpfsOutputTypeDef",
    {
        "containerPath": str,
        "size": int,
        "mountOptions": NotRequired[List[str]],
    },
)
ListSchedulingPoliciesRequestRequestTypeDef = TypedDict(
    "ListSchedulingPoliciesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SchedulingPolicyListingDetailTypeDef = TypedDict(
    "SchedulingPolicyListingDetailTypeDef",
    {
        "arn": str,
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
TaskContainerDependencyTypeDef = TypedDict(
    "TaskContainerDependencyTypeDef",
    {
        "containerName": NotRequired[str],
        "condition": NotRequired[str],
    },
)
TerminateJobRequestRequestTypeDef = TypedDict(
    "TerminateJobRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)
TmpfsTypeDef = TypedDict(
    "TmpfsTypeDef",
    {
        "containerPath": str,
        "size": int,
        "mountOptions": NotRequired[Sequence[str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
AttemptContainerDetailTypeDef = TypedDict(
    "AttemptContainerDetailTypeDef",
    {
        "containerInstanceArn": NotRequired[str],
        "taskArn": NotRequired[str],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
        "logStreamName": NotRequired[str],
        "networkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
    },
)
AttemptTaskContainerDetailsTypeDef = TypedDict(
    "AttemptTaskContainerDetailsTypeDef",
    {
        "exitCode": NotRequired[int],
        "name": NotRequired[str],
        "reason": NotRequired[str],
        "logStreamName": NotRequired[str],
        "networkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
    },
)
ComputeResourceOutputTypeDef = TypedDict(
    "ComputeResourceOutputTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": List[str],
        "allocationStrategy": NotRequired[CRAllocationStrategyType],
        "minvCpus": NotRequired[int],
        "desiredvCpus": NotRequired[int],
        "instanceTypes": NotRequired[List[str]],
        "imageId": NotRequired[str],
        "securityGroupIds": NotRequired[List[str]],
        "ec2KeyPair": NotRequired[str],
        "instanceRole": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "placementGroup": NotRequired[str],
        "bidPercentage": NotRequired[int],
        "spotIamFleetRole": NotRequired[str],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "ec2Configuration": NotRequired[List[Ec2ConfigurationTypeDef]],
    },
)
ComputeResourceTypeDef = TypedDict(
    "ComputeResourceTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": Sequence[str],
        "allocationStrategy": NotRequired[CRAllocationStrategyType],
        "minvCpus": NotRequired[int],
        "desiredvCpus": NotRequired[int],
        "instanceTypes": NotRequired[Sequence[str]],
        "imageId": NotRequired[str],
        "securityGroupIds": NotRequired[Sequence[str]],
        "ec2KeyPair": NotRequired[str],
        "instanceRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "placementGroup": NotRequired[str],
        "bidPercentage": NotRequired[int],
        "spotIamFleetRole": NotRequired[str],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "ec2Configuration": NotRequired[Sequence[Ec2ConfigurationTypeDef]],
    },
)
ComputeResourceUpdateTypeDef = TypedDict(
    "ComputeResourceUpdateTypeDef",
    {
        "minvCpus": NotRequired[int],
        "maxvCpus": NotRequired[int],
        "desiredvCpus": NotRequired[int],
        "subnets": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "allocationStrategy": NotRequired[CRUpdateAllocationStrategyType],
        "instanceTypes": NotRequired[Sequence[str]],
        "ec2KeyPair": NotRequired[str],
        "instanceRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "placementGroup": NotRequired[str],
        "bidPercentage": NotRequired[int],
        "launchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "ec2Configuration": NotRequired[Sequence[Ec2ConfigurationTypeDef]],
        "updateToLatestImageVersion": NotRequired[bool],
        "type": NotRequired[CRTypeType],
        "imageId": NotRequired[str],
    },
)
ContainerOverridesTypeDef = TypedDict(
    "ContainerOverridesTypeDef",
    {
        "vcpus": NotRequired[int],
        "memory": NotRequired[int],
        "command": NotRequired[Sequence[str]],
        "instanceType": NotRequired[str],
        "environment": NotRequired[Sequence[KeyValuePairTypeDef]],
        "resourceRequirements": NotRequired[Sequence[ResourceRequirementTypeDef]],
    },
)
TaskContainerOverridesTypeDef = TypedDict(
    "TaskContainerOverridesTypeDef",
    {
        "command": NotRequired[Sequence[str]],
        "environment": NotRequired[Sequence[KeyValuePairTypeDef]],
        "name": NotRequired[str],
        "resourceRequirements": NotRequired[Sequence[ResourceRequirementTypeDef]],
    },
)
LogConfigurationOutputTypeDef = TypedDict(
    "LogConfigurationOutputTypeDef",
    {
        "logDriver": LogDriverType,
        "options": NotRequired[Dict[str, str]],
        "secretOptions": NotRequired[List[SecretTypeDef]],
    },
)
LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "logDriver": LogDriverType,
        "options": NotRequired[Mapping[str, str]],
        "secretOptions": NotRequired[Sequence[SecretTypeDef]],
    },
)
CreateComputeEnvironmentResponseTypeDef = TypedDict(
    "CreateComputeEnvironmentResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobQueueResponseTypeDef = TypedDict(
    "CreateJobQueueResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSchedulingPolicyResponseTypeDef = TypedDict(
    "CreateSchedulingPolicyResponseTypeDef",
    {
        "name": str,
        "arn": str,
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
RegisterJobDefinitionResponseTypeDef = TypedDict(
    "RegisterJobDefinitionResponseTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubmitJobResponseTypeDef = TypedDict(
    "SubmitJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateComputeEnvironmentResponseTypeDef = TypedDict(
    "UpdateComputeEnvironmentResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateJobQueueResponseTypeDef = TypedDict(
    "UpdateJobQueueResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobQueueRequestRequestTypeDef = TypedDict(
    "CreateJobQueueRequestRequestTypeDef",
    {
        "jobQueueName": str,
        "priority": int,
        "computeEnvironmentOrder": Sequence[ComputeEnvironmentOrderTypeDef],
        "state": NotRequired[JQStateType],
        "schedulingPolicyArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "jobStateTimeLimitActions": NotRequired[Sequence[JobStateTimeLimitActionTypeDef]],
    },
)
JobQueueDetailTypeDef = TypedDict(
    "JobQueueDetailTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": JQStateType,
        "priority": int,
        "computeEnvironmentOrder": List[ComputeEnvironmentOrderTypeDef],
        "schedulingPolicyArn": NotRequired[str],
        "status": NotRequired[JQStatusType],
        "statusReason": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "jobStateTimeLimitActions": NotRequired[List[JobStateTimeLimitActionTypeDef]],
    },
)
UpdateJobQueueRequestRequestTypeDef = TypedDict(
    "UpdateJobQueueRequestRequestTypeDef",
    {
        "jobQueue": str,
        "state": NotRequired[JQStateType],
        "schedulingPolicyArn": NotRequired[str],
        "priority": NotRequired[int],
        "computeEnvironmentOrder": NotRequired[Sequence[ComputeEnvironmentOrderTypeDef]],
        "jobStateTimeLimitActions": NotRequired[Sequence[JobStateTimeLimitActionTypeDef]],
    },
)
DescribeComputeEnvironmentsRequestDescribeComputeEnvironmentsPaginateTypeDef = TypedDict(
    "DescribeComputeEnvironmentsRequestDescribeComputeEnvironmentsPaginateTypeDef",
    {
        "computeEnvironments": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeJobDefinitionsRequestDescribeJobDefinitionsPaginateTypeDef = TypedDict(
    "DescribeJobDefinitionsRequestDescribeJobDefinitionsPaginateTypeDef",
    {
        "jobDefinitions": NotRequired[Sequence[str]],
        "jobDefinitionName": NotRequired[str],
        "status": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeJobQueuesRequestDescribeJobQueuesPaginateTypeDef = TypedDict(
    "DescribeJobQueuesRequestDescribeJobQueuesPaginateTypeDef",
    {
        "jobQueues": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchedulingPoliciesRequestListSchedulingPoliciesPaginateTypeDef = TypedDict(
    "ListSchedulingPoliciesRequestListSchedulingPoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DeviceUnionTypeDef = Union[DeviceTypeDef, DeviceOutputTypeDef]
EFSVolumeConfigurationTypeDef = TypedDict(
    "EFSVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
        "rootDirectory": NotRequired[str],
        "transitEncryption": NotRequired[EFSTransitEncryptionType],
        "transitEncryptionPort": NotRequired[int],
        "authorizationConfig": NotRequired[EFSAuthorizationConfigTypeDef],
    },
)
EksAttemptDetailTypeDef = TypedDict(
    "EksAttemptDetailTypeDef",
    {
        "containers": NotRequired[List[EksAttemptContainerDetailTypeDef]],
        "initContainers": NotRequired[List[EksAttemptContainerDetailTypeDef]],
        "eksClusterArn": NotRequired[str],
        "podName": NotRequired[str],
        "nodeName": NotRequired[str],
        "startedAt": NotRequired[int],
        "stoppedAt": NotRequired[int],
        "statusReason": NotRequired[str],
    },
)
EksContainerDetailTypeDef = TypedDict(
    "EksContainerDetailTypeDef",
    {
        "name": NotRequired[str],
        "image": NotRequired[str],
        "imagePullPolicy": NotRequired[str],
        "command": NotRequired[List[str]],
        "args": NotRequired[List[str]],
        "env": NotRequired[List[EksContainerEnvironmentVariableTypeDef]],
        "resources": NotRequired[EksContainerResourceRequirementsOutputTypeDef],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
        "volumeMounts": NotRequired[List[EksContainerVolumeMountTypeDef]],
        "securityContext": NotRequired[EksContainerSecurityContextTypeDef],
    },
)
EksContainerOutputTypeDef = TypedDict(
    "EksContainerOutputTypeDef",
    {
        "image": str,
        "name": NotRequired[str],
        "imagePullPolicy": NotRequired[str],
        "command": NotRequired[List[str]],
        "args": NotRequired[List[str]],
        "env": NotRequired[List[EksContainerEnvironmentVariableTypeDef]],
        "resources": NotRequired[EksContainerResourceRequirementsOutputTypeDef],
        "volumeMounts": NotRequired[List[EksContainerVolumeMountTypeDef]],
        "securityContext": NotRequired[EksContainerSecurityContextTypeDef],
    },
)
EksContainerResourceRequirementsUnionTypeDef = Union[
    EksContainerResourceRequirementsTypeDef, EksContainerResourceRequirementsOutputTypeDef
]
EksMetadataUnionTypeDef = Union[EksMetadataTypeDef, EksMetadataOutputTypeDef]
EksVolumeTypeDef = TypedDict(
    "EksVolumeTypeDef",
    {
        "name": str,
        "hostPath": NotRequired[EksHostPathTypeDef],
        "emptyDir": NotRequired[EksEmptyDirTypeDef],
        "secret": NotRequired[EksSecretTypeDef],
    },
)
RetryStrategyOutputTypeDef = TypedDict(
    "RetryStrategyOutputTypeDef",
    {
        "attempts": NotRequired[int],
        "evaluateOnExit": NotRequired[List[EvaluateOnExitTypeDef]],
    },
)
RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "attempts": NotRequired[int],
        "evaluateOnExit": NotRequired[Sequence[EvaluateOnExitTypeDef]],
    },
)
FairsharePolicyOutputTypeDef = TypedDict(
    "FairsharePolicyOutputTypeDef",
    {
        "shareDecaySeconds": NotRequired[int],
        "computeReservation": NotRequired[int],
        "shareDistribution": NotRequired[List[ShareAttributesTypeDef]],
    },
)
FairsharePolicyTypeDef = TypedDict(
    "FairsharePolicyTypeDef",
    {
        "shareDecaySeconds": NotRequired[int],
        "computeReservation": NotRequired[int],
        "shareDistribution": NotRequired[Sequence[ShareAttributesTypeDef]],
    },
)
FrontOfQueueDetailTypeDef = TypedDict(
    "FrontOfQueueDetailTypeDef",
    {
        "jobs": NotRequired[List[FrontOfQueueJobSummaryTypeDef]],
        "lastUpdatedAt": NotRequired[int],
    },
)
JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobArn": NotRequired[str],
        "createdAt": NotRequired[int],
        "status": NotRequired[JobStatusType],
        "statusReason": NotRequired[str],
        "startedAt": NotRequired[int],
        "stoppedAt": NotRequired[int],
        "container": NotRequired[ContainerSummaryTypeDef],
        "arrayProperties": NotRequired[ArrayPropertiesSummaryTypeDef],
        "nodeProperties": NotRequired[NodePropertiesSummaryTypeDef],
        "jobDefinition": NotRequired[str],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "jobQueue": NotRequired[str],
        "arrayJobId": NotRequired[str],
        "multiNodeJobId": NotRequired[str],
        "jobStatus": NotRequired[JobStatusType],
        "filters": NotRequired[Sequence[KeyValuesPairTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "jobQueue": NotRequired[str],
        "arrayJobId": NotRequired[str],
        "multiNodeJobId": NotRequired[str],
        "jobStatus": NotRequired[JobStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filters": NotRequired[Sequence[KeyValuesPairTypeDef]],
    },
)
LinuxParametersOutputTypeDef = TypedDict(
    "LinuxParametersOutputTypeDef",
    {
        "devices": NotRequired[List[DeviceOutputTypeDef]],
        "initProcessEnabled": NotRequired[bool],
        "sharedMemorySize": NotRequired[int],
        "tmpfs": NotRequired[List[TmpfsOutputTypeDef]],
        "maxSwap": NotRequired[int],
        "swappiness": NotRequired[int],
    },
)
ListSchedulingPoliciesResponseTypeDef = TypedDict(
    "ListSchedulingPoliciesResponseTypeDef",
    {
        "schedulingPolicies": List[SchedulingPolicyListingDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TmpfsUnionTypeDef = Union[TmpfsTypeDef, TmpfsOutputTypeDef]
AttemptEcsTaskDetailsTypeDef = TypedDict(
    "AttemptEcsTaskDetailsTypeDef",
    {
        "containerInstanceArn": NotRequired[str],
        "taskArn": NotRequired[str],
        "containers": NotRequired[List[AttemptTaskContainerDetailsTypeDef]],
    },
)
ComputeEnvironmentDetailTypeDef = TypedDict(
    "ComputeEnvironmentDetailTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "unmanagedvCpus": NotRequired[int],
        "ecsClusterArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[CETypeType],
        "state": NotRequired[CEStateType],
        "status": NotRequired[CEStatusType],
        "statusReason": NotRequired[str],
        "computeResources": NotRequired[ComputeResourceOutputTypeDef],
        "serviceRole": NotRequired[str],
        "updatePolicy": NotRequired[UpdatePolicyTypeDef],
        "eksConfiguration": NotRequired[EksConfigurationTypeDef],
        "containerOrchestrationType": NotRequired[OrchestrationTypeType],
        "uuid": NotRequired[str],
        "context": NotRequired[str],
    },
)
CreateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironmentName": str,
        "type": CETypeType,
        "state": NotRequired[CEStateType],
        "unmanagedvCpus": NotRequired[int],
        "computeResources": NotRequired[ComputeResourceTypeDef],
        "serviceRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "eksConfiguration": NotRequired[EksConfigurationTypeDef],
        "context": NotRequired[str],
    },
)
UpdateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironment": str,
        "state": NotRequired[CEStateType],
        "unmanagedvCpus": NotRequired[int],
        "computeResources": NotRequired[ComputeResourceUpdateTypeDef],
        "serviceRole": NotRequired[str],
        "updatePolicy": NotRequired[UpdatePolicyTypeDef],
        "context": NotRequired[str],
    },
)
TaskPropertiesOverrideTypeDef = TypedDict(
    "TaskPropertiesOverrideTypeDef",
    {
        "containers": NotRequired[Sequence[TaskContainerOverridesTypeDef]],
    },
)
LogConfigurationUnionTypeDef = Union[LogConfigurationTypeDef, LogConfigurationOutputTypeDef]
DescribeJobQueuesResponseTypeDef = TypedDict(
    "DescribeJobQueuesResponseTypeDef",
    {
        "jobQueues": List[JobQueueDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "host": NotRequired[HostTypeDef],
        "name": NotRequired[str],
        "efsVolumeConfiguration": NotRequired[EFSVolumeConfigurationTypeDef],
    },
)
EksContainerOverrideTypeDef = TypedDict(
    "EksContainerOverrideTypeDef",
    {
        "name": NotRequired[str],
        "image": NotRequired[str],
        "command": NotRequired[Sequence[str]],
        "args": NotRequired[Sequence[str]],
        "env": NotRequired[Sequence[EksContainerEnvironmentVariableTypeDef]],
        "resources": NotRequired[EksContainerResourceRequirementsUnionTypeDef],
    },
)
EksContainerTypeDef = TypedDict(
    "EksContainerTypeDef",
    {
        "image": str,
        "name": NotRequired[str],
        "imagePullPolicy": NotRequired[str],
        "command": NotRequired[Sequence[str]],
        "args": NotRequired[Sequence[str]],
        "env": NotRequired[Sequence[EksContainerEnvironmentVariableTypeDef]],
        "resources": NotRequired[EksContainerResourceRequirementsUnionTypeDef],
        "volumeMounts": NotRequired[Sequence[EksContainerVolumeMountTypeDef]],
        "securityContext": NotRequired[EksContainerSecurityContextTypeDef],
    },
)
EksPodPropertiesDetailTypeDef = TypedDict(
    "EksPodPropertiesDetailTypeDef",
    {
        "serviceAccountName": NotRequired[str],
        "hostNetwork": NotRequired[bool],
        "dnsPolicy": NotRequired[str],
        "imagePullSecrets": NotRequired[List[ImagePullSecretTypeDef]],
        "containers": NotRequired[List[EksContainerDetailTypeDef]],
        "initContainers": NotRequired[List[EksContainerDetailTypeDef]],
        "volumes": NotRequired[List[EksVolumeTypeDef]],
        "podName": NotRequired[str],
        "nodeName": NotRequired[str],
        "metadata": NotRequired[EksMetadataOutputTypeDef],
        "shareProcessNamespace": NotRequired[bool],
    },
)
EksPodPropertiesOutputTypeDef = TypedDict(
    "EksPodPropertiesOutputTypeDef",
    {
        "serviceAccountName": NotRequired[str],
        "hostNetwork": NotRequired[bool],
        "dnsPolicy": NotRequired[str],
        "imagePullSecrets": NotRequired[List[ImagePullSecretTypeDef]],
        "containers": NotRequired[List[EksContainerOutputTypeDef]],
        "initContainers": NotRequired[List[EksContainerOutputTypeDef]],
        "volumes": NotRequired[List[EksVolumeTypeDef]],
        "metadata": NotRequired[EksMetadataOutputTypeDef],
        "shareProcessNamespace": NotRequired[bool],
    },
)
SchedulingPolicyDetailTypeDef = TypedDict(
    "SchedulingPolicyDetailTypeDef",
    {
        "name": str,
        "arn": str,
        "fairsharePolicy": NotRequired[FairsharePolicyOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "CreateSchedulingPolicyRequestRequestTypeDef",
    {
        "name": str,
        "fairsharePolicy": NotRequired[FairsharePolicyTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "UpdateSchedulingPolicyRequestRequestTypeDef",
    {
        "arn": str,
        "fairsharePolicy": NotRequired[FairsharePolicyTypeDef],
    },
)
GetJobQueueSnapshotResponseTypeDef = TypedDict(
    "GetJobQueueSnapshotResponseTypeDef",
    {
        "frontOfQueue": FrontOfQueueDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "jobSummaryList": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TaskContainerDetailsTypeDef = TypedDict(
    "TaskContainerDetailsTypeDef",
    {
        "command": NotRequired[List[str]],
        "dependsOn": NotRequired[List[TaskContainerDependencyTypeDef]],
        "environment": NotRequired[List[KeyValuePairTypeDef]],
        "essential": NotRequired[bool],
        "image": NotRequired[str],
        "linuxParameters": NotRequired[LinuxParametersOutputTypeDef],
        "logConfiguration": NotRequired[LogConfigurationOutputTypeDef],
        "mountPoints": NotRequired[List[MountPointTypeDef]],
        "name": NotRequired[str],
        "privileged": NotRequired[bool],
        "readonlyRootFilesystem": NotRequired[bool],
        "repositoryCredentials": NotRequired[RepositoryCredentialsTypeDef],
        "resourceRequirements": NotRequired[List[ResourceRequirementTypeDef]],
        "secrets": NotRequired[List[SecretTypeDef]],
        "ulimits": NotRequired[List[UlimitTypeDef]],
        "user": NotRequired[str],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
        "logStreamName": NotRequired[str],
        "networkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
    },
)
TaskContainerPropertiesOutputTypeDef = TypedDict(
    "TaskContainerPropertiesOutputTypeDef",
    {
        "image": str,
        "command": NotRequired[List[str]],
        "dependsOn": NotRequired[List[TaskContainerDependencyTypeDef]],
        "environment": NotRequired[List[KeyValuePairTypeDef]],
        "essential": NotRequired[bool],
        "linuxParameters": NotRequired[LinuxParametersOutputTypeDef],
        "logConfiguration": NotRequired[LogConfigurationOutputTypeDef],
        "mountPoints": NotRequired[List[MountPointTypeDef]],
        "name": NotRequired[str],
        "privileged": NotRequired[bool],
        "readonlyRootFilesystem": NotRequired[bool],
        "repositoryCredentials": NotRequired[RepositoryCredentialsTypeDef],
        "resourceRequirements": NotRequired[List[ResourceRequirementTypeDef]],
        "secrets": NotRequired[List[SecretTypeDef]],
        "ulimits": NotRequired[List[UlimitTypeDef]],
        "user": NotRequired[str],
    },
)
LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "devices": NotRequired[Sequence[DeviceUnionTypeDef]],
        "initProcessEnabled": NotRequired[bool],
        "sharedMemorySize": NotRequired[int],
        "tmpfs": NotRequired[Sequence[TmpfsUnionTypeDef]],
        "maxSwap": NotRequired[int],
        "swappiness": NotRequired[int],
    },
)
AttemptDetailTypeDef = TypedDict(
    "AttemptDetailTypeDef",
    {
        "container": NotRequired[AttemptContainerDetailTypeDef],
        "startedAt": NotRequired[int],
        "stoppedAt": NotRequired[int],
        "statusReason": NotRequired[str],
        "taskProperties": NotRequired[List[AttemptEcsTaskDetailsTypeDef]],
    },
)
DescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "DescribeComputeEnvironmentsResponseTypeDef",
    {
        "computeEnvironments": List[ComputeEnvironmentDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EcsPropertiesOverrideTypeDef = TypedDict(
    "EcsPropertiesOverrideTypeDef",
    {
        "taskProperties": NotRequired[Sequence[TaskPropertiesOverrideTypeDef]],
    },
)
ContainerDetailTypeDef = TypedDict(
    "ContainerDetailTypeDef",
    {
        "image": NotRequired[str],
        "vcpus": NotRequired[int],
        "memory": NotRequired[int],
        "command": NotRequired[List[str]],
        "jobRoleArn": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "volumes": NotRequired[List[VolumeTypeDef]],
        "environment": NotRequired[List[KeyValuePairTypeDef]],
        "mountPoints": NotRequired[List[MountPointTypeDef]],
        "readonlyRootFilesystem": NotRequired[bool],
        "ulimits": NotRequired[List[UlimitTypeDef]],
        "privileged": NotRequired[bool],
        "user": NotRequired[str],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
        "containerInstanceArn": NotRequired[str],
        "taskArn": NotRequired[str],
        "logStreamName": NotRequired[str],
        "instanceType": NotRequired[str],
        "networkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
        "resourceRequirements": NotRequired[List[ResourceRequirementTypeDef]],
        "linuxParameters": NotRequired[LinuxParametersOutputTypeDef],
        "logConfiguration": NotRequired[LogConfigurationOutputTypeDef],
        "secrets": NotRequired[List[SecretTypeDef]],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "fargatePlatformConfiguration": NotRequired[FargatePlatformConfigurationTypeDef],
        "ephemeralStorage": NotRequired[EphemeralStorageTypeDef],
        "runtimePlatform": NotRequired[RuntimePlatformTypeDef],
        "repositoryCredentials": NotRequired[RepositoryCredentialsTypeDef],
    },
)
ContainerPropertiesOutputTypeDef = TypedDict(
    "ContainerPropertiesOutputTypeDef",
    {
        "image": NotRequired[str],
        "vcpus": NotRequired[int],
        "memory": NotRequired[int],
        "command": NotRequired[List[str]],
        "jobRoleArn": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "volumes": NotRequired[List[VolumeTypeDef]],
        "environment": NotRequired[List[KeyValuePairTypeDef]],
        "mountPoints": NotRequired[List[MountPointTypeDef]],
        "readonlyRootFilesystem": NotRequired[bool],
        "privileged": NotRequired[bool],
        "ulimits": NotRequired[List[UlimitTypeDef]],
        "user": NotRequired[str],
        "instanceType": NotRequired[str],
        "resourceRequirements": NotRequired[List[ResourceRequirementTypeDef]],
        "linuxParameters": NotRequired[LinuxParametersOutputTypeDef],
        "logConfiguration": NotRequired[LogConfigurationOutputTypeDef],
        "secrets": NotRequired[List[SecretTypeDef]],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "fargatePlatformConfiguration": NotRequired[FargatePlatformConfigurationTypeDef],
        "ephemeralStorage": NotRequired[EphemeralStorageTypeDef],
        "runtimePlatform": NotRequired[RuntimePlatformTypeDef],
        "repositoryCredentials": NotRequired[RepositoryCredentialsTypeDef],
    },
)
EksPodPropertiesOverrideTypeDef = TypedDict(
    "EksPodPropertiesOverrideTypeDef",
    {
        "containers": NotRequired[Sequence[EksContainerOverrideTypeDef]],
        "initContainers": NotRequired[Sequence[EksContainerOverrideTypeDef]],
        "metadata": NotRequired[EksMetadataUnionTypeDef],
    },
)
EksContainerUnionTypeDef = Union[EksContainerTypeDef, EksContainerOutputTypeDef]
EksPropertiesDetailTypeDef = TypedDict(
    "EksPropertiesDetailTypeDef",
    {
        "podProperties": NotRequired[EksPodPropertiesDetailTypeDef],
    },
)
EksPropertiesOutputTypeDef = TypedDict(
    "EksPropertiesOutputTypeDef",
    {
        "podProperties": NotRequired[EksPodPropertiesOutputTypeDef],
    },
)
DescribeSchedulingPoliciesResponseTypeDef = TypedDict(
    "DescribeSchedulingPoliciesResponseTypeDef",
    {
        "schedulingPolicies": List[SchedulingPolicyDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EcsTaskDetailsTypeDef = TypedDict(
    "EcsTaskDetailsTypeDef",
    {
        "containers": NotRequired[List[TaskContainerDetailsTypeDef]],
        "containerInstanceArn": NotRequired[str],
        "taskArn": NotRequired[str],
        "ephemeralStorage": NotRequired[EphemeralStorageTypeDef],
        "executionRoleArn": NotRequired[str],
        "platformVersion": NotRequired[str],
        "ipcMode": NotRequired[str],
        "taskRoleArn": NotRequired[str],
        "pidMode": NotRequired[str],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "runtimePlatform": NotRequired[RuntimePlatformTypeDef],
        "volumes": NotRequired[List[VolumeTypeDef]],
    },
)
EcsTaskPropertiesOutputTypeDef = TypedDict(
    "EcsTaskPropertiesOutputTypeDef",
    {
        "containers": List[TaskContainerPropertiesOutputTypeDef],
        "ephemeralStorage": NotRequired[EphemeralStorageTypeDef],
        "executionRoleArn": NotRequired[str],
        "platformVersion": NotRequired[str],
        "ipcMode": NotRequired[str],
        "taskRoleArn": NotRequired[str],
        "pidMode": NotRequired[str],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "runtimePlatform": NotRequired[RuntimePlatformTypeDef],
        "volumes": NotRequired[List[VolumeTypeDef]],
    },
)
LinuxParametersUnionTypeDef = Union[LinuxParametersTypeDef, LinuxParametersOutputTypeDef]
EksPropertiesOverrideTypeDef = TypedDict(
    "EksPropertiesOverrideTypeDef",
    {
        "podProperties": NotRequired[EksPodPropertiesOverrideTypeDef],
    },
)
EksPodPropertiesTypeDef = TypedDict(
    "EksPodPropertiesTypeDef",
    {
        "serviceAccountName": NotRequired[str],
        "hostNetwork": NotRequired[bool],
        "dnsPolicy": NotRequired[str],
        "imagePullSecrets": NotRequired[Sequence[ImagePullSecretTypeDef]],
        "containers": NotRequired[Sequence[EksContainerUnionTypeDef]],
        "initContainers": NotRequired[Sequence[EksContainerUnionTypeDef]],
        "volumes": NotRequired[Sequence[EksVolumeTypeDef]],
        "metadata": NotRequired[EksMetadataUnionTypeDef],
        "shareProcessNamespace": NotRequired[bool],
    },
)
EcsPropertiesDetailTypeDef = TypedDict(
    "EcsPropertiesDetailTypeDef",
    {
        "taskProperties": NotRequired[List[EcsTaskDetailsTypeDef]],
    },
)
EcsPropertiesOutputTypeDef = TypedDict(
    "EcsPropertiesOutputTypeDef",
    {
        "taskProperties": List[EcsTaskPropertiesOutputTypeDef],
    },
)
ContainerPropertiesTypeDef = TypedDict(
    "ContainerPropertiesTypeDef",
    {
        "image": NotRequired[str],
        "vcpus": NotRequired[int],
        "memory": NotRequired[int],
        "command": NotRequired[Sequence[str]],
        "jobRoleArn": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "volumes": NotRequired[Sequence[VolumeTypeDef]],
        "environment": NotRequired[Sequence[KeyValuePairTypeDef]],
        "mountPoints": NotRequired[Sequence[MountPointTypeDef]],
        "readonlyRootFilesystem": NotRequired[bool],
        "privileged": NotRequired[bool],
        "ulimits": NotRequired[Sequence[UlimitTypeDef]],
        "user": NotRequired[str],
        "instanceType": NotRequired[str],
        "resourceRequirements": NotRequired[Sequence[ResourceRequirementTypeDef]],
        "linuxParameters": NotRequired[LinuxParametersUnionTypeDef],
        "logConfiguration": NotRequired[LogConfigurationUnionTypeDef],
        "secrets": NotRequired[Sequence[SecretTypeDef]],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "fargatePlatformConfiguration": NotRequired[FargatePlatformConfigurationTypeDef],
        "ephemeralStorage": NotRequired[EphemeralStorageTypeDef],
        "runtimePlatform": NotRequired[RuntimePlatformTypeDef],
        "repositoryCredentials": NotRequired[RepositoryCredentialsTypeDef],
    },
)
TaskContainerPropertiesTypeDef = TypedDict(
    "TaskContainerPropertiesTypeDef",
    {
        "image": str,
        "command": NotRequired[Sequence[str]],
        "dependsOn": NotRequired[Sequence[TaskContainerDependencyTypeDef]],
        "environment": NotRequired[Sequence[KeyValuePairTypeDef]],
        "essential": NotRequired[bool],
        "linuxParameters": NotRequired[LinuxParametersUnionTypeDef],
        "logConfiguration": NotRequired[LogConfigurationUnionTypeDef],
        "mountPoints": NotRequired[Sequence[MountPointTypeDef]],
        "name": NotRequired[str],
        "privileged": NotRequired[bool],
        "readonlyRootFilesystem": NotRequired[bool],
        "repositoryCredentials": NotRequired[RepositoryCredentialsTypeDef],
        "resourceRequirements": NotRequired[Sequence[ResourceRequirementTypeDef]],
        "secrets": NotRequired[Sequence[SecretTypeDef]],
        "ulimits": NotRequired[Sequence[UlimitTypeDef]],
        "user": NotRequired[str],
    },
)
NodePropertyOverrideTypeDef = TypedDict(
    "NodePropertyOverrideTypeDef",
    {
        "targetNodes": str,
        "containerOverrides": NotRequired[ContainerOverridesTypeDef],
        "ecsPropertiesOverride": NotRequired[EcsPropertiesOverrideTypeDef],
        "instanceTypes": NotRequired[Sequence[str]],
        "eksPropertiesOverride": NotRequired[EksPropertiesOverrideTypeDef],
    },
)
EksPodPropertiesUnionTypeDef = Union[EksPodPropertiesTypeDef, EksPodPropertiesOutputTypeDef]
NodeRangePropertyOutputTypeDef = TypedDict(
    "NodeRangePropertyOutputTypeDef",
    {
        "targetNodes": str,
        "container": NotRequired[ContainerPropertiesOutputTypeDef],
        "instanceTypes": NotRequired[List[str]],
        "ecsProperties": NotRequired[EcsPropertiesOutputTypeDef],
        "eksProperties": NotRequired[EksPropertiesOutputTypeDef],
    },
)
ContainerPropertiesUnionTypeDef = Union[
    ContainerPropertiesTypeDef, ContainerPropertiesOutputTypeDef
]
TaskContainerPropertiesUnionTypeDef = Union[
    TaskContainerPropertiesTypeDef, TaskContainerPropertiesOutputTypeDef
]
NodeOverridesTypeDef = TypedDict(
    "NodeOverridesTypeDef",
    {
        "numNodes": NotRequired[int],
        "nodePropertyOverrides": NotRequired[Sequence[NodePropertyOverrideTypeDef]],
    },
)
EksPropertiesTypeDef = TypedDict(
    "EksPropertiesTypeDef",
    {
        "podProperties": NotRequired[EksPodPropertiesUnionTypeDef],
    },
)
NodePropertiesOutputTypeDef = TypedDict(
    "NodePropertiesOutputTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[NodeRangePropertyOutputTypeDef],
    },
)
EcsTaskPropertiesTypeDef = TypedDict(
    "EcsTaskPropertiesTypeDef",
    {
        "containers": Sequence[TaskContainerPropertiesUnionTypeDef],
        "ephemeralStorage": NotRequired[EphemeralStorageTypeDef],
        "executionRoleArn": NotRequired[str],
        "platformVersion": NotRequired[str],
        "ipcMode": NotRequired[str],
        "taskRoleArn": NotRequired[str],
        "pidMode": NotRequired[str],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "runtimePlatform": NotRequired[RuntimePlatformTypeDef],
        "volumes": NotRequired[Sequence[VolumeTypeDef]],
    },
)
SubmitJobRequestRequestTypeDef = TypedDict(
    "SubmitJobRequestRequestTypeDef",
    {
        "jobName": str,
        "jobQueue": str,
        "jobDefinition": str,
        "shareIdentifier": NotRequired[str],
        "schedulingPriorityOverride": NotRequired[int],
        "arrayProperties": NotRequired[ArrayPropertiesTypeDef],
        "dependsOn": NotRequired[Sequence[JobDependencyTypeDef]],
        "parameters": NotRequired[Mapping[str, str]],
        "containerOverrides": NotRequired[ContainerOverridesTypeDef],
        "nodeOverrides": NotRequired[NodeOverridesTypeDef],
        "retryStrategy": NotRequired[RetryStrategyTypeDef],
        "propagateTags": NotRequired[bool],
        "timeout": NotRequired[JobTimeoutTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "eksPropertiesOverride": NotRequired[EksPropertiesOverrideTypeDef],
        "ecsPropertiesOverride": NotRequired[EcsPropertiesOverrideTypeDef],
    },
)
EksPropertiesUnionTypeDef = Union[EksPropertiesTypeDef, EksPropertiesOutputTypeDef]
JobDefinitionTypeDef = TypedDict(
    "JobDefinitionTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "type": str,
        "status": NotRequired[str],
        "schedulingPriority": NotRequired[int],
        "parameters": NotRequired[Dict[str, str]],
        "retryStrategy": NotRequired[RetryStrategyOutputTypeDef],
        "containerProperties": NotRequired[ContainerPropertiesOutputTypeDef],
        "timeout": NotRequired[JobTimeoutTypeDef],
        "nodeProperties": NotRequired[NodePropertiesOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "propagateTags": NotRequired[bool],
        "platformCapabilities": NotRequired[List[PlatformCapabilityType]],
        "ecsProperties": NotRequired[EcsPropertiesOutputTypeDef],
        "eksProperties": NotRequired[EksPropertiesOutputTypeDef],
        "containerOrchestrationType": NotRequired[OrchestrationTypeType],
    },
)
JobDetailTypeDef = TypedDict(
    "JobDetailTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": JobStatusType,
        "startedAt": int,
        "jobDefinition": str,
        "jobArn": NotRequired[str],
        "shareIdentifier": NotRequired[str],
        "schedulingPriority": NotRequired[int],
        "attempts": NotRequired[List[AttemptDetailTypeDef]],
        "statusReason": NotRequired[str],
        "createdAt": NotRequired[int],
        "retryStrategy": NotRequired[RetryStrategyOutputTypeDef],
        "stoppedAt": NotRequired[int],
        "dependsOn": NotRequired[List[JobDependencyTypeDef]],
        "parameters": NotRequired[Dict[str, str]],
        "container": NotRequired[ContainerDetailTypeDef],
        "nodeDetails": NotRequired[NodeDetailsTypeDef],
        "nodeProperties": NotRequired[NodePropertiesOutputTypeDef],
        "arrayProperties": NotRequired[ArrayPropertiesDetailTypeDef],
        "timeout": NotRequired[JobTimeoutTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "propagateTags": NotRequired[bool],
        "platformCapabilities": NotRequired[List[PlatformCapabilityType]],
        "eksProperties": NotRequired[EksPropertiesDetailTypeDef],
        "eksAttempts": NotRequired[List[EksAttemptDetailTypeDef]],
        "ecsProperties": NotRequired[EcsPropertiesDetailTypeDef],
        "isCancelled": NotRequired[bool],
        "isTerminated": NotRequired[bool],
    },
)
EcsTaskPropertiesUnionTypeDef = Union[EcsTaskPropertiesTypeDef, EcsTaskPropertiesOutputTypeDef]
DescribeJobDefinitionsResponseTypeDef = TypedDict(
    "DescribeJobDefinitionsResponseTypeDef",
    {
        "jobDefinitions": List[JobDefinitionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeJobsResponseTypeDef = TypedDict(
    "DescribeJobsResponseTypeDef",
    {
        "jobs": List[JobDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EcsPropertiesTypeDef = TypedDict(
    "EcsPropertiesTypeDef",
    {
        "taskProperties": Sequence[EcsTaskPropertiesUnionTypeDef],
    },
)
EcsPropertiesUnionTypeDef = Union[EcsPropertiesTypeDef, EcsPropertiesOutputTypeDef]
NodeRangePropertyTypeDef = TypedDict(
    "NodeRangePropertyTypeDef",
    {
        "targetNodes": str,
        "container": NotRequired[ContainerPropertiesUnionTypeDef],
        "instanceTypes": NotRequired[Sequence[str]],
        "ecsProperties": NotRequired[EcsPropertiesUnionTypeDef],
        "eksProperties": NotRequired[EksPropertiesUnionTypeDef],
    },
)
NodeRangePropertyUnionTypeDef = Union[NodeRangePropertyTypeDef, NodeRangePropertyOutputTypeDef]
NodePropertiesTypeDef = TypedDict(
    "NodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": Sequence[NodeRangePropertyUnionTypeDef],
    },
)
RegisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "RegisterJobDefinitionRequestRequestTypeDef",
    {
        "jobDefinitionName": str,
        "type": JobDefinitionTypeType,
        "parameters": NotRequired[Mapping[str, str]],
        "schedulingPriority": NotRequired[int],
        "containerProperties": NotRequired[ContainerPropertiesTypeDef],
        "nodeProperties": NotRequired[NodePropertiesTypeDef],
        "retryStrategy": NotRequired[RetryStrategyTypeDef],
        "propagateTags": NotRequired[bool],
        "timeout": NotRequired[JobTimeoutTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "platformCapabilities": NotRequired[Sequence[PlatformCapabilityType]],
        "eksProperties": NotRequired[EksPropertiesTypeDef],
        "ecsProperties": NotRequired[EcsPropertiesTypeDef],
    },
)
