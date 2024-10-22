"""
Type annotations for appmesh service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/type_defs/)

Usage::

    ```python
    from mypy_boto3_appmesh.type_defs import AwsCloudMapInstanceAttributeTypeDef

    data: AwsCloudMapInstanceAttributeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    DefaultGatewayRouteRewriteType,
    DnsResponseTypeType,
    DurationUnitType,
    EgressFilterTypeType,
    GatewayRouteStatusCodeType,
    GrpcRetryPolicyEventType,
    HttpMethodType,
    HttpSchemeType,
    IpPreferenceType,
    ListenerTlsModeType,
    MeshStatusCodeType,
    PortProtocolType,
    RouteStatusCodeType,
    VirtualGatewayListenerTlsModeType,
    VirtualGatewayPortProtocolType,
    VirtualGatewayStatusCodeType,
    VirtualNodeStatusCodeType,
    VirtualRouterStatusCodeType,
    VirtualServiceStatusCodeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AwsCloudMapInstanceAttributeTypeDef",
    "ListenerTlsFileCertificateTypeDef",
    "ListenerTlsSdsCertificateTypeDef",
    "TagRefTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteGatewayRouteInputRequestTypeDef",
    "DeleteMeshInputRequestTypeDef",
    "DeleteRouteInputRequestTypeDef",
    "DeleteVirtualGatewayInputRequestTypeDef",
    "DeleteVirtualNodeInputRequestTypeDef",
    "DeleteVirtualRouterInputRequestTypeDef",
    "DeleteVirtualServiceInputRequestTypeDef",
    "DescribeGatewayRouteInputRequestTypeDef",
    "DescribeMeshInputRequestTypeDef",
    "DescribeRouteInputRequestTypeDef",
    "DescribeVirtualGatewayInputRequestTypeDef",
    "DescribeVirtualNodeInputRequestTypeDef",
    "DescribeVirtualRouterInputRequestTypeDef",
    "DescribeVirtualServiceInputRequestTypeDef",
    "DnsServiceDiscoveryTypeDef",
    "DurationTypeDef",
    "EgressFilterTypeDef",
    "GatewayRouteStatusTypeDef",
    "ResourceMetadataTypeDef",
    "GatewayRouteHostnameMatchTypeDef",
    "GatewayRouteHostnameRewriteTypeDef",
    "GatewayRouteRefTypeDef",
    "GatewayRouteVirtualServiceTypeDef",
    "MatchRangeTypeDef",
    "WeightedTargetTypeDef",
    "HealthCheckPolicyTypeDef",
    "HttpPathMatchTypeDef",
    "HttpGatewayRoutePathRewriteTypeDef",
    "HttpGatewayRoutePrefixRewriteTypeDef",
    "QueryParameterMatchTypeDef",
    "JsonFormatRefTypeDef",
    "PaginatorConfigTypeDef",
    "ListGatewayRoutesInputRequestTypeDef",
    "ListMeshesInputRequestTypeDef",
    "MeshRefTypeDef",
    "ListRoutesInputRequestTypeDef",
    "RouteRefTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListVirtualGatewaysInputRequestTypeDef",
    "VirtualGatewayRefTypeDef",
    "ListVirtualNodesInputRequestTypeDef",
    "VirtualNodeRefTypeDef",
    "ListVirtualRoutersInputRequestTypeDef",
    "VirtualRouterRefTypeDef",
    "ListVirtualServicesInputRequestTypeDef",
    "VirtualServiceRefTypeDef",
    "PortMappingTypeDef",
    "ListenerTlsAcmCertificateTypeDef",
    "TlsValidationContextFileTrustTypeDef",
    "TlsValidationContextSdsTrustTypeDef",
    "MeshStatusTypeDef",
    "MeshServiceDiscoveryTypeDef",
    "RouteStatusTypeDef",
    "SubjectAlternativeNameMatchersOutputTypeDef",
    "SubjectAlternativeNameMatchersTypeDef",
    "TcpRouteMatchTypeDef",
    "TlsValidationContextAcmTrustOutputTypeDef",
    "TlsValidationContextAcmTrustTypeDef",
    "UntagResourceInputRequestTypeDef",
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    "VirtualGatewayHttpConnectionPoolTypeDef",
    "VirtualGatewayStatusTypeDef",
    "VirtualGatewayHealthCheckPolicyTypeDef",
    "VirtualGatewayPortMappingTypeDef",
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    "VirtualNodeGrpcConnectionPoolTypeDef",
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    "VirtualNodeHttpConnectionPoolTypeDef",
    "VirtualNodeTcpConnectionPoolTypeDef",
    "VirtualNodeStatusTypeDef",
    "VirtualNodeServiceProviderTypeDef",
    "VirtualRouterStatusTypeDef",
    "VirtualRouterServiceProviderTypeDef",
    "VirtualServiceStatusTypeDef",
    "AwsCloudMapServiceDiscoveryOutputTypeDef",
    "AwsCloudMapServiceDiscoveryTypeDef",
    "ClientTlsCertificateTypeDef",
    "TagResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "GrpcRetryPolicyOutputTypeDef",
    "GrpcRetryPolicyTypeDef",
    "GrpcTimeoutTypeDef",
    "HttpRetryPolicyOutputTypeDef",
    "HttpRetryPolicyTypeDef",
    "HttpTimeoutTypeDef",
    "OutlierDetectionTypeDef",
    "TcpTimeoutTypeDef",
    "GrpcGatewayRouteRewriteTypeDef",
    "ListGatewayRoutesOutputTypeDef",
    "GatewayRouteTargetTypeDef",
    "GrpcMetadataMatchMethodTypeDef",
    "GrpcRouteMetadataMatchMethodTypeDef",
    "HeaderMatchMethodTypeDef",
    "GrpcRouteActionOutputTypeDef",
    "GrpcRouteActionTypeDef",
    "HttpRouteActionOutputTypeDef",
    "HttpRouteActionTypeDef",
    "TcpRouteActionOutputTypeDef",
    "TcpRouteActionTypeDef",
    "HttpGatewayRouteRewriteTypeDef",
    "HttpQueryParameterTypeDef",
    "LoggingFormatOutputTypeDef",
    "LoggingFormatTypeDef",
    "ListGatewayRoutesInputListGatewayRoutesPaginateTypeDef",
    "ListMeshesInputListMeshesPaginateTypeDef",
    "ListRoutesInputListRoutesPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "ListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef",
    "ListVirtualNodesInputListVirtualNodesPaginateTypeDef",
    "ListVirtualRoutersInputListVirtualRoutersPaginateTypeDef",
    "ListVirtualServicesInputListVirtualServicesPaginateTypeDef",
    "ListMeshesOutputTypeDef",
    "ListRoutesOutputTypeDef",
    "ListVirtualGatewaysOutputTypeDef",
    "ListVirtualNodesOutputTypeDef",
    "ListVirtualRoutersOutputTypeDef",
    "ListVirtualServicesOutputTypeDef",
    "VirtualRouterListenerTypeDef",
    "ListenerTlsCertificateTypeDef",
    "ListenerTlsValidationContextTrustTypeDef",
    "MeshSpecTypeDef",
    "SubjectAlternativeNamesOutputTypeDef",
    "SubjectAlternativeNameMatchersUnionTypeDef",
    "TlsValidationContextTrustOutputTypeDef",
    "TlsValidationContextAcmTrustUnionTypeDef",
    "VirtualGatewayClientTlsCertificateTypeDef",
    "VirtualGatewayConnectionPoolTypeDef",
    "VirtualGatewayListenerTlsCertificateTypeDef",
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    "VirtualGatewayTlsValidationContextTrustOutputTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustUnionTypeDef",
    "VirtualNodeConnectionPoolTypeDef",
    "VirtualServiceProviderTypeDef",
    "ServiceDiscoveryOutputTypeDef",
    "AwsCloudMapServiceDiscoveryUnionTypeDef",
    "GrpcRetryPolicyUnionTypeDef",
    "HttpRetryPolicyUnionTypeDef",
    "ListenerTimeoutTypeDef",
    "GrpcGatewayRouteActionTypeDef",
    "GrpcGatewayRouteMetadataTypeDef",
    "GrpcRouteMetadataTypeDef",
    "HttpGatewayRouteHeaderTypeDef",
    "HttpRouteHeaderTypeDef",
    "GrpcRouteActionUnionTypeDef",
    "HttpRouteActionUnionTypeDef",
    "TcpRouteOutputTypeDef",
    "TcpRouteActionUnionTypeDef",
    "HttpGatewayRouteActionTypeDef",
    "FileAccessLogOutputTypeDef",
    "VirtualGatewayFileAccessLogOutputTypeDef",
    "LoggingFormatUnionTypeDef",
    "VirtualRouterSpecOutputTypeDef",
    "VirtualRouterSpecTypeDef",
    "CreateMeshInputRequestTypeDef",
    "MeshDataTypeDef",
    "UpdateMeshInputRequestTypeDef",
    "ListenerTlsValidationContextOutputTypeDef",
    "SubjectAlternativeNamesTypeDef",
    "TlsValidationContextOutputTypeDef",
    "TlsValidationContextTrustTypeDef",
    "VirtualGatewayListenerTlsValidationContextOutputTypeDef",
    "VirtualGatewayTlsValidationContextOutputTypeDef",
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    "VirtualServiceSpecTypeDef",
    "ServiceDiscoveryTypeDef",
    "GrpcGatewayRouteMatchOutputTypeDef",
    "GrpcGatewayRouteMatchTypeDef",
    "GrpcRouteMatchOutputTypeDef",
    "GrpcRouteMatchTypeDef",
    "HttpGatewayRouteMatchOutputTypeDef",
    "HttpGatewayRouteMatchTypeDef",
    "HttpRouteMatchOutputTypeDef",
    "HttpRouteMatchTypeDef",
    "TcpRouteTypeDef",
    "AccessLogOutputTypeDef",
    "VirtualGatewayAccessLogOutputTypeDef",
    "FileAccessLogTypeDef",
    "VirtualGatewayFileAccessLogTypeDef",
    "VirtualRouterDataTypeDef",
    "CreateVirtualRouterInputRequestTypeDef",
    "UpdateVirtualRouterInputRequestTypeDef",
    "CreateMeshOutputTypeDef",
    "DeleteMeshOutputTypeDef",
    "DescribeMeshOutputTypeDef",
    "UpdateMeshOutputTypeDef",
    "ListenerTlsOutputTypeDef",
    "SubjectAlternativeNamesUnionTypeDef",
    "ClientPolicyTlsOutputTypeDef",
    "TlsValidationContextTrustUnionTypeDef",
    "VirtualGatewayListenerTlsOutputTypeDef",
    "VirtualGatewayClientPolicyTlsOutputTypeDef",
    "VirtualGatewayTlsValidationContextTrustUnionTypeDef",
    "CreateVirtualServiceInputRequestTypeDef",
    "UpdateVirtualServiceInputRequestTypeDef",
    "VirtualServiceDataTypeDef",
    "ServiceDiscoveryUnionTypeDef",
    "GrpcGatewayRouteOutputTypeDef",
    "GrpcGatewayRouteMatchUnionTypeDef",
    "GrpcRouteOutputTypeDef",
    "GrpcRouteMatchUnionTypeDef",
    "HttpGatewayRouteOutputTypeDef",
    "HttpGatewayRouteMatchUnionTypeDef",
    "HttpRouteOutputTypeDef",
    "HttpRouteMatchUnionTypeDef",
    "TcpRouteUnionTypeDef",
    "LoggingOutputTypeDef",
    "VirtualGatewayLoggingOutputTypeDef",
    "FileAccessLogUnionTypeDef",
    "VirtualGatewayFileAccessLogUnionTypeDef",
    "CreateVirtualRouterOutputTypeDef",
    "DeleteVirtualRouterOutputTypeDef",
    "DescribeVirtualRouterOutputTypeDef",
    "UpdateVirtualRouterOutputTypeDef",
    "ListenerOutputTypeDef",
    "ListenerTlsValidationContextTypeDef",
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    "ClientPolicyOutputTypeDef",
    "TlsValidationContextTypeDef",
    "VirtualGatewayListenerOutputTypeDef",
    "VirtualGatewayClientPolicyOutputTypeDef",
    "VirtualGatewayTlsValidationContextTypeDef",
    "CreateVirtualServiceOutputTypeDef",
    "DeleteVirtualServiceOutputTypeDef",
    "DescribeVirtualServiceOutputTypeDef",
    "UpdateVirtualServiceOutputTypeDef",
    "GrpcGatewayRouteTypeDef",
    "GrpcRouteTypeDef",
    "GatewayRouteSpecOutputTypeDef",
    "HttpGatewayRouteTypeDef",
    "RouteSpecOutputTypeDef",
    "HttpRouteTypeDef",
    "AccessLogTypeDef",
    "VirtualGatewayAccessLogTypeDef",
    "ListenerTlsValidationContextUnionTypeDef",
    "VirtualGatewayListenerTlsValidationContextUnionTypeDef",
    "BackendDefaultsOutputTypeDef",
    "VirtualServiceBackendOutputTypeDef",
    "TlsValidationContextUnionTypeDef",
    "VirtualGatewayBackendDefaultsOutputTypeDef",
    "VirtualGatewayTlsValidationContextUnionTypeDef",
    "GrpcGatewayRouteUnionTypeDef",
    "GrpcRouteUnionTypeDef",
    "GatewayRouteDataTypeDef",
    "HttpGatewayRouteUnionTypeDef",
    "RouteDataTypeDef",
    "HttpRouteUnionTypeDef",
    "AccessLogUnionTypeDef",
    "VirtualGatewayAccessLogUnionTypeDef",
    "ListenerTlsTypeDef",
    "VirtualGatewayListenerTlsTypeDef",
    "BackendOutputTypeDef",
    "ClientPolicyTlsTypeDef",
    "VirtualGatewaySpecOutputTypeDef",
    "VirtualGatewayClientPolicyTlsTypeDef",
    "CreateGatewayRouteOutputTypeDef",
    "DeleteGatewayRouteOutputTypeDef",
    "DescribeGatewayRouteOutputTypeDef",
    "UpdateGatewayRouteOutputTypeDef",
    "GatewayRouteSpecTypeDef",
    "CreateRouteOutputTypeDef",
    "DeleteRouteOutputTypeDef",
    "DescribeRouteOutputTypeDef",
    "UpdateRouteOutputTypeDef",
    "RouteSpecTypeDef",
    "LoggingTypeDef",
    "VirtualGatewayLoggingTypeDef",
    "ListenerTlsUnionTypeDef",
    "VirtualGatewayListenerTlsUnionTypeDef",
    "VirtualNodeSpecOutputTypeDef",
    "ClientPolicyTlsUnionTypeDef",
    "VirtualGatewayDataTypeDef",
    "VirtualGatewayClientPolicyTlsUnionTypeDef",
    "CreateGatewayRouteInputRequestTypeDef",
    "UpdateGatewayRouteInputRequestTypeDef",
    "CreateRouteInputRequestTypeDef",
    "UpdateRouteInputRequestTypeDef",
    "LoggingUnionTypeDef",
    "VirtualGatewayLoggingUnionTypeDef",
    "ListenerTypeDef",
    "VirtualGatewayListenerTypeDef",
    "VirtualNodeDataTypeDef",
    "ClientPolicyTypeDef",
    "CreateVirtualGatewayOutputTypeDef",
    "DeleteVirtualGatewayOutputTypeDef",
    "DescribeVirtualGatewayOutputTypeDef",
    "UpdateVirtualGatewayOutputTypeDef",
    "VirtualGatewayClientPolicyTypeDef",
    "ListenerUnionTypeDef",
    "VirtualGatewayListenerUnionTypeDef",
    "CreateVirtualNodeOutputTypeDef",
    "DeleteVirtualNodeOutputTypeDef",
    "DescribeVirtualNodeOutputTypeDef",
    "UpdateVirtualNodeOutputTypeDef",
    "ClientPolicyUnionTypeDef",
    "VirtualGatewayClientPolicyUnionTypeDef",
    "BackendDefaultsTypeDef",
    "VirtualServiceBackendTypeDef",
    "VirtualGatewayBackendDefaultsTypeDef",
    "BackendDefaultsUnionTypeDef",
    "VirtualServiceBackendUnionTypeDef",
    "VirtualGatewayBackendDefaultsUnionTypeDef",
    "BackendTypeDef",
    "VirtualGatewaySpecTypeDef",
    "BackendUnionTypeDef",
    "CreateVirtualGatewayInputRequestTypeDef",
    "UpdateVirtualGatewayInputRequestTypeDef",
    "VirtualNodeSpecTypeDef",
    "CreateVirtualNodeInputRequestTypeDef",
    "UpdateVirtualNodeInputRequestTypeDef",
)

AwsCloudMapInstanceAttributeTypeDef = TypedDict(
    "AwsCloudMapInstanceAttributeTypeDef",
    {
        "key": str,
        "value": str,
    },
)
ListenerTlsFileCertificateTypeDef = TypedDict(
    "ListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)
ListenerTlsSdsCertificateTypeDef = TypedDict(
    "ListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)
TagRefTypeDef = TypedDict(
    "TagRefTypeDef",
    {
        "key": str,
        "value": str,
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
DeleteGatewayRouteInputRequestTypeDef = TypedDict(
    "DeleteGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
    },
)
DeleteMeshInputRequestTypeDef = TypedDict(
    "DeleteMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)
DeleteRouteInputRequestTypeDef = TypedDict(
    "DeleteRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
    },
)
DeleteVirtualGatewayInputRequestTypeDef = TypedDict(
    "DeleteVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
    },
)
DeleteVirtualNodeInputRequestTypeDef = TypedDict(
    "DeleteVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
        "meshOwner": NotRequired[str],
    },
)
DeleteVirtualRouterInputRequestTypeDef = TypedDict(
    "DeleteVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
    },
)
DeleteVirtualServiceInputRequestTypeDef = TypedDict(
    "DeleteVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
        "meshOwner": NotRequired[str],
    },
)
DescribeGatewayRouteInputRequestTypeDef = TypedDict(
    "DescribeGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
    },
)
DescribeMeshInputRequestTypeDef = TypedDict(
    "DescribeMeshInputRequestTypeDef",
    {
        "meshName": str,
        "meshOwner": NotRequired[str],
    },
)
DescribeRouteInputRequestTypeDef = TypedDict(
    "DescribeRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
    },
)
DescribeVirtualGatewayInputRequestTypeDef = TypedDict(
    "DescribeVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
    },
)
DescribeVirtualNodeInputRequestTypeDef = TypedDict(
    "DescribeVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
        "meshOwner": NotRequired[str],
    },
)
DescribeVirtualRouterInputRequestTypeDef = TypedDict(
    "DescribeVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
    },
)
DescribeVirtualServiceInputRequestTypeDef = TypedDict(
    "DescribeVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
        "meshOwner": NotRequired[str],
    },
)
DnsServiceDiscoveryTypeDef = TypedDict(
    "DnsServiceDiscoveryTypeDef",
    {
        "hostname": str,
        "ipPreference": NotRequired[IpPreferenceType],
        "responseType": NotRequired[DnsResponseTypeType],
    },
)
DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "unit": NotRequired[DurationUnitType],
        "value": NotRequired[int],
    },
)
EgressFilterTypeDef = TypedDict(
    "EgressFilterTypeDef",
    {
        "type": EgressFilterTypeType,
    },
)
GatewayRouteStatusTypeDef = TypedDict(
    "GatewayRouteStatusTypeDef",
    {
        "status": GatewayRouteStatusCodeType,
    },
)
ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshOwner": str,
        "resourceOwner": str,
        "uid": str,
        "version": int,
    },
)
GatewayRouteHostnameMatchTypeDef = TypedDict(
    "GatewayRouteHostnameMatchTypeDef",
    {
        "exact": NotRequired[str],
        "suffix": NotRequired[str],
    },
)
GatewayRouteHostnameRewriteTypeDef = TypedDict(
    "GatewayRouteHostnameRewriteTypeDef",
    {
        "defaultTargetHostname": NotRequired[DefaultGatewayRouteRewriteType],
    },
)
GatewayRouteRefTypeDef = TypedDict(
    "GatewayRouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "gatewayRouteName": str,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)
GatewayRouteVirtualServiceTypeDef = TypedDict(
    "GatewayRouteVirtualServiceTypeDef",
    {
        "virtualServiceName": str,
    },
)
MatchRangeTypeDef = TypedDict(
    "MatchRangeTypeDef",
    {
        "end": int,
        "start": int,
    },
)
WeightedTargetTypeDef = TypedDict(
    "WeightedTargetTypeDef",
    {
        "virtualNode": str,
        "weight": int,
        "port": NotRequired[int],
    },
)
HealthCheckPolicyTypeDef = TypedDict(
    "HealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": PortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
        "path": NotRequired[str],
        "port": NotRequired[int],
    },
)
HttpPathMatchTypeDef = TypedDict(
    "HttpPathMatchTypeDef",
    {
        "exact": NotRequired[str],
        "regex": NotRequired[str],
    },
)
HttpGatewayRoutePathRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePathRewriteTypeDef",
    {
        "exact": NotRequired[str],
    },
)
HttpGatewayRoutePrefixRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePrefixRewriteTypeDef",
    {
        "defaultPrefix": NotRequired[DefaultGatewayRouteRewriteType],
        "value": NotRequired[str],
    },
)
QueryParameterMatchTypeDef = TypedDict(
    "QueryParameterMatchTypeDef",
    {
        "exact": NotRequired[str],
    },
)
JsonFormatRefTypeDef = TypedDict(
    "JsonFormatRefTypeDef",
    {
        "key": str,
        "value": str,
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
ListGatewayRoutesInputRequestTypeDef = TypedDict(
    "ListGatewayRoutesInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListMeshesInputRequestTypeDef = TypedDict(
    "ListMeshesInputRequestTypeDef",
    {
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
MeshRefTypeDef = TypedDict(
    "MeshRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
    },
)
ListRoutesInputRequestTypeDef = TypedDict(
    "ListRoutesInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
RouteRefTypeDef = TypedDict(
    "RouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "routeName": str,
        "version": int,
        "virtualRouterName": str,
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListVirtualGatewaysInputRequestTypeDef = TypedDict(
    "ListVirtualGatewaysInputRequestTypeDef",
    {
        "meshName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
VirtualGatewayRefTypeDef = TypedDict(
    "VirtualGatewayRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)
ListVirtualNodesInputRequestTypeDef = TypedDict(
    "ListVirtualNodesInputRequestTypeDef",
    {
        "meshName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
VirtualNodeRefTypeDef = TypedDict(
    "VirtualNodeRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualNodeName": str,
    },
)
ListVirtualRoutersInputRequestTypeDef = TypedDict(
    "ListVirtualRoutersInputRequestTypeDef",
    {
        "meshName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
VirtualRouterRefTypeDef = TypedDict(
    "VirtualRouterRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualRouterName": str,
    },
)
ListVirtualServicesInputRequestTypeDef = TypedDict(
    "ListVirtualServicesInputRequestTypeDef",
    {
        "meshName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
VirtualServiceRefTypeDef = TypedDict(
    "VirtualServiceRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualServiceName": str,
    },
)
PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "port": int,
        "protocol": PortProtocolType,
    },
)
ListenerTlsAcmCertificateTypeDef = TypedDict(
    "ListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)
TlsValidationContextFileTrustTypeDef = TypedDict(
    "TlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)
TlsValidationContextSdsTrustTypeDef = TypedDict(
    "TlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)
MeshStatusTypeDef = TypedDict(
    "MeshStatusTypeDef",
    {
        "status": NotRequired[MeshStatusCodeType],
    },
)
MeshServiceDiscoveryTypeDef = TypedDict(
    "MeshServiceDiscoveryTypeDef",
    {
        "ipPreference": NotRequired[IpPreferenceType],
    },
)
RouteStatusTypeDef = TypedDict(
    "RouteStatusTypeDef",
    {
        "status": RouteStatusCodeType,
    },
)
SubjectAlternativeNameMatchersOutputTypeDef = TypedDict(
    "SubjectAlternativeNameMatchersOutputTypeDef",
    {
        "exact": List[str],
    },
)
SubjectAlternativeNameMatchersTypeDef = TypedDict(
    "SubjectAlternativeNameMatchersTypeDef",
    {
        "exact": Sequence[str],
    },
)
TcpRouteMatchTypeDef = TypedDict(
    "TcpRouteMatchTypeDef",
    {
        "port": NotRequired[int],
    },
)
TlsValidationContextAcmTrustOutputTypeDef = TypedDict(
    "TlsValidationContextAcmTrustOutputTypeDef",
    {
        "certificateAuthorityArns": List[str],
    },
)
TlsValidationContextAcmTrustTypeDef = TypedDict(
    "TlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": Sequence[str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
VirtualGatewayListenerTlsFileCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)
VirtualGatewayListenerTlsSdsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)
VirtualGatewayGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)
VirtualGatewayHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)
VirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
        "maxPendingRequests": NotRequired[int],
    },
)
VirtualGatewayStatusTypeDef = TypedDict(
    "VirtualGatewayStatusTypeDef",
    {
        "status": VirtualGatewayStatusCodeType,
    },
)
VirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "VirtualGatewayHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": VirtualGatewayPortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
        "path": NotRequired[str],
        "port": NotRequired[int],
    },
)
VirtualGatewayPortMappingTypeDef = TypedDict(
    "VirtualGatewayPortMappingTypeDef",
    {
        "port": int,
        "protocol": VirtualGatewayPortProtocolType,
    },
)
VirtualGatewayListenerTlsAcmCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)
VirtualGatewayTlsValidationContextFileTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)
VirtualGatewayTlsValidationContextSdsTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)
VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef",
    {
        "certificateAuthorityArns": List[str],
    },
)
VirtualGatewayTlsValidationContextAcmTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": Sequence[str],
    },
)
VirtualNodeGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualNodeGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)
VirtualNodeHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)
VirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "VirtualNodeHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
        "maxPendingRequests": NotRequired[int],
    },
)
VirtualNodeTcpConnectionPoolTypeDef = TypedDict(
    "VirtualNodeTcpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)
VirtualNodeStatusTypeDef = TypedDict(
    "VirtualNodeStatusTypeDef",
    {
        "status": VirtualNodeStatusCodeType,
    },
)
VirtualNodeServiceProviderTypeDef = TypedDict(
    "VirtualNodeServiceProviderTypeDef",
    {
        "virtualNodeName": str,
    },
)
VirtualRouterStatusTypeDef = TypedDict(
    "VirtualRouterStatusTypeDef",
    {
        "status": VirtualRouterStatusCodeType,
    },
)
VirtualRouterServiceProviderTypeDef = TypedDict(
    "VirtualRouterServiceProviderTypeDef",
    {
        "virtualRouterName": str,
    },
)
VirtualServiceStatusTypeDef = TypedDict(
    "VirtualServiceStatusTypeDef",
    {
        "status": VirtualServiceStatusCodeType,
    },
)
AwsCloudMapServiceDiscoveryOutputTypeDef = TypedDict(
    "AwsCloudMapServiceDiscoveryOutputTypeDef",
    {
        "namespaceName": str,
        "serviceName": str,
        "attributes": NotRequired[List[AwsCloudMapInstanceAttributeTypeDef]],
        "ipPreference": NotRequired[IpPreferenceType],
    },
)
AwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "AwsCloudMapServiceDiscoveryTypeDef",
    {
        "namespaceName": str,
        "serviceName": str,
        "attributes": NotRequired[Sequence[AwsCloudMapInstanceAttributeTypeDef]],
        "ipPreference": NotRequired[IpPreferenceType],
    },
)
ClientTlsCertificateTypeDef = TypedDict(
    "ClientTlsCertificateTypeDef",
    {
        "file": NotRequired[ListenerTlsFileCertificateTypeDef],
        "sds": NotRequired[ListenerTlsSdsCertificateTypeDef],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagRefTypeDef],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "nextToken": str,
        "tags": List[TagRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GrpcRetryPolicyOutputTypeDef = TypedDict(
    "GrpcRetryPolicyOutputTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": DurationTypeDef,
        "grpcRetryEvents": NotRequired[List[GrpcRetryPolicyEventType]],
        "httpRetryEvents": NotRequired[List[str]],
        "tcpRetryEvents": NotRequired[List[Literal["connection-error"]]],
    },
)
GrpcRetryPolicyTypeDef = TypedDict(
    "GrpcRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": DurationTypeDef,
        "grpcRetryEvents": NotRequired[Sequence[GrpcRetryPolicyEventType]],
        "httpRetryEvents": NotRequired[Sequence[str]],
        "tcpRetryEvents": NotRequired[Sequence[Literal["connection-error"]]],
    },
)
GrpcTimeoutTypeDef = TypedDict(
    "GrpcTimeoutTypeDef",
    {
        "idle": NotRequired[DurationTypeDef],
        "perRequest": NotRequired[DurationTypeDef],
    },
)
HttpRetryPolicyOutputTypeDef = TypedDict(
    "HttpRetryPolicyOutputTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": DurationTypeDef,
        "httpRetryEvents": NotRequired[List[str]],
        "tcpRetryEvents": NotRequired[List[Literal["connection-error"]]],
    },
)
HttpRetryPolicyTypeDef = TypedDict(
    "HttpRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": DurationTypeDef,
        "httpRetryEvents": NotRequired[Sequence[str]],
        "tcpRetryEvents": NotRequired[Sequence[Literal["connection-error"]]],
    },
)
HttpTimeoutTypeDef = TypedDict(
    "HttpTimeoutTypeDef",
    {
        "idle": NotRequired[DurationTypeDef],
        "perRequest": NotRequired[DurationTypeDef],
    },
)
OutlierDetectionTypeDef = TypedDict(
    "OutlierDetectionTypeDef",
    {
        "baseEjectionDuration": DurationTypeDef,
        "interval": DurationTypeDef,
        "maxEjectionPercent": int,
        "maxServerErrors": int,
    },
)
TcpTimeoutTypeDef = TypedDict(
    "TcpTimeoutTypeDef",
    {
        "idle": NotRequired[DurationTypeDef],
    },
)
GrpcGatewayRouteRewriteTypeDef = TypedDict(
    "GrpcGatewayRouteRewriteTypeDef",
    {
        "hostname": NotRequired[GatewayRouteHostnameRewriteTypeDef],
    },
)
ListGatewayRoutesOutputTypeDef = TypedDict(
    "ListGatewayRoutesOutputTypeDef",
    {
        "gatewayRoutes": List[GatewayRouteRefTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GatewayRouteTargetTypeDef = TypedDict(
    "GatewayRouteTargetTypeDef",
    {
        "virtualService": GatewayRouteVirtualServiceTypeDef,
        "port": NotRequired[int],
    },
)
GrpcMetadataMatchMethodTypeDef = TypedDict(
    "GrpcMetadataMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired[MatchRangeTypeDef],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)
GrpcRouteMetadataMatchMethodTypeDef = TypedDict(
    "GrpcRouteMetadataMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired[MatchRangeTypeDef],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)
HeaderMatchMethodTypeDef = TypedDict(
    "HeaderMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired[MatchRangeTypeDef],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)
GrpcRouteActionOutputTypeDef = TypedDict(
    "GrpcRouteActionOutputTypeDef",
    {
        "weightedTargets": List[WeightedTargetTypeDef],
    },
)
GrpcRouteActionTypeDef = TypedDict(
    "GrpcRouteActionTypeDef",
    {
        "weightedTargets": Sequence[WeightedTargetTypeDef],
    },
)
HttpRouteActionOutputTypeDef = TypedDict(
    "HttpRouteActionOutputTypeDef",
    {
        "weightedTargets": List[WeightedTargetTypeDef],
    },
)
HttpRouteActionTypeDef = TypedDict(
    "HttpRouteActionTypeDef",
    {
        "weightedTargets": Sequence[WeightedTargetTypeDef],
    },
)
TcpRouteActionOutputTypeDef = TypedDict(
    "TcpRouteActionOutputTypeDef",
    {
        "weightedTargets": List[WeightedTargetTypeDef],
    },
)
TcpRouteActionTypeDef = TypedDict(
    "TcpRouteActionTypeDef",
    {
        "weightedTargets": Sequence[WeightedTargetTypeDef],
    },
)
HttpGatewayRouteRewriteTypeDef = TypedDict(
    "HttpGatewayRouteRewriteTypeDef",
    {
        "hostname": NotRequired[GatewayRouteHostnameRewriteTypeDef],
        "path": NotRequired[HttpGatewayRoutePathRewriteTypeDef],
        "prefix": NotRequired[HttpGatewayRoutePrefixRewriteTypeDef],
    },
)
HttpQueryParameterTypeDef = TypedDict(
    "HttpQueryParameterTypeDef",
    {
        "name": str,
        "match": NotRequired[QueryParameterMatchTypeDef],
    },
)
LoggingFormatOutputTypeDef = TypedDict(
    "LoggingFormatOutputTypeDef",
    {
        "json": NotRequired[List[JsonFormatRefTypeDef]],
        "text": NotRequired[str],
    },
)
LoggingFormatTypeDef = TypedDict(
    "LoggingFormatTypeDef",
    {
        "json": NotRequired[Sequence[JsonFormatRefTypeDef]],
        "text": NotRequired[str],
    },
)
ListGatewayRoutesInputListGatewayRoutesPaginateTypeDef = TypedDict(
    "ListGatewayRoutesInputListGatewayRoutesPaginateTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMeshesInputListMeshesPaginateTypeDef = TypedDict(
    "ListMeshesInputListMeshesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRoutesInputListRoutesPaginateTypeDef = TypedDict(
    "ListRoutesInputListRoutesPaginateTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceInputListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    {
        "resourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef = TypedDict(
    "ListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef",
    {
        "meshName": str,
        "meshOwner": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVirtualNodesInputListVirtualNodesPaginateTypeDef = TypedDict(
    "ListVirtualNodesInputListVirtualNodesPaginateTypeDef",
    {
        "meshName": str,
        "meshOwner": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVirtualRoutersInputListVirtualRoutersPaginateTypeDef = TypedDict(
    "ListVirtualRoutersInputListVirtualRoutersPaginateTypeDef",
    {
        "meshName": str,
        "meshOwner": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVirtualServicesInputListVirtualServicesPaginateTypeDef = TypedDict(
    "ListVirtualServicesInputListVirtualServicesPaginateTypeDef",
    {
        "meshName": str,
        "meshOwner": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMeshesOutputTypeDef = TypedDict(
    "ListMeshesOutputTypeDef",
    {
        "meshes": List[MeshRefTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRoutesOutputTypeDef = TypedDict(
    "ListRoutesOutputTypeDef",
    {
        "nextToken": str,
        "routes": List[RouteRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVirtualGatewaysOutputTypeDef = TypedDict(
    "ListVirtualGatewaysOutputTypeDef",
    {
        "nextToken": str,
        "virtualGateways": List[VirtualGatewayRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVirtualNodesOutputTypeDef = TypedDict(
    "ListVirtualNodesOutputTypeDef",
    {
        "nextToken": str,
        "virtualNodes": List[VirtualNodeRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVirtualRoutersOutputTypeDef = TypedDict(
    "ListVirtualRoutersOutputTypeDef",
    {
        "nextToken": str,
        "virtualRouters": List[VirtualRouterRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVirtualServicesOutputTypeDef = TypedDict(
    "ListVirtualServicesOutputTypeDef",
    {
        "nextToken": str,
        "virtualServices": List[VirtualServiceRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VirtualRouterListenerTypeDef = TypedDict(
    "VirtualRouterListenerTypeDef",
    {
        "portMapping": PortMappingTypeDef,
    },
)
ListenerTlsCertificateTypeDef = TypedDict(
    "ListenerTlsCertificateTypeDef",
    {
        "acm": NotRequired[ListenerTlsAcmCertificateTypeDef],
        "file": NotRequired[ListenerTlsFileCertificateTypeDef],
        "sds": NotRequired[ListenerTlsSdsCertificateTypeDef],
    },
)
ListenerTlsValidationContextTrustTypeDef = TypedDict(
    "ListenerTlsValidationContextTrustTypeDef",
    {
        "file": NotRequired[TlsValidationContextFileTrustTypeDef],
        "sds": NotRequired[TlsValidationContextSdsTrustTypeDef],
    },
)
MeshSpecTypeDef = TypedDict(
    "MeshSpecTypeDef",
    {
        "egressFilter": NotRequired[EgressFilterTypeDef],
        "serviceDiscovery": NotRequired[MeshServiceDiscoveryTypeDef],
    },
)
SubjectAlternativeNamesOutputTypeDef = TypedDict(
    "SubjectAlternativeNamesOutputTypeDef",
    {
        "match": SubjectAlternativeNameMatchersOutputTypeDef,
    },
)
SubjectAlternativeNameMatchersUnionTypeDef = Union[
    SubjectAlternativeNameMatchersTypeDef, SubjectAlternativeNameMatchersOutputTypeDef
]
TlsValidationContextTrustOutputTypeDef = TypedDict(
    "TlsValidationContextTrustOutputTypeDef",
    {
        "acm": NotRequired[TlsValidationContextAcmTrustOutputTypeDef],
        "file": NotRequired[TlsValidationContextFileTrustTypeDef],
        "sds": NotRequired[TlsValidationContextSdsTrustTypeDef],
    },
)
TlsValidationContextAcmTrustUnionTypeDef = Union[
    TlsValidationContextAcmTrustTypeDef, TlsValidationContextAcmTrustOutputTypeDef
]
VirtualGatewayClientTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayClientTlsCertificateTypeDef",
    {
        "file": NotRequired[VirtualGatewayListenerTlsFileCertificateTypeDef],
        "sds": NotRequired[VirtualGatewayListenerTlsSdsCertificateTypeDef],
    },
)
VirtualGatewayConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayConnectionPoolTypeDef",
    {
        "grpc": NotRequired[VirtualGatewayGrpcConnectionPoolTypeDef],
        "http": NotRequired[VirtualGatewayHttpConnectionPoolTypeDef],
        "http2": NotRequired[VirtualGatewayHttp2ConnectionPoolTypeDef],
    },
)
VirtualGatewayListenerTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsCertificateTypeDef",
    {
        "acm": NotRequired[VirtualGatewayListenerTlsAcmCertificateTypeDef],
        "file": NotRequired[VirtualGatewayListenerTlsFileCertificateTypeDef],
        "sds": NotRequired[VirtualGatewayListenerTlsSdsCertificateTypeDef],
    },
)
VirtualGatewayListenerTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    {
        "file": NotRequired[VirtualGatewayTlsValidationContextFileTrustTypeDef],
        "sds": NotRequired[VirtualGatewayTlsValidationContextSdsTrustTypeDef],
    },
)
VirtualGatewayTlsValidationContextTrustOutputTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTrustOutputTypeDef",
    {
        "acm": NotRequired[VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef],
        "file": NotRequired[VirtualGatewayTlsValidationContextFileTrustTypeDef],
        "sds": NotRequired[VirtualGatewayTlsValidationContextSdsTrustTypeDef],
    },
)
VirtualGatewayTlsValidationContextAcmTrustUnionTypeDef = Union[
    VirtualGatewayTlsValidationContextAcmTrustTypeDef,
    VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef,
]
VirtualNodeConnectionPoolTypeDef = TypedDict(
    "VirtualNodeConnectionPoolTypeDef",
    {
        "grpc": NotRequired[VirtualNodeGrpcConnectionPoolTypeDef],
        "http": NotRequired[VirtualNodeHttpConnectionPoolTypeDef],
        "http2": NotRequired[VirtualNodeHttp2ConnectionPoolTypeDef],
        "tcp": NotRequired[VirtualNodeTcpConnectionPoolTypeDef],
    },
)
VirtualServiceProviderTypeDef = TypedDict(
    "VirtualServiceProviderTypeDef",
    {
        "virtualNode": NotRequired[VirtualNodeServiceProviderTypeDef],
        "virtualRouter": NotRequired[VirtualRouterServiceProviderTypeDef],
    },
)
ServiceDiscoveryOutputTypeDef = TypedDict(
    "ServiceDiscoveryOutputTypeDef",
    {
        "awsCloudMap": NotRequired[AwsCloudMapServiceDiscoveryOutputTypeDef],
        "dns": NotRequired[DnsServiceDiscoveryTypeDef],
    },
)
AwsCloudMapServiceDiscoveryUnionTypeDef = Union[
    AwsCloudMapServiceDiscoveryTypeDef, AwsCloudMapServiceDiscoveryOutputTypeDef
]
GrpcRetryPolicyUnionTypeDef = Union[GrpcRetryPolicyTypeDef, GrpcRetryPolicyOutputTypeDef]
HttpRetryPolicyUnionTypeDef = Union[HttpRetryPolicyTypeDef, HttpRetryPolicyOutputTypeDef]
ListenerTimeoutTypeDef = TypedDict(
    "ListenerTimeoutTypeDef",
    {
        "grpc": NotRequired[GrpcTimeoutTypeDef],
        "http": NotRequired[HttpTimeoutTypeDef],
        "http2": NotRequired[HttpTimeoutTypeDef],
        "tcp": NotRequired[TcpTimeoutTypeDef],
    },
)
GrpcGatewayRouteActionTypeDef = TypedDict(
    "GrpcGatewayRouteActionTypeDef",
    {
        "target": GatewayRouteTargetTypeDef,
        "rewrite": NotRequired[GrpcGatewayRouteRewriteTypeDef],
    },
)
GrpcGatewayRouteMetadataTypeDef = TypedDict(
    "GrpcGatewayRouteMetadataTypeDef",
    {
        "name": str,
        "invert": NotRequired[bool],
        "match": NotRequired[GrpcMetadataMatchMethodTypeDef],
    },
)
GrpcRouteMetadataTypeDef = TypedDict(
    "GrpcRouteMetadataTypeDef",
    {
        "name": str,
        "invert": NotRequired[bool],
        "match": NotRequired[GrpcRouteMetadataMatchMethodTypeDef],
    },
)
HttpGatewayRouteHeaderTypeDef = TypedDict(
    "HttpGatewayRouteHeaderTypeDef",
    {
        "name": str,
        "invert": NotRequired[bool],
        "match": NotRequired[HeaderMatchMethodTypeDef],
    },
)
HttpRouteHeaderTypeDef = TypedDict(
    "HttpRouteHeaderTypeDef",
    {
        "name": str,
        "invert": NotRequired[bool],
        "match": NotRequired[HeaderMatchMethodTypeDef],
    },
)
GrpcRouteActionUnionTypeDef = Union[GrpcRouteActionTypeDef, GrpcRouteActionOutputTypeDef]
HttpRouteActionUnionTypeDef = Union[HttpRouteActionTypeDef, HttpRouteActionOutputTypeDef]
TcpRouteOutputTypeDef = TypedDict(
    "TcpRouteOutputTypeDef",
    {
        "action": TcpRouteActionOutputTypeDef,
        "match": NotRequired[TcpRouteMatchTypeDef],
        "timeout": NotRequired[TcpTimeoutTypeDef],
    },
)
TcpRouteActionUnionTypeDef = Union[TcpRouteActionTypeDef, TcpRouteActionOutputTypeDef]
HttpGatewayRouteActionTypeDef = TypedDict(
    "HttpGatewayRouteActionTypeDef",
    {
        "target": GatewayRouteTargetTypeDef,
        "rewrite": NotRequired[HttpGatewayRouteRewriteTypeDef],
    },
)
FileAccessLogOutputTypeDef = TypedDict(
    "FileAccessLogOutputTypeDef",
    {
        "path": str,
        "format": NotRequired[LoggingFormatOutputTypeDef],
    },
)
VirtualGatewayFileAccessLogOutputTypeDef = TypedDict(
    "VirtualGatewayFileAccessLogOutputTypeDef",
    {
        "path": str,
        "format": NotRequired[LoggingFormatOutputTypeDef],
    },
)
LoggingFormatUnionTypeDef = Union[LoggingFormatTypeDef, LoggingFormatOutputTypeDef]
VirtualRouterSpecOutputTypeDef = TypedDict(
    "VirtualRouterSpecOutputTypeDef",
    {
        "listeners": NotRequired[List[VirtualRouterListenerTypeDef]],
    },
)
VirtualRouterSpecTypeDef = TypedDict(
    "VirtualRouterSpecTypeDef",
    {
        "listeners": NotRequired[Sequence[VirtualRouterListenerTypeDef]],
    },
)
CreateMeshInputRequestTypeDef = TypedDict(
    "CreateMeshInputRequestTypeDef",
    {
        "meshName": str,
        "clientToken": NotRequired[str],
        "spec": NotRequired[MeshSpecTypeDef],
        "tags": NotRequired[Sequence[TagRefTypeDef]],
    },
)
MeshDataTypeDef = TypedDict(
    "MeshDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": MeshSpecTypeDef,
        "status": MeshStatusTypeDef,
    },
)
UpdateMeshInputRequestTypeDef = TypedDict(
    "UpdateMeshInputRequestTypeDef",
    {
        "meshName": str,
        "clientToken": NotRequired[str],
        "spec": NotRequired[MeshSpecTypeDef],
    },
)
ListenerTlsValidationContextOutputTypeDef = TypedDict(
    "ListenerTlsValidationContextOutputTypeDef",
    {
        "trust": ListenerTlsValidationContextTrustTypeDef,
        "subjectAlternativeNames": NotRequired[SubjectAlternativeNamesOutputTypeDef],
    },
)
SubjectAlternativeNamesTypeDef = TypedDict(
    "SubjectAlternativeNamesTypeDef",
    {
        "match": SubjectAlternativeNameMatchersUnionTypeDef,
    },
)
TlsValidationContextOutputTypeDef = TypedDict(
    "TlsValidationContextOutputTypeDef",
    {
        "trust": TlsValidationContextTrustOutputTypeDef,
        "subjectAlternativeNames": NotRequired[SubjectAlternativeNamesOutputTypeDef],
    },
)
TlsValidationContextTrustTypeDef = TypedDict(
    "TlsValidationContextTrustTypeDef",
    {
        "acm": NotRequired[TlsValidationContextAcmTrustUnionTypeDef],
        "file": NotRequired[TlsValidationContextFileTrustTypeDef],
        "sds": NotRequired[TlsValidationContextSdsTrustTypeDef],
    },
)
VirtualGatewayListenerTlsValidationContextOutputTypeDef = TypedDict(
    "VirtualGatewayListenerTlsValidationContextOutputTypeDef",
    {
        "trust": VirtualGatewayListenerTlsValidationContextTrustTypeDef,
        "subjectAlternativeNames": NotRequired[SubjectAlternativeNamesOutputTypeDef],
    },
)
VirtualGatewayTlsValidationContextOutputTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextOutputTypeDef",
    {
        "trust": VirtualGatewayTlsValidationContextTrustOutputTypeDef,
        "subjectAlternativeNames": NotRequired[SubjectAlternativeNamesOutputTypeDef],
    },
)
VirtualGatewayTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    {
        "acm": NotRequired[VirtualGatewayTlsValidationContextAcmTrustUnionTypeDef],
        "file": NotRequired[VirtualGatewayTlsValidationContextFileTrustTypeDef],
        "sds": NotRequired[VirtualGatewayTlsValidationContextSdsTrustTypeDef],
    },
)
VirtualServiceSpecTypeDef = TypedDict(
    "VirtualServiceSpecTypeDef",
    {
        "provider": NotRequired[VirtualServiceProviderTypeDef],
    },
)
ServiceDiscoveryTypeDef = TypedDict(
    "ServiceDiscoveryTypeDef",
    {
        "awsCloudMap": NotRequired[AwsCloudMapServiceDiscoveryUnionTypeDef],
        "dns": NotRequired[DnsServiceDiscoveryTypeDef],
    },
)
GrpcGatewayRouteMatchOutputTypeDef = TypedDict(
    "GrpcGatewayRouteMatchOutputTypeDef",
    {
        "hostname": NotRequired[GatewayRouteHostnameMatchTypeDef],
        "metadata": NotRequired[List[GrpcGatewayRouteMetadataTypeDef]],
        "port": NotRequired[int],
        "serviceName": NotRequired[str],
    },
)
GrpcGatewayRouteMatchTypeDef = TypedDict(
    "GrpcGatewayRouteMatchTypeDef",
    {
        "hostname": NotRequired[GatewayRouteHostnameMatchTypeDef],
        "metadata": NotRequired[Sequence[GrpcGatewayRouteMetadataTypeDef]],
        "port": NotRequired[int],
        "serviceName": NotRequired[str],
    },
)
GrpcRouteMatchOutputTypeDef = TypedDict(
    "GrpcRouteMatchOutputTypeDef",
    {
        "metadata": NotRequired[List[GrpcRouteMetadataTypeDef]],
        "methodName": NotRequired[str],
        "port": NotRequired[int],
        "serviceName": NotRequired[str],
    },
)
GrpcRouteMatchTypeDef = TypedDict(
    "GrpcRouteMatchTypeDef",
    {
        "metadata": NotRequired[Sequence[GrpcRouteMetadataTypeDef]],
        "methodName": NotRequired[str],
        "port": NotRequired[int],
        "serviceName": NotRequired[str],
    },
)
HttpGatewayRouteMatchOutputTypeDef = TypedDict(
    "HttpGatewayRouteMatchOutputTypeDef",
    {
        "headers": NotRequired[List[HttpGatewayRouteHeaderTypeDef]],
        "hostname": NotRequired[GatewayRouteHostnameMatchTypeDef],
        "method": NotRequired[HttpMethodType],
        "path": NotRequired[HttpPathMatchTypeDef],
        "port": NotRequired[int],
        "prefix": NotRequired[str],
        "queryParameters": NotRequired[List[HttpQueryParameterTypeDef]],
    },
)
HttpGatewayRouteMatchTypeDef = TypedDict(
    "HttpGatewayRouteMatchTypeDef",
    {
        "headers": NotRequired[Sequence[HttpGatewayRouteHeaderTypeDef]],
        "hostname": NotRequired[GatewayRouteHostnameMatchTypeDef],
        "method": NotRequired[HttpMethodType],
        "path": NotRequired[HttpPathMatchTypeDef],
        "port": NotRequired[int],
        "prefix": NotRequired[str],
        "queryParameters": NotRequired[Sequence[HttpQueryParameterTypeDef]],
    },
)
HttpRouteMatchOutputTypeDef = TypedDict(
    "HttpRouteMatchOutputTypeDef",
    {
        "headers": NotRequired[List[HttpRouteHeaderTypeDef]],
        "method": NotRequired[HttpMethodType],
        "path": NotRequired[HttpPathMatchTypeDef],
        "port": NotRequired[int],
        "prefix": NotRequired[str],
        "queryParameters": NotRequired[List[HttpQueryParameterTypeDef]],
        "scheme": NotRequired[HttpSchemeType],
    },
)
HttpRouteMatchTypeDef = TypedDict(
    "HttpRouteMatchTypeDef",
    {
        "headers": NotRequired[Sequence[HttpRouteHeaderTypeDef]],
        "method": NotRequired[HttpMethodType],
        "path": NotRequired[HttpPathMatchTypeDef],
        "port": NotRequired[int],
        "prefix": NotRequired[str],
        "queryParameters": NotRequired[Sequence[HttpQueryParameterTypeDef]],
        "scheme": NotRequired[HttpSchemeType],
    },
)
TcpRouteTypeDef = TypedDict(
    "TcpRouteTypeDef",
    {
        "action": TcpRouteActionUnionTypeDef,
        "match": NotRequired[TcpRouteMatchTypeDef],
        "timeout": NotRequired[TcpTimeoutTypeDef],
    },
)
AccessLogOutputTypeDef = TypedDict(
    "AccessLogOutputTypeDef",
    {
        "file": NotRequired[FileAccessLogOutputTypeDef],
    },
)
VirtualGatewayAccessLogOutputTypeDef = TypedDict(
    "VirtualGatewayAccessLogOutputTypeDef",
    {
        "file": NotRequired[VirtualGatewayFileAccessLogOutputTypeDef],
    },
)
FileAccessLogTypeDef = TypedDict(
    "FileAccessLogTypeDef",
    {
        "path": str,
        "format": NotRequired[LoggingFormatUnionTypeDef],
    },
)
VirtualGatewayFileAccessLogTypeDef = TypedDict(
    "VirtualGatewayFileAccessLogTypeDef",
    {
        "path": str,
        "format": NotRequired[LoggingFormatUnionTypeDef],
    },
)
VirtualRouterDataTypeDef = TypedDict(
    "VirtualRouterDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": VirtualRouterSpecOutputTypeDef,
        "status": VirtualRouterStatusTypeDef,
        "virtualRouterName": str,
    },
)
CreateVirtualRouterInputRequestTypeDef = TypedDict(
    "CreateVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualRouterSpecTypeDef,
        "virtualRouterName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence[TagRefTypeDef]],
    },
)
UpdateVirtualRouterInputRequestTypeDef = TypedDict(
    "UpdateVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualRouterSpecTypeDef,
        "virtualRouterName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)
CreateMeshOutputTypeDef = TypedDict(
    "CreateMeshOutputTypeDef",
    {
        "mesh": MeshDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMeshOutputTypeDef = TypedDict(
    "DeleteMeshOutputTypeDef",
    {
        "mesh": MeshDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMeshOutputTypeDef = TypedDict(
    "DescribeMeshOutputTypeDef",
    {
        "mesh": MeshDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMeshOutputTypeDef = TypedDict(
    "UpdateMeshOutputTypeDef",
    {
        "mesh": MeshDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListenerTlsOutputTypeDef = TypedDict(
    "ListenerTlsOutputTypeDef",
    {
        "certificate": ListenerTlsCertificateTypeDef,
        "mode": ListenerTlsModeType,
        "validation": NotRequired[ListenerTlsValidationContextOutputTypeDef],
    },
)
SubjectAlternativeNamesUnionTypeDef = Union[
    SubjectAlternativeNamesTypeDef, SubjectAlternativeNamesOutputTypeDef
]
ClientPolicyTlsOutputTypeDef = TypedDict(
    "ClientPolicyTlsOutputTypeDef",
    {
        "validation": TlsValidationContextOutputTypeDef,
        "certificate": NotRequired[ClientTlsCertificateTypeDef],
        "enforce": NotRequired[bool],
        "ports": NotRequired[List[int]],
    },
)
TlsValidationContextTrustUnionTypeDef = Union[
    TlsValidationContextTrustTypeDef, TlsValidationContextTrustOutputTypeDef
]
VirtualGatewayListenerTlsOutputTypeDef = TypedDict(
    "VirtualGatewayListenerTlsOutputTypeDef",
    {
        "certificate": VirtualGatewayListenerTlsCertificateTypeDef,
        "mode": VirtualGatewayListenerTlsModeType,
        "validation": NotRequired[VirtualGatewayListenerTlsValidationContextOutputTypeDef],
    },
)
VirtualGatewayClientPolicyTlsOutputTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTlsOutputTypeDef",
    {
        "validation": VirtualGatewayTlsValidationContextOutputTypeDef,
        "certificate": NotRequired[VirtualGatewayClientTlsCertificateTypeDef],
        "enforce": NotRequired[bool],
        "ports": NotRequired[List[int]],
    },
)
VirtualGatewayTlsValidationContextTrustUnionTypeDef = Union[
    VirtualGatewayTlsValidationContextTrustTypeDef,
    VirtualGatewayTlsValidationContextTrustOutputTypeDef,
]
CreateVirtualServiceInputRequestTypeDef = TypedDict(
    "CreateVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualServiceSpecTypeDef,
        "virtualServiceName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence[TagRefTypeDef]],
    },
)
UpdateVirtualServiceInputRequestTypeDef = TypedDict(
    "UpdateVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualServiceSpecTypeDef,
        "virtualServiceName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)
VirtualServiceDataTypeDef = TypedDict(
    "VirtualServiceDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": VirtualServiceSpecTypeDef,
        "status": VirtualServiceStatusTypeDef,
        "virtualServiceName": str,
    },
)
ServiceDiscoveryUnionTypeDef = Union[ServiceDiscoveryTypeDef, ServiceDiscoveryOutputTypeDef]
GrpcGatewayRouteOutputTypeDef = TypedDict(
    "GrpcGatewayRouteOutputTypeDef",
    {
        "action": GrpcGatewayRouteActionTypeDef,
        "match": GrpcGatewayRouteMatchOutputTypeDef,
    },
)
GrpcGatewayRouteMatchUnionTypeDef = Union[
    GrpcGatewayRouteMatchTypeDef, GrpcGatewayRouteMatchOutputTypeDef
]
GrpcRouteOutputTypeDef = TypedDict(
    "GrpcRouteOutputTypeDef",
    {
        "action": GrpcRouteActionOutputTypeDef,
        "match": GrpcRouteMatchOutputTypeDef,
        "retryPolicy": NotRequired[GrpcRetryPolicyOutputTypeDef],
        "timeout": NotRequired[GrpcTimeoutTypeDef],
    },
)
GrpcRouteMatchUnionTypeDef = Union[GrpcRouteMatchTypeDef, GrpcRouteMatchOutputTypeDef]
HttpGatewayRouteOutputTypeDef = TypedDict(
    "HttpGatewayRouteOutputTypeDef",
    {
        "action": HttpGatewayRouteActionTypeDef,
        "match": HttpGatewayRouteMatchOutputTypeDef,
    },
)
HttpGatewayRouteMatchUnionTypeDef = Union[
    HttpGatewayRouteMatchTypeDef, HttpGatewayRouteMatchOutputTypeDef
]
HttpRouteOutputTypeDef = TypedDict(
    "HttpRouteOutputTypeDef",
    {
        "action": HttpRouteActionOutputTypeDef,
        "match": HttpRouteMatchOutputTypeDef,
        "retryPolicy": NotRequired[HttpRetryPolicyOutputTypeDef],
        "timeout": NotRequired[HttpTimeoutTypeDef],
    },
)
HttpRouteMatchUnionTypeDef = Union[HttpRouteMatchTypeDef, HttpRouteMatchOutputTypeDef]
TcpRouteUnionTypeDef = Union[TcpRouteTypeDef, TcpRouteOutputTypeDef]
LoggingOutputTypeDef = TypedDict(
    "LoggingOutputTypeDef",
    {
        "accessLog": NotRequired[AccessLogOutputTypeDef],
    },
)
VirtualGatewayLoggingOutputTypeDef = TypedDict(
    "VirtualGatewayLoggingOutputTypeDef",
    {
        "accessLog": NotRequired[VirtualGatewayAccessLogOutputTypeDef],
    },
)
FileAccessLogUnionTypeDef = Union[FileAccessLogTypeDef, FileAccessLogOutputTypeDef]
VirtualGatewayFileAccessLogUnionTypeDef = Union[
    VirtualGatewayFileAccessLogTypeDef, VirtualGatewayFileAccessLogOutputTypeDef
]
CreateVirtualRouterOutputTypeDef = TypedDict(
    "CreateVirtualRouterOutputTypeDef",
    {
        "virtualRouter": VirtualRouterDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVirtualRouterOutputTypeDef = TypedDict(
    "DeleteVirtualRouterOutputTypeDef",
    {
        "virtualRouter": VirtualRouterDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVirtualRouterOutputTypeDef = TypedDict(
    "DescribeVirtualRouterOutputTypeDef",
    {
        "virtualRouter": VirtualRouterDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVirtualRouterOutputTypeDef = TypedDict(
    "UpdateVirtualRouterOutputTypeDef",
    {
        "virtualRouter": VirtualRouterDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListenerOutputTypeDef = TypedDict(
    "ListenerOutputTypeDef",
    {
        "portMapping": PortMappingTypeDef,
        "connectionPool": NotRequired[VirtualNodeConnectionPoolTypeDef],
        "healthCheck": NotRequired[HealthCheckPolicyTypeDef],
        "outlierDetection": NotRequired[OutlierDetectionTypeDef],
        "timeout": NotRequired[ListenerTimeoutTypeDef],
        "tls": NotRequired[ListenerTlsOutputTypeDef],
    },
)
ListenerTlsValidationContextTypeDef = TypedDict(
    "ListenerTlsValidationContextTypeDef",
    {
        "trust": ListenerTlsValidationContextTrustTypeDef,
        "subjectAlternativeNames": NotRequired[SubjectAlternativeNamesUnionTypeDef],
    },
)
VirtualGatewayListenerTlsValidationContextTypeDef = TypedDict(
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    {
        "trust": VirtualGatewayListenerTlsValidationContextTrustTypeDef,
        "subjectAlternativeNames": NotRequired[SubjectAlternativeNamesUnionTypeDef],
    },
)
ClientPolicyOutputTypeDef = TypedDict(
    "ClientPolicyOutputTypeDef",
    {
        "tls": NotRequired[ClientPolicyTlsOutputTypeDef],
    },
)
TlsValidationContextTypeDef = TypedDict(
    "TlsValidationContextTypeDef",
    {
        "trust": TlsValidationContextTrustUnionTypeDef,
        "subjectAlternativeNames": NotRequired[SubjectAlternativeNamesUnionTypeDef],
    },
)
VirtualGatewayListenerOutputTypeDef = TypedDict(
    "VirtualGatewayListenerOutputTypeDef",
    {
        "portMapping": VirtualGatewayPortMappingTypeDef,
        "connectionPool": NotRequired[VirtualGatewayConnectionPoolTypeDef],
        "healthCheck": NotRequired[VirtualGatewayHealthCheckPolicyTypeDef],
        "tls": NotRequired[VirtualGatewayListenerTlsOutputTypeDef],
    },
)
VirtualGatewayClientPolicyOutputTypeDef = TypedDict(
    "VirtualGatewayClientPolicyOutputTypeDef",
    {
        "tls": NotRequired[VirtualGatewayClientPolicyTlsOutputTypeDef],
    },
)
VirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTypeDef",
    {
        "trust": VirtualGatewayTlsValidationContextTrustUnionTypeDef,
        "subjectAlternativeNames": NotRequired[SubjectAlternativeNamesUnionTypeDef],
    },
)
CreateVirtualServiceOutputTypeDef = TypedDict(
    "CreateVirtualServiceOutputTypeDef",
    {
        "virtualService": VirtualServiceDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVirtualServiceOutputTypeDef = TypedDict(
    "DeleteVirtualServiceOutputTypeDef",
    {
        "virtualService": VirtualServiceDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVirtualServiceOutputTypeDef = TypedDict(
    "DescribeVirtualServiceOutputTypeDef",
    {
        "virtualService": VirtualServiceDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVirtualServiceOutputTypeDef = TypedDict(
    "UpdateVirtualServiceOutputTypeDef",
    {
        "virtualService": VirtualServiceDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GrpcGatewayRouteTypeDef = TypedDict(
    "GrpcGatewayRouteTypeDef",
    {
        "action": GrpcGatewayRouteActionTypeDef,
        "match": GrpcGatewayRouteMatchUnionTypeDef,
    },
)
GrpcRouteTypeDef = TypedDict(
    "GrpcRouteTypeDef",
    {
        "action": GrpcRouteActionUnionTypeDef,
        "match": GrpcRouteMatchUnionTypeDef,
        "retryPolicy": NotRequired[GrpcRetryPolicyUnionTypeDef],
        "timeout": NotRequired[GrpcTimeoutTypeDef],
    },
)
GatewayRouteSpecOutputTypeDef = TypedDict(
    "GatewayRouteSpecOutputTypeDef",
    {
        "grpcRoute": NotRequired[GrpcGatewayRouteOutputTypeDef],
        "http2Route": NotRequired[HttpGatewayRouteOutputTypeDef],
        "httpRoute": NotRequired[HttpGatewayRouteOutputTypeDef],
        "priority": NotRequired[int],
    },
)
HttpGatewayRouteTypeDef = TypedDict(
    "HttpGatewayRouteTypeDef",
    {
        "action": HttpGatewayRouteActionTypeDef,
        "match": HttpGatewayRouteMatchUnionTypeDef,
    },
)
RouteSpecOutputTypeDef = TypedDict(
    "RouteSpecOutputTypeDef",
    {
        "grpcRoute": NotRequired[GrpcRouteOutputTypeDef],
        "http2Route": NotRequired[HttpRouteOutputTypeDef],
        "httpRoute": NotRequired[HttpRouteOutputTypeDef],
        "priority": NotRequired[int],
        "tcpRoute": NotRequired[TcpRouteOutputTypeDef],
    },
)
HttpRouteTypeDef = TypedDict(
    "HttpRouteTypeDef",
    {
        "action": HttpRouteActionUnionTypeDef,
        "match": HttpRouteMatchUnionTypeDef,
        "retryPolicy": NotRequired[HttpRetryPolicyUnionTypeDef],
        "timeout": NotRequired[HttpTimeoutTypeDef],
    },
)
AccessLogTypeDef = TypedDict(
    "AccessLogTypeDef",
    {
        "file": NotRequired[FileAccessLogUnionTypeDef],
    },
)
VirtualGatewayAccessLogTypeDef = TypedDict(
    "VirtualGatewayAccessLogTypeDef",
    {
        "file": NotRequired[VirtualGatewayFileAccessLogUnionTypeDef],
    },
)
ListenerTlsValidationContextUnionTypeDef = Union[
    ListenerTlsValidationContextTypeDef, ListenerTlsValidationContextOutputTypeDef
]
VirtualGatewayListenerTlsValidationContextUnionTypeDef = Union[
    VirtualGatewayListenerTlsValidationContextTypeDef,
    VirtualGatewayListenerTlsValidationContextOutputTypeDef,
]
BackendDefaultsOutputTypeDef = TypedDict(
    "BackendDefaultsOutputTypeDef",
    {
        "clientPolicy": NotRequired[ClientPolicyOutputTypeDef],
    },
)
VirtualServiceBackendOutputTypeDef = TypedDict(
    "VirtualServiceBackendOutputTypeDef",
    {
        "virtualServiceName": str,
        "clientPolicy": NotRequired[ClientPolicyOutputTypeDef],
    },
)
TlsValidationContextUnionTypeDef = Union[
    TlsValidationContextTypeDef, TlsValidationContextOutputTypeDef
]
VirtualGatewayBackendDefaultsOutputTypeDef = TypedDict(
    "VirtualGatewayBackendDefaultsOutputTypeDef",
    {
        "clientPolicy": NotRequired[VirtualGatewayClientPolicyOutputTypeDef],
    },
)
VirtualGatewayTlsValidationContextUnionTypeDef = Union[
    VirtualGatewayTlsValidationContextTypeDef, VirtualGatewayTlsValidationContextOutputTypeDef
]
GrpcGatewayRouteUnionTypeDef = Union[GrpcGatewayRouteTypeDef, GrpcGatewayRouteOutputTypeDef]
GrpcRouteUnionTypeDef = Union[GrpcRouteTypeDef, GrpcRouteOutputTypeDef]
GatewayRouteDataTypeDef = TypedDict(
    "GatewayRouteDataTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": GatewayRouteSpecOutputTypeDef,
        "status": GatewayRouteStatusTypeDef,
        "virtualGatewayName": str,
    },
)
HttpGatewayRouteUnionTypeDef = Union[HttpGatewayRouteTypeDef, HttpGatewayRouteOutputTypeDef]
RouteDataTypeDef = TypedDict(
    "RouteDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "routeName": str,
        "spec": RouteSpecOutputTypeDef,
        "status": RouteStatusTypeDef,
        "virtualRouterName": str,
    },
)
HttpRouteUnionTypeDef = Union[HttpRouteTypeDef, HttpRouteOutputTypeDef]
AccessLogUnionTypeDef = Union[AccessLogTypeDef, AccessLogOutputTypeDef]
VirtualGatewayAccessLogUnionTypeDef = Union[
    VirtualGatewayAccessLogTypeDef, VirtualGatewayAccessLogOutputTypeDef
]
ListenerTlsTypeDef = TypedDict(
    "ListenerTlsTypeDef",
    {
        "certificate": ListenerTlsCertificateTypeDef,
        "mode": ListenerTlsModeType,
        "validation": NotRequired[ListenerTlsValidationContextUnionTypeDef],
    },
)
VirtualGatewayListenerTlsTypeDef = TypedDict(
    "VirtualGatewayListenerTlsTypeDef",
    {
        "certificate": VirtualGatewayListenerTlsCertificateTypeDef,
        "mode": VirtualGatewayListenerTlsModeType,
        "validation": NotRequired[VirtualGatewayListenerTlsValidationContextUnionTypeDef],
    },
)
BackendOutputTypeDef = TypedDict(
    "BackendOutputTypeDef",
    {
        "virtualService": NotRequired[VirtualServiceBackendOutputTypeDef],
    },
)
ClientPolicyTlsTypeDef = TypedDict(
    "ClientPolicyTlsTypeDef",
    {
        "validation": TlsValidationContextUnionTypeDef,
        "certificate": NotRequired[ClientTlsCertificateTypeDef],
        "enforce": NotRequired[bool],
        "ports": NotRequired[Sequence[int]],
    },
)
VirtualGatewaySpecOutputTypeDef = TypedDict(
    "VirtualGatewaySpecOutputTypeDef",
    {
        "listeners": List[VirtualGatewayListenerOutputTypeDef],
        "backendDefaults": NotRequired[VirtualGatewayBackendDefaultsOutputTypeDef],
        "logging": NotRequired[VirtualGatewayLoggingOutputTypeDef],
    },
)
VirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTlsTypeDef",
    {
        "validation": VirtualGatewayTlsValidationContextUnionTypeDef,
        "certificate": NotRequired[VirtualGatewayClientTlsCertificateTypeDef],
        "enforce": NotRequired[bool],
        "ports": NotRequired[Sequence[int]],
    },
)
CreateGatewayRouteOutputTypeDef = TypedDict(
    "CreateGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": GatewayRouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGatewayRouteOutputTypeDef = TypedDict(
    "DeleteGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": GatewayRouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGatewayRouteOutputTypeDef = TypedDict(
    "DescribeGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": GatewayRouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGatewayRouteOutputTypeDef = TypedDict(
    "UpdateGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": GatewayRouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GatewayRouteSpecTypeDef = TypedDict(
    "GatewayRouteSpecTypeDef",
    {
        "grpcRoute": NotRequired[GrpcGatewayRouteUnionTypeDef],
        "http2Route": NotRequired[HttpGatewayRouteUnionTypeDef],
        "httpRoute": NotRequired[HttpGatewayRouteUnionTypeDef],
        "priority": NotRequired[int],
    },
)
CreateRouteOutputTypeDef = TypedDict(
    "CreateRouteOutputTypeDef",
    {
        "route": RouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRouteOutputTypeDef = TypedDict(
    "DeleteRouteOutputTypeDef",
    {
        "route": RouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRouteOutputTypeDef = TypedDict(
    "DescribeRouteOutputTypeDef",
    {
        "route": RouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRouteOutputTypeDef = TypedDict(
    "UpdateRouteOutputTypeDef",
    {
        "route": RouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RouteSpecTypeDef = TypedDict(
    "RouteSpecTypeDef",
    {
        "grpcRoute": NotRequired[GrpcRouteUnionTypeDef],
        "http2Route": NotRequired[HttpRouteUnionTypeDef],
        "httpRoute": NotRequired[HttpRouteUnionTypeDef],
        "priority": NotRequired[int],
        "tcpRoute": NotRequired[TcpRouteUnionTypeDef],
    },
)
LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "accessLog": NotRequired[AccessLogUnionTypeDef],
    },
)
VirtualGatewayLoggingTypeDef = TypedDict(
    "VirtualGatewayLoggingTypeDef",
    {
        "accessLog": NotRequired[VirtualGatewayAccessLogUnionTypeDef],
    },
)
ListenerTlsUnionTypeDef = Union[ListenerTlsTypeDef, ListenerTlsOutputTypeDef]
VirtualGatewayListenerTlsUnionTypeDef = Union[
    VirtualGatewayListenerTlsTypeDef, VirtualGatewayListenerTlsOutputTypeDef
]
VirtualNodeSpecOutputTypeDef = TypedDict(
    "VirtualNodeSpecOutputTypeDef",
    {
        "backendDefaults": NotRequired[BackendDefaultsOutputTypeDef],
        "backends": NotRequired[List[BackendOutputTypeDef]],
        "listeners": NotRequired[List[ListenerOutputTypeDef]],
        "logging": NotRequired[LoggingOutputTypeDef],
        "serviceDiscovery": NotRequired[ServiceDiscoveryOutputTypeDef],
    },
)
ClientPolicyTlsUnionTypeDef = Union[ClientPolicyTlsTypeDef, ClientPolicyTlsOutputTypeDef]
VirtualGatewayDataTypeDef = TypedDict(
    "VirtualGatewayDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": VirtualGatewaySpecOutputTypeDef,
        "status": VirtualGatewayStatusTypeDef,
        "virtualGatewayName": str,
    },
)
VirtualGatewayClientPolicyTlsUnionTypeDef = Union[
    VirtualGatewayClientPolicyTlsTypeDef, VirtualGatewayClientPolicyTlsOutputTypeDef
]
CreateGatewayRouteInputRequestTypeDef = TypedDict(
    "CreateGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": GatewayRouteSpecTypeDef,
        "virtualGatewayName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence[TagRefTypeDef]],
    },
)
UpdateGatewayRouteInputRequestTypeDef = TypedDict(
    "UpdateGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": GatewayRouteSpecTypeDef,
        "virtualGatewayName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)
CreateRouteInputRequestTypeDef = TypedDict(
    "CreateRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": RouteSpecTypeDef,
        "virtualRouterName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence[TagRefTypeDef]],
    },
)
UpdateRouteInputRequestTypeDef = TypedDict(
    "UpdateRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": RouteSpecTypeDef,
        "virtualRouterName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)
LoggingUnionTypeDef = Union[LoggingTypeDef, LoggingOutputTypeDef]
VirtualGatewayLoggingUnionTypeDef = Union[
    VirtualGatewayLoggingTypeDef, VirtualGatewayLoggingOutputTypeDef
]
ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "portMapping": PortMappingTypeDef,
        "connectionPool": NotRequired[VirtualNodeConnectionPoolTypeDef],
        "healthCheck": NotRequired[HealthCheckPolicyTypeDef],
        "outlierDetection": NotRequired[OutlierDetectionTypeDef],
        "timeout": NotRequired[ListenerTimeoutTypeDef],
        "tls": NotRequired[ListenerTlsUnionTypeDef],
    },
)
VirtualGatewayListenerTypeDef = TypedDict(
    "VirtualGatewayListenerTypeDef",
    {
        "portMapping": VirtualGatewayPortMappingTypeDef,
        "connectionPool": NotRequired[VirtualGatewayConnectionPoolTypeDef],
        "healthCheck": NotRequired[VirtualGatewayHealthCheckPolicyTypeDef],
        "tls": NotRequired[VirtualGatewayListenerTlsUnionTypeDef],
    },
)
VirtualNodeDataTypeDef = TypedDict(
    "VirtualNodeDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": VirtualNodeSpecOutputTypeDef,
        "status": VirtualNodeStatusTypeDef,
        "virtualNodeName": str,
    },
)
ClientPolicyTypeDef = TypedDict(
    "ClientPolicyTypeDef",
    {
        "tls": NotRequired[ClientPolicyTlsUnionTypeDef],
    },
)
CreateVirtualGatewayOutputTypeDef = TypedDict(
    "CreateVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": VirtualGatewayDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVirtualGatewayOutputTypeDef = TypedDict(
    "DeleteVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": VirtualGatewayDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVirtualGatewayOutputTypeDef = TypedDict(
    "DescribeVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": VirtualGatewayDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVirtualGatewayOutputTypeDef = TypedDict(
    "UpdateVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": VirtualGatewayDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VirtualGatewayClientPolicyTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTypeDef",
    {
        "tls": NotRequired[VirtualGatewayClientPolicyTlsUnionTypeDef],
    },
)
ListenerUnionTypeDef = Union[ListenerTypeDef, ListenerOutputTypeDef]
VirtualGatewayListenerUnionTypeDef = Union[
    VirtualGatewayListenerTypeDef, VirtualGatewayListenerOutputTypeDef
]
CreateVirtualNodeOutputTypeDef = TypedDict(
    "CreateVirtualNodeOutputTypeDef",
    {
        "virtualNode": VirtualNodeDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVirtualNodeOutputTypeDef = TypedDict(
    "DeleteVirtualNodeOutputTypeDef",
    {
        "virtualNode": VirtualNodeDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVirtualNodeOutputTypeDef = TypedDict(
    "DescribeVirtualNodeOutputTypeDef",
    {
        "virtualNode": VirtualNodeDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVirtualNodeOutputTypeDef = TypedDict(
    "UpdateVirtualNodeOutputTypeDef",
    {
        "virtualNode": VirtualNodeDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ClientPolicyUnionTypeDef = Union[ClientPolicyTypeDef, ClientPolicyOutputTypeDef]
VirtualGatewayClientPolicyUnionTypeDef = Union[
    VirtualGatewayClientPolicyTypeDef, VirtualGatewayClientPolicyOutputTypeDef
]
BackendDefaultsTypeDef = TypedDict(
    "BackendDefaultsTypeDef",
    {
        "clientPolicy": NotRequired[ClientPolicyUnionTypeDef],
    },
)
VirtualServiceBackendTypeDef = TypedDict(
    "VirtualServiceBackendTypeDef",
    {
        "virtualServiceName": str,
        "clientPolicy": NotRequired[ClientPolicyUnionTypeDef],
    },
)
VirtualGatewayBackendDefaultsTypeDef = TypedDict(
    "VirtualGatewayBackendDefaultsTypeDef",
    {
        "clientPolicy": NotRequired[VirtualGatewayClientPolicyUnionTypeDef],
    },
)
BackendDefaultsUnionTypeDef = Union[BackendDefaultsTypeDef, BackendDefaultsOutputTypeDef]
VirtualServiceBackendUnionTypeDef = Union[
    VirtualServiceBackendTypeDef, VirtualServiceBackendOutputTypeDef
]
VirtualGatewayBackendDefaultsUnionTypeDef = Union[
    VirtualGatewayBackendDefaultsTypeDef, VirtualGatewayBackendDefaultsOutputTypeDef
]
BackendTypeDef = TypedDict(
    "BackendTypeDef",
    {
        "virtualService": NotRequired[VirtualServiceBackendUnionTypeDef],
    },
)
VirtualGatewaySpecTypeDef = TypedDict(
    "VirtualGatewaySpecTypeDef",
    {
        "listeners": Sequence[VirtualGatewayListenerUnionTypeDef],
        "backendDefaults": NotRequired[VirtualGatewayBackendDefaultsUnionTypeDef],
        "logging": NotRequired[VirtualGatewayLoggingUnionTypeDef],
    },
)
BackendUnionTypeDef = Union[BackendTypeDef, BackendOutputTypeDef]
CreateVirtualGatewayInputRequestTypeDef = TypedDict(
    "CreateVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualGatewaySpecTypeDef,
        "virtualGatewayName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence[TagRefTypeDef]],
    },
)
UpdateVirtualGatewayInputRequestTypeDef = TypedDict(
    "UpdateVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualGatewaySpecTypeDef,
        "virtualGatewayName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)
VirtualNodeSpecTypeDef = TypedDict(
    "VirtualNodeSpecTypeDef",
    {
        "backendDefaults": NotRequired[BackendDefaultsUnionTypeDef],
        "backends": NotRequired[Sequence[BackendUnionTypeDef]],
        "listeners": NotRequired[Sequence[ListenerUnionTypeDef]],
        "logging": NotRequired[LoggingUnionTypeDef],
        "serviceDiscovery": NotRequired[ServiceDiscoveryUnionTypeDef],
    },
)
CreateVirtualNodeInputRequestTypeDef = TypedDict(
    "CreateVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualNodeSpecTypeDef,
        "virtualNodeName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence[TagRefTypeDef]],
    },
)
UpdateVirtualNodeInputRequestTypeDef = TypedDict(
    "UpdateVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualNodeSpecTypeDef,
        "virtualNodeName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)
