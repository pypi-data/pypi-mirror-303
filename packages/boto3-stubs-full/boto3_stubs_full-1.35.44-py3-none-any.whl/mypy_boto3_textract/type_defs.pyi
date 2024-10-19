"""
Type annotations for textract service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_textract/type_defs/)

Usage::

    ```python
    from mypy_boto3_textract.type_defs import AdapterOverviewTypeDef

    data: AdapterOverviewTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AdapterVersionStatusType,
    AutoUpdateType,
    BlockTypeType,
    ContentClassifierType,
    EntityTypeType,
    FeatureTypeType,
    JobStatusType,
    RelationshipTypeType,
    SelectionStatusType,
    TextTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AdapterOverviewTypeDef",
    "AdapterTypeDef",
    "S3ObjectTypeDef",
    "EvaluationMetricTypeDef",
    "AdapterVersionOverviewTypeDef",
    "DocumentMetadataTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "ResponseMetadataTypeDef",
    "NormalizedValueTypeDef",
    "BlobTypeDef",
    "QueryOutputTypeDef",
    "RelationshipTypeDef",
    "BoundingBoxTypeDef",
    "CreateAdapterRequestRequestTypeDef",
    "OutputConfigTypeDef",
    "DeleteAdapterRequestRequestTypeDef",
    "DeleteAdapterVersionRequestRequestTypeDef",
    "DetectedSignatureTypeDef",
    "SplitDocumentTypeDef",
    "UndetectedSignatureTypeDef",
    "ExpenseCurrencyTypeDef",
    "ExpenseGroupPropertyTypeDef",
    "ExpenseTypeTypeDef",
    "PointTypeDef",
    "GetAdapterRequestRequestTypeDef",
    "GetAdapterVersionRequestRequestTypeDef",
    "GetDocumentAnalysisRequestRequestTypeDef",
    "WarningTypeDef",
    "GetDocumentTextDetectionRequestRequestTypeDef",
    "GetExpenseAnalysisRequestRequestTypeDef",
    "GetLendingAnalysisRequestRequestTypeDef",
    "GetLendingAnalysisSummaryRequestRequestTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NotificationChannelTypeDef",
    "PredictionTypeDef",
    "QueryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAdapterRequestRequestTypeDef",
    "AdaptersConfigTypeDef",
    "AdapterVersionDatasetConfigTypeDef",
    "DocumentLocationTypeDef",
    "AdapterVersionEvaluationMetricTypeDef",
    "CreateAdapterResponseTypeDef",
    "CreateAdapterVersionResponseTypeDef",
    "GetAdapterResponseTypeDef",
    "ListAdapterVersionsResponseTypeDef",
    "ListAdaptersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartDocumentAnalysisResponseTypeDef",
    "StartDocumentTextDetectionResponseTypeDef",
    "StartExpenseAnalysisResponseTypeDef",
    "StartLendingAnalysisResponseTypeDef",
    "UpdateAdapterResponseTypeDef",
    "AnalyzeIDDetectionsTypeDef",
    "DocumentTypeDef",
    "DocumentGroupTypeDef",
    "GeometryTypeDef",
    "HumanLoopConfigTypeDef",
    "ListAdapterVersionsRequestListAdapterVersionsPaginateTypeDef",
    "ListAdapterVersionsRequestRequestTypeDef",
    "ListAdaptersRequestListAdaptersPaginateTypeDef",
    "ListAdaptersRequestRequestTypeDef",
    "PageClassificationTypeDef",
    "QueryUnionTypeDef",
    "CreateAdapterVersionRequestRequestTypeDef",
    "StartDocumentTextDetectionRequestRequestTypeDef",
    "StartExpenseAnalysisRequestRequestTypeDef",
    "StartLendingAnalysisRequestRequestTypeDef",
    "GetAdapterVersionResponseTypeDef",
    "IdentityDocumentFieldTypeDef",
    "AnalyzeExpenseRequestRequestTypeDef",
    "AnalyzeIDRequestRequestTypeDef",
    "DetectDocumentTextRequestRequestTypeDef",
    "LendingSummaryTypeDef",
    "BlockTypeDef",
    "ExpenseDetectionTypeDef",
    "LendingDetectionTypeDef",
    "SignatureDetectionTypeDef",
    "QueriesConfigTypeDef",
    "GetLendingAnalysisSummaryResponseTypeDef",
    "AnalyzeDocumentResponseTypeDef",
    "DetectDocumentTextResponseTypeDef",
    "GetDocumentAnalysisResponseTypeDef",
    "GetDocumentTextDetectionResponseTypeDef",
    "IdentityDocumentTypeDef",
    "ExpenseFieldTypeDef",
    "LendingFieldTypeDef",
    "AnalyzeDocumentRequestRequestTypeDef",
    "StartDocumentAnalysisRequestRequestTypeDef",
    "AnalyzeIDResponseTypeDef",
    "LineItemFieldsTypeDef",
    "LendingDocumentTypeDef",
    "LineItemGroupTypeDef",
    "ExpenseDocumentTypeDef",
    "AnalyzeExpenseResponseTypeDef",
    "ExtractionTypeDef",
    "GetExpenseAnalysisResponseTypeDef",
    "LendingResultTypeDef",
    "GetLendingAnalysisResponseTypeDef",
)

AdapterOverviewTypeDef = TypedDict(
    "AdapterOverviewTypeDef",
    {
        "AdapterId": NotRequired[str],
        "AdapterName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "FeatureTypes": NotRequired[List[FeatureTypeType]],
    },
)
AdapterTypeDef = TypedDict(
    "AdapterTypeDef",
    {
        "AdapterId": str,
        "Version": str,
        "Pages": NotRequired[Sequence[str]],
    },
)
S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "Bucket": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
EvaluationMetricTypeDef = TypedDict(
    "EvaluationMetricTypeDef",
    {
        "F1Score": NotRequired[float],
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
    },
)
AdapterVersionOverviewTypeDef = TypedDict(
    "AdapterVersionOverviewTypeDef",
    {
        "AdapterId": NotRequired[str],
        "AdapterVersion": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "FeatureTypes": NotRequired[List[FeatureTypeType]],
        "Status": NotRequired[AdapterVersionStatusType],
        "StatusMessage": NotRequired[str],
    },
)
DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Pages": NotRequired[int],
    },
)
HumanLoopActivationOutputTypeDef = TypedDict(
    "HumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": NotRequired[str],
        "HumanLoopActivationReasons": NotRequired[List[str]],
        "HumanLoopActivationConditionsEvaluationResults": NotRequired[str],
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
NormalizedValueTypeDef = TypedDict(
    "NormalizedValueTypeDef",
    {
        "Value": NotRequired[str],
        "ValueType": NotRequired[Literal["DATE"]],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
QueryOutputTypeDef = TypedDict(
    "QueryOutputTypeDef",
    {
        "Text": str,
        "Alias": NotRequired[str],
        "Pages": NotRequired[List[str]],
    },
)
RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "Type": NotRequired[RelationshipTypeType],
        "Ids": NotRequired[List[str]],
    },
)
BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {
        "Width": NotRequired[float],
        "Height": NotRequired[float],
        "Left": NotRequired[float],
        "Top": NotRequired[float],
    },
)
CreateAdapterRequestRequestTypeDef = TypedDict(
    "CreateAdapterRequestRequestTypeDef",
    {
        "AdapterName": str,
        "FeatureTypes": Sequence[FeatureTypeType],
        "ClientRequestToken": NotRequired[str],
        "Description": NotRequired[str],
        "AutoUpdate": NotRequired[AutoUpdateType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Bucket": str,
        "S3Prefix": NotRequired[str],
    },
)
DeleteAdapterRequestRequestTypeDef = TypedDict(
    "DeleteAdapterRequestRequestTypeDef",
    {
        "AdapterId": str,
    },
)
DeleteAdapterVersionRequestRequestTypeDef = TypedDict(
    "DeleteAdapterVersionRequestRequestTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
    },
)
DetectedSignatureTypeDef = TypedDict(
    "DetectedSignatureTypeDef",
    {
        "Page": NotRequired[int],
    },
)
SplitDocumentTypeDef = TypedDict(
    "SplitDocumentTypeDef",
    {
        "Index": NotRequired[int],
        "Pages": NotRequired[List[int]],
    },
)
UndetectedSignatureTypeDef = TypedDict(
    "UndetectedSignatureTypeDef",
    {
        "Page": NotRequired[int],
    },
)
ExpenseCurrencyTypeDef = TypedDict(
    "ExpenseCurrencyTypeDef",
    {
        "Code": NotRequired[str],
        "Confidence": NotRequired[float],
    },
)
ExpenseGroupPropertyTypeDef = TypedDict(
    "ExpenseGroupPropertyTypeDef",
    {
        "Types": NotRequired[List[str]],
        "Id": NotRequired[str],
    },
)
ExpenseTypeTypeDef = TypedDict(
    "ExpenseTypeTypeDef",
    {
        "Text": NotRequired[str],
        "Confidence": NotRequired[float],
    },
)
PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": NotRequired[float],
        "Y": NotRequired[float],
    },
)
GetAdapterRequestRequestTypeDef = TypedDict(
    "GetAdapterRequestRequestTypeDef",
    {
        "AdapterId": str,
    },
)
GetAdapterVersionRequestRequestTypeDef = TypedDict(
    "GetAdapterVersionRequestRequestTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
    },
)
GetDocumentAnalysisRequestRequestTypeDef = TypedDict(
    "GetDocumentAnalysisRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "Pages": NotRequired[List[int]],
    },
)
GetDocumentTextDetectionRequestRequestTypeDef = TypedDict(
    "GetDocumentTextDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetExpenseAnalysisRequestRequestTypeDef = TypedDict(
    "GetExpenseAnalysisRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetLendingAnalysisRequestRequestTypeDef = TypedDict(
    "GetLendingAnalysisRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetLendingAnalysisSummaryRequestRequestTypeDef = TypedDict(
    "GetLendingAnalysisSummaryRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": NotRequired[Sequence[ContentClassifierType]],
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
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "SNSTopicArn": str,
        "RoleArn": str,
    },
)
PredictionTypeDef = TypedDict(
    "PredictionTypeDef",
    {
        "Value": NotRequired[str],
        "Confidence": NotRequired[float],
    },
)
QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "Text": str,
        "Alias": NotRequired[str],
        "Pages": NotRequired[Sequence[str]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAdapterRequestRequestTypeDef = TypedDict(
    "UpdateAdapterRequestRequestTypeDef",
    {
        "AdapterId": str,
        "Description": NotRequired[str],
        "AdapterName": NotRequired[str],
        "AutoUpdate": NotRequired[AutoUpdateType],
    },
)
AdaptersConfigTypeDef = TypedDict(
    "AdaptersConfigTypeDef",
    {
        "Adapters": Sequence[AdapterTypeDef],
    },
)
AdapterVersionDatasetConfigTypeDef = TypedDict(
    "AdapterVersionDatasetConfigTypeDef",
    {
        "ManifestS3Object": NotRequired[S3ObjectTypeDef],
    },
)
DocumentLocationTypeDef = TypedDict(
    "DocumentLocationTypeDef",
    {
        "S3Object": NotRequired[S3ObjectTypeDef],
    },
)
AdapterVersionEvaluationMetricTypeDef = TypedDict(
    "AdapterVersionEvaluationMetricTypeDef",
    {
        "Baseline": NotRequired[EvaluationMetricTypeDef],
        "AdapterVersion": NotRequired[EvaluationMetricTypeDef],
        "FeatureType": NotRequired[FeatureTypeType],
    },
)
CreateAdapterResponseTypeDef = TypedDict(
    "CreateAdapterResponseTypeDef",
    {
        "AdapterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAdapterVersionResponseTypeDef = TypedDict(
    "CreateAdapterVersionResponseTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAdapterResponseTypeDef = TypedDict(
    "GetAdapterResponseTypeDef",
    {
        "AdapterId": str,
        "AdapterName": str,
        "CreationTime": datetime,
        "Description": str,
        "FeatureTypes": List[FeatureTypeType],
        "AutoUpdate": AutoUpdateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAdapterVersionsResponseTypeDef = TypedDict(
    "ListAdapterVersionsResponseTypeDef",
    {
        "AdapterVersions": List[AdapterVersionOverviewTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAdaptersResponseTypeDef = TypedDict(
    "ListAdaptersResponseTypeDef",
    {
        "Adapters": List[AdapterOverviewTypeDef],
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
StartDocumentAnalysisResponseTypeDef = TypedDict(
    "StartDocumentAnalysisResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDocumentTextDetectionResponseTypeDef = TypedDict(
    "StartDocumentTextDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartExpenseAnalysisResponseTypeDef = TypedDict(
    "StartExpenseAnalysisResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartLendingAnalysisResponseTypeDef = TypedDict(
    "StartLendingAnalysisResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAdapterResponseTypeDef = TypedDict(
    "UpdateAdapterResponseTypeDef",
    {
        "AdapterId": str,
        "AdapterName": str,
        "CreationTime": datetime,
        "Description": str,
        "FeatureTypes": List[FeatureTypeType],
        "AutoUpdate": AutoUpdateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalyzeIDDetectionsTypeDef = TypedDict(
    "AnalyzeIDDetectionsTypeDef",
    {
        "Text": str,
        "NormalizedValue": NotRequired[NormalizedValueTypeDef],
        "Confidence": NotRequired[float],
    },
)
DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "Bytes": NotRequired[BlobTypeDef],
        "S3Object": NotRequired[S3ObjectTypeDef],
    },
)
DocumentGroupTypeDef = TypedDict(
    "DocumentGroupTypeDef",
    {
        "Type": NotRequired[str],
        "SplitDocuments": NotRequired[List[SplitDocumentTypeDef]],
        "DetectedSignatures": NotRequired[List[DetectedSignatureTypeDef]],
        "UndetectedSignatures": NotRequired[List[UndetectedSignatureTypeDef]],
    },
)
GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Polygon": NotRequired[List[PointTypeDef]],
    },
)
HumanLoopConfigTypeDef = TypedDict(
    "HumanLoopConfigTypeDef",
    {
        "HumanLoopName": str,
        "FlowDefinitionArn": str,
        "DataAttributes": NotRequired[HumanLoopDataAttributesTypeDef],
    },
)
ListAdapterVersionsRequestListAdapterVersionsPaginateTypeDef = TypedDict(
    "ListAdapterVersionsRequestListAdapterVersionsPaginateTypeDef",
    {
        "AdapterId": NotRequired[str],
        "AfterCreationTime": NotRequired[TimestampTypeDef],
        "BeforeCreationTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAdapterVersionsRequestRequestTypeDef = TypedDict(
    "ListAdapterVersionsRequestRequestTypeDef",
    {
        "AdapterId": NotRequired[str],
        "AfterCreationTime": NotRequired[TimestampTypeDef],
        "BeforeCreationTime": NotRequired[TimestampTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAdaptersRequestListAdaptersPaginateTypeDef = TypedDict(
    "ListAdaptersRequestListAdaptersPaginateTypeDef",
    {
        "AfterCreationTime": NotRequired[TimestampTypeDef],
        "BeforeCreationTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAdaptersRequestRequestTypeDef = TypedDict(
    "ListAdaptersRequestRequestTypeDef",
    {
        "AfterCreationTime": NotRequired[TimestampTypeDef],
        "BeforeCreationTime": NotRequired[TimestampTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PageClassificationTypeDef = TypedDict(
    "PageClassificationTypeDef",
    {
        "PageType": List[PredictionTypeDef],
        "PageNumber": List[PredictionTypeDef],
    },
)
QueryUnionTypeDef = Union[QueryTypeDef, QueryOutputTypeDef]
CreateAdapterVersionRequestRequestTypeDef = TypedDict(
    "CreateAdapterVersionRequestRequestTypeDef",
    {
        "AdapterId": str,
        "DatasetConfig": AdapterVersionDatasetConfigTypeDef,
        "OutputConfig": OutputConfigTypeDef,
        "ClientRequestToken": NotRequired[str],
        "KMSKeyId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
StartDocumentTextDetectionRequestRequestTypeDef = TypedDict(
    "StartDocumentTextDetectionRequestRequestTypeDef",
    {
        "DocumentLocation": DocumentLocationTypeDef,
        "ClientRequestToken": NotRequired[str],
        "JobTag": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "OutputConfig": NotRequired[OutputConfigTypeDef],
        "KMSKeyId": NotRequired[str],
    },
)
StartExpenseAnalysisRequestRequestTypeDef = TypedDict(
    "StartExpenseAnalysisRequestRequestTypeDef",
    {
        "DocumentLocation": DocumentLocationTypeDef,
        "ClientRequestToken": NotRequired[str],
        "JobTag": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "OutputConfig": NotRequired[OutputConfigTypeDef],
        "KMSKeyId": NotRequired[str],
    },
)
StartLendingAnalysisRequestRequestTypeDef = TypedDict(
    "StartLendingAnalysisRequestRequestTypeDef",
    {
        "DocumentLocation": DocumentLocationTypeDef,
        "ClientRequestToken": NotRequired[str],
        "JobTag": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "OutputConfig": NotRequired[OutputConfigTypeDef],
        "KMSKeyId": NotRequired[str],
    },
)
GetAdapterVersionResponseTypeDef = TypedDict(
    "GetAdapterVersionResponseTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
        "CreationTime": datetime,
        "FeatureTypes": List[FeatureTypeType],
        "Status": AdapterVersionStatusType,
        "StatusMessage": str,
        "DatasetConfig": AdapterVersionDatasetConfigTypeDef,
        "KMSKeyId": str,
        "OutputConfig": OutputConfigTypeDef,
        "EvaluationMetrics": List[AdapterVersionEvaluationMetricTypeDef],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IdentityDocumentFieldTypeDef = TypedDict(
    "IdentityDocumentFieldTypeDef",
    {
        "Type": NotRequired[AnalyzeIDDetectionsTypeDef],
        "ValueDetection": NotRequired[AnalyzeIDDetectionsTypeDef],
    },
)
AnalyzeExpenseRequestRequestTypeDef = TypedDict(
    "AnalyzeExpenseRequestRequestTypeDef",
    {
        "Document": DocumentTypeDef,
    },
)
AnalyzeIDRequestRequestTypeDef = TypedDict(
    "AnalyzeIDRequestRequestTypeDef",
    {
        "DocumentPages": Sequence[DocumentTypeDef],
    },
)
DetectDocumentTextRequestRequestTypeDef = TypedDict(
    "DetectDocumentTextRequestRequestTypeDef",
    {
        "Document": DocumentTypeDef,
    },
)
LendingSummaryTypeDef = TypedDict(
    "LendingSummaryTypeDef",
    {
        "DocumentGroups": NotRequired[List[DocumentGroupTypeDef]],
        "UndetectedDocumentTypes": NotRequired[List[str]],
    },
)
BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockType": NotRequired[BlockTypeType],
        "Confidence": NotRequired[float],
        "Text": NotRequired[str],
        "TextType": NotRequired[TextTypeType],
        "RowIndex": NotRequired[int],
        "ColumnIndex": NotRequired[int],
        "RowSpan": NotRequired[int],
        "ColumnSpan": NotRequired[int],
        "Geometry": NotRequired[GeometryTypeDef],
        "Id": NotRequired[str],
        "Relationships": NotRequired[List[RelationshipTypeDef]],
        "EntityTypes": NotRequired[List[EntityTypeType]],
        "SelectionStatus": NotRequired[SelectionStatusType],
        "Page": NotRequired[int],
        "Query": NotRequired[QueryOutputTypeDef],
    },
)
ExpenseDetectionTypeDef = TypedDict(
    "ExpenseDetectionTypeDef",
    {
        "Text": NotRequired[str],
        "Geometry": NotRequired[GeometryTypeDef],
        "Confidence": NotRequired[float],
    },
)
LendingDetectionTypeDef = TypedDict(
    "LendingDetectionTypeDef",
    {
        "Text": NotRequired[str],
        "SelectionStatus": NotRequired[SelectionStatusType],
        "Geometry": NotRequired[GeometryTypeDef],
        "Confidence": NotRequired[float],
    },
)
SignatureDetectionTypeDef = TypedDict(
    "SignatureDetectionTypeDef",
    {
        "Confidence": NotRequired[float],
        "Geometry": NotRequired[GeometryTypeDef],
    },
)
QueriesConfigTypeDef = TypedDict(
    "QueriesConfigTypeDef",
    {
        "Queries": Sequence[QueryUnionTypeDef],
    },
)
GetLendingAnalysisSummaryResponseTypeDef = TypedDict(
    "GetLendingAnalysisSummaryResponseTypeDef",
    {
        "DocumentMetadata": DocumentMetadataTypeDef,
        "JobStatus": JobStatusType,
        "Summary": LendingSummaryTypeDef,
        "Warnings": List[WarningTypeDef],
        "StatusMessage": str,
        "AnalyzeLendingModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalyzeDocumentResponseTypeDef = TypedDict(
    "AnalyzeDocumentResponseTypeDef",
    {
        "DocumentMetadata": DocumentMetadataTypeDef,
        "Blocks": List[BlockTypeDef],
        "HumanLoopActivationOutput": HumanLoopActivationOutputTypeDef,
        "AnalyzeDocumentModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectDocumentTextResponseTypeDef = TypedDict(
    "DetectDocumentTextResponseTypeDef",
    {
        "DocumentMetadata": DocumentMetadataTypeDef,
        "Blocks": List[BlockTypeDef],
        "DetectDocumentTextModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDocumentAnalysisResponseTypeDef = TypedDict(
    "GetDocumentAnalysisResponseTypeDef",
    {
        "DocumentMetadata": DocumentMetadataTypeDef,
        "JobStatus": JobStatusType,
        "Blocks": List[BlockTypeDef],
        "Warnings": List[WarningTypeDef],
        "StatusMessage": str,
        "AnalyzeDocumentModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDocumentTextDetectionResponseTypeDef = TypedDict(
    "GetDocumentTextDetectionResponseTypeDef",
    {
        "DocumentMetadata": DocumentMetadataTypeDef,
        "JobStatus": JobStatusType,
        "Blocks": List[BlockTypeDef],
        "Warnings": List[WarningTypeDef],
        "StatusMessage": str,
        "DetectDocumentTextModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
IdentityDocumentTypeDef = TypedDict(
    "IdentityDocumentTypeDef",
    {
        "DocumentIndex": NotRequired[int],
        "IdentityDocumentFields": NotRequired[List[IdentityDocumentFieldTypeDef]],
        "Blocks": NotRequired[List[BlockTypeDef]],
    },
)
ExpenseFieldTypeDef = TypedDict(
    "ExpenseFieldTypeDef",
    {
        "Type": NotRequired[ExpenseTypeTypeDef],
        "LabelDetection": NotRequired[ExpenseDetectionTypeDef],
        "ValueDetection": NotRequired[ExpenseDetectionTypeDef],
        "PageNumber": NotRequired[int],
        "Currency": NotRequired[ExpenseCurrencyTypeDef],
        "GroupProperties": NotRequired[List[ExpenseGroupPropertyTypeDef]],
    },
)
LendingFieldTypeDef = TypedDict(
    "LendingFieldTypeDef",
    {
        "Type": NotRequired[str],
        "KeyDetection": NotRequired[LendingDetectionTypeDef],
        "ValueDetections": NotRequired[List[LendingDetectionTypeDef]],
    },
)
AnalyzeDocumentRequestRequestTypeDef = TypedDict(
    "AnalyzeDocumentRequestRequestTypeDef",
    {
        "Document": DocumentTypeDef,
        "FeatureTypes": Sequence[FeatureTypeType],
        "HumanLoopConfig": NotRequired[HumanLoopConfigTypeDef],
        "QueriesConfig": NotRequired[QueriesConfigTypeDef],
        "AdaptersConfig": NotRequired[AdaptersConfigTypeDef],
    },
)
StartDocumentAnalysisRequestRequestTypeDef = TypedDict(
    "StartDocumentAnalysisRequestRequestTypeDef",
    {
        "DocumentLocation": DocumentLocationTypeDef,
        "FeatureTypes": Sequence[FeatureTypeType],
        "ClientRequestToken": NotRequired[str],
        "JobTag": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "OutputConfig": NotRequired[OutputConfigTypeDef],
        "KMSKeyId": NotRequired[str],
        "QueriesConfig": NotRequired[QueriesConfigTypeDef],
        "AdaptersConfig": NotRequired[AdaptersConfigTypeDef],
    },
)
AnalyzeIDResponseTypeDef = TypedDict(
    "AnalyzeIDResponseTypeDef",
    {
        "IdentityDocuments": List[IdentityDocumentTypeDef],
        "DocumentMetadata": DocumentMetadataTypeDef,
        "AnalyzeIDModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LineItemFieldsTypeDef = TypedDict(
    "LineItemFieldsTypeDef",
    {
        "LineItemExpenseFields": NotRequired[List[ExpenseFieldTypeDef]],
    },
)
LendingDocumentTypeDef = TypedDict(
    "LendingDocumentTypeDef",
    {
        "LendingFields": NotRequired[List[LendingFieldTypeDef]],
        "SignatureDetections": NotRequired[List[SignatureDetectionTypeDef]],
    },
)
LineItemGroupTypeDef = TypedDict(
    "LineItemGroupTypeDef",
    {
        "LineItemGroupIndex": NotRequired[int],
        "LineItems": NotRequired[List[LineItemFieldsTypeDef]],
    },
)
ExpenseDocumentTypeDef = TypedDict(
    "ExpenseDocumentTypeDef",
    {
        "ExpenseIndex": NotRequired[int],
        "SummaryFields": NotRequired[List[ExpenseFieldTypeDef]],
        "LineItemGroups": NotRequired[List[LineItemGroupTypeDef]],
        "Blocks": NotRequired[List[BlockTypeDef]],
    },
)
AnalyzeExpenseResponseTypeDef = TypedDict(
    "AnalyzeExpenseResponseTypeDef",
    {
        "DocumentMetadata": DocumentMetadataTypeDef,
        "ExpenseDocuments": List[ExpenseDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExtractionTypeDef = TypedDict(
    "ExtractionTypeDef",
    {
        "LendingDocument": NotRequired[LendingDocumentTypeDef],
        "ExpenseDocument": NotRequired[ExpenseDocumentTypeDef],
        "IdentityDocument": NotRequired[IdentityDocumentTypeDef],
    },
)
GetExpenseAnalysisResponseTypeDef = TypedDict(
    "GetExpenseAnalysisResponseTypeDef",
    {
        "DocumentMetadata": DocumentMetadataTypeDef,
        "JobStatus": JobStatusType,
        "ExpenseDocuments": List[ExpenseDocumentTypeDef],
        "Warnings": List[WarningTypeDef],
        "StatusMessage": str,
        "AnalyzeExpenseModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LendingResultTypeDef = TypedDict(
    "LendingResultTypeDef",
    {
        "Page": NotRequired[int],
        "PageClassification": NotRequired[PageClassificationTypeDef],
        "Extractions": NotRequired[List[ExtractionTypeDef]],
    },
)
GetLendingAnalysisResponseTypeDef = TypedDict(
    "GetLendingAnalysisResponseTypeDef",
    {
        "DocumentMetadata": DocumentMetadataTypeDef,
        "JobStatus": JobStatusType,
        "Results": List[LendingResultTypeDef],
        "Warnings": List[WarningTypeDef],
        "StatusMessage": str,
        "AnalyzeLendingModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
