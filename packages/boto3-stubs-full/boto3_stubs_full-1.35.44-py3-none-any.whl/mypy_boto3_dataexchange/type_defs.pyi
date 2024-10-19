"""
Type annotations for dataexchange service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/type_defs/)

Usage::

    ```python
    from mypy_boto3_dataexchange.type_defs import AcceptDataGrantRequestRequestTypeDef

    data: AcceptDataGrantRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AcceptanceStateFilterValueType,
    AssetTypeType,
    CodeType,
    DataGrantAcceptanceStateType,
    GrantDistributionScopeType,
    JobErrorLimitNameType,
    JobErrorResourceTypesType,
    LFPermissionType,
    LFResourceTypeType,
    NotificationTypeType,
    OriginType,
    SchemaChangeTypeType,
    ServerSideEncryptionTypesType,
    StateType,
    TableTagPolicyLFPermissionType,
    TypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptDataGrantRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ApiGatewayApiAssetTypeDef",
    "AssetDestinationEntryTypeDef",
    "RedshiftDataShareAssetTypeDef",
    "S3SnapshotAssetTypeDef",
    "AssetSourceEntryTypeDef",
    "AutoExportRevisionDestinationEntryTypeDef",
    "ExportServerSideEncryptionTypeDef",
    "CancelJobRequestRequestTypeDef",
    "TimestampTypeDef",
    "CreateDataSetRequestRequestTypeDef",
    "OriginDetailsTypeDef",
    "CreateRevisionRequestRequestTypeDef",
    "DataGrantSummaryEntryTypeDef",
    "LFTagOutputTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeleteDataGrantRequestRequestTypeDef",
    "DeleteDataSetRequestRequestTypeDef",
    "DeleteEventActionRequestRequestTypeDef",
    "DeleteRevisionRequestRequestTypeDef",
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    "RevisionPublishedTypeDef",
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    "ExportAssetToSignedUrlResponseDetailsTypeDef",
    "RevisionDestinationEntryTypeDef",
    "GetAssetRequestRequestTypeDef",
    "GetDataGrantRequestRequestTypeDef",
    "GetDataSetRequestRequestTypeDef",
    "GetEventActionRequestRequestTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetReceivedDataGrantRequestRequestTypeDef",
    "GetRevisionRequestRequestTypeDef",
    "ImportAssetFromApiGatewayApiRequestDetailsTypeDef",
    "ImportAssetFromApiGatewayApiResponseDetailsTypeDef",
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    "ImportAssetFromSignedUrlResponseDetailsTypeDef",
    "RedshiftDataShareAssetSourceEntryTypeDef",
    "KmsKeyToGrantTypeDef",
    "LFTagTypeDef",
    "LakeFormationTagPolicyDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "ListDataGrantsRequestRequestTypeDef",
    "ListDataSetRevisionsRequestRequestTypeDef",
    "RevisionEntryTypeDef",
    "ListDataSetsRequestRequestTypeDef",
    "ListEventActionsRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListReceivedDataGrantsRequestRequestTypeDef",
    "ReceivedDataGrantSummariesEntryTypeDef",
    "ListRevisionAssetsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RedshiftDataShareDetailsTypeDef",
    "RevokeRevisionRequestRequestTypeDef",
    "S3DataAccessDetailsTypeDef",
    "SchemaChangeDetailsTypeDef",
    "SendApiAssetRequestRequestTypeDef",
    "StartJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAssetRequestRequestTypeDef",
    "UpdateDataSetRequestRequestTypeDef",
    "UpdateRevisionRequestRequestTypeDef",
    "AcceptDataGrantResponseTypeDef",
    "CreateDataGrantResponseTypeDef",
    "CreateRevisionResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDataGrantResponseTypeDef",
    "GetReceivedDataGrantResponseTypeDef",
    "GetRevisionResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RevokeRevisionResponseTypeDef",
    "SendApiAssetResponseTypeDef",
    "UpdateRevisionResponseTypeDef",
    "ImportAssetsFromS3RequestDetailsTypeDef",
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    "AutoExportRevisionToS3RequestDetailsTypeDef",
    "ExportAssetsToS3RequestDetailsTypeDef",
    "ExportAssetsToS3ResponseDetailsTypeDef",
    "CreateDataGrantRequestRequestTypeDef",
    "DataUpdateRequestDetailsTypeDef",
    "DeprecationRequestDetailsTypeDef",
    "CreateDataSetResponseTypeDef",
    "DataSetEntryTypeDef",
    "GetDataSetResponseTypeDef",
    "UpdateDataSetResponseTypeDef",
    "ListDataGrantsResponseTypeDef",
    "DatabaseLFTagPolicyAndPermissionsOutputTypeDef",
    "DatabaseLFTagPolicyTypeDef",
    "TableLFTagPolicyAndPermissionsOutputTypeDef",
    "TableLFTagPolicyTypeDef",
    "DetailsTypeDef",
    "EventTypeDef",
    "ExportRevisionsToS3RequestDetailsTypeDef",
    "ExportRevisionsToS3ResponseDetailsTypeDef",
    "ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef",
    "ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef",
    "S3DataAccessAssetSourceEntryOutputTypeDef",
    "S3DataAccessAssetSourceEntryTypeDef",
    "S3DataAccessAssetTypeDef",
    "LFTagUnionTypeDef",
    "TableLFTagPolicyAndPermissionsTypeDef",
    "ListDataGrantsRequestListDataGrantsPaginateTypeDef",
    "ListDataSetRevisionsRequestListDataSetRevisionsPaginateTypeDef",
    "ListDataSetsRequestListDataSetsPaginateTypeDef",
    "ListEventActionsRequestListEventActionsPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListReceivedDataGrantsRequestListReceivedDataGrantsPaginateTypeDef",
    "ListRevisionAssetsRequestListRevisionAssetsPaginateTypeDef",
    "ListDataSetRevisionsResponseTypeDef",
    "ListReceivedDataGrantsResponseTypeDef",
    "ScopeDetailsTypeDef",
    "SchemaChangeRequestDetailsTypeDef",
    "ActionTypeDef",
    "ListDataSetsResponseTypeDef",
    "ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef",
    "LFResourceDetailsTypeDef",
    "JobErrorTypeDef",
    "CreateS3DataAccessFromS3BucketResponseDetailsTypeDef",
    "S3DataAccessAssetSourceEntryUnionTypeDef",
    "DatabaseLFTagPolicyAndPermissionsTypeDef",
    "TableLFTagPolicyAndPermissionsUnionTypeDef",
    "NotificationDetailsTypeDef",
    "CreateEventActionRequestRequestTypeDef",
    "CreateEventActionResponseTypeDef",
    "EventActionEntryTypeDef",
    "GetEventActionResponseTypeDef",
    "UpdateEventActionRequestRequestTypeDef",
    "UpdateEventActionResponseTypeDef",
    "LFTagPolicyDetailsTypeDef",
    "ResponseDetailsTypeDef",
    "CreateS3DataAccessFromS3BucketRequestDetailsTypeDef",
    "DatabaseLFTagPolicyAndPermissionsUnionTypeDef",
    "SendDataSetNotificationRequestRequestTypeDef",
    "ListEventActionsResponseTypeDef",
    "LakeFormationDataPermissionDetailsTypeDef",
    "CreateJobResponseTypeDef",
    "GetJobResponseTypeDef",
    "JobEntryTypeDef",
    "ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef",
    "LakeFormationDataPermissionAssetTypeDef",
    "ListJobsResponseTypeDef",
    "RequestDetailsTypeDef",
    "AssetDetailsTypeDef",
    "CreateJobRequestRequestTypeDef",
    "AssetEntryTypeDef",
    "GetAssetResponseTypeDef",
    "UpdateAssetResponseTypeDef",
    "ListRevisionAssetsResponseTypeDef",
)

AcceptDataGrantRequestRequestTypeDef = TypedDict(
    "AcceptDataGrantRequestRequestTypeDef",
    {
        "DataGrantArn": str,
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
ApiGatewayApiAssetTypeDef = TypedDict(
    "ApiGatewayApiAssetTypeDef",
    {
        "ApiDescription": NotRequired[str],
        "ApiEndpoint": NotRequired[str],
        "ApiId": NotRequired[str],
        "ApiKey": NotRequired[str],
        "ApiName": NotRequired[str],
        "ApiSpecificationDownloadUrl": NotRequired[str],
        "ApiSpecificationDownloadUrlExpiresAt": NotRequired[datetime],
        "ProtocolType": NotRequired[Literal["REST"]],
        "Stage": NotRequired[str],
    },
)
AssetDestinationEntryTypeDef = TypedDict(
    "AssetDestinationEntryTypeDef",
    {
        "AssetId": str,
        "Bucket": str,
        "Key": NotRequired[str],
    },
)
RedshiftDataShareAssetTypeDef = TypedDict(
    "RedshiftDataShareAssetTypeDef",
    {
        "Arn": str,
    },
)
S3SnapshotAssetTypeDef = TypedDict(
    "S3SnapshotAssetTypeDef",
    {
        "Size": float,
    },
)
AssetSourceEntryTypeDef = TypedDict(
    "AssetSourceEntryTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
AutoExportRevisionDestinationEntryTypeDef = TypedDict(
    "AutoExportRevisionDestinationEntryTypeDef",
    {
        "Bucket": str,
        "KeyPattern": NotRequired[str],
    },
)
ExportServerSideEncryptionTypeDef = TypedDict(
    "ExportServerSideEncryptionTypeDef",
    {
        "Type": ServerSideEncryptionTypesType,
        "KmsKeyArn": NotRequired[str],
    },
)
CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
TimestampTypeDef = Union[datetime, str]
CreateDataSetRequestRequestTypeDef = TypedDict(
    "CreateDataSetRequestRequestTypeDef",
    {
        "AssetType": AssetTypeType,
        "Description": str,
        "Name": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
OriginDetailsTypeDef = TypedDict(
    "OriginDetailsTypeDef",
    {
        "ProductId": NotRequired[str],
        "DataGrantId": NotRequired[str],
    },
)
CreateRevisionRequestRequestTypeDef = TypedDict(
    "CreateRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "Comment": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DataGrantSummaryEntryTypeDef = TypedDict(
    "DataGrantSummaryEntryTypeDef",
    {
        "Name": str,
        "SenderPrincipal": str,
        "ReceiverPrincipal": str,
        "AcceptanceState": DataGrantAcceptanceStateType,
        "DataSetId": str,
        "SourceDataSetId": str,
        "Id": str,
        "Arn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "AcceptedAt": NotRequired[datetime],
        "EndsAt": NotRequired[datetime],
    },
)
LFTagOutputTypeDef = TypedDict(
    "LFTagOutputTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)
DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)
DeleteDataGrantRequestRequestTypeDef = TypedDict(
    "DeleteDataGrantRequestRequestTypeDef",
    {
        "DataGrantId": str,
    },
)
DeleteDataSetRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)
DeleteEventActionRequestRequestTypeDef = TypedDict(
    "DeleteEventActionRequestRequestTypeDef",
    {
        "EventActionId": str,
    },
)
DeleteRevisionRequestRequestTypeDef = TypedDict(
    "DeleteRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
    },
)
ImportAssetFromSignedUrlJobErrorDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    {
        "AssetName": str,
    },
)
RevisionPublishedTypeDef = TypedDict(
    "RevisionPublishedTypeDef",
    {
        "DataSetId": str,
    },
)
ExportAssetToSignedUrlRequestDetailsTypeDef = TypedDict(
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)
ExportAssetToSignedUrlResponseDetailsTypeDef = TypedDict(
    "ExportAssetToSignedUrlResponseDetailsTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
        "SignedUrl": NotRequired[str],
        "SignedUrlExpiresAt": NotRequired[datetime],
    },
)
RevisionDestinationEntryTypeDef = TypedDict(
    "RevisionDestinationEntryTypeDef",
    {
        "Bucket": str,
        "RevisionId": str,
        "KeyPattern": NotRequired[str],
    },
)
GetAssetRequestRequestTypeDef = TypedDict(
    "GetAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)
GetDataGrantRequestRequestTypeDef = TypedDict(
    "GetDataGrantRequestRequestTypeDef",
    {
        "DataGrantId": str,
    },
)
GetDataSetRequestRequestTypeDef = TypedDict(
    "GetDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)
GetEventActionRequestRequestTypeDef = TypedDict(
    "GetEventActionRequestRequestTypeDef",
    {
        "EventActionId": str,
    },
)
GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
GetReceivedDataGrantRequestRequestTypeDef = TypedDict(
    "GetReceivedDataGrantRequestRequestTypeDef",
    {
        "DataGrantArn": str,
    },
)
GetRevisionRequestRequestTypeDef = TypedDict(
    "GetRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
    },
)
ImportAssetFromApiGatewayApiRequestDetailsTypeDef = TypedDict(
    "ImportAssetFromApiGatewayApiRequestDetailsTypeDef",
    {
        "ApiId": str,
        "ApiName": str,
        "ApiSpecificationMd5Hash": str,
        "DataSetId": str,
        "ProtocolType": Literal["REST"],
        "RevisionId": str,
        "Stage": str,
        "ApiDescription": NotRequired[str],
        "ApiKey": NotRequired[str],
    },
)
ImportAssetFromApiGatewayApiResponseDetailsTypeDef = TypedDict(
    "ImportAssetFromApiGatewayApiResponseDetailsTypeDef",
    {
        "ApiId": str,
        "ApiName": str,
        "ApiSpecificationMd5Hash": str,
        "ApiSpecificationUploadUrl": str,
        "ApiSpecificationUploadUrlExpiresAt": datetime,
        "DataSetId": str,
        "ProtocolType": Literal["REST"],
        "RevisionId": str,
        "Stage": str,
        "ApiDescription": NotRequired[str],
        "ApiKey": NotRequired[str],
    },
)
ImportAssetFromSignedUrlRequestDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "Md5Hash": str,
        "RevisionId": str,
    },
)
ImportAssetFromSignedUrlResponseDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlResponseDetailsTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "RevisionId": str,
        "Md5Hash": NotRequired[str],
        "SignedUrl": NotRequired[str],
        "SignedUrlExpiresAt": NotRequired[datetime],
    },
)
RedshiftDataShareAssetSourceEntryTypeDef = TypedDict(
    "RedshiftDataShareAssetSourceEntryTypeDef",
    {
        "DataShareArn": str,
    },
)
KmsKeyToGrantTypeDef = TypedDict(
    "KmsKeyToGrantTypeDef",
    {
        "KmsKeyArn": str,
    },
)
LFTagTypeDef = TypedDict(
    "LFTagTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
    },
)
LakeFormationTagPolicyDetailsTypeDef = TypedDict(
    "LakeFormationTagPolicyDetailsTypeDef",
    {
        "Database": NotRequired[str],
        "Table": NotRequired[str],
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
ListDataGrantsRequestRequestTypeDef = TypedDict(
    "ListDataGrantsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDataSetRevisionsRequestRequestTypeDef = TypedDict(
    "ListDataSetRevisionsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RevisionEntryTypeDef = TypedDict(
    "RevisionEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "UpdatedAt": datetime,
        "Comment": NotRequired[str],
        "Finalized": NotRequired[bool],
        "SourceId": NotRequired[str],
        "RevocationComment": NotRequired[str],
        "Revoked": NotRequired[bool],
        "RevokedAt": NotRequired[datetime],
    },
)
ListDataSetsRequestRequestTypeDef = TypedDict(
    "ListDataSetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Origin": NotRequired[str],
    },
)
ListEventActionsRequestRequestTypeDef = TypedDict(
    "ListEventActionsRequestRequestTypeDef",
    {
        "EventSourceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "DataSetId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "RevisionId": NotRequired[str],
    },
)
ListReceivedDataGrantsRequestRequestTypeDef = TypedDict(
    "ListReceivedDataGrantsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AcceptanceState": NotRequired[Sequence[AcceptanceStateFilterValueType]],
    },
)
ReceivedDataGrantSummariesEntryTypeDef = TypedDict(
    "ReceivedDataGrantSummariesEntryTypeDef",
    {
        "Name": str,
        "SenderPrincipal": str,
        "ReceiverPrincipal": str,
        "AcceptanceState": DataGrantAcceptanceStateType,
        "DataSetId": str,
        "Id": str,
        "Arn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "AcceptedAt": NotRequired[datetime],
        "EndsAt": NotRequired[datetime],
    },
)
ListRevisionAssetsRequestRequestTypeDef = TypedDict(
    "ListRevisionAssetsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
RedshiftDataShareDetailsTypeDef = TypedDict(
    "RedshiftDataShareDetailsTypeDef",
    {
        "Arn": str,
        "Database": str,
        "Function": NotRequired[str],
        "Table": NotRequired[str],
        "Schema": NotRequired[str],
        "View": NotRequired[str],
    },
)
RevokeRevisionRequestRequestTypeDef = TypedDict(
    "RevokeRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
        "RevocationComment": str,
    },
)
S3DataAccessDetailsTypeDef = TypedDict(
    "S3DataAccessDetailsTypeDef",
    {
        "KeyPrefixes": NotRequired[Sequence[str]],
        "Keys": NotRequired[Sequence[str]],
    },
)
SchemaChangeDetailsTypeDef = TypedDict(
    "SchemaChangeDetailsTypeDef",
    {
        "Name": str,
        "Type": SchemaChangeTypeType,
        "Description": NotRequired[str],
    },
)
SendApiAssetRequestRequestTypeDef = TypedDict(
    "SendApiAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
        "Body": NotRequired[str],
        "QueryStringParameters": NotRequired[Mapping[str, str]],
        "RequestHeaders": NotRequired[Mapping[str, str]],
        "Method": NotRequired[str],
        "Path": NotRequired[str],
    },
)
StartJobRequestRequestTypeDef = TypedDict(
    "StartJobRequestRequestTypeDef",
    {
        "JobId": str,
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
UpdateAssetRequestRequestTypeDef = TypedDict(
    "UpdateAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "Name": str,
        "RevisionId": str,
    },
)
UpdateDataSetRequestRequestTypeDef = TypedDict(
    "UpdateDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
        "Description": NotRequired[str],
        "Name": NotRequired[str],
    },
)
UpdateRevisionRequestRequestTypeDef = TypedDict(
    "UpdateRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
        "Comment": NotRequired[str],
        "Finalized": NotRequired[bool],
    },
)
AcceptDataGrantResponseTypeDef = TypedDict(
    "AcceptDataGrantResponseTypeDef",
    {
        "Name": str,
        "SenderPrincipal": str,
        "ReceiverPrincipal": str,
        "Description": str,
        "AcceptanceState": DataGrantAcceptanceStateType,
        "AcceptedAt": datetime,
        "EndsAt": datetime,
        "GrantDistributionScope": GrantDistributionScopeType,
        "DataSetId": str,
        "Id": str,
        "Arn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataGrantResponseTypeDef = TypedDict(
    "CreateDataGrantResponseTypeDef",
    {
        "Name": str,
        "SenderPrincipal": str,
        "ReceiverPrincipal": str,
        "Description": str,
        "AcceptanceState": DataGrantAcceptanceStateType,
        "AcceptedAt": datetime,
        "EndsAt": datetime,
        "GrantDistributionScope": GrantDistributionScopeType,
        "DataSetId": str,
        "SourceDataSetId": str,
        "Id": str,
        "Arn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRevisionResponseTypeDef = TypedDict(
    "CreateRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "RevocationComment": str,
        "Revoked": bool,
        "RevokedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataGrantResponseTypeDef = TypedDict(
    "GetDataGrantResponseTypeDef",
    {
        "Name": str,
        "SenderPrincipal": str,
        "ReceiverPrincipal": str,
        "Description": str,
        "AcceptanceState": DataGrantAcceptanceStateType,
        "AcceptedAt": datetime,
        "EndsAt": datetime,
        "GrantDistributionScope": GrantDistributionScopeType,
        "DataSetId": str,
        "SourceDataSetId": str,
        "Id": str,
        "Arn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReceivedDataGrantResponseTypeDef = TypedDict(
    "GetReceivedDataGrantResponseTypeDef",
    {
        "Name": str,
        "SenderPrincipal": str,
        "ReceiverPrincipal": str,
        "Description": str,
        "AcceptanceState": DataGrantAcceptanceStateType,
        "AcceptedAt": datetime,
        "EndsAt": datetime,
        "GrantDistributionScope": GrantDistributionScopeType,
        "DataSetId": str,
        "Id": str,
        "Arn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRevisionResponseTypeDef = TypedDict(
    "GetRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "RevocationComment": str,
        "Revoked": bool,
        "RevokedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeRevisionResponseTypeDef = TypedDict(
    "RevokeRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "RevocationComment": str,
        "Revoked": bool,
        "RevokedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendApiAssetResponseTypeDef = TypedDict(
    "SendApiAssetResponseTypeDef",
    {
        "Body": str,
        "ResponseHeaders": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRevisionResponseTypeDef = TypedDict(
    "UpdateRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "RevocationComment": str,
        "Revoked": bool,
        "RevokedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportAssetsFromS3RequestDetailsTypeDef = TypedDict(
    "ImportAssetsFromS3RequestDetailsTypeDef",
    {
        "AssetSources": Sequence[AssetSourceEntryTypeDef],
        "DataSetId": str,
        "RevisionId": str,
    },
)
ImportAssetsFromS3ResponseDetailsTypeDef = TypedDict(
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    {
        "AssetSources": List[AssetSourceEntryTypeDef],
        "DataSetId": str,
        "RevisionId": str,
    },
)
AutoExportRevisionToS3RequestDetailsTypeDef = TypedDict(
    "AutoExportRevisionToS3RequestDetailsTypeDef",
    {
        "RevisionDestination": AutoExportRevisionDestinationEntryTypeDef,
        "Encryption": NotRequired[ExportServerSideEncryptionTypeDef],
    },
)
ExportAssetsToS3RequestDetailsTypeDef = TypedDict(
    "ExportAssetsToS3RequestDetailsTypeDef",
    {
        "AssetDestinations": Sequence[AssetDestinationEntryTypeDef],
        "DataSetId": str,
        "RevisionId": str,
        "Encryption": NotRequired[ExportServerSideEncryptionTypeDef],
    },
)
ExportAssetsToS3ResponseDetailsTypeDef = TypedDict(
    "ExportAssetsToS3ResponseDetailsTypeDef",
    {
        "AssetDestinations": List[AssetDestinationEntryTypeDef],
        "DataSetId": str,
        "RevisionId": str,
        "Encryption": NotRequired[ExportServerSideEncryptionTypeDef],
    },
)
CreateDataGrantRequestRequestTypeDef = TypedDict(
    "CreateDataGrantRequestRequestTypeDef",
    {
        "Name": str,
        "GrantDistributionScope": GrantDistributionScopeType,
        "ReceiverPrincipal": str,
        "SourceDataSetId": str,
        "EndsAt": NotRequired[TimestampTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DataUpdateRequestDetailsTypeDef = TypedDict(
    "DataUpdateRequestDetailsTypeDef",
    {
        "DataUpdatedAt": NotRequired[TimestampTypeDef],
    },
)
DeprecationRequestDetailsTypeDef = TypedDict(
    "DeprecationRequestDetailsTypeDef",
    {
        "DeprecationAt": TimestampTypeDef,
    },
)
CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": OriginDetailsTypeDef,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSetEntryTypeDef = TypedDict(
    "DataSetEntryTypeDef",
    {
        "Arn": str,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "UpdatedAt": datetime,
        "OriginDetails": NotRequired[OriginDetailsTypeDef],
        "SourceId": NotRequired[str],
    },
)
GetDataSetResponseTypeDef = TypedDict(
    "GetDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": OriginDetailsTypeDef,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": OriginDetailsTypeDef,
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataGrantsResponseTypeDef = TypedDict(
    "ListDataGrantsResponseTypeDef",
    {
        "DataGrantSummaries": List[DataGrantSummaryEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DatabaseLFTagPolicyAndPermissionsOutputTypeDef = TypedDict(
    "DatabaseLFTagPolicyAndPermissionsOutputTypeDef",
    {
        "Expression": List[LFTagOutputTypeDef],
        "Permissions": List[Literal["DESCRIBE"]],
    },
)
DatabaseLFTagPolicyTypeDef = TypedDict(
    "DatabaseLFTagPolicyTypeDef",
    {
        "Expression": List[LFTagOutputTypeDef],
    },
)
TableLFTagPolicyAndPermissionsOutputTypeDef = TypedDict(
    "TableLFTagPolicyAndPermissionsOutputTypeDef",
    {
        "Expression": List[LFTagOutputTypeDef],
        "Permissions": List[TableTagPolicyLFPermissionType],
    },
)
TableLFTagPolicyTypeDef = TypedDict(
    "TableLFTagPolicyTypeDef",
    {
        "Expression": List[LFTagOutputTypeDef],
    },
)
DetailsTypeDef = TypedDict(
    "DetailsTypeDef",
    {
        "ImportAssetFromSignedUrlJobErrorDetails": NotRequired[
            ImportAssetFromSignedUrlJobErrorDetailsTypeDef
        ],
        "ImportAssetsFromS3JobErrorDetails": NotRequired[List[AssetSourceEntryTypeDef]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "RevisionPublished": NotRequired[RevisionPublishedTypeDef],
    },
)
ExportRevisionsToS3RequestDetailsTypeDef = TypedDict(
    "ExportRevisionsToS3RequestDetailsTypeDef",
    {
        "DataSetId": str,
        "RevisionDestinations": Sequence[RevisionDestinationEntryTypeDef],
        "Encryption": NotRequired[ExportServerSideEncryptionTypeDef],
    },
)
ExportRevisionsToS3ResponseDetailsTypeDef = TypedDict(
    "ExportRevisionsToS3ResponseDetailsTypeDef",
    {
        "DataSetId": str,
        "RevisionDestinations": List[RevisionDestinationEntryTypeDef],
        "Encryption": NotRequired[ExportServerSideEncryptionTypeDef],
        "EventActionArn": NotRequired[str],
    },
)
ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef = TypedDict(
    "ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef",
    {
        "AssetSources": Sequence[RedshiftDataShareAssetSourceEntryTypeDef],
        "DataSetId": str,
        "RevisionId": str,
    },
)
ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef = TypedDict(
    "ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef",
    {
        "AssetSources": List[RedshiftDataShareAssetSourceEntryTypeDef],
        "DataSetId": str,
        "RevisionId": str,
    },
)
S3DataAccessAssetSourceEntryOutputTypeDef = TypedDict(
    "S3DataAccessAssetSourceEntryOutputTypeDef",
    {
        "Bucket": str,
        "KeyPrefixes": NotRequired[List[str]],
        "Keys": NotRequired[List[str]],
        "KmsKeysToGrant": NotRequired[List[KmsKeyToGrantTypeDef]],
    },
)
S3DataAccessAssetSourceEntryTypeDef = TypedDict(
    "S3DataAccessAssetSourceEntryTypeDef",
    {
        "Bucket": str,
        "KeyPrefixes": NotRequired[Sequence[str]],
        "Keys": NotRequired[Sequence[str]],
        "KmsKeysToGrant": NotRequired[Sequence[KmsKeyToGrantTypeDef]],
    },
)
S3DataAccessAssetTypeDef = TypedDict(
    "S3DataAccessAssetTypeDef",
    {
        "Bucket": str,
        "KeyPrefixes": NotRequired[List[str]],
        "Keys": NotRequired[List[str]],
        "S3AccessPointAlias": NotRequired[str],
        "S3AccessPointArn": NotRequired[str],
        "KmsKeysToGrant": NotRequired[List[KmsKeyToGrantTypeDef]],
    },
)
LFTagUnionTypeDef = Union[LFTagTypeDef, LFTagOutputTypeDef]
TableLFTagPolicyAndPermissionsTypeDef = TypedDict(
    "TableLFTagPolicyAndPermissionsTypeDef",
    {
        "Expression": Sequence[LFTagTypeDef],
        "Permissions": Sequence[TableTagPolicyLFPermissionType],
    },
)
ListDataGrantsRequestListDataGrantsPaginateTypeDef = TypedDict(
    "ListDataGrantsRequestListDataGrantsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSetRevisionsRequestListDataSetRevisionsPaginateTypeDef = TypedDict(
    "ListDataSetRevisionsRequestListDataSetRevisionsPaginateTypeDef",
    {
        "DataSetId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSetsRequestListDataSetsPaginateTypeDef = TypedDict(
    "ListDataSetsRequestListDataSetsPaginateTypeDef",
    {
        "Origin": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventActionsRequestListEventActionsPaginateTypeDef = TypedDict(
    "ListEventActionsRequestListEventActionsPaginateTypeDef",
    {
        "EventSourceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "DataSetId": NotRequired[str],
        "RevisionId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReceivedDataGrantsRequestListReceivedDataGrantsPaginateTypeDef = TypedDict(
    "ListReceivedDataGrantsRequestListReceivedDataGrantsPaginateTypeDef",
    {
        "AcceptanceState": NotRequired[Sequence[AcceptanceStateFilterValueType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRevisionAssetsRequestListRevisionAssetsPaginateTypeDef = TypedDict(
    "ListRevisionAssetsRequestListRevisionAssetsPaginateTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSetRevisionsResponseTypeDef = TypedDict(
    "ListDataSetRevisionsResponseTypeDef",
    {
        "Revisions": List[RevisionEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListReceivedDataGrantsResponseTypeDef = TypedDict(
    "ListReceivedDataGrantsResponseTypeDef",
    {
        "DataGrantSummaries": List[ReceivedDataGrantSummariesEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ScopeDetailsTypeDef = TypedDict(
    "ScopeDetailsTypeDef",
    {
        "LakeFormationTagPolicies": NotRequired[Sequence[LakeFormationTagPolicyDetailsTypeDef]],
        "RedshiftDataShares": NotRequired[Sequence[RedshiftDataShareDetailsTypeDef]],
        "S3DataAccesses": NotRequired[Sequence[S3DataAccessDetailsTypeDef]],
    },
)
SchemaChangeRequestDetailsTypeDef = TypedDict(
    "SchemaChangeRequestDetailsTypeDef",
    {
        "SchemaChangeAt": TimestampTypeDef,
        "Changes": NotRequired[Sequence[SchemaChangeDetailsTypeDef]],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ExportRevisionToS3": NotRequired[AutoExportRevisionToS3RequestDetailsTypeDef],
    },
)
ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "DataSets": List[DataSetEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef = TypedDict(
    "ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef",
    {
        "CatalogId": str,
        "RoleArn": str,
        "DataSetId": str,
        "RevisionId": str,
        "Database": NotRequired[DatabaseLFTagPolicyAndPermissionsOutputTypeDef],
        "Table": NotRequired[TableLFTagPolicyAndPermissionsOutputTypeDef],
    },
)
LFResourceDetailsTypeDef = TypedDict(
    "LFResourceDetailsTypeDef",
    {
        "Database": NotRequired[DatabaseLFTagPolicyTypeDef],
        "Table": NotRequired[TableLFTagPolicyTypeDef],
    },
)
JobErrorTypeDef = TypedDict(
    "JobErrorTypeDef",
    {
        "Code": CodeType,
        "Message": str,
        "Details": NotRequired[DetailsTypeDef],
        "LimitName": NotRequired[JobErrorLimitNameType],
        "LimitValue": NotRequired[float],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[JobErrorResourceTypesType],
    },
)
CreateS3DataAccessFromS3BucketResponseDetailsTypeDef = TypedDict(
    "CreateS3DataAccessFromS3BucketResponseDetailsTypeDef",
    {
        "AssetSource": S3DataAccessAssetSourceEntryOutputTypeDef,
        "DataSetId": str,
        "RevisionId": str,
    },
)
S3DataAccessAssetSourceEntryUnionTypeDef = Union[
    S3DataAccessAssetSourceEntryTypeDef, S3DataAccessAssetSourceEntryOutputTypeDef
]
DatabaseLFTagPolicyAndPermissionsTypeDef = TypedDict(
    "DatabaseLFTagPolicyAndPermissionsTypeDef",
    {
        "Expression": Sequence[LFTagUnionTypeDef],
        "Permissions": Sequence[Literal["DESCRIBE"]],
    },
)
TableLFTagPolicyAndPermissionsUnionTypeDef = Union[
    TableLFTagPolicyAndPermissionsTypeDef, TableLFTagPolicyAndPermissionsOutputTypeDef
]
NotificationDetailsTypeDef = TypedDict(
    "NotificationDetailsTypeDef",
    {
        "DataUpdate": NotRequired[DataUpdateRequestDetailsTypeDef],
        "Deprecation": NotRequired[DeprecationRequestDetailsTypeDef],
        "SchemaChange": NotRequired[SchemaChangeRequestDetailsTypeDef],
    },
)
CreateEventActionRequestRequestTypeDef = TypedDict(
    "CreateEventActionRequestRequestTypeDef",
    {
        "Action": ActionTypeDef,
        "Event": EventTypeDef,
    },
)
CreateEventActionResponseTypeDef = TypedDict(
    "CreateEventActionResponseTypeDef",
    {
        "Action": ActionTypeDef,
        "Arn": str,
        "CreatedAt": datetime,
        "Event": EventTypeDef,
        "Id": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventActionEntryTypeDef = TypedDict(
    "EventActionEntryTypeDef",
    {
        "Action": ActionTypeDef,
        "Arn": str,
        "CreatedAt": datetime,
        "Event": EventTypeDef,
        "Id": str,
        "UpdatedAt": datetime,
    },
)
GetEventActionResponseTypeDef = TypedDict(
    "GetEventActionResponseTypeDef",
    {
        "Action": ActionTypeDef,
        "Arn": str,
        "CreatedAt": datetime,
        "Event": EventTypeDef,
        "Id": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEventActionRequestRequestTypeDef = TypedDict(
    "UpdateEventActionRequestRequestTypeDef",
    {
        "EventActionId": str,
        "Action": NotRequired[ActionTypeDef],
    },
)
UpdateEventActionResponseTypeDef = TypedDict(
    "UpdateEventActionResponseTypeDef",
    {
        "Action": ActionTypeDef,
        "Arn": str,
        "CreatedAt": datetime,
        "Event": EventTypeDef,
        "Id": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LFTagPolicyDetailsTypeDef = TypedDict(
    "LFTagPolicyDetailsTypeDef",
    {
        "CatalogId": str,
        "ResourceType": LFResourceTypeType,
        "ResourceDetails": LFResourceDetailsTypeDef,
    },
)
ResponseDetailsTypeDef = TypedDict(
    "ResponseDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": NotRequired[ExportAssetToSignedUrlResponseDetailsTypeDef],
        "ExportAssetsToS3": NotRequired[ExportAssetsToS3ResponseDetailsTypeDef],
        "ExportRevisionsToS3": NotRequired[ExportRevisionsToS3ResponseDetailsTypeDef],
        "ImportAssetFromSignedUrl": NotRequired[ImportAssetFromSignedUrlResponseDetailsTypeDef],
        "ImportAssetsFromS3": NotRequired[ImportAssetsFromS3ResponseDetailsTypeDef],
        "ImportAssetsFromRedshiftDataShares": NotRequired[
            ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef
        ],
        "ImportAssetFromApiGatewayApi": NotRequired[
            ImportAssetFromApiGatewayApiResponseDetailsTypeDef
        ],
        "CreateS3DataAccessFromS3Bucket": NotRequired[
            CreateS3DataAccessFromS3BucketResponseDetailsTypeDef
        ],
        "ImportAssetsFromLakeFormationTagPolicy": NotRequired[
            ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef
        ],
    },
)
CreateS3DataAccessFromS3BucketRequestDetailsTypeDef = TypedDict(
    "CreateS3DataAccessFromS3BucketRequestDetailsTypeDef",
    {
        "AssetSource": S3DataAccessAssetSourceEntryUnionTypeDef,
        "DataSetId": str,
        "RevisionId": str,
    },
)
DatabaseLFTagPolicyAndPermissionsUnionTypeDef = Union[
    DatabaseLFTagPolicyAndPermissionsTypeDef, DatabaseLFTagPolicyAndPermissionsOutputTypeDef
]
SendDataSetNotificationRequestRequestTypeDef = TypedDict(
    "SendDataSetNotificationRequestRequestTypeDef",
    {
        "DataSetId": str,
        "Type": NotificationTypeType,
        "Scope": NotRequired[ScopeDetailsTypeDef],
        "ClientToken": NotRequired[str],
        "Comment": NotRequired[str],
        "Details": NotRequired[NotificationDetailsTypeDef],
    },
)
ListEventActionsResponseTypeDef = TypedDict(
    "ListEventActionsResponseTypeDef",
    {
        "EventActions": List[EventActionEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LakeFormationDataPermissionDetailsTypeDef = TypedDict(
    "LakeFormationDataPermissionDetailsTypeDef",
    {
        "LFTagPolicy": NotRequired[LFTagPolicyDetailsTypeDef],
    },
)
CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ResponseDetailsTypeDef,
        "Errors": List[JobErrorTypeDef],
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ResponseDetailsTypeDef,
        "Errors": List[JobErrorTypeDef],
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobEntryTypeDef = TypedDict(
    "JobEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ResponseDetailsTypeDef,
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "Errors": NotRequired[List[JobErrorTypeDef]],
    },
)
ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef = TypedDict(
    "ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef",
    {
        "CatalogId": str,
        "RoleArn": str,
        "DataSetId": str,
        "RevisionId": str,
        "Database": NotRequired[DatabaseLFTagPolicyAndPermissionsUnionTypeDef],
        "Table": NotRequired[TableLFTagPolicyAndPermissionsUnionTypeDef],
    },
)
LakeFormationDataPermissionAssetTypeDef = TypedDict(
    "LakeFormationDataPermissionAssetTypeDef",
    {
        "LakeFormationDataPermissionDetails": LakeFormationDataPermissionDetailsTypeDef,
        "LakeFormationDataPermissionType": Literal["LFTagPolicy"],
        "Permissions": List[LFPermissionType],
        "RoleArn": NotRequired[str],
    },
)
ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "Jobs": List[JobEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RequestDetailsTypeDef = TypedDict(
    "RequestDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": NotRequired[ExportAssetToSignedUrlRequestDetailsTypeDef],
        "ExportAssetsToS3": NotRequired[ExportAssetsToS3RequestDetailsTypeDef],
        "ExportRevisionsToS3": NotRequired[ExportRevisionsToS3RequestDetailsTypeDef],
        "ImportAssetFromSignedUrl": NotRequired[ImportAssetFromSignedUrlRequestDetailsTypeDef],
        "ImportAssetsFromS3": NotRequired[ImportAssetsFromS3RequestDetailsTypeDef],
        "ImportAssetsFromRedshiftDataShares": NotRequired[
            ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef
        ],
        "ImportAssetFromApiGatewayApi": NotRequired[
            ImportAssetFromApiGatewayApiRequestDetailsTypeDef
        ],
        "CreateS3DataAccessFromS3Bucket": NotRequired[
            CreateS3DataAccessFromS3BucketRequestDetailsTypeDef
        ],
        "ImportAssetsFromLakeFormationTagPolicy": NotRequired[
            ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef
        ],
    },
)
AssetDetailsTypeDef = TypedDict(
    "AssetDetailsTypeDef",
    {
        "S3SnapshotAsset": NotRequired[S3SnapshotAssetTypeDef],
        "RedshiftDataShareAsset": NotRequired[RedshiftDataShareAssetTypeDef],
        "ApiGatewayApiAsset": NotRequired[ApiGatewayApiAssetTypeDef],
        "S3DataAccessAsset": NotRequired[S3DataAccessAssetTypeDef],
        "LakeFormationDataPermissionAsset": NotRequired[LakeFormationDataPermissionAssetTypeDef],
    },
)
CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "Details": RequestDetailsTypeDef,
        "Type": TypeType,
    },
)
AssetEntryTypeDef = TypedDict(
    "AssetEntryTypeDef",
    {
        "Arn": str,
        "AssetDetails": AssetDetailsTypeDef,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "UpdatedAt": datetime,
        "SourceId": NotRequired[str],
    },
)
GetAssetResponseTypeDef = TypedDict(
    "GetAssetResponseTypeDef",
    {
        "Arn": str,
        "AssetDetails": AssetDetailsTypeDef,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssetResponseTypeDef = TypedDict(
    "UpdateAssetResponseTypeDef",
    {
        "Arn": str,
        "AssetDetails": AssetDetailsTypeDef,
        "AssetType": AssetTypeType,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRevisionAssetsResponseTypeDef = TypedDict(
    "ListRevisionAssetsResponseTypeDef",
    {
        "Assets": List[AssetEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
