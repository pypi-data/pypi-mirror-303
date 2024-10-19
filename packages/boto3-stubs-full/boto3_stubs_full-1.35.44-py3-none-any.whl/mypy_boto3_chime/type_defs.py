"""
Type annotations for chime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AccountStatusType,
    AccountTypeType,
    AppInstanceDataTypeType,
    ArtifactsStateType,
    AudioMuxTypeType,
    CallingNameStatusType,
    CapabilityType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    EmailStatusType,
    ErrorCodeType,
    GeoMatchLevelType,
    InviteStatusType,
    LicenseType,
    MediaPipelineStatusType,
    MemberTypeType,
    NotificationTargetType,
    NumberSelectionBehaviorType,
    OrderedPhoneNumberStatusType,
    OriginationRouteProtocolType,
    PhoneNumberAssociationNameType,
    PhoneNumberOrderStatusType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    RegistrationStatusType,
    RoomMembershipRoleType,
    SipRuleTriggerTypeType,
    SortOrderType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribePartialResultsStabilityType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
    UserTypeType,
    VoiceConnectorAwsRegionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AccountSettingsTypeDef",
    "SigninDelegateGroupTypeDef",
    "AddressTypeDef",
    "AlexaForBusinessMetadataTypeDef",
    "IdentityTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "AppInstanceStreamingConfigurationTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "AppInstanceUserMembershipSummaryTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "AppInstanceUserTypeDef",
    "AudioArtifactsConfigurationTypeDef",
    "ContentArtifactsConfigurationTypeDef",
    "VideoArtifactsConfigurationTypeDef",
    "AssociatePhoneNumberWithUserRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    "PhoneNumberErrorTypeDef",
    "ResponseMetadataTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    "AttendeeTypeDef",
    "CreateAttendeeErrorTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    "MembershipItemTypeDef",
    "MemberErrorTypeDef",
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    "BatchSuspendUserRequestRequestTypeDef",
    "UserErrorTypeDef",
    "BatchUnsuspendUserRequestRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "BotTypeDef",
    "BusinessCallingSettingsTypeDef",
    "CandidateAddressTypeDef",
    "ChannelSummaryTypeDef",
    "ConversationRetentionSettingsTypeDef",
    "CreateAccountRequestRequestTypeDef",
    "CreateAppInstanceAdminRequestRequestTypeDef",
    "TagTypeDef",
    "CreateBotRequestRequestTypeDef",
    "CreateChannelBanRequestRequestTypeDef",
    "CreateChannelMembershipRequestRequestTypeDef",
    "CreateChannelModeratorRequestRequestTypeDef",
    "CreateMeetingDialOutRequestRequestTypeDef",
    "MeetingNotificationConfigurationTypeDef",
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    "GeoMatchParamsTypeDef",
    "CreateRoomMembershipRequestRequestTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "RoomTypeDef",
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "CreateUserRequestRequestTypeDef",
    "VoiceConnectorItemTypeDef",
    "CreateVoiceConnectorRequestRequestTypeDef",
    "VoiceConnectorTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DeleteAccountRequestRequestTypeDef",
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    "DeleteAppInstanceRequestRequestTypeDef",
    "DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "DeleteAppInstanceUserRequestRequestTypeDef",
    "DeleteAttendeeRequestRequestTypeDef",
    "DeleteChannelBanRequestRequestTypeDef",
    "DeleteChannelMembershipRequestRequestTypeDef",
    "DeleteChannelMessageRequestRequestTypeDef",
    "DeleteChannelModeratorRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteEventsConfigurationRequestRequestTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "DeleteMeetingRequestRequestTypeDef",
    "DeletePhoneNumberRequestRequestTypeDef",
    "DeleteProxySessionRequestRequestTypeDef",
    "DeleteRoomMembershipRequestRequestTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    "DeleteSipRuleRequestRequestTypeDef",
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    "DeleteVoiceConnectorRequestRequestTypeDef",
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    "DescribeAppInstanceRequestRequestTypeDef",
    "DescribeAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelBanRequestRequestTypeDef",
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelMembershipRequestRequestTypeDef",
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelModeratorRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DisassociatePhoneNumberFromUserRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    "DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "EventsConfigurationTypeDef",
    "GetAccountRequestRequestTypeDef",
    "GetAccountSettingsRequestRequestTypeDef",
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    "GetAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "GetAttendeeRequestRequestTypeDef",
    "GetBotRequestRequestTypeDef",
    "GetChannelMessageRequestRequestTypeDef",
    "GetEventsConfigurationRequestRequestTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMeetingRequestRequestTypeDef",
    "MessagingSessionEndpointTypeDef",
    "GetPhoneNumberOrderRequestRequestTypeDef",
    "GetPhoneNumberRequestRequestTypeDef",
    "GetProxySessionRequestRequestTypeDef",
    "GetRetentionSettingsRequestRequestTypeDef",
    "GetRoomRequestRequestTypeDef",
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "GetSipMediaApplicationRequestRequestTypeDef",
    "GetSipRuleRequestRequestTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserSettingsRequestRequestTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "LoggingConfigurationTypeDef",
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    "ProxyTypeDef",
    "GetVoiceConnectorRequestRequestTypeDef",
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    "TerminationHealthTypeDef",
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    "TerminationOutputTypeDef",
    "InviteTypeDef",
    "InviteUsersRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccountsRequestRequestTypeDef",
    "ListAppInstanceAdminsRequestRequestTypeDef",
    "ListAppInstanceUsersRequestRequestTypeDef",
    "ListAppInstancesRequestRequestTypeDef",
    "ListAttendeeTagsRequestRequestTypeDef",
    "ListAttendeesRequestRequestTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListChannelBansRequestRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    "ListChannelMembershipsRequestRequestTypeDef",
    "TimestampTypeDef",
    "ListChannelModeratorsRequestRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "ListMeetingTagsRequestRequestTypeDef",
    "ListMeetingsRequestRequestTypeDef",
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListProxySessionsRequestRequestTypeDef",
    "ListRoomMembershipsRequestRequestTypeDef",
    "ListRoomsRequestRequestTypeDef",
    "ListSipMediaApplicationsRequestRequestTypeDef",
    "ListSipRulesRequestRequestTypeDef",
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    "PhoneNumberCountryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "ListVoiceConnectorsRequestRequestTypeDef",
    "LogoutUserRequestRequestTypeDef",
    "MediaPlacementTypeDef",
    "MemberTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "PutEventsConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorProxyRequestRequestTypeDef",
    "TerminationTypeDef",
    "RedactChannelMessageRequestRequestTypeDef",
    "RedactConversationMessageRequestRequestTypeDef",
    "RedactRoomMessageRequestRequestTypeDef",
    "RegenerateSecurityTokenRequestRequestTypeDef",
    "ResetPersonalPINRequestRequestTypeDef",
    "RestorePhoneNumberRequestRequestTypeDef",
    "RoomRetentionSettingsTypeDef",
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    "SelectedVideoStreamsOutputTypeDef",
    "SelectedVideoStreamsTypeDef",
    "SendChannelMessageRequestRequestTypeDef",
    "StopMeetingTranscriptionRequestRequestTypeDef",
    "StreamingNotificationTargetTypeDef",
    "TelephonySettingsTypeDef",
    "UntagAttendeeRequestRequestTypeDef",
    "UntagMeetingRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountRequestRequestTypeDef",
    "UpdateAppInstanceRequestRequestTypeDef",
    "UpdateAppInstanceUserRequestRequestTypeDef",
    "UpdateBotRequestRequestTypeDef",
    "UpdateChannelMessageRequestRequestTypeDef",
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    "UpdateProxySessionRequestRequestTypeDef",
    "UpdateRoomMembershipRequestRequestTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    "UpdateVoiceConnectorRequestRequestTypeDef",
    "ValidateE911AddressRequestRequestTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "AccountTypeDef",
    "AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef",
    "UpdateUserRequestItemTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UserTypeDef",
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "BatchChannelMembershipsTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "PutAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "ArtifactsConfigurationTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateMeetingDialOutResponseTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SendChannelMessageResponseTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "CreateAttendeeResponseTypeDef",
    "GetAttendeeResponseTypeDef",
    "ListAttendeesResponseTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "BatchCreateRoomMembershipRequestRequestTypeDef",
    "BatchCreateRoomMembershipResponseTypeDef",
    "BatchSuspendUserResponseTypeDef",
    "BatchUnsuspendUserResponseTypeDef",
    "BatchUpdateUserResponseTypeDef",
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    "CreateBotResponseTypeDef",
    "GetBotResponseTypeDef",
    "ListBotsResponseTypeDef",
    "RegenerateSecurityTokenResponseTypeDef",
    "UpdateBotResponseTypeDef",
    "ValidateE911AddressResponseTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ListChannelsResponseTypeDef",
    "CreateAppInstanceRequestRequestTypeDef",
    "CreateAppInstanceUserRequestRequestTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestRequestTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "ListAttendeeTagsResponseTypeDef",
    "ListMeetingTagsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagAttendeeRequestRequestTypeDef",
    "TagMeetingRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateMeetingRequestRequestTypeDef",
    "CreateProxySessionRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "GetRoomResponseTypeDef",
    "ListRoomsResponseTypeDef",
    "UpdateRoomResponseTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "UpdateSipMediaApplicationCallResponseTypeDef",
    "CreateSipMediaApplicationRequestRequestTypeDef",
    "SipMediaApplicationTypeDef",
    "UpdateSipMediaApplicationRequestRequestTypeDef",
    "CreateSipRuleRequestRequestTypeDef",
    "SipRuleTypeDef",
    "UpdateSipRuleRequestRequestTypeDef",
    "CreateVoiceConnectorGroupRequestRequestTypeDef",
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    "VoiceConnectorGroupTypeDef",
    "CreateVoiceConnectorResponseTypeDef",
    "GetVoiceConnectorResponseTypeDef",
    "ListVoiceConnectorsResponseTypeDef",
    "UpdateVoiceConnectorResponseTypeDef",
    "PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "EmergencyCallingConfigurationOutputTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "TranscriptionConfigurationTypeDef",
    "GetEventsConfigurationResponseTypeDef",
    "PutEventsConfigurationResponseTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "UpdateGlobalSettingsRequestRequestTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorProxyResponseTypeDef",
    "PutVoiceConnectorProxyResponseTypeDef",
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    "GetVoiceConnectorTerminationResponseTypeDef",
    "PutVoiceConnectorTerminationResponseTypeDef",
    "InviteUsersResponseTypeDef",
    "ListAccountsRequestListAccountsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListChannelMessagesRequestRequestTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "MeetingTypeDef",
    "RoomMembershipTypeDef",
    "PhoneNumberOrderTypeDef",
    "OriginationOutputTypeDef",
    "OriginationTypeDef",
    "ProxySessionTypeDef",
    "PhoneNumberTypeDef",
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    "RetentionSettingsTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SelectedVideoStreamsUnionTypeDef",
    "StreamingConfigurationOutputTypeDef",
    "StreamingConfigurationTypeDef",
    "UserSettingsTypeDef",
    "CreateAccountResponseTypeDef",
    "GetAccountResponseTypeDef",
    "ListAccountsResponseTypeDef",
    "UpdateAccountResponseTypeDef",
    "BatchUpdateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "GetUserResponseTypeDef",
    "ListUsersResponseTypeDef",
    "ResetPersonalPINResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "ListChannelBansResponseTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "GetChannelMessageResponseTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "BatchCreateAttendeeRequestRequestTypeDef",
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    "CreateSipMediaApplicationResponseTypeDef",
    "GetSipMediaApplicationResponseTypeDef",
    "ListSipMediaApplicationsResponseTypeDef",
    "UpdateSipMediaApplicationResponseTypeDef",
    "CreateSipRuleResponseTypeDef",
    "GetSipRuleResponseTypeDef",
    "ListSipRulesResponseTypeDef",
    "UpdateSipRuleResponseTypeDef",
    "CreateVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorGroupResponseTypeDef",
    "ListVoiceConnectorGroupsResponseTypeDef",
    "UpdateVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "StartMeetingTranscriptionRequestRequestTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "GetMeetingResponseTypeDef",
    "ListMeetingsResponseTypeDef",
    "CreateRoomMembershipResponseTypeDef",
    "ListRoomMembershipsResponseTypeDef",
    "UpdateRoomMembershipResponseTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "GetVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    "CreateProxySessionResponseTypeDef",
    "GetProxySessionResponseTypeDef",
    "ListProxySessionsResponseTypeDef",
    "UpdateProxySessionResponseTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "GetRetentionSettingsResponseTypeDef",
    "PutRetentionSettingsRequestRequestTypeDef",
    "PutRetentionSettingsResponseTypeDef",
    "ChimeSdkMeetingConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "GetUserSettingsResponseTypeDef",
    "UpdateUserSettingsRequestRequestTypeDef",
    "MediaCapturePipelineTypeDef",
    "SourceConfigurationUnionTypeDef",
    "CreateMediaCapturePipelineResponseTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ChimeSdkMeetingConfigurationTypeDef",
    "CreateMediaCapturePipelineRequestRequestTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "DisableRemoteControl": NotRequired[bool],
        "EnableDialOut": NotRequired[bool],
    },
)
SigninDelegateGroupTypeDef = TypedDict(
    "SigninDelegateGroupTypeDef",
    {
        "GroupName": NotRequired[str],
    },
)
AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "streetName": NotRequired[str],
        "streetSuffix": NotRequired[str],
        "postDirectional": NotRequired[str],
        "preDirectional": NotRequired[str],
        "streetNumber": NotRequired[str],
        "city": NotRequired[str],
        "state": NotRequired[str],
        "postalCode": NotRequired[str],
        "postalCodePlus4": NotRequired[str],
        "country": NotRequired[str],
    },
)
AlexaForBusinessMetadataTypeDef = TypedDict(
    "AlexaForBusinessMetadataTypeDef",
    {
        "IsAlexaForBusinessEnabled": NotRequired[bool],
        "AlexaForBusinessRoomArn": NotRequired[str],
    },
)
IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef",
    {
        "RetentionDays": NotRequired[int],
    },
)
AppInstanceStreamingConfigurationTypeDef = TypedDict(
    "AppInstanceStreamingConfigurationTypeDef",
    {
        "AppInstanceDataType": AppInstanceDataTypeType,
        "ResourceArn": str,
    },
)
AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef",
    {
        "AppInstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)
AppInstanceTypeDef = TypedDict(
    "AppInstanceTypeDef",
    {
        "AppInstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {
        "Type": NotRequired[ChannelMembershipTypeType],
        "ReadMarkerTimestamp": NotRequired[datetime],
    },
)
AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)
AppInstanceUserTypeDef = TypedDict(
    "AppInstanceUserTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "Metadata": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
AudioArtifactsConfigurationTypeDef = TypedDict(
    "AudioArtifactsConfigurationTypeDef",
    {
        "MuxType": AudioMuxTypeType,
    },
)
ContentArtifactsConfigurationTypeDef = TypedDict(
    "ContentArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
        "MuxType": NotRequired[Literal["ContentOnly"]],
    },
)
VideoArtifactsConfigurationTypeDef = TypedDict(
    "VideoArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
        "MuxType": NotRequired[Literal["VideoOnly"]],
    },
)
AssociatePhoneNumberWithUserRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumberWithUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "E164PhoneNumber": str,
    },
)
AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": Sequence[str],
        "ForceAssociate": NotRequired[bool],
    },
)
PhoneNumberErrorTypeDef = TypedDict(
    "PhoneNumberErrorTypeDef",
    {
        "PhoneNumberId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
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
AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": Sequence[str],
        "ForceAssociate": NotRequired[bool],
    },
)
AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": NotRequired[str],
        "AttendeeId": NotRequired[str],
        "JoinToken": NotRequired[str],
    },
)
CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {
        "ExternalUserId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
BatchCreateChannelMembershipErrorTypeDef = TypedDict(
    "BatchCreateChannelMembershipErrorTypeDef",
    {
        "MemberArn": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
BatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArns": Sequence[str],
        "Type": NotRequired[ChannelMembershipTypeType],
        "ChimeBearer": NotRequired[str],
    },
)
MembershipItemTypeDef = TypedDict(
    "MembershipItemTypeDef",
    {
        "MemberId": NotRequired[str],
        "Role": NotRequired[RoomMembershipRoleType],
    },
)
MemberErrorTypeDef = TypedDict(
    "MemberErrorTypeDef",
    {
        "MemberId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
BatchDeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberIds": Sequence[str],
    },
)
BatchSuspendUserRequestRequestTypeDef = TypedDict(
    "BatchSuspendUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserIdList": Sequence[str],
    },
)
UserErrorTypeDef = TypedDict(
    "UserErrorTypeDef",
    {
        "UserId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
BatchUnsuspendUserRequestRequestTypeDef = TypedDict(
    "BatchUnsuspendUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserIdList": Sequence[str],
    },
)
UpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "UpdatePhoneNumberRequestItemTypeDef",
    {
        "PhoneNumberId": str,
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "CallingName": NotRequired[str],
    },
)
BotTypeDef = TypedDict(
    "BotTypeDef",
    {
        "BotId": NotRequired[str],
        "UserId": NotRequired[str],
        "DisplayName": NotRequired[str],
        "BotType": NotRequired[Literal["ChatBot"]],
        "Disabled": NotRequired[bool],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "BotEmail": NotRequired[str],
        "SecurityToken": NotRequired[str],
    },
)
BusinessCallingSettingsTypeDef = TypedDict(
    "BusinessCallingSettingsTypeDef",
    {
        "CdrBucket": NotRequired[str],
    },
)
CandidateAddressTypeDef = TypedDict(
    "CandidateAddressTypeDef",
    {
        "streetInfo": NotRequired[str],
        "streetNumber": NotRequired[str],
        "city": NotRequired[str],
        "state": NotRequired[str],
        "postalCode": NotRequired[str],
        "postalCodePlus4": NotRequired[str],
        "country": NotRequired[str],
    },
)
ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "LastMessageTimestamp": NotRequired[datetime],
    },
)
ConversationRetentionSettingsTypeDef = TypedDict(
    "ConversationRetentionSettingsTypeDef",
    {
        "RetentionDays": NotRequired[int],
    },
)
CreateAccountRequestRequestTypeDef = TypedDict(
    "CreateAccountRequestRequestTypeDef",
    {
        "Name": str,
    },
)
CreateAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreateBotRequestRequestTypeDef = TypedDict(
    "CreateBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "DisplayName": str,
        "Domain": NotRequired[str],
    },
)
CreateChannelBanRequestRequestTypeDef = TypedDict(
    "CreateChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
CreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "CreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": NotRequired[str],
    },
)
CreateChannelModeratorRequestRequestTypeDef = TypedDict(
    "CreateChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
CreateMeetingDialOutRequestRequestTypeDef = TypedDict(
    "CreateMeetingDialOutRequestRequestTypeDef",
    {
        "MeetingId": str,
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "JoinToken": str,
    },
)
MeetingNotificationConfigurationTypeDef = TypedDict(
    "MeetingNotificationConfigurationTypeDef",
    {
        "SnsTopicArn": NotRequired[str],
        "SqsQueueArn": NotRequired[str],
    },
)
CreatePhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "E164PhoneNumbers": Sequence[str],
    },
)
GeoMatchParamsTypeDef = TypedDict(
    "GeoMatchParamsTypeDef",
    {
        "Country": str,
        "AreaCode": str,
    },
)
CreateRoomMembershipRequestRequestTypeDef = TypedDict(
    "CreateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
        "Role": NotRequired[RoomMembershipRoleType],
    },
)
CreateRoomRequestRequestTypeDef = TypedDict(
    "CreateRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "ClientRequestToken": NotRequired[str],
    },
)
RoomTypeDef = TypedDict(
    "RoomTypeDef",
    {
        "RoomId": NotRequired[str],
        "Name": NotRequired[str],
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
CreateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "SipMediaApplicationId": str,
        "SipHeaders": NotRequired[Mapping[str, str]],
    },
)
SipMediaApplicationCallTypeDef = TypedDict(
    "SipMediaApplicationCallTypeDef",
    {
        "TransactionId": NotRequired[str],
    },
)
SipMediaApplicationEndpointTypeDef = TypedDict(
    "SipMediaApplicationEndpointTypeDef",
    {
        "LambdaArn": NotRequired[str],
    },
)
SipRuleTargetApplicationTypeDef = TypedDict(
    "SipRuleTargetApplicationTypeDef",
    {
        "SipMediaApplicationId": NotRequired[str],
        "Priority": NotRequired[int],
        "AwsRegion": NotRequired[str],
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "Username": NotRequired[str],
        "Email": NotRequired[str],
        "UserType": NotRequired[UserTypeType],
    },
)
VoiceConnectorItemTypeDef = TypedDict(
    "VoiceConnectorItemTypeDef",
    {
        "VoiceConnectorId": str,
        "Priority": int,
    },
)
CreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "CreateVoiceConnectorRequestRequestTypeDef",
    {
        "Name": str,
        "RequireEncryption": bool,
        "AwsRegion": NotRequired[VoiceConnectorAwsRegionType],
    },
)
VoiceConnectorTypeDef = TypedDict(
    "VoiceConnectorTypeDef",
    {
        "VoiceConnectorId": NotRequired[str],
        "AwsRegion": NotRequired[VoiceConnectorAwsRegionType],
        "Name": NotRequired[str],
        "OutboundHostName": NotRequired[str],
        "RequireEncryption": NotRequired[bool],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "VoiceConnectorArn": NotRequired[str],
    },
)
CredentialTypeDef = TypedDict(
    "CredentialTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
    },
)
DNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "DNISEmergencyCallingConfigurationTypeDef",
    {
        "EmergencyPhoneNumber": str,
        "CallingCountry": str,
        "TestPhoneNumber": NotRequired[str],
    },
)
DeleteAccountRequestRequestTypeDef = TypedDict(
    "DeleteAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
DeleteAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)
DeleteAppInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
DeleteAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)
DeleteAttendeeRequestRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)
DeleteChannelBanRequestRequestTypeDef = TypedDict(
    "DeleteChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "DeleteChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "DeleteChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": NotRequired[str],
    },
)
DeleteChannelModeratorRequestRequestTypeDef = TypedDict(
    "DeleteChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DeleteEventsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)
DeleteMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)
DeleteMeetingRequestRequestTypeDef = TypedDict(
    "DeleteMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
DeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "DeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
DeleteProxySessionRequestRequestTypeDef = TypedDict(
    "DeleteProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)
DeleteRoomMembershipRequestRequestTypeDef = TypedDict(
    "DeleteRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
    },
)
DeleteRoomRequestRequestTypeDef = TypedDict(
    "DeleteRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)
DeleteSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
DeleteSipRuleRequestRequestTypeDef = TypedDict(
    "DeleteSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)
DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
DeleteVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)
DeleteVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
DeleteVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
DeleteVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Usernames": Sequence[str],
    },
)
DeleteVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
DescribeAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)
DescribeAppInstanceRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
DescribeAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)
DescribeChannelBanRequestRequestTypeDef = TypedDict(
    "DescribeChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DescribeChannelModeratorRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
DisassociatePhoneNumberFromUserRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumberFromUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)
DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": Sequence[str],
    },
)
DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": Sequence[str],
    },
)
DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef = TypedDict(
    "DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "GroupNames": Sequence[str],
    },
)
EngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "EngineTranscribeMedicalSettingsTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "Specialty": TranscribeMedicalSpecialtyType,
        "Type": TranscribeMedicalTypeType,
        "VocabularyName": NotRequired[str],
        "Region": NotRequired[TranscribeMedicalRegionType],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
    },
)
EngineTranscribeSettingsTypeDef = TypedDict(
    "EngineTranscribeSettingsTypeDef",
    {
        "LanguageCode": NotRequired[TranscribeLanguageCodeType],
        "VocabularyFilterMethod": NotRequired[TranscribeVocabularyFilterMethodType],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyName": NotRequired[str],
        "Region": NotRequired[TranscribeRegionType],
        "EnablePartialResultsStabilization": NotRequired[bool],
        "PartialResultsStability": NotRequired[TranscribePartialResultsStabilityType],
        "ContentIdentificationType": NotRequired[Literal["PII"]],
        "ContentRedactionType": NotRequired[Literal["PII"]],
        "PiiEntityTypes": NotRequired[str],
        "LanguageModelName": NotRequired[str],
        "IdentifyLanguage": NotRequired[bool],
        "LanguageOptions": NotRequired[str],
        "PreferredLanguage": NotRequired[TranscribeLanguageCodeType],
        "VocabularyNames": NotRequired[str],
        "VocabularyFilterNames": NotRequired[str],
    },
)
EventsConfigurationTypeDef = TypedDict(
    "EventsConfigurationTypeDef",
    {
        "BotId": NotRequired[str],
        "OutboundEventsHTTPSEndpoint": NotRequired[str],
        "LambdaFunctionArn": NotRequired[str],
    },
)
GetAccountRequestRequestTypeDef = TypedDict(
    "GetAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
GetAccountSettingsRequestRequestTypeDef = TypedDict(
    "GetAccountSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
GetAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
GetAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
GetAttendeeRequestRequestTypeDef = TypedDict(
    "GetAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)
GetBotRequestRequestTypeDef = TypedDict(
    "GetBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)
GetChannelMessageRequestRequestTypeDef = TypedDict(
    "GetChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": NotRequired[str],
    },
)
GetEventsConfigurationRequestRequestTypeDef = TypedDict(
    "GetEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)
VoiceConnectorSettingsTypeDef = TypedDict(
    "VoiceConnectorSettingsTypeDef",
    {
        "CdrBucket": NotRequired[str],
    },
)
GetMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "GetMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)
GetMeetingRequestRequestTypeDef = TypedDict(
    "GetMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
MessagingSessionEndpointTypeDef = TypedDict(
    "MessagingSessionEndpointTypeDef",
    {
        "Url": NotRequired[str],
    },
)
GetPhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberOrderRequestRequestTypeDef",
    {
        "PhoneNumberOrderId": str,
    },
)
GetPhoneNumberRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
GetProxySessionRequestRequestTypeDef = TypedDict(
    "GetProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)
GetRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetRetentionSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
GetRoomRequestRequestTypeDef = TypedDict(
    "GetRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)
GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
SipMediaApplicationLoggingConfigurationTypeDef = TypedDict(
    "SipMediaApplicationLoggingConfigurationTypeDef",
    {
        "EnableSipMediaApplicationMessageLogs": NotRequired[bool],
    },
)
GetSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
GetSipRuleRequestRequestTypeDef = TypedDict(
    "GetSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)
GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)
GetUserSettingsRequestRequestTypeDef = TypedDict(
    "GetUserSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)
GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
GetVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)
GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "EnableSIPLogs": NotRequired[bool],
        "EnableMediaMetricLogs": NotRequired[bool],
    },
)
GetVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
GetVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
ProxyTypeDef = TypedDict(
    "ProxyTypeDef",
    {
        "DefaultSessionExpiryMinutes": NotRequired[int],
        "Disabled": NotRequired[bool],
        "FallBackPhoneNumber": NotRequired[str],
        "PhoneNumberCountries": NotRequired[List[str]],
    },
)
GetVoiceConnectorRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
GetVoiceConnectorTerminationHealthRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
TerminationHealthTypeDef = TypedDict(
    "TerminationHealthTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "Source": NotRequired[str],
    },
)
GetVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
TerminationOutputTypeDef = TypedDict(
    "TerminationOutputTypeDef",
    {
        "CpsLimit": NotRequired[int],
        "DefaultPhoneNumber": NotRequired[str],
        "CallingRegions": NotRequired[List[str]],
        "CidrAllowedList": NotRequired[List[str]],
        "Disabled": NotRequired[bool],
    },
)
InviteTypeDef = TypedDict(
    "InviteTypeDef",
    {
        "InviteId": NotRequired[str],
        "Status": NotRequired[InviteStatusType],
        "EmailAddress": NotRequired[str],
        "EmailStatus": NotRequired[EmailStatusType],
    },
)
InviteUsersRequestRequestTypeDef = TypedDict(
    "InviteUsersRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserEmailList": Sequence[str],
        "UserType": NotRequired[UserTypeType],
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
ListAccountsRequestRequestTypeDef = TypedDict(
    "ListAccountsRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "UserEmail": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "ListAppInstanceAdminsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "ListAppInstanceUsersRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAppInstancesRequestRequestTypeDef = TypedDict(
    "ListAppInstancesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAttendeeTagsRequestRequestTypeDef = TypedDict(
    "ListAttendeeTagsRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)
ListAttendeesRequestRequestTypeDef = TypedDict(
    "ListAttendeesRequestRequestTypeDef",
    {
        "MeetingId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListBotsRequestRequestTypeDef = TypedDict(
    "ListBotsRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelBansRequestRequestTypeDef = TypedDict(
    "ListChannelBansRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
ListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Type": NotRequired[ChannelMembershipTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "ListChannelModeratorsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Privacy": NotRequired[ChannelPrivacyType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
ListMediaCapturePipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMeetingTagsRequestRequestTypeDef = TypedDict(
    "ListMeetingTagsRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
ListMeetingsRequestRequestTypeDef = TypedDict(
    "ListMeetingsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPhoneNumberOrdersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumbersRequestRequestTypeDef",
    {
        "Status": NotRequired[PhoneNumberStatusType],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "FilterName": NotRequired[PhoneNumberAssociationNameType],
        "FilterValue": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListProxySessionsRequestRequestTypeDef = TypedDict(
    "ListProxySessionsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Status": NotRequired[ProxySessionStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRoomMembershipsRequestRequestTypeDef = TypedDict(
    "ListRoomMembershipsRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRoomsRequestRequestTypeDef = TypedDict(
    "ListRoomsRequestRequestTypeDef",
    {
        "AccountId": str,
        "MemberId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSipMediaApplicationsRequestRequestTypeDef = TypedDict(
    "ListSipMediaApplicationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSipRulesRequestRequestTypeDef = TypedDict(
    "ListSipRulesRequestRequestTypeDef",
    {
        "SipMediaApplicationId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSupportedPhoneNumberCountriesRequestRequestTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
    },
)
PhoneNumberCountryTypeDef = TypedDict(
    "PhoneNumberCountryTypeDef",
    {
        "CountryCode": NotRequired[str],
        "SupportedPhoneNumberTypes": NotRequired[List[PhoneNumberTypeType]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserEmail": NotRequired[str],
        "UserType": NotRequired[UserTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListVoiceConnectorGroupsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
ListVoiceConnectorsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
LogoutUserRequestRequestTypeDef = TypedDict(
    "LogoutUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)
MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": NotRequired[str],
        "AudioFallbackUrl": NotRequired[str],
        "ScreenDataUrl": NotRequired[str],
        "ScreenSharingUrl": NotRequired[str],
        "ScreenViewingUrl": NotRequired[str],
        "SignalingUrl": NotRequired[str],
        "TurnControlUrl": NotRequired[str],
        "EventIngestionUrl": NotRequired[str],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "MemberId": NotRequired[str],
        "MemberType": NotRequired[MemberTypeType],
        "Email": NotRequired[str],
        "FullName": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)
OrderedPhoneNumberTypeDef = TypedDict(
    "OrderedPhoneNumberTypeDef",
    {
        "E164PhoneNumber": NotRequired[str],
        "Status": NotRequired[OrderedPhoneNumberStatusType],
    },
)
OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {
        "Host": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[OriginationRouteProtocolType],
        "Priority": NotRequired[int],
        "Weight": NotRequired[int],
    },
)
ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "PhoneNumber": NotRequired[str],
        "ProxyPhoneNumber": NotRequired[str],
    },
)
PhoneNumberAssociationTypeDef = TypedDict(
    "PhoneNumberAssociationTypeDef",
    {
        "Value": NotRequired[str],
        "Name": NotRequired[PhoneNumberAssociationNameType],
        "AssociatedTimestamp": NotRequired[datetime],
    },
)
PhoneNumberCapabilitiesTypeDef = TypedDict(
    "PhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": NotRequired[bool],
        "OutboundCall": NotRequired[bool],
        "InboundSMS": NotRequired[bool],
        "OutboundSMS": NotRequired[bool],
        "InboundMMS": NotRequired[bool],
        "OutboundMMS": NotRequired[bool],
    },
)
PutEventsConfigurationRequestRequestTypeDef = TypedDict(
    "PutEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
        "OutboundEventsHTTPSEndpoint": NotRequired[str],
        "LambdaFunctionArn": NotRequired[str],
    },
)
PutVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "DefaultSessionExpiryMinutes": int,
        "PhoneNumberPoolCountries": Sequence[str],
        "FallBackPhoneNumber": NotRequired[str],
        "Disabled": NotRequired[bool],
    },
)
TerminationTypeDef = TypedDict(
    "TerminationTypeDef",
    {
        "CpsLimit": NotRequired[int],
        "DefaultPhoneNumber": NotRequired[str],
        "CallingRegions": NotRequired[Sequence[str]],
        "CidrAllowedList": NotRequired[Sequence[str]],
        "Disabled": NotRequired[bool],
    },
)
RedactChannelMessageRequestRequestTypeDef = TypedDict(
    "RedactChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": NotRequired[str],
    },
)
RedactConversationMessageRequestRequestTypeDef = TypedDict(
    "RedactConversationMessageRequestRequestTypeDef",
    {
        "AccountId": str,
        "ConversationId": str,
        "MessageId": str,
    },
)
RedactRoomMessageRequestRequestTypeDef = TypedDict(
    "RedactRoomMessageRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MessageId": str,
    },
)
RegenerateSecurityTokenRequestRequestTypeDef = TypedDict(
    "RegenerateSecurityTokenRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)
ResetPersonalPINRequestRequestTypeDef = TypedDict(
    "ResetPersonalPINRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)
RestorePhoneNumberRequestRequestTypeDef = TypedDict(
    "RestorePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
RoomRetentionSettingsTypeDef = TypedDict(
    "RoomRetentionSettingsTypeDef",
    {
        "RetentionDays": NotRequired[int],
    },
)
SearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "AreaCode": NotRequired[str],
        "City": NotRequired[str],
        "Country": NotRequired[str],
        "State": NotRequired[str],
        "TollFreePrefix": NotRequired[str],
        "PhoneNumberType": NotRequired[PhoneNumberTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SelectedVideoStreamsOutputTypeDef = TypedDict(
    "SelectedVideoStreamsOutputTypeDef",
    {
        "AttendeeIds": NotRequired[List[str]],
        "ExternalUserIds": NotRequired[List[str]],
    },
)
SelectedVideoStreamsTypeDef = TypedDict(
    "SelectedVideoStreamsTypeDef",
    {
        "AttendeeIds": NotRequired[Sequence[str]],
        "ExternalUserIds": NotRequired[Sequence[str]],
    },
)
SendChannelMessageRequestRequestTypeDef = TypedDict(
    "SendChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Content": str,
        "Type": ChannelMessageTypeType,
        "Persistence": ChannelMessagePersistenceTypeType,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
StopMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StopMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
StreamingNotificationTargetTypeDef = TypedDict(
    "StreamingNotificationTargetTypeDef",
    {
        "NotificationTarget": NotificationTargetType,
    },
)
TelephonySettingsTypeDef = TypedDict(
    "TelephonySettingsTypeDef",
    {
        "InboundCalling": bool,
        "OutboundCalling": bool,
        "SMS": bool,
    },
)
UntagAttendeeRequestRequestTypeDef = TypedDict(
    "UntagAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "TagKeys": Sequence[str],
    },
)
UntagMeetingRequestRequestTypeDef = TypedDict(
    "UntagMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TagKeys": Sequence[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAccountRequestRequestTypeDef = TypedDict(
    "UpdateAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": NotRequired[str],
        "DefaultLicense": NotRequired[LicenseType],
    },
)
UpdateAppInstanceRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": NotRequired[str],
    },
)
UpdateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": NotRequired[str],
    },
)
UpdateBotRequestRequestTypeDef = TypedDict(
    "UpdateBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
        "Disabled": NotRequired[bool],
    },
)
UpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "UpdateChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
UpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": NotRequired[str],
    },
)
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Mode": ChannelModeType,
        "Metadata": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
UpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "CallingName": NotRequired[str],
    },
)
UpdatePhoneNumberSettingsRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    {
        "CallingName": str,
    },
)
UpdateProxySessionRequestRequestTypeDef = TypedDict(
    "UpdateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Capabilities": Sequence[CapabilityType],
        "ExpiryMinutes": NotRequired[int],
    },
)
UpdateRoomMembershipRequestRequestTypeDef = TypedDict(
    "UpdateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
        "Role": NotRequired[RoomMembershipRoleType],
    },
)
UpdateRoomRequestRequestTypeDef = TypedDict(
    "UpdateRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "Name": NotRequired[str],
    },
)
UpdateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "TransactionId": str,
        "Arguments": Mapping[str, str],
    },
)
UpdateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Name": str,
        "RequireEncryption": bool,
    },
)
ValidateE911AddressRequestRequestTypeDef = TypedDict(
    "ValidateE911AddressRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "StreetNumber": str,
        "StreetInfo": str,
        "City": str,
        "State": str,
        "Country": str,
        "PostalCode": str,
    },
)
UpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccountSettings": AccountSettingsTypeDef,
    },
)
AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": NotRequired[AccountTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "DefaultLicense": NotRequired[LicenseType],
        "SupportedLicenses": NotRequired[List[LicenseType]],
        "AccountStatus": NotRequired[AccountStatusType],
        "SigninDelegateGroups": NotRequired[List[SigninDelegateGroupTypeDef]],
    },
)
AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef = TypedDict(
    "AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "SigninDelegateGroups": Sequence[SigninDelegateGroupTypeDef],
    },
)
UpdateUserRequestItemTypeDef = TypedDict(
    "UpdateUserRequestItemTypeDef",
    {
        "UserId": str,
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "AlexaForBusinessMetadata": NotRequired[AlexaForBusinessMetadataTypeDef],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "AlexaForBusinessMetadata": NotRequired[AlexaForBusinessMetadataTypeDef],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": str,
        "AccountId": NotRequired[str],
        "PrimaryEmail": NotRequired[str],
        "PrimaryProvisionedNumber": NotRequired[str],
        "DisplayName": NotRequired[str],
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "UserRegistrationStatus": NotRequired[RegistrationStatusType],
        "UserInvitationStatus": NotRequired[InviteStatusType],
        "RegisteredOn": NotRequired[datetime],
        "InvitedOn": NotRequired[datetime],
        "AlexaForBusinessMetadata": NotRequired[AlexaForBusinessMetadataTypeDef],
        "PersonalPIN": NotRequired[str],
    },
)
AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef",
    {
        "Admin": NotRequired[IdentityTypeDef],
    },
)
AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {
        "Admin": NotRequired[IdentityTypeDef],
        "AppInstanceArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)
BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": NotRequired[IdentityTypeDef],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Members": NotRequired[List[IdentityTypeDef]],
        "ChannelArn": NotRequired[str],
    },
)
ChannelBanSummaryTypeDef = TypedDict(
    "ChannelBanSummaryTypeDef",
    {
        "Member": NotRequired[IdentityTypeDef],
    },
)
ChannelBanTypeDef = TypedDict(
    "ChannelBanTypeDef",
    {
        "Member": NotRequired[IdentityTypeDef],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "CreatedBy": NotRequired[IdentityTypeDef],
    },
)
ChannelMembershipSummaryTypeDef = TypedDict(
    "ChannelMembershipSummaryTypeDef",
    {
        "Member": NotRequired[IdentityTypeDef],
    },
)
ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": NotRequired[IdentityTypeDef],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Member": NotRequired[IdentityTypeDef],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "Sender": NotRequired[IdentityTypeDef],
        "Redacted": NotRequired[bool],
    },
)
ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": NotRequired[str],
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Sender": NotRequired[IdentityTypeDef],
        "Redacted": NotRequired[bool],
        "Persistence": NotRequired[ChannelMessagePersistenceTypeType],
    },
)
ChannelModeratorSummaryTypeDef = TypedDict(
    "ChannelModeratorSummaryTypeDef",
    {
        "Moderator": NotRequired[IdentityTypeDef],
    },
)
ChannelModeratorTypeDef = TypedDict(
    "ChannelModeratorTypeDef",
    {
        "Moderator": NotRequired[IdentityTypeDef],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "CreatedBy": NotRequired[IdentityTypeDef],
    },
)
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "CreatedBy": NotRequired[IdentityTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "LastMessageTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {
        "ChannelRetentionSettings": NotRequired[ChannelRetentionSettingsTypeDef],
    },
)
PutAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceStreamingConfigurations": Sequence[AppInstanceStreamingConfigurationTypeDef],
    },
)
ArtifactsConfigurationTypeDef = TypedDict(
    "ArtifactsConfigurationTypeDef",
    {
        "Audio": AudioArtifactsConfigurationTypeDef,
        "Video": VideoArtifactsConfigurationTypeDef,
        "Content": ContentArtifactsConfigurationTypeDef,
    },
)
AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "BatchDeletePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "BatchUpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppInstanceAdminResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": IdentityTypeDef,
        "AppInstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppInstanceResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppInstanceUserResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelBanResponseTypeDef = TypedDict(
    "CreateChannelBanResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelMembershipResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelModeratorResponseTypeDef = TypedDict(
    "CreateChannelModeratorResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelModerator": IdentityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMeetingDialOutResponseTypeDef = TypedDict(
    "CreateMeetingDialOutResponseTypeDef",
    {
        "TransactionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAppInstanceResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseTypeDef",
    {
        "AppInstance": AppInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUser": AppInstanceUserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {
        "AccountSettings": AccountSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppInstanceStreamingConfigurationsResponseTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    {
        "AppInstanceStreamingConfigurations": List[AppInstanceStreamingConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "GetPhoneNumberSettingsResponseTypeDef",
    {
        "CallingName": str,
        "CallingNameUpdatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppInstanceUsersResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List[AppInstanceUserSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAppInstancesResponseTypeDef = TypedDict(
    "ListAppInstancesResponseTypeDef",
    {
        "AppInstances": List[AppInstanceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {
        "Usernames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAppInstanceStreamingConfigurationsResponseTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    {
        "AppInstanceStreamingConfigurations": List[AppInstanceStreamingConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RedactChannelMessageResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseTypeDef",
    {
        "E164PhoneNumbers": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SendChannelMessageResponseTypeDef = TypedDict(
    "SendChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAppInstanceResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAppInstanceUserResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelMessageResponseTypeDef = TypedDict(
    "UpdateChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelReadMarkerResponseTypeDef = TypedDict(
    "UpdateChannelReadMarkerResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAttendeeResponseTypeDef = TypedDict(
    "GetAttendeeResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttendeesResponseTypeDef = TypedDict(
    "ListAttendeesResponseTypeDef",
    {
        "Attendees": List[AttendeeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchCreateAttendeeResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List[AttendeeTypeDef],
        "Errors": List[CreateAttendeeErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreateRoomMembershipRequestRequestTypeDef = TypedDict(
    "BatchCreateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MembershipItemList": Sequence[MembershipItemTypeDef],
    },
)
BatchCreateRoomMembershipResponseTypeDef = TypedDict(
    "BatchCreateRoomMembershipResponseTypeDef",
    {
        "Errors": List[MemberErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchSuspendUserResponseTypeDef = TypedDict(
    "BatchSuspendUserResponseTypeDef",
    {
        "UserErrors": List[UserErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUnsuspendUserResponseTypeDef = TypedDict(
    "BatchUnsuspendUserResponseTypeDef",
    {
        "UserErrors": List[UserErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateUserResponseTypeDef = TypedDict(
    "BatchUpdateUserResponseTypeDef",
    {
        "UserErrors": List[UserErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    {
        "UpdatePhoneNumberRequestItems": Sequence[UpdatePhoneNumberRequestItemTypeDef],
    },
)
CreateBotResponseTypeDef = TypedDict(
    "CreateBotResponseTypeDef",
    {
        "Bot": BotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBotResponseTypeDef = TypedDict(
    "GetBotResponseTypeDef",
    {
        "Bot": BotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "Bots": List[BotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RegenerateSecurityTokenResponseTypeDef = TypedDict(
    "RegenerateSecurityTokenResponseTypeDef",
    {
        "Bot": BotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBotResponseTypeDef = TypedDict(
    "UpdateBotResponseTypeDef",
    {
        "Bot": BotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidateE911AddressResponseTypeDef = TypedDict(
    "ValidateE911AddressResponseTypeDef",
    {
        "ValidationResult": int,
        "AddressExternalId": str,
        "Address": AddressTypeDef,
        "CandidateAddressList": List[CandidateAddressTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": NotRequired[ChannelSummaryTypeDef],
        "AppInstanceUserMembershipSummary": NotRequired[AppInstanceUserMembershipSummaryTypeDef],
    },
)
ChannelModeratedByAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": NotRequired[ChannelSummaryTypeDef],
    },
)
ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List[ChannelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateAppInstanceRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUserId": str,
        "Name": str,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateAttendeeRequestItemTypeDef = TypedDict(
    "CreateAttendeeRequestItemTypeDef",
    {
        "ExternalUserId": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateAttendeeRequestRequestTypeDef = TypedDict(
    "CreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "ClientRequestToken": str,
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ChimeBearer": NotRequired[str],
    },
)
ListAttendeeTagsResponseTypeDef = TypedDict(
    "ListAttendeeTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMeetingTagsResponseTypeDef = TypedDict(
    "ListMeetingTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagAttendeeRequestRequestTypeDef = TypedDict(
    "TagAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagMeetingRequestRequestTypeDef = TypedDict(
    "TagMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateMeetingRequestRequestTypeDef = TypedDict(
    "CreateMeetingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ExternalMeetingId": NotRequired[str],
        "MeetingHostId": NotRequired[str],
        "MediaRegion": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "NotificationsConfiguration": NotRequired[MeetingNotificationConfigurationTypeDef],
    },
)
CreateProxySessionRequestRequestTypeDef = TypedDict(
    "CreateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ParticipantPhoneNumbers": Sequence[str],
        "Capabilities": Sequence[CapabilityType],
        "Name": NotRequired[str],
        "ExpiryMinutes": NotRequired[int],
        "NumberSelectionBehavior": NotRequired[NumberSelectionBehaviorType],
        "GeoMatchLevel": NotRequired[GeoMatchLevelType],
        "GeoMatchParams": NotRequired[GeoMatchParamsTypeDef],
    },
)
CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "Room": RoomTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "Room": RoomTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRoomsResponseTypeDef = TypedDict(
    "ListRoomsResponseTypeDef",
    {
        "Rooms": List[RoomTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateRoomResponseTypeDef = TypedDict(
    "UpdateRoomResponseTypeDef",
    {
        "Room": RoomTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": SipMediaApplicationCallTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": SipMediaApplicationCallTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationRequestRequestTypeDef",
    {
        "AwsRegion": str,
        "Name": str,
        "Endpoints": Sequence[SipMediaApplicationEndpointTypeDef],
    },
)
SipMediaApplicationTypeDef = TypedDict(
    "SipMediaApplicationTypeDef",
    {
        "SipMediaApplicationId": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "Name": NotRequired[str],
        "Endpoints": NotRequired[List[SipMediaApplicationEndpointTypeDef]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
UpdateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "UpdateSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "Name": NotRequired[str],
        "Endpoints": NotRequired[Sequence[SipMediaApplicationEndpointTypeDef]],
    },
)
CreateSipRuleRequestRequestTypeDef = TypedDict(
    "CreateSipRuleRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "TargetApplications": Sequence[SipRuleTargetApplicationTypeDef],
        "Disabled": NotRequired[bool],
    },
)
SipRuleTypeDef = TypedDict(
    "SipRuleTypeDef",
    {
        "SipRuleId": NotRequired[str],
        "Name": NotRequired[str],
        "Disabled": NotRequired[bool],
        "TriggerType": NotRequired[SipRuleTriggerTypeType],
        "TriggerValue": NotRequired[str],
        "TargetApplications": NotRequired[List[SipRuleTargetApplicationTypeDef]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
UpdateSipRuleRequestRequestTypeDef = TypedDict(
    "UpdateSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
        "Disabled": NotRequired[bool],
        "TargetApplications": NotRequired[Sequence[SipRuleTargetApplicationTypeDef]],
    },
)
CreateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "CreateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "Name": str,
        "VoiceConnectorItems": NotRequired[Sequence[VoiceConnectorItemTypeDef]],
    },
)
UpdateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": Sequence[VoiceConnectorItemTypeDef],
    },
)
VoiceConnectorGroupTypeDef = TypedDict(
    "VoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": NotRequired[str],
        "Name": NotRequired[str],
        "VoiceConnectorItems": NotRequired[List[VoiceConnectorItemTypeDef]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "VoiceConnectorGroupArn": NotRequired[str],
    },
)
CreateVoiceConnectorResponseTypeDef = TypedDict(
    "CreateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": VoiceConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceConnectorResponseTypeDef = TypedDict(
    "GetVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": VoiceConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVoiceConnectorsResponseTypeDef = TypedDict(
    "ListVoiceConnectorsResponseTypeDef",
    {
        "VoiceConnectors": List[VoiceConnectorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateVoiceConnectorResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": VoiceConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Credentials": NotRequired[Sequence[CredentialTypeDef]],
    },
)
EmergencyCallingConfigurationOutputTypeDef = TypedDict(
    "EmergencyCallingConfigurationOutputTypeDef",
    {
        "DNIS": NotRequired[List[DNISEmergencyCallingConfigurationTypeDef]],
    },
)
EmergencyCallingConfigurationTypeDef = TypedDict(
    "EmergencyCallingConfigurationTypeDef",
    {
        "DNIS": NotRequired[Sequence[DNISEmergencyCallingConfigurationTypeDef]],
    },
)
TranscriptionConfigurationTypeDef = TypedDict(
    "TranscriptionConfigurationTypeDef",
    {
        "EngineTranscribeSettings": NotRequired[EngineTranscribeSettingsTypeDef],
        "EngineTranscribeMedicalSettings": NotRequired[EngineTranscribeMedicalSettingsTypeDef],
    },
)
GetEventsConfigurationResponseTypeDef = TypedDict(
    "GetEventsConfigurationResponseTypeDef",
    {
        "EventsConfiguration": EventsConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutEventsConfigurationResponseTypeDef = TypedDict(
    "PutEventsConfigurationResponseTypeDef",
    {
        "EventsConfiguration": EventsConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGlobalSettingsResponseTypeDef = TypedDict(
    "GetGlobalSettingsResponseTypeDef",
    {
        "BusinessCalling": BusinessCallingSettingsTypeDef,
        "VoiceConnector": VoiceConnectorSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGlobalSettingsRequestRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsRequestRequestTypeDef",
    {
        "BusinessCalling": NotRequired[BusinessCallingSettingsTypeDef],
        "VoiceConnector": NotRequired[VoiceConnectorSettingsTypeDef],
    },
)
GetMessagingSessionEndpointResponseTypeDef = TypedDict(
    "GetMessagingSessionEndpointResponseTypeDef",
    {
        "Endpoint": MessagingSessionEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": SipMediaApplicationLoggingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "SipMediaApplicationLoggingConfiguration": NotRequired[
            SipMediaApplicationLoggingConfigurationTypeDef
        ],
    },
)
PutSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": SipMediaApplicationLoggingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "LoggingConfiguration": LoggingConfigurationTypeDef,
    },
)
PutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceConnectorProxyResponseTypeDef = TypedDict(
    "GetVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": ProxyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorProxyResponseTypeDef = TypedDict(
    "PutVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": ProxyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    {
        "TerminationHealth": TerminationHealthTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": TerminationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "PutVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": TerminationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InviteUsersResponseTypeDef = TypedDict(
    "InviteUsersResponseTypeDef",
    {
        "Invites": List[InviteTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountsRequestListAccountsPaginateTypeDef = TypedDict(
    "ListAccountsRequestListAccountsPaginateTypeDef",
    {
        "Name": NotRequired[str],
        "UserEmail": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "AccountId": str,
        "UserEmail": NotRequired[str],
        "UserType": NotRequired[UserTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListChannelMessagesRequestRequestTypeDef = TypedDict(
    "ListChannelMessagesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "SortOrder": NotRequired[SortOrderType],
        "NotBefore": NotRequired[TimestampTypeDef],
        "NotAfter": NotRequired[TimestampTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)
ListSupportedPhoneNumberCountriesResponseTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    {
        "PhoneNumberCountries": List[PhoneNumberCountryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": NotRequired[str],
        "ExternalMeetingId": NotRequired[str],
        "MediaPlacement": NotRequired[MediaPlacementTypeDef],
        "MediaRegion": NotRequired[str],
    },
)
RoomMembershipTypeDef = TypedDict(
    "RoomMembershipTypeDef",
    {
        "RoomId": NotRequired[str],
        "Member": NotRequired[MemberTypeDef],
        "Role": NotRequired[RoomMembershipRoleType],
        "InvitedBy": NotRequired[str],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
PhoneNumberOrderTypeDef = TypedDict(
    "PhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": NotRequired[str],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "Status": NotRequired[PhoneNumberOrderStatusType],
        "OrderedPhoneNumbers": NotRequired[List[OrderedPhoneNumberTypeDef]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
OriginationOutputTypeDef = TypedDict(
    "OriginationOutputTypeDef",
    {
        "Routes": NotRequired[List[OriginationRouteTypeDef]],
        "Disabled": NotRequired[bool],
    },
)
OriginationTypeDef = TypedDict(
    "OriginationTypeDef",
    {
        "Routes": NotRequired[Sequence[OriginationRouteTypeDef]],
        "Disabled": NotRequired[bool],
    },
)
ProxySessionTypeDef = TypedDict(
    "ProxySessionTypeDef",
    {
        "VoiceConnectorId": NotRequired[str],
        "ProxySessionId": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ProxySessionStatusType],
        "ExpiryMinutes": NotRequired[int],
        "Capabilities": NotRequired[List[CapabilityType]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "EndedTimestamp": NotRequired[datetime],
        "Participants": NotRequired[List[ParticipantTypeDef]],
        "NumberSelectionBehavior": NotRequired[NumberSelectionBehaviorType],
        "GeoMatchLevel": NotRequired[GeoMatchLevelType],
        "GeoMatchParams": NotRequired[GeoMatchParamsTypeDef],
    },
)
PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": NotRequired[str],
        "E164PhoneNumber": NotRequired[str],
        "Country": NotRequired[str],
        "Type": NotRequired[PhoneNumberTypeType],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "Status": NotRequired[PhoneNumberStatusType],
        "Capabilities": NotRequired[PhoneNumberCapabilitiesTypeDef],
        "Associations": NotRequired[List[PhoneNumberAssociationTypeDef]],
        "CallingName": NotRequired[str],
        "CallingNameStatus": NotRequired[CallingNameStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "DeletionTimestamp": NotRequired[datetime],
    },
)
PutVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Termination": TerminationTypeDef,
    },
)
RetentionSettingsTypeDef = TypedDict(
    "RetentionSettingsTypeDef",
    {
        "RoomRetentionSettings": NotRequired[RoomRetentionSettingsTypeDef],
        "ConversationRetentionSettings": NotRequired[ConversationRetentionSettingsTypeDef],
    },
)
SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "SelectedVideoStreams": NotRequired[SelectedVideoStreamsOutputTypeDef],
    },
)
SelectedVideoStreamsUnionTypeDef = Union[
    SelectedVideoStreamsTypeDef, SelectedVideoStreamsOutputTypeDef
]
StreamingConfigurationOutputTypeDef = TypedDict(
    "StreamingConfigurationOutputTypeDef",
    {
        "DataRetentionInHours": int,
        "Disabled": NotRequired[bool],
        "StreamingNotificationTargets": NotRequired[List[StreamingNotificationTargetTypeDef]],
    },
)
StreamingConfigurationTypeDef = TypedDict(
    "StreamingConfigurationTypeDef",
    {
        "DataRetentionInHours": int,
        "Disabled": NotRequired[bool],
        "StreamingNotificationTargets": NotRequired[Sequence[StreamingNotificationTargetTypeDef]],
    },
)
UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "Telephony": TelephonySettingsTypeDef,
    },
)
CreateAccountResponseTypeDef = TypedDict(
    "CreateAccountResponseTypeDef",
    {
        "Account": AccountTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "Account": AccountTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {
        "Accounts": List[AccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateAccountResponseTypeDef = TypedDict(
    "UpdateAccountResponseTypeDef",
    {
        "Account": AccountTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateUserRequestRequestTypeDef = TypedDict(
    "BatchUpdateUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UpdateUserRequestItems": Sequence[UpdateUserRequestItemTypeDef],
    },
)
CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List[UserTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ResetPersonalPINResponseTypeDef = TypedDict(
    "ResetPersonalPINResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppInstanceAdminsResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List[AppInstanceAdminSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeAppInstanceAdminResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": AppInstanceAdminTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreateChannelMembershipResponseTypeDef = TypedDict(
    "BatchCreateChannelMembershipResponseTypeDef",
    {
        "BatchChannelMemberships": BatchChannelMembershipsTypeDef,
        "Errors": List[BatchCreateChannelMembershipErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelBansResponseTypeDef = TypedDict(
    "ListChannelBansResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelBans": List[ChannelBanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeChannelBanResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseTypeDef",
    {
        "ChannelBan": ChannelBanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelMembershipsResponseTypeDef = TypedDict(
    "ListChannelMembershipsResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMemberships": List[ChannelMembershipSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeChannelMembershipResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseTypeDef",
    {
        "ChannelMembership": ChannelMembershipTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelMessagesResponseTypeDef = TypedDict(
    "ListChannelMessagesResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMessages": List[ChannelMessageSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetChannelMessageResponseTypeDef = TypedDict(
    "GetChannelMessageResponseTypeDef",
    {
        "ChannelMessage": ChannelMessageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelModeratorsResponseTypeDef = TypedDict(
    "ListChannelModeratorsResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelModerators": List[ChannelModeratorSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeChannelModeratorResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseTypeDef",
    {
        "ChannelModerator": ChannelModeratorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Channel": ChannelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsTypeDef,
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsTypeDef,
    },
)
PutAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsTypeDef,
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelMembershipForAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    {
        "ChannelMembership": ChannelMembershipForAppInstanceUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelMembershipsForAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    {
        "ChannelMemberships": List[ChannelMembershipForAppInstanceUserSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeChannelModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channel": ChannelModeratedByAppInstanceUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelsModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channels": List[ChannelModeratedByAppInstanceUserSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchCreateAttendeeRequestRequestTypeDef = TypedDict(
    "BatchCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Attendees": Sequence[CreateAttendeeRequestItemTypeDef],
    },
)
CreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ExternalMeetingId": NotRequired[str],
        "MeetingHostId": NotRequired[str],
        "MediaRegion": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "NotificationsConfiguration": NotRequired[MeetingNotificationConfigurationTypeDef],
        "Attendees": NotRequired[Sequence[CreateAttendeeRequestItemTypeDef]],
    },
)
CreateSipMediaApplicationResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": SipMediaApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSipMediaApplicationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": SipMediaApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSipMediaApplicationsResponseTypeDef = TypedDict(
    "ListSipMediaApplicationsResponseTypeDef",
    {
        "SipMediaApplications": List[SipMediaApplicationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateSipMediaApplicationResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": SipMediaApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSipRuleResponseTypeDef = TypedDict(
    "CreateSipRuleResponseTypeDef",
    {
        "SipRule": SipRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSipRuleResponseTypeDef = TypedDict(
    "GetSipRuleResponseTypeDef",
    {
        "SipRule": SipRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSipRulesResponseTypeDef = TypedDict(
    "ListSipRulesResponseTypeDef",
    {
        "SipRules": List[SipRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateSipRuleResponseTypeDef = TypedDict(
    "UpdateSipRuleResponseTypeDef",
    {
        "SipRule": SipRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "CreateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": VoiceConnectorGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "GetVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": VoiceConnectorGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "ListVoiceConnectorGroupsResponseTypeDef",
    {
        "VoiceConnectorGroups": List[VoiceConnectorGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": VoiceConnectorGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": EmergencyCallingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": EmergencyCallingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "EmergencyCallingConfiguration": EmergencyCallingConfigurationTypeDef,
    },
)
StartMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StartMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TranscriptionConfiguration": TranscriptionConfigurationTypeDef,
    },
)
CreateMeetingResponseTypeDef = TypedDict(
    "CreateMeetingResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMeetingWithAttendeesResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "Attendees": List[AttendeeTypeDef],
        "Errors": List[CreateAttendeeErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMeetingResponseTypeDef = TypedDict(
    "GetMeetingResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMeetingsResponseTypeDef = TypedDict(
    "ListMeetingsResponseTypeDef",
    {
        "Meetings": List[MeetingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateRoomMembershipResponseTypeDef = TypedDict(
    "CreateRoomMembershipResponseTypeDef",
    {
        "RoomMembership": RoomMembershipTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRoomMembershipsResponseTypeDef = TypedDict(
    "ListRoomMembershipsResponseTypeDef",
    {
        "RoomMemberships": List[RoomMembershipTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateRoomMembershipResponseTypeDef = TypedDict(
    "UpdateRoomMembershipResponseTypeDef",
    {
        "RoomMembership": RoomMembershipTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "CreatePhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": PhoneNumberOrderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPhoneNumberOrderResponseTypeDef = TypedDict(
    "GetPhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": PhoneNumberOrderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "ListPhoneNumberOrdersResponseTypeDef",
    {
        "PhoneNumberOrders": List[PhoneNumberOrderTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "GetVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": OriginationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "PutVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": OriginationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Origination": OriginationTypeDef,
    },
)
CreateProxySessionResponseTypeDef = TypedDict(
    "CreateProxySessionResponseTypeDef",
    {
        "ProxySession": ProxySessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProxySessionResponseTypeDef = TypedDict(
    "GetProxySessionResponseTypeDef",
    {
        "ProxySession": ProxySessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProxySessionsResponseTypeDef = TypedDict(
    "ListProxySessionsResponseTypeDef",
    {
        "ProxySessions": List[ProxySessionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateProxySessionResponseTypeDef = TypedDict(
    "UpdateProxySessionResponseTypeDef",
    {
        "ProxySession": ProxySessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPhoneNumberResponseTypeDef = TypedDict(
    "GetPhoneNumberResponseTypeDef",
    {
        "PhoneNumber": PhoneNumberTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumbers": List[PhoneNumberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RestorePhoneNumberResponseTypeDef = TypedDict(
    "RestorePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": PhoneNumberTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePhoneNumberResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": PhoneNumberTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRetentionSettingsResponseTypeDef = TypedDict(
    "GetRetentionSettingsResponseTypeDef",
    {
        "RetentionSettings": RetentionSettingsTypeDef,
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutRetentionSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "RetentionSettings": RetentionSettingsTypeDef,
    },
)
PutRetentionSettingsResponseTypeDef = TypedDict(
    "PutRetentionSettingsResponseTypeDef",
    {
        "RetentionSettings": RetentionSettingsTypeDef,
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChimeSdkMeetingConfigurationOutputTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationOutputTypeDef",
    {
        "SourceConfiguration": NotRequired[SourceConfigurationOutputTypeDef],
        "ArtifactsConfiguration": NotRequired[ArtifactsConfigurationTypeDef],
    },
)
SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "SelectedVideoStreams": NotRequired[SelectedVideoStreamsUnionTypeDef],
    },
)
GetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": StreamingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": StreamingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "StreamingConfiguration": StreamingConfigurationTypeDef,
    },
)
GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef",
    {
        "UserSettings": UserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "UpdateUserSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "UserSettings": UserSettingsTypeDef,
    },
)
MediaCapturePipelineTypeDef = TypedDict(
    "MediaCapturePipelineTypeDef",
    {
        "MediaPipelineId": NotRequired[str],
        "SourceType": NotRequired[Literal["ChimeSdkMeeting"]],
        "SourceArn": NotRequired[str],
        "Status": NotRequired[MediaPipelineStatusType],
        "SinkType": NotRequired[Literal["S3Bucket"]],
        "SinkArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "ChimeSdkMeetingConfiguration": NotRequired[ChimeSdkMeetingConfigurationOutputTypeDef],
    },
)
SourceConfigurationUnionTypeDef = Union[
    SourceConfigurationTypeDef, SourceConfigurationOutputTypeDef
]
CreateMediaCapturePipelineResponseTypeDef = TypedDict(
    "CreateMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMediaCapturePipelineResponseTypeDef = TypedDict(
    "GetMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMediaCapturePipelinesResponseTypeDef = TypedDict(
    "ListMediaCapturePipelinesResponseTypeDef",
    {
        "MediaCapturePipelines": List[MediaCapturePipelineTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ChimeSdkMeetingConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationTypeDef",
    {
        "SourceConfiguration": NotRequired[SourceConfigurationUnionTypeDef],
        "ArtifactsConfiguration": NotRequired[ArtifactsConfigurationTypeDef],
    },
)
CreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
        "ClientRequestToken": NotRequired[str],
        "ChimeSdkMeetingConfiguration": NotRequired[ChimeSdkMeetingConfigurationTypeDef],
    },
)
