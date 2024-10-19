"""
Type annotations for mailmanager service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/type_defs/)

Usage::

    ```python
    from mypy_boto3_mailmanager.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AcceptActionType,
    ActionFailurePolicyType,
    ArchiveBooleanOperatorType,
    ArchiveStateType,
    ArchiveStringEmailAttributeType,
    ExportStateType,
    IngressBooleanOperatorType,
    IngressIpOperatorType,
    IngressPointStatusToUpdateType,
    IngressPointStatusType,
    IngressPointTypeType,
    IngressStringOperatorType,
    IngressTlsProtocolAttributeType,
    IngressTlsProtocolOperatorType,
    MailFromType,
    RetentionPeriodType,
    RuleBooleanEmailAttributeType,
    RuleBooleanOperatorType,
    RuleDmarcOperatorType,
    RuleDmarcPolicyType,
    RuleIpOperatorType,
    RuleNumberOperatorType,
    RuleStringEmailAttributeType,
    RuleStringOperatorType,
    RuleVerdictAttributeType,
    RuleVerdictOperatorType,
    RuleVerdictType,
    SearchStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddHeaderActionTypeDef",
    "AddonInstanceTypeDef",
    "AddonSubscriptionTypeDef",
    "AnalysisTypeDef",
    "ArchiveActionTypeDef",
    "ArchiveBooleanToEvaluateTypeDef",
    "ArchiveRetentionTypeDef",
    "ArchiveStringToEvaluateTypeDef",
    "ArchiveTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "IngressPointConfigurationTypeDef",
    "RelayAuthenticationTypeDef",
    "DeleteAddonInstanceRequestRequestTypeDef",
    "DeleteAddonSubscriptionRequestRequestTypeDef",
    "DeleteArchiveRequestRequestTypeDef",
    "DeleteIngressPointRequestRequestTypeDef",
    "DeleteRelayRequestRequestTypeDef",
    "DeleteRuleSetRequestRequestTypeDef",
    "DeleteTrafficPolicyRequestRequestTypeDef",
    "DeliverToMailboxActionTypeDef",
    "EnvelopeTypeDef",
    "S3ExportDestinationConfigurationTypeDef",
    "ExportStatusTypeDef",
    "GetAddonInstanceRequestRequestTypeDef",
    "GetAddonSubscriptionRequestRequestTypeDef",
    "GetArchiveExportRequestRequestTypeDef",
    "GetArchiveMessageContentRequestRequestTypeDef",
    "MessageBodyTypeDef",
    "GetArchiveMessageRequestRequestTypeDef",
    "MetadataTypeDef",
    "GetArchiveRequestRequestTypeDef",
    "GetArchiveSearchRequestRequestTypeDef",
    "SearchStatusTypeDef",
    "GetArchiveSearchResultsRequestRequestTypeDef",
    "GetIngressPointRequestRequestTypeDef",
    "GetRelayRequestRequestTypeDef",
    "RelayAuthenticationOutputTypeDef",
    "GetRuleSetRequestRequestTypeDef",
    "GetTrafficPolicyRequestRequestTypeDef",
    "IngressAnalysisTypeDef",
    "IngressIpToEvaluateTypeDef",
    "IngressPointPasswordConfigurationTypeDef",
    "IngressPointTypeDef",
    "IngressStringToEvaluateTypeDef",
    "IngressTlsProtocolToEvaluateTypeDef",
    "PaginatorConfigTypeDef",
    "ListAddonInstancesRequestRequestTypeDef",
    "ListAddonSubscriptionsRequestRequestTypeDef",
    "ListArchiveExportsRequestRequestTypeDef",
    "ListArchiveSearchesRequestRequestTypeDef",
    "ListArchivesRequestRequestTypeDef",
    "ListIngressPointsRequestRequestTypeDef",
    "ListRelaysRequestRequestTypeDef",
    "RelayTypeDef",
    "ListRuleSetsRequestRequestTypeDef",
    "RuleSetTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTrafficPoliciesRequestRequestTypeDef",
    "TrafficPolicyTypeDef",
    "RelayActionTypeDef",
    "ReplaceRecipientActionOutputTypeDef",
    "ReplaceRecipientActionTypeDef",
    "S3ActionTypeDef",
    "SendActionTypeDef",
    "RuleBooleanToEvaluateTypeDef",
    "RuleDmarcExpressionOutputTypeDef",
    "RuleDmarcExpressionTypeDef",
    "RuleIpToEvaluateTypeDef",
    "RuleNumberToEvaluateTypeDef",
    "RuleStringToEvaluateTypeDef",
    "TimestampTypeDef",
    "StopArchiveExportRequestRequestTypeDef",
    "StopArchiveSearchRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "RuleVerdictToEvaluateTypeDef",
    "ArchiveBooleanExpressionTypeDef",
    "UpdateArchiveRequestRequestTypeDef",
    "ArchiveStringExpressionOutputTypeDef",
    "ArchiveStringExpressionTypeDef",
    "CreateAddonInstanceRequestRequestTypeDef",
    "CreateAddonSubscriptionRequestRequestTypeDef",
    "CreateArchiveRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAddonInstanceResponseTypeDef",
    "CreateAddonSubscriptionResponseTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateIngressPointResponseTypeDef",
    "CreateRelayResponseTypeDef",
    "CreateRuleSetResponseTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "GetAddonInstanceResponseTypeDef",
    "GetAddonSubscriptionResponseTypeDef",
    "GetArchiveResponseTypeDef",
    "ListAddonInstancesResponseTypeDef",
    "ListAddonSubscriptionsResponseTypeDef",
    "ListArchivesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartArchiveExportResponseTypeDef",
    "StartArchiveSearchResponseTypeDef",
    "CreateIngressPointRequestRequestTypeDef",
    "UpdateIngressPointRequestRequestTypeDef",
    "CreateRelayRequestRequestTypeDef",
    "UpdateRelayRequestRequestTypeDef",
    "RowTypeDef",
    "ExportDestinationConfigurationTypeDef",
    "ExportSummaryTypeDef",
    "GetArchiveMessageContentResponseTypeDef",
    "GetArchiveMessageResponseTypeDef",
    "SearchSummaryTypeDef",
    "GetRelayResponseTypeDef",
    "IngressBooleanToEvaluateTypeDef",
    "IngressIpv4ExpressionOutputTypeDef",
    "IngressIpv4ExpressionTypeDef",
    "IngressPointAuthConfigurationTypeDef",
    "ListIngressPointsResponseTypeDef",
    "IngressStringExpressionOutputTypeDef",
    "IngressStringExpressionTypeDef",
    "IngressTlsProtocolExpressionTypeDef",
    "ListAddonInstancesRequestListAddonInstancesPaginateTypeDef",
    "ListAddonSubscriptionsRequestListAddonSubscriptionsPaginateTypeDef",
    "ListArchiveExportsRequestListArchiveExportsPaginateTypeDef",
    "ListArchiveSearchesRequestListArchiveSearchesPaginateTypeDef",
    "ListArchivesRequestListArchivesPaginateTypeDef",
    "ListIngressPointsRequestListIngressPointsPaginateTypeDef",
    "ListRelaysRequestListRelaysPaginateTypeDef",
    "ListRuleSetsRequestListRuleSetsPaginateTypeDef",
    "ListTrafficPoliciesRequestListTrafficPoliciesPaginateTypeDef",
    "ListRelaysResponseTypeDef",
    "ListRuleSetsResponseTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "ReplaceRecipientActionUnionTypeDef",
    "RuleActionOutputTypeDef",
    "RuleBooleanExpressionTypeDef",
    "RuleDmarcExpressionUnionTypeDef",
    "RuleIpExpressionOutputTypeDef",
    "RuleIpExpressionTypeDef",
    "RuleNumberExpressionTypeDef",
    "RuleStringExpressionOutputTypeDef",
    "RuleStringExpressionTypeDef",
    "RuleVerdictExpressionOutputTypeDef",
    "RuleVerdictExpressionTypeDef",
    "ArchiveFilterConditionOutputTypeDef",
    "ArchiveStringExpressionUnionTypeDef",
    "GetArchiveSearchResultsResponseTypeDef",
    "ListArchiveExportsResponseTypeDef",
    "ListArchiveSearchesResponseTypeDef",
    "IngressBooleanExpressionTypeDef",
    "IngressIpv4ExpressionUnionTypeDef",
    "GetIngressPointResponseTypeDef",
    "IngressStringExpressionUnionTypeDef",
    "RuleActionTypeDef",
    "RuleIpExpressionUnionTypeDef",
    "RuleStringExpressionUnionTypeDef",
    "RuleConditionOutputTypeDef",
    "RuleVerdictExpressionUnionTypeDef",
    "ArchiveFiltersOutputTypeDef",
    "ArchiveFilterConditionTypeDef",
    "PolicyConditionOutputTypeDef",
    "PolicyConditionTypeDef",
    "RuleActionUnionTypeDef",
    "RuleOutputTypeDef",
    "RuleConditionTypeDef",
    "GetArchiveExportResponseTypeDef",
    "GetArchiveSearchResponseTypeDef",
    "ArchiveFilterConditionUnionTypeDef",
    "PolicyStatementOutputTypeDef",
    "PolicyConditionUnionTypeDef",
    "GetRuleSetResponseTypeDef",
    "RuleConditionUnionTypeDef",
    "ArchiveFiltersTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "PolicyStatementTypeDef",
    "RuleTypeDef",
    "StartArchiveExportRequestRequestTypeDef",
    "StartArchiveSearchRequestRequestTypeDef",
    "PolicyStatementUnionTypeDef",
    "UpdateTrafficPolicyRequestRequestTypeDef",
    "RuleUnionTypeDef",
    "UpdateRuleSetRequestRequestTypeDef",
    "CreateTrafficPolicyRequestRequestTypeDef",
    "CreateRuleSetRequestRequestTypeDef",
)

AddHeaderActionTypeDef = TypedDict(
    "AddHeaderActionTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)
AddonInstanceTypeDef = TypedDict(
    "AddonInstanceTypeDef",
    {
        "AddonInstanceArn": NotRequired[str],
        "AddonInstanceId": NotRequired[str],
        "AddonName": NotRequired[str],
        "AddonSubscriptionId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)
AddonSubscriptionTypeDef = TypedDict(
    "AddonSubscriptionTypeDef",
    {
        "AddonName": NotRequired[str],
        "AddonSubscriptionArn": NotRequired[str],
        "AddonSubscriptionId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)
AnalysisTypeDef = TypedDict(
    "AnalysisTypeDef",
    {
        "Analyzer": str,
        "ResultField": str,
    },
)
ArchiveActionTypeDef = TypedDict(
    "ArchiveActionTypeDef",
    {
        "TargetArchive": str,
        "ActionFailurePolicy": NotRequired[ActionFailurePolicyType],
    },
)
ArchiveBooleanToEvaluateTypeDef = TypedDict(
    "ArchiveBooleanToEvaluateTypeDef",
    {
        "Attribute": NotRequired[Literal["HAS_ATTACHMENTS"]],
    },
)
ArchiveRetentionTypeDef = TypedDict(
    "ArchiveRetentionTypeDef",
    {
        "RetentionPeriod": NotRequired[RetentionPeriodType],
    },
)
ArchiveStringToEvaluateTypeDef = TypedDict(
    "ArchiveStringToEvaluateTypeDef",
    {
        "Attribute": NotRequired[ArchiveStringEmailAttributeType],
    },
)
ArchiveTypeDef = TypedDict(
    "ArchiveTypeDef",
    {
        "ArchiveId": str,
        "ArchiveName": NotRequired[str],
        "ArchiveState": NotRequired[ArchiveStateType],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
IngressPointConfigurationTypeDef = TypedDict(
    "IngressPointConfigurationTypeDef",
    {
        "SecretArn": NotRequired[str],
        "SmtpPassword": NotRequired[str],
    },
)
RelayAuthenticationTypeDef = TypedDict(
    "RelayAuthenticationTypeDef",
    {
        "NoAuthentication": NotRequired[Mapping[str, Any]],
        "SecretArn": NotRequired[str],
    },
)
DeleteAddonInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAddonInstanceRequestRequestTypeDef",
    {
        "AddonInstanceId": str,
    },
)
DeleteAddonSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAddonSubscriptionRequestRequestTypeDef",
    {
        "AddonSubscriptionId": str,
    },
)
DeleteArchiveRequestRequestTypeDef = TypedDict(
    "DeleteArchiveRequestRequestTypeDef",
    {
        "ArchiveId": str,
    },
)
DeleteIngressPointRequestRequestTypeDef = TypedDict(
    "DeleteIngressPointRequestRequestTypeDef",
    {
        "IngressPointId": str,
    },
)
DeleteRelayRequestRequestTypeDef = TypedDict(
    "DeleteRelayRequestRequestTypeDef",
    {
        "RelayId": str,
    },
)
DeleteRuleSetRequestRequestTypeDef = TypedDict(
    "DeleteRuleSetRequestRequestTypeDef",
    {
        "RuleSetId": str,
    },
)
DeleteTrafficPolicyRequestRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
    },
)
DeliverToMailboxActionTypeDef = TypedDict(
    "DeliverToMailboxActionTypeDef",
    {
        "MailboxArn": str,
        "RoleArn": str,
        "ActionFailurePolicy": NotRequired[ActionFailurePolicyType],
    },
)
EnvelopeTypeDef = TypedDict(
    "EnvelopeTypeDef",
    {
        "From": NotRequired[str],
        "Helo": NotRequired[str],
        "To": NotRequired[List[str]],
    },
)
S3ExportDestinationConfigurationTypeDef = TypedDict(
    "S3ExportDestinationConfigurationTypeDef",
    {
        "S3Location": NotRequired[str],
    },
)
ExportStatusTypeDef = TypedDict(
    "ExportStatusTypeDef",
    {
        "CompletionTimestamp": NotRequired[datetime],
        "ErrorMessage": NotRequired[str],
        "State": NotRequired[ExportStateType],
        "SubmissionTimestamp": NotRequired[datetime],
    },
)
GetAddonInstanceRequestRequestTypeDef = TypedDict(
    "GetAddonInstanceRequestRequestTypeDef",
    {
        "AddonInstanceId": str,
    },
)
GetAddonSubscriptionRequestRequestTypeDef = TypedDict(
    "GetAddonSubscriptionRequestRequestTypeDef",
    {
        "AddonSubscriptionId": str,
    },
)
GetArchiveExportRequestRequestTypeDef = TypedDict(
    "GetArchiveExportRequestRequestTypeDef",
    {
        "ExportId": str,
    },
)
GetArchiveMessageContentRequestRequestTypeDef = TypedDict(
    "GetArchiveMessageContentRequestRequestTypeDef",
    {
        "ArchivedMessageId": str,
    },
)
MessageBodyTypeDef = TypedDict(
    "MessageBodyTypeDef",
    {
        "Html": NotRequired[str],
        "MessageMalformed": NotRequired[bool],
        "Text": NotRequired[str],
    },
)
GetArchiveMessageRequestRequestTypeDef = TypedDict(
    "GetArchiveMessageRequestRequestTypeDef",
    {
        "ArchivedMessageId": str,
    },
)
MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "IngressPointId": NotRequired[str],
        "RuleSetId": NotRequired[str],
        "SenderHostname": NotRequired[str],
        "SenderIpAddress": NotRequired[str],
        "Timestamp": NotRequired[datetime],
        "TlsCipherSuite": NotRequired[str],
        "TlsProtocol": NotRequired[str],
        "TrafficPolicyId": NotRequired[str],
    },
)
GetArchiveRequestRequestTypeDef = TypedDict(
    "GetArchiveRequestRequestTypeDef",
    {
        "ArchiveId": str,
    },
)
GetArchiveSearchRequestRequestTypeDef = TypedDict(
    "GetArchiveSearchRequestRequestTypeDef",
    {
        "SearchId": str,
    },
)
SearchStatusTypeDef = TypedDict(
    "SearchStatusTypeDef",
    {
        "CompletionTimestamp": NotRequired[datetime],
        "ErrorMessage": NotRequired[str],
        "State": NotRequired[SearchStateType],
        "SubmissionTimestamp": NotRequired[datetime],
    },
)
GetArchiveSearchResultsRequestRequestTypeDef = TypedDict(
    "GetArchiveSearchResultsRequestRequestTypeDef",
    {
        "SearchId": str,
    },
)
GetIngressPointRequestRequestTypeDef = TypedDict(
    "GetIngressPointRequestRequestTypeDef",
    {
        "IngressPointId": str,
    },
)
GetRelayRequestRequestTypeDef = TypedDict(
    "GetRelayRequestRequestTypeDef",
    {
        "RelayId": str,
    },
)
RelayAuthenticationOutputTypeDef = TypedDict(
    "RelayAuthenticationOutputTypeDef",
    {
        "NoAuthentication": NotRequired[Dict[str, Any]],
        "SecretArn": NotRequired[str],
    },
)
GetRuleSetRequestRequestTypeDef = TypedDict(
    "GetRuleSetRequestRequestTypeDef",
    {
        "RuleSetId": str,
    },
)
GetTrafficPolicyRequestRequestTypeDef = TypedDict(
    "GetTrafficPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
    },
)
IngressAnalysisTypeDef = TypedDict(
    "IngressAnalysisTypeDef",
    {
        "Analyzer": str,
        "ResultField": str,
    },
)
IngressIpToEvaluateTypeDef = TypedDict(
    "IngressIpToEvaluateTypeDef",
    {
        "Attribute": NotRequired[Literal["SENDER_IP"]],
    },
)
IngressPointPasswordConfigurationTypeDef = TypedDict(
    "IngressPointPasswordConfigurationTypeDef",
    {
        "PreviousSmtpPasswordExpiryTimestamp": NotRequired[datetime],
        "PreviousSmtpPasswordVersion": NotRequired[str],
        "SmtpPasswordVersion": NotRequired[str],
    },
)
IngressPointTypeDef = TypedDict(
    "IngressPointTypeDef",
    {
        "IngressPointId": str,
        "IngressPointName": str,
        "Status": IngressPointStatusType,
        "Type": IngressPointTypeType,
        "ARecord": NotRequired[str],
    },
)
IngressStringToEvaluateTypeDef = TypedDict(
    "IngressStringToEvaluateTypeDef",
    {
        "Attribute": NotRequired[Literal["RECIPIENT"]],
    },
)
IngressTlsProtocolToEvaluateTypeDef = TypedDict(
    "IngressTlsProtocolToEvaluateTypeDef",
    {
        "Attribute": NotRequired[Literal["TLS_PROTOCOL"]],
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
ListAddonInstancesRequestRequestTypeDef = TypedDict(
    "ListAddonInstancesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListAddonSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListAddonSubscriptionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListArchiveExportsRequestRequestTypeDef = TypedDict(
    "ListArchiveExportsRequestRequestTypeDef",
    {
        "ArchiveId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListArchiveSearchesRequestRequestTypeDef = TypedDict(
    "ListArchiveSearchesRequestRequestTypeDef",
    {
        "ArchiveId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListArchivesRequestRequestTypeDef = TypedDict(
    "ListArchivesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListIngressPointsRequestRequestTypeDef = TypedDict(
    "ListIngressPointsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListRelaysRequestRequestTypeDef = TypedDict(
    "ListRelaysRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
RelayTypeDef = TypedDict(
    "RelayTypeDef",
    {
        "LastModifiedTimestamp": NotRequired[datetime],
        "RelayId": NotRequired[str],
        "RelayName": NotRequired[str],
    },
)
ListRuleSetsRequestRequestTypeDef = TypedDict(
    "ListRuleSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
RuleSetTypeDef = TypedDict(
    "RuleSetTypeDef",
    {
        "LastModificationDate": NotRequired[datetime],
        "RuleSetId": NotRequired[str],
        "RuleSetName": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListTrafficPoliciesRequestRequestTypeDef = TypedDict(
    "ListTrafficPoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
TrafficPolicyTypeDef = TypedDict(
    "TrafficPolicyTypeDef",
    {
        "DefaultAction": AcceptActionType,
        "TrafficPolicyId": str,
        "TrafficPolicyName": str,
    },
)
RelayActionTypeDef = TypedDict(
    "RelayActionTypeDef",
    {
        "Relay": str,
        "ActionFailurePolicy": NotRequired[ActionFailurePolicyType],
        "MailFrom": NotRequired[MailFromType],
    },
)
ReplaceRecipientActionOutputTypeDef = TypedDict(
    "ReplaceRecipientActionOutputTypeDef",
    {
        "ReplaceWith": NotRequired[List[str]],
    },
)
ReplaceRecipientActionTypeDef = TypedDict(
    "ReplaceRecipientActionTypeDef",
    {
        "ReplaceWith": NotRequired[Sequence[str]],
    },
)
S3ActionTypeDef = TypedDict(
    "S3ActionTypeDef",
    {
        "RoleArn": str,
        "S3Bucket": str,
        "ActionFailurePolicy": NotRequired[ActionFailurePolicyType],
        "S3Prefix": NotRequired[str],
        "S3SseKmsKeyId": NotRequired[str],
    },
)
SendActionTypeDef = TypedDict(
    "SendActionTypeDef",
    {
        "RoleArn": str,
        "ActionFailurePolicy": NotRequired[ActionFailurePolicyType],
    },
)
RuleBooleanToEvaluateTypeDef = TypedDict(
    "RuleBooleanToEvaluateTypeDef",
    {
        "Attribute": NotRequired[RuleBooleanEmailAttributeType],
    },
)
RuleDmarcExpressionOutputTypeDef = TypedDict(
    "RuleDmarcExpressionOutputTypeDef",
    {
        "Operator": RuleDmarcOperatorType,
        "Values": List[RuleDmarcPolicyType],
    },
)
RuleDmarcExpressionTypeDef = TypedDict(
    "RuleDmarcExpressionTypeDef",
    {
        "Operator": RuleDmarcOperatorType,
        "Values": Sequence[RuleDmarcPolicyType],
    },
)
RuleIpToEvaluateTypeDef = TypedDict(
    "RuleIpToEvaluateTypeDef",
    {
        "Attribute": NotRequired[Literal["SOURCE_IP"]],
    },
)
RuleNumberToEvaluateTypeDef = TypedDict(
    "RuleNumberToEvaluateTypeDef",
    {
        "Attribute": NotRequired[Literal["MESSAGE_SIZE"]],
    },
)
RuleStringToEvaluateTypeDef = TypedDict(
    "RuleStringToEvaluateTypeDef",
    {
        "Attribute": NotRequired[RuleStringEmailAttributeType],
        "MimeHeaderAttribute": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
StopArchiveExportRequestRequestTypeDef = TypedDict(
    "StopArchiveExportRequestRequestTypeDef",
    {
        "ExportId": str,
    },
)
StopArchiveSearchRequestRequestTypeDef = TypedDict(
    "StopArchiveSearchRequestRequestTypeDef",
    {
        "SearchId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
RuleVerdictToEvaluateTypeDef = TypedDict(
    "RuleVerdictToEvaluateTypeDef",
    {
        "Analysis": NotRequired[AnalysisTypeDef],
        "Attribute": NotRequired[RuleVerdictAttributeType],
    },
)
ArchiveBooleanExpressionTypeDef = TypedDict(
    "ArchiveBooleanExpressionTypeDef",
    {
        "Evaluate": ArchiveBooleanToEvaluateTypeDef,
        "Operator": ArchiveBooleanOperatorType,
    },
)
UpdateArchiveRequestRequestTypeDef = TypedDict(
    "UpdateArchiveRequestRequestTypeDef",
    {
        "ArchiveId": str,
        "ArchiveName": NotRequired[str],
        "Retention": NotRequired[ArchiveRetentionTypeDef],
    },
)
ArchiveStringExpressionOutputTypeDef = TypedDict(
    "ArchiveStringExpressionOutputTypeDef",
    {
        "Evaluate": ArchiveStringToEvaluateTypeDef,
        "Operator": Literal["CONTAINS"],
        "Values": List[str],
    },
)
ArchiveStringExpressionTypeDef = TypedDict(
    "ArchiveStringExpressionTypeDef",
    {
        "Evaluate": ArchiveStringToEvaluateTypeDef,
        "Operator": Literal["CONTAINS"],
        "Values": Sequence[str],
    },
)
CreateAddonInstanceRequestRequestTypeDef = TypedDict(
    "CreateAddonInstanceRequestRequestTypeDef",
    {
        "AddonSubscriptionId": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateAddonSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateAddonSubscriptionRequestRequestTypeDef",
    {
        "AddonName": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateArchiveRequestRequestTypeDef = TypedDict(
    "CreateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
        "ClientToken": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "Retention": NotRequired[ArchiveRetentionTypeDef],
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
CreateAddonInstanceResponseTypeDef = TypedDict(
    "CreateAddonInstanceResponseTypeDef",
    {
        "AddonInstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAddonSubscriptionResponseTypeDef = TypedDict(
    "CreateAddonSubscriptionResponseTypeDef",
    {
        "AddonSubscriptionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateArchiveResponseTypeDef = TypedDict(
    "CreateArchiveResponseTypeDef",
    {
        "ArchiveId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIngressPointResponseTypeDef = TypedDict(
    "CreateIngressPointResponseTypeDef",
    {
        "IngressPointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRelayResponseTypeDef = TypedDict(
    "CreateRelayResponseTypeDef",
    {
        "RelayId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRuleSetResponseTypeDef = TypedDict(
    "CreateRuleSetResponseTypeDef",
    {
        "RuleSetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrafficPolicyResponseTypeDef = TypedDict(
    "CreateTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAddonInstanceResponseTypeDef = TypedDict(
    "GetAddonInstanceResponseTypeDef",
    {
        "AddonInstanceArn": str,
        "AddonName": str,
        "AddonSubscriptionId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAddonSubscriptionResponseTypeDef = TypedDict(
    "GetAddonSubscriptionResponseTypeDef",
    {
        "AddonName": str,
        "AddonSubscriptionArn": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetArchiveResponseTypeDef = TypedDict(
    "GetArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "ArchiveId": str,
        "ArchiveName": str,
        "ArchiveState": ArchiveStateType,
        "CreatedTimestamp": datetime,
        "KmsKeyArn": str,
        "LastUpdatedTimestamp": datetime,
        "Retention": ArchiveRetentionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAddonInstancesResponseTypeDef = TypedDict(
    "ListAddonInstancesResponseTypeDef",
    {
        "AddonInstances": List[AddonInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAddonSubscriptionsResponseTypeDef = TypedDict(
    "ListAddonSubscriptionsResponseTypeDef",
    {
        "AddonSubscriptions": List[AddonSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListArchivesResponseTypeDef = TypedDict(
    "ListArchivesResponseTypeDef",
    {
        "Archives": List[ArchiveTypeDef],
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
StartArchiveExportResponseTypeDef = TypedDict(
    "StartArchiveExportResponseTypeDef",
    {
        "ExportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartArchiveSearchResponseTypeDef = TypedDict(
    "StartArchiveSearchResponseTypeDef",
    {
        "SearchId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIngressPointRequestRequestTypeDef = TypedDict(
    "CreateIngressPointRequestRequestTypeDef",
    {
        "IngressPointName": str,
        "RuleSetId": str,
        "TrafficPolicyId": str,
        "Type": IngressPointTypeType,
        "ClientToken": NotRequired[str],
        "IngressPointConfiguration": NotRequired[IngressPointConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateIngressPointRequestRequestTypeDef = TypedDict(
    "UpdateIngressPointRequestRequestTypeDef",
    {
        "IngressPointId": str,
        "IngressPointConfiguration": NotRequired[IngressPointConfigurationTypeDef],
        "IngressPointName": NotRequired[str],
        "RuleSetId": NotRequired[str],
        "StatusToUpdate": NotRequired[IngressPointStatusToUpdateType],
        "TrafficPolicyId": NotRequired[str],
    },
)
CreateRelayRequestRequestTypeDef = TypedDict(
    "CreateRelayRequestRequestTypeDef",
    {
        "Authentication": RelayAuthenticationTypeDef,
        "RelayName": str,
        "ServerName": str,
        "ServerPort": int,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateRelayRequestRequestTypeDef = TypedDict(
    "UpdateRelayRequestRequestTypeDef",
    {
        "RelayId": str,
        "Authentication": NotRequired[RelayAuthenticationTypeDef],
        "RelayName": NotRequired[str],
        "ServerName": NotRequired[str],
        "ServerPort": NotRequired[int],
    },
)
RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "ArchivedMessageId": NotRequired[str],
        "Cc": NotRequired[str],
        "Date": NotRequired[str],
        "Envelope": NotRequired[EnvelopeTypeDef],
        "From": NotRequired[str],
        "HasAttachments": NotRequired[bool],
        "InReplyTo": NotRequired[str],
        "IngressPointId": NotRequired[str],
        "MessageId": NotRequired[str],
        "ReceivedHeaders": NotRequired[List[str]],
        "ReceivedTimestamp": NotRequired[datetime],
        "SenderHostname": NotRequired[str],
        "SenderIpAddress": NotRequired[str],
        "Subject": NotRequired[str],
        "To": NotRequired[str],
        "XMailer": NotRequired[str],
        "XOriginalMailer": NotRequired[str],
        "XPriority": NotRequired[str],
    },
)
ExportDestinationConfigurationTypeDef = TypedDict(
    "ExportDestinationConfigurationTypeDef",
    {
        "S3": NotRequired[S3ExportDestinationConfigurationTypeDef],
    },
)
ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "ExportId": NotRequired[str],
        "Status": NotRequired[ExportStatusTypeDef],
    },
)
GetArchiveMessageContentResponseTypeDef = TypedDict(
    "GetArchiveMessageContentResponseTypeDef",
    {
        "Body": MessageBodyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetArchiveMessageResponseTypeDef = TypedDict(
    "GetArchiveMessageResponseTypeDef",
    {
        "Envelope": EnvelopeTypeDef,
        "MessageDownloadLink": str,
        "Metadata": MetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchSummaryTypeDef = TypedDict(
    "SearchSummaryTypeDef",
    {
        "SearchId": NotRequired[str],
        "Status": NotRequired[SearchStatusTypeDef],
    },
)
GetRelayResponseTypeDef = TypedDict(
    "GetRelayResponseTypeDef",
    {
        "Authentication": RelayAuthenticationOutputTypeDef,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "RelayArn": str,
        "RelayId": str,
        "RelayName": str,
        "ServerName": str,
        "ServerPort": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IngressBooleanToEvaluateTypeDef = TypedDict(
    "IngressBooleanToEvaluateTypeDef",
    {
        "Analysis": NotRequired[IngressAnalysisTypeDef],
    },
)
IngressIpv4ExpressionOutputTypeDef = TypedDict(
    "IngressIpv4ExpressionOutputTypeDef",
    {
        "Evaluate": IngressIpToEvaluateTypeDef,
        "Operator": IngressIpOperatorType,
        "Values": List[str],
    },
)
IngressIpv4ExpressionTypeDef = TypedDict(
    "IngressIpv4ExpressionTypeDef",
    {
        "Evaluate": IngressIpToEvaluateTypeDef,
        "Operator": IngressIpOperatorType,
        "Values": Sequence[str],
    },
)
IngressPointAuthConfigurationTypeDef = TypedDict(
    "IngressPointAuthConfigurationTypeDef",
    {
        "IngressPointPasswordConfiguration": NotRequired[IngressPointPasswordConfigurationTypeDef],
        "SecretArn": NotRequired[str],
    },
)
ListIngressPointsResponseTypeDef = TypedDict(
    "ListIngressPointsResponseTypeDef",
    {
        "IngressPoints": List[IngressPointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
IngressStringExpressionOutputTypeDef = TypedDict(
    "IngressStringExpressionOutputTypeDef",
    {
        "Evaluate": IngressStringToEvaluateTypeDef,
        "Operator": IngressStringOperatorType,
        "Values": List[str],
    },
)
IngressStringExpressionTypeDef = TypedDict(
    "IngressStringExpressionTypeDef",
    {
        "Evaluate": IngressStringToEvaluateTypeDef,
        "Operator": IngressStringOperatorType,
        "Values": Sequence[str],
    },
)
IngressTlsProtocolExpressionTypeDef = TypedDict(
    "IngressTlsProtocolExpressionTypeDef",
    {
        "Evaluate": IngressTlsProtocolToEvaluateTypeDef,
        "Operator": IngressTlsProtocolOperatorType,
        "Value": IngressTlsProtocolAttributeType,
    },
)
ListAddonInstancesRequestListAddonInstancesPaginateTypeDef = TypedDict(
    "ListAddonInstancesRequestListAddonInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAddonSubscriptionsRequestListAddonSubscriptionsPaginateTypeDef = TypedDict(
    "ListAddonSubscriptionsRequestListAddonSubscriptionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListArchiveExportsRequestListArchiveExportsPaginateTypeDef = TypedDict(
    "ListArchiveExportsRequestListArchiveExportsPaginateTypeDef",
    {
        "ArchiveId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListArchiveSearchesRequestListArchiveSearchesPaginateTypeDef = TypedDict(
    "ListArchiveSearchesRequestListArchiveSearchesPaginateTypeDef",
    {
        "ArchiveId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListArchivesRequestListArchivesPaginateTypeDef = TypedDict(
    "ListArchivesRequestListArchivesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIngressPointsRequestListIngressPointsPaginateTypeDef = TypedDict(
    "ListIngressPointsRequestListIngressPointsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRelaysRequestListRelaysPaginateTypeDef = TypedDict(
    "ListRelaysRequestListRelaysPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRuleSetsRequestListRuleSetsPaginateTypeDef = TypedDict(
    "ListRuleSetsRequestListRuleSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrafficPoliciesRequestListTrafficPoliciesPaginateTypeDef = TypedDict(
    "ListTrafficPoliciesRequestListTrafficPoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRelaysResponseTypeDef = TypedDict(
    "ListRelaysResponseTypeDef",
    {
        "Relays": List[RelayTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRuleSetsResponseTypeDef = TypedDict(
    "ListRuleSetsResponseTypeDef",
    {
        "RuleSets": List[RuleSetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTrafficPoliciesResponseTypeDef = TypedDict(
    "ListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicies": List[TrafficPolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ReplaceRecipientActionUnionTypeDef = Union[
    ReplaceRecipientActionTypeDef, ReplaceRecipientActionOutputTypeDef
]
RuleActionOutputTypeDef = TypedDict(
    "RuleActionOutputTypeDef",
    {
        "AddHeader": NotRequired[AddHeaderActionTypeDef],
        "Archive": NotRequired[ArchiveActionTypeDef],
        "DeliverToMailbox": NotRequired[DeliverToMailboxActionTypeDef],
        "Drop": NotRequired[Dict[str, Any]],
        "Relay": NotRequired[RelayActionTypeDef],
        "ReplaceRecipient": NotRequired[ReplaceRecipientActionOutputTypeDef],
        "Send": NotRequired[SendActionTypeDef],
        "WriteToS3": NotRequired[S3ActionTypeDef],
    },
)
RuleBooleanExpressionTypeDef = TypedDict(
    "RuleBooleanExpressionTypeDef",
    {
        "Evaluate": RuleBooleanToEvaluateTypeDef,
        "Operator": RuleBooleanOperatorType,
    },
)
RuleDmarcExpressionUnionTypeDef = Union[
    RuleDmarcExpressionTypeDef, RuleDmarcExpressionOutputTypeDef
]
RuleIpExpressionOutputTypeDef = TypedDict(
    "RuleIpExpressionOutputTypeDef",
    {
        "Evaluate": RuleIpToEvaluateTypeDef,
        "Operator": RuleIpOperatorType,
        "Values": List[str],
    },
)
RuleIpExpressionTypeDef = TypedDict(
    "RuleIpExpressionTypeDef",
    {
        "Evaluate": RuleIpToEvaluateTypeDef,
        "Operator": RuleIpOperatorType,
        "Values": Sequence[str],
    },
)
RuleNumberExpressionTypeDef = TypedDict(
    "RuleNumberExpressionTypeDef",
    {
        "Evaluate": RuleNumberToEvaluateTypeDef,
        "Operator": RuleNumberOperatorType,
        "Value": float,
    },
)
RuleStringExpressionOutputTypeDef = TypedDict(
    "RuleStringExpressionOutputTypeDef",
    {
        "Evaluate": RuleStringToEvaluateTypeDef,
        "Operator": RuleStringOperatorType,
        "Values": List[str],
    },
)
RuleStringExpressionTypeDef = TypedDict(
    "RuleStringExpressionTypeDef",
    {
        "Evaluate": RuleStringToEvaluateTypeDef,
        "Operator": RuleStringOperatorType,
        "Values": Sequence[str],
    },
)
RuleVerdictExpressionOutputTypeDef = TypedDict(
    "RuleVerdictExpressionOutputTypeDef",
    {
        "Evaluate": RuleVerdictToEvaluateTypeDef,
        "Operator": RuleVerdictOperatorType,
        "Values": List[RuleVerdictType],
    },
)
RuleVerdictExpressionTypeDef = TypedDict(
    "RuleVerdictExpressionTypeDef",
    {
        "Evaluate": RuleVerdictToEvaluateTypeDef,
        "Operator": RuleVerdictOperatorType,
        "Values": Sequence[RuleVerdictType],
    },
)
ArchiveFilterConditionOutputTypeDef = TypedDict(
    "ArchiveFilterConditionOutputTypeDef",
    {
        "BooleanExpression": NotRequired[ArchiveBooleanExpressionTypeDef],
        "StringExpression": NotRequired[ArchiveStringExpressionOutputTypeDef],
    },
)
ArchiveStringExpressionUnionTypeDef = Union[
    ArchiveStringExpressionTypeDef, ArchiveStringExpressionOutputTypeDef
]
GetArchiveSearchResultsResponseTypeDef = TypedDict(
    "GetArchiveSearchResultsResponseTypeDef",
    {
        "Rows": List[RowTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListArchiveExportsResponseTypeDef = TypedDict(
    "ListArchiveExportsResponseTypeDef",
    {
        "Exports": List[ExportSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListArchiveSearchesResponseTypeDef = TypedDict(
    "ListArchiveSearchesResponseTypeDef",
    {
        "Searches": List[SearchSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
IngressBooleanExpressionTypeDef = TypedDict(
    "IngressBooleanExpressionTypeDef",
    {
        "Evaluate": IngressBooleanToEvaluateTypeDef,
        "Operator": IngressBooleanOperatorType,
    },
)
IngressIpv4ExpressionUnionTypeDef = Union[
    IngressIpv4ExpressionTypeDef, IngressIpv4ExpressionOutputTypeDef
]
GetIngressPointResponseTypeDef = TypedDict(
    "GetIngressPointResponseTypeDef",
    {
        "ARecord": str,
        "CreatedTimestamp": datetime,
        "IngressPointArn": str,
        "IngressPointAuthConfiguration": IngressPointAuthConfigurationTypeDef,
        "IngressPointId": str,
        "IngressPointName": str,
        "LastUpdatedTimestamp": datetime,
        "RuleSetId": str,
        "Status": IngressPointStatusType,
        "TrafficPolicyId": str,
        "Type": IngressPointTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IngressStringExpressionUnionTypeDef = Union[
    IngressStringExpressionTypeDef, IngressStringExpressionOutputTypeDef
]
RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "AddHeader": NotRequired[AddHeaderActionTypeDef],
        "Archive": NotRequired[ArchiveActionTypeDef],
        "DeliverToMailbox": NotRequired[DeliverToMailboxActionTypeDef],
        "Drop": NotRequired[Mapping[str, Any]],
        "Relay": NotRequired[RelayActionTypeDef],
        "ReplaceRecipient": NotRequired[ReplaceRecipientActionUnionTypeDef],
        "Send": NotRequired[SendActionTypeDef],
        "WriteToS3": NotRequired[S3ActionTypeDef],
    },
)
RuleIpExpressionUnionTypeDef = Union[RuleIpExpressionTypeDef, RuleIpExpressionOutputTypeDef]
RuleStringExpressionUnionTypeDef = Union[
    RuleStringExpressionTypeDef, RuleStringExpressionOutputTypeDef
]
RuleConditionOutputTypeDef = TypedDict(
    "RuleConditionOutputTypeDef",
    {
        "BooleanExpression": NotRequired[RuleBooleanExpressionTypeDef],
        "DmarcExpression": NotRequired[RuleDmarcExpressionOutputTypeDef],
        "IpExpression": NotRequired[RuleIpExpressionOutputTypeDef],
        "NumberExpression": NotRequired[RuleNumberExpressionTypeDef],
        "StringExpression": NotRequired[RuleStringExpressionOutputTypeDef],
        "VerdictExpression": NotRequired[RuleVerdictExpressionOutputTypeDef],
    },
)
RuleVerdictExpressionUnionTypeDef = Union[
    RuleVerdictExpressionTypeDef, RuleVerdictExpressionOutputTypeDef
]
ArchiveFiltersOutputTypeDef = TypedDict(
    "ArchiveFiltersOutputTypeDef",
    {
        "Include": NotRequired[List[ArchiveFilterConditionOutputTypeDef]],
        "Unless": NotRequired[List[ArchiveFilterConditionOutputTypeDef]],
    },
)
ArchiveFilterConditionTypeDef = TypedDict(
    "ArchiveFilterConditionTypeDef",
    {
        "BooleanExpression": NotRequired[ArchiveBooleanExpressionTypeDef],
        "StringExpression": NotRequired[ArchiveStringExpressionUnionTypeDef],
    },
)
PolicyConditionOutputTypeDef = TypedDict(
    "PolicyConditionOutputTypeDef",
    {
        "BooleanExpression": NotRequired[IngressBooleanExpressionTypeDef],
        "IpExpression": NotRequired[IngressIpv4ExpressionOutputTypeDef],
        "StringExpression": NotRequired[IngressStringExpressionOutputTypeDef],
        "TlsExpression": NotRequired[IngressTlsProtocolExpressionTypeDef],
    },
)
PolicyConditionTypeDef = TypedDict(
    "PolicyConditionTypeDef",
    {
        "BooleanExpression": NotRequired[IngressBooleanExpressionTypeDef],
        "IpExpression": NotRequired[IngressIpv4ExpressionUnionTypeDef],
        "StringExpression": NotRequired[IngressStringExpressionUnionTypeDef],
        "TlsExpression": NotRequired[IngressTlsProtocolExpressionTypeDef],
    },
)
RuleActionUnionTypeDef = Union[RuleActionTypeDef, RuleActionOutputTypeDef]
RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "Actions": List[RuleActionOutputTypeDef],
        "Conditions": NotRequired[List[RuleConditionOutputTypeDef]],
        "Name": NotRequired[str],
        "Unless": NotRequired[List[RuleConditionOutputTypeDef]],
    },
)
RuleConditionTypeDef = TypedDict(
    "RuleConditionTypeDef",
    {
        "BooleanExpression": NotRequired[RuleBooleanExpressionTypeDef],
        "DmarcExpression": NotRequired[RuleDmarcExpressionUnionTypeDef],
        "IpExpression": NotRequired[RuleIpExpressionUnionTypeDef],
        "NumberExpression": NotRequired[RuleNumberExpressionTypeDef],
        "StringExpression": NotRequired[RuleStringExpressionUnionTypeDef],
        "VerdictExpression": NotRequired[RuleVerdictExpressionUnionTypeDef],
    },
)
GetArchiveExportResponseTypeDef = TypedDict(
    "GetArchiveExportResponseTypeDef",
    {
        "ArchiveId": str,
        "ExportDestinationConfiguration": ExportDestinationConfigurationTypeDef,
        "Filters": ArchiveFiltersOutputTypeDef,
        "FromTimestamp": datetime,
        "MaxResults": int,
        "Status": ExportStatusTypeDef,
        "ToTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetArchiveSearchResponseTypeDef = TypedDict(
    "GetArchiveSearchResponseTypeDef",
    {
        "ArchiveId": str,
        "Filters": ArchiveFiltersOutputTypeDef,
        "FromTimestamp": datetime,
        "MaxResults": int,
        "Status": SearchStatusTypeDef,
        "ToTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ArchiveFilterConditionUnionTypeDef = Union[
    ArchiveFilterConditionTypeDef, ArchiveFilterConditionOutputTypeDef
]
PolicyStatementOutputTypeDef = TypedDict(
    "PolicyStatementOutputTypeDef",
    {
        "Action": AcceptActionType,
        "Conditions": List[PolicyConditionOutputTypeDef],
    },
)
PolicyConditionUnionTypeDef = Union[PolicyConditionTypeDef, PolicyConditionOutputTypeDef]
GetRuleSetResponseTypeDef = TypedDict(
    "GetRuleSetResponseTypeDef",
    {
        "CreatedDate": datetime,
        "LastModificationDate": datetime,
        "RuleSetArn": str,
        "RuleSetId": str,
        "RuleSetName": str,
        "Rules": List[RuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleConditionUnionTypeDef = Union[RuleConditionTypeDef, RuleConditionOutputTypeDef]
ArchiveFiltersTypeDef = TypedDict(
    "ArchiveFiltersTypeDef",
    {
        "Include": NotRequired[Sequence[ArchiveFilterConditionUnionTypeDef]],
        "Unless": NotRequired[Sequence[ArchiveFilterConditionTypeDef]],
    },
)
GetTrafficPolicyResponseTypeDef = TypedDict(
    "GetTrafficPolicyResponseTypeDef",
    {
        "CreatedTimestamp": datetime,
        "DefaultAction": AcceptActionType,
        "LastUpdatedTimestamp": datetime,
        "MaxMessageSizeBytes": int,
        "PolicyStatements": List[PolicyStatementOutputTypeDef],
        "TrafficPolicyArn": str,
        "TrafficPolicyId": str,
        "TrafficPolicyName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyStatementTypeDef = TypedDict(
    "PolicyStatementTypeDef",
    {
        "Action": AcceptActionType,
        "Conditions": Sequence[PolicyConditionUnionTypeDef],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Actions": Sequence[RuleActionUnionTypeDef],
        "Conditions": NotRequired[Sequence[RuleConditionUnionTypeDef]],
        "Name": NotRequired[str],
        "Unless": NotRequired[Sequence[RuleConditionTypeDef]],
    },
)
StartArchiveExportRequestRequestTypeDef = TypedDict(
    "StartArchiveExportRequestRequestTypeDef",
    {
        "ArchiveId": str,
        "ExportDestinationConfiguration": ExportDestinationConfigurationTypeDef,
        "FromTimestamp": TimestampTypeDef,
        "ToTimestamp": TimestampTypeDef,
        "Filters": NotRequired[ArchiveFiltersTypeDef],
        "IncludeMetadata": NotRequired[bool],
        "MaxResults": NotRequired[int],
    },
)
StartArchiveSearchRequestRequestTypeDef = TypedDict(
    "StartArchiveSearchRequestRequestTypeDef",
    {
        "ArchiveId": str,
        "FromTimestamp": TimestampTypeDef,
        "MaxResults": int,
        "ToTimestamp": TimestampTypeDef,
        "Filters": NotRequired[ArchiveFiltersTypeDef],
    },
)
PolicyStatementUnionTypeDef = Union[PolicyStatementTypeDef, PolicyStatementOutputTypeDef]
UpdateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
        "DefaultAction": NotRequired[AcceptActionType],
        "MaxMessageSizeBytes": NotRequired[int],
        "PolicyStatements": NotRequired[Sequence[PolicyStatementTypeDef]],
        "TrafficPolicyName": NotRequired[str],
    },
)
RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]
UpdateRuleSetRequestRequestTypeDef = TypedDict(
    "UpdateRuleSetRequestRequestTypeDef",
    {
        "RuleSetId": str,
        "RuleSetName": NotRequired[str],
        "Rules": NotRequired[Sequence[RuleTypeDef]],
    },
)
CreateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "CreateTrafficPolicyRequestRequestTypeDef",
    {
        "DefaultAction": AcceptActionType,
        "PolicyStatements": Sequence[PolicyStatementUnionTypeDef],
        "TrafficPolicyName": str,
        "ClientToken": NotRequired[str],
        "MaxMessageSizeBytes": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRuleSetRequestRequestTypeDef = TypedDict(
    "CreateRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rules": Sequence[RuleUnionTypeDef],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
