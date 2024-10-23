"""
Type annotations for savingsplans service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/type_defs/)

Usage::

    ```python
    from mypy_boto3_savingsplans.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    CurrencyCodeType,
    SavingsPlanOfferingFilterAttributeType,
    SavingsPlanOfferingPropertyKeyType,
    SavingsPlanPaymentOptionType,
    SavingsPlanProductTypeType,
    SavingsPlanRateFilterAttributeType,
    SavingsPlanRateFilterNameType,
    SavingsPlanRatePropertyKeyType,
    SavingsPlanRateServiceCodeType,
    SavingsPlanRateUnitType,
    SavingsPlansFilterNameType,
    SavingsPlanStateType,
    SavingsPlanTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteQueuedSavingsPlanRequestRequestTypeDef",
    "SavingsPlanRateFilterTypeDef",
    "SavingsPlanOfferingRateFilterElementTypeDef",
    "SavingsPlanOfferingFilterElementTypeDef",
    "SavingsPlanFilterTypeDef",
    "SavingsPlanTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ParentSavingsPlanOfferingTypeDef",
    "ReturnSavingsPlanRequestRequestTypeDef",
    "SavingsPlanOfferingPropertyTypeDef",
    "SavingsPlanOfferingRatePropertyTypeDef",
    "SavingsPlanRatePropertyTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateSavingsPlanRequestRequestTypeDef",
    "CreateSavingsPlanResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ReturnSavingsPlanResponseTypeDef",
    "DescribeSavingsPlanRatesRequestRequestTypeDef",
    "DescribeSavingsPlansOfferingRatesRequestRequestTypeDef",
    "DescribeSavingsPlansOfferingsRequestRequestTypeDef",
    "DescribeSavingsPlansRequestRequestTypeDef",
    "DescribeSavingsPlansResponseTypeDef",
    "SavingsPlanOfferingTypeDef",
    "SavingsPlanOfferingRateTypeDef",
    "SavingsPlanRateTypeDef",
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    "DescribeSavingsPlanRatesResponseTypeDef",
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
DeleteQueuedSavingsPlanRequestRequestTypeDef = TypedDict(
    "DeleteQueuedSavingsPlanRequestRequestTypeDef",
    {
        "savingsPlanId": str,
    },
)
SavingsPlanRateFilterTypeDef = TypedDict(
    "SavingsPlanRateFilterTypeDef",
    {
        "name": NotRequired[SavingsPlanRateFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)
SavingsPlanOfferingRateFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingRateFilterElementTypeDef",
    {
        "name": NotRequired[SavingsPlanRateFilterAttributeType],
        "values": NotRequired[Sequence[str]],
    },
)
SavingsPlanOfferingFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingFilterElementTypeDef",
    {
        "name": NotRequired[SavingsPlanOfferingFilterAttributeType],
        "values": NotRequired[Sequence[str]],
    },
)
SavingsPlanFilterTypeDef = TypedDict(
    "SavingsPlanFilterTypeDef",
    {
        "name": NotRequired[SavingsPlansFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)
SavingsPlanTypeDef = TypedDict(
    "SavingsPlanTypeDef",
    {
        "offeringId": NotRequired[str],
        "savingsPlanId": NotRequired[str],
        "savingsPlanArn": NotRequired[str],
        "description": NotRequired[str],
        "start": NotRequired[str],
        "end": NotRequired[str],
        "state": NotRequired[SavingsPlanStateType],
        "region": NotRequired[str],
        "ec2InstanceFamily": NotRequired[str],
        "savingsPlanType": NotRequired[SavingsPlanTypeType],
        "paymentOption": NotRequired[SavingsPlanPaymentOptionType],
        "productTypes": NotRequired[List[SavingsPlanProductTypeType]],
        "currency": NotRequired[CurrencyCodeType],
        "commitment": NotRequired[str],
        "upfrontPaymentAmount": NotRequired[str],
        "recurringPaymentAmount": NotRequired[str],
        "termDurationInSeconds": NotRequired[int],
        "tags": NotRequired[Dict[str, str]],
        "returnableUntil": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ParentSavingsPlanOfferingTypeDef = TypedDict(
    "ParentSavingsPlanOfferingTypeDef",
    {
        "offeringId": NotRequired[str],
        "paymentOption": NotRequired[SavingsPlanPaymentOptionType],
        "planType": NotRequired[SavingsPlanTypeType],
        "durationSeconds": NotRequired[int],
        "currency": NotRequired[CurrencyCodeType],
        "planDescription": NotRequired[str],
    },
)
ReturnSavingsPlanRequestRequestTypeDef = TypedDict(
    "ReturnSavingsPlanRequestRequestTypeDef",
    {
        "savingsPlanId": str,
        "clientToken": NotRequired[str],
    },
)
SavingsPlanOfferingPropertyTypeDef = TypedDict(
    "SavingsPlanOfferingPropertyTypeDef",
    {
        "name": NotRequired[SavingsPlanOfferingPropertyKeyType],
        "value": NotRequired[str],
    },
)
SavingsPlanOfferingRatePropertyTypeDef = TypedDict(
    "SavingsPlanOfferingRatePropertyTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)
SavingsPlanRatePropertyTypeDef = TypedDict(
    "SavingsPlanRatePropertyTypeDef",
    {
        "name": NotRequired[SavingsPlanRatePropertyKeyType],
        "value": NotRequired[str],
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
CreateSavingsPlanRequestRequestTypeDef = TypedDict(
    "CreateSavingsPlanRequestRequestTypeDef",
    {
        "savingsPlanOfferingId": str,
        "commitment": str,
        "upfrontPaymentAmount": NotRequired[str],
        "purchaseTime": NotRequired[TimestampTypeDef],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateSavingsPlanResponseTypeDef = TypedDict(
    "CreateSavingsPlanResponseTypeDef",
    {
        "savingsPlanId": str,
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
ReturnSavingsPlanResponseTypeDef = TypedDict(
    "ReturnSavingsPlanResponseTypeDef",
    {
        "savingsPlanId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSavingsPlanRatesRequestRequestTypeDef = TypedDict(
    "DescribeSavingsPlanRatesRequestRequestTypeDef",
    {
        "savingsPlanId": str,
        "filters": NotRequired[Sequence[SavingsPlanRateFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeSavingsPlansOfferingRatesRequestRequestTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingRatesRequestRequestTypeDef",
    {
        "savingsPlanOfferingIds": NotRequired[Sequence[str]],
        "savingsPlanPaymentOptions": NotRequired[Sequence[SavingsPlanPaymentOptionType]],
        "savingsPlanTypes": NotRequired[Sequence[SavingsPlanTypeType]],
        "products": NotRequired[Sequence[SavingsPlanProductTypeType]],
        "serviceCodes": NotRequired[Sequence[SavingsPlanRateServiceCodeType]],
        "usageTypes": NotRequired[Sequence[str]],
        "operations": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[SavingsPlanOfferingRateFilterElementTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeSavingsPlansOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingsRequestRequestTypeDef",
    {
        "offeringIds": NotRequired[Sequence[str]],
        "paymentOptions": NotRequired[Sequence[SavingsPlanPaymentOptionType]],
        "productType": NotRequired[SavingsPlanProductTypeType],
        "planTypes": NotRequired[Sequence[SavingsPlanTypeType]],
        "durations": NotRequired[Sequence[int]],
        "currencies": NotRequired[Sequence[CurrencyCodeType]],
        "descriptions": NotRequired[Sequence[str]],
        "serviceCodes": NotRequired[Sequence[str]],
        "usageTypes": NotRequired[Sequence[str]],
        "operations": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[SavingsPlanOfferingFilterElementTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeSavingsPlansRequestRequestTypeDef = TypedDict(
    "DescribeSavingsPlansRequestRequestTypeDef",
    {
        "savingsPlanArns": NotRequired[Sequence[str]],
        "savingsPlanIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "states": NotRequired[Sequence[SavingsPlanStateType]],
        "filters": NotRequired[Sequence[SavingsPlanFilterTypeDef]],
    },
)
DescribeSavingsPlansResponseTypeDef = TypedDict(
    "DescribeSavingsPlansResponseTypeDef",
    {
        "savingsPlans": List[SavingsPlanTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SavingsPlanOfferingTypeDef = TypedDict(
    "SavingsPlanOfferingTypeDef",
    {
        "offeringId": NotRequired[str],
        "productTypes": NotRequired[List[SavingsPlanProductTypeType]],
        "planType": NotRequired[SavingsPlanTypeType],
        "description": NotRequired[str],
        "paymentOption": NotRequired[SavingsPlanPaymentOptionType],
        "durationSeconds": NotRequired[int],
        "currency": NotRequired[CurrencyCodeType],
        "serviceCode": NotRequired[str],
        "usageType": NotRequired[str],
        "operation": NotRequired[str],
        "properties": NotRequired[List[SavingsPlanOfferingPropertyTypeDef]],
    },
)
SavingsPlanOfferingRateTypeDef = TypedDict(
    "SavingsPlanOfferingRateTypeDef",
    {
        "savingsPlanOffering": NotRequired[ParentSavingsPlanOfferingTypeDef],
        "rate": NotRequired[str],
        "unit": NotRequired[SavingsPlanRateUnitType],
        "productType": NotRequired[SavingsPlanProductTypeType],
        "serviceCode": NotRequired[SavingsPlanRateServiceCodeType],
        "usageType": NotRequired[str],
        "operation": NotRequired[str],
        "properties": NotRequired[List[SavingsPlanOfferingRatePropertyTypeDef]],
    },
)
SavingsPlanRateTypeDef = TypedDict(
    "SavingsPlanRateTypeDef",
    {
        "rate": NotRequired[str],
        "currency": NotRequired[CurrencyCodeType],
        "unit": NotRequired[SavingsPlanRateUnitType],
        "productType": NotRequired[SavingsPlanProductTypeType],
        "serviceCode": NotRequired[SavingsPlanRateServiceCodeType],
        "usageType": NotRequired[str],
        "operation": NotRequired[str],
        "properties": NotRequired[List[SavingsPlanRatePropertyTypeDef]],
    },
)
DescribeSavingsPlansOfferingsResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    {
        "searchResults": List[SavingsPlanOfferingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSavingsPlansOfferingRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    {
        "searchResults": List[SavingsPlanOfferingRateTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSavingsPlanRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlanRatesResponseTypeDef",
    {
        "savingsPlanId": str,
        "searchResults": List[SavingsPlanRateTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
