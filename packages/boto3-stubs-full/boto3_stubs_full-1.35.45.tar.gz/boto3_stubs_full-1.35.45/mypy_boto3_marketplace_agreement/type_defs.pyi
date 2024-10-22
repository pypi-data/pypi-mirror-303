"""
Type annotations for marketplace-agreement service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/type_defs/)

Usage::

    ```python
    from mypy_boto3_marketplace_agreement.type_defs import ByolPricingTermTypeDef

    data: ByolPricingTermTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import AgreementStatusType, SortOrderType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ByolPricingTermTypeDef",
    "RecurringPaymentTermTypeDef",
    "SupportTermTypeDef",
    "ValidityTermTypeDef",
    "AcceptorTypeDef",
    "ProposerTypeDef",
    "DimensionTypeDef",
    "ConstraintsTypeDef",
    "RateCardItemTypeDef",
    "SelectorTypeDef",
    "DescribeAgreementInputRequestTypeDef",
    "EstimatedChargesTypeDef",
    "ResponseMetadataTypeDef",
    "DocumentItemTypeDef",
    "FilterTypeDef",
    "GrantItemTypeDef",
    "GetAgreementTermsInputRequestTypeDef",
    "ScheduleItemTypeDef",
    "ResourceTypeDef",
    "RenewalTermConfigurationTypeDef",
    "SortTypeDef",
    "ConfigurableUpfrontPricingTermConfigurationTypeDef",
    "UsageBasedRateCardItemTypeDef",
    "ConfigurableUpfrontRateCardItemTypeDef",
    "LegalTermTypeDef",
    "FixedUpfrontPricingTermTypeDef",
    "FreeTrialPricingTermTypeDef",
    "PaymentScheduleTermTypeDef",
    "ProposalSummaryTypeDef",
    "RenewalTermTypeDef",
    "SearchAgreementsInputRequestTypeDef",
    "UsageBasedPricingTermTypeDef",
    "ConfigurableUpfrontPricingTermTypeDef",
    "AgreementViewSummaryTypeDef",
    "DescribeAgreementOutputTypeDef",
    "AcceptedTermTypeDef",
    "SearchAgreementsOutputTypeDef",
    "GetAgreementTermsOutputTypeDef",
)

ByolPricingTermTypeDef = TypedDict(
    "ByolPricingTermTypeDef",
    {
        "type": NotRequired[str],
    },
)
RecurringPaymentTermTypeDef = TypedDict(
    "RecurringPaymentTermTypeDef",
    {
        "billingPeriod": NotRequired[str],
        "currencyCode": NotRequired[str],
        "price": NotRequired[str],
        "type": NotRequired[str],
    },
)
SupportTermTypeDef = TypedDict(
    "SupportTermTypeDef",
    {
        "refundPolicy": NotRequired[str],
        "type": NotRequired[str],
    },
)
ValidityTermTypeDef = TypedDict(
    "ValidityTermTypeDef",
    {
        "agreementDuration": NotRequired[str],
        "agreementEndDate": NotRequired[datetime],
        "agreementStartDate": NotRequired[datetime],
        "type": NotRequired[str],
    },
)
AcceptorTypeDef = TypedDict(
    "AcceptorTypeDef",
    {
        "accountId": NotRequired[str],
    },
)
ProposerTypeDef = TypedDict(
    "ProposerTypeDef",
    {
        "accountId": NotRequired[str],
    },
)
DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "dimensionKey": str,
        "dimensionValue": int,
    },
)
ConstraintsTypeDef = TypedDict(
    "ConstraintsTypeDef",
    {
        "multipleDimensionSelection": NotRequired[str],
        "quantityConfiguration": NotRequired[str],
    },
)
RateCardItemTypeDef = TypedDict(
    "RateCardItemTypeDef",
    {
        "dimensionKey": NotRequired[str],
        "price": NotRequired[str],
    },
)
SelectorTypeDef = TypedDict(
    "SelectorTypeDef",
    {
        "type": NotRequired[str],
        "value": NotRequired[str],
    },
)
DescribeAgreementInputRequestTypeDef = TypedDict(
    "DescribeAgreementInputRequestTypeDef",
    {
        "agreementId": str,
    },
)
EstimatedChargesTypeDef = TypedDict(
    "EstimatedChargesTypeDef",
    {
        "agreementValue": NotRequired[str],
        "currencyCode": NotRequired[str],
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
DocumentItemTypeDef = TypedDict(
    "DocumentItemTypeDef",
    {
        "type": NotRequired[str],
        "url": NotRequired[str],
        "version": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
GrantItemTypeDef = TypedDict(
    "GrantItemTypeDef",
    {
        "dimensionKey": NotRequired[str],
        "maxQuantity": NotRequired[int],
    },
)
GetAgreementTermsInputRequestTypeDef = TypedDict(
    "GetAgreementTermsInputRequestTypeDef",
    {
        "agreementId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ScheduleItemTypeDef = TypedDict(
    "ScheduleItemTypeDef",
    {
        "chargeAmount": NotRequired[str],
        "chargeDate": NotRequired[datetime],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[str],
    },
)
RenewalTermConfigurationTypeDef = TypedDict(
    "RenewalTermConfigurationTypeDef",
    {
        "enableAutoRenew": bool,
    },
)
SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "sortBy": NotRequired[str],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ConfigurableUpfrontPricingTermConfigurationTypeDef = TypedDict(
    "ConfigurableUpfrontPricingTermConfigurationTypeDef",
    {
        "dimensions": List[DimensionTypeDef],
        "selectorValue": str,
    },
)
UsageBasedRateCardItemTypeDef = TypedDict(
    "UsageBasedRateCardItemTypeDef",
    {
        "rateCard": NotRequired[List[RateCardItemTypeDef]],
    },
)
ConfigurableUpfrontRateCardItemTypeDef = TypedDict(
    "ConfigurableUpfrontRateCardItemTypeDef",
    {
        "constraints": NotRequired[ConstraintsTypeDef],
        "rateCard": NotRequired[List[RateCardItemTypeDef]],
        "selector": NotRequired[SelectorTypeDef],
    },
)
LegalTermTypeDef = TypedDict(
    "LegalTermTypeDef",
    {
        "documents": NotRequired[List[DocumentItemTypeDef]],
        "type": NotRequired[str],
    },
)
FixedUpfrontPricingTermTypeDef = TypedDict(
    "FixedUpfrontPricingTermTypeDef",
    {
        "currencyCode": NotRequired[str],
        "duration": NotRequired[str],
        "grants": NotRequired[List[GrantItemTypeDef]],
        "price": NotRequired[str],
        "type": NotRequired[str],
    },
)
FreeTrialPricingTermTypeDef = TypedDict(
    "FreeTrialPricingTermTypeDef",
    {
        "duration": NotRequired[str],
        "grants": NotRequired[List[GrantItemTypeDef]],
        "type": NotRequired[str],
    },
)
PaymentScheduleTermTypeDef = TypedDict(
    "PaymentScheduleTermTypeDef",
    {
        "currencyCode": NotRequired[str],
        "schedule": NotRequired[List[ScheduleItemTypeDef]],
        "type": NotRequired[str],
    },
)
ProposalSummaryTypeDef = TypedDict(
    "ProposalSummaryTypeDef",
    {
        "offerId": NotRequired[str],
        "resources": NotRequired[List[ResourceTypeDef]],
    },
)
RenewalTermTypeDef = TypedDict(
    "RenewalTermTypeDef",
    {
        "configuration": NotRequired[RenewalTermConfigurationTypeDef],
        "type": NotRequired[str],
    },
)
SearchAgreementsInputRequestTypeDef = TypedDict(
    "SearchAgreementsInputRequestTypeDef",
    {
        "catalog": NotRequired[str],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortTypeDef],
    },
)
UsageBasedPricingTermTypeDef = TypedDict(
    "UsageBasedPricingTermTypeDef",
    {
        "currencyCode": NotRequired[str],
        "rateCards": NotRequired[List[UsageBasedRateCardItemTypeDef]],
        "type": NotRequired[str],
    },
)
ConfigurableUpfrontPricingTermTypeDef = TypedDict(
    "ConfigurableUpfrontPricingTermTypeDef",
    {
        "configuration": NotRequired[ConfigurableUpfrontPricingTermConfigurationTypeDef],
        "currencyCode": NotRequired[str],
        "rateCards": NotRequired[List[ConfigurableUpfrontRateCardItemTypeDef]],
        "type": NotRequired[str],
    },
)
AgreementViewSummaryTypeDef = TypedDict(
    "AgreementViewSummaryTypeDef",
    {
        "acceptanceTime": NotRequired[datetime],
        "acceptor": NotRequired[AcceptorTypeDef],
        "agreementId": NotRequired[str],
        "agreementType": NotRequired[str],
        "endTime": NotRequired[datetime],
        "proposalSummary": NotRequired[ProposalSummaryTypeDef],
        "proposer": NotRequired[ProposerTypeDef],
        "startTime": NotRequired[datetime],
        "status": NotRequired[AgreementStatusType],
    },
)
DescribeAgreementOutputTypeDef = TypedDict(
    "DescribeAgreementOutputTypeDef",
    {
        "acceptanceTime": datetime,
        "acceptor": AcceptorTypeDef,
        "agreementId": str,
        "agreementType": str,
        "endTime": datetime,
        "estimatedCharges": EstimatedChargesTypeDef,
        "proposalSummary": ProposalSummaryTypeDef,
        "proposer": ProposerTypeDef,
        "startTime": datetime,
        "status": AgreementStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptedTermTypeDef = TypedDict(
    "AcceptedTermTypeDef",
    {
        "byolPricingTerm": NotRequired[ByolPricingTermTypeDef],
        "configurableUpfrontPricingTerm": NotRequired[ConfigurableUpfrontPricingTermTypeDef],
        "fixedUpfrontPricingTerm": NotRequired[FixedUpfrontPricingTermTypeDef],
        "freeTrialPricingTerm": NotRequired[FreeTrialPricingTermTypeDef],
        "legalTerm": NotRequired[LegalTermTypeDef],
        "paymentScheduleTerm": NotRequired[PaymentScheduleTermTypeDef],
        "recurringPaymentTerm": NotRequired[RecurringPaymentTermTypeDef],
        "renewalTerm": NotRequired[RenewalTermTypeDef],
        "supportTerm": NotRequired[SupportTermTypeDef],
        "usageBasedPricingTerm": NotRequired[UsageBasedPricingTermTypeDef],
        "validityTerm": NotRequired[ValidityTermTypeDef],
    },
)
SearchAgreementsOutputTypeDef = TypedDict(
    "SearchAgreementsOutputTypeDef",
    {
        "agreementViewSummaries": List[AgreementViewSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAgreementTermsOutputTypeDef = TypedDict(
    "GetAgreementTermsOutputTypeDef",
    {
        "acceptedTerms": List[AcceptedTermTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
