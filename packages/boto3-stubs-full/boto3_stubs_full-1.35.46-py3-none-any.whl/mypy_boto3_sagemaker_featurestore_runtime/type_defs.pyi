"""
Type annotations for sagemaker-featurestore-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_sagemaker_featurestore_runtime.type_defs import BatchGetRecordErrorTypeDef

    data: BatchGetRecordErrorTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence, Union

from .literals import (
    DeletionModeType,
    ExpirationTimeResponseType,
    TargetStoreType,
    TtlDurationUnitType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BatchGetRecordErrorTypeDef",
    "BatchGetRecordIdentifierOutputTypeDef",
    "BatchGetRecordIdentifierTypeDef",
    "ResponseMetadataTypeDef",
    "FeatureValueOutputTypeDef",
    "DeleteRecordRequestRequestTypeDef",
    "FeatureValueTypeDef",
    "GetRecordRequestRequestTypeDef",
    "TtlDurationTypeDef",
    "BatchGetRecordIdentifierUnionTypeDef",
    "EmptyResponseMetadataTypeDef",
    "BatchGetRecordResultDetailTypeDef",
    "GetRecordResponseTypeDef",
    "FeatureValueUnionTypeDef",
    "BatchGetRecordRequestRequestTypeDef",
    "BatchGetRecordResponseTypeDef",
    "PutRecordRequestRequestTypeDef",
)

BatchGetRecordErrorTypeDef = TypedDict(
    "BatchGetRecordErrorTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)
BatchGetRecordIdentifierOutputTypeDef = TypedDict(
    "BatchGetRecordIdentifierOutputTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifiersValueAsString": List[str],
        "FeatureNames": NotRequired[List[str]],
    },
)
BatchGetRecordIdentifierTypeDef = TypedDict(
    "BatchGetRecordIdentifierTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifiersValueAsString": Sequence[str],
        "FeatureNames": NotRequired[Sequence[str]],
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
FeatureValueOutputTypeDef = TypedDict(
    "FeatureValueOutputTypeDef",
    {
        "FeatureName": str,
        "ValueAsString": NotRequired[str],
        "ValueAsStringList": NotRequired[List[str]],
    },
)
DeleteRecordRequestRequestTypeDef = TypedDict(
    "DeleteRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "EventTime": str,
        "TargetStores": NotRequired[Sequence[TargetStoreType]],
        "DeletionMode": NotRequired[DeletionModeType],
    },
)
FeatureValueTypeDef = TypedDict(
    "FeatureValueTypeDef",
    {
        "FeatureName": str,
        "ValueAsString": NotRequired[str],
        "ValueAsStringList": NotRequired[Sequence[str]],
    },
)
GetRecordRequestRequestTypeDef = TypedDict(
    "GetRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "FeatureNames": NotRequired[Sequence[str]],
        "ExpirationTimeResponse": NotRequired[ExpirationTimeResponseType],
    },
)
TtlDurationTypeDef = TypedDict(
    "TtlDurationTypeDef",
    {
        "Unit": TtlDurationUnitType,
        "Value": int,
    },
)
BatchGetRecordIdentifierUnionTypeDef = Union[
    BatchGetRecordIdentifierTypeDef, BatchGetRecordIdentifierOutputTypeDef
]
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetRecordResultDetailTypeDef = TypedDict(
    "BatchGetRecordResultDetailTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "Record": List[FeatureValueOutputTypeDef],
        "ExpiresAt": NotRequired[str],
    },
)
GetRecordResponseTypeDef = TypedDict(
    "GetRecordResponseTypeDef",
    {
        "Record": List[FeatureValueOutputTypeDef],
        "ExpiresAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FeatureValueUnionTypeDef = Union[FeatureValueTypeDef, FeatureValueOutputTypeDef]
BatchGetRecordRequestRequestTypeDef = TypedDict(
    "BatchGetRecordRequestRequestTypeDef",
    {
        "Identifiers": Sequence[BatchGetRecordIdentifierUnionTypeDef],
        "ExpirationTimeResponse": NotRequired[ExpirationTimeResponseType],
    },
)
BatchGetRecordResponseTypeDef = TypedDict(
    "BatchGetRecordResponseTypeDef",
    {
        "Records": List[BatchGetRecordResultDetailTypeDef],
        "Errors": List[BatchGetRecordErrorTypeDef],
        "UnprocessedIdentifiers": List[BatchGetRecordIdentifierOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRecordRequestRequestTypeDef = TypedDict(
    "PutRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "Record": Sequence[FeatureValueUnionTypeDef],
        "TargetStores": NotRequired[Sequence[TargetStoreType]],
        "TtlDuration": NotRequired[TtlDurationTypeDef],
    },
)
