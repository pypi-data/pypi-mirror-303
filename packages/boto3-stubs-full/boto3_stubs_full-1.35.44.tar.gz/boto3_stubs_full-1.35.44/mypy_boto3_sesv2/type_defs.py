"""
Type annotations for sesv2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/type_defs/)

Usage::

    ```python
    from mypy_boto3_sesv2.type_defs import ReviewDetailsTypeDef

    data: ReviewDetailsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMxFailureType,
    BounceTypeType,
    BulkEmailStatusType,
    ContactLanguageType,
    ContactListImportActionType,
    DataFormatType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DeliveryEventTypeType,
    DimensionValueSourceType,
    DkimSigningAttributesOriginType,
    DkimSigningKeyLengthType,
    DkimStatusType,
    EngagementEventTypeType,
    EventTypeType,
    ExportSourceTypeType,
    FeatureStatusType,
    HttpsPolicyType,
    IdentityTypeType,
    ImportDestinationTypeType,
    JobStatusType,
    ListRecommendationsFilterKeyType,
    MailFromDomainStatusType,
    MailTypeType,
    MetricAggregationType,
    MetricDimensionNameType,
    MetricType,
    QueryErrorCodeType,
    RecommendationImpactType,
    RecommendationStatusType,
    RecommendationTypeType,
    ReviewStatusType,
    ScalingModeType,
    SubscriptionStatusType,
    SuppressionListImportActionType,
    SuppressionListReasonType,
    TlsPolicyType,
    VerificationErrorType,
    VerificationStatusType,
    WarmupStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ReviewDetailsTypeDef",
    "TimestampTypeDef",
    "MetricDataErrorTypeDef",
    "MetricDataResultTypeDef",
    "ResponseMetadataTypeDef",
    "BlacklistEntryTypeDef",
    "BlobTypeDef",
    "ContentTypeDef",
    "BounceTypeDef",
    "BulkEmailEntryResultTypeDef",
    "DestinationTypeDef",
    "MessageHeaderTypeDef",
    "MessageTagTypeDef",
    "CancelExportJobRequestRequestTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ComplaintTypeDef",
    "ContactListDestinationTypeDef",
    "ContactListTypeDef",
    "TopicPreferenceTypeDef",
    "DeliveryOptionsTypeDef",
    "SendingOptionsTypeDef",
    "SuppressionOptionsTypeDef",
    "TagTypeDef",
    "TrackingOptionsTypeDef",
    "TopicTypeDef",
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "CreateEmailIdentityPolicyRequestRequestTypeDef",
    "DkimSigningAttributesTypeDef",
    "DkimAttributesTypeDef",
    "EmailTemplateContentTypeDef",
    "ExportDestinationTypeDef",
    "ImportDataSourceTypeDef",
    "CustomVerificationEmailTemplateMetadataTypeDef",
    "DomainIspPlacementTypeDef",
    "VolumeStatisticsTypeDef",
    "DashboardAttributesTypeDef",
    "DashboardOptionsTypeDef",
    "DedicatedIpPoolTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteContactListRequestRequestTypeDef",
    "DeleteContactRequestRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    "DeleteEmailIdentityPolicyRequestRequestTypeDef",
    "DeleteEmailIdentityRequestRequestTypeDef",
    "DeleteEmailTemplateRequestRequestTypeDef",
    "DeleteSuppressedDestinationRequestRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "InboxPlacementTrackingOptionOutputTypeDef",
    "EmailTemplateMetadataTypeDef",
    "EventBridgeDestinationTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "PinpointDestinationTypeDef",
    "SnsDestinationTypeDef",
    "ExportJobSummaryTypeDef",
    "ExportMetricTypeDef",
    "ExportStatisticsTypeDef",
    "FailureInfoTypeDef",
    "SendQuotaTypeDef",
    "SuppressionAttributesTypeDef",
    "GetBlacklistReportsRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "GetConfigurationSetRequestRequestTypeDef",
    "ReputationOptionsOutputTypeDef",
    "SuppressionOptionsOutputTypeDef",
    "GetContactListRequestRequestTypeDef",
    "GetContactRequestRequestTypeDef",
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    "GetDedicatedIpPoolRequestRequestTypeDef",
    "GetDedicatedIpRequestRequestTypeDef",
    "GetDedicatedIpsRequestRequestTypeDef",
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    "PlacementStatisticsTypeDef",
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    "GetEmailIdentityPoliciesRequestRequestTypeDef",
    "GetEmailIdentityRequestRequestTypeDef",
    "MailFromAttributesTypeDef",
    "GetEmailTemplateRequestRequestTypeDef",
    "GetExportJobRequestRequestTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetMessageInsightsRequestRequestTypeDef",
    "GetSuppressedDestinationRequestRequestTypeDef",
    "GuardianAttributesTypeDef",
    "GuardianOptionsTypeDef",
    "IdentityInfoTypeDef",
    "SuppressionListDestinationTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListContactListsRequestRequestTypeDef",
    "TopicFilterTypeDef",
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    "ListEmailIdentitiesRequestRequestTypeDef",
    "ListEmailTemplatesRequestRequestTypeDef",
    "ListExportJobsRequestRequestTypeDef",
    "ListImportJobsRequestRequestTypeDef",
    "ListManagementOptionsTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "RecommendationTypeDef",
    "SuppressedDestinationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MessageInsightsFiltersOutputTypeDef",
    "MessageInsightsFiltersTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutAccountDetailsRequestRequestTypeDef",
    "PutAccountSendingAttributesRequestRequestTypeDef",
    "PutAccountSuppressionAttributesRequestRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestRequestTypeDef",
    "PutConfigurationSetSuppressionOptionsRequestRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    "PutDedicatedIpPoolScalingAttributesRequestRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    "PutSuppressedDestinationRequestRequestTypeDef",
    "ReplacementTemplateTypeDef",
    "SOARecordTypeDef",
    "SendCustomVerificationEmailRequestRequestTypeDef",
    "SuppressedDestinationAttributesTypeDef",
    "TestRenderEmailTemplateRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "UpdateEmailIdentityPolicyRequestRequestTypeDef",
    "AccountDetailsTypeDef",
    "BatchGetMetricDataQueryTypeDef",
    "GetDomainStatisticsReportRequestRequestTypeDef",
    "ListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    "ListSuppressedDestinationsRequestRequestTypeDef",
    "ReputationOptionsTypeDef",
    "BatchGetMetricDataResponseTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "CreateExportJobResponseTypeDef",
    "CreateImportJobResponseTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetEmailIdentityPoliciesResponseTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendEmailResponseTypeDef",
    "TestRenderEmailTemplateResponseTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "RawMessageTypeDef",
    "BodyTypeDef",
    "SendBulkEmailResponseTypeDef",
    "TemplateTypeDef",
    "CloudWatchDestinationOutputTypeDef",
    "CloudWatchDestinationTypeDef",
    "EventDetailsTypeDef",
    "ListContactListsResponseTypeDef",
    "ContactTypeDef",
    "CreateContactRequestRequestTypeDef",
    "GetContactResponseTypeDef",
    "UpdateContactRequestRequestTypeDef",
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateContactListRequestRequestTypeDef",
    "GetContactListResponseTypeDef",
    "UpdateContactListRequestRequestTypeDef",
    "CreateEmailIdentityRequestRequestTypeDef",
    "PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "CreateEmailTemplateRequestRequestTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "UpdateEmailTemplateRequestRequestTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "DailyVolumeTypeDef",
    "OverallVolumeTypeDef",
    "GetDedicatedIpPoolResponseTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "DomainDeliverabilityTrackingOptionOutputTypeDef",
    "ListEmailTemplatesResponseTypeDef",
    "ListExportJobsResponseTypeDef",
    "MetricsDataSourceOutputTypeDef",
    "MetricsDataSourceTypeDef",
    "IspPlacementTypeDef",
    "VdmAttributesTypeDef",
    "VdmOptionsTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "ImportDestinationTypeDef",
    "InboxPlacementTrackingOptionUnionTypeDef",
    "ListContactsFilterTypeDef",
    "ListRecommendationsResponseTypeDef",
    "ListSuppressedDestinationsResponseTypeDef",
    "MessageInsightsDataSourceOutputTypeDef",
    "MessageInsightsFiltersUnionTypeDef",
    "ReplacementEmailContentTypeDef",
    "VerificationInfoTypeDef",
    "SuppressedDestinationTypeDef",
    "BatchGetMetricDataRequestRequestTypeDef",
    "MessageTypeDef",
    "BulkEmailContentTypeDef",
    "EventDestinationTypeDef",
    "CloudWatchDestinationUnionTypeDef",
    "InsightsEventTypeDef",
    "ListContactsResponseTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "MetricsDataSourceUnionTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "GetAccountResponseTypeDef",
    "PutAccountVdmAttributesRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "PutConfigurationSetVdmOptionsRequestRequestTypeDef",
    "CreateImportJobRequestRequestTypeDef",
    "GetImportJobResponseTypeDef",
    "ImportJobSummaryTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ExportDataSourceOutputTypeDef",
    "MessageInsightsDataSourceTypeDef",
    "BulkEmailEntryTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "GetSuppressedDestinationResponseTypeDef",
    "EmailContentTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EmailInsightsTypeDef",
    "ListImportJobsResponseTypeDef",
    "DomainDeliverabilityTrackingOptionUnionTypeDef",
    "GetExportJobResponseTypeDef",
    "MessageInsightsDataSourceUnionTypeDef",
    "SendBulkEmailRequestRequestTypeDef",
    "CreateDeliverabilityTestReportRequestRequestTypeDef",
    "SendEmailRequestRequestTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "GetMessageInsightsResponseTypeDef",
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
    "ExportDataSourceTypeDef",
    "CreateExportJobRequestRequestTypeDef",
)

ReviewDetailsTypeDef = TypedDict(
    "ReviewDetailsTypeDef",
    {
        "Status": NotRequired[ReviewStatusType],
        "CaseId": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
MetricDataErrorTypeDef = TypedDict(
    "MetricDataErrorTypeDef",
    {
        "Id": NotRequired[str],
        "Code": NotRequired[QueryErrorCodeType],
        "Message": NotRequired[str],
    },
)
MetricDataResultTypeDef = TypedDict(
    "MetricDataResultTypeDef",
    {
        "Id": NotRequired[str],
        "Timestamps": NotRequired[List[datetime]],
        "Values": NotRequired[List[int]],
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
BlacklistEntryTypeDef = TypedDict(
    "BlacklistEntryTypeDef",
    {
        "RblName": NotRequired[str],
        "ListingTime": NotRequired[datetime],
        "Description": NotRequired[str],
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
BounceTypeDef = TypedDict(
    "BounceTypeDef",
    {
        "BounceType": NotRequired[BounceTypeType],
        "BounceSubType": NotRequired[str],
        "DiagnosticCode": NotRequired[str],
    },
)
BulkEmailEntryResultTypeDef = TypedDict(
    "BulkEmailEntryResultTypeDef",
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
MessageHeaderTypeDef = TypedDict(
    "MessageHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
MessageTagTypeDef = TypedDict(
    "MessageTagTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
CancelExportJobRequestRequestTypeDef = TypedDict(
    "CancelExportJobRequestRequestTypeDef",
    {
        "JobId": str,
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
ComplaintTypeDef = TypedDict(
    "ComplaintTypeDef",
    {
        "ComplaintSubType": NotRequired[str],
        "ComplaintFeedbackType": NotRequired[str],
    },
)
ContactListDestinationTypeDef = TypedDict(
    "ContactListDestinationTypeDef",
    {
        "ContactListName": str,
        "ContactListImportAction": ContactListImportActionType,
    },
)
ContactListTypeDef = TypedDict(
    "ContactListTypeDef",
    {
        "ContactListName": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
TopicPreferenceTypeDef = TypedDict(
    "TopicPreferenceTypeDef",
    {
        "TopicName": str,
        "SubscriptionStatus": SubscriptionStatusType,
    },
)
DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": NotRequired[TlsPolicyType],
        "SendingPoolName": NotRequired[str],
        "MaxDeliverySeconds": NotRequired[int],
    },
)
SendingOptionsTypeDef = TypedDict(
    "SendingOptionsTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
    },
)
SuppressionOptionsTypeDef = TypedDict(
    "SuppressionOptionsTypeDef",
    {
        "SuppressedReasons": NotRequired[Sequence[SuppressionListReasonType]],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": str,
        "HttpsPolicy": NotRequired[HttpsPolicyType],
    },
)
TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "TopicName": str,
        "DisplayName": str,
        "DefaultSubscriptionStatus": SubscriptionStatusType,
        "Description": NotRequired[str],
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
CreateEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "CreateEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
        "Policy": str,
    },
)
DkimSigningAttributesTypeDef = TypedDict(
    "DkimSigningAttributesTypeDef",
    {
        "DomainSigningSelector": NotRequired[str],
        "DomainSigningPrivateKey": NotRequired[str],
        "NextSigningKeyLength": NotRequired[DkimSigningKeyLengthType],
    },
)
DkimAttributesTypeDef = TypedDict(
    "DkimAttributesTypeDef",
    {
        "SigningEnabled": NotRequired[bool],
        "Status": NotRequired[DkimStatusType],
        "Tokens": NotRequired[List[str]],
        "SigningAttributesOrigin": NotRequired[DkimSigningAttributesOriginType],
        "NextSigningKeyLength": NotRequired[DkimSigningKeyLengthType],
        "CurrentSigningKeyLength": NotRequired[DkimSigningKeyLengthType],
        "LastKeyGenerationTimestamp": NotRequired[datetime],
    },
)
EmailTemplateContentTypeDef = TypedDict(
    "EmailTemplateContentTypeDef",
    {
        "Subject": NotRequired[str],
        "Text": NotRequired[str],
        "Html": NotRequired[str],
    },
)
ExportDestinationTypeDef = TypedDict(
    "ExportDestinationTypeDef",
    {
        "DataFormat": DataFormatType,
        "S3Url": NotRequired[str],
    },
)
ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef",
    {
        "S3Url": str,
        "DataFormat": DataFormatType,
    },
)
CustomVerificationEmailTemplateMetadataTypeDef = TypedDict(
    "CustomVerificationEmailTemplateMetadataTypeDef",
    {
        "TemplateName": NotRequired[str],
        "FromEmailAddress": NotRequired[str],
        "TemplateSubject": NotRequired[str],
        "SuccessRedirectionURL": NotRequired[str],
        "FailureRedirectionURL": NotRequired[str],
    },
)
DomainIspPlacementTypeDef = TypedDict(
    "DomainIspPlacementTypeDef",
    {
        "IspName": NotRequired[str],
        "InboxRawCount": NotRequired[int],
        "SpamRawCount": NotRequired[int],
        "InboxPercentage": NotRequired[float],
        "SpamPercentage": NotRequired[float],
    },
)
VolumeStatisticsTypeDef = TypedDict(
    "VolumeStatisticsTypeDef",
    {
        "InboxRawCount": NotRequired[int],
        "SpamRawCount": NotRequired[int],
        "ProjectedInbox": NotRequired[int],
        "ProjectedSpam": NotRequired[int],
    },
)
DashboardAttributesTypeDef = TypedDict(
    "DashboardAttributesTypeDef",
    {
        "EngagementMetrics": NotRequired[FeatureStatusType],
    },
)
DashboardOptionsTypeDef = TypedDict(
    "DashboardOptionsTypeDef",
    {
        "EngagementMetrics": NotRequired[FeatureStatusType],
    },
)
DedicatedIpPoolTypeDef = TypedDict(
    "DedicatedIpPoolTypeDef",
    {
        "PoolName": str,
        "ScalingMode": ScalingModeType,
    },
)
DedicatedIpTypeDef = TypedDict(
    "DedicatedIpTypeDef",
    {
        "Ip": str,
        "WarmupStatus": WarmupStatusType,
        "WarmupPercentage": int,
        "PoolName": NotRequired[str],
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
DeleteContactListRequestRequestTypeDef = TypedDict(
    "DeleteContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)
DeleteContactRequestRequestTypeDef = TypedDict(
    "DeleteContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)
DeleteCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
DeleteDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)
DeleteEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
    },
)
DeleteEmailIdentityRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
DeleteEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
DeleteSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "DeleteSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)
DeliverabilityTestReportTypeDef = TypedDict(
    "DeliverabilityTestReportTypeDef",
    {
        "ReportId": NotRequired[str],
        "ReportName": NotRequired[str],
        "Subject": NotRequired[str],
        "FromEmailAddress": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "DeliverabilityTestStatus": NotRequired[DeliverabilityTestStatusType],
    },
)
DomainDeliverabilityCampaignTypeDef = TypedDict(
    "DomainDeliverabilityCampaignTypeDef",
    {
        "CampaignId": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "Subject": NotRequired[str],
        "FromAddress": NotRequired[str],
        "SendingIps": NotRequired[List[str]],
        "FirstSeenDateTime": NotRequired[datetime],
        "LastSeenDateTime": NotRequired[datetime],
        "InboxCount": NotRequired[int],
        "SpamCount": NotRequired[int],
        "ReadRate": NotRequired[float],
        "DeleteRate": NotRequired[float],
        "ReadDeleteRate": NotRequired[float],
        "ProjectedVolume": NotRequired[int],
        "Esps": NotRequired[List[str]],
    },
)
InboxPlacementTrackingOptionOutputTypeDef = TypedDict(
    "InboxPlacementTrackingOptionOutputTypeDef",
    {
        "Global": NotRequired[bool],
        "TrackedIsps": NotRequired[List[str]],
    },
)
EmailTemplateMetadataTypeDef = TypedDict(
    "EmailTemplateMetadataTypeDef",
    {
        "TemplateName": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)
EventBridgeDestinationTypeDef = TypedDict(
    "EventBridgeDestinationTypeDef",
    {
        "EventBusArn": str,
    },
)
KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)
PinpointDestinationTypeDef = TypedDict(
    "PinpointDestinationTypeDef",
    {
        "ApplicationArn": NotRequired[str],
    },
)
SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
)
ExportJobSummaryTypeDef = TypedDict(
    "ExportJobSummaryTypeDef",
    {
        "JobId": NotRequired[str],
        "ExportSourceType": NotRequired[ExportSourceTypeType],
        "JobStatus": NotRequired[JobStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "CompletedTimestamp": NotRequired[datetime],
    },
)
ExportMetricTypeDef = TypedDict(
    "ExportMetricTypeDef",
    {
        "Name": NotRequired[MetricType],
        "Aggregation": NotRequired[MetricAggregationType],
    },
)
ExportStatisticsTypeDef = TypedDict(
    "ExportStatisticsTypeDef",
    {
        "ProcessedRecordsCount": NotRequired[int],
        "ExportedRecordsCount": NotRequired[int],
    },
)
FailureInfoTypeDef = TypedDict(
    "FailureInfoTypeDef",
    {
        "FailedRecordsS3Url": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
SendQuotaTypeDef = TypedDict(
    "SendQuotaTypeDef",
    {
        "Max24HourSend": NotRequired[float],
        "MaxSendRate": NotRequired[float],
        "SentLast24Hours": NotRequired[float],
    },
)
SuppressionAttributesTypeDef = TypedDict(
    "SuppressionAttributesTypeDef",
    {
        "SuppressedReasons": NotRequired[List[SuppressionListReasonType]],
    },
)
GetBlacklistReportsRequestRequestTypeDef = TypedDict(
    "GetBlacklistReportsRequestRequestTypeDef",
    {
        "BlacklistItemNames": Sequence[str],
    },
)
GetConfigurationSetEventDestinationsRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
GetConfigurationSetRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
ReputationOptionsOutputTypeDef = TypedDict(
    "ReputationOptionsOutputTypeDef",
    {
        "ReputationMetricsEnabled": NotRequired[bool],
        "LastFreshStart": NotRequired[datetime],
    },
)
SuppressionOptionsOutputTypeDef = TypedDict(
    "SuppressionOptionsOutputTypeDef",
    {
        "SuppressedReasons": NotRequired[List[SuppressionListReasonType]],
    },
)
GetContactListRequestRequestTypeDef = TypedDict(
    "GetContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)
GetContactRequestRequestTypeDef = TypedDict(
    "GetContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)
GetCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
GetDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)
GetDedicatedIpRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpRequestRequestTypeDef",
    {
        "Ip": str,
    },
)
GetDedicatedIpsRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpsRequestRequestTypeDef",
    {
        "PoolName": NotRequired[str],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
GetDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    {
        "ReportId": str,
    },
)
PlacementStatisticsTypeDef = TypedDict(
    "PlacementStatisticsTypeDef",
    {
        "InboxPercentage": NotRequired[float],
        "SpamPercentage": NotRequired[float],
        "MissingPercentage": NotRequired[float],
        "SpfPercentage": NotRequired[float],
        "DkimPercentage": NotRequired[float],
    },
)
GetDomainDeliverabilityCampaignRequestRequestTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    {
        "CampaignId": str,
    },
)
GetEmailIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "GetEmailIdentityPoliciesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
GetEmailIdentityRequestRequestTypeDef = TypedDict(
    "GetEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
MailFromAttributesTypeDef = TypedDict(
    "MailFromAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": MailFromDomainStatusType,
        "BehaviorOnMxFailure": BehaviorOnMxFailureType,
    },
)
GetEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
GetExportJobRequestRequestTypeDef = TypedDict(
    "GetExportJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
GetImportJobRequestRequestTypeDef = TypedDict(
    "GetImportJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
GetMessageInsightsRequestRequestTypeDef = TypedDict(
    "GetMessageInsightsRequestRequestTypeDef",
    {
        "MessageId": str,
    },
)
GetSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "GetSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)
GuardianAttributesTypeDef = TypedDict(
    "GuardianAttributesTypeDef",
    {
        "OptimizedSharedDelivery": NotRequired[FeatureStatusType],
    },
)
GuardianOptionsTypeDef = TypedDict(
    "GuardianOptionsTypeDef",
    {
        "OptimizedSharedDelivery": NotRequired[FeatureStatusType],
    },
)
IdentityInfoTypeDef = TypedDict(
    "IdentityInfoTypeDef",
    {
        "IdentityType": NotRequired[IdentityTypeType],
        "IdentityName": NotRequired[str],
        "SendingEnabled": NotRequired[bool],
        "VerificationStatus": NotRequired[VerificationStatusType],
    },
)
SuppressionListDestinationTypeDef = TypedDict(
    "SuppressionListDestinationTypeDef",
    {
        "SuppressionListImportAction": SuppressionListImportActionType,
    },
)
InboxPlacementTrackingOptionTypeDef = TypedDict(
    "InboxPlacementTrackingOptionTypeDef",
    {
        "Global": NotRequired[bool],
        "TrackedIsps": NotRequired[Sequence[str]],
    },
)
ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListContactListsRequestRequestTypeDef = TypedDict(
    "ListContactListsRequestRequestTypeDef",
    {
        "PageSize": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TopicFilterTypeDef = TypedDict(
    "TopicFilterTypeDef",
    {
        "TopicName": NotRequired[str],
        "UseDefaultIfPreferenceUnavailable": NotRequired[bool],
    },
)
ListCustomVerificationEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListDedicatedIpPoolsRequestRequestTypeDef = TypedDict(
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListDeliverabilityTestReportsRequestRequestTypeDef = TypedDict(
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListEmailIdentitiesRequestRequestTypeDef = TypedDict(
    "ListEmailIdentitiesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListExportJobsRequestRequestTypeDef = TypedDict(
    "ListExportJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
        "ExportSourceType": NotRequired[ExportSourceTypeType],
        "JobStatus": NotRequired[JobStatusType],
    },
)
ListImportJobsRequestRequestTypeDef = TypedDict(
    "ListImportJobsRequestRequestTypeDef",
    {
        "ImportDestinationType": NotRequired[ImportDestinationTypeType],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListManagementOptionsTypeDef = TypedDict(
    "ListManagementOptionsTypeDef",
    {
        "ContactListName": str,
        "TopicName": NotRequired[str],
    },
)
ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "Filter": NotRequired[Mapping[ListRecommendationsFilterKeyType, str]],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "Type": NotRequired[RecommendationTypeType],
        "Description": NotRequired[str],
        "Status": NotRequired[RecommendationStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Impact": NotRequired[RecommendationImpactType],
    },
)
SuppressedDestinationSummaryTypeDef = TypedDict(
    "SuppressedDestinationSummaryTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
        "LastUpdateTime": datetime,
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
MessageInsightsFiltersOutputTypeDef = TypedDict(
    "MessageInsightsFiltersOutputTypeDef",
    {
        "FromEmailAddress": NotRequired[List[str]],
        "Destination": NotRequired[List[str]],
        "Subject": NotRequired[List[str]],
        "Isp": NotRequired[List[str]],
        "LastDeliveryEvent": NotRequired[List[DeliveryEventTypeType]],
        "LastEngagementEvent": NotRequired[List[EngagementEventTypeType]],
    },
)
MessageInsightsFiltersTypeDef = TypedDict(
    "MessageInsightsFiltersTypeDef",
    {
        "FromEmailAddress": NotRequired[Sequence[str]],
        "Destination": NotRequired[Sequence[str]],
        "Subject": NotRequired[Sequence[str]],
        "Isp": NotRequired[Sequence[str]],
        "LastDeliveryEvent": NotRequired[Sequence[DeliveryEventTypeType]],
        "LastEngagementEvent": NotRequired[Sequence[EngagementEventTypeType]],
    },
)
PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "AutoWarmupEnabled": NotRequired[bool],
    },
)
PutAccountDetailsRequestRequestTypeDef = TypedDict(
    "PutAccountDetailsRequestRequestTypeDef",
    {
        "MailType": MailTypeType,
        "WebsiteURL": str,
        "ContactLanguage": NotRequired[ContactLanguageType],
        "UseCaseDescription": NotRequired[str],
        "AdditionalContactEmailAddresses": NotRequired[Sequence[str]],
        "ProductionAccessEnabled": NotRequired[bool],
    },
)
PutAccountSendingAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSendingAttributesRequestRequestTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
    },
)
PutAccountSuppressionAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSuppressionAttributesRequestRequestTypeDef",
    {
        "SuppressedReasons": NotRequired[Sequence[SuppressionListReasonType]],
    },
)
PutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TlsPolicy": NotRequired[TlsPolicyType],
        "SendingPoolName": NotRequired[str],
        "MaxDeliverySeconds": NotRequired[int],
    },
)
PutConfigurationSetReputationOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetReputationOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "ReputationMetricsEnabled": NotRequired[bool],
    },
)
PutConfigurationSetSendingOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetSendingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "SendingEnabled": NotRequired[bool],
    },
)
PutConfigurationSetSuppressionOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetSuppressionOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "SuppressedReasons": NotRequired[Sequence[SuppressionListReasonType]],
    },
)
PutConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "CustomRedirectDomain": NotRequired[str],
        "HttpsPolicy": NotRequired[HttpsPolicyType],
    },
)
PutDedicatedIpInPoolRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    {
        "Ip": str,
        "DestinationPoolName": str,
    },
)
PutDedicatedIpPoolScalingAttributesRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpPoolScalingAttributesRequestRequestTypeDef",
    {
        "PoolName": str,
        "ScalingMode": ScalingModeType,
    },
)
PutDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "Ip": str,
        "WarmupPercentage": int,
    },
)
PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "ConfigurationSetName": NotRequired[str],
    },
)
PutEmailIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "SigningEnabled": NotRequired[bool],
    },
)
PutEmailIdentityFeedbackAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "EmailForwardingEnabled": NotRequired[bool],
    },
)
PutEmailIdentityMailFromAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "MailFromDomain": NotRequired[str],
        "BehaviorOnMxFailure": NotRequired[BehaviorOnMxFailureType],
    },
)
PutSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "PutSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
    },
)
ReplacementTemplateTypeDef = TypedDict(
    "ReplacementTemplateTypeDef",
    {
        "ReplacementTemplateData": NotRequired[str],
    },
)
SOARecordTypeDef = TypedDict(
    "SOARecordTypeDef",
    {
        "PrimaryNameServer": NotRequired[str],
        "AdminEmail": NotRequired[str],
        "SerialNumber": NotRequired[int],
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
SuppressedDestinationAttributesTypeDef = TypedDict(
    "SuppressedDestinationAttributesTypeDef",
    {
        "MessageId": NotRequired[str],
        "FeedbackId": NotRequired[str],
    },
)
TestRenderEmailTemplateRequestRequestTypeDef = TypedDict(
    "TestRenderEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateData": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
)
UpdateEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "UpdateEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
        "Policy": str,
    },
)
AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "MailType": NotRequired[MailTypeType],
        "WebsiteURL": NotRequired[str],
        "ContactLanguage": NotRequired[ContactLanguageType],
        "UseCaseDescription": NotRequired[str],
        "AdditionalContactEmailAddresses": NotRequired[List[str]],
        "ReviewDetails": NotRequired[ReviewDetailsTypeDef],
    },
)
BatchGetMetricDataQueryTypeDef = TypedDict(
    "BatchGetMetricDataQueryTypeDef",
    {
        "Id": str,
        "Namespace": Literal["VDM"],
        "Metric": MetricType,
        "StartDate": TimestampTypeDef,
        "EndDate": TimestampTypeDef,
        "Dimensions": NotRequired[Mapping[MetricDimensionNameType, str]],
    },
)
GetDomainStatisticsReportRequestRequestTypeDef = TypedDict(
    "GetDomainStatisticsReportRequestRequestTypeDef",
    {
        "Domain": str,
        "StartDate": TimestampTypeDef,
        "EndDate": TimestampTypeDef,
    },
)
ListDomainDeliverabilityCampaignsRequestRequestTypeDef = TypedDict(
    "ListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    {
        "StartDate": TimestampTypeDef,
        "EndDate": TimestampTypeDef,
        "SubscribedDomain": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListSuppressedDestinationsRequestRequestTypeDef = TypedDict(
    "ListSuppressedDestinationsRequestRequestTypeDef",
    {
        "Reasons": NotRequired[Sequence[SuppressionListReasonType]],
        "StartDate": NotRequired[TimestampTypeDef],
        "EndDate": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "ReputationMetricsEnabled": NotRequired[bool],
        "LastFreshStart": NotRequired[TimestampTypeDef],
    },
)
BatchGetMetricDataResponseTypeDef = TypedDict(
    "BatchGetMetricDataResponseTypeDef",
    {
        "Results": List[MetricDataResultTypeDef],
        "Errors": List[MetricDataErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeliverabilityTestReportResponseTypeDef = TypedDict(
    "CreateDeliverabilityTestReportResponseTypeDef",
    {
        "ReportId": str,
        "DeliverabilityTestStatus": DeliverabilityTestStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExportJobResponseTypeDef = TypedDict(
    "CreateExportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateImportJobResponseTypeDef = TypedDict(
    "CreateImportJobResponseTypeDef",
    {
        "JobId": str,
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
GetEmailIdentityPoliciesResponseTypeDef = TypedDict(
    "GetEmailIdentityPoliciesResponseTypeDef",
    {
        "Policies": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDedicatedIpPoolsResponseTypeDef = TypedDict(
    "ListDedicatedIpPoolsResponseTypeDef",
    {
        "DedicatedIpPools": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutEmailIdentityDkimSigningAttributesResponseTypeDef = TypedDict(
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    {
        "DkimStatus": DkimStatusType,
        "DkimTokens": List[str],
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
TestRenderEmailTemplateResponseTypeDef = TypedDict(
    "TestRenderEmailTemplateResponseTypeDef",
    {
        "RenderedTemplate": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBlacklistReportsResponseTypeDef = TypedDict(
    "GetBlacklistReportsResponseTypeDef",
    {
        "BlacklistReport": Dict[str, List[BlacklistEntryTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
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
SendBulkEmailResponseTypeDef = TypedDict(
    "SendBulkEmailResponseTypeDef",
    {
        "BulkEmailEntryResults": List[BulkEmailEntryResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "TemplateName": NotRequired[str],
        "TemplateArn": NotRequired[str],
        "TemplateData": NotRequired[str],
        "Headers": NotRequired[Sequence[MessageHeaderTypeDef]],
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
EventDetailsTypeDef = TypedDict(
    "EventDetailsTypeDef",
    {
        "Bounce": NotRequired[BounceTypeDef],
        "Complaint": NotRequired[ComplaintTypeDef],
    },
)
ListContactListsResponseTypeDef = TypedDict(
    "ListContactListsResponseTypeDef",
    {
        "ContactLists": List[ContactListTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "EmailAddress": NotRequired[str],
        "TopicPreferences": NotRequired[List[TopicPreferenceTypeDef]],
        "TopicDefaultPreferences": NotRequired[List[TopicPreferenceTypeDef]],
        "UnsubscribeAll": NotRequired[bool],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
CreateContactRequestRequestTypeDef = TypedDict(
    "CreateContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
        "TopicPreferences": NotRequired[Sequence[TopicPreferenceTypeDef]],
        "UnsubscribeAll": NotRequired[bool],
        "AttributesData": NotRequired[str],
    },
)
GetContactResponseTypeDef = TypedDict(
    "GetContactResponseTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
        "TopicPreferences": List[TopicPreferenceTypeDef],
        "TopicDefaultPreferences": List[TopicPreferenceTypeDef],
        "UnsubscribeAll": bool,
        "AttributesData": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContactRequestRequestTypeDef = TypedDict(
    "UpdateContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
        "TopicPreferences": NotRequired[Sequence[TopicPreferenceTypeDef]],
        "UnsubscribeAll": NotRequired[bool],
        "AttributesData": NotRequired[str],
    },
)
CreateDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ScalingMode": NotRequired[ScalingModeType],
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
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateContactListRequestRequestTypeDef = TypedDict(
    "CreateContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
        "Topics": NotRequired[Sequence[TopicTypeDef]],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetContactListResponseTypeDef = TypedDict(
    "GetContactListResponseTypeDef",
    {
        "ContactListName": str,
        "Topics": List[TopicTypeDef],
        "Description": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContactListRequestRequestTypeDef = TypedDict(
    "UpdateContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
        "Topics": NotRequired[Sequence[TopicTypeDef]],
        "Description": NotRequired[str],
    },
)
CreateEmailIdentityRequestRequestTypeDef = TypedDict(
    "CreateEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DkimSigningAttributes": NotRequired[DkimSigningAttributesTypeDef],
        "ConfigurationSetName": NotRequired[str],
    },
)
PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "SigningAttributesOrigin": DkimSigningAttributesOriginType,
        "SigningAttributes": NotRequired[DkimSigningAttributesTypeDef],
    },
)
CreateEmailIdentityResponseTypeDef = TypedDict(
    "CreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": DkimAttributesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": EmailTemplateContentTypeDef,
    },
)
GetEmailTemplateResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": EmailTemplateContentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": EmailTemplateContentTypeDef,
    },
)
ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List[CustomVerificationEmailTemplateMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DailyVolumeTypeDef = TypedDict(
    "DailyVolumeTypeDef",
    {
        "StartDate": NotRequired[datetime],
        "VolumeStatistics": NotRequired[VolumeStatisticsTypeDef],
        "DomainIspPlacements": NotRequired[List[DomainIspPlacementTypeDef]],
    },
)
OverallVolumeTypeDef = TypedDict(
    "OverallVolumeTypeDef",
    {
        "VolumeStatistics": NotRequired[VolumeStatisticsTypeDef],
        "ReadRatePercent": NotRequired[float],
        "DomainIspPlacements": NotRequired[List[DomainIspPlacementTypeDef]],
    },
)
GetDedicatedIpPoolResponseTypeDef = TypedDict(
    "GetDedicatedIpPoolResponseTypeDef",
    {
        "DedicatedIpPool": DedicatedIpPoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDedicatedIpResponseTypeDef = TypedDict(
    "GetDedicatedIpResponseTypeDef",
    {
        "DedicatedIp": DedicatedIpTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDedicatedIpsResponseTypeDef = TypedDict(
    "GetDedicatedIpsResponseTypeDef",
    {
        "DedicatedIps": List[DedicatedIpTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "ListDeliverabilityTestReportsResponseTypeDef",
    {
        "DeliverabilityTestReports": List[DeliverabilityTestReportTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDomainDeliverabilityCampaignResponseTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    {
        "DomainDeliverabilityCampaign": DomainDeliverabilityCampaignTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    {
        "DomainDeliverabilityCampaigns": List[DomainDeliverabilityCampaignTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DomainDeliverabilityTrackingOptionOutputTypeDef = TypedDict(
    "DomainDeliverabilityTrackingOptionOutputTypeDef",
    {
        "Domain": NotRequired[str],
        "SubscriptionStartDate": NotRequired[datetime],
        "InboxPlacementTrackingOption": NotRequired[InboxPlacementTrackingOptionOutputTypeDef],
    },
)
ListEmailTemplatesResponseTypeDef = TypedDict(
    "ListEmailTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List[EmailTemplateMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListExportJobsResponseTypeDef = TypedDict(
    "ListExportJobsResponseTypeDef",
    {
        "ExportJobs": List[ExportJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MetricsDataSourceOutputTypeDef = TypedDict(
    "MetricsDataSourceOutputTypeDef",
    {
        "Dimensions": Dict[MetricDimensionNameType, List[str]],
        "Namespace": Literal["VDM"],
        "Metrics": List[ExportMetricTypeDef],
        "StartDate": datetime,
        "EndDate": datetime,
    },
)
MetricsDataSourceTypeDef = TypedDict(
    "MetricsDataSourceTypeDef",
    {
        "Dimensions": Mapping[MetricDimensionNameType, Sequence[str]],
        "Namespace": Literal["VDM"],
        "Metrics": Sequence[ExportMetricTypeDef],
        "StartDate": TimestampTypeDef,
        "EndDate": TimestampTypeDef,
    },
)
IspPlacementTypeDef = TypedDict(
    "IspPlacementTypeDef",
    {
        "IspName": NotRequired[str],
        "PlacementStatistics": NotRequired[PlacementStatisticsTypeDef],
    },
)
VdmAttributesTypeDef = TypedDict(
    "VdmAttributesTypeDef",
    {
        "VdmEnabled": FeatureStatusType,
        "DashboardAttributes": NotRequired[DashboardAttributesTypeDef],
        "GuardianAttributes": NotRequired[GuardianAttributesTypeDef],
    },
)
VdmOptionsTypeDef = TypedDict(
    "VdmOptionsTypeDef",
    {
        "DashboardOptions": NotRequired[DashboardOptionsTypeDef],
        "GuardianOptions": NotRequired[GuardianOptionsTypeDef],
    },
)
ListEmailIdentitiesResponseTypeDef = TypedDict(
    "ListEmailIdentitiesResponseTypeDef",
    {
        "EmailIdentities": List[IdentityInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ImportDestinationTypeDef = TypedDict(
    "ImportDestinationTypeDef",
    {
        "SuppressionListDestination": NotRequired[SuppressionListDestinationTypeDef],
        "ContactListDestination": NotRequired[ContactListDestinationTypeDef],
    },
)
InboxPlacementTrackingOptionUnionTypeDef = Union[
    InboxPlacementTrackingOptionTypeDef, InboxPlacementTrackingOptionOutputTypeDef
]
ListContactsFilterTypeDef = TypedDict(
    "ListContactsFilterTypeDef",
    {
        "FilteredStatus": NotRequired[SubscriptionStatusType],
        "TopicFilter": NotRequired[TopicFilterTypeDef],
    },
)
ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "Recommendations": List[RecommendationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSuppressedDestinationsResponseTypeDef = TypedDict(
    "ListSuppressedDestinationsResponseTypeDef",
    {
        "SuppressedDestinationSummaries": List[SuppressedDestinationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MessageInsightsDataSourceOutputTypeDef = TypedDict(
    "MessageInsightsDataSourceOutputTypeDef",
    {
        "StartDate": datetime,
        "EndDate": datetime,
        "Include": NotRequired[MessageInsightsFiltersOutputTypeDef],
        "Exclude": NotRequired[MessageInsightsFiltersOutputTypeDef],
        "MaxResults": NotRequired[int],
    },
)
MessageInsightsFiltersUnionTypeDef = Union[
    MessageInsightsFiltersTypeDef, MessageInsightsFiltersOutputTypeDef
]
ReplacementEmailContentTypeDef = TypedDict(
    "ReplacementEmailContentTypeDef",
    {
        "ReplacementTemplate": NotRequired[ReplacementTemplateTypeDef],
    },
)
VerificationInfoTypeDef = TypedDict(
    "VerificationInfoTypeDef",
    {
        "LastCheckedTimestamp": NotRequired[datetime],
        "LastSuccessTimestamp": NotRequired[datetime],
        "ErrorType": NotRequired[VerificationErrorType],
        "SOARecord": NotRequired[SOARecordTypeDef],
    },
)
SuppressedDestinationTypeDef = TypedDict(
    "SuppressedDestinationTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
        "LastUpdateTime": datetime,
        "Attributes": NotRequired[SuppressedDestinationAttributesTypeDef],
    },
)
BatchGetMetricDataRequestRequestTypeDef = TypedDict(
    "BatchGetMetricDataRequestRequestTypeDef",
    {
        "Queries": Sequence[BatchGetMetricDataQueryTypeDef],
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Subject": ContentTypeDef,
        "Body": BodyTypeDef,
        "Headers": NotRequired[Sequence[MessageHeaderTypeDef]],
    },
)
BulkEmailContentTypeDef = TypedDict(
    "BulkEmailContentTypeDef",
    {
        "Template": NotRequired[TemplateTypeDef],
    },
)
EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": List[EventTypeType],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "CloudWatchDestination": NotRequired[CloudWatchDestinationOutputTypeDef],
        "SnsDestination": NotRequired[SnsDestinationTypeDef],
        "EventBridgeDestination": NotRequired[EventBridgeDestinationTypeDef],
        "PinpointDestination": NotRequired[PinpointDestinationTypeDef],
    },
)
CloudWatchDestinationUnionTypeDef = Union[
    CloudWatchDestinationTypeDef, CloudWatchDestinationOutputTypeDef
]
InsightsEventTypeDef = TypedDict(
    "InsightsEventTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "Type": NotRequired[EventTypeType],
        "Details": NotRequired[EventDetailsTypeDef],
    },
)
ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {
        "Contacts": List[ContactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDomainStatisticsReportResponseTypeDef = TypedDict(
    "GetDomainStatisticsReportResponseTypeDef",
    {
        "OverallVolume": OverallVolumeTypeDef,
        "DailyVolumes": List[DailyVolumeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": DeliverabilityDashboardAccountStatusType,
        "ActiveSubscribedDomains": List[DomainDeliverabilityTrackingOptionOutputTypeDef],
        "PendingExpirationSubscribedDomains": List[DomainDeliverabilityTrackingOptionOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricsDataSourceUnionTypeDef = Union[MetricsDataSourceTypeDef, MetricsDataSourceOutputTypeDef]
GetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "GetDeliverabilityTestReportResponseTypeDef",
    {
        "DeliverabilityTestReport": DeliverabilityTestReportTypeDef,
        "OverallPlacement": PlacementStatisticsTypeDef,
        "IspPlacements": List[IspPlacementTypeDef],
        "Message": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
        "SendQuota": SendQuotaTypeDef,
        "SendingEnabled": bool,
        "SuppressionAttributes": SuppressionAttributesTypeDef,
        "Details": AccountDetailsTypeDef,
        "VdmAttributes": VdmAttributesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAccountVdmAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountVdmAttributesRequestRequestTypeDef",
    {
        "VdmAttributes": VdmAttributesTypeDef,
    },
)
CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": NotRequired[TrackingOptionsTypeDef],
        "DeliveryOptions": NotRequired[DeliveryOptionsTypeDef],
        "ReputationOptions": NotRequired[ReputationOptionsTypeDef],
        "SendingOptions": NotRequired[SendingOptionsTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SuppressionOptions": NotRequired[SuppressionOptionsTypeDef],
        "VdmOptions": NotRequired[VdmOptionsTypeDef],
    },
)
GetConfigurationSetResponseTypeDef = TypedDict(
    "GetConfigurationSetResponseTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": TrackingOptionsTypeDef,
        "DeliveryOptions": DeliveryOptionsTypeDef,
        "ReputationOptions": ReputationOptionsOutputTypeDef,
        "SendingOptions": SendingOptionsTypeDef,
        "Tags": List[TagTypeDef],
        "SuppressionOptions": SuppressionOptionsOutputTypeDef,
        "VdmOptions": VdmOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutConfigurationSetVdmOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetVdmOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "VdmOptions": NotRequired[VdmOptionsTypeDef],
    },
)
CreateImportJobRequestRequestTypeDef = TypedDict(
    "CreateImportJobRequestRequestTypeDef",
    {
        "ImportDestination": ImportDestinationTypeDef,
        "ImportDataSource": ImportDataSourceTypeDef,
    },
)
GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "JobId": str,
        "ImportDestination": ImportDestinationTypeDef,
        "ImportDataSource": ImportDataSourceTypeDef,
        "FailureInfo": FailureInfoTypeDef,
        "JobStatus": JobStatusType,
        "CreatedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "ProcessedRecordsCount": int,
        "FailedRecordsCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportJobSummaryTypeDef = TypedDict(
    "ImportJobSummaryTypeDef",
    {
        "JobId": NotRequired[str],
        "ImportDestination": NotRequired[ImportDestinationTypeDef],
        "JobStatus": NotRequired[JobStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "ProcessedRecordsCount": NotRequired[int],
        "FailedRecordsCount": NotRequired[int],
    },
)
DomainDeliverabilityTrackingOptionTypeDef = TypedDict(
    "DomainDeliverabilityTrackingOptionTypeDef",
    {
        "Domain": NotRequired[str],
        "SubscriptionStartDate": NotRequired[TimestampTypeDef],
        "InboxPlacementTrackingOption": NotRequired[InboxPlacementTrackingOptionUnionTypeDef],
    },
)
ListContactsRequestRequestTypeDef = TypedDict(
    "ListContactsRequestRequestTypeDef",
    {
        "ContactListName": str,
        "Filter": NotRequired[ListContactsFilterTypeDef],
        "PageSize": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ExportDataSourceOutputTypeDef = TypedDict(
    "ExportDataSourceOutputTypeDef",
    {
        "MetricsDataSource": NotRequired[MetricsDataSourceOutputTypeDef],
        "MessageInsightsDataSource": NotRequired[MessageInsightsDataSourceOutputTypeDef],
    },
)
MessageInsightsDataSourceTypeDef = TypedDict(
    "MessageInsightsDataSourceTypeDef",
    {
        "StartDate": TimestampTypeDef,
        "EndDate": TimestampTypeDef,
        "Include": NotRequired[MessageInsightsFiltersUnionTypeDef],
        "Exclude": NotRequired[MessageInsightsFiltersUnionTypeDef],
        "MaxResults": NotRequired[int],
    },
)
BulkEmailEntryTypeDef = TypedDict(
    "BulkEmailEntryTypeDef",
    {
        "Destination": DestinationTypeDef,
        "ReplacementTags": NotRequired[Sequence[MessageTagTypeDef]],
        "ReplacementEmailContent": NotRequired[ReplacementEmailContentTypeDef],
        "ReplacementHeaders": NotRequired[Sequence[MessageHeaderTypeDef]],
    },
)
GetEmailIdentityResponseTypeDef = TypedDict(
    "GetEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": DkimAttributesTypeDef,
        "MailFromAttributes": MailFromAttributesTypeDef,
        "Policies": Dict[str, str],
        "Tags": List[TagTypeDef],
        "ConfigurationSetName": str,
        "VerificationStatus": VerificationStatusType,
        "VerificationInfo": VerificationInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSuppressedDestinationResponseTypeDef = TypedDict(
    "GetSuppressedDestinationResponseTypeDef",
    {
        "SuppressedDestination": SuppressedDestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "Simple": NotRequired[MessageTypeDef],
        "Raw": NotRequired[RawMessageTypeDef],
        "Template": NotRequired[TemplateTypeDef],
    },
)
GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List[EventDestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "Enabled": NotRequired[bool],
        "MatchingEventTypes": NotRequired[Sequence[EventTypeType]],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "CloudWatchDestination": NotRequired[CloudWatchDestinationUnionTypeDef],
        "SnsDestination": NotRequired[SnsDestinationTypeDef],
        "EventBridgeDestination": NotRequired[EventBridgeDestinationTypeDef],
        "PinpointDestination": NotRequired[PinpointDestinationTypeDef],
    },
)
EmailInsightsTypeDef = TypedDict(
    "EmailInsightsTypeDef",
    {
        "Destination": NotRequired[str],
        "Isp": NotRequired[str],
        "Events": NotRequired[List[InsightsEventTypeDef]],
    },
)
ListImportJobsResponseTypeDef = TypedDict(
    "ListImportJobsResponseTypeDef",
    {
        "ImportJobs": List[ImportJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DomainDeliverabilityTrackingOptionUnionTypeDef = Union[
    DomainDeliverabilityTrackingOptionTypeDef, DomainDeliverabilityTrackingOptionOutputTypeDef
]
GetExportJobResponseTypeDef = TypedDict(
    "GetExportJobResponseTypeDef",
    {
        "JobId": str,
        "ExportSourceType": ExportSourceTypeType,
        "JobStatus": JobStatusType,
        "ExportDestination": ExportDestinationTypeDef,
        "ExportDataSource": ExportDataSourceOutputTypeDef,
        "CreatedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "FailureInfo": FailureInfoTypeDef,
        "Statistics": ExportStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MessageInsightsDataSourceUnionTypeDef = Union[
    MessageInsightsDataSourceTypeDef, MessageInsightsDataSourceOutputTypeDef
]
SendBulkEmailRequestRequestTypeDef = TypedDict(
    "SendBulkEmailRequestRequestTypeDef",
    {
        "DefaultContent": BulkEmailContentTypeDef,
        "BulkEmailEntries": Sequence[BulkEmailEntryTypeDef],
        "FromEmailAddress": NotRequired[str],
        "FromEmailAddressIdentityArn": NotRequired[str],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "FeedbackForwardingEmailAddress": NotRequired[str],
        "FeedbackForwardingEmailAddressIdentityArn": NotRequired[str],
        "DefaultEmailTags": NotRequired[Sequence[MessageTagTypeDef]],
        "ConfigurationSetName": NotRequired[str],
    },
)
CreateDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "CreateDeliverabilityTestReportRequestRequestTypeDef",
    {
        "FromEmailAddress": str,
        "Content": EmailContentTypeDef,
        "ReportName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
SendEmailRequestRequestTypeDef = TypedDict(
    "SendEmailRequestRequestTypeDef",
    {
        "Content": EmailContentTypeDef,
        "FromEmailAddress": NotRequired[str],
        "FromEmailAddressIdentityArn": NotRequired[str],
        "Destination": NotRequired[DestinationTypeDef],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "FeedbackForwardingEmailAddress": NotRequired[str],
        "FeedbackForwardingEmailAddressIdentityArn": NotRequired[str],
        "EmailTags": NotRequired[Sequence[MessageTagTypeDef]],
        "ConfigurationSetName": NotRequired[str],
        "ListManagementOptions": NotRequired[ListManagementOptionsTypeDef],
    },
)
CreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": EventDestinationDefinitionTypeDef,
    },
)
UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": EventDestinationDefinitionTypeDef,
    },
)
GetMessageInsightsResponseTypeDef = TypedDict(
    "GetMessageInsightsResponseTypeDef",
    {
        "MessageId": str,
        "FromEmailAddress": str,
        "Subject": str,
        "EmailTags": List[MessageTagTypeDef],
        "Insights": List[EmailInsightsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDeliverabilityDashboardOptionRequestRequestTypeDef = TypedDict(
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscribedDomains": NotRequired[Sequence[DomainDeliverabilityTrackingOptionUnionTypeDef]],
    },
)
ExportDataSourceTypeDef = TypedDict(
    "ExportDataSourceTypeDef",
    {
        "MetricsDataSource": NotRequired[MetricsDataSourceUnionTypeDef],
        "MessageInsightsDataSource": NotRequired[MessageInsightsDataSourceUnionTypeDef],
    },
)
CreateExportJobRequestRequestTypeDef = TypedDict(
    "CreateExportJobRequestRequestTypeDef",
    {
        "ExportDataSource": ExportDataSourceTypeDef,
        "ExportDestination": ExportDestinationTypeDef,
    },
)
