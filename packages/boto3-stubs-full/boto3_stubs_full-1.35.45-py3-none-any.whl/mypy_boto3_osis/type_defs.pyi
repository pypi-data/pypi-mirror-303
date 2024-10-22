"""
Type annotations for osis service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/type_defs/)

Usage::

    ```python
    from mypy_boto3_osis.type_defs import BufferOptionsTypeDef

    data: BufferOptionsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    ChangeProgressStageStatusesType,
    ChangeProgressStatusesType,
    PipelineStatusType,
    VpcEndpointManagementType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BufferOptionsTypeDef",
    "ChangeProgressStageTypeDef",
    "CloudWatchLogDestinationTypeDef",
    "EncryptionAtRestOptionsTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "GetPipelineBlueprintRequestRequestTypeDef",
    "PipelineBlueprintTypeDef",
    "GetPipelineChangeProgressRequestRequestTypeDef",
    "GetPipelineRequestRequestTypeDef",
    "PipelineBlueprintSummaryTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PipelineDestinationTypeDef",
    "PipelineStatusReasonTypeDef",
    "ServiceVpcEndpointTypeDef",
    "StartPipelineRequestRequestTypeDef",
    "StopPipelineRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ValidatePipelineRequestRequestTypeDef",
    "ValidationMessageTypeDef",
    "VpcAttachmentOptionsTypeDef",
    "ChangeProgressStatusTypeDef",
    "LogPublishingOptionsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "GetPipelineBlueprintResponseTypeDef",
    "ListPipelineBlueprintsResponseTypeDef",
    "PipelineSummaryTypeDef",
    "ValidatePipelineResponseTypeDef",
    "VpcOptionsOutputTypeDef",
    "VpcOptionsTypeDef",
    "GetPipelineChangeProgressResponseTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "VpcEndpointTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "PipelineTypeDef",
    "CreatePipelineResponseTypeDef",
    "GetPipelineResponseTypeDef",
    "StartPipelineResponseTypeDef",
    "StopPipelineResponseTypeDef",
    "UpdatePipelineResponseTypeDef",
)

BufferOptionsTypeDef = TypedDict(
    "BufferOptionsTypeDef",
    {
        "PersistentBufferEnabled": bool,
    },
)
ChangeProgressStageTypeDef = TypedDict(
    "ChangeProgressStageTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[ChangeProgressStageStatusesType],
        "Description": NotRequired[str],
        "LastUpdatedAt": NotRequired[datetime],
    },
)
CloudWatchLogDestinationTypeDef = TypedDict(
    "CloudWatchLogDestinationTypeDef",
    {
        "LogGroup": str,
    },
)
EncryptionAtRestOptionsTypeDef = TypedDict(
    "EncryptionAtRestOptionsTypeDef",
    {
        "KmsKeyArn": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
GetPipelineBlueprintRequestRequestTypeDef = TypedDict(
    "GetPipelineBlueprintRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "Format": NotRequired[str],
    },
)
PipelineBlueprintTypeDef = TypedDict(
    "PipelineBlueprintTypeDef",
    {
        "BlueprintName": NotRequired[str],
        "PipelineConfigurationBody": NotRequired[str],
        "DisplayName": NotRequired[str],
        "DisplayDescription": NotRequired[str],
        "Service": NotRequired[str],
        "UseCase": NotRequired[str],
    },
)
GetPipelineChangeProgressRequestRequestTypeDef = TypedDict(
    "GetPipelineChangeProgressRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
GetPipelineRequestRequestTypeDef = TypedDict(
    "GetPipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
PipelineBlueprintSummaryTypeDef = TypedDict(
    "PipelineBlueprintSummaryTypeDef",
    {
        "BlueprintName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "DisplayDescription": NotRequired[str],
        "Service": NotRequired[str],
        "UseCase": NotRequired[str],
    },
)
ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
PipelineDestinationTypeDef = TypedDict(
    "PipelineDestinationTypeDef",
    {
        "ServiceName": NotRequired[str],
        "Endpoint": NotRequired[str],
    },
)
PipelineStatusReasonTypeDef = TypedDict(
    "PipelineStatusReasonTypeDef",
    {
        "Description": NotRequired[str],
    },
)
ServiceVpcEndpointTypeDef = TypedDict(
    "ServiceVpcEndpointTypeDef",
    {
        "ServiceName": NotRequired[Literal["OPENSEARCH_SERVERLESS"]],
        "VpcEndpointId": NotRequired[str],
    },
)
StartPipelineRequestRequestTypeDef = TypedDict(
    "StartPipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
StopPipelineRequestRequestTypeDef = TypedDict(
    "StopPipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": Sequence[str],
    },
)
ValidatePipelineRequestRequestTypeDef = TypedDict(
    "ValidatePipelineRequestRequestTypeDef",
    {
        "PipelineConfigurationBody": str,
    },
)
ValidationMessageTypeDef = TypedDict(
    "ValidationMessageTypeDef",
    {
        "Message": NotRequired[str],
    },
)
VpcAttachmentOptionsTypeDef = TypedDict(
    "VpcAttachmentOptionsTypeDef",
    {
        "AttachToVpc": bool,
        "CidrBlock": NotRequired[str],
    },
)
ChangeProgressStatusTypeDef = TypedDict(
    "ChangeProgressStatusTypeDef",
    {
        "StartTime": NotRequired[datetime],
        "Status": NotRequired[ChangeProgressStatusesType],
        "TotalNumberOfStages": NotRequired[int],
        "ChangeProgressStages": NotRequired[List[ChangeProgressStageTypeDef]],
    },
)
LogPublishingOptionsTypeDef = TypedDict(
    "LogPublishingOptionsTypeDef",
    {
        "IsLoggingEnabled": NotRequired[bool],
        "CloudWatchLogDestination": NotRequired[CloudWatchLogDestinationTypeDef],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPipelineBlueprintResponseTypeDef = TypedDict(
    "GetPipelineBlueprintResponseTypeDef",
    {
        "Blueprint": PipelineBlueprintTypeDef,
        "Format": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPipelineBlueprintsResponseTypeDef = TypedDict(
    "ListPipelineBlueprintsResponseTypeDef",
    {
        "Blueprints": List[PipelineBlueprintSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "Status": NotRequired[PipelineStatusType],
        "StatusReason": NotRequired[PipelineStatusReasonTypeDef],
        "PipelineName": NotRequired[str],
        "PipelineArn": NotRequired[str],
        "MinUnits": NotRequired[int],
        "MaxUnits": NotRequired[int],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Destinations": NotRequired[List[PipelineDestinationTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ValidatePipelineResponseTypeDef = TypedDict(
    "ValidatePipelineResponseTypeDef",
    {
        "isValid": bool,
        "Errors": List[ValidationMessageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpcOptionsOutputTypeDef = TypedDict(
    "VpcOptionsOutputTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "VpcAttachmentOptions": NotRequired[VpcAttachmentOptionsTypeDef],
        "VpcEndpointManagement": NotRequired[VpcEndpointManagementType],
    },
)
VpcOptionsTypeDef = TypedDict(
    "VpcOptionsTypeDef",
    {
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "VpcAttachmentOptions": NotRequired[VpcAttachmentOptionsTypeDef],
        "VpcEndpointManagement": NotRequired[VpcEndpointManagementType],
    },
)
GetPipelineChangeProgressResponseTypeDef = TypedDict(
    "GetPipelineChangeProgressResponseTypeDef",
    {
        "ChangeProgressStatuses": List[ChangeProgressStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipelineRequestRequestTypeDef = TypedDict(
    "UpdatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "MinUnits": NotRequired[int],
        "MaxUnits": NotRequired[int],
        "PipelineConfigurationBody": NotRequired[str],
        "LogPublishingOptions": NotRequired[LogPublishingOptionsTypeDef],
        "BufferOptions": NotRequired[BufferOptionsTypeDef],
        "EncryptionAtRestOptions": NotRequired[EncryptionAtRestOptionsTypeDef],
    },
)
ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "Pipelines": List[PipelineSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcOptions": NotRequired[VpcOptionsOutputTypeDef],
    },
)
CreatePipelineRequestRequestTypeDef = TypedDict(
    "CreatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "MinUnits": int,
        "MaxUnits": int,
        "PipelineConfigurationBody": str,
        "LogPublishingOptions": NotRequired[LogPublishingOptionsTypeDef],
        "VpcOptions": NotRequired[VpcOptionsTypeDef],
        "BufferOptions": NotRequired[BufferOptionsTypeDef],
        "EncryptionAtRestOptions": NotRequired[EncryptionAtRestOptionsTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "PipelineName": NotRequired[str],
        "PipelineArn": NotRequired[str],
        "MinUnits": NotRequired[int],
        "MaxUnits": NotRequired[int],
        "Status": NotRequired[PipelineStatusType],
        "StatusReason": NotRequired[PipelineStatusReasonTypeDef],
        "PipelineConfigurationBody": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "IngestEndpointUrls": NotRequired[List[str]],
        "LogPublishingOptions": NotRequired[LogPublishingOptionsTypeDef],
        "VpcEndpoints": NotRequired[List[VpcEndpointTypeDef]],
        "BufferOptions": NotRequired[BufferOptionsTypeDef],
        "EncryptionAtRestOptions": NotRequired[EncryptionAtRestOptionsTypeDef],
        "VpcEndpointService": NotRequired[str],
        "ServiceVpcEndpoints": NotRequired[List[ServiceVpcEndpointTypeDef]],
        "Destinations": NotRequired[List[PipelineDestinationTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPipelineResponseTypeDef = TypedDict(
    "GetPipelineResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartPipelineResponseTypeDef = TypedDict(
    "StartPipelineResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopPipelineResponseTypeDef = TypedDict(
    "StopPipelineResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipelineResponseTypeDef = TypedDict(
    "UpdatePipelineResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
