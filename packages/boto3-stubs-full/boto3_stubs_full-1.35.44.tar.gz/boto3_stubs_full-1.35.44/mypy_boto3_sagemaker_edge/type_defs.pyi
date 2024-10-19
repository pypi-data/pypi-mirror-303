"""
Type annotations for sagemaker-edge service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/type_defs/)

Usage::

    ```python
    from mypy_boto3_sagemaker_edge.type_defs import ChecksumTypeDef

    data: ChecksumTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import DeploymentStatusType, FailureHandlingPolicyType, ModelStateType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ChecksumTypeDef",
    "DeploymentModelTypeDef",
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "GetDeploymentsRequestRequestTypeDef",
    "GetDeviceRegistrationRequestRequestTypeDef",
    "DefinitionTypeDef",
    "DeploymentResultTypeDef",
    "EdgeMetricTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDeviceRegistrationResultTypeDef",
    "EdgeDeploymentTypeDef",
    "ModelTypeDef",
    "GetDeploymentsResultTypeDef",
    "SendHeartbeatRequestRequestTypeDef",
)

ChecksumTypeDef = TypedDict(
    "ChecksumTypeDef",
    {
        "Type": NotRequired[Literal["SHA1"]],
        "Sum": NotRequired[str],
    },
)
DeploymentModelTypeDef = TypedDict(
    "DeploymentModelTypeDef",
    {
        "ModelHandle": NotRequired[str],
        "ModelName": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "DesiredState": NotRequired[ModelStateType],
        "State": NotRequired[ModelStateType],
        "Status": NotRequired[DeploymentStatusType],
        "StatusReason": NotRequired[str],
        "RollbackFailureReason": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
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
GetDeploymentsRequestRequestTypeDef = TypedDict(
    "GetDeploymentsRequestRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)
GetDeviceRegistrationRequestRequestTypeDef = TypedDict(
    "GetDeviceRegistrationRequestRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)
DefinitionTypeDef = TypedDict(
    "DefinitionTypeDef",
    {
        "ModelHandle": NotRequired[str],
        "S3Url": NotRequired[str],
        "Checksum": NotRequired[ChecksumTypeDef],
        "State": NotRequired[ModelStateType],
    },
)
DeploymentResultTypeDef = TypedDict(
    "DeploymentResultTypeDef",
    {
        "DeploymentName": NotRequired[str],
        "DeploymentStatus": NotRequired[str],
        "DeploymentStatusMessage": NotRequired[str],
        "DeploymentStartTime": NotRequired[TimestampTypeDef],
        "DeploymentEndTime": NotRequired[TimestampTypeDef],
        "DeploymentModels": NotRequired[Sequence[DeploymentModelTypeDef]],
    },
)
EdgeMetricTypeDef = TypedDict(
    "EdgeMetricTypeDef",
    {
        "Dimension": NotRequired[str],
        "MetricName": NotRequired[str],
        "Value": NotRequired[float],
        "Timestamp": NotRequired[TimestampTypeDef],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeviceRegistrationResultTypeDef = TypedDict(
    "GetDeviceRegistrationResultTypeDef",
    {
        "DeviceRegistration": str,
        "CacheTTL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EdgeDeploymentTypeDef = TypedDict(
    "EdgeDeploymentTypeDef",
    {
        "DeploymentName": NotRequired[str],
        "Type": NotRequired[Literal["Model"]],
        "FailureHandlingPolicy": NotRequired[FailureHandlingPolicyType],
        "Definitions": NotRequired[List[DefinitionTypeDef]],
    },
)
ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "ModelName": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "LatestSampleTime": NotRequired[TimestampTypeDef],
        "LatestInference": NotRequired[TimestampTypeDef],
        "ModelMetrics": NotRequired[Sequence[EdgeMetricTypeDef]],
    },
)
GetDeploymentsResultTypeDef = TypedDict(
    "GetDeploymentsResultTypeDef",
    {
        "Deployments": List[EdgeDeploymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendHeartbeatRequestRequestTypeDef = TypedDict(
    "SendHeartbeatRequestRequestTypeDef",
    {
        "AgentVersion": str,
        "DeviceName": str,
        "DeviceFleetName": str,
        "AgentMetrics": NotRequired[Sequence[EdgeMetricTypeDef]],
        "Models": NotRequired[Sequence[ModelTypeDef]],
        "DeploymentResult": NotRequired[DeploymentResultTypeDef],
    },
)
