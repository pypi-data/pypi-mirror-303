"""
Type annotations for pinpoint service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/type_defs/)

Usage::

    ```python
    from mypy_boto3_pinpoint.type_defs import ADMChannelRequestTypeDef

    data: ADMChannelRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ActionType,
    AlignmentType,
    AttributeTypeType,
    ButtonActionType,
    CampaignStatusType,
    ChannelTypeType,
    DayOfWeekType,
    DeliveryStatusType,
    DimensionTypeType,
    DurationType,
    EndpointTypesElementType,
    FilterTypeType,
    FormatType,
    FrequencyType,
    IncludeType,
    JobStatusType,
    JourneyRunStatusType,
    LayoutType,
    MessageTypeType,
    ModeType,
    OperatorType,
    RecencyTypeType,
    SegmentTypeType,
    SourceTypeType,
    StateType,
    TemplateTypeType,
    TimezoneEstimationMethodsElementType,
    TypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ADMChannelRequestTypeDef",
    "ADMChannelResponseTypeDef",
    "ADMMessageTypeDef",
    "APNSChannelRequestTypeDef",
    "APNSChannelResponseTypeDef",
    "APNSMessageTypeDef",
    "APNSPushNotificationTemplateTypeDef",
    "APNSSandboxChannelRequestTypeDef",
    "APNSSandboxChannelResponseTypeDef",
    "APNSVoipChannelRequestTypeDef",
    "APNSVoipChannelResponseTypeDef",
    "APNSVoipSandboxChannelRequestTypeDef",
    "APNSVoipSandboxChannelResponseTypeDef",
    "ActivityResponseTypeDef",
    "ContactCenterActivityTypeDef",
    "HoldoutActivityTypeDef",
    "AddressConfigurationTypeDef",
    "AndroidPushNotificationTemplateTypeDef",
    "ApplicationResponseTypeDef",
    "JourneyTimeframeCapTypeDef",
    "CampaignHookTypeDef",
    "CampaignLimitsTypeDef",
    "QuietTimeTypeDef",
    "AttributeDimensionOutputTypeDef",
    "AttributeDimensionTypeDef",
    "AttributesResourceTypeDef",
    "BaiduChannelRequestTypeDef",
    "BaiduChannelResponseTypeDef",
    "BaiduMessageTypeDef",
    "BlobTypeDef",
    "CampaignCustomMessageTypeDef",
    "MessageHeaderTypeDef",
    "CampaignStateTypeDef",
    "CustomDeliveryConfigurationOutputTypeDef",
    "CampaignSmsMessageTypeDef",
    "ChannelResponseTypeDef",
    "ClosedDaysRuleTypeDef",
    "WaitTimeTypeDef",
    "CreateApplicationRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateTemplateMessageBodyTypeDef",
    "ExportJobRequestTypeDef",
    "ImportJobRequestTypeDef",
    "TemplateCreateMessageBodyTypeDef",
    "CreateRecommenderConfigurationTypeDef",
    "RecommenderConfigurationResponseTypeDef",
    "SMSTemplateRequestTypeDef",
    "VoiceTemplateRequestTypeDef",
    "CustomDeliveryConfigurationTypeDef",
    "JourneyCustomMessageTypeDef",
    "DefaultButtonConfigurationTypeDef",
    "DefaultMessageTypeDef",
    "DefaultPushNotificationMessageTypeDef",
    "DefaultPushNotificationTemplateTypeDef",
    "DeleteAdmChannelRequestRequestTypeDef",
    "DeleteApnsChannelRequestRequestTypeDef",
    "DeleteApnsSandboxChannelRequestRequestTypeDef",
    "DeleteApnsVoipChannelRequestRequestTypeDef",
    "DeleteApnsVoipSandboxChannelRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteBaiduChannelRequestRequestTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteEmailChannelRequestRequestTypeDef",
    "EmailChannelResponseTypeDef",
    "DeleteEmailTemplateRequestRequestTypeDef",
    "MessageBodyTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "DeleteEventStreamRequestRequestTypeDef",
    "EventStreamTypeDef",
    "DeleteGcmChannelRequestRequestTypeDef",
    "GCMChannelResponseTypeDef",
    "DeleteInAppTemplateRequestRequestTypeDef",
    "DeleteJourneyRequestRequestTypeDef",
    "DeletePushTemplateRequestRequestTypeDef",
    "DeleteRecommenderConfigurationRequestRequestTypeDef",
    "DeleteSegmentRequestRequestTypeDef",
    "DeleteSmsChannelRequestRequestTypeDef",
    "SMSChannelResponseTypeDef",
    "DeleteSmsTemplateRequestRequestTypeDef",
    "DeleteUserEndpointsRequestRequestTypeDef",
    "DeleteVoiceChannelRequestRequestTypeDef",
    "VoiceChannelResponseTypeDef",
    "DeleteVoiceTemplateRequestRequestTypeDef",
    "GCMMessageTypeDef",
    "SMSMessageTypeDef",
    "VoiceMessageTypeDef",
    "EmailChannelRequestTypeDef",
    "JourneyEmailMessageTypeDef",
    "EndpointDemographicTypeDef",
    "EndpointLocationTypeDef",
    "EndpointItemResponseTypeDef",
    "EndpointMessageResultTypeDef",
    "EndpointUserOutputTypeDef",
    "EndpointSendConfigurationTypeDef",
    "EndpointUserTypeDef",
    "MetricDimensionTypeDef",
    "SetDimensionOutputTypeDef",
    "EventItemResponseTypeDef",
    "SessionTypeDef",
    "ExportJobResourceTypeDef",
    "GCMChannelRequestTypeDef",
    "GPSCoordinatesTypeDef",
    "GetAdmChannelRequestRequestTypeDef",
    "GetApnsChannelRequestRequestTypeDef",
    "GetApnsSandboxChannelRequestRequestTypeDef",
    "GetApnsVoipChannelRequestRequestTypeDef",
    "GetApnsVoipSandboxChannelRequestRequestTypeDef",
    "GetAppRequestRequestTypeDef",
    "TimestampTypeDef",
    "GetApplicationSettingsRequestRequestTypeDef",
    "GetAppsRequestRequestTypeDef",
    "GetBaiduChannelRequestRequestTypeDef",
    "GetCampaignActivitiesRequestRequestTypeDef",
    "GetCampaignRequestRequestTypeDef",
    "GetCampaignVersionRequestRequestTypeDef",
    "GetCampaignVersionsRequestRequestTypeDef",
    "GetCampaignsRequestRequestTypeDef",
    "GetChannelsRequestRequestTypeDef",
    "GetEmailChannelRequestRequestTypeDef",
    "GetEmailTemplateRequestRequestTypeDef",
    "GetEndpointRequestRequestTypeDef",
    "GetEventStreamRequestRequestTypeDef",
    "GetExportJobRequestRequestTypeDef",
    "GetExportJobsRequestRequestTypeDef",
    "GetGcmChannelRequestRequestTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetImportJobsRequestRequestTypeDef",
    "GetInAppMessagesRequestRequestTypeDef",
    "GetInAppTemplateRequestRequestTypeDef",
    "GetJourneyExecutionActivityMetricsRequestRequestTypeDef",
    "JourneyExecutionActivityMetricsResponseTypeDef",
    "GetJourneyExecutionMetricsRequestRequestTypeDef",
    "JourneyExecutionMetricsResponseTypeDef",
    "GetJourneyRequestRequestTypeDef",
    "GetJourneyRunExecutionActivityMetricsRequestRequestTypeDef",
    "JourneyRunExecutionActivityMetricsResponseTypeDef",
    "GetJourneyRunExecutionMetricsRequestRequestTypeDef",
    "JourneyRunExecutionMetricsResponseTypeDef",
    "GetJourneyRunsRequestRequestTypeDef",
    "GetPushTemplateRequestRequestTypeDef",
    "GetRecommenderConfigurationRequestRequestTypeDef",
    "GetRecommenderConfigurationsRequestRequestTypeDef",
    "GetSegmentExportJobsRequestRequestTypeDef",
    "GetSegmentImportJobsRequestRequestTypeDef",
    "GetSegmentRequestRequestTypeDef",
    "GetSegmentVersionRequestRequestTypeDef",
    "GetSegmentVersionsRequestRequestTypeDef",
    "GetSegmentsRequestRequestTypeDef",
    "GetSmsChannelRequestRequestTypeDef",
    "GetSmsTemplateRequestRequestTypeDef",
    "SMSTemplateResponseTypeDef",
    "GetUserEndpointsRequestRequestTypeDef",
    "GetVoiceChannelRequestRequestTypeDef",
    "GetVoiceTemplateRequestRequestTypeDef",
    "VoiceTemplateResponseTypeDef",
    "ImportJobResourceTypeDef",
    "InAppMessageBodyConfigTypeDef",
    "OverrideButtonConfigurationTypeDef",
    "InAppMessageHeaderConfigTypeDef",
    "JourneyChannelSettingsTypeDef",
    "JourneyPushMessageTypeDef",
    "JourneyScheduleOutputTypeDef",
    "JourneyRunResponseTypeDef",
    "JourneySMSMessageTypeDef",
    "JourneyStateRequestTypeDef",
    "ListJourneysRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagsModelOutputTypeDef",
    "ListTemplateVersionsRequestRequestTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "MessageTypeDef",
    "MessageResultTypeDef",
    "NumberValidateRequestTypeDef",
    "NumberValidateResponseTypeDef",
    "OpenHoursRuleTypeDef",
    "WriteEventStreamTypeDef",
    "RandomSplitEntryTypeDef",
    "RecencyDimensionTypeDef",
    "UpdateAttributesRequestTypeDef",
    "ResultRowValueTypeDef",
    "SMSChannelRequestTypeDef",
    "SegmentConditionTypeDef",
    "SegmentReferenceTypeDef",
    "SegmentImportResourceTypeDef",
    "SendOTPMessageRequestParametersTypeDef",
    "SetDimensionTypeDef",
    "SimpleEmailPartTypeDef",
    "TagsModelTypeDef",
    "TemplateActiveVersionRequestTypeDef",
    "TemplateTypeDef",
    "TemplateResponseTypeDef",
    "TemplateVersionResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRecommenderConfigurationTypeDef",
    "VoiceChannelRequestTypeDef",
    "VerificationResponseTypeDef",
    "VerifyOTPMessageRequestParametersTypeDef",
    "UpdateAdmChannelRequestRequestTypeDef",
    "UpdateApnsChannelRequestRequestTypeDef",
    "UpdateApnsSandboxChannelRequestRequestTypeDef",
    "UpdateApnsVoipChannelRequestRequestTypeDef",
    "UpdateApnsVoipSandboxChannelRequestRequestTypeDef",
    "ActivitiesResponseTypeDef",
    "ApplicationsResponseTypeDef",
    "ApplicationSettingsJourneyLimitsTypeDef",
    "JourneyLimitsTypeDef",
    "AttributeDimensionUnionTypeDef",
    "UpdateBaiduChannelRequestRequestTypeDef",
    "RawEmailTypeDef",
    "CampaignEmailMessageOutputTypeDef",
    "CampaignEmailMessageTypeDef",
    "EmailTemplateRequestTypeDef",
    "EmailTemplateResponseTypeDef",
    "ChannelsResponseTypeDef",
    "ClosedDaysOutputTypeDef",
    "ClosedDaysTypeDef",
    "WaitActivityTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "DeleteAdmChannelResponseTypeDef",
    "DeleteApnsChannelResponseTypeDef",
    "DeleteApnsSandboxChannelResponseTypeDef",
    "DeleteApnsVoipChannelResponseTypeDef",
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    "DeleteAppResponseTypeDef",
    "DeleteBaiduChannelResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAdmChannelResponseTypeDef",
    "GetApnsChannelResponseTypeDef",
    "GetApnsSandboxChannelResponseTypeDef",
    "GetApnsVoipChannelResponseTypeDef",
    "GetApnsVoipSandboxChannelResponseTypeDef",
    "GetAppResponseTypeDef",
    "GetBaiduChannelResponseTypeDef",
    "RemoveAttributesResponseTypeDef",
    "UpdateAdmChannelResponseTypeDef",
    "UpdateApnsChannelResponseTypeDef",
    "UpdateApnsSandboxChannelResponseTypeDef",
    "UpdateApnsVoipChannelResponseTypeDef",
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    "UpdateBaiduChannelResponseTypeDef",
    "CreateEmailTemplateResponseTypeDef",
    "CreatePushTemplateResponseTypeDef",
    "CreateSmsTemplateResponseTypeDef",
    "CreateVoiceTemplateResponseTypeDef",
    "CreateExportJobRequestRequestTypeDef",
    "CreateImportJobRequestRequestTypeDef",
    "CreateInAppTemplateResponseTypeDef",
    "CreateRecommenderConfigurationRequestRequestTypeDef",
    "CreateRecommenderConfigurationResponseTypeDef",
    "DeleteRecommenderConfigurationResponseTypeDef",
    "GetRecommenderConfigurationResponseTypeDef",
    "ListRecommenderConfigurationsResponseTypeDef",
    "UpdateRecommenderConfigurationResponseTypeDef",
    "CreateSmsTemplateRequestRequestTypeDef",
    "UpdateSmsTemplateRequestRequestTypeDef",
    "CreateVoiceTemplateRequestRequestTypeDef",
    "UpdateVoiceTemplateRequestRequestTypeDef",
    "CustomDeliveryConfigurationUnionTypeDef",
    "CustomMessageActivityOutputTypeDef",
    "CustomMessageActivityTypeDef",
    "PushNotificationTemplateRequestTypeDef",
    "PushNotificationTemplateResponseTypeDef",
    "DeleteEmailChannelResponseTypeDef",
    "GetEmailChannelResponseTypeDef",
    "UpdateEmailChannelResponseTypeDef",
    "DeleteEmailTemplateResponseTypeDef",
    "DeleteInAppTemplateResponseTypeDef",
    "DeletePushTemplateResponseTypeDef",
    "DeleteSmsTemplateResponseTypeDef",
    "DeleteVoiceTemplateResponseTypeDef",
    "UpdateEmailTemplateResponseTypeDef",
    "UpdateEndpointResponseTypeDef",
    "UpdateEndpointsBatchResponseTypeDef",
    "UpdateInAppTemplateResponseTypeDef",
    "UpdatePushTemplateResponseTypeDef",
    "UpdateSmsTemplateResponseTypeDef",
    "UpdateTemplateActiveVersionResponseTypeDef",
    "UpdateVoiceTemplateResponseTypeDef",
    "DeleteEventStreamResponseTypeDef",
    "GetEventStreamResponseTypeDef",
    "PutEventStreamResponseTypeDef",
    "DeleteGcmChannelResponseTypeDef",
    "GetGcmChannelResponseTypeDef",
    "UpdateGcmChannelResponseTypeDef",
    "DeleteSmsChannelResponseTypeDef",
    "GetSmsChannelResponseTypeDef",
    "UpdateSmsChannelResponseTypeDef",
    "DeleteVoiceChannelResponseTypeDef",
    "GetVoiceChannelResponseTypeDef",
    "UpdateVoiceChannelResponseTypeDef",
    "UpdateEmailChannelRequestRequestTypeDef",
    "EmailMessageActivityTypeDef",
    "SendUsersMessageResponseTypeDef",
    "EndpointResponseTypeDef",
    "EndpointUserUnionTypeDef",
    "EventDimensionsOutputTypeDef",
    "SegmentDemographicsOutputTypeDef",
    "ItemResponseTypeDef",
    "EventTypeDef",
    "ExportJobResponseTypeDef",
    "UpdateGcmChannelRequestRequestTypeDef",
    "GPSPointDimensionTypeDef",
    "GetApplicationDateRangeKpiRequestRequestTypeDef",
    "GetCampaignDateRangeKpiRequestRequestTypeDef",
    "GetJourneyDateRangeKpiRequestRequestTypeDef",
    "JourneyScheduleTypeDef",
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    "GetJourneyExecutionMetricsResponseTypeDef",
    "GetJourneyRunExecutionActivityMetricsResponseTypeDef",
    "GetJourneyRunExecutionMetricsResponseTypeDef",
    "GetSmsTemplateResponseTypeDef",
    "GetVoiceTemplateResponseTypeDef",
    "ImportJobResponseTypeDef",
    "InAppMessageButtonTypeDef",
    "PushMessageActivityTypeDef",
    "JourneyRunsResponseTypeDef",
    "SMSMessageActivityTypeDef",
    "UpdateJourneyStateRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageResponseTypeDef",
    "PhoneNumberValidateRequestRequestTypeDef",
    "PhoneNumberValidateResponseTypeDef",
    "OpenHoursOutputTypeDef",
    "OpenHoursTypeDef",
    "PutEventStreamRequestRequestTypeDef",
    "RandomSplitActivityOutputTypeDef",
    "RandomSplitActivityTypeDef",
    "SegmentBehaviorsTypeDef",
    "RemoveAttributesRequestRequestTypeDef",
    "ResultRowTypeDef",
    "UpdateSmsChannelRequestRequestTypeDef",
    "SendOTPMessageRequestRequestTypeDef",
    "SetDimensionUnionTypeDef",
    "SimpleEmailTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UpdateTemplateActiveVersionRequestRequestTypeDef",
    "TemplateConfigurationTypeDef",
    "TemplatesResponseTypeDef",
    "TemplateVersionsResponseTypeDef",
    "UpdateRecommenderConfigurationRequestRequestTypeDef",
    "UpdateVoiceChannelRequestRequestTypeDef",
    "VerifyOTPMessageResponseTypeDef",
    "VerifyOTPMessageRequestRequestTypeDef",
    "GetCampaignActivitiesResponseTypeDef",
    "GetAppsResponseTypeDef",
    "ApplicationSettingsResourceTypeDef",
    "WriteApplicationSettingsRequestTypeDef",
    "CampaignEmailMessageUnionTypeDef",
    "CreateEmailTemplateRequestRequestTypeDef",
    "UpdateEmailTemplateRequestRequestTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetChannelsResponseTypeDef",
    "ClosedDaysUnionTypeDef",
    "GetRecommenderConfigurationsResponseTypeDef",
    "CustomMessageActivityUnionTypeDef",
    "CreatePushTemplateRequestRequestTypeDef",
    "UpdatePushTemplateRequestRequestTypeDef",
    "GetPushTemplateResponseTypeDef",
    "SendUsersMessagesResponseTypeDef",
    "DeleteEndpointResponseTypeDef",
    "EndpointsResponseTypeDef",
    "GetEndpointResponseTypeDef",
    "EndpointBatchItemTypeDef",
    "EndpointRequestTypeDef",
    "PublicEndpointTypeDef",
    "CampaignEventFilterOutputTypeDef",
    "EventConditionOutputTypeDef",
    "EventFilterOutputTypeDef",
    "EventsResponseTypeDef",
    "CreateExportJobResponseTypeDef",
    "ExportJobsResponseTypeDef",
    "GetExportJobResponseTypeDef",
    "SegmentLocationOutputTypeDef",
    "JourneyScheduleUnionTypeDef",
    "CreateImportJobResponseTypeDef",
    "GetImportJobResponseTypeDef",
    "ImportJobsResponseTypeDef",
    "InAppMessageContentTypeDef",
    "GetJourneyRunsResponseTypeDef",
    "SendMessagesResponseTypeDef",
    "SendOTPMessageResponseTypeDef",
    "OpenHoursUnionTypeDef",
    "RandomSplitActivityUnionTypeDef",
    "BaseKpiResultTypeDef",
    "EventDimensionsTypeDef",
    "SegmentDemographicsTypeDef",
    "SegmentLocationTypeDef",
    "EmailMessageTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "GetApplicationSettingsResponseTypeDef",
    "UpdateApplicationSettingsResponseTypeDef",
    "UpdateApplicationSettingsRequestRequestTypeDef",
    "DeleteUserEndpointsResponseTypeDef",
    "GetUserEndpointsResponseTypeDef",
    "EndpointBatchRequestTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "EventsBatchTypeDef",
    "InAppCampaignScheduleTypeDef",
    "ScheduleOutputTypeDef",
    "EventStartConditionOutputTypeDef",
    "PutEventsResponseTypeDef",
    "GetExportJobsResponseTypeDef",
    "GetSegmentExportJobsResponseTypeDef",
    "SegmentDimensionsOutputTypeDef",
    "GetImportJobsResponseTypeDef",
    "GetSegmentImportJobsResponseTypeDef",
    "CampaignInAppMessageOutputTypeDef",
    "CampaignInAppMessageTypeDef",
    "InAppMessageTypeDef",
    "InAppTemplateRequestTypeDef",
    "InAppTemplateResponseTypeDef",
    "ApplicationDateRangeKpiResponseTypeDef",
    "CampaignDateRangeKpiResponseTypeDef",
    "JourneyDateRangeKpiResponseTypeDef",
    "EventDimensionsUnionTypeDef",
    "SegmentDemographicsUnionTypeDef",
    "SegmentLocationUnionTypeDef",
    "DirectMessageConfigurationTypeDef",
    "UpdateEndpointsBatchRequestRequestTypeDef",
    "EventsRequestTypeDef",
    "StartConditionOutputTypeDef",
    "SegmentGroupOutputTypeDef",
    "SimpleConditionOutputTypeDef",
    "MessageConfigurationOutputTypeDef",
    "CampaignInAppMessageUnionTypeDef",
    "InAppMessageCampaignTypeDef",
    "CreateInAppTemplateRequestRequestTypeDef",
    "UpdateInAppTemplateRequestRequestTypeDef",
    "GetInAppTemplateResponseTypeDef",
    "GetApplicationDateRangeKpiResponseTypeDef",
    "GetCampaignDateRangeKpiResponseTypeDef",
    "GetJourneyDateRangeKpiResponseTypeDef",
    "CampaignEventFilterTypeDef",
    "EventConditionTypeDef",
    "EventFilterTypeDef",
    "SegmentDimensionsTypeDef",
    "MessageRequestTypeDef",
    "SendUsersMessageRequestTypeDef",
    "PutEventsRequestRequestTypeDef",
    "SegmentGroupListOutputTypeDef",
    "ConditionOutputTypeDef",
    "MultiConditionalBranchOutputTypeDef",
    "TreatmentResourceTypeDef",
    "MessageConfigurationTypeDef",
    "InAppMessagesResponseTypeDef",
    "CampaignEventFilterUnionTypeDef",
    "EventConditionUnionTypeDef",
    "EventFilterUnionTypeDef",
    "SegmentDimensionsUnionTypeDef",
    "SendMessagesRequestRequestTypeDef",
    "SendUsersMessagesRequestRequestTypeDef",
    "SegmentResponseTypeDef",
    "ConditionalSplitActivityOutputTypeDef",
    "MultiConditionalSplitActivityOutputTypeDef",
    "CampaignResponseTypeDef",
    "MessageConfigurationUnionTypeDef",
    "GetInAppMessagesResponseTypeDef",
    "ScheduleTypeDef",
    "EventStartConditionTypeDef",
    "SegmentGroupTypeDef",
    "SimpleConditionTypeDef",
    "CreateSegmentResponseTypeDef",
    "DeleteSegmentResponseTypeDef",
    "GetSegmentResponseTypeDef",
    "GetSegmentVersionResponseTypeDef",
    "SegmentsResponseTypeDef",
    "UpdateSegmentResponseTypeDef",
    "ActivityOutputTypeDef",
    "CampaignsResponseTypeDef",
    "CreateCampaignResponseTypeDef",
    "DeleteCampaignResponseTypeDef",
    "GetCampaignResponseTypeDef",
    "GetCampaignVersionResponseTypeDef",
    "UpdateCampaignResponseTypeDef",
    "ScheduleUnionTypeDef",
    "EventStartConditionUnionTypeDef",
    "SegmentGroupUnionTypeDef",
    "SimpleConditionUnionTypeDef",
    "GetSegmentVersionsResponseTypeDef",
    "GetSegmentsResponseTypeDef",
    "JourneyResponseTypeDef",
    "GetCampaignVersionsResponseTypeDef",
    "GetCampaignsResponseTypeDef",
    "WriteTreatmentResourceTypeDef",
    "StartConditionTypeDef",
    "SegmentGroupListTypeDef",
    "ConditionTypeDef",
    "MultiConditionalBranchTypeDef",
    "CreateJourneyResponseTypeDef",
    "DeleteJourneyResponseTypeDef",
    "GetJourneyResponseTypeDef",
    "JourneysResponseTypeDef",
    "UpdateJourneyResponseTypeDef",
    "UpdateJourneyStateResponseTypeDef",
    "WriteCampaignRequestTypeDef",
    "StartConditionUnionTypeDef",
    "SegmentGroupListUnionTypeDef",
    "ConditionUnionTypeDef",
    "MultiConditionalBranchUnionTypeDef",
    "ListJourneysResponseTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "WriteSegmentRequestTypeDef",
    "ConditionalSplitActivityTypeDef",
    "MultiConditionalSplitActivityTypeDef",
    "CreateSegmentRequestRequestTypeDef",
    "UpdateSegmentRequestRequestTypeDef",
    "ConditionalSplitActivityUnionTypeDef",
    "MultiConditionalSplitActivityUnionTypeDef",
    "ActivityTypeDef",
    "ActivityUnionTypeDef",
    "WriteJourneyRequestTypeDef",
    "CreateJourneyRequestRequestTypeDef",
    "UpdateJourneyRequestRequestTypeDef",
)

ADMChannelRequestTypeDef = TypedDict(
    "ADMChannelRequestTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
        "Enabled": NotRequired[bool],
    },
)
ADMChannelResponseTypeDef = TypedDict(
    "ADMChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
ADMMessageTypeDef = TypedDict(
    "ADMMessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "ConsolidationKey": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "ExpiresAfter": NotRequired[str],
        "IconReference": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "MD5": NotRequired[str],
        "RawContent": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "SmallImageIconUrl": NotRequired[str],
        "Sound": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
APNSChannelRequestTypeDef = TypedDict(
    "APNSChannelRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "Certificate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
        "TokenKey": NotRequired[str],
        "TokenKeyId": NotRequired[str],
    },
)
APNSChannelResponseTypeDef = TypedDict(
    "APNSChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasTokenKey": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
APNSMessageTypeDef = TypedDict(
    "APNSMessageTypeDef",
    {
        "APNSPushType": NotRequired[str],
        "Action": NotRequired[ActionType],
        "Badge": NotRequired[int],
        "Body": NotRequired[str],
        "Category": NotRequired[str],
        "CollapseId": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "MediaUrl": NotRequired[str],
        "PreferredAuthenticationMethod": NotRequired[str],
        "Priority": NotRequired[str],
        "RawContent": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "Sound": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "ThreadId": NotRequired[str],
        "TimeToLive": NotRequired[int],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
APNSPushNotificationTemplateTypeDef = TypedDict(
    "APNSPushNotificationTemplateTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "MediaUrl": NotRequired[str],
        "RawContent": NotRequired[str],
        "Sound": NotRequired[str],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
APNSSandboxChannelRequestTypeDef = TypedDict(
    "APNSSandboxChannelRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "Certificate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
        "TokenKey": NotRequired[str],
        "TokenKeyId": NotRequired[str],
    },
)
APNSSandboxChannelResponseTypeDef = TypedDict(
    "APNSSandboxChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasTokenKey": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
APNSVoipChannelRequestTypeDef = TypedDict(
    "APNSVoipChannelRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "Certificate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
        "TokenKey": NotRequired[str],
        "TokenKeyId": NotRequired[str],
    },
)
APNSVoipChannelResponseTypeDef = TypedDict(
    "APNSVoipChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasTokenKey": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
APNSVoipSandboxChannelRequestTypeDef = TypedDict(
    "APNSVoipSandboxChannelRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "Certificate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
        "TokenKey": NotRequired[str],
        "TokenKeyId": NotRequired[str],
    },
)
APNSVoipSandboxChannelResponseTypeDef = TypedDict(
    "APNSVoipSandboxChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasTokenKey": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
ActivityResponseTypeDef = TypedDict(
    "ActivityResponseTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "Id": str,
        "End": NotRequired[str],
        "Result": NotRequired[str],
        "ScheduledStart": NotRequired[str],
        "Start": NotRequired[str],
        "State": NotRequired[str],
        "SuccessfulEndpointCount": NotRequired[int],
        "TimezonesCompletedCount": NotRequired[int],
        "TimezonesTotalCount": NotRequired[int],
        "TotalEndpointCount": NotRequired[int],
        "TreatmentId": NotRequired[str],
        "ExecutionMetrics": NotRequired[Dict[str, str]],
    },
)
ContactCenterActivityTypeDef = TypedDict(
    "ContactCenterActivityTypeDef",
    {
        "NextActivity": NotRequired[str],
    },
)
HoldoutActivityTypeDef = TypedDict(
    "HoldoutActivityTypeDef",
    {
        "Percentage": int,
        "NextActivity": NotRequired[str],
    },
)
AddressConfigurationTypeDef = TypedDict(
    "AddressConfigurationTypeDef",
    {
        "BodyOverride": NotRequired[str],
        "ChannelType": NotRequired[ChannelTypeType],
        "Context": NotRequired[Mapping[str, str]],
        "RawContent": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "TitleOverride": NotRequired[str],
    },
)
AndroidPushNotificationTemplateTypeDef = TypedDict(
    "AndroidPushNotificationTemplateTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "RawContent": NotRequired[str],
        "SmallImageIconUrl": NotRequired[str],
        "Sound": NotRequired[str],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
ApplicationResponseTypeDef = TypedDict(
    "ApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "tags": NotRequired[Dict[str, str]],
        "CreationDate": NotRequired[str],
    },
)
JourneyTimeframeCapTypeDef = TypedDict(
    "JourneyTimeframeCapTypeDef",
    {
        "Cap": NotRequired[int],
        "Days": NotRequired[int],
    },
)
CampaignHookTypeDef = TypedDict(
    "CampaignHookTypeDef",
    {
        "LambdaFunctionName": NotRequired[str],
        "Mode": NotRequired[ModeType],
        "WebUrl": NotRequired[str],
    },
)
CampaignLimitsTypeDef = TypedDict(
    "CampaignLimitsTypeDef",
    {
        "Daily": NotRequired[int],
        "MaximumDuration": NotRequired[int],
        "MessagesPerSecond": NotRequired[int],
        "Total": NotRequired[int],
        "Session": NotRequired[int],
    },
)
QuietTimeTypeDef = TypedDict(
    "QuietTimeTypeDef",
    {
        "End": NotRequired[str],
        "Start": NotRequired[str],
    },
)
AttributeDimensionOutputTypeDef = TypedDict(
    "AttributeDimensionOutputTypeDef",
    {
        "Values": List[str],
        "AttributeType": NotRequired[AttributeTypeType],
    },
)
AttributeDimensionTypeDef = TypedDict(
    "AttributeDimensionTypeDef",
    {
        "Values": Sequence[str],
        "AttributeType": NotRequired[AttributeTypeType],
    },
)
AttributesResourceTypeDef = TypedDict(
    "AttributesResourceTypeDef",
    {
        "ApplicationId": str,
        "AttributeType": str,
        "Attributes": NotRequired[List[str]],
    },
)
BaiduChannelRequestTypeDef = TypedDict(
    "BaiduChannelRequestTypeDef",
    {
        "ApiKey": str,
        "SecretKey": str,
        "Enabled": NotRequired[bool],
    },
)
BaiduChannelResponseTypeDef = TypedDict(
    "BaiduChannelResponseTypeDef",
    {
        "Credential": str,
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
BaiduMessageTypeDef = TypedDict(
    "BaiduMessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "IconReference": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "RawContent": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "SmallImageIconUrl": NotRequired[str],
        "Sound": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "TimeToLive": NotRequired[int],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CampaignCustomMessageTypeDef = TypedDict(
    "CampaignCustomMessageTypeDef",
    {
        "Data": NotRequired[str],
    },
)
MessageHeaderTypeDef = TypedDict(
    "MessageHeaderTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
CampaignStateTypeDef = TypedDict(
    "CampaignStateTypeDef",
    {
        "CampaignStatus": NotRequired[CampaignStatusType],
    },
)
CustomDeliveryConfigurationOutputTypeDef = TypedDict(
    "CustomDeliveryConfigurationOutputTypeDef",
    {
        "DeliveryUri": str,
        "EndpointTypes": NotRequired[List[EndpointTypesElementType]],
    },
)
CampaignSmsMessageTypeDef = TypedDict(
    "CampaignSmsMessageTypeDef",
    {
        "Body": NotRequired[str],
        "MessageType": NotRequired[MessageTypeType],
        "OriginationNumber": NotRequired[str],
        "SenderId": NotRequired[str],
        "EntityId": NotRequired[str],
        "TemplateId": NotRequired[str],
    },
)
ChannelResponseTypeDef = TypedDict(
    "ChannelResponseTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
ClosedDaysRuleTypeDef = TypedDict(
    "ClosedDaysRuleTypeDef",
    {
        "Name": NotRequired[str],
        "StartDateTime": NotRequired[str],
        "EndDateTime": NotRequired[str],
    },
)
WaitTimeTypeDef = TypedDict(
    "WaitTimeTypeDef",
    {
        "WaitFor": NotRequired[str],
        "WaitUntil": NotRequired[str],
    },
)
CreateApplicationRequestTypeDef = TypedDict(
    "CreateApplicationRequestTypeDef",
    {
        "Name": str,
        "tags": NotRequired[Mapping[str, str]],
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
CreateTemplateMessageBodyTypeDef = TypedDict(
    "CreateTemplateMessageBodyTypeDef",
    {
        "Arn": NotRequired[str],
        "Message": NotRequired[str],
        "RequestID": NotRequired[str],
    },
)
ExportJobRequestTypeDef = TypedDict(
    "ExportJobRequestTypeDef",
    {
        "RoleArn": str,
        "S3UrlPrefix": str,
        "SegmentId": NotRequired[str],
        "SegmentVersion": NotRequired[int],
    },
)
ImportJobRequestTypeDef = TypedDict(
    "ImportJobRequestTypeDef",
    {
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
        "DefineSegment": NotRequired[bool],
        "ExternalId": NotRequired[str],
        "RegisterEndpoints": NotRequired[bool],
        "SegmentId": NotRequired[str],
        "SegmentName": NotRequired[str],
    },
)
TemplateCreateMessageBodyTypeDef = TypedDict(
    "TemplateCreateMessageBodyTypeDef",
    {
        "Arn": NotRequired[str],
        "Message": NotRequired[str],
        "RequestID": NotRequired[str],
    },
)
CreateRecommenderConfigurationTypeDef = TypedDict(
    "CreateRecommenderConfigurationTypeDef",
    {
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
        "Attributes": NotRequired[Mapping[str, str]],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "RecommendationProviderIdType": NotRequired[str],
        "RecommendationTransformerUri": NotRequired[str],
        "RecommendationsDisplayName": NotRequired[str],
        "RecommendationsPerMessage": NotRequired[int],
    },
)
RecommenderConfigurationResponseTypeDef = TypedDict(
    "RecommenderConfigurationResponseTypeDef",
    {
        "CreationDate": str,
        "Id": str,
        "LastModifiedDate": str,
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
        "Attributes": NotRequired[Dict[str, str]],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "RecommendationProviderIdType": NotRequired[str],
        "RecommendationTransformerUri": NotRequired[str],
        "RecommendationsDisplayName": NotRequired[str],
        "RecommendationsPerMessage": NotRequired[int],
    },
)
SMSTemplateRequestTypeDef = TypedDict(
    "SMSTemplateRequestTypeDef",
    {
        "Body": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "RecommenderId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
    },
)
VoiceTemplateRequestTypeDef = TypedDict(
    "VoiceTemplateRequestTypeDef",
    {
        "Body": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
        "VoiceId": NotRequired[str],
    },
)
CustomDeliveryConfigurationTypeDef = TypedDict(
    "CustomDeliveryConfigurationTypeDef",
    {
        "DeliveryUri": str,
        "EndpointTypes": NotRequired[Sequence[EndpointTypesElementType]],
    },
)
JourneyCustomMessageTypeDef = TypedDict(
    "JourneyCustomMessageTypeDef",
    {
        "Data": NotRequired[str],
    },
)
DefaultButtonConfigurationTypeDef = TypedDict(
    "DefaultButtonConfigurationTypeDef",
    {
        "ButtonAction": ButtonActionType,
        "Text": str,
        "BackgroundColor": NotRequired[str],
        "BorderRadius": NotRequired[int],
        "Link": NotRequired[str],
        "TextColor": NotRequired[str],
    },
)
DefaultMessageTypeDef = TypedDict(
    "DefaultMessageTypeDef",
    {
        "Body": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
    },
)
DefaultPushNotificationMessageTypeDef = TypedDict(
    "DefaultPushNotificationMessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "SilentPush": NotRequired[bool],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
DefaultPushNotificationTemplateTypeDef = TypedDict(
    "DefaultPushNotificationTemplateTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "Sound": NotRequired[str],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
DeleteAdmChannelRequestRequestTypeDef = TypedDict(
    "DeleteAdmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
DeleteApnsChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
DeleteApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
DeleteApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsVoipChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
DeleteApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
DeleteBaiduChannelRequestRequestTypeDef = TypedDict(
    "DeleteBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)
DeleteEmailChannelRequestRequestTypeDef = TypedDict(
    "DeleteEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
EmailChannelResponseTypeDef = TypedDict(
    "EmailChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "ConfigurationSet": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "FromAddress": NotRequired[str],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "Identity": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "MessagesPerSecond": NotRequired[int],
        "RoleArn": NotRequired[str],
        "OrchestrationSendingRoleArn": NotRequired[str],
        "Version": NotRequired[int],
    },
)
DeleteEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
MessageBodyTypeDef = TypedDict(
    "MessageBodyTypeDef",
    {
        "Message": NotRequired[str],
        "RequestID": NotRequired[str],
    },
)
DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)
DeleteEventStreamRequestRequestTypeDef = TypedDict(
    "DeleteEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
EventStreamTypeDef = TypedDict(
    "EventStreamTypeDef",
    {
        "ApplicationId": str,
        "DestinationStreamArn": str,
        "RoleArn": str,
        "ExternalId": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "LastUpdatedBy": NotRequired[str],
    },
)
DeleteGcmChannelRequestRequestTypeDef = TypedDict(
    "DeleteGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GCMChannelResponseTypeDef = TypedDict(
    "GCMChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Credential": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasFcmServiceCredentials": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
DeleteInAppTemplateRequestRequestTypeDef = TypedDict(
    "DeleteInAppTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
DeleteJourneyRequestRequestTypeDef = TypedDict(
    "DeleteJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)
DeletePushTemplateRequestRequestTypeDef = TypedDict(
    "DeletePushTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
DeleteRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
    },
)
DeleteSegmentRequestRequestTypeDef = TypedDict(
    "DeleteSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)
DeleteSmsChannelRequestRequestTypeDef = TypedDict(
    "DeleteSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
SMSChannelResponseTypeDef = TypedDict(
    "SMSChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "PromotionalMessagesPerSecond": NotRequired[int],
        "SenderId": NotRequired[str],
        "ShortCode": NotRequired[str],
        "TransactionalMessagesPerSecond": NotRequired[int],
        "Version": NotRequired[int],
    },
)
DeleteSmsTemplateRequestRequestTypeDef = TypedDict(
    "DeleteSmsTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
DeleteUserEndpointsRequestRequestTypeDef = TypedDict(
    "DeleteUserEndpointsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "UserId": str,
    },
)
DeleteVoiceChannelRequestRequestTypeDef = TypedDict(
    "DeleteVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
VoiceChannelResponseTypeDef = TypedDict(
    "VoiceChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)
DeleteVoiceTemplateRequestRequestTypeDef = TypedDict(
    "DeleteVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
GCMMessageTypeDef = TypedDict(
    "GCMMessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "CollapseKey": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "IconReference": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "PreferredAuthenticationMethod": NotRequired[str],
        "Priority": NotRequired[str],
        "RawContent": NotRequired[str],
        "RestrictedPackageName": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "SmallImageIconUrl": NotRequired[str],
        "Sound": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "TimeToLive": NotRequired[int],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
SMSMessageTypeDef = TypedDict(
    "SMSMessageTypeDef",
    {
        "Body": NotRequired[str],
        "Keyword": NotRequired[str],
        "MediaUrl": NotRequired[str],
        "MessageType": NotRequired[MessageTypeType],
        "OriginationNumber": NotRequired[str],
        "SenderId": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "EntityId": NotRequired[str],
        "TemplateId": NotRequired[str],
    },
)
VoiceMessageTypeDef = TypedDict(
    "VoiceMessageTypeDef",
    {
        "Body": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "OriginationNumber": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "VoiceId": NotRequired[str],
    },
)
EmailChannelRequestTypeDef = TypedDict(
    "EmailChannelRequestTypeDef",
    {
        "FromAddress": str,
        "Identity": str,
        "ConfigurationSet": NotRequired[str],
        "Enabled": NotRequired[bool],
        "RoleArn": NotRequired[str],
        "OrchestrationSendingRoleArn": NotRequired[str],
    },
)
JourneyEmailMessageTypeDef = TypedDict(
    "JourneyEmailMessageTypeDef",
    {
        "FromAddress": NotRequired[str],
    },
)
EndpointDemographicTypeDef = TypedDict(
    "EndpointDemographicTypeDef",
    {
        "AppVersion": NotRequired[str],
        "Locale": NotRequired[str],
        "Make": NotRequired[str],
        "Model": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "Platform": NotRequired[str],
        "PlatformVersion": NotRequired[str],
        "Timezone": NotRequired[str],
    },
)
EndpointLocationTypeDef = TypedDict(
    "EndpointLocationTypeDef",
    {
        "City": NotRequired[str],
        "Country": NotRequired[str],
        "Latitude": NotRequired[float],
        "Longitude": NotRequired[float],
        "PostalCode": NotRequired[str],
        "Region": NotRequired[str],
    },
)
EndpointItemResponseTypeDef = TypedDict(
    "EndpointItemResponseTypeDef",
    {
        "Message": NotRequired[str],
        "StatusCode": NotRequired[int],
    },
)
EndpointMessageResultTypeDef = TypedDict(
    "EndpointMessageResultTypeDef",
    {
        "DeliveryStatus": DeliveryStatusType,
        "StatusCode": int,
        "Address": NotRequired[str],
        "MessageId": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "UpdatedToken": NotRequired[str],
    },
)
EndpointUserOutputTypeDef = TypedDict(
    "EndpointUserOutputTypeDef",
    {
        "UserAttributes": NotRequired[Dict[str, List[str]]],
        "UserId": NotRequired[str],
    },
)
EndpointSendConfigurationTypeDef = TypedDict(
    "EndpointSendConfigurationTypeDef",
    {
        "BodyOverride": NotRequired[str],
        "Context": NotRequired[Mapping[str, str]],
        "RawContent": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "TitleOverride": NotRequired[str],
    },
)
EndpointUserTypeDef = TypedDict(
    "EndpointUserTypeDef",
    {
        "UserAttributes": NotRequired[Mapping[str, Sequence[str]]],
        "UserId": NotRequired[str],
    },
)
MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "ComparisonOperator": str,
        "Value": float,
    },
)
SetDimensionOutputTypeDef = TypedDict(
    "SetDimensionOutputTypeDef",
    {
        "Values": List[str],
        "DimensionType": NotRequired[DimensionTypeType],
    },
)
EventItemResponseTypeDef = TypedDict(
    "EventItemResponseTypeDef",
    {
        "Message": NotRequired[str],
        "StatusCode": NotRequired[int],
    },
)
SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "Id": str,
        "StartTimestamp": str,
        "Duration": NotRequired[int],
        "StopTimestamp": NotRequired[str],
    },
)
ExportJobResourceTypeDef = TypedDict(
    "ExportJobResourceTypeDef",
    {
        "RoleArn": str,
        "S3UrlPrefix": str,
        "SegmentId": NotRequired[str],
        "SegmentVersion": NotRequired[int],
    },
)
GCMChannelRequestTypeDef = TypedDict(
    "GCMChannelRequestTypeDef",
    {
        "ApiKey": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "ServiceJson": NotRequired[str],
    },
)
GPSCoordinatesTypeDef = TypedDict(
    "GPSCoordinatesTypeDef",
    {
        "Latitude": float,
        "Longitude": float,
    },
)
GetAdmChannelRequestRequestTypeDef = TypedDict(
    "GetAdmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetApnsChannelRequestRequestTypeDef = TypedDict(
    "GetApnsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "GetApnsSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "GetApnsVoipChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetAppRequestRequestTypeDef = TypedDict(
    "GetAppRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
TimestampTypeDef = Union[datetime, str]
GetApplicationSettingsRequestRequestTypeDef = TypedDict(
    "GetApplicationSettingsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetAppsRequestRequestTypeDef = TypedDict(
    "GetAppsRequestRequestTypeDef",
    {
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetBaiduChannelRequestRequestTypeDef = TypedDict(
    "GetBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetCampaignActivitiesRequestRequestTypeDef = TypedDict(
    "GetCampaignActivitiesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetCampaignRequestRequestTypeDef = TypedDict(
    "GetCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)
GetCampaignVersionRequestRequestTypeDef = TypedDict(
    "GetCampaignVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "Version": str,
    },
)
GetCampaignVersionsRequestRequestTypeDef = TypedDict(
    "GetCampaignVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetCampaignsRequestRequestTypeDef = TypedDict(
    "GetCampaignsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetChannelsRequestRequestTypeDef = TypedDict(
    "GetChannelsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetEmailChannelRequestRequestTypeDef = TypedDict(
    "GetEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
GetEndpointRequestRequestTypeDef = TypedDict(
    "GetEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)
GetEventStreamRequestRequestTypeDef = TypedDict(
    "GetEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetExportJobRequestRequestTypeDef = TypedDict(
    "GetExportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JobId": str,
    },
)
GetExportJobsRequestRequestTypeDef = TypedDict(
    "GetExportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetGcmChannelRequestRequestTypeDef = TypedDict(
    "GetGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetImportJobRequestRequestTypeDef = TypedDict(
    "GetImportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JobId": str,
    },
)
GetImportJobsRequestRequestTypeDef = TypedDict(
    "GetImportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetInAppMessagesRequestRequestTypeDef = TypedDict(
    "GetInAppMessagesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)
GetInAppTemplateRequestRequestTypeDef = TypedDict(
    "GetInAppTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
GetJourneyExecutionActivityMetricsRequestRequestTypeDef = TypedDict(
    "GetJourneyExecutionActivityMetricsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)
JourneyExecutionActivityMetricsResponseTypeDef = TypedDict(
    "JourneyExecutionActivityMetricsResponseTypeDef",
    {
        "ActivityType": str,
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
    },
)
GetJourneyExecutionMetricsRequestRequestTypeDef = TypedDict(
    "GetJourneyExecutionMetricsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)
JourneyExecutionMetricsResponseTypeDef = TypedDict(
    "JourneyExecutionMetricsResponseTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
    },
)
GetJourneyRequestRequestTypeDef = TypedDict(
    "GetJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)
GetJourneyRunExecutionActivityMetricsRequestRequestTypeDef = TypedDict(
    "GetJourneyRunExecutionActivityMetricsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
        "RunId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)
JourneyRunExecutionActivityMetricsResponseTypeDef = TypedDict(
    "JourneyRunExecutionActivityMetricsResponseTypeDef",
    {
        "ActivityType": str,
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
        "RunId": str,
    },
)
GetJourneyRunExecutionMetricsRequestRequestTypeDef = TypedDict(
    "GetJourneyRunExecutionMetricsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "RunId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)
JourneyRunExecutionMetricsResponseTypeDef = TypedDict(
    "JourneyRunExecutionMetricsResponseTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
        "RunId": str,
    },
)
GetJourneyRunsRequestRequestTypeDef = TypedDict(
    "GetJourneyRunsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetPushTemplateRequestRequestTypeDef = TypedDict(
    "GetPushTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
GetRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "GetRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
    },
)
GetRecommenderConfigurationsRequestRequestTypeDef = TypedDict(
    "GetRecommenderConfigurationsRequestRequestTypeDef",
    {
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetSegmentExportJobsRequestRequestTypeDef = TypedDict(
    "GetSegmentExportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetSegmentImportJobsRequestRequestTypeDef = TypedDict(
    "GetSegmentImportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetSegmentRequestRequestTypeDef = TypedDict(
    "GetSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)
GetSegmentVersionRequestRequestTypeDef = TypedDict(
    "GetSegmentVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "Version": str,
    },
)
GetSegmentVersionsRequestRequestTypeDef = TypedDict(
    "GetSegmentVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetSegmentsRequestRequestTypeDef = TypedDict(
    "GetSegmentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
GetSmsChannelRequestRequestTypeDef = TypedDict(
    "GetSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetSmsTemplateRequestRequestTypeDef = TypedDict(
    "GetSmsTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
SMSTemplateResponseTypeDef = TypedDict(
    "SMSTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "Body": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "RecommenderId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)
GetUserEndpointsRequestRequestTypeDef = TypedDict(
    "GetUserEndpointsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "UserId": str,
    },
)
GetVoiceChannelRequestRequestTypeDef = TypedDict(
    "GetVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetVoiceTemplateRequestRequestTypeDef = TypedDict(
    "GetVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)
VoiceTemplateResponseTypeDef = TypedDict(
    "VoiceTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "Body": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
        "VoiceId": NotRequired[str],
    },
)
ImportJobResourceTypeDef = TypedDict(
    "ImportJobResourceTypeDef",
    {
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
        "DefineSegment": NotRequired[bool],
        "ExternalId": NotRequired[str],
        "RegisterEndpoints": NotRequired[bool],
        "SegmentId": NotRequired[str],
        "SegmentName": NotRequired[str],
    },
)
InAppMessageBodyConfigTypeDef = TypedDict(
    "InAppMessageBodyConfigTypeDef",
    {
        "Alignment": AlignmentType,
        "Body": str,
        "TextColor": str,
    },
)
OverrideButtonConfigurationTypeDef = TypedDict(
    "OverrideButtonConfigurationTypeDef",
    {
        "ButtonAction": ButtonActionType,
        "Link": NotRequired[str],
    },
)
InAppMessageHeaderConfigTypeDef = TypedDict(
    "InAppMessageHeaderConfigTypeDef",
    {
        "Alignment": AlignmentType,
        "Header": str,
        "TextColor": str,
    },
)
JourneyChannelSettingsTypeDef = TypedDict(
    "JourneyChannelSettingsTypeDef",
    {
        "ConnectCampaignArn": NotRequired[str],
        "ConnectCampaignExecutionRoleArn": NotRequired[str],
    },
)
JourneyPushMessageTypeDef = TypedDict(
    "JourneyPushMessageTypeDef",
    {
        "TimeToLive": NotRequired[str],
    },
)
JourneyScheduleOutputTypeDef = TypedDict(
    "JourneyScheduleOutputTypeDef",
    {
        "EndTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "Timezone": NotRequired[str],
    },
)
JourneyRunResponseTypeDef = TypedDict(
    "JourneyRunResponseTypeDef",
    {
        "CreationTime": str,
        "LastUpdateTime": str,
        "RunId": str,
        "Status": JourneyRunStatusType,
    },
)
JourneySMSMessageTypeDef = TypedDict(
    "JourneySMSMessageTypeDef",
    {
        "MessageType": NotRequired[MessageTypeType],
        "OriginationNumber": NotRequired[str],
        "SenderId": NotRequired[str],
        "EntityId": NotRequired[str],
        "TemplateId": NotRequired[str],
    },
)
JourneyStateRequestTypeDef = TypedDict(
    "JourneyStateRequestTypeDef",
    {
        "State": NotRequired[StateType],
    },
)
ListJourneysRequestRequestTypeDef = TypedDict(
    "ListJourneysRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TagsModelOutputTypeDef = TypedDict(
    "TagsModelOutputTypeDef",
    {
        "tags": Dict[str, str],
    },
)
ListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "ListTemplateVersionsRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateType": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)
ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
        "Prefix": NotRequired[str],
        "TemplateType": NotRequired[str],
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageSmallIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "JsonBody": NotRequired[str],
        "MediaUrl": NotRequired[str],
        "RawContent": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "TimeToLive": NotRequired[int],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)
MessageResultTypeDef = TypedDict(
    "MessageResultTypeDef",
    {
        "DeliveryStatus": DeliveryStatusType,
        "StatusCode": int,
        "MessageId": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "UpdatedToken": NotRequired[str],
    },
)
NumberValidateRequestTypeDef = TypedDict(
    "NumberValidateRequestTypeDef",
    {
        "IsoCountryCode": NotRequired[str],
        "PhoneNumber": NotRequired[str],
    },
)
NumberValidateResponseTypeDef = TypedDict(
    "NumberValidateResponseTypeDef",
    {
        "Carrier": NotRequired[str],
        "City": NotRequired[str],
        "CleansedPhoneNumberE164": NotRequired[str],
        "CleansedPhoneNumberNational": NotRequired[str],
        "Country": NotRequired[str],
        "CountryCodeIso2": NotRequired[str],
        "CountryCodeNumeric": NotRequired[str],
        "County": NotRequired[str],
        "OriginalCountryCodeIso2": NotRequired[str],
        "OriginalPhoneNumber": NotRequired[str],
        "PhoneType": NotRequired[str],
        "PhoneTypeCode": NotRequired[int],
        "Timezone": NotRequired[str],
        "ZipCode": NotRequired[str],
    },
)
OpenHoursRuleTypeDef = TypedDict(
    "OpenHoursRuleTypeDef",
    {
        "StartTime": NotRequired[str],
        "EndTime": NotRequired[str],
    },
)
WriteEventStreamTypeDef = TypedDict(
    "WriteEventStreamTypeDef",
    {
        "DestinationStreamArn": str,
        "RoleArn": str,
    },
)
RandomSplitEntryTypeDef = TypedDict(
    "RandomSplitEntryTypeDef",
    {
        "NextActivity": NotRequired[str],
        "Percentage": NotRequired[int],
    },
)
RecencyDimensionTypeDef = TypedDict(
    "RecencyDimensionTypeDef",
    {
        "Duration": DurationType,
        "RecencyType": RecencyTypeType,
    },
)
UpdateAttributesRequestTypeDef = TypedDict(
    "UpdateAttributesRequestTypeDef",
    {
        "Blacklist": NotRequired[Sequence[str]],
    },
)
ResultRowValueTypeDef = TypedDict(
    "ResultRowValueTypeDef",
    {
        "Key": str,
        "Type": str,
        "Value": str,
    },
)
SMSChannelRequestTypeDef = TypedDict(
    "SMSChannelRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
        "SenderId": NotRequired[str],
        "ShortCode": NotRequired[str],
    },
)
SegmentConditionTypeDef = TypedDict(
    "SegmentConditionTypeDef",
    {
        "SegmentId": str,
    },
)
SegmentReferenceTypeDef = TypedDict(
    "SegmentReferenceTypeDef",
    {
        "Id": str,
        "Version": NotRequired[int],
    },
)
SegmentImportResourceTypeDef = TypedDict(
    "SegmentImportResourceTypeDef",
    {
        "ExternalId": str,
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
        "Size": int,
        "ChannelCounts": NotRequired[Dict[str, int]],
    },
)
SendOTPMessageRequestParametersTypeDef = TypedDict(
    "SendOTPMessageRequestParametersTypeDef",
    {
        "BrandName": str,
        "Channel": str,
        "DestinationIdentity": str,
        "OriginationIdentity": str,
        "ReferenceId": str,
        "AllowedAttempts": NotRequired[int],
        "CodeLength": NotRequired[int],
        "EntityId": NotRequired[str],
        "Language": NotRequired[str],
        "TemplateId": NotRequired[str],
        "ValidityPeriod": NotRequired[int],
    },
)
SetDimensionTypeDef = TypedDict(
    "SetDimensionTypeDef",
    {
        "Values": Sequence[str],
        "DimensionType": NotRequired[DimensionTypeType],
    },
)
SimpleEmailPartTypeDef = TypedDict(
    "SimpleEmailPartTypeDef",
    {
        "Charset": NotRequired[str],
        "Data": NotRequired[str],
    },
)
TagsModelTypeDef = TypedDict(
    "TagsModelTypeDef",
    {
        "tags": Mapping[str, str],
    },
)
TemplateActiveVersionRequestTypeDef = TypedDict(
    "TemplateActiveVersionRequestTypeDef",
    {
        "Version": NotRequired[str],
    },
)
TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
TemplateResponseTypeDef = TypedDict(
    "TemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)
TemplateVersionResponseTypeDef = TypedDict(
    "TemplateVersionResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": str,
        "DefaultSubstitutions": NotRequired[str],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateRecommenderConfigurationTypeDef = TypedDict(
    "UpdateRecommenderConfigurationTypeDef",
    {
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
        "Attributes": NotRequired[Mapping[str, str]],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "RecommendationProviderIdType": NotRequired[str],
        "RecommendationTransformerUri": NotRequired[str],
        "RecommendationsDisplayName": NotRequired[str],
        "RecommendationsPerMessage": NotRequired[int],
    },
)
VoiceChannelRequestTypeDef = TypedDict(
    "VoiceChannelRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
VerificationResponseTypeDef = TypedDict(
    "VerificationResponseTypeDef",
    {
        "Valid": NotRequired[bool],
    },
)
VerifyOTPMessageRequestParametersTypeDef = TypedDict(
    "VerifyOTPMessageRequestParametersTypeDef",
    {
        "DestinationIdentity": str,
        "Otp": str,
        "ReferenceId": str,
    },
)
UpdateAdmChannelRequestRequestTypeDef = TypedDict(
    "UpdateAdmChannelRequestRequestTypeDef",
    {
        "ADMChannelRequest": ADMChannelRequestTypeDef,
        "ApplicationId": str,
    },
)
UpdateApnsChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsChannelRequestRequestTypeDef",
    {
        "APNSChannelRequest": APNSChannelRequestTypeDef,
        "ApplicationId": str,
    },
)
UpdateApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsSandboxChannelRequestRequestTypeDef",
    {
        "APNSSandboxChannelRequest": APNSSandboxChannelRequestTypeDef,
        "ApplicationId": str,
    },
)
UpdateApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsVoipChannelRequestRequestTypeDef",
    {
        "APNSVoipChannelRequest": APNSVoipChannelRequestTypeDef,
        "ApplicationId": str,
    },
)
UpdateApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "APNSVoipSandboxChannelRequest": APNSVoipSandboxChannelRequestTypeDef,
        "ApplicationId": str,
    },
)
ActivitiesResponseTypeDef = TypedDict(
    "ActivitiesResponseTypeDef",
    {
        "Item": List[ActivityResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
ApplicationsResponseTypeDef = TypedDict(
    "ApplicationsResponseTypeDef",
    {
        "Item": NotRequired[List[ApplicationResponseTypeDef]],
        "NextToken": NotRequired[str],
    },
)
ApplicationSettingsJourneyLimitsTypeDef = TypedDict(
    "ApplicationSettingsJourneyLimitsTypeDef",
    {
        "DailyCap": NotRequired[int],
        "TimeframeCap": NotRequired[JourneyTimeframeCapTypeDef],
        "TotalCap": NotRequired[int],
    },
)
JourneyLimitsTypeDef = TypedDict(
    "JourneyLimitsTypeDef",
    {
        "DailyCap": NotRequired[int],
        "EndpointReentryCap": NotRequired[int],
        "MessagesPerSecond": NotRequired[int],
        "EndpointReentryInterval": NotRequired[str],
        "TimeframeCap": NotRequired[JourneyTimeframeCapTypeDef],
        "TotalCap": NotRequired[int],
    },
)
AttributeDimensionUnionTypeDef = Union[AttributeDimensionTypeDef, AttributeDimensionOutputTypeDef]
UpdateBaiduChannelRequestRequestTypeDef = TypedDict(
    "UpdateBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "BaiduChannelRequest": BaiduChannelRequestTypeDef,
    },
)
RawEmailTypeDef = TypedDict(
    "RawEmailTypeDef",
    {
        "Data": NotRequired[BlobTypeDef],
    },
)
CampaignEmailMessageOutputTypeDef = TypedDict(
    "CampaignEmailMessageOutputTypeDef",
    {
        "Body": NotRequired[str],
        "FromAddress": NotRequired[str],
        "Headers": NotRequired[List[MessageHeaderTypeDef]],
        "HtmlBody": NotRequired[str],
        "Title": NotRequired[str],
    },
)
CampaignEmailMessageTypeDef = TypedDict(
    "CampaignEmailMessageTypeDef",
    {
        "Body": NotRequired[str],
        "FromAddress": NotRequired[str],
        "Headers": NotRequired[Sequence[MessageHeaderTypeDef]],
        "HtmlBody": NotRequired[str],
        "Title": NotRequired[str],
    },
)
EmailTemplateRequestTypeDef = TypedDict(
    "EmailTemplateRequestTypeDef",
    {
        "DefaultSubstitutions": NotRequired[str],
        "HtmlPart": NotRequired[str],
        "RecommenderId": NotRequired[str],
        "Subject": NotRequired[str],
        "Headers": NotRequired[Sequence[MessageHeaderTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
        "TextPart": NotRequired[str],
    },
)
EmailTemplateResponseTypeDef = TypedDict(
    "EmailTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "HtmlPart": NotRequired[str],
        "RecommenderId": NotRequired[str],
        "Subject": NotRequired[str],
        "Headers": NotRequired[List[MessageHeaderTypeDef]],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "TextPart": NotRequired[str],
        "Version": NotRequired[str],
    },
)
ChannelsResponseTypeDef = TypedDict(
    "ChannelsResponseTypeDef",
    {
        "Channels": Dict[str, ChannelResponseTypeDef],
    },
)
ClosedDaysOutputTypeDef = TypedDict(
    "ClosedDaysOutputTypeDef",
    {
        "EMAIL": NotRequired[List[ClosedDaysRuleTypeDef]],
        "SMS": NotRequired[List[ClosedDaysRuleTypeDef]],
        "PUSH": NotRequired[List[ClosedDaysRuleTypeDef]],
        "VOICE": NotRequired[List[ClosedDaysRuleTypeDef]],
        "CUSTOM": NotRequired[List[ClosedDaysRuleTypeDef]],
    },
)
ClosedDaysTypeDef = TypedDict(
    "ClosedDaysTypeDef",
    {
        "EMAIL": NotRequired[Sequence[ClosedDaysRuleTypeDef]],
        "SMS": NotRequired[Sequence[ClosedDaysRuleTypeDef]],
        "PUSH": NotRequired[Sequence[ClosedDaysRuleTypeDef]],
        "VOICE": NotRequired[Sequence[ClosedDaysRuleTypeDef]],
        "CUSTOM": NotRequired[Sequence[ClosedDaysRuleTypeDef]],
    },
)
WaitActivityTypeDef = TypedDict(
    "WaitActivityTypeDef",
    {
        "NextActivity": NotRequired[str],
        "WaitTime": NotRequired[WaitTimeTypeDef],
    },
)
CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "CreateApplicationRequest": CreateApplicationRequestTypeDef,
    },
)
CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "ApplicationResponse": ApplicationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAdmChannelResponseTypeDef = TypedDict(
    "DeleteAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": ADMChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApnsChannelResponseTypeDef = TypedDict(
    "DeleteApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": APNSChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApnsSandboxChannelResponseTypeDef = TypedDict(
    "DeleteApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": APNSSandboxChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApnsVoipChannelResponseTypeDef = TypedDict(
    "DeleteApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": APNSVoipChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": APNSVoipSandboxChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAppResponseTypeDef = TypedDict(
    "DeleteAppResponseTypeDef",
    {
        "ApplicationResponse": ApplicationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBaiduChannelResponseTypeDef = TypedDict(
    "DeleteBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": BaiduChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAdmChannelResponseTypeDef = TypedDict(
    "GetAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": ADMChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApnsChannelResponseTypeDef = TypedDict(
    "GetApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": APNSChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApnsSandboxChannelResponseTypeDef = TypedDict(
    "GetApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": APNSSandboxChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApnsVoipChannelResponseTypeDef = TypedDict(
    "GetApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": APNSVoipChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": APNSVoipSandboxChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "ApplicationResponse": ApplicationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBaiduChannelResponseTypeDef = TypedDict(
    "GetBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": BaiduChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveAttributesResponseTypeDef = TypedDict(
    "RemoveAttributesResponseTypeDef",
    {
        "AttributesResource": AttributesResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAdmChannelResponseTypeDef = TypedDict(
    "UpdateAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": ADMChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApnsChannelResponseTypeDef = TypedDict(
    "UpdateApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": APNSChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApnsSandboxChannelResponseTypeDef = TypedDict(
    "UpdateApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": APNSSandboxChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApnsVoipChannelResponseTypeDef = TypedDict(
    "UpdateApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": APNSVoipChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": APNSVoipSandboxChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBaiduChannelResponseTypeDef = TypedDict(
    "UpdateBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": BaiduChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEmailTemplateResponseTypeDef = TypedDict(
    "CreateEmailTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": CreateTemplateMessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePushTemplateResponseTypeDef = TypedDict(
    "CreatePushTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": CreateTemplateMessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSmsTemplateResponseTypeDef = TypedDict(
    "CreateSmsTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": CreateTemplateMessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVoiceTemplateResponseTypeDef = TypedDict(
    "CreateVoiceTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": CreateTemplateMessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExportJobRequestRequestTypeDef = TypedDict(
    "CreateExportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ExportJobRequest": ExportJobRequestTypeDef,
    },
)
CreateImportJobRequestRequestTypeDef = TypedDict(
    "CreateImportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ImportJobRequest": ImportJobRequestTypeDef,
    },
)
CreateInAppTemplateResponseTypeDef = TypedDict(
    "CreateInAppTemplateResponseTypeDef",
    {
        "TemplateCreateMessageBody": TemplateCreateMessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "CreateRecommenderConfigurationRequestRequestTypeDef",
    {
        "CreateRecommenderConfiguration": CreateRecommenderConfigurationTypeDef,
    },
)
CreateRecommenderConfigurationResponseTypeDef = TypedDict(
    "CreateRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": RecommenderConfigurationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRecommenderConfigurationResponseTypeDef = TypedDict(
    "DeleteRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": RecommenderConfigurationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommenderConfigurationResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": RecommenderConfigurationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecommenderConfigurationsResponseTypeDef = TypedDict(
    "ListRecommenderConfigurationsResponseTypeDef",
    {
        "Item": List[RecommenderConfigurationResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
UpdateRecommenderConfigurationResponseTypeDef = TypedDict(
    "UpdateRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": RecommenderConfigurationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSmsTemplateRequestRequestTypeDef = TypedDict(
    "CreateSmsTemplateRequestRequestTypeDef",
    {
        "SMSTemplateRequest": SMSTemplateRequestTypeDef,
        "TemplateName": str,
    },
)
UpdateSmsTemplateRequestRequestTypeDef = TypedDict(
    "UpdateSmsTemplateRequestRequestTypeDef",
    {
        "SMSTemplateRequest": SMSTemplateRequestTypeDef,
        "TemplateName": str,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)
CreateVoiceTemplateRequestRequestTypeDef = TypedDict(
    "CreateVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "VoiceTemplateRequest": VoiceTemplateRequestTypeDef,
    },
)
UpdateVoiceTemplateRequestRequestTypeDef = TypedDict(
    "UpdateVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "VoiceTemplateRequest": VoiceTemplateRequestTypeDef,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)
CustomDeliveryConfigurationUnionTypeDef = Union[
    CustomDeliveryConfigurationTypeDef, CustomDeliveryConfigurationOutputTypeDef
]
CustomMessageActivityOutputTypeDef = TypedDict(
    "CustomMessageActivityOutputTypeDef",
    {
        "DeliveryUri": NotRequired[str],
        "EndpointTypes": NotRequired[List[EndpointTypesElementType]],
        "MessageConfig": NotRequired[JourneyCustomMessageTypeDef],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)
CustomMessageActivityTypeDef = TypedDict(
    "CustomMessageActivityTypeDef",
    {
        "DeliveryUri": NotRequired[str],
        "EndpointTypes": NotRequired[Sequence[EndpointTypesElementType]],
        "MessageConfig": NotRequired[JourneyCustomMessageTypeDef],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)
PushNotificationTemplateRequestTypeDef = TypedDict(
    "PushNotificationTemplateRequestTypeDef",
    {
        "ADM": NotRequired[AndroidPushNotificationTemplateTypeDef],
        "APNS": NotRequired[APNSPushNotificationTemplateTypeDef],
        "Baidu": NotRequired[AndroidPushNotificationTemplateTypeDef],
        "Default": NotRequired[DefaultPushNotificationTemplateTypeDef],
        "DefaultSubstitutions": NotRequired[str],
        "GCM": NotRequired[AndroidPushNotificationTemplateTypeDef],
        "RecommenderId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
    },
)
PushNotificationTemplateResponseTypeDef = TypedDict(
    "PushNotificationTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "ADM": NotRequired[AndroidPushNotificationTemplateTypeDef],
        "APNS": NotRequired[APNSPushNotificationTemplateTypeDef],
        "Arn": NotRequired[str],
        "Baidu": NotRequired[AndroidPushNotificationTemplateTypeDef],
        "Default": NotRequired[DefaultPushNotificationTemplateTypeDef],
        "DefaultSubstitutions": NotRequired[str],
        "GCM": NotRequired[AndroidPushNotificationTemplateTypeDef],
        "RecommenderId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)
DeleteEmailChannelResponseTypeDef = TypedDict(
    "DeleteEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": EmailChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEmailChannelResponseTypeDef = TypedDict(
    "GetEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": EmailChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEmailChannelResponseTypeDef = TypedDict(
    "UpdateEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": EmailChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEmailTemplateResponseTypeDef = TypedDict(
    "DeleteEmailTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInAppTemplateResponseTypeDef = TypedDict(
    "DeleteInAppTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePushTemplateResponseTypeDef = TypedDict(
    "DeletePushTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSmsTemplateResponseTypeDef = TypedDict(
    "DeleteSmsTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVoiceTemplateResponseTypeDef = TypedDict(
    "DeleteVoiceTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEmailTemplateResponseTypeDef = TypedDict(
    "UpdateEmailTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEndpointResponseTypeDef = TypedDict(
    "UpdateEndpointResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEndpointsBatchResponseTypeDef = TypedDict(
    "UpdateEndpointsBatchResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateInAppTemplateResponseTypeDef = TypedDict(
    "UpdateInAppTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePushTemplateResponseTypeDef = TypedDict(
    "UpdatePushTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSmsTemplateResponseTypeDef = TypedDict(
    "UpdateSmsTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTemplateActiveVersionResponseTypeDef = TypedDict(
    "UpdateTemplateActiveVersionResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVoiceTemplateResponseTypeDef = TypedDict(
    "UpdateVoiceTemplateResponseTypeDef",
    {
        "MessageBody": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEventStreamResponseTypeDef = TypedDict(
    "DeleteEventStreamResponseTypeDef",
    {
        "EventStream": EventStreamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEventStreamResponseTypeDef = TypedDict(
    "GetEventStreamResponseTypeDef",
    {
        "EventStream": EventStreamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutEventStreamResponseTypeDef = TypedDict(
    "PutEventStreamResponseTypeDef",
    {
        "EventStream": EventStreamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGcmChannelResponseTypeDef = TypedDict(
    "DeleteGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": GCMChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGcmChannelResponseTypeDef = TypedDict(
    "GetGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": GCMChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGcmChannelResponseTypeDef = TypedDict(
    "UpdateGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": GCMChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSmsChannelResponseTypeDef = TypedDict(
    "DeleteSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": SMSChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSmsChannelResponseTypeDef = TypedDict(
    "GetSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": SMSChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSmsChannelResponseTypeDef = TypedDict(
    "UpdateSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": SMSChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVoiceChannelResponseTypeDef = TypedDict(
    "DeleteVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": VoiceChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceChannelResponseTypeDef = TypedDict(
    "GetVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": VoiceChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVoiceChannelResponseTypeDef = TypedDict(
    "UpdateVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": VoiceChannelResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEmailChannelRequestRequestTypeDef = TypedDict(
    "UpdateEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EmailChannelRequest": EmailChannelRequestTypeDef,
    },
)
EmailMessageActivityTypeDef = TypedDict(
    "EmailMessageActivityTypeDef",
    {
        "MessageConfig": NotRequired[JourneyEmailMessageTypeDef],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)
SendUsersMessageResponseTypeDef = TypedDict(
    "SendUsersMessageResponseTypeDef",
    {
        "ApplicationId": str,
        "RequestId": NotRequired[str],
        "Result": NotRequired[Dict[str, Dict[str, EndpointMessageResultTypeDef]]],
    },
)
EndpointResponseTypeDef = TypedDict(
    "EndpointResponseTypeDef",
    {
        "Address": NotRequired[str],
        "ApplicationId": NotRequired[str],
        "Attributes": NotRequired[Dict[str, List[str]]],
        "ChannelType": NotRequired[ChannelTypeType],
        "CohortId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Demographic": NotRequired[EndpointDemographicTypeDef],
        "EffectiveDate": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "Id": NotRequired[str],
        "Location": NotRequired[EndpointLocationTypeDef],
        "Metrics": NotRequired[Dict[str, float]],
        "OptOut": NotRequired[str],
        "RequestId": NotRequired[str],
        "User": NotRequired[EndpointUserOutputTypeDef],
    },
)
EndpointUserUnionTypeDef = Union[EndpointUserTypeDef, EndpointUserOutputTypeDef]
EventDimensionsOutputTypeDef = TypedDict(
    "EventDimensionsOutputTypeDef",
    {
        "Attributes": NotRequired[Dict[str, AttributeDimensionOutputTypeDef]],
        "EventType": NotRequired[SetDimensionOutputTypeDef],
        "Metrics": NotRequired[Dict[str, MetricDimensionTypeDef]],
    },
)
SegmentDemographicsOutputTypeDef = TypedDict(
    "SegmentDemographicsOutputTypeDef",
    {
        "AppVersion": NotRequired[SetDimensionOutputTypeDef],
        "Channel": NotRequired[SetDimensionOutputTypeDef],
        "DeviceType": NotRequired[SetDimensionOutputTypeDef],
        "Make": NotRequired[SetDimensionOutputTypeDef],
        "Model": NotRequired[SetDimensionOutputTypeDef],
        "Platform": NotRequired[SetDimensionOutputTypeDef],
    },
)
ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "EndpointItemResponse": NotRequired[EndpointItemResponseTypeDef],
        "EventsItemResponse": NotRequired[Dict[str, EventItemResponseTypeDef]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventType": str,
        "Timestamp": str,
        "AppPackageName": NotRequired[str],
        "AppTitle": NotRequired[str],
        "AppVersionCode": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "ClientSdkVersion": NotRequired[str],
        "Metrics": NotRequired[Mapping[str, float]],
        "SdkName": NotRequired[str],
        "Session": NotRequired[SessionTypeDef],
    },
)
ExportJobResponseTypeDef = TypedDict(
    "ExportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": ExportJobResourceTypeDef,
        "Id": str,
        "JobStatus": JobStatusType,
        "Type": str,
        "CompletedPieces": NotRequired[int],
        "CompletionDate": NotRequired[str],
        "FailedPieces": NotRequired[int],
        "Failures": NotRequired[List[str]],
        "TotalFailures": NotRequired[int],
        "TotalPieces": NotRequired[int],
        "TotalProcessed": NotRequired[int],
    },
)
UpdateGcmChannelRequestRequestTypeDef = TypedDict(
    "UpdateGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "GCMChannelRequest": GCMChannelRequestTypeDef,
    },
)
GPSPointDimensionTypeDef = TypedDict(
    "GPSPointDimensionTypeDef",
    {
        "Coordinates": GPSCoordinatesTypeDef,
        "RangeInKilometers": NotRequired[float],
    },
)
GetApplicationDateRangeKpiRequestRequestTypeDef = TypedDict(
    "GetApplicationDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "KpiName": str,
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
GetCampaignDateRangeKpiRequestRequestTypeDef = TypedDict(
    "GetCampaignDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "KpiName": str,
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
GetJourneyDateRangeKpiRequestRequestTypeDef = TypedDict(
    "GetJourneyDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "KpiName": str,
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
JourneyScheduleTypeDef = TypedDict(
    "JourneyScheduleTypeDef",
    {
        "EndTime": NotRequired[TimestampTypeDef],
        "StartTime": NotRequired[TimestampTypeDef],
        "Timezone": NotRequired[str],
    },
)
GetJourneyExecutionActivityMetricsResponseTypeDef = TypedDict(
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    {
        "JourneyExecutionActivityMetricsResponse": JourneyExecutionActivityMetricsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJourneyExecutionMetricsResponseTypeDef = TypedDict(
    "GetJourneyExecutionMetricsResponseTypeDef",
    {
        "JourneyExecutionMetricsResponse": JourneyExecutionMetricsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJourneyRunExecutionActivityMetricsResponseTypeDef = TypedDict(
    "GetJourneyRunExecutionActivityMetricsResponseTypeDef",
    {
        "JourneyRunExecutionActivityMetricsResponse": JourneyRunExecutionActivityMetricsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJourneyRunExecutionMetricsResponseTypeDef = TypedDict(
    "GetJourneyRunExecutionMetricsResponseTypeDef",
    {
        "JourneyRunExecutionMetricsResponse": JourneyRunExecutionMetricsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSmsTemplateResponseTypeDef = TypedDict(
    "GetSmsTemplateResponseTypeDef",
    {
        "SMSTemplateResponse": SMSTemplateResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceTemplateResponseTypeDef = TypedDict(
    "GetVoiceTemplateResponseTypeDef",
    {
        "VoiceTemplateResponse": VoiceTemplateResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportJobResponseTypeDef = TypedDict(
    "ImportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": ImportJobResourceTypeDef,
        "Id": str,
        "JobStatus": JobStatusType,
        "Type": str,
        "CompletedPieces": NotRequired[int],
        "CompletionDate": NotRequired[str],
        "FailedPieces": NotRequired[int],
        "Failures": NotRequired[List[str]],
        "TotalFailures": NotRequired[int],
        "TotalPieces": NotRequired[int],
        "TotalProcessed": NotRequired[int],
    },
)
InAppMessageButtonTypeDef = TypedDict(
    "InAppMessageButtonTypeDef",
    {
        "Android": NotRequired[OverrideButtonConfigurationTypeDef],
        "DefaultConfig": NotRequired[DefaultButtonConfigurationTypeDef],
        "IOS": NotRequired[OverrideButtonConfigurationTypeDef],
        "Web": NotRequired[OverrideButtonConfigurationTypeDef],
    },
)
PushMessageActivityTypeDef = TypedDict(
    "PushMessageActivityTypeDef",
    {
        "MessageConfig": NotRequired[JourneyPushMessageTypeDef],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)
JourneyRunsResponseTypeDef = TypedDict(
    "JourneyRunsResponseTypeDef",
    {
        "Item": List[JourneyRunResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
SMSMessageActivityTypeDef = TypedDict(
    "SMSMessageActivityTypeDef",
    {
        "MessageConfig": NotRequired[JourneySMSMessageTypeDef],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)
UpdateJourneyStateRequestRequestTypeDef = TypedDict(
    "UpdateJourneyStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "JourneyStateRequest": JourneyStateRequestTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagsModel": TagsModelOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MessageResponseTypeDef = TypedDict(
    "MessageResponseTypeDef",
    {
        "ApplicationId": str,
        "EndpointResult": NotRequired[Dict[str, EndpointMessageResultTypeDef]],
        "RequestId": NotRequired[str],
        "Result": NotRequired[Dict[str, MessageResultTypeDef]],
    },
)
PhoneNumberValidateRequestRequestTypeDef = TypedDict(
    "PhoneNumberValidateRequestRequestTypeDef",
    {
        "NumberValidateRequest": NumberValidateRequestTypeDef,
    },
)
PhoneNumberValidateResponseTypeDef = TypedDict(
    "PhoneNumberValidateResponseTypeDef",
    {
        "NumberValidateResponse": NumberValidateResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OpenHoursOutputTypeDef = TypedDict(
    "OpenHoursOutputTypeDef",
    {
        "EMAIL": NotRequired[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]],
        "SMS": NotRequired[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]],
        "PUSH": NotRequired[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]],
        "VOICE": NotRequired[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]],
        "CUSTOM": NotRequired[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]],
    },
)
OpenHoursTypeDef = TypedDict(
    "OpenHoursTypeDef",
    {
        "EMAIL": NotRequired[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]],
        "SMS": NotRequired[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]],
        "PUSH": NotRequired[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]],
        "VOICE": NotRequired[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]],
        "CUSTOM": NotRequired[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]],
    },
)
PutEventStreamRequestRequestTypeDef = TypedDict(
    "PutEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteEventStream": WriteEventStreamTypeDef,
    },
)
RandomSplitActivityOutputTypeDef = TypedDict(
    "RandomSplitActivityOutputTypeDef",
    {
        "Branches": NotRequired[List[RandomSplitEntryTypeDef]],
    },
)
RandomSplitActivityTypeDef = TypedDict(
    "RandomSplitActivityTypeDef",
    {
        "Branches": NotRequired[Sequence[RandomSplitEntryTypeDef]],
    },
)
SegmentBehaviorsTypeDef = TypedDict(
    "SegmentBehaviorsTypeDef",
    {
        "Recency": NotRequired[RecencyDimensionTypeDef],
    },
)
RemoveAttributesRequestRequestTypeDef = TypedDict(
    "RemoveAttributesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "AttributeType": str,
        "UpdateAttributesRequest": UpdateAttributesRequestTypeDef,
    },
)
ResultRowTypeDef = TypedDict(
    "ResultRowTypeDef",
    {
        "GroupedBys": List[ResultRowValueTypeDef],
        "Values": List[ResultRowValueTypeDef],
    },
)
UpdateSmsChannelRequestRequestTypeDef = TypedDict(
    "UpdateSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SMSChannelRequest": SMSChannelRequestTypeDef,
    },
)
SendOTPMessageRequestRequestTypeDef = TypedDict(
    "SendOTPMessageRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SendOTPMessageRequestParameters": SendOTPMessageRequestParametersTypeDef,
    },
)
SetDimensionUnionTypeDef = Union[SetDimensionTypeDef, SetDimensionOutputTypeDef]
SimpleEmailTypeDef = TypedDict(
    "SimpleEmailTypeDef",
    {
        "HtmlPart": NotRequired[SimpleEmailPartTypeDef],
        "Subject": NotRequired[SimpleEmailPartTypeDef],
        "TextPart": NotRequired[SimpleEmailPartTypeDef],
        "Headers": NotRequired[Sequence[MessageHeaderTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsModel": TagsModelTypeDef,
    },
)
UpdateTemplateActiveVersionRequestRequestTypeDef = TypedDict(
    "UpdateTemplateActiveVersionRequestRequestTypeDef",
    {
        "TemplateActiveVersionRequest": TemplateActiveVersionRequestTypeDef,
        "TemplateName": str,
        "TemplateType": str,
    },
)
TemplateConfigurationTypeDef = TypedDict(
    "TemplateConfigurationTypeDef",
    {
        "EmailTemplate": NotRequired[TemplateTypeDef],
        "PushTemplate": NotRequired[TemplateTypeDef],
        "SMSTemplate": NotRequired[TemplateTypeDef],
        "VoiceTemplate": NotRequired[TemplateTypeDef],
        "InAppTemplate": NotRequired[TemplateTypeDef],
    },
)
TemplatesResponseTypeDef = TypedDict(
    "TemplatesResponseTypeDef",
    {
        "Item": List[TemplateResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
TemplateVersionsResponseTypeDef = TypedDict(
    "TemplateVersionsResponseTypeDef",
    {
        "Item": List[TemplateVersionResponseTypeDef],
        "Message": NotRequired[str],
        "NextToken": NotRequired[str],
        "RequestID": NotRequired[str],
    },
)
UpdateRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
        "UpdateRecommenderConfiguration": UpdateRecommenderConfigurationTypeDef,
    },
)
UpdateVoiceChannelRequestRequestTypeDef = TypedDict(
    "UpdateVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "VoiceChannelRequest": VoiceChannelRequestTypeDef,
    },
)
VerifyOTPMessageResponseTypeDef = TypedDict(
    "VerifyOTPMessageResponseTypeDef",
    {
        "VerificationResponse": VerificationResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyOTPMessageRequestRequestTypeDef = TypedDict(
    "VerifyOTPMessageRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "VerifyOTPMessageRequestParameters": VerifyOTPMessageRequestParametersTypeDef,
    },
)
GetCampaignActivitiesResponseTypeDef = TypedDict(
    "GetCampaignActivitiesResponseTypeDef",
    {
        "ActivitiesResponse": ActivitiesResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppsResponseTypeDef = TypedDict(
    "GetAppsResponseTypeDef",
    {
        "ApplicationsResponse": ApplicationsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplicationSettingsResourceTypeDef = TypedDict(
    "ApplicationSettingsResourceTypeDef",
    {
        "ApplicationId": str,
        "CampaignHook": NotRequired[CampaignHookTypeDef],
        "LastModifiedDate": NotRequired[str],
        "Limits": NotRequired[CampaignLimitsTypeDef],
        "QuietTime": NotRequired[QuietTimeTypeDef],
        "JourneyLimits": NotRequired[ApplicationSettingsJourneyLimitsTypeDef],
    },
)
WriteApplicationSettingsRequestTypeDef = TypedDict(
    "WriteApplicationSettingsRequestTypeDef",
    {
        "CampaignHook": NotRequired[CampaignHookTypeDef],
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "EventTaggingEnabled": NotRequired[bool],
        "Limits": NotRequired[CampaignLimitsTypeDef],
        "QuietTime": NotRequired[QuietTimeTypeDef],
        "JourneyLimits": NotRequired[ApplicationSettingsJourneyLimitsTypeDef],
    },
)
CampaignEmailMessageUnionTypeDef = Union[
    CampaignEmailMessageTypeDef, CampaignEmailMessageOutputTypeDef
]
CreateEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateEmailTemplateRequestRequestTypeDef",
    {
        "EmailTemplateRequest": EmailTemplateRequestTypeDef,
        "TemplateName": str,
    },
)
UpdateEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateEmailTemplateRequestRequestTypeDef",
    {
        "EmailTemplateRequest": EmailTemplateRequestTypeDef,
        "TemplateName": str,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)
GetEmailTemplateResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseTypeDef",
    {
        "EmailTemplateResponse": EmailTemplateResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChannelsResponseTypeDef = TypedDict(
    "GetChannelsResponseTypeDef",
    {
        "ChannelsResponse": ChannelsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ClosedDaysUnionTypeDef = Union[ClosedDaysTypeDef, ClosedDaysOutputTypeDef]
GetRecommenderConfigurationsResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationsResponseTypeDef",
    {
        "ListRecommenderConfigurationsResponse": ListRecommenderConfigurationsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomMessageActivityUnionTypeDef = Union[
    CustomMessageActivityTypeDef, CustomMessageActivityOutputTypeDef
]
CreatePushTemplateRequestRequestTypeDef = TypedDict(
    "CreatePushTemplateRequestRequestTypeDef",
    {
        "PushNotificationTemplateRequest": PushNotificationTemplateRequestTypeDef,
        "TemplateName": str,
    },
)
UpdatePushTemplateRequestRequestTypeDef = TypedDict(
    "UpdatePushTemplateRequestRequestTypeDef",
    {
        "PushNotificationTemplateRequest": PushNotificationTemplateRequestTypeDef,
        "TemplateName": str,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)
GetPushTemplateResponseTypeDef = TypedDict(
    "GetPushTemplateResponseTypeDef",
    {
        "PushNotificationTemplateResponse": PushNotificationTemplateResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendUsersMessagesResponseTypeDef = TypedDict(
    "SendUsersMessagesResponseTypeDef",
    {
        "SendUsersMessageResponse": SendUsersMessageResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef",
    {
        "EndpointResponse": EndpointResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EndpointsResponseTypeDef = TypedDict(
    "EndpointsResponseTypeDef",
    {
        "Item": List[EndpointResponseTypeDef],
    },
)
GetEndpointResponseTypeDef = TypedDict(
    "GetEndpointResponseTypeDef",
    {
        "EndpointResponse": EndpointResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EndpointBatchItemTypeDef = TypedDict(
    "EndpointBatchItemTypeDef",
    {
        "Address": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, Sequence[str]]],
        "ChannelType": NotRequired[ChannelTypeType],
        "Demographic": NotRequired[EndpointDemographicTypeDef],
        "EffectiveDate": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "Id": NotRequired[str],
        "Location": NotRequired[EndpointLocationTypeDef],
        "Metrics": NotRequired[Mapping[str, float]],
        "OptOut": NotRequired[str],
        "RequestId": NotRequired[str],
        "User": NotRequired[EndpointUserUnionTypeDef],
    },
)
EndpointRequestTypeDef = TypedDict(
    "EndpointRequestTypeDef",
    {
        "Address": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, Sequence[str]]],
        "ChannelType": NotRequired[ChannelTypeType],
        "Demographic": NotRequired[EndpointDemographicTypeDef],
        "EffectiveDate": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "Location": NotRequired[EndpointLocationTypeDef],
        "Metrics": NotRequired[Mapping[str, float]],
        "OptOut": NotRequired[str],
        "RequestId": NotRequired[str],
        "User": NotRequired[EndpointUserUnionTypeDef],
    },
)
PublicEndpointTypeDef = TypedDict(
    "PublicEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, Sequence[str]]],
        "ChannelType": NotRequired[ChannelTypeType],
        "Demographic": NotRequired[EndpointDemographicTypeDef],
        "EffectiveDate": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "Location": NotRequired[EndpointLocationTypeDef],
        "Metrics": NotRequired[Mapping[str, float]],
        "OptOut": NotRequired[str],
        "RequestId": NotRequired[str],
        "User": NotRequired[EndpointUserUnionTypeDef],
    },
)
CampaignEventFilterOutputTypeDef = TypedDict(
    "CampaignEventFilterOutputTypeDef",
    {
        "Dimensions": EventDimensionsOutputTypeDef,
        "FilterType": FilterTypeType,
    },
)
EventConditionOutputTypeDef = TypedDict(
    "EventConditionOutputTypeDef",
    {
        "Dimensions": NotRequired[EventDimensionsOutputTypeDef],
        "MessageActivity": NotRequired[str],
    },
)
EventFilterOutputTypeDef = TypedDict(
    "EventFilterOutputTypeDef",
    {
        "Dimensions": EventDimensionsOutputTypeDef,
        "FilterType": FilterTypeType,
    },
)
EventsResponseTypeDef = TypedDict(
    "EventsResponseTypeDef",
    {
        "Results": NotRequired[Dict[str, ItemResponseTypeDef]],
    },
)
CreateExportJobResponseTypeDef = TypedDict(
    "CreateExportJobResponseTypeDef",
    {
        "ExportJobResponse": ExportJobResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportJobsResponseTypeDef = TypedDict(
    "ExportJobsResponseTypeDef",
    {
        "Item": List[ExportJobResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
GetExportJobResponseTypeDef = TypedDict(
    "GetExportJobResponseTypeDef",
    {
        "ExportJobResponse": ExportJobResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SegmentLocationOutputTypeDef = TypedDict(
    "SegmentLocationOutputTypeDef",
    {
        "Country": NotRequired[SetDimensionOutputTypeDef],
        "GPSPoint": NotRequired[GPSPointDimensionTypeDef],
    },
)
JourneyScheduleUnionTypeDef = Union[JourneyScheduleTypeDef, JourneyScheduleOutputTypeDef]
CreateImportJobResponseTypeDef = TypedDict(
    "CreateImportJobResponseTypeDef",
    {
        "ImportJobResponse": ImportJobResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "ImportJobResponse": ImportJobResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportJobsResponseTypeDef = TypedDict(
    "ImportJobsResponseTypeDef",
    {
        "Item": List[ImportJobResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
InAppMessageContentTypeDef = TypedDict(
    "InAppMessageContentTypeDef",
    {
        "BackgroundColor": NotRequired[str],
        "BodyConfig": NotRequired[InAppMessageBodyConfigTypeDef],
        "HeaderConfig": NotRequired[InAppMessageHeaderConfigTypeDef],
        "ImageUrl": NotRequired[str],
        "PrimaryBtn": NotRequired[InAppMessageButtonTypeDef],
        "SecondaryBtn": NotRequired[InAppMessageButtonTypeDef],
    },
)
GetJourneyRunsResponseTypeDef = TypedDict(
    "GetJourneyRunsResponseTypeDef",
    {
        "JourneyRunsResponse": JourneyRunsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendMessagesResponseTypeDef = TypedDict(
    "SendMessagesResponseTypeDef",
    {
        "MessageResponse": MessageResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendOTPMessageResponseTypeDef = TypedDict(
    "SendOTPMessageResponseTypeDef",
    {
        "MessageResponse": MessageResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OpenHoursUnionTypeDef = Union[OpenHoursTypeDef, OpenHoursOutputTypeDef]
RandomSplitActivityUnionTypeDef = Union[
    RandomSplitActivityTypeDef, RandomSplitActivityOutputTypeDef
]
BaseKpiResultTypeDef = TypedDict(
    "BaseKpiResultTypeDef",
    {
        "Rows": List[ResultRowTypeDef],
    },
)
EventDimensionsTypeDef = TypedDict(
    "EventDimensionsTypeDef",
    {
        "Attributes": NotRequired[Mapping[str, AttributeDimensionUnionTypeDef]],
        "EventType": NotRequired[SetDimensionUnionTypeDef],
        "Metrics": NotRequired[Mapping[str, MetricDimensionTypeDef]],
    },
)
SegmentDemographicsTypeDef = TypedDict(
    "SegmentDemographicsTypeDef",
    {
        "AppVersion": NotRequired[SetDimensionUnionTypeDef],
        "Channel": NotRequired[SetDimensionUnionTypeDef],
        "DeviceType": NotRequired[SetDimensionUnionTypeDef],
        "Make": NotRequired[SetDimensionUnionTypeDef],
        "Model": NotRequired[SetDimensionUnionTypeDef],
        "Platform": NotRequired[SetDimensionUnionTypeDef],
    },
)
SegmentLocationTypeDef = TypedDict(
    "SegmentLocationTypeDef",
    {
        "Country": NotRequired[SetDimensionUnionTypeDef],
        "GPSPoint": NotRequired[GPSPointDimensionTypeDef],
    },
)
EmailMessageTypeDef = TypedDict(
    "EmailMessageTypeDef",
    {
        "Body": NotRequired[str],
        "FeedbackForwardingAddress": NotRequired[str],
        "FromAddress": NotRequired[str],
        "RawEmail": NotRequired[RawEmailTypeDef],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "SimpleEmail": NotRequired[SimpleEmailTypeDef],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
    },
)
ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplatesResponse": TemplatesResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionsResponse": TemplateVersionsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationSettingsResponseTypeDef = TypedDict(
    "GetApplicationSettingsResponseTypeDef",
    {
        "ApplicationSettingsResource": ApplicationSettingsResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationSettingsResponseTypeDef = TypedDict(
    "UpdateApplicationSettingsResponseTypeDef",
    {
        "ApplicationSettingsResource": ApplicationSettingsResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationSettingsRequestRequestTypeDef = TypedDict(
    "UpdateApplicationSettingsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteApplicationSettingsRequest": WriteApplicationSettingsRequestTypeDef,
    },
)
DeleteUserEndpointsResponseTypeDef = TypedDict(
    "DeleteUserEndpointsResponseTypeDef",
    {
        "EndpointsResponse": EndpointsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserEndpointsResponseTypeDef = TypedDict(
    "GetUserEndpointsResponseTypeDef",
    {
        "EndpointsResponse": EndpointsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EndpointBatchRequestTypeDef = TypedDict(
    "EndpointBatchRequestTypeDef",
    {
        "Item": Sequence[EndpointBatchItemTypeDef],
    },
)
UpdateEndpointRequestRequestTypeDef = TypedDict(
    "UpdateEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
        "EndpointRequest": EndpointRequestTypeDef,
    },
)
EventsBatchTypeDef = TypedDict(
    "EventsBatchTypeDef",
    {
        "Endpoint": PublicEndpointTypeDef,
        "Events": Mapping[str, EventTypeDef],
    },
)
InAppCampaignScheduleTypeDef = TypedDict(
    "InAppCampaignScheduleTypeDef",
    {
        "EndDate": NotRequired[str],
        "EventFilter": NotRequired[CampaignEventFilterOutputTypeDef],
        "QuietTime": NotRequired[QuietTimeTypeDef],
    },
)
ScheduleOutputTypeDef = TypedDict(
    "ScheduleOutputTypeDef",
    {
        "StartTime": str,
        "EndTime": NotRequired[str],
        "EventFilter": NotRequired[CampaignEventFilterOutputTypeDef],
        "Frequency": NotRequired[FrequencyType],
        "IsLocalTime": NotRequired[bool],
        "QuietTime": NotRequired[QuietTimeTypeDef],
        "Timezone": NotRequired[str],
    },
)
EventStartConditionOutputTypeDef = TypedDict(
    "EventStartConditionOutputTypeDef",
    {
        "EventFilter": NotRequired[EventFilterOutputTypeDef],
        "SegmentId": NotRequired[str],
    },
)
PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef",
    {
        "EventsResponse": EventsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExportJobsResponseTypeDef = TypedDict(
    "GetExportJobsResponseTypeDef",
    {
        "ExportJobsResponse": ExportJobsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSegmentExportJobsResponseTypeDef = TypedDict(
    "GetSegmentExportJobsResponseTypeDef",
    {
        "ExportJobsResponse": ExportJobsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SegmentDimensionsOutputTypeDef = TypedDict(
    "SegmentDimensionsOutputTypeDef",
    {
        "Attributes": NotRequired[Dict[str, AttributeDimensionOutputTypeDef]],
        "Behavior": NotRequired[SegmentBehaviorsTypeDef],
        "Demographic": NotRequired[SegmentDemographicsOutputTypeDef],
        "Location": NotRequired[SegmentLocationOutputTypeDef],
        "Metrics": NotRequired[Dict[str, MetricDimensionTypeDef]],
        "UserAttributes": NotRequired[Dict[str, AttributeDimensionOutputTypeDef]],
    },
)
GetImportJobsResponseTypeDef = TypedDict(
    "GetImportJobsResponseTypeDef",
    {
        "ImportJobsResponse": ImportJobsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSegmentImportJobsResponseTypeDef = TypedDict(
    "GetSegmentImportJobsResponseTypeDef",
    {
        "ImportJobsResponse": ImportJobsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CampaignInAppMessageOutputTypeDef = TypedDict(
    "CampaignInAppMessageOutputTypeDef",
    {
        "Body": NotRequired[str],
        "Content": NotRequired[List[InAppMessageContentTypeDef]],
        "CustomConfig": NotRequired[Dict[str, str]],
        "Layout": NotRequired[LayoutType],
    },
)
CampaignInAppMessageTypeDef = TypedDict(
    "CampaignInAppMessageTypeDef",
    {
        "Body": NotRequired[str],
        "Content": NotRequired[Sequence[InAppMessageContentTypeDef]],
        "CustomConfig": NotRequired[Mapping[str, str]],
        "Layout": NotRequired[LayoutType],
    },
)
InAppMessageTypeDef = TypedDict(
    "InAppMessageTypeDef",
    {
        "Content": NotRequired[List[InAppMessageContentTypeDef]],
        "CustomConfig": NotRequired[Dict[str, str]],
        "Layout": NotRequired[LayoutType],
    },
)
InAppTemplateRequestTypeDef = TypedDict(
    "InAppTemplateRequestTypeDef",
    {
        "Content": NotRequired[Sequence[InAppMessageContentTypeDef]],
        "CustomConfig": NotRequired[Mapping[str, str]],
        "Layout": NotRequired[LayoutType],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
    },
)
InAppTemplateResponseTypeDef = TypedDict(
    "InAppTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "Content": NotRequired[List[InAppMessageContentTypeDef]],
        "CustomConfig": NotRequired[Dict[str, str]],
        "Layout": NotRequired[LayoutType],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)
ApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "ApplicationDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "EndTime": datetime,
        "KpiName": str,
        "KpiResult": BaseKpiResultTypeDef,
        "StartTime": datetime,
        "NextToken": NotRequired[str],
    },
)
CampaignDateRangeKpiResponseTypeDef = TypedDict(
    "CampaignDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "EndTime": datetime,
        "KpiName": str,
        "KpiResult": BaseKpiResultTypeDef,
        "StartTime": datetime,
        "NextToken": NotRequired[str],
    },
)
JourneyDateRangeKpiResponseTypeDef = TypedDict(
    "JourneyDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "EndTime": datetime,
        "JourneyId": str,
        "KpiName": str,
        "KpiResult": BaseKpiResultTypeDef,
        "StartTime": datetime,
        "NextToken": NotRequired[str],
    },
)
EventDimensionsUnionTypeDef = Union[EventDimensionsTypeDef, EventDimensionsOutputTypeDef]
SegmentDemographicsUnionTypeDef = Union[
    SegmentDemographicsTypeDef, SegmentDemographicsOutputTypeDef
]
SegmentLocationUnionTypeDef = Union[SegmentLocationTypeDef, SegmentLocationOutputTypeDef]
DirectMessageConfigurationTypeDef = TypedDict(
    "DirectMessageConfigurationTypeDef",
    {
        "ADMMessage": NotRequired[ADMMessageTypeDef],
        "APNSMessage": NotRequired[APNSMessageTypeDef],
        "BaiduMessage": NotRequired[BaiduMessageTypeDef],
        "DefaultMessage": NotRequired[DefaultMessageTypeDef],
        "DefaultPushNotificationMessage": NotRequired[DefaultPushNotificationMessageTypeDef],
        "EmailMessage": NotRequired[EmailMessageTypeDef],
        "GCMMessage": NotRequired[GCMMessageTypeDef],
        "SMSMessage": NotRequired[SMSMessageTypeDef],
        "VoiceMessage": NotRequired[VoiceMessageTypeDef],
    },
)
UpdateEndpointsBatchRequestRequestTypeDef = TypedDict(
    "UpdateEndpointsBatchRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointBatchRequest": EndpointBatchRequestTypeDef,
    },
)
EventsRequestTypeDef = TypedDict(
    "EventsRequestTypeDef",
    {
        "BatchItem": Mapping[str, EventsBatchTypeDef],
    },
)
StartConditionOutputTypeDef = TypedDict(
    "StartConditionOutputTypeDef",
    {
        "Description": NotRequired[str],
        "EventStartCondition": NotRequired[EventStartConditionOutputTypeDef],
        "SegmentStartCondition": NotRequired[SegmentConditionTypeDef],
    },
)
SegmentGroupOutputTypeDef = TypedDict(
    "SegmentGroupOutputTypeDef",
    {
        "Dimensions": NotRequired[List[SegmentDimensionsOutputTypeDef]],
        "SourceSegments": NotRequired[List[SegmentReferenceTypeDef]],
        "SourceType": NotRequired[SourceTypeType],
        "Type": NotRequired[TypeType],
    },
)
SimpleConditionOutputTypeDef = TypedDict(
    "SimpleConditionOutputTypeDef",
    {
        "EventCondition": NotRequired[EventConditionOutputTypeDef],
        "SegmentCondition": NotRequired[SegmentConditionTypeDef],
        "SegmentDimensions": NotRequired[SegmentDimensionsOutputTypeDef],
    },
)
MessageConfigurationOutputTypeDef = TypedDict(
    "MessageConfigurationOutputTypeDef",
    {
        "ADMMessage": NotRequired[MessageTypeDef],
        "APNSMessage": NotRequired[MessageTypeDef],
        "BaiduMessage": NotRequired[MessageTypeDef],
        "CustomMessage": NotRequired[CampaignCustomMessageTypeDef],
        "DefaultMessage": NotRequired[MessageTypeDef],
        "EmailMessage": NotRequired[CampaignEmailMessageOutputTypeDef],
        "GCMMessage": NotRequired[MessageTypeDef],
        "SMSMessage": NotRequired[CampaignSmsMessageTypeDef],
        "InAppMessage": NotRequired[CampaignInAppMessageOutputTypeDef],
    },
)
CampaignInAppMessageUnionTypeDef = Union[
    CampaignInAppMessageTypeDef, CampaignInAppMessageOutputTypeDef
]
InAppMessageCampaignTypeDef = TypedDict(
    "InAppMessageCampaignTypeDef",
    {
        "CampaignId": NotRequired[str],
        "DailyCap": NotRequired[int],
        "InAppMessage": NotRequired[InAppMessageTypeDef],
        "Priority": NotRequired[int],
        "Schedule": NotRequired[InAppCampaignScheduleTypeDef],
        "SessionCap": NotRequired[int],
        "TotalCap": NotRequired[int],
        "TreatmentId": NotRequired[str],
    },
)
CreateInAppTemplateRequestRequestTypeDef = TypedDict(
    "CreateInAppTemplateRequestRequestTypeDef",
    {
        "InAppTemplateRequest": InAppTemplateRequestTypeDef,
        "TemplateName": str,
    },
)
UpdateInAppTemplateRequestRequestTypeDef = TypedDict(
    "UpdateInAppTemplateRequestRequestTypeDef",
    {
        "InAppTemplateRequest": InAppTemplateRequestTypeDef,
        "TemplateName": str,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)
GetInAppTemplateResponseTypeDef = TypedDict(
    "GetInAppTemplateResponseTypeDef",
    {
        "InAppTemplateResponse": InAppTemplateResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "GetApplicationDateRangeKpiResponseTypeDef",
    {
        "ApplicationDateRangeKpiResponse": ApplicationDateRangeKpiResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCampaignDateRangeKpiResponseTypeDef = TypedDict(
    "GetCampaignDateRangeKpiResponseTypeDef",
    {
        "CampaignDateRangeKpiResponse": CampaignDateRangeKpiResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJourneyDateRangeKpiResponseTypeDef = TypedDict(
    "GetJourneyDateRangeKpiResponseTypeDef",
    {
        "JourneyDateRangeKpiResponse": JourneyDateRangeKpiResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CampaignEventFilterTypeDef = TypedDict(
    "CampaignEventFilterTypeDef",
    {
        "Dimensions": EventDimensionsUnionTypeDef,
        "FilterType": FilterTypeType,
    },
)
EventConditionTypeDef = TypedDict(
    "EventConditionTypeDef",
    {
        "Dimensions": NotRequired[EventDimensionsUnionTypeDef],
        "MessageActivity": NotRequired[str],
    },
)
EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Dimensions": EventDimensionsUnionTypeDef,
        "FilterType": FilterTypeType,
    },
)
SegmentDimensionsTypeDef = TypedDict(
    "SegmentDimensionsTypeDef",
    {
        "Attributes": NotRequired[Mapping[str, AttributeDimensionUnionTypeDef]],
        "Behavior": NotRequired[SegmentBehaviorsTypeDef],
        "Demographic": NotRequired[SegmentDemographicsUnionTypeDef],
        "Location": NotRequired[SegmentLocationUnionTypeDef],
        "Metrics": NotRequired[Mapping[str, MetricDimensionTypeDef]],
        "UserAttributes": NotRequired[Mapping[str, AttributeDimensionTypeDef]],
    },
)
MessageRequestTypeDef = TypedDict(
    "MessageRequestTypeDef",
    {
        "MessageConfiguration": DirectMessageConfigurationTypeDef,
        "Addresses": NotRequired[Mapping[str, AddressConfigurationTypeDef]],
        "Context": NotRequired[Mapping[str, str]],
        "Endpoints": NotRequired[Mapping[str, EndpointSendConfigurationTypeDef]],
        "TemplateConfiguration": NotRequired[TemplateConfigurationTypeDef],
        "TraceId": NotRequired[str],
    },
)
SendUsersMessageRequestTypeDef = TypedDict(
    "SendUsersMessageRequestTypeDef",
    {
        "MessageConfiguration": DirectMessageConfigurationTypeDef,
        "Users": Mapping[str, EndpointSendConfigurationTypeDef],
        "Context": NotRequired[Mapping[str, str]],
        "TemplateConfiguration": NotRequired[TemplateConfigurationTypeDef],
        "TraceId": NotRequired[str],
    },
)
PutEventsRequestRequestTypeDef = TypedDict(
    "PutEventsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EventsRequest": EventsRequestTypeDef,
    },
)
SegmentGroupListOutputTypeDef = TypedDict(
    "SegmentGroupListOutputTypeDef",
    {
        "Groups": NotRequired[List[SegmentGroupOutputTypeDef]],
        "Include": NotRequired[IncludeType],
    },
)
ConditionOutputTypeDef = TypedDict(
    "ConditionOutputTypeDef",
    {
        "Conditions": NotRequired[List[SimpleConditionOutputTypeDef]],
        "Operator": NotRequired[OperatorType],
    },
)
MultiConditionalBranchOutputTypeDef = TypedDict(
    "MultiConditionalBranchOutputTypeDef",
    {
        "Condition": NotRequired[SimpleConditionOutputTypeDef],
        "NextActivity": NotRequired[str],
    },
)
TreatmentResourceTypeDef = TypedDict(
    "TreatmentResourceTypeDef",
    {
        "Id": str,
        "SizePercent": int,
        "CustomDeliveryConfiguration": NotRequired[CustomDeliveryConfigurationOutputTypeDef],
        "MessageConfiguration": NotRequired[MessageConfigurationOutputTypeDef],
        "Schedule": NotRequired[ScheduleOutputTypeDef],
        "State": NotRequired[CampaignStateTypeDef],
        "TemplateConfiguration": NotRequired[TemplateConfigurationTypeDef],
        "TreatmentDescription": NotRequired[str],
        "TreatmentName": NotRequired[str],
    },
)
MessageConfigurationTypeDef = TypedDict(
    "MessageConfigurationTypeDef",
    {
        "ADMMessage": NotRequired[MessageTypeDef],
        "APNSMessage": NotRequired[MessageTypeDef],
        "BaiduMessage": NotRequired[MessageTypeDef],
        "CustomMessage": NotRequired[CampaignCustomMessageTypeDef],
        "DefaultMessage": NotRequired[MessageTypeDef],
        "EmailMessage": NotRequired[CampaignEmailMessageUnionTypeDef],
        "GCMMessage": NotRequired[MessageTypeDef],
        "SMSMessage": NotRequired[CampaignSmsMessageTypeDef],
        "InAppMessage": NotRequired[CampaignInAppMessageUnionTypeDef],
    },
)
InAppMessagesResponseTypeDef = TypedDict(
    "InAppMessagesResponseTypeDef",
    {
        "InAppMessageCampaigns": NotRequired[List[InAppMessageCampaignTypeDef]],
    },
)
CampaignEventFilterUnionTypeDef = Union[
    CampaignEventFilterTypeDef, CampaignEventFilterOutputTypeDef
]
EventConditionUnionTypeDef = Union[EventConditionTypeDef, EventConditionOutputTypeDef]
EventFilterUnionTypeDef = Union[EventFilterTypeDef, EventFilterOutputTypeDef]
SegmentDimensionsUnionTypeDef = Union[SegmentDimensionsTypeDef, SegmentDimensionsOutputTypeDef]
SendMessagesRequestRequestTypeDef = TypedDict(
    "SendMessagesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MessageRequest": MessageRequestTypeDef,
    },
)
SendUsersMessagesRequestRequestTypeDef = TypedDict(
    "SendUsersMessagesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SendUsersMessageRequest": SendUsersMessageRequestTypeDef,
    },
)
SegmentResponseTypeDef = TypedDict(
    "SegmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreationDate": str,
        "Id": str,
        "SegmentType": SegmentTypeType,
        "Dimensions": NotRequired[SegmentDimensionsOutputTypeDef],
        "ImportDefinition": NotRequired[SegmentImportResourceTypeDef],
        "LastModifiedDate": NotRequired[str],
        "Name": NotRequired[str],
        "SegmentGroups": NotRequired[SegmentGroupListOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "Version": NotRequired[int],
    },
)
ConditionalSplitActivityOutputTypeDef = TypedDict(
    "ConditionalSplitActivityOutputTypeDef",
    {
        "Condition": NotRequired[ConditionOutputTypeDef],
        "EvaluationWaitTime": NotRequired[WaitTimeTypeDef],
        "FalseActivity": NotRequired[str],
        "TrueActivity": NotRequired[str],
    },
)
MultiConditionalSplitActivityOutputTypeDef = TypedDict(
    "MultiConditionalSplitActivityOutputTypeDef",
    {
        "Branches": NotRequired[List[MultiConditionalBranchOutputTypeDef]],
        "DefaultActivity": NotRequired[str],
        "EvaluationWaitTime": NotRequired[WaitTimeTypeDef],
    },
)
CampaignResponseTypeDef = TypedDict(
    "CampaignResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreationDate": str,
        "Id": str,
        "LastModifiedDate": str,
        "SegmentId": str,
        "SegmentVersion": int,
        "AdditionalTreatments": NotRequired[List[TreatmentResourceTypeDef]],
        "CustomDeliveryConfiguration": NotRequired[CustomDeliveryConfigurationOutputTypeDef],
        "DefaultState": NotRequired[CampaignStateTypeDef],
        "Description": NotRequired[str],
        "HoldoutPercent": NotRequired[int],
        "Hook": NotRequired[CampaignHookTypeDef],
        "IsPaused": NotRequired[bool],
        "Limits": NotRequired[CampaignLimitsTypeDef],
        "MessageConfiguration": NotRequired[MessageConfigurationOutputTypeDef],
        "Name": NotRequired[str],
        "Schedule": NotRequired[ScheduleOutputTypeDef],
        "State": NotRequired[CampaignStateTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "TemplateConfiguration": NotRequired[TemplateConfigurationTypeDef],
        "TreatmentDescription": NotRequired[str],
        "TreatmentName": NotRequired[str],
        "Version": NotRequired[int],
        "Priority": NotRequired[int],
    },
)
MessageConfigurationUnionTypeDef = Union[
    MessageConfigurationTypeDef, MessageConfigurationOutputTypeDef
]
GetInAppMessagesResponseTypeDef = TypedDict(
    "GetInAppMessagesResponseTypeDef",
    {
        "InAppMessagesResponse": InAppMessagesResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "StartTime": str,
        "EndTime": NotRequired[str],
        "EventFilter": NotRequired[CampaignEventFilterUnionTypeDef],
        "Frequency": NotRequired[FrequencyType],
        "IsLocalTime": NotRequired[bool],
        "QuietTime": NotRequired[QuietTimeTypeDef],
        "Timezone": NotRequired[str],
    },
)
EventStartConditionTypeDef = TypedDict(
    "EventStartConditionTypeDef",
    {
        "EventFilter": NotRequired[EventFilterUnionTypeDef],
        "SegmentId": NotRequired[str],
    },
)
SegmentGroupTypeDef = TypedDict(
    "SegmentGroupTypeDef",
    {
        "Dimensions": NotRequired[Sequence[SegmentDimensionsUnionTypeDef]],
        "SourceSegments": NotRequired[Sequence[SegmentReferenceTypeDef]],
        "SourceType": NotRequired[SourceTypeType],
        "Type": NotRequired[TypeType],
    },
)
SimpleConditionTypeDef = TypedDict(
    "SimpleConditionTypeDef",
    {
        "EventCondition": NotRequired[EventConditionUnionTypeDef],
        "SegmentCondition": NotRequired[SegmentConditionTypeDef],
        "SegmentDimensions": NotRequired[SegmentDimensionsUnionTypeDef],
    },
)
CreateSegmentResponseTypeDef = TypedDict(
    "CreateSegmentResponseTypeDef",
    {
        "SegmentResponse": SegmentResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSegmentResponseTypeDef = TypedDict(
    "DeleteSegmentResponseTypeDef",
    {
        "SegmentResponse": SegmentResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSegmentResponseTypeDef = TypedDict(
    "GetSegmentResponseTypeDef",
    {
        "SegmentResponse": SegmentResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSegmentVersionResponseTypeDef = TypedDict(
    "GetSegmentVersionResponseTypeDef",
    {
        "SegmentResponse": SegmentResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SegmentsResponseTypeDef = TypedDict(
    "SegmentsResponseTypeDef",
    {
        "Item": List[SegmentResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
UpdateSegmentResponseTypeDef = TypedDict(
    "UpdateSegmentResponseTypeDef",
    {
        "SegmentResponse": SegmentResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActivityOutputTypeDef = TypedDict(
    "ActivityOutputTypeDef",
    {
        "CUSTOM": NotRequired[CustomMessageActivityOutputTypeDef],
        "ConditionalSplit": NotRequired[ConditionalSplitActivityOutputTypeDef],
        "Description": NotRequired[str],
        "EMAIL": NotRequired[EmailMessageActivityTypeDef],
        "Holdout": NotRequired[HoldoutActivityTypeDef],
        "MultiCondition": NotRequired[MultiConditionalSplitActivityOutputTypeDef],
        "PUSH": NotRequired[PushMessageActivityTypeDef],
        "RandomSplit": NotRequired[RandomSplitActivityOutputTypeDef],
        "SMS": NotRequired[SMSMessageActivityTypeDef],
        "Wait": NotRequired[WaitActivityTypeDef],
        "ContactCenter": NotRequired[ContactCenterActivityTypeDef],
    },
)
CampaignsResponseTypeDef = TypedDict(
    "CampaignsResponseTypeDef",
    {
        "Item": List[CampaignResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "CampaignResponse": CampaignResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCampaignResponseTypeDef = TypedDict(
    "DeleteCampaignResponseTypeDef",
    {
        "CampaignResponse": CampaignResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCampaignResponseTypeDef = TypedDict(
    "GetCampaignResponseTypeDef",
    {
        "CampaignResponse": CampaignResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCampaignVersionResponseTypeDef = TypedDict(
    "GetCampaignVersionResponseTypeDef",
    {
        "CampaignResponse": CampaignResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "CampaignResponse": CampaignResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduleUnionTypeDef = Union[ScheduleTypeDef, ScheduleOutputTypeDef]
EventStartConditionUnionTypeDef = Union[
    EventStartConditionTypeDef, EventStartConditionOutputTypeDef
]
SegmentGroupUnionTypeDef = Union[SegmentGroupTypeDef, SegmentGroupOutputTypeDef]
SimpleConditionUnionTypeDef = Union[SimpleConditionTypeDef, SimpleConditionOutputTypeDef]
GetSegmentVersionsResponseTypeDef = TypedDict(
    "GetSegmentVersionsResponseTypeDef",
    {
        "SegmentsResponse": SegmentsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSegmentsResponseTypeDef = TypedDict(
    "GetSegmentsResponseTypeDef",
    {
        "SegmentsResponse": SegmentsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JourneyResponseTypeDef = TypedDict(
    "JourneyResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Activities": NotRequired[Dict[str, ActivityOutputTypeDef]],
        "CreationDate": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Limits": NotRequired[JourneyLimitsTypeDef],
        "LocalTime": NotRequired[bool],
        "QuietTime": NotRequired[QuietTimeTypeDef],
        "RefreshFrequency": NotRequired[str],
        "Schedule": NotRequired[JourneyScheduleOutputTypeDef],
        "StartActivity": NotRequired[str],
        "StartCondition": NotRequired[StartConditionOutputTypeDef],
        "State": NotRequired[StateType],
        "tags": NotRequired[Dict[str, str]],
        "WaitForQuietTime": NotRequired[bool],
        "RefreshOnSegmentUpdate": NotRequired[bool],
        "JourneyChannelSettings": NotRequired[JourneyChannelSettingsTypeDef],
        "SendingSchedule": NotRequired[bool],
        "OpenHours": NotRequired[OpenHoursOutputTypeDef],
        "ClosedDays": NotRequired[ClosedDaysOutputTypeDef],
        "TimezoneEstimationMethods": NotRequired[List[TimezoneEstimationMethodsElementType]],
    },
)
GetCampaignVersionsResponseTypeDef = TypedDict(
    "GetCampaignVersionsResponseTypeDef",
    {
        "CampaignsResponse": CampaignsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCampaignsResponseTypeDef = TypedDict(
    "GetCampaignsResponseTypeDef",
    {
        "CampaignsResponse": CampaignsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WriteTreatmentResourceTypeDef = TypedDict(
    "WriteTreatmentResourceTypeDef",
    {
        "SizePercent": int,
        "CustomDeliveryConfiguration": NotRequired[CustomDeliveryConfigurationUnionTypeDef],
        "MessageConfiguration": NotRequired[MessageConfigurationUnionTypeDef],
        "Schedule": NotRequired[ScheduleUnionTypeDef],
        "TemplateConfiguration": NotRequired[TemplateConfigurationTypeDef],
        "TreatmentDescription": NotRequired[str],
        "TreatmentName": NotRequired[str],
    },
)
StartConditionTypeDef = TypedDict(
    "StartConditionTypeDef",
    {
        "Description": NotRequired[str],
        "EventStartCondition": NotRequired[EventStartConditionUnionTypeDef],
        "SegmentStartCondition": NotRequired[SegmentConditionTypeDef],
    },
)
SegmentGroupListTypeDef = TypedDict(
    "SegmentGroupListTypeDef",
    {
        "Groups": NotRequired[Sequence[SegmentGroupUnionTypeDef]],
        "Include": NotRequired[IncludeType],
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Conditions": NotRequired[Sequence[SimpleConditionUnionTypeDef]],
        "Operator": NotRequired[OperatorType],
    },
)
MultiConditionalBranchTypeDef = TypedDict(
    "MultiConditionalBranchTypeDef",
    {
        "Condition": NotRequired[SimpleConditionUnionTypeDef],
        "NextActivity": NotRequired[str],
    },
)
CreateJourneyResponseTypeDef = TypedDict(
    "CreateJourneyResponseTypeDef",
    {
        "JourneyResponse": JourneyResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteJourneyResponseTypeDef = TypedDict(
    "DeleteJourneyResponseTypeDef",
    {
        "JourneyResponse": JourneyResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJourneyResponseTypeDef = TypedDict(
    "GetJourneyResponseTypeDef",
    {
        "JourneyResponse": JourneyResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JourneysResponseTypeDef = TypedDict(
    "JourneysResponseTypeDef",
    {
        "Item": List[JourneyResponseTypeDef],
        "NextToken": NotRequired[str],
    },
)
UpdateJourneyResponseTypeDef = TypedDict(
    "UpdateJourneyResponseTypeDef",
    {
        "JourneyResponse": JourneyResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateJourneyStateResponseTypeDef = TypedDict(
    "UpdateJourneyStateResponseTypeDef",
    {
        "JourneyResponse": JourneyResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WriteCampaignRequestTypeDef = TypedDict(
    "WriteCampaignRequestTypeDef",
    {
        "AdditionalTreatments": NotRequired[Sequence[WriteTreatmentResourceTypeDef]],
        "CustomDeliveryConfiguration": NotRequired[CustomDeliveryConfigurationUnionTypeDef],
        "Description": NotRequired[str],
        "HoldoutPercent": NotRequired[int],
        "Hook": NotRequired[CampaignHookTypeDef],
        "IsPaused": NotRequired[bool],
        "Limits": NotRequired[CampaignLimitsTypeDef],
        "MessageConfiguration": NotRequired[MessageConfigurationUnionTypeDef],
        "Name": NotRequired[str],
        "Schedule": NotRequired[ScheduleUnionTypeDef],
        "SegmentId": NotRequired[str],
        "SegmentVersion": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateConfiguration": NotRequired[TemplateConfigurationTypeDef],
        "TreatmentDescription": NotRequired[str],
        "TreatmentName": NotRequired[str],
        "Priority": NotRequired[int],
    },
)
StartConditionUnionTypeDef = Union[StartConditionTypeDef, StartConditionOutputTypeDef]
SegmentGroupListUnionTypeDef = Union[SegmentGroupListTypeDef, SegmentGroupListOutputTypeDef]
ConditionUnionTypeDef = Union[ConditionTypeDef, ConditionOutputTypeDef]
MultiConditionalBranchUnionTypeDef = Union[
    MultiConditionalBranchTypeDef, MultiConditionalBranchOutputTypeDef
]
ListJourneysResponseTypeDef = TypedDict(
    "ListJourneysResponseTypeDef",
    {
        "JourneysResponse": JourneysResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCampaignRequestRequestTypeDef = TypedDict(
    "CreateCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteCampaignRequest": WriteCampaignRequestTypeDef,
    },
)
UpdateCampaignRequestRequestTypeDef = TypedDict(
    "UpdateCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "WriteCampaignRequest": WriteCampaignRequestTypeDef,
    },
)
WriteSegmentRequestTypeDef = TypedDict(
    "WriteSegmentRequestTypeDef",
    {
        "Dimensions": NotRequired[SegmentDimensionsUnionTypeDef],
        "Name": NotRequired[str],
        "SegmentGroups": NotRequired[SegmentGroupListUnionTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ConditionalSplitActivityTypeDef = TypedDict(
    "ConditionalSplitActivityTypeDef",
    {
        "Condition": NotRequired[ConditionUnionTypeDef],
        "EvaluationWaitTime": NotRequired[WaitTimeTypeDef],
        "FalseActivity": NotRequired[str],
        "TrueActivity": NotRequired[str],
    },
)
MultiConditionalSplitActivityTypeDef = TypedDict(
    "MultiConditionalSplitActivityTypeDef",
    {
        "Branches": NotRequired[Sequence[MultiConditionalBranchUnionTypeDef]],
        "DefaultActivity": NotRequired[str],
        "EvaluationWaitTime": NotRequired[WaitTimeTypeDef],
    },
)
CreateSegmentRequestRequestTypeDef = TypedDict(
    "CreateSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteSegmentRequest": WriteSegmentRequestTypeDef,
    },
)
UpdateSegmentRequestRequestTypeDef = TypedDict(
    "UpdateSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "WriteSegmentRequest": WriteSegmentRequestTypeDef,
    },
)
ConditionalSplitActivityUnionTypeDef = Union[
    ConditionalSplitActivityTypeDef, ConditionalSplitActivityOutputTypeDef
]
MultiConditionalSplitActivityUnionTypeDef = Union[
    MultiConditionalSplitActivityTypeDef, MultiConditionalSplitActivityOutputTypeDef
]
ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "CUSTOM": NotRequired[CustomMessageActivityUnionTypeDef],
        "ConditionalSplit": NotRequired[ConditionalSplitActivityUnionTypeDef],
        "Description": NotRequired[str],
        "EMAIL": NotRequired[EmailMessageActivityTypeDef],
        "Holdout": NotRequired[HoldoutActivityTypeDef],
        "MultiCondition": NotRequired[MultiConditionalSplitActivityUnionTypeDef],
        "PUSH": NotRequired[PushMessageActivityTypeDef],
        "RandomSplit": NotRequired[RandomSplitActivityUnionTypeDef],
        "SMS": NotRequired[SMSMessageActivityTypeDef],
        "Wait": NotRequired[WaitActivityTypeDef],
        "ContactCenter": NotRequired[ContactCenterActivityTypeDef],
    },
)
ActivityUnionTypeDef = Union[ActivityTypeDef, ActivityOutputTypeDef]
WriteJourneyRequestTypeDef = TypedDict(
    "WriteJourneyRequestTypeDef",
    {
        "Name": str,
        "Activities": NotRequired[Mapping[str, ActivityUnionTypeDef]],
        "CreationDate": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Limits": NotRequired[JourneyLimitsTypeDef],
        "LocalTime": NotRequired[bool],
        "QuietTime": NotRequired[QuietTimeTypeDef],
        "RefreshFrequency": NotRequired[str],
        "Schedule": NotRequired[JourneyScheduleUnionTypeDef],
        "StartActivity": NotRequired[str],
        "StartCondition": NotRequired[StartConditionUnionTypeDef],
        "State": NotRequired[StateType],
        "WaitForQuietTime": NotRequired[bool],
        "RefreshOnSegmentUpdate": NotRequired[bool],
        "JourneyChannelSettings": NotRequired[JourneyChannelSettingsTypeDef],
        "SendingSchedule": NotRequired[bool],
        "OpenHours": NotRequired[OpenHoursUnionTypeDef],
        "ClosedDays": NotRequired[ClosedDaysUnionTypeDef],
        "TimezoneEstimationMethods": NotRequired[Sequence[TimezoneEstimationMethodsElementType]],
    },
)
CreateJourneyRequestRequestTypeDef = TypedDict(
    "CreateJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteJourneyRequest": WriteJourneyRequestTypeDef,
    },
)
UpdateJourneyRequestRequestTypeDef = TypedDict(
    "UpdateJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "WriteJourneyRequest": WriteJourneyRequestTypeDef,
    },
)
