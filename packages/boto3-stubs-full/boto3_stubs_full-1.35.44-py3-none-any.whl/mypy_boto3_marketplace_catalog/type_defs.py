"""
Type annotations for marketplace-catalog service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/type_defs/)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import AmiProductEntityIdFilterTypeDef

    data: AmiProductEntityIdFilterTypeDef = ...
    ```
"""

import sys
from typing import Any, Dict, List, Mapping, Sequence

from .literals import (
    AmiProductSortByType,
    AmiProductVisibilityStringType,
    ChangeStatusType,
    ContainerProductSortByType,
    ContainerProductVisibilityStringType,
    DataProductSortByType,
    DataProductVisibilityStringType,
    FailureCodeType,
    IntentType,
    OfferSortByType,
    OfferStateStringType,
    OfferTargetingStringType,
    OwnershipTypeType,
    ResaleAuthorizationSortByType,
    ResaleAuthorizationStatusStringType,
    SaaSProductSortByType,
    SaaSProductVisibilityStringType,
    SortOrderType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AmiProductEntityIdFilterTypeDef",
    "AmiProductTitleFilterTypeDef",
    "AmiProductVisibilityFilterTypeDef",
    "AmiProductLastModifiedDateFilterDateRangeTypeDef",
    "AmiProductSortTypeDef",
    "AmiProductSummaryTypeDef",
    "EntityRequestTypeDef",
    "BatchDescribeErrorDetailTypeDef",
    "EntityDetailTypeDef",
    "ResponseMetadataTypeDef",
    "CancelChangeSetRequestRequestTypeDef",
    "ChangeSetSummaryListItemTypeDef",
    "EntityTypeDef",
    "ErrorDetailTypeDef",
    "TagTypeDef",
    "ContainerProductEntityIdFilterTypeDef",
    "ContainerProductTitleFilterTypeDef",
    "ContainerProductVisibilityFilterTypeDef",
    "ContainerProductLastModifiedDateFilterDateRangeTypeDef",
    "ContainerProductSortTypeDef",
    "ContainerProductSummaryTypeDef",
    "DataProductEntityIdFilterTypeDef",
    "DataProductTitleFilterTypeDef",
    "DataProductVisibilityFilterTypeDef",
    "DataProductLastModifiedDateFilterDateRangeTypeDef",
    "DataProductSortTypeDef",
    "DataProductSummaryTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DescribeChangeSetRequestRequestTypeDef",
    "DescribeEntityRequestRequestTypeDef",
    "OfferSummaryTypeDef",
    "ResaleAuthorizationSummaryTypeDef",
    "SaaSProductSummaryTypeDef",
    "OfferSortTypeDef",
    "ResaleAuthorizationSortTypeDef",
    "SaaSProductSortTypeDef",
    "FilterTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "SortTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "OfferAvailabilityEndDateFilterDateRangeTypeDef",
    "OfferBuyerAccountsFilterTypeDef",
    "OfferEntityIdFilterTypeDef",
    "OfferNameFilterTypeDef",
    "OfferProductIdFilterTypeDef",
    "OfferResaleAuthorizationIdFilterTypeDef",
    "OfferStateFilterTypeDef",
    "OfferTargetingFilterTypeDef",
    "OfferLastModifiedDateFilterDateRangeTypeDef",
    "OfferReleaseDateFilterDateRangeTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef",
    "ResaleAuthorizationCreatedDateFilterDateRangeTypeDef",
    "ResaleAuthorizationEntityIdFilterTypeDef",
    "ResaleAuthorizationManufacturerAccountIdFilterTypeDef",
    "ResaleAuthorizationManufacturerLegalNameFilterTypeDef",
    "ResaleAuthorizationNameFilterTypeDef",
    "ResaleAuthorizationOfferExtendedStatusFilterTypeDef",
    "ResaleAuthorizationProductIdFilterTypeDef",
    "ResaleAuthorizationProductNameFilterTypeDef",
    "ResaleAuthorizationResellerAccountIDFilterTypeDef",
    "ResaleAuthorizationResellerLegalNameFilterTypeDef",
    "ResaleAuthorizationStatusFilterTypeDef",
    "ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef",
    "SaaSProductEntityIdFilterTypeDef",
    "SaaSProductTitleFilterTypeDef",
    "SaaSProductVisibilityFilterTypeDef",
    "SaaSProductLastModifiedDateFilterDateRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AmiProductLastModifiedDateFilterTypeDef",
    "BatchDescribeEntitiesRequestRequestTypeDef",
    "BatchDescribeEntitiesResponseTypeDef",
    "CancelChangeSetResponseTypeDef",
    "DescribeEntityResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "StartChangeSetResponseTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ChangeSummaryTypeDef",
    "ChangeTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ContainerProductLastModifiedDateFilterTypeDef",
    "DataProductLastModifiedDateFilterTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeSortTypeDef",
    "ListChangeSetsRequestListChangeSetsPaginateTypeDef",
    "ListChangeSetsRequestRequestTypeDef",
    "OfferAvailabilityEndDateFilterTypeDef",
    "OfferLastModifiedDateFilterTypeDef",
    "OfferReleaseDateFilterTypeDef",
    "ResaleAuthorizationAvailabilityEndDateFilterTypeDef",
    "ResaleAuthorizationCreatedDateFilterTypeDef",
    "ResaleAuthorizationLastModifiedDateFilterTypeDef",
    "SaaSProductLastModifiedDateFilterTypeDef",
    "AmiProductFiltersTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "StartChangeSetRequestRequestTypeDef",
    "ContainerProductFiltersTypeDef",
    "DataProductFiltersTypeDef",
    "ListEntitiesResponseTypeDef",
    "OfferFiltersTypeDef",
    "ResaleAuthorizationFiltersTypeDef",
    "SaaSProductFiltersTypeDef",
    "EntityTypeFiltersTypeDef",
    "ListEntitiesRequestListEntitiesPaginateTypeDef",
    "ListEntitiesRequestRequestTypeDef",
)

