"""
Type annotations for chime-sdk-voice service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_voice.type_defs import AddressTypeDef

    data: AddressTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AlexaSkillStatusType,
    CallingNameStatusType,
    CallLegTypeType,
    CapabilityType,
    ErrorCodeType,
    GeoMatchLevelType,
    NotificationTargetType,
    NumberSelectionBehaviorType,
    OrderedPhoneNumberStatusType,
    OriginationRouteProtocolType,
    PhoneNumberAssociationNameType,
    PhoneNumberOrderStatusType,
    PhoneNumberOrderTypeType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    SipRuleTriggerTypeType,
    VoiceConnectorAwsRegionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AddressTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    "PhoneNumberErrorTypeDef",
    "ResponseMetadataTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "CallDetailsTypeDef",
    "CandidateAddressTypeDef",
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    "GeoMatchParamsTypeDef",
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "TagTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "CreateVoiceProfileRequestRequestTypeDef",
    "VoiceProfileTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DeletePhoneNumberRequestRequestTypeDef",
    "DeleteProxySessionRequestRequestTypeDef",
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
    "DeleteVoiceProfileDomainRequestRequestTypeDef",
    "DeleteVoiceProfileRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "GetPhoneNumberOrderRequestRequestTypeDef",
    "GetPhoneNumberRequestRequestTypeDef",
    "GetProxySessionRequestRequestTypeDef",
    "GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    "SipMediaApplicationAlexaSkillConfigurationOutputTypeDef",
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "GetSipMediaApplicationRequestRequestTypeDef",
    "GetSipRuleRequestRequestTypeDef",
    "GetSpeakerSearchTaskRequestRequestTypeDef",
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
    "GetVoiceProfileDomainRequestRequestTypeDef",
    "GetVoiceProfileRequestRequestTypeDef",
    "GetVoiceToneAnalysisTaskRequestRequestTypeDef",
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListProxySessionsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListSipMediaApplicationsRequestRequestTypeDef",
    "ListSipRulesRequestRequestTypeDef",
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    "PhoneNumberCountryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "ListVoiceConnectorsRequestRequestTypeDef",
    "ListVoiceProfileDomainsRequestRequestTypeDef",
    "VoiceProfileDomainSummaryTypeDef",
    "ListVoiceProfilesRequestRequestTypeDef",
    "VoiceProfileSummaryTypeDef",
    "MediaInsightsConfigurationTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "SipMediaApplicationAlexaSkillConfigurationTypeDef",
    "PutVoiceConnectorProxyRequestRequestTypeDef",
    "TerminationTypeDef",
    "RestorePhoneNumberRequestRequestTypeDef",
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    "SpeakerSearchResultTypeDef",
    "StartSpeakerSearchTaskRequestRequestTypeDef",
    "StartVoiceToneAnalysisTaskRequestRequestTypeDef",
    "StopSpeakerSearchTaskRequestRequestTypeDef",
    "StopVoiceToneAnalysisTaskRequestRequestTypeDef",
    "StreamingNotificationTargetTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    "UpdateProxySessionRequestRequestTypeDef",
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    "UpdateVoiceConnectorRequestRequestTypeDef",
    "UpdateVoiceProfileDomainRequestRequestTypeDef",
    "UpdateVoiceProfileRequestRequestTypeDef",
    "ValidateE911AddressRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "ListAvailableVoiceConnectorRegionsResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    "VoiceToneAnalysisTaskTypeDef",
    "ValidateE911AddressResponseTypeDef",
    "CreateProxySessionRequestRequestTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "UpdateSipMediaApplicationCallResponseTypeDef",
    "SipMediaApplicationTypeDef",
    "UpdateSipMediaApplicationRequestRequestTypeDef",
    "CreateSipMediaApplicationRequestRequestTypeDef",
    "CreateVoiceConnectorRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
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
    "CreateVoiceProfileDomainRequestRequestTypeDef",
    "VoiceProfileDomainTypeDef",
    "CreateVoiceProfileResponseTypeDef",
    "GetVoiceProfileResponseTypeDef",
    "UpdateVoiceProfileResponseTypeDef",
    "PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "EmergencyCallingConfigurationOutputTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "UpdateGlobalSettingsRequestRequestTypeDef",
    "GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    "PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
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
    "ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef",
    "ListSipRulesRequestListSipRulesPaginateTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "ListVoiceProfileDomainsResponseTypeDef",
    "ListVoiceProfilesResponseTypeDef",
    "PhoneNumberOrderTypeDef",
    "OriginationOutputTypeDef",
    "OriginationTypeDef",
    "ProxySessionTypeDef",
    "PhoneNumberTypeDef",
    "PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    "SpeakerSearchDetailsTypeDef",
    "StreamingConfigurationOutputTypeDef",
    "StreamingConfigurationTypeDef",
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    "StartVoiceToneAnalysisTaskResponseTypeDef",
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
    "CreateVoiceProfileDomainResponseTypeDef",
    "GetVoiceProfileDomainResponseTypeDef",
    "UpdateVoiceProfileDomainResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
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
    "SpeakerSearchTaskTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "GetSpeakerSearchTaskResponseTypeDef",
    "StartSpeakerSearchTaskResponseTypeDef",
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
BatchDeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberIds": Sequence[str],
    },
)
UpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "UpdatePhoneNumberRequestItemTypeDef",
    {
        "PhoneNumberId": str,
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "CallingName": NotRequired[str],
        "Name": NotRequired[str],
    },
)
CallDetailsTypeDef = TypedDict(
    "CallDetailsTypeDef",
    {
        "VoiceConnectorId": NotRequired[str],
        "TransactionId": NotRequired[str],
        "IsCaller": NotRequired[bool],
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
CreatePhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "E164PhoneNumbers": Sequence[str],
        "Name": NotRequired[str],
    },
)
GeoMatchParamsTypeDef = TypedDict(
    "GeoMatchParamsTypeDef",
    {
        "Country": str,
        "AreaCode": str,
    },
)
CreateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "SipMediaApplicationId": str,
        "SipHeaders": NotRequired[Mapping[str, str]],
        "ArgumentsMap": NotRequired[Mapping[str, str]],
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
VoiceConnectorItemTypeDef = TypedDict(
    "VoiceConnectorItemTypeDef",
    {
        "VoiceConnectorId": str,
        "Priority": int,
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
ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyArn": str,
    },
)
CreateVoiceProfileRequestRequestTypeDef = TypedDict(
    "CreateVoiceProfileRequestRequestTypeDef",
    {
        "SpeakerSearchTaskId": str,
    },
)
VoiceProfileTypeDef = TypedDict(
    "VoiceProfileTypeDef",
    {
        "VoiceProfileId": NotRequired[str],
        "VoiceProfileArn": NotRequired[str],
        "VoiceProfileDomainId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "ExpirationTimestamp": NotRequired[datetime],
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
DeleteVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "DeleteVoiceProfileDomainRequestRequestTypeDef",
    {
        "VoiceProfileDomainId": str,
    },
)
DeleteVoiceProfileRequestRequestTypeDef = TypedDict(
    "DeleteVoiceProfileRequestRequestTypeDef",
    {
        "VoiceProfileId": str,
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
VoiceConnectorSettingsTypeDef = TypedDict(
    "VoiceConnectorSettingsTypeDef",
    {
        "CdrBucket": NotRequired[str],
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
GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
SipMediaApplicationAlexaSkillConfigurationOutputTypeDef = TypedDict(
    "SipMediaApplicationAlexaSkillConfigurationOutputTypeDef",
    {
        "AlexaSkillStatus": AlexaSkillStatusType,
        "AlexaSkillIds": List[str],
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
GetSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "GetSpeakerSearchTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "SpeakerSearchTaskId": str,
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
GetVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "GetVoiceProfileDomainRequestRequestTypeDef",
    {
        "VoiceProfileDomainId": str,
    },
)
GetVoiceProfileRequestRequestTypeDef = TypedDict(
    "GetVoiceProfileRequestRequestTypeDef",
    {
        "VoiceProfileId": str,
    },
)
GetVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "GetVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "VoiceToneAnalysisTaskId": str,
        "IsCaller": bool,
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
        "Status": NotRequired[str],
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
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
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
ListVoiceProfileDomainsRequestRequestTypeDef = TypedDict(
    "ListVoiceProfileDomainsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
VoiceProfileDomainSummaryTypeDef = TypedDict(
    "VoiceProfileDomainSummaryTypeDef",
    {
        "VoiceProfileDomainId": NotRequired[str],
        "VoiceProfileDomainArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
ListVoiceProfilesRequestRequestTypeDef = TypedDict(
    "ListVoiceProfilesRequestRequestTypeDef",
    {
        "VoiceProfileDomainId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
VoiceProfileSummaryTypeDef = TypedDict(
    "VoiceProfileSummaryTypeDef",
    {
        "VoiceProfileId": NotRequired[str],
        "VoiceProfileArn": NotRequired[str],
        "VoiceProfileDomainId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "ExpirationTimestamp": NotRequired[datetime],
    },
)
MediaInsightsConfigurationTypeDef = TypedDict(
    "MediaInsightsConfigurationTypeDef",
    {
        "Disabled": NotRequired[bool],
        "ConfigurationArn": NotRequired[str],
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
SipMediaApplicationAlexaSkillConfigurationTypeDef = TypedDict(
    "SipMediaApplicationAlexaSkillConfigurationTypeDef",
    {
        "AlexaSkillStatus": AlexaSkillStatusType,
        "AlexaSkillIds": Sequence[str],
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
RestorePhoneNumberRequestRequestTypeDef = TypedDict(
    "RestorePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
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
SpeakerSearchResultTypeDef = TypedDict(
    "SpeakerSearchResultTypeDef",
    {
        "ConfidenceScore": NotRequired[float],
        "VoiceProfileId": NotRequired[str],
    },
)
StartSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "StartSpeakerSearchTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "TransactionId": str,
        "VoiceProfileDomainId": str,
        "ClientRequestToken": NotRequired[str],
        "CallLeg": NotRequired[CallLegTypeType],
    },
)
StartVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "StartVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "TransactionId": str,
        "LanguageCode": Literal["en-US"],
        "ClientRequestToken": NotRequired[str],
    },
)
StopSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "StopSpeakerSearchTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "SpeakerSearchTaskId": str,
    },
)
StopVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "StopVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "VoiceToneAnalysisTaskId": str,
    },
)
StreamingNotificationTargetTypeDef = TypedDict(
    "StreamingNotificationTargetTypeDef",
    {
        "NotificationTarget": NotRequired[NotificationTargetType],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "CallingName": NotRequired[str],
        "Name": NotRequired[str],
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
UpdateVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "UpdateVoiceProfileDomainRequestRequestTypeDef",
    {
        "VoiceProfileDomainId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateVoiceProfileRequestRequestTypeDef = TypedDict(
    "UpdateVoiceProfileRequestRequestTypeDef",
    {
        "VoiceProfileId": str,
        "SpeakerSearchTaskId": str,
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
GetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "GetPhoneNumberSettingsResponseTypeDef",
    {
        "CallingName": str,
        "CallingNameUpdatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAvailableVoiceConnectorRegionsResponseTypeDef = TypedDict(
    "ListAvailableVoiceConnectorRegionsResponseTypeDef",
    {
        "VoiceConnectorRegions": List[VoiceConnectorAwsRegionType],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {
        "Usernames": List[str],
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
BatchUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    {
        "UpdatePhoneNumberRequestItems": Sequence[UpdatePhoneNumberRequestItemTypeDef],
    },
)
VoiceToneAnalysisTaskTypeDef = TypedDict(
    "VoiceToneAnalysisTaskTypeDef",
    {
        "VoiceToneAnalysisTaskId": NotRequired[str],
        "VoiceToneAnalysisTaskStatus": NotRequired[str],
        "CallDetails": NotRequired[CallDetailsTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "StartedTimestamp": NotRequired[datetime],
        "StatusMessage": NotRequired[str],
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
SipMediaApplicationTypeDef = TypedDict(
    "SipMediaApplicationTypeDef",
    {
        "SipMediaApplicationId": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "Name": NotRequired[str],
        "Endpoints": NotRequired[List[SipMediaApplicationEndpointTypeDef]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "SipMediaApplicationArn": NotRequired[str],
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
CreateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationRequestRequestTypeDef",
    {
        "AwsRegion": str,
        "Name": str,
        "Endpoints": Sequence[SipMediaApplicationEndpointTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "CreateVoiceConnectorRequestRequestTypeDef",
    {
        "Name": str,
        "RequireEncryption": bool,
        "AwsRegion": NotRequired[VoiceConnectorAwsRegionType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateSipRuleRequestRequestTypeDef = TypedDict(
    "CreateSipRuleRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "Disabled": NotRequired[bool],
        "TargetApplications": NotRequired[Sequence[SipRuleTargetApplicationTypeDef]],
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
CreateVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "CreateVoiceProfileDomainRequestRequestTypeDef",
    {
        "Name": str,
        "ServerSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
VoiceProfileDomainTypeDef = TypedDict(
    "VoiceProfileDomainTypeDef",
    {
        "VoiceProfileDomainId": NotRequired[str],
        "VoiceProfileDomainArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
CreateVoiceProfileResponseTypeDef = TypedDict(
    "CreateVoiceProfileResponseTypeDef",
    {
        "VoiceProfile": VoiceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceProfileResponseTypeDef = TypedDict(
    "GetVoiceProfileResponseTypeDef",
    {
        "VoiceProfile": VoiceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVoiceProfileResponseTypeDef = TypedDict(
    "UpdateVoiceProfileResponseTypeDef",
    {
        "VoiceProfile": VoiceProfileTypeDef,
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
GetGlobalSettingsResponseTypeDef = TypedDict(
    "GetGlobalSettingsResponseTypeDef",
    {
        "VoiceConnector": VoiceConnectorSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGlobalSettingsRequestRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsRequestRequestTypeDef",
    {
        "VoiceConnector": NotRequired[VoiceConnectorSettingsTypeDef],
    },
)
GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    {
        "SipMediaApplicationAlexaSkillConfiguration": SipMediaApplicationAlexaSkillConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    {
        "SipMediaApplicationAlexaSkillConfiguration": SipMediaApplicationAlexaSkillConfigurationOutputTypeDef,
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
ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef = TypedDict(
    "ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSipRulesRequestListSipRulesPaginateTypeDef = TypedDict(
    "ListSipRulesRequestListSipRulesPaginateTypeDef",
    {
        "SipMediaApplicationId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSupportedPhoneNumberCountriesResponseTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    {
        "PhoneNumberCountries": List[PhoneNumberCountryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVoiceProfileDomainsResponseTypeDef = TypedDict(
    "ListVoiceProfileDomainsResponseTypeDef",
    {
        "VoiceProfileDomains": List[VoiceProfileDomainSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListVoiceProfilesResponseTypeDef = TypedDict(
    "ListVoiceProfilesResponseTypeDef",
    {
        "VoiceProfiles": List[VoiceProfileSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PhoneNumberOrderTypeDef = TypedDict(
    "PhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": NotRequired[str],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "Status": NotRequired[PhoneNumberOrderStatusType],
        "OrderType": NotRequired[PhoneNumberOrderTypeType],
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
        "OrderId": NotRequired[str],
        "Name": NotRequired[str],
    },
)
PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef = TypedDict(
    "PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "SipMediaApplicationAlexaSkillConfiguration": NotRequired[
            SipMediaApplicationAlexaSkillConfigurationTypeDef
        ],
    },
)
PutVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Termination": TerminationTypeDef,
    },
)
SpeakerSearchDetailsTypeDef = TypedDict(
    "SpeakerSearchDetailsTypeDef",
    {
        "Results": NotRequired[List[SpeakerSearchResultTypeDef]],
        "VoiceprintGenerationStatus": NotRequired[str],
    },
)
StreamingConfigurationOutputTypeDef = TypedDict(
    "StreamingConfigurationOutputTypeDef",
    {
        "DataRetentionInHours": int,
        "Disabled": bool,
        "StreamingNotificationTargets": NotRequired[List[StreamingNotificationTargetTypeDef]],
        "MediaInsightsConfiguration": NotRequired[MediaInsightsConfigurationTypeDef],
    },
)
StreamingConfigurationTypeDef = TypedDict(
    "StreamingConfigurationTypeDef",
    {
        "DataRetentionInHours": int,
        "Disabled": bool,
        "StreamingNotificationTargets": NotRequired[Sequence[StreamingNotificationTargetTypeDef]],
        "MediaInsightsConfiguration": NotRequired[MediaInsightsConfigurationTypeDef],
    },
)
GetVoiceToneAnalysisTaskResponseTypeDef = TypedDict(
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    {
        "VoiceToneAnalysisTask": VoiceToneAnalysisTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartVoiceToneAnalysisTaskResponseTypeDef = TypedDict(
    "StartVoiceToneAnalysisTaskResponseTypeDef",
    {
        "VoiceToneAnalysisTask": VoiceToneAnalysisTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
CreateVoiceProfileDomainResponseTypeDef = TypedDict(
    "CreateVoiceProfileDomainResponseTypeDef",
    {
        "VoiceProfileDomain": VoiceProfileDomainTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceProfileDomainResponseTypeDef = TypedDict(
    "GetVoiceProfileDomainResponseTypeDef",
    {
        "VoiceProfileDomain": VoiceProfileDomainTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVoiceProfileDomainResponseTypeDef = TypedDict(
    "UpdateVoiceProfileDomainResponseTypeDef",
    {
        "VoiceProfileDomain": VoiceProfileDomainTypeDef,
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
SpeakerSearchTaskTypeDef = TypedDict(
    "SpeakerSearchTaskTypeDef",
    {
        "SpeakerSearchTaskId": NotRequired[str],
        "SpeakerSearchTaskStatus": NotRequired[str],
        "CallDetails": NotRequired[CallDetailsTypeDef],
        "SpeakerSearchDetails": NotRequired[SpeakerSearchDetailsTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "StartedTimestamp": NotRequired[datetime],
        "StatusMessage": NotRequired[str],
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
GetSpeakerSearchTaskResponseTypeDef = TypedDict(
    "GetSpeakerSearchTaskResponseTypeDef",
    {
        "SpeakerSearchTask": SpeakerSearchTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSpeakerSearchTaskResponseTypeDef = TypedDict(
    "StartSpeakerSearchTaskResponseTypeDef",
    {
        "SpeakerSearchTask": SpeakerSearchTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
