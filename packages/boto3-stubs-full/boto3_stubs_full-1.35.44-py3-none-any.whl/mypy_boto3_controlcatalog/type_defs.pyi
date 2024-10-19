"""
Type annotations for controlcatalog service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/type_defs/)

Usage::

    ```python
    from mypy_boto3_controlcatalog.type_defs import AssociatedDomainSummaryTypeDef

    data: AssociatedDomainSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import ControlBehaviorType, ControlScopeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssociatedDomainSummaryTypeDef",
    "AssociatedObjectiveSummaryTypeDef",
    "ObjectiveResourceFilterTypeDef",
    "ControlSummaryTypeDef",
    "DomainResourceFilterTypeDef",
    "DomainSummaryTypeDef",
    "GetControlRequestRequestTypeDef",
    "RegionConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "ListControlsRequestRequestTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ObjectiveSummaryTypeDef",
    "CommonControlSummaryTypeDef",
    "CommonControlFilterTypeDef",
    "ObjectiveFilterTypeDef",
    "GetControlResponseTypeDef",
    "ListControlsResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListControlsRequestListControlsPaginateTypeDef",
    "ListDomainsRequestListDomainsPaginateTypeDef",
    "ListObjectivesResponseTypeDef",
    "ListCommonControlsResponseTypeDef",
    "ListCommonControlsRequestListCommonControlsPaginateTypeDef",
    "ListCommonControlsRequestRequestTypeDef",
    "ListObjectivesRequestListObjectivesPaginateTypeDef",
    "ListObjectivesRequestRequestTypeDef",
)

AssociatedDomainSummaryTypeDef = TypedDict(
    "AssociatedDomainSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
AssociatedObjectiveSummaryTypeDef = TypedDict(
    "AssociatedObjectiveSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ObjectiveResourceFilterTypeDef = TypedDict(
    "ObjectiveResourceFilterTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
ControlSummaryTypeDef = TypedDict(
    "ControlSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
    },
)
DomainResourceFilterTypeDef = TypedDict(
    "DomainResourceFilterTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
    },
)
GetControlRequestRequestTypeDef = TypedDict(
    "GetControlRequestRequestTypeDef",
    {
        "ControlArn": str,
    },
)
RegionConfigurationTypeDef = TypedDict(
    "RegionConfigurationTypeDef",
    {
        "Scope": ControlScopeType,
        "DeployableRegions": NotRequired[List[str]],
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
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListControlsRequestRequestTypeDef = TypedDict(
    "ListControlsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ObjectiveSummaryTypeDef = TypedDict(
    "ObjectiveSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Domain": AssociatedDomainSummaryTypeDef,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
    },
)
CommonControlSummaryTypeDef = TypedDict(
    "CommonControlSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Domain": AssociatedDomainSummaryTypeDef,
        "Objective": AssociatedObjectiveSummaryTypeDef,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
    },
)
CommonControlFilterTypeDef = TypedDict(
    "CommonControlFilterTypeDef",
    {
        "Objectives": NotRequired[Sequence[ObjectiveResourceFilterTypeDef]],
    },
)
ObjectiveFilterTypeDef = TypedDict(
    "ObjectiveFilterTypeDef",
    {
        "Domains": NotRequired[Sequence[DomainResourceFilterTypeDef]],
    },
)
GetControlResponseTypeDef = TypedDict(
    "GetControlResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Behavior": ControlBehaviorType,
        "RegionConfiguration": RegionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListControlsResponseTypeDef = TypedDict(
    "ListControlsResponseTypeDef",
    {
        "Controls": List[ControlSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List[DomainSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListControlsRequestListControlsPaginateTypeDef = TypedDict(
    "ListControlsRequestListControlsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDomainsRequestListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsRequestListDomainsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListObjectivesResponseTypeDef = TypedDict(
    "ListObjectivesResponseTypeDef",
    {
        "Objectives": List[ObjectiveSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCommonControlsResponseTypeDef = TypedDict(
    "ListCommonControlsResponseTypeDef",
    {
        "CommonControls": List[CommonControlSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCommonControlsRequestListCommonControlsPaginateTypeDef = TypedDict(
    "ListCommonControlsRequestListCommonControlsPaginateTypeDef",
    {
        "CommonControlFilter": NotRequired[CommonControlFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCommonControlsRequestRequestTypeDef = TypedDict(
    "ListCommonControlsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "CommonControlFilter": NotRequired[CommonControlFilterTypeDef],
    },
)
ListObjectivesRequestListObjectivesPaginateTypeDef = TypedDict(
    "ListObjectivesRequestListObjectivesPaginateTypeDef",
    {
        "ObjectiveFilter": NotRequired[ObjectiveFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListObjectivesRequestRequestTypeDef = TypedDict(
    "ListObjectivesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ObjectiveFilter": NotRequired[ObjectiveFilterTypeDef],
    },
)
