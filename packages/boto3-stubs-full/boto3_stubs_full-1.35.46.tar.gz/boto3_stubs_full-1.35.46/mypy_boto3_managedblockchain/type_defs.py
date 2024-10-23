"""
Type annotations for managedblockchain service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/type_defs/)

Usage::

    ```python
    from mypy_boto3_managedblockchain.type_defs import AccessorSummaryTypeDef

    data: AccessorSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AccessorNetworkTypeType,
    AccessorStatusType,
    EditionType,
    FrameworkType,
    InvitationStatusType,
    MemberStatusType,
    NetworkStatusType,
    NodeStatusType,
    ProposalStatusType,
    StateDBTypeType,
    ThresholdComparatorType,
    VoteValueType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AccessorSummaryTypeDef",
    "AccessorTypeDef",
    "ApprovalThresholdPolicyTypeDef",
    "CreateAccessorInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteAccessorInputRequestTypeDef",
    "DeleteMemberInputRequestTypeDef",
    "DeleteNodeInputRequestTypeDef",
    "GetAccessorInputRequestTypeDef",
    "GetMemberInputRequestTypeDef",
    "GetNetworkInputRequestTypeDef",
    "GetNodeInputRequestTypeDef",
    "GetProposalInputRequestTypeDef",
    "NetworkSummaryTypeDef",
    "InviteActionTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccessorsInputRequestTypeDef",
    "ListInvitationsInputRequestTypeDef",
    "ListMembersInputRequestTypeDef",
    "MemberSummaryTypeDef",
    "ListNetworksInputRequestTypeDef",
    "ListNodesInputRequestTypeDef",
    "NodeSummaryTypeDef",
    "ListProposalVotesInputRequestTypeDef",
    "VoteSummaryTypeDef",
    "ListProposalsInputRequestTypeDef",
    "ProposalSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "LogConfigurationTypeDef",
    "MemberFabricAttributesTypeDef",
    "MemberFabricConfigurationTypeDef",
    "NetworkEthereumAttributesTypeDef",
    "NetworkFabricAttributesTypeDef",
    "NetworkFabricConfigurationTypeDef",
    "NodeEthereumAttributesTypeDef",
    "NodeFabricAttributesTypeDef",
    "RemoveActionTypeDef",
    "RejectInvitationInputRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VoteOnProposalInputRequestTypeDef",
    "VotingPolicyTypeDef",
    "CreateAccessorOutputTypeDef",
    "CreateMemberOutputTypeDef",
    "CreateNetworkOutputTypeDef",
    "CreateNodeOutputTypeDef",
    "CreateProposalOutputTypeDef",
    "GetAccessorOutputTypeDef",
    "ListAccessorsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "InvitationTypeDef",
    "ListNetworksOutputTypeDef",
    "ListAccessorsInputListAccessorsPaginateTypeDef",
    "ListMembersOutputTypeDef",
    "ListNodesOutputTypeDef",
    "ListProposalVotesOutputTypeDef",
    "ListProposalsOutputTypeDef",
    "LogConfigurationsTypeDef",
    "MemberFrameworkAttributesTypeDef",
    "MemberFrameworkConfigurationTypeDef",
    "NetworkFrameworkAttributesTypeDef",
    "NetworkFrameworkConfigurationTypeDef",
    "NodeFrameworkAttributesTypeDef",
    "ProposalActionsOutputTypeDef",
    "ProposalActionsTypeDef",
    "ListInvitationsOutputTypeDef",
    "MemberFabricLogPublishingConfigurationTypeDef",
    "NodeFabricLogPublishingConfigurationTypeDef",
    "NetworkTypeDef",
    "ProposalTypeDef",
    "CreateProposalInputRequestTypeDef",
    "MemberLogPublishingConfigurationTypeDef",
    "NodeLogPublishingConfigurationTypeDef",
    "GetNetworkOutputTypeDef",
    "GetProposalOutputTypeDef",
    "MemberConfigurationTypeDef",
    "MemberTypeDef",
    "UpdateMemberInputRequestTypeDef",
    "NodeConfigurationTypeDef",
    "NodeTypeDef",
    "UpdateNodeInputRequestTypeDef",
    "CreateMemberInputRequestTypeDef",
    "CreateNetworkInputRequestTypeDef",
    "GetMemberOutputTypeDef",
    "CreateNodeInputRequestTypeDef",
    "GetNodeOutputTypeDef",
)

AccessorSummaryTypeDef = TypedDict(
    "AccessorSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[Literal["BILLING_TOKEN"]],
        "Status": NotRequired[AccessorStatusType],
        "CreationDate": NotRequired[datetime],
        "Arn": NotRequired[str],
        "NetworkType": NotRequired[AccessorNetworkTypeType],
    },
)
AccessorTypeDef = TypedDict(
    "AccessorTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[Literal["BILLING_TOKEN"]],
        "BillingToken": NotRequired[str],
        "Status": NotRequired[AccessorStatusType],
        "CreationDate": NotRequired[datetime],
        "Arn": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "NetworkType": NotRequired[AccessorNetworkTypeType],
    },
)
ApprovalThresholdPolicyTypeDef = TypedDict(
    "ApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": NotRequired[int],
        "ProposalDurationInHours": NotRequired[int],
        "ThresholdComparator": NotRequired[ThresholdComparatorType],
    },
)
CreateAccessorInputRequestTypeDef = TypedDict(
    "CreateAccessorInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "AccessorType": Literal["BILLING_TOKEN"],
        "Tags": NotRequired[Mapping[str, str]],
        "NetworkType": NotRequired[AccessorNetworkTypeType],
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
DeleteAccessorInputRequestTypeDef = TypedDict(
    "DeleteAccessorInputRequestTypeDef",
    {
        "AccessorId": str,
    },
)
DeleteMemberInputRequestTypeDef = TypedDict(
    "DeleteMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)
DeleteNodeInputRequestTypeDef = TypedDict(
    "DeleteNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
        "MemberId": NotRequired[str],
    },
)
GetAccessorInputRequestTypeDef = TypedDict(
    "GetAccessorInputRequestTypeDef",
    {
        "AccessorId": str,
    },
)
GetMemberInputRequestTypeDef = TypedDict(
    "GetMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)
GetNetworkInputRequestTypeDef = TypedDict(
    "GetNetworkInputRequestTypeDef",
    {
        "NetworkId": str,
    },
)
GetNodeInputRequestTypeDef = TypedDict(
    "GetNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
        "MemberId": NotRequired[str],
    },
)
GetProposalInputRequestTypeDef = TypedDict(
    "GetProposalInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
    },
)
NetworkSummaryTypeDef = TypedDict(
    "NetworkSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Framework": NotRequired[FrameworkType],
        "FrameworkVersion": NotRequired[str],
        "Status": NotRequired[NetworkStatusType],
        "CreationDate": NotRequired[datetime],
        "Arn": NotRequired[str],
    },
)
InviteActionTypeDef = TypedDict(
    "InviteActionTypeDef",
    {
        "Principal": str,
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
ListAccessorsInputRequestTypeDef = TypedDict(
    "ListAccessorsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "NetworkType": NotRequired[AccessorNetworkTypeType],
    },
)
ListInvitationsInputRequestTypeDef = TypedDict(
    "ListInvitationsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMembersInputRequestTypeDef = TypedDict(
    "ListMembersInputRequestTypeDef",
    {
        "NetworkId": str,
        "Name": NotRequired[str],
        "Status": NotRequired[MemberStatusType],
        "IsOwned": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MemberSummaryTypeDef = TypedDict(
    "MemberSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[MemberStatusType],
        "CreationDate": NotRequired[datetime],
        "IsOwned": NotRequired[bool],
        "Arn": NotRequired[str],
    },
)
ListNetworksInputRequestTypeDef = TypedDict(
    "ListNetworksInputRequestTypeDef",
    {
        "Name": NotRequired[str],
        "Framework": NotRequired[FrameworkType],
        "Status": NotRequired[NetworkStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListNodesInputRequestTypeDef = TypedDict(
    "ListNodesInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": NotRequired[str],
        "Status": NotRequired[NodeStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NodeSummaryTypeDef = TypedDict(
    "NodeSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Status": NotRequired[NodeStatusType],
        "CreationDate": NotRequired[datetime],
        "AvailabilityZone": NotRequired[str],
        "InstanceType": NotRequired[str],
        "Arn": NotRequired[str],
    },
)
ListProposalVotesInputRequestTypeDef = TypedDict(
    "ListProposalVotesInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
VoteSummaryTypeDef = TypedDict(
    "VoteSummaryTypeDef",
    {
        "Vote": NotRequired[VoteValueType],
        "MemberName": NotRequired[str],
        "MemberId": NotRequired[str],
    },
)
ListProposalsInputRequestTypeDef = TypedDict(
    "ListProposalsInputRequestTypeDef",
    {
        "NetworkId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ProposalSummaryTypeDef = TypedDict(
    "ProposalSummaryTypeDef",
    {
        "ProposalId": NotRequired[str],
        "Description": NotRequired[str],
        "ProposedByMemberId": NotRequired[str],
        "ProposedByMemberName": NotRequired[str],
        "Status": NotRequired[ProposalStatusType],
        "CreationDate": NotRequired[datetime],
        "ExpirationDate": NotRequired[datetime],
        "Arn": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
MemberFabricAttributesTypeDef = TypedDict(
    "MemberFabricAttributesTypeDef",
    {
        "AdminUsername": NotRequired[str],
        "CaEndpoint": NotRequired[str],
    },
)
MemberFabricConfigurationTypeDef = TypedDict(
    "MemberFabricConfigurationTypeDef",
    {
        "AdminUsername": str,
        "AdminPassword": str,
    },
)
NetworkEthereumAttributesTypeDef = TypedDict(
    "NetworkEthereumAttributesTypeDef",
    {
        "ChainId": NotRequired[str],
    },
)
NetworkFabricAttributesTypeDef = TypedDict(
    "NetworkFabricAttributesTypeDef",
    {
        "OrderingServiceEndpoint": NotRequired[str],
        "Edition": NotRequired[EditionType],
    },
)
NetworkFabricConfigurationTypeDef = TypedDict(
    "NetworkFabricConfigurationTypeDef",
    {
        "Edition": EditionType,
    },
)
NodeEthereumAttributesTypeDef = TypedDict(
    "NodeEthereumAttributesTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "WebSocketEndpoint": NotRequired[str],
    },
)
NodeFabricAttributesTypeDef = TypedDict(
    "NodeFabricAttributesTypeDef",
    {
        "PeerEndpoint": NotRequired[str],
        "PeerEventEndpoint": NotRequired[str],
    },
)
RemoveActionTypeDef = TypedDict(
    "RemoveActionTypeDef",
    {
        "MemberId": str,
    },
)
RejectInvitationInputRequestTypeDef = TypedDict(
    "RejectInvitationInputRequestTypeDef",
    {
        "InvitationId": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
VoteOnProposalInputRequestTypeDef = TypedDict(
    "VoteOnProposalInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
        "VoterMemberId": str,
        "Vote": VoteValueType,
    },
)
VotingPolicyTypeDef = TypedDict(
    "VotingPolicyTypeDef",
    {
        "ApprovalThresholdPolicy": NotRequired[ApprovalThresholdPolicyTypeDef],
    },
)
CreateAccessorOutputTypeDef = TypedDict(
    "CreateAccessorOutputTypeDef",
    {
        "AccessorId": str,
        "BillingToken": str,
        "NetworkType": AccessorNetworkTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMemberOutputTypeDef = TypedDict(
    "CreateMemberOutputTypeDef",
    {
        "MemberId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkOutputTypeDef = TypedDict(
    "CreateNetworkOutputTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNodeOutputTypeDef = TypedDict(
    "CreateNodeOutputTypeDef",
    {
        "NodeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProposalOutputTypeDef = TypedDict(
    "CreateProposalOutputTypeDef",
    {
        "ProposalId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessorOutputTypeDef = TypedDict(
    "GetAccessorOutputTypeDef",
    {
        "Accessor": AccessorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessorsOutputTypeDef = TypedDict(
    "ListAccessorsOutputTypeDef",
    {
        "Accessors": List[AccessorSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "InvitationId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "ExpirationDate": NotRequired[datetime],
        "Status": NotRequired[InvitationStatusType],
        "NetworkSummary": NotRequired[NetworkSummaryTypeDef],
        "Arn": NotRequired[str],
    },
)
ListNetworksOutputTypeDef = TypedDict(
    "ListNetworksOutputTypeDef",
    {
        "Networks": List[NetworkSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAccessorsInputListAccessorsPaginateTypeDef = TypedDict(
    "ListAccessorsInputListAccessorsPaginateTypeDef",
    {
        "NetworkType": NotRequired[AccessorNetworkTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMembersOutputTypeDef = TypedDict(
    "ListMembersOutputTypeDef",
    {
        "Members": List[MemberSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListNodesOutputTypeDef = TypedDict(
    "ListNodesOutputTypeDef",
    {
        "Nodes": List[NodeSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProposalVotesOutputTypeDef = TypedDict(
    "ListProposalVotesOutputTypeDef",
    {
        "ProposalVotes": List[VoteSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProposalsOutputTypeDef = TypedDict(
    "ListProposalsOutputTypeDef",
    {
        "Proposals": List[ProposalSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LogConfigurationsTypeDef = TypedDict(
    "LogConfigurationsTypeDef",
    {
        "Cloudwatch": NotRequired[LogConfigurationTypeDef],
    },
)
MemberFrameworkAttributesTypeDef = TypedDict(
    "MemberFrameworkAttributesTypeDef",
    {
        "Fabric": NotRequired[MemberFabricAttributesTypeDef],
    },
)
MemberFrameworkConfigurationTypeDef = TypedDict(
    "MemberFrameworkConfigurationTypeDef",
    {
        "Fabric": NotRequired[MemberFabricConfigurationTypeDef],
    },
)
NetworkFrameworkAttributesTypeDef = TypedDict(
    "NetworkFrameworkAttributesTypeDef",
    {
        "Fabric": NotRequired[NetworkFabricAttributesTypeDef],
        "Ethereum": NotRequired[NetworkEthereumAttributesTypeDef],
    },
)
NetworkFrameworkConfigurationTypeDef = TypedDict(
    "NetworkFrameworkConfigurationTypeDef",
    {
        "Fabric": NotRequired[NetworkFabricConfigurationTypeDef],
    },
)
NodeFrameworkAttributesTypeDef = TypedDict(
    "NodeFrameworkAttributesTypeDef",
    {
        "Fabric": NotRequired[NodeFabricAttributesTypeDef],
        "Ethereum": NotRequired[NodeEthereumAttributesTypeDef],
    },
)
ProposalActionsOutputTypeDef = TypedDict(
    "ProposalActionsOutputTypeDef",
    {
        "Invitations": NotRequired[List[InviteActionTypeDef]],
        "Removals": NotRequired[List[RemoveActionTypeDef]],
    },
)
ProposalActionsTypeDef = TypedDict(
    "ProposalActionsTypeDef",
    {
        "Invitations": NotRequired[Sequence[InviteActionTypeDef]],
        "Removals": NotRequired[Sequence[RemoveActionTypeDef]],
    },
)
ListInvitationsOutputTypeDef = TypedDict(
    "ListInvitationsOutputTypeDef",
    {
        "Invitations": List[InvitationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MemberFabricLogPublishingConfigurationTypeDef = TypedDict(
    "MemberFabricLogPublishingConfigurationTypeDef",
    {
        "CaLogs": NotRequired[LogConfigurationsTypeDef],
    },
)
NodeFabricLogPublishingConfigurationTypeDef = TypedDict(
    "NodeFabricLogPublishingConfigurationTypeDef",
    {
        "ChaincodeLogs": NotRequired[LogConfigurationsTypeDef],
        "PeerLogs": NotRequired[LogConfigurationsTypeDef],
    },
)
NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Framework": NotRequired[FrameworkType],
        "FrameworkVersion": NotRequired[str],
        "FrameworkAttributes": NotRequired[NetworkFrameworkAttributesTypeDef],
        "VpcEndpointServiceName": NotRequired[str],
        "VotingPolicy": NotRequired[VotingPolicyTypeDef],
        "Status": NotRequired[NetworkStatusType],
        "CreationDate": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
    },
)
ProposalTypeDef = TypedDict(
    "ProposalTypeDef",
    {
        "ProposalId": NotRequired[str],
        "NetworkId": NotRequired[str],
        "Description": NotRequired[str],
        "Actions": NotRequired[ProposalActionsOutputTypeDef],
        "ProposedByMemberId": NotRequired[str],
        "ProposedByMemberName": NotRequired[str],
        "Status": NotRequired[ProposalStatusType],
        "CreationDate": NotRequired[datetime],
        "ExpirationDate": NotRequired[datetime],
        "YesVoteCount": NotRequired[int],
        "NoVoteCount": NotRequired[int],
        "OutstandingVoteCount": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
    },
)
CreateProposalInputRequestTypeDef = TypedDict(
    "CreateProposalInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NetworkId": str,
        "MemberId": str,
        "Actions": ProposalActionsTypeDef,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
MemberLogPublishingConfigurationTypeDef = TypedDict(
    "MemberLogPublishingConfigurationTypeDef",
    {
        "Fabric": NotRequired[MemberFabricLogPublishingConfigurationTypeDef],
    },
)
NodeLogPublishingConfigurationTypeDef = TypedDict(
    "NodeLogPublishingConfigurationTypeDef",
    {
        "Fabric": NotRequired[NodeFabricLogPublishingConfigurationTypeDef],
    },
)
GetNetworkOutputTypeDef = TypedDict(
    "GetNetworkOutputTypeDef",
    {
        "Network": NetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProposalOutputTypeDef = TypedDict(
    "GetProposalOutputTypeDef",
    {
        "Proposal": ProposalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MemberConfigurationTypeDef = TypedDict(
    "MemberConfigurationTypeDef",
    {
        "Name": str,
        "FrameworkConfiguration": MemberFrameworkConfigurationTypeDef,
        "Description": NotRequired[str],
        "LogPublishingConfiguration": NotRequired[MemberLogPublishingConfigurationTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "KmsKeyArn": NotRequired[str],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "NetworkId": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "FrameworkAttributes": NotRequired[MemberFrameworkAttributesTypeDef],
        "LogPublishingConfiguration": NotRequired[MemberLogPublishingConfigurationTypeDef],
        "Status": NotRequired[MemberStatusType],
        "CreationDate": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
    },
)
UpdateMemberInputRequestTypeDef = TypedDict(
    "UpdateMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "LogPublishingConfiguration": NotRequired[MemberLogPublishingConfigurationTypeDef],
    },
)
NodeConfigurationTypeDef = TypedDict(
    "NodeConfigurationTypeDef",
    {
        "InstanceType": str,
        "AvailabilityZone": NotRequired[str],
        "LogPublishingConfiguration": NotRequired[NodeLogPublishingConfigurationTypeDef],
        "StateDB": NotRequired[StateDBTypeType],
    },
)
NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "NetworkId": NotRequired[str],
        "MemberId": NotRequired[str],
        "Id": NotRequired[str],
        "InstanceType": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "FrameworkAttributes": NotRequired[NodeFrameworkAttributesTypeDef],
        "LogPublishingConfiguration": NotRequired[NodeLogPublishingConfigurationTypeDef],
        "StateDB": NotRequired[StateDBTypeType],
        "Status": NotRequired[NodeStatusType],
        "CreationDate": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
    },
)
UpdateNodeInputRequestTypeDef = TypedDict(
    "UpdateNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
        "MemberId": NotRequired[str],
        "LogPublishingConfiguration": NotRequired[NodeLogPublishingConfigurationTypeDef],
    },
)
CreateMemberInputRequestTypeDef = TypedDict(
    "CreateMemberInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "InvitationId": str,
        "NetworkId": str,
        "MemberConfiguration": MemberConfigurationTypeDef,
    },
)
CreateNetworkInputRequestTypeDef = TypedDict(
    "CreateNetworkInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Name": str,
        "Framework": FrameworkType,
        "FrameworkVersion": str,
        "VotingPolicy": VotingPolicyTypeDef,
        "MemberConfiguration": MemberConfigurationTypeDef,
        "Description": NotRequired[str],
        "FrameworkConfiguration": NotRequired[NetworkFrameworkConfigurationTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
GetMemberOutputTypeDef = TypedDict(
    "GetMemberOutputTypeDef",
    {
        "Member": MemberTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNodeInputRequestTypeDef = TypedDict(
    "CreateNodeInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NetworkId": str,
        "NodeConfiguration": NodeConfigurationTypeDef,
        "MemberId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
GetNodeOutputTypeDef = TypedDict(
    "GetNodeOutputTypeDef",
    {
        "Node": NodeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
