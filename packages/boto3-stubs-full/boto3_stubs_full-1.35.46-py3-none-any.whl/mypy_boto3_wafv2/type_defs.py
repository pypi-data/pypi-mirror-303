"""
Type annotations for wafv2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/type_defs/)

Usage::

    ```python
    from mypy_boto3_wafv2.type_defs import APIKeySummaryTypeDef

    data: APIKeySummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ActionValueType,
    AssociatedResourceTypeType,
    BodyParsingFallbackBehaviorType,
    ComparisonOperatorType,
    CountryCodeType,
    FailureReasonType,
    FallbackBehaviorType,
    FilterBehaviorType,
    FilterRequirementType,
    ForwardedIPPositionType,
    InspectionLevelType,
    IPAddressVersionType,
    JsonMatchScopeType,
    LabelMatchScopeType,
    LogScopeType,
    MapMatchScopeType,
    OversizeHandlingType,
    PayloadTypeType,
    PlatformType,
    PositionalConstraintType,
    RateBasedStatementAggregateKeyTypeType,
    ResourceTypeType,
    ResponseContentTypeType,
    ScopeType,
    SensitivityLevelType,
    SizeInspectionLimitType,
    TextTransformationTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "APIKeySummaryTypeDef",
    "AWSManagedRulesBotControlRuleSetTypeDef",
    "ActionConditionTypeDef",
    "AddressFieldTypeDef",
    "AndStatementOutputTypeDef",
    "AndStatementTypeDef",
    "AssociateWebACLRequestRequestTypeDef",
    "RequestBodyAssociatedResourceTypeConfigTypeDef",
    "BlobTypeDef",
    "BodyTypeDef",
    "TextTransformationTypeDef",
    "ImmunityTimePropertyTypeDef",
    "CaptchaResponseTypeDef",
    "ChallengeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "LabelNameConditionTypeDef",
    "CookieMatchPatternOutputTypeDef",
    "CookieMatchPatternTypeDef",
    "CreateAPIKeyRequestRequestTypeDef",
    "TagTypeDef",
    "IPSetSummaryTypeDef",
    "RegexTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "CustomResponseBodyTypeDef",
    "VisibilityConfigTypeDef",
    "RuleGroupSummaryTypeDef",
    "WebACLSummaryTypeDef",
    "CustomHTTPHeaderTypeDef",
    "DeleteAPIKeyRequestRequestTypeDef",
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeletePermissionPolicyRequestRequestTypeDef",
    "DeleteRegexPatternSetRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteWebACLRequestRequestTypeDef",
    "DescribeAllManagedProductsRequestRequestTypeDef",
    "ManagedProductDescriptorTypeDef",
    "DescribeManagedProductsByVendorRequestRequestTypeDef",
    "DescribeManagedRuleGroupRequestRequestTypeDef",
    "LabelSummaryTypeDef",
    "DisassociateWebACLRequestRequestTypeDef",
    "EmailFieldTypeDef",
    "ExcludedRuleTypeDef",
    "HeaderOrderTypeDef",
    "JA3FingerprintTypeDef",
    "SingleHeaderTypeDef",
    "SingleQueryArgumentTypeDef",
    "ForwardedIPConfigTypeDef",
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    "GetDecryptedAPIKeyRequestRequestTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "IPSetTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetManagedRuleSetRequestRequestTypeDef",
    "GetMobileSdkReleaseRequestRequestTypeDef",
    "GetPermissionPolicyRequestRequestTypeDef",
    "GetRateBasedStatementManagedKeysRequestRequestTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "GetRegexPatternSetRequestRequestTypeDef",
    "GetRuleGroupRequestRequestTypeDef",
    "TimeWindowOutputTypeDef",
    "GetWebACLForResourceRequestRequestTypeDef",
    "GetWebACLRequestRequestTypeDef",
    "HTTPHeaderTypeDef",
    "HeaderMatchPatternOutputTypeDef",
    "HeaderMatchPatternTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "JsonMatchPatternOutputTypeDef",
    "JsonMatchPatternTypeDef",
    "LabelMatchStatementTypeDef",
    "LabelTypeDef",
    "ListAPIKeysRequestRequestTypeDef",
    "ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    "ManagedRuleGroupVersionTypeDef",
    "ListAvailableManagedRuleGroupsRequestRequestTypeDef",
    "ManagedRuleGroupSummaryTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListManagedRuleSetsRequestRequestTypeDef",
    "ManagedRuleSetSummaryTypeDef",
    "ListMobileSdkReleasesRequestRequestTypeDef",
    "ReleaseSummaryTypeDef",
    "ListRegexPatternSetsRequestRequestTypeDef",
    "ListResourcesForWebACLRequestRequestTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWebACLsRequestRequestTypeDef",
    "PasswordFieldTypeDef",
    "UsernameFieldTypeDef",
    "ManagedRuleSetVersionTypeDef",
    "NotStatementOutputTypeDef",
    "NotStatementTypeDef",
    "OrStatementOutputTypeDef",
    "OrStatementTypeDef",
    "PhoneNumberFieldTypeDef",
    "VersionToPublishTypeDef",
    "PutPermissionPolicyRequestRequestTypeDef",
    "RateLimitLabelNamespaceTypeDef",
    "ResponseInspectionBodyContainsOutputTypeDef",
    "ResponseInspectionBodyContainsTypeDef",
    "ResponseInspectionHeaderOutputTypeDef",
    "ResponseInspectionHeaderTypeDef",
    "ResponseInspectionJsonOutputTypeDef",
    "ResponseInspectionJsonTypeDef",
    "ResponseInspectionStatusCodeOutputTypeDef",
    "ResponseInspectionStatusCodeTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "AndStatementUnionTypeDef",
    "AssociationConfigOutputTypeDef",
    "AssociationConfigTypeDef",
    "RateLimitCookieOutputTypeDef",
    "RateLimitCookieTypeDef",
    "RateLimitHeaderOutputTypeDef",
    "RateLimitHeaderTypeDef",
    "RateLimitQueryArgumentOutputTypeDef",
    "RateLimitQueryArgumentTypeDef",
    "RateLimitQueryStringOutputTypeDef",
    "RateLimitQueryStringTypeDef",
    "RateLimitUriPathOutputTypeDef",
    "RateLimitUriPathTypeDef",
    "CaptchaConfigTypeDef",
    "ChallengeConfigTypeDef",
    "CheckCapacityResponseTypeDef",
    "CreateAPIKeyResponseTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    "GetDecryptedAPIKeyResponseTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "ListAPIKeysResponseTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "PutManagedRuleSetVersionsResponseTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateWebACLResponseTypeDef",
    "ConditionTypeDef",
    "CookiesOutputTypeDef",
    "CookieMatchPatternUnionTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "MobileSdkReleaseTypeDef",
    "TagInfoForResourceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "CreateRegexPatternSetRequestRequestTypeDef",
    "RegexPatternSetTypeDef",
    "UpdateRegexPatternSetRequestRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "CreateWebACLResponseTypeDef",
    "ListWebACLsResponseTypeDef",
    "CustomRequestHandlingOutputTypeDef",
    "CustomRequestHandlingTypeDef",
    "CustomResponseOutputTypeDef",
    "CustomResponseTypeDef",
    "DescribeAllManagedProductsResponseTypeDef",
    "DescribeManagedProductsByVendorResponseTypeDef",
    "GeoMatchStatementOutputTypeDef",
    "GeoMatchStatementTypeDef",
    "GetIPSetResponseTypeDef",
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    "HTTPRequestTypeDef",
    "HeadersOutputTypeDef",
    "HeaderMatchPatternUnionTypeDef",
    "IPSetReferenceStatementTypeDef",
    "JsonBodyOutputTypeDef",
    "JsonMatchPatternUnionTypeDef",
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    "ListManagedRuleSetsResponseTypeDef",
    "ListMobileSdkReleasesResponseTypeDef",
    "RequestInspectionTypeDef",
    "ManagedRuleSetTypeDef",
    "NotStatementUnionTypeDef",
    "OrStatementUnionTypeDef",
    "RequestInspectionACFPOutputTypeDef",
    "RequestInspectionACFPTypeDef",
    "PutManagedRuleSetVersionsRequestRequestTypeDef",
    "ResponseInspectionBodyContainsUnionTypeDef",
    "ResponseInspectionHeaderUnionTypeDef",
    "ResponseInspectionJsonUnionTypeDef",
    "ResponseInspectionOutputTypeDef",
    "ResponseInspectionStatusCodeUnionTypeDef",
    "TimeWindowTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef",
    "RateLimitCookieUnionTypeDef",
    "RateLimitHeaderUnionTypeDef",
    "RateLimitQueryArgumentUnionTypeDef",
    "RateLimitQueryStringUnionTypeDef",
    "RateBasedStatementCustomKeyOutputTypeDef",
    "RateLimitUriPathUnionTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "CookiesTypeDef",
    "GetMobileSdkReleaseResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "AllowActionOutputTypeDef",
    "CaptchaActionOutputTypeDef",
    "ChallengeActionOutputTypeDef",
    "CountActionOutputTypeDef",
    "CustomRequestHandlingUnionTypeDef",
    "BlockActionOutputTypeDef",
    "CustomResponseUnionTypeDef",
    "GeoMatchStatementUnionTypeDef",
    "SampledHTTPRequestTypeDef",
    "HeadersTypeDef",
    "FieldToMatchOutputTypeDef",
    "JsonBodyTypeDef",
    "GetManagedRuleSetResponseTypeDef",
    "RequestInspectionACFPUnionTypeDef",
    "AWSManagedRulesACFPRuleSetOutputTypeDef",
    "AWSManagedRulesATPRuleSetOutputTypeDef",
    "ResponseInspectionTypeDef",
    "GetSampledRequestsRequestRequestTypeDef",
    "RateBasedStatementOutputTypeDef",
    "RateBasedStatementCustomKeyTypeDef",
    "LoggingFilterOutputTypeDef",
    "FilterUnionTypeDef",
    "CookiesUnionTypeDef",
    "OverrideActionOutputTypeDef",
    "AllowActionTypeDef",
    "CaptchaActionTypeDef",
    "ChallengeActionTypeDef",
    "CountActionTypeDef",
    "DefaultActionOutputTypeDef",
    "RuleActionOutputTypeDef",
    "BlockActionTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "HeadersUnionTypeDef",
    "ByteMatchStatementOutputTypeDef",
    "RegexMatchStatementOutputTypeDef",
    "RegexPatternSetReferenceStatementOutputTypeDef",
    "SizeConstraintStatementOutputTypeDef",
    "SqliMatchStatementOutputTypeDef",
    "XssMatchStatementOutputTypeDef",
    "JsonBodyUnionTypeDef",
    "ManagedRuleGroupConfigOutputTypeDef",
    "ResponseInspectionUnionTypeDef",
    "RateBasedStatementCustomKeyUnionTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingFilterTypeDef",
    "AllowActionUnionTypeDef",
    "CaptchaActionUnionTypeDef",
    "ChallengeActionUnionTypeDef",
    "CountActionUnionTypeDef",
    "RuleActionOverrideOutputTypeDef",
    "RuleSummaryTypeDef",
    "BlockActionUnionTypeDef",
    "FieldToMatchTypeDef",
    "AWSManagedRulesACFPRuleSetTypeDef",
    "AWSManagedRulesATPRuleSetTypeDef",
    "RateBasedStatementTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "LoggingFilterUnionTypeDef",
    "OverrideActionTypeDef",
    "ManagedRuleGroupStatementOutputTypeDef",
    "RuleGroupReferenceStatementOutputTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "DefaultActionTypeDef",
    "RuleActionTypeDef",
    "FieldToMatchUnionTypeDef",
    "AWSManagedRulesACFPRuleSetUnionTypeDef",
    "AWSManagedRulesATPRuleSetUnionTypeDef",
    "RateBasedStatementUnionTypeDef",
    "OverrideActionUnionTypeDef",
    "FirewallManagerStatementTypeDef",
    "StatementOutputTypeDef",
    "RuleActionUnionTypeDef",
    "ByteMatchStatementTypeDef",
    "LoggingConfigurationTypeDef",
    "RegexMatchStatementTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "SizeConstraintStatementTypeDef",
    "SqliMatchStatementTypeDef",
    "XssMatchStatementTypeDef",
    "ManagedRuleGroupConfigTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "RuleOutputTypeDef",
    "RuleActionOverrideTypeDef",
    "ByteMatchStatementUnionTypeDef",
    "PutLoggingConfigurationRequestRequestTypeDef",
    "RegexMatchStatementUnionTypeDef",
    "RegexPatternSetReferenceStatementUnionTypeDef",
    "SizeConstraintStatementUnionTypeDef",
    "SqliMatchStatementUnionTypeDef",
    "XssMatchStatementUnionTypeDef",
    "ManagedRuleGroupConfigUnionTypeDef",
    "RuleGroupTypeDef",
    "WebACLTypeDef",
    "RuleActionOverrideUnionTypeDef",
    "ManagedRuleGroupStatementTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLResponseTypeDef",
    "RuleGroupReferenceStatementTypeDef",
    "ManagedRuleGroupStatementUnionTypeDef",
    "RuleGroupReferenceStatementUnionTypeDef",
    "StatementTypeDef",
    "StatementUnionTypeDef",
    "RuleTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateWebACLRequestRequestTypeDef",
    "RuleUnionTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateWebACLRequestRequestTypeDef",
    "CheckCapacityRequestRequestTypeDef",
)

APIKeySummaryTypeDef = TypedDict(
    "APIKeySummaryTypeDef",
    {
        "TokenDomains": NotRequired[List[str]],
        "APIKey": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Version": NotRequired[int],
    },
)
AWSManagedRulesBotControlRuleSetTypeDef = TypedDict(
    "AWSManagedRulesBotControlRuleSetTypeDef",
    {
        "InspectionLevel": InspectionLevelType,
        "EnableMachineLearning": NotRequired[bool],
    },
)
ActionConditionTypeDef = TypedDict(
    "ActionConditionTypeDef",
    {
        "Action": ActionValueType,
    },
)
AddressFieldTypeDef = TypedDict(
    "AddressFieldTypeDef",
    {
        "Identifier": str,
    },
)
AndStatementOutputTypeDef = TypedDict(
    "AndStatementOutputTypeDef",
    {
        "Statements": List[Dict[str, Any]],
    },
)
AndStatementTypeDef = TypedDict(
    "AndStatementTypeDef",
    {
        "Statements": Sequence[Mapping[str, Any]],
    },
)
AssociateWebACLRequestRequestTypeDef = TypedDict(
    "AssociateWebACLRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "ResourceArn": str,
    },
)
RequestBodyAssociatedResourceTypeConfigTypeDef = TypedDict(
    "RequestBodyAssociatedResourceTypeConfigTypeDef",
    {
        "DefaultSizeInspectionLimit": SizeInspectionLimitType,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "OversizeHandling": NotRequired[OversizeHandlingType],
    },
)
TextTransformationTypeDef = TypedDict(
    "TextTransformationTypeDef",
    {
        "Priority": int,
        "Type": TextTransformationTypeType,
    },
)
ImmunityTimePropertyTypeDef = TypedDict(
    "ImmunityTimePropertyTypeDef",
    {
        "ImmunityTime": int,
    },
)
CaptchaResponseTypeDef = TypedDict(
    "CaptchaResponseTypeDef",
    {
        "ResponseCode": NotRequired[int],
        "SolveTimestamp": NotRequired[int],
        "FailureReason": NotRequired[FailureReasonType],
    },
)
ChallengeResponseTypeDef = TypedDict(
    "ChallengeResponseTypeDef",
    {
        "ResponseCode": NotRequired[int],
        "SolveTimestamp": NotRequired[int],
        "FailureReason": NotRequired[FailureReasonType],
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
LabelNameConditionTypeDef = TypedDict(
    "LabelNameConditionTypeDef",
    {
        "LabelName": str,
    },
)
CookieMatchPatternOutputTypeDef = TypedDict(
    "CookieMatchPatternOutputTypeDef",
    {
        "All": NotRequired[Dict[str, Any]],
        "IncludedCookies": NotRequired[List[str]],
        "ExcludedCookies": NotRequired[List[str]],
    },
)
CookieMatchPatternTypeDef = TypedDict(
    "CookieMatchPatternTypeDef",
    {
        "All": NotRequired[Mapping[str, Any]],
        "IncludedCookies": NotRequired[Sequence[str]],
        "ExcludedCookies": NotRequired[Sequence[str]],
    },
)
CreateAPIKeyRequestRequestTypeDef = TypedDict(
    "CreateAPIKeyRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "TokenDomains": Sequence[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
RegexTypeDef = TypedDict(
    "RegexTypeDef",
    {
        "RegexString": NotRequired[str],
    },
)
RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
CustomResponseBodyTypeDef = TypedDict(
    "CustomResponseBodyTypeDef",
    {
        "ContentType": ResponseContentTypeType,
        "Content": str,
    },
)
VisibilityConfigTypeDef = TypedDict(
    "VisibilityConfigTypeDef",
    {
        "SampledRequestsEnabled": bool,
        "CloudWatchMetricsEnabled": bool,
        "MetricName": str,
    },
)
RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
CustomHTTPHeaderTypeDef = TypedDict(
    "CustomHTTPHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
DeleteAPIKeyRequestRequestTypeDef = TypedDict(
    "DeleteAPIKeyRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "APIKey": str,
    },
)
DeleteFirewallManagerRuleGroupsRequestRequestTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "WebACLLockToken": str,
    },
)
DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)
DeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "LogType": NotRequired[Literal["WAF_LOGS"]],
        "LogScope": NotRequired[LogScopeType],
    },
)
DeletePermissionPolicyRequestRequestTypeDef = TypedDict(
    "DeletePermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DeleteRegexPatternSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)
DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)
DeleteWebACLRequestRequestTypeDef = TypedDict(
    "DeleteWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)
DescribeAllManagedProductsRequestRequestTypeDef = TypedDict(
    "DescribeAllManagedProductsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
ManagedProductDescriptorTypeDef = TypedDict(
    "ManagedProductDescriptorTypeDef",
    {
        "VendorName": NotRequired[str],
        "ManagedRuleSetName": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductLink": NotRequired[str],
        "ProductTitle": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "IsVersioningSupported": NotRequired[bool],
        "IsAdvancedManagedRuleSet": NotRequired[bool],
    },
)
DescribeManagedProductsByVendorRequestRequestTypeDef = TypedDict(
    "DescribeManagedProductsByVendorRequestRequestTypeDef",
    {
        "VendorName": str,
        "Scope": ScopeType,
    },
)
DescribeManagedRuleGroupRequestRequestTypeDef = TypedDict(
    "DescribeManagedRuleGroupRequestRequestTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Scope": ScopeType,
        "VersionName": NotRequired[str],
    },
)
LabelSummaryTypeDef = TypedDict(
    "LabelSummaryTypeDef",
    {
        "Name": NotRequired[str],
    },
)
DisassociateWebACLRequestRequestTypeDef = TypedDict(
    "DisassociateWebACLRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
EmailFieldTypeDef = TypedDict(
    "EmailFieldTypeDef",
    {
        "Identifier": str,
    },
)
ExcludedRuleTypeDef = TypedDict(
    "ExcludedRuleTypeDef",
    {
        "Name": str,
    },
)
HeaderOrderTypeDef = TypedDict(
    "HeaderOrderTypeDef",
    {
        "OversizeHandling": OversizeHandlingType,
    },
)
JA3FingerprintTypeDef = TypedDict(
    "JA3FingerprintTypeDef",
    {
        "FallbackBehavior": FallbackBehaviorType,
    },
)
SingleHeaderTypeDef = TypedDict(
    "SingleHeaderTypeDef",
    {
        "Name": str,
    },
)
SingleQueryArgumentTypeDef = TypedDict(
    "SingleQueryArgumentTypeDef",
    {
        "Name": str,
    },
)
ForwardedIPConfigTypeDef = TypedDict(
    "ForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
    },
)
GenerateMobileSdkReleaseUrlRequestRequestTypeDef = TypedDict(
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "ReleaseVersion": str,
    },
)
GetDecryptedAPIKeyRequestRequestTypeDef = TypedDict(
    "GetDecryptedAPIKeyRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "APIKey": str,
    },
)
GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)
IPSetTypeDef = TypedDict(
    "IPSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
        "Description": NotRequired[str],
    },
)
GetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "LogType": NotRequired[Literal["WAF_LOGS"]],
        "LogScope": NotRequired[LogScopeType],
    },
)
GetManagedRuleSetRequestRequestTypeDef = TypedDict(
    "GetManagedRuleSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)
GetMobileSdkReleaseRequestRequestTypeDef = TypedDict(
    "GetMobileSdkReleaseRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "ReleaseVersion": str,
    },
)
GetPermissionPolicyRequestRequestTypeDef = TypedDict(
    "GetPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetRateBasedStatementManagedKeysRequestRequestTypeDef = TypedDict(
    "GetRateBasedStatementManagedKeysRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "WebACLName": str,
        "WebACLId": str,
        "RuleName": str,
        "RuleGroupRuleName": NotRequired[str],
    },
)
RateBasedStatementManagedKeysIPSetTypeDef = TypedDict(
    "RateBasedStatementManagedKeysIPSetTypeDef",
    {
        "IPAddressVersion": NotRequired[IPAddressVersionType],
        "Addresses": NotRequired[List[str]],
    },
)
GetRegexPatternSetRequestRequestTypeDef = TypedDict(
    "GetRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)
GetRuleGroupRequestRequestTypeDef = TypedDict(
    "GetRuleGroupRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "Scope": NotRequired[ScopeType],
        "Id": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
TimeWindowOutputTypeDef = TypedDict(
    "TimeWindowOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
)
GetWebACLForResourceRequestRequestTypeDef = TypedDict(
    "GetWebACLForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetWebACLRequestRequestTypeDef = TypedDict(
    "GetWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)
HTTPHeaderTypeDef = TypedDict(
    "HTTPHeaderTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
HeaderMatchPatternOutputTypeDef = TypedDict(
    "HeaderMatchPatternOutputTypeDef",
    {
        "All": NotRequired[Dict[str, Any]],
        "IncludedHeaders": NotRequired[List[str]],
        "ExcludedHeaders": NotRequired[List[str]],
    },
)
HeaderMatchPatternTypeDef = TypedDict(
    "HeaderMatchPatternTypeDef",
    {
        "All": NotRequired[Mapping[str, Any]],
        "IncludedHeaders": NotRequired[Sequence[str]],
        "ExcludedHeaders": NotRequired[Sequence[str]],
    },
)
IPSetForwardedIPConfigTypeDef = TypedDict(
    "IPSetForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
        "Position": ForwardedIPPositionType,
    },
)
JsonMatchPatternOutputTypeDef = TypedDict(
    "JsonMatchPatternOutputTypeDef",
    {
        "All": NotRequired[Dict[str, Any]],
        "IncludedPaths": NotRequired[List[str]],
    },
)
JsonMatchPatternTypeDef = TypedDict(
    "JsonMatchPatternTypeDef",
    {
        "All": NotRequired[Mapping[str, Any]],
        "IncludedPaths": NotRequired[Sequence[str]],
    },
)
LabelMatchStatementTypeDef = TypedDict(
    "LabelMatchStatementTypeDef",
    {
        "Scope": LabelMatchScopeType,
        "Key": str,
    },
)
LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": str,
    },
)
ListAPIKeysRequestRequestTypeDef = TypedDict(
    "ListAPIKeysRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ManagedRuleGroupVersionTypeDef = TypedDict(
    "ManagedRuleGroupVersionTypeDef",
    {
        "Name": NotRequired[str],
        "LastUpdateTimestamp": NotRequired[datetime],
    },
)
ListAvailableManagedRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ManagedRuleGroupSummaryTypeDef = TypedDict(
    "ManagedRuleGroupSummaryTypeDef",
    {
        "VendorName": NotRequired[str],
        "Name": NotRequired[str],
        "VersioningSupported": NotRequired[bool],
        "Description": NotRequired[str],
    },
)
ListIPSetsRequestRequestTypeDef = TypedDict(
    "ListIPSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
        "LogScope": NotRequired[LogScopeType],
    },
)
ListManagedRuleSetsRequestRequestTypeDef = TypedDict(
    "ListManagedRuleSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ManagedRuleSetSummaryTypeDef = TypedDict(
    "ManagedRuleSetSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
        "LabelNamespace": NotRequired[str],
    },
)
ListMobileSdkReleasesRequestRequestTypeDef = TypedDict(
    "ListMobileSdkReleasesRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ReleaseSummaryTypeDef = TypedDict(
    "ReleaseSummaryTypeDef",
    {
        "ReleaseVersion": NotRequired[str],
        "Timestamp": NotRequired[datetime],
    },
)
ListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "ListRegexPatternSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListResourcesForWebACLRequestRequestTypeDef = TypedDict(
    "ListResourcesForWebACLRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "ResourceType": NotRequired[ResourceTypeType],
    },
)
ListRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListWebACLsRequestRequestTypeDef = TypedDict(
    "ListWebACLsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
PasswordFieldTypeDef = TypedDict(
    "PasswordFieldTypeDef",
    {
        "Identifier": str,
    },
)
UsernameFieldTypeDef = TypedDict(
    "UsernameFieldTypeDef",
    {
        "Identifier": str,
    },
)
ManagedRuleSetVersionTypeDef = TypedDict(
    "ManagedRuleSetVersionTypeDef",
    {
        "AssociatedRuleGroupArn": NotRequired[str],
        "Capacity": NotRequired[int],
        "ForecastedLifetime": NotRequired[int],
        "PublishTimestamp": NotRequired[datetime],
        "LastUpdateTimestamp": NotRequired[datetime],
        "ExpiryTimestamp": NotRequired[datetime],
    },
)
NotStatementOutputTypeDef = TypedDict(
    "NotStatementOutputTypeDef",
    {
        "Statement": Dict[str, Any],
    },
)
NotStatementTypeDef = TypedDict(
    "NotStatementTypeDef",
    {
        "Statement": Mapping[str, Any],
    },
)
OrStatementOutputTypeDef = TypedDict(
    "OrStatementOutputTypeDef",
    {
        "Statements": List[Dict[str, Any]],
    },
)
OrStatementTypeDef = TypedDict(
    "OrStatementTypeDef",
    {
        "Statements": Sequence[Mapping[str, Any]],
    },
)
PhoneNumberFieldTypeDef = TypedDict(
    "PhoneNumberFieldTypeDef",
    {
        "Identifier": str,
    },
)
VersionToPublishTypeDef = TypedDict(
    "VersionToPublishTypeDef",
    {
        "AssociatedRuleGroupArn": NotRequired[str],
        "ForecastedLifetime": NotRequired[int],
    },
)
PutPermissionPolicyRequestRequestTypeDef = TypedDict(
    "PutPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)
RateLimitLabelNamespaceTypeDef = TypedDict(
    "RateLimitLabelNamespaceTypeDef",
    {
        "Namespace": str,
    },
)
ResponseInspectionBodyContainsOutputTypeDef = TypedDict(
    "ResponseInspectionBodyContainsOutputTypeDef",
    {
        "SuccessStrings": List[str],
        "FailureStrings": List[str],
    },
)
ResponseInspectionBodyContainsTypeDef = TypedDict(
    "ResponseInspectionBodyContainsTypeDef",
    {
        "SuccessStrings": Sequence[str],
        "FailureStrings": Sequence[str],
    },
)
ResponseInspectionHeaderOutputTypeDef = TypedDict(
    "ResponseInspectionHeaderOutputTypeDef",
    {
        "Name": str,
        "SuccessValues": List[str],
        "FailureValues": List[str],
    },
)
ResponseInspectionHeaderTypeDef = TypedDict(
    "ResponseInspectionHeaderTypeDef",
    {
        "Name": str,
        "SuccessValues": Sequence[str],
        "FailureValues": Sequence[str],
    },
)
ResponseInspectionJsonOutputTypeDef = TypedDict(
    "ResponseInspectionJsonOutputTypeDef",
    {
        "Identifier": str,
        "SuccessValues": List[str],
        "FailureValues": List[str],
    },
)
ResponseInspectionJsonTypeDef = TypedDict(
    "ResponseInspectionJsonTypeDef",
    {
        "Identifier": str,
        "SuccessValues": Sequence[str],
        "FailureValues": Sequence[str],
    },
)
ResponseInspectionStatusCodeOutputTypeDef = TypedDict(
    "ResponseInspectionStatusCodeOutputTypeDef",
    {
        "SuccessCodes": List[int],
        "FailureCodes": List[int],
    },
)
ResponseInspectionStatusCodeTypeDef = TypedDict(
    "ResponseInspectionStatusCodeTypeDef",
    {
        "SuccessCodes": Sequence[int],
        "FailureCodes": Sequence[int],
    },
)
TimestampTypeDef = Union[datetime, str]
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateIPSetRequestRequestTypeDef = TypedDict(
    "UpdateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "Addresses": Sequence[str],
        "LockToken": str,
        "Description": NotRequired[str],
    },
)
AndStatementUnionTypeDef = Union[AndStatementTypeDef, AndStatementOutputTypeDef]
AssociationConfigOutputTypeDef = TypedDict(
    "AssociationConfigOutputTypeDef",
    {
        "RequestBody": NotRequired[
            Dict[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfigTypeDef]
        ],
    },
)
AssociationConfigTypeDef = TypedDict(
    "AssociationConfigTypeDef",
    {
        "RequestBody": NotRequired[
            Mapping[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfigTypeDef]
        ],
    },
)
RateLimitCookieOutputTypeDef = TypedDict(
    "RateLimitCookieOutputTypeDef",
    {
        "Name": str,
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
RateLimitCookieTypeDef = TypedDict(
    "RateLimitCookieTypeDef",
    {
        "Name": str,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
RateLimitHeaderOutputTypeDef = TypedDict(
    "RateLimitHeaderOutputTypeDef",
    {
        "Name": str,
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
RateLimitHeaderTypeDef = TypedDict(
    "RateLimitHeaderTypeDef",
    {
        "Name": str,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
RateLimitQueryArgumentOutputTypeDef = TypedDict(
    "RateLimitQueryArgumentOutputTypeDef",
    {
        "Name": str,
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
RateLimitQueryArgumentTypeDef = TypedDict(
    "RateLimitQueryArgumentTypeDef",
    {
        "Name": str,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
RateLimitQueryStringOutputTypeDef = TypedDict(
    "RateLimitQueryStringOutputTypeDef",
    {
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
RateLimitQueryStringTypeDef = TypedDict(
    "RateLimitQueryStringTypeDef",
    {
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
RateLimitUriPathOutputTypeDef = TypedDict(
    "RateLimitUriPathOutputTypeDef",
    {
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
RateLimitUriPathTypeDef = TypedDict(
    "RateLimitUriPathTypeDef",
    {
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
CaptchaConfigTypeDef = TypedDict(
    "CaptchaConfigTypeDef",
    {
        "ImmunityTimeProperty": NotRequired[ImmunityTimePropertyTypeDef],
    },
)
ChallengeConfigTypeDef = TypedDict(
    "ChallengeConfigTypeDef",
    {
        "ImmunityTimeProperty": NotRequired[ImmunityTimePropertyTypeDef],
    },
)
CheckCapacityResponseTypeDef = TypedDict(
    "CheckCapacityResponseTypeDef",
    {
        "Capacity": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAPIKeyResponseTypeDef = TypedDict(
    "CreateAPIKeyResponseTypeDef",
    {
        "APIKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFirewallManagerRuleGroupsResponseTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    {
        "NextWebACLLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateMobileSdkReleaseUrlResponseTypeDef = TypedDict(
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    {
        "Url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDecryptedAPIKeyResponseTypeDef = TypedDict(
    "GetDecryptedAPIKeyResponseTypeDef",
    {
        "TokenDomains": List[str],
        "CreationTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPermissionPolicyResponseTypeDef = TypedDict(
    "GetPermissionPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAPIKeysResponseTypeDef = TypedDict(
    "ListAPIKeysResponseTypeDef",
    {
        "NextMarker": str,
        "APIKeySummaries": List[APIKeySummaryTypeDef],
        "ApplicationIntegrationURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesForWebACLResponseTypeDef = TypedDict(
    "ListResourcesForWebACLResponseTypeDef",
    {
        "ResourceArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutManagedRuleSetVersionsResponseTypeDef = TypedDict(
    "PutManagedRuleSetVersionsResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateManagedRuleSetVersionExpiryDateResponseTypeDef = TypedDict(
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    {
        "ExpiringVersion": str,
        "ExpiryTimestamp": datetime,
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ActionCondition": NotRequired[ActionConditionTypeDef],
        "LabelNameCondition": NotRequired[LabelNameConditionTypeDef],
    },
)
CookiesOutputTypeDef = TypedDict(
    "CookiesOutputTypeDef",
    {
        "MatchPattern": CookieMatchPatternOutputTypeDef,
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)
CookieMatchPatternUnionTypeDef = Union[CookieMatchPatternTypeDef, CookieMatchPatternOutputTypeDef]
CreateIPSetRequestRequestTypeDef = TypedDict(
    "CreateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": Sequence[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
MobileSdkReleaseTypeDef = TypedDict(
    "MobileSdkReleaseTypeDef",
    {
        "ReleaseVersion": NotRequired[str],
        "Timestamp": NotRequired[datetime],
        "ReleaseNotes": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TagInfoForResourceTypeDef = TypedDict(
    "TagInfoForResourceTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "TagList": NotRequired[List[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "Summary": IPSetSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "NextMarker": str,
        "IPSets": List[IPSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "CreateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "RegularExpressionList": Sequence[RegexTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
RegexPatternSetTypeDef = TypedDict(
    "RegexPatternSetTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "ARN": NotRequired[str],
        "Description": NotRequired[str],
        "RegularExpressionList": NotRequired[List[RegexTypeDef]],
    },
)
UpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "UpdateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "RegularExpressionList": Sequence[RegexTypeDef],
        "LockToken": str,
        "Description": NotRequired[str],
    },
)
CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "Summary": RegexPatternSetSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRegexPatternSetsResponseTypeDef = TypedDict(
    "ListRegexPatternSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List[RegexPatternSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "Summary": RuleGroupSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List[RuleGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef",
    {
        "Summary": WebACLSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWebACLsResponseTypeDef = TypedDict(
    "ListWebACLsResponseTypeDef",
    {
        "NextMarker": str,
        "WebACLs": List[WebACLSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomRequestHandlingOutputTypeDef = TypedDict(
    "CustomRequestHandlingOutputTypeDef",
    {
        "InsertHeaders": List[CustomHTTPHeaderTypeDef],
    },
)
CustomRequestHandlingTypeDef = TypedDict(
    "CustomRequestHandlingTypeDef",
    {
        "InsertHeaders": Sequence[CustomHTTPHeaderTypeDef],
    },
)
CustomResponseOutputTypeDef = TypedDict(
    "CustomResponseOutputTypeDef",
    {
        "ResponseCode": int,
        "CustomResponseBodyKey": NotRequired[str],
        "ResponseHeaders": NotRequired[List[CustomHTTPHeaderTypeDef]],
    },
)
CustomResponseTypeDef = TypedDict(
    "CustomResponseTypeDef",
    {
        "ResponseCode": int,
        "CustomResponseBodyKey": NotRequired[str],
        "ResponseHeaders": NotRequired[Sequence[CustomHTTPHeaderTypeDef]],
    },
)
DescribeAllManagedProductsResponseTypeDef = TypedDict(
    "DescribeAllManagedProductsResponseTypeDef",
    {
        "ManagedProducts": List[ManagedProductDescriptorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeManagedProductsByVendorResponseTypeDef = TypedDict(
    "DescribeManagedProductsByVendorResponseTypeDef",
    {
        "ManagedProducts": List[ManagedProductDescriptorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GeoMatchStatementOutputTypeDef = TypedDict(
    "GeoMatchStatementOutputTypeDef",
    {
        "CountryCodes": NotRequired[List[CountryCodeType]],
        "ForwardedIPConfig": NotRequired[ForwardedIPConfigTypeDef],
    },
)
GeoMatchStatementTypeDef = TypedDict(
    "GeoMatchStatementTypeDef",
    {
        "CountryCodes": NotRequired[Sequence[CountryCodeType]],
        "ForwardedIPConfig": NotRequired[ForwardedIPConfigTypeDef],
    },
)
GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": IPSetTypeDef,
        "LockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRateBasedStatementManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    {
        "ManagedKeysIPV4": RateBasedStatementManagedKeysIPSetTypeDef,
        "ManagedKeysIPV6": RateBasedStatementManagedKeysIPSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HTTPRequestTypeDef = TypedDict(
    "HTTPRequestTypeDef",
    {
        "ClientIP": NotRequired[str],
        "Country": NotRequired[str],
        "URI": NotRequired[str],
        "Method": NotRequired[str],
        "HTTPVersion": NotRequired[str],
        "Headers": NotRequired[List[HTTPHeaderTypeDef]],
    },
)
HeadersOutputTypeDef = TypedDict(
    "HeadersOutputTypeDef",
    {
        "MatchPattern": HeaderMatchPatternOutputTypeDef,
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)
HeaderMatchPatternUnionTypeDef = Union[HeaderMatchPatternTypeDef, HeaderMatchPatternOutputTypeDef]
IPSetReferenceStatementTypeDef = TypedDict(
    "IPSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "IPSetForwardedIPConfig": NotRequired[IPSetForwardedIPConfigTypeDef],
    },
)
JsonBodyOutputTypeDef = TypedDict(
    "JsonBodyOutputTypeDef",
    {
        "MatchPattern": JsonMatchPatternOutputTypeDef,
        "MatchScope": JsonMatchScopeType,
        "InvalidFallbackBehavior": NotRequired[BodyParsingFallbackBehaviorType],
        "OversizeHandling": NotRequired[OversizeHandlingType],
    },
)
JsonMatchPatternUnionTypeDef = Union[JsonMatchPatternTypeDef, JsonMatchPatternOutputTypeDef]
ListAvailableManagedRuleGroupVersionsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    {
        "NextMarker": str,
        "Versions": List[ManagedRuleGroupVersionTypeDef],
        "CurrentDefaultVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAvailableManagedRuleGroupsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleGroups": List[ManagedRuleGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListManagedRuleSetsResponseTypeDef = TypedDict(
    "ListManagedRuleSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleSets": List[ManagedRuleSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMobileSdkReleasesResponseTypeDef = TypedDict(
    "ListMobileSdkReleasesResponseTypeDef",
    {
        "ReleaseSummaries": List[ReleaseSummaryTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestInspectionTypeDef = TypedDict(
    "RequestInspectionTypeDef",
    {
        "PayloadType": PayloadTypeType,
        "UsernameField": UsernameFieldTypeDef,
        "PasswordField": PasswordFieldTypeDef,
    },
)
ManagedRuleSetTypeDef = TypedDict(
    "ManagedRuleSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "Description": NotRequired[str],
        "PublishedVersions": NotRequired[Dict[str, ManagedRuleSetVersionTypeDef]],
        "RecommendedVersion": NotRequired[str],
        "LabelNamespace": NotRequired[str],
    },
)
NotStatementUnionTypeDef = Union[NotStatementTypeDef, NotStatementOutputTypeDef]
OrStatementUnionTypeDef = Union[OrStatementTypeDef, OrStatementOutputTypeDef]
RequestInspectionACFPOutputTypeDef = TypedDict(
    "RequestInspectionACFPOutputTypeDef",
    {
        "PayloadType": PayloadTypeType,
        "UsernameField": NotRequired[UsernameFieldTypeDef],
        "PasswordField": NotRequired[PasswordFieldTypeDef],
        "EmailField": NotRequired[EmailFieldTypeDef],
        "PhoneNumberFields": NotRequired[List[PhoneNumberFieldTypeDef]],
        "AddressFields": NotRequired[List[AddressFieldTypeDef]],
    },
)
RequestInspectionACFPTypeDef = TypedDict(
    "RequestInspectionACFPTypeDef",
    {
        "PayloadType": PayloadTypeType,
        "UsernameField": NotRequired[UsernameFieldTypeDef],
        "PasswordField": NotRequired[PasswordFieldTypeDef],
        "EmailField": NotRequired[EmailFieldTypeDef],
        "PhoneNumberFields": NotRequired[Sequence[PhoneNumberFieldTypeDef]],
        "AddressFields": NotRequired[Sequence[AddressFieldTypeDef]],
    },
)
PutManagedRuleSetVersionsRequestRequestTypeDef = TypedDict(
    "PutManagedRuleSetVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
        "RecommendedVersion": NotRequired[str],
        "VersionsToPublish": NotRequired[Mapping[str, VersionToPublishTypeDef]],
    },
)
ResponseInspectionBodyContainsUnionTypeDef = Union[
    ResponseInspectionBodyContainsTypeDef, ResponseInspectionBodyContainsOutputTypeDef
]
ResponseInspectionHeaderUnionTypeDef = Union[
    ResponseInspectionHeaderTypeDef, ResponseInspectionHeaderOutputTypeDef
]
ResponseInspectionJsonUnionTypeDef = Union[
    ResponseInspectionJsonTypeDef, ResponseInspectionJsonOutputTypeDef
]
ResponseInspectionOutputTypeDef = TypedDict(
    "ResponseInspectionOutputTypeDef",
    {
        "StatusCode": NotRequired[ResponseInspectionStatusCodeOutputTypeDef],
        "Header": NotRequired[ResponseInspectionHeaderOutputTypeDef],
        "BodyContains": NotRequired[ResponseInspectionBodyContainsOutputTypeDef],
        "Json": NotRequired[ResponseInspectionJsonOutputTypeDef],
    },
)
ResponseInspectionStatusCodeUnionTypeDef = Union[
    ResponseInspectionStatusCodeTypeDef, ResponseInspectionStatusCodeOutputTypeDef
]
TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
    },
)
UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef = TypedDict(
    "UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
        "VersionToExpire": str,
        "ExpiryTimestamp": TimestampTypeDef,
    },
)
RateLimitCookieUnionTypeDef = Union[RateLimitCookieTypeDef, RateLimitCookieOutputTypeDef]
RateLimitHeaderUnionTypeDef = Union[RateLimitHeaderTypeDef, RateLimitHeaderOutputTypeDef]
RateLimitQueryArgumentUnionTypeDef = Union[
    RateLimitQueryArgumentTypeDef, RateLimitQueryArgumentOutputTypeDef
]
RateLimitQueryStringUnionTypeDef = Union[
    RateLimitQueryStringTypeDef, RateLimitQueryStringOutputTypeDef
]
RateBasedStatementCustomKeyOutputTypeDef = TypedDict(
    "RateBasedStatementCustomKeyOutputTypeDef",
    {
        "Header": NotRequired[RateLimitHeaderOutputTypeDef],
        "Cookie": NotRequired[RateLimitCookieOutputTypeDef],
        "QueryArgument": NotRequired[RateLimitQueryArgumentOutputTypeDef],
        "QueryString": NotRequired[RateLimitQueryStringOutputTypeDef],
        "HTTPMethod": NotRequired[Dict[str, Any]],
        "ForwardedIP": NotRequired[Dict[str, Any]],
        "IP": NotRequired[Dict[str, Any]],
        "LabelNamespace": NotRequired[RateLimitLabelNamespaceTypeDef],
        "UriPath": NotRequired[RateLimitUriPathOutputTypeDef],
    },
)
RateLimitUriPathUnionTypeDef = Union[RateLimitUriPathTypeDef, RateLimitUriPathOutputTypeDef]
FilterOutputTypeDef = TypedDict(
    "FilterOutputTypeDef",
    {
        "Behavior": FilterBehaviorType,
        "Requirement": FilterRequirementType,
        "Conditions": List[ConditionTypeDef],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Behavior": FilterBehaviorType,
        "Requirement": FilterRequirementType,
        "Conditions": Sequence[ConditionTypeDef],
    },
)
CookiesTypeDef = TypedDict(
    "CookiesTypeDef",
    {
        "MatchPattern": CookieMatchPatternUnionTypeDef,
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)
GetMobileSdkReleaseResponseTypeDef = TypedDict(
    "GetMobileSdkReleaseResponseTypeDef",
    {
        "MobileSdkRelease": MobileSdkReleaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextMarker": str,
        "TagInfoForResource": TagInfoForResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": RegexPatternSetTypeDef,
        "LockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AllowActionOutputTypeDef = TypedDict(
    "AllowActionOutputTypeDef",
    {
        "CustomRequestHandling": NotRequired[CustomRequestHandlingOutputTypeDef],
    },
)
CaptchaActionOutputTypeDef = TypedDict(
    "CaptchaActionOutputTypeDef",
    {
        "CustomRequestHandling": NotRequired[CustomRequestHandlingOutputTypeDef],
    },
)
ChallengeActionOutputTypeDef = TypedDict(
    "ChallengeActionOutputTypeDef",
    {
        "CustomRequestHandling": NotRequired[CustomRequestHandlingOutputTypeDef],
    },
)
CountActionOutputTypeDef = TypedDict(
    "CountActionOutputTypeDef",
    {
        "CustomRequestHandling": NotRequired[CustomRequestHandlingOutputTypeDef],
    },
)
CustomRequestHandlingUnionTypeDef = Union[
    CustomRequestHandlingTypeDef, CustomRequestHandlingOutputTypeDef
]
BlockActionOutputTypeDef = TypedDict(
    "BlockActionOutputTypeDef",
    {
        "CustomResponse": NotRequired[CustomResponseOutputTypeDef],
    },
)
CustomResponseUnionTypeDef = Union[CustomResponseTypeDef, CustomResponseOutputTypeDef]
GeoMatchStatementUnionTypeDef = Union[GeoMatchStatementTypeDef, GeoMatchStatementOutputTypeDef]
SampledHTTPRequestTypeDef = TypedDict(
    "SampledHTTPRequestTypeDef",
    {
        "Request": HTTPRequestTypeDef,
        "Weight": int,
        "Timestamp": NotRequired[datetime],
        "Action": NotRequired[str],
        "RuleNameWithinRuleGroup": NotRequired[str],
        "RequestHeadersInserted": NotRequired[List[HTTPHeaderTypeDef]],
        "ResponseCodeSent": NotRequired[int],
        "Labels": NotRequired[List[LabelTypeDef]],
        "CaptchaResponse": NotRequired[CaptchaResponseTypeDef],
        "ChallengeResponse": NotRequired[ChallengeResponseTypeDef],
        "OverriddenAction": NotRequired[str],
    },
)
HeadersTypeDef = TypedDict(
    "HeadersTypeDef",
    {
        "MatchPattern": HeaderMatchPatternUnionTypeDef,
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)
FieldToMatchOutputTypeDef = TypedDict(
    "FieldToMatchOutputTypeDef",
    {
        "SingleHeader": NotRequired[SingleHeaderTypeDef],
        "SingleQueryArgument": NotRequired[SingleQueryArgumentTypeDef],
        "AllQueryArguments": NotRequired[Dict[str, Any]],
        "UriPath": NotRequired[Dict[str, Any]],
        "QueryString": NotRequired[Dict[str, Any]],
        "Body": NotRequired[BodyTypeDef],
        "Method": NotRequired[Dict[str, Any]],
        "JsonBody": NotRequired[JsonBodyOutputTypeDef],
        "Headers": NotRequired[HeadersOutputTypeDef],
        "Cookies": NotRequired[CookiesOutputTypeDef],
        "HeaderOrder": NotRequired[HeaderOrderTypeDef],
        "JA3Fingerprint": NotRequired[JA3FingerprintTypeDef],
    },
)
JsonBodyTypeDef = TypedDict(
    "JsonBodyTypeDef",
    {
        "MatchPattern": JsonMatchPatternUnionTypeDef,
        "MatchScope": JsonMatchScopeType,
        "InvalidFallbackBehavior": NotRequired[BodyParsingFallbackBehaviorType],
        "OversizeHandling": NotRequired[OversizeHandlingType],
    },
)
GetManagedRuleSetResponseTypeDef = TypedDict(
    "GetManagedRuleSetResponseTypeDef",
    {
        "ManagedRuleSet": ManagedRuleSetTypeDef,
        "LockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestInspectionACFPUnionTypeDef = Union[
    RequestInspectionACFPTypeDef, RequestInspectionACFPOutputTypeDef
]
AWSManagedRulesACFPRuleSetOutputTypeDef = TypedDict(
    "AWSManagedRulesACFPRuleSetOutputTypeDef",
    {
        "CreationPath": str,
        "RegistrationPagePath": str,
        "RequestInspection": RequestInspectionACFPOutputTypeDef,
        "ResponseInspection": NotRequired[ResponseInspectionOutputTypeDef],
        "EnableRegexInPath": NotRequired[bool],
    },
)
AWSManagedRulesATPRuleSetOutputTypeDef = TypedDict(
    "AWSManagedRulesATPRuleSetOutputTypeDef",
    {
        "LoginPath": str,
        "RequestInspection": NotRequired[RequestInspectionTypeDef],
        "ResponseInspection": NotRequired[ResponseInspectionOutputTypeDef],
        "EnableRegexInPath": NotRequired[bool],
    },
)
ResponseInspectionTypeDef = TypedDict(
    "ResponseInspectionTypeDef",
    {
        "StatusCode": NotRequired[ResponseInspectionStatusCodeUnionTypeDef],
        "Header": NotRequired[ResponseInspectionHeaderUnionTypeDef],
        "BodyContains": NotRequired[ResponseInspectionBodyContainsUnionTypeDef],
        "Json": NotRequired[ResponseInspectionJsonUnionTypeDef],
    },
)
GetSampledRequestsRequestRequestTypeDef = TypedDict(
    "GetSampledRequestsRequestRequestTypeDef",
    {
        "WebAclArn": str,
        "RuleMetricName": str,
        "Scope": ScopeType,
        "TimeWindow": TimeWindowTypeDef,
        "MaxItems": int,
    },
)
RateBasedStatementOutputTypeDef = TypedDict(
    "RateBasedStatementOutputTypeDef",
    {
        "Limit": int,
        "AggregateKeyType": RateBasedStatementAggregateKeyTypeType,
        "EvaluationWindowSec": NotRequired[int],
        "ScopeDownStatement": NotRequired[Dict[str, Any]],
        "ForwardedIPConfig": NotRequired[ForwardedIPConfigTypeDef],
        "CustomKeys": NotRequired[List[RateBasedStatementCustomKeyOutputTypeDef]],
    },
)
RateBasedStatementCustomKeyTypeDef = TypedDict(
    "RateBasedStatementCustomKeyTypeDef",
    {
        "Header": NotRequired[RateLimitHeaderUnionTypeDef],
        "Cookie": NotRequired[RateLimitCookieUnionTypeDef],
        "QueryArgument": NotRequired[RateLimitQueryArgumentUnionTypeDef],
        "QueryString": NotRequired[RateLimitQueryStringUnionTypeDef],
        "HTTPMethod": NotRequired[Mapping[str, Any]],
        "ForwardedIP": NotRequired[Mapping[str, Any]],
        "IP": NotRequired[Mapping[str, Any]],
        "LabelNamespace": NotRequired[RateLimitLabelNamespaceTypeDef],
        "UriPath": NotRequired[RateLimitUriPathUnionTypeDef],
    },
)
LoggingFilterOutputTypeDef = TypedDict(
    "LoggingFilterOutputTypeDef",
    {
        "Filters": List[FilterOutputTypeDef],
        "DefaultBehavior": FilterBehaviorType,
    },
)
FilterUnionTypeDef = Union[FilterTypeDef, FilterOutputTypeDef]
CookiesUnionTypeDef = Union[CookiesTypeDef, CookiesOutputTypeDef]
OverrideActionOutputTypeDef = TypedDict(
    "OverrideActionOutputTypeDef",
    {
        "Count": NotRequired[CountActionOutputTypeDef],
        "None": NotRequired[Dict[str, Any]],
    },
)
AllowActionTypeDef = TypedDict(
    "AllowActionTypeDef",
    {
        "CustomRequestHandling": NotRequired[CustomRequestHandlingUnionTypeDef],
    },
)
CaptchaActionTypeDef = TypedDict(
    "CaptchaActionTypeDef",
    {
        "CustomRequestHandling": NotRequired[CustomRequestHandlingUnionTypeDef],
    },
)
ChallengeActionTypeDef = TypedDict(
    "ChallengeActionTypeDef",
    {
        "CustomRequestHandling": NotRequired[CustomRequestHandlingUnionTypeDef],
    },
)
CountActionTypeDef = TypedDict(
    "CountActionTypeDef",
    {
        "CustomRequestHandling": NotRequired[CustomRequestHandlingUnionTypeDef],
    },
)
DefaultActionOutputTypeDef = TypedDict(
    "DefaultActionOutputTypeDef",
    {
        "Block": NotRequired[BlockActionOutputTypeDef],
        "Allow": NotRequired[AllowActionOutputTypeDef],
    },
)
RuleActionOutputTypeDef = TypedDict(
    "RuleActionOutputTypeDef",
    {
        "Block": NotRequired[BlockActionOutputTypeDef],
        "Allow": NotRequired[AllowActionOutputTypeDef],
        "Count": NotRequired[CountActionOutputTypeDef],
        "Captcha": NotRequired[CaptchaActionOutputTypeDef],
        "Challenge": NotRequired[ChallengeActionOutputTypeDef],
    },
)
BlockActionTypeDef = TypedDict(
    "BlockActionTypeDef",
    {
        "CustomResponse": NotRequired[CustomResponseUnionTypeDef],
    },
)
GetSampledRequestsResponseTypeDef = TypedDict(
    "GetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List[SampledHTTPRequestTypeDef],
        "PopulationSize": int,
        "TimeWindow": TimeWindowOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HeadersUnionTypeDef = Union[HeadersTypeDef, HeadersOutputTypeDef]
ByteMatchStatementOutputTypeDef = TypedDict(
    "ByteMatchStatementOutputTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationTypeDef],
        "PositionalConstraint": PositionalConstraintType,
    },
)
RegexMatchStatementOutputTypeDef = TypedDict(
    "RegexMatchStatementOutputTypeDef",
    {
        "RegexString": str,
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
RegexPatternSetReferenceStatementOutputTypeDef = TypedDict(
    "RegexPatternSetReferenceStatementOutputTypeDef",
    {
        "ARN": str,
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
SizeConstraintStatementOutputTypeDef = TypedDict(
    "SizeConstraintStatementOutputTypeDef",
    {
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
SqliMatchStatementOutputTypeDef = TypedDict(
    "SqliMatchStatementOutputTypeDef",
    {
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationTypeDef],
        "SensitivityLevel": NotRequired[SensitivityLevelType],
    },
)
XssMatchStatementOutputTypeDef = TypedDict(
    "XssMatchStatementOutputTypeDef",
    {
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationTypeDef],
    },
)
JsonBodyUnionTypeDef = Union[JsonBodyTypeDef, JsonBodyOutputTypeDef]
ManagedRuleGroupConfigOutputTypeDef = TypedDict(
    "ManagedRuleGroupConfigOutputTypeDef",
    {
        "LoginPath": NotRequired[str],
        "PayloadType": NotRequired[PayloadTypeType],
        "UsernameField": NotRequired[UsernameFieldTypeDef],
        "PasswordField": NotRequired[PasswordFieldTypeDef],
        "AWSManagedRulesBotControlRuleSet": NotRequired[AWSManagedRulesBotControlRuleSetTypeDef],
        "AWSManagedRulesATPRuleSet": NotRequired[AWSManagedRulesATPRuleSetOutputTypeDef],
        "AWSManagedRulesACFPRuleSet": NotRequired[AWSManagedRulesACFPRuleSetOutputTypeDef],
    },
)
ResponseInspectionUnionTypeDef = Union[ResponseInspectionTypeDef, ResponseInspectionOutputTypeDef]
RateBasedStatementCustomKeyUnionTypeDef = Union[
    RateBasedStatementCustomKeyTypeDef, RateBasedStatementCustomKeyOutputTypeDef
]
LoggingConfigurationOutputTypeDef = TypedDict(
    "LoggingConfigurationOutputTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": NotRequired[List[FieldToMatchOutputTypeDef]],
        "ManagedByFirewallManager": NotRequired[bool],
        "LoggingFilter": NotRequired[LoggingFilterOutputTypeDef],
        "LogType": NotRequired[Literal["WAF_LOGS"]],
        "LogScope": NotRequired[LogScopeType],
    },
)
LoggingFilterTypeDef = TypedDict(
    "LoggingFilterTypeDef",
    {
        "Filters": Sequence[FilterUnionTypeDef],
        "DefaultBehavior": FilterBehaviorType,
    },
)
AllowActionUnionTypeDef = Union[AllowActionTypeDef, AllowActionOutputTypeDef]
CaptchaActionUnionTypeDef = Union[CaptchaActionTypeDef, CaptchaActionOutputTypeDef]
ChallengeActionUnionTypeDef = Union[ChallengeActionTypeDef, ChallengeActionOutputTypeDef]
CountActionUnionTypeDef = Union[CountActionTypeDef, CountActionOutputTypeDef]
RuleActionOverrideOutputTypeDef = TypedDict(
    "RuleActionOverrideOutputTypeDef",
    {
        "Name": str,
        "ActionToUse": RuleActionOutputTypeDef,
    },
)
RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Action": NotRequired[RuleActionOutputTypeDef],
    },
)
BlockActionUnionTypeDef = Union[BlockActionTypeDef, BlockActionOutputTypeDef]
FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "SingleHeader": NotRequired[SingleHeaderTypeDef],
        "SingleQueryArgument": NotRequired[SingleQueryArgumentTypeDef],
        "AllQueryArguments": NotRequired[Mapping[str, Any]],
        "UriPath": NotRequired[Mapping[str, Any]],
        "QueryString": NotRequired[Mapping[str, Any]],
        "Body": NotRequired[BodyTypeDef],
        "Method": NotRequired[Mapping[str, Any]],
        "JsonBody": NotRequired[JsonBodyUnionTypeDef],
        "Headers": NotRequired[HeadersUnionTypeDef],
        "Cookies": NotRequired[CookiesUnionTypeDef],
        "HeaderOrder": NotRequired[HeaderOrderTypeDef],
        "JA3Fingerprint": NotRequired[JA3FingerprintTypeDef],
    },
)
AWSManagedRulesACFPRuleSetTypeDef = TypedDict(
    "AWSManagedRulesACFPRuleSetTypeDef",
    {
        "CreationPath": str,
        "RegistrationPagePath": str,
        "RequestInspection": RequestInspectionACFPUnionTypeDef,
        "ResponseInspection": NotRequired[ResponseInspectionUnionTypeDef],
        "EnableRegexInPath": NotRequired[bool],
    },
)
AWSManagedRulesATPRuleSetTypeDef = TypedDict(
    "AWSManagedRulesATPRuleSetTypeDef",
    {
        "LoginPath": str,
        "RequestInspection": NotRequired[RequestInspectionTypeDef],
        "ResponseInspection": NotRequired[ResponseInspectionUnionTypeDef],
        "EnableRegexInPath": NotRequired[bool],
    },
)
RateBasedStatementTypeDef = TypedDict(
    "RateBasedStatementTypeDef",
    {
        "Limit": int,
        "AggregateKeyType": RateBasedStatementAggregateKeyTypeType,
        "EvaluationWindowSec": NotRequired[int],
        "ScopeDownStatement": NotRequired[Mapping[str, Any]],
        "ForwardedIPConfig": NotRequired[ForwardedIPConfigTypeDef],
        "CustomKeys": NotRequired[Sequence[RateBasedStatementCustomKeyUnionTypeDef]],
    },
)
GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List[LoggingConfigurationOutputTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutLoggingConfigurationResponseTypeDef = TypedDict(
    "PutLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingFilterUnionTypeDef = Union[LoggingFilterTypeDef, LoggingFilterOutputTypeDef]
OverrideActionTypeDef = TypedDict(
    "OverrideActionTypeDef",
    {
        "Count": NotRequired[CountActionUnionTypeDef],
        "None": NotRequired[Mapping[str, Any]],
    },
)
ManagedRuleGroupStatementOutputTypeDef = TypedDict(
    "ManagedRuleGroupStatementOutputTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Version": NotRequired[str],
        "ExcludedRules": NotRequired[List[ExcludedRuleTypeDef]],
        "ScopeDownStatement": NotRequired[Dict[str, Any]],
        "ManagedRuleGroupConfigs": NotRequired[List[ManagedRuleGroupConfigOutputTypeDef]],
        "RuleActionOverrides": NotRequired[List[RuleActionOverrideOutputTypeDef]],
    },
)
RuleGroupReferenceStatementOutputTypeDef = TypedDict(
    "RuleGroupReferenceStatementOutputTypeDef",
    {
        "ARN": str,
        "ExcludedRules": NotRequired[List[ExcludedRuleTypeDef]],
        "RuleActionOverrides": NotRequired[List[RuleActionOverrideOutputTypeDef]],
    },
)
DescribeManagedRuleGroupResponseTypeDef = TypedDict(
    "DescribeManagedRuleGroupResponseTypeDef",
    {
        "VersionName": str,
        "SnsTopicArn": str,
        "Capacity": int,
        "Rules": List[RuleSummaryTypeDef],
        "LabelNamespace": str,
        "AvailableLabels": List[LabelSummaryTypeDef],
        "ConsumedLabels": List[LabelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefaultActionTypeDef = TypedDict(
    "DefaultActionTypeDef",
    {
        "Block": NotRequired[BlockActionUnionTypeDef],
        "Allow": NotRequired[AllowActionUnionTypeDef],
    },
)
RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "Block": NotRequired[BlockActionUnionTypeDef],
        "Allow": NotRequired[AllowActionUnionTypeDef],
        "Count": NotRequired[CountActionUnionTypeDef],
        "Captcha": NotRequired[CaptchaActionUnionTypeDef],
        "Challenge": NotRequired[ChallengeActionUnionTypeDef],
    },
)
FieldToMatchUnionTypeDef = Union[FieldToMatchTypeDef, FieldToMatchOutputTypeDef]
AWSManagedRulesACFPRuleSetUnionTypeDef = Union[
    AWSManagedRulesACFPRuleSetTypeDef, AWSManagedRulesACFPRuleSetOutputTypeDef
]
AWSManagedRulesATPRuleSetUnionTypeDef = Union[
    AWSManagedRulesATPRuleSetTypeDef, AWSManagedRulesATPRuleSetOutputTypeDef
]
RateBasedStatementUnionTypeDef = Union[RateBasedStatementTypeDef, RateBasedStatementOutputTypeDef]
OverrideActionUnionTypeDef = Union[OverrideActionTypeDef, OverrideActionOutputTypeDef]
FirewallManagerStatementTypeDef = TypedDict(
    "FirewallManagerStatementTypeDef",
    {
        "ManagedRuleGroupStatement": NotRequired[ManagedRuleGroupStatementOutputTypeDef],
        "RuleGroupReferenceStatement": NotRequired[RuleGroupReferenceStatementOutputTypeDef],
    },
)
StatementOutputTypeDef = TypedDict(
    "StatementOutputTypeDef",
    {
        "ByteMatchStatement": NotRequired[ByteMatchStatementOutputTypeDef],
        "SqliMatchStatement": NotRequired[SqliMatchStatementOutputTypeDef],
        "XssMatchStatement": NotRequired[XssMatchStatementOutputTypeDef],
        "SizeConstraintStatement": NotRequired[SizeConstraintStatementOutputTypeDef],
        "GeoMatchStatement": NotRequired[GeoMatchStatementOutputTypeDef],
        "RuleGroupReferenceStatement": NotRequired[RuleGroupReferenceStatementOutputTypeDef],
        "IPSetReferenceStatement": NotRequired[IPSetReferenceStatementTypeDef],
        "RegexPatternSetReferenceStatement": NotRequired[
            RegexPatternSetReferenceStatementOutputTypeDef
        ],
        "RateBasedStatement": NotRequired[RateBasedStatementOutputTypeDef],
        "AndStatement": NotRequired[AndStatementOutputTypeDef],
        "OrStatement": NotRequired[OrStatementOutputTypeDef],
        "NotStatement": NotRequired[NotStatementOutputTypeDef],
        "ManagedRuleGroupStatement": NotRequired[ManagedRuleGroupStatementOutputTypeDef],
        "LabelMatchStatement": NotRequired[LabelMatchStatementTypeDef],
        "RegexMatchStatement": NotRequired[RegexMatchStatementOutputTypeDef],
    },
)
RuleActionUnionTypeDef = Union[RuleActionTypeDef, RuleActionOutputTypeDef]
ByteMatchStatementTypeDef = TypedDict(
    "ByteMatchStatementTypeDef",
    {
        "SearchString": BlobTypeDef,
        "FieldToMatch": FieldToMatchUnionTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
        "PositionalConstraint": PositionalConstraintType,
    },
)
LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": Sequence[str],
        "RedactedFields": NotRequired[Sequence[FieldToMatchUnionTypeDef]],
        "ManagedByFirewallManager": NotRequired[bool],
        "LoggingFilter": NotRequired[LoggingFilterUnionTypeDef],
        "LogType": NotRequired[Literal["WAF_LOGS"]],
        "LogScope": NotRequired[LogScopeType],
    },
)
RegexMatchStatementTypeDef = TypedDict(
    "RegexMatchStatementTypeDef",
    {
        "RegexString": str,
        "FieldToMatch": FieldToMatchUnionTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
RegexPatternSetReferenceStatementTypeDef = TypedDict(
    "RegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": FieldToMatchUnionTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
SizeConstraintStatementTypeDef = TypedDict(
    "SizeConstraintStatementTypeDef",
    {
        "FieldToMatch": FieldToMatchUnionTypeDef,
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
SqliMatchStatementTypeDef = TypedDict(
    "SqliMatchStatementTypeDef",
    {
        "FieldToMatch": FieldToMatchUnionTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
        "SensitivityLevel": NotRequired[SensitivityLevelType],
    },
)
XssMatchStatementTypeDef = TypedDict(
    "XssMatchStatementTypeDef",
    {
        "FieldToMatch": FieldToMatchUnionTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
ManagedRuleGroupConfigTypeDef = TypedDict(
    "ManagedRuleGroupConfigTypeDef",
    {
        "LoginPath": NotRequired[str],
        "PayloadType": NotRequired[PayloadTypeType],
        "UsernameField": NotRequired[UsernameFieldTypeDef],
        "PasswordField": NotRequired[PasswordFieldTypeDef],
        "AWSManagedRulesBotControlRuleSet": NotRequired[AWSManagedRulesBotControlRuleSetTypeDef],
        "AWSManagedRulesATPRuleSet": NotRequired[AWSManagedRulesATPRuleSetUnionTypeDef],
        "AWSManagedRulesACFPRuleSet": NotRequired[AWSManagedRulesACFPRuleSetUnionTypeDef],
    },
)
FirewallManagerRuleGroupTypeDef = TypedDict(
    "FirewallManagerRuleGroupTypeDef",
    {
        "Name": str,
        "Priority": int,
        "FirewallManagerStatement": FirewallManagerStatementTypeDef,
        "OverrideAction": OverrideActionOutputTypeDef,
        "VisibilityConfig": VisibilityConfigTypeDef,
    },
)
RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": StatementOutputTypeDef,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "Action": NotRequired[RuleActionOutputTypeDef],
        "OverrideAction": NotRequired[OverrideActionOutputTypeDef],
        "RuleLabels": NotRequired[List[LabelTypeDef]],
        "CaptchaConfig": NotRequired[CaptchaConfigTypeDef],
        "ChallengeConfig": NotRequired[ChallengeConfigTypeDef],
    },
)
RuleActionOverrideTypeDef = TypedDict(
    "RuleActionOverrideTypeDef",
    {
        "Name": str,
        "ActionToUse": RuleActionUnionTypeDef,
    },
)
ByteMatchStatementUnionTypeDef = Union[ByteMatchStatementTypeDef, ByteMatchStatementOutputTypeDef]
PutLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutLoggingConfigurationRequestRequestTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationTypeDef,
    },
)
RegexMatchStatementUnionTypeDef = Union[
    RegexMatchStatementTypeDef, RegexMatchStatementOutputTypeDef
]
RegexPatternSetReferenceStatementUnionTypeDef = Union[
    RegexPatternSetReferenceStatementTypeDef, RegexPatternSetReferenceStatementOutputTypeDef
]
SizeConstraintStatementUnionTypeDef = Union[
    SizeConstraintStatementTypeDef, SizeConstraintStatementOutputTypeDef
]
SqliMatchStatementUnionTypeDef = Union[SqliMatchStatementTypeDef, SqliMatchStatementOutputTypeDef]
XssMatchStatementUnionTypeDef = Union[XssMatchStatementTypeDef, XssMatchStatementOutputTypeDef]
ManagedRuleGroupConfigUnionTypeDef = Union[
    ManagedRuleGroupConfigTypeDef, ManagedRuleGroupConfigOutputTypeDef
]
RuleGroupTypeDef = TypedDict(
    "RuleGroupTypeDef",
    {
        "Name": str,
        "Id": str,
        "Capacity": int,
        "ARN": str,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "Description": NotRequired[str],
        "Rules": NotRequired[List[RuleOutputTypeDef]],
        "LabelNamespace": NotRequired[str],
        "CustomResponseBodies": NotRequired[Dict[str, CustomResponseBodyTypeDef]],
        "AvailableLabels": NotRequired[List[LabelSummaryTypeDef]],
        "ConsumedLabels": NotRequired[List[LabelSummaryTypeDef]],
    },
)
WebACLTypeDef = TypedDict(
    "WebACLTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "DefaultAction": DefaultActionOutputTypeDef,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "Description": NotRequired[str],
        "Rules": NotRequired[List[RuleOutputTypeDef]],
        "Capacity": NotRequired[int],
        "PreProcessFirewallManagerRuleGroups": NotRequired[List[FirewallManagerRuleGroupTypeDef]],
        "PostProcessFirewallManagerRuleGroups": NotRequired[List[FirewallManagerRuleGroupTypeDef]],
        "ManagedByFirewallManager": NotRequired[bool],
        "LabelNamespace": NotRequired[str],
        "CustomResponseBodies": NotRequired[Dict[str, CustomResponseBodyTypeDef]],
        "CaptchaConfig": NotRequired[CaptchaConfigTypeDef],
        "ChallengeConfig": NotRequired[ChallengeConfigTypeDef],
        "TokenDomains": NotRequired[List[str]],
        "AssociationConfig": NotRequired[AssociationConfigOutputTypeDef],
        "RetrofittedByFirewallManager": NotRequired[bool],
    },
)
RuleActionOverrideUnionTypeDef = Union[RuleActionOverrideTypeDef, RuleActionOverrideOutputTypeDef]
ManagedRuleGroupStatementTypeDef = TypedDict(
    "ManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Version": NotRequired[str],
        "ExcludedRules": NotRequired[Sequence[ExcludedRuleTypeDef]],
        "ScopeDownStatement": NotRequired[Mapping[str, Any]],
        "ManagedRuleGroupConfigs": NotRequired[Sequence[ManagedRuleGroupConfigUnionTypeDef]],
        "RuleActionOverrides": NotRequired[Sequence[RuleActionOverrideTypeDef]],
    },
)
GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": RuleGroupTypeDef,
        "LockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWebACLForResourceResponseTypeDef = TypedDict(
    "GetWebACLForResourceResponseTypeDef",
    {
        "WebACL": WebACLTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": WebACLTypeDef,
        "LockToken": str,
        "ApplicationIntegrationURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleGroupReferenceStatementTypeDef = TypedDict(
    "RuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": NotRequired[Sequence[ExcludedRuleTypeDef]],
        "RuleActionOverrides": NotRequired[Sequence[RuleActionOverrideUnionTypeDef]],
    },
)
ManagedRuleGroupStatementUnionTypeDef = Union[
    ManagedRuleGroupStatementTypeDef, ManagedRuleGroupStatementOutputTypeDef
]
RuleGroupReferenceStatementUnionTypeDef = Union[
    RuleGroupReferenceStatementTypeDef, RuleGroupReferenceStatementOutputTypeDef
]
StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "ByteMatchStatement": NotRequired[ByteMatchStatementUnionTypeDef],
        "SqliMatchStatement": NotRequired[SqliMatchStatementUnionTypeDef],
        "XssMatchStatement": NotRequired[XssMatchStatementUnionTypeDef],
        "SizeConstraintStatement": NotRequired[SizeConstraintStatementUnionTypeDef],
        "GeoMatchStatement": NotRequired[GeoMatchStatementUnionTypeDef],
        "RuleGroupReferenceStatement": NotRequired[RuleGroupReferenceStatementUnionTypeDef],
        "IPSetReferenceStatement": NotRequired[IPSetReferenceStatementTypeDef],
        "RegexPatternSetReferenceStatement": NotRequired[
            RegexPatternSetReferenceStatementUnionTypeDef
        ],
        "RateBasedStatement": NotRequired[RateBasedStatementUnionTypeDef],
        "AndStatement": NotRequired[AndStatementUnionTypeDef],
        "OrStatement": NotRequired[OrStatementUnionTypeDef],
        "NotStatement": NotRequired[NotStatementUnionTypeDef],
        "ManagedRuleGroupStatement": NotRequired[ManagedRuleGroupStatementUnionTypeDef],
        "LabelMatchStatement": NotRequired[LabelMatchStatementTypeDef],
        "RegexMatchStatement": NotRequired[RegexMatchStatementUnionTypeDef],
    },
)
StatementUnionTypeDef = Union[StatementTypeDef, StatementOutputTypeDef]
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": StatementUnionTypeDef,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "Action": NotRequired[RuleActionUnionTypeDef],
        "OverrideAction": NotRequired[OverrideActionUnionTypeDef],
        "RuleLabels": NotRequired[Sequence[LabelTypeDef]],
        "CaptchaConfig": NotRequired[CaptchaConfigTypeDef],
        "ChallengeConfig": NotRequired[ChallengeConfigTypeDef],
    },
)
CreateRuleGroupRequestRequestTypeDef = TypedDict(
    "CreateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Capacity": int,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence[RuleTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "CustomResponseBodies": NotRequired[Mapping[str, CustomResponseBodyTypeDef]],
    },
)
CreateWebACLRequestRequestTypeDef = TypedDict(
    "CreateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "DefaultAction": DefaultActionTypeDef,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence[RuleTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "CustomResponseBodies": NotRequired[Mapping[str, CustomResponseBodyTypeDef]],
        "CaptchaConfig": NotRequired[CaptchaConfigTypeDef],
        "ChallengeConfig": NotRequired[ChallengeConfigTypeDef],
        "TokenDomains": NotRequired[Sequence[str]],
        "AssociationConfig": NotRequired[AssociationConfigTypeDef],
    },
)
RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]
UpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "UpdateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "LockToken": str,
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence[RuleTypeDef]],
        "CustomResponseBodies": NotRequired[Mapping[str, CustomResponseBodyTypeDef]],
    },
)
UpdateWebACLRequestRequestTypeDef = TypedDict(
    "UpdateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "DefaultAction": DefaultActionTypeDef,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "LockToken": str,
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence[RuleTypeDef]],
        "CustomResponseBodies": NotRequired[Mapping[str, CustomResponseBodyTypeDef]],
        "CaptchaConfig": NotRequired[CaptchaConfigTypeDef],
        "ChallengeConfig": NotRequired[ChallengeConfigTypeDef],
        "TokenDomains": NotRequired[Sequence[str]],
        "AssociationConfig": NotRequired[AssociationConfigTypeDef],
    },
)
CheckCapacityRequestRequestTypeDef = TypedDict(
    "CheckCapacityRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "Rules": Sequence[RuleUnionTypeDef],
    },
)
