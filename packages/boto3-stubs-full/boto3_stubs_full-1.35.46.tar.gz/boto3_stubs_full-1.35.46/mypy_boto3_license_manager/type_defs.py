"""
Type annotations for license-manager service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/type_defs/)

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AcceptGrantRequestRequestTypeDef

    data: AcceptGrantRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ActivationOverrideBehaviorType,
    AllowedOperationType,
    CheckoutTypeType,
    EntitlementDataUnitType,
    EntitlementUnitType,
    GrantStatusType,
    InventoryFilterConditionType,
    LicenseConfigurationStatusType,
    LicenseConversionTaskStatusType,
    LicenseCountingTypeType,
    LicenseDeletionStatusType,
    LicenseStatusType,
    ReceivedStatusType,
    RenewTypeType,
    ReportFrequencyTypeType,
    ReportTypeType,
    ResourceTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceptGrantRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "CheckInLicenseRequestRequestTypeDef",
    "EntitlementDataTypeDef",
    "MetadataTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ProvisionalConfigurationTypeDef",
    "CreateGrantRequestRequestTypeDef",
    "OptionsTypeDef",
    "TagTypeDef",
    "LicenseConversionContextTypeDef",
    "ReportContextTypeDef",
    "ReportFrequencyTypeDef",
    "DatetimeRangeTypeDef",
    "EntitlementTypeDef",
    "IssuerTypeDef",
    "CreateTokenRequestRequestTypeDef",
    "DeleteGrantRequestRequestTypeDef",
    "DeleteLicenseConfigurationRequestRequestTypeDef",
    "DeleteLicenseManagerReportGeneratorRequestRequestTypeDef",
    "DeleteLicenseRequestRequestTypeDef",
    "DeleteTokenRequestRequestTypeDef",
    "EntitlementUsageTypeDef",
    "ExtendLicenseConsumptionRequestRequestTypeDef",
    "FilterTypeDef",
    "GetAccessTokenRequestRequestTypeDef",
    "GetGrantRequestRequestTypeDef",
    "GetLicenseConfigurationRequestRequestTypeDef",
    "ManagedResourceSummaryTypeDef",
    "GetLicenseConversionTaskRequestRequestTypeDef",
    "GetLicenseManagerReportGeneratorRequestRequestTypeDef",
    "GetLicenseRequestRequestTypeDef",
    "GetLicenseUsageRequestRequestTypeDef",
    "OrganizationConfigurationTypeDef",
    "IssuerDetailsTypeDef",
    "ReceivedMetadataTypeDef",
    "InventoryFilterTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    "ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    "ListLicenseSpecificationsForResourceRequestRequestTypeDef",
    "ListLicenseVersionsRequestRequestTypeDef",
    "ResourceInventoryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TokenDataTypeDef",
    "ProductInformationFilterOutputTypeDef",
    "ProductInformationFilterTypeDef",
    "RejectGrantRequestRequestTypeDef",
    "ReportContextOutputTypeDef",
    "S3LocationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AcceptGrantResponseTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "CreateLicenseConversionTaskForResourceResponseTypeDef",
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenResponseTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseResponseTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "GetAccessTokenResponseTypeDef",
    "RejectGrantResponseTypeDef",
    "CheckoutLicenseRequestRequestTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "CheckoutBorrowLicenseRequestRequestTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "LicenseOperationFailureTypeDef",
    "ConsumptionConfigurationTypeDef",
    "CreateGrantVersionRequestRequestTypeDef",
    "GrantTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateLicenseConversionTaskForResourceRequestRequestTypeDef",
    "GetLicenseConversionTaskResponseTypeDef",
    "LicenseConversionTaskTypeDef",
    "CreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    "UpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    "LicenseUsageTypeDef",
    "ListDistributedGrantsRequestRequestTypeDef",
    "ListLicenseConfigurationsRequestRequestTypeDef",
    "ListLicenseConversionTasksRequestRequestTypeDef",
    "ListLicenseManagerReportGeneratorsRequestRequestTypeDef",
    "ListLicensesRequestRequestTypeDef",
    "ListReceivedGrantsForOrganizationRequestRequestTypeDef",
    "ListReceivedGrantsRequestRequestTypeDef",
    "ListReceivedLicensesForOrganizationRequestRequestTypeDef",
    "ListReceivedLicensesRequestRequestTypeDef",
    "ListTokensRequestRequestTypeDef",
    "ListUsageForLicenseConfigurationRequestRequestTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "UpdateServiceSettingsRequestRequestTypeDef",
    "ListResourceInventoryRequestRequestTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "UpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    "ListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef",
    "ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateTypeDef",
    "ListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef",
    "ListResourceInventoryRequestListResourceInventoryPaginateTypeDef",
    "ListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTokensResponseTypeDef",
    "ProductInformationOutputTypeDef",
    "ProductInformationFilterUnionTypeDef",
    "ReportGeneratorTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "CreateLicenseRequestRequestTypeDef",
    "CreateLicenseVersionRequestRequestTypeDef",
    "GrantedLicenseTypeDef",
    "LicenseTypeDef",
    "GetGrantResponseTypeDef",
    "ListDistributedGrantsResponseTypeDef",
    "ListReceivedGrantsForOrganizationResponseTypeDef",
    "ListReceivedGrantsResponseTypeDef",
    "ListLicenseConversionTasksResponseTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "LicenseConfigurationTypeDef",
    "ProductInformationTypeDef",
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    "ListReceivedLicensesForOrganizationResponseTypeDef",
    "ListReceivedLicensesResponseTypeDef",
    "GetLicenseResponseTypeDef",
    "ListLicenseVersionsResponseTypeDef",
    "ListLicensesResponseTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "ProductInformationUnionTypeDef",
    "UpdateLicenseConfigurationRequestRequestTypeDef",
    "CreateLicenseConfigurationRequestRequestTypeDef",
)

AcceptGrantRequestRequestTypeDef = TypedDict(
    "AcceptGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
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
AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef",
    {
        "LastRunTime": NotRequired[datetime],
    },
)
BorrowConfigurationTypeDef = TypedDict(
    "BorrowConfigurationTypeDef",
    {
        "AllowEarlyCheckIn": bool,
        "MaxTimeToLiveInMinutes": int,
    },
)
CheckInLicenseRequestRequestTypeDef = TypedDict(
    "CheckInLicenseRequestRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
        "Beneficiary": NotRequired[str],
    },
)
EntitlementDataTypeDef = TypedDict(
    "EntitlementDataTypeDef",
    {
        "Name": str,
        "Unit": EntitlementDataUnitType,
        "Value": NotRequired[str],
    },
)
MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ConsumedLicenseSummaryTypeDef = TypedDict(
    "ConsumedLicenseSummaryTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "ConsumedLicenses": NotRequired[int],
    },
)
ProvisionalConfigurationTypeDef = TypedDict(
    "ProvisionalConfigurationTypeDef",
    {
        "MaxTimeToLiveInMinutes": int,
    },
)
CreateGrantRequestRequestTypeDef = TypedDict(
    "CreateGrantRequestRequestTypeDef",
    {
        "ClientToken": str,
        "GrantName": str,
        "LicenseArn": str,
        "Principals": Sequence[str],
        "HomeRegion": str,
        "AllowedOperations": Sequence[AllowedOperationType],
    },
)
OptionsTypeDef = TypedDict(
    "OptionsTypeDef",
    {
        "ActivationOverrideBehavior": NotRequired[ActivationOverrideBehaviorType],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
LicenseConversionContextTypeDef = TypedDict(
    "LicenseConversionContextTypeDef",
    {
        "UsageOperation": NotRequired[str],
    },
)
ReportContextTypeDef = TypedDict(
    "ReportContextTypeDef",
    {
        "licenseConfigurationArns": Sequence[str],
    },
)
ReportFrequencyTypeDef = TypedDict(
    "ReportFrequencyTypeDef",
    {
        "value": NotRequired[int],
        "period": NotRequired[ReportFrequencyTypeType],
    },
)
DatetimeRangeTypeDef = TypedDict(
    "DatetimeRangeTypeDef",
    {
        "Begin": str,
        "End": NotRequired[str],
    },
)
EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "Name": str,
        "Unit": EntitlementUnitType,
        "Value": NotRequired[str],
        "MaxCount": NotRequired[int],
        "Overage": NotRequired[bool],
        "AllowCheckIn": NotRequired[bool],
    },
)
IssuerTypeDef = TypedDict(
    "IssuerTypeDef",
    {
        "Name": str,
        "SignKey": NotRequired[str],
    },
)
CreateTokenRequestRequestTypeDef = TypedDict(
    "CreateTokenRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "ClientToken": str,
        "RoleArns": NotRequired[Sequence[str]],
        "ExpirationInDays": NotRequired[int],
        "TokenProperties": NotRequired[Sequence[str]],
    },
)
DeleteGrantRequestRequestTypeDef = TypedDict(
    "DeleteGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
        "Version": str,
        "StatusReason": NotRequired[str],
    },
)
DeleteLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
DeleteLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "DeleteLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)
DeleteLicenseRequestRequestTypeDef = TypedDict(
    "DeleteLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "SourceVersion": str,
    },
)
DeleteTokenRequestRequestTypeDef = TypedDict(
    "DeleteTokenRequestRequestTypeDef",
    {
        "TokenId": str,
    },
)
EntitlementUsageTypeDef = TypedDict(
    "EntitlementUsageTypeDef",
    {
        "Name": str,
        "ConsumedValue": str,
        "Unit": EntitlementDataUnitType,
        "MaxCount": NotRequired[str],
    },
)
ExtendLicenseConsumptionRequestRequestTypeDef = TypedDict(
    "ExtendLicenseConsumptionRequestRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
        "DryRun": NotRequired[bool],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
GetAccessTokenRequestRequestTypeDef = TypedDict(
    "GetAccessTokenRequestRequestTypeDef",
    {
        "Token": str,
        "TokenProperties": NotRequired[Sequence[str]],
    },
)
GetGrantRequestRequestTypeDef = TypedDict(
    "GetGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
        "Version": NotRequired[str],
    },
)
GetLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "GetLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "AssociationCount": NotRequired[int],
    },
)
GetLicenseConversionTaskRequestRequestTypeDef = TypedDict(
    "GetLicenseConversionTaskRequestRequestTypeDef",
    {
        "LicenseConversionTaskId": str,
    },
)
GetLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)
GetLicenseRequestRequestTypeDef = TypedDict(
    "GetLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "Version": NotRequired[str],
    },
)
GetLicenseUsageRequestRequestTypeDef = TypedDict(
    "GetLicenseUsageRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)
OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef",
    {
        "EnableIntegration": bool,
    },
)
IssuerDetailsTypeDef = TypedDict(
    "IssuerDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "SignKey": NotRequired[str],
        "KeyFingerprint": NotRequired[str],
    },
)
ReceivedMetadataTypeDef = TypedDict(
    "ReceivedMetadataTypeDef",
    {
        "ReceivedStatus": NotRequired[ReceivedStatusType],
        "ReceivedStatusReason": NotRequired[str],
        "AllowedOperations": NotRequired[List[AllowedOperationType]],
    },
)
InventoryFilterTypeDef = TypedDict(
    "InventoryFilterTypeDef",
    {
        "Name": str,
        "Condition": InventoryFilterConditionType,
        "Value": NotRequired[str],
    },
)
LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ResourceOwnerId": NotRequired[str],
        "AssociationTime": NotRequired[datetime],
        "AmiAssociationScope": NotRequired[str],
    },
)
LicenseConfigurationUsageTypeDef = TypedDict(
    "LicenseConfigurationUsageTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ResourceStatus": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "AssociationTime": NotRequired[datetime],
        "ConsumedLicenses": NotRequired[int],
    },
)
LicenseSpecificationTypeDef = TypedDict(
    "LicenseSpecificationTypeDef",
    {
        "LicenseConfigurationArn": str,
        "AmiAssociationScope": NotRequired[str],
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
ListAssociationsForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLicenseVersionsRequestRequestTypeDef = TypedDict(
    "ListLicenseVersionsRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ResourceInventoryTypeDef = TypedDict(
    "ResourceInventoryTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ResourceArn": NotRequired[str],
        "Platform": NotRequired[str],
        "PlatformVersion": NotRequired[str],
        "ResourceOwningAccountId": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TokenDataTypeDef = TypedDict(
    "TokenDataTypeDef",
    {
        "TokenId": NotRequired[str],
        "TokenType": NotRequired[str],
        "LicenseArn": NotRequired[str],
        "ExpirationTime": NotRequired[str],
        "TokenProperties": NotRequired[List[str]],
        "RoleArns": NotRequired[List[str]],
        "Status": NotRequired[str],
    },
)
ProductInformationFilterOutputTypeDef = TypedDict(
    "ProductInformationFilterOutputTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterComparator": str,
        "ProductInformationFilterValue": NotRequired[List[str]],
    },
)
ProductInformationFilterTypeDef = TypedDict(
    "ProductInformationFilterTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterComparator": str,
        "ProductInformationFilterValue": NotRequired[Sequence[str]],
    },
)
RejectGrantRequestRequestTypeDef = TypedDict(
    "RejectGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)
ReportContextOutputTypeDef = TypedDict(
    "ReportContextOutputTypeDef",
    {
        "licenseConfigurationArns": List[str],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
AcceptGrantResponseTypeDef = TypedDict(
    "AcceptGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGrantVersionResponseTypeDef = TypedDict(
    "CreateGrantVersionResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLicenseConfigurationResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLicenseConversionTaskForResourceResponseTypeDef = TypedDict(
    "CreateLicenseConversionTaskForResourceResponseTypeDef",
    {
        "LicenseConversionTaskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLicenseResponseTypeDef = TypedDict(
    "CreateLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "Status": LicenseStatusType,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLicenseVersionResponseTypeDef = TypedDict(
    "CreateLicenseVersionResponseTypeDef",
    {
        "LicenseArn": str,
        "Version": str,
        "Status": LicenseStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "TokenId": str,
        "TokenType": Literal["REFRESH_TOKEN"],
        "Token": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGrantResponseTypeDef = TypedDict(
    "DeleteGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLicenseResponseTypeDef = TypedDict(
    "DeleteLicenseResponseTypeDef",
    {
        "Status": LicenseDeletionStatusType,
        "DeletionDate": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExtendLicenseConsumptionResponseTypeDef = TypedDict(
    "ExtendLicenseConsumptionResponseTypeDef",
    {
        "LicenseConsumptionToken": str,
        "Expiration": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessTokenResponseTypeDef = TypedDict(
    "GetAccessTokenResponseTypeDef",
    {
        "AccessToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectGrantResponseTypeDef = TypedDict(
    "RejectGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CheckoutLicenseRequestRequestTypeDef = TypedDict(
    "CheckoutLicenseRequestRequestTypeDef",
    {
        "ProductSKU": str,
        "CheckoutType": CheckoutTypeType,
        "KeyFingerprint": str,
        "Entitlements": Sequence[EntitlementDataTypeDef],
        "ClientToken": str,
        "Beneficiary": NotRequired[str],
        "NodeId": NotRequired[str],
    },
)
CheckoutLicenseResponseTypeDef = TypedDict(
    "CheckoutLicenseResponseTypeDef",
    {
        "CheckoutType": CheckoutTypeType,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List[EntitlementDataTypeDef],
        "SignedToken": str,
        "NodeId": str,
        "IssuedAt": str,
        "Expiration": str,
        "LicenseArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CheckoutBorrowLicenseRequestRequestTypeDef = TypedDict(
    "CheckoutBorrowLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "Entitlements": Sequence[EntitlementDataTypeDef],
        "DigitalSignatureMethod": Literal["JWT_PS384"],
        "ClientToken": str,
        "NodeId": NotRequired[str],
        "CheckoutMetadata": NotRequired[Sequence[MetadataTypeDef]],
    },
)
CheckoutBorrowLicenseResponseTypeDef = TypedDict(
    "CheckoutBorrowLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List[EntitlementDataTypeDef],
        "NodeId": str,
        "SignedToken": str,
        "IssuedAt": str,
        "Expiration": str,
        "CheckoutMetadata": List[MetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LicenseOperationFailureTypeDef = TypedDict(
    "LicenseOperationFailureTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ErrorMessage": NotRequired[str],
        "FailureTime": NotRequired[datetime],
        "OperationName": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "OperationRequestedBy": NotRequired[str],
        "MetadataList": NotRequired[List[MetadataTypeDef]],
    },
)
ConsumptionConfigurationTypeDef = TypedDict(
    "ConsumptionConfigurationTypeDef",
    {
        "RenewType": NotRequired[RenewTypeType],
        "ProvisionalConfiguration": NotRequired[ProvisionalConfigurationTypeDef],
        "BorrowConfiguration": NotRequired[BorrowConfigurationTypeDef],
    },
)
CreateGrantVersionRequestRequestTypeDef = TypedDict(
    "CreateGrantVersionRequestRequestTypeDef",
    {
        "ClientToken": str,
        "GrantArn": str,
        "GrantName": NotRequired[str],
        "AllowedOperations": NotRequired[Sequence[AllowedOperationType]],
        "Status": NotRequired[GrantStatusType],
        "StatusReason": NotRequired[str],
        "SourceVersion": NotRequired[str],
        "Options": NotRequired[OptionsTypeDef],
    },
)
GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "GrantArn": str,
        "GrantName": str,
        "ParentArn": str,
        "LicenseArn": str,
        "GranteePrincipalArn": str,
        "HomeRegion": str,
        "GrantStatus": GrantStatusType,
        "Version": str,
        "GrantedOperations": List[AllowedOperationType],
        "StatusReason": NotRequired[str],
        "Options": NotRequired[OptionsTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
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
CreateLicenseConversionTaskForResourceRequestRequestTypeDef = TypedDict(
    "CreateLicenseConversionTaskForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "SourceLicenseContext": LicenseConversionContextTypeDef,
        "DestinationLicenseContext": LicenseConversionContextTypeDef,
    },
)
GetLicenseConversionTaskResponseTypeDef = TypedDict(
    "GetLicenseConversionTaskResponseTypeDef",
    {
        "LicenseConversionTaskId": str,
        "ResourceArn": str,
        "SourceLicenseContext": LicenseConversionContextTypeDef,
        "DestinationLicenseContext": LicenseConversionContextTypeDef,
        "StatusMessage": str,
        "Status": LicenseConversionTaskStatusType,
        "StartTime": datetime,
        "LicenseConversionTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LicenseConversionTaskTypeDef = TypedDict(
    "LicenseConversionTaskTypeDef",
    {
        "LicenseConversionTaskId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "SourceLicenseContext": NotRequired[LicenseConversionContextTypeDef],
        "DestinationLicenseContext": NotRequired[LicenseConversionContextTypeDef],
        "Status": NotRequired[LicenseConversionTaskStatusType],
        "StatusMessage": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "LicenseConversionTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
CreateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "ReportGeneratorName": str,
        "Type": Sequence[ReportTypeType],
        "ReportContext": ReportContextTypeDef,
        "ReportFrequency": ReportFrequencyTypeDef,
        "ClientToken": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "UpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ReportGeneratorName": str,
        "Type": Sequence[ReportTypeType],
        "ReportContext": ReportContextTypeDef,
        "ReportFrequency": ReportFrequencyTypeDef,
        "ClientToken": str,
        "Description": NotRequired[str],
    },
)
LicenseUsageTypeDef = TypedDict(
    "LicenseUsageTypeDef",
    {
        "EntitlementUsages": NotRequired[List[EntitlementUsageTypeDef]],
    },
)
ListDistributedGrantsRequestRequestTypeDef = TypedDict(
    "ListDistributedGrantsRequestRequestTypeDef",
    {
        "GrantArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListLicenseConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLicenseConfigurationsRequestRequestTypeDef",
    {
        "LicenseConfigurationArns": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListLicenseConversionTasksRequestRequestTypeDef = TypedDict(
    "ListLicenseConversionTasksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListLicenseManagerReportGeneratorsRequestRequestTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListLicensesRequestRequestTypeDef = TypedDict(
    "ListLicensesRequestRequestTypeDef",
    {
        "LicenseArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReceivedGrantsForOrganizationRequestRequestTypeDef = TypedDict(
    "ListReceivedGrantsForOrganizationRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReceivedGrantsRequestRequestTypeDef = TypedDict(
    "ListReceivedGrantsRequestRequestTypeDef",
    {
        "GrantArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReceivedLicensesForOrganizationRequestRequestTypeDef = TypedDict(
    "ListReceivedLicensesForOrganizationRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReceivedLicensesRequestRequestTypeDef = TypedDict(
    "ListReceivedLicensesRequestRequestTypeDef",
    {
        "LicenseArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTokensRequestRequestTypeDef = TypedDict(
    "ListTokensRequestRequestTypeDef",
    {
        "TokenIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListUsageForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": OrganizationConfigurationTypeDef,
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "UpdateServiceSettingsRequestRequestTypeDef",
    {
        "S3BucketArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "OrganizationConfiguration": NotRequired[OrganizationConfigurationTypeDef],
        "EnableCrossAccountsDiscovery": NotRequired[bool],
    },
)
ListResourceInventoryRequestRequestTypeDef = TypedDict(
    "ListResourceInventoryRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[InventoryFilterTypeDef]],
    },
)
ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[LicenseConfigurationAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[LicenseConfigurationUsageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List[LicenseSpecificationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "UpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "AddLicenseSpecifications": NotRequired[Sequence[LicenseSpecificationTypeDef]],
        "RemoveLicenseSpecifications": NotRequired[Sequence[LicenseSpecificationTypeDef]],
    },
)
ListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef",
    {
        "LicenseConfigurationArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateTypeDef = TypedDict(
    "ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateTypeDef",
    {
        "LicenseConfigurationArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceInventoryRequestListResourceInventoryPaginateTypeDef = TypedDict(
    "ListResourceInventoryRequestListResourceInventoryPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[InventoryFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef",
    {
        "LicenseConfigurationArn": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List[ResourceInventoryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTokensResponseTypeDef = TypedDict(
    "ListTokensResponseTypeDef",
    {
        "Tokens": List[TokenDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ProductInformationOutputTypeDef = TypedDict(
    "ProductInformationOutputTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[ProductInformationFilterOutputTypeDef],
    },
)
ProductInformationFilterUnionTypeDef = Union[
    ProductInformationFilterTypeDef, ProductInformationFilterOutputTypeDef
]
ReportGeneratorTypeDef = TypedDict(
    "ReportGeneratorTypeDef",
    {
        "ReportGeneratorName": NotRequired[str],
        "ReportType": NotRequired[List[ReportTypeType]],
        "ReportContext": NotRequired[ReportContextOutputTypeDef],
        "ReportFrequency": NotRequired[ReportFrequencyTypeDef],
        "LicenseManagerReportGeneratorArn": NotRequired[str],
        "LastRunStatus": NotRequired[str],
        "LastRunFailureReason": NotRequired[str],
        "LastReportGenerationTime": NotRequired[str],
        "ReportCreatorAccount": NotRequired[str],
        "Description": NotRequired[str],
        "S3Location": NotRequired[S3LocationTypeDef],
        "CreateTime": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {
        "LicenseOperationFailureList": List[LicenseOperationFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateLicenseRequestRequestTypeDef = TypedDict(
    "CreateLicenseRequestRequestTypeDef",
    {
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": IssuerTypeDef,
        "HomeRegion": str,
        "Validity": DatetimeRangeTypeDef,
        "Entitlements": Sequence[EntitlementTypeDef],
        "Beneficiary": str,
        "ConsumptionConfiguration": ConsumptionConfigurationTypeDef,
        "ClientToken": str,
        "LicenseMetadata": NotRequired[Sequence[MetadataTypeDef]],
    },
)
CreateLicenseVersionRequestRequestTypeDef = TypedDict(
    "CreateLicenseVersionRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "Issuer": IssuerTypeDef,
        "HomeRegion": str,
        "Validity": DatetimeRangeTypeDef,
        "Entitlements": Sequence[EntitlementTypeDef],
        "ConsumptionConfiguration": ConsumptionConfigurationTypeDef,
        "Status": LicenseStatusType,
        "ClientToken": str,
        "LicenseMetadata": NotRequired[Sequence[MetadataTypeDef]],
        "SourceVersion": NotRequired[str],
    },
)
GrantedLicenseTypeDef = TypedDict(
    "GrantedLicenseTypeDef",
    {
        "LicenseArn": NotRequired[str],
        "LicenseName": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProductSKU": NotRequired[str],
        "Issuer": NotRequired[IssuerDetailsTypeDef],
        "HomeRegion": NotRequired[str],
        "Status": NotRequired[LicenseStatusType],
        "Validity": NotRequired[DatetimeRangeTypeDef],
        "Beneficiary": NotRequired[str],
        "Entitlements": NotRequired[List[EntitlementTypeDef]],
        "ConsumptionConfiguration": NotRequired[ConsumptionConfigurationTypeDef],
        "LicenseMetadata": NotRequired[List[MetadataTypeDef]],
        "CreateTime": NotRequired[str],
        "Version": NotRequired[str],
        "ReceivedMetadata": NotRequired[ReceivedMetadataTypeDef],
    },
)
LicenseTypeDef = TypedDict(
    "LicenseTypeDef",
    {
        "LicenseArn": NotRequired[str],
        "LicenseName": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProductSKU": NotRequired[str],
        "Issuer": NotRequired[IssuerDetailsTypeDef],
        "HomeRegion": NotRequired[str],
        "Status": NotRequired[LicenseStatusType],
        "Validity": NotRequired[DatetimeRangeTypeDef],
        "Beneficiary": NotRequired[str],
        "Entitlements": NotRequired[List[EntitlementTypeDef]],
        "ConsumptionConfiguration": NotRequired[ConsumptionConfigurationTypeDef],
        "LicenseMetadata": NotRequired[List[MetadataTypeDef]],
        "CreateTime": NotRequired[str],
        "Version": NotRequired[str],
    },
)
GetGrantResponseTypeDef = TypedDict(
    "GetGrantResponseTypeDef",
    {
        "Grant": GrantTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDistributedGrantsResponseTypeDef = TypedDict(
    "ListDistributedGrantsResponseTypeDef",
    {
        "Grants": List[GrantTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListReceivedGrantsForOrganizationResponseTypeDef = TypedDict(
    "ListReceivedGrantsForOrganizationResponseTypeDef",
    {
        "Grants": List[GrantTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListReceivedGrantsResponseTypeDef = TypedDict(
    "ListReceivedGrantsResponseTypeDef",
    {
        "Grants": List[GrantTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLicenseConversionTasksResponseTypeDef = TypedDict(
    "ListLicenseConversionTasksResponseTypeDef",
    {
        "LicenseConversionTasks": List[LicenseConversionTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetLicenseUsageResponseTypeDef = TypedDict(
    "GetLicenseUsageResponseTypeDef",
    {
        "LicenseUsage": LicenseUsageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLicenseConfigurationResponseTypeDef = TypedDict(
    "GetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingTypeType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[ConsumedLicenseSummaryTypeDef],
        "ManagedResourceSummaryList": List[ManagedResourceSummaryTypeDef],
        "Tags": List[TagTypeDef],
        "ProductInformationList": List[ProductInformationOutputTypeDef],
        "AutomatedDiscoveryInformation": AutomatedDiscoveryInformationTypeDef,
        "DisassociateWhenNotFound": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationId": NotRequired[str],
        "LicenseConfigurationArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LicenseCountingType": NotRequired[LicenseCountingTypeType],
        "LicenseRules": NotRequired[List[str]],
        "LicenseCount": NotRequired[int],
        "LicenseCountHardLimit": NotRequired[bool],
        "DisassociateWhenNotFound": NotRequired[bool],
        "ConsumedLicenses": NotRequired[int],
        "Status": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "ConsumedLicenseSummaryList": NotRequired[List[ConsumedLicenseSummaryTypeDef]],
        "ManagedResourceSummaryList": NotRequired[List[ManagedResourceSummaryTypeDef]],
        "ProductInformationList": NotRequired[List[ProductInformationOutputTypeDef]],
        "AutomatedDiscoveryInformation": NotRequired[AutomatedDiscoveryInformationTypeDef],
    },
)
ProductInformationTypeDef = TypedDict(
    "ProductInformationTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": Sequence[ProductInformationFilterUnionTypeDef],
    },
)
GetLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    {
        "ReportGenerator": ReportGeneratorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLicenseManagerReportGeneratorsResponseTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    {
        "ReportGenerators": List[ReportGeneratorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListReceivedLicensesForOrganizationResponseTypeDef = TypedDict(
    "ListReceivedLicensesForOrganizationResponseTypeDef",
    {
        "Licenses": List[GrantedLicenseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListReceivedLicensesResponseTypeDef = TypedDict(
    "ListReceivedLicensesResponseTypeDef",
    {
        "Licenses": List[GrantedLicenseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetLicenseResponseTypeDef = TypedDict(
    "GetLicenseResponseTypeDef",
    {
        "License": LicenseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLicenseVersionsResponseTypeDef = TypedDict(
    "ListLicenseVersionsResponseTypeDef",
    {
        "Licenses": List[LicenseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLicensesResponseTypeDef = TypedDict(
    "ListLicensesResponseTypeDef",
    {
        "Licenses": List[LicenseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List[LicenseConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ProductInformationUnionTypeDef = Union[ProductInformationTypeDef, ProductInformationOutputTypeDef]
UpdateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
        "LicenseConfigurationStatus": NotRequired[LicenseConfigurationStatusType],
        "LicenseRules": NotRequired[Sequence[str]],
        "LicenseCount": NotRequired[int],
        "LicenseCountHardLimit": NotRequired[bool],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ProductInformationList": NotRequired[Sequence[ProductInformationTypeDef]],
        "DisassociateWhenNotFound": NotRequired[bool],
    },
)
CreateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "CreateLicenseConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "LicenseCountingType": LicenseCountingTypeType,
        "Description": NotRequired[str],
        "LicenseCount": NotRequired[int],
        "LicenseCountHardLimit": NotRequired[bool],
        "LicenseRules": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DisassociateWhenNotFound": NotRequired[bool],
        "ProductInformationList": NotRequired[Sequence[ProductInformationUnionTypeDef]],
    },
)
