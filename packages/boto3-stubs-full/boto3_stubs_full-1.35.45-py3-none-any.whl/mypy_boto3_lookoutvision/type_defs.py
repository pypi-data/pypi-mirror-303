"""
Type annotations for lookoutvision service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/type_defs/)

Usage::

    ```python
    from mypy_boto3_lookoutvision.type_defs import PixelAnomalyTypeDef

    data: PixelAnomalyTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    DatasetStatusType,
    ModelHostingStatusType,
    ModelPackagingJobStatusType,
    ModelStatusType,
    TargetPlatformArchType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "PixelAnomalyTypeDef",
    "BlobTypeDef",
    "DatasetMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "ProjectMetadataTypeDef",
    "DatasetImageStatsTypeDef",
    "InputS3ObjectTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeModelPackagingJobRequestRequestTypeDef",
    "DescribeModelRequestRequestTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "ImageSourceTypeDef",
    "S3LocationTypeDef",
    "TargetPlatformTypeDef",
    "GreengrassOutputDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "ListModelPackagingJobsRequestRequestTypeDef",
    "ModelPackagingJobMetadataTypeDef",
    "ListModelsRequestRequestTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ModelPerformanceTypeDef",
    "OutputS3ObjectTypeDef",
    "StartModelRequestRequestTypeDef",
    "StopModelRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AnomalyTypeDef",
    "DetectAnomaliesRequestRequestTypeDef",
    "UpdateDatasetEntriesRequestRequestTypeDef",
    "ProjectDescriptionTypeDef",
    "CreateDatasetResponseTypeDef",
    "DeleteModelResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "StartModelPackagingJobResponseTypeDef",
    "StartModelResponseTypeDef",
    "StopModelResponseTypeDef",
    "UpdateDatasetEntriesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetGroundTruthManifestTypeDef",
    "OutputConfigTypeDef",
    "GreengrassConfigurationOutputTypeDef",
    "GreengrassConfigurationTypeDef",
    "ModelPackagingOutputDetailsTypeDef",
    "ListModelPackagingJobsRequestListModelPackagingJobsPaginateTypeDef",
    "ListModelsRequestListModelsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef",
    "ListDatasetEntriesRequestRequestTypeDef",
    "ListModelPackagingJobsResponseTypeDef",
    "ModelMetadataTypeDef",
    "DetectAnomalyResultTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DatasetSourceTypeDef",
    "CreateModelRequestRequestTypeDef",
    "ModelDescriptionTypeDef",
    "ModelPackagingConfigurationOutputTypeDef",
    "GreengrassConfigurationUnionTypeDef",
    "CreateModelResponseTypeDef",
    "ListModelsResponseTypeDef",
    "DetectAnomaliesResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "DescribeModelResponseTypeDef",
    "ModelPackagingDescriptionTypeDef",
    "ModelPackagingConfigurationTypeDef",
    "DescribeModelPackagingJobResponseTypeDef",
    "StartModelPackagingJobRequestRequestTypeDef",
)

PixelAnomalyTypeDef = TypedDict(
    "PixelAnomalyTypeDef",
    {
        "TotalPercentageArea": NotRequired[float],
        "Color": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "DatasetType": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Status": NotRequired[DatasetStatusType],
        "StatusMessage": NotRequired[str],
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ClientToken": NotRequired[str],
    },
)
ProjectMetadataTypeDef = TypedDict(
    "ProjectMetadataTypeDef",
    {
        "ProjectArn": NotRequired[str],
        "ProjectName": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
    },
)
DatasetImageStatsTypeDef = TypedDict(
    "DatasetImageStatsTypeDef",
    {
        "Total": NotRequired[int],
        "Labeled": NotRequired[int],
        "Normal": NotRequired[int],
        "Anomaly": NotRequired[int],
    },
)
InputS3ObjectTypeDef = TypedDict(
    "InputS3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "ClientToken": NotRequired[str],
    },
)
DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "ClientToken": NotRequired[str],
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ClientToken": NotRequired[str],
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)
DescribeModelPackagingJobRequestRequestTypeDef = TypedDict(
    "DescribeModelPackagingJobRequestRequestTypeDef",
    {
        "ProjectName": str,
        "JobName": str,
    },
)
DescribeModelRequestRequestTypeDef = TypedDict(
    "DescribeModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
    },
)
DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)
ImageSourceTypeDef = TypedDict(
    "ImageSourceTypeDef",
    {
        "Type": NotRequired[str],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": str,
        "Prefix": NotRequired[str],
    },
)
TargetPlatformTypeDef = TypedDict(
    "TargetPlatformTypeDef",
    {
        "Os": Literal["LINUX"],
        "Arch": TargetPlatformArchType,
        "Accelerator": NotRequired[Literal["NVIDIA"]],
    },
)
GreengrassOutputDetailsTypeDef = TypedDict(
    "GreengrassOutputDetailsTypeDef",
    {
        "ComponentVersionArn": NotRequired[str],
        "ComponentName": NotRequired[str],
        "ComponentVersion": NotRequired[str],
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
TimestampTypeDef = Union[datetime, str]
ListModelPackagingJobsRequestRequestTypeDef = TypedDict(
    "ListModelPackagingJobsRequestRequestTypeDef",
    {
        "ProjectName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ModelPackagingJobMetadataTypeDef = TypedDict(
    "ModelPackagingJobMetadataTypeDef",
    {
        "JobName": NotRequired[str],
        "ProjectName": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "ModelPackagingJobDescription": NotRequired[str],
        "ModelPackagingMethod": NotRequired[str],
        "Status": NotRequired[ModelPackagingJobStatusType],
        "StatusMessage": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
ListModelsRequestRequestTypeDef = TypedDict(
    "ListModelsRequestRequestTypeDef",
    {
        "ProjectName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
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
ModelPerformanceTypeDef = TypedDict(
    "ModelPerformanceTypeDef",
    {
        "F1Score": NotRequired[float],
        "Recall": NotRequired[float],
        "Precision": NotRequired[float],
    },
)
OutputS3ObjectTypeDef = TypedDict(
    "OutputS3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
StartModelRequestRequestTypeDef = TypedDict(
    "StartModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "MinInferenceUnits": int,
        "ClientToken": NotRequired[str],
        "MaxInferenceUnits": NotRequired[int],
    },
)
StopModelRequestRequestTypeDef = TypedDict(
    "StopModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "ClientToken": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "Name": NotRequired[str],
        "PixelAnomaly": NotRequired[PixelAnomalyTypeDef],
    },
)
DetectAnomaliesRequestRequestTypeDef = TypedDict(
    "DetectAnomaliesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "Body": BlobTypeDef,
        "ContentType": str,
    },
)
UpdateDatasetEntriesRequestRequestTypeDef = TypedDict(
    "UpdateDatasetEntriesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "Changes": BlobTypeDef,
        "ClientToken": NotRequired[str],
    },
)
ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": NotRequired[str],
        "ProjectName": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Datasets": NotRequired[List[DatasetMetadataTypeDef]],
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetMetadata": DatasetMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteModelResponseTypeDef = TypedDict(
    "DeleteModelResponseTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetEntriesResponseTypeDef = TypedDict(
    "ListDatasetEntriesResponseTypeDef",
    {
        "DatasetEntries": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartModelPackagingJobResponseTypeDef = TypedDict(
    "StartModelPackagingJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartModelResponseTypeDef = TypedDict(
    "StartModelResponseTypeDef",
    {
        "Status": ModelHostingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopModelResponseTypeDef = TypedDict(
    "StopModelResponseTypeDef",
    {
        "Status": ModelHostingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDatasetEntriesResponseTypeDef = TypedDict(
    "UpdateDatasetEntriesResponseTypeDef",
    {
        "Status": DatasetStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "ProjectMetadata": ProjectMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "Projects": List[ProjectMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DatasetDescriptionTypeDef = TypedDict(
    "DatasetDescriptionTypeDef",
    {
        "ProjectName": NotRequired[str],
        "DatasetType": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Status": NotRequired[DatasetStatusType],
        "StatusMessage": NotRequired[str],
        "ImageStats": NotRequired[DatasetImageStatsTypeDef],
    },
)
DatasetGroundTruthManifestTypeDef = TypedDict(
    "DatasetGroundTruthManifestTypeDef",
    {
        "S3Object": NotRequired[InputS3ObjectTypeDef],
    },
)
OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Location": S3LocationTypeDef,
    },
)
GreengrassConfigurationOutputTypeDef = TypedDict(
    "GreengrassConfigurationOutputTypeDef",
    {
        "S3OutputLocation": S3LocationTypeDef,
        "ComponentName": str,
        "CompilerOptions": NotRequired[str],
        "TargetDevice": NotRequired[Literal["jetson_xavier"]],
        "TargetPlatform": NotRequired[TargetPlatformTypeDef],
        "ComponentVersion": NotRequired[str],
        "ComponentDescription": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
GreengrassConfigurationTypeDef = TypedDict(
    "GreengrassConfigurationTypeDef",
    {
        "S3OutputLocation": S3LocationTypeDef,
        "ComponentName": str,
        "CompilerOptions": NotRequired[str],
        "TargetDevice": NotRequired[Literal["jetson_xavier"]],
        "TargetPlatform": NotRequired[TargetPlatformTypeDef],
        "ComponentVersion": NotRequired[str],
        "ComponentDescription": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ModelPackagingOutputDetailsTypeDef = TypedDict(
    "ModelPackagingOutputDetailsTypeDef",
    {
        "Greengrass": NotRequired[GreengrassOutputDetailsTypeDef],
    },
)
ListModelPackagingJobsRequestListModelPackagingJobsPaginateTypeDef = TypedDict(
    "ListModelPackagingJobsRequestListModelPackagingJobsPaginateTypeDef",
    {
        "ProjectName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListModelsRequestListModelsPaginateTypeDef = TypedDict(
    "ListModelsRequestListModelsPaginateTypeDef",
    {
        "ProjectName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef = TypedDict(
    "ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "Labeled": NotRequired[bool],
        "AnomalyClass": NotRequired[str],
        "BeforeCreationDate": NotRequired[TimestampTypeDef],
        "AfterCreationDate": NotRequired[TimestampTypeDef],
        "SourceRefContains": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetEntriesRequestRequestTypeDef = TypedDict(
    "ListDatasetEntriesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "Labeled": NotRequired[bool],
        "AnomalyClass": NotRequired[str],
        "BeforeCreationDate": NotRequired[TimestampTypeDef],
        "AfterCreationDate": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SourceRefContains": NotRequired[str],
    },
)
ListModelPackagingJobsResponseTypeDef = TypedDict(
    "ListModelPackagingJobsResponseTypeDef",
    {
        "ModelPackagingJobs": List[ModelPackagingJobMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ModelMetadataTypeDef = TypedDict(
    "ModelMetadataTypeDef",
    {
        "CreationTimestamp": NotRequired[datetime],
        "ModelVersion": NotRequired[str],
        "ModelArn": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[ModelStatusType],
        "StatusMessage": NotRequired[str],
        "Performance": NotRequired[ModelPerformanceTypeDef],
    },
)
DetectAnomalyResultTypeDef = TypedDict(
    "DetectAnomalyResultTypeDef",
    {
        "Source": NotRequired[ImageSourceTypeDef],
        "IsAnomalous": NotRequired[bool],
        "Confidence": NotRequired[float],
        "Anomalies": NotRequired[List[AnomalyTypeDef]],
        "AnomalyMask": NotRequired[bytes],
    },
)
DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "ProjectDescription": ProjectDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetDescription": DatasetDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetSourceTypeDef = TypedDict(
    "DatasetSourceTypeDef",
    {
        "GroundTruthManifest": NotRequired[DatasetGroundTruthManifestTypeDef],
    },
)
CreateModelRequestRequestTypeDef = TypedDict(
    "CreateModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "OutputConfig": OutputConfigTypeDef,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ModelDescriptionTypeDef = TypedDict(
    "ModelDescriptionTypeDef",
    {
        "ModelVersion": NotRequired[str],
        "ModelArn": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Description": NotRequired[str],
        "Status": NotRequired[ModelStatusType],
        "StatusMessage": NotRequired[str],
        "Performance": NotRequired[ModelPerformanceTypeDef],
        "OutputConfig": NotRequired[OutputConfigTypeDef],
        "EvaluationManifest": NotRequired[OutputS3ObjectTypeDef],
        "EvaluationResult": NotRequired[OutputS3ObjectTypeDef],
        "EvaluationEndTimestamp": NotRequired[datetime],
        "KmsKeyId": NotRequired[str],
        "MinInferenceUnits": NotRequired[int],
        "MaxInferenceUnits": NotRequired[int],
    },
)
ModelPackagingConfigurationOutputTypeDef = TypedDict(
    "ModelPackagingConfigurationOutputTypeDef",
    {
        "Greengrass": GreengrassConfigurationOutputTypeDef,
    },
)
GreengrassConfigurationUnionTypeDef = Union[
    GreengrassConfigurationTypeDef, GreengrassConfigurationOutputTypeDef
]
CreateModelResponseTypeDef = TypedDict(
    "CreateModelResponseTypeDef",
    {
        "ModelMetadata": ModelMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListModelsResponseTypeDef = TypedDict(
    "ListModelsResponseTypeDef",
    {
        "Models": List[ModelMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DetectAnomaliesResponseTypeDef = TypedDict(
    "DetectAnomaliesResponseTypeDef",
    {
        "DetectAnomalyResult": DetectAnomalyResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "DatasetSource": NotRequired[DatasetSourceTypeDef],
        "ClientToken": NotRequired[str],
    },
)
DescribeModelResponseTypeDef = TypedDict(
    "DescribeModelResponseTypeDef",
    {
        "ModelDescription": ModelDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModelPackagingDescriptionTypeDef = TypedDict(
    "ModelPackagingDescriptionTypeDef",
    {
        "JobName": NotRequired[str],
        "ProjectName": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "ModelPackagingConfiguration": NotRequired[ModelPackagingConfigurationOutputTypeDef],
        "ModelPackagingJobDescription": NotRequired[str],
        "ModelPackagingMethod": NotRequired[str],
        "ModelPackagingOutputDetails": NotRequired[ModelPackagingOutputDetailsTypeDef],
        "Status": NotRequired[ModelPackagingJobStatusType],
        "StatusMessage": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
ModelPackagingConfigurationTypeDef = TypedDict(
    "ModelPackagingConfigurationTypeDef",
    {
        "Greengrass": GreengrassConfigurationUnionTypeDef,
    },
)
DescribeModelPackagingJobResponseTypeDef = TypedDict(
    "DescribeModelPackagingJobResponseTypeDef",
    {
        "ModelPackagingDescription": ModelPackagingDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartModelPackagingJobRequestRequestTypeDef = TypedDict(
    "StartModelPackagingJobRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "Configuration": ModelPackagingConfigurationTypeDef,
        "JobName": NotRequired[str],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
