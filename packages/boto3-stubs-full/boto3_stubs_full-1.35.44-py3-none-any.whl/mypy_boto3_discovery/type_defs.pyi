"""
Type annotations for discovery service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/type_defs/)

Usage::

    ```python
    from mypy_boto3_discovery.type_defs import AgentConfigurationStatusTypeDef

    data: AgentConfigurationStatusTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AgentStatusType,
    BatchDeleteConfigurationTaskStatusType,
    BatchDeleteImportDataErrorCodeType,
    ConfigurationItemTypeType,
    ContinuousExportStatusType,
    DeleteAgentErrorCodeType,
    ExportStatusType,
    ImportStatusType,
    ImportTaskFilterNameType,
    OfferingClassType,
    OrderStringType,
    PurchasingOptionType,
    TenancyType,
    TermLengthType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AgentConfigurationStatusTypeDef",
    "AgentNetworkInfoTypeDef",
    "AssociateConfigurationItemsToApplicationRequestRequestTypeDef",
    "BatchDeleteAgentErrorTypeDef",
    "DeleteAgentTypeDef",
    "ResponseMetadataTypeDef",
    "DeletionWarningTypeDef",
    "FailedConfigurationTypeDef",
    "BatchDeleteImportDataErrorTypeDef",
    "BatchDeleteImportDataRequestRequestTypeDef",
    "ConfigurationTagTypeDef",
    "ContinuousExportDescriptionTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "TagTypeDef",
    "CustomerAgentInfoTypeDef",
    "CustomerAgentlessCollectorInfoTypeDef",
    "CustomerConnectorInfoTypeDef",
    "CustomerMeCollectorInfoTypeDef",
    "DeleteApplicationsRequestRequestTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeBatchDeleteConfigurationTaskRequestRequestTypeDef",
    "DescribeConfigurationsRequestRequestTypeDef",
    "DescribeContinuousExportsRequestRequestTypeDef",
    "DescribeExportConfigurationsRequestRequestTypeDef",
    "ExportInfoTypeDef",
    "ExportFilterTypeDef",
    "ImportTaskFilterTypeDef",
    "ImportTaskTypeDef",
    "TagFilterTypeDef",
    "DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef",
    "ReservedInstanceOptionsTypeDef",
    "UsageMetricBasisTypeDef",
    "OrderByElementTypeDef",
    "ListServerNeighborsRequestRequestTypeDef",
    "NeighborConnectionDetailTypeDef",
    "StartBatchDeleteConfigurationTaskRequestRequestTypeDef",
    "StartDataCollectionByAgentIdsRequestRequestTypeDef",
    "TimestampTypeDef",
    "StartImportTaskRequestRequestTypeDef",
    "StopContinuousExportRequestRequestTypeDef",
    "StopDataCollectionByAgentIdsRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "AgentInfoTypeDef",
    "BatchDeleteAgentsRequestRequestTypeDef",
    "BatchDeleteAgentsResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "DescribeConfigurationsResponseTypeDef",
    "ExportConfigurationsResponseTypeDef",
    "ListConfigurationsResponseTypeDef",
    "StartBatchDeleteConfigurationTaskResponseTypeDef",
    "StartContinuousExportResponseTypeDef",
    "StartDataCollectionByAgentIdsResponseTypeDef",
    "StartExportTaskResponseTypeDef",
    "StopContinuousExportResponseTypeDef",
    "StopDataCollectionByAgentIdsResponseTypeDef",
    "BatchDeleteConfigurationTaskTypeDef",
    "BatchDeleteImportDataResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "DescribeContinuousExportsResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "GetDiscoverySummaryResponseTypeDef",
    "DescribeAgentsRequestRequestTypeDef",
    "DescribeAgentsRequestDescribeAgentsPaginateTypeDef",
    "DescribeContinuousExportsRequestDescribeContinuousExportsPaginateTypeDef",
    "DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateTypeDef",
    "DescribeExportConfigurationsResponseTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef",
    "DescribeExportTasksRequestRequestTypeDef",
    "DescribeImportTasksRequestDescribeImportTasksPaginateTypeDef",
    "DescribeImportTasksRequestRequestTypeDef",
    "DescribeImportTasksResponseTypeDef",
    "StartImportTaskResponseTypeDef",
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "Ec2RecommendationsExportPreferencesTypeDef",
    "ListConfigurationsRequestListConfigurationsPaginateTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListServerNeighborsResponseTypeDef",
    "DescribeAgentsResponseTypeDef",
    "DescribeBatchDeleteConfigurationTaskResponseTypeDef",
    "ExportPreferencesTypeDef",
    "StartExportTaskRequestRequestTypeDef",
)

AgentConfigurationStatusTypeDef = TypedDict(
    "AgentConfigurationStatusTypeDef",
    {
        "agentId": NotRequired[str],
        "operationSucceeded": NotRequired[bool],
        "description": NotRequired[str],
    },
)
AgentNetworkInfoTypeDef = TypedDict(
    "AgentNetworkInfoTypeDef",
    {
        "ipAddress": NotRequired[str],
        "macAddress": NotRequired[str],
    },
)
AssociateConfigurationItemsToApplicationRequestRequestTypeDef = TypedDict(
    "AssociateConfigurationItemsToApplicationRequestRequestTypeDef",
    {
        "applicationConfigurationId": str,
        "configurationIds": Sequence[str],
    },
)
BatchDeleteAgentErrorTypeDef = TypedDict(
    "BatchDeleteAgentErrorTypeDef",
    {
        "agentId": str,
        "errorMessage": str,
        "errorCode": DeleteAgentErrorCodeType,
    },
)
DeleteAgentTypeDef = TypedDict(
    "DeleteAgentTypeDef",
    {
        "agentId": str,
        "force": NotRequired[bool],
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
DeletionWarningTypeDef = TypedDict(
    "DeletionWarningTypeDef",
    {
        "configurationId": NotRequired[str],
        "warningCode": NotRequired[int],
        "warningText": NotRequired[str],
    },
)
FailedConfigurationTypeDef = TypedDict(
    "FailedConfigurationTypeDef",
    {
        "configurationId": NotRequired[str],
        "errorStatusCode": NotRequired[int],
        "errorMessage": NotRequired[str],
    },
)
BatchDeleteImportDataErrorTypeDef = TypedDict(
    "BatchDeleteImportDataErrorTypeDef",
    {
        "importTaskId": NotRequired[str],
        "errorCode": NotRequired[BatchDeleteImportDataErrorCodeType],
        "errorDescription": NotRequired[str],
    },
)
BatchDeleteImportDataRequestRequestTypeDef = TypedDict(
    "BatchDeleteImportDataRequestRequestTypeDef",
    {
        "importTaskIds": Sequence[str],
        "deleteHistory": NotRequired[bool],
    },
)
ConfigurationTagTypeDef = TypedDict(
    "ConfigurationTagTypeDef",
    {
        "configurationType": NotRequired[ConfigurationItemTypeType],
        "configurationId": NotRequired[str],
        "key": NotRequired[str],
        "value": NotRequired[str],
        "timeOfCreation": NotRequired[datetime],
    },
)
ContinuousExportDescriptionTypeDef = TypedDict(
    "ContinuousExportDescriptionTypeDef",
    {
        "exportId": NotRequired[str],
        "status": NotRequired[ContinuousExportStatusType],
        "statusDetail": NotRequired[str],
        "s3Bucket": NotRequired[str],
        "startTime": NotRequired[datetime],
        "stopTime": NotRequired[datetime],
        "dataSource": NotRequired[Literal["AGENT"]],
        "schemaStorageConfig": NotRequired[Dict[str, str]],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
CustomerAgentInfoTypeDef = TypedDict(
    "CustomerAgentInfoTypeDef",
    {
        "activeAgents": int,
        "healthyAgents": int,
        "blackListedAgents": int,
        "shutdownAgents": int,
        "unhealthyAgents": int,
        "totalAgents": int,
        "unknownAgents": int,
    },
)
CustomerAgentlessCollectorInfoTypeDef = TypedDict(
    "CustomerAgentlessCollectorInfoTypeDef",
    {
        "activeAgentlessCollectors": int,
        "healthyAgentlessCollectors": int,
        "denyListedAgentlessCollectors": int,
        "shutdownAgentlessCollectors": int,
        "unhealthyAgentlessCollectors": int,
        "totalAgentlessCollectors": int,
        "unknownAgentlessCollectors": int,
    },
)
CustomerConnectorInfoTypeDef = TypedDict(
    "CustomerConnectorInfoTypeDef",
    {
        "activeConnectors": int,
        "healthyConnectors": int,
        "blackListedConnectors": int,
        "shutdownConnectors": int,
        "unhealthyConnectors": int,
        "totalConnectors": int,
        "unknownConnectors": int,
    },
)
CustomerMeCollectorInfoTypeDef = TypedDict(
    "CustomerMeCollectorInfoTypeDef",
    {
        "activeMeCollectors": int,
        "healthyMeCollectors": int,
        "denyListedMeCollectors": int,
        "shutdownMeCollectors": int,
        "unhealthyMeCollectors": int,
        "totalMeCollectors": int,
        "unknownMeCollectors": int,
    },
)
DeleteApplicationsRequestRequestTypeDef = TypedDict(
    "DeleteApplicationsRequestRequestTypeDef",
    {
        "configurationIds": Sequence[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
        "condition": str,
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
DescribeBatchDeleteConfigurationTaskRequestRequestTypeDef = TypedDict(
    "DescribeBatchDeleteConfigurationTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)
DescribeConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationsRequestRequestTypeDef",
    {
        "configurationIds": Sequence[str],
    },
)
DescribeContinuousExportsRequestRequestTypeDef = TypedDict(
    "DescribeContinuousExportsRequestRequestTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeExportConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeExportConfigurationsRequestRequestTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ExportInfoTypeDef = TypedDict(
    "ExportInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
        "statusMessage": str,
        "exportRequestTime": datetime,
        "configurationsDownloadUrl": NotRequired[str],
        "isTruncated": NotRequired[bool],
        "requestedStartTime": NotRequired[datetime],
        "requestedEndTime": NotRequired[datetime],
    },
)
ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
        "condition": str,
    },
)
ImportTaskFilterTypeDef = TypedDict(
    "ImportTaskFilterTypeDef",
    {
        "name": NotRequired[ImportTaskFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)
ImportTaskTypeDef = TypedDict(
    "ImportTaskTypeDef",
    {
        "importTaskId": NotRequired[str],
        "clientRequestToken": NotRequired[str],
        "name": NotRequired[str],
        "importUrl": NotRequired[str],
        "status": NotRequired[ImportStatusType],
        "importRequestTime": NotRequired[datetime],
        "importCompletionTime": NotRequired[datetime],
        "importDeletedTime": NotRequired[datetime],
        "serverImportSuccess": NotRequired[int],
        "serverImportFailure": NotRequired[int],
        "applicationImportSuccess": NotRequired[int],
        "applicationImportFailure": NotRequired[int],
        "errorsAndFailedEntriesZip": NotRequired[str],
    },
)
TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
    },
)
DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef = TypedDict(
    "DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef",
    {
        "applicationConfigurationId": str,
        "configurationIds": Sequence[str],
    },
)
ReservedInstanceOptionsTypeDef = TypedDict(
    "ReservedInstanceOptionsTypeDef",
    {
        "purchasingOption": PurchasingOptionType,
        "offeringClass": OfferingClassType,
        "termLength": TermLengthType,
    },
)
UsageMetricBasisTypeDef = TypedDict(
    "UsageMetricBasisTypeDef",
    {
        "name": NotRequired[str],
        "percentageAdjust": NotRequired[float],
    },
)
OrderByElementTypeDef = TypedDict(
    "OrderByElementTypeDef",
    {
        "fieldName": str,
        "sortOrder": NotRequired[OrderStringType],
    },
)
ListServerNeighborsRequestRequestTypeDef = TypedDict(
    "ListServerNeighborsRequestRequestTypeDef",
    {
        "configurationId": str,
        "portInformationNeeded": NotRequired[bool],
        "neighborConfigurationIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
NeighborConnectionDetailTypeDef = TypedDict(
    "NeighborConnectionDetailTypeDef",
    {
        "sourceServerId": str,
        "destinationServerId": str,
        "connectionsCount": int,
        "destinationPort": NotRequired[int],
        "transportProtocol": NotRequired[str],
    },
)
StartBatchDeleteConfigurationTaskRequestRequestTypeDef = TypedDict(
    "StartBatchDeleteConfigurationTaskRequestRequestTypeDef",
    {
        "configurationType": Literal["SERVER"],
        "configurationIds": Sequence[str],
    },
)
StartDataCollectionByAgentIdsRequestRequestTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsRequestRequestTypeDef",
    {
        "agentIds": Sequence[str],
    },
)
TimestampTypeDef = Union[datetime, str]
StartImportTaskRequestRequestTypeDef = TypedDict(
    "StartImportTaskRequestRequestTypeDef",
    {
        "name": str,
        "importUrl": str,
        "clientRequestToken": NotRequired[str],
    },
)
StopContinuousExportRequestRequestTypeDef = TypedDict(
    "StopContinuousExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)
StopDataCollectionByAgentIdsRequestRequestTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsRequestRequestTypeDef",
    {
        "agentIds": Sequence[str],
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "configurationId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
AgentInfoTypeDef = TypedDict(
    "AgentInfoTypeDef",
    {
        "agentId": NotRequired[str],
        "hostName": NotRequired[str],
        "agentNetworkInfoList": NotRequired[List[AgentNetworkInfoTypeDef]],
        "connectorId": NotRequired[str],
        "version": NotRequired[str],
        "health": NotRequired[AgentStatusType],
        "lastHealthPingTime": NotRequired[str],
        "collectionStatus": NotRequired[str],
        "agentType": NotRequired[str],
        "registeredTime": NotRequired[str],
    },
)
BatchDeleteAgentsRequestRequestTypeDef = TypedDict(
    "BatchDeleteAgentsRequestRequestTypeDef",
    {
        "deleteAgents": Sequence[DeleteAgentTypeDef],
    },
)
BatchDeleteAgentsResponseTypeDef = TypedDict(
    "BatchDeleteAgentsResponseTypeDef",
    {
        "errors": List[BatchDeleteAgentErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "configurationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConfigurationsResponseTypeDef = TypedDict(
    "DescribeConfigurationsResponseTypeDef",
    {
        "configurations": List[Dict[str, str]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportConfigurationsResponseTypeDef = TypedDict(
    "ExportConfigurationsResponseTypeDef",
    {
        "exportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "configurations": List[Dict[str, str]],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartBatchDeleteConfigurationTaskResponseTypeDef = TypedDict(
    "StartBatchDeleteConfigurationTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartContinuousExportResponseTypeDef = TypedDict(
    "StartContinuousExportResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[AgentConfigurationStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartExportTaskResponseTypeDef = TypedDict(
    "StartExportTaskResponseTypeDef",
    {
        "exportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopContinuousExportResponseTypeDef = TypedDict(
    "StopContinuousExportResponseTypeDef",
    {
        "startTime": datetime,
        "stopTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[AgentConfigurationStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteConfigurationTaskTypeDef = TypedDict(
    "BatchDeleteConfigurationTaskTypeDef",
    {
        "taskId": NotRequired[str],
        "status": NotRequired[BatchDeleteConfigurationTaskStatusType],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "configurationType": NotRequired[Literal["SERVER"]],
        "requestedConfigurations": NotRequired[List[str]],
        "deletedConfigurations": NotRequired[List[str]],
        "failedConfigurations": NotRequired[List[FailedConfigurationTypeDef]],
        "deletionWarnings": NotRequired[List[DeletionWarningTypeDef]],
    },
)
BatchDeleteImportDataResponseTypeDef = TypedDict(
    "BatchDeleteImportDataResponseTypeDef",
    {
        "errors": List[BatchDeleteImportDataErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {
        "tags": List[ConfigurationTagTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeContinuousExportsResponseTypeDef = TypedDict(
    "DescribeContinuousExportsResponseTypeDef",
    {
        "descriptions": List[ContinuousExportDescriptionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "configurationIds": Sequence[str],
        "tags": Sequence[TagTypeDef],
    },
)
DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "configurationIds": Sequence[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetDiscoverySummaryResponseTypeDef = TypedDict(
    "GetDiscoverySummaryResponseTypeDef",
    {
        "servers": int,
        "applications": int,
        "serversMappedToApplications": int,
        "serversMappedtoTags": int,
        "agentSummary": CustomerAgentInfoTypeDef,
        "connectorSummary": CustomerConnectorInfoTypeDef,
        "meCollectorSummary": CustomerMeCollectorInfoTypeDef,
        "agentlessCollectorSummary": CustomerAgentlessCollectorInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAgentsRequestRequestTypeDef = TypedDict(
    "DescribeAgentsRequestRequestTypeDef",
    {
        "agentIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeAgentsRequestDescribeAgentsPaginateTypeDef = TypedDict(
    "DescribeAgentsRequestDescribeAgentsPaginateTypeDef",
    {
        "agentIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeContinuousExportsRequestDescribeContinuousExportsPaginateTypeDef = TypedDict(
    "DescribeContinuousExportsRequestDescribeContinuousExportsPaginateTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateTypeDef = TypedDict(
    "DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeExportConfigurationsResponseTypeDef = TypedDict(
    "DescribeExportConfigurationsResponseTypeDef",
    {
        "exportsInfo": List[ExportInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {
        "exportsInfo": List[ExportInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef = TypedDict(
    "DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[ExportFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeExportTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestRequestTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[ExportFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeImportTasksRequestDescribeImportTasksPaginateTypeDef = TypedDict(
    "DescribeImportTasksRequestDescribeImportTasksPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[ImportTaskFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeImportTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportTasksRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[ImportTaskFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeImportTasksResponseTypeDef = TypedDict(
    "DescribeImportTasksResponseTypeDef",
    {
        "nextToken": str,
        "tasks": List[ImportTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportTaskResponseTypeDef = TypedDict(
    "StartImportTaskResponseTypeDef",
    {
        "task": ImportTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTagsRequestDescribeTagsPaginateTypeDef = TypedDict(
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[TagFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[TagFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
Ec2RecommendationsExportPreferencesTypeDef = TypedDict(
    "Ec2RecommendationsExportPreferencesTypeDef",
    {
        "enabled": NotRequired[bool],
        "cpuPerformanceMetricBasis": NotRequired[UsageMetricBasisTypeDef],
        "ramPerformanceMetricBasis": NotRequired[UsageMetricBasisTypeDef],
        "tenancy": NotRequired[TenancyType],
        "excludedInstanceTypes": NotRequired[Sequence[str]],
        "preferredRegion": NotRequired[str],
        "reservedInstanceOptions": NotRequired[ReservedInstanceOptionsTypeDef],
    },
)
ListConfigurationsRequestListConfigurationsPaginateTypeDef = TypedDict(
    "ListConfigurationsRequestListConfigurationsPaginateTypeDef",
    {
        "configurationType": ConfigurationItemTypeType,
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "orderBy": NotRequired[Sequence[OrderByElementTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "configurationType": ConfigurationItemTypeType,
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "orderBy": NotRequired[Sequence[OrderByElementTypeDef]],
    },
)
ListServerNeighborsResponseTypeDef = TypedDict(
    "ListServerNeighborsResponseTypeDef",
    {
        "neighbors": List[NeighborConnectionDetailTypeDef],
        "nextToken": str,
        "knownDependencyCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAgentsResponseTypeDef = TypedDict(
    "DescribeAgentsResponseTypeDef",
    {
        "agentsInfo": List[AgentInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBatchDeleteConfigurationTaskResponseTypeDef = TypedDict(
    "DescribeBatchDeleteConfigurationTaskResponseTypeDef",
    {
        "task": BatchDeleteConfigurationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportPreferencesTypeDef = TypedDict(
    "ExportPreferencesTypeDef",
    {
        "ec2RecommendationsPreferences": NotRequired[Ec2RecommendationsExportPreferencesTypeDef],
    },
)
StartExportTaskRequestRequestTypeDef = TypedDict(
    "StartExportTaskRequestRequestTypeDef",
    {
        "exportDataFormat": NotRequired[Sequence[Literal["CSV"]]],
        "filters": NotRequired[Sequence[ExportFilterTypeDef]],
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
        "preferences": NotRequired[ExportPreferencesTypeDef],
    },
)
