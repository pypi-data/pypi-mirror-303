"""
Type annotations for marketplacecommerceanalytics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/type_defs/)

Usage::

    ```python
    from mypy_boto3_marketplacecommerceanalytics.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, Mapping, Union

from .literals import DataSetTypeType, SupportDataSetTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "GenerateDataSetRequestRequestTypeDef",
    "StartSupportDataExportRequestRequestTypeDef",
    "GenerateDataSetResultTypeDef",
    "StartSupportDataExportResultTypeDef",
)

TimestampTypeDef = Union[datetime, str]
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
GenerateDataSetRequestRequestTypeDef = TypedDict(
    "GenerateDataSetRequestRequestTypeDef",
    {
        "dataSetType": DataSetTypeType,
        "dataSetPublicationDate": TimestampTypeDef,
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
        "destinationS3Prefix": NotRequired[str],
        "customerDefinedValues": NotRequired[Mapping[str, str]],
    },
)
StartSupportDataExportRequestRequestTypeDef = TypedDict(
    "StartSupportDataExportRequestRequestTypeDef",
    {
        "dataSetType": SupportDataSetTypeType,
        "fromDate": TimestampTypeDef,
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
        "destinationS3Prefix": NotRequired[str],
        "customerDefinedValues": NotRequired[Mapping[str, str]],
    },
)
GenerateDataSetResultTypeDef = TypedDict(
    "GenerateDataSetResultTypeDef",
    {
        "dataSetRequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSupportDataExportResultTypeDef = TypedDict(
    "StartSupportDataExportResultTypeDef",
    {
        "dataSetRequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
