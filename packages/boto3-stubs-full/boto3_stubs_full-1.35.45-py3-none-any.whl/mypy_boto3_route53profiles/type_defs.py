"""
Type annotations for route53profiles service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/type_defs/)

Usage::

    ```python
    from mypy_boto3_route53profiles.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import ProfileStatusType, ShareStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "TagTypeDef",
    "ProfileAssociationTypeDef",
    "ResponseMetadataTypeDef",
    "AssociateResourceToProfileRequestRequestTypeDef",
    "ProfileResourceAssociationTypeDef",
    "ProfileTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DisassociateProfileRequestRequestTypeDef",
    "DisassociateResourceFromProfileRequestRequestTypeDef",
    "GetProfileAssociationRequestRequestTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetProfileResourceAssociationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListProfileAssociationsRequestRequestTypeDef",
    "ListProfileResourceAssociationsRequestRequestTypeDef",
    "ListProfilesRequestRequestTypeDef",
    "ProfileSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProfileResourceAssociationRequestRequestTypeDef",
    "AssociateProfileRequestRequestTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "AssociateProfileResponseTypeDef",
    "DisassociateProfileResponseTypeDef",
    "GetProfileAssociationResponseTypeDef",
    "ListProfileAssociationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "AssociateResourceToProfileResponseTypeDef",
    "DisassociateResourceFromProfileResponseTypeDef",
    "GetProfileResourceAssociationResponseTypeDef",
    "ListProfileResourceAssociationsResponseTypeDef",
    "UpdateProfileResourceAssociationResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteProfileResponseTypeDef",
    "GetProfileResponseTypeDef",
    "ListProfileAssociationsRequestListProfileAssociationsPaginateTypeDef",
    "ListProfileResourceAssociationsRequestListProfileResourceAssociationsPaginateTypeDef",
    "ListProfilesRequestListProfilesPaginateTypeDef",
    "ListProfilesResponseTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ProfileAssociationTypeDef = TypedDict(
    "ProfileAssociationTypeDef",
    {
        "CreationTime": NotRequired[datetime],
        "Id": NotRequired[str],
        "ModificationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "OwnerId": NotRequired[str],
        "ProfileId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Status": NotRequired[ProfileStatusType],
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
AssociateResourceToProfileRequestRequestTypeDef = TypedDict(
    "AssociateResourceToProfileRequestRequestTypeDef",
    {
        "Name": str,
        "ProfileId": str,
        "ResourceArn": str,
        "ResourceProperties": NotRequired[str],
    },
)
ProfileResourceAssociationTypeDef = TypedDict(
    "ProfileResourceAssociationTypeDef",
    {
        "CreationTime": NotRequired[datetime],
        "Id": NotRequired[str],
        "ModificationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "OwnerId": NotRequired[str],
        "ProfileId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceProperties": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Status": NotRequired[ProfileStatusType],
        "StatusMessage": NotRequired[str],
    },
)
ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "ClientToken": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Id": NotRequired[str],
        "ModificationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "OwnerId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
        "Status": NotRequired[ProfileStatusType],
        "StatusMessage": NotRequired[str],
    },
)
DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)
DisassociateProfileRequestRequestTypeDef = TypedDict(
    "DisassociateProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "ResourceId": str,
    },
)
DisassociateResourceFromProfileRequestRequestTypeDef = TypedDict(
    "DisassociateResourceFromProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "ResourceArn": str,
    },
)
GetProfileAssociationRequestRequestTypeDef = TypedDict(
    "GetProfileAssociationRequestRequestTypeDef",
    {
        "ProfileAssociationId": str,
    },
)
GetProfileRequestRequestTypeDef = TypedDict(
    "GetProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)
GetProfileResourceAssociationRequestRequestTypeDef = TypedDict(
    "GetProfileResourceAssociationRequestRequestTypeDef",
    {
        "ProfileResourceAssociationId": str,
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
ListProfileAssociationsRequestRequestTypeDef = TypedDict(
    "ListProfileAssociationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProfileId": NotRequired[str],
        "ResourceId": NotRequired[str],
    },
)
ListProfileResourceAssociationsRequestRequestTypeDef = TypedDict(
    "ListProfileResourceAssociationsRequestRequestTypeDef",
    {
        "ProfileId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)
ListProfilesRequestRequestTypeDef = TypedDict(
    "ListProfilesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ProfileSummaryTypeDef = TypedDict(
    "ProfileSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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
UpdateProfileResourceAssociationRequestRequestTypeDef = TypedDict(
    "UpdateProfileResourceAssociationRequestRequestTypeDef",
    {
        "ProfileResourceAssociationId": str,
        "Name": NotRequired[str],
        "ResourceProperties": NotRequired[str],
    },
)
AssociateProfileRequestRequestTypeDef = TypedDict(
    "AssociateProfileRequestRequestTypeDef",
    {
        "Name": str,
        "ProfileId": str,
        "ResourceId": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateProfileRequestRequestTypeDef = TypedDict(
    "CreateProfileRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
AssociateProfileResponseTypeDef = TypedDict(
    "AssociateProfileResponseTypeDef",
    {
        "ProfileAssociation": ProfileAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateProfileResponseTypeDef = TypedDict(
    "DisassociateProfileResponseTypeDef",
    {
        "ProfileAssociation": ProfileAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileAssociationResponseTypeDef = TypedDict(
    "GetProfileAssociationResponseTypeDef",
    {
        "ProfileAssociation": ProfileAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfileAssociationsResponseTypeDef = TypedDict(
    "ListProfileAssociationsResponseTypeDef",
    {
        "ProfileAssociations": List[ProfileAssociationTypeDef],
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
AssociateResourceToProfileResponseTypeDef = TypedDict(
    "AssociateResourceToProfileResponseTypeDef",
    {
        "ProfileResourceAssociation": ProfileResourceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateResourceFromProfileResponseTypeDef = TypedDict(
    "DisassociateResourceFromProfileResponseTypeDef",
    {
        "ProfileResourceAssociation": ProfileResourceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileResourceAssociationResponseTypeDef = TypedDict(
    "GetProfileResourceAssociationResponseTypeDef",
    {
        "ProfileResourceAssociation": ProfileResourceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfileResourceAssociationsResponseTypeDef = TypedDict(
    "ListProfileResourceAssociationsResponseTypeDef",
    {
        "ProfileResourceAssociations": List[ProfileResourceAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateProfileResourceAssociationResponseTypeDef = TypedDict(
    "UpdateProfileResourceAssociationResponseTypeDef",
    {
        "ProfileResourceAssociation": ProfileResourceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "Profile": ProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileResponseTypeDef = TypedDict(
    "DeleteProfileResponseTypeDef",
    {
        "Profile": ProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "Profile": ProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfileAssociationsRequestListProfileAssociationsPaginateTypeDef = TypedDict(
    "ListProfileAssociationsRequestListProfileAssociationsPaginateTypeDef",
    {
        "ProfileId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfileResourceAssociationsRequestListProfileResourceAssociationsPaginateTypeDef = TypedDict(
    "ListProfileResourceAssociationsRequestListProfileResourceAssociationsPaginateTypeDef",
    {
        "ProfileId": str,
        "ResourceType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfilesRequestListProfilesPaginateTypeDef = TypedDict(
    "ListProfilesRequestListProfilesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "ProfileSummaries": List[ProfileSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
