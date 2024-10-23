"""
Type annotations for appintegrations service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/type_defs/)

Usage::

    ```python
    from mypy_boto3_appintegrations.type_defs import ApplicationAssociationSummaryTypeDef

    data: ApplicationAssociationSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import ExecutionModeType, ExecutionStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ApplicationAssociationSummaryTypeDef",
    "ExternalUrlConfigOutputTypeDef",
    "ApplicationSummaryTypeDef",
    "PublicationTypeDef",
    "SubscriptionTypeDef",
    "ResponseMetadataTypeDef",
    "FileConfigurationTypeDef",
    "ScheduleConfigurationTypeDef",
    "FileConfigurationOutputTypeDef",
    "EventFilterTypeDef",
    "LastExecutionStatusTypeDef",
    "DataIntegrationSummaryTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteDataIntegrationRequestRequestTypeDef",
    "DeleteEventIntegrationRequestRequestTypeDef",
    "EventIntegrationAssociationTypeDef",
    "OnDemandConfigurationTypeDef",
    "ExternalUrlConfigTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetDataIntegrationRequestRequestTypeDef",
    "GetEventIntegrationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationAssociationsRequestRequestTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListDataIntegrationAssociationsRequestRequestTypeDef",
    "ListDataIntegrationsRequestRequestTypeDef",
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    "ListEventIntegrationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataIntegrationRequestRequestTypeDef",
    "UpdateEventIntegrationRequestRequestTypeDef",
    "ApplicationSourceConfigOutputTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDataIntegrationAssociationResponseTypeDef",
    "CreateEventIntegrationResponseTypeDef",
    "ListApplicationAssociationsResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateDataIntegrationRequestRequestTypeDef",
    "CreateDataIntegrationResponseTypeDef",
    "GetDataIntegrationResponseTypeDef",
    "CreateEventIntegrationRequestRequestTypeDef",
    "EventIntegrationTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "ListDataIntegrationsResponseTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ExecutionConfigurationTypeDef",
    "ExternalUrlConfigUnionTypeDef",
    "ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef",
    "ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef",
    "ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef",
    "ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef",
    "GetApplicationResponseTypeDef",
    "ListEventIntegrationsResponseTypeDef",
    "CreateDataIntegrationAssociationRequestRequestTypeDef",
    "DataIntegrationAssociationSummaryTypeDef",
    "UpdateDataIntegrationAssociationRequestRequestTypeDef",
    "ApplicationSourceConfigTypeDef",
    "ListDataIntegrationAssociationsResponseTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
)

ApplicationAssociationSummaryTypeDef = TypedDict(
    "ApplicationAssociationSummaryTypeDef",
    {
        "ApplicationAssociationArn": NotRequired[str],
        "ApplicationArn": NotRequired[str],
        "ClientId": NotRequired[str],
    },
)
ExternalUrlConfigOutputTypeDef = TypedDict(
    "ExternalUrlConfigOutputTypeDef",
    {
        "AccessUrl": str,
        "ApprovedOrigins": NotRequired[List[str]],
    },
)
ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Namespace": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)
PublicationTypeDef = TypedDict(
    "PublicationTypeDef",
    {
        "Event": str,
        "Schema": str,
        "Description": NotRequired[str],
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "Event": str,
        "Description": NotRequired[str],
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
FileConfigurationTypeDef = TypedDict(
    "FileConfigurationTypeDef",
    {
        "Folders": Sequence[str],
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
    },
)
ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "ScheduleExpression": str,
        "FirstExecutionFrom": NotRequired[str],
        "Object": NotRequired[str],
    },
)
FileConfigurationOutputTypeDef = TypedDict(
    "FileConfigurationOutputTypeDef",
    {
        "Folders": List[str],
        "Filters": NotRequired[Dict[str, List[str]]],
    },
)
EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Source": str,
    },
)
LastExecutionStatusTypeDef = TypedDict(
    "LastExecutionStatusTypeDef",
    {
        "ExecutionStatus": NotRequired[ExecutionStatusType],
        "StatusMessage": NotRequired[str],
    },
)
DataIntegrationSummaryTypeDef = TypedDict(
    "DataIntegrationSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "SourceURI": NotRequired[str],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
DeleteDataIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteDataIntegrationRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
    },
)
DeleteEventIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
EventIntegrationAssociationTypeDef = TypedDict(
    "EventIntegrationAssociationTypeDef",
    {
        "EventIntegrationAssociationArn": NotRequired[str],
        "EventIntegrationAssociationId": NotRequired[str],
        "EventIntegrationName": NotRequired[str],
        "ClientId": NotRequired[str],
        "EventBridgeRuleName": NotRequired[str],
        "ClientAssociationMetadata": NotRequired[Dict[str, str]],
    },
)
OnDemandConfigurationTypeDef = TypedDict(
    "OnDemandConfigurationTypeDef",
    {
        "StartTime": str,
        "EndTime": NotRequired[str],
    },
)
ExternalUrlConfigTypeDef = TypedDict(
    "ExternalUrlConfigTypeDef",
    {
        "AccessUrl": str,
        "ApprovedOrigins": NotRequired[Sequence[str]],
    },
)
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
GetDataIntegrationRequestRequestTypeDef = TypedDict(
    "GetDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetEventIntegrationRequestRequestTypeDef = TypedDict(
    "GetEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
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
ListApplicationAssociationsRequestRequestTypeDef = TypedDict(
    "ListApplicationAssociationsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "ListDataIntegrationAssociationsRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataIntegrationsRequestRequestTypeDef = TypedDict(
    "ListDataIntegrationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "EventIntegrationName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEventIntegrationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateDataIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
    },
)
ApplicationSourceConfigOutputTypeDef = TypedDict(
    "ApplicationSourceConfigOutputTypeDef",
    {
        "ExternalUrlConfig": NotRequired[ExternalUrlConfigOutputTypeDef],
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataIntegrationAssociationResponseTypeDef = TypedDict(
    "CreateDataIntegrationAssociationResponseTypeDef",
    {
        "DataIntegrationAssociationId": str,
        "DataIntegrationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventIntegrationResponseTypeDef = TypedDict(
    "CreateEventIntegrationResponseTypeDef",
    {
        "EventIntegrationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationAssociationsResponseTypeDef = TypedDict(
    "ListApplicationAssociationsResponseTypeDef",
    {
        "ApplicationAssociations": List[ApplicationAssociationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "Applications": List[ApplicationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataIntegrationRequestRequestTypeDef = TypedDict(
    "CreateDataIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "KmsKey": str,
        "Description": NotRequired[str],
        "SourceURI": NotRequired[str],
        "ScheduleConfig": NotRequired[ScheduleConfigurationTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "ClientToken": NotRequired[str],
        "FileConfiguration": NotRequired[FileConfigurationTypeDef],
        "ObjectConfiguration": NotRequired[Mapping[str, Mapping[str, Sequence[str]]]],
    },
)
CreateDataIntegrationResponseTypeDef = TypedDict(
    "CreateDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "Tags": Dict[str, str],
        "ClientToken": str,
        "FileConfiguration": FileConfigurationOutputTypeDef,
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataIntegrationResponseTypeDef = TypedDict(
    "GetDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "Tags": Dict[str, str],
        "FileConfiguration": FileConfigurationOutputTypeDef,
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "CreateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "EventFilter": EventFilterTypeDef,
        "EventBridgeBus": str,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
EventIntegrationTypeDef = TypedDict(
    "EventIntegrationTypeDef",
    {
        "EventIntegrationArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EventFilter": NotRequired[EventFilterTypeDef],
        "EventBridgeBus": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
GetEventIntegrationResponseTypeDef = TypedDict(
    "GetEventIntegrationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "EventIntegrationArn": str,
        "EventBridgeBus": str,
        "EventFilter": EventFilterTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataIntegrationsResponseTypeDef = TypedDict(
    "ListDataIntegrationsResponseTypeDef",
    {
        "DataIntegrations": List[DataIntegrationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEventIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListEventIntegrationAssociationsResponseTypeDef",
    {
        "EventIntegrationAssociations": List[EventIntegrationAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExecutionConfigurationTypeDef = TypedDict(
    "ExecutionConfigurationTypeDef",
    {
        "ExecutionMode": ExecutionModeType,
        "OnDemandConfiguration": NotRequired[OnDemandConfigurationTypeDef],
        "ScheduleConfiguration": NotRequired[ScheduleConfigurationTypeDef],
    },
)
ExternalUrlConfigUnionTypeDef = Union[ExternalUrlConfigTypeDef, ExternalUrlConfigOutputTypeDef]
ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef = TypedDict(
    "ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef",
    {
        "ApplicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef = TypedDict(
    "ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef",
    {
        "DataIntegrationIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef = TypedDict(
    "ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef = TypedDict(
    "ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef",
    {
        "EventIntegrationName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef = TypedDict(
    "ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Namespace": str,
        "Description": str,
        "ApplicationSourceConfig": ApplicationSourceConfigOutputTypeDef,
        "Subscriptions": List[SubscriptionTypeDef],
        "Publications": List[PublicationTypeDef],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
        "Tags": Dict[str, str],
        "Permissions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventIntegrationsResponseTypeDef = TypedDict(
    "ListEventIntegrationsResponseTypeDef",
    {
        "EventIntegrations": List[EventIntegrationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateDataIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "CreateDataIntegrationAssociationRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
        "ClientId": NotRequired[str],
        "ObjectConfiguration": NotRequired[Mapping[str, Mapping[str, Sequence[str]]]],
        "DestinationURI": NotRequired[str],
        "ClientAssociationMetadata": NotRequired[Mapping[str, str]],
        "ClientToken": NotRequired[str],
        "ExecutionConfiguration": NotRequired[ExecutionConfigurationTypeDef],
    },
)
DataIntegrationAssociationSummaryTypeDef = TypedDict(
    "DataIntegrationAssociationSummaryTypeDef",
    {
        "DataIntegrationAssociationArn": NotRequired[str],
        "DataIntegrationArn": NotRequired[str],
        "ClientId": NotRequired[str],
        "DestinationURI": NotRequired[str],
        "LastExecutionStatus": NotRequired[LastExecutionStatusTypeDef],
        "ExecutionConfiguration": NotRequired[ExecutionConfigurationTypeDef],
    },
)
UpdateDataIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "UpdateDataIntegrationAssociationRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
        "DataIntegrationAssociationIdentifier": str,
        "ExecutionConfiguration": ExecutionConfigurationTypeDef,
    },
)
ApplicationSourceConfigTypeDef = TypedDict(
    "ApplicationSourceConfigTypeDef",
    {
        "ExternalUrlConfig": NotRequired[ExternalUrlConfigUnionTypeDef],
    },
)
ListDataIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListDataIntegrationAssociationsResponseTypeDef",
    {
        "DataIntegrationAssociations": List[DataIntegrationAssociationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Namespace": str,
        "ApplicationSourceConfig": ApplicationSourceConfigTypeDef,
        "Description": NotRequired[str],
        "Subscriptions": NotRequired[Sequence[SubscriptionTypeDef]],
        "Publications": NotRequired[Sequence[PublicationTypeDef]],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Permissions": NotRequired[Sequence[str]],
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ApplicationSourceConfig": NotRequired[ApplicationSourceConfigTypeDef],
        "Subscriptions": NotRequired[Sequence[SubscriptionTypeDef]],
        "Publications": NotRequired[Sequence[PublicationTypeDef]],
        "Permissions": NotRequired[Sequence[str]],
    },
)
