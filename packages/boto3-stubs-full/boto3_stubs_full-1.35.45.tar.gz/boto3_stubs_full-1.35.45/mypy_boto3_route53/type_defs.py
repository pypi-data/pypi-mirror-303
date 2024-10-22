"""
Type annotations for route53 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/type_defs/)

Usage::

    ```python
    from mypy_boto3_route53.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AccountLimitTypeType,
    ChangeActionType,
    ChangeStatusType,
    CidrCollectionChangeActionType,
    CloudWatchRegionType,
    ComparisonOperatorType,
    HealthCheckRegionType,
    HealthCheckTypeType,
    HostedZoneLimitTypeType,
    InsufficientDataHealthStatusType,
    ResettableElementNameType,
    ResourceRecordSetFailoverType,
    ResourceRecordSetRegionType,
    RRTypeType,
    StatisticType,
    TagResourceTypeType,
    VPCRegionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AccountLimitTypeDef",
    "ActivateKeySigningKeyRequestRequestTypeDef",
    "ChangeInfoTypeDef",
    "ResponseMetadataTypeDef",
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "VPCTypeDef",
    "CidrCollectionChangeTypeDef",
    "TagTypeDef",
    "CidrBlockSummaryTypeDef",
    "CidrCollectionTypeDef",
    "CidrRoutingConfigTypeDef",
    "DimensionTypeDef",
    "CollectionSummaryTypeDef",
    "CoordinatesTypeDef",
    "CreateCidrCollectionRequestRequestTypeDef",
    "HostedZoneConfigTypeDef",
    "DelegationSetTypeDef",
    "CreateKeySigningKeyRequestRequestTypeDef",
    "KeySigningKeyTypeDef",
    "CreateQueryLoggingConfigRequestRequestTypeDef",
    "QueryLoggingConfigTypeDef",
    "CreateReusableDelegationSetRequestRequestTypeDef",
    "CreateTrafficPolicyInstanceRequestRequestTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "CreateTrafficPolicyRequestRequestTypeDef",
    "TrafficPolicyTypeDef",
    "CreateTrafficPolicyVersionRequestRequestTypeDef",
    "DNSSECStatusTypeDef",
    "DeactivateKeySigningKeyRequestRequestTypeDef",
    "DeleteCidrCollectionRequestRequestTypeDef",
    "DeleteHealthCheckRequestRequestTypeDef",
    "DeleteHostedZoneRequestRequestTypeDef",
    "DeleteKeySigningKeyRequestRequestTypeDef",
    "DeleteQueryLoggingConfigRequestRequestTypeDef",
    "DeleteReusableDelegationSetRequestRequestTypeDef",
    "DeleteTrafficPolicyInstanceRequestRequestTypeDef",
    "DeleteTrafficPolicyRequestRequestTypeDef",
    "DisableHostedZoneDNSSECRequestRequestTypeDef",
    "EnableHostedZoneDNSSECRequestRequestTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
    "GetAccountLimitRequestRequestTypeDef",
    "GetChangeRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetDNSSECRequestRequestTypeDef",
    "GetGeoLocationRequestRequestTypeDef",
    "GetHealthCheckLastFailureReasonRequestRequestTypeDef",
    "GetHealthCheckRequestRequestTypeDef",
    "GetHealthCheckStatusRequestRequestTypeDef",
    "GetHostedZoneLimitRequestRequestTypeDef",
    "HostedZoneLimitTypeDef",
    "GetHostedZoneRequestRequestTypeDef",
    "GetQueryLoggingConfigRequestRequestTypeDef",
    "GetReusableDelegationSetLimitRequestRequestTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "GetReusableDelegationSetRequestRequestTypeDef",
    "GetTrafficPolicyInstanceRequestRequestTypeDef",
    "GetTrafficPolicyRequestRequestTypeDef",
    "StatusReportTypeDef",
    "LinkedServiceTypeDef",
    "HostedZoneOwnerTypeDef",
    "PaginatorConfigTypeDef",
    "ListCidrBlocksRequestRequestTypeDef",
    "ListCidrCollectionsRequestRequestTypeDef",
    "ListCidrLocationsRequestRequestTypeDef",
    "LocationSummaryTypeDef",
    "ListGeoLocationsRequestRequestTypeDef",
    "ListHealthChecksRequestRequestTypeDef",
    "ListHostedZonesByNameRequestRequestTypeDef",
    "ListHostedZonesByVPCRequestRequestTypeDef",
    "ListHostedZonesRequestRequestTypeDef",
    "ListQueryLoggingConfigsRequestRequestTypeDef",
    "ListResourceRecordSetsRequestRequestTypeDef",
    "ListReusableDelegationSetsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourcesRequestRequestTypeDef",
    "ListTrafficPoliciesRequestRequestTypeDef",
    "TrafficPolicySummaryTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef",
    "ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef",
    "ListTrafficPolicyInstancesRequestRequestTypeDef",
    "ListTrafficPolicyVersionsRequestRequestTypeDef",
    "ListVPCAssociationAuthorizationsRequestRequestTypeDef",
    "ResourceRecordTypeDef",
    "TestDNSAnswerRequestRequestTypeDef",
    "UpdateHostedZoneCommentRequestRequestTypeDef",
    "UpdateTrafficPolicyCommentRequestRequestTypeDef",
    "UpdateTrafficPolicyInstanceRequestRequestTypeDef",
    "ActivateKeySigningKeyResponseTypeDef",
    "AssociateVPCWithHostedZoneResponseTypeDef",
    "ChangeCidrCollectionResponseTypeDef",
    "ChangeResourceRecordSetsResponseTypeDef",
    "DeactivateKeySigningKeyResponseTypeDef",
    "DeleteHostedZoneResponseTypeDef",
    "DeleteKeySigningKeyResponseTypeDef",
    "DisableHostedZoneDNSSECResponseTypeDef",
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    "EnableHostedZoneDNSSECResponseTypeDef",
    "GetAccountLimitResponseTypeDef",
    "GetChangeResponseTypeDef",
    "GetCheckerIpRangesResponseTypeDef",
    "GetHealthCheckCountResponseTypeDef",
    "GetHostedZoneCountResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    "TestDNSAnswerResponseTypeDef",
    "HealthCheckConfigOutputTypeDef",
    "HealthCheckConfigTypeDef",
    "UpdateHealthCheckRequestRequestTypeDef",
    "AssociateVPCWithHostedZoneRequestRequestTypeDef",
    "CreateVPCAssociationAuthorizationRequestRequestTypeDef",
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    "DeleteVPCAssociationAuthorizationRequestRequestTypeDef",
    "DisassociateVPCFromHostedZoneRequestRequestTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "ChangeCidrCollectionRequestRequestTypeDef",
    "ChangeTagsForResourceRequestRequestTypeDef",
    "ResourceTagSetTypeDef",
    "ListCidrBlocksResponseTypeDef",
    "CreateCidrCollectionResponseTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "ListCidrCollectionsResponseTypeDef",
    "GeoProximityLocationTypeDef",
    "CreateHostedZoneRequestRequestTypeDef",
    "CreateReusableDelegationSetResponseTypeDef",
    "GetReusableDelegationSetResponseTypeDef",
    "ListReusableDelegationSetsResponseTypeDef",
    "CreateKeySigningKeyResponseTypeDef",
    "CreateQueryLoggingConfigResponseTypeDef",
    "GetQueryLoggingConfigResponseTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "CreateTrafficPolicyInstanceResponseTypeDef",
    "GetTrafficPolicyInstanceResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ListTrafficPolicyInstancesResponseTypeDef",
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "CreateTrafficPolicyVersionResponseTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "ListTrafficPolicyVersionsResponseTypeDef",
    "UpdateTrafficPolicyCommentResponseTypeDef",
    "GetDNSSECResponseTypeDef",
    "GetGeoLocationResponseTypeDef",
    "ListGeoLocationsResponseTypeDef",
    "GetChangeRequestResourceRecordSetsChangedWaitTypeDef",
    "GetHostedZoneLimitResponseTypeDef",
    "GetReusableDelegationSetLimitResponseTypeDef",
    "HealthCheckObservationTypeDef",
    "HostedZoneTypeDef",
    "HostedZoneSummaryTypeDef",
    "ListCidrBlocksRequestListCidrBlocksPaginateTypeDef",
    "ListCidrCollectionsRequestListCidrCollectionsPaginateTypeDef",
    "ListCidrLocationsRequestListCidrLocationsPaginateTypeDef",
    "ListHealthChecksRequestListHealthChecksPaginateTypeDef",
    "ListHostedZonesRequestListHostedZonesPaginateTypeDef",
    "ListQueryLoggingConfigsRequestListQueryLoggingConfigsPaginateTypeDef",
    "ListResourceRecordSetsRequestListResourceRecordSetsPaginateTypeDef",
    "ListVPCAssociationAuthorizationsRequestListVPCAssociationAuthorizationsPaginateTypeDef",
    "ListCidrLocationsResponseTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "CreateHealthCheckRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "HealthCheckTypeDef",
    "ResourceRecordSetOutputTypeDef",
    "ResourceRecordSetTypeDef",
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    "GetHealthCheckStatusResponseTypeDef",
    "CreateHostedZoneResponseTypeDef",
    "GetHostedZoneResponseTypeDef",
    "ListHostedZonesByNameResponseTypeDef",
    "ListHostedZonesResponseTypeDef",
    "UpdateHostedZoneCommentResponseTypeDef",
    "ListHostedZonesByVPCResponseTypeDef",
    "CreateHealthCheckResponseTypeDef",
    "GetHealthCheckResponseTypeDef",
    "ListHealthChecksResponseTypeDef",
    "UpdateHealthCheckResponseTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "ResourceRecordSetUnionTypeDef",
    "ChangeTypeDef",
    "ChangeBatchTypeDef",
    "ChangeResourceRecordSetsRequestRequestTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Type": AccountLimitTypeType,
        "Value": int,
    },
)
ActivateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "ActivateKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)
ChangeInfoTypeDef = TypedDict(
    "ChangeInfoTypeDef",
    {
        "Id": str,
        "Status": ChangeStatusType,
        "SubmittedAt": datetime,
        "Comment": NotRequired[str],
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
AlarmIdentifierTypeDef = TypedDict(
    "AlarmIdentifierTypeDef",
    {
        "Region": CloudWatchRegionType,
        "Name": str,
    },
)
AliasTargetTypeDef = TypedDict(
    "AliasTargetTypeDef",
    {
        "HostedZoneId": str,
        "DNSName": str,
        "EvaluateTargetHealth": bool,
    },
)
VPCTypeDef = TypedDict(
    "VPCTypeDef",
    {
        "VPCRegion": NotRequired[VPCRegionType],
        "VPCId": NotRequired[str],
    },
)
CidrCollectionChangeTypeDef = TypedDict(
    "CidrCollectionChangeTypeDef",
    {
        "LocationName": str,
        "Action": CidrCollectionChangeActionType,
        "CidrList": Sequence[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
CidrBlockSummaryTypeDef = TypedDict(
    "CidrBlockSummaryTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "LocationName": NotRequired[str],
    },
)
CidrCollectionTypeDef = TypedDict(
    "CidrCollectionTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[int],
    },
)
CidrRoutingConfigTypeDef = TypedDict(
    "CidrRoutingConfigTypeDef",
    {
        "CollectionId": str,
        "LocationName": str,
    },
)
DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
CollectionSummaryTypeDef = TypedDict(
    "CollectionSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[int],
    },
)
CoordinatesTypeDef = TypedDict(
    "CoordinatesTypeDef",
    {
        "Latitude": str,
        "Longitude": str,
    },
)
CreateCidrCollectionRequestRequestTypeDef = TypedDict(
    "CreateCidrCollectionRequestRequestTypeDef",
    {
        "Name": str,
        "CallerReference": str,
    },
)
HostedZoneConfigTypeDef = TypedDict(
    "HostedZoneConfigTypeDef",
    {
        "Comment": NotRequired[str],
        "PrivateZone": NotRequired[bool],
    },
)
DelegationSetTypeDef = TypedDict(
    "DelegationSetTypeDef",
    {
        "NameServers": List[str],
        "Id": NotRequired[str],
        "CallerReference": NotRequired[str],
    },
)
CreateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "CreateKeySigningKeyRequestRequestTypeDef",
    {
        "CallerReference": str,
        "HostedZoneId": str,
        "KeyManagementServiceArn": str,
        "Name": str,
        "Status": str,
    },
)
KeySigningKeyTypeDef = TypedDict(
    "KeySigningKeyTypeDef",
    {
        "Name": NotRequired[str],
        "KmsArn": NotRequired[str],
        "Flag": NotRequired[int],
        "SigningAlgorithmMnemonic": NotRequired[str],
        "SigningAlgorithmType": NotRequired[int],
        "DigestAlgorithmMnemonic": NotRequired[str],
        "DigestAlgorithmType": NotRequired[int],
        "KeyTag": NotRequired[int],
        "DigestValue": NotRequired[str],
        "PublicKey": NotRequired[str],
        "DSRecord": NotRequired[str],
        "DNSKEYRecord": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "LastModifiedDate": NotRequired[datetime],
    },
)
CreateQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "CreateQueryLoggingConfigRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "CloudWatchLogsLogGroupArn": str,
    },
)
QueryLoggingConfigTypeDef = TypedDict(
    "QueryLoggingConfigTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "CloudWatchLogsLogGroupArn": str,
    },
)
CreateReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "CreateReusableDelegationSetRequestRequestTypeDef",
    {
        "CallerReference": str,
        "HostedZoneId": NotRequired[str],
    },
)
CreateTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)
TrafficPolicyInstanceTypeDef = TypedDict(
    "TrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": RRTypeType,
    },
)
CreateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "CreateTrafficPolicyRequestRequestTypeDef",
    {
        "Name": str,
        "Document": str,
        "Comment": NotRequired[str],
    },
)
TrafficPolicyTypeDef = TypedDict(
    "TrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": RRTypeType,
        "Document": str,
        "Comment": NotRequired[str],
    },
)
CreateTrafficPolicyVersionRequestRequestTypeDef = TypedDict(
    "CreateTrafficPolicyVersionRequestRequestTypeDef",
    {
        "Id": str,
        "Document": str,
        "Comment": NotRequired[str],
    },
)
DNSSECStatusTypeDef = TypedDict(
    "DNSSECStatusTypeDef",
    {
        "ServeSignature": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)
DeactivateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "DeactivateKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)
DeleteCidrCollectionRequestRequestTypeDef = TypedDict(
    "DeleteCidrCollectionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteHealthCheckRequestRequestTypeDef = TypedDict(
    "DeleteHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)
DeleteHostedZoneRequestRequestTypeDef = TypedDict(
    "DeleteHostedZoneRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteKeySigningKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)
DeleteQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "DeleteQueryLoggingConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "DeleteReusableDelegationSetRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteTrafficPolicyRequestRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
    },
)
DisableHostedZoneDNSSECRequestRequestTypeDef = TypedDict(
    "DisableHostedZoneDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
EnableHostedZoneDNSSECRequestRequestTypeDef = TypedDict(
    "EnableHostedZoneDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
GeoLocationDetailsTypeDef = TypedDict(
    "GeoLocationDetailsTypeDef",
    {
        "ContinentCode": NotRequired[str],
        "ContinentName": NotRequired[str],
        "CountryCode": NotRequired[str],
        "CountryName": NotRequired[str],
        "SubdivisionCode": NotRequired[str],
        "SubdivisionName": NotRequired[str],
    },
)
GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "ContinentCode": NotRequired[str],
        "CountryCode": NotRequired[str],
        "SubdivisionCode": NotRequired[str],
    },
)
GetAccountLimitRequestRequestTypeDef = TypedDict(
    "GetAccountLimitRequestRequestTypeDef",
    {
        "Type": AccountLimitTypeType,
    },
)
GetChangeRequestRequestTypeDef = TypedDict(
    "GetChangeRequestRequestTypeDef",
    {
        "Id": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetDNSSECRequestRequestTypeDef = TypedDict(
    "GetDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
GetGeoLocationRequestRequestTypeDef = TypedDict(
    "GetGeoLocationRequestRequestTypeDef",
    {
        "ContinentCode": NotRequired[str],
        "CountryCode": NotRequired[str],
        "SubdivisionCode": NotRequired[str],
    },
)
GetHealthCheckLastFailureReasonRequestRequestTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)
GetHealthCheckRequestRequestTypeDef = TypedDict(
    "GetHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)
GetHealthCheckStatusRequestRequestTypeDef = TypedDict(
    "GetHealthCheckStatusRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)
GetHostedZoneLimitRequestRequestTypeDef = TypedDict(
    "GetHostedZoneLimitRequestRequestTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "HostedZoneId": str,
    },
)
HostedZoneLimitTypeDef = TypedDict(
    "HostedZoneLimitTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "Value": int,
    },
)
GetHostedZoneRequestRequestTypeDef = TypedDict(
    "GetHostedZoneRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "GetQueryLoggingConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetReusableDelegationSetLimitRequestRequestTypeDef = TypedDict(
    "GetReusableDelegationSetLimitRequestRequestTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "DelegationSetId": str,
    },
)
ReusableDelegationSetLimitTypeDef = TypedDict(
    "ReusableDelegationSetLimitTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "Value": int,
    },
)
GetReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "GetReusableDelegationSetRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "GetTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetTrafficPolicyRequestRequestTypeDef = TypedDict(
    "GetTrafficPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
    },
)
StatusReportTypeDef = TypedDict(
    "StatusReportTypeDef",
    {
        "Status": NotRequired[str],
        "CheckedTime": NotRequired[datetime],
    },
)
LinkedServiceTypeDef = TypedDict(
    "LinkedServiceTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "Description": NotRequired[str],
    },
)
HostedZoneOwnerTypeDef = TypedDict(
    "HostedZoneOwnerTypeDef",
    {
        "OwningAccount": NotRequired[str],
        "OwningService": NotRequired[str],
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
ListCidrBlocksRequestRequestTypeDef = TypedDict(
    "ListCidrBlocksRequestRequestTypeDef",
    {
        "CollectionId": str,
        "LocationName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[str],
    },
)
ListCidrCollectionsRequestRequestTypeDef = TypedDict(
    "ListCidrCollectionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[str],
    },
)
ListCidrLocationsRequestRequestTypeDef = TypedDict(
    "ListCidrLocationsRequestRequestTypeDef",
    {
        "CollectionId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[str],
    },
)
LocationSummaryTypeDef = TypedDict(
    "LocationSummaryTypeDef",
    {
        "LocationName": NotRequired[str],
    },
)
ListGeoLocationsRequestRequestTypeDef = TypedDict(
    "ListGeoLocationsRequestRequestTypeDef",
    {
        "StartContinentCode": NotRequired[str],
        "StartCountryCode": NotRequired[str],
        "StartSubdivisionCode": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListHealthChecksRequestRequestTypeDef = TypedDict(
    "ListHealthChecksRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListHostedZonesByNameRequestRequestTypeDef = TypedDict(
    "ListHostedZonesByNameRequestRequestTypeDef",
    {
        "DNSName": NotRequired[str],
        "HostedZoneId": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListHostedZonesByVPCRequestRequestTypeDef = TypedDict(
    "ListHostedZonesByVPCRequestRequestTypeDef",
    {
        "VPCId": str,
        "VPCRegion": VPCRegionType,
        "MaxItems": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListHostedZonesRequestRequestTypeDef = TypedDict(
    "ListHostedZonesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
        "DelegationSetId": NotRequired[str],
        "HostedZoneType": NotRequired[Literal["PrivateHostedZone"]],
    },
)
ListQueryLoggingConfigsRequestRequestTypeDef = TypedDict(
    "ListQueryLoggingConfigsRequestRequestTypeDef",
    {
        "HostedZoneId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[str],
    },
)
ListResourceRecordSetsRequestRequestTypeDef = TypedDict(
    "ListResourceRecordSetsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "StartRecordName": NotRequired[str],
        "StartRecordType": NotRequired[RRTypeType],
        "StartRecordIdentifier": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListReusableDelegationSetsRequestRequestTypeDef = TypedDict(
    "ListReusableDelegationSetsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
    },
)
ListTagsForResourcesRequestRequestTypeDef = TypedDict(
    "ListTagsForResourcesRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceIds": Sequence[str],
    },
)
ListTrafficPoliciesRequestRequestTypeDef = TypedDict(
    "ListTrafficPoliciesRequestRequestTypeDef",
    {
        "TrafficPolicyIdMarker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
TrafficPolicySummaryTypeDef = TypedDict(
    "TrafficPolicySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": RRTypeType,
        "LatestVersion": int,
        "TrafficPolicyCount": int,
    },
)
ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "TrafficPolicyInstanceNameMarker": NotRequired[str],
        "TrafficPolicyInstanceTypeMarker": NotRequired[RRTypeType],
        "MaxItems": NotRequired[str],
    },
)
ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "HostedZoneIdMarker": NotRequired[str],
        "TrafficPolicyInstanceNameMarker": NotRequired[str],
        "TrafficPolicyInstanceTypeMarker": NotRequired[RRTypeType],
        "MaxItems": NotRequired[str],
    },
)
ListTrafficPolicyInstancesRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyInstancesRequestRequestTypeDef",
    {
        "HostedZoneIdMarker": NotRequired[str],
        "TrafficPolicyInstanceNameMarker": NotRequired[str],
        "TrafficPolicyInstanceTypeMarker": NotRequired[RRTypeType],
        "MaxItems": NotRequired[str],
    },
)
ListTrafficPolicyVersionsRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyVersionsRequestRequestTypeDef",
    {
        "Id": str,
        "TrafficPolicyVersionMarker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListVPCAssociationAuthorizationsRequestRequestTypeDef = TypedDict(
    "ListVPCAssociationAuthorizationsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[str],
    },
)
ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Value": str,
    },
)
TestDNSAnswerRequestRequestTypeDef = TypedDict(
    "TestDNSAnswerRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "RecordName": str,
        "RecordType": RRTypeType,
        "ResolverIP": NotRequired[str],
        "EDNS0ClientSubnetIP": NotRequired[str],
        "EDNS0ClientSubnetMask": NotRequired[str],
    },
)
UpdateHostedZoneCommentRequestRequestTypeDef = TypedDict(
    "UpdateHostedZoneCommentRequestRequestTypeDef",
    {
        "Id": str,
        "Comment": NotRequired[str],
    },
)
UpdateTrafficPolicyCommentRequestRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
        "Comment": str,
    },
)
UpdateTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
        "TTL": int,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)
ActivateKeySigningKeyResponseTypeDef = TypedDict(
    "ActivateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateVPCWithHostedZoneResponseTypeDef = TypedDict(
    "AssociateVPCWithHostedZoneResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChangeCidrCollectionResponseTypeDef = TypedDict(
    "ChangeCidrCollectionResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChangeResourceRecordSetsResponseTypeDef = TypedDict(
    "ChangeResourceRecordSetsResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeactivateKeySigningKeyResponseTypeDef = TypedDict(
    "DeactivateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteHostedZoneResponseTypeDef = TypedDict(
    "DeleteHostedZoneResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteKeySigningKeyResponseTypeDef = TypedDict(
    "DeleteKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "DisableHostedZoneDNSSECResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateVPCFromHostedZoneResponseTypeDef = TypedDict(
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "EnableHostedZoneDNSSECResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountLimitResponseTypeDef = TypedDict(
    "GetAccountLimitResponseTypeDef",
    {
        "Limit": AccountLimitTypeDef,
        "Count": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChangeResponseTypeDef = TypedDict(
    "GetChangeResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCheckerIpRangesResponseTypeDef = TypedDict(
    "GetCheckerIpRangesResponseTypeDef",
    {
        "CheckerIpRanges": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHealthCheckCountResponseTypeDef = TypedDict(
    "GetHealthCheckCountResponseTypeDef",
    {
        "HealthCheckCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHostedZoneCountResponseTypeDef = TypedDict(
    "GetHostedZoneCountResponseTypeDef",
    {
        "HostedZoneCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrafficPolicyInstanceCountResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    {
        "TrafficPolicyInstanceCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestDNSAnswerResponseTypeDef = TypedDict(
    "TestDNSAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": RRTypeType,
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HealthCheckConfigOutputTypeDef = TypedDict(
    "HealthCheckConfigOutputTypeDef",
    {
        "Type": HealthCheckTypeType,
        "IPAddress": NotRequired[str],
        "Port": NotRequired[int],
        "ResourcePath": NotRequired[str],
        "FullyQualifiedDomainName": NotRequired[str],
        "SearchString": NotRequired[str],
        "RequestInterval": NotRequired[int],
        "FailureThreshold": NotRequired[int],
        "MeasureLatency": NotRequired[bool],
        "Inverted": NotRequired[bool],
        "Disabled": NotRequired[bool],
        "HealthThreshold": NotRequired[int],
        "ChildHealthChecks": NotRequired[List[str]],
        "EnableSNI": NotRequired[bool],
        "Regions": NotRequired[List[HealthCheckRegionType]],
        "AlarmIdentifier": NotRequired[AlarmIdentifierTypeDef],
        "InsufficientDataHealthStatus": NotRequired[InsufficientDataHealthStatusType],
        "RoutingControlArn": NotRequired[str],
    },
)
HealthCheckConfigTypeDef = TypedDict(
    "HealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
        "IPAddress": NotRequired[str],
        "Port": NotRequired[int],
        "ResourcePath": NotRequired[str],
        "FullyQualifiedDomainName": NotRequired[str],
        "SearchString": NotRequired[str],
        "RequestInterval": NotRequired[int],
        "FailureThreshold": NotRequired[int],
        "MeasureLatency": NotRequired[bool],
        "Inverted": NotRequired[bool],
        "Disabled": NotRequired[bool],
        "HealthThreshold": NotRequired[int],
        "ChildHealthChecks": NotRequired[Sequence[str]],
        "EnableSNI": NotRequired[bool],
        "Regions": NotRequired[Sequence[HealthCheckRegionType]],
        "AlarmIdentifier": NotRequired[AlarmIdentifierTypeDef],
        "InsufficientDataHealthStatus": NotRequired[InsufficientDataHealthStatusType],
        "RoutingControlArn": NotRequired[str],
    },
)
UpdateHealthCheckRequestRequestTypeDef = TypedDict(
    "UpdateHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
        "HealthCheckVersion": NotRequired[int],
        "IPAddress": NotRequired[str],
        "Port": NotRequired[int],
        "ResourcePath": NotRequired[str],
        "FullyQualifiedDomainName": NotRequired[str],
        "SearchString": NotRequired[str],
        "FailureThreshold": NotRequired[int],
        "Inverted": NotRequired[bool],
        "Disabled": NotRequired[bool],
        "HealthThreshold": NotRequired[int],
        "ChildHealthChecks": NotRequired[Sequence[str]],
        "EnableSNI": NotRequired[bool],
        "Regions": NotRequired[Sequence[HealthCheckRegionType]],
        "AlarmIdentifier": NotRequired[AlarmIdentifierTypeDef],
        "InsufficientDataHealthStatus": NotRequired[InsufficientDataHealthStatusType],
        "ResetElements": NotRequired[Sequence[ResettableElementNameType]],
    },
)
AssociateVPCWithHostedZoneRequestRequestTypeDef = TypedDict(
    "AssociateVPCWithHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": VPCTypeDef,
        "Comment": NotRequired[str],
    },
)
CreateVPCAssociationAuthorizationRequestRequestTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": VPCTypeDef,
    },
)
CreateVPCAssociationAuthorizationResponseTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPC": VPCTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVPCAssociationAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteVPCAssociationAuthorizationRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": VPCTypeDef,
    },
)
DisassociateVPCFromHostedZoneRequestRequestTypeDef = TypedDict(
    "DisassociateVPCFromHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": VPCTypeDef,
        "Comment": NotRequired[str],
    },
)
ListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPCs": List[VPCTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ChangeCidrCollectionRequestRequestTypeDef = TypedDict(
    "ChangeCidrCollectionRequestRequestTypeDef",
    {
        "Id": str,
        "Changes": Sequence[CidrCollectionChangeTypeDef],
        "CollectionVersion": NotRequired[int],
    },
)
ChangeTagsForResourceRequestRequestTypeDef = TypedDict(
    "ChangeTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
        "AddTags": NotRequired[Sequence[TagTypeDef]],
        "RemoveTagKeys": NotRequired[Sequence[str]],
    },
)
ResourceTagSetTypeDef = TypedDict(
    "ResourceTagSetTypeDef",
    {
        "ResourceType": NotRequired[TagResourceTypeType],
        "ResourceId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ListCidrBlocksResponseTypeDef = TypedDict(
    "ListCidrBlocksResponseTypeDef",
    {
        "CidrBlocks": List[CidrBlockSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateCidrCollectionResponseTypeDef = TypedDict(
    "CreateCidrCollectionResponseTypeDef",
    {
        "Collection": CidrCollectionTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CloudWatchAlarmConfigurationTypeDef = TypedDict(
    "CloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorType,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
        "Dimensions": NotRequired[List[DimensionTypeDef]],
    },
)
ListCidrCollectionsResponseTypeDef = TypedDict(
    "ListCidrCollectionsResponseTypeDef",
    {
        "CidrCollections": List[CollectionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GeoProximityLocationTypeDef = TypedDict(
    "GeoProximityLocationTypeDef",
    {
        "AWSRegion": NotRequired[str],
        "LocalZoneGroup": NotRequired[str],
        "Coordinates": NotRequired[CoordinatesTypeDef],
        "Bias": NotRequired[int],
    },
)
CreateHostedZoneRequestRequestTypeDef = TypedDict(
    "CreateHostedZoneRequestRequestTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "VPC": NotRequired[VPCTypeDef],
        "HostedZoneConfig": NotRequired[HostedZoneConfigTypeDef],
        "DelegationSetId": NotRequired[str],
    },
)
CreateReusableDelegationSetResponseTypeDef = TypedDict(
    "CreateReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": DelegationSetTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReusableDelegationSetResponseTypeDef = TypedDict(
    "GetReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": DelegationSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReusableDelegationSetsResponseTypeDef = TypedDict(
    "ListReusableDelegationSetsResponseTypeDef",
    {
        "DelegationSets": List[DelegationSetTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKeySigningKeyResponseTypeDef = TypedDict(
    "CreateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": ChangeInfoTypeDef,
        "KeySigningKey": KeySigningKeyTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateQueryLoggingConfigResponseTypeDef = TypedDict(
    "CreateQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": QueryLoggingConfigTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryLoggingConfigResponseTypeDef = TypedDict(
    "GetQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": QueryLoggingConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "ListQueryLoggingConfigsResponseTypeDef",
    {
        "QueryLoggingConfigs": List[QueryLoggingConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": TrafficPolicyInstanceTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": TrafficPolicyInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstances": List[TrafficPolicyInstanceTypeDef],
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "TrafficPolicyInstances": List[TrafficPolicyInstanceTypeDef],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesResponseTypeDef",
    {
        "TrafficPolicyInstances": List[TrafficPolicyInstanceTypeDef],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": TrafficPolicyInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrafficPolicyResponseTypeDef = TypedDict(
    "CreateTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": TrafficPolicyTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrafficPolicyVersionResponseTypeDef = TypedDict(
    "CreateTrafficPolicyVersionResponseTypeDef",
    {
        "TrafficPolicy": TrafficPolicyTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrafficPolicyResponseTypeDef = TypedDict(
    "GetTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": TrafficPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrafficPolicyVersionsResponseTypeDef = TypedDict(
    "ListTrafficPolicyVersionsResponseTypeDef",
    {
        "TrafficPolicies": List[TrafficPolicyTypeDef],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrafficPolicyCommentResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentResponseTypeDef",
    {
        "TrafficPolicy": TrafficPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDNSSECResponseTypeDef = TypedDict(
    "GetDNSSECResponseTypeDef",
    {
        "Status": DNSSECStatusTypeDef,
        "KeySigningKeys": List[KeySigningKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGeoLocationResponseTypeDef = TypedDict(
    "GetGeoLocationResponseTypeDef",
    {
        "GeoLocationDetails": GeoLocationDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGeoLocationsResponseTypeDef = TypedDict(
    "ListGeoLocationsResponseTypeDef",
    {
        "GeoLocationDetailsList": List[GeoLocationDetailsTypeDef],
        "IsTruncated": bool,
        "NextContinentCode": str,
        "NextCountryCode": str,
        "NextSubdivisionCode": str,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChangeRequestResourceRecordSetsChangedWaitTypeDef = TypedDict(
    "GetChangeRequestResourceRecordSetsChangedWaitTypeDef",
    {
        "Id": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetHostedZoneLimitResponseTypeDef = TypedDict(
    "GetHostedZoneLimitResponseTypeDef",
    {
        "Limit": HostedZoneLimitTypeDef,
        "Count": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReusableDelegationSetLimitResponseTypeDef = TypedDict(
    "GetReusableDelegationSetLimitResponseTypeDef",
    {
        "Limit": ReusableDelegationSetLimitTypeDef,
        "Count": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HealthCheckObservationTypeDef = TypedDict(
    "HealthCheckObservationTypeDef",
    {
        "Region": NotRequired[HealthCheckRegionType],
        "IPAddress": NotRequired[str],
        "StatusReport": NotRequired[StatusReportTypeDef],
    },
)
HostedZoneTypeDef = TypedDict(
    "HostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": NotRequired[HostedZoneConfigTypeDef],
        "ResourceRecordSetCount": NotRequired[int],
        "LinkedService": NotRequired[LinkedServiceTypeDef],
    },
)
HostedZoneSummaryTypeDef = TypedDict(
    "HostedZoneSummaryTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
        "Owner": HostedZoneOwnerTypeDef,
    },
)
ListCidrBlocksRequestListCidrBlocksPaginateTypeDef = TypedDict(
    "ListCidrBlocksRequestListCidrBlocksPaginateTypeDef",
    {
        "CollectionId": str,
        "LocationName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCidrCollectionsRequestListCidrCollectionsPaginateTypeDef = TypedDict(
    "ListCidrCollectionsRequestListCidrCollectionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCidrLocationsRequestListCidrLocationsPaginateTypeDef = TypedDict(
    "ListCidrLocationsRequestListCidrLocationsPaginateTypeDef",
    {
        "CollectionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHealthChecksRequestListHealthChecksPaginateTypeDef = TypedDict(
    "ListHealthChecksRequestListHealthChecksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHostedZonesRequestListHostedZonesPaginateTypeDef = TypedDict(
    "ListHostedZonesRequestListHostedZonesPaginateTypeDef",
    {
        "DelegationSetId": NotRequired[str],
        "HostedZoneType": NotRequired[Literal["PrivateHostedZone"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueryLoggingConfigsRequestListQueryLoggingConfigsPaginateTypeDef = TypedDict(
    "ListQueryLoggingConfigsRequestListQueryLoggingConfigsPaginateTypeDef",
    {
        "HostedZoneId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceRecordSetsRequestListResourceRecordSetsPaginateTypeDef = TypedDict(
    "ListResourceRecordSetsRequestListResourceRecordSetsPaginateTypeDef",
    {
        "HostedZoneId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVPCAssociationAuthorizationsRequestListVPCAssociationAuthorizationsPaginateTypeDef = TypedDict(
    "ListVPCAssociationAuthorizationsRequestListVPCAssociationAuthorizationsPaginateTypeDef",
    {
        "HostedZoneId": str,
        "MaxResults": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCidrLocationsResponseTypeDef = TypedDict(
    "ListCidrLocationsResponseTypeDef",
    {
        "CidrLocations": List[LocationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTrafficPoliciesResponseTypeDef = TypedDict(
    "ListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicySummaries": List[TrafficPolicySummaryTypeDef],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHealthCheckRequestRequestTypeDef = TypedDict(
    "CreateHealthCheckRequestRequestTypeDef",
    {
        "CallerReference": str,
        "HealthCheckConfig": HealthCheckConfigTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceTagSet": ResourceTagSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourcesResponseTypeDef = TypedDict(
    "ListTagsForResourcesResponseTypeDef",
    {
        "ResourceTagSets": List[ResourceTagSetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HealthCheckTypeDef = TypedDict(
    "HealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "HealthCheckConfig": HealthCheckConfigOutputTypeDef,
        "HealthCheckVersion": int,
        "LinkedService": NotRequired[LinkedServiceTypeDef],
        "CloudWatchAlarmConfiguration": NotRequired[CloudWatchAlarmConfigurationTypeDef],
    },
)
ResourceRecordSetOutputTypeDef = TypedDict(
    "ResourceRecordSetOutputTypeDef",
    {
        "Name": str,
        "Type": RRTypeType,
        "SetIdentifier": NotRequired[str],
        "Weight": NotRequired[int],
        "Region": NotRequired[ResourceRecordSetRegionType],
        "GeoLocation": NotRequired[GeoLocationTypeDef],
        "Failover": NotRequired[ResourceRecordSetFailoverType],
        "MultiValueAnswer": NotRequired[bool],
        "TTL": NotRequired[int],
        "ResourceRecords": NotRequired[List[ResourceRecordTypeDef]],
        "AliasTarget": NotRequired[AliasTargetTypeDef],
        "HealthCheckId": NotRequired[str],
        "TrafficPolicyInstanceId": NotRequired[str],
        "CidrRoutingConfig": NotRequired[CidrRoutingConfigTypeDef],
        "GeoProximityLocation": NotRequired[GeoProximityLocationTypeDef],
    },
)
ResourceRecordSetTypeDef = TypedDict(
    "ResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": RRTypeType,
        "SetIdentifier": NotRequired[str],
        "Weight": NotRequired[int],
        "Region": NotRequired[ResourceRecordSetRegionType],
        "GeoLocation": NotRequired[GeoLocationTypeDef],
        "Failover": NotRequired[ResourceRecordSetFailoverType],
        "MultiValueAnswer": NotRequired[bool],
        "TTL": NotRequired[int],
        "ResourceRecords": NotRequired[Sequence[ResourceRecordTypeDef]],
        "AliasTarget": NotRequired[AliasTargetTypeDef],
        "HealthCheckId": NotRequired[str],
        "TrafficPolicyInstanceId": NotRequired[str],
        "CidrRoutingConfig": NotRequired[CidrRoutingConfigTypeDef],
        "GeoProximityLocation": NotRequired[GeoProximityLocationTypeDef],
    },
)
GetHealthCheckLastFailureReasonResponseTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    {
        "HealthCheckObservations": List[HealthCheckObservationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHealthCheckStatusResponseTypeDef = TypedDict(
    "GetHealthCheckStatusResponseTypeDef",
    {
        "HealthCheckObservations": List[HealthCheckObservationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHostedZoneResponseTypeDef = TypedDict(
    "CreateHostedZoneResponseTypeDef",
    {
        "HostedZone": HostedZoneTypeDef,
        "ChangeInfo": ChangeInfoTypeDef,
        "DelegationSet": DelegationSetTypeDef,
        "VPC": VPCTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHostedZoneResponseTypeDef = TypedDict(
    "GetHostedZoneResponseTypeDef",
    {
        "HostedZone": HostedZoneTypeDef,
        "DelegationSet": DelegationSetTypeDef,
        "VPCs": List[VPCTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHostedZonesByNameResponseTypeDef = TypedDict(
    "ListHostedZonesByNameResponseTypeDef",
    {
        "HostedZones": List[HostedZoneTypeDef],
        "DNSName": str,
        "HostedZoneId": str,
        "IsTruncated": bool,
        "NextDNSName": str,
        "NextHostedZoneId": str,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHostedZonesResponseTypeDef = TypedDict(
    "ListHostedZonesResponseTypeDef",
    {
        "HostedZones": List[HostedZoneTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateHostedZoneCommentResponseTypeDef = TypedDict(
    "UpdateHostedZoneCommentResponseTypeDef",
    {
        "HostedZone": HostedZoneTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHostedZonesByVPCResponseTypeDef = TypedDict(
    "ListHostedZonesByVPCResponseTypeDef",
    {
        "HostedZoneSummaries": List[HostedZoneSummaryTypeDef],
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateHealthCheckResponseTypeDef = TypedDict(
    "CreateHealthCheckResponseTypeDef",
    {
        "HealthCheck": HealthCheckTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHealthCheckResponseTypeDef = TypedDict(
    "GetHealthCheckResponseTypeDef",
    {
        "HealthCheck": HealthCheckTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHealthChecksResponseTypeDef = TypedDict(
    "ListHealthChecksResponseTypeDef",
    {
        "HealthChecks": List[HealthCheckTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateHealthCheckResponseTypeDef = TypedDict(
    "UpdateHealthCheckResponseTypeDef",
    {
        "HealthCheck": HealthCheckTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceRecordSetsResponseTypeDef = TypedDict(
    "ListResourceRecordSetsResponseTypeDef",
    {
        "ResourceRecordSets": List[ResourceRecordSetOutputTypeDef],
        "IsTruncated": bool,
        "NextRecordName": str,
        "NextRecordType": RRTypeType,
        "NextRecordIdentifier": str,
        "MaxItems": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceRecordSetUnionTypeDef = Union[ResourceRecordSetTypeDef, ResourceRecordSetOutputTypeDef]
ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Action": ChangeActionType,
        "ResourceRecordSet": ResourceRecordSetUnionTypeDef,
    },
)
ChangeBatchTypeDef = TypedDict(
    "ChangeBatchTypeDef",
    {
        "Changes": Sequence[ChangeTypeDef],
        "Comment": NotRequired[str],
    },
)
ChangeResourceRecordSetsRequestRequestTypeDef = TypedDict(
    "ChangeResourceRecordSetsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "ChangeBatch": ChangeBatchTypeDef,
    },
)
