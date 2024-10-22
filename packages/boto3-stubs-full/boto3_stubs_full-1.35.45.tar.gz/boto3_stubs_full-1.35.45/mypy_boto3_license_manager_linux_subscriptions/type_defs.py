"""
Type annotations for license-manager-linux-subscriptions service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/type_defs/)

Usage::

    ```python
    from mypy_boto3_license_manager_linux_subscriptions.type_defs import DeregisterSubscriptionProviderRequestRequestTypeDef

    data: DeregisterSubscriptionProviderRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    LinuxSubscriptionsDiscoveryType,
    OperatorType,
    OrganizationIntegrationType,
    StatusType,
    SubscriptionProviderStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "DeregisterSubscriptionProviderRequestRequestTypeDef",
    "FilterTypeDef",
    "GetRegisteredSubscriptionProviderRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "LinuxSubscriptionsDiscoverySettingsOutputTypeDef",
    "InstanceTypeDef",
    "LinuxSubscriptionsDiscoverySettingsTypeDef",
    "PaginatorConfigTypeDef",
    "SubscriptionTypeDef",
    "ListRegisteredSubscriptionProvidersRequestRequestTypeDef",
    "RegisteredSubscriptionProviderTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RegisterSubscriptionProviderRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ListLinuxSubscriptionInstancesRequestRequestTypeDef",
    "ListLinuxSubscriptionsRequestRequestTypeDef",
    "GetRegisteredSubscriptionProviderResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RegisterSubscriptionProviderResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "UpdateServiceSettingsResponseTypeDef",
    "ListLinuxSubscriptionInstancesResponseTypeDef",
    "UpdateServiceSettingsRequestRequestTypeDef",
    "ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef",
    "ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef",
    "ListRegisteredSubscriptionProvidersRequestListRegisteredSubscriptionProvidersPaginateTypeDef",
    "ListLinuxSubscriptionsResponseTypeDef",
    "ListRegisteredSubscriptionProvidersResponseTypeDef",
)

DeregisterSubscriptionProviderRequestRequestTypeDef = TypedDict(
    "DeregisterSubscriptionProviderRequestRequestTypeDef",
    {
        "SubscriptionProviderArn": str,
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Operator": NotRequired[OperatorType],
        "Values": NotRequired[Sequence[str]],
    },
)
GetRegisteredSubscriptionProviderRequestRequestTypeDef = TypedDict(
    "GetRegisteredSubscriptionProviderRequestRequestTypeDef",
    {
        "SubscriptionProviderArn": str,
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
LinuxSubscriptionsDiscoverySettingsOutputTypeDef = TypedDict(
    "LinuxSubscriptionsDiscoverySettingsOutputTypeDef",
    {
        "OrganizationIntegration": OrganizationIntegrationType,
        "SourceRegions": List[str],
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AccountID": NotRequired[str],
        "AmiId": NotRequired[str],
        "DualSubscription": NotRequired[str],
        "InstanceID": NotRequired[str],
        "InstanceType": NotRequired[str],
        "LastUpdatedTime": NotRequired[str],
        "OsVersion": NotRequired[str],
        "ProductCode": NotRequired[List[str]],
        "Region": NotRequired[str],
        "RegisteredWithSubscriptionProvider": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionName": NotRequired[str],
        "SubscriptionProviderCreateTime": NotRequired[str],
        "SubscriptionProviderUpdateTime": NotRequired[str],
        "UsageOperation": NotRequired[str],
    },
)
LinuxSubscriptionsDiscoverySettingsTypeDef = TypedDict(
    "LinuxSubscriptionsDiscoverySettingsTypeDef",
    {
        "OrganizationIntegration": OrganizationIntegrationType,
        "SourceRegions": Sequence[str],
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
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
ListRegisteredSubscriptionProvidersRequestRequestTypeDef = TypedDict(
    "ListRegisteredSubscriptionProvidersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SubscriptionProviderSources": NotRequired[Sequence[Literal["RedHat"]]],
    },
)
RegisteredSubscriptionProviderTypeDef = TypedDict(
    "RegisteredSubscriptionProviderTypeDef",
    {
        "LastSuccessfulDataRetrievalTime": NotRequired[str],
        "SecretArn": NotRequired[str],
        "SubscriptionProviderArn": NotRequired[str],
        "SubscriptionProviderSource": NotRequired[Literal["RedHat"]],
        "SubscriptionProviderStatus": NotRequired[SubscriptionProviderStatusType],
        "SubscriptionProviderStatusMessage": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RegisterSubscriptionProviderRequestRequestTypeDef = TypedDict(
    "RegisterSubscriptionProviderRequestRequestTypeDef",
    {
        "SecretArn": str,
        "SubscriptionProviderSource": Literal["RedHat"],
        "Tags": NotRequired[Mapping[str, str]],
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
ListLinuxSubscriptionInstancesRequestRequestTypeDef = TypedDict(
    "ListLinuxSubscriptionInstancesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLinuxSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListLinuxSubscriptionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetRegisteredSubscriptionProviderResponseTypeDef = TypedDict(
    "GetRegisteredSubscriptionProviderResponseTypeDef",
    {
        "LastSuccessfulDataRetrievalTime": str,
        "SecretArn": str,
        "SubscriptionProviderArn": str,
        "SubscriptionProviderSource": Literal["RedHat"],
        "SubscriptionProviderStatus": SubscriptionProviderStatusType,
        "SubscriptionProviderStatusMessage": str,
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
RegisterSubscriptionProviderResponseTypeDef = TypedDict(
    "RegisterSubscriptionProviderResponseTypeDef",
    {
        "SubscriptionProviderArn": str,
        "SubscriptionProviderSource": Literal["RedHat"],
        "SubscriptionProviderStatus": SubscriptionProviderStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "HomeRegions": List[str],
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": LinuxSubscriptionsDiscoverySettingsOutputTypeDef,
        "Status": StatusType,
        "StatusMessage": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceSettingsResponseTypeDef = TypedDict(
    "UpdateServiceSettingsResponseTypeDef",
    {
        "HomeRegions": List[str],
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": LinuxSubscriptionsDiscoverySettingsOutputTypeDef,
        "Status": StatusType,
        "StatusMessage": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLinuxSubscriptionInstancesResponseTypeDef = TypedDict(
    "ListLinuxSubscriptionInstancesResponseTypeDef",
    {
        "Instances": List[InstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "UpdateServiceSettingsRequestRequestTypeDef",
    {
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": LinuxSubscriptionsDiscoverySettingsTypeDef,
        "AllowUpdate": NotRequired[bool],
    },
)
ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef = TypedDict(
    "ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef = TypedDict(
    "ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegisteredSubscriptionProvidersRequestListRegisteredSubscriptionProvidersPaginateTypeDef = TypedDict(
    "ListRegisteredSubscriptionProvidersRequestListRegisteredSubscriptionProvidersPaginateTypeDef",
    {
        "SubscriptionProviderSources": NotRequired[Sequence[Literal["RedHat"]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLinuxSubscriptionsResponseTypeDef = TypedDict(
    "ListLinuxSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List[SubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRegisteredSubscriptionProvidersResponseTypeDef = TypedDict(
    "ListRegisteredSubscriptionProvidersResponseTypeDef",
    {
        "RegisteredSubscriptionProviders": List[RegisteredSubscriptionProviderTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
