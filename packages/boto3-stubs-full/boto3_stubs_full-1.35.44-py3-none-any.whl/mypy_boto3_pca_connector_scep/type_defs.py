"""
Type annotations for pca-connector-scep service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/type_defs/)

Usage::

    ```python
    from mypy_boto3_pca_connector_scep.type_defs import ChallengeMetadataSummaryTypeDef

    data: ChallengeMetadataSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import ConnectorStatusReasonType, ConnectorStatusType, ConnectorTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ChallengeMetadataSummaryTypeDef",
    "ChallengeMetadataTypeDef",
    "ChallengeTypeDef",
    "OpenIdConfigurationTypeDef",
    "CreateChallengeRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteChallengeRequestRequestTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "GetChallengeMetadataRequestRequestTypeDef",
    "GetChallengePasswordRequestRequestTypeDef",
    "GetConnectorRequestRequestTypeDef",
    "IntuneConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ListChallengeMetadataRequestRequestTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateChallengeResponseTypeDef",
    "CreateConnectorResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetChallengeMetadataResponseTypeDef",
    "GetChallengePasswordResponseTypeDef",
    "ListChallengeMetadataResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MobileDeviceManagementTypeDef",
    "ListChallengeMetadataRequestListChallengeMetadataPaginateTypeDef",
    "ListConnectorsRequestListConnectorsPaginateTypeDef",
    "ConnectorSummaryTypeDef",
    "ConnectorTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "GetConnectorResponseTypeDef",
)

ChallengeMetadataSummaryTypeDef = TypedDict(
    "ChallengeMetadataSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "ConnectorArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
ChallengeMetadataTypeDef = TypedDict(
    "ChallengeMetadataTypeDef",
    {
        "Arn": NotRequired[str],
        "ConnectorArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
ChallengeTypeDef = TypedDict(
    "ChallengeTypeDef",
    {
        "Arn": NotRequired[str],
        "ConnectorArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "Password": NotRequired[str],
    },
)
OpenIdConfigurationTypeDef = TypedDict(
    "OpenIdConfigurationTypeDef",
    {
        "Issuer": NotRequired[str],
        "Subject": NotRequired[str],
        "Audience": NotRequired[str],
    },
)
CreateChallengeRequestRequestTypeDef = TypedDict(
    "CreateChallengeRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
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
DeleteChallengeRequestRequestTypeDef = TypedDict(
    "DeleteChallengeRequestRequestTypeDef",
    {
        "ChallengeArn": str,
    },
)
DeleteConnectorRequestRequestTypeDef = TypedDict(
    "DeleteConnectorRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)
GetChallengeMetadataRequestRequestTypeDef = TypedDict(
    "GetChallengeMetadataRequestRequestTypeDef",
    {
        "ChallengeArn": str,
    },
)
GetChallengePasswordRequestRequestTypeDef = TypedDict(
    "GetChallengePasswordRequestRequestTypeDef",
    {
        "ChallengeArn": str,
    },
)
GetConnectorRequestRequestTypeDef = TypedDict(
    "GetConnectorRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)
IntuneConfigurationTypeDef = TypedDict(
    "IntuneConfigurationTypeDef",
    {
        "AzureApplicationId": str,
        "Domain": str,
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
ListChallengeMetadataRequestRequestTypeDef = TypedDict(
    "ListChallengeMetadataRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
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
CreateChallengeResponseTypeDef = TypedDict(
    "CreateChallengeResponseTypeDef",
    {
        "Challenge": ChallengeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectorResponseTypeDef = TypedDict(
    "CreateConnectorResponseTypeDef",
    {
        "ConnectorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChallengeMetadataResponseTypeDef = TypedDict(
    "GetChallengeMetadataResponseTypeDef",
    {
        "ChallengeMetadata": ChallengeMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChallengePasswordResponseTypeDef = TypedDict(
    "GetChallengePasswordResponseTypeDef",
    {
        "Password": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChallengeMetadataResponseTypeDef = TypedDict(
    "ListChallengeMetadataResponseTypeDef",
    {
        "Challenges": List[ChallengeMetadataSummaryTypeDef],
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
MobileDeviceManagementTypeDef = TypedDict(
    "MobileDeviceManagementTypeDef",
    {
        "Intune": NotRequired[IntuneConfigurationTypeDef],
    },
)
ListChallengeMetadataRequestListChallengeMetadataPaginateTypeDef = TypedDict(
    "ListChallengeMetadataRequestListChallengeMetadataPaginateTypeDef",
    {
        "ConnectorArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConnectorsRequestListConnectorsPaginateTypeDef = TypedDict(
    "ListConnectorsRequestListConnectorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ConnectorSummaryTypeDef = TypedDict(
    "ConnectorSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "Type": NotRequired[ConnectorTypeType],
        "MobileDeviceManagement": NotRequired[MobileDeviceManagementTypeDef],
        "OpenIdConfiguration": NotRequired[OpenIdConfigurationTypeDef],
        "Status": NotRequired[ConnectorStatusType],
        "StatusReason": NotRequired[ConnectorStatusReasonType],
        "Endpoint": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "Type": NotRequired[ConnectorTypeType],
        "MobileDeviceManagement": NotRequired[MobileDeviceManagementTypeDef],
        "OpenIdConfiguration": NotRequired[OpenIdConfigurationTypeDef],
        "Status": NotRequired[ConnectorStatusType],
        "StatusReason": NotRequired[ConnectorStatusReasonType],
        "Endpoint": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
CreateConnectorRequestRequestTypeDef = TypedDict(
    "CreateConnectorRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "MobileDeviceManagement": NotRequired[MobileDeviceManagementTypeDef],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "Connectors": List[ConnectorSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetConnectorResponseTypeDef = TypedDict(
    "GetConnectorResponseTypeDef",
    {
        "Connector": ConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
