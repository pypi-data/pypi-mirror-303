"""
Type annotations for resource-explorer-2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/type_defs/)

Usage::

    ```python
    from mypy_boto3_resource_explorer_2.type_defs import AssociateDefaultViewInputRequestTypeDef

    data: AssociateDefaultViewInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from .literals import AWSServiceAccessStatusType, IndexStateType, IndexTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssociateDefaultViewInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BatchGetViewErrorTypeDef",
    "BatchGetViewInputRequestTypeDef",
    "CreateIndexInputRequestTypeDef",
    "IncludedPropertyTypeDef",
    "SearchFilterTypeDef",
    "DeleteIndexInputRequestTypeDef",
    "DeleteViewInputRequestTypeDef",
    "OrgConfigurationTypeDef",
    "GetViewInputRequestTypeDef",
    "IndexTypeDef",
    "PaginatorConfigTypeDef",
    "ListIndexesForMembersInputRequestTypeDef",
    "MemberIndexTypeDef",
    "ListIndexesInputRequestTypeDef",
    "ListSupportedResourceTypesInputRequestTypeDef",
    "SupportedResourceTypeTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListViewsInputRequestTypeDef",
    "ResourceCountTypeDef",
    "ResourcePropertyTypeDef",
    "SearchInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateIndexTypeInputRequestTypeDef",
    "AssociateDefaultViewOutputTypeDef",
    "CreateIndexOutputTypeDef",
    "DeleteIndexOutputTypeDef",
    "DeleteViewOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDefaultViewOutputTypeDef",
    "GetIndexOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListViewsOutputTypeDef",
    "UpdateIndexTypeOutputTypeDef",
    "CreateViewInputRequestTypeDef",
    "ListResourcesInputRequestTypeDef",
    "UpdateViewInputRequestTypeDef",
    "ViewTypeDef",
    "GetAccountLevelServiceConfigurationOutputTypeDef",
    "ListIndexesOutputTypeDef",
    "ListIndexesForMembersInputListIndexesForMembersPaginateTypeDef",
    "ListIndexesInputListIndexesPaginateTypeDef",
    "ListResourcesInputListResourcesPaginateTypeDef",
    "ListSupportedResourceTypesInputListSupportedResourceTypesPaginateTypeDef",
    "ListViewsInputListViewsPaginateTypeDef",
    "SearchInputSearchPaginateTypeDef",
    "ListIndexesForMembersOutputTypeDef",
    "ListSupportedResourceTypesOutputTypeDef",
    "ResourceTypeDef",
    "BatchGetViewOutputTypeDef",
    "CreateViewOutputTypeDef",
    "GetViewOutputTypeDef",
    "UpdateViewOutputTypeDef",
    "ListResourcesOutputTypeDef",
    "SearchOutputTypeDef",
)

AssociateDefaultViewInputRequestTypeDef = TypedDict(
    "AssociateDefaultViewInputRequestTypeDef",
    {
        "ViewArn": str,
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
BatchGetViewErrorTypeDef = TypedDict(
    "BatchGetViewErrorTypeDef",
    {
        "ErrorMessage": str,
        "ViewArn": str,
    },
)
BatchGetViewInputRequestTypeDef = TypedDict(
    "BatchGetViewInputRequestTypeDef",
    {
        "ViewArns": NotRequired[Sequence[str]],
    },
)
CreateIndexInputRequestTypeDef = TypedDict(
    "CreateIndexInputRequestTypeDef",
    {
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
IncludedPropertyTypeDef = TypedDict(
    "IncludedPropertyTypeDef",
    {
        "Name": str,
    },
)
SearchFilterTypeDef = TypedDict(
    "SearchFilterTypeDef",
    {
        "FilterString": str,
    },
)
DeleteIndexInputRequestTypeDef = TypedDict(
    "DeleteIndexInputRequestTypeDef",
    {
        "Arn": str,
    },
)
DeleteViewInputRequestTypeDef = TypedDict(
    "DeleteViewInputRequestTypeDef",
    {
        "ViewArn": str,
    },
)
OrgConfigurationTypeDef = TypedDict(
    "OrgConfigurationTypeDef",
    {
        "AWSServiceAccessStatus": AWSServiceAccessStatusType,
        "ServiceLinkedRole": NotRequired[str],
    },
)
GetViewInputRequestTypeDef = TypedDict(
    "GetViewInputRequestTypeDef",
    {
        "ViewArn": str,
    },
)
IndexTypeDef = TypedDict(
    "IndexTypeDef",
    {
        "Arn": NotRequired[str],
        "Region": NotRequired[str],
        "Type": NotRequired[IndexTypeType],
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
ListIndexesForMembersInputRequestTypeDef = TypedDict(
    "ListIndexesForMembersInputRequestTypeDef",
    {
        "AccountIdList": Sequence[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MemberIndexTypeDef = TypedDict(
    "MemberIndexTypeDef",
    {
        "AccountId": NotRequired[str],
        "Arn": NotRequired[str],
        "Region": NotRequired[str],
        "Type": NotRequired[IndexTypeType],
    },
)
ListIndexesInputRequestTypeDef = TypedDict(
    "ListIndexesInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Regions": NotRequired[Sequence[str]],
        "Type": NotRequired[IndexTypeType],
    },
)
ListSupportedResourceTypesInputRequestTypeDef = TypedDict(
    "ListSupportedResourceTypesInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SupportedResourceTypeTypeDef = TypedDict(
    "SupportedResourceTypeTypeDef",
    {
        "ResourceType": NotRequired[str],
        "Service": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListViewsInputRequestTypeDef = TypedDict(
    "ListViewsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ResourceCountTypeDef = TypedDict(
    "ResourceCountTypeDef",
    {
        "Complete": NotRequired[bool],
        "TotalResources": NotRequired[int],
    },
)
ResourcePropertyTypeDef = TypedDict(
    "ResourcePropertyTypeDef",
    {
        "Data": NotRequired[Dict[str, Any]],
        "LastReportedAt": NotRequired[datetime],
        "Name": NotRequired[str],
    },
)
SearchInputRequestTypeDef = TypedDict(
    "SearchInputRequestTypeDef",
    {
        "QueryString": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ViewArn": NotRequired[str],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateIndexTypeInputRequestTypeDef = TypedDict(
    "UpdateIndexTypeInputRequestTypeDef",
    {
        "Arn": str,
        "Type": IndexTypeType,
    },
)
AssociateDefaultViewOutputTypeDef = TypedDict(
    "AssociateDefaultViewOutputTypeDef",
    {
        "ViewArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIndexOutputTypeDef = TypedDict(
    "CreateIndexOutputTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "State": IndexStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIndexOutputTypeDef = TypedDict(
    "DeleteIndexOutputTypeDef",
    {
        "Arn": str,
        "LastUpdatedAt": datetime,
        "State": IndexStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteViewOutputTypeDef = TypedDict(
    "DeleteViewOutputTypeDef",
    {
        "ViewArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDefaultViewOutputTypeDef = TypedDict(
    "GetDefaultViewOutputTypeDef",
    {
        "ViewArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIndexOutputTypeDef = TypedDict(
    "GetIndexOutputTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ReplicatingFrom": List[str],
        "ReplicatingTo": List[str],
        "State": IndexStateType,
        "Tags": Dict[str, str],
        "Type": IndexTypeType,
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
ListViewsOutputTypeDef = TypedDict(
    "ListViewsOutputTypeDef",
    {
        "Views": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateIndexTypeOutputTypeDef = TypedDict(
    "UpdateIndexTypeOutputTypeDef",
    {
        "Arn": str,
        "LastUpdatedAt": datetime,
        "State": IndexStateType,
        "Type": IndexTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateViewInputRequestTypeDef = TypedDict(
    "CreateViewInputRequestTypeDef",
    {
        "ViewName": str,
        "ClientToken": NotRequired[str],
        "Filters": NotRequired[SearchFilterTypeDef],
        "IncludedProperties": NotRequired[Sequence[IncludedPropertyTypeDef]],
        "Scope": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListResourcesInputRequestTypeDef = TypedDict(
    "ListResourcesInputRequestTypeDef",
    {
        "Filters": NotRequired[SearchFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ViewArn": NotRequired[str],
    },
)
UpdateViewInputRequestTypeDef = TypedDict(
    "UpdateViewInputRequestTypeDef",
    {
        "ViewArn": str,
        "Filters": NotRequired[SearchFilterTypeDef],
        "IncludedProperties": NotRequired[Sequence[IncludedPropertyTypeDef]],
    },
)
ViewTypeDef = TypedDict(
    "ViewTypeDef",
    {
        "Filters": NotRequired[SearchFilterTypeDef],
        "IncludedProperties": NotRequired[List[IncludedPropertyTypeDef]],
        "LastUpdatedAt": NotRequired[datetime],
        "Owner": NotRequired[str],
        "Scope": NotRequired[str],
        "ViewArn": NotRequired[str],
    },
)
GetAccountLevelServiceConfigurationOutputTypeDef = TypedDict(
    "GetAccountLevelServiceConfigurationOutputTypeDef",
    {
        "OrgConfiguration": OrgConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIndexesOutputTypeDef = TypedDict(
    "ListIndexesOutputTypeDef",
    {
        "Indexes": List[IndexTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIndexesForMembersInputListIndexesForMembersPaginateTypeDef = TypedDict(
    "ListIndexesForMembersInputListIndexesForMembersPaginateTypeDef",
    {
        "AccountIdList": Sequence[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIndexesInputListIndexesPaginateTypeDef = TypedDict(
    "ListIndexesInputListIndexesPaginateTypeDef",
    {
        "Regions": NotRequired[Sequence[str]],
        "Type": NotRequired[IndexTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourcesInputListResourcesPaginateTypeDef = TypedDict(
    "ListResourcesInputListResourcesPaginateTypeDef",
    {
        "Filters": NotRequired[SearchFilterTypeDef],
        "ViewArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSupportedResourceTypesInputListSupportedResourceTypesPaginateTypeDef = TypedDict(
    "ListSupportedResourceTypesInputListSupportedResourceTypesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListViewsInputListViewsPaginateTypeDef = TypedDict(
    "ListViewsInputListViewsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchInputSearchPaginateTypeDef = TypedDict(
    "SearchInputSearchPaginateTypeDef",
    {
        "QueryString": str,
        "ViewArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIndexesForMembersOutputTypeDef = TypedDict(
    "ListIndexesForMembersOutputTypeDef",
    {
        "Indexes": List[MemberIndexTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSupportedResourceTypesOutputTypeDef = TypedDict(
    "ListSupportedResourceTypesOutputTypeDef",
    {
        "ResourceTypes": List[SupportedResourceTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Arn": NotRequired[str],
        "LastReportedAt": NotRequired[datetime],
        "OwningAccountId": NotRequired[str],
        "Properties": NotRequired[List[ResourcePropertyTypeDef]],
        "Region": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Service": NotRequired[str],
    },
)
BatchGetViewOutputTypeDef = TypedDict(
    "BatchGetViewOutputTypeDef",
    {
        "Errors": List[BatchGetViewErrorTypeDef],
        "Views": List[ViewTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateViewOutputTypeDef = TypedDict(
    "CreateViewOutputTypeDef",
    {
        "View": ViewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetViewOutputTypeDef = TypedDict(
    "GetViewOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "View": ViewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateViewOutputTypeDef = TypedDict(
    "UpdateViewOutputTypeDef",
    {
        "View": ViewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesOutputTypeDef = TypedDict(
    "ListResourcesOutputTypeDef",
    {
        "Resources": List[ResourceTypeDef],
        "ViewArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchOutputTypeDef = TypedDict(
    "SearchOutputTypeDef",
    {
        "Count": ResourceCountTypeDef,
        "Resources": List[ResourceTypeDef],
        "ViewArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
