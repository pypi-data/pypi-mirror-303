"""
Type annotations for servicediscovery service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/type_defs/)

Usage::

    ```python
    from mypy_boto3_servicediscovery.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    CustomHealthStatusType,
    FilterConditionType,
    HealthCheckTypeType,
    HealthStatusFilterType,
    HealthStatusType,
    NamespaceFilterNameType,
    NamespaceTypeType,
    OperationFilterNameType,
    OperationStatusType,
    OperationTargetTypeType,
    OperationTypeType,
    RecordTypeType,
    RoutingPolicyType,
    ServiceTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckCustomConfigTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeregisterInstanceRequestRequestTypeDef",
    "DiscoverInstancesRequestRequestTypeDef",
    "HttpInstanceSummaryTypeDef",
    "DiscoverInstancesRevisionRequestRequestTypeDef",
    "DnsRecordTypeDef",
    "SOATypeDef",
    "GetInstanceRequestRequestTypeDef",
    "InstanceTypeDef",
    "GetInstancesHealthStatusRequestRequestTypeDef",
    "GetNamespaceRequestRequestTypeDef",
    "GetOperationRequestRequestTypeDef",
    "OperationTypeDef",
    "GetServiceRequestRequestTypeDef",
    "HttpNamespaceChangeTypeDef",
    "HttpPropertiesTypeDef",
    "InstanceSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "NamespaceFilterTypeDef",
    "OperationFilterTypeDef",
    "OperationSummaryTypeDef",
    "ServiceFilterTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "SOAChangeTypeDef",
    "RegisterInstanceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateInstanceCustomHealthStatusRequestRequestTypeDef",
    "CreateHttpNamespaceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateHttpNamespaceResponseTypeDef",
    "CreatePrivateDnsNamespaceResponseTypeDef",
    "CreatePublicDnsNamespaceResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeregisterInstanceResponseTypeDef",
    "DiscoverInstancesRevisionResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetInstancesHealthStatusResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RegisterInstanceResponseTypeDef",
    "UpdateHttpNamespaceResponseTypeDef",
    "UpdatePrivateDnsNamespaceResponseTypeDef",
    "UpdatePublicDnsNamespaceResponseTypeDef",
    "UpdateServiceResponseTypeDef",
    "DiscoverInstancesResponseTypeDef",
    "DnsConfigChangeTypeDef",
    "DnsConfigOutputTypeDef",
    "DnsConfigTypeDef",
    "DnsPropertiesTypeDef",
    "PrivateDnsPropertiesMutableTypeDef",
    "PublicDnsPropertiesMutableTypeDef",
    "GetInstanceResponseTypeDef",
    "GetOperationResponseTypeDef",
    "UpdateHttpNamespaceRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListInstancesRequestListInstancesPaginateTypeDef",
    "ListNamespacesRequestListNamespacesPaginateTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListOperationsRequestListOperationsPaginateTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesRequestListServicesPaginateTypeDef",
    "ListServicesRequestRequestTypeDef",
    "PrivateDnsPropertiesMutableChangeTypeDef",
    "PublicDnsPropertiesMutableChangeTypeDef",
    "ServiceChangeTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "NamespacePropertiesTypeDef",
    "PrivateDnsNamespacePropertiesTypeDef",
    "PublicDnsNamespacePropertiesTypeDef",
    "PrivateDnsNamespacePropertiesChangeTypeDef",
    "PublicDnsNamespacePropertiesChangeTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "CreateServiceResponseTypeDef",
    "GetServiceResponseTypeDef",
    "NamespaceSummaryTypeDef",
    "NamespaceTypeDef",
    "CreatePrivateDnsNamespaceRequestRequestTypeDef",
    "CreatePublicDnsNamespaceRequestRequestTypeDef",
    "PrivateDnsNamespaceChangeTypeDef",
    "PublicDnsNamespaceChangeTypeDef",
    "ListNamespacesResponseTypeDef",
    "GetNamespaceResponseTypeDef",
    "UpdatePrivateDnsNamespaceRequestRequestTypeDef",
    "UpdatePublicDnsNamespaceRequestRequestTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
HealthCheckConfigTypeDef = TypedDict(
    "HealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
        "ResourcePath": NotRequired[str],
        "FailureThreshold": NotRequired[int],
    },
)
HealthCheckCustomConfigTypeDef = TypedDict(
    "HealthCheckCustomConfigTypeDef",
    {
        "FailureThreshold": NotRequired[int],
    },
)
DeleteNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeregisterInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
    },
)
DiscoverInstancesRequestRequestTypeDef = TypedDict(
    "DiscoverInstancesRequestRequestTypeDef",
    {
        "NamespaceName": str,
        "ServiceName": str,
        "MaxResults": NotRequired[int],
        "QueryParameters": NotRequired[Mapping[str, str]],
        "OptionalParameters": NotRequired[Mapping[str, str]],
        "HealthStatus": NotRequired[HealthStatusFilterType],
    },
)
HttpInstanceSummaryTypeDef = TypedDict(
    "HttpInstanceSummaryTypeDef",
    {
        "InstanceId": NotRequired[str],
        "NamespaceName": NotRequired[str],
        "ServiceName": NotRequired[str],
        "HealthStatus": NotRequired[HealthStatusType],
        "Attributes": NotRequired[Dict[str, str]],
    },
)
DiscoverInstancesRevisionRequestRequestTypeDef = TypedDict(
    "DiscoverInstancesRevisionRequestRequestTypeDef",
    {
        "NamespaceName": str,
        "ServiceName": str,
    },
)
DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef",
    {
        "Type": RecordTypeType,
        "TTL": int,
    },
)
SOATypeDef = TypedDict(
    "SOATypeDef",
    {
        "TTL": int,
    },
)
GetInstanceRequestRequestTypeDef = TypedDict(
    "GetInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "CreatorRequestId": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)
GetInstancesHealthStatusRequestRequestTypeDef = TypedDict(
    "GetInstancesHealthStatusRequestRequestTypeDef",
    {
        "ServiceId": str,
        "Instances": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetNamespaceRequestRequestTypeDef = TypedDict(
    "GetNamespaceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetOperationRequestRequestTypeDef = TypedDict(
    "GetOperationRequestRequestTypeDef",
    {
        "OperationId": str,
    },
)
OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[OperationTypeType],
        "Status": NotRequired[OperationStatusType],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UpdateDate": NotRequired[datetime],
        "Targets": NotRequired[Dict[OperationTargetTypeType, str]],
    },
)
GetServiceRequestRequestTypeDef = TypedDict(
    "GetServiceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
HttpNamespaceChangeTypeDef = TypedDict(
    "HttpNamespaceChangeTypeDef",
    {
        "Description": str,
    },
)
HttpPropertiesTypeDef = TypedDict(
    "HttpPropertiesTypeDef",
    {
        "HttpName": NotRequired[str],
    },
)
InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
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
ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "ServiceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
NamespaceFilterTypeDef = TypedDict(
    "NamespaceFilterTypeDef",
    {
        "Name": NamespaceFilterNameType,
        "Values": Sequence[str],
        "Condition": NotRequired[FilterConditionType],
    },
)
OperationFilterTypeDef = TypedDict(
    "OperationFilterTypeDef",
    {
        "Name": OperationFilterNameType,
        "Values": Sequence[str],
        "Condition": NotRequired[FilterConditionType],
    },
)
OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Status": NotRequired[OperationStatusType],
    },
)
ServiceFilterTypeDef = TypedDict(
    "ServiceFilterTypeDef",
    {
        "Name": Literal["NAMESPACE_ID"],
        "Values": Sequence[str],
        "Condition": NotRequired[FilterConditionType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
SOAChangeTypeDef = TypedDict(
    "SOAChangeTypeDef",
    {
        "TTL": int,
    },
)
RegisterInstanceRequestRequestTypeDef = TypedDict(
    "RegisterInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
        "Attributes": Mapping[str, str],
        "CreatorRequestId": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateInstanceCustomHealthStatusRequestRequestTypeDef = TypedDict(
    "UpdateInstanceCustomHealthStatusRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
        "Status": CustomHealthStatusType,
    },
)
CreateHttpNamespaceRequestRequestTypeDef = TypedDict(
    "CreateHttpNamespaceRequestRequestTypeDef",
    {
        "Name": str,
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateHttpNamespaceResponseTypeDef = TypedDict(
    "CreateHttpNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePrivateDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePublicDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterInstanceResponseTypeDef = TypedDict(
    "DeregisterInstanceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DiscoverInstancesRevisionResponseTypeDef = TypedDict(
    "DiscoverInstancesRevisionResponseTypeDef",
    {
        "InstancesRevision": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstancesHealthStatusResponseTypeDef = TypedDict(
    "GetInstancesHealthStatusResponseTypeDef",
    {
        "Status": Dict[str, HealthStatusType],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterInstanceResponseTypeDef = TypedDict(
    "RegisterInstanceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateHttpNamespaceResponseTypeDef = TypedDict(
    "UpdateHttpNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "UpdatePrivateDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "UpdatePublicDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DiscoverInstancesResponseTypeDef = TypedDict(
    "DiscoverInstancesResponseTypeDef",
    {
        "Instances": List[HttpInstanceSummaryTypeDef],
        "InstancesRevision": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DnsConfigChangeTypeDef = TypedDict(
    "DnsConfigChangeTypeDef",
    {
        "DnsRecords": Sequence[DnsRecordTypeDef],
    },
)
DnsConfigOutputTypeDef = TypedDict(
    "DnsConfigOutputTypeDef",
    {
        "DnsRecords": List[DnsRecordTypeDef],
        "NamespaceId": NotRequired[str],
        "RoutingPolicy": NotRequired[RoutingPolicyType],
    },
)
DnsConfigTypeDef = TypedDict(
    "DnsConfigTypeDef",
    {
        "DnsRecords": Sequence[DnsRecordTypeDef],
        "NamespaceId": NotRequired[str],
        "RoutingPolicy": NotRequired[RoutingPolicyType],
    },
)
DnsPropertiesTypeDef = TypedDict(
    "DnsPropertiesTypeDef",
    {
        "HostedZoneId": NotRequired[str],
        "SOA": NotRequired[SOATypeDef],
    },
)
PrivateDnsPropertiesMutableTypeDef = TypedDict(
    "PrivateDnsPropertiesMutableTypeDef",
    {
        "SOA": SOATypeDef,
    },
)
PublicDnsPropertiesMutableTypeDef = TypedDict(
    "PublicDnsPropertiesMutableTypeDef",
    {
        "SOA": SOATypeDef,
    },
)
GetInstanceResponseTypeDef = TypedDict(
    "GetInstanceResponseTypeDef",
    {
        "Instance": InstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOperationResponseTypeDef = TypedDict(
    "GetOperationResponseTypeDef",
    {
        "Operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateHttpNamespaceRequestRequestTypeDef = TypedDict(
    "UpdateHttpNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": HttpNamespaceChangeTypeDef,
        "UpdaterRequestId": NotRequired[str],
    },
)
ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "Instances": List[InstanceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListInstancesRequestListInstancesPaginateTypeDef = TypedDict(
    "ListInstancesRequestListInstancesPaginateTypeDef",
    {
        "ServiceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNamespacesRequestListNamespacesPaginateTypeDef = TypedDict(
    "ListNamespacesRequestListNamespacesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[NamespaceFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNamespacesRequestRequestTypeDef = TypedDict(
    "ListNamespacesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[NamespaceFilterTypeDef]],
    },
)
ListOperationsRequestListOperationsPaginateTypeDef = TypedDict(
    "ListOperationsRequestListOperationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[OperationFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOperationsRequestRequestTypeDef = TypedDict(
    "ListOperationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[OperationFilterTypeDef]],
    },
)
ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "Operations": List[OperationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListServicesRequestListServicesPaginateTypeDef = TypedDict(
    "ListServicesRequestListServicesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[ServiceFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[ServiceFilterTypeDef]],
    },
)
PrivateDnsPropertiesMutableChangeTypeDef = TypedDict(
    "PrivateDnsPropertiesMutableChangeTypeDef",
    {
        "SOA": SOAChangeTypeDef,
    },
)
PublicDnsPropertiesMutableChangeTypeDef = TypedDict(
    "PublicDnsPropertiesMutableChangeTypeDef",
    {
        "SOA": SOAChangeTypeDef,
    },
)
ServiceChangeTypeDef = TypedDict(
    "ServiceChangeTypeDef",
    {
        "Description": NotRequired[str],
        "DnsConfig": NotRequired[DnsConfigChangeTypeDef],
        "HealthCheckConfig": NotRequired[HealthCheckConfigTypeDef],
    },
)
ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ServiceTypeType],
        "Description": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "DnsConfig": NotRequired[DnsConfigOutputTypeDef],
        "HealthCheckConfig": NotRequired[HealthCheckConfigTypeDef],
        "HealthCheckCustomConfig": NotRequired[HealthCheckCustomConfigTypeDef],
        "CreateDate": NotRequired[datetime],
    },
)
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "NamespaceId": NotRequired[str],
        "Description": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "DnsConfig": NotRequired[DnsConfigOutputTypeDef],
        "Type": NotRequired[ServiceTypeType],
        "HealthCheckConfig": NotRequired[HealthCheckConfigTypeDef],
        "HealthCheckCustomConfig": NotRequired[HealthCheckCustomConfigTypeDef],
        "CreateDate": NotRequired[datetime],
        "CreatorRequestId": NotRequired[str],
    },
)
CreateServiceRequestRequestTypeDef = TypedDict(
    "CreateServiceRequestRequestTypeDef",
    {
        "Name": str,
        "NamespaceId": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "DnsConfig": NotRequired[DnsConfigTypeDef],
        "HealthCheckConfig": NotRequired[HealthCheckConfigTypeDef],
        "HealthCheckCustomConfig": NotRequired[HealthCheckCustomConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Type": NotRequired[Literal["HTTP"]],
    },
)
NamespacePropertiesTypeDef = TypedDict(
    "NamespacePropertiesTypeDef",
    {
        "DnsProperties": NotRequired[DnsPropertiesTypeDef],
        "HttpProperties": NotRequired[HttpPropertiesTypeDef],
    },
)
PrivateDnsNamespacePropertiesTypeDef = TypedDict(
    "PrivateDnsNamespacePropertiesTypeDef",
    {
        "DnsProperties": PrivateDnsPropertiesMutableTypeDef,
    },
)
PublicDnsNamespacePropertiesTypeDef = TypedDict(
    "PublicDnsNamespacePropertiesTypeDef",
    {
        "DnsProperties": PublicDnsPropertiesMutableTypeDef,
    },
)
PrivateDnsNamespacePropertiesChangeTypeDef = TypedDict(
    "PrivateDnsNamespacePropertiesChangeTypeDef",
    {
        "DnsProperties": PrivateDnsPropertiesMutableChangeTypeDef,
    },
)
PublicDnsNamespacePropertiesChangeTypeDef = TypedDict(
    "PublicDnsNamespacePropertiesChangeTypeDef",
    {
        "DnsProperties": PublicDnsPropertiesMutableChangeTypeDef,
    },
)
UpdateServiceRequestRequestTypeDef = TypedDict(
    "UpdateServiceRequestRequestTypeDef",
    {
        "Id": str,
        "Service": ServiceChangeTypeDef,
    },
)
ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "Services": List[ServiceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NamespaceSummaryTypeDef = TypedDict(
    "NamespaceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[NamespaceTypeType],
        "Description": NotRequired[str],
        "ServiceCount": NotRequired[int],
        "Properties": NotRequired[NamespacePropertiesTypeDef],
        "CreateDate": NotRequired[datetime],
    },
)
NamespaceTypeDef = TypedDict(
    "NamespaceTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[NamespaceTypeType],
        "Description": NotRequired[str],
        "ServiceCount": NotRequired[int],
        "Properties": NotRequired[NamespacePropertiesTypeDef],
        "CreateDate": NotRequired[datetime],
        "CreatorRequestId": NotRequired[str],
    },
)
CreatePrivateDnsNamespaceRequestRequestTypeDef = TypedDict(
    "CreatePrivateDnsNamespaceRequestRequestTypeDef",
    {
        "Name": str,
        "Vpc": str,
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Properties": NotRequired[PrivateDnsNamespacePropertiesTypeDef],
    },
)
CreatePublicDnsNamespaceRequestRequestTypeDef = TypedDict(
    "CreatePublicDnsNamespaceRequestRequestTypeDef",
    {
        "Name": str,
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Properties": NotRequired[PublicDnsNamespacePropertiesTypeDef],
    },
)
PrivateDnsNamespaceChangeTypeDef = TypedDict(
    "PrivateDnsNamespaceChangeTypeDef",
    {
        "Description": NotRequired[str],
        "Properties": NotRequired[PrivateDnsNamespacePropertiesChangeTypeDef],
    },
)
PublicDnsNamespaceChangeTypeDef = TypedDict(
    "PublicDnsNamespaceChangeTypeDef",
    {
        "Description": NotRequired[str],
        "Properties": NotRequired[PublicDnsNamespacePropertiesChangeTypeDef],
    },
)
ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List[NamespaceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetNamespaceResponseTypeDef = TypedDict(
    "GetNamespaceResponseTypeDef",
    {
        "Namespace": NamespaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePrivateDnsNamespaceRequestRequestTypeDef = TypedDict(
    "UpdatePrivateDnsNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": PrivateDnsNamespaceChangeTypeDef,
        "UpdaterRequestId": NotRequired[str],
    },
)
UpdatePublicDnsNamespaceRequestRequestTypeDef = TypedDict(
    "UpdatePublicDnsNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": PublicDnsNamespaceChangeTypeDef,
        "UpdaterRequestId": NotRequired[str],
    },
)
