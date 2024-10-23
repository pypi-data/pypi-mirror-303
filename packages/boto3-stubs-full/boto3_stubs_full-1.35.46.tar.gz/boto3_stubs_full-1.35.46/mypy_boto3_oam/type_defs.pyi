"""
Type annotations for oam service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/type_defs/)

Usage::

    ```python
    from mypy_boto3_oam.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import ResourceTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "CreateSinkInputRequestTypeDef",
    "DeleteLinkInputRequestTypeDef",
    "DeleteSinkInputRequestTypeDef",
    "GetLinkInputRequestTypeDef",
    "GetSinkInputRequestTypeDef",
    "GetSinkPolicyInputRequestTypeDef",
    "LogGroupConfigurationTypeDef",
    "MetricConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ListAttachedLinksInputRequestTypeDef",
    "ListAttachedLinksItemTypeDef",
    "ListLinksInputRequestTypeDef",
    "ListLinksItemTypeDef",
    "ListSinksInputRequestTypeDef",
    "ListSinksItemTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "PutSinkPolicyInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "CreateSinkOutputTypeDef",
    "GetSinkOutputTypeDef",
    "GetSinkPolicyOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PutSinkPolicyOutputTypeDef",
    "LinkConfigurationTypeDef",
    "ListAttachedLinksInputListAttachedLinksPaginateTypeDef",
    "ListLinksInputListLinksPaginateTypeDef",
    "ListSinksInputListSinksPaginateTypeDef",
    "ListAttachedLinksOutputTypeDef",
    "ListLinksOutputTypeDef",
    "ListSinksOutputTypeDef",
    "CreateLinkInputRequestTypeDef",
    "CreateLinkOutputTypeDef",
    "GetLinkOutputTypeDef",
    "UpdateLinkInputRequestTypeDef",
    "UpdateLinkOutputTypeDef",
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
CreateSinkInputRequestTypeDef = TypedDict(
    "CreateSinkInputRequestTypeDef",
    {
        "Name": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteLinkInputRequestTypeDef = TypedDict(
    "DeleteLinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)
DeleteSinkInputRequestTypeDef = TypedDict(
    "DeleteSinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetLinkInputRequestTypeDef = TypedDict(
    "GetLinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetSinkInputRequestTypeDef = TypedDict(
    "GetSinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetSinkPolicyInputRequestTypeDef = TypedDict(
    "GetSinkPolicyInputRequestTypeDef",
    {
        "SinkIdentifier": str,
    },
)
LogGroupConfigurationTypeDef = TypedDict(
    "LogGroupConfigurationTypeDef",
    {
        "Filter": str,
    },
)
MetricConfigurationTypeDef = TypedDict(
    "MetricConfigurationTypeDef",
    {
        "Filter": str,
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
ListAttachedLinksInputRequestTypeDef = TypedDict(
    "ListAttachedLinksInputRequestTypeDef",
    {
        "SinkIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAttachedLinksItemTypeDef = TypedDict(
    "ListAttachedLinksItemTypeDef",
    {
        "Label": NotRequired[str],
        "LinkArn": NotRequired[str],
        "ResourceTypes": NotRequired[List[str]],
    },
)
ListLinksInputRequestTypeDef = TypedDict(
    "ListLinksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLinksItemTypeDef = TypedDict(
    "ListLinksItemTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Label": NotRequired[str],
        "ResourceTypes": NotRequired[List[str]],
        "SinkArn": NotRequired[str],
    },
)
ListSinksInputRequestTypeDef = TypedDict(
    "ListSinksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSinksItemTypeDef = TypedDict(
    "ListSinksItemTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PutSinkPolicyInputRequestTypeDef = TypedDict(
    "PutSinkPolicyInputRequestTypeDef",
    {
        "Policy": str,
        "SinkIdentifier": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
CreateSinkOutputTypeDef = TypedDict(
    "CreateSinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSinkOutputTypeDef = TypedDict(
    "GetSinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSinkPolicyOutputTypeDef = TypedDict(
    "GetSinkPolicyOutputTypeDef",
    {
        "Policy": str,
        "SinkArn": str,
        "SinkId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSinkPolicyOutputTypeDef = TypedDict(
    "PutSinkPolicyOutputTypeDef",
    {
        "Policy": str,
        "SinkArn": str,
        "SinkId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LinkConfigurationTypeDef = TypedDict(
    "LinkConfigurationTypeDef",
    {
        "LogGroupConfiguration": NotRequired[LogGroupConfigurationTypeDef],
        "MetricConfiguration": NotRequired[MetricConfigurationTypeDef],
    },
)
ListAttachedLinksInputListAttachedLinksPaginateTypeDef = TypedDict(
    "ListAttachedLinksInputListAttachedLinksPaginateTypeDef",
    {
        "SinkIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLinksInputListLinksPaginateTypeDef = TypedDict(
    "ListLinksInputListLinksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSinksInputListSinksPaginateTypeDef = TypedDict(
    "ListSinksInputListSinksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttachedLinksOutputTypeDef = TypedDict(
    "ListAttachedLinksOutputTypeDef",
    {
        "Items": List[ListAttachedLinksItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLinksOutputTypeDef = TypedDict(
    "ListLinksOutputTypeDef",
    {
        "Items": List[ListLinksItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSinksOutputTypeDef = TypedDict(
    "ListSinksOutputTypeDef",
    {
        "Items": List[ListSinksItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateLinkInputRequestTypeDef = TypedDict(
    "CreateLinkInputRequestTypeDef",
    {
        "LabelTemplate": str,
        "ResourceTypes": Sequence[ResourceTypeType],
        "SinkIdentifier": str,
        "LinkConfiguration": NotRequired[LinkConfigurationTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateLinkOutputTypeDef = TypedDict(
    "CreateLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "LinkConfiguration": LinkConfigurationTypeDef,
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLinkOutputTypeDef = TypedDict(
    "GetLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "LinkConfiguration": LinkConfigurationTypeDef,
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLinkInputRequestTypeDef = TypedDict(
    "UpdateLinkInputRequestTypeDef",
    {
        "Identifier": str,
        "ResourceTypes": Sequence[ResourceTypeType],
        "LinkConfiguration": NotRequired[LinkConfigurationTypeDef],
    },
)
UpdateLinkOutputTypeDef = TypedDict(
    "UpdateLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "LinkConfiguration": LinkConfigurationTypeDef,
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
