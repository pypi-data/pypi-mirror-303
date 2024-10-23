"""
Type annotations for synthetics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_synthetics/type_defs/)

Usage::

    ```python
    from mypy_boto3_synthetics.type_defs import S3EncryptionConfigTypeDef

    data: S3EncryptionConfigTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    CanaryRunStateReasonCodeType,
    CanaryRunStateType,
    CanaryStateReasonCodeType,
    CanaryStateType,
    EncryptionModeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "S3EncryptionConfigTypeDef",
    "AssociateResourceRequestRequestTypeDef",
    "BaseScreenshotOutputTypeDef",
    "BaseScreenshotTypeDef",
    "BlobTypeDef",
    "CanaryCodeOutputTypeDef",
    "CanaryRunConfigInputTypeDef",
    "CanaryRunConfigOutputTypeDef",
    "CanaryRunStatusTypeDef",
    "CanaryRunTimelineTypeDef",
    "CanaryScheduleInputTypeDef",
    "CanaryScheduleOutputTypeDef",
    "CanaryStatusTypeDef",
    "CanaryTimelineTypeDef",
    "VpcConfigOutputTypeDef",
    "VpcConfigInputTypeDef",
    "ResponseMetadataTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "GroupTypeDef",
    "DeleteCanaryRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DescribeCanariesLastRunRequestRequestTypeDef",
    "DescribeCanariesRequestRequestTypeDef",
    "DescribeRuntimeVersionsRequestRequestTypeDef",
    "RuntimeVersionTypeDef",
    "DisassociateResourceRequestRequestTypeDef",
    "GetCanaryRequestRequestTypeDef",
    "GetCanaryRunsRequestRequestTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GroupSummaryTypeDef",
    "ListAssociatedGroupsRequestRequestTypeDef",
    "ListGroupResourcesRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StartCanaryRequestRequestTypeDef",
    "StopCanaryRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ArtifactConfigInputTypeDef",
    "ArtifactConfigOutputTypeDef",
    "VisualReferenceOutputTypeDef",
    "BaseScreenshotUnionTypeDef",
    "CanaryCodeInputTypeDef",
    "CanaryRunTypeDef",
    "ListGroupResourcesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "GetGroupResponseTypeDef",
    "DescribeRuntimeVersionsResponseTypeDef",
    "ListAssociatedGroupsResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "CanaryTypeDef",
    "VisualReferenceInputTypeDef",
    "CreateCanaryRequestRequestTypeDef",
    "CanaryLastRunTypeDef",
    "GetCanaryRunsResponseTypeDef",
    "CreateCanaryResponseTypeDef",
    "DescribeCanariesResponseTypeDef",
    "GetCanaryResponseTypeDef",
    "UpdateCanaryRequestRequestTypeDef",
    "DescribeCanariesLastRunResponseTypeDef",
)

S3EncryptionConfigTypeDef = TypedDict(
    "S3EncryptionConfigTypeDef",
    {
        "EncryptionMode": NotRequired[EncryptionModeType],
        "KmsKeyArn": NotRequired[str],
    },
)
AssociateResourceRequestRequestTypeDef = TypedDict(
    "AssociateResourceRequestRequestTypeDef",
    {
        "GroupIdentifier": str,
        "ResourceArn": str,
    },
)
BaseScreenshotOutputTypeDef = TypedDict(
    "BaseScreenshotOutputTypeDef",
    {
        "ScreenshotName": str,
        "IgnoreCoordinates": NotRequired[List[str]],
    },
)
BaseScreenshotTypeDef = TypedDict(
    "BaseScreenshotTypeDef",
    {
        "ScreenshotName": str,
        "IgnoreCoordinates": NotRequired[Sequence[str]],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CanaryCodeOutputTypeDef = TypedDict(
    "CanaryCodeOutputTypeDef",
    {
        "SourceLocationArn": NotRequired[str],
        "Handler": NotRequired[str],
    },
)
CanaryRunConfigInputTypeDef = TypedDict(
    "CanaryRunConfigInputTypeDef",
    {
        "TimeoutInSeconds": NotRequired[int],
        "MemoryInMB": NotRequired[int],
        "ActiveTracing": NotRequired[bool],
        "EnvironmentVariables": NotRequired[Mapping[str, str]],
    },
)
CanaryRunConfigOutputTypeDef = TypedDict(
    "CanaryRunConfigOutputTypeDef",
    {
        "TimeoutInSeconds": NotRequired[int],
        "MemoryInMB": NotRequired[int],
        "ActiveTracing": NotRequired[bool],
    },
)
CanaryRunStatusTypeDef = TypedDict(
    "CanaryRunStatusTypeDef",
    {
        "State": NotRequired[CanaryRunStateType],
        "StateReason": NotRequired[str],
        "StateReasonCode": NotRequired[CanaryRunStateReasonCodeType],
    },
)
CanaryRunTimelineTypeDef = TypedDict(
    "CanaryRunTimelineTypeDef",
    {
        "Started": NotRequired[datetime],
        "Completed": NotRequired[datetime],
    },
)
CanaryScheduleInputTypeDef = TypedDict(
    "CanaryScheduleInputTypeDef",
    {
        "Expression": str,
        "DurationInSeconds": NotRequired[int],
    },
)
CanaryScheduleOutputTypeDef = TypedDict(
    "CanaryScheduleOutputTypeDef",
    {
        "Expression": NotRequired[str],
        "DurationInSeconds": NotRequired[int],
    },
)
CanaryStatusTypeDef = TypedDict(
    "CanaryStatusTypeDef",
    {
        "State": NotRequired[CanaryStateType],
        "StateReason": NotRequired[str],
        "StateReasonCode": NotRequired[CanaryStateReasonCodeType],
    },
)
CanaryTimelineTypeDef = TypedDict(
    "CanaryTimelineTypeDef",
    {
        "Created": NotRequired[datetime],
        "LastModified": NotRequired[datetime],
        "LastStarted": NotRequired[datetime],
        "LastStopped": NotRequired[datetime],
    },
)
VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
    },
)
VpcConfigInputTypeDef = TypedDict(
    "VpcConfigInputTypeDef",
    {
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
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
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)
DeleteCanaryRequestRequestTypeDef = TypedDict(
    "DeleteCanaryRequestRequestTypeDef",
    {
        "Name": str,
        "DeleteLambda": NotRequired[bool],
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupIdentifier": str,
    },
)
DescribeCanariesLastRunRequestRequestTypeDef = TypedDict(
    "DescribeCanariesLastRunRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Names": NotRequired[Sequence[str]],
    },
)
DescribeCanariesRequestRequestTypeDef = TypedDict(
    "DescribeCanariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Names": NotRequired[Sequence[str]],
    },
)
DescribeRuntimeVersionsRequestRequestTypeDef = TypedDict(
    "DescribeRuntimeVersionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RuntimeVersionTypeDef = TypedDict(
    "RuntimeVersionTypeDef",
    {
        "VersionName": NotRequired[str],
        "Description": NotRequired[str],
        "ReleaseDate": NotRequired[datetime],
        "DeprecationDate": NotRequired[datetime],
    },
)
DisassociateResourceRequestRequestTypeDef = TypedDict(
    "DisassociateResourceRequestRequestTypeDef",
    {
        "GroupIdentifier": str,
        "ResourceArn": str,
    },
)
GetCanaryRequestRequestTypeDef = TypedDict(
    "GetCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetCanaryRunsRequestRequestTypeDef = TypedDict(
    "GetCanaryRunsRequestRequestTypeDef",
    {
        "Name": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupIdentifier": str,
    },
)
GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
    },
)
ListAssociatedGroupsRequestRequestTypeDef = TypedDict(
    "ListAssociatedGroupsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListGroupResourcesRequestRequestTypeDef = TypedDict(
    "ListGroupResourcesRequestRequestTypeDef",
    {
        "GroupIdentifier": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
StartCanaryRequestRequestTypeDef = TypedDict(
    "StartCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StopCanaryRequestRequestTypeDef = TypedDict(
    "StopCanaryRequestRequestTypeDef",
    {
        "Name": str,
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
ArtifactConfigInputTypeDef = TypedDict(
    "ArtifactConfigInputTypeDef",
    {
        "S3Encryption": NotRequired[S3EncryptionConfigTypeDef],
    },
)
ArtifactConfigOutputTypeDef = TypedDict(
    "ArtifactConfigOutputTypeDef",
    {
        "S3Encryption": NotRequired[S3EncryptionConfigTypeDef],
    },
)
VisualReferenceOutputTypeDef = TypedDict(
    "VisualReferenceOutputTypeDef",
    {
        "BaseScreenshots": NotRequired[List[BaseScreenshotOutputTypeDef]],
        "BaseCanaryRunId": NotRequired[str],
    },
)
BaseScreenshotUnionTypeDef = Union[BaseScreenshotTypeDef, BaseScreenshotOutputTypeDef]
CanaryCodeInputTypeDef = TypedDict(
    "CanaryCodeInputTypeDef",
    {
        "Handler": str,
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3Version": NotRequired[str],
        "ZipFile": NotRequired[BlobTypeDef],
    },
)
CanaryRunTypeDef = TypedDict(
    "CanaryRunTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[CanaryRunStatusTypeDef],
        "Timeline": NotRequired[CanaryRunTimelineTypeDef],
        "ArtifactS3Location": NotRequired[str],
    },
)
ListGroupResourcesResponseTypeDef = TypedDict(
    "ListGroupResourcesResponseTypeDef",
    {
        "Resources": List[str],
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
CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRuntimeVersionsResponseTypeDef = TypedDict(
    "DescribeRuntimeVersionsResponseTypeDef",
    {
        "RuntimeVersions": List[RuntimeVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAssociatedGroupsResponseTypeDef = TypedDict(
    "ListAssociatedGroupsResponseTypeDef",
    {
        "Groups": List[GroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List[GroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CanaryTypeDef = TypedDict(
    "CanaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Code": NotRequired[CanaryCodeOutputTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "Schedule": NotRequired[CanaryScheduleOutputTypeDef],
        "RunConfig": NotRequired[CanaryRunConfigOutputTypeDef],
        "SuccessRetentionPeriodInDays": NotRequired[int],
        "FailureRetentionPeriodInDays": NotRequired[int],
        "Status": NotRequired[CanaryStatusTypeDef],
        "Timeline": NotRequired[CanaryTimelineTypeDef],
        "ArtifactS3Location": NotRequired[str],
        "EngineArn": NotRequired[str],
        "RuntimeVersion": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigOutputTypeDef],
        "VisualReference": NotRequired[VisualReferenceOutputTypeDef],
        "Tags": NotRequired[Dict[str, str]],
        "ArtifactConfig": NotRequired[ArtifactConfigOutputTypeDef],
    },
)
VisualReferenceInputTypeDef = TypedDict(
    "VisualReferenceInputTypeDef",
    {
        "BaseCanaryRunId": str,
        "BaseScreenshots": NotRequired[Sequence[BaseScreenshotUnionTypeDef]],
    },
)
CreateCanaryRequestRequestTypeDef = TypedDict(
    "CreateCanaryRequestRequestTypeDef",
    {
        "Name": str,
        "Code": CanaryCodeInputTypeDef,
        "ArtifactS3Location": str,
        "ExecutionRoleArn": str,
        "Schedule": CanaryScheduleInputTypeDef,
        "RuntimeVersion": str,
        "RunConfig": NotRequired[CanaryRunConfigInputTypeDef],
        "SuccessRetentionPeriodInDays": NotRequired[int],
        "FailureRetentionPeriodInDays": NotRequired[int],
        "VpcConfig": NotRequired[VpcConfigInputTypeDef],
        "ResourcesToReplicateTags": NotRequired[Sequence[Literal["lambda-function"]]],
        "Tags": NotRequired[Mapping[str, str]],
        "ArtifactConfig": NotRequired[ArtifactConfigInputTypeDef],
    },
)
CanaryLastRunTypeDef = TypedDict(
    "CanaryLastRunTypeDef",
    {
        "CanaryName": NotRequired[str],
        "LastRun": NotRequired[CanaryRunTypeDef],
    },
)
GetCanaryRunsResponseTypeDef = TypedDict(
    "GetCanaryRunsResponseTypeDef",
    {
        "CanaryRuns": List[CanaryRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateCanaryResponseTypeDef = TypedDict(
    "CreateCanaryResponseTypeDef",
    {
        "Canary": CanaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCanariesResponseTypeDef = TypedDict(
    "DescribeCanariesResponseTypeDef",
    {
        "Canaries": List[CanaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetCanaryResponseTypeDef = TypedDict(
    "GetCanaryResponseTypeDef",
    {
        "Canary": CanaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCanaryRequestRequestTypeDef = TypedDict(
    "UpdateCanaryRequestRequestTypeDef",
    {
        "Name": str,
        "Code": NotRequired[CanaryCodeInputTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "RuntimeVersion": NotRequired[str],
        "Schedule": NotRequired[CanaryScheduleInputTypeDef],
        "RunConfig": NotRequired[CanaryRunConfigInputTypeDef],
        "SuccessRetentionPeriodInDays": NotRequired[int],
        "FailureRetentionPeriodInDays": NotRequired[int],
        "VpcConfig": NotRequired[VpcConfigInputTypeDef],
        "VisualReference": NotRequired[VisualReferenceInputTypeDef],
        "ArtifactS3Location": NotRequired[str],
        "ArtifactConfig": NotRequired[ArtifactConfigInputTypeDef],
    },
)
DescribeCanariesLastRunResponseTypeDef = TypedDict(
    "DescribeCanariesLastRunResponseTypeDef",
    {
        "CanariesLastRun": List[CanaryLastRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