AmiProductEntityIdFilterTypeDef = TypedDict(
    "AmiProductEntityIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
AmiProductTitleFilterTypeDef = TypedDict(
    "AmiProductTitleFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
AmiProductVisibilityFilterTypeDef = TypedDict(
    "AmiProductVisibilityFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[AmiProductVisibilityStringType]],
    },
)
AmiProductLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "AmiProductLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
AmiProductSortTypeDef = TypedDict(
    "AmiProductSortTypeDef",
    {
        "SortBy": NotRequired[AmiProductSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)
AmiProductSummaryTypeDef = TypedDict(
    "AmiProductSummaryTypeDef",
    {
        "ProductTitle": NotRequired[str],
        "Visibility": NotRequired[AmiProductVisibilityStringType],
    },
)
EntityRequestTypeDef = TypedDict(
    "EntityRequestTypeDef",
    {
        "Catalog": str,
        "EntityId": str,
    },
)
BatchDescribeErrorDetailTypeDef = TypedDict(
    "BatchDescribeErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
EntityDetailTypeDef = TypedDict(
    "EntityDetailTypeDef",
    {
        "EntityType": NotRequired[str],
        "EntityArn": NotRequired[str],
        "EntityIdentifier": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "DetailsDocument": NotRequired[Dict[str, Any]],
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
CancelChangeSetRequestRequestTypeDef = TypedDict(
    "CancelChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)
ChangeSetSummaryListItemTypeDef = TypedDict(
    "ChangeSetSummaryListItemTypeDef",
    {
        "ChangeSetId": NotRequired[str],
        "ChangeSetArn": NotRequired[str],
        "ChangeSetName": NotRequired[str],
        "StartTime": NotRequired[str],
        "EndTime": NotRequired[str],
        "Status": NotRequired[ChangeStatusType],
        "EntityIdList": NotRequired[List[str]],
        "FailureCode": NotRequired[FailureCodeType],
    },
)
EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Type": str,
        "Identifier": NotRequired[str],
    },
)
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ContainerProductEntityIdFilterTypeDef = TypedDict(
    "ContainerProductEntityIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
ContainerProductTitleFilterTypeDef = TypedDict(
    "ContainerProductTitleFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
ContainerProductVisibilityFilterTypeDef = TypedDict(
    "ContainerProductVisibilityFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[ContainerProductVisibilityStringType]],
    },
)
ContainerProductLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "ContainerProductLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
ContainerProductSortTypeDef = TypedDict(
    "ContainerProductSortTypeDef",
    {
        "SortBy": NotRequired[ContainerProductSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ContainerProductSummaryTypeDef = TypedDict(
    "ContainerProductSummaryTypeDef",
    {
        "ProductTitle": NotRequired[str],
        "Visibility": NotRequired[ContainerProductVisibilityStringType],
    },
)
DataProductEntityIdFilterTypeDef = TypedDict(
    "DataProductEntityIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
DataProductTitleFilterTypeDef = TypedDict(
    "DataProductTitleFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
DataProductVisibilityFilterTypeDef = TypedDict(
    "DataProductVisibilityFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[DataProductVisibilityStringType]],
    },
)
DataProductLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "DataProductLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
DataProductSortTypeDef = TypedDict(
    "DataProductSortTypeDef",
    {
        "SortBy": NotRequired[DataProductSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)
DataProductSummaryTypeDef = TypedDict(
    "DataProductSummaryTypeDef",
    {
        "ProductTitle": NotRequired[str],
        "Visibility": NotRequired[DataProductVisibilityStringType],
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DescribeChangeSetRequestRequestTypeDef = TypedDict(
    "DescribeChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)
DescribeEntityRequestRequestTypeDef = TypedDict(
    "DescribeEntityRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityId": str,
    },
)
OfferSummaryTypeDef = TypedDict(
    "OfferSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "ProductId": NotRequired[str],
        "ResaleAuthorizationId": NotRequired[str],
        "ReleaseDate": NotRequired[str],
        "AvailabilityEndDate": NotRequired[str],
        "BuyerAccounts": NotRequired[List[str]],
        "State": NotRequired[OfferStateStringType],
        "Targeting": NotRequired[List[OfferTargetingStringType]],
    },
)
ResaleAuthorizationSummaryTypeDef = TypedDict(
    "ResaleAuthorizationSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ManufacturerAccountId": NotRequired[str],
        "ManufacturerLegalName": NotRequired[str],
        "ResellerAccountID": NotRequired[str],
        "ResellerLegalName": NotRequired[str],
        "Status": NotRequired[ResaleAuthorizationStatusStringType],
        "OfferExtendedStatus": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "AvailabilityEndDate": NotRequired[str],
    },
)
SaaSProductSummaryTypeDef = TypedDict(
    "SaaSProductSummaryTypeDef",
    {
        "ProductTitle": NotRequired[str],
        "Visibility": NotRequired[SaaSProductVisibilityStringType],
    },
)
OfferSortTypeDef = TypedDict(
    "OfferSortTypeDef",
    {
        "SortBy": NotRequired[OfferSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ResaleAuthorizationSortTypeDef = TypedDict(
    "ResaleAuthorizationSortTypeDef",
    {
        "SortBy": NotRequired[ResaleAuthorizationSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)
SaaSProductSortTypeDef = TypedDict(
    "SaaSProductSortTypeDef",
    {
        "SortBy": NotRequired[SaaSProductSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "ValueList": NotRequired[Sequence[str]],
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
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
SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
OfferAvailabilityEndDateFilterDateRangeTypeDef = TypedDict(
    "OfferAvailabilityEndDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
OfferBuyerAccountsFilterTypeDef = TypedDict(
    "OfferBuyerAccountsFilterTypeDef",
    {
        "WildCardValue": NotRequired[str],
    },
)
OfferEntityIdFilterTypeDef = TypedDict(
    "OfferEntityIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
OfferNameFilterTypeDef = TypedDict(
    "OfferNameFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
OfferProductIdFilterTypeDef = TypedDict(
    "OfferProductIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
OfferResaleAuthorizationIdFilterTypeDef = TypedDict(
    "OfferResaleAuthorizationIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
OfferStateFilterTypeDef = TypedDict(
    "OfferStateFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[OfferStateStringType]],
    },
)
OfferTargetingFilterTypeDef = TypedDict(
    "OfferTargetingFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[OfferTargetingStringType]],
    },
)
OfferLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "OfferLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
OfferReleaseDateFilterDateRangeTypeDef = TypedDict(
    "OfferReleaseDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)
ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef = TypedDict(
    "ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
ResaleAuthorizationCreatedDateFilterDateRangeTypeDef = TypedDict(
    "ResaleAuthorizationCreatedDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
ResaleAuthorizationEntityIdFilterTypeDef = TypedDict(
    "ResaleAuthorizationEntityIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
ResaleAuthorizationManufacturerAccountIdFilterTypeDef = TypedDict(
    "ResaleAuthorizationManufacturerAccountIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
ResaleAuthorizationManufacturerLegalNameFilterTypeDef = TypedDict(
    "ResaleAuthorizationManufacturerLegalNameFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
ResaleAuthorizationNameFilterTypeDef = TypedDict(
    "ResaleAuthorizationNameFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
ResaleAuthorizationOfferExtendedStatusFilterTypeDef = TypedDict(
    "ResaleAuthorizationOfferExtendedStatusFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
ResaleAuthorizationProductIdFilterTypeDef = TypedDict(
    "ResaleAuthorizationProductIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
ResaleAuthorizationProductNameFilterTypeDef = TypedDict(
    "ResaleAuthorizationProductNameFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
ResaleAuthorizationResellerAccountIDFilterTypeDef = TypedDict(
    "ResaleAuthorizationResellerAccountIDFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
ResaleAuthorizationResellerLegalNameFilterTypeDef = TypedDict(
    "ResaleAuthorizationResellerLegalNameFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
ResaleAuthorizationStatusFilterTypeDef = TypedDict(
    "ResaleAuthorizationStatusFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[ResaleAuthorizationStatusStringType]],
    },
)
ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
SaaSProductEntityIdFilterTypeDef = TypedDict(
    "SaaSProductEntityIdFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
SaaSProductTitleFilterTypeDef = TypedDict(
    "SaaSProductTitleFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
        "WildCardValue": NotRequired[str],
    },
)
SaaSProductVisibilityFilterTypeDef = TypedDict(
    "SaaSProductVisibilityFilterTypeDef",
    {
        "ValueList": NotRequired[Sequence[SaaSProductVisibilityStringType]],
    },
)
SaaSProductLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "SaaSProductLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": NotRequired[str],
        "BeforeValue": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
AmiProductLastModifiedDateFilterTypeDef = TypedDict(
    "AmiProductLastModifiedDateFilterTypeDef",
    {
        "DateRange": NotRequired[AmiProductLastModifiedDateFilterDateRangeTypeDef],
    },
)
BatchDescribeEntitiesRequestRequestTypeDef = TypedDict(
    "BatchDescribeEntitiesRequestRequestTypeDef",
    {
        "EntityRequestList": Sequence[EntityRequestTypeDef],
    },
)
BatchDescribeEntitiesResponseTypeDef = TypedDict(
    "BatchDescribeEntitiesResponseTypeDef",
    {
        "EntityDetails": Dict[str, EntityDetailTypeDef],
        "Errors": Dict[str, BatchDescribeErrorDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelChangeSetResponseTypeDef = TypedDict(
    "CancelChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
        "DetailsDocument": Dict[str, Any],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartChangeSetResponseTypeDef = TypedDict(
    "StartChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChangeSetsResponseTypeDef = TypedDict(
    "ListChangeSetsResponseTypeDef",
    {
        "ChangeSetSummaryList": List[ChangeSetSummaryListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ChangeSummaryTypeDef = TypedDict(
    "ChangeSummaryTypeDef",
    {
        "ChangeType": NotRequired[str],
        "Entity": NotRequired[EntityTypeDef],
        "Details": NotRequired[str],
        "DetailsDocument": NotRequired[Dict[str, Any]],
        "ErrorDetailList": NotRequired[List[ErrorDetailTypeDef]],
        "ChangeName": NotRequired[str],
    },
)
ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "ChangeType": str,
        "Entity": EntityTypeDef,
        "EntityTags": NotRequired[Sequence[TagTypeDef]],
        "Details": NotRequired[str],
        "DetailsDocument": NotRequired[Mapping[str, Any]],
        "ChangeName": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ContainerProductLastModifiedDateFilterTypeDef = TypedDict(
    "ContainerProductLastModifiedDateFilterTypeDef",
    {
        "DateRange": NotRequired[ContainerProductLastModifiedDateFilterDateRangeTypeDef],
    },
)
DataProductLastModifiedDateFilterTypeDef = TypedDict(
    "DataProductLastModifiedDateFilterTypeDef",
    {
        "DateRange": NotRequired[DataProductLastModifiedDateFilterDateRangeTypeDef],
    },
)
EntitySummaryTypeDef = TypedDict(
    "EntitySummaryTypeDef",
    {
        "Name": NotRequired[str],
        "EntityType": NotRequired[str],
        "EntityId": NotRequired[str],
        "EntityArn": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Visibility": NotRequired[str],
        "AmiProductSummary": NotRequired[AmiProductSummaryTypeDef],
        "ContainerProductSummary": NotRequired[ContainerProductSummaryTypeDef],
        "DataProductSummary": NotRequired[DataProductSummaryTypeDef],
        "SaaSProductSummary": NotRequired[SaaSProductSummaryTypeDef],
        "OfferSummary": NotRequired[OfferSummaryTypeDef],
        "ResaleAuthorizationSummary": NotRequired[ResaleAuthorizationSummaryTypeDef],
    },
)
EntityTypeSortTypeDef = TypedDict(
    "EntityTypeSortTypeDef",
    {
        "DataProductSort": NotRequired[DataProductSortTypeDef],
        "SaaSProductSort": NotRequired[SaaSProductSortTypeDef],
        "AmiProductSort": NotRequired[AmiProductSortTypeDef],
        "OfferSort": NotRequired[OfferSortTypeDef],
        "ContainerProductSort": NotRequired[ContainerProductSortTypeDef],
        "ResaleAuthorizationSort": NotRequired[ResaleAuthorizationSortTypeDef],
    },
)
ListChangeSetsRequestListChangeSetsPaginateTypeDef = TypedDict(
    "ListChangeSetsRequestListChangeSetsPaginateTypeDef",
    {
        "Catalog": str,
        "FilterList": NotRequired[Sequence[FilterTypeDef]],
        "Sort": NotRequired[SortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListChangeSetsRequestRequestTypeDef = TypedDict(
    "ListChangeSetsRequestRequestTypeDef",
    {
        "Catalog": str,
        "FilterList": NotRequired[Sequence[FilterTypeDef]],
        "Sort": NotRequired[SortTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
OfferAvailabilityEndDateFilterTypeDef = TypedDict(
    "OfferAvailabilityEndDateFilterTypeDef",
    {
        "DateRange": NotRequired[OfferAvailabilityEndDateFilterDateRangeTypeDef],
    },
)
OfferLastModifiedDateFilterTypeDef = TypedDict(
    "OfferLastModifiedDateFilterTypeDef",
    {
        "DateRange": NotRequired[OfferLastModifiedDateFilterDateRangeTypeDef],
    },
)
OfferReleaseDateFilterTypeDef = TypedDict(
    "OfferReleaseDateFilterTypeDef",
    {
        "DateRange": NotRequired[OfferReleaseDateFilterDateRangeTypeDef],
    },
)
ResaleAuthorizationAvailabilityEndDateFilterTypeDef = TypedDict(
    "ResaleAuthorizationAvailabilityEndDateFilterTypeDef",
    {
        "DateRange": NotRequired[ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef],
        "ValueList": NotRequired[Sequence[str]],
    },
)
ResaleAuthorizationCreatedDateFilterTypeDef = TypedDict(
    "ResaleAuthorizationCreatedDateFilterTypeDef",
    {
        "DateRange": NotRequired[ResaleAuthorizationCreatedDateFilterDateRangeTypeDef],
        "ValueList": NotRequired[Sequence[str]],
    },
)
ResaleAuthorizationLastModifiedDateFilterTypeDef = TypedDict(
    "ResaleAuthorizationLastModifiedDateFilterTypeDef",
    {
        "DateRange": NotRequired[ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef],
    },
)
SaaSProductLastModifiedDateFilterTypeDef = TypedDict(
    "SaaSProductLastModifiedDateFilterTypeDef",
    {
        "DateRange": NotRequired[SaaSProductLastModifiedDateFilterDateRangeTypeDef],
    },
)
AmiProductFiltersTypeDef = TypedDict(
    "AmiProductFiltersTypeDef",
    {
        "EntityId": NotRequired[AmiProductEntityIdFilterTypeDef],
        "LastModifiedDate": NotRequired[AmiProductLastModifiedDateFilterTypeDef],
        "ProductTitle": NotRequired[AmiProductTitleFilterTypeDef],
        "Visibility": NotRequired[AmiProductVisibilityFilterTypeDef],
    },
)
DescribeChangeSetResponseTypeDef = TypedDict(
    "DescribeChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "Intent": IntentType,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "FailureCode": FailureCodeType,
        "FailureDescription": str,
        "ChangeSet": List[ChangeSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartChangeSetRequestRequestTypeDef = TypedDict(
    "StartChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSet": Sequence[ChangeTypeDef],
        "ChangeSetName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "ChangeSetTags": NotRequired[Sequence[TagTypeDef]],
        "Intent": NotRequired[IntentType],
    },
)
ContainerProductFiltersTypeDef = TypedDict(
    "ContainerProductFiltersTypeDef",
    {
        "EntityId": NotRequired[ContainerProductEntityIdFilterTypeDef],
        "LastModifiedDate": NotRequired[ContainerProductLastModifiedDateFilterTypeDef],
        "ProductTitle": NotRequired[ContainerProductTitleFilterTypeDef],
        "Visibility": NotRequired[ContainerProductVisibilityFilterTypeDef],
    },
)
DataProductFiltersTypeDef = TypedDict(
    "DataProductFiltersTypeDef",
    {
        "EntityId": NotRequired[DataProductEntityIdFilterTypeDef],
        "ProductTitle": NotRequired[DataProductTitleFilterTypeDef],
        "Visibility": NotRequired[DataProductVisibilityFilterTypeDef],
        "LastModifiedDate": NotRequired[DataProductLastModifiedDateFilterTypeDef],
    },
)
ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "EntitySummaryList": List[EntitySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
OfferFiltersTypeDef = TypedDict(
    "OfferFiltersTypeDef",
    {
        "EntityId": NotRequired[OfferEntityIdFilterTypeDef],
        "Name": NotRequired[OfferNameFilterTypeDef],
        "ProductId": NotRequired[OfferProductIdFilterTypeDef],
        "ResaleAuthorizationId": NotRequired[OfferResaleAuthorizationIdFilterTypeDef],
        "ReleaseDate": NotRequired[OfferReleaseDateFilterTypeDef],
        "AvailabilityEndDate": NotRequired[OfferAvailabilityEndDateFilterTypeDef],
        "BuyerAccounts": NotRequired[OfferBuyerAccountsFilterTypeDef],
        "State": NotRequired[OfferStateFilterTypeDef],
        "Targeting": NotRequired[OfferTargetingFilterTypeDef],
        "LastModifiedDate": NotRequired[OfferLastModifiedDateFilterTypeDef],
    },
)
ResaleAuthorizationFiltersTypeDef = TypedDict(
    "ResaleAuthorizationFiltersTypeDef",
    {
        "EntityId": NotRequired[ResaleAuthorizationEntityIdFilterTypeDef],
        "Name": NotRequired[ResaleAuthorizationNameFilterTypeDef],
        "ProductId": NotRequired[ResaleAuthorizationProductIdFilterTypeDef],
        "CreatedDate": NotRequired[ResaleAuthorizationCreatedDateFilterTypeDef],
        "AvailabilityEndDate": NotRequired[ResaleAuthorizationAvailabilityEndDateFilterTypeDef],
        "ManufacturerAccountId": NotRequired[ResaleAuthorizationManufacturerAccountIdFilterTypeDef],
        "ProductName": NotRequired[ResaleAuthorizationProductNameFilterTypeDef],
        "ManufacturerLegalName": NotRequired[ResaleAuthorizationManufacturerLegalNameFilterTypeDef],
        "ResellerAccountID": NotRequired[ResaleAuthorizationResellerAccountIDFilterTypeDef],
        "ResellerLegalName": NotRequired[ResaleAuthorizationResellerLegalNameFilterTypeDef],
        "Status": NotRequired[ResaleAuthorizationStatusFilterTypeDef],
        "OfferExtendedStatus": NotRequired[ResaleAuthorizationOfferExtendedStatusFilterTypeDef],
        "LastModifiedDate": NotRequired[ResaleAuthorizationLastModifiedDateFilterTypeDef],
    },
)
SaaSProductFiltersTypeDef = TypedDict(
    "SaaSProductFiltersTypeDef",
    {
        "EntityId": NotRequired[SaaSProductEntityIdFilterTypeDef],
        "ProductTitle": NotRequired[SaaSProductTitleFilterTypeDef],
        "Visibility": NotRequired[SaaSProductVisibilityFilterTypeDef],
        "LastModifiedDate": NotRequired[SaaSProductLastModifiedDateFilterTypeDef],
    },
)
EntityTypeFiltersTypeDef = TypedDict(
    "EntityTypeFiltersTypeDef",
    {
        "DataProductFilters": NotRequired[DataProductFiltersTypeDef],
        "SaaSProductFilters": NotRequired[SaaSProductFiltersTypeDef],
        "AmiProductFilters": NotRequired[AmiProductFiltersTypeDef],
        "OfferFilters": NotRequired[OfferFiltersTypeDef],
        "ContainerProductFilters": NotRequired[ContainerProductFiltersTypeDef],
        "ResaleAuthorizationFilters": NotRequired[ResaleAuthorizationFiltersTypeDef],
    },
)
ListEntitiesRequestListEntitiesPaginateTypeDef = TypedDict(
    "ListEntitiesRequestListEntitiesPaginateTypeDef",
    {
        "Catalog": str,
        "EntityType": str,
        "FilterList": NotRequired[Sequence[FilterTypeDef]],
        "Sort": NotRequired[SortTypeDef],
        "OwnershipType": NotRequired[OwnershipTypeType],
        "EntityTypeFilters": NotRequired[EntityTypeFiltersTypeDef],
        "EntityTypeSort": NotRequired[EntityTypeSortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEntitiesRequestRequestTypeDef = TypedDict(
    "ListEntitiesRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityType": str,
        "FilterList": NotRequired[Sequence[FilterTypeDef]],
        "Sort": NotRequired[SortTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "OwnershipType": NotRequired[OwnershipTypeType],
        "EntityTypeFilters": NotRequired[EntityTypeFiltersTypeDef],
        "EntityTypeSort": NotRequired[EntityTypeSortTypeDef],
    },
)
