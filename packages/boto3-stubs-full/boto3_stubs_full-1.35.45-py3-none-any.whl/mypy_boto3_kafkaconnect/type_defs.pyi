"""
Type annotations for kafkaconnect service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/type_defs/)

Usage::

    ```python
    from mypy_boto3_kafkaconnect.type_defs import VpcDescriptionTypeDef

    data: VpcDescriptionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ConnectorStateType,
    CustomPluginContentTypeType,
    CustomPluginStateType,
    KafkaClusterClientAuthenticationTypeType,
    KafkaClusterEncryptionInTransitTypeType,
    WorkerConfigurationStateType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "VpcDescriptionTypeDef",
    "VpcTypeDef",
    "ScaleInPolicyDescriptionTypeDef",
    "ScaleOutPolicyDescriptionTypeDef",
    "ScaleInPolicyTypeDef",
    "ScaleOutPolicyTypeDef",
    "ScaleInPolicyUpdateTypeDef",
    "ScaleOutPolicyUpdateTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "ProvisionedCapacityTypeDef",
    "ProvisionedCapacityUpdateTypeDef",
    "CloudWatchLogsLogDeliveryDescriptionTypeDef",
    "CloudWatchLogsLogDeliveryTypeDef",
    "KafkaClusterClientAuthenticationDescriptionTypeDef",
    "KafkaClusterEncryptionInTransitDescriptionTypeDef",
    "WorkerConfigurationDescriptionTypeDef",
    "KafkaClusterClientAuthenticationTypeDef",
    "KafkaClusterEncryptionInTransitTypeDef",
    "WorkerConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "CreateWorkerConfigurationRequestRequestTypeDef",
    "WorkerConfigurationRevisionSummaryTypeDef",
    "CustomPluginDescriptionTypeDef",
    "CustomPluginFileDescriptionTypeDef",
    "S3LocationDescriptionTypeDef",
    "S3LocationTypeDef",
    "CustomPluginTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "DeleteCustomPluginRequestRequestTypeDef",
    "DeleteWorkerConfigurationRequestRequestTypeDef",
    "DescribeConnectorRequestRequestTypeDef",
    "StateDescriptionTypeDef",
    "DescribeCustomPluginRequestRequestTypeDef",
    "DescribeWorkerConfigurationRequestRequestTypeDef",
    "WorkerConfigurationRevisionDescriptionTypeDef",
    "FirehoseLogDeliveryDescriptionTypeDef",
    "FirehoseLogDeliveryTypeDef",
    "PaginatorConfigTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListCustomPluginsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWorkerConfigurationsRequestRequestTypeDef",
    "S3LogDeliveryDescriptionTypeDef",
    "S3LogDeliveryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ApacheKafkaClusterDescriptionTypeDef",
    "ApacheKafkaClusterTypeDef",
    "AutoScalingDescriptionTypeDef",
    "AutoScalingTypeDef",
    "AutoScalingUpdateTypeDef",
    "CreateConnectorResponseTypeDef",
    "CreateCustomPluginResponseTypeDef",
    "DeleteConnectorResponseTypeDef",
    "DeleteCustomPluginResponseTypeDef",
    "DeleteWorkerConfigurationResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateConnectorResponseTypeDef",
    "CreateWorkerConfigurationResponseTypeDef",
    "WorkerConfigurationSummaryTypeDef",
    "PluginDescriptionTypeDef",
    "CustomPluginLocationDescriptionTypeDef",
    "CustomPluginLocationTypeDef",
    "PluginTypeDef",
    "DescribeWorkerConfigurationResponseTypeDef",
    "ListConnectorsRequestListConnectorsPaginateTypeDef",
    "ListCustomPluginsRequestListCustomPluginsPaginateTypeDef",
    "ListWorkerConfigurationsRequestListWorkerConfigurationsPaginateTypeDef",
    "WorkerLogDeliveryDescriptionTypeDef",
    "WorkerLogDeliveryTypeDef",
    "KafkaClusterDescriptionTypeDef",
    "KafkaClusterTypeDef",
    "CapacityDescriptionTypeDef",
    "CapacityTypeDef",
    "CapacityUpdateTypeDef",
    "ListWorkerConfigurationsResponseTypeDef",
    "CustomPluginRevisionSummaryTypeDef",
    "CreateCustomPluginRequestRequestTypeDef",
    "LogDeliveryDescriptionTypeDef",
    "LogDeliveryTypeDef",
    "UpdateConnectorRequestRequestTypeDef",
    "CustomPluginSummaryTypeDef",
    "DescribeCustomPluginResponseTypeDef",
    "ConnectorSummaryTypeDef",
    "DescribeConnectorResponseTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "ListCustomPluginsResponseTypeDef",
    "ListConnectorsResponseTypeDef",
)

VpcDescriptionTypeDef = TypedDict(
    "VpcDescriptionTypeDef",
    {
        "securityGroups": NotRequired[List[str]],
        "subnets": NotRequired[List[str]],
    },
)
VpcTypeDef = TypedDict(
    "VpcTypeDef",
    {
        "subnets": Sequence[str],
        "securityGroups": NotRequired[Sequence[str]],
    },
)
ScaleInPolicyDescriptionTypeDef = TypedDict(
    "ScaleInPolicyDescriptionTypeDef",
    {
        "cpuUtilizationPercentage": NotRequired[int],
    },
)
ScaleOutPolicyDescriptionTypeDef = TypedDict(
    "ScaleOutPolicyDescriptionTypeDef",
    {
        "cpuUtilizationPercentage": NotRequired[int],
    },
)
ScaleInPolicyTypeDef = TypedDict(
    "ScaleInPolicyTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)
ScaleOutPolicyTypeDef = TypedDict(
    "ScaleOutPolicyTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)
ScaleInPolicyUpdateTypeDef = TypedDict(
    "ScaleInPolicyUpdateTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)
ScaleOutPolicyUpdateTypeDef = TypedDict(
    "ScaleOutPolicyUpdateTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)
ProvisionedCapacityDescriptionTypeDef = TypedDict(
    "ProvisionedCapacityDescriptionTypeDef",
    {
        "mcuCount": NotRequired[int],
        "workerCount": NotRequired[int],
    },
)
ProvisionedCapacityTypeDef = TypedDict(
    "ProvisionedCapacityTypeDef",
    {
        "mcuCount": int,
        "workerCount": int,
    },
)
ProvisionedCapacityUpdateTypeDef = TypedDict(
    "ProvisionedCapacityUpdateTypeDef",
    {
        "mcuCount": int,
        "workerCount": int,
    },
)
CloudWatchLogsLogDeliveryDescriptionTypeDef = TypedDict(
    "CloudWatchLogsLogDeliveryDescriptionTypeDef",
    {
        "enabled": NotRequired[bool],
        "logGroup": NotRequired[str],
    },
)
CloudWatchLogsLogDeliveryTypeDef = TypedDict(
    "CloudWatchLogsLogDeliveryTypeDef",
    {
        "enabled": bool,
        "logGroup": NotRequired[str],
    },
)
KafkaClusterClientAuthenticationDescriptionTypeDef = TypedDict(
    "KafkaClusterClientAuthenticationDescriptionTypeDef",
    {
        "authenticationType": NotRequired[KafkaClusterClientAuthenticationTypeType],
    },
)
KafkaClusterEncryptionInTransitDescriptionTypeDef = TypedDict(
    "KafkaClusterEncryptionInTransitDescriptionTypeDef",
    {
        "encryptionType": NotRequired[KafkaClusterEncryptionInTransitTypeType],
    },
)
WorkerConfigurationDescriptionTypeDef = TypedDict(
    "WorkerConfigurationDescriptionTypeDef",
    {
        "revision": NotRequired[int],
        "workerConfigurationArn": NotRequired[str],
    },
)
KafkaClusterClientAuthenticationTypeDef = TypedDict(
    "KafkaClusterClientAuthenticationTypeDef",
    {
        "authenticationType": KafkaClusterClientAuthenticationTypeType,
    },
)
KafkaClusterEncryptionInTransitTypeDef = TypedDict(
    "KafkaClusterEncryptionInTransitTypeDef",
    {
        "encryptionType": KafkaClusterEncryptionInTransitTypeType,
    },
)
WorkerConfigurationTypeDef = TypedDict(
    "WorkerConfigurationTypeDef",
    {
        "revision": int,
        "workerConfigurationArn": str,
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
CreateWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "CreateWorkerConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "propertiesFileContent": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
WorkerConfigurationRevisionSummaryTypeDef = TypedDict(
    "WorkerConfigurationRevisionSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "description": NotRequired[str],
        "revision": NotRequired[int],
    },
)
CustomPluginDescriptionTypeDef = TypedDict(
    "CustomPluginDescriptionTypeDef",
    {
        "customPluginArn": NotRequired[str],
        "revision": NotRequired[int],
    },
)
CustomPluginFileDescriptionTypeDef = TypedDict(
    "CustomPluginFileDescriptionTypeDef",
    {
        "fileMd5": NotRequired[str],
        "fileSize": NotRequired[int],
    },
)
S3LocationDescriptionTypeDef = TypedDict(
    "S3LocationDescriptionTypeDef",
    {
        "bucketArn": NotRequired[str],
        "fileKey": NotRequired[str],
        "objectVersion": NotRequired[str],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketArn": str,
        "fileKey": str,
        "objectVersion": NotRequired[str],
    },
)
CustomPluginTypeDef = TypedDict(
    "CustomPluginTypeDef",
    {
        "customPluginArn": str,
        "revision": int,
    },
)
DeleteConnectorRequestRequestTypeDef = TypedDict(
    "DeleteConnectorRequestRequestTypeDef",
    {
        "connectorArn": str,
        "currentVersion": NotRequired[str],
    },
)
DeleteCustomPluginRequestRequestTypeDef = TypedDict(
    "DeleteCustomPluginRequestRequestTypeDef",
    {
        "customPluginArn": str,
    },
)
DeleteWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteWorkerConfigurationRequestRequestTypeDef",
    {
        "workerConfigurationArn": str,
    },
)
DescribeConnectorRequestRequestTypeDef = TypedDict(
    "DescribeConnectorRequestRequestTypeDef",
    {
        "connectorArn": str,
    },
)
StateDescriptionTypeDef = TypedDict(
    "StateDescriptionTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
DescribeCustomPluginRequestRequestTypeDef = TypedDict(
    "DescribeCustomPluginRequestRequestTypeDef",
    {
        "customPluginArn": str,
    },
)
DescribeWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeWorkerConfigurationRequestRequestTypeDef",
    {
        "workerConfigurationArn": str,
    },
)
WorkerConfigurationRevisionDescriptionTypeDef = TypedDict(
    "WorkerConfigurationRevisionDescriptionTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "description": NotRequired[str],
        "propertiesFileContent": NotRequired[str],
        "revision": NotRequired[int],
    },
)
FirehoseLogDeliveryDescriptionTypeDef = TypedDict(
    "FirehoseLogDeliveryDescriptionTypeDef",
    {
        "deliveryStream": NotRequired[str],
        "enabled": NotRequired[bool],
    },
)
FirehoseLogDeliveryTypeDef = TypedDict(
    "FirehoseLogDeliveryTypeDef",
    {
        "enabled": bool,
        "deliveryStream": NotRequired[str],
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
ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "connectorNamePrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListCustomPluginsRequestRequestTypeDef = TypedDict(
    "ListCustomPluginsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "namePrefix": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListWorkerConfigurationsRequestRequestTypeDef = TypedDict(
    "ListWorkerConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "namePrefix": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
S3LogDeliveryDescriptionTypeDef = TypedDict(
    "S3LogDeliveryDescriptionTypeDef",
    {
        "bucket": NotRequired[str],
        "enabled": NotRequired[bool],
        "prefix": NotRequired[str],
    },
)
S3LogDeliveryTypeDef = TypedDict(
    "S3LogDeliveryTypeDef",
    {
        "enabled": bool,
        "bucket": NotRequired[str],
        "prefix": NotRequired[str],
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
ApacheKafkaClusterDescriptionTypeDef = TypedDict(
    "ApacheKafkaClusterDescriptionTypeDef",
    {
        "bootstrapServers": NotRequired[str],
        "vpc": NotRequired[VpcDescriptionTypeDef],
    },
)
ApacheKafkaClusterTypeDef = TypedDict(
    "ApacheKafkaClusterTypeDef",
    {
        "bootstrapServers": str,
        "vpc": VpcTypeDef,
    },
)
AutoScalingDescriptionTypeDef = TypedDict(
    "AutoScalingDescriptionTypeDef",
    {
        "maxWorkerCount": NotRequired[int],
        "mcuCount": NotRequired[int],
        "minWorkerCount": NotRequired[int],
        "scaleInPolicy": NotRequired[ScaleInPolicyDescriptionTypeDef],
        "scaleOutPolicy": NotRequired[ScaleOutPolicyDescriptionTypeDef],
    },
)
AutoScalingTypeDef = TypedDict(
    "AutoScalingTypeDef",
    {
        "maxWorkerCount": int,
        "mcuCount": int,
        "minWorkerCount": int,
        "scaleInPolicy": NotRequired[ScaleInPolicyTypeDef],
        "scaleOutPolicy": NotRequired[ScaleOutPolicyTypeDef],
    },
)
AutoScalingUpdateTypeDef = TypedDict(
    "AutoScalingUpdateTypeDef",
    {
        "maxWorkerCount": int,
        "mcuCount": int,
        "minWorkerCount": int,
        "scaleInPolicy": ScaleInPolicyUpdateTypeDef,
        "scaleOutPolicy": ScaleOutPolicyUpdateTypeDef,
    },
)
CreateConnectorResponseTypeDef = TypedDict(
    "CreateConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorName": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCustomPluginResponseTypeDef = TypedDict(
    "CreateCustomPluginResponseTypeDef",
    {
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "name": str,
        "revision": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteConnectorResponseTypeDef = TypedDict(
    "DeleteConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCustomPluginResponseTypeDef = TypedDict(
    "DeleteCustomPluginResponseTypeDef",
    {
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkerConfigurationResponseTypeDef = TypedDict(
    "DeleteWorkerConfigurationResponseTypeDef",
    {
        "workerConfigurationArn": str,
        "workerConfigurationState": WorkerConfigurationStateType,
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
UpdateConnectorResponseTypeDef = TypedDict(
    "UpdateConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkerConfigurationResponseTypeDef = TypedDict(
    "CreateWorkerConfigurationResponseTypeDef",
    {
        "creationTime": datetime,
        "latestRevision": WorkerConfigurationRevisionSummaryTypeDef,
        "name": str,
        "workerConfigurationArn": str,
        "workerConfigurationState": WorkerConfigurationStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkerConfigurationSummaryTypeDef = TypedDict(
    "WorkerConfigurationSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "description": NotRequired[str],
        "latestRevision": NotRequired[WorkerConfigurationRevisionSummaryTypeDef],
        "name": NotRequired[str],
        "workerConfigurationArn": NotRequired[str],
        "workerConfigurationState": NotRequired[WorkerConfigurationStateType],
    },
)
PluginDescriptionTypeDef = TypedDict(
    "PluginDescriptionTypeDef",
    {
        "customPlugin": NotRequired[CustomPluginDescriptionTypeDef],
    },
)
CustomPluginLocationDescriptionTypeDef = TypedDict(
    "CustomPluginLocationDescriptionTypeDef",
    {
        "s3Location": NotRequired[S3LocationDescriptionTypeDef],
    },
)
CustomPluginLocationTypeDef = TypedDict(
    "CustomPluginLocationTypeDef",
    {
        "s3Location": S3LocationTypeDef,
    },
)
PluginTypeDef = TypedDict(
    "PluginTypeDef",
    {
        "customPlugin": CustomPluginTypeDef,
    },
)
DescribeWorkerConfigurationResponseTypeDef = TypedDict(
    "DescribeWorkerConfigurationResponseTypeDef",
    {
        "creationTime": datetime,
        "description": str,
        "latestRevision": WorkerConfigurationRevisionDescriptionTypeDef,
        "name": str,
        "workerConfigurationArn": str,
        "workerConfigurationState": WorkerConfigurationStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConnectorsRequestListConnectorsPaginateTypeDef = TypedDict(
    "ListConnectorsRequestListConnectorsPaginateTypeDef",
    {
        "connectorNamePrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomPluginsRequestListCustomPluginsPaginateTypeDef = TypedDict(
    "ListCustomPluginsRequestListCustomPluginsPaginateTypeDef",
    {
        "namePrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkerConfigurationsRequestListWorkerConfigurationsPaginateTypeDef = TypedDict(
    "ListWorkerConfigurationsRequestListWorkerConfigurationsPaginateTypeDef",
    {
        "namePrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
WorkerLogDeliveryDescriptionTypeDef = TypedDict(
    "WorkerLogDeliveryDescriptionTypeDef",
    {
        "cloudWatchLogs": NotRequired[CloudWatchLogsLogDeliveryDescriptionTypeDef],
        "firehose": NotRequired[FirehoseLogDeliveryDescriptionTypeDef],
        "s3": NotRequired[S3LogDeliveryDescriptionTypeDef],
    },
)
WorkerLogDeliveryTypeDef = TypedDict(
    "WorkerLogDeliveryTypeDef",
    {
        "cloudWatchLogs": NotRequired[CloudWatchLogsLogDeliveryTypeDef],
        "firehose": NotRequired[FirehoseLogDeliveryTypeDef],
        "s3": NotRequired[S3LogDeliveryTypeDef],
    },
)
KafkaClusterDescriptionTypeDef = TypedDict(
    "KafkaClusterDescriptionTypeDef",
    {
        "apacheKafkaCluster": NotRequired[ApacheKafkaClusterDescriptionTypeDef],
    },
)
KafkaClusterTypeDef = TypedDict(
    "KafkaClusterTypeDef",
    {
        "apacheKafkaCluster": ApacheKafkaClusterTypeDef,
    },
)
CapacityDescriptionTypeDef = TypedDict(
    "CapacityDescriptionTypeDef",
    {
        "autoScaling": NotRequired[AutoScalingDescriptionTypeDef],
        "provisionedCapacity": NotRequired[ProvisionedCapacityDescriptionTypeDef],
    },
)
CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "autoScaling": NotRequired[AutoScalingTypeDef],
        "provisionedCapacity": NotRequired[ProvisionedCapacityTypeDef],
    },
)
CapacityUpdateTypeDef = TypedDict(
    "CapacityUpdateTypeDef",
    {
        "autoScaling": NotRequired[AutoScalingUpdateTypeDef],
        "provisionedCapacity": NotRequired[ProvisionedCapacityUpdateTypeDef],
    },
)
ListWorkerConfigurationsResponseTypeDef = TypedDict(
    "ListWorkerConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "workerConfigurations": List[WorkerConfigurationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomPluginRevisionSummaryTypeDef = TypedDict(
    "CustomPluginRevisionSummaryTypeDef",
    {
        "contentType": NotRequired[CustomPluginContentTypeType],
        "creationTime": NotRequired[datetime],
        "description": NotRequired[str],
        "fileDescription": NotRequired[CustomPluginFileDescriptionTypeDef],
        "location": NotRequired[CustomPluginLocationDescriptionTypeDef],
        "revision": NotRequired[int],
    },
)
CreateCustomPluginRequestRequestTypeDef = TypedDict(
    "CreateCustomPluginRequestRequestTypeDef",
    {
        "contentType": CustomPluginContentTypeType,
        "location": CustomPluginLocationTypeDef,
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
LogDeliveryDescriptionTypeDef = TypedDict(
    "LogDeliveryDescriptionTypeDef",
    {
        "workerLogDelivery": NotRequired[WorkerLogDeliveryDescriptionTypeDef],
    },
)
LogDeliveryTypeDef = TypedDict(
    "LogDeliveryTypeDef",
    {
        "workerLogDelivery": WorkerLogDeliveryTypeDef,
    },
)
UpdateConnectorRequestRequestTypeDef = TypedDict(
    "UpdateConnectorRequestRequestTypeDef",
    {
        "capacity": CapacityUpdateTypeDef,
        "connectorArn": str,
        "currentVersion": str,
    },
)
CustomPluginSummaryTypeDef = TypedDict(
    "CustomPluginSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "customPluginArn": NotRequired[str],
        "customPluginState": NotRequired[CustomPluginStateType],
        "description": NotRequired[str],
        "latestRevision": NotRequired[CustomPluginRevisionSummaryTypeDef],
        "name": NotRequired[str],
    },
)
DescribeCustomPluginResponseTypeDef = TypedDict(
    "DescribeCustomPluginResponseTypeDef",
    {
        "creationTime": datetime,
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "description": str,
        "latestRevision": CustomPluginRevisionSummaryTypeDef,
        "name": str,
        "stateDescription": StateDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectorSummaryTypeDef = TypedDict(
    "ConnectorSummaryTypeDef",
    {
        "capacity": NotRequired[CapacityDescriptionTypeDef],
        "connectorArn": NotRequired[str],
        "connectorDescription": NotRequired[str],
        "connectorName": NotRequired[str],
        "connectorState": NotRequired[ConnectorStateType],
        "creationTime": NotRequired[datetime],
        "currentVersion": NotRequired[str],
        "kafkaCluster": NotRequired[KafkaClusterDescriptionTypeDef],
        "kafkaClusterClientAuthentication": NotRequired[
            KafkaClusterClientAuthenticationDescriptionTypeDef
        ],
        "kafkaClusterEncryptionInTransit": NotRequired[
            KafkaClusterEncryptionInTransitDescriptionTypeDef
        ],
        "kafkaConnectVersion": NotRequired[str],
        "logDelivery": NotRequired[LogDeliveryDescriptionTypeDef],
        "plugins": NotRequired[List[PluginDescriptionTypeDef]],
        "serviceExecutionRoleArn": NotRequired[str],
        "workerConfiguration": NotRequired[WorkerConfigurationDescriptionTypeDef],
    },
)
DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "capacity": CapacityDescriptionTypeDef,
        "connectorArn": str,
        "connectorConfiguration": Dict[str, str],
        "connectorDescription": str,
        "connectorName": str,
        "connectorState": ConnectorStateType,
        "creationTime": datetime,
        "currentVersion": str,
        "kafkaCluster": KafkaClusterDescriptionTypeDef,
        "kafkaClusterClientAuthentication": KafkaClusterClientAuthenticationDescriptionTypeDef,
        "kafkaClusterEncryptionInTransit": KafkaClusterEncryptionInTransitDescriptionTypeDef,
        "kafkaConnectVersion": str,
        "logDelivery": LogDeliveryDescriptionTypeDef,
        "plugins": List[PluginDescriptionTypeDef],
        "serviceExecutionRoleArn": str,
        "stateDescription": StateDescriptionTypeDef,
        "workerConfiguration": WorkerConfigurationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectorRequestRequestTypeDef = TypedDict(
    "CreateConnectorRequestRequestTypeDef",
    {
        "capacity": CapacityTypeDef,
        "connectorConfiguration": Mapping[str, str],
        "connectorName": str,
        "kafkaCluster": KafkaClusterTypeDef,
        "kafkaClusterClientAuthentication": KafkaClusterClientAuthenticationTypeDef,
        "kafkaClusterEncryptionInTransit": KafkaClusterEncryptionInTransitTypeDef,
        "kafkaConnectVersion": str,
        "plugins": Sequence[PluginTypeDef],
        "serviceExecutionRoleArn": str,
        "connectorDescription": NotRequired[str],
        "logDelivery": NotRequired[LogDeliveryTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "workerConfiguration": NotRequired[WorkerConfigurationTypeDef],
    },
)
ListCustomPluginsResponseTypeDef = TypedDict(
    "ListCustomPluginsResponseTypeDef",
    {
        "customPlugins": List[CustomPluginSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "connectors": List[ConnectorSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
