"""
Type annotations for cognito-idp service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cognito_idp.client import CognitoIdentityProviderClient

    session = Session()
    client: CognitoIdentityProviderClient = session.client("cognito-idp")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    AdminListGroupsForUserPaginator,
    AdminListUserAuthEventsPaginator,
    ListGroupsPaginator,
    ListIdentityProvidersPaginator,
    ListResourceServersPaginator,
    ListUserPoolClientsPaginator,
    ListUserPoolsPaginator,
    ListUsersInGroupPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AddCustomAttributesRequestRequestTypeDef,
    AdminAddUserToGroupRequestRequestTypeDef,
    AdminConfirmSignUpRequestRequestTypeDef,
    AdminCreateUserRequestRequestTypeDef,
    AdminCreateUserResponseTypeDef,
    AdminDeleteUserAttributesRequestRequestTypeDef,
    AdminDeleteUserRequestRequestTypeDef,
    AdminDisableProviderForUserRequestRequestTypeDef,
    AdminDisableUserRequestRequestTypeDef,
    AdminEnableUserRequestRequestTypeDef,
    AdminForgetDeviceRequestRequestTypeDef,
    AdminGetDeviceRequestRequestTypeDef,
    AdminGetDeviceResponseTypeDef,
    AdminGetUserRequestRequestTypeDef,
    AdminGetUserResponseTypeDef,
    AdminInitiateAuthRequestRequestTypeDef,
    AdminInitiateAuthResponseTypeDef,
    AdminLinkProviderForUserRequestRequestTypeDef,
    AdminListDevicesRequestRequestTypeDef,
    AdminListDevicesResponseTypeDef,
    AdminListGroupsForUserRequestRequestTypeDef,
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsRequestRequestTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    AdminRemoveUserFromGroupRequestRequestTypeDef,
    AdminResetUserPasswordRequestRequestTypeDef,
    AdminRespondToAuthChallengeRequestRequestTypeDef,
    AdminRespondToAuthChallengeResponseTypeDef,
    AdminSetUserMFAPreferenceRequestRequestTypeDef,
    AdminSetUserPasswordRequestRequestTypeDef,
    AdminSetUserSettingsRequestRequestTypeDef,
    AdminUpdateAuthEventFeedbackRequestRequestTypeDef,
    AdminUpdateDeviceStatusRequestRequestTypeDef,
    AdminUpdateUserAttributesRequestRequestTypeDef,
    AdminUserGlobalSignOutRequestRequestTypeDef,
    AssociateSoftwareTokenRequestRequestTypeDef,
    AssociateSoftwareTokenResponseTypeDef,
    ChangePasswordRequestRequestTypeDef,
    ConfirmDeviceRequestRequestTypeDef,
    ConfirmDeviceResponseTypeDef,
    ConfirmForgotPasswordRequestRequestTypeDef,
    ConfirmSignUpRequestRequestTypeDef,
    CreateGroupRequestRequestTypeDef,
    CreateGroupResponseTypeDef,
    CreateIdentityProviderRequestRequestTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateResourceServerRequestRequestTypeDef,
    CreateResourceServerResponseTypeDef,
    CreateUserImportJobRequestRequestTypeDef,
    CreateUserImportJobResponseTypeDef,
    CreateUserPoolClientRequestRequestTypeDef,
    CreateUserPoolClientResponseTypeDef,
    CreateUserPoolDomainRequestRequestTypeDef,
    CreateUserPoolDomainResponseTypeDef,
    CreateUserPoolRequestRequestTypeDef,
    CreateUserPoolResponseTypeDef,
    DeleteGroupRequestRequestTypeDef,
    DeleteIdentityProviderRequestRequestTypeDef,
    DeleteResourceServerRequestRequestTypeDef,
    DeleteUserAttributesRequestRequestTypeDef,
    DeleteUserPoolClientRequestRequestTypeDef,
    DeleteUserPoolDomainRequestRequestTypeDef,
    DeleteUserPoolRequestRequestTypeDef,
    DeleteUserRequestRequestTypeDef,
    DescribeIdentityProviderRequestRequestTypeDef,
    DescribeIdentityProviderResponseTypeDef,
    DescribeResourceServerRequestRequestTypeDef,
    DescribeResourceServerResponseTypeDef,
    DescribeRiskConfigurationRequestRequestTypeDef,
    DescribeRiskConfigurationResponseTypeDef,
    DescribeUserImportJobRequestRequestTypeDef,
    DescribeUserImportJobResponseTypeDef,
    DescribeUserPoolClientRequestRequestTypeDef,
    DescribeUserPoolClientResponseTypeDef,
    DescribeUserPoolDomainRequestRequestTypeDef,
    DescribeUserPoolDomainResponseTypeDef,
    DescribeUserPoolRequestRequestTypeDef,
    DescribeUserPoolResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ForgetDeviceRequestRequestTypeDef,
    ForgotPasswordRequestRequestTypeDef,
    ForgotPasswordResponseTypeDef,
    GetCSVHeaderRequestRequestTypeDef,
    GetCSVHeaderResponseTypeDef,
    GetDeviceRequestRequestTypeDef,
    GetDeviceResponseTypeDef,
    GetGroupRequestRequestTypeDef,
    GetGroupResponseTypeDef,
    GetIdentityProviderByIdentifierRequestRequestTypeDef,
    GetIdentityProviderByIdentifierResponseTypeDef,
    GetLogDeliveryConfigurationRequestRequestTypeDef,
    GetLogDeliveryConfigurationResponseTypeDef,
    GetSigningCertificateRequestRequestTypeDef,
    GetSigningCertificateResponseTypeDef,
    GetUICustomizationRequestRequestTypeDef,
    GetUICustomizationResponseTypeDef,
    GetUserAttributeVerificationCodeRequestRequestTypeDef,
    GetUserAttributeVerificationCodeResponseTypeDef,
    GetUserPoolMfaConfigRequestRequestTypeDef,
    GetUserPoolMfaConfigResponseTypeDef,
    GetUserRequestRequestTypeDef,
    GetUserResponseTypeDef,
    GlobalSignOutRequestRequestTypeDef,
    InitiateAuthRequestRequestTypeDef,
    InitiateAuthResponseTypeDef,
    ListDevicesRequestRequestTypeDef,
    ListDevicesResponseTypeDef,
    ListGroupsRequestRequestTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersRequestRequestTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersRequestRequestTypeDef,
    ListResourceServersResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUserImportJobsRequestRequestTypeDef,
    ListUserImportJobsResponseTypeDef,
    ListUserPoolClientsRequestRequestTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsRequestRequestTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupRequestRequestTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersRequestRequestTypeDef,
    ListUsersResponseTypeDef,
    ResendConfirmationCodeRequestRequestTypeDef,
    ResendConfirmationCodeResponseTypeDef,
    RespondToAuthChallengeRequestRequestTypeDef,
    RespondToAuthChallengeResponseTypeDef,
    RevokeTokenRequestRequestTypeDef,
    SetLogDeliveryConfigurationRequestRequestTypeDef,
    SetLogDeliveryConfigurationResponseTypeDef,
    SetRiskConfigurationRequestRequestTypeDef,
    SetRiskConfigurationResponseTypeDef,
    SetUICustomizationRequestRequestTypeDef,
    SetUICustomizationResponseTypeDef,
    SetUserMFAPreferenceRequestRequestTypeDef,
    SetUserPoolMfaConfigRequestRequestTypeDef,
    SetUserPoolMfaConfigResponseTypeDef,
    SetUserSettingsRequestRequestTypeDef,
    SignUpRequestRequestTypeDef,
    SignUpResponseTypeDef,
    StartUserImportJobRequestRequestTypeDef,
    StartUserImportJobResponseTypeDef,
    StopUserImportJobRequestRequestTypeDef,
    StopUserImportJobResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAuthEventFeedbackRequestRequestTypeDef,
    UpdateDeviceStatusRequestRequestTypeDef,
    UpdateGroupRequestRequestTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIdentityProviderRequestRequestTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateResourceServerRequestRequestTypeDef,
    UpdateResourceServerResponseTypeDef,
    UpdateUserAttributesRequestRequestTypeDef,
    UpdateUserAttributesResponseTypeDef,
    UpdateUserPoolClientRequestRequestTypeDef,
    UpdateUserPoolClientResponseTypeDef,
    UpdateUserPoolDomainRequestRequestTypeDef,
    UpdateUserPoolDomainResponseTypeDef,
    UpdateUserPoolRequestRequestTypeDef,
    VerifySoftwareTokenRequestRequestTypeDef,
    VerifySoftwareTokenResponseTypeDef,
    VerifyUserAttributeRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CognitoIdentityProviderClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AliasExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CodeDeliveryFailureException: Type[BotocoreClientError]
    CodeMismatchException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DuplicateProviderException: Type[BotocoreClientError]
    EnableSoftwareTokenMFAException: Type[BotocoreClientError]
    ExpiredCodeException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GroupExistsException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidEmailRoleAccessPolicyException: Type[BotocoreClientError]
    InvalidLambdaResponseException: Type[BotocoreClientError]
    InvalidOAuthFlowException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    InvalidSmsRoleAccessPolicyException: Type[BotocoreClientError]
    InvalidSmsRoleTrustRelationshipException: Type[BotocoreClientError]
    InvalidUserPoolConfigurationException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MFAMethodNotFoundException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    PasswordHistoryPolicyViolationException: Type[BotocoreClientError]
    PasswordResetRequiredException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ScopeDoesNotExistException: Type[BotocoreClientError]
    SoftwareTokenMFANotFoundException: Type[BotocoreClientError]
    TooManyFailedAttemptsException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnexpectedLambdaException: Type[BotocoreClientError]
    UnsupportedIdentityProviderException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UnsupportedTokenTypeException: Type[BotocoreClientError]
    UnsupportedUserStateException: Type[BotocoreClientError]
    UserImportInProgressException: Type[BotocoreClientError]
    UserLambdaValidationException: Type[BotocoreClientError]
    UserNotConfirmedException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]
    UserPoolAddOnNotEnabledException: Type[BotocoreClientError]
    UserPoolTaggingException: Type[BotocoreClientError]
    UsernameExistsException: Type[BotocoreClientError]

class CognitoIdentityProviderClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CognitoIdentityProviderClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#exceptions)
        """

    def add_custom_attributes(
        self, **kwargs: Unpack[AddCustomAttributesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds additional user attributes to the user pool schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.add_custom_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#add_custom_attributes)
        """

    def admin_add_user_to_group(
        self, **kwargs: Unpack[AdminAddUserToGroupRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a user to a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_add_user_to_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_add_user_to_group)
        """

    def admin_confirm_sign_up(
        self, **kwargs: Unpack[AdminConfirmSignUpRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This IAM-authenticated API operation confirms user sign-up as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_confirm_sign_up)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_confirm_sign_up)
        """

    def admin_create_user(
        self, **kwargs: Unpack[AdminCreateUserRequestRequestTypeDef]
    ) -> AdminCreateUserResponseTypeDef:
        """
        Creates a new user in the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_create_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_create_user)
        """

    def admin_delete_user(
        self, **kwargs: Unpack[AdminDeleteUserRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_delete_user)
        """

    def admin_delete_user_attributes(
        self, **kwargs: Unpack[AdminDeleteUserAttributesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the user attributes in a user pool as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_delete_user_attributes)
        """

    def admin_disable_provider_for_user(
        self, **kwargs: Unpack[AdminDisableProviderForUserRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Prevents the user from signing in with the specified external (SAML or social)
        identity provider
        (IdP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_provider_for_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_disable_provider_for_user)
        """

    def admin_disable_user(
        self, **kwargs: Unpack[AdminDisableUserRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deactivates a user and revokes all access tokens for the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_disable_user)
        """

    def admin_enable_user(
        self, **kwargs: Unpack[AdminEnableUserRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enables the specified user as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_enable_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_enable_user)
        """

    def admin_forget_device(
        self, **kwargs: Unpack[AdminForgetDeviceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Forgets the device, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_forget_device)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_forget_device)
        """

    def admin_get_device(
        self, **kwargs: Unpack[AdminGetDeviceRequestRequestTypeDef]
    ) -> AdminGetDeviceResponseTypeDef:
        """
        Gets the device, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_device)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_get_device)
        """

    def admin_get_user(
        self, **kwargs: Unpack[AdminGetUserRequestRequestTypeDef]
    ) -> AdminGetUserResponseTypeDef:
        """
        Gets the specified user by user name in a user pool as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_get_user)
        """

    def admin_initiate_auth(
        self, **kwargs: Unpack[AdminInitiateAuthRequestRequestTypeDef]
    ) -> AdminInitiateAuthResponseTypeDef:
        """
        Initiates the authentication flow, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_initiate_auth)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_initiate_auth)
        """

    def admin_link_provider_for_user(
        self, **kwargs: Unpack[AdminLinkProviderForUserRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Links an existing user account in a user pool ( `DestinationUser`) to an
        identity from an external IdP ( `SourceUser`) based on a specified attribute
        name and value from the external
        IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_link_provider_for_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_link_provider_for_user)
        """

    def admin_list_devices(
        self, **kwargs: Unpack[AdminListDevicesRequestRequestTypeDef]
    ) -> AdminListDevicesResponseTypeDef:
        """
        Lists devices, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_devices)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_list_devices)
        """

    def admin_list_groups_for_user(
        self, **kwargs: Unpack[AdminListGroupsForUserRequestRequestTypeDef]
    ) -> AdminListGroupsForUserResponseTypeDef:
        """
        Lists the groups that a user belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_groups_for_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_list_groups_for_user)
        """

    def admin_list_user_auth_events(
        self, **kwargs: Unpack[AdminListUserAuthEventsRequestRequestTypeDef]
    ) -> AdminListUserAuthEventsResponseTypeDef:
        """
        A history of user activity and any risks detected as part of Amazon Cognito
        advanced
        security.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_user_auth_events)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_list_user_auth_events)
        """

    def admin_remove_user_from_group(
        self, **kwargs: Unpack[AdminRemoveUserFromGroupRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified user from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_remove_user_from_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_remove_user_from_group)
        """

    def admin_reset_user_password(
        self, **kwargs: Unpack[AdminResetUserPasswordRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Resets the specified user's password in a user pool as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_reset_user_password)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_reset_user_password)
        """

    def admin_respond_to_auth_challenge(
        self, **kwargs: Unpack[AdminRespondToAuthChallengeRequestRequestTypeDef]
    ) -> AdminRespondToAuthChallengeResponseTypeDef:
        """
        Some API operations in a user pool generate a challenge, like a prompt for an
        MFA code, for device authentication that bypasses MFA, or for a custom
        authentication
        challenge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_respond_to_auth_challenge)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_respond_to_auth_challenge)
        """

    def admin_set_user_mfa_preference(
        self, **kwargs: Unpack[AdminSetUserMFAPreferenceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the user's multi-factor authentication (MFA) preference, including which
        MFA options are activated, and if any are
        preferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_mfa_preference)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_set_user_mfa_preference)
        """

    def admin_set_user_password(
        self, **kwargs: Unpack[AdminSetUserPasswordRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the specified user's password in a user pool as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_password)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_set_user_password)
        """

    def admin_set_user_settings(
        self, **kwargs: Unpack[AdminSetUserSettingsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        *This action is no longer supported.* You can use it to configure only SMS MFA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_set_user_settings)
        """

    def admin_update_auth_event_feedback(
        self, **kwargs: Unpack[AdminUpdateAuthEventFeedbackRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Provides feedback for an authentication event indicating if it was from a valid
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_auth_event_feedback)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_update_auth_event_feedback)
        """

    def admin_update_device_status(
        self, **kwargs: Unpack[AdminUpdateDeviceStatusRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the device status as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_device_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_update_device_status)
        """

    def admin_update_user_attributes(
        self, **kwargs: Unpack[AdminUpdateUserAttributesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_user_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_update_user_attributes)
        """

    def admin_user_global_sign_out(
        self, **kwargs: Unpack[AdminUserGlobalSignOutRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Invalidates the identity, access, and refresh tokens that Amazon Cognito issued
        to a
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_user_global_sign_out)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_user_global_sign_out)
        """

    def associate_software_token(
        self, **kwargs: Unpack[AssociateSoftwareTokenRequestRequestTypeDef]
    ) -> AssociateSoftwareTokenResponseTypeDef:
        """
        Begins setup of time-based one-time password (TOTP) multi-factor authentication
        (MFA) for a user, with a unique private key that Amazon Cognito generates and
        returns in the API
        response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.associate_software_token)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#associate_software_token)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#can_paginate)
        """

    def change_password(
        self, **kwargs: Unpack[ChangePasswordRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Changes the password for a specified user in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.change_password)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#change_password)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#close)
        """

    def confirm_device(
        self, **kwargs: Unpack[ConfirmDeviceRequestRequestTypeDef]
    ) -> ConfirmDeviceResponseTypeDef:
        """
        Confirms tracking of the device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_device)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#confirm_device)
        """

    def confirm_forgot_password(
        self, **kwargs: Unpack[ConfirmForgotPasswordRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Allows a user to enter a confirmation code to reset a forgotten password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_forgot_password)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#confirm_forgot_password)
        """

    def confirm_sign_up(
        self, **kwargs: Unpack[ConfirmSignUpRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This public API operation provides a code that Amazon Cognito sent to your user
        when they signed up in your user pool via the
        [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html)
        API
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_sign_up)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#confirm_sign_up)
        """

    def create_group(
        self, **kwargs: Unpack[CreateGroupRequestRequestTypeDef]
    ) -> CreateGroupResponseTypeDef:
        """
        Creates a new group in the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_group)
        """

    def create_identity_provider(
        self, **kwargs: Unpack[CreateIdentityProviderRequestRequestTypeDef]
    ) -> CreateIdentityProviderResponseTypeDef:
        """
        Adds a configuration and trust relationship between a third-party identity
        provider (IdP) and a user
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_identity_provider)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_identity_provider)
        """

    def create_resource_server(
        self, **kwargs: Unpack[CreateResourceServerRequestRequestTypeDef]
    ) -> CreateResourceServerResponseTypeDef:
        """
        Creates a new OAuth2.0 resource server and defines custom scopes within it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_resource_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_resource_server)
        """

    def create_user_import_job(
        self, **kwargs: Unpack[CreateUserImportJobRequestRequestTypeDef]
    ) -> CreateUserImportJobResponseTypeDef:
        """
        Creates a user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_user_import_job)
        """

    def create_user_pool(
        self, **kwargs: Unpack[CreateUserPoolRequestRequestTypeDef]
    ) -> CreateUserPoolResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_user_pool)
        """

    def create_user_pool_client(
        self, **kwargs: Unpack[CreateUserPoolClientRequestRequestTypeDef]
    ) -> CreateUserPoolClientResponseTypeDef:
        """
        Creates the user pool client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_client)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_user_pool_client)
        """

    def create_user_pool_domain(
        self, **kwargs: Unpack[CreateUserPoolDomainRequestRequestTypeDef]
    ) -> CreateUserPoolDomainResponseTypeDef:
        """
        Creates a new domain for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_domain)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_user_pool_domain)
        """

    def delete_group(
        self, **kwargs: Unpack[DeleteGroupRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_group)
        """

    def delete_identity_provider(
        self, **kwargs: Unpack[DeleteIdentityProviderRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an IdP for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_identity_provider)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_identity_provider)
        """

    def delete_resource_server(
        self, **kwargs: Unpack[DeleteResourceServerRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_resource_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_resource_server)
        """

    def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Allows a user to delete their own user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user)
        """

    def delete_user_attributes(
        self, **kwargs: Unpack[DeleteUserAttributesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the attributes for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user_attributes)
        """

    def delete_user_pool(
        self, **kwargs: Unpack[DeleteUserPoolRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user_pool)
        """

    def delete_user_pool_client(
        self, **kwargs: Unpack[DeleteUserPoolClientRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Allows the developer to delete the user pool client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_client)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user_pool_client)
        """

    def delete_user_pool_domain(
        self, **kwargs: Unpack[DeleteUserPoolDomainRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a domain for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_domain)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user_pool_domain)
        """

    def describe_identity_provider(
        self, **kwargs: Unpack[DescribeIdentityProviderRequestRequestTypeDef]
    ) -> DescribeIdentityProviderResponseTypeDef:
        """
        Gets information about a specific IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_identity_provider)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_identity_provider)
        """

    def describe_resource_server(
        self, **kwargs: Unpack[DescribeResourceServerRequestRequestTypeDef]
    ) -> DescribeResourceServerResponseTypeDef:
        """
        Describes a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_resource_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_resource_server)
        """

    def describe_risk_configuration(
        self, **kwargs: Unpack[DescribeRiskConfigurationRequestRequestTypeDef]
    ) -> DescribeRiskConfigurationResponseTypeDef:
        """
        Describes the risk configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_risk_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_risk_configuration)
        """

    def describe_user_import_job(
        self, **kwargs: Unpack[DescribeUserImportJobRequestRequestTypeDef]
    ) -> DescribeUserImportJobResponseTypeDef:
        """
        Describes the user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_user_import_job)
        """

    def describe_user_pool(
        self, **kwargs: Unpack[DescribeUserPoolRequestRequestTypeDef]
    ) -> DescribeUserPoolResponseTypeDef:
        """
        Returns the configuration information and metadata of the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_user_pool)
        """

    def describe_user_pool_client(
        self, **kwargs: Unpack[DescribeUserPoolClientRequestRequestTypeDef]
    ) -> DescribeUserPoolClientResponseTypeDef:
        """
        Client method for returning the configuration information and metadata of the
        specified user pool app
        client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_client)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_user_pool_client)
        """

    def describe_user_pool_domain(
        self, **kwargs: Unpack[DescribeUserPoolDomainRequestRequestTypeDef]
    ) -> DescribeUserPoolDomainResponseTypeDef:
        """
        Gets information about a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_domain)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_user_pool_domain)
        """

    def forget_device(
        self, **kwargs: Unpack[ForgetDeviceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Forgets the specified device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forget_device)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#forget_device)
        """

    def forgot_password(
        self, **kwargs: Unpack[ForgotPasswordRequestRequestTypeDef]
    ) -> ForgotPasswordResponseTypeDef:
        """
        Calling this API causes a message to be sent to the end user with a
        confirmation code that is required to change the user's
        password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forgot_password)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#forgot_password)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#generate_presigned_url)
        """

    def get_csv_header(
        self, **kwargs: Unpack[GetCSVHeaderRequestRequestTypeDef]
    ) -> GetCSVHeaderResponseTypeDef:
        """
        Gets the header information for the comma-separated value (CSV) file to be used
        as input for the user import
        job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_csv_header)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_csv_header)
        """

    def get_device(
        self, **kwargs: Unpack[GetDeviceRequestRequestTypeDef]
    ) -> GetDeviceResponseTypeDef:
        """
        Gets the device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_device)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_device)
        """

    def get_group(self, **kwargs: Unpack[GetGroupRequestRequestTypeDef]) -> GetGroupResponseTypeDef:
        """
        Gets a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_group)
        """

    def get_identity_provider_by_identifier(
        self, **kwargs: Unpack[GetIdentityProviderByIdentifierRequestRequestTypeDef]
    ) -> GetIdentityProviderByIdentifierResponseTypeDef:
        """
        Gets the specified IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_identity_provider_by_identifier)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_identity_provider_by_identifier)
        """

    def get_log_delivery_configuration(
        self, **kwargs: Unpack[GetLogDeliveryConfigurationRequestRequestTypeDef]
    ) -> GetLogDeliveryConfigurationResponseTypeDef:
        """
        Gets the logging configuration of a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_log_delivery_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_log_delivery_configuration)
        """

    def get_signing_certificate(
        self, **kwargs: Unpack[GetSigningCertificateRequestRequestTypeDef]
    ) -> GetSigningCertificateResponseTypeDef:
        """
        This method takes a user pool ID, and returns the signing certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_signing_certificate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_signing_certificate)
        """

    def get_ui_customization(
        self, **kwargs: Unpack[GetUICustomizationRequestRequestTypeDef]
    ) -> GetUICustomizationResponseTypeDef:
        """
        Gets the user interface (UI) Customization information for a particular app
        client's app UI, if any such information exists for the
        client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_ui_customization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_ui_customization)
        """

    def get_user(self, **kwargs: Unpack[GetUserRequestRequestTypeDef]) -> GetUserResponseTypeDef:
        """
        Gets the user attributes and metadata for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_user)
        """

    def get_user_attribute_verification_code(
        self, **kwargs: Unpack[GetUserAttributeVerificationCodeRequestRequestTypeDef]
    ) -> GetUserAttributeVerificationCodeResponseTypeDef:
        """
        Generates a user attribute verification code for the specified attribute name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_attribute_verification_code)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_user_attribute_verification_code)
        """

    def get_user_pool_mfa_config(
        self, **kwargs: Unpack[GetUserPoolMfaConfigRequestRequestTypeDef]
    ) -> GetUserPoolMfaConfigResponseTypeDef:
        """
        Gets the user pool multi-factor authentication (MFA) configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_pool_mfa_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_user_pool_mfa_config)
        """

    def global_sign_out(
        self, **kwargs: Unpack[GlobalSignOutRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Invalidates the identity, access, and refresh tokens that Amazon Cognito issued
        to a
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.global_sign_out)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#global_sign_out)
        """

    def initiate_auth(
        self, **kwargs: Unpack[InitiateAuthRequestRequestTypeDef]
    ) -> InitiateAuthResponseTypeDef:
        """
        Initiates sign-in for a user in the Amazon Cognito user directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.initiate_auth)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#initiate_auth)
        """

    def list_devices(
        self, **kwargs: Unpack[ListDevicesRequestRequestTypeDef]
    ) -> ListDevicesResponseTypeDef:
        """
        Lists the sign-in devices that Amazon Cognito has registered to the current
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_devices)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_devices)
        """

    def list_groups(
        self, **kwargs: Unpack[ListGroupsRequestRequestTypeDef]
    ) -> ListGroupsResponseTypeDef:
        """
        Lists the groups associated with a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_groups)
        """

    def list_identity_providers(
        self, **kwargs: Unpack[ListIdentityProvidersRequestRequestTypeDef]
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Lists information about all IdPs for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_identity_providers)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_identity_providers)
        """

    def list_resource_servers(
        self, **kwargs: Unpack[ListResourceServersRequestRequestTypeDef]
    ) -> ListResourceServersResponseTypeDef:
        """
        Lists the resource servers for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_resource_servers)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_resource_servers)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are assigned to an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_tags_for_resource)
        """

    def list_user_import_jobs(
        self, **kwargs: Unpack[ListUserImportJobsRequestRequestTypeDef]
    ) -> ListUserImportJobsResponseTypeDef:
        """
        Lists user import jobs for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_import_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_user_import_jobs)
        """

    def list_user_pool_clients(
        self, **kwargs: Unpack[ListUserPoolClientsRequestRequestTypeDef]
    ) -> ListUserPoolClientsResponseTypeDef:
        """
        Lists the clients that have been created for the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pool_clients)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_user_pool_clients)
        """

    def list_user_pools(
        self, **kwargs: Unpack[ListUserPoolsRequestRequestTypeDef]
    ) -> ListUserPoolsResponseTypeDef:
        """
        Lists the user pools associated with an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pools)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_user_pools)
        """

    def list_users(
        self, **kwargs: Unpack[ListUsersRequestRequestTypeDef]
    ) -> ListUsersResponseTypeDef:
        """
        Lists users and their basic details in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_users)
        """

    def list_users_in_group(
        self, **kwargs: Unpack[ListUsersInGroupRequestRequestTypeDef]
    ) -> ListUsersInGroupResponseTypeDef:
        """
        Lists the users in the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users_in_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_users_in_group)
        """

    def resend_confirmation_code(
        self, **kwargs: Unpack[ResendConfirmationCodeRequestRequestTypeDef]
    ) -> ResendConfirmationCodeResponseTypeDef:
        """
        Resends the confirmation (for confirmation of registration) to a specific user
        in the user
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.resend_confirmation_code)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#resend_confirmation_code)
        """

    def respond_to_auth_challenge(
        self, **kwargs: Unpack[RespondToAuthChallengeRequestRequestTypeDef]
    ) -> RespondToAuthChallengeResponseTypeDef:
        """
        Some API operations in a user pool generate a challenge, like a prompt for an
        MFA code, for device authentication that bypasses MFA, or for a custom
        authentication
        challenge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.respond_to_auth_challenge)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#respond_to_auth_challenge)
        """

    def revoke_token(self, **kwargs: Unpack[RevokeTokenRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Revokes all of the access tokens generated by, and at the same time as, the
        specified refresh
        token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.revoke_token)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#revoke_token)
        """

    def set_log_delivery_configuration(
        self, **kwargs: Unpack[SetLogDeliveryConfigurationRequestRequestTypeDef]
    ) -> SetLogDeliveryConfigurationResponseTypeDef:
        """
        Sets up or modifies the logging configuration of a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_log_delivery_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_log_delivery_configuration)
        """

    def set_risk_configuration(
        self, **kwargs: Unpack[SetRiskConfigurationRequestRequestTypeDef]
    ) -> SetRiskConfigurationResponseTypeDef:
        """
        Configures actions on detected risks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_risk_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_risk_configuration)
        """

    def set_ui_customization(
        self, **kwargs: Unpack[SetUICustomizationRequestRequestTypeDef]
    ) -> SetUICustomizationResponseTypeDef:
        """
        Sets the user interface (UI) customization information for a user pool's
        built-in app
        UI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_ui_customization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_ui_customization)
        """

    def set_user_mfa_preference(
        self, **kwargs: Unpack[SetUserMFAPreferenceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Set the user's multi-factor authentication (MFA) method preference, including
        which MFA factors are activated and if any are
        preferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_mfa_preference)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_user_mfa_preference)
        """

    def set_user_pool_mfa_config(
        self, **kwargs: Unpack[SetUserPoolMfaConfigRequestRequestTypeDef]
    ) -> SetUserPoolMfaConfigResponseTypeDef:
        """
        Sets the user pool multi-factor authentication (MFA) configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_pool_mfa_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_user_pool_mfa_config)
        """

    def set_user_settings(
        self, **kwargs: Unpack[SetUserSettingsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        *This action is no longer supported.* You can use it to configure only SMS MFA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_user_settings)
        """

    def sign_up(self, **kwargs: Unpack[SignUpRequestRequestTypeDef]) -> SignUpResponseTypeDef:
        """
        Registers the user in the specified user pool and creates a user name,
        password, and user
        attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.sign_up)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#sign_up)
        """

    def start_user_import_job(
        self, **kwargs: Unpack[StartUserImportJobRequestRequestTypeDef]
    ) -> StartUserImportJobResponseTypeDef:
        """
        Starts the user import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.start_user_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#start_user_import_job)
        """

    def stop_user_import_job(
        self, **kwargs: Unpack[StopUserImportJobRequestRequestTypeDef]
    ) -> StopUserImportJobResponseTypeDef:
        """
        Stops the user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.stop_user_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#stop_user_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns a set of tags to an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified tags from an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#untag_resource)
        """

    def update_auth_event_feedback(
        self, **kwargs: Unpack[UpdateAuthEventFeedbackRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Provides the feedback for an authentication event, whether it was from a valid
        user or
        not.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_auth_event_feedback)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_auth_event_feedback)
        """

    def update_device_status(
        self, **kwargs: Unpack[UpdateDeviceStatusRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the device status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_device_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_device_status)
        """

    def update_group(
        self, **kwargs: Unpack[UpdateGroupRequestRequestTypeDef]
    ) -> UpdateGroupResponseTypeDef:
        """
        Updates the specified group with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_group)
        """

    def update_identity_provider(
        self, **kwargs: Unpack[UpdateIdentityProviderRequestRequestTypeDef]
    ) -> UpdateIdentityProviderResponseTypeDef:
        """
        Updates IdP information for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_identity_provider)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_identity_provider)
        """

    def update_resource_server(
        self, **kwargs: Unpack[UpdateResourceServerRequestRequestTypeDef]
    ) -> UpdateResourceServerResponseTypeDef:
        """
        Updates the name and scopes of resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_resource_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_resource_server)
        """

    def update_user_attributes(
        self, **kwargs: Unpack[UpdateUserAttributesRequestRequestTypeDef]
    ) -> UpdateUserAttributesResponseTypeDef:
        """
        With this operation, your users can update one or more of their attributes with
        their own
        credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_user_attributes)
        """

    def update_user_pool(
        self, **kwargs: Unpack[UpdateUserPoolRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_user_pool)
        """

    def update_user_pool_client(
        self, **kwargs: Unpack[UpdateUserPoolClientRequestRequestTypeDef]
    ) -> UpdateUserPoolClientResponseTypeDef:
        """
        Updates the specified user pool app client with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_client)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_user_pool_client)
        """

    def update_user_pool_domain(
        self, **kwargs: Unpack[UpdateUserPoolDomainRequestRequestTypeDef]
    ) -> UpdateUserPoolDomainResponseTypeDef:
        """
        Updates the Secure Sockets Layer (SSL) certificate for the custom domain for
        your user
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_domain)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_user_pool_domain)
        """

    def verify_software_token(
        self, **kwargs: Unpack[VerifySoftwareTokenRequestRequestTypeDef]
    ) -> VerifySoftwareTokenResponseTypeDef:
        """
        Use this API to register a user's entered time-based one-time password (TOTP)
        code and mark the user's software token MFA status as "verified" if
        successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_software_token)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#verify_software_token)
        """

    def verify_user_attribute(
        self, **kwargs: Unpack[VerifyUserAttributeRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Verifies the specified user attributes in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_user_attribute)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#verify_user_attribute)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["admin_list_groups_for_user"]
    ) -> AdminListGroupsForUserPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["admin_list_user_auth_events"]
    ) -> AdminListUserAuthEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_providers"]
    ) -> ListIdentityProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_servers"]
    ) -> ListResourceServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_pool_clients"]
    ) -> ListUserPoolClientsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_user_pools"]) -> ListUserPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_users_in_group"]
    ) -> ListUsersInGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """
