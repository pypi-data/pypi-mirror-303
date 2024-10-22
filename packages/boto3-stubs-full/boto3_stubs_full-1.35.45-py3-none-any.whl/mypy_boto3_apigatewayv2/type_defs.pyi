"""
Type annotations for apigatewayv2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/type_defs/)

Usage::

    ```python
    from mypy_boto3_apigatewayv2.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AuthorizationTypeType,
    AuthorizerTypeType,
    ConnectionTypeType,
    ContentHandlingStrategyType,
    DeploymentStatusType,
    DomainNameStatusType,
    EndpointTypeType,
    IntegrationTypeType,
    JSONYAMLType,
    LoggingLevelType,
    PassthroughBehaviorType,
    ProtocolTypeType,
    SecurityPolicyType,
    VpcLinkStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessLogSettingsTypeDef",
    "ApiMappingTypeDef",
    "CorsOutputTypeDef",
    "JWTConfigurationOutputTypeDef",
    "CorsTypeDef",
    "CreateApiMappingRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "JWTConfigurationTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "DomainNameConfigurationOutputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "TlsConfigInputTypeDef",
    "CreateIntegrationResponseRequestRequestTypeDef",
    "TlsConfigTypeDef",
    "CreateModelRequestRequestTypeDef",
    "ParameterConstraintsTypeDef",
    "RouteSettingsTypeDef",
    "CreateVpcLinkRequestRequestTypeDef",
    "DeleteAccessLogSettingsRequestRequestTypeDef",
    "DeleteApiMappingRequestRequestTypeDef",
    "DeleteApiRequestRequestTypeDef",
    "DeleteAuthorizerRequestRequestTypeDef",
    "DeleteCorsConfigurationRequestRequestTypeDef",
    "DeleteDeploymentRequestRequestTypeDef",
    "DeleteDomainNameRequestRequestTypeDef",
    "DeleteIntegrationRequestRequestTypeDef",
    "DeleteIntegrationResponseRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteRouteRequestParameterRequestRequestTypeDef",
    "DeleteRouteRequestRequestTypeDef",
    "DeleteRouteResponseRequestRequestTypeDef",
    "DeleteRouteSettingsRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DeleteVpcLinkRequestRequestTypeDef",
    "DeploymentTypeDef",
    "TimestampTypeDef",
    "ExportApiRequestRequestTypeDef",
    "GetApiMappingRequestRequestTypeDef",
    "GetApiMappingsRequestRequestTypeDef",
    "GetApiRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetApisRequestRequestTypeDef",
    "GetAuthorizerRequestRequestTypeDef",
    "GetAuthorizersRequestRequestTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentsRequestRequestTypeDef",
    "GetDomainNameRequestRequestTypeDef",
    "GetDomainNamesRequestRequestTypeDef",
    "GetIntegrationRequestRequestTypeDef",
    "GetIntegrationResponseRequestRequestTypeDef",
    "GetIntegrationResponsesRequestRequestTypeDef",
    "IntegrationResponseTypeDef",
    "GetIntegrationsRequestRequestTypeDef",
    "GetModelRequestRequestTypeDef",
    "GetModelTemplateRequestRequestTypeDef",
    "GetModelsRequestRequestTypeDef",
    "ModelTypeDef",
    "GetRouteRequestRequestTypeDef",
    "GetRouteResponseRequestRequestTypeDef",
    "GetRouteResponsesRequestRequestTypeDef",
    "GetRoutesRequestRequestTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStagesRequestRequestTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetVpcLinkRequestRequestTypeDef",
    "GetVpcLinksRequestRequestTypeDef",
    "VpcLinkTypeDef",
    "ImportApiRequestRequestTypeDef",
    "ReimportApiRequestRequestTypeDef",
    "ResetAuthorizersCacheRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiMappingRequestRequestTypeDef",
    "UpdateDeploymentRequestRequestTypeDef",
    "UpdateIntegrationResponseRequestRequestTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateVpcLinkRequestRequestTypeDef",
    "ApiTypeDef",
    "AuthorizerTypeDef",
    "CreateApiRequestRequestTypeDef",
    "UpdateApiRequestRequestTypeDef",
    "CreateApiMappingResponseTypeDef",
    "CreateApiResponseTypeDef",
    "CreateAuthorizerResponseTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateIntegrationResponseResponseTypeDef",
    "CreateModelResponseTypeDef",
    "CreateVpcLinkResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportApiResponseTypeDef",
    "GetApiMappingResponseTypeDef",
    "GetApiMappingsResponseTypeDef",
    "GetApiResponseTypeDef",
    "GetAuthorizerResponseTypeDef",
    "GetDeploymentResponseTypeDef",
    "GetIntegrationResponseResponseTypeDef",
    "GetModelResponseTypeDef",
    "GetModelTemplateResponseTypeDef",
    "GetTagsResponseTypeDef",
    "GetVpcLinkResponseTypeDef",
    "ImportApiResponseTypeDef",
    "ReimportApiResponseTypeDef",
    "UpdateApiMappingResponseTypeDef",
    "UpdateApiResponseTypeDef",
    "UpdateAuthorizerResponseTypeDef",
    "UpdateDeploymentResponseTypeDef",
    "UpdateIntegrationResponseResponseTypeDef",
    "UpdateModelResponseTypeDef",
    "UpdateVpcLinkResponseTypeDef",
    "CreateAuthorizerRequestRequestTypeDef",
    "UpdateAuthorizerRequestRequestTypeDef",
    "CreateDomainNameResponseTypeDef",
    "DomainNameTypeDef",
    "GetDomainNameResponseTypeDef",
    "UpdateDomainNameResponseTypeDef",
    "CreateIntegrationRequestRequestTypeDef",
    "UpdateIntegrationRequestRequestTypeDef",
    "CreateIntegrationResultTypeDef",
    "GetIntegrationResultTypeDef",
    "IntegrationTypeDef",
    "UpdateIntegrationResultTypeDef",
    "CreateRouteRequestRequestTypeDef",
    "CreateRouteResponseRequestRequestTypeDef",
    "CreateRouteResponseResponseTypeDef",
    "CreateRouteResultTypeDef",
    "GetRouteResponseResponseTypeDef",
    "GetRouteResultTypeDef",
    "RouteResponseTypeDef",
    "RouteTypeDef",
    "UpdateRouteRequestRequestTypeDef",
    "UpdateRouteResponseRequestRequestTypeDef",
    "UpdateRouteResponseResponseTypeDef",
    "UpdateRouteResultTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateStageResponseTypeDef",
    "GetStageResponseTypeDef",
    "StageTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "UpdateStageResponseTypeDef",
    "GetDeploymentsResponseTypeDef",
    "DomainNameConfigurationTypeDef",
    "GetApisRequestGetApisPaginateTypeDef",
    "GetAuthorizersRequestGetAuthorizersPaginateTypeDef",
    "GetDeploymentsRequestGetDeploymentsPaginateTypeDef",
    "GetDomainNamesRequestGetDomainNamesPaginateTypeDef",
    "GetIntegrationResponsesRequestGetIntegrationResponsesPaginateTypeDef",
    "GetIntegrationsRequestGetIntegrationsPaginateTypeDef",
    "GetModelsRequestGetModelsPaginateTypeDef",
    "GetRouteResponsesRequestGetRouteResponsesPaginateTypeDef",
    "GetRoutesRequestGetRoutesPaginateTypeDef",
    "GetStagesRequestGetStagesPaginateTypeDef",
    "GetIntegrationResponsesResponseTypeDef",
    "GetModelsResponseTypeDef",
    "GetVpcLinksResponseTypeDef",
    "GetApisResponseTypeDef",
    "GetAuthorizersResponseTypeDef",
    "GetDomainNamesResponseTypeDef",
    "GetIntegrationsResponseTypeDef",
    "GetRouteResponsesResponseTypeDef",
    "GetRoutesResponseTypeDef",
    "GetStagesResponseTypeDef",
    "DomainNameConfigurationUnionTypeDef",
    "UpdateDomainNameRequestRequestTypeDef",
    "CreateDomainNameRequestRequestTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef",
    {
        "DestinationArn": NotRequired[str],
        "Format": NotRequired[str],
    },
)
ApiMappingTypeDef = TypedDict(
    "ApiMappingTypeDef",
    {
        "ApiId": str,
        "Stage": str,
        "ApiMappingId": NotRequired[str],
        "ApiMappingKey": NotRequired[str],
    },
)
CorsOutputTypeDef = TypedDict(
    "CorsOutputTypeDef",
    {
        "AllowCredentials": NotRequired[bool],
        "AllowHeaders": NotRequired[List[str]],
        "AllowMethods": NotRequired[List[str]],
        "AllowOrigins": NotRequired[List[str]],
        "ExposeHeaders": NotRequired[List[str]],
        "MaxAge": NotRequired[int],
    },
)
JWTConfigurationOutputTypeDef = TypedDict(
    "JWTConfigurationOutputTypeDef",
    {
        "Audience": NotRequired[List[str]],
        "Issuer": NotRequired[str],
    },
)
CorsTypeDef = TypedDict(
    "CorsTypeDef",
    {
        "AllowCredentials": NotRequired[bool],
        "AllowHeaders": NotRequired[Sequence[str]],
        "AllowMethods": NotRequired[Sequence[str]],
        "AllowOrigins": NotRequired[Sequence[str]],
        "ExposeHeaders": NotRequired[Sequence[str]],
        "MaxAge": NotRequired[int],
    },
)
CreateApiMappingRequestRequestTypeDef = TypedDict(
    "CreateApiMappingRequestRequestTypeDef",
    {
        "ApiId": str,
        "DomainName": str,
        "Stage": str,
        "ApiMappingKey": NotRequired[str],
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
JWTConfigurationTypeDef = TypedDict(
    "JWTConfigurationTypeDef",
    {
        "Audience": NotRequired[Sequence[str]],
        "Issuer": NotRequired[str],
    },
)
CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "ApiId": str,
        "Description": NotRequired[str],
        "StageName": NotRequired[str],
    },
)
MutualTlsAuthenticationInputTypeDef = TypedDict(
    "MutualTlsAuthenticationInputTypeDef",
    {
        "TruststoreUri": NotRequired[str],
        "TruststoreVersion": NotRequired[str],
    },
)
DomainNameConfigurationOutputTypeDef = TypedDict(
    "DomainNameConfigurationOutputTypeDef",
    {
        "ApiGatewayDomainName": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "CertificateName": NotRequired[str],
        "CertificateUploadDate": NotRequired[datetime],
        "DomainNameStatus": NotRequired[DomainNameStatusType],
        "DomainNameStatusMessage": NotRequired[str],
        "EndpointType": NotRequired[EndpointTypeType],
        "HostedZoneId": NotRequired[str],
        "SecurityPolicy": NotRequired[SecurityPolicyType],
        "OwnershipVerificationCertificateArn": NotRequired[str],
    },
)
MutualTlsAuthenticationTypeDef = TypedDict(
    "MutualTlsAuthenticationTypeDef",
    {
        "TruststoreUri": NotRequired[str],
        "TruststoreVersion": NotRequired[str],
        "TruststoreWarnings": NotRequired[List[str]],
    },
)
TlsConfigInputTypeDef = TypedDict(
    "TlsConfigInputTypeDef",
    {
        "ServerNameToVerify": NotRequired[str],
    },
)
CreateIntegrationResponseRequestRequestTypeDef = TypedDict(
    "CreateIntegrationResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseKey": str,
        "ContentHandlingStrategy": NotRequired[ContentHandlingStrategyType],
        "ResponseParameters": NotRequired[Mapping[str, str]],
        "ResponseTemplates": NotRequired[Mapping[str, str]],
        "TemplateSelectionExpression": NotRequired[str],
    },
)
TlsConfigTypeDef = TypedDict(
    "TlsConfigTypeDef",
    {
        "ServerNameToVerify": NotRequired[str],
    },
)
CreateModelRequestRequestTypeDef = TypedDict(
    "CreateModelRequestRequestTypeDef",
    {
        "ApiId": str,
        "Name": str,
        "Schema": str,
        "ContentType": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "Required": NotRequired[bool],
    },
)
RouteSettingsTypeDef = TypedDict(
    "RouteSettingsTypeDef",
    {
        "DataTraceEnabled": NotRequired[bool],
        "DetailedMetricsEnabled": NotRequired[bool],
        "LoggingLevel": NotRequired[LoggingLevelType],
        "ThrottlingBurstLimit": NotRequired[int],
        "ThrottlingRateLimit": NotRequired[float],
    },
)
CreateVpcLinkRequestRequestTypeDef = TypedDict(
    "CreateVpcLinkRequestRequestTypeDef",
    {
        "Name": str,
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteAccessLogSettingsRequestRequestTypeDef = TypedDict(
    "DeleteAccessLogSettingsRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)
DeleteApiMappingRequestRequestTypeDef = TypedDict(
    "DeleteApiMappingRequestRequestTypeDef",
    {
        "ApiMappingId": str,
        "DomainName": str,
    },
)
DeleteApiRequestRequestTypeDef = TypedDict(
    "DeleteApiRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
DeleteAuthorizerRequestRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
    },
)
DeleteCorsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteCorsConfigurationRequestRequestTypeDef",
    {
        "ApiId": str,
    },
)
DeleteDeploymentRequestRequestTypeDef = TypedDict(
    "DeleteDeploymentRequestRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
    },
)
DeleteDomainNameRequestRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DeleteIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)
DeleteIntegrationResponseRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
    },
)
DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)
DeleteRouteRequestParameterRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestParameterRequestRequestTypeDef",
    {
        "ApiId": str,
        "RequestParameterKey": str,
        "RouteId": str,
    },
)
DeleteRouteRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)
DeleteRouteResponseRequestRequestTypeDef = TypedDict(
    "DeleteRouteResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
    },
)
DeleteRouteSettingsRequestRequestTypeDef = TypedDict(
    "DeleteRouteSettingsRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteKey": str,
        "StageName": str,
    },
)
DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)
DeleteVpcLinkRequestRequestTypeDef = TypedDict(
    "DeleteVpcLinkRequestRequestTypeDef",
    {
        "VpcLinkId": str,
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "AutoDeployed": NotRequired[bool],
        "CreatedDate": NotRequired[datetime],
        "DeploymentId": NotRequired[str],
        "DeploymentStatus": NotRequired[DeploymentStatusType],
        "DeploymentStatusMessage": NotRequired[str],
        "Description": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ExportApiRequestRequestTypeDef = TypedDict(
    "ExportApiRequestRequestTypeDef",
    {
        "ApiId": str,
        "OutputType": JSONYAMLType,
        "Specification": Literal["OAS30"],
        "ExportVersion": NotRequired[str],
        "IncludeExtensions": NotRequired[bool],
        "StageName": NotRequired[str],
    },
)
GetApiMappingRequestRequestTypeDef = TypedDict(
    "GetApiMappingRequestRequestTypeDef",
    {
        "ApiMappingId": str,
        "DomainName": str,
    },
)
GetApiMappingsRequestRequestTypeDef = TypedDict(
    "GetApiMappingsRequestRequestTypeDef",
    {
        "DomainName": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetApiRequestRequestTypeDef = TypedDict(
    "GetApiRequestRequestTypeDef",
    {
        "ApiId": str,
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
GetApisRequestRequestTypeDef = TypedDict(
    "GetApisRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetAuthorizerRequestRequestTypeDef = TypedDict(
    "GetAuthorizerRequestRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
    },
)
GetAuthorizersRequestRequestTypeDef = TypedDict(
    "GetAuthorizersRequestRequestTypeDef",
    {
        "ApiId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
    },
)
GetDeploymentsRequestRequestTypeDef = TypedDict(
    "GetDeploymentsRequestRequestTypeDef",
    {
        "ApiId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetDomainNameRequestRequestTypeDef = TypedDict(
    "GetDomainNameRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
GetDomainNamesRequestRequestTypeDef = TypedDict(
    "GetDomainNamesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetIntegrationRequestRequestTypeDef = TypedDict(
    "GetIntegrationRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)
GetIntegrationResponseRequestRequestTypeDef = TypedDict(
    "GetIntegrationResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
    },
)
GetIntegrationResponsesRequestRequestTypeDef = TypedDict(
    "GetIntegrationResponsesRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
IntegrationResponseTypeDef = TypedDict(
    "IntegrationResponseTypeDef",
    {
        "IntegrationResponseKey": str,
        "ContentHandlingStrategy": NotRequired[ContentHandlingStrategyType],
        "IntegrationResponseId": NotRequired[str],
        "ResponseParameters": NotRequired[Dict[str, str]],
        "ResponseTemplates": NotRequired[Dict[str, str]],
        "TemplateSelectionExpression": NotRequired[str],
    },
)
GetIntegrationsRequestRequestTypeDef = TypedDict(
    "GetIntegrationsRequestRequestTypeDef",
    {
        "ApiId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetModelRequestRequestTypeDef = TypedDict(
    "GetModelRequestRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)
GetModelTemplateRequestRequestTypeDef = TypedDict(
    "GetModelTemplateRequestRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)
GetModelsRequestRequestTypeDef = TypedDict(
    "GetModelsRequestRequestTypeDef",
    {
        "ApiId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "Name": str,
        "ContentType": NotRequired[str],
        "Description": NotRequired[str],
        "ModelId": NotRequired[str],
        "Schema": NotRequired[str],
    },
)
GetRouteRequestRequestTypeDef = TypedDict(
    "GetRouteRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)
GetRouteResponseRequestRequestTypeDef = TypedDict(
    "GetRouteResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
    },
)
GetRouteResponsesRequestRequestTypeDef = TypedDict(
    "GetRouteResponsesRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetRoutesRequestRequestTypeDef = TypedDict(
    "GetRoutesRequestRequestTypeDef",
    {
        "ApiId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)
GetStagesRequestRequestTypeDef = TypedDict(
    "GetStagesRequestRequestTypeDef",
    {
        "ApiId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetTagsRequestRequestTypeDef = TypedDict(
    "GetTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetVpcLinkRequestRequestTypeDef = TypedDict(
    "GetVpcLinkRequestRequestTypeDef",
    {
        "VpcLinkId": str,
    },
)
GetVpcLinksRequestRequestTypeDef = TypedDict(
    "GetVpcLinksRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
VpcLinkTypeDef = TypedDict(
    "VpcLinkTypeDef",
    {
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VpcLinkId": str,
        "CreatedDate": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
        "VpcLinkStatus": NotRequired[VpcLinkStatusType],
        "VpcLinkStatusMessage": NotRequired[str],
        "VpcLinkVersion": NotRequired[Literal["V2"]],
    },
)
ImportApiRequestRequestTypeDef = TypedDict(
    "ImportApiRequestRequestTypeDef",
    {
        "Body": str,
        "Basepath": NotRequired[str],
        "FailOnWarnings": NotRequired[bool],
    },
)
ReimportApiRequestRequestTypeDef = TypedDict(
    "ReimportApiRequestRequestTypeDef",
    {
        "ApiId": str,
        "Body": str,
        "Basepath": NotRequired[str],
        "FailOnWarnings": NotRequired[bool],
    },
)
ResetAuthorizersCacheRequestRequestTypeDef = TypedDict(
    "ResetAuthorizersCacheRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateApiMappingRequestRequestTypeDef = TypedDict(
    "UpdateApiMappingRequestRequestTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "DomainName": str,
        "ApiMappingKey": NotRequired[str],
        "Stage": NotRequired[str],
    },
)
UpdateDeploymentRequestRequestTypeDef = TypedDict(
    "UpdateDeploymentRequestRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
        "Description": NotRequired[str],
    },
)
UpdateIntegrationResponseRequestRequestTypeDef = TypedDict(
    "UpdateIntegrationResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
        "ContentHandlingStrategy": NotRequired[ContentHandlingStrategyType],
        "IntegrationResponseKey": NotRequired[str],
        "ResponseParameters": NotRequired[Mapping[str, str]],
        "ResponseTemplates": NotRequired[Mapping[str, str]],
        "TemplateSelectionExpression": NotRequired[str],
    },
)
UpdateModelRequestRequestTypeDef = TypedDict(
    "UpdateModelRequestRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
        "ContentType": NotRequired[str],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Schema": NotRequired[str],
    },
)
UpdateVpcLinkRequestRequestTypeDef = TypedDict(
    "UpdateVpcLinkRequestRequestTypeDef",
    {
        "VpcLinkId": str,
        "Name": NotRequired[str],
    },
)
ApiTypeDef = TypedDict(
    "ApiTypeDef",
    {
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "ApiEndpoint": NotRequired[str],
        "ApiGatewayManaged": NotRequired[bool],
        "ApiId": NotRequired[str],
        "ApiKeySelectionExpression": NotRequired[str],
        "CorsConfiguration": NotRequired[CorsOutputTypeDef],
        "CreatedDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "DisableSchemaValidation": NotRequired[bool],
        "DisableExecuteApiEndpoint": NotRequired[bool],
        "ImportInfo": NotRequired[List[str]],
        "Tags": NotRequired[Dict[str, str]],
        "Version": NotRequired[str],
        "Warnings": NotRequired[List[str]],
    },
)
AuthorizerTypeDef = TypedDict(
    "AuthorizerTypeDef",
    {
        "Name": str,
        "AuthorizerCredentialsArn": NotRequired[str],
        "AuthorizerId": NotRequired[str],
        "AuthorizerPayloadFormatVersion": NotRequired[str],
        "AuthorizerResultTtlInSeconds": NotRequired[int],
        "AuthorizerType": NotRequired[AuthorizerTypeType],
        "AuthorizerUri": NotRequired[str],
        "EnableSimpleResponses": NotRequired[bool],
        "IdentitySource": NotRequired[List[str]],
        "IdentityValidationExpression": NotRequired[str],
        "JwtConfiguration": NotRequired[JWTConfigurationOutputTypeDef],
    },
)
CreateApiRequestRequestTypeDef = TypedDict(
    "CreateApiRequestRequestTypeDef",
    {
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "ApiKeySelectionExpression": NotRequired[str],
        "CorsConfiguration": NotRequired[CorsTypeDef],
        "CredentialsArn": NotRequired[str],
        "Description": NotRequired[str],
        "DisableSchemaValidation": NotRequired[bool],
        "DisableExecuteApiEndpoint": NotRequired[bool],
        "RouteKey": NotRequired[str],
        "RouteSelectionExpression": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Target": NotRequired[str],
        "Version": NotRequired[str],
    },
)
UpdateApiRequestRequestTypeDef = TypedDict(
    "UpdateApiRequestRequestTypeDef",
    {
        "ApiId": str,
        "ApiKeySelectionExpression": NotRequired[str],
        "CorsConfiguration": NotRequired[CorsTypeDef],
        "CredentialsArn": NotRequired[str],
        "Description": NotRequired[str],
        "DisableSchemaValidation": NotRequired[bool],
        "DisableExecuteApiEndpoint": NotRequired[bool],
        "Name": NotRequired[str],
        "RouteKey": NotRequired[str],
        "RouteSelectionExpression": NotRequired[str],
        "Target": NotRequired[str],
        "Version": NotRequired[str],
    },
)
CreateApiMappingResponseTypeDef = TypedDict(
    "CreateApiMappingResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApiResponseTypeDef = TypedDict(
    "CreateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": CorsOutputTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAuthorizerResponseTypeDef = TypedDict(
    "CreateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": JWTConfigurationOutputTypeDef,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIntegrationResponseResponseTypeDef = TypedDict(
    "CreateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelResponseTypeDef = TypedDict(
    "CreateModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpcLinkResponseTypeDef = TypedDict(
    "CreateVpcLinkResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportApiResponseTypeDef = TypedDict(
    "ExportApiResponseTypeDef",
    {
        "body": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApiMappingResponseTypeDef = TypedDict(
    "GetApiMappingResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApiMappingsResponseTypeDef = TypedDict(
    "GetApiMappingsResponseTypeDef",
    {
        "Items": List[ApiMappingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetApiResponseTypeDef = TypedDict(
    "GetApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": CorsOutputTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAuthorizerResponseTypeDef = TypedDict(
    "GetAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": JWTConfigurationOutputTypeDef,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentResponseTypeDef = TypedDict(
    "GetDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIntegrationResponseResponseTypeDef = TypedDict(
    "GetIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetModelResponseTypeDef = TypedDict(
    "GetModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetModelTemplateResponseTypeDef = TypedDict(
    "GetModelTemplateResponseTypeDef",
    {
        "Value": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTagsResponseTypeDef = TypedDict(
    "GetTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVpcLinkResponseTypeDef = TypedDict(
    "GetVpcLinkResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportApiResponseTypeDef = TypedDict(
    "ImportApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": CorsOutputTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReimportApiResponseTypeDef = TypedDict(
    "ReimportApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": CorsOutputTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApiMappingResponseTypeDef = TypedDict(
    "UpdateApiMappingResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApiResponseTypeDef = TypedDict(
    "UpdateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": CorsOutputTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAuthorizerResponseTypeDef = TypedDict(
    "UpdateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": JWTConfigurationOutputTypeDef,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDeploymentResponseTypeDef = TypedDict(
    "UpdateDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIntegrationResponseResponseTypeDef = TypedDict(
    "UpdateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateModelResponseTypeDef = TypedDict(
    "UpdateModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVpcLinkResponseTypeDef = TypedDict(
    "UpdateVpcLinkResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAuthorizerRequestRequestTypeDef = TypedDict(
    "CreateAuthorizerRequestRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerType": AuthorizerTypeType,
        "IdentitySource": Sequence[str],
        "Name": str,
        "AuthorizerCredentialsArn": NotRequired[str],
        "AuthorizerPayloadFormatVersion": NotRequired[str],
        "AuthorizerResultTtlInSeconds": NotRequired[int],
        "AuthorizerUri": NotRequired[str],
        "EnableSimpleResponses": NotRequired[bool],
        "IdentityValidationExpression": NotRequired[str],
        "JwtConfiguration": NotRequired[JWTConfigurationTypeDef],
    },
)
UpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "UpdateAuthorizerRequestRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
        "AuthorizerCredentialsArn": NotRequired[str],
        "AuthorizerPayloadFormatVersion": NotRequired[str],
        "AuthorizerResultTtlInSeconds": NotRequired[int],
        "AuthorizerType": NotRequired[AuthorizerTypeType],
        "AuthorizerUri": NotRequired[str],
        "EnableSimpleResponses": NotRequired[bool],
        "IdentitySource": NotRequired[Sequence[str]],
        "IdentityValidationExpression": NotRequired[str],
        "JwtConfiguration": NotRequired[JWTConfigurationTypeDef],
        "Name": NotRequired[str],
    },
)
CreateDomainNameResponseTypeDef = TypedDict(
    "CreateDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[DomainNameConfigurationOutputTypeDef],
        "MutualTlsAuthentication": MutualTlsAuthenticationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DomainNameTypeDef = TypedDict(
    "DomainNameTypeDef",
    {
        "DomainName": str,
        "ApiMappingSelectionExpression": NotRequired[str],
        "DomainNameConfigurations": NotRequired[List[DomainNameConfigurationOutputTypeDef]],
        "MutualTlsAuthentication": NotRequired[MutualTlsAuthenticationTypeDef],
        "Tags": NotRequired[Dict[str, str]],
    },
)
GetDomainNameResponseTypeDef = TypedDict(
    "GetDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[DomainNameConfigurationOutputTypeDef],
        "MutualTlsAuthentication": MutualTlsAuthenticationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainNameResponseTypeDef = TypedDict(
    "UpdateDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[DomainNameConfigurationOutputTypeDef],
        "MutualTlsAuthentication": MutualTlsAuthenticationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIntegrationRequestRequestTypeDef = TypedDict(
    "CreateIntegrationRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationType": IntegrationTypeType,
        "ConnectionId": NotRequired[str],
        "ConnectionType": NotRequired[ConnectionTypeType],
        "ContentHandlingStrategy": NotRequired[ContentHandlingStrategyType],
        "CredentialsArn": NotRequired[str],
        "Description": NotRequired[str],
        "IntegrationMethod": NotRequired[str],
        "IntegrationSubtype": NotRequired[str],
        "IntegrationUri": NotRequired[str],
        "PassthroughBehavior": NotRequired[PassthroughBehaviorType],
        "PayloadFormatVersion": NotRequired[str],
        "RequestParameters": NotRequired[Mapping[str, str]],
        "RequestTemplates": NotRequired[Mapping[str, str]],
        "ResponseParameters": NotRequired[Mapping[str, Mapping[str, str]]],
        "TemplateSelectionExpression": NotRequired[str],
        "TimeoutInMillis": NotRequired[int],
        "TlsConfig": NotRequired[TlsConfigInputTypeDef],
    },
)
UpdateIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateIntegrationRequestRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "ConnectionId": NotRequired[str],
        "ConnectionType": NotRequired[ConnectionTypeType],
        "ContentHandlingStrategy": NotRequired[ContentHandlingStrategyType],
        "CredentialsArn": NotRequired[str],
        "Description": NotRequired[str],
        "IntegrationMethod": NotRequired[str],
        "IntegrationSubtype": NotRequired[str],
        "IntegrationType": NotRequired[IntegrationTypeType],
        "IntegrationUri": NotRequired[str],
        "PassthroughBehavior": NotRequired[PassthroughBehaviorType],
        "PayloadFormatVersion": NotRequired[str],
        "RequestParameters": NotRequired[Mapping[str, str]],
        "RequestTemplates": NotRequired[Mapping[str, str]],
        "ResponseParameters": NotRequired[Mapping[str, Mapping[str, str]]],
        "TemplateSelectionExpression": NotRequired[str],
        "TimeoutInMillis": NotRequired[int],
        "TlsConfig": NotRequired[TlsConfigInputTypeDef],
    },
)
CreateIntegrationResultTypeDef = TypedDict(
    "CreateIntegrationResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": TlsConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIntegrationResultTypeDef = TypedDict(
    "GetIntegrationResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": TlsConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "ApiGatewayManaged": NotRequired[bool],
        "ConnectionId": NotRequired[str],
        "ConnectionType": NotRequired[ConnectionTypeType],
        "ContentHandlingStrategy": NotRequired[ContentHandlingStrategyType],
        "CredentialsArn": NotRequired[str],
        "Description": NotRequired[str],
        "IntegrationId": NotRequired[str],
        "IntegrationMethod": NotRequired[str],
        "IntegrationResponseSelectionExpression": NotRequired[str],
        "IntegrationSubtype": NotRequired[str],
        "IntegrationType": NotRequired[IntegrationTypeType],
        "IntegrationUri": NotRequired[str],
        "PassthroughBehavior": NotRequired[PassthroughBehaviorType],
        "PayloadFormatVersion": NotRequired[str],
        "RequestParameters": NotRequired[Dict[str, str]],
        "RequestTemplates": NotRequired[Dict[str, str]],
        "ResponseParameters": NotRequired[Dict[str, Dict[str, str]]],
        "TemplateSelectionExpression": NotRequired[str],
        "TimeoutInMillis": NotRequired[int],
        "TlsConfig": NotRequired[TlsConfigTypeDef],
    },
)
UpdateIntegrationResultTypeDef = TypedDict(
    "UpdateIntegrationResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": TlsConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRouteRequestRequestTypeDef = TypedDict(
    "CreateRouteRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteKey": str,
        "ApiKeyRequired": NotRequired[bool],
        "AuthorizationScopes": NotRequired[Sequence[str]],
        "AuthorizationType": NotRequired[AuthorizationTypeType],
        "AuthorizerId": NotRequired[str],
        "ModelSelectionExpression": NotRequired[str],
        "OperationName": NotRequired[str],
        "RequestModels": NotRequired[Mapping[str, str]],
        "RequestParameters": NotRequired[Mapping[str, ParameterConstraintsTypeDef]],
        "RouteResponseSelectionExpression": NotRequired[str],
        "Target": NotRequired[str],
    },
)
CreateRouteResponseRequestRequestTypeDef = TypedDict(
    "CreateRouteResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseKey": str,
        "ModelSelectionExpression": NotRequired[str],
        "ResponseModels": NotRequired[Mapping[str, str]],
        "ResponseParameters": NotRequired[Mapping[str, ParameterConstraintsTypeDef]],
    },
)
CreateRouteResponseResponseTypeDef = TypedDict(
    "CreateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ParameterConstraintsTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRouteResultTypeDef = TypedDict(
    "CreateRouteResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ParameterConstraintsTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRouteResponseResponseTypeDef = TypedDict(
    "GetRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ParameterConstraintsTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRouteResultTypeDef = TypedDict(
    "GetRouteResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ParameterConstraintsTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RouteResponseTypeDef = TypedDict(
    "RouteResponseTypeDef",
    {
        "RouteResponseKey": str,
        "ModelSelectionExpression": NotRequired[str],
        "ResponseModels": NotRequired[Dict[str, str]],
        "ResponseParameters": NotRequired[Dict[str, ParameterConstraintsTypeDef]],
        "RouteResponseId": NotRequired[str],
    },
)
RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "RouteKey": str,
        "ApiGatewayManaged": NotRequired[bool],
        "ApiKeyRequired": NotRequired[bool],
        "AuthorizationScopes": NotRequired[List[str]],
        "AuthorizationType": NotRequired[AuthorizationTypeType],
        "AuthorizerId": NotRequired[str],
        "ModelSelectionExpression": NotRequired[str],
        "OperationName": NotRequired[str],
        "RequestModels": NotRequired[Dict[str, str]],
        "RequestParameters": NotRequired[Dict[str, ParameterConstraintsTypeDef]],
        "RouteId": NotRequired[str],
        "RouteResponseSelectionExpression": NotRequired[str],
        "Target": NotRequired[str],
    },
)
UpdateRouteRequestRequestTypeDef = TypedDict(
    "UpdateRouteRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "ApiKeyRequired": NotRequired[bool],
        "AuthorizationScopes": NotRequired[Sequence[str]],
        "AuthorizationType": NotRequired[AuthorizationTypeType],
        "AuthorizerId": NotRequired[str],
        "ModelSelectionExpression": NotRequired[str],
        "OperationName": NotRequired[str],
        "RequestModels": NotRequired[Mapping[str, str]],
        "RequestParameters": NotRequired[Mapping[str, ParameterConstraintsTypeDef]],
        "RouteKey": NotRequired[str],
        "RouteResponseSelectionExpression": NotRequired[str],
        "Target": NotRequired[str],
    },
)
UpdateRouteResponseRequestRequestTypeDef = TypedDict(
    "UpdateRouteResponseRequestRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
        "ModelSelectionExpression": NotRequired[str],
        "ResponseModels": NotRequired[Mapping[str, str]],
        "ResponseParameters": NotRequired[Mapping[str, ParameterConstraintsTypeDef]],
        "RouteResponseKey": NotRequired[str],
    },
)
UpdateRouteResponseResponseTypeDef = TypedDict(
    "UpdateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ParameterConstraintsTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRouteResultTypeDef = TypedDict(
    "UpdateRouteResultTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ParameterConstraintsTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStageRequestRequestTypeDef = TypedDict(
    "CreateStageRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
        "AccessLogSettings": NotRequired[AccessLogSettingsTypeDef],
        "AutoDeploy": NotRequired[bool],
        "ClientCertificateId": NotRequired[str],
        "DefaultRouteSettings": NotRequired[RouteSettingsTypeDef],
        "DeploymentId": NotRequired[str],
        "Description": NotRequired[str],
        "RouteSettings": NotRequired[Mapping[str, RouteSettingsTypeDef]],
        "StageVariables": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateStageResponseTypeDef = TypedDict(
    "CreateStageResponseTypeDef",
    {
        "AccessLogSettings": AccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": RouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, RouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStageResponseTypeDef = TypedDict(
    "GetStageResponseTypeDef",
    {
        "AccessLogSettings": AccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": RouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, RouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "StageName": str,
        "AccessLogSettings": NotRequired[AccessLogSettingsTypeDef],
        "ApiGatewayManaged": NotRequired[bool],
        "AutoDeploy": NotRequired[bool],
        "ClientCertificateId": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "DefaultRouteSettings": NotRequired[RouteSettingsTypeDef],
        "DeploymentId": NotRequired[str],
        "Description": NotRequired[str],
        "LastDeploymentStatusMessage": NotRequired[str],
        "LastUpdatedDate": NotRequired[datetime],
        "RouteSettings": NotRequired[Dict[str, RouteSettingsTypeDef]],
        "StageVariables": NotRequired[Dict[str, str]],
        "Tags": NotRequired[Dict[str, str]],
    },
)
UpdateStageRequestRequestTypeDef = TypedDict(
    "UpdateStageRequestRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
        "AccessLogSettings": NotRequired[AccessLogSettingsTypeDef],
        "AutoDeploy": NotRequired[bool],
        "ClientCertificateId": NotRequired[str],
        "DefaultRouteSettings": NotRequired[RouteSettingsTypeDef],
        "DeploymentId": NotRequired[str],
        "Description": NotRequired[str],
        "RouteSettings": NotRequired[Mapping[str, RouteSettingsTypeDef]],
        "StageVariables": NotRequired[Mapping[str, str]],
    },
)
UpdateStageResponseTypeDef = TypedDict(
    "UpdateStageResponseTypeDef",
    {
        "AccessLogSettings": AccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": RouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, RouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentsResponseTypeDef = TypedDict(
    "GetDeploymentsResponseTypeDef",
    {
        "Items": List[DeploymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DomainNameConfigurationTypeDef = TypedDict(
    "DomainNameConfigurationTypeDef",
    {
        "ApiGatewayDomainName": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "CertificateName": NotRequired[str],
        "CertificateUploadDate": NotRequired[TimestampTypeDef],
        "DomainNameStatus": NotRequired[DomainNameStatusType],
        "DomainNameStatusMessage": NotRequired[str],
        "EndpointType": NotRequired[EndpointTypeType],
        "HostedZoneId": NotRequired[str],
        "SecurityPolicy": NotRequired[SecurityPolicyType],
        "OwnershipVerificationCertificateArn": NotRequired[str],
    },
)
GetApisRequestGetApisPaginateTypeDef = TypedDict(
    "GetApisRequestGetApisPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAuthorizersRequestGetAuthorizersPaginateTypeDef = TypedDict(
    "GetAuthorizersRequestGetAuthorizersPaginateTypeDef",
    {
        "ApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDeploymentsRequestGetDeploymentsPaginateTypeDef = TypedDict(
    "GetDeploymentsRequestGetDeploymentsPaginateTypeDef",
    {
        "ApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDomainNamesRequestGetDomainNamesPaginateTypeDef = TypedDict(
    "GetDomainNamesRequestGetDomainNamesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIntegrationResponsesRequestGetIntegrationResponsesPaginateTypeDef = TypedDict(
    "GetIntegrationResponsesRequestGetIntegrationResponsesPaginateTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIntegrationsRequestGetIntegrationsPaginateTypeDef = TypedDict(
    "GetIntegrationsRequestGetIntegrationsPaginateTypeDef",
    {
        "ApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetModelsRequestGetModelsPaginateTypeDef = TypedDict(
    "GetModelsRequestGetModelsPaginateTypeDef",
    {
        "ApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRouteResponsesRequestGetRouteResponsesPaginateTypeDef = TypedDict(
    "GetRouteResponsesRequestGetRouteResponsesPaginateTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRoutesRequestGetRoutesPaginateTypeDef = TypedDict(
    "GetRoutesRequestGetRoutesPaginateTypeDef",
    {
        "ApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetStagesRequestGetStagesPaginateTypeDef = TypedDict(
    "GetStagesRequestGetStagesPaginateTypeDef",
    {
        "ApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIntegrationResponsesResponseTypeDef = TypedDict(
    "GetIntegrationResponsesResponseTypeDef",
    {
        "Items": List[IntegrationResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetModelsResponseTypeDef = TypedDict(
    "GetModelsResponseTypeDef",
    {
        "Items": List[ModelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetVpcLinksResponseTypeDef = TypedDict(
    "GetVpcLinksResponseTypeDef",
    {
        "Items": List[VpcLinkTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetApisResponseTypeDef = TypedDict(
    "GetApisResponseTypeDef",
    {
        "Items": List[ApiTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetAuthorizersResponseTypeDef = TypedDict(
    "GetAuthorizersResponseTypeDef",
    {
        "Items": List[AuthorizerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDomainNamesResponseTypeDef = TypedDict(
    "GetDomainNamesResponseTypeDef",
    {
        "Items": List[DomainNameTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetIntegrationsResponseTypeDef = TypedDict(
    "GetIntegrationsResponseTypeDef",
    {
        "Items": List[IntegrationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetRouteResponsesResponseTypeDef = TypedDict(
    "GetRouteResponsesResponseTypeDef",
    {
        "Items": List[RouteResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetRoutesResponseTypeDef = TypedDict(
    "GetRoutesResponseTypeDef",
    {
        "Items": List[RouteTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetStagesResponseTypeDef = TypedDict(
    "GetStagesResponseTypeDef",
    {
        "Items": List[StageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DomainNameConfigurationUnionTypeDef = Union[
    DomainNameConfigurationTypeDef, DomainNameConfigurationOutputTypeDef
]
UpdateDomainNameRequestRequestTypeDef = TypedDict(
    "UpdateDomainNameRequestRequestTypeDef",
    {
        "DomainName": str,
        "DomainNameConfigurations": NotRequired[Sequence[DomainNameConfigurationTypeDef]],
        "MutualTlsAuthentication": NotRequired[MutualTlsAuthenticationInputTypeDef],
    },
)
CreateDomainNameRequestRequestTypeDef = TypedDict(
    "CreateDomainNameRequestRequestTypeDef",
    {
        "DomainName": str,
        "DomainNameConfigurations": NotRequired[Sequence[DomainNameConfigurationUnionTypeDef]],
        "MutualTlsAuthentication": NotRequired[MutualTlsAuthenticationInputTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
