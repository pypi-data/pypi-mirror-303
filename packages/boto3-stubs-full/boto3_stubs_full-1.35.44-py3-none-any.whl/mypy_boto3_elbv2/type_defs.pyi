"""
Type annotations for elbv2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/type_defs/)

Usage::

    ```python
    from mypy_boto3_elbv2.type_defs import AuthenticateCognitoActionConfigOutputTypeDef

    data: AuthenticateCognitoActionConfigOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionTypeEnumType,
    AnomalyResultEnumType,
    AuthenticateCognitoActionConditionalBehaviorEnumType,
    AuthenticateOidcActionConditionalBehaviorEnumType,
    DescribeTargetHealthInputIncludeEnumType,
    EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType,
    IpAddressTypeType,
    LoadBalancerSchemeEnumType,
    LoadBalancerStateEnumType,
    LoadBalancerTypeEnumType,
    MitigationInEffectEnumType,
    ProtocolEnumType,
    RedirectActionStatusCodeEnumType,
    TargetAdministrativeOverrideReasonEnumType,
    TargetAdministrativeOverrideStateEnumType,
    TargetGroupIpAddressTypeEnumType,
    TargetHealthReasonEnumType,
    TargetHealthStateEnumType,
    TargetTypeEnumType,
    TrustStoreAssociationStatusEnumType,
    TrustStoreStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AuthenticateCognitoActionConfigOutputTypeDef",
    "AuthenticateOidcActionConfigOutputTypeDef",
    "FixedResponseActionConfigTypeDef",
    "RedirectActionConfigTypeDef",
    "CertificateTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "RevocationContentTypeDef",
    "TrustStoreRevocationTypeDef",
    "AdministrativeOverrideTypeDef",
    "AnomalyDetectionTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "LoadBalancerAddressTypeDef",
    "CipherTypeDef",
    "MutualAuthenticationAttributesTypeDef",
    "SubnetMappingTypeDef",
    "MatcherTypeDef",
    "TrustStoreTypeDef",
    "DeleteListenerInputRequestTypeDef",
    "DeleteLoadBalancerInputRequestTypeDef",
    "DeleteRuleInputRequestTypeDef",
    "DeleteSharedTrustStoreAssociationInputRequestTypeDef",
    "DeleteTargetGroupInputRequestTypeDef",
    "DeleteTrustStoreInputRequestTypeDef",
    "TargetDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "LimitTypeDef",
    "DescribeListenerAttributesInputRequestTypeDef",
    "ListenerAttributeTypeDef",
    "DescribeListenerCertificatesInputRequestTypeDef",
    "DescribeListenersInputRequestTypeDef",
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    "LoadBalancerAttributeTypeDef",
    "WaiterConfigTypeDef",
    "DescribeLoadBalancersInputRequestTypeDef",
    "DescribeRulesInputRequestTypeDef",
    "DescribeSSLPoliciesInputRequestTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DescribeTargetGroupAttributesInputRequestTypeDef",
    "TargetGroupAttributeTypeDef",
    "DescribeTargetGroupsInputRequestTypeDef",
    "DescribeTrustStoreAssociationsInputRequestTypeDef",
    "TrustStoreAssociationTypeDef",
    "DescribeTrustStoreRevocationTypeDef",
    "DescribeTrustStoreRevocationsInputRequestTypeDef",
    "DescribeTrustStoresInputRequestTypeDef",
    "TargetGroupStickinessConfigTypeDef",
    "TargetGroupTupleTypeDef",
    "GetResourcePolicyInputRequestTypeDef",
    "GetTrustStoreCaCertificatesBundleInputRequestTypeDef",
    "GetTrustStoreRevocationContentInputRequestTypeDef",
    "HostHeaderConditionConfigOutputTypeDef",
    "HostHeaderConditionConfigTypeDef",
    "HttpHeaderConditionConfigOutputTypeDef",
    "HttpHeaderConditionConfigTypeDef",
    "HttpRequestMethodConditionConfigOutputTypeDef",
    "HttpRequestMethodConditionConfigTypeDef",
    "LoadBalancerStateTypeDef",
    "ModifyTrustStoreInputRequestTypeDef",
    "PathPatternConditionConfigOutputTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "RemoveTrustStoreRevocationsInputRequestTypeDef",
    "SourceIpConditionConfigOutputTypeDef",
    "RulePriorityPairTypeDef",
    "SetIpAddressTypeInputRequestTypeDef",
    "SetSecurityGroupsInputRequestTypeDef",
    "SourceIpConditionConfigTypeDef",
    "TargetHealthTypeDef",
    "AddListenerCertificatesInputRequestTypeDef",
    "RemoveListenerCertificatesInputRequestTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GetTrustStoreCaCertificatesBundleOutputTypeDef",
    "GetTrustStoreRevocationContentOutputTypeDef",
    "SetIpAddressTypeOutputTypeDef",
    "SetSecurityGroupsOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "CreateTrustStoreInputRequestTypeDef",
    "TagDescriptionTypeDef",
    "AddTrustStoreRevocationsInputRequestTypeDef",
    "AddTrustStoreRevocationsOutputTypeDef",
    "AuthenticateCognitoActionConfigUnionTypeDef",
    "AuthenticateOidcActionConfigUnionTypeDef",
    "AvailabilityZoneTypeDef",
    "SslPolicyTypeDef",
    "CreateLoadBalancerInputRequestTypeDef",
    "SetSubnetsInputRequestTypeDef",
    "CreateTargetGroupInputRequestTypeDef",
    "ModifyTargetGroupInputRequestTypeDef",
    "TargetGroupTypeDef",
    "CreateTrustStoreOutputTypeDef",
    "DescribeTrustStoresOutputTypeDef",
    "ModifyTrustStoreOutputTypeDef",
    "DeregisterTargetsInputRequestTypeDef",
    "DescribeTargetHealthInputRequestTypeDef",
    "RegisterTargetsInputRequestTypeDef",
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    "DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef",
    "DescribeListenersInputDescribeListenersPaginateTypeDef",
    "DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef",
    "DescribeRulesInputDescribeRulesPaginateTypeDef",
    "DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef",
    "DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeListenerAttributesOutputTypeDef",
    "ModifyListenerAttributesInputRequestTypeDef",
    "ModifyListenerAttributesOutputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef",
    "DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef",
    "DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef",
    "DescribeTargetHealthInputTargetDeregisteredWaitTypeDef",
    "DescribeTargetHealthInputTargetInServiceWaitTypeDef",
    "DescribeTargetGroupAttributesOutputTypeDef",
    "ModifyTargetGroupAttributesInputRequestTypeDef",
    "ModifyTargetGroupAttributesOutputTypeDef",
    "DescribeTrustStoreAssociationsOutputTypeDef",
    "DescribeTrustStoreRevocationsOutputTypeDef",
    "ForwardActionConfigOutputTypeDef",
    "ForwardActionConfigTypeDef",
    "HostHeaderConditionConfigUnionTypeDef",
    "HttpHeaderConditionConfigUnionTypeDef",
    "HttpRequestMethodConditionConfigUnionTypeDef",
    "PathPatternConditionConfigUnionTypeDef",
    "QueryStringConditionConfigOutputTypeDef",
    "QueryStringConditionConfigTypeDef",
    "SetRulePrioritiesInputRequestTypeDef",
    "SourceIpConditionConfigUnionTypeDef",
    "TargetHealthDescriptionTypeDef",
    "DescribeTagsOutputTypeDef",
    "LoadBalancerTypeDef",
    "SetSubnetsOutputTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "CreateTargetGroupOutputTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "ModifyTargetGroupOutputTypeDef",
    "ActionOutputTypeDef",
    "ForwardActionConfigUnionTypeDef",
    "RuleConditionOutputTypeDef",
    "QueryStringConditionConfigUnionTypeDef",
    "DescribeTargetHealthOutputTypeDef",
    "CreateLoadBalancerOutputTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "ListenerTypeDef",
    "ActionTypeDef",
    "RuleTypeDef",
    "RuleConditionTypeDef",
    "CreateListenerOutputTypeDef",
    "DescribeListenersOutputTypeDef",
    "ModifyListenerOutputTypeDef",
    "ActionUnionTypeDef",
    "ModifyListenerInputRequestTypeDef",
    "CreateRuleOutputTypeDef",
    "DescribeRulesOutputTypeDef",
    "ModifyRuleOutputTypeDef",
    "SetRulePrioritiesOutputTypeDef",
    "ModifyRuleInputRequestTypeDef",
    "RuleConditionUnionTypeDef",
    "CreateListenerInputRequestTypeDef",
    "CreateRuleInputRequestTypeDef",
)

AuthenticateCognitoActionConfigOutputTypeDef = TypedDict(
    "AuthenticateCognitoActionConfigOutputTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": NotRequired[str],
        "Scope": NotRequired[str],
        "SessionTimeout": NotRequired[int],
        "AuthenticationRequestExtraParams": NotRequired[Dict[str, str]],
        "OnUnauthenticatedRequest": NotRequired[
            AuthenticateCognitoActionConditionalBehaviorEnumType
        ],
    },
)
AuthenticateOidcActionConfigOutputTypeDef = TypedDict(
    "AuthenticateOidcActionConfigOutputTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": NotRequired[str],
        "SessionCookieName": NotRequired[str],
        "Scope": NotRequired[str],
        "SessionTimeout": NotRequired[int],
        "AuthenticationRequestExtraParams": NotRequired[Dict[str, str]],
        "OnUnauthenticatedRequest": NotRequired[AuthenticateOidcActionConditionalBehaviorEnumType],
        "UseExistingClientSecret": NotRequired[bool],
    },
)
FixedResponseActionConfigTypeDef = TypedDict(
    "FixedResponseActionConfigTypeDef",
    {
        "StatusCode": str,
        "MessageBody": NotRequired[str],
        "ContentType": NotRequired[str],
    },
)
RedirectActionConfigTypeDef = TypedDict(
    "RedirectActionConfigTypeDef",
    {
        "StatusCode": RedirectActionStatusCodeEnumType,
        "Protocol": NotRequired[str],
        "Port": NotRequired[str],
        "Host": NotRequired[str],
        "Path": NotRequired[str],
        "Query": NotRequired[str],
    },
)
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "IsDefault": NotRequired[bool],
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
        "Key": str,
        "Value": NotRequired[str],
    },
)
RevocationContentTypeDef = TypedDict(
    "RevocationContentTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3ObjectVersion": NotRequired[str],
        "RevocationType": NotRequired[Literal["CRL"]],
    },
)
TrustStoreRevocationTypeDef = TypedDict(
    "TrustStoreRevocationTypeDef",
    {
        "TrustStoreArn": NotRequired[str],
        "RevocationId": NotRequired[int],
        "RevocationType": NotRequired[Literal["CRL"]],
        "NumberOfRevokedEntries": NotRequired[int],
    },
)
AdministrativeOverrideTypeDef = TypedDict(
    "AdministrativeOverrideTypeDef",
    {
        "State": NotRequired[TargetAdministrativeOverrideStateEnumType],
        "Reason": NotRequired[TargetAdministrativeOverrideReasonEnumType],
        "Description": NotRequired[str],
    },
)
AnomalyDetectionTypeDef = TypedDict(
    "AnomalyDetectionTypeDef",
    {
        "Result": NotRequired[AnomalyResultEnumType],
        "MitigationInEffect": NotRequired[MitigationInEffectEnumType],
    },
)
AuthenticateCognitoActionConfigTypeDef = TypedDict(
    "AuthenticateCognitoActionConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": NotRequired[str],
        "Scope": NotRequired[str],
        "SessionTimeout": NotRequired[int],
        "AuthenticationRequestExtraParams": NotRequired[Mapping[str, str]],
        "OnUnauthenticatedRequest": NotRequired[
            AuthenticateCognitoActionConditionalBehaviorEnumType
        ],
    },
)
AuthenticateOidcActionConfigTypeDef = TypedDict(
    "AuthenticateOidcActionConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": NotRequired[str],
        "SessionCookieName": NotRequired[str],
        "Scope": NotRequired[str],
        "SessionTimeout": NotRequired[int],
        "AuthenticationRequestExtraParams": NotRequired[Mapping[str, str]],
        "OnUnauthenticatedRequest": NotRequired[AuthenticateOidcActionConditionalBehaviorEnumType],
        "UseExistingClientSecret": NotRequired[bool],
    },
)
LoadBalancerAddressTypeDef = TypedDict(
    "LoadBalancerAddressTypeDef",
    {
        "IpAddress": NotRequired[str],
        "AllocationId": NotRequired[str],
        "PrivateIPv4Address": NotRequired[str],
        "IPv6Address": NotRequired[str],
    },
)
CipherTypeDef = TypedDict(
    "CipherTypeDef",
    {
        "Name": NotRequired[str],
        "Priority": NotRequired[int],
    },
)
MutualAuthenticationAttributesTypeDef = TypedDict(
    "MutualAuthenticationAttributesTypeDef",
    {
        "Mode": NotRequired[str],
        "TrustStoreArn": NotRequired[str],
        "IgnoreClientCertificateExpiry": NotRequired[bool],
        "TrustStoreAssociationStatus": NotRequired[TrustStoreAssociationStatusEnumType],
    },
)
SubnetMappingTypeDef = TypedDict(
    "SubnetMappingTypeDef",
    {
        "SubnetId": NotRequired[str],
        "AllocationId": NotRequired[str],
        "PrivateIPv4Address": NotRequired[str],
        "IPv6Address": NotRequired[str],
    },
)
MatcherTypeDef = TypedDict(
    "MatcherTypeDef",
    {
        "HttpCode": NotRequired[str],
        "GrpcCode": NotRequired[str],
    },
)
TrustStoreTypeDef = TypedDict(
    "TrustStoreTypeDef",
    {
        "Name": NotRequired[str],
        "TrustStoreArn": NotRequired[str],
        "Status": NotRequired[TrustStoreStatusType],
        "NumberOfCaCertificates": NotRequired[int],
        "TotalRevokedEntries": NotRequired[int],
    },
)
DeleteListenerInputRequestTypeDef = TypedDict(
    "DeleteListenerInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
DeleteLoadBalancerInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)
DeleteRuleInputRequestTypeDef = TypedDict(
    "DeleteRuleInputRequestTypeDef",
    {
        "RuleArn": str,
    },
)
DeleteSharedTrustStoreAssociationInputRequestTypeDef = TypedDict(
    "DeleteSharedTrustStoreAssociationInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "ResourceArn": str,
    },
)
DeleteTargetGroupInputRequestTypeDef = TypedDict(
    "DeleteTargetGroupInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)
DeleteTrustStoreInputRequestTypeDef = TypedDict(
    "DeleteTrustStoreInputRequestTypeDef",
    {
        "TrustStoreArn": str,
    },
)
TargetDescriptionTypeDef = TypedDict(
    "TargetDescriptionTypeDef",
    {
        "Id": str,
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
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
DescribeAccountLimitsInputRequestTypeDef = TypedDict(
    "DescribeAccountLimitsInputRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Name": NotRequired[str],
        "Max": NotRequired[str],
    },
)
DescribeListenerAttributesInputRequestTypeDef = TypedDict(
    "DescribeListenerAttributesInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
ListenerAttributeTypeDef = TypedDict(
    "ListenerAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
DescribeListenerCertificatesInputRequestTypeDef = TypedDict(
    "DescribeListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
DescribeListenersInputRequestTypeDef = TypedDict(
    "DescribeListenersInputRequestTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "ListenerArns": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
DescribeLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)
LoadBalancerAttributeTypeDef = TypedDict(
    "LoadBalancerAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeLoadBalancersInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancersInputRequestTypeDef",
    {
        "LoadBalancerArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
DescribeRulesInputRequestTypeDef = TypedDict(
    "DescribeRulesInputRequestTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "RuleArns": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
DescribeSSLPoliciesInputRequestTypeDef = TypedDict(
    "DescribeSSLPoliciesInputRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
        "LoadBalancerType": NotRequired[LoadBalancerTypeEnumType],
    },
)
DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
    },
)
DescribeTargetGroupAttributesInputRequestTypeDef = TypedDict(
    "DescribeTargetGroupAttributesInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)
TargetGroupAttributeTypeDef = TypedDict(
    "TargetGroupAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
DescribeTargetGroupsInputRequestTypeDef = TypedDict(
    "DescribeTargetGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "TargetGroupArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
DescribeTrustStoreAssociationsInputRequestTypeDef = TypedDict(
    "DescribeTrustStoreAssociationsInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
TrustStoreAssociationTypeDef = TypedDict(
    "TrustStoreAssociationTypeDef",
    {
        "ResourceArn": NotRequired[str],
    },
)
DescribeTrustStoreRevocationTypeDef = TypedDict(
    "DescribeTrustStoreRevocationTypeDef",
    {
        "TrustStoreArn": NotRequired[str],
        "RevocationId": NotRequired[int],
        "RevocationType": NotRequired[Literal["CRL"]],
        "NumberOfRevokedEntries": NotRequired[int],
    },
)
DescribeTrustStoreRevocationsInputRequestTypeDef = TypedDict(
    "DescribeTrustStoreRevocationsInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "RevocationIds": NotRequired[Sequence[int]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
DescribeTrustStoresInputRequestTypeDef = TypedDict(
    "DescribeTrustStoresInputRequestTypeDef",
    {
        "TrustStoreArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
TargetGroupStickinessConfigTypeDef = TypedDict(
    "TargetGroupStickinessConfigTypeDef",
    {
        "Enabled": NotRequired[bool],
        "DurationSeconds": NotRequired[int],
    },
)
TargetGroupTupleTypeDef = TypedDict(
    "TargetGroupTupleTypeDef",
    {
        "TargetGroupArn": NotRequired[str],
        "Weight": NotRequired[int],
    },
)
GetResourcePolicyInputRequestTypeDef = TypedDict(
    "GetResourcePolicyInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetTrustStoreCaCertificatesBundleInputRequestTypeDef = TypedDict(
    "GetTrustStoreCaCertificatesBundleInputRequestTypeDef",
    {
        "TrustStoreArn": str,
    },
)
GetTrustStoreRevocationContentInputRequestTypeDef = TypedDict(
    "GetTrustStoreRevocationContentInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "RevocationId": int,
    },
)
HostHeaderConditionConfigOutputTypeDef = TypedDict(
    "HostHeaderConditionConfigOutputTypeDef",
    {
        "Values": NotRequired[List[str]],
    },
)
HostHeaderConditionConfigTypeDef = TypedDict(
    "HostHeaderConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)
HttpHeaderConditionConfigOutputTypeDef = TypedDict(
    "HttpHeaderConditionConfigOutputTypeDef",
    {
        "HttpHeaderName": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)
HttpHeaderConditionConfigTypeDef = TypedDict(
    "HttpHeaderConditionConfigTypeDef",
    {
        "HttpHeaderName": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
HttpRequestMethodConditionConfigOutputTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigOutputTypeDef",
    {
        "Values": NotRequired[List[str]],
    },
)
HttpRequestMethodConditionConfigTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)
LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": NotRequired[LoadBalancerStateEnumType],
        "Reason": NotRequired[str],
    },
)
ModifyTrustStoreInputRequestTypeDef = TypedDict(
    "ModifyTrustStoreInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "CaCertificatesBundleS3Bucket": str,
        "CaCertificatesBundleS3Key": str,
        "CaCertificatesBundleS3ObjectVersion": NotRequired[str],
    },
)
PathPatternConditionConfigOutputTypeDef = TypedDict(
    "PathPatternConditionConfigOutputTypeDef",
    {
        "Values": NotRequired[List[str]],
    },
)
PathPatternConditionConfigTypeDef = TypedDict(
    "PathPatternConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)
QueryStringKeyValuePairTypeDef = TypedDict(
    "QueryStringKeyValuePairTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
        "TagKeys": Sequence[str],
    },
)
RemoveTrustStoreRevocationsInputRequestTypeDef = TypedDict(
    "RemoveTrustStoreRevocationsInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "RevocationIds": Sequence[int],
    },
)
SourceIpConditionConfigOutputTypeDef = TypedDict(
    "SourceIpConditionConfigOutputTypeDef",
    {
        "Values": NotRequired[List[str]],
    },
)
RulePriorityPairTypeDef = TypedDict(
    "RulePriorityPairTypeDef",
    {
        "RuleArn": NotRequired[str],
        "Priority": NotRequired[int],
    },
)
SetIpAddressTypeInputRequestTypeDef = TypedDict(
    "SetIpAddressTypeInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "IpAddressType": IpAddressTypeType,
    },
)
SetSecurityGroupsInputRequestTypeDef = TypedDict(
    "SetSecurityGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "SecurityGroups": Sequence[str],
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic": NotRequired[
            EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType
        ],
    },
)
SourceIpConditionConfigTypeDef = TypedDict(
    "SourceIpConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)
TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": NotRequired[TargetHealthStateEnumType],
        "Reason": NotRequired[TargetHealthReasonEnumType],
        "Description": NotRequired[str],
    },
)
AddListenerCertificatesInputRequestTypeDef = TypedDict(
    "AddListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Certificates": Sequence[CertificateTypeDef],
    },
)
RemoveListenerCertificatesInputRequestTypeDef = TypedDict(
    "RemoveListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Certificates": Sequence[CertificateTypeDef],
    },
)
AddListenerCertificatesOutputTypeDef = TypedDict(
    "AddListenerCertificatesOutputTypeDef",
    {
        "Certificates": List[CertificateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeListenerCertificatesOutputTypeDef = TypedDict(
    "DescribeListenerCertificatesOutputTypeDef",
    {
        "Certificates": List[CertificateTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyOutputTypeDef = TypedDict(
    "GetResourcePolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrustStoreCaCertificatesBundleOutputTypeDef = TypedDict(
    "GetTrustStoreCaCertificatesBundleOutputTypeDef",
    {
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrustStoreRevocationContentOutputTypeDef = TypedDict(
    "GetTrustStoreRevocationContentOutputTypeDef",
    {
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetIpAddressTypeOutputTypeDef = TypedDict(
    "SetIpAddressTypeOutputTypeDef",
    {
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetSecurityGroupsOutputTypeDef = TypedDict(
    "SetSecurityGroupsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic": EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
CreateTrustStoreInputRequestTypeDef = TypedDict(
    "CreateTrustStoreInputRequestTypeDef",
    {
        "Name": str,
        "CaCertificatesBundleS3Bucket": str,
        "CaCertificatesBundleS3Key": str,
        "CaCertificatesBundleS3ObjectVersion": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
AddTrustStoreRevocationsInputRequestTypeDef = TypedDict(
    "AddTrustStoreRevocationsInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "RevocationContents": NotRequired[Sequence[RevocationContentTypeDef]],
    },
)
AddTrustStoreRevocationsOutputTypeDef = TypedDict(
    "AddTrustStoreRevocationsOutputTypeDef",
    {
        "TrustStoreRevocations": List[TrustStoreRevocationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthenticateCognitoActionConfigUnionTypeDef = Union[
    AuthenticateCognitoActionConfigTypeDef, AuthenticateCognitoActionConfigOutputTypeDef
]
AuthenticateOidcActionConfigUnionTypeDef = Union[
    AuthenticateOidcActionConfigTypeDef, AuthenticateOidcActionConfigOutputTypeDef
]
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": NotRequired[str],
        "SubnetId": NotRequired[str],
        "OutpostId": NotRequired[str],
        "LoadBalancerAddresses": NotRequired[List[LoadBalancerAddressTypeDef]],
    },
)
SslPolicyTypeDef = TypedDict(
    "SslPolicyTypeDef",
    {
        "SslProtocols": NotRequired[List[str]],
        "Ciphers": NotRequired[List[CipherTypeDef]],
        "Name": NotRequired[str],
        "SupportedLoadBalancerTypes": NotRequired[List[str]],
    },
)
CreateLoadBalancerInputRequestTypeDef = TypedDict(
    "CreateLoadBalancerInputRequestTypeDef",
    {
        "Name": str,
        "Subnets": NotRequired[Sequence[str]],
        "SubnetMappings": NotRequired[Sequence[SubnetMappingTypeDef]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Scheme": NotRequired[LoadBalancerSchemeEnumType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Type": NotRequired[LoadBalancerTypeEnumType],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "CustomerOwnedIpv4Pool": NotRequired[str],
    },
)
SetSubnetsInputRequestTypeDef = TypedDict(
    "SetSubnetsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "Subnets": NotRequired[Sequence[str]],
        "SubnetMappings": NotRequired[Sequence[SubnetMappingTypeDef]],
        "IpAddressType": NotRequired[IpAddressTypeType],
    },
)
CreateTargetGroupInputRequestTypeDef = TypedDict(
    "CreateTargetGroupInputRequestTypeDef",
    {
        "Name": str,
        "Protocol": NotRequired[ProtocolEnumType],
        "ProtocolVersion": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "HealthCheckProtocol": NotRequired[ProtocolEnumType],
        "HealthCheckPort": NotRequired[str],
        "HealthCheckEnabled": NotRequired[bool],
        "HealthCheckPath": NotRequired[str],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "HealthCheckTimeoutSeconds": NotRequired[int],
        "HealthyThresholdCount": NotRequired[int],
        "UnhealthyThresholdCount": NotRequired[int],
        "Matcher": NotRequired[MatcherTypeDef],
        "TargetType": NotRequired[TargetTypeEnumType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "IpAddressType": NotRequired[TargetGroupIpAddressTypeEnumType],
    },
)
ModifyTargetGroupInputRequestTypeDef = TypedDict(
    "ModifyTargetGroupInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "HealthCheckProtocol": NotRequired[ProtocolEnumType],
        "HealthCheckPort": NotRequired[str],
        "HealthCheckPath": NotRequired[str],
        "HealthCheckEnabled": NotRequired[bool],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "HealthCheckTimeoutSeconds": NotRequired[int],
        "HealthyThresholdCount": NotRequired[int],
        "UnhealthyThresholdCount": NotRequired[int],
        "Matcher": NotRequired[MatcherTypeDef],
    },
)
TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": NotRequired[str],
        "TargetGroupName": NotRequired[str],
        "Protocol": NotRequired[ProtocolEnumType],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "HealthCheckProtocol": NotRequired[ProtocolEnumType],
        "HealthCheckPort": NotRequired[str],
        "HealthCheckEnabled": NotRequired[bool],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "HealthCheckTimeoutSeconds": NotRequired[int],
        "HealthyThresholdCount": NotRequired[int],
        "UnhealthyThresholdCount": NotRequired[int],
        "HealthCheckPath": NotRequired[str],
        "Matcher": NotRequired[MatcherTypeDef],
        "LoadBalancerArns": NotRequired[List[str]],
        "TargetType": NotRequired[TargetTypeEnumType],
        "ProtocolVersion": NotRequired[str],
        "IpAddressType": NotRequired[TargetGroupIpAddressTypeEnumType],
    },
)
CreateTrustStoreOutputTypeDef = TypedDict(
    "CreateTrustStoreOutputTypeDef",
    {
        "TrustStores": List[TrustStoreTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrustStoresOutputTypeDef = TypedDict(
    "DescribeTrustStoresOutputTypeDef",
    {
        "TrustStores": List[TrustStoreTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTrustStoreOutputTypeDef = TypedDict(
    "ModifyTrustStoreOutputTypeDef",
    {
        "TrustStores": List[TrustStoreTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterTargetsInputRequestTypeDef = TypedDict(
    "DeregisterTargetsInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": Sequence[TargetDescriptionTypeDef],
    },
)
DescribeTargetHealthInputRequestTypeDef = TypedDict(
    "DescribeTargetHealthInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": NotRequired[Sequence[TargetDescriptionTypeDef]],
        "Include": NotRequired[Sequence[DescribeTargetHealthInputIncludeEnumType]],
    },
)
RegisterTargetsInputRequestTypeDef = TypedDict(
    "RegisterTargetsInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": Sequence[TargetDescriptionTypeDef],
    },
)
DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef = TypedDict(
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef = TypedDict(
    "DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef",
    {
        "ListenerArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeListenersInputDescribeListenersPaginateTypeDef = TypedDict(
    "DescribeListenersInputDescribeListenersPaginateTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "ListenerArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef = TypedDict(
    "DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef",
    {
        "LoadBalancerArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRulesInputDescribeRulesPaginateTypeDef = TypedDict(
    "DescribeRulesInputDescribeRulesPaginateTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "RuleArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef = TypedDict(
    "DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "LoadBalancerType": NotRequired[LoadBalancerTypeEnumType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef = TypedDict(
    "DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "TargetGroupArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "Limits": List[LimitTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeListenerAttributesOutputTypeDef = TypedDict(
    "DescribeListenerAttributesOutputTypeDef",
    {
        "Attributes": List[ListenerAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyListenerAttributesInputRequestTypeDef = TypedDict(
    "ModifyListenerAttributesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Attributes": Sequence[ListenerAttributeTypeDef],
    },
)
ModifyListenerAttributesOutputTypeDef = TypedDict(
    "ModifyListenerAttributesOutputTypeDef",
    {
        "Attributes": List[ListenerAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List[LoadBalancerAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "Attributes": Sequence[LoadBalancerAttributeTypeDef],
    },
)
ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List[LoadBalancerAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef = TypedDict(
    "DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef",
    {
        "LoadBalancerArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef = TypedDict(
    "DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef",
    {
        "LoadBalancerArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef = TypedDict(
    "DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef",
    {
        "LoadBalancerArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeTargetHealthInputTargetDeregisteredWaitTypeDef = TypedDict(
    "DescribeTargetHealthInputTargetDeregisteredWaitTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": NotRequired[Sequence[TargetDescriptionTypeDef]],
        "Include": NotRequired[Sequence[DescribeTargetHealthInputIncludeEnumType]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeTargetHealthInputTargetInServiceWaitTypeDef = TypedDict(
    "DescribeTargetHealthInputTargetInServiceWaitTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": NotRequired[Sequence[TargetDescriptionTypeDef]],
        "Include": NotRequired[Sequence[DescribeTargetHealthInputIncludeEnumType]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeTargetGroupAttributesOutputTypeDef = TypedDict(
    "DescribeTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List[TargetGroupAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTargetGroupAttributesInputRequestTypeDef = TypedDict(
    "ModifyTargetGroupAttributesInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Attributes": Sequence[TargetGroupAttributeTypeDef],
    },
)
ModifyTargetGroupAttributesOutputTypeDef = TypedDict(
    "ModifyTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List[TargetGroupAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrustStoreAssociationsOutputTypeDef = TypedDict(
    "DescribeTrustStoreAssociationsOutputTypeDef",
    {
        "TrustStoreAssociations": List[TrustStoreAssociationTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrustStoreRevocationsOutputTypeDef = TypedDict(
    "DescribeTrustStoreRevocationsOutputTypeDef",
    {
        "TrustStoreRevocations": List[DescribeTrustStoreRevocationTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ForwardActionConfigOutputTypeDef = TypedDict(
    "ForwardActionConfigOutputTypeDef",
    {
        "TargetGroups": NotRequired[List[TargetGroupTupleTypeDef]],
        "TargetGroupStickinessConfig": NotRequired[TargetGroupStickinessConfigTypeDef],
    },
)
ForwardActionConfigTypeDef = TypedDict(
    "ForwardActionConfigTypeDef",
    {
        "TargetGroups": NotRequired[Sequence[TargetGroupTupleTypeDef]],
        "TargetGroupStickinessConfig": NotRequired[TargetGroupStickinessConfigTypeDef],
    },
)
HostHeaderConditionConfigUnionTypeDef = Union[
    HostHeaderConditionConfigTypeDef, HostHeaderConditionConfigOutputTypeDef
]
HttpHeaderConditionConfigUnionTypeDef = Union[
    HttpHeaderConditionConfigTypeDef, HttpHeaderConditionConfigOutputTypeDef
]
HttpRequestMethodConditionConfigUnionTypeDef = Union[
    HttpRequestMethodConditionConfigTypeDef, HttpRequestMethodConditionConfigOutputTypeDef
]
PathPatternConditionConfigUnionTypeDef = Union[
    PathPatternConditionConfigTypeDef, PathPatternConditionConfigOutputTypeDef
]
QueryStringConditionConfigOutputTypeDef = TypedDict(
    "QueryStringConditionConfigOutputTypeDef",
    {
        "Values": NotRequired[List[QueryStringKeyValuePairTypeDef]],
    },
)
QueryStringConditionConfigTypeDef = TypedDict(
    "QueryStringConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[QueryStringKeyValuePairTypeDef]],
    },
)
SetRulePrioritiesInputRequestTypeDef = TypedDict(
    "SetRulePrioritiesInputRequestTypeDef",
    {
        "RulePriorities": Sequence[RulePriorityPairTypeDef],
    },
)
SourceIpConditionConfigUnionTypeDef = Union[
    SourceIpConditionConfigTypeDef, SourceIpConditionConfigOutputTypeDef
]
TargetHealthDescriptionTypeDef = TypedDict(
    "TargetHealthDescriptionTypeDef",
    {
        "Target": NotRequired[TargetDescriptionTypeDef],
        "HealthCheckPort": NotRequired[str],
        "TargetHealth": NotRequired[TargetHealthTypeDef],
        "AnomalyDetection": NotRequired[AnomalyDetectionTypeDef],
        "AdministrativeOverride": NotRequired[AdministrativeOverrideTypeDef],
    },
)
DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "TagDescriptions": List[TagDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "DNSName": NotRequired[str],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LoadBalancerName": NotRequired[str],
        "Scheme": NotRequired[LoadBalancerSchemeEnumType],
        "VpcId": NotRequired[str],
        "State": NotRequired[LoadBalancerStateTypeDef],
        "Type": NotRequired[LoadBalancerTypeEnumType],
        "AvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "SecurityGroups": NotRequired[List[str]],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic": NotRequired[str],
    },
)
SetSubnetsOutputTypeDef = TypedDict(
    "SetSubnetsOutputTypeDef",
    {
        "AvailabilityZones": List[AvailabilityZoneTypeDef],
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSSLPoliciesOutputTypeDef = TypedDict(
    "DescribeSSLPoliciesOutputTypeDef",
    {
        "SslPolicies": List[SslPolicyTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTargetGroupOutputTypeDef = TypedDict(
    "CreateTargetGroupOutputTypeDef",
    {
        "TargetGroups": List[TargetGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTargetGroupsOutputTypeDef = TypedDict(
    "DescribeTargetGroupsOutputTypeDef",
    {
        "TargetGroups": List[TargetGroupTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyTargetGroupOutputTypeDef = TypedDict(
    "ModifyTargetGroupOutputTypeDef",
    {
        "TargetGroups": List[TargetGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "Type": ActionTypeEnumType,
        "TargetGroupArn": NotRequired[str],
        "AuthenticateOidcConfig": NotRequired[AuthenticateOidcActionConfigOutputTypeDef],
        "AuthenticateCognitoConfig": NotRequired[AuthenticateCognitoActionConfigOutputTypeDef],
        "Order": NotRequired[int],
        "RedirectConfig": NotRequired[RedirectActionConfigTypeDef],
        "FixedResponseConfig": NotRequired[FixedResponseActionConfigTypeDef],
        "ForwardConfig": NotRequired[ForwardActionConfigOutputTypeDef],
    },
)
ForwardActionConfigUnionTypeDef = Union[
    ForwardActionConfigTypeDef, ForwardActionConfigOutputTypeDef
]
RuleConditionOutputTypeDef = TypedDict(
    "RuleConditionOutputTypeDef",
    {
        "Field": NotRequired[str],
        "Values": NotRequired[List[str]],
        "HostHeaderConfig": NotRequired[HostHeaderConditionConfigOutputTypeDef],
        "PathPatternConfig": NotRequired[PathPatternConditionConfigOutputTypeDef],
        "HttpHeaderConfig": NotRequired[HttpHeaderConditionConfigOutputTypeDef],
        "QueryStringConfig": NotRequired[QueryStringConditionConfigOutputTypeDef],
        "HttpRequestMethodConfig": NotRequired[HttpRequestMethodConditionConfigOutputTypeDef],
        "SourceIpConfig": NotRequired[SourceIpConditionConfigOutputTypeDef],
    },
)
QueryStringConditionConfigUnionTypeDef = Union[
    QueryStringConditionConfigTypeDef, QueryStringConditionConfigOutputTypeDef
]
DescribeTargetHealthOutputTypeDef = TypedDict(
    "DescribeTargetHealthOutputTypeDef",
    {
        "TargetHealthDescriptions": List[TargetHealthDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLoadBalancerOutputTypeDef = TypedDict(
    "CreateLoadBalancerOutputTypeDef",
    {
        "LoadBalancers": List[LoadBalancerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLoadBalancersOutputTypeDef = TypedDict(
    "DescribeLoadBalancersOutputTypeDef",
    {
        "LoadBalancers": List[LoadBalancerTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "LoadBalancerArn": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolEnumType],
        "Certificates": NotRequired[List[CertificateTypeDef]],
        "SslPolicy": NotRequired[str],
        "DefaultActions": NotRequired[List[ActionOutputTypeDef]],
        "AlpnPolicy": NotRequired[List[str]],
        "MutualAuthentication": NotRequired[MutualAuthenticationAttributesTypeDef],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "Type": ActionTypeEnumType,
        "TargetGroupArn": NotRequired[str],
        "AuthenticateOidcConfig": NotRequired[AuthenticateOidcActionConfigUnionTypeDef],
        "AuthenticateCognitoConfig": NotRequired[AuthenticateCognitoActionConfigUnionTypeDef],
        "Order": NotRequired[int],
        "RedirectConfig": NotRequired[RedirectActionConfigTypeDef],
        "FixedResponseConfig": NotRequired[FixedResponseActionConfigTypeDef],
        "ForwardConfig": NotRequired[ForwardActionConfigUnionTypeDef],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "RuleArn": NotRequired[str],
        "Priority": NotRequired[str],
        "Conditions": NotRequired[List[RuleConditionOutputTypeDef]],
        "Actions": NotRequired[List[ActionOutputTypeDef]],
        "IsDefault": NotRequired[bool],
    },
)
RuleConditionTypeDef = TypedDict(
    "RuleConditionTypeDef",
    {
        "Field": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "HostHeaderConfig": NotRequired[HostHeaderConditionConfigUnionTypeDef],
        "PathPatternConfig": NotRequired[PathPatternConditionConfigUnionTypeDef],
        "HttpHeaderConfig": NotRequired[HttpHeaderConditionConfigUnionTypeDef],
        "QueryStringConfig": NotRequired[QueryStringConditionConfigUnionTypeDef],
        "HttpRequestMethodConfig": NotRequired[HttpRequestMethodConditionConfigUnionTypeDef],
        "SourceIpConfig": NotRequired[SourceIpConditionConfigUnionTypeDef],
    },
)
CreateListenerOutputTypeDef = TypedDict(
    "CreateListenerOutputTypeDef",
    {
        "Listeners": List[ListenerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeListenersOutputTypeDef = TypedDict(
    "DescribeListenersOutputTypeDef",
    {
        "Listeners": List[ListenerTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyListenerOutputTypeDef = TypedDict(
    "ModifyListenerOutputTypeDef",
    {
        "Listeners": List[ListenerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActionUnionTypeDef = Union[ActionTypeDef, ActionOutputTypeDef]
ModifyListenerInputRequestTypeDef = TypedDict(
    "ModifyListenerInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolEnumType],
        "SslPolicy": NotRequired[str],
        "Certificates": NotRequired[Sequence[CertificateTypeDef]],
        "DefaultActions": NotRequired[Sequence[ActionTypeDef]],
        "AlpnPolicy": NotRequired[Sequence[str]],
        "MutualAuthentication": NotRequired[MutualAuthenticationAttributesTypeDef],
    },
)
CreateRuleOutputTypeDef = TypedDict(
    "CreateRuleOutputTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRulesOutputTypeDef = TypedDict(
    "DescribeRulesOutputTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyRuleOutputTypeDef = TypedDict(
    "ModifyRuleOutputTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetRulePrioritiesOutputTypeDef = TypedDict(
    "SetRulePrioritiesOutputTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyRuleInputRequestTypeDef = TypedDict(
    "ModifyRuleInputRequestTypeDef",
    {
        "RuleArn": str,
        "Conditions": NotRequired[Sequence[RuleConditionTypeDef]],
        "Actions": NotRequired[Sequence[ActionTypeDef]],
    },
)
RuleConditionUnionTypeDef = Union[RuleConditionTypeDef, RuleConditionOutputTypeDef]
CreateListenerInputRequestTypeDef = TypedDict(
    "CreateListenerInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "DefaultActions": Sequence[ActionUnionTypeDef],
        "Protocol": NotRequired[ProtocolEnumType],
        "Port": NotRequired[int],
        "SslPolicy": NotRequired[str],
        "Certificates": NotRequired[Sequence[CertificateTypeDef]],
        "AlpnPolicy": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "MutualAuthentication": NotRequired[MutualAuthenticationAttributesTypeDef],
    },
)
CreateRuleInputRequestTypeDef = TypedDict(
    "CreateRuleInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Conditions": Sequence[RuleConditionUnionTypeDef],
        "Priority": int,
        "Actions": Sequence[ActionTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
