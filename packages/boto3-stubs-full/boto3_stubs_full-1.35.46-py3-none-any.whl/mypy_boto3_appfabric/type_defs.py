"""
Type annotations for appfabric service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/type_defs/)

Usage::

    ```python
    from mypy_boto3_appfabric.type_defs import ApiKeyCredentialTypeDef

    data: ApiKeyCredentialTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AppAuthorizationStatusType,
    AuthTypeType,
    FormatType,
    IngestionDestinationStatusType,
    IngestionStateType,
    PersonaType,
    ResultStatusType,
    SchemaType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ApiKeyCredentialTypeDef",
    "TenantTypeDef",
    "AppBundleSummaryTypeDef",
    "AppBundleTypeDef",
    "AuditLogProcessingConfigurationTypeDef",
    "AuthRequestTypeDef",
    "BatchGetUserAccessTasksRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "IngestionTypeDef",
    "Oauth2CredentialTypeDef",
    "DeleteAppAuthorizationRequestRequestTypeDef",
    "DeleteAppBundleRequestRequestTypeDef",
    "DeleteIngestionDestinationRequestRequestTypeDef",
    "DeleteIngestionRequestRequestTypeDef",
    "FirehoseStreamTypeDef",
    "S3BucketTypeDef",
    "GetAppAuthorizationRequestRequestTypeDef",
    "GetAppBundleRequestRequestTypeDef",
    "GetIngestionDestinationRequestRequestTypeDef",
    "GetIngestionRequestRequestTypeDef",
    "IngestionDestinationSummaryTypeDef",
    "IngestionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListAppAuthorizationsRequestRequestTypeDef",
    "ListAppBundlesRequestRequestTypeDef",
    "ListIngestionDestinationsRequestRequestTypeDef",
    "ListIngestionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StartIngestionRequestRequestTypeDef",
    "StartUserAccessTasksRequestRequestTypeDef",
    "StopIngestionRequestRequestTypeDef",
    "TaskErrorTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AppAuthorizationSummaryTypeDef",
    "AppAuthorizationTypeDef",
    "ProcessingConfigurationTypeDef",
    "ConnectAppAuthorizationRequestRequestTypeDef",
    "CreateAppBundleResponseTypeDef",
    "GetAppBundleResponseTypeDef",
    "ListAppBundlesResponseTypeDef",
    "CreateAppBundleRequestRequestTypeDef",
    "CreateIngestionRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateIngestionResponseTypeDef",
    "GetIngestionResponseTypeDef",
    "CredentialTypeDef",
    "DestinationTypeDef",
    "ListIngestionDestinationsResponseTypeDef",
    "ListIngestionsResponseTypeDef",
    "ListAppAuthorizationsRequestListAppAuthorizationsPaginateTypeDef",
    "ListAppBundlesRequestListAppBundlesPaginateTypeDef",
    "ListIngestionDestinationsRequestListIngestionDestinationsPaginateTypeDef",
    "ListIngestionsRequestListIngestionsPaginateTypeDef",
    "UserAccessResultItemTypeDef",
    "UserAccessTaskItemTypeDef",
    "ConnectAppAuthorizationResponseTypeDef",
    "ListAppAuthorizationsResponseTypeDef",
    "CreateAppAuthorizationResponseTypeDef",
    "GetAppAuthorizationResponseTypeDef",
    "UpdateAppAuthorizationResponseTypeDef",
    "CreateAppAuthorizationRequestRequestTypeDef",
    "UpdateAppAuthorizationRequestRequestTypeDef",
    "AuditLogDestinationConfigurationTypeDef",
    "BatchGetUserAccessTasksResponseTypeDef",
    "StartUserAccessTasksResponseTypeDef",
    "DestinationConfigurationTypeDef",
    "CreateIngestionDestinationRequestRequestTypeDef",
    "IngestionDestinationTypeDef",
    "UpdateIngestionDestinationRequestRequestTypeDef",
    "CreateIngestionDestinationResponseTypeDef",
    "GetIngestionDestinationResponseTypeDef",
    "UpdateIngestionDestinationResponseTypeDef",
)

ApiKeyCredentialTypeDef = TypedDict(
    "ApiKeyCredentialTypeDef",
    {
        "apiKey": str,
    },
)
TenantTypeDef = TypedDict(
    "TenantTypeDef",
    {
        "tenantIdentifier": str,
        "tenantDisplayName": str,
    },
)
AppBundleSummaryTypeDef = TypedDict(
    "AppBundleSummaryTypeDef",
    {
        "arn": str,
    },
)
AppBundleTypeDef = TypedDict(
    "AppBundleTypeDef",
    {
        "arn": str,
        "customerManagedKeyArn": NotRequired[str],
    },
)
AuditLogProcessingConfigurationTypeDef = TypedDict(
    "AuditLogProcessingConfigurationTypeDef",
    {
        "schema": SchemaType,
        "format": FormatType,
    },
)
AuthRequestTypeDef = TypedDict(
    "AuthRequestTypeDef",
    {
        "redirectUri": str,
        "code": str,
    },
)
BatchGetUserAccessTasksRequestRequestTypeDef = TypedDict(
    "BatchGetUserAccessTasksRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "taskIdList": Sequence[str],
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
IngestionTypeDef = TypedDict(
    "IngestionTypeDef",
    {
        "arn": str,
        "appBundleArn": str,
        "app": str,
        "tenantId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "state": IngestionStateType,
        "ingestionType": Literal["auditLog"],
    },
)
Oauth2CredentialTypeDef = TypedDict(
    "Oauth2CredentialTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
DeleteAppAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "appAuthorizationIdentifier": str,
    },
)
DeleteAppBundleRequestRequestTypeDef = TypedDict(
    "DeleteAppBundleRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
    },
)
DeleteIngestionDestinationRequestRequestTypeDef = TypedDict(
    "DeleteIngestionDestinationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "ingestionDestinationIdentifier": str,
    },
)
DeleteIngestionRequestRequestTypeDef = TypedDict(
    "DeleteIngestionRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
    },
)
FirehoseStreamTypeDef = TypedDict(
    "FirehoseStreamTypeDef",
    {
        "streamName": str,
    },
)
S3BucketTypeDef = TypedDict(
    "S3BucketTypeDef",
    {
        "bucketName": str,
        "prefix": NotRequired[str],
    },
)
GetAppAuthorizationRequestRequestTypeDef = TypedDict(
    "GetAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "appAuthorizationIdentifier": str,
    },
)
GetAppBundleRequestRequestTypeDef = TypedDict(
    "GetAppBundleRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
    },
)
GetIngestionDestinationRequestRequestTypeDef = TypedDict(
    "GetIngestionDestinationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "ingestionDestinationIdentifier": str,
    },
)
GetIngestionRequestRequestTypeDef = TypedDict(
    "GetIngestionRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
    },
)
IngestionDestinationSummaryTypeDef = TypedDict(
    "IngestionDestinationSummaryTypeDef",
    {
        "arn": str,
    },
)
IngestionSummaryTypeDef = TypedDict(
    "IngestionSummaryTypeDef",
    {
        "arn": str,
        "app": str,
        "tenantId": str,
        "state": IngestionStateType,
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
ListAppAuthorizationsRequestRequestTypeDef = TypedDict(
    "ListAppAuthorizationsRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAppBundlesRequestRequestTypeDef = TypedDict(
    "ListAppBundlesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListIngestionDestinationsRequestRequestTypeDef = TypedDict(
    "ListIngestionDestinationsRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListIngestionsRequestRequestTypeDef = TypedDict(
    "ListIngestionsRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
StartIngestionRequestRequestTypeDef = TypedDict(
    "StartIngestionRequestRequestTypeDef",
    {
        "ingestionIdentifier": str,
        "appBundleIdentifier": str,
    },
)
StartUserAccessTasksRequestRequestTypeDef = TypedDict(
    "StartUserAccessTasksRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "email": str,
    },
)
StopIngestionRequestRequestTypeDef = TypedDict(
    "StopIngestionRequestRequestTypeDef",
    {
        "ingestionIdentifier": str,
        "appBundleIdentifier": str,
    },
)
TaskErrorTypeDef = TypedDict(
    "TaskErrorTypeDef",
    {
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
AppAuthorizationSummaryTypeDef = TypedDict(
    "AppAuthorizationSummaryTypeDef",
    {
        "appAuthorizationArn": str,
        "appBundleArn": str,
        "app": str,
        "tenant": TenantTypeDef,
        "status": AppAuthorizationStatusType,
        "updatedAt": datetime,
    },
)
AppAuthorizationTypeDef = TypedDict(
    "AppAuthorizationTypeDef",
    {
        "appAuthorizationArn": str,
        "appBundleArn": str,
        "app": str,
        "tenant": TenantTypeDef,
        "authType": AuthTypeType,
        "status": AppAuthorizationStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "persona": NotRequired[PersonaType],
        "authUrl": NotRequired[str],
    },
)
ProcessingConfigurationTypeDef = TypedDict(
    "ProcessingConfigurationTypeDef",
    {
        "auditLog": NotRequired[AuditLogProcessingConfigurationTypeDef],
    },
)
ConnectAppAuthorizationRequestRequestTypeDef = TypedDict(
    "ConnectAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "appAuthorizationIdentifier": str,
        "authRequest": NotRequired[AuthRequestTypeDef],
    },
)
CreateAppBundleResponseTypeDef = TypedDict(
    "CreateAppBundleResponseTypeDef",
    {
        "appBundle": AppBundleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppBundleResponseTypeDef = TypedDict(
    "GetAppBundleResponseTypeDef",
    {
        "appBundle": AppBundleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppBundlesResponseTypeDef = TypedDict(
    "ListAppBundlesResponseTypeDef",
    {
        "appBundleSummaryList": List[AppBundleSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppBundleRequestRequestTypeDef = TypedDict(
    "CreateAppBundleRequestRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "customerManagedKeyIdentifier": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateIngestionRequestRequestTypeDef = TypedDict(
    "CreateIngestionRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "app": str,
        "tenantId": str,
        "ingestionType": Literal["auditLog"],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateIngestionResponseTypeDef = TypedDict(
    "CreateIngestionResponseTypeDef",
    {
        "ingestion": IngestionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIngestionResponseTypeDef = TypedDict(
    "GetIngestionResponseTypeDef",
    {
        "ingestion": IngestionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CredentialTypeDef = TypedDict(
    "CredentialTypeDef",
    {
        "oauth2Credential": NotRequired[Oauth2CredentialTypeDef],
        "apiKeyCredential": NotRequired[ApiKeyCredentialTypeDef],
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3Bucket": NotRequired[S3BucketTypeDef],
        "firehoseStream": NotRequired[FirehoseStreamTypeDef],
    },
)
ListIngestionDestinationsResponseTypeDef = TypedDict(
    "ListIngestionDestinationsResponseTypeDef",
    {
        "ingestionDestinations": List[IngestionDestinationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIngestionsResponseTypeDef = TypedDict(
    "ListIngestionsResponseTypeDef",
    {
        "ingestions": List[IngestionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppAuthorizationsRequestListAppAuthorizationsPaginateTypeDef = TypedDict(
    "ListAppAuthorizationsRequestListAppAuthorizationsPaginateTypeDef",
    {
        "appBundleIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAppBundlesRequestListAppBundlesPaginateTypeDef = TypedDict(
    "ListAppBundlesRequestListAppBundlesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIngestionDestinationsRequestListIngestionDestinationsPaginateTypeDef = TypedDict(
    "ListIngestionDestinationsRequestListIngestionDestinationsPaginateTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIngestionsRequestListIngestionsPaginateTypeDef = TypedDict(
    "ListIngestionsRequestListIngestionsPaginateTypeDef",
    {
        "appBundleIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
UserAccessResultItemTypeDef = TypedDict(
    "UserAccessResultItemTypeDef",
    {
        "app": NotRequired[str],
        "tenantId": NotRequired[str],
        "tenantDisplayName": NotRequired[str],
        "taskId": NotRequired[str],
        "resultStatus": NotRequired[ResultStatusType],
        "email": NotRequired[str],
        "userId": NotRequired[str],
        "userFullName": NotRequired[str],
        "userFirstName": NotRequired[str],
        "userLastName": NotRequired[str],
        "userStatus": NotRequired[str],
        "taskError": NotRequired[TaskErrorTypeDef],
    },
)
UserAccessTaskItemTypeDef = TypedDict(
    "UserAccessTaskItemTypeDef",
    {
        "app": str,
        "tenantId": str,
        "taskId": NotRequired[str],
        "error": NotRequired[TaskErrorTypeDef],
    },
)
ConnectAppAuthorizationResponseTypeDef = TypedDict(
    "ConnectAppAuthorizationResponseTypeDef",
    {
        "appAuthorizationSummary": AppAuthorizationSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppAuthorizationsResponseTypeDef = TypedDict(
    "ListAppAuthorizationsResponseTypeDef",
    {
        "appAuthorizationSummaryList": List[AppAuthorizationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppAuthorizationResponseTypeDef = TypedDict(
    "CreateAppAuthorizationResponseTypeDef",
    {
        "appAuthorization": AppAuthorizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppAuthorizationResponseTypeDef = TypedDict(
    "GetAppAuthorizationResponseTypeDef",
    {
        "appAuthorization": AppAuthorizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAppAuthorizationResponseTypeDef = TypedDict(
    "UpdateAppAuthorizationResponseTypeDef",
    {
        "appAuthorization": AppAuthorizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppAuthorizationRequestRequestTypeDef = TypedDict(
    "CreateAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "app": str,
        "credential": CredentialTypeDef,
        "tenant": TenantTypeDef,
        "authType": AuthTypeType,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateAppAuthorizationRequestRequestTypeDef = TypedDict(
    "UpdateAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "appAuthorizationIdentifier": str,
        "credential": NotRequired[CredentialTypeDef],
        "tenant": NotRequired[TenantTypeDef],
    },
)
AuditLogDestinationConfigurationTypeDef = TypedDict(
    "AuditLogDestinationConfigurationTypeDef",
    {
        "destination": DestinationTypeDef,
    },
)
BatchGetUserAccessTasksResponseTypeDef = TypedDict(
    "BatchGetUserAccessTasksResponseTypeDef",
    {
        "userAccessResultsList": List[UserAccessResultItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartUserAccessTasksResponseTypeDef = TypedDict(
    "StartUserAccessTasksResponseTypeDef",
    {
        "userAccessTasksList": List[UserAccessTaskItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "auditLog": NotRequired[AuditLogDestinationConfigurationTypeDef],
    },
)
CreateIngestionDestinationRequestRequestTypeDef = TypedDict(
    "CreateIngestionDestinationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "processingConfiguration": ProcessingConfigurationTypeDef,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
IngestionDestinationTypeDef = TypedDict(
    "IngestionDestinationTypeDef",
    {
        "arn": str,
        "ingestionArn": str,
        "processingConfiguration": ProcessingConfigurationTypeDef,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "status": NotRequired[IngestionDestinationStatusType],
        "statusReason": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
UpdateIngestionDestinationRequestRequestTypeDef = TypedDict(
    "UpdateIngestionDestinationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "ingestionDestinationIdentifier": str,
        "destinationConfiguration": DestinationConfigurationTypeDef,
    },
)
CreateIngestionDestinationResponseTypeDef = TypedDict(
    "CreateIngestionDestinationResponseTypeDef",
    {
        "ingestionDestination": IngestionDestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIngestionDestinationResponseTypeDef = TypedDict(
    "GetIngestionDestinationResponseTypeDef",
    {
        "ingestionDestination": IngestionDestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIngestionDestinationResponseTypeDef = TypedDict(
    "UpdateIngestionDestinationResponseTypeDef",
    {
        "ingestionDestination": IngestionDestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
