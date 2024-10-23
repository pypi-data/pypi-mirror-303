"""
Type annotations for robomaker service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/type_defs/)

Usage::

    ```python
    from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsRequestRequestTypeDef

    data: BatchDeleteWorldsRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ArchitectureType,
    ComputeTypeType,
    DataSourceTypeType,
    DeploymentJobErrorCodeType,
    DeploymentStatusType,
    ExitBehaviorType,
    FailureBehaviorType,
    RobotDeploymentStepType,
    RobotSoftwareSuiteTypeType,
    RobotSoftwareSuiteVersionTypeType,
    RobotStatusType,
    SimulationJobBatchStatusType,
    SimulationJobErrorCodeType,
    SimulationJobStatusType,
    SimulationSoftwareSuiteTypeType,
    UploadBehaviorType,
    WorldExportJobErrorCodeType,
    WorldExportJobStatusType,
    WorldGenerationJobErrorCodeType,
    WorldGenerationJobStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BatchDeleteWorldsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDescribeSimulationJobRequestRequestTypeDef",
    "BatchPolicyTypeDef",
    "CancelDeploymentJobRequestRequestTypeDef",
    "CancelSimulationJobBatchRequestRequestTypeDef",
    "CancelSimulationJobRequestRequestTypeDef",
    "CancelWorldExportJobRequestRequestTypeDef",
    "CancelWorldGenerationJobRequestRequestTypeDef",
    "ComputeResponseTypeDef",
    "ComputeTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "EnvironmentTypeDef",
    "RobotSoftwareSuiteTypeDef",
    "SourceConfigTypeDef",
    "SourceTypeDef",
    "CreateRobotApplicationVersionRequestRequestTypeDef",
    "CreateRobotRequestRequestTypeDef",
    "RenderingEngineTypeDef",
    "SimulationSoftwareSuiteTypeDef",
    "CreateSimulationApplicationVersionRequestRequestTypeDef",
    "LoggingConfigTypeDef",
    "OutputLocationTypeDef",
    "VPCConfigTypeDef",
    "VPCConfigResponseTypeDef",
    "WorldCountTypeDef",
    "TemplateLocationTypeDef",
    "DataSourceConfigOutputTypeDef",
    "DataSourceConfigTypeDef",
    "S3KeyOutputTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteRobotApplicationRequestRequestTypeDef",
    "DeleteRobotRequestRequestTypeDef",
    "DeleteSimulationApplicationRequestRequestTypeDef",
    "DeleteWorldTemplateRequestRequestTypeDef",
    "DeploymentLaunchConfigOutputTypeDef",
    "S3ObjectTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "DeregisterRobotRequestRequestTypeDef",
    "DescribeDeploymentJobRequestRequestTypeDef",
    "DescribeFleetRequestRequestTypeDef",
    "RobotTypeDef",
    "DescribeRobotApplicationRequestRequestTypeDef",
    "DescribeRobotRequestRequestTypeDef",
    "DescribeSimulationApplicationRequestRequestTypeDef",
    "DescribeSimulationJobBatchRequestRequestTypeDef",
    "SimulationJobSummaryTypeDef",
    "DescribeSimulationJobRequestRequestTypeDef",
    "NetworkInterfaceTypeDef",
    "DescribeWorldExportJobRequestRequestTypeDef",
    "DescribeWorldGenerationJobRequestRequestTypeDef",
    "DescribeWorldRequestRequestTypeDef",
    "DescribeWorldTemplateRequestRequestTypeDef",
    "WorldFailureTypeDef",
    "FilterTypeDef",
    "FleetTypeDef",
    "GetWorldTemplateBodyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "SimulationJobBatchSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWorldTemplatesRequestRequestTypeDef",
    "TemplateSummaryTypeDef",
    "WorldSummaryTypeDef",
    "PortMappingTypeDef",
    "ProgressDetailTypeDef",
    "RegisterRobotRequestRequestTypeDef",
    "RestartSimulationJobRequestRequestTypeDef",
    "ToolTypeDef",
    "UploadConfigurationTypeDef",
    "WorldConfigTypeDef",
    "VPCConfigOutputTypeDef",
    "SyncDeploymentJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchDeleteWorldsResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateRobotResponseTypeDef",
    "CreateWorldTemplateResponseTypeDef",
    "DeregisterRobotResponseTypeDef",
    "DescribeRobotResponseTypeDef",
    "DescribeWorldResponseTypeDef",
    "DescribeWorldTemplateResponseTypeDef",
    "GetWorldTemplateBodyResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RegisterRobotResponseTypeDef",
    "UpdateWorldTemplateResponseTypeDef",
    "RobotApplicationSummaryTypeDef",
    "CreateRobotApplicationRequestRequestTypeDef",
    "UpdateRobotApplicationRequestRequestTypeDef",
    "CreateRobotApplicationResponseTypeDef",
    "CreateRobotApplicationVersionResponseTypeDef",
    "DescribeRobotApplicationResponseTypeDef",
    "UpdateRobotApplicationResponseTypeDef",
    "CreateSimulationApplicationRequestRequestTypeDef",
    "CreateSimulationApplicationResponseTypeDef",
    "CreateSimulationApplicationVersionResponseTypeDef",
    "DescribeSimulationApplicationResponseTypeDef",
    "SimulationApplicationSummaryTypeDef",
    "UpdateSimulationApplicationRequestRequestTypeDef",
    "UpdateSimulationApplicationResponseTypeDef",
    "CreateWorldExportJobRequestRequestTypeDef",
    "CreateWorldExportJobResponseTypeDef",
    "DescribeWorldExportJobResponseTypeDef",
    "WorldExportJobSummaryTypeDef",
    "CreateWorldGenerationJobRequestRequestTypeDef",
    "CreateWorldGenerationJobResponseTypeDef",
    "WorldGenerationJobSummaryTypeDef",
    "CreateWorldTemplateRequestRequestTypeDef",
    "UpdateWorldTemplateRequestRequestTypeDef",
    "DataSourceConfigUnionTypeDef",
    "DataSourceTypeDef",
    "DeploymentApplicationConfigOutputTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentLaunchConfigUnionTypeDef",
    "DescribeFleetResponseTypeDef",
    "ListRobotsResponseTypeDef",
    "ListSimulationJobsResponseTypeDef",
    "FailureSummaryTypeDef",
    "ListDeploymentJobsRequestRequestTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListRobotApplicationsRequestRequestTypeDef",
    "ListRobotsRequestRequestTypeDef",
    "ListSimulationApplicationsRequestRequestTypeDef",
    "ListSimulationJobBatchesRequestRequestTypeDef",
    "ListSimulationJobsRequestRequestTypeDef",
    "ListWorldExportJobsRequestRequestTypeDef",
    "ListWorldGenerationJobsRequestRequestTypeDef",
    "ListWorldsRequestRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListDeploymentJobsRequestListDeploymentJobsPaginateTypeDef",
    "ListFleetsRequestListFleetsPaginateTypeDef",
    "ListRobotApplicationsRequestListRobotApplicationsPaginateTypeDef",
    "ListRobotsRequestListRobotsPaginateTypeDef",
    "ListSimulationApplicationsRequestListSimulationApplicationsPaginateTypeDef",
    "ListSimulationJobBatchesRequestListSimulationJobBatchesPaginateTypeDef",
    "ListSimulationJobsRequestListSimulationJobsPaginateTypeDef",
    "ListWorldExportJobsRequestListWorldExportJobsPaginateTypeDef",
    "ListWorldGenerationJobsRequestListWorldGenerationJobsPaginateTypeDef",
    "ListWorldTemplatesRequestListWorldTemplatesPaginateTypeDef",
    "ListWorldsRequestListWorldsPaginateTypeDef",
    "ListSimulationJobBatchesResponseTypeDef",
    "ListWorldTemplatesResponseTypeDef",
    "ListWorldsResponseTypeDef",
    "PortForwardingConfigOutputTypeDef",
    "PortForwardingConfigTypeDef",
    "RobotDeploymentTypeDef",
    "VPCConfigUnionTypeDef",
    "ListRobotApplicationsResponseTypeDef",
    "ListSimulationApplicationsResponseTypeDef",
    "ListWorldExportJobsResponseTypeDef",
    "ListWorldGenerationJobsResponseTypeDef",
    "CreateDeploymentJobResponseTypeDef",
    "DeploymentJobTypeDef",
    "SyncDeploymentJobResponseTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "FinishedWorldsSummaryTypeDef",
    "LaunchConfigOutputTypeDef",
    "PortForwardingConfigUnionTypeDef",
    "DescribeDeploymentJobResponseTypeDef",
    "ListDeploymentJobsResponseTypeDef",
    "DeploymentApplicationConfigUnionTypeDef",
    "DescribeWorldGenerationJobResponseTypeDef",
    "RobotApplicationConfigOutputTypeDef",
    "SimulationApplicationConfigOutputTypeDef",
    "LaunchConfigTypeDef",
    "CreateDeploymentJobRequestRequestTypeDef",
    "CreateSimulationJobResponseTypeDef",
    "DescribeSimulationJobResponseTypeDef",
    "SimulationJobRequestOutputTypeDef",
    "SimulationJobTypeDef",
    "LaunchConfigUnionTypeDef",
    "FailedCreateSimulationJobRequestTypeDef",
    "BatchDescribeSimulationJobResponseTypeDef",
    "RobotApplicationConfigTypeDef",
    "SimulationApplicationConfigTypeDef",
    "DescribeSimulationJobBatchResponseTypeDef",
    "StartSimulationJobBatchResponseTypeDef",
    "RobotApplicationConfigUnionTypeDef",
    "SimulationApplicationConfigUnionTypeDef",
    "CreateSimulationJobRequestRequestTypeDef",
    "SimulationJobRequestTypeDef",
    "SimulationJobRequestUnionTypeDef",
    "StartSimulationJobBatchRequestRequestTypeDef",
)

BatchDeleteWorldsRequestRequestTypeDef = TypedDict(
    "BatchDeleteWorldsRequestRequestTypeDef",
    {
        "worlds": Sequence[str],
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
BatchDescribeSimulationJobRequestRequestTypeDef = TypedDict(
    "BatchDescribeSimulationJobRequestRequestTypeDef",
    {
        "jobs": Sequence[str],
    },
)
BatchPolicyTypeDef = TypedDict(
    "BatchPolicyTypeDef",
    {
        "timeoutInSeconds": NotRequired[int],
        "maxConcurrency": NotRequired[int],
    },
)
CancelDeploymentJobRequestRequestTypeDef = TypedDict(
    "CancelDeploymentJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
CancelSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "CancelSimulationJobBatchRequestRequestTypeDef",
    {
        "batch": str,
    },
)
CancelSimulationJobRequestRequestTypeDef = TypedDict(
    "CancelSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
CancelWorldExportJobRequestRequestTypeDef = TypedDict(
    "CancelWorldExportJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
CancelWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "CancelWorldGenerationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
ComputeResponseTypeDef = TypedDict(
    "ComputeResponseTypeDef",
    {
        "simulationUnitLimit": NotRequired[int],
        "computeType": NotRequired[ComputeTypeType],
        "gpuUnitLimit": NotRequired[int],
    },
)
ComputeTypeDef = TypedDict(
    "ComputeTypeDef",
    {
        "simulationUnitLimit": NotRequired[int],
        "computeType": NotRequired[ComputeTypeType],
        "gpuUnitLimit": NotRequired[int],
    },
)
CreateFleetRequestRequestTypeDef = TypedDict(
    "CreateFleetRequestRequestTypeDef",
    {
        "name": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "uri": NotRequired[str],
    },
)
RobotSoftwareSuiteTypeDef = TypedDict(
    "RobotSoftwareSuiteTypeDef",
    {
        "name": NotRequired[RobotSoftwareSuiteTypeType],
        "version": NotRequired[RobotSoftwareSuiteVersionTypeType],
    },
)
SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3Key": NotRequired[str],
        "architecture": NotRequired[ArchitectureType],
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3Key": NotRequired[str],
        "etag": NotRequired[str],
        "architecture": NotRequired[ArchitectureType],
    },
)
CreateRobotApplicationVersionRequestRequestTypeDef = TypedDict(
    "CreateRobotApplicationVersionRequestRequestTypeDef",
    {
        "application": str,
        "currentRevisionId": NotRequired[str],
        "s3Etags": NotRequired[Sequence[str]],
        "imageDigest": NotRequired[str],
    },
)
CreateRobotRequestRequestTypeDef = TypedDict(
    "CreateRobotRequestRequestTypeDef",
    {
        "name": str,
        "architecture": ArchitectureType,
        "greengrassGroupId": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
RenderingEngineTypeDef = TypedDict(
    "RenderingEngineTypeDef",
    {
        "name": NotRequired[Literal["OGRE"]],
        "version": NotRequired[str],
    },
)
SimulationSoftwareSuiteTypeDef = TypedDict(
    "SimulationSoftwareSuiteTypeDef",
    {
        "name": NotRequired[SimulationSoftwareSuiteTypeType],
        "version": NotRequired[str],
    },
)
CreateSimulationApplicationVersionRequestRequestTypeDef = TypedDict(
    "CreateSimulationApplicationVersionRequestRequestTypeDef",
    {
        "application": str,
        "currentRevisionId": NotRequired[str],
        "s3Etags": NotRequired[Sequence[str]],
        "imageDigest": NotRequired[str],
    },
)
LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "recordAllRosTopics": NotRequired[bool],
    },
)
OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3Prefix": NotRequired[str],
    },
)
VPCConfigTypeDef = TypedDict(
    "VPCConfigTypeDef",
    {
        "subnets": Sequence[str],
        "securityGroups": NotRequired[Sequence[str]],
        "assignPublicIp": NotRequired[bool],
    },
)
VPCConfigResponseTypeDef = TypedDict(
    "VPCConfigResponseTypeDef",
    {
        "subnets": NotRequired[List[str]],
        "securityGroups": NotRequired[List[str]],
        "vpcId": NotRequired[str],
        "assignPublicIp": NotRequired[bool],
    },
)
WorldCountTypeDef = TypedDict(
    "WorldCountTypeDef",
    {
        "floorplanCount": NotRequired[int],
        "interiorCountPerFloorplan": NotRequired[int],
    },
)
TemplateLocationTypeDef = TypedDict(
    "TemplateLocationTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
    },
)
DataSourceConfigOutputTypeDef = TypedDict(
    "DataSourceConfigOutputTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[str],
        "type": NotRequired[DataSourceTypeType],
        "destination": NotRequired[str],
    },
)
DataSourceConfigTypeDef = TypedDict(
    "DataSourceConfigTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": Sequence[str],
        "type": NotRequired[DataSourceTypeType],
        "destination": NotRequired[str],
    },
)
S3KeyOutputTypeDef = TypedDict(
    "S3KeyOutputTypeDef",
    {
        "s3Key": NotRequired[str],
        "etag": NotRequired[str],
    },
)
DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "fleet": str,
    },
)
DeleteRobotApplicationRequestRequestTypeDef = TypedDict(
    "DeleteRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
        "applicationVersion": NotRequired[str],
    },
)
DeleteRobotRequestRequestTypeDef = TypedDict(
    "DeleteRobotRequestRequestTypeDef",
    {
        "robot": str,
    },
)
DeleteSimulationApplicationRequestRequestTypeDef = TypedDict(
    "DeleteSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
        "applicationVersion": NotRequired[str],
    },
)
DeleteWorldTemplateRequestRequestTypeDef = TypedDict(
    "DeleteWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
    },
)
DeploymentLaunchConfigOutputTypeDef = TypedDict(
    "DeploymentLaunchConfigOutputTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "preLaunchFile": NotRequired[str],
        "postLaunchFile": NotRequired[str],
        "environmentVariables": NotRequired[Dict[str, str]],
    },
)
S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucket": str,
        "key": str,
        "etag": NotRequired[str],
    },
)
DeploymentLaunchConfigTypeDef = TypedDict(
    "DeploymentLaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "preLaunchFile": NotRequired[str],
        "postLaunchFile": NotRequired[str],
        "environmentVariables": NotRequired[Mapping[str, str]],
    },
)
DeregisterRobotRequestRequestTypeDef = TypedDict(
    "DeregisterRobotRequestRequestTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
)
DescribeDeploymentJobRequestRequestTypeDef = TypedDict(
    "DescribeDeploymentJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
DescribeFleetRequestRequestTypeDef = TypedDict(
    "DescribeFleetRequestRequestTypeDef",
    {
        "fleet": str,
    },
)
RobotTypeDef = TypedDict(
    "RobotTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "fleetArn": NotRequired[str],
        "status": NotRequired[RobotStatusType],
        "greenGrassGroupId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "architecture": NotRequired[ArchitectureType],
        "lastDeploymentJob": NotRequired[str],
        "lastDeploymentTime": NotRequired[datetime],
    },
)
DescribeRobotApplicationRequestRequestTypeDef = TypedDict(
    "DescribeRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
        "applicationVersion": NotRequired[str],
    },
)
DescribeRobotRequestRequestTypeDef = TypedDict(
    "DescribeRobotRequestRequestTypeDef",
    {
        "robot": str,
    },
)
DescribeSimulationApplicationRequestRequestTypeDef = TypedDict(
    "DescribeSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
        "applicationVersion": NotRequired[str],
    },
)
DescribeSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "DescribeSimulationJobBatchRequestRequestTypeDef",
    {
        "batch": str,
    },
)
SimulationJobSummaryTypeDef = TypedDict(
    "SimulationJobSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "status": NotRequired[SimulationJobStatusType],
        "simulationApplicationNames": NotRequired[List[str]],
        "robotApplicationNames": NotRequired[List[str]],
        "dataSourceNames": NotRequired[List[str]],
        "computeType": NotRequired[ComputeTypeType],
    },
)
DescribeSimulationJobRequestRequestTypeDef = TypedDict(
    "DescribeSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": NotRequired[str],
        "privateIpAddress": NotRequired[str],
        "publicIpAddress": NotRequired[str],
    },
)
DescribeWorldExportJobRequestRequestTypeDef = TypedDict(
    "DescribeWorldExportJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
DescribeWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "DescribeWorldGenerationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
DescribeWorldRequestRequestTypeDef = TypedDict(
    "DescribeWorldRequestRequestTypeDef",
    {
        "world": str,
    },
)
DescribeWorldTemplateRequestRequestTypeDef = TypedDict(
    "DescribeWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
    },
)
WorldFailureTypeDef = TypedDict(
    "WorldFailureTypeDef",
    {
        "failureCode": NotRequired[WorldGenerationJobErrorCodeType],
        "sampleFailureReason": NotRequired[str],
        "failureCount": NotRequired[int],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastDeploymentStatus": NotRequired[DeploymentStatusType],
        "lastDeploymentJob": NotRequired[str],
        "lastDeploymentTime": NotRequired[datetime],
    },
)
GetWorldTemplateBodyRequestRequestTypeDef = TypedDict(
    "GetWorldTemplateBodyRequestRequestTypeDef",
    {
        "template": NotRequired[str],
        "generationJob": NotRequired[str],
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
SimulationJobBatchSummaryTypeDef = TypedDict(
    "SimulationJobBatchSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "createdAt": NotRequired[datetime],
        "status": NotRequired[SimulationJobBatchStatusType],
        "failedRequestCount": NotRequired[int],
        "pendingRequestCount": NotRequired[int],
        "createdRequestCount": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListWorldTemplatesRequestRequestTypeDef = TypedDict(
    "ListWorldTemplatesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "version": NotRequired[str],
    },
)
WorldSummaryTypeDef = TypedDict(
    "WorldSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "generationJob": NotRequired[str],
        "template": NotRequired[str],
    },
)
PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "jobPort": int,
        "applicationPort": int,
        "enableOnPublicIp": NotRequired[bool],
    },
)
ProgressDetailTypeDef = TypedDict(
    "ProgressDetailTypeDef",
    {
        "currentProgress": NotRequired[RobotDeploymentStepType],
        "percentDone": NotRequired[float],
        "estimatedTimeRemainingSeconds": NotRequired[int],
        "targetResource": NotRequired[str],
    },
)
RegisterRobotRequestRequestTypeDef = TypedDict(
    "RegisterRobotRequestRequestTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
)
RestartSimulationJobRequestRequestTypeDef = TypedDict(
    "RestartSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)
ToolTypeDef = TypedDict(
    "ToolTypeDef",
    {
        "name": str,
        "command": str,
        "streamUI": NotRequired[bool],
        "streamOutputToCloudWatch": NotRequired[bool],
        "exitBehavior": NotRequired[ExitBehaviorType],
    },
)
UploadConfigurationTypeDef = TypedDict(
    "UploadConfigurationTypeDef",
    {
        "name": str,
        "path": str,
        "uploadBehavior": UploadBehaviorType,
    },
)
WorldConfigTypeDef = TypedDict(
    "WorldConfigTypeDef",
    {
        "world": NotRequired[str],
    },
)
VPCConfigOutputTypeDef = TypedDict(
    "VPCConfigOutputTypeDef",
    {
        "subnets": List[str],
        "securityGroups": NotRequired[List[str]],
        "assignPublicIp": NotRequired[bool],
    },
)
SyncDeploymentJobRequestRequestTypeDef = TypedDict(
    "SyncDeploymentJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "fleet": str,
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
BatchDeleteWorldsResponseTypeDef = TypedDict(
    "BatchDeleteWorldsResponseTypeDef",
    {
        "unprocessedWorlds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRobotResponseTypeDef = TypedDict(
    "CreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": ArchitectureType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorldTemplateResponseTypeDef = TypedDict(
    "CreateWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "createdAt": datetime,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterRobotResponseTypeDef = TypedDict(
    "DeregisterRobotResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRobotResponseTypeDef = TypedDict(
    "DescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": RobotStatusType,
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": ArchitectureType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorldResponseTypeDef = TypedDict(
    "DescribeWorldResponseTypeDef",
    {
        "arn": str,
        "generationJob": str,
        "template": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
        "worldDescriptionBody": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorldTemplateResponseTypeDef = TypedDict(
    "DescribeWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorldTemplateBodyResponseTypeDef = TypedDict(
    "GetWorldTemplateBodyResponseTypeDef",
    {
        "templateBody": str,
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
RegisterRobotResponseTypeDef = TypedDict(
    "RegisterRobotResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorldTemplateResponseTypeDef = TypedDict(
    "UpdateWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RobotApplicationSummaryTypeDef = TypedDict(
    "RobotApplicationSummaryTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "version": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "robotSoftwareSuite": NotRequired[RobotSoftwareSuiteTypeDef],
    },
)
CreateRobotApplicationRequestRequestTypeDef = TypedDict(
    "CreateRobotApplicationRequestRequestTypeDef",
    {
        "name": str,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "sources": NotRequired[Sequence[SourceConfigTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "environment": NotRequired[EnvironmentTypeDef],
    },
)
UpdateRobotApplicationRequestRequestTypeDef = TypedDict(
    "UpdateRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "sources": NotRequired[Sequence[SourceConfigTypeDef]],
        "currentRevisionId": NotRequired[str],
        "environment": NotRequired[EnvironmentTypeDef],
    },
)
CreateRobotApplicationResponseTypeDef = TypedDict(
    "CreateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRobotApplicationVersionResponseTypeDef = TypedDict(
    "CreateRobotApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRobotApplicationResponseTypeDef = TypedDict(
    "DescribeRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
        "environment": EnvironmentTypeDef,
        "imageDigest": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRobotApplicationResponseTypeDef = TypedDict(
    "UpdateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSimulationApplicationRequestRequestTypeDef = TypedDict(
    "CreateSimulationApplicationRequestRequestTypeDef",
    {
        "name": str,
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "sources": NotRequired[Sequence[SourceConfigTypeDef]],
        "renderingEngine": NotRequired[RenderingEngineTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "environment": NotRequired[EnvironmentTypeDef],
    },
)
CreateSimulationApplicationResponseTypeDef = TypedDict(
    "CreateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "renderingEngine": RenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSimulationApplicationVersionResponseTypeDef = TypedDict(
    "CreateSimulationApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "renderingEngine": RenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSimulationApplicationResponseTypeDef = TypedDict(
    "DescribeSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "renderingEngine": RenderingEngineTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
        "environment": EnvironmentTypeDef,
        "imageDigest": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SimulationApplicationSummaryTypeDef = TypedDict(
    "SimulationApplicationSummaryTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "version": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "robotSoftwareSuite": NotRequired[RobotSoftwareSuiteTypeDef],
        "simulationSoftwareSuite": NotRequired[SimulationSoftwareSuiteTypeDef],
    },
)
UpdateSimulationApplicationRequestRequestTypeDef = TypedDict(
    "UpdateSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "sources": NotRequired[Sequence[SourceConfigTypeDef]],
        "renderingEngine": NotRequired[RenderingEngineTypeDef],
        "currentRevisionId": NotRequired[str],
        "environment": NotRequired[EnvironmentTypeDef],
    },
)
UpdateSimulationApplicationResponseTypeDef = TypedDict(
    "UpdateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "renderingEngine": RenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorldExportJobRequestRequestTypeDef = TypedDict(
    "CreateWorldExportJobRequestRequestTypeDef",
    {
        "worlds": Sequence[str],
        "outputLocation": OutputLocationTypeDef,
        "iamRole": str,
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateWorldExportJobResponseTypeDef = TypedDict(
    "CreateWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "clientRequestToken": str,
        "outputLocation": OutputLocationTypeDef,
        "iamRole": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorldExportJobResponseTypeDef = TypedDict(
    "DescribeWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "worlds": List[str],
        "outputLocation": OutputLocationTypeDef,
        "iamRole": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorldExportJobSummaryTypeDef = TypedDict(
    "WorldExportJobSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "status": NotRequired[WorldExportJobStatusType],
        "createdAt": NotRequired[datetime],
        "worlds": NotRequired[List[str]],
        "outputLocation": NotRequired[OutputLocationTypeDef],
    },
)
CreateWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "CreateWorldGenerationJobRequestRequestTypeDef",
    {
        "template": str,
        "worldCount": WorldCountTypeDef,
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "worldTags": NotRequired[Mapping[str, str]],
    },
)
CreateWorldGenerationJobResponseTypeDef = TypedDict(
    "CreateWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldGenerationJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldGenerationJobErrorCodeType,
        "clientRequestToken": str,
        "template": str,
        "worldCount": WorldCountTypeDef,
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorldGenerationJobSummaryTypeDef = TypedDict(
    "WorldGenerationJobSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "template": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "status": NotRequired[WorldGenerationJobStatusType],
        "worldCount": NotRequired[WorldCountTypeDef],
        "succeededWorldCount": NotRequired[int],
        "failedWorldCount": NotRequired[int],
    },
)
CreateWorldTemplateRequestRequestTypeDef = TypedDict(
    "CreateWorldTemplateRequestRequestTypeDef",
    {
        "clientRequestToken": NotRequired[str],
        "name": NotRequired[str],
        "templateBody": NotRequired[str],
        "templateLocation": NotRequired[TemplateLocationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateWorldTemplateRequestRequestTypeDef = TypedDict(
    "UpdateWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
        "name": NotRequired[str],
        "templateBody": NotRequired[str],
        "templateLocation": NotRequired[TemplateLocationTypeDef],
    },
)
DataSourceConfigUnionTypeDef = Union[DataSourceConfigTypeDef, DataSourceConfigOutputTypeDef]
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "name": NotRequired[str],
        "s3Bucket": NotRequired[str],
        "s3Keys": NotRequired[List[S3KeyOutputTypeDef]],
        "type": NotRequired[DataSourceTypeType],
        "destination": NotRequired[str],
    },
)
DeploymentApplicationConfigOutputTypeDef = TypedDict(
    "DeploymentApplicationConfigOutputTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": DeploymentLaunchConfigOutputTypeDef,
    },
)
DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": NotRequired[int],
        "failureThresholdPercentage": NotRequired[int],
        "robotDeploymentTimeoutInSeconds": NotRequired[int],
        "downloadConditionFile": NotRequired[S3ObjectTypeDef],
    },
)
DeploymentLaunchConfigUnionTypeDef = Union[
    DeploymentLaunchConfigTypeDef, DeploymentLaunchConfigOutputTypeDef
]
DescribeFleetResponseTypeDef = TypedDict(
    "DescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List[RobotTypeDef],
        "createdAt": datetime,
        "lastDeploymentStatus": DeploymentStatusType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRobotsResponseTypeDef = TypedDict(
    "ListRobotsResponseTypeDef",
    {
        "robots": List[RobotTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSimulationJobsResponseTypeDef = TypedDict(
    "ListSimulationJobsResponseTypeDef",
    {
        "simulationJobSummaries": List[SimulationJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailureSummaryTypeDef = TypedDict(
    "FailureSummaryTypeDef",
    {
        "totalFailureCount": NotRequired[int],
        "failures": NotRequired[List[WorldFailureTypeDef]],
    },
)
ListDeploymentJobsRequestRequestTypeDef = TypedDict(
    "ListDeploymentJobsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListRobotApplicationsRequestRequestTypeDef = TypedDict(
    "ListRobotApplicationsRequestRequestTypeDef",
    {
        "versionQualifier": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListRobotsRequestRequestTypeDef = TypedDict(
    "ListRobotsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListSimulationApplicationsRequestRequestTypeDef = TypedDict(
    "ListSimulationApplicationsRequestRequestTypeDef",
    {
        "versionQualifier": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListSimulationJobBatchesRequestRequestTypeDef = TypedDict(
    "ListSimulationJobBatchesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListSimulationJobsRequestRequestTypeDef = TypedDict(
    "ListSimulationJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListWorldExportJobsRequestRequestTypeDef = TypedDict(
    "ListWorldExportJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListWorldGenerationJobsRequestRequestTypeDef = TypedDict(
    "ListWorldGenerationJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListWorldsRequestRequestTypeDef = TypedDict(
    "ListWorldsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleetDetails": List[FleetTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentJobsRequestListDeploymentJobsPaginateTypeDef = TypedDict(
    "ListDeploymentJobsRequestListDeploymentJobsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFleetsRequestListFleetsPaginateTypeDef = TypedDict(
    "ListFleetsRequestListFleetsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRobotApplicationsRequestListRobotApplicationsPaginateTypeDef = TypedDict(
    "ListRobotApplicationsRequestListRobotApplicationsPaginateTypeDef",
    {
        "versionQualifier": NotRequired[str],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRobotsRequestListRobotsPaginateTypeDef = TypedDict(
    "ListRobotsRequestListRobotsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSimulationApplicationsRequestListSimulationApplicationsPaginateTypeDef = TypedDict(
    "ListSimulationApplicationsRequestListSimulationApplicationsPaginateTypeDef",
    {
        "versionQualifier": NotRequired[str],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSimulationJobBatchesRequestListSimulationJobBatchesPaginateTypeDef = TypedDict(
    "ListSimulationJobBatchesRequestListSimulationJobBatchesPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSimulationJobsRequestListSimulationJobsPaginateTypeDef = TypedDict(
    "ListSimulationJobsRequestListSimulationJobsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorldExportJobsRequestListWorldExportJobsPaginateTypeDef = TypedDict(
    "ListWorldExportJobsRequestListWorldExportJobsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorldGenerationJobsRequestListWorldGenerationJobsPaginateTypeDef = TypedDict(
    "ListWorldGenerationJobsRequestListWorldGenerationJobsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorldTemplatesRequestListWorldTemplatesPaginateTypeDef = TypedDict(
    "ListWorldTemplatesRequestListWorldTemplatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorldsRequestListWorldsPaginateTypeDef = TypedDict(
    "ListWorldsRequestListWorldsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSimulationJobBatchesResponseTypeDef = TypedDict(
    "ListSimulationJobBatchesResponseTypeDef",
    {
        "simulationJobBatchSummaries": List[SimulationJobBatchSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorldTemplatesResponseTypeDef = TypedDict(
    "ListWorldTemplatesResponseTypeDef",
    {
        "templateSummaries": List[TemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorldsResponseTypeDef = TypedDict(
    "ListWorldsResponseTypeDef",
    {
        "worldSummaries": List[WorldSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PortForwardingConfigOutputTypeDef = TypedDict(
    "PortForwardingConfigOutputTypeDef",
    {
        "portMappings": NotRequired[List[PortMappingTypeDef]],
    },
)
PortForwardingConfigTypeDef = TypedDict(
    "PortForwardingConfigTypeDef",
    {
        "portMappings": NotRequired[Sequence[PortMappingTypeDef]],
    },
)
RobotDeploymentTypeDef = TypedDict(
    "RobotDeploymentTypeDef",
    {
        "arn": NotRequired[str],
        "deploymentStartTime": NotRequired[datetime],
        "deploymentFinishTime": NotRequired[datetime],
        "status": NotRequired[RobotStatusType],
        "progressDetail": NotRequired[ProgressDetailTypeDef],
        "failureReason": NotRequired[str],
        "failureCode": NotRequired[DeploymentJobErrorCodeType],
    },
)
VPCConfigUnionTypeDef = Union[VPCConfigTypeDef, VPCConfigOutputTypeDef]
ListRobotApplicationsResponseTypeDef = TypedDict(
    "ListRobotApplicationsResponseTypeDef",
    {
        "robotApplicationSummaries": List[RobotApplicationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSimulationApplicationsResponseTypeDef = TypedDict(
    "ListSimulationApplicationsResponseTypeDef",
    {
        "simulationApplicationSummaries": List[SimulationApplicationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorldExportJobsResponseTypeDef = TypedDict(
    "ListWorldExportJobsResponseTypeDef",
    {
        "worldExportJobSummaries": List[WorldExportJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorldGenerationJobsResponseTypeDef = TypedDict(
    "ListWorldGenerationJobsResponseTypeDef",
    {
        "worldGenerationJobSummaries": List[WorldGenerationJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentJobResponseTypeDef = TypedDict(
    "CreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentApplicationConfigs": List[DeploymentApplicationConfigOutputTypeDef],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "deploymentConfig": DeploymentConfigTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentJobTypeDef = TypedDict(
    "DeploymentJobTypeDef",
    {
        "arn": NotRequired[str],
        "fleet": NotRequired[str],
        "status": NotRequired[DeploymentStatusType],
        "deploymentApplicationConfigs": NotRequired[List[DeploymentApplicationConfigOutputTypeDef]],
        "deploymentConfig": NotRequired[DeploymentConfigTypeDef],
        "failureReason": NotRequired[str],
        "failureCode": NotRequired[DeploymentJobErrorCodeType],
        "createdAt": NotRequired[datetime],
    },
)
SyncDeploymentJobResponseTypeDef = TypedDict(
    "SyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": DeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[DeploymentApplicationConfigOutputTypeDef],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentApplicationConfigTypeDef = TypedDict(
    "DeploymentApplicationConfigTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": DeploymentLaunchConfigUnionTypeDef,
    },
)
FinishedWorldsSummaryTypeDef = TypedDict(
    "FinishedWorldsSummaryTypeDef",
    {
        "finishedCount": NotRequired[int],
        "succeededWorlds": NotRequired[List[str]],
        "failureSummary": NotRequired[FailureSummaryTypeDef],
    },
)
LaunchConfigOutputTypeDef = TypedDict(
    "LaunchConfigOutputTypeDef",
    {
        "packageName": NotRequired[str],
        "launchFile": NotRequired[str],
        "environmentVariables": NotRequired[Dict[str, str]],
        "portForwardingConfig": NotRequired[PortForwardingConfigOutputTypeDef],
        "streamUI": NotRequired[bool],
        "command": NotRequired[List[str]],
    },
)
PortForwardingConfigUnionTypeDef = Union[
    PortForwardingConfigTypeDef, PortForwardingConfigOutputTypeDef
]
DescribeDeploymentJobResponseTypeDef = TypedDict(
    "DescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": DeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[DeploymentApplicationConfigOutputTypeDef],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "robotDeploymentSummary": List[RobotDeploymentTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentJobsResponseTypeDef = TypedDict(
    "ListDeploymentJobsResponseTypeDef",
    {
        "deploymentJobs": List[DeploymentJobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentApplicationConfigUnionTypeDef = Union[
    DeploymentApplicationConfigTypeDef, DeploymentApplicationConfigOutputTypeDef
]
DescribeWorldGenerationJobResponseTypeDef = TypedDict(
    "DescribeWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldGenerationJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldGenerationJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "template": str,
        "worldCount": WorldCountTypeDef,
        "finishedWorldsSummary": FinishedWorldsSummaryTypeDef,
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RobotApplicationConfigOutputTypeDef = TypedDict(
    "RobotApplicationConfigOutputTypeDef",
    {
        "application": str,
        "launchConfig": LaunchConfigOutputTypeDef,
        "applicationVersion": NotRequired[str],
        "uploadConfigurations": NotRequired[List[UploadConfigurationTypeDef]],
        "useDefaultUploadConfigurations": NotRequired[bool],
        "tools": NotRequired[List[ToolTypeDef]],
        "useDefaultTools": NotRequired[bool],
    },
)
SimulationApplicationConfigOutputTypeDef = TypedDict(
    "SimulationApplicationConfigOutputTypeDef",
    {
        "application": str,
        "launchConfig": LaunchConfigOutputTypeDef,
        "applicationVersion": NotRequired[str],
        "uploadConfigurations": NotRequired[List[UploadConfigurationTypeDef]],
        "worldConfigs": NotRequired[List[WorldConfigTypeDef]],
        "useDefaultUploadConfigurations": NotRequired[bool],
        "tools": NotRequired[List[ToolTypeDef]],
        "useDefaultTools": NotRequired[bool],
    },
)
LaunchConfigTypeDef = TypedDict(
    "LaunchConfigTypeDef",
    {
        "packageName": NotRequired[str],
        "launchFile": NotRequired[str],
        "environmentVariables": NotRequired[Mapping[str, str]],
        "portForwardingConfig": NotRequired[PortForwardingConfigUnionTypeDef],
        "streamUI": NotRequired[bool],
        "command": NotRequired[Sequence[str]],
    },
)
CreateDeploymentJobRequestRequestTypeDef = TypedDict(
    "CreateDeploymentJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "fleet": str,
        "deploymentApplicationConfigs": Sequence[DeploymentApplicationConfigUnionTypeDef],
        "deploymentConfig": NotRequired[DeploymentConfigTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateSimulationJobResponseTypeDef = TypedDict(
    "CreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
        "clientRequestToken": str,
        "outputLocation": OutputLocationTypeDef,
        "loggingConfig": LoggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[RobotApplicationConfigOutputTypeDef],
        "simulationApplications": List[SimulationApplicationConfigOutputTypeDef],
        "dataSources": List[DataSourceTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": VPCConfigResponseTypeDef,
        "compute": ComputeResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSimulationJobResponseTypeDef = TypedDict(
    "DescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": OutputLocationTypeDef,
        "loggingConfig": LoggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[RobotApplicationConfigOutputTypeDef],
        "simulationApplications": List[SimulationApplicationConfigOutputTypeDef],
        "dataSources": List[DataSourceTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": VPCConfigResponseTypeDef,
        "networkInterface": NetworkInterfaceTypeDef,
        "compute": ComputeResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SimulationJobRequestOutputTypeDef = TypedDict(
    "SimulationJobRequestOutputTypeDef",
    {
        "maxJobDurationInSeconds": int,
        "outputLocation": NotRequired[OutputLocationTypeDef],
        "loggingConfig": NotRequired[LoggingConfigTypeDef],
        "iamRole": NotRequired[str],
        "failureBehavior": NotRequired[FailureBehaviorType],
        "useDefaultApplications": NotRequired[bool],
        "robotApplications": NotRequired[List[RobotApplicationConfigOutputTypeDef]],
        "simulationApplications": NotRequired[List[SimulationApplicationConfigOutputTypeDef]],
        "dataSources": NotRequired[List[DataSourceConfigOutputTypeDef]],
        "vpcConfig": NotRequired[VPCConfigOutputTypeDef],
        "compute": NotRequired[ComputeTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
SimulationJobTypeDef = TypedDict(
    "SimulationJobTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[SimulationJobStatusType],
        "lastStartedAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "failureBehavior": NotRequired[FailureBehaviorType],
        "failureCode": NotRequired[SimulationJobErrorCodeType],
        "failureReason": NotRequired[str],
        "clientRequestToken": NotRequired[str],
        "outputLocation": NotRequired[OutputLocationTypeDef],
        "loggingConfig": NotRequired[LoggingConfigTypeDef],
        "maxJobDurationInSeconds": NotRequired[int],
        "simulationTimeMillis": NotRequired[int],
        "iamRole": NotRequired[str],
        "robotApplications": NotRequired[List[RobotApplicationConfigOutputTypeDef]],
        "simulationApplications": NotRequired[List[SimulationApplicationConfigOutputTypeDef]],
        "dataSources": NotRequired[List[DataSourceTypeDef]],
        "tags": NotRequired[Dict[str, str]],
        "vpcConfig": NotRequired[VPCConfigResponseTypeDef],
        "networkInterface": NotRequired[NetworkInterfaceTypeDef],
        "compute": NotRequired[ComputeResponseTypeDef],
    },
)
LaunchConfigUnionTypeDef = Union[LaunchConfigTypeDef, LaunchConfigOutputTypeDef]
FailedCreateSimulationJobRequestTypeDef = TypedDict(
    "FailedCreateSimulationJobRequestTypeDef",
    {
        "request": NotRequired[SimulationJobRequestOutputTypeDef],
        "failureReason": NotRequired[str],
        "failureCode": NotRequired[SimulationJobErrorCodeType],
        "failedAt": NotRequired[datetime],
    },
)
BatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "BatchDescribeSimulationJobResponseTypeDef",
    {
        "jobs": List[SimulationJobTypeDef],
        "unprocessedJobs": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RobotApplicationConfigTypeDef = TypedDict(
    "RobotApplicationConfigTypeDef",
    {
        "application": str,
        "launchConfig": LaunchConfigUnionTypeDef,
        "applicationVersion": NotRequired[str],
        "uploadConfigurations": NotRequired[Sequence[UploadConfigurationTypeDef]],
        "useDefaultUploadConfigurations": NotRequired[bool],
        "tools": NotRequired[Sequence[ToolTypeDef]],
        "useDefaultTools": NotRequired[bool],
    },
)
SimulationApplicationConfigTypeDef = TypedDict(
    "SimulationApplicationConfigTypeDef",
    {
        "application": str,
        "launchConfig": LaunchConfigUnionTypeDef,
        "applicationVersion": NotRequired[str],
        "uploadConfigurations": NotRequired[Sequence[UploadConfigurationTypeDef]],
        "worldConfigs": NotRequired[Sequence[WorldConfigTypeDef]],
        "useDefaultUploadConfigurations": NotRequired[bool],
        "tools": NotRequired[Sequence[ToolTypeDef]],
        "useDefaultTools": NotRequired[bool],
    },
)
DescribeSimulationJobBatchResponseTypeDef = TypedDict(
    "DescribeSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobBatchStatusType,
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": BatchPolicyTypeDef,
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List[FailedCreateSimulationJobRequestTypeDef],
        "pendingRequests": List[SimulationJobRequestOutputTypeDef],
        "createdRequests": List[SimulationJobSummaryTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSimulationJobBatchResponseTypeDef = TypedDict(
    "StartSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobBatchStatusType,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": BatchPolicyTypeDef,
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List[FailedCreateSimulationJobRequestTypeDef],
        "pendingRequests": List[SimulationJobRequestOutputTypeDef],
        "createdRequests": List[SimulationJobSummaryTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RobotApplicationConfigUnionTypeDef = Union[
    RobotApplicationConfigTypeDef, RobotApplicationConfigOutputTypeDef
]
SimulationApplicationConfigUnionTypeDef = Union[
    SimulationApplicationConfigTypeDef, SimulationApplicationConfigOutputTypeDef
]
CreateSimulationJobRequestRequestTypeDef = TypedDict(
    "CreateSimulationJobRequestRequestTypeDef",
    {
        "maxJobDurationInSeconds": int,
        "iamRole": str,
        "clientRequestToken": NotRequired[str],
        "outputLocation": NotRequired[OutputLocationTypeDef],
        "loggingConfig": NotRequired[LoggingConfigTypeDef],
        "failureBehavior": NotRequired[FailureBehaviorType],
        "robotApplications": NotRequired[Sequence[RobotApplicationConfigUnionTypeDef]],
        "simulationApplications": NotRequired[Sequence[SimulationApplicationConfigUnionTypeDef]],
        "dataSources": NotRequired[Sequence[DataSourceConfigUnionTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "vpcConfig": NotRequired[VPCConfigTypeDef],
        "compute": NotRequired[ComputeTypeDef],
    },
)
SimulationJobRequestTypeDef = TypedDict(
    "SimulationJobRequestTypeDef",
    {
        "maxJobDurationInSeconds": int,
        "outputLocation": NotRequired[OutputLocationTypeDef],
        "loggingConfig": NotRequired[LoggingConfigTypeDef],
        "iamRole": NotRequired[str],
        "failureBehavior": NotRequired[FailureBehaviorType],
        "useDefaultApplications": NotRequired[bool],
        "robotApplications": NotRequired[Sequence[RobotApplicationConfigUnionTypeDef]],
        "simulationApplications": NotRequired[Sequence[SimulationApplicationConfigUnionTypeDef]],
        "dataSources": NotRequired[Sequence[DataSourceConfigUnionTypeDef]],
        "vpcConfig": NotRequired[VPCConfigUnionTypeDef],
        "compute": NotRequired[ComputeTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
SimulationJobRequestUnionTypeDef = Union[
    SimulationJobRequestTypeDef, SimulationJobRequestOutputTypeDef
]
StartSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "StartSimulationJobBatchRequestRequestTypeDef",
    {
        "createSimulationJobRequests": Sequence[SimulationJobRequestUnionTypeDef],
        "clientRequestToken": NotRequired[str],
        "batchPolicy": NotRequired[BatchPolicyTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
