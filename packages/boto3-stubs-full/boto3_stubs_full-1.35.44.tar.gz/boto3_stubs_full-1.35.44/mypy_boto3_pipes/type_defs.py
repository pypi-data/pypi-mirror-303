"""
Type annotations for pipes service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pipes/type_defs/)

Usage::

    ```python
    from mypy_boto3_pipes.type_defs import AwsVpcConfigurationOutputTypeDef

    data: AwsVpcConfigurationOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AssignPublicIpType,
    BatchJobDependencyTypeType,
    BatchResourceRequirementTypeType,
    DynamoDBStreamStartPositionType,
    EcsResourceRequirementTypeType,
    EpochTimeUnitType,
    KinesisStreamStartPositionType,
    LaunchTypeType,
    LogLevelType,
    MeasureValueTypeType,
    MSKStartPositionType,
    PipeStateType,
    PipeTargetInvocationTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    RequestedPipeStateDescribeResponseType,
    RequestedPipeStateType,
    S3OutputFormatType,
    SelfManagedKafkaStartPositionType,
    TimeFieldTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchEnvironmentVariableTypeDef",
    "BatchResourceRequirementTypeDef",
    "BatchJobDependencyTypeDef",
    "BatchRetryStrategyTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CloudwatchLogsLogDestinationParametersTypeDef",
    "CloudwatchLogsLogDestinationTypeDef",
    "ResponseMetadataTypeDef",
    "DeadLetterConfigTypeDef",
    "DeletePipeRequestRequestTypeDef",
    "DescribePipeRequestRequestTypeDef",
    "DimensionMappingTypeDef",
    "EcsEnvironmentFileTypeDef",
    "EcsEnvironmentVariableTypeDef",
    "EcsResourceRequirementTypeDef",
    "EcsEphemeralStorageTypeDef",
    "EcsInferenceAcceleratorOverrideTypeDef",
    "FilterTypeDef",
    "FirehoseLogDestinationParametersTypeDef",
    "FirehoseLogDestinationTypeDef",
    "PaginatorConfigTypeDef",
    "ListPipesRequestRequestTypeDef",
    "PipeTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MQBrokerAccessCredentialsTypeDef",
    "MSKAccessCredentialsTypeDef",
    "MultiMeasureAttributeMappingTypeDef",
    "PipeEnrichmentHttpParametersOutputTypeDef",
    "PipeEnrichmentHttpParametersTypeDef",
    "S3LogDestinationParametersTypeDef",
    "S3LogDestinationTypeDef",
    "TimestampTypeDef",
    "PipeSourceSqsQueueParametersTypeDef",
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcOutputTypeDef",
    "PipeTargetCloudWatchLogsParametersTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "TagTypeDef",
    "PipeTargetEventBridgeEventBusParametersOutputTypeDef",
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    "PipeTargetHttpParametersOutputTypeDef",
    "PipeTargetHttpParametersTypeDef",
    "PipeTargetKinesisStreamParametersTypeDef",
    "PipeTargetLambdaFunctionParametersTypeDef",
    "PipeTargetRedshiftDataParametersOutputTypeDef",
    "PipeTargetSqsQueueParametersTypeDef",
    "PipeTargetStateMachineParametersTypeDef",
    "PipeTargetRedshiftDataParametersTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SingleMeasureMappingTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    "StartPipeRequestRequestTypeDef",
    "StopPipeRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePipeSourceSqsQueueParametersTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "AwsVpcConfigurationUnionTypeDef",
    "BatchContainerOverridesOutputTypeDef",
    "BatchContainerOverridesTypeDef",
    "CreatePipeResponseTypeDef",
    "DeletePipeResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartPipeResponseTypeDef",
    "StopPipeResponseTypeDef",
    "UpdatePipeResponseTypeDef",
    "PipeSourceDynamoDBStreamParametersTypeDef",
    "PipeSourceKinesisStreamParametersOutputTypeDef",
    "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    "EcsContainerOverrideOutputTypeDef",
    "EcsContainerOverrideTypeDef",
    "FilterCriteriaOutputTypeDef",
    "FilterCriteriaTypeDef",
    "ListPipesRequestListPipesPaginateTypeDef",
    "ListPipesResponseTypeDef",
    "PipeSourceActiveMQBrokerParametersTypeDef",
    "PipeSourceRabbitMQBrokerParametersTypeDef",
    "UpdatePipeSourceActiveMQBrokerParametersTypeDef",
    "UpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    "PipeSourceManagedStreamingKafkaParametersTypeDef",
    "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
    "MultiMeasureMappingOutputTypeDef",
    "MultiMeasureMappingTypeDef",
    "PipeEnrichmentParametersOutputTypeDef",
    "PipeEnrichmentHttpParametersUnionTypeDef",
    "PipeLogConfigurationParametersTypeDef",
    "PipeLogConfigurationTypeDef",
    "PipeSourceKinesisStreamParametersTypeDef",
    "PipeSourceSelfManagedKafkaParametersOutputTypeDef",
    "PipeTargetEventBridgeEventBusParametersUnionTypeDef",
    "PipeTargetHttpParametersUnionTypeDef",
    "PipeTargetRedshiftDataParametersUnionTypeDef",
    "PipeTargetSageMakerPipelineParametersOutputTypeDef",
    "PipeTargetSageMakerPipelineParametersTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcUnionTypeDef",
    "NetworkConfigurationTypeDef",
    "PipeTargetBatchJobParametersOutputTypeDef",
    "BatchContainerOverridesUnionTypeDef",
    "EcsTaskOverrideOutputTypeDef",
    "EcsContainerOverrideUnionTypeDef",
    "FilterCriteriaUnionTypeDef",
    "PipeTargetTimestreamParametersOutputTypeDef",
    "MultiMeasureMappingUnionTypeDef",
    "PipeEnrichmentParametersTypeDef",
    "PipeSourceKinesisStreamParametersUnionTypeDef",
    "PipeSourceParametersOutputTypeDef",
    "PipeTargetSageMakerPipelineParametersUnionTypeDef",
    "PipeSourceSelfManagedKafkaParametersTypeDef",
    "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    "NetworkConfigurationUnionTypeDef",
    "PipeTargetBatchJobParametersTypeDef",
    "PipeTargetEcsTaskParametersOutputTypeDef",
    "EcsTaskOverrideTypeDef",
    "PipeTargetTimestreamParametersTypeDef",
    "PipeSourceSelfManagedKafkaParametersUnionTypeDef",
    "UpdatePipeSourceParametersTypeDef",
    "PipeTargetBatchJobParametersUnionTypeDef",
    "PipeTargetParametersOutputTypeDef",
    "EcsTaskOverrideUnionTypeDef",
    "PipeTargetTimestreamParametersUnionTypeDef",
    "PipeSourceParametersTypeDef",
    "DescribePipeResponseTypeDef",
    "PipeTargetEcsTaskParametersTypeDef",
    "PipeTargetEcsTaskParametersUnionTypeDef",
    "PipeTargetParametersTypeDef",
    "CreatePipeRequestRequestTypeDef",
    "UpdatePipeRequestRequestTypeDef",
)

AwsVpcConfigurationOutputTypeDef = TypedDict(
    "AwsVpcConfigurationOutputTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": NotRequired[List[str]],
        "AssignPublicIp": NotRequired[AssignPublicIpType],
    },
)
AwsVpcConfigurationTypeDef = TypedDict(
    "AwsVpcConfigurationTypeDef",
    {
        "Subnets": Sequence[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "AssignPublicIp": NotRequired[AssignPublicIpType],
    },
)
BatchArrayPropertiesTypeDef = TypedDict(
    "BatchArrayPropertiesTypeDef",
    {
        "Size": NotRequired[int],
    },
)
BatchEnvironmentVariableTypeDef = TypedDict(
    "BatchEnvironmentVariableTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
BatchResourceRequirementTypeDef = TypedDict(
    "BatchResourceRequirementTypeDef",
    {
        "Type": BatchResourceRequirementTypeType,
        "Value": str,
    },
)
BatchJobDependencyTypeDef = TypedDict(
    "BatchJobDependencyTypeDef",
    {
        "JobId": NotRequired[str],
        "Type": NotRequired[BatchJobDependencyTypeType],
    },
)
BatchRetryStrategyTypeDef = TypedDict(
    "BatchRetryStrategyTypeDef",
    {
        "Attempts": NotRequired[int],
    },
)
CapacityProviderStrategyItemTypeDef = TypedDict(
    "CapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
        "weight": NotRequired[int],
        "base": NotRequired[int],
    },
)
CloudwatchLogsLogDestinationParametersTypeDef = TypedDict(
    "CloudwatchLogsLogDestinationParametersTypeDef",
    {
        "LogGroupArn": str,
    },
)
CloudwatchLogsLogDestinationTypeDef = TypedDict(
    "CloudwatchLogsLogDestinationTypeDef",
    {
        "LogGroupArn": NotRequired[str],
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
DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
DeletePipeRequestRequestTypeDef = TypedDict(
    "DeletePipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribePipeRequestRequestTypeDef = TypedDict(
    "DescribePipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DimensionMappingTypeDef = TypedDict(
    "DimensionMappingTypeDef",
    {
        "DimensionValue": str,
        "DimensionValueType": Literal["VARCHAR"],
        "DimensionName": str,
    },
)
EcsEnvironmentFileTypeDef = TypedDict(
    "EcsEnvironmentFileTypeDef",
    {
        "type": Literal["s3"],
        "value": str,
    },
)
EcsEnvironmentVariableTypeDef = TypedDict(
    "EcsEnvironmentVariableTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)
EcsResourceRequirementTypeDef = TypedDict(
    "EcsResourceRequirementTypeDef",
    {
        "type": EcsResourceRequirementTypeType,
        "value": str,
    },
)
EcsEphemeralStorageTypeDef = TypedDict(
    "EcsEphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)
EcsInferenceAcceleratorOverrideTypeDef = TypedDict(
    "EcsInferenceAcceleratorOverrideTypeDef",
    {
        "deviceName": NotRequired[str],
        "deviceType": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Pattern": NotRequired[str],
    },
)
FirehoseLogDestinationParametersTypeDef = TypedDict(
    "FirehoseLogDestinationParametersTypeDef",
    {
        "DeliveryStreamArn": str,
    },
)
FirehoseLogDestinationTypeDef = TypedDict(
    "FirehoseLogDestinationTypeDef",
    {
        "DeliveryStreamArn": NotRequired[str],
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
ListPipesRequestRequestTypeDef = TypedDict(
    "ListPipesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "CurrentState": NotRequired[PipeStateType],
        "SourcePrefix": NotRequired[str],
        "TargetPrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
PipeTypeDef = TypedDict(
    "PipeTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "CurrentState": NotRequired[PipeStateType],
        "StateReason": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "Source": NotRequired[str],
        "Target": NotRequired[str],
        "Enrichment": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
MQBrokerAccessCredentialsTypeDef = TypedDict(
    "MQBrokerAccessCredentialsTypeDef",
    {
        "BasicAuth": NotRequired[str],
    },
)
MSKAccessCredentialsTypeDef = TypedDict(
    "MSKAccessCredentialsTypeDef",
    {
        "SaslScram512Auth": NotRequired[str],
        "ClientCertificateTlsAuth": NotRequired[str],
    },
)
MultiMeasureAttributeMappingTypeDef = TypedDict(
    "MultiMeasureAttributeMappingTypeDef",
    {
        "MeasureValue": str,
        "MeasureValueType": MeasureValueTypeType,
        "MultiMeasureAttributeName": str,
    },
)
PipeEnrichmentHttpParametersOutputTypeDef = TypedDict(
    "PipeEnrichmentHttpParametersOutputTypeDef",
    {
        "PathParameterValues": NotRequired[List[str]],
        "HeaderParameters": NotRequired[Dict[str, str]],
        "QueryStringParameters": NotRequired[Dict[str, str]],
    },
)
PipeEnrichmentHttpParametersTypeDef = TypedDict(
    "PipeEnrichmentHttpParametersTypeDef",
    {
        "PathParameterValues": NotRequired[Sequence[str]],
        "HeaderParameters": NotRequired[Mapping[str, str]],
        "QueryStringParameters": NotRequired[Mapping[str, str]],
    },
)
S3LogDestinationParametersTypeDef = TypedDict(
    "S3LogDestinationParametersTypeDef",
    {
        "BucketName": str,
        "BucketOwner": str,
        "OutputFormat": NotRequired[S3OutputFormatType],
        "Prefix": NotRequired[str],
    },
)
S3LogDestinationTypeDef = TypedDict(
    "S3LogDestinationTypeDef",
    {
        "BucketName": NotRequired[str],
        "Prefix": NotRequired[str],
        "BucketOwner": NotRequired[str],
        "OutputFormat": NotRequired[S3OutputFormatType],
    },
)
TimestampTypeDef = Union[datetime, str]
PipeSourceSqsQueueParametersTypeDef = TypedDict(
    "PipeSourceSqsQueueParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
SelfManagedKafkaAccessConfigurationCredentialsTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    {
        "BasicAuth": NotRequired[str],
        "SaslScram512Auth": NotRequired[str],
        "SaslScram256Auth": NotRequired[str],
        "ClientCertificateTlsAuth": NotRequired[str],
    },
)
SelfManagedKafkaAccessConfigurationVpcOutputTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationVpcOutputTypeDef",
    {
        "Subnets": NotRequired[List[str]],
        "SecurityGroup": NotRequired[List[str]],
    },
)
PipeTargetCloudWatchLogsParametersTypeDef = TypedDict(
    "PipeTargetCloudWatchLogsParametersTypeDef",
    {
        "LogStreamName": NotRequired[str],
        "Timestamp": NotRequired[str],
    },
)
PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": NotRequired[PlacementConstraintTypeType],
        "expression": NotRequired[str],
    },
)
PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": NotRequired[PlacementStrategyTypeType],
        "field": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
PipeTargetEventBridgeEventBusParametersOutputTypeDef = TypedDict(
    "PipeTargetEventBridgeEventBusParametersOutputTypeDef",
    {
        "EndpointId": NotRequired[str],
        "DetailType": NotRequired[str],
        "Source": NotRequired[str],
        "Resources": NotRequired[List[str]],
        "Time": NotRequired[str],
    },
)
PipeTargetEventBridgeEventBusParametersTypeDef = TypedDict(
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    {
        "EndpointId": NotRequired[str],
        "DetailType": NotRequired[str],
        "Source": NotRequired[str],
        "Resources": NotRequired[Sequence[str]],
        "Time": NotRequired[str],
    },
)
PipeTargetHttpParametersOutputTypeDef = TypedDict(
    "PipeTargetHttpParametersOutputTypeDef",
    {
        "PathParameterValues": NotRequired[List[str]],
        "HeaderParameters": NotRequired[Dict[str, str]],
        "QueryStringParameters": NotRequired[Dict[str, str]],
    },
)
PipeTargetHttpParametersTypeDef = TypedDict(
    "PipeTargetHttpParametersTypeDef",
    {
        "PathParameterValues": NotRequired[Sequence[str]],
        "HeaderParameters": NotRequired[Mapping[str, str]],
        "QueryStringParameters": NotRequired[Mapping[str, str]],
    },
)
PipeTargetKinesisStreamParametersTypeDef = TypedDict(
    "PipeTargetKinesisStreamParametersTypeDef",
    {
        "PartitionKey": str,
    },
)
PipeTargetLambdaFunctionParametersTypeDef = TypedDict(
    "PipeTargetLambdaFunctionParametersTypeDef",
    {
        "InvocationType": NotRequired[PipeTargetInvocationTypeType],
    },
)
PipeTargetRedshiftDataParametersOutputTypeDef = TypedDict(
    "PipeTargetRedshiftDataParametersOutputTypeDef",
    {
        "Database": str,
        "Sqls": List[str],
        "SecretManagerArn": NotRequired[str],
        "DbUser": NotRequired[str],
        "StatementName": NotRequired[str],
        "WithEvent": NotRequired[bool],
    },
)
PipeTargetSqsQueueParametersTypeDef = TypedDict(
    "PipeTargetSqsQueueParametersTypeDef",
    {
        "MessageGroupId": NotRequired[str],
        "MessageDeduplicationId": NotRequired[str],
    },
)
PipeTargetStateMachineParametersTypeDef = TypedDict(
    "PipeTargetStateMachineParametersTypeDef",
    {
        "InvocationType": NotRequired[PipeTargetInvocationTypeType],
    },
)
PipeTargetRedshiftDataParametersTypeDef = TypedDict(
    "PipeTargetRedshiftDataParametersTypeDef",
    {
        "Database": str,
        "Sqls": Sequence[str],
        "SecretManagerArn": NotRequired[str],
        "DbUser": NotRequired[str],
        "StatementName": NotRequired[str],
        "WithEvent": NotRequired[bool],
    },
)
SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
SingleMeasureMappingTypeDef = TypedDict(
    "SingleMeasureMappingTypeDef",
    {
        "MeasureValue": str,
        "MeasureValueType": MeasureValueTypeType,
        "MeasureName": str,
    },
)
SelfManagedKafkaAccessConfigurationVpcTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    {
        "Subnets": NotRequired[Sequence[str]],
        "SecurityGroup": NotRequired[Sequence[str]],
    },
)
StartPipeRequestRequestTypeDef = TypedDict(
    "StartPipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StopPipeRequestRequestTypeDef = TypedDict(
    "StopPipeRequestRequestTypeDef",
    {
        "Name": str,
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
UpdatePipeSourceSqsQueueParametersTypeDef = TypedDict(
    "UpdatePipeSourceSqsQueueParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "awsvpcConfiguration": NotRequired[AwsVpcConfigurationOutputTypeDef],
    },
)
AwsVpcConfigurationUnionTypeDef = Union[
    AwsVpcConfigurationTypeDef, AwsVpcConfigurationOutputTypeDef
]
BatchContainerOverridesOutputTypeDef = TypedDict(
    "BatchContainerOverridesOutputTypeDef",
    {
        "Command": NotRequired[List[str]],
        "Environment": NotRequired[List[BatchEnvironmentVariableTypeDef]],
        "InstanceType": NotRequired[str],
        "ResourceRequirements": NotRequired[List[BatchResourceRequirementTypeDef]],
    },
)
BatchContainerOverridesTypeDef = TypedDict(
    "BatchContainerOverridesTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Environment": NotRequired[Sequence[BatchEnvironmentVariableTypeDef]],
        "InstanceType": NotRequired[str],
        "ResourceRequirements": NotRequired[Sequence[BatchResourceRequirementTypeDef]],
    },
)
CreatePipeResponseTypeDef = TypedDict(
    "CreatePipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePipeResponseTypeDef = TypedDict(
    "DeletePipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
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
StartPipeResponseTypeDef = TypedDict(
    "StartPipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopPipeResponseTypeDef = TypedDict(
    "StopPipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipeResponseTypeDef = TypedDict(
    "UpdatePipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "PipeSourceDynamoDBStreamParametersTypeDef",
    {
        "StartingPosition": DynamoDBStreamStartPositionType,
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "ParallelizationFactor": NotRequired[int],
    },
)
PipeSourceKinesisStreamParametersOutputTypeDef = TypedDict(
    "PipeSourceKinesisStreamParametersOutputTypeDef",
    {
        "StartingPosition": KinesisStreamStartPositionType,
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "ParallelizationFactor": NotRequired[int],
        "StartingPositionTimestamp": NotRequired[datetime],
    },
)
UpdatePipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "ParallelizationFactor": NotRequired[int],
    },
)
UpdatePipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "ParallelizationFactor": NotRequired[int],
    },
)
EcsContainerOverrideOutputTypeDef = TypedDict(
    "EcsContainerOverrideOutputTypeDef",
    {
        "Command": NotRequired[List[str]],
        "Cpu": NotRequired[int],
        "Environment": NotRequired[List[EcsEnvironmentVariableTypeDef]],
        "EnvironmentFiles": NotRequired[List[EcsEnvironmentFileTypeDef]],
        "Memory": NotRequired[int],
        "MemoryReservation": NotRequired[int],
        "Name": NotRequired[str],
        "ResourceRequirements": NotRequired[List[EcsResourceRequirementTypeDef]],
    },
)
EcsContainerOverrideTypeDef = TypedDict(
    "EcsContainerOverrideTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Cpu": NotRequired[int],
        "Environment": NotRequired[Sequence[EcsEnvironmentVariableTypeDef]],
        "EnvironmentFiles": NotRequired[Sequence[EcsEnvironmentFileTypeDef]],
        "Memory": NotRequired[int],
        "MemoryReservation": NotRequired[int],
        "Name": NotRequired[str],
        "ResourceRequirements": NotRequired[Sequence[EcsResourceRequirementTypeDef]],
    },
)
FilterCriteriaOutputTypeDef = TypedDict(
    "FilterCriteriaOutputTypeDef",
    {
        "Filters": NotRequired[List[FilterTypeDef]],
    },
)
FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListPipesRequestListPipesPaginateTypeDef = TypedDict(
    "ListPipesRequestListPipesPaginateTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "CurrentState": NotRequired[PipeStateType],
        "SourcePrefix": NotRequired[str],
        "TargetPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipesResponseTypeDef = TypedDict(
    "ListPipesResponseTypeDef",
    {
        "Pipes": List[PipeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "PipeSourceActiveMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "QueueName": str,
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
PipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "PipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "QueueName": str,
        "VirtualHost": NotRequired[str],
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
UpdatePipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "UpdatePipeSourceActiveMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
UpdatePipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "UpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
PipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "PipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "TopicName": str,
        "StartingPosition": NotRequired[MSKStartPositionType],
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "ConsumerGroupID": NotRequired[str],
        "Credentials": NotRequired[MSKAccessCredentialsTypeDef],
    },
)
UpdatePipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "Credentials": NotRequired[MSKAccessCredentialsTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
MultiMeasureMappingOutputTypeDef = TypedDict(
    "MultiMeasureMappingOutputTypeDef",
    {
        "MultiMeasureName": str,
        "MultiMeasureAttributeMappings": List[MultiMeasureAttributeMappingTypeDef],
    },
)
MultiMeasureMappingTypeDef = TypedDict(
    "MultiMeasureMappingTypeDef",
    {
        "MultiMeasureName": str,
        "MultiMeasureAttributeMappings": Sequence[MultiMeasureAttributeMappingTypeDef],
    },
)
PipeEnrichmentParametersOutputTypeDef = TypedDict(
    "PipeEnrichmentParametersOutputTypeDef",
    {
        "InputTemplate": NotRequired[str],
        "HttpParameters": NotRequired[PipeEnrichmentHttpParametersOutputTypeDef],
    },
)
PipeEnrichmentHttpParametersUnionTypeDef = Union[
    PipeEnrichmentHttpParametersTypeDef, PipeEnrichmentHttpParametersOutputTypeDef
]
PipeLogConfigurationParametersTypeDef = TypedDict(
    "PipeLogConfigurationParametersTypeDef",
    {
        "Level": LogLevelType,
        "S3LogDestination": NotRequired[S3LogDestinationParametersTypeDef],
        "FirehoseLogDestination": NotRequired[FirehoseLogDestinationParametersTypeDef],
        "CloudwatchLogsLogDestination": NotRequired[CloudwatchLogsLogDestinationParametersTypeDef],
        "IncludeExecutionData": NotRequired[Sequence[Literal["ALL"]]],
    },
)
PipeLogConfigurationTypeDef = TypedDict(
    "PipeLogConfigurationTypeDef",
    {
        "S3LogDestination": NotRequired[S3LogDestinationTypeDef],
        "FirehoseLogDestination": NotRequired[FirehoseLogDestinationTypeDef],
        "CloudwatchLogsLogDestination": NotRequired[CloudwatchLogsLogDestinationTypeDef],
        "Level": NotRequired[LogLevelType],
        "IncludeExecutionData": NotRequired[List[Literal["ALL"]]],
    },
)
PipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "PipeSourceKinesisStreamParametersTypeDef",
    {
        "StartingPosition": KinesisStreamStartPositionType,
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "ParallelizationFactor": NotRequired[int],
        "StartingPositionTimestamp": NotRequired[TimestampTypeDef],
    },
)
PipeSourceSelfManagedKafkaParametersOutputTypeDef = TypedDict(
    "PipeSourceSelfManagedKafkaParametersOutputTypeDef",
    {
        "TopicName": str,
        "StartingPosition": NotRequired[SelfManagedKafkaStartPositionType],
        "AdditionalBootstrapServers": NotRequired[List[str]],
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "ConsumerGroupID": NotRequired[str],
        "Credentials": NotRequired[SelfManagedKafkaAccessConfigurationCredentialsTypeDef],
        "ServerRootCaCertificate": NotRequired[str],
        "Vpc": NotRequired[SelfManagedKafkaAccessConfigurationVpcOutputTypeDef],
    },
)
PipeTargetEventBridgeEventBusParametersUnionTypeDef = Union[
    PipeTargetEventBridgeEventBusParametersTypeDef,
    PipeTargetEventBridgeEventBusParametersOutputTypeDef,
]
PipeTargetHttpParametersUnionTypeDef = Union[
    PipeTargetHttpParametersTypeDef, PipeTargetHttpParametersOutputTypeDef
]
PipeTargetRedshiftDataParametersUnionTypeDef = Union[
    PipeTargetRedshiftDataParametersTypeDef, PipeTargetRedshiftDataParametersOutputTypeDef
]
PipeTargetSageMakerPipelineParametersOutputTypeDef = TypedDict(
    "PipeTargetSageMakerPipelineParametersOutputTypeDef",
    {
        "PipelineParameterList": NotRequired[List[SageMakerPipelineParameterTypeDef]],
    },
)
PipeTargetSageMakerPipelineParametersTypeDef = TypedDict(
    "PipeTargetSageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": NotRequired[Sequence[SageMakerPipelineParameterTypeDef]],
    },
)
SelfManagedKafkaAccessConfigurationVpcUnionTypeDef = Union[
    SelfManagedKafkaAccessConfigurationVpcTypeDef,
    SelfManagedKafkaAccessConfigurationVpcOutputTypeDef,
]
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": NotRequired[AwsVpcConfigurationUnionTypeDef],
    },
)
PipeTargetBatchJobParametersOutputTypeDef = TypedDict(
    "PipeTargetBatchJobParametersOutputTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": NotRequired[BatchArrayPropertiesTypeDef],
        "RetryStrategy": NotRequired[BatchRetryStrategyTypeDef],
        "ContainerOverrides": NotRequired[BatchContainerOverridesOutputTypeDef],
        "DependsOn": NotRequired[List[BatchJobDependencyTypeDef]],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
BatchContainerOverridesUnionTypeDef = Union[
    BatchContainerOverridesTypeDef, BatchContainerOverridesOutputTypeDef
]
EcsTaskOverrideOutputTypeDef = TypedDict(
    "EcsTaskOverrideOutputTypeDef",
    {
        "ContainerOverrides": NotRequired[List[EcsContainerOverrideOutputTypeDef]],
        "Cpu": NotRequired[str],
        "EphemeralStorage": NotRequired[EcsEphemeralStorageTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "InferenceAcceleratorOverrides": NotRequired[List[EcsInferenceAcceleratorOverrideTypeDef]],
        "Memory": NotRequired[str],
        "TaskRoleArn": NotRequired[str],
    },
)
EcsContainerOverrideUnionTypeDef = Union[
    EcsContainerOverrideTypeDef, EcsContainerOverrideOutputTypeDef
]
FilterCriteriaUnionTypeDef = Union[FilterCriteriaTypeDef, FilterCriteriaOutputTypeDef]
PipeTargetTimestreamParametersOutputTypeDef = TypedDict(
    "PipeTargetTimestreamParametersOutputTypeDef",
    {
        "TimeValue": str,
        "VersionValue": str,
        "DimensionMappings": List[DimensionMappingTypeDef],
        "EpochTimeUnit": NotRequired[EpochTimeUnitType],
        "TimeFieldType": NotRequired[TimeFieldTypeType],
        "TimestampFormat": NotRequired[str],
        "SingleMeasureMappings": NotRequired[List[SingleMeasureMappingTypeDef]],
        "MultiMeasureMappings": NotRequired[List[MultiMeasureMappingOutputTypeDef]],
    },
)
MultiMeasureMappingUnionTypeDef = Union[
    MultiMeasureMappingTypeDef, MultiMeasureMappingOutputTypeDef
]
PipeEnrichmentParametersTypeDef = TypedDict(
    "PipeEnrichmentParametersTypeDef",
    {
        "InputTemplate": NotRequired[str],
        "HttpParameters": NotRequired[PipeEnrichmentHttpParametersUnionTypeDef],
    },
)
PipeSourceKinesisStreamParametersUnionTypeDef = Union[
    PipeSourceKinesisStreamParametersTypeDef, PipeSourceKinesisStreamParametersOutputTypeDef
]
PipeSourceParametersOutputTypeDef = TypedDict(
    "PipeSourceParametersOutputTypeDef",
    {
        "FilterCriteria": NotRequired[FilterCriteriaOutputTypeDef],
        "KinesisStreamParameters": NotRequired[PipeSourceKinesisStreamParametersOutputTypeDef],
        "DynamoDBStreamParameters": NotRequired[PipeSourceDynamoDBStreamParametersTypeDef],
        "SqsQueueParameters": NotRequired[PipeSourceSqsQueueParametersTypeDef],
        "ActiveMQBrokerParameters": NotRequired[PipeSourceActiveMQBrokerParametersTypeDef],
        "RabbitMQBrokerParameters": NotRequired[PipeSourceRabbitMQBrokerParametersTypeDef],
        "ManagedStreamingKafkaParameters": NotRequired[
            PipeSourceManagedStreamingKafkaParametersTypeDef
        ],
        "SelfManagedKafkaParameters": NotRequired[
            PipeSourceSelfManagedKafkaParametersOutputTypeDef
        ],
    },
)
PipeTargetSageMakerPipelineParametersUnionTypeDef = Union[
    PipeTargetSageMakerPipelineParametersTypeDef, PipeTargetSageMakerPipelineParametersOutputTypeDef
]
PipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "PipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "TopicName": str,
        "StartingPosition": NotRequired[SelfManagedKafkaStartPositionType],
        "AdditionalBootstrapServers": NotRequired[Sequence[str]],
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "ConsumerGroupID": NotRequired[str],
        "Credentials": NotRequired[SelfManagedKafkaAccessConfigurationCredentialsTypeDef],
        "ServerRootCaCertificate": NotRequired[str],
        "Vpc": NotRequired[SelfManagedKafkaAccessConfigurationVpcUnionTypeDef],
    },
)
UpdatePipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "Credentials": NotRequired[SelfManagedKafkaAccessConfigurationCredentialsTypeDef],
        "ServerRootCaCertificate": NotRequired[str],
        "Vpc": NotRequired[SelfManagedKafkaAccessConfigurationVpcUnionTypeDef],
    },
)
NetworkConfigurationUnionTypeDef = Union[
    NetworkConfigurationTypeDef, NetworkConfigurationOutputTypeDef
]
PipeTargetBatchJobParametersTypeDef = TypedDict(
    "PipeTargetBatchJobParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": NotRequired[BatchArrayPropertiesTypeDef],
        "RetryStrategy": NotRequired[BatchRetryStrategyTypeDef],
        "ContainerOverrides": NotRequired[BatchContainerOverridesUnionTypeDef],
        "DependsOn": NotRequired[Sequence[BatchJobDependencyTypeDef]],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
PipeTargetEcsTaskParametersOutputTypeDef = TypedDict(
    "PipeTargetEcsTaskParametersOutputTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": NotRequired[int],
        "LaunchType": NotRequired[LaunchTypeType],
        "NetworkConfiguration": NotRequired[NetworkConfigurationOutputTypeDef],
        "PlatformVersion": NotRequired[str],
        "Group": NotRequired[str],
        "CapacityProviderStrategy": NotRequired[List[CapacityProviderStrategyItemTypeDef]],
        "EnableECSManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "PlacementConstraints": NotRequired[List[PlacementConstraintTypeDef]],
        "PlacementStrategy": NotRequired[List[PlacementStrategyTypeDef]],
        "PropagateTags": NotRequired[Literal["TASK_DEFINITION"]],
        "ReferenceId": NotRequired[str],
        "Overrides": NotRequired[EcsTaskOverrideOutputTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
EcsTaskOverrideTypeDef = TypedDict(
    "EcsTaskOverrideTypeDef",
    {
        "ContainerOverrides": NotRequired[Sequence[EcsContainerOverrideUnionTypeDef]],
        "Cpu": NotRequired[str],
        "EphemeralStorage": NotRequired[EcsEphemeralStorageTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "InferenceAcceleratorOverrides": NotRequired[
            Sequence[EcsInferenceAcceleratorOverrideTypeDef]
        ],
        "Memory": NotRequired[str],
        "TaskRoleArn": NotRequired[str],
    },
)
PipeTargetTimestreamParametersTypeDef = TypedDict(
    "PipeTargetTimestreamParametersTypeDef",
    {
        "TimeValue": str,
        "VersionValue": str,
        "DimensionMappings": Sequence[DimensionMappingTypeDef],
        "EpochTimeUnit": NotRequired[EpochTimeUnitType],
        "TimeFieldType": NotRequired[TimeFieldTypeType],
        "TimestampFormat": NotRequired[str],
        "SingleMeasureMappings": NotRequired[Sequence[SingleMeasureMappingTypeDef]],
        "MultiMeasureMappings": NotRequired[Sequence[MultiMeasureMappingUnionTypeDef]],
    },
)
PipeSourceSelfManagedKafkaParametersUnionTypeDef = Union[
    PipeSourceSelfManagedKafkaParametersTypeDef, PipeSourceSelfManagedKafkaParametersOutputTypeDef
]
UpdatePipeSourceParametersTypeDef = TypedDict(
    "UpdatePipeSourceParametersTypeDef",
    {
        "FilterCriteria": NotRequired[FilterCriteriaUnionTypeDef],
        "KinesisStreamParameters": NotRequired[UpdatePipeSourceKinesisStreamParametersTypeDef],
        "DynamoDBStreamParameters": NotRequired[UpdatePipeSourceDynamoDBStreamParametersTypeDef],
        "SqsQueueParameters": NotRequired[UpdatePipeSourceSqsQueueParametersTypeDef],
        "ActiveMQBrokerParameters": NotRequired[UpdatePipeSourceActiveMQBrokerParametersTypeDef],
        "RabbitMQBrokerParameters": NotRequired[UpdatePipeSourceRabbitMQBrokerParametersTypeDef],
        "ManagedStreamingKafkaParameters": NotRequired[
            UpdatePipeSourceManagedStreamingKafkaParametersTypeDef
        ],
        "SelfManagedKafkaParameters": NotRequired[
            UpdatePipeSourceSelfManagedKafkaParametersTypeDef
        ],
    },
)
PipeTargetBatchJobParametersUnionTypeDef = Union[
    PipeTargetBatchJobParametersTypeDef, PipeTargetBatchJobParametersOutputTypeDef
]
PipeTargetParametersOutputTypeDef = TypedDict(
    "PipeTargetParametersOutputTypeDef",
    {
        "InputTemplate": NotRequired[str],
        "LambdaFunctionParameters": NotRequired[PipeTargetLambdaFunctionParametersTypeDef],
        "StepFunctionStateMachineParameters": NotRequired[PipeTargetStateMachineParametersTypeDef],
        "KinesisStreamParameters": NotRequired[PipeTargetKinesisStreamParametersTypeDef],
        "EcsTaskParameters": NotRequired[PipeTargetEcsTaskParametersOutputTypeDef],
        "BatchJobParameters": NotRequired[PipeTargetBatchJobParametersOutputTypeDef],
        "SqsQueueParameters": NotRequired[PipeTargetSqsQueueParametersTypeDef],
        "HttpParameters": NotRequired[PipeTargetHttpParametersOutputTypeDef],
        "RedshiftDataParameters": NotRequired[PipeTargetRedshiftDataParametersOutputTypeDef],
        "SageMakerPipelineParameters": NotRequired[
            PipeTargetSageMakerPipelineParametersOutputTypeDef
        ],
        "EventBridgeEventBusParameters": NotRequired[
            PipeTargetEventBridgeEventBusParametersOutputTypeDef
        ],
        "CloudWatchLogsParameters": NotRequired[PipeTargetCloudWatchLogsParametersTypeDef],
        "TimestreamParameters": NotRequired[PipeTargetTimestreamParametersOutputTypeDef],
    },
)
EcsTaskOverrideUnionTypeDef = Union[EcsTaskOverrideTypeDef, EcsTaskOverrideOutputTypeDef]
PipeTargetTimestreamParametersUnionTypeDef = Union[
    PipeTargetTimestreamParametersTypeDef, PipeTargetTimestreamParametersOutputTypeDef
]
PipeSourceParametersTypeDef = TypedDict(
    "PipeSourceParametersTypeDef",
    {
        "FilterCriteria": NotRequired[FilterCriteriaUnionTypeDef],
        "KinesisStreamParameters": NotRequired[PipeSourceKinesisStreamParametersUnionTypeDef],
        "DynamoDBStreamParameters": NotRequired[PipeSourceDynamoDBStreamParametersTypeDef],
        "SqsQueueParameters": NotRequired[PipeSourceSqsQueueParametersTypeDef],
        "ActiveMQBrokerParameters": NotRequired[PipeSourceActiveMQBrokerParametersTypeDef],
        "RabbitMQBrokerParameters": NotRequired[PipeSourceRabbitMQBrokerParametersTypeDef],
        "ManagedStreamingKafkaParameters": NotRequired[
            PipeSourceManagedStreamingKafkaParametersTypeDef
        ],
        "SelfManagedKafkaParameters": NotRequired[PipeSourceSelfManagedKafkaParametersUnionTypeDef],
    },
)
DescribePipeResponseTypeDef = TypedDict(
    "DescribePipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "CurrentState": PipeStateType,
        "StateReason": str,
        "Source": str,
        "SourceParameters": PipeSourceParametersOutputTypeDef,
        "Enrichment": str,
        "EnrichmentParameters": PipeEnrichmentParametersOutputTypeDef,
        "Target": str,
        "TargetParameters": PipeTargetParametersOutputTypeDef,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LogConfiguration": PipeLogConfigurationTypeDef,
        "KmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PipeTargetEcsTaskParametersTypeDef = TypedDict(
    "PipeTargetEcsTaskParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": NotRequired[int],
        "LaunchType": NotRequired[LaunchTypeType],
        "NetworkConfiguration": NotRequired[NetworkConfigurationUnionTypeDef],
        "PlatformVersion": NotRequired[str],
        "Group": NotRequired[str],
        "CapacityProviderStrategy": NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]],
        "EnableECSManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "PlacementConstraints": NotRequired[Sequence[PlacementConstraintTypeDef]],
        "PlacementStrategy": NotRequired[Sequence[PlacementStrategyTypeDef]],
        "PropagateTags": NotRequired[Literal["TASK_DEFINITION"]],
        "ReferenceId": NotRequired[str],
        "Overrides": NotRequired[EcsTaskOverrideUnionTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PipeTargetEcsTaskParametersUnionTypeDef = Union[
    PipeTargetEcsTaskParametersTypeDef, PipeTargetEcsTaskParametersOutputTypeDef
]
PipeTargetParametersTypeDef = TypedDict(
    "PipeTargetParametersTypeDef",
    {
        "InputTemplate": NotRequired[str],
        "LambdaFunctionParameters": NotRequired[PipeTargetLambdaFunctionParametersTypeDef],
        "StepFunctionStateMachineParameters": NotRequired[PipeTargetStateMachineParametersTypeDef],
        "KinesisStreamParameters": NotRequired[PipeTargetKinesisStreamParametersTypeDef],
        "EcsTaskParameters": NotRequired[PipeTargetEcsTaskParametersUnionTypeDef],
        "BatchJobParameters": NotRequired[PipeTargetBatchJobParametersUnionTypeDef],
        "SqsQueueParameters": NotRequired[PipeTargetSqsQueueParametersTypeDef],
        "HttpParameters": NotRequired[PipeTargetHttpParametersUnionTypeDef],
        "RedshiftDataParameters": NotRequired[PipeTargetRedshiftDataParametersUnionTypeDef],
        "SageMakerPipelineParameters": NotRequired[
            PipeTargetSageMakerPipelineParametersUnionTypeDef
        ],
        "EventBridgeEventBusParameters": NotRequired[
            PipeTargetEventBridgeEventBusParametersUnionTypeDef
        ],
        "CloudWatchLogsParameters": NotRequired[PipeTargetCloudWatchLogsParametersTypeDef],
        "TimestreamParameters": NotRequired[PipeTargetTimestreamParametersUnionTypeDef],
    },
)
CreatePipeRequestRequestTypeDef = TypedDict(
    "CreatePipeRequestRequestTypeDef",
    {
        "Name": str,
        "Source": str,
        "Target": str,
        "RoleArn": str,
        "Description": NotRequired[str],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "SourceParameters": NotRequired[PipeSourceParametersTypeDef],
        "Enrichment": NotRequired[str],
        "EnrichmentParameters": NotRequired[PipeEnrichmentParametersTypeDef],
        "TargetParameters": NotRequired[PipeTargetParametersTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "LogConfiguration": NotRequired[PipeLogConfigurationParametersTypeDef],
        "KmsKeyIdentifier": NotRequired[str],
    },
)
UpdatePipeRequestRequestTypeDef = TypedDict(
    "UpdatePipeRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Description": NotRequired[str],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "SourceParameters": NotRequired[UpdatePipeSourceParametersTypeDef],
        "Enrichment": NotRequired[str],
        "EnrichmentParameters": NotRequired[PipeEnrichmentParametersTypeDef],
        "Target": NotRequired[str],
        "TargetParameters": NotRequired[PipeTargetParametersTypeDef],
        "LogConfiguration": NotRequired[PipeLogConfigurationParametersTypeDef],
        "KmsKeyIdentifier": NotRequired[str],
    },
)
