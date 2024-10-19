"""
Type annotations for amplifybackend service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/type_defs/)

Usage::

    ```python
    from mypy_boto3_amplifybackend.type_defs import BackendAPIAppSyncAuthSettingsTypeDef

    data: BackendAPIAppSyncAuthSettingsTypeDef = ...
    ```
"""

import sys
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AdditionalConstraintsElementType,
    AuthenticatedElementType,
    AuthResourcesType,
    DeliveryMethodType,
    MFAModeType,
    MfaTypesElementType,
    ModeType,
    OAuthGrantTypeType,
    OAuthScopesElementType,
    RequiredSignUpAttributesElementType,
    ResolutionStrategyType,
    SignInMethodType,
    StatusType,
    UnAuthenticatedElementType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BackendAPIAppSyncAuthSettingsTypeDef",
    "BackendAPIConflictResolutionTypeDef",
    "BackendAuthAppleProviderConfigTypeDef",
    "BackendAuthSocialProviderConfigTypeDef",
    "BackendJobRespObjTypeDef",
    "BackendStoragePermissionsOutputTypeDef",
    "BackendStoragePermissionsTypeDef",
    "CloneBackendRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "EmailSettingsTypeDef",
    "SmsSettingsTypeDef",
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    "SettingsOutputTypeDef",
    "CreateBackendAuthPasswordPolicyConfigOutputTypeDef",
    "CreateBackendAuthPasswordPolicyConfigTypeDef",
    "CreateBackendConfigRequestRequestTypeDef",
    "CreateBackendRequestRequestTypeDef",
    "CreateTokenRequestRequestTypeDef",
    "DeleteBackendAuthRequestRequestTypeDef",
    "DeleteBackendRequestRequestTypeDef",
    "DeleteBackendStorageRequestRequestTypeDef",
    "DeleteTokenRequestRequestTypeDef",
    "GenerateBackendAPIModelsRequestRequestTypeDef",
    "GetBackendAPIModelsRequestRequestTypeDef",
    "GetBackendAuthRequestRequestTypeDef",
    "GetBackendJobRequestRequestTypeDef",
    "GetBackendRequestRequestTypeDef",
    "GetBackendStorageRequestRequestTypeDef",
    "GetTokenRequestRequestTypeDef",
    "ImportBackendAuthRequestRequestTypeDef",
    "ImportBackendStorageRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListBackendJobsRequestRequestTypeDef",
    "ListS3BucketsRequestRequestTypeDef",
    "S3BucketInfoTypeDef",
    "LoginAuthConfigReqObjTypeDef",
    "RemoveAllBackendsRequestRequestTypeDef",
    "RemoveBackendConfigRequestRequestTypeDef",
    "SettingsTypeDef",
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    "UpdateBackendJobRequestRequestTypeDef",
    "BackendAPIAuthTypeTypeDef",
    "SocialProviderSettingsTypeDef",
    "GetBackendStorageResourceConfigTypeDef",
    "BackendStoragePermissionsUnionTypeDef",
    "CloneBackendResponseTypeDef",
    "CreateBackendAPIResponseTypeDef",
    "CreateBackendAuthResponseTypeDef",
    "CreateBackendConfigResponseTypeDef",
    "CreateBackendResponseTypeDef",
    "CreateBackendStorageResponseTypeDef",
    "CreateTokenResponseTypeDef",
    "DeleteBackendAPIResponseTypeDef",
    "DeleteBackendAuthResponseTypeDef",
    "DeleteBackendResponseTypeDef",
    "DeleteBackendStorageResponseTypeDef",
    "DeleteTokenResponseTypeDef",
    "GenerateBackendAPIModelsResponseTypeDef",
    "GetBackendAPIModelsResponseTypeDef",
    "GetBackendJobResponseTypeDef",
    "GetBackendResponseTypeDef",
    "GetTokenResponseTypeDef",
    "ImportBackendAuthResponseTypeDef",
    "ImportBackendStorageResponseTypeDef",
    "ListBackendJobsResponseTypeDef",
    "RemoveAllBackendsResponseTypeDef",
    "RemoveBackendConfigResponseTypeDef",
    "UpdateBackendAPIResponseTypeDef",
    "UpdateBackendAuthResponseTypeDef",
    "UpdateBackendJobResponseTypeDef",
    "UpdateBackendStorageResponseTypeDef",
    "CreateBackendAuthForgotPasswordConfigTypeDef",
    "CreateBackendAuthVerificationMessageConfigTypeDef",
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    "UpdateBackendAuthVerificationMessageConfigTypeDef",
    "CreateBackendAuthMFAConfigOutputTypeDef",
    "CreateBackendAuthPasswordPolicyConfigUnionTypeDef",
    "ListBackendJobsRequestListBackendJobsPaginateTypeDef",
    "ListS3BucketsResponseTypeDef",
    "UpdateBackendConfigRequestRequestTypeDef",
    "UpdateBackendConfigResponseTypeDef",
    "SettingsUnionTypeDef",
    "BackendAPIResourceConfigOutputTypeDef",
    "BackendAPIResourceConfigTypeDef",
    "CreateBackendAuthOAuthConfigOutputTypeDef",
    "CreateBackendAuthOAuthConfigTypeDef",
    "UpdateBackendAuthOAuthConfigTypeDef",
    "GetBackendStorageResponseTypeDef",
    "CreateBackendStorageResourceConfigTypeDef",
    "UpdateBackendStorageResourceConfigTypeDef",
    "CreateBackendAuthMFAConfigTypeDef",
    "UpdateBackendAuthMFAConfigTypeDef",
    "GetBackendAPIResponseTypeDef",
    "CreateBackendAPIRequestRequestTypeDef",
    "DeleteBackendAPIRequestRequestTypeDef",
    "GetBackendAPIRequestRequestTypeDef",
    "UpdateBackendAPIRequestRequestTypeDef",
    "CreateBackendAuthUserPoolConfigOutputTypeDef",
    "CreateBackendAuthOAuthConfigUnionTypeDef",
    "CreateBackendStorageRequestRequestTypeDef",
    "UpdateBackendStorageRequestRequestTypeDef",
    "CreateBackendAuthMFAConfigUnionTypeDef",
    "UpdateBackendAuthUserPoolConfigTypeDef",
    "CreateBackendAuthResourceConfigOutputTypeDef",
    "CreateBackendAuthUserPoolConfigTypeDef",
    "UpdateBackendAuthResourceConfigTypeDef",
    "GetBackendAuthResponseTypeDef",
    "CreateBackendAuthUserPoolConfigUnionTypeDef",
    "UpdateBackendAuthRequestRequestTypeDef",
    "CreateBackendAuthResourceConfigTypeDef",
    "CreateBackendAuthRequestRequestTypeDef",
)

