"""
Type annotations for route53resolver service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/type_defs/)

Usage::

    ```python
    from mypy_boto3_route53resolver.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import (
    ActionType,
    AutodefinedReverseFlagType,
    BlockResponseType,
    FirewallDomainListStatusType,
    FirewallDomainRedirectionActionType,
    FirewallDomainUpdateOperationType,
    FirewallFailOpenStatusType,
    FirewallRuleGroupAssociationStatusType,
    FirewallRuleGroupStatusType,
    IpAddressStatusType,
    MutationProtectionStatusType,
    OutpostResolverStatusType,
    ProtocolType,
    ResolverAutodefinedReverseStatusType,
    ResolverDNSSECValidationStatusType,
    ResolverEndpointDirectionType,
    ResolverEndpointStatusType,
    ResolverEndpointTypeType,
    ResolverQueryLogConfigAssociationErrorType,
    ResolverQueryLogConfigAssociationStatusType,
    ResolverQueryLogConfigStatusType,
    ResolverRuleAssociationStatusType,
    ResolverRuleStatusType,
    RuleTypeOptionType,
    ShareStatusType,
    SortOrderType,
    ValidationType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "TagTypeDef",
    "FirewallRuleGroupAssociationTypeDef",
    "ResponseMetadataTypeDef",
    "IpAddressUpdateTypeDef",
    "ResolverEndpointTypeDef",
    "AssociateResolverQueryLogConfigRequestRequestTypeDef",
    "ResolverQueryLogConfigAssociationTypeDef",
    "AssociateResolverRuleRequestRequestTypeDef",
    "ResolverRuleAssociationTypeDef",
    "FirewallDomainListTypeDef",
    "FirewallRuleGroupTypeDef",
    "CreateFirewallRuleRequestRequestTypeDef",
    "FirewallRuleTypeDef",
    "OutpostResolverTypeDef",
    "IpAddressRequestTypeDef",
    "ResolverQueryLogConfigTypeDef",
    "TargetAddressTypeDef",
    "DeleteFirewallDomainListRequestRequestTypeDef",
    "DeleteFirewallRuleGroupRequestRequestTypeDef",
    "DeleteFirewallRuleRequestRequestTypeDef",
    "DeleteOutpostResolverRequestRequestTypeDef",
    "DeleteResolverEndpointRequestRequestTypeDef",
    "DeleteResolverQueryLogConfigRequestRequestTypeDef",
    "DeleteResolverRuleRequestRequestTypeDef",
    "DisassociateFirewallRuleGroupRequestRequestTypeDef",
    "DisassociateResolverQueryLogConfigRequestRequestTypeDef",
    "DisassociateResolverRuleRequestRequestTypeDef",
    "FilterTypeDef",
    "FirewallConfigTypeDef",
    "FirewallDomainListMetadataTypeDef",
    "FirewallRuleGroupMetadataTypeDef",
    "GetFirewallConfigRequestRequestTypeDef",
    "GetFirewallDomainListRequestRequestTypeDef",
    "GetFirewallRuleGroupAssociationRequestRequestTypeDef",
    "GetFirewallRuleGroupPolicyRequestRequestTypeDef",
    "GetFirewallRuleGroupRequestRequestTypeDef",
    "GetOutpostResolverRequestRequestTypeDef",
    "GetResolverConfigRequestRequestTypeDef",
    "ResolverConfigTypeDef",
    "GetResolverDnssecConfigRequestRequestTypeDef",
    "ResolverDnssecConfigTypeDef",
    "GetResolverEndpointRequestRequestTypeDef",
    "GetResolverQueryLogConfigAssociationRequestRequestTypeDef",
    "GetResolverQueryLogConfigPolicyRequestRequestTypeDef",
    "GetResolverQueryLogConfigRequestRequestTypeDef",
    "GetResolverRuleAssociationRequestRequestTypeDef",
    "GetResolverRulePolicyRequestRequestTypeDef",
    "GetResolverRuleRequestRequestTypeDef",
    "ImportFirewallDomainsRequestRequestTypeDef",
    "IpAddressResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ListFirewallConfigsRequestRequestTypeDef",
    "ListFirewallDomainListsRequestRequestTypeDef",
    "ListFirewallDomainsRequestRequestTypeDef",
    "ListFirewallRuleGroupAssociationsRequestRequestTypeDef",
    "ListFirewallRuleGroupsRequestRequestTypeDef",
    "ListFirewallRulesRequestRequestTypeDef",
    "ListOutpostResolversRequestRequestTypeDef",
    "ListResolverConfigsRequestRequestTypeDef",
    "ListResolverEndpointIpAddressesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutFirewallRuleGroupPolicyRequestRequestTypeDef",
    "PutResolverQueryLogConfigPolicyRequestRequestTypeDef",
    "PutResolverRulePolicyRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFirewallConfigRequestRequestTypeDef",
    "UpdateFirewallDomainsRequestRequestTypeDef",
    "UpdateFirewallRuleGroupAssociationRequestRequestTypeDef",
    "UpdateFirewallRuleRequestRequestTypeDef",
    "UpdateIpAddressTypeDef",
    "UpdateOutpostResolverRequestRequestTypeDef",
    "UpdateResolverConfigRequestRequestTypeDef",
    "UpdateResolverDnssecConfigRequestRequestTypeDef",
    "AssociateFirewallRuleGroupRequestRequestTypeDef",
    "CreateFirewallDomainListRequestRequestTypeDef",
    "CreateFirewallRuleGroupRequestRequestTypeDef",
    "CreateOutpostResolverRequestRequestTypeDef",
    "CreateResolverQueryLogConfigRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "AssociateFirewallRuleGroupResponseTypeDef",
    "DisassociateFirewallRuleGroupResponseTypeDef",
    "GetFirewallRuleGroupAssociationResponseTypeDef",
    "GetFirewallRuleGroupPolicyResponseTypeDef",
    "GetResolverQueryLogConfigPolicyResponseTypeDef",
    "GetResolverRulePolicyResponseTypeDef",
    "ImportFirewallDomainsResponseTypeDef",
    "ListFirewallDomainsResponseTypeDef",
    "ListFirewallRuleGroupAssociationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutFirewallRuleGroupPolicyResponseTypeDef",
    "PutResolverQueryLogConfigPolicyResponseTypeDef",
    "PutResolverRulePolicyResponseTypeDef",
    "UpdateFirewallDomainsResponseTypeDef",
    "UpdateFirewallRuleGroupAssociationResponseTypeDef",
    "AssociateResolverEndpointIpAddressRequestRequestTypeDef",
    "DisassociateResolverEndpointIpAddressRequestRequestTypeDef",
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    "CreateResolverEndpointResponseTypeDef",
    "DeleteResolverEndpointResponseTypeDef",
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    "GetResolverEndpointResponseTypeDef",
    "ListResolverEndpointsResponseTypeDef",
    "UpdateResolverEndpointResponseTypeDef",
    "AssociateResolverQueryLogConfigResponseTypeDef",
    "DisassociateResolverQueryLogConfigResponseTypeDef",
    "GetResolverQueryLogConfigAssociationResponseTypeDef",
    "ListResolverQueryLogConfigAssociationsResponseTypeDef",
    "AssociateResolverRuleResponseTypeDef",
    "DisassociateResolverRuleResponseTypeDef",
    "GetResolverRuleAssociationResponseTypeDef",
    "ListResolverRuleAssociationsResponseTypeDef",
    "CreateFirewallDomainListResponseTypeDef",
    "DeleteFirewallDomainListResponseTypeDef",
    "GetFirewallDomainListResponseTypeDef",
    "CreateFirewallRuleGroupResponseTypeDef",
    "DeleteFirewallRuleGroupResponseTypeDef",
    "GetFirewallRuleGroupResponseTypeDef",
    "CreateFirewallRuleResponseTypeDef",
    "DeleteFirewallRuleResponseTypeDef",
    "ListFirewallRulesResponseTypeDef",
    "UpdateFirewallRuleResponseTypeDef",
    "CreateOutpostResolverResponseTypeDef",
    "DeleteOutpostResolverResponseTypeDef",
    "GetOutpostResolverResponseTypeDef",
    "ListOutpostResolversResponseTypeDef",
    "UpdateOutpostResolverResponseTypeDef",
    "CreateResolverEndpointRequestRequestTypeDef",
    "CreateResolverQueryLogConfigResponseTypeDef",
    "DeleteResolverQueryLogConfigResponseTypeDef",
    "GetResolverQueryLogConfigResponseTypeDef",
    "ListResolverQueryLogConfigsResponseTypeDef",
    "CreateResolverRuleRequestRequestTypeDef",
    "ResolverRuleConfigTypeDef",
    "ResolverRuleTypeDef",
    "ListResolverDnssecConfigsRequestRequestTypeDef",
    "ListResolverEndpointsRequestRequestTypeDef",
    "ListResolverQueryLogConfigAssociationsRequestRequestTypeDef",
    "ListResolverQueryLogConfigsRequestRequestTypeDef",
    "ListResolverRuleAssociationsRequestRequestTypeDef",
    "ListResolverRulesRequestRequestTypeDef",
    "GetFirewallConfigResponseTypeDef",
    "ListFirewallConfigsResponseTypeDef",
    "UpdateFirewallConfigResponseTypeDef",
    "ListFirewallDomainListsResponseTypeDef",
    "ListFirewallRuleGroupsResponseTypeDef",
    "GetResolverConfigResponseTypeDef",
    "ListResolverConfigsResponseTypeDef",
    "UpdateResolverConfigResponseTypeDef",
    "GetResolverDnssecConfigResponseTypeDef",
    "ListResolverDnssecConfigsResponseTypeDef",
    "UpdateResolverDnssecConfigResponseTypeDef",
    "ListResolverEndpointIpAddressesResponseTypeDef",
    "ListFirewallConfigsRequestListFirewallConfigsPaginateTypeDef",
    "ListFirewallDomainListsRequestListFirewallDomainListsPaginateTypeDef",
    "ListFirewallDomainsRequestListFirewallDomainsPaginateTypeDef",
    "ListFirewallRuleGroupAssociationsRequestListFirewallRuleGroupAssociationsPaginateTypeDef",
    "ListFirewallRuleGroupsRequestListFirewallRuleGroupsPaginateTypeDef",
    "ListFirewallRulesRequestListFirewallRulesPaginateTypeDef",
    "ListOutpostResolversRequestListOutpostResolversPaginateTypeDef",
    "ListResolverConfigsRequestListResolverConfigsPaginateTypeDef",
    "ListResolverDnssecConfigsRequestListResolverDnssecConfigsPaginateTypeDef",
    "ListResolverEndpointIpAddressesRequestListResolverEndpointIpAddressesPaginateTypeDef",
    "ListResolverEndpointsRequestListResolverEndpointsPaginateTypeDef",
    "ListResolverQueryLogConfigAssociationsRequestListResolverQueryLogConfigAssociationsPaginateTypeDef",
    "ListResolverQueryLogConfigsRequestListResolverQueryLogConfigsPaginateTypeDef",
    "ListResolverRuleAssociationsRequestListResolverRuleAssociationsPaginateTypeDef",
    "ListResolverRulesRequestListResolverRulesPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "UpdateResolverEndpointRequestRequestTypeDef",
    "UpdateResolverRuleRequestRequestTypeDef",
    "CreateResolverRuleResponseTypeDef",
    "DeleteResolverRuleResponseTypeDef",
    "GetResolverRuleResponseTypeDef",
    "ListResolverRulesResponseTypeDef",
    "UpdateResolverRuleResponseTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
FirewallRuleGroupAssociationTypeDef = TypedDict(
    "FirewallRuleGroupAssociationTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "FirewallRuleGroupId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Name": NotRequired[str],
        "Priority": NotRequired[int],
        "MutationProtection": NotRequired[MutationProtectionStatusType],
        "ManagedOwnerName": NotRequired[str],
        "Status": NotRequired[FirewallRuleGroupAssociationStatusType],
        "StatusMessage": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
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
IpAddressUpdateTypeDef = TypedDict(
    "IpAddressUpdateTypeDef",
    {
        "IpId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Ip": NotRequired[str],
        "Ipv6": NotRequired[str],
    },
)
ResolverEndpointTypeDef = TypedDict(
    "ResolverEndpointTypeDef",
    {
        "Id": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "Direction": NotRequired[ResolverEndpointDirectionType],
        "IpAddressCount": NotRequired[int],
        "HostVPCId": NotRequired[str],
        "Status": NotRequired[ResolverEndpointStatusType],
        "StatusMessage": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "PreferredInstanceType": NotRequired[str],
        "ResolverEndpointType": NotRequired[ResolverEndpointTypeType],
        "Protocols": NotRequired[List[ProtocolType]],
    },
)
AssociateResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "AssociateResolverQueryLogConfigRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
        "ResourceId": str,
    },
)
ResolverQueryLogConfigAssociationTypeDef = TypedDict(
    "ResolverQueryLogConfigAssociationTypeDef",
    {
        "Id": NotRequired[str],
        "ResolverQueryLogConfigId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Status": NotRequired[ResolverQueryLogConfigAssociationStatusType],
        "Error": NotRequired[ResolverQueryLogConfigAssociationErrorType],
        "ErrorMessage": NotRequired[str],
        "CreationTime": NotRequired[str],
    },
)
AssociateResolverRuleRequestRequestTypeDef = TypedDict(
    "AssociateResolverRuleRequestRequestTypeDef",
    {
        "ResolverRuleId": str,
        "VPCId": str,
        "Name": NotRequired[str],
    },
)
ResolverRuleAssociationTypeDef = TypedDict(
    "ResolverRuleAssociationTypeDef",
    {
        "Id": NotRequired[str],
        "ResolverRuleId": NotRequired[str],
        "Name": NotRequired[str],
        "VPCId": NotRequired[str],
        "Status": NotRequired[ResolverRuleAssociationStatusType],
        "StatusMessage": NotRequired[str],
    },
)
FirewallDomainListTypeDef = TypedDict(
    "FirewallDomainListTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "DomainCount": NotRequired[int],
        "Status": NotRequired[FirewallDomainListStatusType],
        "StatusMessage": NotRequired[str],
        "ManagedOwnerName": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)
FirewallRuleGroupTypeDef = TypedDict(
    "FirewallRuleGroupTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "RuleCount": NotRequired[int],
        "Status": NotRequired[FirewallRuleGroupStatusType],
        "StatusMessage": NotRequired[str],
        "OwnerId": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)
CreateFirewallRuleRequestRequestTypeDef = TypedDict(
    "CreateFirewallRuleRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
        "Priority": int,
        "Action": ActionType,
        "Name": str,
        "BlockResponse": NotRequired[BlockResponseType],
        "BlockOverrideDomain": NotRequired[str],
        "BlockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "BlockOverrideTtl": NotRequired[int],
        "FirewallDomainRedirectionAction": NotRequired[FirewallDomainRedirectionActionType],
        "Qtype": NotRequired[str],
    },
)
FirewallRuleTypeDef = TypedDict(
    "FirewallRuleTypeDef",
    {
        "FirewallRuleGroupId": NotRequired[str],
        "FirewallDomainListId": NotRequired[str],
        "Name": NotRequired[str],
        "Priority": NotRequired[int],
        "Action": NotRequired[ActionType],
        "BlockResponse": NotRequired[BlockResponseType],
        "BlockOverrideDomain": NotRequired[str],
        "BlockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "BlockOverrideTtl": NotRequired[int],
        "CreatorRequestId": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
        "FirewallDomainRedirectionAction": NotRequired[FirewallDomainRedirectionActionType],
        "Qtype": NotRequired[str],
    },
)
OutpostResolverTypeDef = TypedDict(
    "OutpostResolverTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "Id": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "PreferredInstanceType": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[OutpostResolverStatusType],
        "StatusMessage": NotRequired[str],
        "OutpostArn": NotRequired[str],
    },
)
IpAddressRequestTypeDef = TypedDict(
    "IpAddressRequestTypeDef",
    {
        "SubnetId": str,
        "Ip": NotRequired[str],
        "Ipv6": NotRequired[str],
    },
)
ResolverQueryLogConfigTypeDef = TypedDict(
    "ResolverQueryLogConfigTypeDef",
    {
        "Id": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Status": NotRequired[ResolverQueryLogConfigStatusType],
        "ShareStatus": NotRequired[ShareStatusType],
        "AssociationCount": NotRequired[int],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "DestinationArn": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "CreationTime": NotRequired[str],
    },
)
TargetAddressTypeDef = TypedDict(
    "TargetAddressTypeDef",
    {
        "Ip": NotRequired[str],
        "Port": NotRequired[int],
        "Ipv6": NotRequired[str],
        "Protocol": NotRequired[ProtocolType],
        "ServerNameIndication": NotRequired[str],
    },
)
DeleteFirewallDomainListRequestRequestTypeDef = TypedDict(
    "DeleteFirewallDomainListRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
    },
)
DeleteFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteFirewallRuleGroupRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
    },
)
DeleteFirewallRuleRequestRequestTypeDef = TypedDict(
    "DeleteFirewallRuleRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
        "Qtype": NotRequired[str],
    },
)
DeleteOutpostResolverRequestRequestTypeDef = TypedDict(
    "DeleteOutpostResolverRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteResolverEndpointRequestRequestTypeDef = TypedDict(
    "DeleteResolverEndpointRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
    },
)
DeleteResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "DeleteResolverQueryLogConfigRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
    },
)
DeleteResolverRuleRequestRequestTypeDef = TypedDict(
    "DeleteResolverRuleRequestRequestTypeDef",
    {
        "ResolverRuleId": str,
    },
)
DisassociateFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "DisassociateFirewallRuleGroupRequestRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
    },
)
DisassociateResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "DisassociateResolverQueryLogConfigRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
        "ResourceId": str,
    },
)
DisassociateResolverRuleRequestRequestTypeDef = TypedDict(
    "DisassociateResolverRuleRequestRequestTypeDef",
    {
        "VPCId": str,
        "ResolverRuleId": str,
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
FirewallConfigTypeDef = TypedDict(
    "FirewallConfigTypeDef",
    {
        "Id": NotRequired[str],
        "ResourceId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "FirewallFailOpen": NotRequired[FirewallFailOpenStatusType],
    },
)
FirewallDomainListMetadataTypeDef = TypedDict(
    "FirewallDomainListMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "ManagedOwnerName": NotRequired[str],
    },
)
FirewallRuleGroupMetadataTypeDef = TypedDict(
    "FirewallRuleGroupMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "OwnerId": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
    },
)
GetFirewallConfigRequestRequestTypeDef = TypedDict(
    "GetFirewallConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
GetFirewallDomainListRequestRequestTypeDef = TypedDict(
    "GetFirewallDomainListRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
    },
)
GetFirewallRuleGroupAssociationRequestRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupAssociationRequestRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
    },
)
GetFirewallRuleGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupPolicyRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
GetFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
    },
)
GetOutpostResolverRequestRequestTypeDef = TypedDict(
    "GetOutpostResolverRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetResolverConfigRequestRequestTypeDef = TypedDict(
    "GetResolverConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
ResolverConfigTypeDef = TypedDict(
    "ResolverConfigTypeDef",
    {
        "Id": NotRequired[str],
        "ResourceId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "AutodefinedReverse": NotRequired[ResolverAutodefinedReverseStatusType],
    },
)
GetResolverDnssecConfigRequestRequestTypeDef = TypedDict(
    "GetResolverDnssecConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
ResolverDnssecConfigTypeDef = TypedDict(
    "ResolverDnssecConfigTypeDef",
    {
        "Id": NotRequired[str],
        "OwnerId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ValidationStatus": NotRequired[ResolverDNSSECValidationStatusType],
    },
)
GetResolverEndpointRequestRequestTypeDef = TypedDict(
    "GetResolverEndpointRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
    },
)
GetResolverQueryLogConfigAssociationRequestRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigAssociationRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigAssociationId": str,
    },
)
GetResolverQueryLogConfigPolicyRequestRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigPolicyRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
GetResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
    },
)
GetResolverRuleAssociationRequestRequestTypeDef = TypedDict(
    "GetResolverRuleAssociationRequestRequestTypeDef",
    {
        "ResolverRuleAssociationId": str,
    },
)
GetResolverRulePolicyRequestRequestTypeDef = TypedDict(
    "GetResolverRulePolicyRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
GetResolverRuleRequestRequestTypeDef = TypedDict(
    "GetResolverRuleRequestRequestTypeDef",
    {
        "ResolverRuleId": str,
    },
)
ImportFirewallDomainsRequestRequestTypeDef = TypedDict(
    "ImportFirewallDomainsRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
        "Operation": Literal["REPLACE"],
        "DomainFileUrl": str,
    },
)
IpAddressResponseTypeDef = TypedDict(
    "IpAddressResponseTypeDef",
    {
        "IpId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Ip": NotRequired[str],
        "Ipv6": NotRequired[str],
        "Status": NotRequired[IpAddressStatusType],
        "StatusMessage": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
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
ListFirewallConfigsRequestRequestTypeDef = TypedDict(
    "ListFirewallConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFirewallDomainListsRequestRequestTypeDef = TypedDict(
    "ListFirewallDomainListsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFirewallDomainsRequestRequestTypeDef = TypedDict(
    "ListFirewallDomainsRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFirewallRuleGroupAssociationsRequestRequestTypeDef = TypedDict(
    "ListFirewallRuleGroupAssociationsRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Priority": NotRequired[int],
        "Status": NotRequired[FirewallRuleGroupAssociationStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFirewallRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListFirewallRuleGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFirewallRulesRequestRequestTypeDef = TypedDict(
    "ListFirewallRulesRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "Priority": NotRequired[int],
        "Action": NotRequired[ActionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOutpostResolversRequestRequestTypeDef = TypedDict(
    "ListOutpostResolversRequestRequestTypeDef",
    {
        "OutpostArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListResolverConfigsRequestRequestTypeDef = TypedDict(
    "ListResolverConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListResolverEndpointIpAddressesRequestRequestTypeDef = TypedDict(
    "ListResolverEndpointIpAddressesRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PutFirewallRuleGroupPolicyRequestRequestTypeDef = TypedDict(
    "PutFirewallRuleGroupPolicyRequestRequestTypeDef",
    {
        "Arn": str,
        "FirewallRuleGroupPolicy": str,
    },
)
PutResolverQueryLogConfigPolicyRequestRequestTypeDef = TypedDict(
    "PutResolverQueryLogConfigPolicyRequestRequestTypeDef",
    {
        "Arn": str,
        "ResolverQueryLogConfigPolicy": str,
    },
)
PutResolverRulePolicyRequestRequestTypeDef = TypedDict(
    "PutResolverRulePolicyRequestRequestTypeDef",
    {
        "Arn": str,
        "ResolverRulePolicy": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateFirewallConfigRequestRequestTypeDef = TypedDict(
    "UpdateFirewallConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
        "FirewallFailOpen": FirewallFailOpenStatusType,
    },
)
UpdateFirewallDomainsRequestRequestTypeDef = TypedDict(
    "UpdateFirewallDomainsRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
        "Operation": FirewallDomainUpdateOperationType,
        "Domains": Sequence[str],
    },
)
UpdateFirewallRuleGroupAssociationRequestRequestTypeDef = TypedDict(
    "UpdateFirewallRuleGroupAssociationRequestRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
        "Priority": NotRequired[int],
        "MutationProtection": NotRequired[MutationProtectionStatusType],
        "Name": NotRequired[str],
    },
)
UpdateFirewallRuleRequestRequestTypeDef = TypedDict(
    "UpdateFirewallRuleRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
        "Priority": NotRequired[int],
        "Action": NotRequired[ActionType],
        "BlockResponse": NotRequired[BlockResponseType],
        "BlockOverrideDomain": NotRequired[str],
        "BlockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "BlockOverrideTtl": NotRequired[int],
        "Name": NotRequired[str],
        "FirewallDomainRedirectionAction": NotRequired[FirewallDomainRedirectionActionType],
        "Qtype": NotRequired[str],
    },
)
UpdateIpAddressTypeDef = TypedDict(
    "UpdateIpAddressTypeDef",
    {
        "IpId": str,
        "Ipv6": str,
    },
)
UpdateOutpostResolverRequestRequestTypeDef = TypedDict(
    "UpdateOutpostResolverRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "PreferredInstanceType": NotRequired[str],
    },
)
UpdateResolverConfigRequestRequestTypeDef = TypedDict(
    "UpdateResolverConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AutodefinedReverseFlag": AutodefinedReverseFlagType,
    },
)
UpdateResolverDnssecConfigRequestRequestTypeDef = TypedDict(
    "UpdateResolverDnssecConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Validation": ValidationType,
    },
)
AssociateFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "AssociateFirewallRuleGroupRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "FirewallRuleGroupId": str,
        "VpcId": str,
        "Priority": int,
        "Name": str,
        "MutationProtection": NotRequired[MutationProtectionStatusType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateFirewallDomainListRequestRequestTypeDef = TypedDict(
    "CreateFirewallDomainListRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Name": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "CreateFirewallRuleGroupRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Name": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateOutpostResolverRequestRequestTypeDef = TypedDict(
    "CreateOutpostResolverRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Name": str,
        "PreferredInstanceType": str,
        "OutpostArn": str,
        "InstanceCount": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "CreateResolverQueryLogConfigRequestRequestTypeDef",
    {
        "Name": str,
        "DestinationArn": str,
        "CreatorRequestId": str,
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
AssociateFirewallRuleGroupResponseTypeDef = TypedDict(
    "AssociateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": FirewallRuleGroupAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateFirewallRuleGroupResponseTypeDef = TypedDict(
    "DisassociateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": FirewallRuleGroupAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFirewallRuleGroupAssociationResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupAssociationResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": FirewallRuleGroupAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFirewallRuleGroupPolicyResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupPolicyResponseTypeDef",
    {
        "FirewallRuleGroupPolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResolverQueryLogConfigPolicyResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigPolicyResponseTypeDef",
    {
        "ResolverQueryLogConfigPolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResolverRulePolicyResponseTypeDef = TypedDict(
    "GetResolverRulePolicyResponseTypeDef",
    {
        "ResolverRulePolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportFirewallDomainsResponseTypeDef = TypedDict(
    "ImportFirewallDomainsResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFirewallDomainsResponseTypeDef = TypedDict(
    "ListFirewallDomainsResponseTypeDef",
    {
        "Domains": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFirewallRuleGroupAssociationsResponseTypeDef = TypedDict(
    "ListFirewallRuleGroupAssociationsResponseTypeDef",
    {
        "FirewallRuleGroupAssociations": List[FirewallRuleGroupAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutFirewallRuleGroupPolicyResponseTypeDef = TypedDict(
    "PutFirewallRuleGroupPolicyResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResolverQueryLogConfigPolicyResponseTypeDef = TypedDict(
    "PutResolverQueryLogConfigPolicyResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResolverRulePolicyResponseTypeDef = TypedDict(
    "PutResolverRulePolicyResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFirewallDomainsResponseTypeDef = TypedDict(
    "UpdateFirewallDomainsResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFirewallRuleGroupAssociationResponseTypeDef = TypedDict(
    "UpdateFirewallRuleGroupAssociationResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": FirewallRuleGroupAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateResolverEndpointIpAddressRequestRequestTypeDef = TypedDict(
    "AssociateResolverEndpointIpAddressRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "IpAddress": IpAddressUpdateTypeDef,
    },
)
DisassociateResolverEndpointIpAddressRequestRequestTypeDef = TypedDict(
    "DisassociateResolverEndpointIpAddressRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "IpAddress": IpAddressUpdateTypeDef,
    },
)
AssociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": ResolverEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResolverEndpointResponseTypeDef = TypedDict(
    "CreateResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": ResolverEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResolverEndpointResponseTypeDef = TypedDict(
    "DeleteResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": ResolverEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": ResolverEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResolverEndpointResponseTypeDef = TypedDict(
    "GetResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": ResolverEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResolverEndpointsResponseTypeDef = TypedDict(
    "ListResolverEndpointsResponseTypeDef",
    {
        "MaxResults": int,
        "ResolverEndpoints": List[ResolverEndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateResolverEndpointResponseTypeDef = TypedDict(
    "UpdateResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": ResolverEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "AssociateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": ResolverQueryLogConfigAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "DisassociateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": ResolverQueryLogConfigAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResolverQueryLogConfigAssociationResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigAssociationResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": ResolverQueryLogConfigAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResolverQueryLogConfigAssociationsResponseTypeDef = TypedDict(
    "ListResolverQueryLogConfigAssociationsResponseTypeDef",
    {
        "TotalCount": int,
        "TotalFilteredCount": int,
        "ResolverQueryLogConfigAssociations": List[ResolverQueryLogConfigAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AssociateResolverRuleResponseTypeDef = TypedDict(
    "AssociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": ResolverRuleAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateResolverRuleResponseTypeDef = TypedDict(
    "DisassociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": ResolverRuleAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResolverRuleAssociationResponseTypeDef = TypedDict(
    "GetResolverRuleAssociationResponseTypeDef",
    {
        "ResolverRuleAssociation": ResolverRuleAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResolverRuleAssociationsResponseTypeDef = TypedDict(
    "ListResolverRuleAssociationsResponseTypeDef",
    {
        "MaxResults": int,
        "ResolverRuleAssociations": List[ResolverRuleAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateFirewallDomainListResponseTypeDef = TypedDict(
    "CreateFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": FirewallDomainListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFirewallDomainListResponseTypeDef = TypedDict(
    "DeleteFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": FirewallDomainListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFirewallDomainListResponseTypeDef = TypedDict(
    "GetFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": FirewallDomainListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFirewallRuleGroupResponseTypeDef = TypedDict(
    "CreateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": FirewallRuleGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFirewallRuleGroupResponseTypeDef = TypedDict(
    "DeleteFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": FirewallRuleGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFirewallRuleGroupResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": FirewallRuleGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFirewallRuleResponseTypeDef = TypedDict(
    "CreateFirewallRuleResponseTypeDef",
    {
        "FirewallRule": FirewallRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFirewallRuleResponseTypeDef = TypedDict(
    "DeleteFirewallRuleResponseTypeDef",
    {
        "FirewallRule": FirewallRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFirewallRulesResponseTypeDef = TypedDict(
    "ListFirewallRulesResponseTypeDef",
    {
        "FirewallRules": List[FirewallRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateFirewallRuleResponseTypeDef = TypedDict(
    "UpdateFirewallRuleResponseTypeDef",
    {
        "FirewallRule": FirewallRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOutpostResolverResponseTypeDef = TypedDict(
    "CreateOutpostResolverResponseTypeDef",
    {
        "OutpostResolver": OutpostResolverTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteOutpostResolverResponseTypeDef = TypedDict(
    "DeleteOutpostResolverResponseTypeDef",
    {
        "OutpostResolver": OutpostResolverTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOutpostResolverResponseTypeDef = TypedDict(
    "GetOutpostResolverResponseTypeDef",
    {
        "OutpostResolver": OutpostResolverTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOutpostResolversResponseTypeDef = TypedDict(
    "ListOutpostResolversResponseTypeDef",
    {
        "OutpostResolvers": List[OutpostResolverTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateOutpostResolverResponseTypeDef = TypedDict(
    "UpdateOutpostResolverResponseTypeDef",
    {
        "OutpostResolver": OutpostResolverTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResolverEndpointRequestRequestTypeDef = TypedDict(
    "CreateResolverEndpointRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "SecurityGroupIds": Sequence[str],
        "Direction": ResolverEndpointDirectionType,
        "IpAddresses": Sequence[IpAddressRequestTypeDef],
        "Name": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "PreferredInstanceType": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ResolverEndpointType": NotRequired[ResolverEndpointTypeType],
        "Protocols": NotRequired[Sequence[ProtocolType]],
    },
)
CreateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "CreateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": ResolverQueryLogConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResolverQueryLogConfigResponseTypeDef = TypedDict(
    "DeleteResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": ResolverQueryLogConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResolverQueryLogConfigResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": ResolverQueryLogConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResolverQueryLogConfigsResponseTypeDef = TypedDict(
    "ListResolverQueryLogConfigsResponseTypeDef",
    {
        "TotalCount": int,
        "TotalFilteredCount": int,
        "ResolverQueryLogConfigs": List[ResolverQueryLogConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateResolverRuleRequestRequestTypeDef = TypedDict(
    "CreateResolverRuleRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "RuleType": RuleTypeOptionType,
        "Name": NotRequired[str],
        "DomainName": NotRequired[str],
        "TargetIps": NotRequired[Sequence[TargetAddressTypeDef]],
        "ResolverEndpointId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ResolverRuleConfigTypeDef = TypedDict(
    "ResolverRuleConfigTypeDef",
    {
        "Name": NotRequired[str],
        "TargetIps": NotRequired[Sequence[TargetAddressTypeDef]],
        "ResolverEndpointId": NotRequired[str],
    },
)
ResolverRuleTypeDef = TypedDict(
    "ResolverRuleTypeDef",
    {
        "Id": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "Arn": NotRequired[str],
        "DomainName": NotRequired[str],
        "Status": NotRequired[ResolverRuleStatusType],
        "StatusMessage": NotRequired[str],
        "RuleType": NotRequired[RuleTypeOptionType],
        "Name": NotRequired[str],
        "TargetIps": NotRequired[List[TargetAddressTypeDef]],
        "ResolverEndpointId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)
ListResolverDnssecConfigsRequestRequestTypeDef = TypedDict(
    "ListResolverDnssecConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListResolverEndpointsRequestRequestTypeDef = TypedDict(
    "ListResolverEndpointsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListResolverQueryLogConfigAssociationsRequestRequestTypeDef = TypedDict(
    "ListResolverQueryLogConfigAssociationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ListResolverQueryLogConfigsRequestRequestTypeDef = TypedDict(
    "ListResolverQueryLogConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ListResolverRuleAssociationsRequestRequestTypeDef = TypedDict(
    "ListResolverRuleAssociationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListResolverRulesRequestRequestTypeDef = TypedDict(
    "ListResolverRulesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
GetFirewallConfigResponseTypeDef = TypedDict(
    "GetFirewallConfigResponseTypeDef",
    {
        "FirewallConfig": FirewallConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFirewallConfigsResponseTypeDef = TypedDict(
    "ListFirewallConfigsResponseTypeDef",
    {
        "FirewallConfigs": List[FirewallConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateFirewallConfigResponseTypeDef = TypedDict(
    "UpdateFirewallConfigResponseTypeDef",
    {
        "FirewallConfig": FirewallConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFirewallDomainListsResponseTypeDef = TypedDict(
    "ListFirewallDomainListsResponseTypeDef",
    {
        "FirewallDomainLists": List[FirewallDomainListMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFirewallRuleGroupsResponseTypeDef = TypedDict(
    "ListFirewallRuleGroupsResponseTypeDef",
    {
        "FirewallRuleGroups": List[FirewallRuleGroupMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetResolverConfigResponseTypeDef = TypedDict(
    "GetResolverConfigResponseTypeDef",
    {
        "ResolverConfig": ResolverConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResolverConfigsResponseTypeDef = TypedDict(
    "ListResolverConfigsResponseTypeDef",
    {
        "ResolverConfigs": List[ResolverConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateResolverConfigResponseTypeDef = TypedDict(
    "UpdateResolverConfigResponseTypeDef",
    {
        "ResolverConfig": ResolverConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResolverDnssecConfigResponseTypeDef = TypedDict(
    "GetResolverDnssecConfigResponseTypeDef",
    {
        "ResolverDNSSECConfig": ResolverDnssecConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResolverDnssecConfigsResponseTypeDef = TypedDict(
    "ListResolverDnssecConfigsResponseTypeDef",
    {
        "ResolverDnssecConfigs": List[ResolverDnssecConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateResolverDnssecConfigResponseTypeDef = TypedDict(
    "UpdateResolverDnssecConfigResponseTypeDef",
    {
        "ResolverDNSSECConfig": ResolverDnssecConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResolverEndpointIpAddressesResponseTypeDef = TypedDict(
    "ListResolverEndpointIpAddressesResponseTypeDef",
    {
        "MaxResults": int,
        "IpAddresses": List[IpAddressResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFirewallConfigsRequestListFirewallConfigsPaginateTypeDef = TypedDict(
    "ListFirewallConfigsRequestListFirewallConfigsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFirewallDomainListsRequestListFirewallDomainListsPaginateTypeDef = TypedDict(
    "ListFirewallDomainListsRequestListFirewallDomainListsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFirewallDomainsRequestListFirewallDomainsPaginateTypeDef = TypedDict(
    "ListFirewallDomainsRequestListFirewallDomainsPaginateTypeDef",
    {
        "FirewallDomainListId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFirewallRuleGroupAssociationsRequestListFirewallRuleGroupAssociationsPaginateTypeDef = (
    TypedDict(
        "ListFirewallRuleGroupAssociationsRequestListFirewallRuleGroupAssociationsPaginateTypeDef",
        {
            "FirewallRuleGroupId": NotRequired[str],
            "VpcId": NotRequired[str],
            "Priority": NotRequired[int],
            "Status": NotRequired[FirewallRuleGroupAssociationStatusType],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListFirewallRuleGroupsRequestListFirewallRuleGroupsPaginateTypeDef = TypedDict(
    "ListFirewallRuleGroupsRequestListFirewallRuleGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFirewallRulesRequestListFirewallRulesPaginateTypeDef = TypedDict(
    "ListFirewallRulesRequestListFirewallRulesPaginateTypeDef",
    {
        "FirewallRuleGroupId": str,
        "Priority": NotRequired[int],
        "Action": NotRequired[ActionType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOutpostResolversRequestListOutpostResolversPaginateTypeDef = TypedDict(
    "ListOutpostResolversRequestListOutpostResolversPaginateTypeDef",
    {
        "OutpostArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResolverConfigsRequestListResolverConfigsPaginateTypeDef = TypedDict(
    "ListResolverConfigsRequestListResolverConfigsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResolverDnssecConfigsRequestListResolverDnssecConfigsPaginateTypeDef = TypedDict(
    "ListResolverDnssecConfigsRequestListResolverDnssecConfigsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResolverEndpointIpAddressesRequestListResolverEndpointIpAddressesPaginateTypeDef = TypedDict(
    "ListResolverEndpointIpAddressesRequestListResolverEndpointIpAddressesPaginateTypeDef",
    {
        "ResolverEndpointId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResolverEndpointsRequestListResolverEndpointsPaginateTypeDef = TypedDict(
    "ListResolverEndpointsRequestListResolverEndpointsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResolverQueryLogConfigAssociationsRequestListResolverQueryLogConfigAssociationsPaginateTypeDef = TypedDict(
    "ListResolverQueryLogConfigAssociationsRequestListResolverQueryLogConfigAssociationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResolverQueryLogConfigsRequestListResolverQueryLogConfigsPaginateTypeDef = TypedDict(
    "ListResolverQueryLogConfigsRequestListResolverQueryLogConfigsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResolverRuleAssociationsRequestListResolverRuleAssociationsPaginateTypeDef = TypedDict(
    "ListResolverRuleAssociationsRequestListResolverRuleAssociationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResolverRulesRequestListResolverRulesPaginateTypeDef = TypedDict(
    "ListResolverRulesRequestListResolverRulesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
UpdateResolverEndpointRequestRequestTypeDef = TypedDict(
    "UpdateResolverEndpointRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "Name": NotRequired[str],
        "ResolverEndpointType": NotRequired[ResolverEndpointTypeType],
        "UpdateIpAddresses": NotRequired[Sequence[UpdateIpAddressTypeDef]],
        "Protocols": NotRequired[Sequence[ProtocolType]],
    },
)
UpdateResolverRuleRequestRequestTypeDef = TypedDict(
    "UpdateResolverRuleRequestRequestTypeDef",
    {
        "ResolverRuleId": str,
        "Config": ResolverRuleConfigTypeDef,
    },
)
CreateResolverRuleResponseTypeDef = TypedDict(
    "CreateResolverRuleResponseTypeDef",
    {
        "ResolverRule": ResolverRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResolverRuleResponseTypeDef = TypedDict(
    "DeleteResolverRuleResponseTypeDef",
    {
        "ResolverRule": ResolverRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResolverRuleResponseTypeDef = TypedDict(
    "GetResolverRuleResponseTypeDef",
    {
        "ResolverRule": ResolverRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResolverRulesResponseTypeDef = TypedDict(
    "ListResolverRulesResponseTypeDef",
    {
        "MaxResults": int,
        "ResolverRules": List[ResolverRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateResolverRuleResponseTypeDef = TypedDict(
    "UpdateResolverRuleResponseTypeDef",
    {
        "ResolverRule": ResolverRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
