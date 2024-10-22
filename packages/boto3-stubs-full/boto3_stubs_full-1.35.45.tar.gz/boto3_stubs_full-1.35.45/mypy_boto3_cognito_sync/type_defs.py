"""
Type annotations for cognito-sync service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/type_defs/)

Usage::

    ```python
    from mypy_boto3_cognito_sync.type_defs import BulkPublishRequestRequestTypeDef

    data: BulkPublishRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import BulkPublishStatusType, OperationType, PlatformType, StreamingStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "BulkPublishRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CognitoStreamsTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeIdentityPoolUsageRequestRequestTypeDef",
    "IdentityPoolUsageTypeDef",
    "DescribeIdentityUsageRequestRequestTypeDef",
    "IdentityUsageTypeDef",
    "GetBulkPublishDetailsRequestRequestTypeDef",
    "GetCognitoEventsRequestRequestTypeDef",
    "GetIdentityPoolConfigurationRequestRequestTypeDef",
    "PushSyncOutputTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListIdentityPoolUsageRequestRequestTypeDef",
    "ListRecordsRequestRequestTypeDef",
    "RecordTypeDef",
    "PushSyncTypeDef",
    "TimestampTypeDef",
    "RegisterDeviceRequestRequestTypeDef",
    "SetCognitoEventsRequestRequestTypeDef",
    "SubscribeToDatasetRequestRequestTypeDef",
    "UnsubscribeFromDatasetRequestRequestTypeDef",
    "BulkPublishResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetBulkPublishDetailsResponseTypeDef",
    "GetCognitoEventsResponseTypeDef",
    "RegisterDeviceResponseTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "DescribeIdentityPoolUsageResponseTypeDef",
    "ListIdentityPoolUsageResponseTypeDef",
    "DescribeIdentityUsageResponseTypeDef",
    "GetIdentityPoolConfigurationResponseTypeDef",
    "SetIdentityPoolConfigurationResponseTypeDef",
    "ListRecordsResponseTypeDef",
    "UpdateRecordsResponseTypeDef",
    "SetIdentityPoolConfigurationRequestRequestTypeDef",
    "RecordPatchTypeDef",
    "UpdateRecordsRequestRequestTypeDef",
)

BulkPublishRequestRequestTypeDef = TypedDict(
    "BulkPublishRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
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
CognitoStreamsTypeDef = TypedDict(
    "CognitoStreamsTypeDef",
    {
        "StreamName": NotRequired[str],
        "RoleArn": NotRequired[str],
        "StreamingStatus": NotRequired[StreamingStatusType],
    },
)
DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "IdentityId": NotRequired[str],
        "DatasetName": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "DataStorage": NotRequired[int],
        "NumRecords": NotRequired[int],
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)
DescribeIdentityPoolUsageRequestRequestTypeDef = TypedDict(
    "DescribeIdentityPoolUsageRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
IdentityPoolUsageTypeDef = TypedDict(
    "IdentityPoolUsageTypeDef",
    {
        "IdentityPoolId": NotRequired[str],
        "SyncSessionsCount": NotRequired[int],
        "DataStorage": NotRequired[int],
        "LastModifiedDate": NotRequired[datetime],
    },
)
DescribeIdentityUsageRequestRequestTypeDef = TypedDict(
    "DescribeIdentityUsageRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
    },
)
IdentityUsageTypeDef = TypedDict(
    "IdentityUsageTypeDef",
    {
        "IdentityId": NotRequired[str],
        "IdentityPoolId": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "DatasetCount": NotRequired[int],
        "DataStorage": NotRequired[int],
    },
)
GetBulkPublishDetailsRequestRequestTypeDef = TypedDict(
    "GetBulkPublishDetailsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
GetCognitoEventsRequestRequestTypeDef = TypedDict(
    "GetCognitoEventsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
GetIdentityPoolConfigurationRequestRequestTypeDef = TypedDict(
    "GetIdentityPoolConfigurationRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
PushSyncOutputTypeDef = TypedDict(
    "PushSyncOutputTypeDef",
    {
        "ApplicationArns": NotRequired[List[str]],
        "RoleArn": NotRequired[str],
    },
)
ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIdentityPoolUsageRequestRequestTypeDef = TypedDict(
    "ListIdentityPoolUsageRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRecordsRequestRequestTypeDef = TypedDict(
    "ListRecordsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "LastSyncCount": NotRequired[int],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SyncSessionToken": NotRequired[str],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "SyncCount": NotRequired[int],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "DeviceLastModifiedDate": NotRequired[datetime],
    },
)
PushSyncTypeDef = TypedDict(
    "PushSyncTypeDef",
    {
        "ApplicationArns": NotRequired[Sequence[str]],
        "RoleArn": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
RegisterDeviceRequestRequestTypeDef = TypedDict(
    "RegisterDeviceRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "Platform": PlatformType,
        "Token": str,
    },
)
SetCognitoEventsRequestRequestTypeDef = TypedDict(
    "SetCognitoEventsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Events": Mapping[str, str],
    },
)
SubscribeToDatasetRequestRequestTypeDef = TypedDict(
    "SubscribeToDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "DeviceId": str,
    },
)
UnsubscribeFromDatasetRequestRequestTypeDef = TypedDict(
    "UnsubscribeFromDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "DeviceId": str,
    },
)
BulkPublishResponseTypeDef = TypedDict(
    "BulkPublishResponseTypeDef",
    {
        "IdentityPoolId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBulkPublishDetailsResponseTypeDef = TypedDict(
    "GetBulkPublishDetailsResponseTypeDef",
    {
        "IdentityPoolId": str,
        "BulkPublishStartTime": datetime,
        "BulkPublishCompleteTime": datetime,
        "BulkPublishStatus": BulkPublishStatusType,
        "FailureMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCognitoEventsResponseTypeDef = TypedDict(
    "GetCognitoEventsResponseTypeDef",
    {
        "Events": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterDeviceResponseTypeDef = TypedDict(
    "RegisterDeviceResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Dataset": DatasetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "Dataset": DatasetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List[DatasetTypeDef],
        "Count": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeIdentityPoolUsageResponseTypeDef = TypedDict(
    "DescribeIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsage": IdentityPoolUsageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdentityPoolUsageResponseTypeDef = TypedDict(
    "ListIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsages": List[IdentityPoolUsageTypeDef],
        "MaxResults": int,
        "Count": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeIdentityUsageResponseTypeDef = TypedDict(
    "DescribeIdentityUsageResponseTypeDef",
    {
        "IdentityUsage": IdentityUsageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "GetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": PushSyncOutputTypeDef,
        "CognitoStreams": CognitoStreamsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "SetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": PushSyncOutputTypeDef,
        "CognitoStreams": CognitoStreamsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecordsResponseTypeDef = TypedDict(
    "ListRecordsResponseTypeDef",
    {
        "Records": List[RecordTypeDef],
        "Count": int,
        "DatasetSyncCount": int,
        "LastModifiedBy": str,
        "MergedDatasetNames": List[str],
        "DatasetExists": bool,
        "DatasetDeletedAfterRequestedSyncCount": bool,
        "SyncSessionToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateRecordsResponseTypeDef = TypedDict(
    "UpdateRecordsResponseTypeDef",
    {
        "Records": List[RecordTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetIdentityPoolConfigurationRequestRequestTypeDef = TypedDict(
    "SetIdentityPoolConfigurationRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": NotRequired[PushSyncTypeDef],
        "CognitoStreams": NotRequired[CognitoStreamsTypeDef],
    },
)
RecordPatchTypeDef = TypedDict(
    "RecordPatchTypeDef",
    {
        "Op": OperationType,
        "Key": str,
        "SyncCount": int,
        "Value": NotRequired[str],
        "DeviceLastModifiedDate": NotRequired[TimestampTypeDef],
    },
)
UpdateRecordsRequestRequestTypeDef = TypedDict(
    "UpdateRecordsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "SyncSessionToken": str,
        "DeviceId": NotRequired[str],
        "RecordPatches": NotRequired[Sequence[RecordPatchTypeDef]],
        "ClientContext": NotRequired[str],
    },
)
