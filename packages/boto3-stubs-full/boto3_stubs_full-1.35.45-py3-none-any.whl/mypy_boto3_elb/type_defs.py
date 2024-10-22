"""
Type annotations for elb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/type_defs/)

Usage::

    ```python
    from mypy_boto3_elb.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AccessLogTypeDef",
    "AddAvailabilityZonesInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "AdditionalAttributeTypeDef",
    "AppCookieStickinessPolicyTypeDef",
    "ApplySecurityGroupsToLoadBalancerInputRequestTypeDef",
    "AttachLoadBalancerToSubnetsInputRequestTypeDef",
    "BackendServerDescriptionTypeDef",
    "HealthCheckTypeDef",
    "ConnectionDrainingTypeDef",
    "ConnectionSettingsTypeDef",
    "ListenerTypeDef",
    "CreateAppCookieStickinessPolicyInputRequestTypeDef",
    "CreateLBCookieStickinessPolicyInputRequestTypeDef",
    "PolicyAttributeTypeDef",
    "CrossZoneLoadBalancingTypeDef",
    "DeleteAccessPointInputRequestTypeDef",
    "DeleteLoadBalancerListenerInputRequestTypeDef",
    "DeleteLoadBalancerPolicyInputRequestTypeDef",
    "InstanceTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAccessPointsInputRequestTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "LimitTypeDef",
    "WaiterConfigTypeDef",
    "InstanceStateTypeDef",
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    "DescribeLoadBalancerPoliciesInputRequestTypeDef",
    "DescribeLoadBalancerPolicyTypesInputRequestTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DetachLoadBalancerFromSubnetsInputRequestTypeDef",
    "LBCookieStickinessPolicyTypeDef",
    "SourceSecurityGroupTypeDef",
    "PolicyAttributeDescriptionTypeDef",
    "PolicyAttributeTypeDescriptionTypeDef",
    "RemoveAvailabilityZonesInputRequestTypeDef",
    "TagKeyOnlyTypeDef",
    "SetLoadBalancerListenerSSLCertificateInputRequestTypeDef",
    "SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef",
    "SetLoadBalancerPoliciesOfListenerInputRequestTypeDef",
    "AddAvailabilityZonesOutputTypeDef",
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    "CreateAccessPointOutputTypeDef",
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    "RemoveAvailabilityZonesOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "TagDescriptionTypeDef",
    "ConfigureHealthCheckInputRequestTypeDef",
    "ConfigureHealthCheckOutputTypeDef",
    "CreateAccessPointInputRequestTypeDef",
    "CreateLoadBalancerListenerInputRequestTypeDef",
    "ListenerDescriptionTypeDef",
    "CreateLoadBalancerPolicyInputRequestTypeDef",
    "LoadBalancerAttributesOutputTypeDef",
    "LoadBalancerAttributesTypeDef",
    "DeregisterEndPointsInputRequestTypeDef",
    "DeregisterEndPointsOutputTypeDef",
    "DescribeEndPointStateInputRequestTypeDef",
    "RegisterEndPointsInputRequestTypeDef",
    "RegisterEndPointsOutputTypeDef",
    "DescribeAccessPointsInputDescribeLoadBalancersPaginateTypeDef",
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef",
    "DescribeEndPointStateInputInstanceDeregisteredWaitTypeDef",
    "DescribeEndPointStateInputInstanceInServiceWaitTypeDef",
    "DescribeEndPointStateOutputTypeDef",
    "PoliciesTypeDef",
    "PolicyDescriptionTypeDef",
    "PolicyTypeDescriptionTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    "DescribeAccessPointsOutputTypeDef",
)

AccessLogTypeDef = TypedDict(
    "AccessLogTypeDef",
    {
        "Enabled": bool,
        "S3BucketName": NotRequired[str],
        "EmitInterval": NotRequired[int],
        "S3BucketPrefix": NotRequired[str],
    },
)
AddAvailabilityZonesInputRequestTypeDef = TypedDict(
    "AddAvailabilityZonesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "AvailabilityZones": Sequence[str],
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
AdditionalAttributeTypeDef = TypedDict(
    "AdditionalAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AppCookieStickinessPolicyTypeDef = TypedDict(
    "AppCookieStickinessPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "CookieName": NotRequired[str],
    },
)
ApplySecurityGroupsToLoadBalancerInputRequestTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "SecurityGroups": Sequence[str],
    },
)
AttachLoadBalancerToSubnetsInputRequestTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Subnets": Sequence[str],
    },
)
BackendServerDescriptionTypeDef = TypedDict(
    "BackendServerDescriptionTypeDef",
    {
        "InstancePort": NotRequired[int],
        "PolicyNames": NotRequired[List[str]],
    },
)
HealthCheckTypeDef = TypedDict(
    "HealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
)
ConnectionDrainingTypeDef = TypedDict(
    "ConnectionDrainingTypeDef",
    {
        "Enabled": bool,
        "Timeout": NotRequired[int],
    },
)
ConnectionSettingsTypeDef = TypedDict(
    "ConnectionSettingsTypeDef",
    {
        "IdleTimeout": int,
    },
)
ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstancePort": int,
        "InstanceProtocol": NotRequired[str],
        "SSLCertificateId": NotRequired[str],
    },
)
CreateAppCookieStickinessPolicyInputRequestTypeDef = TypedDict(
    "CreateAppCookieStickinessPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "CookieName": str,
    },
)
CreateLBCookieStickinessPolicyInputRequestTypeDef = TypedDict(
    "CreateLBCookieStickinessPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "CookieExpirationPeriod": NotRequired[int],
    },
)
PolicyAttributeTypeDef = TypedDict(
    "PolicyAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValue": NotRequired[str],
    },
)
CrossZoneLoadBalancingTypeDef = TypedDict(
    "CrossZoneLoadBalancingTypeDef",
    {
        "Enabled": bool,
    },
)
DeleteAccessPointInputRequestTypeDef = TypedDict(
    "DeleteAccessPointInputRequestTypeDef",
    {
        "LoadBalancerName": str,
    },
)
DeleteLoadBalancerListenerInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPorts": Sequence[int],
    },
)
DeleteLoadBalancerPolicyInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
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
DescribeAccessPointsInputRequestTypeDef = TypedDict(
    "DescribeAccessPointsInputRequestTypeDef",
    {
        "LoadBalancerNames": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
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
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "InstanceId": NotRequired[str],
        "State": NotRequired[str],
        "ReasonCode": NotRequired[str],
        "Description": NotRequired[str],
    },
)
DescribeLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
    },
)
DescribeLoadBalancerPoliciesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesInputRequestTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "PolicyNames": NotRequired[Sequence[str]],
    },
)
DescribeLoadBalancerPolicyTypesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesInputRequestTypeDef",
    {
        "PolicyTypeNames": NotRequired[Sequence[str]],
    },
)
DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
    },
)
DetachLoadBalancerFromSubnetsInputRequestTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Subnets": Sequence[str],
    },
)
LBCookieStickinessPolicyTypeDef = TypedDict(
    "LBCookieStickinessPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "CookieExpirationPeriod": NotRequired[int],
    },
)
SourceSecurityGroupTypeDef = TypedDict(
    "SourceSecurityGroupTypeDef",
    {
        "OwnerAlias": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)
PolicyAttributeDescriptionTypeDef = TypedDict(
    "PolicyAttributeDescriptionTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValue": NotRequired[str],
    },
)
PolicyAttributeTypeDescriptionTypeDef = TypedDict(
    "PolicyAttributeTypeDescriptionTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeType": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "Cardinality": NotRequired[str],
    },
)
RemoveAvailabilityZonesInputRequestTypeDef = TypedDict(
    "RemoveAvailabilityZonesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "AvailabilityZones": Sequence[str],
    },
)
TagKeyOnlyTypeDef = TypedDict(
    "TagKeyOnlyTypeDef",
    {
        "Key": NotRequired[str],
    },
)
SetLoadBalancerListenerSSLCertificateInputRequestTypeDef = TypedDict(
    "SetLoadBalancerListenerSSLCertificateInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPort": int,
        "SSLCertificateId": str,
    },
)
SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef = TypedDict(
    "SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "InstancePort": int,
        "PolicyNames": Sequence[str],
    },
)
SetLoadBalancerPoliciesOfListenerInputRequestTypeDef = TypedDict(
    "SetLoadBalancerPoliciesOfListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPort": int,
        "PolicyNames": Sequence[str],
    },
)
AddAvailabilityZonesOutputTypeDef = TypedDict(
    "AddAvailabilityZonesOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplySecurityGroupsToLoadBalancerOutputTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachLoadBalancerToSubnetsOutputTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    {
        "Subnets": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessPointOutputTypeDef = TypedDict(
    "CreateAccessPointOutputTypeDef",
    {
        "DNSName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachLoadBalancerFromSubnetsOutputTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    {
        "Subnets": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveAvailabilityZonesOutputTypeDef = TypedDict(
    "RemoveAvailabilityZonesOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ConfigureHealthCheckInputRequestTypeDef = TypedDict(
    "ConfigureHealthCheckInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "HealthCheck": HealthCheckTypeDef,
    },
)
ConfigureHealthCheckOutputTypeDef = TypedDict(
    "ConfigureHealthCheckOutputTypeDef",
    {
        "HealthCheck": HealthCheckTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessPointInputRequestTypeDef = TypedDict(
    "CreateAccessPointInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Listeners": Sequence[ListenerTypeDef],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "Subnets": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Scheme": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateLoadBalancerListenerInputRequestTypeDef = TypedDict(
    "CreateLoadBalancerListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Listeners": Sequence[ListenerTypeDef],
    },
)
ListenerDescriptionTypeDef = TypedDict(
    "ListenerDescriptionTypeDef",
    {
        "Listener": NotRequired[ListenerTypeDef],
        "PolicyNames": NotRequired[List[str]],
    },
)
CreateLoadBalancerPolicyInputRequestTypeDef = TypedDict(
    "CreateLoadBalancerPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "PolicyTypeName": str,
        "PolicyAttributes": NotRequired[Sequence[PolicyAttributeTypeDef]],
    },
)
LoadBalancerAttributesOutputTypeDef = TypedDict(
    "LoadBalancerAttributesOutputTypeDef",
    {
        "CrossZoneLoadBalancing": NotRequired[CrossZoneLoadBalancingTypeDef],
        "AccessLog": NotRequired[AccessLogTypeDef],
        "ConnectionDraining": NotRequired[ConnectionDrainingTypeDef],
        "ConnectionSettings": NotRequired[ConnectionSettingsTypeDef],
        "AdditionalAttributes": NotRequired[List[AdditionalAttributeTypeDef]],
    },
)
LoadBalancerAttributesTypeDef = TypedDict(
    "LoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": NotRequired[CrossZoneLoadBalancingTypeDef],
        "AccessLog": NotRequired[AccessLogTypeDef],
        "ConnectionDraining": NotRequired[ConnectionDrainingTypeDef],
        "ConnectionSettings": NotRequired[ConnectionSettingsTypeDef],
        "AdditionalAttributes": NotRequired[Sequence[AdditionalAttributeTypeDef]],
    },
)
DeregisterEndPointsInputRequestTypeDef = TypedDict(
    "DeregisterEndPointsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": Sequence[InstanceTypeDef],
    },
)
DeregisterEndPointsOutputTypeDef = TypedDict(
    "DeregisterEndPointsOutputTypeDef",
    {
        "Instances": List[InstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEndPointStateInputRequestTypeDef = TypedDict(
    "DescribeEndPointStateInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": NotRequired[Sequence[InstanceTypeDef]],
    },
)
RegisterEndPointsInputRequestTypeDef = TypedDict(
    "RegisterEndPointsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": Sequence[InstanceTypeDef],
    },
)
RegisterEndPointsOutputTypeDef = TypedDict(
    "RegisterEndPointsOutputTypeDef",
    {
        "Instances": List[InstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccessPointsInputDescribeLoadBalancersPaginateTypeDef = TypedDict(
    "DescribeAccessPointsInputDescribeLoadBalancersPaginateTypeDef",
    {
        "LoadBalancerNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef = TypedDict(
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    {
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
DescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef = TypedDict(
    "DescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": NotRequired[Sequence[InstanceTypeDef]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEndPointStateInputInstanceDeregisteredWaitTypeDef = TypedDict(
    "DescribeEndPointStateInputInstanceDeregisteredWaitTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": NotRequired[Sequence[InstanceTypeDef]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEndPointStateInputInstanceInServiceWaitTypeDef = TypedDict(
    "DescribeEndPointStateInputInstanceInServiceWaitTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": NotRequired[Sequence[InstanceTypeDef]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEndPointStateOutputTypeDef = TypedDict(
    "DescribeEndPointStateOutputTypeDef",
    {
        "InstanceStates": List[InstanceStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PoliciesTypeDef = TypedDict(
    "PoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": NotRequired[List[AppCookieStickinessPolicyTypeDef]],
        "LBCookieStickinessPolicies": NotRequired[List[LBCookieStickinessPolicyTypeDef]],
        "OtherPolicies": NotRequired[List[str]],
    },
)
PolicyDescriptionTypeDef = TypedDict(
    "PolicyDescriptionTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyTypeName": NotRequired[str],
        "PolicyAttributeDescriptions": NotRequired[List[PolicyAttributeDescriptionTypeDef]],
    },
)
PolicyTypeDescriptionTypeDef = TypedDict(
    "PolicyTypeDescriptionTypeDef",
    {
        "PolicyTypeName": NotRequired[str],
        "Description": NotRequired[str],
        "PolicyAttributeTypeDescriptions": NotRequired[List[PolicyAttributeTypeDescriptionTypeDef]],
    },
)
RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
        "Tags": Sequence[TagKeyOnlyTypeDef],
    },
)
DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "TagDescriptions": List[TagDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "LoadBalancerAttributes": LoadBalancerAttributesOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": LoadBalancerAttributesOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": LoadBalancerAttributesTypeDef,
    },
)
LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "DNSName": NotRequired[str],
        "CanonicalHostedZoneName": NotRequired[str],
        "CanonicalHostedZoneNameID": NotRequired[str],
        "ListenerDescriptions": NotRequired[List[ListenerDescriptionTypeDef]],
        "Policies": NotRequired[PoliciesTypeDef],
        "BackendServerDescriptions": NotRequired[List[BackendServerDescriptionTypeDef]],
        "AvailabilityZones": NotRequired[List[str]],
        "Subnets": NotRequired[List[str]],
        "VPCId": NotRequired[str],
        "Instances": NotRequired[List[InstanceTypeDef]],
        "HealthCheck": NotRequired[HealthCheckTypeDef],
        "SourceSecurityGroup": NotRequired[SourceSecurityGroupTypeDef],
        "SecurityGroups": NotRequired[List[str]],
        "CreatedTime": NotRequired[datetime],
        "Scheme": NotRequired[str],
    },
)
DescribeLoadBalancerPoliciesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    {
        "PolicyDescriptions": List[PolicyDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLoadBalancerPolicyTypesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    {
        "PolicyTypeDescriptions": List[PolicyTypeDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccessPointsOutputTypeDef = TypedDict(
    "DescribeAccessPointsOutputTypeDef",
    {
        "LoadBalancerDescriptions": List[LoadBalancerDescriptionTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
