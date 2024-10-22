"""
Type annotations for cognito-idp service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/type_defs/)

Usage::

    ```python
    from mypy_boto3_cognito_idp.type_defs import RecoveryOptionTypeTypeDef

    data: RecoveryOptionTypeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AccountTakeoverEventActionTypeType,
    AdvancedSecurityEnabledModeTypeType,
    AdvancedSecurityModeTypeType,
    AliasAttributeTypeType,
    AttributeDataTypeType,
    AuthFlowTypeType,
    ChallengeNameType,
    ChallengeNameTypeType,
    ChallengeResponseType,
    CompromisedCredentialsEventActionTypeType,
    DefaultEmailOptionTypeType,
    DeletionProtectionTypeType,
    DeliveryMediumTypeType,
    DeviceRememberedStatusTypeType,
    DomainStatusTypeType,
    EmailSendingAccountTypeType,
    EventFilterTypeType,
    EventResponseTypeType,
    EventSourceNameType,
    EventTypeType,
    ExplicitAuthFlowsTypeType,
    FeedbackValueTypeType,
    IdentityProviderTypeTypeType,
    LogLevelType,
    MessageActionTypeType,
    OAuthFlowTypeType,
    PreTokenGenerationLambdaVersionTypeType,
    PreventUserExistenceErrorTypesType,
    RecoveryOptionNameTypeType,
    RiskDecisionTypeType,
    RiskLevelTypeType,
    StatusTypeType,
    TimeUnitsTypeType,
    UserImportJobStatusTypeType,
    UsernameAttributeTypeType,
    UserPoolMfaTypeType,
    UserStatusTypeType,
    VerifiedAttributeTypeType,
    VerifySoftwareTokenResponseTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "RecoveryOptionTypeTypeDef",
    "AccountTakeoverActionTypeTypeDef",
    "AdminAddUserToGroupRequestRequestTypeDef",
    "AdminConfirmSignUpRequestRequestTypeDef",
    "MessageTemplateTypeTypeDef",
    "AttributeTypeTypeDef",
    "ResponseMetadataTypeDef",
    "AdminDeleteUserAttributesRequestRequestTypeDef",
    "AdminDeleteUserRequestRequestTypeDef",
    "ProviderUserIdentifierTypeTypeDef",
    "AdminDisableUserRequestRequestTypeDef",
    "AdminEnableUserRequestRequestTypeDef",
    "AdminForgetDeviceRequestRequestTypeDef",
    "AdminGetDeviceRequestRequestTypeDef",
    "AdminGetUserRequestRequestTypeDef",
    "MFAOptionTypeTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AdminListDevicesRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "AdminListGroupsForUserRequestRequestTypeDef",
    "GroupTypeTypeDef",
    "AdminListUserAuthEventsRequestRequestTypeDef",
    "AdminRemoveUserFromGroupRequestRequestTypeDef",
    "AdminResetUserPasswordRequestRequestTypeDef",
    "EmailMfaSettingsTypeTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "AdminSetUserPasswordRequestRequestTypeDef",
    "AdminUpdateAuthEventFeedbackRequestRequestTypeDef",
    "AdminUpdateDeviceStatusRequestRequestTypeDef",
    "AdminUserGlobalSignOutRequestRequestTypeDef",
    "AdvancedSecurityAdditionalFlowsTypeTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AssociateSoftwareTokenRequestRequestTypeDef",
    "ChallengeResponseTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "NewDeviceMetadataTypeTypeDef",
    "BlobTypeDef",
    "ChangePasswordRequestRequestTypeDef",
    "CloudWatchLogsConfigurationTypeTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "UserContextDataTypeTypeDef",
    "HttpHeaderTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "IdentityProviderTypeTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "CreateUserImportJobRequestRequestTypeDef",
    "UserImportJobTypeTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "SmsConfigurationTypeTypeDef",
    "UserAttributeUpdateSettingsTypeTypeDef",
    "UsernameConfigurationTypeTypeDef",
    "VerificationMessageTemplateTypeTypeDef",
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteResourceServerRequestRequestTypeDef",
    "DeleteUserAttributesRequestRequestTypeDef",
    "DeleteUserPoolClientRequestRequestTypeDef",
    "DeleteUserPoolDomainRequestRequestTypeDef",
    "DeleteUserPoolRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeIdentityProviderRequestRequestTypeDef",
    "DescribeResourceServerRequestRequestTypeDef",
    "DescribeRiskConfigurationRequestRequestTypeDef",
    "DescribeUserImportJobRequestRequestTypeDef",
    "DescribeUserPoolClientRequestRequestTypeDef",
    "DescribeUserPoolDomainRequestRequestTypeDef",
    "DescribeUserPoolRequestRequestTypeDef",
    "EmailMfaConfigTypeTypeDef",
    "FirehoseConfigurationTypeTypeDef",
    "ForgetDeviceRequestRequestTypeDef",
    "GetCSVHeaderRequestRequestTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetIdentityProviderByIdentifierRequestRequestTypeDef",
    "GetLogDeliveryConfigurationRequestRequestTypeDef",
    "GetSigningCertificateRequestRequestTypeDef",
    "GetUICustomizationRequestRequestTypeDef",
    "UICustomizationTypeTypeDef",
    "GetUserAttributeVerificationCodeRequestRequestTypeDef",
    "GetUserPoolMfaConfigRequestRequestTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "GetUserRequestRequestTypeDef",
    "GlobalSignOutRequestRequestTypeDef",
    "PreTokenGenerationVersionConfigTypeTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ProviderDescriptionTypeDef",
    "ListResourceServersRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListUserImportJobsRequestRequestTypeDef",
    "ListUserPoolClientsRequestRequestTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "ListUserPoolsRequestRequestTypeDef",
    "ListUsersInGroupRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "S3ConfigurationTypeTypeDef",
    "NotifyEmailTypeTypeDef",
    "NumberAttributeConstraintsTypeTypeDef",
    "PasswordPolicyTypeTypeDef",
    "RevokeTokenRequestRequestTypeDef",
    "RiskExceptionConfigurationTypeOutputTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "StartUserImportJobRequestRequestTypeDef",
    "StopUserImportJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAuthEventFeedbackRequestRequestTypeDef",
    "UpdateDeviceStatusRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UserAttributeUpdateSettingsTypeOutputTypeDef",
    "VerifySoftwareTokenRequestRequestTypeDef",
    "VerifyUserAttributeRequestRequestTypeDef",
    "AccountRecoverySettingTypeOutputTypeDef",
    "AccountRecoverySettingTypeTypeDef",
    "AccountTakeoverActionsTypeTypeDef",
    "AdminCreateUserConfigTypeTypeDef",
    "AdminCreateUserRequestRequestTypeDef",
    "AdminUpdateUserAttributesRequestRequestTypeDef",
    "DeviceTypeTypeDef",
    "UpdateUserAttributesRequestRequestTypeDef",
    "AssociateSoftwareTokenResponseTypeDef",
    "ConfirmDeviceResponseTypeDef",
    "CreateUserPoolDomainResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCSVHeaderResponseTypeDef",
    "GetSigningCertificateResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateUserPoolDomainResponseTypeDef",
    "VerifySoftwareTokenResponseTypeDef",
    "AdminDisableProviderForUserRequestRequestTypeDef",
    "AdminLinkProviderForUserRequestRequestTypeDef",
    "AdminGetUserResponseTypeDef",
    "AdminSetUserSettingsRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "SetUserSettingsRequestRequestTypeDef",
    "UserTypeTypeDef",
    "AdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef",
    "AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    "ListResourceServersRequestListResourceServersPaginateTypeDef",
    "ListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef",
    "ListUserPoolsRequestListUserPoolsPaginateTypeDef",
    "ListUsersInGroupRequestListUsersInGroupPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "GetGroupResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "UpdateGroupResponseTypeDef",
    "AdminSetUserMFAPreferenceRequestRequestTypeDef",
    "SetUserMFAPreferenceRequestRequestTypeDef",
    "UserPoolAddOnsTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "SetUICustomizationRequestRequestTypeDef",
    "ForgotPasswordResponseTypeDef",
    "GetUserAttributeVerificationCodeResponseTypeDef",
    "ResendConfirmationCodeResponseTypeDef",
    "SignUpResponseTypeDef",
    "UpdateUserAttributesResponseTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeOutputTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "ConfirmDeviceRequestRequestTypeDef",
    "ConfirmForgotPasswordRequestRequestTypeDef",
    "ConfirmSignUpRequestRequestTypeDef",
    "ForgotPasswordRequestRequestTypeDef",
    "InitiateAuthRequestRequestTypeDef",
    "ResendConfirmationCodeRequestRequestTypeDef",
    "RespondToAuthChallengeRequestRequestTypeDef",
    "SignUpRequestRequestTypeDef",
    "ContextDataTypeTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "DescribeIdentityProviderResponseTypeDef",
    "GetIdentityProviderByIdentifierResponseTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "CreateResourceServerRequestRequestTypeDef",
    "ResourceServerTypeTypeDef",
    "UpdateResourceServerRequestRequestTypeDef",
    "CreateUserImportJobResponseTypeDef",
    "DescribeUserImportJobResponseTypeDef",
    "ListUserImportJobsResponseTypeDef",
    "StartUserImportJobResponseTypeDef",
    "StopUserImportJobResponseTypeDef",
    "CreateUserPoolClientRequestRequestTypeDef",
    "UpdateUserPoolClientRequestRequestTypeDef",
    "UserPoolClientTypeTypeDef",
    "CreateUserPoolDomainRequestRequestTypeDef",
    "DomainDescriptionTypeTypeDef",
    "UpdateUserPoolDomainRequestRequestTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "GetUICustomizationResponseTypeDef",
    "SetUICustomizationResponseTypeDef",
    "LambdaConfigTypeTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "LogConfigurationTypeTypeDef",
    "NotifyConfigurationTypeTypeDef",
    "UserPoolPolicyTypeTypeDef",
    "SchemaAttributeTypeTypeDef",
    "AdminGetDeviceResponseTypeDef",
    "AdminListDevicesResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "AdminCreateUserResponseTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "AdminInitiateAuthResponseTypeDef",
    "AdminRespondToAuthChallengeResponseTypeDef",
    "InitiateAuthResponseTypeDef",
    "RespondToAuthChallengeResponseTypeDef",
    "AdminInitiateAuthRequestRequestTypeDef",
    "AdminRespondToAuthChallengeRequestRequestTypeDef",
    "CreateResourceServerResponseTypeDef",
    "DescribeResourceServerResponseTypeDef",
    "ListResourceServersResponseTypeDef",
    "UpdateResourceServerResponseTypeDef",
    "CreateUserPoolClientResponseTypeDef",
    "DescribeUserPoolClientResponseTypeDef",
    "UpdateUserPoolClientResponseTypeDef",
    "DescribeUserPoolDomainResponseTypeDef",
    "GetUserPoolMfaConfigResponseTypeDef",
    "SetUserPoolMfaConfigRequestRequestTypeDef",
    "SetUserPoolMfaConfigResponseTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "LogDeliveryConfigurationTypeTypeDef",
    "SetLogDeliveryConfigurationRequestRequestTypeDef",
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    "UpdateUserPoolRequestRequestTypeDef",
    "AddCustomAttributesRequestRequestTypeDef",
    "CreateUserPoolRequestRequestTypeDef",
    "UserPoolTypeTypeDef",
    "ListUserPoolsResponseTypeDef",
    "GetLogDeliveryConfigurationResponseTypeDef",
    "SetLogDeliveryConfigurationResponseTypeDef",
    "RiskConfigurationTypeTypeDef",
    "SetRiskConfigurationRequestRequestTypeDef",
    "CreateUserPoolResponseTypeDef",
    "DescribeUserPoolResponseTypeDef",
    "DescribeRiskConfigurationResponseTypeDef",
    "SetRiskConfigurationResponseTypeDef",
)

RecoveryOptionTypeTypeDef = TypedDict(
    "RecoveryOptionTypeTypeDef",
    {
        "Priority": int,
        "Name": RecoveryOptionNameTypeType,
    },
)
AccountTakeoverActionTypeTypeDef = TypedDict(
    "AccountTakeoverActionTypeTypeDef",
    {
        "Notify": bool,
        "EventAction": AccountTakeoverEventActionTypeType,
    },
)
AdminAddUserToGroupRequestRequestTypeDef = TypedDict(
    "AdminAddUserToGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)
AdminConfirmSignUpRequestRequestTypeDef = TypedDict(
    "AdminConfirmSignUpRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
MessageTemplateTypeTypeDef = TypedDict(
    "MessageTemplateTypeTypeDef",
    {
        "SMSMessage": NotRequired[str],
        "EmailMessage": NotRequired[str],
        "EmailSubject": NotRequired[str],
    },
)
AttributeTypeTypeDef = TypedDict(
    "AttributeTypeTypeDef",
    {
        "Name": str,
        "Value": NotRequired[str],
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
AdminDeleteUserAttributesRequestRequestTypeDef = TypedDict(
    "AdminDeleteUserAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributeNames": Sequence[str],
    },
)
AdminDeleteUserRequestRequestTypeDef = TypedDict(
    "AdminDeleteUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
ProviderUserIdentifierTypeTypeDef = TypedDict(
    "ProviderUserIdentifierTypeTypeDef",
    {
        "ProviderName": NotRequired[str],
        "ProviderAttributeName": NotRequired[str],
        "ProviderAttributeValue": NotRequired[str],
    },
)
AdminDisableUserRequestRequestTypeDef = TypedDict(
    "AdminDisableUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
AdminEnableUserRequestRequestTypeDef = TypedDict(
    "AdminEnableUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
AdminForgetDeviceRequestRequestTypeDef = TypedDict(
    "AdminForgetDeviceRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
    },
)
AdminGetDeviceRequestRequestTypeDef = TypedDict(
    "AdminGetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
        "UserPoolId": str,
        "Username": str,
    },
)
AdminGetUserRequestRequestTypeDef = TypedDict(
    "AdminGetUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
MFAOptionTypeTypeDef = TypedDict(
    "MFAOptionTypeTypeDef",
    {
        "DeliveryMedium": NotRequired[DeliveryMediumTypeType],
        "AttributeName": NotRequired[str],
    },
)
AnalyticsMetadataTypeTypeDef = TypedDict(
    "AnalyticsMetadataTypeTypeDef",
    {
        "AnalyticsEndpointId": NotRequired[str],
    },
)
AdminListDevicesRequestRequestTypeDef = TypedDict(
    "AdminListDevicesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "Limit": NotRequired[int],
        "PaginationToken": NotRequired[str],
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
AdminListGroupsForUserRequestRequestTypeDef = TypedDict(
    "AdminListGroupsForUserRequestRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GroupTypeTypeDef = TypedDict(
    "GroupTypeTypeDef",
    {
        "GroupName": NotRequired[str],
        "UserPoolId": NotRequired[str],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Precedence": NotRequired[int],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)
AdminListUserAuthEventsRequestRequestTypeDef = TypedDict(
    "AdminListUserAuthEventsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
AdminRemoveUserFromGroupRequestRequestTypeDef = TypedDict(
    "AdminRemoveUserFromGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)
AdminResetUserPasswordRequestRequestTypeDef = TypedDict(
    "AdminResetUserPasswordRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
EmailMfaSettingsTypeTypeDef = TypedDict(
    "EmailMfaSettingsTypeTypeDef",
    {
        "Enabled": NotRequired[bool],
        "PreferredMfa": NotRequired[bool],
    },
)
SMSMfaSettingsTypeTypeDef = TypedDict(
    "SMSMfaSettingsTypeTypeDef",
    {
        "Enabled": NotRequired[bool],
        "PreferredMfa": NotRequired[bool],
    },
)
SoftwareTokenMfaSettingsTypeTypeDef = TypedDict(
    "SoftwareTokenMfaSettingsTypeTypeDef",
    {
        "Enabled": NotRequired[bool],
        "PreferredMfa": NotRequired[bool],
    },
)
AdminSetUserPasswordRequestRequestTypeDef = TypedDict(
    "AdminSetUserPasswordRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "Password": str,
        "Permanent": NotRequired[bool],
    },
)
AdminUpdateAuthEventFeedbackRequestRequestTypeDef = TypedDict(
    "AdminUpdateAuthEventFeedbackRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)
AdminUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "AdminUpdateDeviceStatusRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
        "DeviceRememberedStatus": NotRequired[DeviceRememberedStatusTypeType],
    },
)
AdminUserGlobalSignOutRequestRequestTypeDef = TypedDict(
    "AdminUserGlobalSignOutRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
AdvancedSecurityAdditionalFlowsTypeTypeDef = TypedDict(
    "AdvancedSecurityAdditionalFlowsTypeTypeDef",
    {
        "CustomAuthMode": NotRequired[AdvancedSecurityEnabledModeTypeType],
    },
)
AnalyticsConfigurationTypeTypeDef = TypedDict(
    "AnalyticsConfigurationTypeTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ApplicationArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ExternalId": NotRequired[str],
        "UserDataShared": NotRequired[bool],
    },
)
AssociateSoftwareTokenRequestRequestTypeDef = TypedDict(
    "AssociateSoftwareTokenRequestRequestTypeDef",
    {
        "AccessToken": NotRequired[str],
        "Session": NotRequired[str],
    },
)
ChallengeResponseTypeTypeDef = TypedDict(
    "ChallengeResponseTypeTypeDef",
    {
        "ChallengeName": NotRequired[ChallengeNameType],
        "ChallengeResponse": NotRequired[ChallengeResponseType],
    },
)
EventContextDataTypeTypeDef = TypedDict(
    "EventContextDataTypeTypeDef",
    {
        "IpAddress": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Timezone": NotRequired[str],
        "City": NotRequired[str],
        "Country": NotRequired[str],
    },
)
EventFeedbackTypeTypeDef = TypedDict(
    "EventFeedbackTypeTypeDef",
    {
        "FeedbackValue": FeedbackValueTypeType,
        "Provider": str,
        "FeedbackDate": NotRequired[datetime],
    },
)
EventRiskTypeTypeDef = TypedDict(
    "EventRiskTypeTypeDef",
    {
        "RiskDecision": NotRequired[RiskDecisionTypeType],
        "RiskLevel": NotRequired[RiskLevelTypeType],
        "CompromisedCredentialsDetected": NotRequired[bool],
    },
)
NewDeviceMetadataTypeTypeDef = TypedDict(
    "NewDeviceMetadataTypeTypeDef",
    {
        "DeviceKey": NotRequired[str],
        "DeviceGroupKey": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ChangePasswordRequestRequestTypeDef = TypedDict(
    "ChangePasswordRequestRequestTypeDef",
    {
        "PreviousPassword": str,
        "ProposedPassword": str,
        "AccessToken": str,
    },
)
CloudWatchLogsConfigurationTypeTypeDef = TypedDict(
    "CloudWatchLogsConfigurationTypeTypeDef",
    {
        "LogGroupArn": NotRequired[str],
    },
)
CodeDeliveryDetailsTypeTypeDef = TypedDict(
    "CodeDeliveryDetailsTypeTypeDef",
    {
        "Destination": NotRequired[str],
        "DeliveryMedium": NotRequired[DeliveryMediumTypeType],
        "AttributeName": NotRequired[str],
    },
)
CompromisedCredentialsActionsTypeTypeDef = TypedDict(
    "CompromisedCredentialsActionsTypeTypeDef",
    {
        "EventAction": CompromisedCredentialsEventActionTypeType,
    },
)
DeviceSecretVerifierConfigTypeTypeDef = TypedDict(
    "DeviceSecretVerifierConfigTypeTypeDef",
    {
        "PasswordVerifier": NotRequired[str],
        "Salt": NotRequired[str],
    },
)
UserContextDataTypeTypeDef = TypedDict(
    "UserContextDataTypeTypeDef",
    {
        "IpAddress": NotRequired[str],
        "EncodedData": NotRequired[str],
    },
)
HttpHeaderTypeDef = TypedDict(
    "HttpHeaderTypeDef",
    {
        "headerName": NotRequired[str],
        "headerValue": NotRequired[str],
    },
)
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Precedence": NotRequired[int],
    },
)
CreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "CreateIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "ProviderDetails": Mapping[str, str],
        "AttributeMapping": NotRequired[Mapping[str, str]],
        "IdpIdentifiers": NotRequired[Sequence[str]],
    },
)
IdentityProviderTypeTypeDef = TypedDict(
    "IdentityProviderTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "ProviderName": NotRequired[str],
        "ProviderType": NotRequired[IdentityProviderTypeTypeType],
        "ProviderDetails": NotRequired[Dict[str, str]],
        "AttributeMapping": NotRequired[Dict[str, str]],
        "IdpIdentifiers": NotRequired[List[str]],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)
ResourceServerScopeTypeTypeDef = TypedDict(
    "ResourceServerScopeTypeTypeDef",
    {
        "ScopeName": str,
        "ScopeDescription": str,
    },
)
CreateUserImportJobRequestRequestTypeDef = TypedDict(
    "CreateUserImportJobRequestRequestTypeDef",
    {
        "JobName": str,
        "UserPoolId": str,
        "CloudWatchLogsRoleArn": str,
    },
)
UserImportJobTypeTypeDef = TypedDict(
    "UserImportJobTypeTypeDef",
    {
        "JobName": NotRequired[str],
        "JobId": NotRequired[str],
        "UserPoolId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "StartDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "Status": NotRequired[UserImportJobStatusTypeType],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "ImportedUsers": NotRequired[int],
        "SkippedUsers": NotRequired[int],
        "FailedUsers": NotRequired[int],
        "CompletionMessage": NotRequired[str],
    },
)
TokenValidityUnitsTypeTypeDef = TypedDict(
    "TokenValidityUnitsTypeTypeDef",
    {
        "AccessToken": NotRequired[TimeUnitsTypeType],
        "IdToken": NotRequired[TimeUnitsTypeType],
        "RefreshToken": NotRequired[TimeUnitsTypeType],
    },
)
CustomDomainConfigTypeTypeDef = TypedDict(
    "CustomDomainConfigTypeTypeDef",
    {
        "CertificateArn": str,
    },
)
DeviceConfigurationTypeTypeDef = TypedDict(
    "DeviceConfigurationTypeTypeDef",
    {
        "ChallengeRequiredOnNewDevice": NotRequired[bool],
        "DeviceOnlyRememberedOnUserPrompt": NotRequired[bool],
    },
)
EmailConfigurationTypeTypeDef = TypedDict(
    "EmailConfigurationTypeTypeDef",
    {
        "SourceArn": NotRequired[str],
        "ReplyToEmailAddress": NotRequired[str],
        "EmailSendingAccount": NotRequired[EmailSendingAccountTypeType],
        "From": NotRequired[str],
        "ConfigurationSet": NotRequired[str],
    },
)
SmsConfigurationTypeTypeDef = TypedDict(
    "SmsConfigurationTypeTypeDef",
    {
        "SnsCallerArn": str,
        "ExternalId": NotRequired[str],
        "SnsRegion": NotRequired[str],
    },
)
UserAttributeUpdateSettingsTypeTypeDef = TypedDict(
    "UserAttributeUpdateSettingsTypeTypeDef",
    {
        "AttributesRequireVerificationBeforeUpdate": NotRequired[
            Sequence[VerifiedAttributeTypeType]
        ],
    },
)
UsernameConfigurationTypeTypeDef = TypedDict(
    "UsernameConfigurationTypeTypeDef",
    {
        "CaseSensitive": bool,
    },
)
VerificationMessageTemplateTypeTypeDef = TypedDict(
    "VerificationMessageTemplateTypeTypeDef",
    {
        "SmsMessage": NotRequired[str],
        "EmailMessage": NotRequired[str],
        "EmailSubject": NotRequired[str],
        "EmailMessageByLink": NotRequired[str],
        "EmailSubjectByLink": NotRequired[str],
        "DefaultEmailOption": NotRequired[DefaultEmailOptionTypeType],
    },
)
CustomEmailLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)
CustomSMSLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)
DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)
DeleteResourceServerRequestRequestTypeDef = TypedDict(
    "DeleteResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)
DeleteUserAttributesRequestRequestTypeDef = TypedDict(
    "DeleteUserAttributesRequestRequestTypeDef",
    {
        "UserAttributeNames": Sequence[str],
        "AccessToken": str,
    },
)
DeleteUserPoolClientRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)
DeleteUserPoolDomainRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
    },
)
DeleteUserPoolRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)
DescribeIdentityProviderRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)
DescribeResourceServerRequestRequestTypeDef = TypedDict(
    "DescribeResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)
DescribeRiskConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeRiskConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": NotRequired[str],
    },
)
DescribeUserImportJobRequestRequestTypeDef = TypedDict(
    "DescribeUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)
DescribeUserPoolClientRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)
DescribeUserPoolDomainRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
    },
)
DescribeUserPoolRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
EmailMfaConfigTypeTypeDef = TypedDict(
    "EmailMfaConfigTypeTypeDef",
    {
        "Message": NotRequired[str],
        "Subject": NotRequired[str],
    },
)
FirehoseConfigurationTypeTypeDef = TypedDict(
    "FirehoseConfigurationTypeTypeDef",
    {
        "StreamArn": NotRequired[str],
    },
)
ForgetDeviceRequestRequestTypeDef = TypedDict(
    "ForgetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
        "AccessToken": NotRequired[str],
    },
)
GetCSVHeaderRequestRequestTypeDef = TypedDict(
    "GetCSVHeaderRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
        "AccessToken": NotRequired[str],
    },
)
GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)
GetIdentityProviderByIdentifierRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "IdpIdentifier": str,
    },
)
GetLogDeliveryConfigurationRequestRequestTypeDef = TypedDict(
    "GetLogDeliveryConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
GetSigningCertificateRequestRequestTypeDef = TypedDict(
    "GetSigningCertificateRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
GetUICustomizationRequestRequestTypeDef = TypedDict(
    "GetUICustomizationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": NotRequired[str],
    },
)
UICustomizationTypeTypeDef = TypedDict(
    "UICustomizationTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "ClientId": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "CSS": NotRequired[str],
        "CSSVersion": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)
GetUserAttributeVerificationCodeRequestRequestTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeRequestRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
GetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "GetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
SoftwareTokenMfaConfigTypeTypeDef = TypedDict(
    "SoftwareTokenMfaConfigTypeTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)
GlobalSignOutRequestRequestTypeDef = TypedDict(
    "GlobalSignOutRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)
PreTokenGenerationVersionConfigTypeTypeDef = TypedDict(
    "PreTokenGenerationVersionConfigTypeTypeDef",
    {
        "LambdaVersion": PreTokenGenerationLambdaVersionTypeType,
        "LambdaArn": str,
    },
)
ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "AccessToken": str,
        "Limit": NotRequired[int],
        "PaginationToken": NotRequired[str],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "ListIdentityProvidersRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ProviderDescriptionTypeDef = TypedDict(
    "ProviderDescriptionTypeDef",
    {
        "ProviderName": NotRequired[str],
        "ProviderType": NotRequired[IdentityProviderTypeTypeType],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)
ListResourceServersRequestRequestTypeDef = TypedDict(
    "ListResourceServersRequestRequestTypeDef",
    {
        "UserPoolId": str,
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
ListUserImportJobsRequestRequestTypeDef = TypedDict(
    "ListUserImportJobsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": int,
        "PaginationToken": NotRequired[str],
    },
)
ListUserPoolClientsRequestRequestTypeDef = TypedDict(
    "ListUserPoolClientsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
UserPoolClientDescriptionTypeDef = TypedDict(
    "UserPoolClientDescriptionTypeDef",
    {
        "ClientId": NotRequired[str],
        "UserPoolId": NotRequired[str],
        "ClientName": NotRequired[str],
    },
)
ListUserPoolsRequestRequestTypeDef = TypedDict(
    "ListUserPoolsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": NotRequired[str],
    },
)
ListUsersInGroupRequestRequestTypeDef = TypedDict(
    "ListUsersInGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "GroupName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "PaginationToken": NotRequired[str],
        "Filter": NotRequired[str],
    },
)
S3ConfigurationTypeTypeDef = TypedDict(
    "S3ConfigurationTypeTypeDef",
    {
        "BucketArn": NotRequired[str],
    },
)
NotifyEmailTypeTypeDef = TypedDict(
    "NotifyEmailTypeTypeDef",
    {
        "Subject": str,
        "HtmlBody": NotRequired[str],
        "TextBody": NotRequired[str],
    },
)
NumberAttributeConstraintsTypeTypeDef = TypedDict(
    "NumberAttributeConstraintsTypeTypeDef",
    {
        "MinValue": NotRequired[str],
        "MaxValue": NotRequired[str],
    },
)
PasswordPolicyTypeTypeDef = TypedDict(
    "PasswordPolicyTypeTypeDef",
    {
        "MinimumLength": NotRequired[int],
        "RequireUppercase": NotRequired[bool],
        "RequireLowercase": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireSymbols": NotRequired[bool],
        "PasswordHistorySize": NotRequired[int],
        "TemporaryPasswordValidityDays": NotRequired[int],
    },
)
RevokeTokenRequestRequestTypeDef = TypedDict(
    "RevokeTokenRequestRequestTypeDef",
    {
        "Token": str,
        "ClientId": str,
        "ClientSecret": NotRequired[str],
    },
)
RiskExceptionConfigurationTypeOutputTypeDef = TypedDict(
    "RiskExceptionConfigurationTypeOutputTypeDef",
    {
        "BlockedIPRangeList": NotRequired[List[str]],
        "SkippedIPRangeList": NotRequired[List[str]],
    },
)
RiskExceptionConfigurationTypeTypeDef = TypedDict(
    "RiskExceptionConfigurationTypeTypeDef",
    {
        "BlockedIPRangeList": NotRequired[Sequence[str]],
        "SkippedIPRangeList": NotRequired[Sequence[str]],
    },
)
StringAttributeConstraintsTypeTypeDef = TypedDict(
    "StringAttributeConstraintsTypeTypeDef",
    {
        "MinLength": NotRequired[str],
        "MaxLength": NotRequired[str],
    },
)
StartUserImportJobRequestRequestTypeDef = TypedDict(
    "StartUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)
StopUserImportJobRequestRequestTypeDef = TypedDict(
    "StopUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
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
UpdateAuthEventFeedbackRequestRequestTypeDef = TypedDict(
    "UpdateAuthEventFeedbackRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackToken": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)
UpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "UpdateDeviceStatusRequestRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
        "DeviceRememberedStatus": NotRequired[DeviceRememberedStatusTypeType],
    },
)
UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Precedence": NotRequired[int],
    },
)
UpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "UpdateIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderDetails": NotRequired[Mapping[str, str]],
        "AttributeMapping": NotRequired[Mapping[str, str]],
        "IdpIdentifiers": NotRequired[Sequence[str]],
    },
)
UserAttributeUpdateSettingsTypeOutputTypeDef = TypedDict(
    "UserAttributeUpdateSettingsTypeOutputTypeDef",
    {
        "AttributesRequireVerificationBeforeUpdate": NotRequired[List[VerifiedAttributeTypeType]],
    },
)
VerifySoftwareTokenRequestRequestTypeDef = TypedDict(
    "VerifySoftwareTokenRequestRequestTypeDef",
    {
        "UserCode": str,
        "AccessToken": NotRequired[str],
        "Session": NotRequired[str],
        "FriendlyDeviceName": NotRequired[str],
    },
)
VerifyUserAttributeRequestRequestTypeDef = TypedDict(
    "VerifyUserAttributeRequestRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
        "Code": str,
    },
)
AccountRecoverySettingTypeOutputTypeDef = TypedDict(
    "AccountRecoverySettingTypeOutputTypeDef",
    {
        "RecoveryMechanisms": NotRequired[List[RecoveryOptionTypeTypeDef]],
    },
)
AccountRecoverySettingTypeTypeDef = TypedDict(
    "AccountRecoverySettingTypeTypeDef",
    {
        "RecoveryMechanisms": NotRequired[Sequence[RecoveryOptionTypeTypeDef]],
    },
)
AccountTakeoverActionsTypeTypeDef = TypedDict(
    "AccountTakeoverActionsTypeTypeDef",
    {
        "LowAction": NotRequired[AccountTakeoverActionTypeTypeDef],
        "MediumAction": NotRequired[AccountTakeoverActionTypeTypeDef],
        "HighAction": NotRequired[AccountTakeoverActionTypeTypeDef],
    },
)
AdminCreateUserConfigTypeTypeDef = TypedDict(
    "AdminCreateUserConfigTypeTypeDef",
    {
        "AllowAdminCreateUserOnly": NotRequired[bool],
        "UnusedAccountValidityDays": NotRequired[int],
        "InviteMessageTemplate": NotRequired[MessageTemplateTypeTypeDef],
    },
)
AdminCreateUserRequestRequestTypeDef = TypedDict(
    "AdminCreateUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributes": NotRequired[Sequence[AttributeTypeTypeDef]],
        "ValidationData": NotRequired[Sequence[AttributeTypeTypeDef]],
        "TemporaryPassword": NotRequired[str],
        "ForceAliasCreation": NotRequired[bool],
        "MessageAction": NotRequired[MessageActionTypeType],
        "DesiredDeliveryMediums": NotRequired[Sequence[DeliveryMediumTypeType]],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
AdminUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "AdminUpdateUserAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributes": Sequence[AttributeTypeTypeDef],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
DeviceTypeTypeDef = TypedDict(
    "DeviceTypeTypeDef",
    {
        "DeviceKey": NotRequired[str],
        "DeviceAttributes": NotRequired[List[AttributeTypeTypeDef]],
        "DeviceCreateDate": NotRequired[datetime],
        "DeviceLastModifiedDate": NotRequired[datetime],
        "DeviceLastAuthenticatedDate": NotRequired[datetime],
    },
)
UpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "UpdateUserAttributesRequestRequestTypeDef",
    {
        "UserAttributes": Sequence[AttributeTypeTypeDef],
        "AccessToken": str,
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
AssociateSoftwareTokenResponseTypeDef = TypedDict(
    "AssociateSoftwareTokenResponseTypeDef",
    {
        "SecretCode": str,
        "Session": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfirmDeviceResponseTypeDef = TypedDict(
    "ConfirmDeviceResponseTypeDef",
    {
        "UserConfirmationNecessary": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserPoolDomainResponseTypeDef = TypedDict(
    "CreateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCSVHeaderResponseTypeDef = TypedDict(
    "GetCSVHeaderResponseTypeDef",
    {
        "UserPoolId": str,
        "CSVHeader": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSigningCertificateResponseTypeDef = TypedDict(
    "GetSigningCertificateResponseTypeDef",
    {
        "Certificate": str,
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
UpdateUserPoolDomainResponseTypeDef = TypedDict(
    "UpdateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifySoftwareTokenResponseTypeDef = TypedDict(
    "VerifySoftwareTokenResponseTypeDef",
    {
        "Status": VerifySoftwareTokenResponseTypeType,
        "Session": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdminDisableProviderForUserRequestRequestTypeDef = TypedDict(
    "AdminDisableProviderForUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "User": ProviderUserIdentifierTypeTypeDef,
    },
)
AdminLinkProviderForUserRequestRequestTypeDef = TypedDict(
    "AdminLinkProviderForUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "DestinationUser": ProviderUserIdentifierTypeTypeDef,
        "SourceUser": ProviderUserIdentifierTypeTypeDef,
    },
)
AdminGetUserResponseTypeDef = TypedDict(
    "AdminGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[AttributeTypeTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List[MFAOptionTypeTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdminSetUserSettingsRequestRequestTypeDef = TypedDict(
    "AdminSetUserSettingsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "MFAOptions": Sequence[MFAOptionTypeTypeDef],
    },
)
GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[AttributeTypeTypeDef],
        "MFAOptions": List[MFAOptionTypeTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetUserSettingsRequestRequestTypeDef = TypedDict(
    "SetUserSettingsRequestRequestTypeDef",
    {
        "AccessToken": str,
        "MFAOptions": Sequence[MFAOptionTypeTypeDef],
    },
)
UserTypeTypeDef = TypedDict(
    "UserTypeTypeDef",
    {
        "Username": NotRequired[str],
        "Attributes": NotRequired[List[AttributeTypeTypeDef]],
        "UserCreateDate": NotRequired[datetime],
        "UserLastModifiedDate": NotRequired[datetime],
        "Enabled": NotRequired[bool],
        "UserStatus": NotRequired[UserStatusTypeType],
        "MFAOptions": NotRequired[List[MFAOptionTypeTypeDef]],
    },
)
AdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef = TypedDict(
    "AdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef = TypedDict(
    "AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "UserPoolId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef = TypedDict(
    "ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    {
        "UserPoolId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceServersRequestListResourceServersPaginateTypeDef = TypedDict(
    "ListResourceServersRequestListResourceServersPaginateTypeDef",
    {
        "UserPoolId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef = TypedDict(
    "ListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef",
    {
        "UserPoolId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUserPoolsRequestListUserPoolsPaginateTypeDef = TypedDict(
    "ListUserPoolsRequestListUserPoolsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersInGroupRequestListUsersInGroupPaginateTypeDef = TypedDict(
    "ListUsersInGroupRequestListUsersInGroupPaginateTypeDef",
    {
        "UserPoolId": str,
        "GroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "UserPoolId": str,
        "AttributesToGet": NotRequired[Sequence[str]],
        "Filter": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
AdminListGroupsForUserResponseTypeDef = TypedDict(
    "AdminListGroupsForUserResponseTypeDef",
    {
        "Groups": List[GroupTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": GroupTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": GroupTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List[GroupTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": GroupTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdminSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "AdminSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
        "SMSMfaSettings": NotRequired[SMSMfaSettingsTypeTypeDef],
        "SoftwareTokenMfaSettings": NotRequired[SoftwareTokenMfaSettingsTypeTypeDef],
        "EmailMfaSettings": NotRequired[EmailMfaSettingsTypeTypeDef],
    },
)
SetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "SetUserMFAPreferenceRequestRequestTypeDef",
    {
        "AccessToken": str,
        "SMSMfaSettings": NotRequired[SMSMfaSettingsTypeTypeDef],
        "SoftwareTokenMfaSettings": NotRequired[SoftwareTokenMfaSettingsTypeTypeDef],
        "EmailMfaSettings": NotRequired[EmailMfaSettingsTypeTypeDef],
    },
)
UserPoolAddOnsTypeTypeDef = TypedDict(
    "UserPoolAddOnsTypeTypeDef",
    {
        "AdvancedSecurityMode": AdvancedSecurityModeTypeType,
        "AdvancedSecurityAdditionalFlows": NotRequired[AdvancedSecurityAdditionalFlowsTypeTypeDef],
    },
)
AuthEventTypeTypeDef = TypedDict(
    "AuthEventTypeTypeDef",
    {
        "EventId": NotRequired[str],
        "EventType": NotRequired[EventTypeType],
        "CreationDate": NotRequired[datetime],
        "EventResponse": NotRequired[EventResponseTypeType],
        "EventRisk": NotRequired[EventRiskTypeTypeDef],
        "ChallengeResponses": NotRequired[List[ChallengeResponseTypeTypeDef]],
        "EventContextData": NotRequired[EventContextDataTypeTypeDef],
        "EventFeedback": NotRequired[EventFeedbackTypeTypeDef],
    },
)
AuthenticationResultTypeTypeDef = TypedDict(
    "AuthenticationResultTypeTypeDef",
    {
        "AccessToken": NotRequired[str],
        "ExpiresIn": NotRequired[int],
        "TokenType": NotRequired[str],
        "RefreshToken": NotRequired[str],
        "IdToken": NotRequired[str],
        "NewDeviceMetadata": NotRequired[NewDeviceMetadataTypeTypeDef],
    },
)
SetUICustomizationRequestRequestTypeDef = TypedDict(
    "SetUICustomizationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": NotRequired[str],
        "CSS": NotRequired[str],
        "ImageFile": NotRequired[BlobTypeDef],
    },
)
ForgotPasswordResponseTypeDef = TypedDict(
    "ForgotPasswordResponseTypeDef",
    {
        "CodeDeliveryDetails": CodeDeliveryDetailsTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": CodeDeliveryDetailsTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResendConfirmationCodeResponseTypeDef = TypedDict(
    "ResendConfirmationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": CodeDeliveryDetailsTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SignUpResponseTypeDef = TypedDict(
    "SignUpResponseTypeDef",
    {
        "UserConfirmed": bool,
        "CodeDeliveryDetails": CodeDeliveryDetailsTypeTypeDef,
        "UserSub": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserAttributesResponseTypeDef = TypedDict(
    "UpdateUserAttributesResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List[CodeDeliveryDetailsTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CompromisedCredentialsRiskConfigurationTypeOutputTypeDef = TypedDict(
    "CompromisedCredentialsRiskConfigurationTypeOutputTypeDef",
    {
        "Actions": CompromisedCredentialsActionsTypeTypeDef,
        "EventFilter": NotRequired[List[EventFilterTypeType]],
    },
)
CompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    {
        "Actions": CompromisedCredentialsActionsTypeTypeDef,
        "EventFilter": NotRequired[Sequence[EventFilterTypeType]],
    },
)
ConfirmDeviceRequestRequestTypeDef = TypedDict(
    "ConfirmDeviceRequestRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
        "DeviceSecretVerifierConfig": NotRequired[DeviceSecretVerifierConfigTypeTypeDef],
        "DeviceName": NotRequired[str],
    },
)
ConfirmForgotPasswordRequestRequestTypeDef = TypedDict(
    "ConfirmForgotPasswordRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
        "Password": str,
        "SecretHash": NotRequired[str],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "UserContextData": NotRequired[UserContextDataTypeTypeDef],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
ConfirmSignUpRequestRequestTypeDef = TypedDict(
    "ConfirmSignUpRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
        "SecretHash": NotRequired[str],
        "ForceAliasCreation": NotRequired[bool],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "UserContextData": NotRequired[UserContextDataTypeTypeDef],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
ForgotPasswordRequestRequestTypeDef = TypedDict(
    "ForgotPasswordRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "SecretHash": NotRequired[str],
        "UserContextData": NotRequired[UserContextDataTypeTypeDef],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
InitiateAuthRequestRequestTypeDef = TypedDict(
    "InitiateAuthRequestRequestTypeDef",
    {
        "AuthFlow": AuthFlowTypeType,
        "ClientId": str,
        "AuthParameters": NotRequired[Mapping[str, str]],
        "ClientMetadata": NotRequired[Mapping[str, str]],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "UserContextData": NotRequired[UserContextDataTypeTypeDef],
    },
)
ResendConfirmationCodeRequestRequestTypeDef = TypedDict(
    "ResendConfirmationCodeRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "SecretHash": NotRequired[str],
        "UserContextData": NotRequired[UserContextDataTypeTypeDef],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
RespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "RespondToAuthChallengeRequestRequestTypeDef",
    {
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
        "Session": NotRequired[str],
        "ChallengeResponses": NotRequired[Mapping[str, str]],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "UserContextData": NotRequired[UserContextDataTypeTypeDef],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
SignUpRequestRequestTypeDef = TypedDict(
    "SignUpRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "Password": str,
        "SecretHash": NotRequired[str],
        "UserAttributes": NotRequired[Sequence[AttributeTypeTypeDef]],
        "ValidationData": NotRequired[Sequence[AttributeTypeTypeDef]],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "UserContextData": NotRequired[UserContextDataTypeTypeDef],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
ContextDataTypeTypeDef = TypedDict(
    "ContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": Sequence[HttpHeaderTypeDef],
        "EncodedData": NotRequired[str],
    },
)
CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIdentityProviderResponseTypeDef = TypedDict(
    "DescribeIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierResponseTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceServerRequestRequestTypeDef = TypedDict(
    "CreateResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": NotRequired[Sequence[ResourceServerScopeTypeTypeDef]],
    },
)
ResourceServerTypeTypeDef = TypedDict(
    "ResourceServerTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "Identifier": NotRequired[str],
        "Name": NotRequired[str],
        "Scopes": NotRequired[List[ResourceServerScopeTypeTypeDef]],
    },
)
UpdateResourceServerRequestRequestTypeDef = TypedDict(
    "UpdateResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": NotRequired[Sequence[ResourceServerScopeTypeTypeDef]],
    },
)
CreateUserImportJobResponseTypeDef = TypedDict(
    "CreateUserImportJobResponseTypeDef",
    {
        "UserImportJob": UserImportJobTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUserImportJobResponseTypeDef = TypedDict(
    "DescribeUserImportJobResponseTypeDef",
    {
        "UserImportJob": UserImportJobTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUserImportJobsResponseTypeDef = TypedDict(
    "ListUserImportJobsResponseTypeDef",
    {
        "UserImportJobs": List[UserImportJobTypeTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartUserImportJobResponseTypeDef = TypedDict(
    "StartUserImportJobResponseTypeDef",
    {
        "UserImportJob": UserImportJobTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopUserImportJobResponseTypeDef = TypedDict(
    "StopUserImportJobResponseTypeDef",
    {
        "UserImportJob": UserImportJobTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserPoolClientRequestRequestTypeDef = TypedDict(
    "CreateUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "GenerateSecret": NotRequired[bool],
        "RefreshTokenValidity": NotRequired[int],
        "AccessTokenValidity": NotRequired[int],
        "IdTokenValidity": NotRequired[int],
        "TokenValidityUnits": NotRequired[TokenValidityUnitsTypeTypeDef],
        "ReadAttributes": NotRequired[Sequence[str]],
        "WriteAttributes": NotRequired[Sequence[str]],
        "ExplicitAuthFlows": NotRequired[Sequence[ExplicitAuthFlowsTypeType]],
        "SupportedIdentityProviders": NotRequired[Sequence[str]],
        "CallbackURLs": NotRequired[Sequence[str]],
        "LogoutURLs": NotRequired[Sequence[str]],
        "DefaultRedirectURI": NotRequired[str],
        "AllowedOAuthFlows": NotRequired[Sequence[OAuthFlowTypeType]],
        "AllowedOAuthScopes": NotRequired[Sequence[str]],
        "AllowedOAuthFlowsUserPoolClient": NotRequired[bool],
        "AnalyticsConfiguration": NotRequired[AnalyticsConfigurationTypeTypeDef],
        "PreventUserExistenceErrors": NotRequired[PreventUserExistenceErrorTypesType],
        "EnableTokenRevocation": NotRequired[bool],
        "EnablePropagateAdditionalUserContextData": NotRequired[bool],
        "AuthSessionValidity": NotRequired[int],
    },
)
UpdateUserPoolClientRequestRequestTypeDef = TypedDict(
    "UpdateUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ClientName": NotRequired[str],
        "RefreshTokenValidity": NotRequired[int],
        "AccessTokenValidity": NotRequired[int],
        "IdTokenValidity": NotRequired[int],
        "TokenValidityUnits": NotRequired[TokenValidityUnitsTypeTypeDef],
        "ReadAttributes": NotRequired[Sequence[str]],
        "WriteAttributes": NotRequired[Sequence[str]],
        "ExplicitAuthFlows": NotRequired[Sequence[ExplicitAuthFlowsTypeType]],
        "SupportedIdentityProviders": NotRequired[Sequence[str]],
        "CallbackURLs": NotRequired[Sequence[str]],
        "LogoutURLs": NotRequired[Sequence[str]],
        "DefaultRedirectURI": NotRequired[str],
        "AllowedOAuthFlows": NotRequired[Sequence[OAuthFlowTypeType]],
        "AllowedOAuthScopes": NotRequired[Sequence[str]],
        "AllowedOAuthFlowsUserPoolClient": NotRequired[bool],
        "AnalyticsConfiguration": NotRequired[AnalyticsConfigurationTypeTypeDef],
        "PreventUserExistenceErrors": NotRequired[PreventUserExistenceErrorTypesType],
        "EnableTokenRevocation": NotRequired[bool],
        "EnablePropagateAdditionalUserContextData": NotRequired[bool],
        "AuthSessionValidity": NotRequired[int],
    },
)
UserPoolClientTypeTypeDef = TypedDict(
    "UserPoolClientTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "ClientName": NotRequired[str],
        "ClientId": NotRequired[str],
        "ClientSecret": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
        "RefreshTokenValidity": NotRequired[int],
        "AccessTokenValidity": NotRequired[int],
        "IdTokenValidity": NotRequired[int],
        "TokenValidityUnits": NotRequired[TokenValidityUnitsTypeTypeDef],
        "ReadAttributes": NotRequired[List[str]],
        "WriteAttributes": NotRequired[List[str]],
        "ExplicitAuthFlows": NotRequired[List[ExplicitAuthFlowsTypeType]],
        "SupportedIdentityProviders": NotRequired[List[str]],
        "CallbackURLs": NotRequired[List[str]],
        "LogoutURLs": NotRequired[List[str]],
        "DefaultRedirectURI": NotRequired[str],
        "AllowedOAuthFlows": NotRequired[List[OAuthFlowTypeType]],
        "AllowedOAuthScopes": NotRequired[List[str]],
        "AllowedOAuthFlowsUserPoolClient": NotRequired[bool],
        "AnalyticsConfiguration": NotRequired[AnalyticsConfigurationTypeTypeDef],
        "PreventUserExistenceErrors": NotRequired[PreventUserExistenceErrorTypesType],
        "EnableTokenRevocation": NotRequired[bool],
        "EnablePropagateAdditionalUserContextData": NotRequired[bool],
        "AuthSessionValidity": NotRequired[int],
    },
)
CreateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "CreateUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
        "CustomDomainConfig": NotRequired[CustomDomainConfigTypeTypeDef],
    },
)
DomainDescriptionTypeTypeDef = TypedDict(
    "DomainDescriptionTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "AWSAccountId": NotRequired[str],
        "Domain": NotRequired[str],
        "S3Bucket": NotRequired[str],
        "CloudFrontDistribution": NotRequired[str],
        "Version": NotRequired[str],
        "Status": NotRequired[DomainStatusTypeType],
        "CustomDomainConfig": NotRequired[CustomDomainConfigTypeTypeDef],
    },
)
UpdateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "UpdateUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
        "CustomDomainConfig": CustomDomainConfigTypeTypeDef,
    },
)
SmsMfaConfigTypeTypeDef = TypedDict(
    "SmsMfaConfigTypeTypeDef",
    {
        "SmsAuthenticationMessage": NotRequired[str],
        "SmsConfiguration": NotRequired[SmsConfigurationTypeTypeDef],
    },
)
GetUICustomizationResponseTypeDef = TypedDict(
    "GetUICustomizationResponseTypeDef",
    {
        "UICustomization": UICustomizationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetUICustomizationResponseTypeDef = TypedDict(
    "SetUICustomizationResponseTypeDef",
    {
        "UICustomization": UICustomizationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LambdaConfigTypeTypeDef = TypedDict(
    "LambdaConfigTypeTypeDef",
    {
        "PreSignUp": NotRequired[str],
        "CustomMessage": NotRequired[str],
        "PostConfirmation": NotRequired[str],
        "PreAuthentication": NotRequired[str],
        "PostAuthentication": NotRequired[str],
        "DefineAuthChallenge": NotRequired[str],
        "CreateAuthChallenge": NotRequired[str],
        "VerifyAuthChallengeResponse": NotRequired[str],
        "PreTokenGeneration": NotRequired[str],
        "UserMigration": NotRequired[str],
        "PreTokenGenerationConfig": NotRequired[PreTokenGenerationVersionConfigTypeTypeDef],
        "CustomSMSSender": NotRequired[CustomSMSLambdaVersionConfigTypeTypeDef],
        "CustomEmailSender": NotRequired[CustomEmailLambdaVersionConfigTypeTypeDef],
        "KMSKeyID": NotRequired[str],
    },
)
ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "Providers": List[ProviderDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUserPoolClientsResponseTypeDef = TypedDict(
    "ListUserPoolClientsResponseTypeDef",
    {
        "UserPoolClients": List[UserPoolClientDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LogConfigurationTypeTypeDef = TypedDict(
    "LogConfigurationTypeTypeDef",
    {
        "LogLevel": LogLevelType,
        "EventSource": EventSourceNameType,
        "CloudWatchLogsConfiguration": NotRequired[CloudWatchLogsConfigurationTypeTypeDef],
        "S3Configuration": NotRequired[S3ConfigurationTypeTypeDef],
        "FirehoseConfiguration": NotRequired[FirehoseConfigurationTypeTypeDef],
    },
)
NotifyConfigurationTypeTypeDef = TypedDict(
    "NotifyConfigurationTypeTypeDef",
    {
        "SourceArn": str,
        "From": NotRequired[str],
        "ReplyTo": NotRequired[str],
        "BlockEmail": NotRequired[NotifyEmailTypeTypeDef],
        "NoActionEmail": NotRequired[NotifyEmailTypeTypeDef],
        "MfaEmail": NotRequired[NotifyEmailTypeTypeDef],
    },
)
UserPoolPolicyTypeTypeDef = TypedDict(
    "UserPoolPolicyTypeTypeDef",
    {
        "PasswordPolicy": NotRequired[PasswordPolicyTypeTypeDef],
    },
)
SchemaAttributeTypeTypeDef = TypedDict(
    "SchemaAttributeTypeTypeDef",
    {
        "Name": NotRequired[str],
        "AttributeDataType": NotRequired[AttributeDataTypeType],
        "DeveloperOnlyAttribute": NotRequired[bool],
        "Mutable": NotRequired[bool],
        "Required": NotRequired[bool],
        "NumberAttributeConstraints": NotRequired[NumberAttributeConstraintsTypeTypeDef],
        "StringAttributeConstraints": NotRequired[StringAttributeConstraintsTypeTypeDef],
    },
)
AdminGetDeviceResponseTypeDef = TypedDict(
    "AdminGetDeviceResponseTypeDef",
    {
        "Device": DeviceTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdminListDevicesResponseTypeDef = TypedDict(
    "AdminListDevicesResponseTypeDef",
    {
        "Devices": List[DeviceTypeTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "Device": DeviceTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List[DeviceTypeTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdminCreateUserResponseTypeDef = TypedDict(
    "AdminCreateUserResponseTypeDef",
    {
        "User": UserTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUsersInGroupResponseTypeDef = TypedDict(
    "ListUsersInGroupResponseTypeDef",
    {
        "Users": List[UserTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List[UserTypeTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdminListUserAuthEventsResponseTypeDef = TypedDict(
    "AdminListUserAuthEventsResponseTypeDef",
    {
        "AuthEvents": List[AuthEventTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AdminInitiateAuthResponseTypeDef = TypedDict(
    "AdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": AuthenticationResultTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "AdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": AuthenticationResultTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitiateAuthResponseTypeDef = TypedDict(
    "InitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": AuthenticationResultTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RespondToAuthChallengeResponseTypeDef = TypedDict(
    "RespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": AuthenticationResultTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdminInitiateAuthRequestRequestTypeDef = TypedDict(
    "AdminInitiateAuthRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "AuthFlow": AuthFlowTypeType,
        "AuthParameters": NotRequired[Mapping[str, str]],
        "ClientMetadata": NotRequired[Mapping[str, str]],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "ContextData": NotRequired[ContextDataTypeTypeDef],
    },
)
AdminRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "AdminRespondToAuthChallengeRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
        "ChallengeResponses": NotRequired[Mapping[str, str]],
        "Session": NotRequired[str],
        "AnalyticsMetadata": NotRequired[AnalyticsMetadataTypeTypeDef],
        "ContextData": NotRequired[ContextDataTypeTypeDef],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)
CreateResourceServerResponseTypeDef = TypedDict(
    "CreateResourceServerResponseTypeDef",
    {
        "ResourceServer": ResourceServerTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeResourceServerResponseTypeDef = TypedDict(
    "DescribeResourceServerResponseTypeDef",
    {
        "ResourceServer": ResourceServerTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceServersResponseTypeDef = TypedDict(
    "ListResourceServersResponseTypeDef",
    {
        "ResourceServers": List[ResourceServerTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateResourceServerResponseTypeDef = TypedDict(
    "UpdateResourceServerResponseTypeDef",
    {
        "ResourceServer": ResourceServerTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserPoolClientResponseTypeDef = TypedDict(
    "CreateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": UserPoolClientTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUserPoolClientResponseTypeDef = TypedDict(
    "DescribeUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": UserPoolClientTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserPoolClientResponseTypeDef = TypedDict(
    "UpdateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": UserPoolClientTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUserPoolDomainResponseTypeDef = TypedDict(
    "DescribeUserPoolDomainResponseTypeDef",
    {
        "DomainDescription": DomainDescriptionTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "GetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": SmsMfaConfigTypeTypeDef,
        "SoftwareTokenMfaConfiguration": SoftwareTokenMfaConfigTypeTypeDef,
        "EmailMfaConfiguration": EmailMfaConfigTypeTypeDef,
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "SetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "SmsMfaConfiguration": NotRequired[SmsMfaConfigTypeTypeDef],
        "SoftwareTokenMfaConfiguration": NotRequired[SoftwareTokenMfaConfigTypeTypeDef],
        "EmailMfaConfiguration": NotRequired[EmailMfaConfigTypeTypeDef],
        "MfaConfiguration": NotRequired[UserPoolMfaTypeType],
    },
)
SetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "SetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": SmsMfaConfigTypeTypeDef,
        "SoftwareTokenMfaConfiguration": SoftwareTokenMfaConfigTypeTypeDef,
        "EmailMfaConfiguration": EmailMfaConfigTypeTypeDef,
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserPoolDescriptionTypeTypeDef = TypedDict(
    "UserPoolDescriptionTypeTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "LambdaConfig": NotRequired[LambdaConfigTypeTypeDef],
        "Status": NotRequired[StatusTypeType],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)
LogDeliveryConfigurationTypeTypeDef = TypedDict(
    "LogDeliveryConfigurationTypeTypeDef",
    {
        "UserPoolId": str,
        "LogConfigurations": List[LogConfigurationTypeTypeDef],
    },
)
SetLogDeliveryConfigurationRequestRequestTypeDef = TypedDict(
    "SetLogDeliveryConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "LogConfigurations": Sequence[LogConfigurationTypeTypeDef],
    },
)
AccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    {
        "Actions": AccountTakeoverActionsTypeTypeDef,
        "NotifyConfiguration": NotRequired[NotifyConfigurationTypeTypeDef],
    },
)
UpdateUserPoolRequestRequestTypeDef = TypedDict(
    "UpdateUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Policies": NotRequired[UserPoolPolicyTypeTypeDef],
        "DeletionProtection": NotRequired[DeletionProtectionTypeType],
        "LambdaConfig": NotRequired[LambdaConfigTypeTypeDef],
        "AutoVerifiedAttributes": NotRequired[Sequence[VerifiedAttributeTypeType]],
        "SmsVerificationMessage": NotRequired[str],
        "EmailVerificationMessage": NotRequired[str],
        "EmailVerificationSubject": NotRequired[str],
        "VerificationMessageTemplate": NotRequired[VerificationMessageTemplateTypeTypeDef],
        "SmsAuthenticationMessage": NotRequired[str],
        "UserAttributeUpdateSettings": NotRequired[UserAttributeUpdateSettingsTypeTypeDef],
        "MfaConfiguration": NotRequired[UserPoolMfaTypeType],
        "DeviceConfiguration": NotRequired[DeviceConfigurationTypeTypeDef],
        "EmailConfiguration": NotRequired[EmailConfigurationTypeTypeDef],
        "SmsConfiguration": NotRequired[SmsConfigurationTypeTypeDef],
        "UserPoolTags": NotRequired[Mapping[str, str]],
        "AdminCreateUserConfig": NotRequired[AdminCreateUserConfigTypeTypeDef],
        "UserPoolAddOns": NotRequired[UserPoolAddOnsTypeTypeDef],
        "AccountRecoverySetting": NotRequired[AccountRecoverySettingTypeTypeDef],
    },
)
AddCustomAttributesRequestRequestTypeDef = TypedDict(
    "AddCustomAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "CustomAttributes": Sequence[SchemaAttributeTypeTypeDef],
    },
)
CreateUserPoolRequestRequestTypeDef = TypedDict(
    "CreateUserPoolRequestRequestTypeDef",
    {
        "PoolName": str,
        "Policies": NotRequired[UserPoolPolicyTypeTypeDef],
        "DeletionProtection": NotRequired[DeletionProtectionTypeType],
        "LambdaConfig": NotRequired[LambdaConfigTypeTypeDef],
        "AutoVerifiedAttributes": NotRequired[Sequence[VerifiedAttributeTypeType]],
        "AliasAttributes": NotRequired[Sequence[AliasAttributeTypeType]],
        "UsernameAttributes": NotRequired[Sequence[UsernameAttributeTypeType]],
        "SmsVerificationMessage": NotRequired[str],
        "EmailVerificationMessage": NotRequired[str],
        "EmailVerificationSubject": NotRequired[str],
        "VerificationMessageTemplate": NotRequired[VerificationMessageTemplateTypeTypeDef],
        "SmsAuthenticationMessage": NotRequired[str],
        "MfaConfiguration": NotRequired[UserPoolMfaTypeType],
        "UserAttributeUpdateSettings": NotRequired[UserAttributeUpdateSettingsTypeTypeDef],
        "DeviceConfiguration": NotRequired[DeviceConfigurationTypeTypeDef],
        "EmailConfiguration": NotRequired[EmailConfigurationTypeTypeDef],
        "SmsConfiguration": NotRequired[SmsConfigurationTypeTypeDef],
        "UserPoolTags": NotRequired[Mapping[str, str]],
        "AdminCreateUserConfig": NotRequired[AdminCreateUserConfigTypeTypeDef],
        "Schema": NotRequired[Sequence[SchemaAttributeTypeTypeDef]],
        "UserPoolAddOns": NotRequired[UserPoolAddOnsTypeTypeDef],
        "UsernameConfiguration": NotRequired[UsernameConfigurationTypeTypeDef],
        "AccountRecoverySetting": NotRequired[AccountRecoverySettingTypeTypeDef],
    },
)
UserPoolTypeTypeDef = TypedDict(
    "UserPoolTypeTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Policies": NotRequired[UserPoolPolicyTypeTypeDef],
        "DeletionProtection": NotRequired[DeletionProtectionTypeType],
        "LambdaConfig": NotRequired[LambdaConfigTypeTypeDef],
        "Status": NotRequired[StatusTypeType],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
        "SchemaAttributes": NotRequired[List[SchemaAttributeTypeTypeDef]],
        "AutoVerifiedAttributes": NotRequired[List[VerifiedAttributeTypeType]],
        "AliasAttributes": NotRequired[List[AliasAttributeTypeType]],
        "UsernameAttributes": NotRequired[List[UsernameAttributeTypeType]],
        "SmsVerificationMessage": NotRequired[str],
        "EmailVerificationMessage": NotRequired[str],
        "EmailVerificationSubject": NotRequired[str],
        "VerificationMessageTemplate": NotRequired[VerificationMessageTemplateTypeTypeDef],
        "SmsAuthenticationMessage": NotRequired[str],
        "UserAttributeUpdateSettings": NotRequired[UserAttributeUpdateSettingsTypeOutputTypeDef],
        "MfaConfiguration": NotRequired[UserPoolMfaTypeType],
        "DeviceConfiguration": NotRequired[DeviceConfigurationTypeTypeDef],
        "EstimatedNumberOfUsers": NotRequired[int],
        "EmailConfiguration": NotRequired[EmailConfigurationTypeTypeDef],
        "SmsConfiguration": NotRequired[SmsConfigurationTypeTypeDef],
        "UserPoolTags": NotRequired[Dict[str, str]],
        "SmsConfigurationFailure": NotRequired[str],
        "EmailConfigurationFailure": NotRequired[str],
        "Domain": NotRequired[str],
        "CustomDomain": NotRequired[str],
        "AdminCreateUserConfig": NotRequired[AdminCreateUserConfigTypeTypeDef],
        "UserPoolAddOns": NotRequired[UserPoolAddOnsTypeTypeDef],
        "UsernameConfiguration": NotRequired[UsernameConfigurationTypeTypeDef],
        "Arn": NotRequired[str],
        "AccountRecoverySetting": NotRequired[AccountRecoverySettingTypeOutputTypeDef],
    },
)
ListUserPoolsResponseTypeDef = TypedDict(
    "ListUserPoolsResponseTypeDef",
    {
        "UserPools": List[UserPoolDescriptionTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetLogDeliveryConfigurationResponseTypeDef = TypedDict(
    "GetLogDeliveryConfigurationResponseTypeDef",
    {
        "LogDeliveryConfiguration": LogDeliveryConfigurationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetLogDeliveryConfigurationResponseTypeDef = TypedDict(
    "SetLogDeliveryConfigurationResponseTypeDef",
    {
        "LogDeliveryConfiguration": LogDeliveryConfigurationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RiskConfigurationTypeTypeDef = TypedDict(
    "RiskConfigurationTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "ClientId": NotRequired[str],
        "CompromisedCredentialsRiskConfiguration": NotRequired[
            CompromisedCredentialsRiskConfigurationTypeOutputTypeDef
        ],
        "AccountTakeoverRiskConfiguration": NotRequired[
            AccountTakeoverRiskConfigurationTypeTypeDef
        ],
        "RiskExceptionConfiguration": NotRequired[RiskExceptionConfigurationTypeOutputTypeDef],
        "LastModifiedDate": NotRequired[datetime],
    },
)
SetRiskConfigurationRequestRequestTypeDef = TypedDict(
    "SetRiskConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": NotRequired[str],
        "CompromisedCredentialsRiskConfiguration": NotRequired[
            CompromisedCredentialsRiskConfigurationTypeTypeDef
        ],
        "AccountTakeoverRiskConfiguration": NotRequired[
            AccountTakeoverRiskConfigurationTypeTypeDef
        ],
        "RiskExceptionConfiguration": NotRequired[RiskExceptionConfigurationTypeTypeDef],
    },
)
CreateUserPoolResponseTypeDef = TypedDict(
    "CreateUserPoolResponseTypeDef",
    {
        "UserPool": UserPoolTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUserPoolResponseTypeDef = TypedDict(
    "DescribeUserPoolResponseTypeDef",
    {
        "UserPool": UserPoolTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRiskConfigurationResponseTypeDef = TypedDict(
    "DescribeRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": RiskConfigurationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetRiskConfigurationResponseTypeDef = TypedDict(
    "SetRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": RiskConfigurationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
