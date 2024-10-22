"""
Type annotations for route53-recovery-control-config service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/type_defs/)

Usage::

    ```python
    from mypy_boto3_route53_recovery_control_config.type_defs import RuleConfigTypeDef

    data: RuleConfigTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import RuleTypeType, StatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "RuleConfigTypeDef",
    "AssertionRuleUpdateTypeDef",
    "ClusterEndpointTypeDef",
    "ControlPanelTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateControlPanelRequestRequestTypeDef",
    "CreateRoutingControlRequestRequestTypeDef",
    "RoutingControlTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteControlPanelRequestRequestTypeDef",
    "DeleteRoutingControlRequestRequestTypeDef",
    "DeleteSafetyRuleRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeControlPanelRequestRequestTypeDef",
    "DescribeRoutingControlRequestRequestTypeDef",
    "DescribeSafetyRuleRequestRequestTypeDef",
    "GatingRuleUpdateTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssociatedRoute53HealthChecksRequestRequestTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListControlPanelsRequestRequestTypeDef",
    "ListRoutingControlsRequestRequestTypeDef",
    "ListSafetyRulesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateControlPanelRequestRequestTypeDef",
    "UpdateRoutingControlRequestRequestTypeDef",
    "AssertionRuleTypeDef",
    "GatingRuleTypeDef",
    "NewAssertionRuleTypeDef",
    "NewGatingRuleTypeDef",
    "ClusterTypeDef",
    "CreateControlPanelResponseTypeDef",
    "DescribeControlPanelResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListAssociatedRoute53HealthChecksResponseTypeDef",
    "ListControlPanelsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateControlPanelResponseTypeDef",
    "CreateRoutingControlResponseTypeDef",
    "DescribeRoutingControlResponseTypeDef",
    "ListRoutingControlsResponseTypeDef",
    "UpdateRoutingControlResponseTypeDef",
    "DescribeClusterRequestClusterCreatedWaitTypeDef",
    "DescribeClusterRequestClusterDeletedWaitTypeDef",
    "DescribeControlPanelRequestControlPanelCreatedWaitTypeDef",
    "DescribeControlPanelRequestControlPanelDeletedWaitTypeDef",
    "DescribeRoutingControlRequestRoutingControlCreatedWaitTypeDef",
    "DescribeRoutingControlRequestRoutingControlDeletedWaitTypeDef",
    "UpdateSafetyRuleRequestRequestTypeDef",
    "ListAssociatedRoute53HealthChecksRequestListAssociatedRoute53HealthChecksPaginateTypeDef",
    "ListClustersRequestListClustersPaginateTypeDef",
    "ListControlPanelsRequestListControlPanelsPaginateTypeDef",
    "ListRoutingControlsRequestListRoutingControlsPaginateTypeDef",
    "ListSafetyRulesRequestListSafetyRulesPaginateTypeDef",
    "CreateSafetyRuleResponseTypeDef",
    "DescribeSafetyRuleResponseTypeDef",
    "RuleTypeDef",
    "UpdateSafetyRuleResponseTypeDef",
    "CreateSafetyRuleRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "DescribeClusterResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListSafetyRulesResponseTypeDef",
)

RuleConfigTypeDef = TypedDict(
    "RuleConfigTypeDef",
    {
        "Inverted": bool,
        "Threshold": int,
        "Type": RuleTypeType,
    },
)
AssertionRuleUpdateTypeDef = TypedDict(
    "AssertionRuleUpdateTypeDef",
    {
        "Name": str,
        "SafetyRuleArn": str,
        "WaitPeriodMs": int,
    },
)
ClusterEndpointTypeDef = TypedDict(
    "ClusterEndpointTypeDef",
    {
        "Endpoint": NotRequired[str],
        "Region": NotRequired[str],
    },
)
ControlPanelTypeDef = TypedDict(
    "ControlPanelTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "ControlPanelArn": NotRequired[str],
        "DefaultControlPanel": NotRequired[bool],
        "Name": NotRequired[str],
        "RoutingControlCount": NotRequired[int],
        "Status": NotRequired[StatusType],
        "Owner": NotRequired[str],
    },
)
CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
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
CreateControlPanelRequestRequestTypeDef = TypedDict(
    "CreateControlPanelRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ControlPanelName": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateRoutingControlRequestRequestTypeDef = TypedDict(
    "CreateRoutingControlRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "RoutingControlName": str,
        "ClientToken": NotRequired[str],
        "ControlPanelArn": NotRequired[str],
    },
)
RoutingControlTypeDef = TypedDict(
    "RoutingControlTypeDef",
    {
        "ControlPanelArn": NotRequired[str],
        "Name": NotRequired[str],
        "RoutingControlArn": NotRequired[str],
        "Status": NotRequired[StatusType],
        "Owner": NotRequired[str],
    },
)
DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
DeleteControlPanelRequestRequestTypeDef = TypedDict(
    "DeleteControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
    },
)
DeleteRoutingControlRequestRequestTypeDef = TypedDict(
    "DeleteRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)
DeleteSafetyRuleRequestRequestTypeDef = TypedDict(
    "DeleteSafetyRuleRequestRequestTypeDef",
    {
        "SafetyRuleArn": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
DescribeControlPanelRequestRequestTypeDef = TypedDict(
    "DescribeControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
    },
)
DescribeRoutingControlRequestRequestTypeDef = TypedDict(
    "DescribeRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)
DescribeSafetyRuleRequestRequestTypeDef = TypedDict(
    "DescribeSafetyRuleRequestRequestTypeDef",
    {
        "SafetyRuleArn": str,
    },
)
GatingRuleUpdateTypeDef = TypedDict(
    "GatingRuleUpdateTypeDef",
    {
        "Name": str,
        "SafetyRuleArn": str,
        "WaitPeriodMs": int,
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
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
ListAssociatedRoute53HealthChecksRequestRequestTypeDef = TypedDict(
    "ListAssociatedRoute53HealthChecksRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListControlPanelsRequestRequestTypeDef = TypedDict(
    "ListControlPanelsRequestRequestTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRoutingControlsRequestRequestTypeDef = TypedDict(
    "ListRoutingControlsRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSafetyRulesRequestRequestTypeDef = TypedDict(
    "ListSafetyRulesRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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
UpdateControlPanelRequestRequestTypeDef = TypedDict(
    "UpdateControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
        "ControlPanelName": str,
    },
)
UpdateRoutingControlRequestRequestTypeDef = TypedDict(
    "UpdateRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlName": str,
    },
)
AssertionRuleTypeDef = TypedDict(
    "AssertionRuleTypeDef",
    {
        "AssertedControls": List[str],
        "ControlPanelArn": str,
        "Name": str,
        "RuleConfig": RuleConfigTypeDef,
        "SafetyRuleArn": str,
        "Status": StatusType,
        "WaitPeriodMs": int,
        "Owner": NotRequired[str],
    },
)
GatingRuleTypeDef = TypedDict(
    "GatingRuleTypeDef",
    {
        "ControlPanelArn": str,
        "GatingControls": List[str],
        "Name": str,
        "RuleConfig": RuleConfigTypeDef,
        "SafetyRuleArn": str,
        "Status": StatusType,
        "TargetControls": List[str],
        "WaitPeriodMs": int,
        "Owner": NotRequired[str],
    },
)
NewAssertionRuleTypeDef = TypedDict(
    "NewAssertionRuleTypeDef",
    {
        "AssertedControls": Sequence[str],
        "ControlPanelArn": str,
        "Name": str,
        "RuleConfig": RuleConfigTypeDef,
        "WaitPeriodMs": int,
    },
)
NewGatingRuleTypeDef = TypedDict(
    "NewGatingRuleTypeDef",
    {
        "ControlPanelArn": str,
        "GatingControls": Sequence[str],
        "Name": str,
        "RuleConfig": RuleConfigTypeDef,
        "TargetControls": Sequence[str],
        "WaitPeriodMs": int,
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "ClusterEndpoints": NotRequired[List[ClusterEndpointTypeDef]],
        "Name": NotRequired[str],
        "Status": NotRequired[StatusType],
        "Owner": NotRequired[str],
    },
)
CreateControlPanelResponseTypeDef = TypedDict(
    "CreateControlPanelResponseTypeDef",
    {
        "ControlPanel": ControlPanelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeControlPanelResponseTypeDef = TypedDict(
    "DescribeControlPanelResponseTypeDef",
    {
        "ControlPanel": ControlPanelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssociatedRoute53HealthChecksResponseTypeDef = TypedDict(
    "ListAssociatedRoute53HealthChecksResponseTypeDef",
    {
        "HealthCheckIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListControlPanelsResponseTypeDef = TypedDict(
    "ListControlPanelsResponseTypeDef",
    {
        "ControlPanels": List[ControlPanelTypeDef],
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
UpdateControlPanelResponseTypeDef = TypedDict(
    "UpdateControlPanelResponseTypeDef",
    {
        "ControlPanel": ControlPanelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRoutingControlResponseTypeDef = TypedDict(
    "CreateRoutingControlResponseTypeDef",
    {
        "RoutingControl": RoutingControlTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRoutingControlResponseTypeDef = TypedDict(
    "DescribeRoutingControlResponseTypeDef",
    {
        "RoutingControl": RoutingControlTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRoutingControlsResponseTypeDef = TypedDict(
    "ListRoutingControlsResponseTypeDef",
    {
        "RoutingControls": List[RoutingControlTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateRoutingControlResponseTypeDef = TypedDict(
    "UpdateRoutingControlResponseTypeDef",
    {
        "RoutingControl": RoutingControlTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClusterRequestClusterCreatedWaitTypeDef = TypedDict(
    "DescribeClusterRequestClusterCreatedWaitTypeDef",
    {
        "ClusterArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeClusterRequestClusterDeletedWaitTypeDef = TypedDict(
    "DescribeClusterRequestClusterDeletedWaitTypeDef",
    {
        "ClusterArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeControlPanelRequestControlPanelCreatedWaitTypeDef = TypedDict(
    "DescribeControlPanelRequestControlPanelCreatedWaitTypeDef",
    {
        "ControlPanelArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeControlPanelRequestControlPanelDeletedWaitTypeDef = TypedDict(
    "DescribeControlPanelRequestControlPanelDeletedWaitTypeDef",
    {
        "ControlPanelArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeRoutingControlRequestRoutingControlCreatedWaitTypeDef = TypedDict(
    "DescribeRoutingControlRequestRoutingControlCreatedWaitTypeDef",
    {
        "RoutingControlArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeRoutingControlRequestRoutingControlDeletedWaitTypeDef = TypedDict(
    "DescribeRoutingControlRequestRoutingControlDeletedWaitTypeDef",
    {
        "RoutingControlArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
UpdateSafetyRuleRequestRequestTypeDef = TypedDict(
    "UpdateSafetyRuleRequestRequestTypeDef",
    {
        "AssertionRuleUpdate": NotRequired[AssertionRuleUpdateTypeDef],
        "GatingRuleUpdate": NotRequired[GatingRuleUpdateTypeDef],
    },
)
ListAssociatedRoute53HealthChecksRequestListAssociatedRoute53HealthChecksPaginateTypeDef = (
    TypedDict(
        "ListAssociatedRoute53HealthChecksRequestListAssociatedRoute53HealthChecksPaginateTypeDef",
        {
            "RoutingControlArn": str,
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListClustersRequestListClustersPaginateTypeDef = TypedDict(
    "ListClustersRequestListClustersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListControlPanelsRequestListControlPanelsPaginateTypeDef = TypedDict(
    "ListControlPanelsRequestListControlPanelsPaginateTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRoutingControlsRequestListRoutingControlsPaginateTypeDef = TypedDict(
    "ListRoutingControlsRequestListRoutingControlsPaginateTypeDef",
    {
        "ControlPanelArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSafetyRulesRequestListSafetyRulesPaginateTypeDef = TypedDict(
    "ListSafetyRulesRequestListSafetyRulesPaginateTypeDef",
    {
        "ControlPanelArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
CreateSafetyRuleResponseTypeDef = TypedDict(
    "CreateSafetyRuleResponseTypeDef",
    {
        "AssertionRule": AssertionRuleTypeDef,
        "GatingRule": GatingRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSafetyRuleResponseTypeDef = TypedDict(
    "DescribeSafetyRuleResponseTypeDef",
    {
        "AssertionRule": AssertionRuleTypeDef,
        "GatingRule": GatingRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "ASSERTION": NotRequired[AssertionRuleTypeDef],
        "GATING": NotRequired[GatingRuleTypeDef],
    },
)
UpdateSafetyRuleResponseTypeDef = TypedDict(
    "UpdateSafetyRuleResponseTypeDef",
    {
        "AssertionRule": AssertionRuleTypeDef,
        "GatingRule": GatingRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSafetyRuleRequestRequestTypeDef = TypedDict(
    "CreateSafetyRuleRequestRequestTypeDef",
    {
        "AssertionRule": NotRequired[NewAssertionRuleTypeDef],
        "ClientToken": NotRequired[str],
        "GatingRule": NotRequired[NewGatingRuleTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "Clusters": List[ClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSafetyRulesResponseTypeDef = TypedDict(
    "ListSafetyRulesResponseTypeDef",
    {
        "SafetyRules": List[RuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
