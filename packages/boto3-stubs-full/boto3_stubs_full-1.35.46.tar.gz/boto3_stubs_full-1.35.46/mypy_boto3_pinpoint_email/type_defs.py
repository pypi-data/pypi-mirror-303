"""
Type annotations for pinpoint-email service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/type_defs/)

Usage::

    ```python
    from mypy_boto3_pinpoint_email.type_defs import BlacklistEntryTypeDef

    data: BlacklistEntryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMxFailureType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DimensionValueSourceType,
    DkimStatusType,
    EventTypeType,
    IdentityTypeType,
    MailFromDomainStatusType,
    TlsPolicyType,
    WarmupStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "BlacklistEntryTypeDef",
    "BlobTypeDef",
    "ContentTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "DeliveryOptionsTypeDef",
    "SendingOptionsTypeDef",
    "TagTypeDef",
    "TrackingOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "DkimAttributesTypeDef",
    "DomainIspPlacementTypeDef",
    "VolumeStatisticsTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    "DeleteEmailIdentityRequestRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DestinationTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "InboxPlacementTrackingOptionOutputTypeDef",
    "TimestampTypeDef",
    "TemplateTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "PinpointDestinationTypeDef",
    "SnsDestinationTypeDef",
    "SendQuotaTypeDef",
    "GetBlacklistReportsRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "GetConfigurationSetRequestRequestTypeDef",
    "ReputationOptionsOutputTypeDef",
    "GetDedicatedIpRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetDedicatedIpsRequestRequestTypeDef",
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    "PlacementStatisticsTypeDef",
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    "GetEmailIdentityRequestRequestTypeDef",
    "MailFromAttributesTypeDef",
    "IdentityInfoTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    "ListEmailIdentitiesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MessageTagTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutAccountSendingAttributesRequestRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "RawMessageTypeDef",
    "BodyTypeDef",
    "CloudWatchDestinationOutputTypeDef",
    "CloudWatchDestinationTypeDef",
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    "CreateEmailIdentityRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SendEmailResponseTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "DailyVolumeTypeDef",
    "OverallVolumeTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "DomainDeliverabilityTrackingOptionOutputTypeDef",
    "GetDomainStatisticsReportRequestRequestTypeDef",
    "ListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    "ReputationOptionsTypeDef",
    "GetAccountResponseTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef",
    "ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef",
    "ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef",
    "ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef",
    "ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef",
    "IspPlacementTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "InboxPlacementTrackingOptionUnionTypeDef",
    "MessageTypeDef",
    "EventDestinationTypeDef",
    "CloudWatchDestinationUnionTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "EmailContentTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "EventDestinationDefinitionTypeDef",
    "DomainDeliverabilityTrackingOptionUnionTypeDef",
    "CreateDeliverabilityTestReportRequestRequestTypeDef",
    "SendEmailRequestRequestTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
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
CloudWatchDimensionConfigurationTypeDef = TypedDict(
    "CloudWatchDimensionConfigurationTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": DimensionValueSourceType,
        "DefaultDimensionValue": str,
    },
)
DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": NotRequired[TlsPolicyType],
        "SendingPoolName": NotRequired[str],
    },
)
SendingOptionsTypeDef = TypedDict(
    "SendingOptionsTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
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
DkimAttributesTypeDef = TypedDict(
    "DkimAttributesTypeDef",
    {
        "SigningEnabled": NotRequired[bool],
        "Status": NotRequired[DkimStatusType],
        "Tokens": NotRequired[List[str]],
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
DeleteDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)
DeleteEmailIdentityRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
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
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "ToAddresses": NotRequired[Sequence[str]],
        "CcAddresses": NotRequired[Sequence[str]],
        "BccAddresses": NotRequired[Sequence[str]],
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
TimestampTypeDef = Union[datetime, str]
TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "TemplateArn": NotRequired[str],
        "TemplateData": NotRequired[str],
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
SendQuotaTypeDef = TypedDict(
    "SendQuotaTypeDef",
    {
        "Max24HourSend": NotRequired[float],
        "MaxSendRate": NotRequired[float],
        "SentLast24Hours": NotRequired[float],
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
GetDedicatedIpRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpRequestRequestTypeDef",
    {
        "Ip": str,
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
IdentityInfoTypeDef = TypedDict(
    "IdentityInfoTypeDef",
    {
        "IdentityType": NotRequired[IdentityTypeType],
        "IdentityName": NotRequired[str],
        "SendingEnabled": NotRequired[bool],
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
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
MessageTagTypeDef = TypedDict(
    "MessageTagTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "AutoWarmupEnabled": NotRequired[bool],
    },
)
PutAccountSendingAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSendingAttributesRequestRequestTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
    },
)
PutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TlsPolicy": NotRequired[TlsPolicyType],
        "SendingPoolName": NotRequired[str],
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
PutConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "CustomRedirectDomain": NotRequired[str],
    },
)
PutDedicatedIpInPoolRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    {
        "Ip": str,
        "DestinationPoolName": str,
    },
)
PutDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "Ip": str,
        "WarmupPercentage": int,
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
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
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
CreateDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateEmailIdentityRequestRequestTypeDef = TypedDict(
    "CreateEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
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
GetBlacklistReportsResponseTypeDef = TypedDict(
    "GetBlacklistReportsResponseTypeDef",
    {
        "BlacklistReport": Dict[str, List[BlacklistEntryTypeDef]],
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
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
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
CreateEmailIdentityResponseTypeDef = TypedDict(
    "CreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": DkimAttributesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "ReputationMetricsEnabled": NotRequired[bool],
        "LastFreshStart": NotRequired[TimestampTypeDef],
    },
)
GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "SendQuota": SendQuotaTypeDef,
        "SendingEnabled": bool,
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef = TypedDict(
    "GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef",
    {
        "PoolName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef = TypedDict(
    "ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef = TypedDict(
    "ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef = TypedDict(
    "ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef = TypedDict(
    "ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
IspPlacementTypeDef = TypedDict(
    "IspPlacementTypeDef",
    {
        "IspName": NotRequired[str],
        "PlacementStatistics": NotRequired[PlacementStatisticsTypeDef],
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
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
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
InboxPlacementTrackingOptionUnionTypeDef = Union[
    InboxPlacementTrackingOptionTypeDef, InboxPlacementTrackingOptionOutputTypeDef
]
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Subject": ContentTypeDef,
        "Body": BodyTypeDef,
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
        "PinpointDestination": NotRequired[PinpointDestinationTypeDef],
    },
)
CloudWatchDestinationUnionTypeDef = Union[
    CloudWatchDestinationTypeDef, CloudWatchDestinationOutputTypeDef
]
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
CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": NotRequired[TrackingOptionsTypeDef],
        "DeliveryOptions": NotRequired[DeliveryOptionsTypeDef],
        "ReputationOptions": NotRequired[ReputationOptionsTypeDef],
        "SendingOptions": NotRequired[SendingOptionsTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
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
DomainDeliverabilityTrackingOptionTypeDef = TypedDict(
    "DomainDeliverabilityTrackingOptionTypeDef",
    {
        "Domain": NotRequired[str],
        "SubscriptionStartDate": NotRequired[TimestampTypeDef],
        "InboxPlacementTrackingOption": NotRequired[InboxPlacementTrackingOptionUnionTypeDef],
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
        "PinpointDestination": NotRequired[PinpointDestinationTypeDef],
    },
)
DomainDeliverabilityTrackingOptionUnionTypeDef = Union[
    DomainDeliverabilityTrackingOptionTypeDef, DomainDeliverabilityTrackingOptionOutputTypeDef
]
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
        "Destination": DestinationTypeDef,
        "Content": EmailContentTypeDef,
        "FromEmailAddress": NotRequired[str],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "FeedbackForwardingEmailAddress": NotRequired[str],
        "EmailTags": NotRequired[Sequence[MessageTagTypeDef]],
        "ConfigurationSetName": NotRequired[str],
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
PutDeliverabilityDashboardOptionRequestRequestTypeDef = TypedDict(
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscribedDomains": NotRequired[Sequence[DomainDeliverabilityTrackingOptionUnionTypeDef]],
    },
)
