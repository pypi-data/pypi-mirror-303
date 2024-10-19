"""
Type annotations for servicecatalog-appregistry service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/type_defs/)

Usage::

    ```python
    from mypy_boto3_servicecatalog_appregistry.type_defs import TagQueryConfigurationTypeDef

    data: TagQueryConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ApplicationTagStatusType,
    AssociationOptionType,
    ResourceGroupStateType,
    ResourceItemStatusType,
    ResourceTypeType,
    SyncActionType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "TagQueryConfigurationTypeDef",
    "ApplicationSummaryTypeDef",
    "ResourcesListItemTypeDef",
    "ApplicationTypeDef",
    "AssociateAttributeGroupRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociateResourceRequestRequestTypeDef",
    "AttributeGroupDetailsTypeDef",
    "AttributeGroupSummaryTypeDef",
    "AttributeGroupTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateAttributeGroupRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteAttributeGroupRequestRequestTypeDef",
    "DisassociateAttributeGroupRequestRequestTypeDef",
    "DisassociateResourceRequestRequestTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetAssociatedResourceRequestRequestTypeDef",
    "GetAttributeGroupRequestRequestTypeDef",
    "ResourceGroupTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListAssociatedAttributeGroupsRequestRequestTypeDef",
    "ListAssociatedResourcesRequestRequestTypeDef",
    "ListAttributeGroupsForApplicationRequestRequestTypeDef",
    "ListAttributeGroupsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ResourceDetailsTypeDef",
    "SyncResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateAttributeGroupRequestRequestTypeDef",
    "AppRegistryConfigurationTypeDef",
    "ApplicationTagResultTypeDef",
    "AssociateAttributeGroupResponseTypeDef",
    "AssociateResourceResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationResponseTypeDef",
    "DisassociateAttributeGroupResponseTypeDef",
    "DisassociateResourceResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAttributeGroupResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListAssociatedAttributeGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SyncResourceResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "ListAttributeGroupsForApplicationResponseTypeDef",
    "DeleteAttributeGroupResponseTypeDef",
    "ListAttributeGroupsResponseTypeDef",
    "CreateAttributeGroupResponseTypeDef",
    "UpdateAttributeGroupResponseTypeDef",
    "IntegrationsTypeDef",
    "ResourceIntegrationsTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListAssociatedAttributeGroupsRequestListAssociatedAttributeGroupsPaginateTypeDef",
    "ListAssociatedResourcesRequestListAssociatedResourcesPaginateTypeDef",
    "ListAttributeGroupsForApplicationRequestListAttributeGroupsForApplicationPaginateTypeDef",
    "ListAttributeGroupsRequestListAttributeGroupsPaginateTypeDef",
    "ResourceInfoTypeDef",
    "GetConfigurationResponseTypeDef",
    "PutConfigurationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "ResourceTypeDef",
    "ListAssociatedResourcesResponseTypeDef",
    "GetAssociatedResourceResponseTypeDef",
)

TagQueryConfigurationTypeDef = TypedDict(
    "TagQueryConfigurationTypeDef",
    {
        "tagKey": NotRequired[str],
    },
)
ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)
ResourcesListItemTypeDef = TypedDict(
    "ResourcesListItemTypeDef",
    {
        "resourceArn": NotRequired[str],
        "errorMessage": NotRequired[str],
        "status": NotRequired[str],
        "resourceType": NotRequired[str],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "applicationTag": NotRequired[Dict[str, str]],
    },
)
AssociateAttributeGroupRequestRequestTypeDef = TypedDict(
    "AssociateAttributeGroupRequestRequestTypeDef",
    {
        "application": str,
        "attributeGroup": str,
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
AssociateResourceRequestRequestTypeDef = TypedDict(
    "AssociateResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": ResourceTypeType,
        "resource": str,
        "options": NotRequired[Sequence[AssociationOptionType]],
    },
)
AttributeGroupDetailsTypeDef = TypedDict(
    "AttributeGroupDetailsTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "createdBy": NotRequired[str],
    },
)
AttributeGroupSummaryTypeDef = TypedDict(
    "AttributeGroupSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "createdBy": NotRequired[str],
    },
)
AttributeGroupTypeDef = TypedDict(
    "AttributeGroupTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "clientToken": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateAttributeGroupRequestRequestTypeDef = TypedDict(
    "CreateAttributeGroupRequestRequestTypeDef",
    {
        "name": str,
        "attributes": str,
        "clientToken": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)
DeleteAttributeGroupRequestRequestTypeDef = TypedDict(
    "DeleteAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
    },
)
DisassociateAttributeGroupRequestRequestTypeDef = TypedDict(
    "DisassociateAttributeGroupRequestRequestTypeDef",
    {
        "application": str,
        "attributeGroup": str,
    },
)
DisassociateResourceRequestRequestTypeDef = TypedDict(
    "DisassociateResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": ResourceTypeType,
        "resource": str,
    },
)
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)
GetAssociatedResourceRequestRequestTypeDef = TypedDict(
    "GetAssociatedResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": ResourceTypeType,
        "resource": str,
        "nextToken": NotRequired[str],
        "resourceTagStatus": NotRequired[Sequence[ResourceItemStatusType]],
        "maxResults": NotRequired[int],
    },
)
GetAttributeGroupRequestRequestTypeDef = TypedDict(
    "GetAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
    },
)
ResourceGroupTypeDef = TypedDict(
    "ResourceGroupTypeDef",
    {
        "state": NotRequired[ResourceGroupStateType],
        "arn": NotRequired[str],
        "errorMessage": NotRequired[str],
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
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssociatedAttributeGroupsRequestRequestTypeDef = TypedDict(
    "ListAssociatedAttributeGroupsRequestRequestTypeDef",
    {
        "application": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssociatedResourcesRequestRequestTypeDef = TypedDict(
    "ListAssociatedResourcesRequestRequestTypeDef",
    {
        "application": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAttributeGroupsForApplicationRequestRequestTypeDef = TypedDict(
    "ListAttributeGroupsForApplicationRequestRequestTypeDef",
    {
        "application": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAttributeGroupsRequestRequestTypeDef = TypedDict(
    "ListAttributeGroupsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "tagValue": NotRequired[str],
    },
)
SyncResourceRequestRequestTypeDef = TypedDict(
    "SyncResourceRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resource": str,
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
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "application": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
UpdateAttributeGroupRequestRequestTypeDef = TypedDict(
    "UpdateAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "attributes": NotRequired[str],
    },
)
AppRegistryConfigurationTypeDef = TypedDict(
    "AppRegistryConfigurationTypeDef",
    {
        "tagQueryConfiguration": NotRequired[TagQueryConfigurationTypeDef],
    },
)
ApplicationTagResultTypeDef = TypedDict(
    "ApplicationTagResultTypeDef",
    {
        "applicationTagStatus": NotRequired[ApplicationTagStatusType],
        "errorMessage": NotRequired[str],
        "resources": NotRequired[List[ResourcesListItemTypeDef]],
        "nextToken": NotRequired[str],
    },
)
AssociateAttributeGroupResponseTypeDef = TypedDict(
    "AssociateAttributeGroupResponseTypeDef",
    {
        "applicationArn": str,
        "attributeGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateResourceResponseTypeDef = TypedDict(
    "AssociateResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "options": List[AssociationOptionType],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "application": ApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApplicationResponseTypeDef = TypedDict(
    "DeleteApplicationResponseTypeDef",
    {
        "application": ApplicationSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateAttributeGroupResponseTypeDef = TypedDict(
    "DisassociateAttributeGroupResponseTypeDef",
    {
        "applicationArn": str,
        "attributeGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateResourceResponseTypeDef = TypedDict(
    "DisassociateResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAttributeGroupResponseTypeDef = TypedDict(
    "GetAttributeGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "attributes": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
        "createdBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applications": List[ApplicationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssociatedAttributeGroupsResponseTypeDef = TypedDict(
    "ListAssociatedAttributeGroupsResponseTypeDef",
    {
        "attributeGroups": List[str],
        "nextToken": str,
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
SyncResourceResponseTypeDef = TypedDict(
    "SyncResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "actionTaken": SyncActionType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "application": ApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttributeGroupsForApplicationResponseTypeDef = TypedDict(
    "ListAttributeGroupsForApplicationResponseTypeDef",
    {
        "attributeGroupsDetails": List[AttributeGroupDetailsTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAttributeGroupResponseTypeDef = TypedDict(
    "DeleteAttributeGroupResponseTypeDef",
    {
        "attributeGroup": AttributeGroupSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttributeGroupsResponseTypeDef = TypedDict(
    "ListAttributeGroupsResponseTypeDef",
    {
        "attributeGroups": List[AttributeGroupSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAttributeGroupResponseTypeDef = TypedDict(
    "CreateAttributeGroupResponseTypeDef",
    {
        "attributeGroup": AttributeGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAttributeGroupResponseTypeDef = TypedDict(
    "UpdateAttributeGroupResponseTypeDef",
    {
        "attributeGroup": AttributeGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IntegrationsTypeDef = TypedDict(
    "IntegrationsTypeDef",
    {
        "resourceGroup": NotRequired[ResourceGroupTypeDef],
        "applicationTagResourceGroup": NotRequired[ResourceGroupTypeDef],
    },
)
ResourceIntegrationsTypeDef = TypedDict(
    "ResourceIntegrationsTypeDef",
    {
        "resourceGroup": NotRequired[ResourceGroupTypeDef],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssociatedAttributeGroupsRequestListAssociatedAttributeGroupsPaginateTypeDef = TypedDict(
    "ListAssociatedAttributeGroupsRequestListAssociatedAttributeGroupsPaginateTypeDef",
    {
        "application": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssociatedResourcesRequestListAssociatedResourcesPaginateTypeDef = TypedDict(
    "ListAssociatedResourcesRequestListAssociatedResourcesPaginateTypeDef",
    {
        "application": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttributeGroupsForApplicationRequestListAttributeGroupsForApplicationPaginateTypeDef = (
    TypedDict(
        "ListAttributeGroupsForApplicationRequestListAttributeGroupsForApplicationPaginateTypeDef",
        {
            "application": str,
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListAttributeGroupsRequestListAttributeGroupsPaginateTypeDef = TypedDict(
    "ListAttributeGroupsRequestListAttributeGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "resourceDetails": NotRequired[ResourceDetailsTypeDef],
        "options": NotRequired[List[AssociationOptionType]],
    },
)
GetConfigurationResponseTypeDef = TypedDict(
    "GetConfigurationResponseTypeDef",
    {
        "configuration": AppRegistryConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutConfigurationRequestRequestTypeDef = TypedDict(
    "PutConfigurationRequestRequestTypeDef",
    {
        "configuration": AppRegistryConfigurationTypeDef,
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "associatedResourceCount": int,
        "tags": Dict[str, str],
        "integrations": IntegrationsTypeDef,
        "applicationTag": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "associationTime": NotRequired[datetime],
        "integrations": NotRequired[ResourceIntegrationsTypeDef],
    },
)
ListAssociatedResourcesResponseTypeDef = TypedDict(
    "ListAssociatedResourcesResponseTypeDef",
    {
        "resources": List[ResourceInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssociatedResourceResponseTypeDef = TypedDict(
    "GetAssociatedResourceResponseTypeDef",
    {
        "resource": ResourceTypeDef,
        "options": List[AssociationOptionType],
        "applicationTagResult": ApplicationTagResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
