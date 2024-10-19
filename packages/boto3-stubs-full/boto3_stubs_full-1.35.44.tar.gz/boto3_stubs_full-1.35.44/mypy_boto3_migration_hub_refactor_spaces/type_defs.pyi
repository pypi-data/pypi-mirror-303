"""
Type annotations for migration-hub-refactor-spaces service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/type_defs/)

Usage::

    ```python
    from mypy_boto3_migration_hub_refactor_spaces.type_defs import ApiGatewayProxyConfigTypeDef

    data: ApiGatewayProxyConfigTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ApiGatewayEndpointTypeType,
    ApplicationStateType,
    EnvironmentStateType,
    ErrorCodeType,
    ErrorResourceTypeType,
    HttpMethodType,
    NetworkFabricTypeType,
    RouteActivationStateType,
    RouteStateType,
    RouteTypeType,
    ServiceEndpointTypeType,
    ServiceStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ApiGatewayProxyConfigTypeDef",
    "ApiGatewayProxyInputTypeDef",
    "ApiGatewayProxySummaryTypeDef",
    "ErrorResponseTypeDef",
    "ResponseMetadataTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "DefaultRouteInputTypeDef",
    "UriPathRouteInputTypeDef",
    "UriPathRouteInputOutputTypeDef",
    "LambdaEndpointInputTypeDef",
    "UrlEndpointInputTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRouteRequestRequestTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "EnvironmentVpcTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetRouteRequestRequestTypeDef",
    "GetServiceRequestRequestTypeDef",
    "LambdaEndpointConfigTypeDef",
    "UrlEndpointConfigTypeDef",
    "LambdaEndpointSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListEnvironmentVpcsRequestRequestTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListRoutesRequestRequestTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "UrlEndpointSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRouteRequestRequestTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "ApplicationSummaryTypeDef",
    "EnvironmentSummaryTypeDef",
    "RouteSummaryTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "DeleteApplicationResponseTypeDef",
    "DeleteEnvironmentResponseTypeDef",
    "DeleteRouteResponseTypeDef",
    "DeleteServiceResponseTypeDef",
    "GetApplicationResponseTypeDef",
    "GetEnvironmentResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetRouteResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateRouteResponseTypeDef",
    "CreateRouteRequestRequestTypeDef",
    "CreateRouteResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "ListEnvironmentVpcsResponseTypeDef",
    "GetServiceResponseTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListEnvironmentVpcsRequestListEnvironmentVpcsPaginateTypeDef",
    "ListEnvironmentsRequestListEnvironmentsPaginateTypeDef",
    "ListRoutesRequestListRoutesPaginateTypeDef",
    "ListServicesRequestListServicesPaginateTypeDef",
    "ServiceSummaryTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListRoutesResponseTypeDef",
    "ListServicesResponseTypeDef",
)

ApiGatewayProxyConfigTypeDef = TypedDict(
    "ApiGatewayProxyConfigTypeDef",
    {
        "ApiGatewayId": NotRequired[str],
        "EndpointType": NotRequired[ApiGatewayEndpointTypeType],
        "NlbArn": NotRequired[str],
        "NlbName": NotRequired[str],
        "ProxyUrl": NotRequired[str],
        "StageName": NotRequired[str],
        "VpcLinkId": NotRequired[str],
    },
)
ApiGatewayProxyInputTypeDef = TypedDict(
    "ApiGatewayProxyInputTypeDef",
    {
        "EndpointType": NotRequired[ApiGatewayEndpointTypeType],
        "StageName": NotRequired[str],
    },
)
ApiGatewayProxySummaryTypeDef = TypedDict(
    "ApiGatewayProxySummaryTypeDef",
    {
        "ApiGatewayId": NotRequired[str],
        "EndpointType": NotRequired[ApiGatewayEndpointTypeType],
        "NlbArn": NotRequired[str],
        "NlbName": NotRequired[str],
        "ProxyUrl": NotRequired[str],
        "StageName": NotRequired[str],
        "VpcLinkId": NotRequired[str],
    },
)
ErrorResponseTypeDef = TypedDict(
    "ErrorResponseTypeDef",
    {
        "AccountId": NotRequired[str],
        "AdditionalDetails": NotRequired[Dict[str, str]],
        "Code": NotRequired[ErrorCodeType],
        "Message": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
        "ResourceType": NotRequired[ErrorResourceTypeType],
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
CreateEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateEnvironmentRequestRequestTypeDef",
    {
        "Name": str,
        "NetworkFabricType": NetworkFabricTypeType,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DefaultRouteInputTypeDef = TypedDict(
    "DefaultRouteInputTypeDef",
    {
        "ActivationState": NotRequired[RouteActivationStateType],
    },
)
UriPathRouteInputTypeDef = TypedDict(
    "UriPathRouteInputTypeDef",
    {
        "ActivationState": RouteActivationStateType,
        "SourcePath": str,
        "AppendSourcePath": NotRequired[bool],
        "IncludeChildPaths": NotRequired[bool],
        "Methods": NotRequired[Sequence[HttpMethodType]],
    },
)
UriPathRouteInputOutputTypeDef = TypedDict(
    "UriPathRouteInputOutputTypeDef",
    {
        "ActivationState": RouteActivationStateType,
        "SourcePath": str,
        "AppendSourcePath": NotRequired[bool],
        "IncludeChildPaths": NotRequired[bool],
        "Methods": NotRequired[List[HttpMethodType]],
    },
)
LambdaEndpointInputTypeDef = TypedDict(
    "LambdaEndpointInputTypeDef",
    {
        "Arn": str,
    },
)
UrlEndpointInputTypeDef = TypedDict(
    "UrlEndpointInputTypeDef",
    {
        "Url": str,
        "HealthUrl": NotRequired[str],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
    },
)
DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
DeleteRouteRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteIdentifier": str,
    },
)
DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "ServiceIdentifier": str,
    },
)
EnvironmentVpcTypeDef = TypedDict(
    "EnvironmentVpcTypeDef",
    {
        "AccountId": NotRequired[str],
        "CidrBlocks": NotRequired[List[str]],
        "CreatedTime": NotRequired[datetime],
        "EnvironmentId": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "VpcId": NotRequired[str],
        "VpcName": NotRequired[str],
    },
)
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
    },
)
GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetRouteRequestRequestTypeDef = TypedDict(
    "GetRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteIdentifier": str,
    },
)
GetServiceRequestRequestTypeDef = TypedDict(
    "GetServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "ServiceIdentifier": str,
    },
)
LambdaEndpointConfigTypeDef = TypedDict(
    "LambdaEndpointConfigTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
UrlEndpointConfigTypeDef = TypedDict(
    "UrlEndpointConfigTypeDef",
    {
        "HealthUrl": NotRequired[str],
        "Url": NotRequired[str],
    },
)
LambdaEndpointSummaryTypeDef = TypedDict(
    "LambdaEndpointSummaryTypeDef",
    {
        "Arn": NotRequired[str],
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
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListEnvironmentVpcsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentVpcsRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRoutesRequestRequestTypeDef = TypedDict(
    "ListRoutesRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
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
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "Policy": str,
        "ResourceArn": str,
    },
)
UrlEndpointSummaryTypeDef = TypedDict(
    "UrlEndpointSummaryTypeDef",
    {
        "HealthUrl": NotRequired[str],
        "Url": NotRequired[str],
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
UpdateRouteRequestRequestTypeDef = TypedDict(
    "UpdateRouteRequestRequestTypeDef",
    {
        "ActivationState": RouteActivationStateType,
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteIdentifier": str,
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
        "Name": str,
        "ProxyType": Literal["API_GATEWAY"],
        "VpcId": str,
        "ApiGatewayProxy": NotRequired[ApiGatewayProxyInputTypeDef],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApiGatewayProxy": NotRequired[ApiGatewayProxySummaryTypeDef],
        "ApplicationId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedByAccountId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "EnvironmentId": NotRequired[str],
        "Error": NotRequired[ErrorResponseTypeDef],
        "LastUpdatedTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "ProxyType": NotRequired[Literal["API_GATEWAY"]],
        "State": NotRequired[ApplicationStateType],
        "Tags": NotRequired[Dict[str, str]],
        "VpcId": NotRequired[str],
    },
)
EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "Error": NotRequired[ErrorResponseTypeDef],
        "LastUpdatedTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "NetworkFabricType": NotRequired[NetworkFabricTypeType],
        "OwnerAccountId": NotRequired[str],
        "State": NotRequired[EnvironmentStateType],
        "Tags": NotRequired[Dict[str, str]],
        "TransitGatewayId": NotRequired[str],
    },
)
RouteSummaryTypeDef = TypedDict(
    "RouteSummaryTypeDef",
    {
        "AppendSourcePath": NotRequired[bool],
        "ApplicationId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedByAccountId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "EnvironmentId": NotRequired[str],
        "Error": NotRequired[ErrorResponseTypeDef],
        "IncludeChildPaths": NotRequired[bool],
        "LastUpdatedTime": NotRequired[datetime],
        "Methods": NotRequired[List[HttpMethodType]],
        "OwnerAccountId": NotRequired[str],
        "PathResourceToId": NotRequired[Dict[str, str]],
        "RouteId": NotRequired[str],
        "RouteType": NotRequired[RouteTypeType],
        "ServiceId": NotRequired[str],
        "SourcePath": NotRequired[str],
        "State": NotRequired[RouteStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApiGatewayProxy": ApiGatewayProxyInputTypeDef,
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ProxyType": Literal["API_GATEWAY"],
        "State": ApplicationStateType,
        "Tags": Dict[str, str],
        "VpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentResponseTypeDef = TypedDict(
    "CreateEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "Description": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "NetworkFabricType": NetworkFabricTypeType,
        "OwnerAccountId": str,
        "State": EnvironmentStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApplicationResponseTypeDef = TypedDict(
    "DeleteApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "State": ApplicationStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEnvironmentResponseTypeDef = TypedDict(
    "DeleteEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "State": EnvironmentStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRouteResponseTypeDef = TypedDict(
    "DeleteRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "LastUpdatedTime": datetime,
        "RouteId": str,
        "ServiceId": str,
        "State": RouteStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "ApiGatewayProxy": ApiGatewayProxyConfigTypeDef,
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "Error": ErrorResponseTypeDef,
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ProxyType": Literal["API_GATEWAY"],
        "State": ApplicationStateType,
        "Tags": Dict[str, str],
        "VpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentResponseTypeDef = TypedDict(
    "GetEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "Description": str,
        "EnvironmentId": str,
        "Error": ErrorResponseTypeDef,
        "LastUpdatedTime": datetime,
        "Name": str,
        "NetworkFabricType": NetworkFabricTypeType,
        "OwnerAccountId": str,
        "State": EnvironmentStateType,
        "Tags": Dict[str, str],
        "TransitGatewayId": str,
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
GetRouteResponseTypeDef = TypedDict(
    "GetRouteResponseTypeDef",
    {
        "AppendSourcePath": bool,
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "Error": ErrorResponseTypeDef,
        "IncludeChildPaths": bool,
        "LastUpdatedTime": datetime,
        "Methods": List[HttpMethodType],
        "OwnerAccountId": str,
        "PathResourceToId": Dict[str, str],
        "RouteId": str,
        "RouteType": RouteTypeType,
        "ServiceId": str,
        "SourcePath": str,
        "State": RouteStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRouteResponseTypeDef = TypedDict(
    "UpdateRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "LastUpdatedTime": datetime,
        "RouteId": str,
        "ServiceId": str,
        "State": RouteStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRouteRequestRequestTypeDef = TypedDict(
    "CreateRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteType": RouteTypeType,
        "ServiceIdentifier": str,
        "ClientToken": NotRequired[str],
        "DefaultRoute": NotRequired[DefaultRouteInputTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "UriPathRoute": NotRequired[UriPathRouteInputTypeDef],
    },
)
CreateRouteResponseTypeDef = TypedDict(
    "CreateRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "OwnerAccountId": str,
        "RouteId": str,
        "RouteType": RouteTypeType,
        "ServiceId": str,
        "State": RouteStateType,
        "Tags": Dict[str, str],
        "UriPathRoute": UriPathRouteInputOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceRequestRequestTypeDef = TypedDict(
    "CreateServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentIdentifier": str,
        "Name": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "LambdaEndpoint": NotRequired[LambdaEndpointInputTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "UrlEndpoint": NotRequired[UrlEndpointInputTypeDef],
        "VpcId": NotRequired[str],
    },
)
CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "Description": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentId": str,
        "LambdaEndpoint": LambdaEndpointInputTypeDef,
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "Tags": Dict[str, str],
        "UrlEndpoint": UrlEndpointInputTypeDef,
        "VpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentVpcsResponseTypeDef = TypedDict(
    "ListEnvironmentVpcsResponseTypeDef",
    {
        "EnvironmentVpcList": List[EnvironmentVpcTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "Description": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentId": str,
        "Error": ErrorResponseTypeDef,
        "LambdaEndpoint": LambdaEndpointConfigTypeDef,
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "Tags": Dict[str, str],
        "UrlEndpoint": UrlEndpointConfigTypeDef,
        "VpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "EnvironmentIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentVpcsRequestListEnvironmentVpcsPaginateTypeDef = TypedDict(
    "ListEnvironmentVpcsRequestListEnvironmentVpcsPaginateTypeDef",
    {
        "EnvironmentIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentsRequestListEnvironmentsPaginateTypeDef = TypedDict(
    "ListEnvironmentsRequestListEnvironmentsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRoutesRequestListRoutesPaginateTypeDef = TypedDict(
    "ListRoutesRequestListRoutesPaginateTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicesRequestListServicesPaginateTypeDef = TypedDict(
    "ListServicesRequestListServicesPaginateTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedByAccountId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "EndpointType": NotRequired[ServiceEndpointTypeType],
        "EnvironmentId": NotRequired[str],
        "Error": NotRequired[ErrorResponseTypeDef],
        "LambdaEndpoint": NotRequired[LambdaEndpointSummaryTypeDef],
        "LastUpdatedTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "ServiceId": NotRequired[str],
        "State": NotRequired[ServiceStateType],
        "Tags": NotRequired[Dict[str, str]],
        "UrlEndpoint": NotRequired[UrlEndpointSummaryTypeDef],
        "VpcId": NotRequired[str],
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaryList": List[ApplicationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEnvironmentsResponseTypeDef = TypedDict(
    "ListEnvironmentsResponseTypeDef",
    {
        "EnvironmentSummaryList": List[EnvironmentSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRoutesResponseTypeDef = TypedDict(
    "ListRoutesResponseTypeDef",
    {
        "RouteSummaryList": List[RouteSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "ServiceSummaryList": List[ServiceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
