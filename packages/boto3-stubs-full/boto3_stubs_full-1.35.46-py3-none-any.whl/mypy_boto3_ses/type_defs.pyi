"""
Type annotations for ses service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/type_defs/)

Usage::

    ```python
    from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMXFailureType,
    BounceTypeType,
    BulkEmailStatusType,
    ConfigurationSetAttributeType,
    CustomMailFromStatusType,
    DimensionValueSourceType,
    DsnActionType,
    EventTypeType,
    IdentityTypeType,
    InvocationTypeType,
    NotificationTypeType,
    ReceiptFilterPolicyType,
    SNSActionEncodingType,
    TlsPolicyType,
    VerificationStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddHeaderActionTypeDef",
    "BlobTypeDef",
    "ContentTypeDef",
    "BounceActionTypeDef",
    "BulkEmailDestinationStatusTypeDef",
    "DestinationTypeDef",
    "MessageTagTypeDef",
    "CloneReceiptRuleSetRequestRequestTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ConfigurationSetTypeDef",
    "TrackingOptionsTypeDef",
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "CreateReceiptRuleSetRequestRequestTypeDef",
    "TemplateTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    "DeleteIdentityPolicyRequestRequestTypeDef",
    "DeleteIdentityRequestRequestTypeDef",
    "DeleteReceiptFilterRequestRequestTypeDef",
    "DeleteReceiptRuleRequestRequestTypeDef",
    "DeleteReceiptRuleSetRequestRequestTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DeleteVerifiedEmailAddressRequestRequestTypeDef",
    "DeliveryOptionsTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeConfigurationSetRequestRequestTypeDef",
    "ReputationOptionsTypeDef",
    "DescribeReceiptRuleRequestRequestTypeDef",
    "DescribeReceiptRuleSetRequestRequestTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "SNSDestinationTypeDef",
    "ExtensionFieldTypeDef",
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    "GetIdentityDkimAttributesRequestRequestTypeDef",
    "IdentityDkimAttributesTypeDef",
    "GetIdentityMailFromDomainAttributesRequestRequestTypeDef",
    "IdentityMailFromDomainAttributesTypeDef",
    "GetIdentityNotificationAttributesRequestRequestTypeDef",
    "IdentityNotificationAttributesTypeDef",
    "GetIdentityPoliciesRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetIdentityVerificationAttributesRequestRequestTypeDef",
    "IdentityVerificationAttributesTypeDef",
    "SendDataPointTypeDef",
    "GetTemplateRequestRequestTypeDef",
    "LambdaActionTypeDef",
    "PaginatorConfigTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    "ListIdentitiesRequestRequestTypeDef",
    "ListIdentityPoliciesRequestRequestTypeDef",
    "ListReceiptRuleSetsRequestRequestTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "TemplateMetadataTypeDef",
    "TimestampTypeDef",
    "PutIdentityPolicyRequestRequestTypeDef",
    "S3ActionTypeDef",
    "SNSActionTypeDef",
    "StopActionTypeDef",
    "WorkmailActionTypeDef",
    "ReceiptIpFilterTypeDef",
    "ReorderReceiptRuleSetRequestRequestTypeDef",
    "SendCustomVerificationEmailRequestRequestTypeDef",
    "SetActiveReceiptRuleSetRequestRequestTypeDef",
    "SetIdentityDkimEnabledRequestRequestTypeDef",
    "SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef",
    "SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef",
    "SetIdentityMailFromDomainRequestRequestTypeDef",
    "SetIdentityNotificationTopicRequestRequestTypeDef",
    "SetReceiptRulePositionRequestRequestTypeDef",
    "TestRenderTemplateRequestRequestTypeDef",
    "UpdateAccountSendingEnabledRequestRequestTypeDef",
    "UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef",
    "UpdateConfigurationSetSendingEnabledRequestRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "VerifyDomainDkimRequestRequestTypeDef",
    "VerifyDomainIdentityRequestRequestTypeDef",
    "VerifyEmailAddressRequestRequestTypeDef",
    "VerifyEmailIdentityRequestRequestTypeDef",
    "RawMessageTypeDef",
    "BodyTypeDef",
    "BulkEmailDestinationTypeDef",
    "SendTemplatedEmailRequestRequestTypeDef",
    "CloudWatchDestinationOutputTypeDef",
    "CloudWatchDestinationTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAccountSendingEnabledResponseTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetIdentityPoliciesResponseTypeDef",
    "GetSendQuotaResponseTypeDef",
    "GetTemplateResponseTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoliciesResponseTypeDef",
    "ListReceiptRuleSetsResponseTypeDef",
    "ListVerifiedEmailAddressesResponseTypeDef",
    "SendBounceResponseTypeDef",
    "SendBulkTemplatedEmailResponseTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendEmailResponseTypeDef",
    "SendRawEmailResponseTypeDef",
    "SendTemplatedEmailResponseTypeDef",
    "TestRenderTemplateResponseTypeDef",
    "VerifyDomainDkimResponseTypeDef",
    "VerifyDomainIdentityResponseTypeDef",
    "GetIdentityDkimAttributesResponseTypeDef",
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    "GetIdentityNotificationAttributesResponseTypeDef",
    "GetIdentityVerificationAttributesRequestIdentityExistsWaitTypeDef",
    "GetIdentityVerificationAttributesResponseTypeDef",
    "GetSendStatisticsResponseTypeDef",
    "ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef",
    "ListCustomVerificationEmailTemplatesRequestListCustomVerificationEmailTemplatesPaginateTypeDef",
    "ListIdentitiesRequestListIdentitiesPaginateTypeDef",
    "ListReceiptRuleSetsRequestListReceiptRuleSetsPaginateTypeDef",
    "ListTemplatesRequestListTemplatesPaginateTypeDef",
    "ListTemplatesResponseTypeDef",
    "MessageDsnTypeDef",
    "RecipientDsnFieldsTypeDef",
    "ReceiptActionTypeDef",
    "ReceiptFilterTypeDef",
    "SendRawEmailRequestRequestTypeDef",
    "MessageTypeDef",
    "SendBulkTemplatedEmailRequestRequestTypeDef",
    "EventDestinationOutputTypeDef",
    "CloudWatchDestinationUnionTypeDef",
    "BouncedRecipientInfoTypeDef",
    "ReceiptRuleOutputTypeDef",
    "ReceiptRuleTypeDef",
    "CreateReceiptFilterRequestRequestTypeDef",
    "ListReceiptFiltersResponseTypeDef",
    "SendEmailRequestRequestTypeDef",
    "DescribeConfigurationSetResponseTypeDef",
    "EventDestinationTypeDef",
    "SendBounceRequestRequestTypeDef",
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    "DescribeReceiptRuleResponseTypeDef",
    "DescribeReceiptRuleSetResponseTypeDef",
    "CreateReceiptRuleRequestRequestTypeDef",
    "UpdateReceiptRuleRequestRequestTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
)

AddHeaderActionTypeDef = TypedDict(
    "AddHeaderActionTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ContentTypeDef = TypedDict(
    "ContentTypeDef",
    {
        "Data": str,
        "Charset": NotRequired[str],
    },
)
BounceActionTypeDef = TypedDict(
    "BounceActionTypeDef",
    {
        "SmtpReplyCode": str,
        "Message": str,
        "Sender": str,
        "TopicArn": NotRequired[str],
        "StatusCode": NotRequired[str],
    },
)
BulkEmailDestinationStatusTypeDef = TypedDict(
    "BulkEmailDestinationStatusTypeDef",
    {
        "Status": NotRequired[BulkEmailStatusType],
        "Error": NotRequired[str],
        "MessageId": NotRequired[str],
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "ToAddresses": NotRequired[Sequence[str]],
        "CcAddresses": NotRequired[Sequence[str]],
        "BccAddresses": NotRequired[Sequence[str]],
    },
)
MessageTagTypeDef = TypedDict(
    "MessageTagTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
CloneReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "CloneReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "OriginalRuleSetName": str,
    },
)
CloudWatchDimensionConfigurationTypeDef = TypedDict(
    "CloudWatchDimensionConfigurationTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": DimensionValueSourceType,
        "DefaultDimensionValue": str,
    },
)
ConfigurationSetTypeDef = TypedDict(
    "ConfigurationSetTypeDef",
    {
        "Name": str,
    },
)
TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": NotRequired[str],
    },
)
CreateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
)
CreateReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "CreateReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)
TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "TemplateName": str,
        "SubjectPart": NotRequired[str],
        "TextPart": NotRequired[str],
        "HtmlPart": NotRequired[str],
    },
)
CustomVerificationEmailTemplateTypeDef = TypedDict(
    "CustomVerificationEmailTemplateTypeDef",
    {
        "TemplateName": NotRequired[str],
        "FromEmailAddress": NotRequired[str],
        "TemplateSubject": NotRequired[str],
        "SuccessRedirectionURL": NotRequired[str],
        "FailureRedirectionURL": NotRequired[str],
    },
)
DeleteConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)
DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
DeleteCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
DeleteIdentityPolicyRequestRequestTypeDef = TypedDict(
    "DeleteIdentityPolicyRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyName": str,
    },
)
DeleteIdentityRequestRequestTypeDef = TypedDict(
    "DeleteIdentityRequestRequestTypeDef",
    {
        "Identity": str,
    },
)
DeleteReceiptFilterRequestRequestTypeDef = TypedDict(
    "DeleteReceiptFilterRequestRequestTypeDef",
    {
        "FilterName": str,
    },
)
DeleteReceiptRuleRequestRequestTypeDef = TypedDict(
    "DeleteReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)
DeleteReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "DeleteReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)
DeleteTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
DeleteVerifiedEmailAddressRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedEmailAddressRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)
DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": NotRequired[TlsPolicyType],
    },
)
ReceiptRuleSetMetadataTypeDef = TypedDict(
    "ReceiptRuleSetMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
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
DescribeConfigurationSetRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "ConfigurationSetAttributeNames": NotRequired[Sequence[ConfigurationSetAttributeType]],
    },
)
ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
        "ReputationMetricsEnabled": NotRequired[bool],
        "LastFreshStart": NotRequired[datetime],
    },
)
DescribeReceiptRuleRequestRequestTypeDef = TypedDict(
    "DescribeReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)
DescribeReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "DescribeReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)
KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IAMRoleARN": str,
        "DeliveryStreamARN": str,
    },
)
SNSDestinationTypeDef = TypedDict(
    "SNSDestinationTypeDef",
    {
        "TopicARN": str,
    },
)
ExtensionFieldTypeDef = TypedDict(
    "ExtensionFieldTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
GetCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
GetIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityDkimAttributesRequestRequestTypeDef",
    {
        "Identities": Sequence[str],
    },
)
IdentityDkimAttributesTypeDef = TypedDict(
    "IdentityDkimAttributesTypeDef",
    {
        "DkimEnabled": bool,
        "DkimVerificationStatus": VerificationStatusType,
        "DkimTokens": NotRequired[List[str]],
    },
)
GetIdentityMailFromDomainAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesRequestRequestTypeDef",
    {
        "Identities": Sequence[str],
    },
)
IdentityMailFromDomainAttributesTypeDef = TypedDict(
    "IdentityMailFromDomainAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": CustomMailFromStatusType,
        "BehaviorOnMXFailure": BehaviorOnMXFailureType,
    },
)
GetIdentityNotificationAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityNotificationAttributesRequestRequestTypeDef",
    {
        "Identities": Sequence[str],
    },
)
IdentityNotificationAttributesTypeDef = TypedDict(
    "IdentityNotificationAttributesTypeDef",
    {
        "BounceTopic": str,
        "ComplaintTopic": str,
        "DeliveryTopic": str,
        "ForwardingEnabled": bool,
        "HeadersInBounceNotificationsEnabled": NotRequired[bool],
        "HeadersInComplaintNotificationsEnabled": NotRequired[bool],
        "HeadersInDeliveryNotificationsEnabled": NotRequired[bool],
    },
)
GetIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "GetIdentityPoliciesRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyNames": Sequence[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetIdentityVerificationAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityVerificationAttributesRequestRequestTypeDef",
    {
        "Identities": Sequence[str],
    },
)
IdentityVerificationAttributesTypeDef = TypedDict(
    "IdentityVerificationAttributesTypeDef",
    {
        "VerificationStatus": VerificationStatusType,
        "VerificationToken": NotRequired[str],
    },
)
SendDataPointTypeDef = TypedDict(
    "SendDataPointTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "DeliveryAttempts": NotRequired[int],
        "Bounces": NotRequired[int],
        "Complaints": NotRequired[int],
        "Rejects": NotRequired[int],
    },
)
GetTemplateRequestRequestTypeDef = TypedDict(
    "GetTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
LambdaActionTypeDef = TypedDict(
    "LambdaActionTypeDef",
    {
        "FunctionArn": str,
        "TopicArn": NotRequired[str],
        "InvocationType": NotRequired[InvocationTypeType],
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
ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListCustomVerificationEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIdentitiesRequestRequestTypeDef = TypedDict(
    "ListIdentitiesRequestRequestTypeDef",
    {
        "IdentityType": NotRequired[IdentityTypeType],
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "ListIdentityPoliciesRequestRequestTypeDef",
    {
        "Identity": str,
    },
)
ListReceiptRuleSetsRequestRequestTypeDef = TypedDict(
    "ListReceiptRuleSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
TemplateMetadataTypeDef = TypedDict(
    "TemplateMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]
PutIdentityPolicyRequestRequestTypeDef = TypedDict(
    "PutIdentityPolicyRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyName": str,
        "Policy": str,
    },
)
S3ActionTypeDef = TypedDict(
    "S3ActionTypeDef",
    {
        "BucketName": str,
        "TopicArn": NotRequired[str],
        "ObjectKeyPrefix": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)
SNSActionTypeDef = TypedDict(
    "SNSActionTypeDef",
    {
        "TopicArn": str,
        "Encoding": NotRequired[SNSActionEncodingType],
    },
)
StopActionTypeDef = TypedDict(
    "StopActionTypeDef",
    {
        "Scope": Literal["RuleSet"],
        "TopicArn": NotRequired[str],
    },
)
WorkmailActionTypeDef = TypedDict(
    "WorkmailActionTypeDef",
    {
        "OrganizationArn": str,
        "TopicArn": NotRequired[str],
    },
)
ReceiptIpFilterTypeDef = TypedDict(
    "ReceiptIpFilterTypeDef",
    {
        "Policy": ReceiptFilterPolicyType,
        "Cidr": str,
    },
)
ReorderReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "ReorderReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleNames": Sequence[str],
    },
)
SendCustomVerificationEmailRequestRequestTypeDef = TypedDict(
    "SendCustomVerificationEmailRequestRequestTypeDef",
    {
        "EmailAddress": str,
        "TemplateName": str,
        "ConfigurationSetName": NotRequired[str],
    },
)
SetActiveReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "SetActiveReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": NotRequired[str],
    },
)
SetIdentityDkimEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityDkimEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "DkimEnabled": bool,
    },
)
SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "ForwardingEnabled": bool,
    },
)
SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "NotificationType": NotificationTypeType,
        "Enabled": bool,
    },
)
SetIdentityMailFromDomainRequestRequestTypeDef = TypedDict(
    "SetIdentityMailFromDomainRequestRequestTypeDef",
    {
        "Identity": str,
        "MailFromDomain": NotRequired[str],
        "BehaviorOnMXFailure": NotRequired[BehaviorOnMXFailureType],
    },
)
SetIdentityNotificationTopicRequestRequestTypeDef = TypedDict(
    "SetIdentityNotificationTopicRequestRequestTypeDef",
    {
        "Identity": str,
        "NotificationType": NotificationTypeType,
        "SnsTopic": NotRequired[str],
    },
)
SetReceiptRulePositionRequestRequestTypeDef = TypedDict(
    "SetReceiptRulePositionRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
        "After": NotRequired[str],
    },
)
TestRenderTemplateRequestRequestTypeDef = TypedDict(
    "TestRenderTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateData": str,
    },
)
UpdateAccountSendingEnabledRequestRequestTypeDef = TypedDict(
    "UpdateAccountSendingEnabledRequestRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Enabled": bool,
    },
)
UpdateConfigurationSetSendingEnabledRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetSendingEnabledRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Enabled": bool,
    },
)
UpdateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": NotRequired[str],
        "TemplateSubject": NotRequired[str],
        "TemplateContent": NotRequired[str],
        "SuccessRedirectionURL": NotRequired[str],
        "FailureRedirectionURL": NotRequired[str],
    },
)
VerifyDomainDkimRequestRequestTypeDef = TypedDict(
    "VerifyDomainDkimRequestRequestTypeDef",
    {
        "Domain": str,
    },
)
VerifyDomainIdentityRequestRequestTypeDef = TypedDict(
    "VerifyDomainIdentityRequestRequestTypeDef",
    {
        "Domain": str,
    },
)
VerifyEmailAddressRequestRequestTypeDef = TypedDict(
    "VerifyEmailAddressRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)
VerifyEmailIdentityRequestRequestTypeDef = TypedDict(
    "VerifyEmailIdentityRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)
RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": BlobTypeDef,
    },
)
BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": NotRequired[ContentTypeDef],
        "Html": NotRequired[ContentTypeDef],
    },
)
BulkEmailDestinationTypeDef = TypedDict(
    "BulkEmailDestinationTypeDef",
    {
        "Destination": DestinationTypeDef,
        "ReplacementTags": NotRequired[Sequence[MessageTagTypeDef]],
        "ReplacementTemplateData": NotRequired[str],
    },
)
SendTemplatedEmailRequestRequestTypeDef = TypedDict(
    "SendTemplatedEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": DestinationTypeDef,
        "Template": str,
        "TemplateData": str,
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "ReturnPath": NotRequired[str],
        "SourceArn": NotRequired[str],
        "ReturnPathArn": NotRequired[str],
        "Tags": NotRequired[Sequence[MessageTagTypeDef]],
        "ConfigurationSetName": NotRequired[str],
        "TemplateArn": NotRequired[str],
    },
)
CloudWatchDestinationOutputTypeDef = TypedDict(
    "CloudWatchDestinationOutputTypeDef",
    {
        "DimensionConfigurations": List[CloudWatchDimensionConfigurationTypeDef],
    },
)
CloudWatchDestinationTypeDef = TypedDict(
    "CloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": Sequence[CloudWatchDimensionConfigurationTypeDef],
    },
)
CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSet": ConfigurationSetTypeDef,
    },
)
CreateConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": TrackingOptionsTypeDef,
    },
)
UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": TrackingOptionsTypeDef,
    },
)
CreateTemplateRequestRequestTypeDef = TypedDict(
    "CreateTemplateRequestRequestTypeDef",
    {
        "Template": TemplateTypeDef,
    },
)
UpdateTemplateRequestRequestTypeDef = TypedDict(
    "UpdateTemplateRequestRequestTypeDef",
    {
        "Template": TemplateTypeDef,
    },
)
PutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "DeliveryOptions": NotRequired[DeliveryOptionsTypeDef],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountSendingEnabledResponseTypeDef = TypedDict(
    "GetAccountSendingEnabledResponseTypeDef",
    {
        "Enabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCustomVerificationEmailTemplateResponseTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdentityPoliciesResponseTypeDef = TypedDict(
    "GetIdentityPoliciesResponseTypeDef",
    {
        "Policies": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSendQuotaResponseTypeDef = TypedDict(
    "GetSendQuotaResponseTypeDef",
    {
        "Max24HourSend": float,
        "MaxSendRate": float,
        "SentLast24Hours": float,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "Template": TemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[ConfigurationSetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List[CustomVerificationEmailTemplateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIdentitiesResponseTypeDef = TypedDict(
    "ListIdentitiesResponseTypeDef",
    {
        "Identities": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIdentityPoliciesResponseTypeDef = TypedDict(
    "ListIdentityPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReceiptRuleSetsResponseTypeDef = TypedDict(
    "ListReceiptRuleSetsResponseTypeDef",
    {
        "RuleSets": List[ReceiptRuleSetMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListVerifiedEmailAddressesResponseTypeDef = TypedDict(
    "ListVerifiedEmailAddressesResponseTypeDef",
    {
        "VerifiedEmailAddresses": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendBounceResponseTypeDef = TypedDict(
    "SendBounceResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendBulkTemplatedEmailResponseTypeDef = TypedDict(
    "SendBulkTemplatedEmailResponseTypeDef",
    {
        "Status": List[BulkEmailDestinationStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendCustomVerificationEmailResponseTypeDef = TypedDict(
    "SendCustomVerificationEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendEmailResponseTypeDef = TypedDict(
    "SendEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendRawEmailResponseTypeDef = TypedDict(
    "SendRawEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendTemplatedEmailResponseTypeDef = TypedDict(
    "SendTemplatedEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestRenderTemplateResponseTypeDef = TypedDict(
    "TestRenderTemplateResponseTypeDef",
    {
        "RenderedTemplate": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyDomainDkimResponseTypeDef = TypedDict(
    "VerifyDomainDkimResponseTypeDef",
    {
        "DkimTokens": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyDomainIdentityResponseTypeDef = TypedDict(
    "VerifyDomainIdentityResponseTypeDef",
    {
        "VerificationToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdentityDkimAttributesResponseTypeDef = TypedDict(
    "GetIdentityDkimAttributesResponseTypeDef",
    {
        "DkimAttributes": Dict[str, IdentityDkimAttributesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdentityMailFromDomainAttributesResponseTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    {
        "MailFromDomainAttributes": Dict[str, IdentityMailFromDomainAttributesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdentityNotificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityNotificationAttributesResponseTypeDef",
    {
        "NotificationAttributes": Dict[str, IdentityNotificationAttributesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdentityVerificationAttributesRequestIdentityExistsWaitTypeDef = TypedDict(
    "GetIdentityVerificationAttributesRequestIdentityExistsWaitTypeDef",
    {
        "Identities": Sequence[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetIdentityVerificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityVerificationAttributesResponseTypeDef",
    {
        "VerificationAttributes": Dict[str, IdentityVerificationAttributesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSendStatisticsResponseTypeDef = TypedDict(
    "GetSendStatisticsResponseTypeDef",
    {
        "SendDataPoints": List[SendDataPointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef = TypedDict(
    "ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomVerificationEmailTemplatesRequestListCustomVerificationEmailTemplatesPaginateTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestListCustomVerificationEmailTemplatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIdentitiesRequestListIdentitiesPaginateTypeDef = TypedDict(
    "ListIdentitiesRequestListIdentitiesPaginateTypeDef",
    {
        "IdentityType": NotRequired[IdentityTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReceiptRuleSetsRequestListReceiptRuleSetsPaginateTypeDef = TypedDict(
    "ListReceiptRuleSetsRequestListReceiptRuleSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplatesRequestListTemplatesPaginateTypeDef = TypedDict(
    "ListTemplatesRequestListTemplatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List[TemplateMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MessageDsnTypeDef = TypedDict(
    "MessageDsnTypeDef",
    {
        "ReportingMta": str,
        "ArrivalDate": NotRequired[TimestampTypeDef],
        "ExtensionFields": NotRequired[Sequence[ExtensionFieldTypeDef]],
    },
)
RecipientDsnFieldsTypeDef = TypedDict(
    "RecipientDsnFieldsTypeDef",
    {
        "Action": DsnActionType,
        "Status": str,
        "FinalRecipient": NotRequired[str],
        "RemoteMta": NotRequired[str],
        "DiagnosticCode": NotRequired[str],
        "LastAttemptDate": NotRequired[TimestampTypeDef],
        "ExtensionFields": NotRequired[Sequence[ExtensionFieldTypeDef]],
    },
)
ReceiptActionTypeDef = TypedDict(
    "ReceiptActionTypeDef",
    {
        "S3Action": NotRequired[S3ActionTypeDef],
        "BounceAction": NotRequired[BounceActionTypeDef],
        "WorkmailAction": NotRequired[WorkmailActionTypeDef],
        "LambdaAction": NotRequired[LambdaActionTypeDef],
        "StopAction": NotRequired[StopActionTypeDef],
        "AddHeaderAction": NotRequired[AddHeaderActionTypeDef],
        "SNSAction": NotRequired[SNSActionTypeDef],
    },
)
ReceiptFilterTypeDef = TypedDict(
    "ReceiptFilterTypeDef",
    {
        "Name": str,
        "IpFilter": ReceiptIpFilterTypeDef,
    },
)
SendRawEmailRequestRequestTypeDef = TypedDict(
    "SendRawEmailRequestRequestTypeDef",
    {
        "RawMessage": RawMessageTypeDef,
        "Source": NotRequired[str],
        "Destinations": NotRequired[Sequence[str]],
        "FromArn": NotRequired[str],
        "SourceArn": NotRequired[str],
        "ReturnPathArn": NotRequired[str],
        "Tags": NotRequired[Sequence[MessageTagTypeDef]],
        "ConfigurationSetName": NotRequired[str],
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Subject": ContentTypeDef,
        "Body": BodyTypeDef,
    },
)
SendBulkTemplatedEmailRequestRequestTypeDef = TypedDict(
    "SendBulkTemplatedEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Template": str,
        "DefaultTemplateData": str,
        "Destinations": Sequence[BulkEmailDestinationTypeDef],
        "SourceArn": NotRequired[str],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "ReturnPath": NotRequired[str],
        "ReturnPathArn": NotRequired[str],
        "ConfigurationSetName": NotRequired[str],
        "DefaultTags": NotRequired[Sequence[MessageTagTypeDef]],
        "TemplateArn": NotRequired[str],
    },
)
EventDestinationOutputTypeDef = TypedDict(
    "EventDestinationOutputTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": List[EventTypeType],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "CloudWatchDestination": NotRequired[CloudWatchDestinationOutputTypeDef],
        "SNSDestination": NotRequired[SNSDestinationTypeDef],
    },
)
CloudWatchDestinationUnionTypeDef = Union[
    CloudWatchDestinationTypeDef, CloudWatchDestinationOutputTypeDef
]
BouncedRecipientInfoTypeDef = TypedDict(
    "BouncedRecipientInfoTypeDef",
    {
        "Recipient": str,
        "RecipientArn": NotRequired[str],
        "BounceType": NotRequired[BounceTypeType],
        "RecipientDsnFields": NotRequired[RecipientDsnFieldsTypeDef],
    },
)
ReceiptRuleOutputTypeDef = TypedDict(
    "ReceiptRuleOutputTypeDef",
    {
        "Name": str,
        "Enabled": NotRequired[bool],
        "TlsPolicy": NotRequired[TlsPolicyType],
        "Recipients": NotRequired[List[str]],
        "Actions": NotRequired[List[ReceiptActionTypeDef]],
        "ScanEnabled": NotRequired[bool],
    },
)
ReceiptRuleTypeDef = TypedDict(
    "ReceiptRuleTypeDef",
    {
        "Name": str,
        "Enabled": NotRequired[bool],
        "TlsPolicy": NotRequired[TlsPolicyType],
        "Recipients": NotRequired[Sequence[str]],
        "Actions": NotRequired[Sequence[ReceiptActionTypeDef]],
        "ScanEnabled": NotRequired[bool],
    },
)
CreateReceiptFilterRequestRequestTypeDef = TypedDict(
    "CreateReceiptFilterRequestRequestTypeDef",
    {
        "Filter": ReceiptFilterTypeDef,
    },
)
ListReceiptFiltersResponseTypeDef = TypedDict(
    "ListReceiptFiltersResponseTypeDef",
    {
        "Filters": List[ReceiptFilterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendEmailRequestRequestTypeDef = TypedDict(
    "SendEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": DestinationTypeDef,
        "Message": MessageTypeDef,
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "ReturnPath": NotRequired[str],
        "SourceArn": NotRequired[str],
        "ReturnPathArn": NotRequired[str],
        "Tags": NotRequired[Sequence[MessageTagTypeDef]],
        "ConfigurationSetName": NotRequired[str],
    },
)
DescribeConfigurationSetResponseTypeDef = TypedDict(
    "DescribeConfigurationSetResponseTypeDef",
    {
        "ConfigurationSet": ConfigurationSetTypeDef,
        "EventDestinations": List[EventDestinationOutputTypeDef],
        "TrackingOptions": TrackingOptionsTypeDef,
        "DeliveryOptions": DeliveryOptionsTypeDef,
        "ReputationOptions": ReputationOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": Sequence[EventTypeType],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "CloudWatchDestination": NotRequired[CloudWatchDestinationUnionTypeDef],
        "SNSDestination": NotRequired[SNSDestinationTypeDef],
    },
)
SendBounceRequestRequestTypeDef = TypedDict(
    "SendBounceRequestRequestTypeDef",
    {
        "OriginalMessageId": str,
        "BounceSender": str,
        "BouncedRecipientInfoList": Sequence[BouncedRecipientInfoTypeDef],
        "Explanation": NotRequired[str],
        "MessageDsn": NotRequired[MessageDsnTypeDef],
        "BounceSenderArn": NotRequired[str],
    },
)
DescribeActiveReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    {
        "Metadata": ReceiptRuleSetMetadataTypeDef,
        "Rules": List[ReceiptRuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReceiptRuleResponseTypeDef = TypedDict(
    "DescribeReceiptRuleResponseTypeDef",
    {
        "Rule": ReceiptRuleOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeReceiptRuleSetResponseTypeDef",
    {
        "Metadata": ReceiptRuleSetMetadataTypeDef,
        "Rules": List[ReceiptRuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReceiptRuleRequestRequestTypeDef = TypedDict(
    "CreateReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rule": ReceiptRuleTypeDef,
        "After": NotRequired[str],
    },
)
UpdateReceiptRuleRequestRequestTypeDef = TypedDict(
    "UpdateReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rule": ReceiptRuleTypeDef,
    },
)
CreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": EventDestinationTypeDef,
    },
)
UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": EventDestinationTypeDef,
    },
)
