"""
Type annotations for ssm-contacts service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/type_defs/)

Usage::

    ```python
    from mypy_boto3_ssm_contacts.type_defs import AcceptPageRequestRequestTypeDef

    data: AcceptPageRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AcceptCodeValidationType,
    AcceptTypeType,
    ActivationStatusType,
    ChannelTypeType,
    ContactTypeType,
    DayOfWeekType,
    ReceiptTypeType,
    ShiftTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptPageRequestRequestTypeDef",
    "ActivateContactChannelRequestRequestTypeDef",
    "ChannelTargetInfoTypeDef",
    "ContactChannelAddressTypeDef",
    "ContactTargetInfoTypeDef",
    "ContactTypeDef",
    "HandOffTimeTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "DeactivateContactChannelRequestRequestTypeDef",
    "DeleteContactChannelRequestRequestTypeDef",
    "DeleteContactRequestRequestTypeDef",
    "DeleteRotationOverrideRequestRequestTypeDef",
    "DeleteRotationRequestRequestTypeDef",
    "DescribeEngagementRequestRequestTypeDef",
    "DescribePageRequestRequestTypeDef",
    "EngagementTypeDef",
    "GetContactChannelRequestRequestTypeDef",
    "GetContactPolicyRequestRequestTypeDef",
    "GetContactRequestRequestTypeDef",
    "GetRotationOverrideRequestRequestTypeDef",
    "GetRotationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListContactChannelsRequestRequestTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ListPageReceiptsRequestRequestTypeDef",
    "ReceiptTypeDef",
    "ListPageResolutionsRequestRequestTypeDef",
    "ResolutionContactTypeDef",
    "ListPagesByContactRequestRequestTypeDef",
    "PageTypeDef",
    "ListPagesByEngagementRequestRequestTypeDef",
    "RotationOverrideTypeDef",
    "ListRotationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutContactPolicyRequestRequestTypeDef",
    "ShiftDetailsTypeDef",
    "SendActivationCodeRequestRequestTypeDef",
    "StartEngagementRequestRequestTypeDef",
    "StopEngagementRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ContactChannelTypeDef",
    "CreateContactChannelRequestRequestTypeDef",
    "UpdateContactChannelRequestRequestTypeDef",
    "TargetTypeDef",
    "CoverageTimeTypeDef",
    "MonthlySettingTypeDef",
    "WeeklySettingTypeDef",
    "CreateContactChannelResultTypeDef",
    "CreateContactResultTypeDef",
    "CreateRotationOverrideResultTypeDef",
    "CreateRotationResultTypeDef",
    "DescribeEngagementResultTypeDef",
    "DescribePageResultTypeDef",
    "GetContactChannelResultTypeDef",
    "GetContactPolicyResultTypeDef",
    "GetRotationOverrideResultTypeDef",
    "ListContactsResultTypeDef",
    "StartEngagementResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateRotationOverrideRequestRequestTypeDef",
    "ListRotationOverridesRequestRequestTypeDef",
    "ListRotationShiftsRequestRequestTypeDef",
    "PreviewOverrideTypeDef",
    "TimeRangeTypeDef",
    "ListEngagementsResultTypeDef",
    "ListContactChannelsRequestListContactChannelsPaginateTypeDef",
    "ListContactsRequestListContactsPaginateTypeDef",
    "ListPageReceiptsRequestListPageReceiptsPaginateTypeDef",
    "ListPageResolutionsRequestListPageResolutionsPaginateTypeDef",
    "ListPagesByContactRequestListPagesByContactPaginateTypeDef",
    "ListPagesByEngagementRequestListPagesByEngagementPaginateTypeDef",
    "ListRotationOverridesRequestListRotationOverridesPaginateTypeDef",
    "ListRotationShiftsRequestListRotationShiftsPaginateTypeDef",
    "ListRotationsRequestListRotationsPaginateTypeDef",
    "ListPageReceiptsResultTypeDef",
    "ListPageResolutionsResultTypeDef",
    "ListPagesByContactResultTypeDef",
    "ListPagesByEngagementResultTypeDef",
    "ListRotationOverridesResultTypeDef",
    "RotationShiftTypeDef",
    "ListContactChannelsResultTypeDef",
    "StageOutputTypeDef",
    "StageTypeDef",
    "RecurrenceSettingsOutputTypeDef",
    "RecurrenceSettingsTypeDef",
    "ListEngagementsRequestListEngagementsPaginateTypeDef",
    "ListEngagementsRequestRequestTypeDef",
    "ListPreviewRotationShiftsResultTypeDef",
    "ListRotationShiftsResultTypeDef",
    "PlanOutputTypeDef",
    "StageUnionTypeDef",
    "GetRotationResultTypeDef",
    "RotationTypeDef",
    "CreateRotationRequestRequestTypeDef",
    "ListPreviewRotationShiftsRequestListPreviewRotationShiftsPaginateTypeDef",
    "ListPreviewRotationShiftsRequestRequestTypeDef",
    "UpdateRotationRequestRequestTypeDef",
    "GetContactResultTypeDef",
    "PlanTypeDef",
    "ListRotationsResultTypeDef",
    "CreateContactRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
)

AcceptPageRequestRequestTypeDef = TypedDict(
    "AcceptPageRequestRequestTypeDef",
    {
        "PageId": str,
        "AcceptType": AcceptTypeType,
        "AcceptCode": str,
        "ContactChannelId": NotRequired[str],
        "Note": NotRequired[str],
        "AcceptCodeValidation": NotRequired[AcceptCodeValidationType],
    },
)
ActivateContactChannelRequestRequestTypeDef = TypedDict(
    "ActivateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
        "ActivationCode": str,
    },
)
ChannelTargetInfoTypeDef = TypedDict(
    "ChannelTargetInfoTypeDef",
    {
        "ContactChannelId": str,
        "RetryIntervalInMinutes": NotRequired[int],
    },
)
ContactChannelAddressTypeDef = TypedDict(
    "ContactChannelAddressTypeDef",
    {
        "SimpleAddress": NotRequired[str],
    },
)
ContactTargetInfoTypeDef = TypedDict(
    "ContactTargetInfoTypeDef",
    {
        "IsEssential": bool,
        "ContactId": NotRequired[str],
    },
)
ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "Type": ContactTypeType,
        "DisplayName": NotRequired[str],
    },
)
HandOffTimeTypeDef = TypedDict(
    "HandOffTimeTypeDef",
    {
        "HourOfDay": int,
        "MinuteOfHour": int,
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
DeactivateContactChannelRequestRequestTypeDef = TypedDict(
    "DeactivateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)
DeleteContactChannelRequestRequestTypeDef = TypedDict(
    "DeleteContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)
DeleteContactRequestRequestTypeDef = TypedDict(
    "DeleteContactRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)
DeleteRotationOverrideRequestRequestTypeDef = TypedDict(
    "DeleteRotationOverrideRequestRequestTypeDef",
    {
        "RotationId": str,
        "RotationOverrideId": str,
    },
)
DeleteRotationRequestRequestTypeDef = TypedDict(
    "DeleteRotationRequestRequestTypeDef",
    {
        "RotationId": str,
    },
)
DescribeEngagementRequestRequestTypeDef = TypedDict(
    "DescribeEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
    },
)
DescribePageRequestRequestTypeDef = TypedDict(
    "DescribePageRequestRequestTypeDef",
    {
        "PageId": str,
    },
)
EngagementTypeDef = TypedDict(
    "EngagementTypeDef",
    {
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "IncidentId": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "StopTime": NotRequired[datetime],
    },
)
GetContactChannelRequestRequestTypeDef = TypedDict(
    "GetContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)
GetContactPolicyRequestRequestTypeDef = TypedDict(
    "GetContactPolicyRequestRequestTypeDef",
    {
        "ContactArn": str,
    },
)
GetContactRequestRequestTypeDef = TypedDict(
    "GetContactRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)
GetRotationOverrideRequestRequestTypeDef = TypedDict(
    "GetRotationOverrideRequestRequestTypeDef",
    {
        "RotationId": str,
        "RotationOverrideId": str,
    },
)
GetRotationRequestRequestTypeDef = TypedDict(
    "GetRotationRequestRequestTypeDef",
    {
        "RotationId": str,
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
ListContactChannelsRequestRequestTypeDef = TypedDict(
    "ListContactChannelsRequestRequestTypeDef",
    {
        "ContactId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListContactsRequestRequestTypeDef = TypedDict(
    "ListContactsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AliasPrefix": NotRequired[str],
        "Type": NotRequired[ContactTypeType],
    },
)
ListPageReceiptsRequestRequestTypeDef = TypedDict(
    "ListPageReceiptsRequestRequestTypeDef",
    {
        "PageId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ReceiptTypeDef = TypedDict(
    "ReceiptTypeDef",
    {
        "ReceiptType": ReceiptTypeType,
        "ReceiptTime": datetime,
        "ContactChannelArn": NotRequired[str],
        "ReceiptInfo": NotRequired[str],
    },
)
ListPageResolutionsRequestRequestTypeDef = TypedDict(
    "ListPageResolutionsRequestRequestTypeDef",
    {
        "PageId": str,
        "NextToken": NotRequired[str],
    },
)
ResolutionContactTypeDef = TypedDict(
    "ResolutionContactTypeDef",
    {
        "ContactArn": str,
        "Type": ContactTypeType,
        "StageIndex": NotRequired[int],
    },
)
ListPagesByContactRequestRequestTypeDef = TypedDict(
    "ListPagesByContactRequestRequestTypeDef",
    {
        "ContactId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "IncidentId": NotRequired[str],
        "SentTime": NotRequired[datetime],
        "DeliveryTime": NotRequired[datetime],
        "ReadTime": NotRequired[datetime],
    },
)
ListPagesByEngagementRequestRequestTypeDef = TypedDict(
    "ListPagesByEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RotationOverrideTypeDef = TypedDict(
    "RotationOverrideTypeDef",
    {
        "RotationOverrideId": str,
        "NewContactIds": List[str],
        "StartTime": datetime,
        "EndTime": datetime,
        "CreateTime": datetime,
    },
)
ListRotationsRequestRequestTypeDef = TypedDict(
    "ListRotationsRequestRequestTypeDef",
    {
        "RotationNamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
PutContactPolicyRequestRequestTypeDef = TypedDict(
    "PutContactPolicyRequestRequestTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
    },
)
ShiftDetailsTypeDef = TypedDict(
    "ShiftDetailsTypeDef",
    {
        "OverriddenContactIds": List[str],
    },
)
SendActivationCodeRequestRequestTypeDef = TypedDict(
    "SendActivationCodeRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)
StartEngagementRequestRequestTypeDef = TypedDict(
    "StartEngagementRequestRequestTypeDef",
    {
        "ContactId": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": NotRequired[str],
        "PublicContent": NotRequired[str],
        "IncidentId": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
    },
)
StopEngagementRequestRequestTypeDef = TypedDict(
    "StopEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
        "Reason": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
ContactChannelTypeDef = TypedDict(
    "ContactChannelTypeDef",
    {
        "ContactChannelArn": str,
        "ContactArn": str,
        "Name": str,
        "DeliveryAddress": ContactChannelAddressTypeDef,
        "ActivationStatus": ActivationStatusType,
        "Type": NotRequired[ChannelTypeType],
    },
)
CreateContactChannelRequestRequestTypeDef = TypedDict(
    "CreateContactChannelRequestRequestTypeDef",
    {
        "ContactId": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": ContactChannelAddressTypeDef,
        "DeferActivation": NotRequired[bool],
        "IdempotencyToken": NotRequired[str],
    },
)
UpdateContactChannelRequestRequestTypeDef = TypedDict(
    "UpdateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
        "Name": NotRequired[str],
        "DeliveryAddress": NotRequired[ContactChannelAddressTypeDef],
    },
)
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "ChannelTargetInfo": NotRequired[ChannelTargetInfoTypeDef],
        "ContactTargetInfo": NotRequired[ContactTargetInfoTypeDef],
    },
)
CoverageTimeTypeDef = TypedDict(
    "CoverageTimeTypeDef",
    {
        "Start": NotRequired[HandOffTimeTypeDef],
        "End": NotRequired[HandOffTimeTypeDef],
    },
)
MonthlySettingTypeDef = TypedDict(
    "MonthlySettingTypeDef",
    {
        "DayOfMonth": int,
        "HandOffTime": HandOffTimeTypeDef,
    },
)
WeeklySettingTypeDef = TypedDict(
    "WeeklySettingTypeDef",
    {
        "DayOfWeek": DayOfWeekType,
        "HandOffTime": HandOffTimeTypeDef,
    },
)
CreateContactChannelResultTypeDef = TypedDict(
    "CreateContactChannelResultTypeDef",
    {
        "ContactChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContactResultTypeDef = TypedDict(
    "CreateContactResultTypeDef",
    {
        "ContactArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRotationOverrideResultTypeDef = TypedDict(
    "CreateRotationOverrideResultTypeDef",
    {
        "RotationOverrideId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRotationResultTypeDef = TypedDict(
    "CreateRotationResultTypeDef",
    {
        "RotationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEngagementResultTypeDef = TypedDict(
    "DescribeEngagementResultTypeDef",
    {
        "ContactArn": str,
        "EngagementArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "StartTime": datetime,
        "StopTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePageResultTypeDef = TypedDict(
    "DescribePageResultTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "SentTime": datetime,
        "ReadTime": datetime,
        "DeliveryTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContactChannelResultTypeDef = TypedDict(
    "GetContactChannelResultTypeDef",
    {
        "ContactArn": str,
        "ContactChannelArn": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": ContactChannelAddressTypeDef,
        "ActivationStatus": ActivationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContactPolicyResultTypeDef = TypedDict(
    "GetContactPolicyResultTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRotationOverrideResultTypeDef = TypedDict(
    "GetRotationOverrideResultTypeDef",
    {
        "RotationOverrideId": str,
        "RotationArn": str,
        "NewContactIds": List[str],
        "StartTime": datetime,
        "EndTime": datetime,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListContactsResultTypeDef = TypedDict(
    "ListContactsResultTypeDef",
    {
        "Contacts": List[ContactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartEngagementResultTypeDef = TypedDict(
    "StartEngagementResultTypeDef",
    {
        "EngagementArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
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
CreateRotationOverrideRequestRequestTypeDef = TypedDict(
    "CreateRotationOverrideRequestRequestTypeDef",
    {
        "RotationId": str,
        "NewContactIds": Sequence[str],
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "IdempotencyToken": NotRequired[str],
    },
)
ListRotationOverridesRequestRequestTypeDef = TypedDict(
    "ListRotationOverridesRequestRequestTypeDef",
    {
        "RotationId": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRotationShiftsRequestRequestTypeDef = TypedDict(
    "ListRotationShiftsRequestRequestTypeDef",
    {
        "RotationId": str,
        "EndTime": TimestampTypeDef,
        "StartTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PreviewOverrideTypeDef = TypedDict(
    "PreviewOverrideTypeDef",
    {
        "NewMembers": NotRequired[Sequence[str]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
    },
)
TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
    },
)
ListEngagementsResultTypeDef = TypedDict(
    "ListEngagementsResultTypeDef",
    {
        "Engagements": List[EngagementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListContactChannelsRequestListContactChannelsPaginateTypeDef = TypedDict(
    "ListContactChannelsRequestListContactChannelsPaginateTypeDef",
    {
        "ContactId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListContactsRequestListContactsPaginateTypeDef = TypedDict(
    "ListContactsRequestListContactsPaginateTypeDef",
    {
        "AliasPrefix": NotRequired[str],
        "Type": NotRequired[ContactTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPageReceiptsRequestListPageReceiptsPaginateTypeDef = TypedDict(
    "ListPageReceiptsRequestListPageReceiptsPaginateTypeDef",
    {
        "PageId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPageResolutionsRequestListPageResolutionsPaginateTypeDef = TypedDict(
    "ListPageResolutionsRequestListPageResolutionsPaginateTypeDef",
    {
        "PageId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPagesByContactRequestListPagesByContactPaginateTypeDef = TypedDict(
    "ListPagesByContactRequestListPagesByContactPaginateTypeDef",
    {
        "ContactId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPagesByEngagementRequestListPagesByEngagementPaginateTypeDef = TypedDict(
    "ListPagesByEngagementRequestListPagesByEngagementPaginateTypeDef",
    {
        "EngagementId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRotationOverridesRequestListRotationOverridesPaginateTypeDef = TypedDict(
    "ListRotationOverridesRequestListRotationOverridesPaginateTypeDef",
    {
        "RotationId": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRotationShiftsRequestListRotationShiftsPaginateTypeDef = TypedDict(
    "ListRotationShiftsRequestListRotationShiftsPaginateTypeDef",
    {
        "RotationId": str,
        "EndTime": TimestampTypeDef,
        "StartTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRotationsRequestListRotationsPaginateTypeDef = TypedDict(
    "ListRotationsRequestListRotationsPaginateTypeDef",
    {
        "RotationNamePrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPageReceiptsResultTypeDef = TypedDict(
    "ListPageReceiptsResultTypeDef",
    {
        "Receipts": List[ReceiptTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPageResolutionsResultTypeDef = TypedDict(
    "ListPageResolutionsResultTypeDef",
    {
        "PageResolutions": List[ResolutionContactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPagesByContactResultTypeDef = TypedDict(
    "ListPagesByContactResultTypeDef",
    {
        "Pages": List[PageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPagesByEngagementResultTypeDef = TypedDict(
    "ListPagesByEngagementResultTypeDef",
    {
        "Pages": List[PageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRotationOverridesResultTypeDef = TypedDict(
    "ListRotationOverridesResultTypeDef",
    {
        "RotationOverrides": List[RotationOverrideTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RotationShiftTypeDef = TypedDict(
    "RotationShiftTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ContactIds": NotRequired[List[str]],
        "Type": NotRequired[ShiftTypeType],
        "ShiftDetails": NotRequired[ShiftDetailsTypeDef],
    },
)
ListContactChannelsResultTypeDef = TypedDict(
    "ListContactChannelsResultTypeDef",
    {
        "ContactChannels": List[ContactChannelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StageOutputTypeDef = TypedDict(
    "StageOutputTypeDef",
    {
        "DurationInMinutes": int,
        "Targets": List[TargetTypeDef],
    },
)
StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "DurationInMinutes": int,
        "Targets": Sequence[TargetTypeDef],
    },
)
RecurrenceSettingsOutputTypeDef = TypedDict(
    "RecurrenceSettingsOutputTypeDef",
    {
        "NumberOfOnCalls": int,
        "RecurrenceMultiplier": int,
        "MonthlySettings": NotRequired[List[MonthlySettingTypeDef]],
        "WeeklySettings": NotRequired[List[WeeklySettingTypeDef]],
        "DailySettings": NotRequired[List[HandOffTimeTypeDef]],
        "ShiftCoverages": NotRequired[Dict[DayOfWeekType, List[CoverageTimeTypeDef]]],
    },
)
RecurrenceSettingsTypeDef = TypedDict(
    "RecurrenceSettingsTypeDef",
    {
        "NumberOfOnCalls": int,
        "RecurrenceMultiplier": int,
        "MonthlySettings": NotRequired[Sequence[MonthlySettingTypeDef]],
        "WeeklySettings": NotRequired[Sequence[WeeklySettingTypeDef]],
        "DailySettings": NotRequired[Sequence[HandOffTimeTypeDef]],
        "ShiftCoverages": NotRequired[Mapping[DayOfWeekType, Sequence[CoverageTimeTypeDef]]],
    },
)
ListEngagementsRequestListEngagementsPaginateTypeDef = TypedDict(
    "ListEngagementsRequestListEngagementsPaginateTypeDef",
    {
        "IncidentId": NotRequired[str],
        "TimeRangeValue": NotRequired[TimeRangeTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEngagementsRequestRequestTypeDef = TypedDict(
    "ListEngagementsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncidentId": NotRequired[str],
        "TimeRangeValue": NotRequired[TimeRangeTypeDef],
    },
)
ListPreviewRotationShiftsResultTypeDef = TypedDict(
    "ListPreviewRotationShiftsResultTypeDef",
    {
        "RotationShifts": List[RotationShiftTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRotationShiftsResultTypeDef = TypedDict(
    "ListRotationShiftsResultTypeDef",
    {
        "RotationShifts": List[RotationShiftTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PlanOutputTypeDef = TypedDict(
    "PlanOutputTypeDef",
    {
        "Stages": NotRequired[List[StageOutputTypeDef]],
        "RotationIds": NotRequired[List[str]],
    },
)
StageUnionTypeDef = Union[StageTypeDef, StageOutputTypeDef]
GetRotationResultTypeDef = TypedDict(
    "GetRotationResultTypeDef",
    {
        "RotationArn": str,
        "Name": str,
        "ContactIds": List[str],
        "StartTime": datetime,
        "TimeZoneId": str,
        "Recurrence": RecurrenceSettingsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RotationTypeDef = TypedDict(
    "RotationTypeDef",
    {
        "RotationArn": str,
        "Name": str,
        "ContactIds": NotRequired[List[str]],
        "StartTime": NotRequired[datetime],
        "TimeZoneId": NotRequired[str],
        "Recurrence": NotRequired[RecurrenceSettingsOutputTypeDef],
    },
)
CreateRotationRequestRequestTypeDef = TypedDict(
    "CreateRotationRequestRequestTypeDef",
    {
        "Name": str,
        "ContactIds": Sequence[str],
        "TimeZoneId": str,
        "Recurrence": RecurrenceSettingsTypeDef,
        "StartTime": NotRequired[TimestampTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "IdempotencyToken": NotRequired[str],
    },
)
ListPreviewRotationShiftsRequestListPreviewRotationShiftsPaginateTypeDef = TypedDict(
    "ListPreviewRotationShiftsRequestListPreviewRotationShiftsPaginateTypeDef",
    {
        "EndTime": TimestampTypeDef,
        "Members": Sequence[str],
        "TimeZoneId": str,
        "Recurrence": RecurrenceSettingsTypeDef,
        "RotationStartTime": NotRequired[TimestampTypeDef],
        "StartTime": NotRequired[TimestampTypeDef],
        "Overrides": NotRequired[Sequence[PreviewOverrideTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPreviewRotationShiftsRequestRequestTypeDef = TypedDict(
    "ListPreviewRotationShiftsRequestRequestTypeDef",
    {
        "EndTime": TimestampTypeDef,
        "Members": Sequence[str],
        "TimeZoneId": str,
        "Recurrence": RecurrenceSettingsTypeDef,
        "RotationStartTime": NotRequired[TimestampTypeDef],
        "StartTime": NotRequired[TimestampTypeDef],
        "Overrides": NotRequired[Sequence[PreviewOverrideTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
UpdateRotationRequestRequestTypeDef = TypedDict(
    "UpdateRotationRequestRequestTypeDef",
    {
        "RotationId": str,
        "Recurrence": RecurrenceSettingsTypeDef,
        "ContactIds": NotRequired[Sequence[str]],
        "StartTime": NotRequired[TimestampTypeDef],
        "TimeZoneId": NotRequired[str],
    },
)
GetContactResultTypeDef = TypedDict(
    "GetContactResultTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "DisplayName": str,
        "Type": ContactTypeType,
        "Plan": PlanOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PlanTypeDef = TypedDict(
    "PlanTypeDef",
    {
        "Stages": NotRequired[Sequence[StageUnionTypeDef]],
        "RotationIds": NotRequired[Sequence[str]],
    },
)
ListRotationsResultTypeDef = TypedDict(
    "ListRotationsResultTypeDef",
    {
        "Rotations": List[RotationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateContactRequestRequestTypeDef = TypedDict(
    "CreateContactRequestRequestTypeDef",
    {
        "Alias": str,
        "Type": ContactTypeType,
        "Plan": PlanTypeDef,
        "DisplayName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "IdempotencyToken": NotRequired[str],
    },
)
UpdateContactRequestRequestTypeDef = TypedDict(
    "UpdateContactRequestRequestTypeDef",
    {
        "ContactId": str,
        "DisplayName": NotRequired[str],
        "Plan": NotRequired[PlanTypeDef],
    },
)
