"""
Type annotations for budgets service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/type_defs/)

Usage::

    ```python
    from mypy_boto3_budgets.type_defs import ActionThresholdTypeDef

    data: ActionThresholdTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionStatusType,
    ActionSubTypeType,
    ActionTypeType,
    ApprovalModelType,
    AutoAdjustTypeType,
    BudgetTypeType,
    ComparisonOperatorType,
    EventTypeType,
    ExecutionTypeType,
    NotificationStateType,
    NotificationTypeType,
    SubscriptionTypeType,
    ThresholdTypeType,
    TimeUnitType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ActionThresholdTypeDef",
    "SubscriberTypeDef",
    "HistoricalOptionsTypeDef",
    "TimestampTypeDef",
    "NotificationTypeDef",
    "CostTypesTypeDef",
    "SpendTypeDef",
    "TimePeriodOutputTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "IamActionDefinitionOutputTypeDef",
    "ScpActionDefinitionOutputTypeDef",
    "SsmActionDefinitionOutputTypeDef",
    "DeleteBudgetActionRequestRequestTypeDef",
    "DeleteBudgetRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeBudgetActionRequestRequestTypeDef",
    "DescribeBudgetActionsForAccountRequestRequestTypeDef",
    "DescribeBudgetActionsForBudgetRequestRequestTypeDef",
    "DescribeBudgetNotificationsForAccountRequestRequestTypeDef",
    "DescribeBudgetRequestRequestTypeDef",
    "DescribeBudgetsRequestRequestTypeDef",
    "DescribeNotificationsForBudgetRequestRequestTypeDef",
    "ExecuteBudgetActionRequestRequestTypeDef",
    "IamActionDefinitionTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ScpActionDefinitionTypeDef",
    "SsmActionDefinitionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AutoAdjustDataOutputTypeDef",
    "AutoAdjustDataTypeDef",
    "TimePeriodTypeDef",
    "BudgetNotificationsForAccountTypeDef",
    "CreateNotificationRequestRequestTypeDef",
    "CreateSubscriberRequestRequestTypeDef",
    "DeleteNotificationRequestRequestTypeDef",
    "DeleteSubscriberRequestRequestTypeDef",
    "DescribeSubscribersForNotificationRequestRequestTypeDef",
    "NotificationWithSubscribersTypeDef",
    "UpdateNotificationRequestRequestTypeDef",
    "UpdateSubscriberRequestRequestTypeDef",
    "CalculatedSpendTypeDef",
    "BudgetedAndActualAmountsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateBudgetActionResponseTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "ExecuteBudgetActionResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "DefinitionOutputTypeDef",
    "DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef",
    "DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef",
    "DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef",
    "DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef",
    "DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef",
    "DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef",
    "IamActionDefinitionUnionTypeDef",
    "ScpActionDefinitionUnionTypeDef",
    "SsmActionDefinitionUnionTypeDef",
    "AutoAdjustDataUnionTypeDef",
    "DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef",
    "DescribeBudgetActionHistoriesRequestRequestTypeDef",
    "DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef",
    "DescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    "TimePeriodUnionTypeDef",
    "DescribeBudgetNotificationsForAccountResponseTypeDef",
    "BudgetOutputTypeDef",
    "BudgetPerformanceHistoryTypeDef",
    "ActionTypeDef",
    "DefinitionTypeDef",
    "BudgetTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "ActionHistoryDetailsTypeDef",
    "DeleteBudgetActionResponseTypeDef",
    "DescribeBudgetActionResponseTypeDef",
    "DescribeBudgetActionsForAccountResponseTypeDef",
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    "UpdateBudgetActionResponseTypeDef",
    "CreateBudgetActionRequestRequestTypeDef",
    "UpdateBudgetActionRequestRequestTypeDef",
    "CreateBudgetRequestRequestTypeDef",
    "UpdateBudgetRequestRequestTypeDef",
    "ActionHistoryTypeDef",
    "DescribeBudgetActionHistoriesResponseTypeDef",
)

ActionThresholdTypeDef = TypedDict(
    "ActionThresholdTypeDef",
    {
        "ActionThresholdValue": float,
        "ActionThresholdType": ThresholdTypeType,
    },
)
SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "SubscriptionType": SubscriptionTypeType,
        "Address": str,
    },
)
HistoricalOptionsTypeDef = TypedDict(
    "HistoricalOptionsTypeDef",
    {
        "BudgetAdjustmentPeriod": int,
        "LookBackAvailablePeriods": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "NotificationType": NotificationTypeType,
        "ComparisonOperator": ComparisonOperatorType,
        "Threshold": float,
        "ThresholdType": NotRequired[ThresholdTypeType],
        "NotificationState": NotRequired[NotificationStateType],
    },
)
CostTypesTypeDef = TypedDict(
    "CostTypesTypeDef",
    {
        "IncludeTax": NotRequired[bool],
        "IncludeSubscription": NotRequired[bool],
        "UseBlended": NotRequired[bool],
        "IncludeRefund": NotRequired[bool],
        "IncludeCredit": NotRequired[bool],
        "IncludeUpfront": NotRequired[bool],
        "IncludeRecurring": NotRequired[bool],
        "IncludeOtherSubscription": NotRequired[bool],
        "IncludeSupport": NotRequired[bool],
        "IncludeDiscount": NotRequired[bool],
        "UseAmortized": NotRequired[bool],
    },
)
SpendTypeDef = TypedDict(
    "SpendTypeDef",
    {
        "Amount": str,
        "Unit": str,
    },
)
TimePeriodOutputTypeDef = TypedDict(
    "TimePeriodOutputTypeDef",
    {
        "Start": NotRequired[datetime],
        "End": NotRequired[datetime],
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
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
IamActionDefinitionOutputTypeDef = TypedDict(
    "IamActionDefinitionOutputTypeDef",
    {
        "PolicyArn": str,
        "Roles": NotRequired[List[str]],
        "Groups": NotRequired[List[str]],
        "Users": NotRequired[List[str]],
    },
)
ScpActionDefinitionOutputTypeDef = TypedDict(
    "ScpActionDefinitionOutputTypeDef",
    {
        "PolicyId": str,
        "TargetIds": List[str],
    },
)
SsmActionDefinitionOutputTypeDef = TypedDict(
    "SsmActionDefinitionOutputTypeDef",
    {
        "ActionSubType": ActionSubTypeType,
        "Region": str,
        "InstanceIds": List[str],
    },
)
DeleteBudgetActionRequestRequestTypeDef = TypedDict(
    "DeleteBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)
DeleteBudgetRequestRequestTypeDef = TypedDict(
    "DeleteBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
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
DescribeBudgetActionRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)
DescribeBudgetActionsForAccountRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetActionsForBudgetRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetNotificationsForAccountRequestRequestTypeDef = TypedDict(
    "DescribeBudgetNotificationsForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetRequestRequestTypeDef = TypedDict(
    "DescribeBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)
DescribeBudgetsRequestRequestTypeDef = TypedDict(
    "DescribeBudgetsRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeNotificationsForBudgetRequestRequestTypeDef = TypedDict(
    "DescribeNotificationsForBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ExecuteBudgetActionRequestRequestTypeDef = TypedDict(
    "ExecuteBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
    },
)
IamActionDefinitionTypeDef = TypedDict(
    "IamActionDefinitionTypeDef",
    {
        "PolicyArn": str,
        "Roles": NotRequired[Sequence[str]],
        "Groups": NotRequired[Sequence[str]],
        "Users": NotRequired[Sequence[str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
ScpActionDefinitionTypeDef = TypedDict(
    "ScpActionDefinitionTypeDef",
    {
        "PolicyId": str,
        "TargetIds": Sequence[str],
    },
)
SsmActionDefinitionTypeDef = TypedDict(
    "SsmActionDefinitionTypeDef",
    {
        "ActionSubType": ActionSubTypeType,
        "Region": str,
        "InstanceIds": Sequence[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "ResourceTagKeys": Sequence[str],
    },
)
AutoAdjustDataOutputTypeDef = TypedDict(
    "AutoAdjustDataOutputTypeDef",
    {
        "AutoAdjustType": AutoAdjustTypeType,
        "HistoricalOptions": NotRequired[HistoricalOptionsTypeDef],
        "LastAutoAdjustTime": NotRequired[datetime],
    },
)
AutoAdjustDataTypeDef = TypedDict(
    "AutoAdjustDataTypeDef",
    {
        "AutoAdjustType": AutoAdjustTypeType,
        "HistoricalOptions": NotRequired[HistoricalOptionsTypeDef],
        "LastAutoAdjustTime": NotRequired[TimestampTypeDef],
    },
)
TimePeriodTypeDef = TypedDict(
    "TimePeriodTypeDef",
    {
        "Start": NotRequired[TimestampTypeDef],
        "End": NotRequired[TimestampTypeDef],
    },
)
BudgetNotificationsForAccountTypeDef = TypedDict(
    "BudgetNotificationsForAccountTypeDef",
    {
        "Notifications": NotRequired[List[NotificationTypeDef]],
        "BudgetName": NotRequired[str],
    },
)
CreateNotificationRequestRequestTypeDef = TypedDict(
    "CreateNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "Subscribers": Sequence[SubscriberTypeDef],
    },
)
CreateSubscriberRequestRequestTypeDef = TypedDict(
    "CreateSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "Subscriber": SubscriberTypeDef,
    },
)
DeleteNotificationRequestRequestTypeDef = TypedDict(
    "DeleteNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
    },
)
DeleteSubscriberRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "Subscriber": SubscriberTypeDef,
    },
)
DescribeSubscribersForNotificationRequestRequestTypeDef = TypedDict(
    "DescribeSubscribersForNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NotificationWithSubscribersTypeDef = TypedDict(
    "NotificationWithSubscribersTypeDef",
    {
        "Notification": NotificationTypeDef,
        "Subscribers": Sequence[SubscriberTypeDef],
    },
)
UpdateNotificationRequestRequestTypeDef = TypedDict(
    "UpdateNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldNotification": NotificationTypeDef,
        "NewNotification": NotificationTypeDef,
    },
)
UpdateSubscriberRequestRequestTypeDef = TypedDict(
    "UpdateSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "OldSubscriber": SubscriberTypeDef,
        "NewSubscriber": SubscriberTypeDef,
    },
)
CalculatedSpendTypeDef = TypedDict(
    "CalculatedSpendTypeDef",
    {
        "ActualSpend": SpendTypeDef,
        "ForecastedSpend": NotRequired[SpendTypeDef],
    },
)
BudgetedAndActualAmountsTypeDef = TypedDict(
    "BudgetedAndActualAmountsTypeDef",
    {
        "BudgetedAmount": NotRequired[SpendTypeDef],
        "ActualAmount": NotRequired[SpendTypeDef],
        "TimePeriod": NotRequired[TimePeriodOutputTypeDef],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "ResourceTags": Sequence[ResourceTagTypeDef],
    },
)
CreateBudgetActionResponseTypeDef = TypedDict(
    "CreateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "DescribeNotificationsForBudgetResponseTypeDef",
    {
        "Notifications": List[NotificationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "DescribeSubscribersForNotificationResponseTypeDef",
    {
        "Subscribers": List[SubscriberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExecuteBudgetActionResponseTypeDef = TypedDict(
    "ExecuteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceTags": List[ResourceTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefinitionOutputTypeDef = TypedDict(
    "DefinitionOutputTypeDef",
    {
        "IamActionDefinition": NotRequired[IamActionDefinitionOutputTypeDef],
        "ScpActionDefinition": NotRequired[ScpActionDefinitionOutputTypeDef],
        "SsmActionDefinition": NotRequired[SsmActionDefinitionOutputTypeDef],
    },
)
DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef",
    {
        "AccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef = TypedDict(
    "DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef",
    {
        "AccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef = TypedDict(
    "DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef",
    {
        "AccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef = TypedDict(
    "DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef = TypedDict(
    "DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
IamActionDefinitionUnionTypeDef = Union[
    IamActionDefinitionTypeDef, IamActionDefinitionOutputTypeDef
]
ScpActionDefinitionUnionTypeDef = Union[
    ScpActionDefinitionTypeDef, ScpActionDefinitionOutputTypeDef
]
SsmActionDefinitionUnionTypeDef = Union[
    SsmActionDefinitionTypeDef, SsmActionDefinitionOutputTypeDef
]
AutoAdjustDataUnionTypeDef = Union[AutoAdjustDataTypeDef, AutoAdjustDataOutputTypeDef]
DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetActionHistoriesRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetPerformanceHistoryRequestRequestTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimePeriodUnionTypeDef = Union[TimePeriodTypeDef, TimePeriodOutputTypeDef]
DescribeBudgetNotificationsForAccountResponseTypeDef = TypedDict(
    "DescribeBudgetNotificationsForAccountResponseTypeDef",
    {
        "BudgetNotificationsForAccount": List[BudgetNotificationsForAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BudgetOutputTypeDef = TypedDict(
    "BudgetOutputTypeDef",
    {
        "BudgetName": str,
        "TimeUnit": TimeUnitType,
        "BudgetType": BudgetTypeType,
        "BudgetLimit": NotRequired[SpendTypeDef],
        "PlannedBudgetLimits": NotRequired[Dict[str, SpendTypeDef]],
        "CostFilters": NotRequired[Dict[str, List[str]]],
        "CostTypes": NotRequired[CostTypesTypeDef],
        "TimePeriod": NotRequired[TimePeriodOutputTypeDef],
        "CalculatedSpend": NotRequired[CalculatedSpendTypeDef],
        "LastUpdatedTime": NotRequired[datetime],
        "AutoAdjustData": NotRequired[AutoAdjustDataOutputTypeDef],
    },
)
BudgetPerformanceHistoryTypeDef = TypedDict(
    "BudgetPerformanceHistoryTypeDef",
    {
        "BudgetName": NotRequired[str],
        "BudgetType": NotRequired[BudgetTypeType],
        "CostFilters": NotRequired[Dict[str, List[str]]],
        "CostTypes": NotRequired[CostTypesTypeDef],
        "TimeUnit": NotRequired[TimeUnitType],
        "BudgetedAndActualAmountsList": NotRequired[List[BudgetedAndActualAmountsTypeDef]],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": ActionThresholdTypeDef,
        "Definition": DefinitionOutputTypeDef,
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Status": ActionStatusType,
        "Subscribers": List[SubscriberTypeDef],
    },
)
DefinitionTypeDef = TypedDict(
    "DefinitionTypeDef",
    {
        "IamActionDefinition": NotRequired[IamActionDefinitionUnionTypeDef],
        "ScpActionDefinition": NotRequired[ScpActionDefinitionUnionTypeDef],
        "SsmActionDefinition": NotRequired[SsmActionDefinitionUnionTypeDef],
    },
)
BudgetTypeDef = TypedDict(
    "BudgetTypeDef",
    {
        "BudgetName": str,
        "TimeUnit": TimeUnitType,
        "BudgetType": BudgetTypeType,
        "BudgetLimit": NotRequired[SpendTypeDef],
        "PlannedBudgetLimits": NotRequired[Mapping[str, SpendTypeDef]],
        "CostFilters": NotRequired[Mapping[str, Sequence[str]]],
        "CostTypes": NotRequired[CostTypesTypeDef],
        "TimePeriod": NotRequired[TimePeriodUnionTypeDef],
        "CalculatedSpend": NotRequired[CalculatedSpendTypeDef],
        "LastUpdatedTime": NotRequired[TimestampTypeDef],
        "AutoAdjustData": NotRequired[AutoAdjustDataUnionTypeDef],
    },
)
DescribeBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetResponseTypeDef",
    {
        "Budget": BudgetOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetsResponseTypeDef = TypedDict(
    "DescribeBudgetsResponseTypeDef",
    {
        "Budgets": List[BudgetOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    {
        "BudgetPerformanceHistory": BudgetPerformanceHistoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ActionHistoryDetailsTypeDef = TypedDict(
    "ActionHistoryDetailsTypeDef",
    {
        "Message": str,
        "Action": ActionTypeDef,
    },
)
DeleteBudgetActionResponseTypeDef = TypedDict(
    "DeleteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": ActionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetActionResponseTypeDef = TypedDict(
    "DescribeBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": ActionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetActionsForAccountResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountResponseTypeDef",
    {
        "Actions": List[ActionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetActionsForBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    {
        "Actions": List[ActionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateBudgetActionResponseTypeDef = TypedDict(
    "UpdateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldAction": ActionTypeDef,
        "NewAction": ActionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBudgetActionRequestRequestTypeDef = TypedDict(
    "CreateBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": ActionThresholdTypeDef,
        "Definition": DefinitionTypeDef,
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Subscribers": Sequence[SubscriberTypeDef],
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
UpdateBudgetActionRequestRequestTypeDef = TypedDict(
    "UpdateBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "NotificationType": NotRequired[NotificationTypeType],
        "ActionThreshold": NotRequired[ActionThresholdTypeDef],
        "Definition": NotRequired[DefinitionTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "ApprovalModel": NotRequired[ApprovalModelType],
        "Subscribers": NotRequired[Sequence[SubscriberTypeDef]],
    },
)
CreateBudgetRequestRequestTypeDef = TypedDict(
    "CreateBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "Budget": BudgetTypeDef,
        "NotificationsWithSubscribers": NotRequired[Sequence[NotificationWithSubscribersTypeDef]],
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
UpdateBudgetRequestRequestTypeDef = TypedDict(
    "UpdateBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "NewBudget": BudgetTypeDef,
    },
)
ActionHistoryTypeDef = TypedDict(
    "ActionHistoryTypeDef",
    {
        "Timestamp": datetime,
        "Status": ActionStatusType,
        "EventType": EventTypeType,
        "ActionHistoryDetails": ActionHistoryDetailsTypeDef,
    },
)
DescribeBudgetActionHistoriesResponseTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesResponseTypeDef",
    {
        "ActionHistories": List[ActionHistoryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
