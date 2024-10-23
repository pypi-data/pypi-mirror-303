"""
Type annotations for repostspace service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/type_defs/)

Usage::

    ```python
    from mypy_boto3_repostspace.type_defs import BatchAddRoleInputRequestTypeDef

    data: BatchAddRoleInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import ConfigurationStatusType, RoleType, TierLevelType, VanityDomainStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "BatchAddRoleInputRequestTypeDef",
    "BatchErrorTypeDef",
    "ResponseMetadataTypeDef",
    "BatchRemoveRoleInputRequestTypeDef",
    "CreateSpaceInputRequestTypeDef",
    "DeleteSpaceInputRequestTypeDef",
    "DeregisterAdminInputRequestTypeDef",
    "GetSpaceInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListSpacesInputRequestTypeDef",
    "SpaceDataTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RegisterAdminInputRequestTypeDef",
    "SendInvitesInputRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSpaceInputRequestTypeDef",
    "BatchAddRoleOutputTypeDef",
    "BatchRemoveRoleOutputTypeDef",
    "CreateSpaceOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetSpaceOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListSpacesInputListSpacesPaginateTypeDef",
    "ListSpacesOutputTypeDef",
)

BatchAddRoleInputRequestTypeDef = TypedDict(
    "BatchAddRoleInputRequestTypeDef",
    {
        "accessorIds": Sequence[str],
        "role": RoleType,
        "spaceId": str,
    },
)
BatchErrorTypeDef = TypedDict(
    "BatchErrorTypeDef",
    {
        "accessorId": str,
        "error": int,
        "message": str,
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
BatchRemoveRoleInputRequestTypeDef = TypedDict(
    "BatchRemoveRoleInputRequestTypeDef",
    {
        "accessorIds": Sequence[str],
        "role": RoleType,
        "spaceId": str,
    },
)
CreateSpaceInputRequestTypeDef = TypedDict(
    "CreateSpaceInputRequestTypeDef",
    {
        "name": str,
        "subdomain": str,
        "tier": TierLevelType,
        "description": NotRequired[str],
        "roleArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "userKMSKey": NotRequired[str],
    },
)
DeleteSpaceInputRequestTypeDef = TypedDict(
    "DeleteSpaceInputRequestTypeDef",
    {
        "spaceId": str,
    },
)
DeregisterAdminInputRequestTypeDef = TypedDict(
    "DeregisterAdminInputRequestTypeDef",
    {
        "adminId": str,
        "spaceId": str,
    },
)
GetSpaceInputRequestTypeDef = TypedDict(
    "GetSpaceInputRequestTypeDef",
    {
        "spaceId": str,
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
ListSpacesInputRequestTypeDef = TypedDict(
    "ListSpacesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SpaceDataTypeDef = TypedDict(
    "SpaceDataTypeDef",
    {
        "arn": str,
        "configurationStatus": ConfigurationStatusType,
        "createDateTime": datetime,
        "name": str,
        "randomDomain": str,
        "spaceId": str,
        "status": str,
        "storageLimit": int,
        "tier": TierLevelType,
        "vanityDomain": str,
        "vanityDomainStatus": VanityDomainStatusType,
        "contentSize": NotRequired[int],
        "deleteDateTime": NotRequired[datetime],
        "description": NotRequired[str],
        "userCount": NotRequired[int],
        "userKMSKey": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RegisterAdminInputRequestTypeDef = TypedDict(
    "RegisterAdminInputRequestTypeDef",
    {
        "adminId": str,
        "spaceId": str,
    },
)
SendInvitesInputRequestTypeDef = TypedDict(
    "SendInvitesInputRequestTypeDef",
    {
        "accessorIds": Sequence[str],
        "body": str,
        "spaceId": str,
        "title": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateSpaceInputRequestTypeDef = TypedDict(
    "UpdateSpaceInputRequestTypeDef",
    {
        "spaceId": str,
        "description": NotRequired[str],
        "roleArn": NotRequired[str],
        "tier": NotRequired[TierLevelType],
    },
)
BatchAddRoleOutputTypeDef = TypedDict(
    "BatchAddRoleOutputTypeDef",
    {
        "addedAccessorIds": List[str],
        "errors": List[BatchErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchRemoveRoleOutputTypeDef = TypedDict(
    "BatchRemoveRoleOutputTypeDef",
    {
        "errors": List[BatchErrorTypeDef],
        "removedAccessorIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSpaceOutputTypeDef = TypedDict(
    "CreateSpaceOutputTypeDef",
    {
        "spaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSpaceOutputTypeDef = TypedDict(
    "GetSpaceOutputTypeDef",
    {
        "arn": str,
        "clientId": str,
        "configurationStatus": ConfigurationStatusType,
        "contentSize": int,
        "createDateTime": datetime,
        "customerRoleArn": str,
        "deleteDateTime": datetime,
        "description": str,
        "groupAdmins": List[str],
        "name": str,
        "randomDomain": str,
        "roles": Dict[str, List[RoleType]],
        "spaceId": str,
        "status": str,
        "storageLimit": int,
        "tier": TierLevelType,
        "userAdmins": List[str],
        "userCount": int,
        "userKMSKey": str,
        "vanityDomain": str,
        "vanityDomainStatus": VanityDomainStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSpacesInputListSpacesPaginateTypeDef = TypedDict(
    "ListSpacesInputListSpacesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSpacesOutputTypeDef = TypedDict(
    "ListSpacesOutputTypeDef",
    {
        "nextToken": str,
        "spaces": List[SpaceDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
