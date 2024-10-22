"""
Type annotations for iot1click-projects service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/type_defs/)

Usage::

    ```python
    from mypy_boto3_iot1click_projects.type_defs import AssociateDeviceWithPlacementRequestRequestTypeDef

    data: AssociateDeviceWithPlacementRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AssociateDeviceWithPlacementRequestRequestTypeDef",
    "CreatePlacementRequestRequestTypeDef",
    "DeletePlacementRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DescribePlacementRequestRequestTypeDef",
    "PlacementDescriptionTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DeviceTemplateOutputTypeDef",
    "DeviceTemplateTypeDef",
    "DisassociateDeviceFromPlacementRequestRequestTypeDef",
    "GetDevicesInPlacementRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListPlacementsRequestRequestTypeDef",
    "PlacementSummaryTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ProjectSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePlacementRequestRequestTypeDef",
    "DescribePlacementResponseTypeDef",
    "GetDevicesInPlacementResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PlacementTemplateOutputTypeDef",
    "DeviceTemplateUnionTypeDef",
    "ListPlacementsRequestListPlacementsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListPlacementsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ProjectDescriptionTypeDef",
    "PlacementTemplateTypeDef",
    "DescribeProjectResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
)

AssociateDeviceWithPlacementRequestRequestTypeDef = TypedDict(
    "AssociateDeviceWithPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceId": str,
        "deviceTemplateName": str,
    },
)
CreatePlacementRequestRequestTypeDef = TypedDict(
    "CreatePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
        "attributes": NotRequired[Mapping[str, str]],
    },
)
DeletePlacementRequestRequestTypeDef = TypedDict(
    "DeletePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)
DescribePlacementRequestRequestTypeDef = TypedDict(
    "DescribePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)
PlacementDescriptionTypeDef = TypedDict(
    "PlacementDescriptionTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
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
DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)
DeviceTemplateOutputTypeDef = TypedDict(
    "DeviceTemplateOutputTypeDef",
    {
        "deviceType": NotRequired[str],
        "callbackOverrides": NotRequired[Dict[str, str]],
    },
)
DeviceTemplateTypeDef = TypedDict(
    "DeviceTemplateTypeDef",
    {
        "deviceType": NotRequired[str],
        "callbackOverrides": NotRequired[Mapping[str, str]],
    },
)
DisassociateDeviceFromPlacementRequestRequestTypeDef = TypedDict(
    "DisassociateDeviceFromPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceTemplateName": str,
    },
)
GetDevicesInPlacementRequestRequestTypeDef = TypedDict(
    "GetDevicesInPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
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
ListPlacementsRequestRequestTypeDef = TypedDict(
    "ListPlacementsRequestRequestTypeDef",
    {
        "projectName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PlacementSummaryTypeDef = TypedDict(
    "PlacementSummaryTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "arn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
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
UpdatePlacementRequestRequestTypeDef = TypedDict(
    "UpdatePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
        "attributes": NotRequired[Mapping[str, str]],
    },
)
DescribePlacementResponseTypeDef = TypedDict(
    "DescribePlacementResponseTypeDef",
    {
        "placement": PlacementDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevicesInPlacementResponseTypeDef = TypedDict(
    "GetDevicesInPlacementResponseTypeDef",
    {
        "devices": Dict[str, str],
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
PlacementTemplateOutputTypeDef = TypedDict(
    "PlacementTemplateOutputTypeDef",
    {
        "defaultAttributes": NotRequired[Dict[str, str]],
        "deviceTemplates": NotRequired[Dict[str, DeviceTemplateOutputTypeDef]],
    },
)
DeviceTemplateUnionTypeDef = Union[DeviceTemplateTypeDef, DeviceTemplateOutputTypeDef]
ListPlacementsRequestListPlacementsPaginateTypeDef = TypedDict(
    "ListPlacementsRequestListPlacementsPaginateTypeDef",
    {
        "projectName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPlacementsResponseTypeDef = TypedDict(
    "ListPlacementsResponseTypeDef",
    {
        "placements": List[PlacementSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "projects": List[ProjectSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "placementTemplate": NotRequired[PlacementTemplateOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
PlacementTemplateTypeDef = TypedDict(
    "PlacementTemplateTypeDef",
    {
        "defaultAttributes": NotRequired[Mapping[str, str]],
        "deviceTemplates": NotRequired[Mapping[str, DeviceTemplateUnionTypeDef]],
    },
)
DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "project": ProjectDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "projectName": str,
        "description": NotRequired[str],
        "placementTemplate": NotRequired[PlacementTemplateTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "projectName": str,
        "description": NotRequired[str],
        "placementTemplate": NotRequired[PlacementTemplateTypeDef],
    },
)
