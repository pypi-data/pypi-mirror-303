"""
Type annotations for pinpoint-sms-voice-v2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/type_defs/)

Usage::

    ```python
    from mypy_boto3_pinpoint_sms_voice_v2.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AccountAttributeNameType,
    AccountLimitNameType,
    AttachmentStatusType,
    ConfigurationSetFilterNameType,
    DestinationCountryParameterKeyType,
    EventTypeType,
    FieldRequirementType,
    FieldTypeType,
    KeywordActionType,
    LanguageCodeType,
    MessageTypeType,
    NumberCapabilityType,
    NumberStatusType,
    NumberTypeType,
    OwnerType,
    PhoneNumberFilterNameType,
    PoolFilterNameType,
    PoolOriginationIdentitiesFilterNameType,
    PoolStatusType,
    ProtectConfigurationFilterNameType,
    ProtectStatusType,
    RegistrationAssociationBehaviorType,
    RegistrationAssociationFilterNameType,
    RegistrationDisassociationBehaviorType,
    RegistrationFilterNameType,
    RegistrationStatusType,
    RegistrationTypeFilterNameType,
    RegistrationVersionStatusType,
    RequestableNumberTypeType,
    SenderIdFilterNameType,
    SpendLimitNameType,
    VerificationChannelType,
    VerificationStatusType,
    VoiceIdType,
    VoiceMessageBodyTextTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AccountAttributeTypeDef",
    "AccountLimitTypeDef",
    "AssociateOriginationIdentityRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociateProtectConfigurationRequestRequestTypeDef",
    "BlobTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "ConfigurationSetFilterTypeDef",
    "TagTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "SnsDestinationTypeDef",
    "CreateRegistrationAssociationRequestRequestTypeDef",
    "CreateRegistrationVersionRequestRequestTypeDef",
    "RegistrationVersionStatusHistoryTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteDefaultMessageTypeRequestRequestTypeDef",
    "DeleteDefaultSenderIdRequestRequestTypeDef",
    "DeleteEventDestinationRequestRequestTypeDef",
    "DeleteKeywordRequestRequestTypeDef",
    "DeleteOptOutListRequestRequestTypeDef",
    "DeleteOptedOutNumberRequestRequestTypeDef",
    "DeletePoolRequestRequestTypeDef",
    "DeleteProtectConfigurationRequestRequestTypeDef",
    "DeleteRegistrationAttachmentRequestRequestTypeDef",
    "DeleteRegistrationFieldValueRequestRequestTypeDef",
    "DeleteRegistrationRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteVerifiedDestinationNumberRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAccountAttributesRequestRequestTypeDef",
    "DescribeAccountLimitsRequestRequestTypeDef",
    "KeywordFilterTypeDef",
    "KeywordInformationTypeDef",
    "DescribeOptOutListsRequestRequestTypeDef",
    "OptOutListInformationTypeDef",
    "OptedOutFilterTypeDef",
    "OptedOutNumberInformationTypeDef",
    "PhoneNumberFilterTypeDef",
    "PhoneNumberInformationTypeDef",
    "PoolFilterTypeDef",
    "PoolInformationTypeDef",
    "ProtectConfigurationFilterTypeDef",
    "ProtectConfigurationInformationTypeDef",
    "RegistrationAttachmentFilterTypeDef",
    "RegistrationAttachmentsInformationTypeDef",
    "DescribeRegistrationFieldDefinitionsRequestRequestTypeDef",
    "DescribeRegistrationFieldValuesRequestRequestTypeDef",
    "RegistrationFieldValueInformationTypeDef",
    "DescribeRegistrationSectionDefinitionsRequestRequestTypeDef",
    "RegistrationTypeFilterTypeDef",
    "RegistrationVersionFilterTypeDef",
    "RegistrationFilterTypeDef",
    "RegistrationInformationTypeDef",
    "SenderIdAndCountryTypeDef",
    "SenderIdFilterTypeDef",
    "SenderIdInformationTypeDef",
    "DescribeSpendLimitsRequestRequestTypeDef",
    "SpendLimitTypeDef",
    "VerifiedDestinationNumberFilterTypeDef",
    "VerifiedDestinationNumberInformationTypeDef",
    "DisassociateOriginationIdentityRequestRequestTypeDef",
    "DisassociateProtectConfigurationRequestRequestTypeDef",
    "DiscardRegistrationVersionRequestRequestTypeDef",
    "GetProtectConfigurationCountryRuleSetRequestRequestTypeDef",
    "ProtectConfigurationCountryRuleSetInformationTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "PoolOriginationIdentitiesFilterTypeDef",
    "OriginationIdentityMetadataTypeDef",
    "RegistrationAssociationFilterTypeDef",
    "RegistrationAssociationMetadataTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutKeywordRequestRequestTypeDef",
    "PutOptedOutNumberRequestRequestTypeDef",
    "PutRegistrationFieldValueRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RegistrationDeniedReasonInformationTypeDef",
    "SelectValidationTypeDef",
    "TextValidationTypeDef",
    "SelectOptionDescriptionTypeDef",
    "RegistrationSectionDisplayHintsTypeDef",
    "RegistrationTypeDisplayHintsTypeDef",
    "SupportedAssociationTypeDef",
    "ReleasePhoneNumberRequestRequestTypeDef",
    "ReleaseSenderIdRequestRequestTypeDef",
    "SendDestinationNumberVerificationCodeRequestRequestTypeDef",
    "SendMediaMessageRequestRequestTypeDef",
    "SendTextMessageRequestRequestTypeDef",
    "SendVoiceMessageRequestRequestTypeDef",
    "SetAccountDefaultProtectConfigurationRequestRequestTypeDef",
    "SetDefaultMessageTypeRequestRequestTypeDef",
    "SetDefaultSenderIdRequestRequestTypeDef",
    "SetMediaMessageSpendLimitOverrideRequestRequestTypeDef",
    "SetTextMessageSpendLimitOverrideRequestRequestTypeDef",
    "SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef",
    "SubmitRegistrationVersionRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePoolRequestRequestTypeDef",
    "UpdateProtectConfigurationRequestRequestTypeDef",
    "UpdateSenderIdRequestRequestTypeDef",
    "VerifyDestinationNumberRequestRequestTypeDef",
    "AssociateOriginationIdentityResultTypeDef",
    "AssociateProtectConfigurationResultTypeDef",
    "CreateRegistrationAssociationResultTypeDef",
    "DeleteAccountDefaultProtectConfigurationResultTypeDef",
    "DeleteDefaultMessageTypeResultTypeDef",
    "DeleteDefaultSenderIdResultTypeDef",
    "DeleteKeywordResultTypeDef",
    "DeleteMediaMessageSpendLimitOverrideResultTypeDef",
    "DeleteOptOutListResultTypeDef",
    "DeleteOptedOutNumberResultTypeDef",
    "DeletePoolResultTypeDef",
    "DeleteProtectConfigurationResultTypeDef",
    "DeleteRegistrationAttachmentResultTypeDef",
    "DeleteRegistrationFieldValueResultTypeDef",
    "DeleteRegistrationResultTypeDef",
    "DeleteResourcePolicyResultTypeDef",
    "DeleteTextMessageSpendLimitOverrideResultTypeDef",
    "DeleteVerifiedDestinationNumberResultTypeDef",
    "DeleteVoiceMessageSpendLimitOverrideResultTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeAccountLimitsResultTypeDef",
    "DisassociateOriginationIdentityResultTypeDef",
    "DisassociateProtectConfigurationResultTypeDef",
    "GetResourcePolicyResultTypeDef",
    "PutKeywordResultTypeDef",
    "PutOptedOutNumberResultTypeDef",
    "PutRegistrationFieldValueResultTypeDef",
    "PutResourcePolicyResultTypeDef",
    "ReleasePhoneNumberResultTypeDef",
    "ReleaseSenderIdResultTypeDef",
    "SendDestinationNumberVerificationCodeResultTypeDef",
    "SendMediaMessageResultTypeDef",
    "SendTextMessageResultTypeDef",
    "SendVoiceMessageResultTypeDef",
    "SetAccountDefaultProtectConfigurationResultTypeDef",
    "SetDefaultMessageTypeResultTypeDef",
    "SetDefaultSenderIdResultTypeDef",
    "SetMediaMessageSpendLimitOverrideResultTypeDef",
    "SetTextMessageSpendLimitOverrideResultTypeDef",
    "SetVoiceMessageSpendLimitOverrideResultTypeDef",
    "UpdatePhoneNumberResultTypeDef",
    "UpdatePoolResultTypeDef",
    "UpdateProtectConfigurationResultTypeDef",
    "UpdateSenderIdResultTypeDef",
    "VerifyDestinationNumberResultTypeDef",
    "DescribeConfigurationSetsRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateConfigurationSetResultTypeDef",
    "CreateOptOutListRequestRequestTypeDef",
    "CreateOptOutListResultTypeDef",
    "CreatePoolRequestRequestTypeDef",
    "CreatePoolResultTypeDef",
    "CreateProtectConfigurationRequestRequestTypeDef",
    "CreateProtectConfigurationResultTypeDef",
    "CreateRegistrationAttachmentRequestRequestTypeDef",
    "CreateRegistrationAttachmentResultTypeDef",
    "CreateRegistrationRequestRequestTypeDef",
    "CreateRegistrationResultTypeDef",
    "CreateVerifiedDestinationNumberRequestRequestTypeDef",
    "CreateVerifiedDestinationNumberResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "RequestPhoneNumberRequestRequestTypeDef",
    "RequestPhoneNumberResultTypeDef",
    "RequestSenderIdRequestRequestTypeDef",
    "RequestSenderIdResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateEventDestinationRequestRequestTypeDef",
    "EventDestinationTypeDef",
    "UpdateEventDestinationRequestRequestTypeDef",
    "CreateRegistrationVersionResultTypeDef",
    "DiscardRegistrationVersionResultTypeDef",
    "SubmitRegistrationVersionResultTypeDef",
    "DescribeAccountAttributesRequestDescribeAccountAttributesPaginateTypeDef",
    "DescribeAccountLimitsRequestDescribeAccountLimitsPaginateTypeDef",
    "DescribeConfigurationSetsRequestDescribeConfigurationSetsPaginateTypeDef",
    "DescribeOptOutListsRequestDescribeOptOutListsPaginateTypeDef",
    "DescribeRegistrationFieldDefinitionsRequestDescribeRegistrationFieldDefinitionsPaginateTypeDef",
    "DescribeRegistrationFieldValuesRequestDescribeRegistrationFieldValuesPaginateTypeDef",
    "DescribeRegistrationSectionDefinitionsRequestDescribeRegistrationSectionDefinitionsPaginateTypeDef",
    "DescribeSpendLimitsRequestDescribeSpendLimitsPaginateTypeDef",
    "DescribeKeywordsRequestDescribeKeywordsPaginateTypeDef",
    "DescribeKeywordsRequestRequestTypeDef",
    "DescribeKeywordsResultTypeDef",
    "DescribeOptOutListsResultTypeDef",
    "DescribeOptedOutNumbersRequestDescribeOptedOutNumbersPaginateTypeDef",
    "DescribeOptedOutNumbersRequestRequestTypeDef",
    "DescribeOptedOutNumbersResultTypeDef",
    "DescribePhoneNumbersRequestDescribePhoneNumbersPaginateTypeDef",
    "DescribePhoneNumbersRequestRequestTypeDef",
    "DescribePhoneNumbersResultTypeDef",
    "DescribePoolsRequestDescribePoolsPaginateTypeDef",
    "DescribePoolsRequestRequestTypeDef",
    "DescribePoolsResultTypeDef",
    "DescribeProtectConfigurationsRequestDescribeProtectConfigurationsPaginateTypeDef",
    "DescribeProtectConfigurationsRequestRequestTypeDef",
    "DescribeProtectConfigurationsResultTypeDef",
    "DescribeRegistrationAttachmentsRequestDescribeRegistrationAttachmentsPaginateTypeDef",
    "DescribeRegistrationAttachmentsRequestRequestTypeDef",
    "DescribeRegistrationAttachmentsResultTypeDef",
    "DescribeRegistrationFieldValuesResultTypeDef",
    "DescribeRegistrationTypeDefinitionsRequestDescribeRegistrationTypeDefinitionsPaginateTypeDef",
    "DescribeRegistrationTypeDefinitionsRequestRequestTypeDef",
    "DescribeRegistrationVersionsRequestDescribeRegistrationVersionsPaginateTypeDef",
    "DescribeRegistrationVersionsRequestRequestTypeDef",
    "DescribeRegistrationsRequestDescribeRegistrationsPaginateTypeDef",
    "DescribeRegistrationsRequestRequestTypeDef",
    "DescribeRegistrationsResultTypeDef",
    "DescribeSenderIdsRequestDescribeSenderIdsPaginateTypeDef",
    "DescribeSenderIdsRequestRequestTypeDef",
    "DescribeSenderIdsResultTypeDef",
    "DescribeSpendLimitsResultTypeDef",
    "DescribeVerifiedDestinationNumbersRequestDescribeVerifiedDestinationNumbersPaginateTypeDef",
    "DescribeVerifiedDestinationNumbersRequestRequestTypeDef",
    "DescribeVerifiedDestinationNumbersResultTypeDef",
    "GetProtectConfigurationCountryRuleSetResultTypeDef",
    "UpdateProtectConfigurationCountryRuleSetRequestRequestTypeDef",
    "UpdateProtectConfigurationCountryRuleSetResultTypeDef",
    "ListPoolOriginationIdentitiesRequestListPoolOriginationIdentitiesPaginateTypeDef",
    "ListPoolOriginationIdentitiesRequestRequestTypeDef",
    "ListPoolOriginationIdentitiesResultTypeDef",
    "ListRegistrationAssociationsRequestListRegistrationAssociationsPaginateTypeDef",
    "ListRegistrationAssociationsRequestRequestTypeDef",
    "ListRegistrationAssociationsResultTypeDef",
    "RegistrationVersionInformationTypeDef",
    "RegistrationFieldDisplayHintsTypeDef",
    "RegistrationSectionDefinitionTypeDef",
    "RegistrationTypeDefinitionTypeDef",
    "ConfigurationSetInformationTypeDef",
    "CreateEventDestinationResultTypeDef",
    "DeleteConfigurationSetResultTypeDef",
    "DeleteEventDestinationResultTypeDef",
    "UpdateEventDestinationResultTypeDef",
    "DescribeRegistrationVersionsResultTypeDef",
    "RegistrationFieldDefinitionTypeDef",
    "DescribeRegistrationSectionDefinitionsResultTypeDef",
    "DescribeRegistrationTypeDefinitionsResultTypeDef",
    "DescribeConfigurationSetsResultTypeDef",
    "DescribeRegistrationFieldDefinitionsResultTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "Name": AccountAttributeNameType,
        "Value": str,
    },
)
AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Name": AccountLimitNameType,
        "Used": int,
        "Max": int,
    },
)
AssociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "AssociateOriginationIdentityRequestRequestTypeDef",
    {
        "PoolId": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "ClientToken": NotRequired[str],
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
AssociateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "AssociateProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "ConfigurationSetName": str,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "IamRoleArn": str,
        "LogGroupArn": str,
    },
)
ConfigurationSetFilterTypeDef = TypedDict(
    "ConfigurationSetFilterTypeDef",
    {
        "Name": ConfigurationSetFilterNameType,
        "Values": Sequence[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)
SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
)
CreateRegistrationAssociationRequestRequestTypeDef = TypedDict(
    "CreateRegistrationAssociationRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "ResourceId": str,
    },
)
CreateRegistrationVersionRequestRequestTypeDef = TypedDict(
    "CreateRegistrationVersionRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)
RegistrationVersionStatusHistoryTypeDef = TypedDict(
    "RegistrationVersionStatusHistoryTypeDef",
    {
        "DraftTimestamp": datetime,
        "SubmittedTimestamp": NotRequired[datetime],
        "ReviewingTimestamp": NotRequired[datetime],
        "ApprovedTimestamp": NotRequired[datetime],
        "DiscardedTimestamp": NotRequired[datetime],
        "DeniedTimestamp": NotRequired[datetime],
        "RevokedTimestamp": NotRequired[datetime],
        "ArchivedTimestamp": NotRequired[datetime],
    },
)
DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
DeleteDefaultMessageTypeRequestRequestTypeDef = TypedDict(
    "DeleteDefaultMessageTypeRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
DeleteDefaultSenderIdRequestRequestTypeDef = TypedDict(
    "DeleteDefaultSenderIdRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
DeleteEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)
DeleteKeywordRequestRequestTypeDef = TypedDict(
    "DeleteKeywordRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "Keyword": str,
    },
)
DeleteOptOutListRequestRequestTypeDef = TypedDict(
    "DeleteOptOutListRequestRequestTypeDef",
    {
        "OptOutListName": str,
    },
)
DeleteOptedOutNumberRequestRequestTypeDef = TypedDict(
    "DeleteOptedOutNumberRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "OptedOutNumber": str,
    },
)
DeletePoolRequestRequestTypeDef = TypedDict(
    "DeletePoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
DeleteProtectConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
    },
)
DeleteRegistrationAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteRegistrationAttachmentRequestRequestTypeDef",
    {
        "RegistrationAttachmentId": str,
    },
)
DeleteRegistrationFieldValueRequestRequestTypeDef = TypedDict(
    "DeleteRegistrationFieldValueRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "FieldPath": str,
    },
)
DeleteRegistrationRequestRequestTypeDef = TypedDict(
    "DeleteRegistrationRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DeleteVerifiedDestinationNumberRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedDestinationNumberRequestRequestTypeDef",
    {
        "VerifiedDestinationNumberId": str,
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
DescribeAccountAttributesRequestRequestTypeDef = TypedDict(
    "DescribeAccountAttributesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeAccountLimitsRequestRequestTypeDef = TypedDict(
    "DescribeAccountLimitsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
KeywordFilterTypeDef = TypedDict(
    "KeywordFilterTypeDef",
    {
        "Name": Literal["keyword-action"],
        "Values": Sequence[str],
    },
)
KeywordInformationTypeDef = TypedDict(
    "KeywordInformationTypeDef",
    {
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
    },
)
DescribeOptOutListsRequestRequestTypeDef = TypedDict(
    "DescribeOptOutListsRequestRequestTypeDef",
    {
        "OptOutListNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Owner": NotRequired[OwnerType],
    },
)
OptOutListInformationTypeDef = TypedDict(
    "OptOutListInformationTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "CreatedTimestamp": datetime,
    },
)
OptedOutFilterTypeDef = TypedDict(
    "OptedOutFilterTypeDef",
    {
        "Name": Literal["end-user-opted-out"],
        "Values": Sequence[str],
    },
)
OptedOutNumberInformationTypeDef = TypedDict(
    "OptedOutNumberInformationTypeDef",
    {
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
    },
)
PhoneNumberFilterTypeDef = TypedDict(
    "PhoneNumberFilterTypeDef",
    {
        "Name": PhoneNumberFilterNameType,
        "Values": Sequence[str],
    },
)
PhoneNumberInformationTypeDef = TypedDict(
    "PhoneNumberInformationTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "PhoneNumberId": NotRequired[str],
        "TwoWayChannelArn": NotRequired[str],
        "TwoWayChannelRole": NotRequired[str],
        "PoolId": NotRequired[str],
        "RegistrationId": NotRequired[str],
    },
)
PoolFilterTypeDef = TypedDict(
    "PoolFilterTypeDef",
    {
        "Name": PoolFilterNameType,
        "Values": Sequence[str],
    },
)
PoolInformationTypeDef = TypedDict(
    "PoolInformationTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "TwoWayChannelArn": NotRequired[str],
        "TwoWayChannelRole": NotRequired[str],
    },
)
ProtectConfigurationFilterTypeDef = TypedDict(
    "ProtectConfigurationFilterTypeDef",
    {
        "Name": ProtectConfigurationFilterNameType,
        "Values": Sequence[str],
    },
)
ProtectConfigurationInformationTypeDef = TypedDict(
    "ProtectConfigurationInformationTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "CreatedTimestamp": datetime,
        "AccountDefault": bool,
        "DeletionProtectionEnabled": bool,
    },
)
RegistrationAttachmentFilterTypeDef = TypedDict(
    "RegistrationAttachmentFilterTypeDef",
    {
        "Name": Literal["attachment-status"],
        "Values": Sequence[str],
    },
)
RegistrationAttachmentsInformationTypeDef = TypedDict(
    "RegistrationAttachmentsInformationTypeDef",
    {
        "RegistrationAttachmentArn": str,
        "RegistrationAttachmentId": str,
        "AttachmentStatus": AttachmentStatusType,
        "CreatedTimestamp": datetime,
        "AttachmentUploadErrorReason": NotRequired[Literal["INTERNAL_ERROR"]],
    },
)
DescribeRegistrationFieldDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationFieldDefinitionsRequestRequestTypeDef",
    {
        "RegistrationType": str,
        "SectionPath": NotRequired[str],
        "FieldPaths": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeRegistrationFieldValuesRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationFieldValuesRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "VersionNumber": NotRequired[int],
        "SectionPath": NotRequired[str],
        "FieldPaths": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RegistrationFieldValueInformationTypeDef = TypedDict(
    "RegistrationFieldValueInformationTypeDef",
    {
        "FieldPath": str,
        "SelectChoices": NotRequired[List[str]],
        "TextValue": NotRequired[str],
        "RegistrationAttachmentId": NotRequired[str],
        "DeniedReason": NotRequired[str],
    },
)
DescribeRegistrationSectionDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationSectionDefinitionsRequestRequestTypeDef",
    {
        "RegistrationType": str,
        "SectionPaths": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RegistrationTypeFilterTypeDef = TypedDict(
    "RegistrationTypeFilterTypeDef",
    {
        "Name": RegistrationTypeFilterNameType,
        "Values": Sequence[str],
    },
)
RegistrationVersionFilterTypeDef = TypedDict(
    "RegistrationVersionFilterTypeDef",
    {
        "Name": Literal["registration-version-status"],
        "Values": Sequence[str],
    },
)
RegistrationFilterTypeDef = TypedDict(
    "RegistrationFilterTypeDef",
    {
        "Name": RegistrationFilterNameType,
        "Values": Sequence[str],
    },
)
RegistrationInformationTypeDef = TypedDict(
    "RegistrationInformationTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "RegistrationStatus": RegistrationStatusType,
        "CurrentVersionNumber": int,
        "CreatedTimestamp": datetime,
        "ApprovedVersionNumber": NotRequired[int],
        "LatestDeniedVersionNumber": NotRequired[int],
        "AdditionalAttributes": NotRequired[Dict[str, str]],
    },
)
SenderIdAndCountryTypeDef = TypedDict(
    "SenderIdAndCountryTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
    },
)
SenderIdFilterTypeDef = TypedDict(
    "SenderIdFilterTypeDef",
    {
        "Name": SenderIdFilterNameType,
        "Values": Sequence[str],
    },
)
SenderIdInformationTypeDef = TypedDict(
    "SenderIdInformationTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
        "DeletionProtectionEnabled": bool,
        "Registered": bool,
        "RegistrationId": NotRequired[str],
    },
)
DescribeSpendLimitsRequestRequestTypeDef = TypedDict(
    "DescribeSpendLimitsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SpendLimitTypeDef = TypedDict(
    "SpendLimitTypeDef",
    {
        "Name": SpendLimitNameType,
        "EnforcedLimit": int,
        "MaxLimit": int,
        "Overridden": bool,
    },
)
VerifiedDestinationNumberFilterTypeDef = TypedDict(
    "VerifiedDestinationNumberFilterTypeDef",
    {
        "Name": Literal["status"],
        "Values": Sequence[str],
    },
)
VerifiedDestinationNumberInformationTypeDef = TypedDict(
    "VerifiedDestinationNumberInformationTypeDef",
    {
        "VerifiedDestinationNumberArn": str,
        "VerifiedDestinationNumberId": str,
        "DestinationPhoneNumber": str,
        "Status": VerificationStatusType,
        "CreatedTimestamp": datetime,
    },
)
DisassociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "DisassociateOriginationIdentityRequestRequestTypeDef",
    {
        "PoolId": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "ClientToken": NotRequired[str],
    },
)
DisassociateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "DisassociateProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "ConfigurationSetName": str,
    },
)
DiscardRegistrationVersionRequestRequestTypeDef = TypedDict(
    "DiscardRegistrationVersionRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)
GetProtectConfigurationCountryRuleSetRequestRequestTypeDef = TypedDict(
    "GetProtectConfigurationCountryRuleSetRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "NumberCapability": NumberCapabilityType,
    },
)
ProtectConfigurationCountryRuleSetInformationTypeDef = TypedDict(
    "ProtectConfigurationCountryRuleSetInformationTypeDef",
    {
        "ProtectStatus": ProtectStatusType,
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PoolOriginationIdentitiesFilterTypeDef = TypedDict(
    "PoolOriginationIdentitiesFilterTypeDef",
    {
        "Name": PoolOriginationIdentitiesFilterNameType,
        "Values": Sequence[str],
    },
)
OriginationIdentityMetadataTypeDef = TypedDict(
    "OriginationIdentityMetadataTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "NumberCapabilities": List[NumberCapabilityType],
        "PhoneNumber": NotRequired[str],
    },
)
RegistrationAssociationFilterTypeDef = TypedDict(
    "RegistrationAssociationFilterTypeDef",
    {
        "Name": RegistrationAssociationFilterNameType,
        "Values": Sequence[str],
    },
)
RegistrationAssociationMetadataTypeDef = TypedDict(
    "RegistrationAssociationMetadataTypeDef",
    {
        "ResourceArn": str,
        "ResourceId": str,
        "ResourceType": str,
        "IsoCountryCode": NotRequired[str],
        "PhoneNumber": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PutKeywordRequestRequestTypeDef = TypedDict(
    "PutKeywordRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": NotRequired[KeywordActionType],
    },
)
PutOptedOutNumberRequestRequestTypeDef = TypedDict(
    "PutOptedOutNumberRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "OptedOutNumber": str,
    },
)
PutRegistrationFieldValueRequestRequestTypeDef = TypedDict(
    "PutRegistrationFieldValueRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "FieldPath": str,
        "SelectChoices": NotRequired[Sequence[str]],
        "TextValue": NotRequired[str],
        "RegistrationAttachmentId": NotRequired[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)
RegistrationDeniedReasonInformationTypeDef = TypedDict(
    "RegistrationDeniedReasonInformationTypeDef",
    {
        "Reason": str,
        "ShortDescription": str,
        "LongDescription": NotRequired[str],
        "DocumentationTitle": NotRequired[str],
        "DocumentationLink": NotRequired[str],
    },
)
SelectValidationTypeDef = TypedDict(
    "SelectValidationTypeDef",
    {
        "MinChoices": int,
        "MaxChoices": int,
        "Options": List[str],
    },
)
TextValidationTypeDef = TypedDict(
    "TextValidationTypeDef",
    {
        "MinLength": int,
        "MaxLength": int,
        "Pattern": str,
    },
)
SelectOptionDescriptionTypeDef = TypedDict(
    "SelectOptionDescriptionTypeDef",
    {
        "Option": str,
        "Title": NotRequired[str],
        "Description": NotRequired[str],
    },
)
RegistrationSectionDisplayHintsTypeDef = TypedDict(
    "RegistrationSectionDisplayHintsTypeDef",
    {
        "Title": str,
        "ShortDescription": str,
        "LongDescription": NotRequired[str],
        "DocumentationTitle": NotRequired[str],
        "DocumentationLink": NotRequired[str],
    },
)
RegistrationTypeDisplayHintsTypeDef = TypedDict(
    "RegistrationTypeDisplayHintsTypeDef",
    {
        "Title": str,
        "ShortDescription": NotRequired[str],
        "LongDescription": NotRequired[str],
        "DocumentationTitle": NotRequired[str],
        "DocumentationLink": NotRequired[str],
    },
)
SupportedAssociationTypeDef = TypedDict(
    "SupportedAssociationTypeDef",
    {
        "ResourceType": str,
        "AssociationBehavior": RegistrationAssociationBehaviorType,
        "DisassociationBehavior": RegistrationDisassociationBehaviorType,
        "IsoCountryCode": NotRequired[str],
    },
)
ReleasePhoneNumberRequestRequestTypeDef = TypedDict(
    "ReleasePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
ReleaseSenderIdRequestRequestTypeDef = TypedDict(
    "ReleaseSenderIdRequestRequestTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
    },
)
SendDestinationNumberVerificationCodeRequestRequestTypeDef = TypedDict(
    "SendDestinationNumberVerificationCodeRequestRequestTypeDef",
    {
        "VerifiedDestinationNumberId": str,
        "VerificationChannel": VerificationChannelType,
        "LanguageCode": NotRequired[LanguageCodeType],
        "OriginationIdentity": NotRequired[str],
        "ConfigurationSetName": NotRequired[str],
        "Context": NotRequired[Mapping[str, str]],
        "DestinationCountryParameters": NotRequired[
            Mapping[DestinationCountryParameterKeyType, str]
        ],
    },
)
SendMediaMessageRequestRequestTypeDef = TypedDict(
    "SendMediaMessageRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "OriginationIdentity": str,
        "MessageBody": NotRequired[str],
        "MediaUrls": NotRequired[Sequence[str]],
        "ConfigurationSetName": NotRequired[str],
        "MaxPrice": NotRequired[str],
        "TimeToLive": NotRequired[int],
        "Context": NotRequired[Mapping[str, str]],
        "DryRun": NotRequired[bool],
        "ProtectConfigurationId": NotRequired[str],
    },
)
SendTextMessageRequestRequestTypeDef = TypedDict(
    "SendTextMessageRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "OriginationIdentity": NotRequired[str],
        "MessageBody": NotRequired[str],
        "MessageType": NotRequired[MessageTypeType],
        "Keyword": NotRequired[str],
        "ConfigurationSetName": NotRequired[str],
        "MaxPrice": NotRequired[str],
        "TimeToLive": NotRequired[int],
        "Context": NotRequired[Mapping[str, str]],
        "DestinationCountryParameters": NotRequired[
            Mapping[DestinationCountryParameterKeyType, str]
        ],
        "DryRun": NotRequired[bool],
        "ProtectConfigurationId": NotRequired[str],
    },
)
SendVoiceMessageRequestRequestTypeDef = TypedDict(
    "SendVoiceMessageRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "OriginationIdentity": str,
        "MessageBody": NotRequired[str],
        "MessageBodyTextType": NotRequired[VoiceMessageBodyTextTypeType],
        "VoiceId": NotRequired[VoiceIdType],
        "ConfigurationSetName": NotRequired[str],
        "MaxPricePerMinute": NotRequired[str],
        "TimeToLive": NotRequired[int],
        "Context": NotRequired[Mapping[str, str]],
        "DryRun": NotRequired[bool],
        "ProtectConfigurationId": NotRequired[str],
    },
)
SetAccountDefaultProtectConfigurationRequestRequestTypeDef = TypedDict(
    "SetAccountDefaultProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
    },
)
SetDefaultMessageTypeRequestRequestTypeDef = TypedDict(
    "SetDefaultMessageTypeRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
    },
)
SetDefaultSenderIdRequestRequestTypeDef = TypedDict(
    "SetDefaultSenderIdRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "SenderId": str,
    },
)
SetMediaMessageSpendLimitOverrideRequestRequestTypeDef = TypedDict(
    "SetMediaMessageSpendLimitOverrideRequestRequestTypeDef",
    {
        "MonthlyLimit": int,
    },
)
SetTextMessageSpendLimitOverrideRequestRequestTypeDef = TypedDict(
    "SetTextMessageSpendLimitOverrideRequestRequestTypeDef",
    {
        "MonthlyLimit": int,
    },
)
SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef = TypedDict(
    "SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef",
    {
        "MonthlyLimit": int,
    },
)
SubmitRegistrationVersionRequestRequestTypeDef = TypedDict(
    "SubmitRegistrationVersionRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "TwoWayEnabled": NotRequired[bool],
        "TwoWayChannelArn": NotRequired[str],
        "TwoWayChannelRole": NotRequired[str],
        "SelfManagedOptOutsEnabled": NotRequired[bool],
        "OptOutListName": NotRequired[str],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
UpdatePoolRequestRequestTypeDef = TypedDict(
    "UpdatePoolRequestRequestTypeDef",
    {
        "PoolId": str,
        "TwoWayEnabled": NotRequired[bool],
        "TwoWayChannelArn": NotRequired[str],
        "TwoWayChannelRole": NotRequired[str],
        "SelfManagedOptOutsEnabled": NotRequired[bool],
        "OptOutListName": NotRequired[str],
        "SharedRoutesEnabled": NotRequired[bool],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
UpdateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
UpdateSenderIdRequestRequestTypeDef = TypedDict(
    "UpdateSenderIdRequestRequestTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
VerifyDestinationNumberRequestRequestTypeDef = TypedDict(
    "VerifyDestinationNumberRequestRequestTypeDef",
    {
        "VerifiedDestinationNumberId": str,
        "VerificationCode": str,
    },
)
AssociateOriginationIdentityResultTypeDef = TypedDict(
    "AssociateOriginationIdentityResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateProtectConfigurationResultTypeDef = TypedDict(
    "AssociateProtectConfigurationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRegistrationAssociationResultTypeDef = TypedDict(
    "CreateRegistrationAssociationResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "ResourceArn": str,
        "ResourceId": str,
        "ResourceType": str,
        "IsoCountryCode": str,
        "PhoneNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAccountDefaultProtectConfigurationResultTypeDef = TypedDict(
    "DeleteAccountDefaultProtectConfigurationResultTypeDef",
    {
        "DefaultProtectConfigurationArn": str,
        "DefaultProtectConfigurationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDefaultMessageTypeResultTypeDef = TypedDict(
    "DeleteDefaultMessageTypeResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDefaultSenderIdResultTypeDef = TypedDict(
    "DeleteDefaultSenderIdResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "SenderId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteKeywordResultTypeDef = TypedDict(
    "DeleteKeywordResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMediaMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "DeleteMediaMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteOptOutListResultTypeDef = TypedDict(
    "DeleteOptOutListResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteOptedOutNumberResultTypeDef = TypedDict(
    "DeleteOptedOutNumberResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePoolResultTypeDef = TypedDict(
    "DeletePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProtectConfigurationResultTypeDef = TypedDict(
    "DeleteProtectConfigurationResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "CreatedTimestamp": datetime,
        "AccountDefault": bool,
        "DeletionProtectionEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRegistrationAttachmentResultTypeDef = TypedDict(
    "DeleteRegistrationAttachmentResultTypeDef",
    {
        "RegistrationAttachmentArn": str,
        "RegistrationAttachmentId": str,
        "AttachmentStatus": AttachmentStatusType,
        "AttachmentUploadErrorReason": Literal["INTERNAL_ERROR"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRegistrationFieldValueResultTypeDef = TypedDict(
    "DeleteRegistrationFieldValueResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "FieldPath": str,
        "SelectChoices": List[str],
        "TextValue": str,
        "RegistrationAttachmentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRegistrationResultTypeDef = TypedDict(
    "DeleteRegistrationResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "RegistrationStatus": RegistrationStatusType,
        "CurrentVersionNumber": int,
        "ApprovedVersionNumber": int,
        "LatestDeniedVersionNumber": int,
        "AdditionalAttributes": Dict[str, str],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResourcePolicyResultTypeDef = TypedDict(
    "DeleteResourcePolicyResultTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTextMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "DeleteTextMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVerifiedDestinationNumberResultTypeDef = TypedDict(
    "DeleteVerifiedDestinationNumberResultTypeDef",
    {
        "VerifiedDestinationNumberArn": str,
        "VerifiedDestinationNumberId": str,
        "DestinationPhoneNumber": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVoiceMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "DeleteVoiceMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {
        "AccountAttributes": List[AccountAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeAccountLimitsResultTypeDef = TypedDict(
    "DescribeAccountLimitsResultTypeDef",
    {
        "AccountLimits": List[AccountLimitTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DisassociateOriginationIdentityResultTypeDef = TypedDict(
    "DisassociateOriginationIdentityResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateProtectConfigurationResultTypeDef = TypedDict(
    "DisassociateProtectConfigurationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResultTypeDef = TypedDict(
    "GetResourcePolicyResultTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutKeywordResultTypeDef = TypedDict(
    "PutKeywordResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutOptedOutNumberResultTypeDef = TypedDict(
    "PutOptedOutNumberResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRegistrationFieldValueResultTypeDef = TypedDict(
    "PutRegistrationFieldValueResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "FieldPath": str,
        "SelectChoices": List[str],
        "TextValue": str,
        "RegistrationAttachmentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourcePolicyResultTypeDef = TypedDict(
    "PutResourcePolicyResultTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReleasePhoneNumberResultTypeDef = TypedDict(
    "ReleasePhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "RegistrationId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReleaseSenderIdResultTypeDef = TypedDict(
    "ReleaseSenderIdResultTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
        "Registered": bool,
        "RegistrationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendDestinationNumberVerificationCodeResultTypeDef = TypedDict(
    "SendDestinationNumberVerificationCodeResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendMediaMessageResultTypeDef = TypedDict(
    "SendMediaMessageResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendTextMessageResultTypeDef = TypedDict(
    "SendTextMessageResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendVoiceMessageResultTypeDef = TypedDict(
    "SendVoiceMessageResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetAccountDefaultProtectConfigurationResultTypeDef = TypedDict(
    "SetAccountDefaultProtectConfigurationResultTypeDef",
    {
        "DefaultProtectConfigurationArn": str,
        "DefaultProtectConfigurationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetDefaultMessageTypeResultTypeDef = TypedDict(
    "SetDefaultMessageTypeResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetDefaultSenderIdResultTypeDef = TypedDict(
    "SetDefaultSenderIdResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "SenderId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetMediaMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "SetMediaMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetTextMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "SetTextMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetVoiceMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "SetVoiceMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePhoneNumberResultTypeDef = TypedDict(
    "UpdatePhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "RegistrationId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePoolResultTypeDef = TypedDict(
    "UpdatePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProtectConfigurationResultTypeDef = TypedDict(
    "UpdateProtectConfigurationResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "CreatedTimestamp": datetime,
        "AccountDefault": bool,
        "DeletionProtectionEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSenderIdResultTypeDef = TypedDict(
    "UpdateSenderIdResultTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
        "DeletionProtectionEnabled": bool,
        "Registered": bool,
        "RegistrationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyDestinationNumberResultTypeDef = TypedDict(
    "VerifyDestinationNumberResultTypeDef",
    {
        "VerifiedDestinationNumberArn": str,
        "VerifiedDestinationNumberId": str,
        "DestinationPhoneNumber": str,
        "Status": VerificationStatusType,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConfigurationSetsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationSetsRequestRequestTypeDef",
    {
        "ConfigurationSetNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[ConfigurationSetFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateConfigurationSetResultTypeDef = TypedDict(
    "CreateConfigurationSetResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "Tags": List[TagTypeDef],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOptOutListRequestRequestTypeDef = TypedDict(
    "CreateOptOutListRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateOptOutListResultTypeDef = TypedDict(
    "CreateOptOutListResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "Tags": List[TagTypeDef],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePoolRequestRequestTypeDef = TypedDict(
    "CreatePoolRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "DeletionProtectionEnabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreatePoolResultTypeDef = TypedDict(
    "CreatePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "Tags": List[TagTypeDef],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "CreateProtectConfigurationRequestRequestTypeDef",
    {
        "ClientToken": NotRequired[str],
        "DeletionProtectionEnabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateProtectConfigurationResultTypeDef = TypedDict(
    "CreateProtectConfigurationResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "CreatedTimestamp": datetime,
        "AccountDefault": bool,
        "DeletionProtectionEnabled": bool,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRegistrationAttachmentRequestRequestTypeDef = TypedDict(
    "CreateRegistrationAttachmentRequestRequestTypeDef",
    {
        "AttachmentBody": NotRequired[BlobTypeDef],
        "AttachmentUrl": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateRegistrationAttachmentResultTypeDef = TypedDict(
    "CreateRegistrationAttachmentResultTypeDef",
    {
        "RegistrationAttachmentArn": str,
        "RegistrationAttachmentId": str,
        "AttachmentStatus": AttachmentStatusType,
        "Tags": List[TagTypeDef],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRegistrationRequestRequestTypeDef = TypedDict(
    "CreateRegistrationRequestRequestTypeDef",
    {
        "RegistrationType": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateRegistrationResultTypeDef = TypedDict(
    "CreateRegistrationResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "RegistrationStatus": RegistrationStatusType,
        "CurrentVersionNumber": int,
        "AdditionalAttributes": Dict[str, str],
        "Tags": List[TagTypeDef],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVerifiedDestinationNumberRequestRequestTypeDef = TypedDict(
    "CreateVerifiedDestinationNumberRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateVerifiedDestinationNumberResultTypeDef = TypedDict(
    "CreateVerifiedDestinationNumberResultTypeDef",
    {
        "VerifiedDestinationNumberArn": str,
        "VerifiedDestinationNumberId": str,
        "DestinationPhoneNumber": str,
        "Status": VerificationStatusType,
        "Tags": List[TagTypeDef],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "ResourceArn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestPhoneNumberRequestRequestTypeDef = TypedDict(
    "RequestPhoneNumberRequestRequestTypeDef",
    {
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": Sequence[NumberCapabilityType],
        "NumberType": RequestableNumberTypeType,
        "OptOutListName": NotRequired[str],
        "PoolId": NotRequired[str],
        "RegistrationId": NotRequired[str],
        "DeletionProtectionEnabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
RequestPhoneNumberResultTypeDef = TypedDict(
    "RequestPhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": RequestableNumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "PoolId": str,
        "RegistrationId": str,
        "Tags": List[TagTypeDef],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestSenderIdRequestRequestTypeDef = TypedDict(
    "RequestSenderIdRequestRequestTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": NotRequired[Sequence[MessageTypeType]],
        "DeletionProtectionEnabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
RequestSenderIdResultTypeDef = TypedDict(
    "RequestSenderIdResultTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
        "DeletionProtectionEnabled": bool,
        "Registered": bool,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateEventDestinationRequestRequestTypeDef = TypedDict(
    "CreateEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "MatchingEventTypes": Sequence[EventTypeType],
        "CloudWatchLogsDestination": NotRequired[CloudWatchLogsDestinationTypeDef],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "SnsDestination": NotRequired[SnsDestinationTypeDef],
        "ClientToken": NotRequired[str],
    },
)
EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "EventDestinationName": str,
        "Enabled": bool,
        "MatchingEventTypes": List[EventTypeType],
        "CloudWatchLogsDestination": NotRequired[CloudWatchLogsDestinationTypeDef],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "SnsDestination": NotRequired[SnsDestinationTypeDef],
    },
)
UpdateEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "Enabled": NotRequired[bool],
        "MatchingEventTypes": NotRequired[Sequence[EventTypeType]],
        "CloudWatchLogsDestination": NotRequired[CloudWatchLogsDestinationTypeDef],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "SnsDestination": NotRequired[SnsDestinationTypeDef],
    },
)
CreateRegistrationVersionResultTypeDef = TypedDict(
    "CreateRegistrationVersionResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "RegistrationVersionStatus": RegistrationVersionStatusType,
        "RegistrationVersionStatusHistory": RegistrationVersionStatusHistoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DiscardRegistrationVersionResultTypeDef = TypedDict(
    "DiscardRegistrationVersionResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "RegistrationVersionStatus": RegistrationVersionStatusType,
        "RegistrationVersionStatusHistory": RegistrationVersionStatusHistoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubmitRegistrationVersionResultTypeDef = TypedDict(
    "SubmitRegistrationVersionResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "RegistrationVersionStatus": RegistrationVersionStatusType,
        "RegistrationVersionStatusHistory": RegistrationVersionStatusHistoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountAttributesRequestDescribeAccountAttributesPaginateTypeDef = TypedDict(
    "DescribeAccountAttributesRequestDescribeAccountAttributesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAccountLimitsRequestDescribeAccountLimitsPaginateTypeDef = TypedDict(
    "DescribeAccountLimitsRequestDescribeAccountLimitsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConfigurationSetsRequestDescribeConfigurationSetsPaginateTypeDef = TypedDict(
    "DescribeConfigurationSetsRequestDescribeConfigurationSetsPaginateTypeDef",
    {
        "ConfigurationSetNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[ConfigurationSetFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOptOutListsRequestDescribeOptOutListsPaginateTypeDef = TypedDict(
    "DescribeOptOutListsRequestDescribeOptOutListsPaginateTypeDef",
    {
        "OptOutListNames": NotRequired[Sequence[str]],
        "Owner": NotRequired[OwnerType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegistrationFieldDefinitionsRequestDescribeRegistrationFieldDefinitionsPaginateTypeDef = TypedDict(
    "DescribeRegistrationFieldDefinitionsRequestDescribeRegistrationFieldDefinitionsPaginateTypeDef",
    {
        "RegistrationType": str,
        "SectionPath": NotRequired[str],
        "FieldPaths": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegistrationFieldValuesRequestDescribeRegistrationFieldValuesPaginateTypeDef = TypedDict(
    "DescribeRegistrationFieldValuesRequestDescribeRegistrationFieldValuesPaginateTypeDef",
    {
        "RegistrationId": str,
        "VersionNumber": NotRequired[int],
        "SectionPath": NotRequired[str],
        "FieldPaths": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegistrationSectionDefinitionsRequestDescribeRegistrationSectionDefinitionsPaginateTypeDef = TypedDict(
    "DescribeRegistrationSectionDefinitionsRequestDescribeRegistrationSectionDefinitionsPaginateTypeDef",
    {
        "RegistrationType": str,
        "SectionPaths": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSpendLimitsRequestDescribeSpendLimitsPaginateTypeDef = TypedDict(
    "DescribeSpendLimitsRequestDescribeSpendLimitsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeKeywordsRequestDescribeKeywordsPaginateTypeDef = TypedDict(
    "DescribeKeywordsRequestDescribeKeywordsPaginateTypeDef",
    {
        "OriginationIdentity": str,
        "Keywords": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[KeywordFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeKeywordsRequestRequestTypeDef = TypedDict(
    "DescribeKeywordsRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "Keywords": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[KeywordFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeKeywordsResultTypeDef = TypedDict(
    "DescribeKeywordsResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keywords": List[KeywordInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeOptOutListsResultTypeDef = TypedDict(
    "DescribeOptOutListsResultTypeDef",
    {
        "OptOutLists": List[OptOutListInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeOptedOutNumbersRequestDescribeOptedOutNumbersPaginateTypeDef = TypedDict(
    "DescribeOptedOutNumbersRequestDescribeOptedOutNumbersPaginateTypeDef",
    {
        "OptOutListName": str,
        "OptedOutNumbers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[OptedOutFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOptedOutNumbersRequestRequestTypeDef = TypedDict(
    "DescribeOptedOutNumbersRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "OptedOutNumbers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[OptedOutFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeOptedOutNumbersResultTypeDef = TypedDict(
    "DescribeOptedOutNumbersResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumbers": List[OptedOutNumberInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribePhoneNumbersRequestDescribePhoneNumbersPaginateTypeDef = TypedDict(
    "DescribePhoneNumbersRequestDescribePhoneNumbersPaginateTypeDef",
    {
        "PhoneNumberIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[PhoneNumberFilterTypeDef]],
        "Owner": NotRequired[OwnerType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePhoneNumbersRequestRequestTypeDef = TypedDict(
    "DescribePhoneNumbersRequestRequestTypeDef",
    {
        "PhoneNumberIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[PhoneNumberFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Owner": NotRequired[OwnerType],
    },
)
DescribePhoneNumbersResultTypeDef = TypedDict(
    "DescribePhoneNumbersResultTypeDef",
    {
        "PhoneNumbers": List[PhoneNumberInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribePoolsRequestDescribePoolsPaginateTypeDef = TypedDict(
    "DescribePoolsRequestDescribePoolsPaginateTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[PoolFilterTypeDef]],
        "Owner": NotRequired[OwnerType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePoolsRequestRequestTypeDef = TypedDict(
    "DescribePoolsRequestRequestTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[PoolFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Owner": NotRequired[OwnerType],
    },
)
DescribePoolsResultTypeDef = TypedDict(
    "DescribePoolsResultTypeDef",
    {
        "Pools": List[PoolInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeProtectConfigurationsRequestDescribeProtectConfigurationsPaginateTypeDef = TypedDict(
    "DescribeProtectConfigurationsRequestDescribeProtectConfigurationsPaginateTypeDef",
    {
        "ProtectConfigurationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[ProtectConfigurationFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeProtectConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeProtectConfigurationsRequestRequestTypeDef",
    {
        "ProtectConfigurationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[ProtectConfigurationFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeProtectConfigurationsResultTypeDef = TypedDict(
    "DescribeProtectConfigurationsResultTypeDef",
    {
        "ProtectConfigurations": List[ProtectConfigurationInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeRegistrationAttachmentsRequestDescribeRegistrationAttachmentsPaginateTypeDef = TypedDict(
    "DescribeRegistrationAttachmentsRequestDescribeRegistrationAttachmentsPaginateTypeDef",
    {
        "RegistrationAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[RegistrationAttachmentFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegistrationAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationAttachmentsRequestRequestTypeDef",
    {
        "RegistrationAttachmentIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[RegistrationAttachmentFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeRegistrationAttachmentsResultTypeDef = TypedDict(
    "DescribeRegistrationAttachmentsResultTypeDef",
    {
        "RegistrationAttachments": List[RegistrationAttachmentsInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeRegistrationFieldValuesResultTypeDef = TypedDict(
    "DescribeRegistrationFieldValuesResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "RegistrationFieldValues": List[RegistrationFieldValueInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeRegistrationTypeDefinitionsRequestDescribeRegistrationTypeDefinitionsPaginateTypeDef = TypedDict(
    "DescribeRegistrationTypeDefinitionsRequestDescribeRegistrationTypeDefinitionsPaginateTypeDef",
    {
        "RegistrationTypes": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[RegistrationTypeFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegistrationTypeDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationTypeDefinitionsRequestRequestTypeDef",
    {
        "RegistrationTypes": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[RegistrationTypeFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeRegistrationVersionsRequestDescribeRegistrationVersionsPaginateTypeDef = TypedDict(
    "DescribeRegistrationVersionsRequestDescribeRegistrationVersionsPaginateTypeDef",
    {
        "RegistrationId": str,
        "VersionNumbers": NotRequired[Sequence[int]],
        "Filters": NotRequired[Sequence[RegistrationVersionFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegistrationVersionsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationVersionsRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "VersionNumbers": NotRequired[Sequence[int]],
        "Filters": NotRequired[Sequence[RegistrationVersionFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeRegistrationsRequestDescribeRegistrationsPaginateTypeDef = TypedDict(
    "DescribeRegistrationsRequestDescribeRegistrationsPaginateTypeDef",
    {
        "RegistrationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[RegistrationFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegistrationsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationsRequestRequestTypeDef",
    {
        "RegistrationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[RegistrationFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeRegistrationsResultTypeDef = TypedDict(
    "DescribeRegistrationsResultTypeDef",
    {
        "Registrations": List[RegistrationInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeSenderIdsRequestDescribeSenderIdsPaginateTypeDef = TypedDict(
    "DescribeSenderIdsRequestDescribeSenderIdsPaginateTypeDef",
    {
        "SenderIds": NotRequired[Sequence[SenderIdAndCountryTypeDef]],
        "Filters": NotRequired[Sequence[SenderIdFilterTypeDef]],
        "Owner": NotRequired[OwnerType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSenderIdsRequestRequestTypeDef = TypedDict(
    "DescribeSenderIdsRequestRequestTypeDef",
    {
        "SenderIds": NotRequired[Sequence[SenderIdAndCountryTypeDef]],
        "Filters": NotRequired[Sequence[SenderIdFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Owner": NotRequired[OwnerType],
    },
)
DescribeSenderIdsResultTypeDef = TypedDict(
    "DescribeSenderIdsResultTypeDef",
    {
        "SenderIds": List[SenderIdInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeSpendLimitsResultTypeDef = TypedDict(
    "DescribeSpendLimitsResultTypeDef",
    {
        "SpendLimits": List[SpendLimitTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeVerifiedDestinationNumbersRequestDescribeVerifiedDestinationNumbersPaginateTypeDef = TypedDict(
    "DescribeVerifiedDestinationNumbersRequestDescribeVerifiedDestinationNumbersPaginateTypeDef",
    {
        "VerifiedDestinationNumberIds": NotRequired[Sequence[str]],
        "DestinationPhoneNumbers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[VerifiedDestinationNumberFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVerifiedDestinationNumbersRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedDestinationNumbersRequestRequestTypeDef",
    {
        "VerifiedDestinationNumberIds": NotRequired[Sequence[str]],
        "DestinationPhoneNumbers": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[VerifiedDestinationNumberFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeVerifiedDestinationNumbersResultTypeDef = TypedDict(
    "DescribeVerifiedDestinationNumbersResultTypeDef",
    {
        "VerifiedDestinationNumbers": List[VerifiedDestinationNumberInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetProtectConfigurationCountryRuleSetResultTypeDef = TypedDict(
    "GetProtectConfigurationCountryRuleSetResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "NumberCapability": NumberCapabilityType,
        "CountryRuleSet": Dict[str, ProtectConfigurationCountryRuleSetInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProtectConfigurationCountryRuleSetRequestRequestTypeDef = TypedDict(
    "UpdateProtectConfigurationCountryRuleSetRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "NumberCapability": NumberCapabilityType,
        "CountryRuleSetUpdates": Mapping[str, ProtectConfigurationCountryRuleSetInformationTypeDef],
    },
)
UpdateProtectConfigurationCountryRuleSetResultTypeDef = TypedDict(
    "UpdateProtectConfigurationCountryRuleSetResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "NumberCapability": NumberCapabilityType,
        "CountryRuleSet": Dict[str, ProtectConfigurationCountryRuleSetInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPoolOriginationIdentitiesRequestListPoolOriginationIdentitiesPaginateTypeDef = TypedDict(
    "ListPoolOriginationIdentitiesRequestListPoolOriginationIdentitiesPaginateTypeDef",
    {
        "PoolId": str,
        "Filters": NotRequired[Sequence[PoolOriginationIdentitiesFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoolOriginationIdentitiesRequestRequestTypeDef = TypedDict(
    "ListPoolOriginationIdentitiesRequestRequestTypeDef",
    {
        "PoolId": str,
        "Filters": NotRequired[Sequence[PoolOriginationIdentitiesFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPoolOriginationIdentitiesResultTypeDef = TypedDict(
    "ListPoolOriginationIdentitiesResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentities": List[OriginationIdentityMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRegistrationAssociationsRequestListRegistrationAssociationsPaginateTypeDef = TypedDict(
    "ListRegistrationAssociationsRequestListRegistrationAssociationsPaginateTypeDef",
    {
        "RegistrationId": str,
        "Filters": NotRequired[Sequence[RegistrationAssociationFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegistrationAssociationsRequestRequestTypeDef = TypedDict(
    "ListRegistrationAssociationsRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "Filters": NotRequired[Sequence[RegistrationAssociationFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRegistrationAssociationsResultTypeDef = TypedDict(
    "ListRegistrationAssociationsResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "RegistrationAssociations": List[RegistrationAssociationMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RegistrationVersionInformationTypeDef = TypedDict(
    "RegistrationVersionInformationTypeDef",
    {
        "VersionNumber": int,
        "RegistrationVersionStatus": RegistrationVersionStatusType,
        "RegistrationVersionStatusHistory": RegistrationVersionStatusHistoryTypeDef,
        "DeniedReasons": NotRequired[List[RegistrationDeniedReasonInformationTypeDef]],
    },
)
RegistrationFieldDisplayHintsTypeDef = TypedDict(
    "RegistrationFieldDisplayHintsTypeDef",
    {
        "Title": str,
        "ShortDescription": str,
        "LongDescription": NotRequired[str],
        "DocumentationTitle": NotRequired[str],
        "DocumentationLink": NotRequired[str],
        "SelectOptionDescriptions": NotRequired[List[SelectOptionDescriptionTypeDef]],
        "TextValidationDescription": NotRequired[str],
        "ExampleTextValue": NotRequired[str],
    },
)
RegistrationSectionDefinitionTypeDef = TypedDict(
    "RegistrationSectionDefinitionTypeDef",
    {
        "SectionPath": str,
        "DisplayHints": RegistrationSectionDisplayHintsTypeDef,
    },
)
RegistrationTypeDefinitionTypeDef = TypedDict(
    "RegistrationTypeDefinitionTypeDef",
    {
        "RegistrationType": str,
        "DisplayHints": RegistrationTypeDisplayHintsTypeDef,
        "SupportedAssociations": NotRequired[List[SupportedAssociationTypeDef]],
    },
)
ConfigurationSetInformationTypeDef = TypedDict(
    "ConfigurationSetInformationTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestinations": List[EventDestinationTypeDef],
        "CreatedTimestamp": datetime,
        "DefaultMessageType": NotRequired[MessageTypeType],
        "DefaultSenderId": NotRequired[str],
        "ProtectConfigurationId": NotRequired[str],
    },
)
CreateEventDestinationResultTypeDef = TypedDict(
    "CreateEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": EventDestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteConfigurationSetResultTypeDef = TypedDict(
    "DeleteConfigurationSetResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestinations": List[EventDestinationTypeDef],
        "DefaultMessageType": MessageTypeType,
        "DefaultSenderId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEventDestinationResultTypeDef = TypedDict(
    "DeleteEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": EventDestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEventDestinationResultTypeDef = TypedDict(
    "UpdateEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": EventDestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRegistrationVersionsResultTypeDef = TypedDict(
    "DescribeRegistrationVersionsResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationVersions": List[RegistrationVersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RegistrationFieldDefinitionTypeDef = TypedDict(
    "RegistrationFieldDefinitionTypeDef",
    {
        "SectionPath": str,
        "FieldPath": str,
        "FieldType": FieldTypeType,
        "FieldRequirement": FieldRequirementType,
        "DisplayHints": RegistrationFieldDisplayHintsTypeDef,
        "SelectValidation": NotRequired[SelectValidationTypeDef],
        "TextValidation": NotRequired[TextValidationTypeDef],
    },
)
DescribeRegistrationSectionDefinitionsResultTypeDef = TypedDict(
    "DescribeRegistrationSectionDefinitionsResultTypeDef",
    {
        "RegistrationType": str,
        "RegistrationSectionDefinitions": List[RegistrationSectionDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeRegistrationTypeDefinitionsResultTypeDef = TypedDict(
    "DescribeRegistrationTypeDefinitionsResultTypeDef",
    {
        "RegistrationTypeDefinitions": List[RegistrationTypeDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeConfigurationSetsResultTypeDef = TypedDict(
    "DescribeConfigurationSetsResultTypeDef",
    {
        "ConfigurationSets": List[ConfigurationSetInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeRegistrationFieldDefinitionsResultTypeDef = TypedDict(
    "DescribeRegistrationFieldDefinitionsResultTypeDef",
    {
        "RegistrationType": str,
        "RegistrationFieldDefinitions": List[RegistrationFieldDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