BackendAPIAppSyncAuthSettingsTypeDef = TypedDict(
    "BackendAPIAppSyncAuthSettingsTypeDef",
    {
        "CognitoUserPoolId": NotRequired[str],
        "Description": NotRequired[str],
        "ExpirationTime": NotRequired[float],
        "OpenIDAuthTTL": NotRequired[str],
        "OpenIDClientId": NotRequired[str],
        "OpenIDIatTTL": NotRequired[str],
        "OpenIDIssueURL": NotRequired[str],
        "OpenIDProviderName": NotRequired[str],
    },
)
BackendAPIConflictResolutionTypeDef = TypedDict(
    "BackendAPIConflictResolutionTypeDef",
    {
        "ResolutionStrategy": NotRequired[ResolutionStrategyType],
    },
)
BackendAuthAppleProviderConfigTypeDef = TypedDict(
    "BackendAuthAppleProviderConfigTypeDef",
    {
        "ClientId": NotRequired[str],
        "KeyId": NotRequired[str],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
    },
)
BackendAuthSocialProviderConfigTypeDef = TypedDict(
    "BackendAuthSocialProviderConfigTypeDef",
    {
        "ClientId": NotRequired[str],
        "ClientSecret": NotRequired[str],
    },
)
BackendJobRespObjTypeDef = TypedDict(
    "BackendJobRespObjTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": NotRequired[str],
        "Error": NotRequired[str],
        "JobId": NotRequired[str],
        "Operation": NotRequired[str],
        "Status": NotRequired[str],
        "UpdateTime": NotRequired[str],
    },
)
BackendStoragePermissionsOutputTypeDef = TypedDict(
    "BackendStoragePermissionsOutputTypeDef",
    {
        "Authenticated": List[AuthenticatedElementType],
        "UnAuthenticated": NotRequired[List[UnAuthenticatedElementType]],
    },
)
BackendStoragePermissionsTypeDef = TypedDict(
    "BackendStoragePermissionsTypeDef",
    {
        "Authenticated": Sequence[AuthenticatedElementType],
        "UnAuthenticated": NotRequired[Sequence[UnAuthenticatedElementType]],
    },
)
CloneBackendRequestRequestTypeDef = TypedDict(
    "CloneBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "TargetEnvironmentName": str,
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
EmailSettingsTypeDef = TypedDict(
    "EmailSettingsTypeDef",
    {
        "EmailMessage": NotRequired[str],
        "EmailSubject": NotRequired[str],
    },
)
SmsSettingsTypeDef = TypedDict(
    "SmsSettingsTypeDef",
    {
        "SmsMessage": NotRequired[str],
    },
)
CreateBackendAuthIdentityPoolConfigTypeDef = TypedDict(
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    {
        "IdentityPoolName": str,
        "UnauthenticatedLogin": bool,
    },
)
SettingsOutputTypeDef = TypedDict(
    "SettingsOutputTypeDef",
    {
        "MfaTypes": NotRequired[List[MfaTypesElementType]],
        "SmsMessage": NotRequired[str],
    },
)
CreateBackendAuthPasswordPolicyConfigOutputTypeDef = TypedDict(
    "CreateBackendAuthPasswordPolicyConfigOutputTypeDef",
    {
        "MinimumLength": float,
        "AdditionalConstraints": NotRequired[List[AdditionalConstraintsElementType]],
    },
)
CreateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "CreateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "MinimumLength": float,
        "AdditionalConstraints": NotRequired[Sequence[AdditionalConstraintsElementType]],
    },
)
CreateBackendConfigRequestRequestTypeDef = TypedDict(
    "CreateBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendManagerAppId": NotRequired[str],
    },
)
CreateBackendRequestRequestTypeDef = TypedDict(
    "CreateBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "AppName": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": NotRequired[Mapping[str, Any]],
        "ResourceName": NotRequired[str],
    },
)
CreateTokenRequestRequestTypeDef = TypedDict(
    "CreateTokenRequestRequestTypeDef",
    {
        "AppId": str,
    },
)
DeleteBackendAuthRequestRequestTypeDef = TypedDict(
    "DeleteBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
DeleteBackendRequestRequestTypeDef = TypedDict(
    "DeleteBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
    },
)
DeleteBackendStorageRequestRequestTypeDef = TypedDict(
    "DeleteBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ServiceName": Literal["S3"],
    },
)
DeleteTokenRequestRequestTypeDef = TypedDict(
    "DeleteTokenRequestRequestTypeDef",
    {
        "AppId": str,
        "SessionId": str,
    },
)
GenerateBackendAPIModelsRequestRequestTypeDef = TypedDict(
    "GenerateBackendAPIModelsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
GetBackendAPIModelsRequestRequestTypeDef = TypedDict(
    "GetBackendAPIModelsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
GetBackendAuthRequestRequestTypeDef = TypedDict(
    "GetBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
GetBackendJobRequestRequestTypeDef = TypedDict(
    "GetBackendJobRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
    },
)
GetBackendRequestRequestTypeDef = TypedDict(
    "GetBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": NotRequired[str],
    },
)
GetBackendStorageRequestRequestTypeDef = TypedDict(
    "GetBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
GetTokenRequestRequestTypeDef = TypedDict(
    "GetTokenRequestRequestTypeDef",
    {
        "AppId": str,
        "SessionId": str,
    },
)
ImportBackendAuthRequestRequestTypeDef = TypedDict(
    "ImportBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "NativeClientId": str,
        "UserPoolId": str,
        "WebClientId": str,
        "IdentityPoolId": NotRequired[str],
    },
)
ImportBackendStorageRequestRequestTypeDef = TypedDict(
    "ImportBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
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
ListBackendJobsRequestRequestTypeDef = TypedDict(
    "ListBackendJobsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Operation": NotRequired[str],
        "Status": NotRequired[str],
    },
)
ListS3BucketsRequestRequestTypeDef = TypedDict(
    "ListS3BucketsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
S3BucketInfoTypeDef = TypedDict(
    "S3BucketInfoTypeDef",
    {
        "CreationDate": NotRequired[str],
        "Name": NotRequired[str],
    },
)
LoginAuthConfigReqObjTypeDef = TypedDict(
    "LoginAuthConfigReqObjTypeDef",
    {
        "AwsCognitoIdentityPoolId": NotRequired[str],
        "AwsCognitoRegion": NotRequired[str],
        "AwsUserPoolsId": NotRequired[str],
        "AwsUserPoolsWebClientId": NotRequired[str],
    },
)
RemoveAllBackendsRequestRequestTypeDef = TypedDict(
    "RemoveAllBackendsRequestRequestTypeDef",
    {
        "AppId": str,
        "CleanAmplifyApp": NotRequired[bool],
    },
)
RemoveBackendConfigRequestRequestTypeDef = TypedDict(
    "RemoveBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
    },
)
SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "MfaTypes": NotRequired[Sequence[MfaTypesElementType]],
        "SmsMessage": NotRequired[str],
    },
)
UpdateBackendAuthIdentityPoolConfigTypeDef = TypedDict(
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    {
        "UnauthenticatedLogin": NotRequired[bool],
    },
)
UpdateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "AdditionalConstraints": NotRequired[Sequence[AdditionalConstraintsElementType]],
        "MinimumLength": NotRequired[float],
    },
)
UpdateBackendJobRequestRequestTypeDef = TypedDict(
    "UpdateBackendJobRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Operation": NotRequired[str],
        "Status": NotRequired[str],
    },
)
BackendAPIAuthTypeTypeDef = TypedDict(
    "BackendAPIAuthTypeTypeDef",
    {
        "Mode": NotRequired[ModeType],
        "Settings": NotRequired[BackendAPIAppSyncAuthSettingsTypeDef],
    },
)
SocialProviderSettingsTypeDef = TypedDict(
    "SocialProviderSettingsTypeDef",
    {
        "Facebook": NotRequired[BackendAuthSocialProviderConfigTypeDef],
        "Google": NotRequired[BackendAuthSocialProviderConfigTypeDef],
        "LoginWithAmazon": NotRequired[BackendAuthSocialProviderConfigTypeDef],
        "SignInWithApple": NotRequired[BackendAuthAppleProviderConfigTypeDef],
    },
)
GetBackendStorageResourceConfigTypeDef = TypedDict(
    "GetBackendStorageResourceConfigTypeDef",
    {
        "Imported": bool,
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
        "Permissions": NotRequired[BackendStoragePermissionsOutputTypeDef],
    },
)
BackendStoragePermissionsUnionTypeDef = Union[
    BackendStoragePermissionsTypeDef, BackendStoragePermissionsOutputTypeDef
]
CloneBackendResponseTypeDef = TypedDict(
    "CloneBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendAPIResponseTypeDef = TypedDict(
    "CreateBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendAuthResponseTypeDef = TypedDict(
    "CreateBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendConfigResponseTypeDef = TypedDict(
    "CreateBackendConfigResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendResponseTypeDef = TypedDict(
    "CreateBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendStorageResponseTypeDef = TypedDict(
    "CreateBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "AppId": str,
        "ChallengeCode": str,
        "SessionId": str,
        "Ttl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBackendAPIResponseTypeDef = TypedDict(
    "DeleteBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBackendAuthResponseTypeDef = TypedDict(
    "DeleteBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBackendResponseTypeDef = TypedDict(
    "DeleteBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBackendStorageResponseTypeDef = TypedDict(
    "DeleteBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTokenResponseTypeDef = TypedDict(
    "DeleteTokenResponseTypeDef",
    {
        "IsSuccess": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateBackendAPIModelsResponseTypeDef = TypedDict(
    "GenerateBackendAPIModelsResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBackendAPIModelsResponseTypeDef = TypedDict(
    "GetBackendAPIModelsResponseTypeDef",
    {
        "Models": str,
        "Status": StatusType,
        "ModelIntrospectionSchema": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBackendJobResponseTypeDef = TypedDict(
    "GetBackendJobResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBackendResponseTypeDef = TypedDict(
    "GetBackendResponseTypeDef",
    {
        "AmplifyFeatureFlags": str,
        "AmplifyMetaConfig": str,
        "AppId": str,
        "AppName": str,
        "BackendEnvironmentList": List[str],
        "BackendEnvironmentName": str,
        "Error": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTokenResponseTypeDef = TypedDict(
    "GetTokenResponseTypeDef",
    {
        "AppId": str,
        "ChallengeCode": str,
        "SessionId": str,
        "Ttl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportBackendAuthResponseTypeDef = TypedDict(
    "ImportBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportBackendStorageResponseTypeDef = TypedDict(
    "ImportBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBackendJobsResponseTypeDef = TypedDict(
    "ListBackendJobsResponseTypeDef",
    {
        "Jobs": List[BackendJobRespObjTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RemoveAllBackendsResponseTypeDef = TypedDict(
    "RemoveAllBackendsResponseTypeDef",
    {
        "AppId": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveBackendConfigResponseTypeDef = TypedDict(
    "RemoveBackendConfigResponseTypeDef",
    {
        "Error": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBackendAPIResponseTypeDef = TypedDict(
    "UpdateBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBackendAuthResponseTypeDef = TypedDict(
    "UpdateBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBackendJobResponseTypeDef = TypedDict(
    "UpdateBackendJobResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBackendStorageResponseTypeDef = TypedDict(
    "UpdateBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "CreateBackendAuthForgotPasswordConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
        "EmailSettings": NotRequired[EmailSettingsTypeDef],
        "SmsSettings": NotRequired[SmsSettingsTypeDef],
    },
)
CreateBackendAuthVerificationMessageConfigTypeDef = TypedDict(
    "CreateBackendAuthVerificationMessageConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
        "EmailSettings": NotRequired[EmailSettingsTypeDef],
        "SmsSettings": NotRequired[SmsSettingsTypeDef],
    },
)
UpdateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    {
        "DeliveryMethod": NotRequired[DeliveryMethodType],
        "EmailSettings": NotRequired[EmailSettingsTypeDef],
        "SmsSettings": NotRequired[SmsSettingsTypeDef],
    },
)
UpdateBackendAuthVerificationMessageConfigTypeDef = TypedDict(
    "UpdateBackendAuthVerificationMessageConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
        "EmailSettings": NotRequired[EmailSettingsTypeDef],
        "SmsSettings": NotRequired[SmsSettingsTypeDef],
    },
)
CreateBackendAuthMFAConfigOutputTypeDef = TypedDict(
    "CreateBackendAuthMFAConfigOutputTypeDef",
    {
        "MFAMode": MFAModeType,
        "Settings": NotRequired[SettingsOutputTypeDef],
    },
)
CreateBackendAuthPasswordPolicyConfigUnionTypeDef = Union[
    CreateBackendAuthPasswordPolicyConfigTypeDef, CreateBackendAuthPasswordPolicyConfigOutputTypeDef
]
ListBackendJobsRequestListBackendJobsPaginateTypeDef = TypedDict(
    "ListBackendJobsRequestListBackendJobsPaginateTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": NotRequired[str],
        "Operation": NotRequired[str],
        "Status": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListS3BucketsResponseTypeDef = TypedDict(
    "ListS3BucketsResponseTypeDef",
    {
        "Buckets": List[S3BucketInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateBackendConfigRequestRequestTypeDef = TypedDict(
    "UpdateBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
        "LoginAuthConfig": NotRequired[LoginAuthConfigReqObjTypeDef],
    },
)
UpdateBackendConfigResponseTypeDef = TypedDict(
    "UpdateBackendConfigResponseTypeDef",
    {
        "AppId": str,
        "BackendManagerAppId": str,
        "Error": str,
        "LoginAuthConfig": LoginAuthConfigReqObjTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SettingsUnionTypeDef = Union[SettingsTypeDef, SettingsOutputTypeDef]
BackendAPIResourceConfigOutputTypeDef = TypedDict(
    "BackendAPIResourceConfigOutputTypeDef",
    {
        "AdditionalAuthTypes": NotRequired[List[BackendAPIAuthTypeTypeDef]],
        "ApiName": NotRequired[str],
        "ConflictResolution": NotRequired[BackendAPIConflictResolutionTypeDef],
        "DefaultAuthType": NotRequired[BackendAPIAuthTypeTypeDef],
        "Service": NotRequired[str],
        "TransformSchema": NotRequired[str],
    },
)
BackendAPIResourceConfigTypeDef = TypedDict(
    "BackendAPIResourceConfigTypeDef",
    {
        "AdditionalAuthTypes": NotRequired[Sequence[BackendAPIAuthTypeTypeDef]],
        "ApiName": NotRequired[str],
        "ConflictResolution": NotRequired[BackendAPIConflictResolutionTypeDef],
        "DefaultAuthType": NotRequired[BackendAPIAuthTypeTypeDef],
        "Service": NotRequired[str],
        "TransformSchema": NotRequired[str],
    },
)
CreateBackendAuthOAuthConfigOutputTypeDef = TypedDict(
    "CreateBackendAuthOAuthConfigOutputTypeDef",
    {
        "OAuthGrantType": OAuthGrantTypeType,
        "OAuthScopes": List[OAuthScopesElementType],
        "RedirectSignInURIs": List[str],
        "RedirectSignOutURIs": List[str],
        "DomainPrefix": NotRequired[str],
        "SocialProviderSettings": NotRequired[SocialProviderSettingsTypeDef],
    },
)
CreateBackendAuthOAuthConfigTypeDef = TypedDict(
    "CreateBackendAuthOAuthConfigTypeDef",
    {
        "OAuthGrantType": OAuthGrantTypeType,
        "OAuthScopes": Sequence[OAuthScopesElementType],
        "RedirectSignInURIs": Sequence[str],
        "RedirectSignOutURIs": Sequence[str],
        "DomainPrefix": NotRequired[str],
        "SocialProviderSettings": NotRequired[SocialProviderSettingsTypeDef],
    },
)
UpdateBackendAuthOAuthConfigTypeDef = TypedDict(
    "UpdateBackendAuthOAuthConfigTypeDef",
    {
        "DomainPrefix": NotRequired[str],
        "OAuthGrantType": NotRequired[OAuthGrantTypeType],
        "OAuthScopes": NotRequired[Sequence[OAuthScopesElementType]],
        "RedirectSignInURIs": NotRequired[Sequence[str]],
        "RedirectSignOutURIs": NotRequired[Sequence[str]],
        "SocialProviderSettings": NotRequired[SocialProviderSettingsTypeDef],
    },
)
GetBackendStorageResponseTypeDef = TypedDict(
    "GetBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": GetBackendStorageResourceConfigTypeDef,
        "ResourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendStorageResourceConfigTypeDef = TypedDict(
    "CreateBackendStorageResourceConfigTypeDef",
    {
        "Permissions": BackendStoragePermissionsUnionTypeDef,
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
    },
)
UpdateBackendStorageResourceConfigTypeDef = TypedDict(
    "UpdateBackendStorageResourceConfigTypeDef",
    {
        "Permissions": BackendStoragePermissionsUnionTypeDef,
        "ServiceName": Literal["S3"],
    },
)
CreateBackendAuthMFAConfigTypeDef = TypedDict(
    "CreateBackendAuthMFAConfigTypeDef",
    {
        "MFAMode": MFAModeType,
        "Settings": NotRequired[SettingsUnionTypeDef],
    },
)
UpdateBackendAuthMFAConfigTypeDef = TypedDict(
    "UpdateBackendAuthMFAConfigTypeDef",
    {
        "MFAMode": NotRequired[MFAModeType],
        "Settings": NotRequired[SettingsUnionTypeDef],
    },
)
GetBackendAPIResponseTypeDef = TypedDict(
    "GetBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "ResourceConfig": BackendAPIResourceConfigOutputTypeDef,
        "ResourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendAPIRequestRequestTypeDef = TypedDict(
    "CreateBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": BackendAPIResourceConfigTypeDef,
        "ResourceName": str,
    },
)
DeleteBackendAPIRequestRequestTypeDef = TypedDict(
    "DeleteBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ResourceConfig": NotRequired[BackendAPIResourceConfigTypeDef],
    },
)
GetBackendAPIRequestRequestTypeDef = TypedDict(
    "GetBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ResourceConfig": NotRequired[BackendAPIResourceConfigTypeDef],
    },
)
UpdateBackendAPIRequestRequestTypeDef = TypedDict(
    "UpdateBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ResourceConfig": NotRequired[BackendAPIResourceConfigTypeDef],
    },
)
CreateBackendAuthUserPoolConfigOutputTypeDef = TypedDict(
    "CreateBackendAuthUserPoolConfigOutputTypeDef",
    {
        "RequiredSignUpAttributes": List[RequiredSignUpAttributesElementType],
        "SignInMethod": SignInMethodType,
        "UserPoolName": str,
        "ForgotPassword": NotRequired[CreateBackendAuthForgotPasswordConfigTypeDef],
        "Mfa": NotRequired[CreateBackendAuthMFAConfigOutputTypeDef],
        "OAuth": NotRequired[CreateBackendAuthOAuthConfigOutputTypeDef],
        "PasswordPolicy": NotRequired[CreateBackendAuthPasswordPolicyConfigOutputTypeDef],
        "VerificationMessage": NotRequired[CreateBackendAuthVerificationMessageConfigTypeDef],
    },
)
CreateBackendAuthOAuthConfigUnionTypeDef = Union[
    CreateBackendAuthOAuthConfigTypeDef, CreateBackendAuthOAuthConfigOutputTypeDef
]
CreateBackendStorageRequestRequestTypeDef = TypedDict(
    "CreateBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": CreateBackendStorageResourceConfigTypeDef,
        "ResourceName": str,
    },
)
UpdateBackendStorageRequestRequestTypeDef = TypedDict(
    "UpdateBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": UpdateBackendStorageResourceConfigTypeDef,
        "ResourceName": str,
    },
)
CreateBackendAuthMFAConfigUnionTypeDef = Union[
    CreateBackendAuthMFAConfigTypeDef, CreateBackendAuthMFAConfigOutputTypeDef
]
UpdateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "UpdateBackendAuthUserPoolConfigTypeDef",
    {
        "ForgotPassword": NotRequired[UpdateBackendAuthForgotPasswordConfigTypeDef],
        "Mfa": NotRequired[UpdateBackendAuthMFAConfigTypeDef],
        "OAuth": NotRequired[UpdateBackendAuthOAuthConfigTypeDef],
        "PasswordPolicy": NotRequired[UpdateBackendAuthPasswordPolicyConfigTypeDef],
        "VerificationMessage": NotRequired[UpdateBackendAuthVerificationMessageConfigTypeDef],
    },
)
CreateBackendAuthResourceConfigOutputTypeDef = TypedDict(
    "CreateBackendAuthResourceConfigOutputTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": CreateBackendAuthUserPoolConfigOutputTypeDef,
        "IdentityPoolConfigs": NotRequired[CreateBackendAuthIdentityPoolConfigTypeDef],
    },
)
CreateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "CreateBackendAuthUserPoolConfigTypeDef",
    {
        "RequiredSignUpAttributes": Sequence[RequiredSignUpAttributesElementType],
        "SignInMethod": SignInMethodType,
        "UserPoolName": str,
        "ForgotPassword": NotRequired[CreateBackendAuthForgotPasswordConfigTypeDef],
        "Mfa": NotRequired[CreateBackendAuthMFAConfigUnionTypeDef],
        "OAuth": NotRequired[CreateBackendAuthOAuthConfigUnionTypeDef],
        "PasswordPolicy": NotRequired[CreateBackendAuthPasswordPolicyConfigUnionTypeDef],
        "VerificationMessage": NotRequired[CreateBackendAuthVerificationMessageConfigTypeDef],
    },
)
UpdateBackendAuthResourceConfigTypeDef = TypedDict(
    "UpdateBackendAuthResourceConfigTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": UpdateBackendAuthUserPoolConfigTypeDef,
        "IdentityPoolConfigs": NotRequired[UpdateBackendAuthIdentityPoolConfigTypeDef],
    },
)
GetBackendAuthResponseTypeDef = TypedDict(
    "GetBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "ResourceConfig": CreateBackendAuthResourceConfigOutputTypeDef,
        "ResourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackendAuthUserPoolConfigUnionTypeDef = Union[
    CreateBackendAuthUserPoolConfigTypeDef, CreateBackendAuthUserPoolConfigOutputTypeDef
]
UpdateBackendAuthRequestRequestTypeDef = TypedDict(
    "UpdateBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": UpdateBackendAuthResourceConfigTypeDef,
        "ResourceName": str,
    },
)
CreateBackendAuthResourceConfigTypeDef = TypedDict(
    "CreateBackendAuthResourceConfigTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": CreateBackendAuthUserPoolConfigUnionTypeDef,
        "IdentityPoolConfigs": NotRequired[CreateBackendAuthIdentityPoolConfigTypeDef],
    },
)
CreateBackendAuthRequestRequestTypeDef = TypedDict(
    "CreateBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": CreateBackendAuthResourceConfigTypeDef,
        "ResourceName": str,
    },
)
