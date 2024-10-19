"""
Type annotations for waf service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_waf/type_defs/)

Usage::

    ```python
    from mypy_boto3_waf.type_defs import ExcludedRuleTypeDef

    data: ExcludedRuleTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ChangeActionType,
    ChangeTokenStatusType,
    ComparisonOperatorType,
    GeoMatchConstraintValueType,
    IPSetDescriptorTypeType,
    MatchFieldTypeType,
    PositionalConstraintType,
    PredicateTypeType,
    TextTransformationType,
    WafActionTypeType,
    WafOverrideActionTypeType,
    WafRuleTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ExcludedRuleTypeDef",
    "WafActionTypeDef",
    "WafOverrideActionTypeDef",
    "BlobTypeDef",
    "ByteMatchSetSummaryTypeDef",
    "FieldToMatchTypeDef",
    "CreateByteMatchSetRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateGeoMatchSetRequestRequestTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "TagTypeDef",
    "CreateRegexMatchSetRequestRequestTypeDef",
    "CreateRegexPatternSetRequestRequestTypeDef",
    "RegexPatternSetTypeDef",
    "RuleGroupTypeDef",
    "CreateSizeConstraintSetRequestRequestTypeDef",
    "CreateSqlInjectionMatchSetRequestRequestTypeDef",
    "CreateWebACLMigrationStackRequestRequestTypeDef",
    "CreateXssMatchSetRequestRequestTypeDef",
    "DeleteByteMatchSetRequestRequestTypeDef",
    "DeleteGeoMatchSetRequestRequestTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeletePermissionPolicyRequestRequestTypeDef",
    "DeleteRateBasedRuleRequestRequestTypeDef",
    "DeleteRegexMatchSetRequestRequestTypeDef",
    "DeleteRegexPatternSetRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DeleteSizeConstraintSetRequestRequestTypeDef",
    "DeleteSqlInjectionMatchSetRequestRequestTypeDef",
    "DeleteWebACLRequestRequestTypeDef",
    "DeleteXssMatchSetRequestRequestTypeDef",
    "GeoMatchConstraintTypeDef",
    "GeoMatchSetSummaryTypeDef",
    "GetByteMatchSetRequestRequestTypeDef",
    "GetChangeTokenStatusRequestRequestTypeDef",
    "GetGeoMatchSetRequestRequestTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetPermissionPolicyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetRateBasedRuleManagedKeysRequestRequestTypeDef",
    "GetRateBasedRuleRequestRequestTypeDef",
    "GetRegexMatchSetRequestRequestTypeDef",
    "GetRegexPatternSetRequestRequestTypeDef",
    "GetRuleGroupRequestRequestTypeDef",
    "GetRuleRequestRequestTypeDef",
    "TimeWindowOutputTypeDef",
    "GetSizeConstraintSetRequestRequestTypeDef",
    "GetSqlInjectionMatchSetRequestRequestTypeDef",
    "GetWebACLRequestRequestTypeDef",
    "GetXssMatchSetRequestRequestTypeDef",
    "HTTPHeaderTypeDef",
    "IPSetDescriptorTypeDef",
    "IPSetSummaryTypeDef",
    "ListActivatedRulesInRuleGroupRequestRequestTypeDef",
    "ListByteMatchSetsRequestRequestTypeDef",
    "ListGeoMatchSetsRequestRequestTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListRateBasedRulesRequestRequestTypeDef",
    "RuleSummaryTypeDef",
    "ListRegexMatchSetsRequestRequestTypeDef",
    "RegexMatchSetSummaryTypeDef",
    "ListRegexPatternSetsRequestRequestTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "RuleGroupSummaryTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListSizeConstraintSetsRequestRequestTypeDef",
    "SizeConstraintSetSummaryTypeDef",
    "ListSqlInjectionMatchSetsRequestRequestTypeDef",
    "SqlInjectionMatchSetSummaryTypeDef",
    "ListSubscribedRuleGroupsRequestRequestTypeDef",
    "SubscribedRuleGroupSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWebACLsRequestRequestTypeDef",
    "WebACLSummaryTypeDef",
    "ListXssMatchSetsRequestRequestTypeDef",
    "XssMatchSetSummaryTypeDef",
    "PredicateTypeDef",
    "PutPermissionPolicyRequestRequestTypeDef",
    "RegexPatternSetUpdateTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ActivatedRuleOutputTypeDef",
    "ActivatedRuleTypeDef",
    "ByteMatchTupleOutputTypeDef",
    "ByteMatchTupleTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "RegexMatchTupleTypeDef",
    "SizeConstraintTypeDef",
    "SqlInjectionMatchTupleTypeDef",
    "XssMatchTupleTypeDef",
    "CreateWebACLMigrationStackResponseTypeDef",
    "DeleteByteMatchSetResponseTypeDef",
    "DeleteGeoMatchSetResponseTypeDef",
    "DeleteIPSetResponseTypeDef",
    "DeleteRateBasedRuleResponseTypeDef",
    "DeleteRegexMatchSetResponseTypeDef",
    "DeleteRegexPatternSetResponseTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DeleteRuleResponseTypeDef",
    "DeleteSizeConstraintSetResponseTypeDef",
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    "DeleteWebACLResponseTypeDef",
    "DeleteXssMatchSetResponseTypeDef",
    "GetChangeTokenResponseTypeDef",
    "GetChangeTokenStatusResponseTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    "ListByteMatchSetsResponseTypeDef",
    "UpdateByteMatchSetResponseTypeDef",
    "UpdateGeoMatchSetResponseTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRateBasedRuleResponseTypeDef",
    "UpdateRegexMatchSetResponseTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateRuleResponseTypeDef",
    "UpdateSizeConstraintSetResponseTypeDef",
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UpdateXssMatchSetResponseTypeDef",
    "CreateRateBasedRuleRequestRequestTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateWebACLRequestRequestTypeDef",
    "TagInfoForResourceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GeoMatchSetTypeDef",
    "GeoMatchSetUpdateTypeDef",
    "ListGeoMatchSetsResponseTypeDef",
    "GetRateBasedRuleManagedKeysRequestGetRateBasedRuleManagedKeysPaginateTypeDef",
    "ListActivatedRulesInRuleGroupRequestListActivatedRulesInRuleGroupPaginateTypeDef",
    "ListByteMatchSetsRequestListByteMatchSetsPaginateTypeDef",
    "ListGeoMatchSetsRequestListGeoMatchSetsPaginateTypeDef",
    "ListIPSetsRequestListIPSetsPaginateTypeDef",
    "ListLoggingConfigurationsRequestListLoggingConfigurationsPaginateTypeDef",
    "ListRateBasedRulesRequestListRateBasedRulesPaginateTypeDef",
    "ListRegexMatchSetsRequestListRegexMatchSetsPaginateTypeDef",
    "ListRegexPatternSetsRequestListRegexPatternSetsPaginateTypeDef",
    "ListRuleGroupsRequestListRuleGroupsPaginateTypeDef",
    "ListRulesRequestListRulesPaginateTypeDef",
    "ListSizeConstraintSetsRequestListSizeConstraintSetsPaginateTypeDef",
    "ListSqlInjectionMatchSetsRequestListSqlInjectionMatchSetsPaginateTypeDef",
    "ListSubscribedRuleGroupsRequestListSubscribedRuleGroupsPaginateTypeDef",
    "ListWebACLsRequestListWebACLsPaginateTypeDef",
    "ListXssMatchSetsRequestListXssMatchSetsPaginateTypeDef",
    "HTTPRequestTypeDef",
    "IPSetTypeDef",
    "IPSetUpdateTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListRateBasedRulesResponseTypeDef",
    "ListRulesResponseTypeDef",
    "ListRegexMatchSetsResponseTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListSizeConstraintSetsResponseTypeDef",
    "ListSqlInjectionMatchSetsResponseTypeDef",
    "ListSubscribedRuleGroupsResponseTypeDef",
    "ListWebACLsResponseTypeDef",
    "ListXssMatchSetsResponseTypeDef",
    "RateBasedRuleTypeDef",
    "RuleTypeDef",
    "RuleUpdateTypeDef",
    "UpdateRegexPatternSetRequestRequestTypeDef",
    "TimeWindowTypeDef",
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    "WebACLTypeDef",
    "ActivatedRuleUnionTypeDef",
    "ByteMatchSetTypeDef",
    "ByteMatchTupleUnionTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutLoggingConfigurationRequestRequestTypeDef",
    "RegexMatchSetTypeDef",
    "RegexMatchSetUpdateTypeDef",
    "SizeConstraintSetTypeDef",
    "SizeConstraintSetUpdateTypeDef",
    "SqlInjectionMatchSetTypeDef",
    "SqlInjectionMatchSetUpdateTypeDef",
    "XssMatchSetTypeDef",
    "XssMatchSetUpdateTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateGeoMatchSetResponseTypeDef",
    "GetGeoMatchSetResponseTypeDef",
    "UpdateGeoMatchSetRequestRequestTypeDef",
    "SampledHTTPRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "GetIPSetResponseTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "CreateRateBasedRuleResponseTypeDef",
    "GetRateBasedRuleResponseTypeDef",
    "CreateRuleResponseTypeDef",
    "GetRuleResponseTypeDef",
    "UpdateRateBasedRuleRequestRequestTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "GetSampledRequestsRequestRequestTypeDef",
    "CreateWebACLResponseTypeDef",
    "GetWebACLResponseTypeDef",
    "RuleGroupUpdateTypeDef",
    "WebACLUpdateTypeDef",
    "CreateByteMatchSetResponseTypeDef",
    "GetByteMatchSetResponseTypeDef",
    "ByteMatchSetUpdateTypeDef",
    "CreateRegexMatchSetResponseTypeDef",
    "GetRegexMatchSetResponseTypeDef",
    "UpdateRegexMatchSetRequestRequestTypeDef",
    "CreateSizeConstraintSetResponseTypeDef",
    "GetSizeConstraintSetResponseTypeDef",
    "UpdateSizeConstraintSetRequestRequestTypeDef",
    "CreateSqlInjectionMatchSetResponseTypeDef",
    "GetSqlInjectionMatchSetResponseTypeDef",
    "UpdateSqlInjectionMatchSetRequestRequestTypeDef",
    "CreateXssMatchSetResponseTypeDef",
    "GetXssMatchSetResponseTypeDef",
    "UpdateXssMatchSetRequestRequestTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateWebACLRequestRequestTypeDef",
    "UpdateByteMatchSetRequestRequestTypeDef",
)

ExcludedRuleTypeDef = TypedDict(
    "ExcludedRuleTypeDef",
    {
        "RuleId": str,
    },
)
WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": WafActionTypeType,
    },
)
WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": WafOverrideActionTypeType,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ByteMatchSetSummaryTypeDef = TypedDict(
    "ByteMatchSetSummaryTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
    },
)
FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "Type": MatchFieldTypeType,
        "Data": NotRequired[str],
    },
)
CreateByteMatchSetRequestRequestTypeDef = TypedDict(
    "CreateByteMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
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
CreateGeoMatchSetRequestRequestTypeDef = TypedDict(
    "CreateGeoMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)
CreateIPSetRequestRequestTypeDef = TypedDict(
    "CreateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreateRegexMatchSetRequestRequestTypeDef = TypedDict(
    "CreateRegexMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)
CreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "CreateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)
RegexPatternSetTypeDef = TypedDict(
    "RegexPatternSetTypeDef",
    {
        "RegexPatternSetId": str,
        "RegexPatternStrings": List[str],
        "Name": NotRequired[str],
    },
)
RuleGroupTypeDef = TypedDict(
    "RuleGroupTypeDef",
    {
        "RuleGroupId": str,
        "Name": NotRequired[str],
        "MetricName": NotRequired[str],
    },
)
CreateSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "CreateSizeConstraintSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)
CreateSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)
CreateWebACLMigrationStackRequestRequestTypeDef = TypedDict(
    "CreateWebACLMigrationStackRequestRequestTypeDef",
    {
        "WebACLId": str,
        "S3BucketName": str,
        "IgnoreUnsupportedType": bool,
    },
)
CreateXssMatchSetRequestRequestTypeDef = TypedDict(
    "CreateXssMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)
DeleteByteMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
        "ChangeToken": str,
    },
)
DeleteGeoMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
        "ChangeToken": str,
    },
)
DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
        "ChangeToken": str,
    },
)
DeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DeletePermissionPolicyRequestRequestTypeDef = TypedDict(
    "DeletePermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DeleteRateBasedRuleRequestRequestTypeDef = TypedDict(
    "DeleteRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
    },
)
DeleteRegexMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
        "ChangeToken": str,
    },
)
DeleteRegexPatternSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
        "ChangeToken": str,
    },
)
DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
        "ChangeToken": str,
    },
)
DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
    },
)
DeleteSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "DeleteSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
        "ChangeToken": str,
    },
)
DeleteSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "ChangeToken": str,
    },
)
DeleteWebACLRequestRequestTypeDef = TypedDict(
    "DeleteWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
        "ChangeToken": str,
    },
)
DeleteXssMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
        "ChangeToken": str,
    },
)
GeoMatchConstraintTypeDef = TypedDict(
    "GeoMatchConstraintTypeDef",
    {
        "Type": Literal["Country"],
        "Value": GeoMatchConstraintValueType,
    },
)
GeoMatchSetSummaryTypeDef = TypedDict(
    "GeoMatchSetSummaryTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
    },
)
GetByteMatchSetRequestRequestTypeDef = TypedDict(
    "GetByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
    },
)
GetChangeTokenStatusRequestRequestTypeDef = TypedDict(
    "GetChangeTokenStatusRequestRequestTypeDef",
    {
        "ChangeToken": str,
    },
)
GetGeoMatchSetRequestRequestTypeDef = TypedDict(
    "GetGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
    },
)
GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
    },
)
GetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetPermissionPolicyRequestRequestTypeDef = TypedDict(
    "GetPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
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
GetRateBasedRuleManagedKeysRequestRequestTypeDef = TypedDict(
    "GetRateBasedRuleManagedKeysRequestRequestTypeDef",
    {
        "RuleId": str,
        "NextMarker": NotRequired[str],
    },
)
GetRateBasedRuleRequestRequestTypeDef = TypedDict(
    "GetRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
    },
)
GetRegexMatchSetRequestRequestTypeDef = TypedDict(
    "GetRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
    },
)
GetRegexPatternSetRequestRequestTypeDef = TypedDict(
    "GetRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
    },
)
GetRuleGroupRequestRequestTypeDef = TypedDict(
    "GetRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
    },
)
GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "RuleId": str,
    },
)
TimeWindowOutputTypeDef = TypedDict(
    "TimeWindowOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
)
GetSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "GetSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
    },
)
GetSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "GetSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
    },
)
GetWebACLRequestRequestTypeDef = TypedDict(
    "GetWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
    },
)
GetXssMatchSetRequestRequestTypeDef = TypedDict(
    "GetXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
    },
)
HTTPHeaderTypeDef = TypedDict(
    "HTTPHeaderTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
IPSetDescriptorTypeDef = TypedDict(
    "IPSetDescriptorTypeDef",
    {
        "Type": IPSetDescriptorTypeType,
        "Value": str,
    },
)
IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "IPSetId": str,
        "Name": str,
    },
)
ListActivatedRulesInRuleGroupRequestRequestTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": NotRequired[str],
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListByteMatchSetsRequestRequestTypeDef = TypedDict(
    "ListByteMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListGeoMatchSetsRequestRequestTypeDef = TypedDict(
    "ListGeoMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListIPSetsRequestRequestTypeDef = TypedDict(
    "ListIPSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListRateBasedRulesRequestRequestTypeDef = TypedDict(
    "ListRateBasedRulesRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "RuleId": str,
        "Name": str,
    },
)
ListRegexMatchSetsRequestRequestTypeDef = TypedDict(
    "ListRegexMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
RegexMatchSetSummaryTypeDef = TypedDict(
    "RegexMatchSetSummaryTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
    },
)
ListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "ListRegexPatternSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {
        "RegexPatternSetId": str,
        "Name": str,
    },
)
ListRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "RuleGroupId": str,
        "Name": str,
    },
)
ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListSizeConstraintSetsRequestRequestTypeDef = TypedDict(
    "ListSizeConstraintSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
SizeConstraintSetSummaryTypeDef = TypedDict(
    "SizeConstraintSetSummaryTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
    },
)
ListSqlInjectionMatchSetsRequestRequestTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
SqlInjectionMatchSetSummaryTypeDef = TypedDict(
    "SqlInjectionMatchSetSummaryTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
    },
)
ListSubscribedRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListSubscribedRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
SubscribedRuleGroupSummaryTypeDef = TypedDict(
    "SubscribedRuleGroupSummaryTypeDef",
    {
        "RuleGroupId": str,
        "Name": str,
        "MetricName": str,
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
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "WebACLId": str,
        "Name": str,
    },
)
ListXssMatchSetsRequestRequestTypeDef = TypedDict(
    "ListXssMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
XssMatchSetSummaryTypeDef = TypedDict(
    "XssMatchSetSummaryTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
    },
)
PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Negated": bool,
        "Type": PredicateTypeType,
        "DataId": str,
    },
)
PutPermissionPolicyRequestRequestTypeDef = TypedDict(
    "PutPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)
RegexPatternSetUpdateTypeDef = TypedDict(
    "RegexPatternSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "RegexPatternString": str,
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
ActivatedRuleOutputTypeDef = TypedDict(
    "ActivatedRuleOutputTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": NotRequired[WafActionTypeDef],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Type": NotRequired[WafRuleTypeType],
        "ExcludedRules": NotRequired[List[ExcludedRuleTypeDef]],
    },
)
ActivatedRuleTypeDef = TypedDict(
    "ActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": NotRequired[WafActionTypeDef],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Type": NotRequired[WafRuleTypeType],
        "ExcludedRules": NotRequired[Sequence[ExcludedRuleTypeDef]],
    },
)
ByteMatchTupleOutputTypeDef = TypedDict(
    "ByteMatchTupleOutputTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": TextTransformationType,
        "PositionalConstraint": PositionalConstraintType,
    },
)
ByteMatchTupleTypeDef = TypedDict(
    "ByteMatchTupleTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "TargetString": BlobTypeDef,
        "TextTransformation": TextTransformationType,
        "PositionalConstraint": PositionalConstraintType,
    },
)
LoggingConfigurationOutputTypeDef = TypedDict(
    "LoggingConfigurationOutputTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": NotRequired[List[FieldToMatchTypeDef]],
    },
)
LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": Sequence[str],
        "RedactedFields": NotRequired[Sequence[FieldToMatchTypeDef]],
    },
)
RegexMatchTupleTypeDef = TypedDict(
    "RegexMatchTupleTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformation": TextTransformationType,
        "RegexPatternSetId": str,
    },
)
SizeConstraintTypeDef = TypedDict(
    "SizeConstraintTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformation": TextTransformationType,
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
    },
)
SqlInjectionMatchTupleTypeDef = TypedDict(
    "SqlInjectionMatchTupleTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformation": TextTransformationType,
    },
)
XssMatchTupleTypeDef = TypedDict(
    "XssMatchTupleTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformation": TextTransformationType,
    },
)
CreateWebACLMigrationStackResponseTypeDef = TypedDict(
    "CreateWebACLMigrationStackResponseTypeDef",
    {
        "S3ObjectUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteByteMatchSetResponseTypeDef = TypedDict(
    "DeleteByteMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGeoMatchSetResponseTypeDef = TypedDict(
    "DeleteGeoMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIPSetResponseTypeDef = TypedDict(
    "DeleteIPSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRateBasedRuleResponseTypeDef = TypedDict(
    "DeleteRateBasedRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRegexMatchSetResponseTypeDef = TypedDict(
    "DeleteRegexMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRegexPatternSetResponseTypeDef = TypedDict(
    "DeleteRegexPatternSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRuleGroupResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRuleResponseTypeDef = TypedDict(
    "DeleteRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSizeConstraintSetResponseTypeDef = TypedDict(
    "DeleteSizeConstraintSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWebACLResponseTypeDef = TypedDict(
    "DeleteWebACLResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteXssMatchSetResponseTypeDef = TypedDict(
    "DeleteXssMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChangeTokenResponseTypeDef = TypedDict(
    "GetChangeTokenResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChangeTokenStatusResponseTypeDef = TypedDict(
    "GetChangeTokenStatusResponseTypeDef",
    {
        "ChangeTokenStatus": ChangeTokenStatusType,
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
GetRateBasedRuleManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    {
        "ManagedKeys": List[str],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListByteMatchSetsResponseTypeDef = TypedDict(
    "ListByteMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ByteMatchSets": List[ByteMatchSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateByteMatchSetResponseTypeDef = TypedDict(
    "UpdateByteMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGeoMatchSetResponseTypeDef = TypedDict(
    "UpdateGeoMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRateBasedRuleResponseTypeDef = TypedDict(
    "UpdateRateBasedRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRegexMatchSetResponseTypeDef = TypedDict(
    "UpdateRegexMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSizeConstraintSetResponseTypeDef = TypedDict(
    "UpdateSizeConstraintSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateXssMatchSetResponseTypeDef = TypedDict(
    "UpdateXssMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRateBasedRuleRequestRequestTypeDef = TypedDict(
    "CreateRateBasedRuleRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "RateKey": Literal["IP"],
        "RateLimit": int,
        "ChangeToken": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRuleGroupRequestRequestTypeDef = TypedDict(
    "CreateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "ChangeToken": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRuleRequestRequestTypeDef = TypedDict(
    "CreateRuleRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "ChangeToken": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateWebACLRequestRequestTypeDef = TypedDict(
    "CreateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "DefaultAction": WafActionTypeDef,
        "ChangeToken": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
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
CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": RegexPatternSetTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": RegexPatternSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "RuleGroup": RuleGroupTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": RuleGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GeoMatchSetTypeDef = TypedDict(
    "GeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "GeoMatchConstraints": List[GeoMatchConstraintTypeDef],
        "Name": NotRequired[str],
    },
)
GeoMatchSetUpdateTypeDef = TypedDict(
    "GeoMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "GeoMatchConstraint": GeoMatchConstraintTypeDef,
    },
)
ListGeoMatchSetsResponseTypeDef = TypedDict(
    "ListGeoMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "GeoMatchSets": List[GeoMatchSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRateBasedRuleManagedKeysRequestGetRateBasedRuleManagedKeysPaginateTypeDef = TypedDict(
    "GetRateBasedRuleManagedKeysRequestGetRateBasedRuleManagedKeysPaginateTypeDef",
    {
        "RuleId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListActivatedRulesInRuleGroupRequestListActivatedRulesInRuleGroupPaginateTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupRequestListActivatedRulesInRuleGroupPaginateTypeDef",
    {
        "RuleGroupId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListByteMatchSetsRequestListByteMatchSetsPaginateTypeDef = TypedDict(
    "ListByteMatchSetsRequestListByteMatchSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGeoMatchSetsRequestListGeoMatchSetsPaginateTypeDef = TypedDict(
    "ListGeoMatchSetsRequestListGeoMatchSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIPSetsRequestListIPSetsPaginateTypeDef = TypedDict(
    "ListIPSetsRequestListIPSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLoggingConfigurationsRequestListLoggingConfigurationsPaginateTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestListLoggingConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRateBasedRulesRequestListRateBasedRulesPaginateTypeDef = TypedDict(
    "ListRateBasedRulesRequestListRateBasedRulesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegexMatchSetsRequestListRegexMatchSetsPaginateTypeDef = TypedDict(
    "ListRegexMatchSetsRequestListRegexMatchSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegexPatternSetsRequestListRegexPatternSetsPaginateTypeDef = TypedDict(
    "ListRegexPatternSetsRequestListRegexPatternSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRuleGroupsRequestListRuleGroupsPaginateTypeDef = TypedDict(
    "ListRuleGroupsRequestListRuleGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "ListRulesRequestListRulesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSizeConstraintSetsRequestListSizeConstraintSetsPaginateTypeDef = TypedDict(
    "ListSizeConstraintSetsRequestListSizeConstraintSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSqlInjectionMatchSetsRequestListSqlInjectionMatchSetsPaginateTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsRequestListSqlInjectionMatchSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscribedRuleGroupsRequestListSubscribedRuleGroupsPaginateTypeDef = TypedDict(
    "ListSubscribedRuleGroupsRequestListSubscribedRuleGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWebACLsRequestListWebACLsPaginateTypeDef = TypedDict(
    "ListWebACLsRequestListWebACLsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListXssMatchSetsRequestListXssMatchSetsPaginateTypeDef = TypedDict(
    "ListXssMatchSetsRequestListXssMatchSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
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
IPSetTypeDef = TypedDict(
    "IPSetTypeDef",
    {
        "IPSetId": str,
        "IPSetDescriptors": List[IPSetDescriptorTypeDef],
        "Name": NotRequired[str],
    },
)
IPSetUpdateTypeDef = TypedDict(
    "IPSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "IPSetDescriptor": IPSetDescriptorTypeDef,
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
ListRateBasedRulesResponseTypeDef = TypedDict(
    "ListRateBasedRulesResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List[RuleSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List[RuleSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRegexMatchSetsResponseTypeDef = TypedDict(
    "ListRegexMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexMatchSets": List[RegexMatchSetSummaryTypeDef],
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
ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List[RuleGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSizeConstraintSetsResponseTypeDef = TypedDict(
    "ListSizeConstraintSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SizeConstraintSets": List[SizeConstraintSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSqlInjectionMatchSetsResponseTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SqlInjectionMatchSets": List[SqlInjectionMatchSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscribedRuleGroupsResponseTypeDef = TypedDict(
    "ListSubscribedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List[SubscribedRuleGroupSummaryTypeDef],
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
ListXssMatchSetsResponseTypeDef = TypedDict(
    "ListXssMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "XssMatchSets": List[XssMatchSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RateBasedRuleTypeDef = TypedDict(
    "RateBasedRuleTypeDef",
    {
        "RuleId": str,
        "MatchPredicates": List[PredicateTypeDef],
        "RateKey": Literal["IP"],
        "RateLimit": int,
        "Name": NotRequired[str],
        "MetricName": NotRequired[str],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "RuleId": str,
        "Predicates": List[PredicateTypeDef],
        "Name": NotRequired[str],
        "MetricName": NotRequired[str],
    },
)
RuleUpdateTypeDef = TypedDict(
    "RuleUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "Predicate": PredicateTypeDef,
    },
)
UpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "UpdateRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
        "Updates": Sequence[RegexPatternSetUpdateTypeDef],
        "ChangeToken": str,
    },
)
TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
    },
)
ListActivatedRulesInRuleGroupResponseTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    {
        "NextMarker": str,
        "ActivatedRules": List[ActivatedRuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WebACLTypeDef = TypedDict(
    "WebACLTypeDef",
    {
        "WebACLId": str,
        "DefaultAction": WafActionTypeDef,
        "Rules": List[ActivatedRuleOutputTypeDef],
        "Name": NotRequired[str],
        "MetricName": NotRequired[str],
        "WebACLArn": NotRequired[str],
    },
)
ActivatedRuleUnionTypeDef = Union[ActivatedRuleTypeDef, ActivatedRuleOutputTypeDef]
ByteMatchSetTypeDef = TypedDict(
    "ByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "ByteMatchTuples": List[ByteMatchTupleOutputTypeDef],
        "Name": NotRequired[str],
    },
)
ByteMatchTupleUnionTypeDef = Union[ByteMatchTupleTypeDef, ByteMatchTupleOutputTypeDef]
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
PutLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutLoggingConfigurationRequestRequestTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationTypeDef,
    },
)
RegexMatchSetTypeDef = TypedDict(
    "RegexMatchSetTypeDef",
    {
        "RegexMatchSetId": NotRequired[str],
        "Name": NotRequired[str],
        "RegexMatchTuples": NotRequired[List[RegexMatchTupleTypeDef]],
    },
)
RegexMatchSetUpdateTypeDef = TypedDict(
    "RegexMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "RegexMatchTuple": RegexMatchTupleTypeDef,
    },
)
SizeConstraintSetTypeDef = TypedDict(
    "SizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "SizeConstraints": List[SizeConstraintTypeDef],
        "Name": NotRequired[str],
    },
)
SizeConstraintSetUpdateTypeDef = TypedDict(
    "SizeConstraintSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "SizeConstraint": SizeConstraintTypeDef,
    },
)
SqlInjectionMatchSetTypeDef = TypedDict(
    "SqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "SqlInjectionMatchTuples": List[SqlInjectionMatchTupleTypeDef],
        "Name": NotRequired[str],
    },
)
SqlInjectionMatchSetUpdateTypeDef = TypedDict(
    "SqlInjectionMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "SqlInjectionMatchTuple": SqlInjectionMatchTupleTypeDef,
    },
)
XssMatchSetTypeDef = TypedDict(
    "XssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "XssMatchTuples": List[XssMatchTupleTypeDef],
        "Name": NotRequired[str],
    },
)
XssMatchSetUpdateTypeDef = TypedDict(
    "XssMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "XssMatchTuple": XssMatchTupleTypeDef,
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
CreateGeoMatchSetResponseTypeDef = TypedDict(
    "CreateGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": GeoMatchSetTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGeoMatchSetResponseTypeDef = TypedDict(
    "GetGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": GeoMatchSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGeoMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
        "ChangeToken": str,
        "Updates": Sequence[GeoMatchSetUpdateTypeDef],
    },
)
SampledHTTPRequestTypeDef = TypedDict(
    "SampledHTTPRequestTypeDef",
    {
        "Request": HTTPRequestTypeDef,
        "Weight": int,
        "Timestamp": NotRequired[datetime],
        "Action": NotRequired[str],
        "RuleWithinRuleGroup": NotRequired[str],
    },
)
CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "IPSet": IPSetTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": IPSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIPSetRequestRequestTypeDef = TypedDict(
    "UpdateIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
        "ChangeToken": str,
        "Updates": Sequence[IPSetUpdateTypeDef],
    },
)
CreateRateBasedRuleResponseTypeDef = TypedDict(
    "CreateRateBasedRuleResponseTypeDef",
    {
        "Rule": RateBasedRuleTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRateBasedRuleResponseTypeDef = TypedDict(
    "GetRateBasedRuleResponseTypeDef",
    {
        "Rule": RateBasedRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "Rule": RuleTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "Rule": RuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRateBasedRuleRequestRequestTypeDef = TypedDict(
    "UpdateRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
        "Updates": Sequence[RuleUpdateTypeDef],
        "RateLimit": int,
    },
)
UpdateRuleRequestRequestTypeDef = TypedDict(
    "UpdateRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
        "Updates": Sequence[RuleUpdateTypeDef],
    },
)
GetSampledRequestsRequestRequestTypeDef = TypedDict(
    "GetSampledRequestsRequestRequestTypeDef",
    {
        "WebAclId": str,
        "RuleId": str,
        "TimeWindow": TimeWindowTypeDef,
        "MaxItems": int,
    },
)
CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef",
    {
        "WebACL": WebACLTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": WebACLTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleGroupUpdateTypeDef = TypedDict(
    "RuleGroupUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ActivatedRule": ActivatedRuleUnionTypeDef,
    },
)
WebACLUpdateTypeDef = TypedDict(
    "WebACLUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ActivatedRule": ActivatedRuleUnionTypeDef,
    },
)
CreateByteMatchSetResponseTypeDef = TypedDict(
    "CreateByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": ByteMatchSetTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetByteMatchSetResponseTypeDef = TypedDict(
    "GetByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": ByteMatchSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ByteMatchSetUpdateTypeDef = TypedDict(
    "ByteMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ByteMatchTuple": ByteMatchTupleUnionTypeDef,
    },
)
CreateRegexMatchSetResponseTypeDef = TypedDict(
    "CreateRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": RegexMatchSetTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegexMatchSetResponseTypeDef = TypedDict(
    "GetRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": RegexMatchSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRegexMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
        "Updates": Sequence[RegexMatchSetUpdateTypeDef],
        "ChangeToken": str,
    },
)
CreateSizeConstraintSetResponseTypeDef = TypedDict(
    "CreateSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": SizeConstraintSetTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSizeConstraintSetResponseTypeDef = TypedDict(
    "GetSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": SizeConstraintSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "UpdateSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
        "ChangeToken": str,
        "Updates": Sequence[SizeConstraintSetUpdateTypeDef],
    },
)
CreateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": SqlInjectionMatchSetTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "GetSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": SqlInjectionMatchSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "ChangeToken": str,
        "Updates": Sequence[SqlInjectionMatchSetUpdateTypeDef],
    },
)
CreateXssMatchSetResponseTypeDef = TypedDict(
    "CreateXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": XssMatchSetTypeDef,
        "ChangeToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetXssMatchSetResponseTypeDef = TypedDict(
    "GetXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": XssMatchSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateXssMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
        "ChangeToken": str,
        "Updates": Sequence[XssMatchSetUpdateTypeDef],
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
UpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "UpdateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
        "Updates": Sequence[RuleGroupUpdateTypeDef],
        "ChangeToken": str,
    },
)
UpdateWebACLRequestRequestTypeDef = TypedDict(
    "UpdateWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
        "ChangeToken": str,
        "Updates": NotRequired[Sequence[WebACLUpdateTypeDef]],
        "DefaultAction": NotRequired[WafActionTypeDef],
    },
)
UpdateByteMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
        "ChangeToken": str,
        "Updates": Sequence[ByteMatchSetUpdateTypeDef],
    },
)
