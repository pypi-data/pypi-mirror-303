"""
Type annotations for mwaa service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/type_defs/)

Usage::

    ```python
    from mypy_boto3_mwaa.type_defs import CreateCliTokenRequestRequestTypeDef

    data: CreateCliTokenRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    EndpointManagementType,
    EnvironmentStatusType,
    LoggingLevelType,
    UnitType,
    UpdateStatusType,
    WebserverAccessModeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "CreateCliTokenRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "NetworkConfigurationTypeDef",
    "CreateWebLoginTokenRequestRequestTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DimensionTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "UpdateErrorTypeDef",
    "PaginatorConfigTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "StatisticSetTypeDef",
    "TimestampTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
    "CreateCliTokenResponseTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateWebLoginTokenResponseTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "LastUpdateTypeDef",
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    "LoggingConfigurationInputTypeDef",
    "LoggingConfigurationTypeDef",
    "MetricDatumTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "EnvironmentTypeDef",
    "PublishMetricsInputRequestTypeDef",
    "GetEnvironmentOutputTypeDef",
)

CreateCliTokenRequestRequestTypeDef = TypedDict(
    "CreateCliTokenRequestRequestTypeDef",
    {
        "Name": str,
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
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)
CreateWebLoginTokenRequestRequestTypeDef = TypedDict(
    "CreateWebLoginTokenRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)
DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "SubnetIds": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
    },
)
GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)
UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
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
ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ModuleLoggingConfigurationInputTypeDef = TypedDict(
    "ModuleLoggingConfigurationInputTypeDef",
    {
        "Enabled": bool,
        "LogLevel": LoggingLevelType,
    },
)
ModuleLoggingConfigurationTypeDef = TypedDict(
    "ModuleLoggingConfigurationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LogLevel": NotRequired[LoggingLevelType],
        "CloudWatchLogGroupArn": NotRequired[str],
    },
)
StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "SampleCount": NotRequired[int],
        "Sum": NotRequired[float],
        "Minimum": NotRequired[float],
        "Maximum": NotRequired[float],
    },
)
TimestampTypeDef = Union[datetime, str]
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateNetworkConfigurationInputTypeDef = TypedDict(
    "UpdateNetworkConfigurationInputTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
    },
)
CreateCliTokenResponseTypeDef = TypedDict(
    "CreateCliTokenResponseTypeDef",
    {
        "CliToken": str,
        "WebServerHostname": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWebLoginTokenResponseTypeDef = TypedDict(
    "CreateWebLoginTokenResponseTypeDef",
    {
        "WebToken": str,
        "WebServerHostname": str,
        "IamIdentity": str,
        "AirflowIdentity": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "Environments": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LastUpdateTypeDef = TypedDict(
    "LastUpdateTypeDef",
    {
        "Status": NotRequired[UpdateStatusType],
        "CreatedAt": NotRequired[datetime],
        "Error": NotRequired[UpdateErrorTypeDef],
        "Source": NotRequired[str],
    },
)
ListEnvironmentsInputListEnvironmentsPaginateTypeDef = TypedDict(
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LoggingConfigurationInputTypeDef = TypedDict(
    "LoggingConfigurationInputTypeDef",
    {
        "DagProcessingLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
        "SchedulerLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
        "WebserverLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
        "WorkerLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
        "TaskLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
    },
)
LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "DagProcessingLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
        "SchedulerLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
        "WebserverLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
        "WorkerLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
        "TaskLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
    },
)
MetricDatumTypeDef = TypedDict(
    "MetricDatumTypeDef",
    {
        "MetricName": str,
        "Timestamp": TimestampTypeDef,
        "Dimensions": NotRequired[Sequence[DimensionTypeDef]],
        "Value": NotRequired[float],
        "Unit": NotRequired[UnitType],
        "StatisticValues": NotRequired[StatisticSetTypeDef],
    },
)
CreateEnvironmentInputRequestTypeDef = TypedDict(
    "CreateEnvironmentInputRequestTypeDef",
    {
        "Name": str,
        "ExecutionRoleArn": str,
        "SourceBucketArn": str,
        "DagS3Path": str,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "PluginsS3Path": NotRequired[str],
        "PluginsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "StartupScriptS3Path": NotRequired[str],
        "StartupScriptS3ObjectVersion": NotRequired[str],
        "AirflowConfigurationOptions": NotRequired[Mapping[str, str]],
        "EnvironmentClass": NotRequired[str],
        "MaxWorkers": NotRequired[int],
        "KmsKey": NotRequired[str],
        "AirflowVersion": NotRequired[str],
        "LoggingConfiguration": NotRequired[LoggingConfigurationInputTypeDef],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "MinWorkers": NotRequired[int],
        "Schedulers": NotRequired[int],
        "EndpointManagement": NotRequired[EndpointManagementType],
        "MinWebservers": NotRequired[int],
        "MaxWebservers": NotRequired[int],
    },
)
UpdateEnvironmentInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentInputRequestTypeDef",
    {
        "Name": str,
        "ExecutionRoleArn": NotRequired[str],
        "AirflowVersion": NotRequired[str],
        "SourceBucketArn": NotRequired[str],
        "DagS3Path": NotRequired[str],
        "PluginsS3Path": NotRequired[str],
        "PluginsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "StartupScriptS3Path": NotRequired[str],
        "StartupScriptS3ObjectVersion": NotRequired[str],
        "AirflowConfigurationOptions": NotRequired[Mapping[str, str]],
        "EnvironmentClass": NotRequired[str],
        "MaxWorkers": NotRequired[int],
        "NetworkConfiguration": NotRequired[UpdateNetworkConfigurationInputTypeDef],
        "LoggingConfiguration": NotRequired[LoggingConfigurationInputTypeDef],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "MinWorkers": NotRequired[int],
        "Schedulers": NotRequired[int],
        "MinWebservers": NotRequired[int],
        "MaxWebservers": NotRequired[int],
    },
)
EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[EnvironmentStatusType],
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "WebserverUrl": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "ServiceRoleArn": NotRequired[str],
        "KmsKey": NotRequired[str],
        "AirflowVersion": NotRequired[str],
        "SourceBucketArn": NotRequired[str],
        "DagS3Path": NotRequired[str],
        "PluginsS3Path": NotRequired[str],
        "PluginsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "StartupScriptS3Path": NotRequired[str],
        "StartupScriptS3ObjectVersion": NotRequired[str],
        "AirflowConfigurationOptions": NotRequired[Dict[str, str]],
        "EnvironmentClass": NotRequired[str],
        "MaxWorkers": NotRequired[int],
        "NetworkConfiguration": NotRequired[NetworkConfigurationOutputTypeDef],
        "LoggingConfiguration": NotRequired[LoggingConfigurationTypeDef],
        "LastUpdate": NotRequired[LastUpdateTypeDef],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "MinWorkers": NotRequired[int],
        "Schedulers": NotRequired[int],
        "WebserverVpcEndpointService": NotRequired[str],
        "DatabaseVpcEndpointService": NotRequired[str],
        "CeleryExecutorQueue": NotRequired[str],
        "EndpointManagement": NotRequired[EndpointManagementType],
        "MinWebservers": NotRequired[int],
        "MaxWebservers": NotRequired[int],
    },
)
PublishMetricsInputRequestTypeDef = TypedDict(
    "PublishMetricsInputRequestTypeDef",
    {
        "EnvironmentName": str,
        "MetricData": Sequence[MetricDatumTypeDef],
    },
)
GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "Environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
