"""
Type annotations for cloudcontrol service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudcontrol.type_defs import CancelResourceRequestInputRequestTypeDef

    data: CancelResourceRequestInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import HandlerErrorCodeType, OperationStatusType, OperationType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CancelResourceRequestInputRequestTypeDef",
    "ProgressEventTypeDef",
    "ResponseMetadataTypeDef",
    "CreateResourceInputRequestTypeDef",
    "DeleteResourceInputRequestTypeDef",
    "GetResourceInputRequestTypeDef",
    "ResourceDescriptionTypeDef",
    "GetResourceRequestStatusInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceRequestStatusFilterTypeDef",
    "ListResourcesInputRequestTypeDef",
    "UpdateResourceInputRequestTypeDef",
    "CancelResourceRequestOutputTypeDef",
    "CreateResourceOutputTypeDef",
    "DeleteResourceOutputTypeDef",
    "GetResourceRequestStatusOutputTypeDef",
    "ListResourceRequestsOutputTypeDef",
    "UpdateResourceOutputTypeDef",
    "GetResourceOutputTypeDef",
    "ListResourcesOutputTypeDef",
    "GetResourceRequestStatusInputResourceRequestSuccessWaitTypeDef",
    "ListResourcesInputListResourcesPaginateTypeDef",
    "ListResourceRequestsInputListResourceRequestsPaginateTypeDef",
    "ListResourceRequestsInputRequestTypeDef",
)

CancelResourceRequestInputRequestTypeDef = TypedDict(
    "CancelResourceRequestInputRequestTypeDef",
    {
        "RequestToken": str,
    },
)
ProgressEventTypeDef = TypedDict(
    "ProgressEventTypeDef",
    {
        "TypeName": NotRequired[str],
        "Identifier": NotRequired[str],
        "RequestToken": NotRequired[str],
        "Operation": NotRequired[OperationType],
        "OperationStatus": NotRequired[OperationStatusType],
        "EventTime": NotRequired[datetime],
        "ResourceModel": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "ErrorCode": NotRequired[HandlerErrorCodeType],
        "RetryAfter": NotRequired[datetime],
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
CreateResourceInputRequestTypeDef = TypedDict(
    "CreateResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "DesiredState": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
DeleteResourceInputRequestTypeDef = TypedDict(
    "DeleteResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
GetResourceInputRequestTypeDef = TypedDict(
    "GetResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)
ResourceDescriptionTypeDef = TypedDict(
    "ResourceDescriptionTypeDef",
    {
        "Identifier": NotRequired[str],
        "Properties": NotRequired[str],
    },
)
GetResourceRequestStatusInputRequestTypeDef = TypedDict(
    "GetResourceRequestStatusInputRequestTypeDef",
    {
        "RequestToken": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
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
ResourceRequestStatusFilterTypeDef = TypedDict(
    "ResourceRequestStatusFilterTypeDef",
    {
        "Operations": NotRequired[Sequence[OperationType]],
        "OperationStatuses": NotRequired[Sequence[OperationStatusType]],
    },
)
ListResourcesInputRequestTypeDef = TypedDict(
    "ListResourcesInputRequestTypeDef",
    {
        "TypeName": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceModel": NotRequired[str],
    },
)
UpdateResourceInputRequestTypeDef = TypedDict(
    "UpdateResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
        "PatchDocument": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
CancelResourceRequestOutputTypeDef = TypedDict(
    "CancelResourceRequestOutputTypeDef",
    {
        "ProgressEvent": ProgressEventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceOutputTypeDef = TypedDict(
    "CreateResourceOutputTypeDef",
    {
        "ProgressEvent": ProgressEventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResourceOutputTypeDef = TypedDict(
    "DeleteResourceOutputTypeDef",
    {
        "ProgressEvent": ProgressEventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceRequestStatusOutputTypeDef = TypedDict(
    "GetResourceRequestStatusOutputTypeDef",
    {
        "ProgressEvent": ProgressEventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceRequestsOutputTypeDef = TypedDict(
    "ListResourceRequestsOutputTypeDef",
    {
        "ResourceRequestStatusSummaries": List[ProgressEventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateResourceOutputTypeDef = TypedDict(
    "UpdateResourceOutputTypeDef",
    {
        "ProgressEvent": ProgressEventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceOutputTypeDef = TypedDict(
    "GetResourceOutputTypeDef",
    {
        "TypeName": str,
        "ResourceDescription": ResourceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesOutputTypeDef = TypedDict(
    "ListResourcesOutputTypeDef",
    {
        "TypeName": str,
        "ResourceDescriptions": List[ResourceDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetResourceRequestStatusInputResourceRequestSuccessWaitTypeDef = TypedDict(
    "GetResourceRequestStatusInputResourceRequestSuccessWaitTypeDef",
    {
        "RequestToken": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
ListResourcesInputListResourcesPaginateTypeDef = TypedDict(
    "ListResourcesInputListResourcesPaginateTypeDef",
    {
        "TypeName": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ResourceModel": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceRequestsInputListResourceRequestsPaginateTypeDef = TypedDict(
    "ListResourceRequestsInputListResourceRequestsPaginateTypeDef",
    {
        "ResourceRequestStatusFilter": NotRequired[ResourceRequestStatusFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceRequestsInputRequestTypeDef = TypedDict(
    "ListResourceRequestsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ResourceRequestStatusFilter": NotRequired[ResourceRequestStatusFilterTypeDef],
    },
)
