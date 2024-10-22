"""
Type annotations for iotsitewise service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotsitewise.type_defs import ActionDefinitionTypeDef

    data: ActionDefinitionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AggregateTypeType,
    AssetModelStateType,
    AssetModelTypeType,
    AssetModelVersionTypeType,
    AssetStateType,
    AuthModeType,
    BatchEntryCompletionStatusType,
    BatchGetAssetPropertyAggregatesErrorCodeType,
    BatchGetAssetPropertyValueErrorCodeType,
    BatchGetAssetPropertyValueHistoryErrorCodeType,
    BatchPutAssetPropertyValueErrorCodeType,
    CapabilitySyncStatusType,
    ColumnNameType,
    ComputeLocationType,
    ConfigurationStateType,
    DetailedErrorCodeType,
    DisassociatedDataStorageStateType,
    EncryptionTypeType,
    ErrorCodeType,
    ForwardingConfigStateType,
    IdentityTypeType,
    JobStatusType,
    ListAssetModelPropertiesFilterType,
    ListAssetPropertiesFilterType,
    ListAssetsFilterType,
    ListBulkImportJobsFilterType,
    ListTimeSeriesTypeType,
    LoggingLevelType,
    MonitorErrorCodeType,
    PermissionType,
    PortalStateType,
    PropertyDataTypeType,
    PropertyNotificationStateType,
    QualityType,
    ResourceTypeType,
    ScalarTypeType,
    StorageTypeType,
    TimeOrderingType,
    TraversalDirectionType,
    WarmTierStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ActionDefinitionTypeDef",
    "ActionPayloadTypeDef",
    "TargetResourceTypeDef",
    "AggregatesTypeDef",
    "AlarmsTypeDef",
    "AssetCompositeModelPathSegmentTypeDef",
    "AssetErrorDetailsTypeDef",
    "AssetHierarchyInfoTypeDef",
    "AssetHierarchyTypeDef",
    "AssetModelCompositeModelPathSegmentTypeDef",
    "AssetModelHierarchyDefinitionTypeDef",
    "AssetModelHierarchyTypeDef",
    "AssetModelPropertyPathSegmentTypeDef",
    "AssetPropertyPathSegmentTypeDef",
    "PropertyNotificationTypeDef",
    "TimeInNanosTypeDef",
    "VariantTypeDef",
    "AssociateAssetsRequestRequestTypeDef",
    "AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef",
    "AttributeTypeDef",
    "BatchAssociateProjectAssetsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDisassociateProjectAssetsRequestRequestTypeDef",
    "TimestampTypeDef",
    "BatchGetAssetPropertyAggregatesErrorEntryTypeDef",
    "BatchGetAssetPropertyAggregatesErrorInfoTypeDef",
    "BatchGetAssetPropertyValueEntryTypeDef",
    "BatchGetAssetPropertyValueErrorEntryTypeDef",
    "BatchGetAssetPropertyValueErrorInfoTypeDef",
    "BatchGetAssetPropertyValueHistoryErrorEntryTypeDef",
    "BatchGetAssetPropertyValueHistoryErrorInfoTypeDef",
    "BlobTypeDef",
    "ColumnTypeTypeDef",
    "CompositionRelationshipItemTypeDef",
    "CompositionRelationshipSummaryTypeDef",
    "ConfigurationErrorDetailsTypeDef",
    "CreateAssetRequestRequestTypeDef",
    "ErrorReportLocationTypeDef",
    "FileTypeDef",
    "CreateDashboardRequestRequestTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CsvOutputTypeDef",
    "CsvTypeDef",
    "CustomerManagedS3StorageTypeDef",
    "DashboardSummaryTypeDef",
    "DatumPaginatorTypeDef",
    "DatumTypeDef",
    "DeleteAccessPolicyRequestRequestTypeDef",
    "DeleteAssetModelCompositeModelRequestRequestTypeDef",
    "DeleteAssetModelRequestRequestTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeleteDashboardRequestRequestTypeDef",
    "DeleteGatewayRequestRequestTypeDef",
    "DeletePortalRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteTimeSeriesRequestRequestTypeDef",
    "DescribeAccessPolicyRequestRequestTypeDef",
    "DescribeActionRequestRequestTypeDef",
    "DescribeAssetCompositeModelRequestRequestTypeDef",
    "DescribeAssetModelCompositeModelRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeAssetModelRequestRequestTypeDef",
    "DescribeAssetPropertyRequestRequestTypeDef",
    "DescribeAssetRequestRequestTypeDef",
    "DescribeBulkImportJobRequestRequestTypeDef",
    "DescribeDashboardRequestRequestTypeDef",
    "DescribeGatewayCapabilityConfigurationRequestRequestTypeDef",
    "DescribeGatewayRequestRequestTypeDef",
    "GatewayCapabilitySummaryTypeDef",
    "LoggingOptionsTypeDef",
    "DescribePortalRequestRequestTypeDef",
    "ImageLocationTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "RetentionPeriodTypeDef",
    "WarmTierRetentionPeriodTypeDef",
    "DescribeTimeSeriesRequestRequestTypeDef",
    "DetailedErrorTypeDef",
    "DisassociateAssetsRequestRequestTypeDef",
    "DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ExecuteQueryRequestRequestTypeDef",
    "ForwardingConfigTypeDef",
    "GreengrassTypeDef",
    "GreengrassV2TypeDef",
    "SiemensIETypeDef",
    "GetAssetPropertyValueRequestRequestTypeDef",
    "GetInterpolatedAssetPropertyValuesRequestRequestTypeDef",
    "GroupIdentityTypeDef",
    "IAMRoleIdentityTypeDef",
    "IAMUserIdentityTypeDef",
    "UserIdentityTypeDef",
    "JobSummaryTypeDef",
    "ListAccessPoliciesRequestRequestTypeDef",
    "ListActionsRequestRequestTypeDef",
    "ListAssetModelCompositeModelsRequestRequestTypeDef",
    "ListAssetModelPropertiesRequestRequestTypeDef",
    "ListAssetModelsRequestRequestTypeDef",
    "ListAssetPropertiesRequestRequestTypeDef",
    "ListAssetRelationshipsRequestRequestTypeDef",
    "ListAssetsRequestRequestTypeDef",
    "ListAssociatedAssetsRequestRequestTypeDef",
    "ListBulkImportJobsRequestRequestTypeDef",
    "ListCompositionRelationshipsRequestRequestTypeDef",
    "ListDashboardsRequestRequestTypeDef",
    "ListGatewaysRequestRequestTypeDef",
    "ListPortalsRequestRequestTypeDef",
    "ListProjectAssetsRequestRequestTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ProjectSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTimeSeriesRequestRequestTypeDef",
    "TimeSeriesSummaryTypeDef",
    "MetricProcessingConfigTypeDef",
    "TumblingWindowTypeDef",
    "MonitorErrorDetailsTypeDef",
    "PortalResourceTypeDef",
    "ProjectResourceTypeDef",
    "PutDefaultEncryptionConfigurationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAssetPropertyRequestRequestTypeDef",
    "UpdateAssetRequestRequestTypeDef",
    "UpdateDashboardRequestRequestTypeDef",
    "UpdateGatewayCapabilityConfigurationRequestRequestTypeDef",
    "UpdateGatewayRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "ActionSummaryTypeDef",
    "ExecuteActionRequestRequestTypeDef",
    "AggregatedValueTypeDef",
    "AssetCompositeModelSummaryTypeDef",
    "AssetRelationshipSummaryTypeDef",
    "AssetModelCompositeModelSummaryTypeDef",
    "VariableValueOutputTypeDef",
    "VariableValueTypeDef",
    "AssetPropertySummaryTypeDef",
    "AssetPropertyTypeDef",
    "BatchPutAssetPropertyErrorTypeDef",
    "AssetPropertyValueTypeDef",
    "InterpolatedAssetPropertyValueTypeDef",
    "BatchAssociateProjectAssetsResponseTypeDef",
    "BatchDisassociateProjectAssetsResponseTypeDef",
    "CreateAccessPolicyResponseTypeDef",
    "CreateBulkImportJobResponseTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateGatewayResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "DescribeActionResponseTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeTimeSeriesResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExecuteActionResponseTypeDef",
    "ListProjectAssetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    "BatchGetAssetPropertyAggregatesEntryTypeDef",
    "BatchGetAssetPropertyValueHistoryEntryTypeDef",
    "GetAssetPropertyAggregatesRequestRequestTypeDef",
    "GetAssetPropertyValueHistoryRequestRequestTypeDef",
    "BatchGetAssetPropertyAggregatesSkippedEntryTypeDef",
    "BatchGetAssetPropertyValueRequestRequestTypeDef",
    "BatchGetAssetPropertyValueSkippedEntryTypeDef",
    "BatchGetAssetPropertyValueHistorySkippedEntryTypeDef",
    "ImageFileTypeDef",
    "ColumnInfoTypeDef",
    "CompositionDetailsTypeDef",
    "ListCompositionRelationshipsResponseTypeDef",
    "ConfigurationStatusTypeDef",
    "FileFormatOutputTypeDef",
    "CsvUnionTypeDef",
    "MultiLayerStorageTypeDef",
    "ListDashboardsResponseTypeDef",
    "RowPaginatorTypeDef",
    "RowTypeDef",
    "DescribeAssetModelRequestAssetModelActiveWaitTypeDef",
    "DescribeAssetModelRequestAssetModelNotExistsWaitTypeDef",
    "DescribeAssetRequestAssetActiveWaitTypeDef",
    "DescribeAssetRequestAssetNotExistsWaitTypeDef",
    "DescribePortalRequestPortalActiveWaitTypeDef",
    "DescribePortalRequestPortalNotExistsWaitTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "ErrorDetailsTypeDef",
    "ExecuteQueryRequestExecuteQueryPaginateTypeDef",
    "GetAssetPropertyAggregatesRequestGetAssetPropertyAggregatesPaginateTypeDef",
    "GetAssetPropertyValueHistoryRequestGetAssetPropertyValueHistoryPaginateTypeDef",
    "GetInterpolatedAssetPropertyValuesRequestGetInterpolatedAssetPropertyValuesPaginateTypeDef",
    "ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef",
    "ListActionsRequestListActionsPaginateTypeDef",
    "ListAssetModelCompositeModelsRequestListAssetModelCompositeModelsPaginateTypeDef",
    "ListAssetModelPropertiesRequestListAssetModelPropertiesPaginateTypeDef",
    "ListAssetModelsRequestListAssetModelsPaginateTypeDef",
    "ListAssetPropertiesRequestListAssetPropertiesPaginateTypeDef",
    "ListAssetRelationshipsRequestListAssetRelationshipsPaginateTypeDef",
    "ListAssetsRequestListAssetsPaginateTypeDef",
    "ListAssociatedAssetsRequestListAssociatedAssetsPaginateTypeDef",
    "ListBulkImportJobsRequestListBulkImportJobsPaginateTypeDef",
    "ListCompositionRelationshipsRequestListCompositionRelationshipsPaginateTypeDef",
    "ListDashboardsRequestListDashboardsPaginateTypeDef",
    "ListGatewaysRequestListGatewaysPaginateTypeDef",
    "ListPortalsRequestListPortalsPaginateTypeDef",
    "ListProjectAssetsRequestListProjectAssetsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListTimeSeriesRequestListTimeSeriesPaginateTypeDef",
    "MeasurementProcessingConfigTypeDef",
    "TransformProcessingConfigTypeDef",
    "GatewayPlatformTypeDef",
    "IdentityTypeDef",
    "ListBulkImportJobsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTimeSeriesResponseTypeDef",
    "MetricWindowTypeDef",
    "PortalStatusTypeDef",
    "ResourceTypeDef",
    "ListActionsResponseTypeDef",
    "BatchGetAssetPropertyAggregatesSuccessEntryTypeDef",
    "GetAssetPropertyAggregatesResponseTypeDef",
    "ListAssetRelationshipsResponseTypeDef",
    "ListAssetModelCompositeModelsResponseTypeDef",
    "ExpressionVariableOutputTypeDef",
    "VariableValueUnionTypeDef",
    "ListAssetPropertiesResponseTypeDef",
    "AssetCompositeModelTypeDef",
    "DescribeAssetCompositeModelResponseTypeDef",
    "BatchPutAssetPropertyErrorEntryTypeDef",
    "BatchGetAssetPropertyValueHistorySuccessEntryTypeDef",
    "BatchGetAssetPropertyValueSuccessEntryTypeDef",
    "GetAssetPropertyValueHistoryResponseTypeDef",
    "GetAssetPropertyValueResponseTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "GetInterpolatedAssetPropertyValuesResponseTypeDef",
    "BatchGetAssetPropertyAggregatesRequestRequestTypeDef",
    "BatchGetAssetPropertyValueHistoryRequestRequestTypeDef",
    "CreatePortalRequestRequestTypeDef",
    "ImageTypeDef",
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    "JobConfigurationOutputTypeDef",
    "FileFormatTypeDef",
    "DescribeStorageConfigurationResponseTypeDef",
    "PutStorageConfigurationRequestRequestTypeDef",
    "PutStorageConfigurationResponseTypeDef",
    "ExecuteQueryResponsePaginatorTypeDef",
    "ExecuteQueryResponseTypeDef",
    "AssetModelStatusTypeDef",
    "AssetStatusTypeDef",
    "MeasurementTypeDef",
    "CreateGatewayRequestRequestTypeDef",
    "DescribeGatewayResponseTypeDef",
    "GatewaySummaryTypeDef",
    "CreatePortalResponseTypeDef",
    "DeletePortalResponseTypeDef",
    "DescribePortalResponseTypeDef",
    "PortalSummaryTypeDef",
    "UpdatePortalResponseTypeDef",
    "AccessPolicySummaryTypeDef",
    "CreateAccessPolicyRequestRequestTypeDef",
    "DescribeAccessPolicyResponseTypeDef",
    "UpdateAccessPolicyRequestRequestTypeDef",
    "BatchGetAssetPropertyAggregatesResponseTypeDef",
    "MetricOutputTypeDef",
    "TransformOutputTypeDef",
    "ExpressionVariableTypeDef",
    "BatchPutAssetPropertyValueResponseTypeDef",
    "BatchGetAssetPropertyValueHistoryResponseTypeDef",
    "BatchGetAssetPropertyValueResponseTypeDef",
    "BatchPutAssetPropertyValueRequestRequestTypeDef",
    "UpdatePortalRequestRequestTypeDef",
    "DescribeBulkImportJobResponseTypeDef",
    "FileFormatUnionTypeDef",
    "AssetModelSummaryTypeDef",
    "CreateAssetModelCompositeModelResponseTypeDef",
    "CreateAssetModelResponseTypeDef",
    "DeleteAssetModelCompositeModelResponseTypeDef",
    "DeleteAssetModelResponseTypeDef",
    "UpdateAssetModelCompositeModelResponseTypeDef",
    "UpdateAssetModelResponseTypeDef",
    "AssetSummaryTypeDef",
    "AssociatedAssetsSummaryTypeDef",
    "CreateAssetResponseTypeDef",
    "DeleteAssetResponseTypeDef",
    "DescribeAssetResponseTypeDef",
    "UpdateAssetResponseTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListPortalsResponseTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "PropertyTypeOutputTypeDef",
    "ExpressionVariableUnionTypeDef",
    "JobConfigurationTypeDef",
    "ListAssetModelsResponseTypeDef",
    "ListAssetsResponseTypeDef",
    "ListAssociatedAssetsResponseTypeDef",
    "AssetModelPropertyOutputTypeDef",
    "AssetModelPropertySummaryTypeDef",
    "PropertyTypeDef",
    "MetricTypeDef",
    "TransformTypeDef",
    "CreateBulkImportJobRequestRequestTypeDef",
    "AssetModelCompositeModelOutputTypeDef",
    "DescribeAssetModelCompositeModelResponseTypeDef",
    "ListAssetModelPropertiesResponseTypeDef",
    "CompositeModelPropertyTypeDef",
    "MetricUnionTypeDef",
    "TransformUnionTypeDef",
    "DescribeAssetModelResponseTypeDef",
    "DescribeAssetPropertyResponseTypeDef",
    "PropertyTypeTypeDef",
    "PropertyTypeUnionTypeDef",
    "AssetModelPropertyDefinitionTypeDef",
    "AssetModelPropertyTypeDef",
    "AssetModelCompositeModelDefinitionTypeDef",
    "CreateAssetModelCompositeModelRequestRequestTypeDef",
    "AssetModelPropertyUnionTypeDef",
    "UpdateAssetModelCompositeModelRequestRequestTypeDef",
    "CreateAssetModelRequestRequestTypeDef",
    "AssetModelCompositeModelTypeDef",
    "AssetModelCompositeModelUnionTypeDef",
    "UpdateAssetModelRequestRequestTypeDef",
)

ActionDefinitionTypeDef = TypedDict(
    "ActionDefinitionTypeDef",
    {
        "actionDefinitionId": str,
        "actionName": str,
        "actionType": str,
    },
)
ActionPayloadTypeDef = TypedDict(
    "ActionPayloadTypeDef",
    {
        "stringValue": str,
    },
)
TargetResourceTypeDef = TypedDict(
    "TargetResourceTypeDef",
    {
        "assetId": str,
    },
)
AggregatesTypeDef = TypedDict(
    "AggregatesTypeDef",
    {
        "average": NotRequired[float],
        "count": NotRequired[float],
        "maximum": NotRequired[float],
        "minimum": NotRequired[float],
        "sum": NotRequired[float],
        "standardDeviation": NotRequired[float],
    },
)
AlarmsTypeDef = TypedDict(
    "AlarmsTypeDef",
    {
        "alarmRoleArn": str,
        "notificationLambdaArn": NotRequired[str],
    },
)
AssetCompositeModelPathSegmentTypeDef = TypedDict(
    "AssetCompositeModelPathSegmentTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
AssetErrorDetailsTypeDef = TypedDict(
    "AssetErrorDetailsTypeDef",
    {
        "assetId": str,
        "code": Literal["INTERNAL_FAILURE"],
        "message": str,
    },
)
AssetHierarchyInfoTypeDef = TypedDict(
    "AssetHierarchyInfoTypeDef",
    {
        "parentAssetId": NotRequired[str],
        "childAssetId": NotRequired[str],
    },
)
AssetHierarchyTypeDef = TypedDict(
    "AssetHierarchyTypeDef",
    {
        "name": str,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
AssetModelCompositeModelPathSegmentTypeDef = TypedDict(
    "AssetModelCompositeModelPathSegmentTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
AssetModelHierarchyDefinitionTypeDef = TypedDict(
    "AssetModelHierarchyDefinitionTypeDef",
    {
        "name": str,
        "childAssetModelId": str,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
AssetModelHierarchyTypeDef = TypedDict(
    "AssetModelHierarchyTypeDef",
    {
        "name": str,
        "childAssetModelId": str,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
AssetModelPropertyPathSegmentTypeDef = TypedDict(
    "AssetModelPropertyPathSegmentTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
AssetPropertyPathSegmentTypeDef = TypedDict(
    "AssetPropertyPathSegmentTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
PropertyNotificationTypeDef = TypedDict(
    "PropertyNotificationTypeDef",
    {
        "topic": str,
        "state": PropertyNotificationStateType,
    },
)
TimeInNanosTypeDef = TypedDict(
    "TimeInNanosTypeDef",
    {
        "timeInSeconds": int,
        "offsetInNanos": NotRequired[int],
    },
)
VariantTypeDef = TypedDict(
    "VariantTypeDef",
    {
        "stringValue": NotRequired[str],
        "integerValue": NotRequired[int],
        "doubleValue": NotRequired[float],
        "booleanValue": NotRequired[bool],
    },
)
AssociateAssetsRequestRequestTypeDef = TypedDict(
    "AssociateAssetsRequestRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": str,
        "childAssetId": str,
        "clientToken": NotRequired[str],
    },
)
AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef = TypedDict(
    "AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef",
    {
        "alias": str,
        "assetId": str,
        "propertyId": str,
        "clientToken": NotRequired[str],
    },
)
AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "defaultValue": NotRequired[str],
    },
)
BatchAssociateProjectAssetsRequestRequestTypeDef = TypedDict(
    "BatchAssociateProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
        "assetIds": Sequence[str],
        "clientToken": NotRequired[str],
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
BatchDisassociateProjectAssetsRequestRequestTypeDef = TypedDict(
    "BatchDisassociateProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
        "assetIds": Sequence[str],
        "clientToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
BatchGetAssetPropertyAggregatesErrorEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesErrorEntryTypeDef",
    {
        "errorCode": BatchGetAssetPropertyAggregatesErrorCodeType,
        "errorMessage": str,
        "entryId": str,
    },
)
BatchGetAssetPropertyAggregatesErrorInfoTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesErrorInfoTypeDef",
    {
        "errorCode": BatchGetAssetPropertyAggregatesErrorCodeType,
        "errorTimestamp": datetime,
    },
)
BatchGetAssetPropertyValueEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
    },
)
BatchGetAssetPropertyValueErrorEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueErrorEntryTypeDef",
    {
        "errorCode": BatchGetAssetPropertyValueErrorCodeType,
        "errorMessage": str,
        "entryId": str,
    },
)
BatchGetAssetPropertyValueErrorInfoTypeDef = TypedDict(
    "BatchGetAssetPropertyValueErrorInfoTypeDef",
    {
        "errorCode": BatchGetAssetPropertyValueErrorCodeType,
        "errorTimestamp": datetime,
    },
)
BatchGetAssetPropertyValueHistoryErrorEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistoryErrorEntryTypeDef",
    {
        "errorCode": BatchGetAssetPropertyValueHistoryErrorCodeType,
        "errorMessage": str,
        "entryId": str,
    },
)
BatchGetAssetPropertyValueHistoryErrorInfoTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistoryErrorInfoTypeDef",
    {
        "errorCode": BatchGetAssetPropertyValueHistoryErrorCodeType,
        "errorTimestamp": datetime,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ColumnTypeTypeDef = TypedDict(
    "ColumnTypeTypeDef",
    {
        "scalarType": NotRequired[ScalarTypeType],
    },
)
CompositionRelationshipItemTypeDef = TypedDict(
    "CompositionRelationshipItemTypeDef",
    {
        "id": NotRequired[str],
    },
)
CompositionRelationshipSummaryTypeDef = TypedDict(
    "CompositionRelationshipSummaryTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelType": str,
    },
)
ConfigurationErrorDetailsTypeDef = TypedDict(
    "ConfigurationErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
)
CreateAssetRequestRequestTypeDef = TypedDict(
    "CreateAssetRequestRequestTypeDef",
    {
        "assetName": str,
        "assetModelId": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "assetDescription": NotRequired[str],
        "assetId": NotRequired[str],
        "assetExternalId": NotRequired[str],
    },
)
ErrorReportLocationTypeDef = TypedDict(
    "ErrorReportLocationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
)
FileTypeDef = TypedDict(
    "FileTypeDef",
    {
        "bucket": str,
        "key": str,
        "versionId": NotRequired[str],
    },
)
CreateDashboardRequestRequestTypeDef = TypedDict(
    "CreateDashboardRequestRequestTypeDef",
    {
        "projectId": str,
        "dashboardName": str,
        "dashboardDefinition": str,
        "dashboardDescription": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "portalId": str,
        "projectName": str,
        "projectDescription": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CsvOutputTypeDef = TypedDict(
    "CsvOutputTypeDef",
    {
        "columnNames": List[ColumnNameType],
    },
)
CsvTypeDef = TypedDict(
    "CsvTypeDef",
    {
        "columnNames": Sequence[ColumnNameType],
    },
)
CustomerManagedS3StorageTypeDef = TypedDict(
    "CustomerManagedS3StorageTypeDef",
    {
        "s3ResourceArn": str,
        "roleArn": str,
    },
)
DashboardSummaryTypeDef = TypedDict(
    "DashboardSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "description": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "lastUpdateDate": NotRequired[datetime],
    },
)
DatumPaginatorTypeDef = TypedDict(
    "DatumPaginatorTypeDef",
    {
        "scalarValue": NotRequired[str],
        "arrayValue": NotRequired[List[Dict[str, Any]]],
        "rowValue": NotRequired[Dict[str, Any]],
        "nullValue": NotRequired[bool],
    },
)
DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "scalarValue": NotRequired[str],
        "arrayValue": NotRequired[List[Dict[str, Any]]],
        "rowValue": NotRequired[Dict[str, Any]],
        "nullValue": NotRequired[bool],
    },
)
DeleteAccessPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
        "clientToken": NotRequired[str],
    },
)
DeleteAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "DeleteAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
        "clientToken": NotRequired[str],
        "ifMatch": NotRequired[str],
        "ifNoneMatch": NotRequired[str],
        "matchForVersionType": NotRequired[AssetModelVersionTypeType],
    },
)
DeleteAssetModelRequestRequestTypeDef = TypedDict(
    "DeleteAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "clientToken": NotRequired[str],
        "ifMatch": NotRequired[str],
        "ifNoneMatch": NotRequired[str],
        "matchForVersionType": NotRequired[AssetModelVersionTypeType],
    },
)
DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "assetId": str,
        "clientToken": NotRequired[str],
    },
)
DeleteDashboardRequestRequestTypeDef = TypedDict(
    "DeleteDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
        "clientToken": NotRequired[str],
    },
)
DeleteGatewayRequestRequestTypeDef = TypedDict(
    "DeleteGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
    },
)
DeletePortalRequestRequestTypeDef = TypedDict(
    "DeletePortalRequestRequestTypeDef",
    {
        "portalId": str,
        "clientToken": NotRequired[str],
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "projectId": str,
        "clientToken": NotRequired[str],
    },
)
DeleteTimeSeriesRequestRequestTypeDef = TypedDict(
    "DeleteTimeSeriesRequestRequestTypeDef",
    {
        "alias": NotRequired[str],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
DescribeAccessPolicyRequestRequestTypeDef = TypedDict(
    "DescribeAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
    },
)
DescribeActionRequestRequestTypeDef = TypedDict(
    "DescribeActionRequestRequestTypeDef",
    {
        "actionId": str,
    },
)
DescribeAssetCompositeModelRequestRequestTypeDef = TypedDict(
    "DescribeAssetCompositeModelRequestRequestTypeDef",
    {
        "assetId": str,
        "assetCompositeModelId": str,
    },
)
DescribeAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "DescribeAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
        "assetModelVersion": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeAssetModelRequestRequestTypeDef = TypedDict(
    "DescribeAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "excludeProperties": NotRequired[bool],
        "assetModelVersion": NotRequired[str],
    },
)
DescribeAssetPropertyRequestRequestTypeDef = TypedDict(
    "DescribeAssetPropertyRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
    },
)
DescribeAssetRequestRequestTypeDef = TypedDict(
    "DescribeAssetRequestRequestTypeDef",
    {
        "assetId": str,
        "excludeProperties": NotRequired[bool],
    },
)
DescribeBulkImportJobRequestRequestTypeDef = TypedDict(
    "DescribeBulkImportJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
DescribeDashboardRequestRequestTypeDef = TypedDict(
    "DescribeDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
    },
)
DescribeGatewayCapabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationRequestRequestTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
    },
)
DescribeGatewayRequestRequestTypeDef = TypedDict(
    "DescribeGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
    },
)
GatewayCapabilitySummaryTypeDef = TypedDict(
    "GatewayCapabilitySummaryTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
    },
)
LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "level": LoggingLevelType,
    },
)
DescribePortalRequestRequestTypeDef = TypedDict(
    "DescribePortalRequestRequestTypeDef",
    {
        "portalId": str,
    },
)
ImageLocationTypeDef = TypedDict(
    "ImageLocationTypeDef",
    {
        "id": str,
        "url": str,
    },
)
DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "projectId": str,
    },
)
RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "numberOfDays": NotRequired[int],
        "unlimited": NotRequired[bool],
    },
)
WarmTierRetentionPeriodTypeDef = TypedDict(
    "WarmTierRetentionPeriodTypeDef",
    {
        "numberOfDays": NotRequired[int],
        "unlimited": NotRequired[bool],
    },
)
DescribeTimeSeriesRequestRequestTypeDef = TypedDict(
    "DescribeTimeSeriesRequestRequestTypeDef",
    {
        "alias": NotRequired[str],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
    },
)
DetailedErrorTypeDef = TypedDict(
    "DetailedErrorTypeDef",
    {
        "code": DetailedErrorCodeType,
        "message": str,
    },
)
DisassociateAssetsRequestRequestTypeDef = TypedDict(
    "DisassociateAssetsRequestRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": str,
        "childAssetId": str,
        "clientToken": NotRequired[str],
    },
)
DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef = TypedDict(
    "DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef",
    {
        "alias": str,
        "assetId": str,
        "propertyId": str,
        "clientToken": NotRequired[str],
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
ExecuteQueryRequestRequestTypeDef = TypedDict(
    "ExecuteQueryRequestRequestTypeDef",
    {
        "queryStatement": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ForwardingConfigTypeDef = TypedDict(
    "ForwardingConfigTypeDef",
    {
        "state": ForwardingConfigStateType,
    },
)
GreengrassTypeDef = TypedDict(
    "GreengrassTypeDef",
    {
        "groupArn": str,
    },
)
GreengrassV2TypeDef = TypedDict(
    "GreengrassV2TypeDef",
    {
        "coreDeviceThingName": str,
    },
)
SiemensIETypeDef = TypedDict(
    "SiemensIETypeDef",
    {
        "iotCoreThingName": str,
    },
)
GetAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "GetAssetPropertyValueRequestRequestTypeDef",
    {
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
    },
)
GetInterpolatedAssetPropertyValuesRequestRequestTypeDef = TypedDict(
    "GetInterpolatedAssetPropertyValuesRequestRequestTypeDef",
    {
        "startTimeInSeconds": int,
        "endTimeInSeconds": int,
        "quality": QualityType,
        "intervalInSeconds": int,
        "type": str,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "startTimeOffsetInNanos": NotRequired[int],
        "endTimeOffsetInNanos": NotRequired[int],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "intervalWindowInSeconds": NotRequired[int],
    },
)
GroupIdentityTypeDef = TypedDict(
    "GroupIdentityTypeDef",
    {
        "id": str,
    },
)
IAMRoleIdentityTypeDef = TypedDict(
    "IAMRoleIdentityTypeDef",
    {
        "arn": str,
    },
)
IAMUserIdentityTypeDef = TypedDict(
    "IAMUserIdentityTypeDef",
    {
        "arn": str,
    },
)
UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "id": str,
    },
)
JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "status": JobStatusType,
    },
)
ListAccessPoliciesRequestRequestTypeDef = TypedDict(
    "ListAccessPoliciesRequestRequestTypeDef",
    {
        "identityType": NotRequired[IdentityTypeType],
        "identityId": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "iamArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListActionsRequestRequestTypeDef = TypedDict(
    "ListActionsRequestRequestTypeDef",
    {
        "targetResourceType": Literal["ASSET"],
        "targetResourceId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssetModelCompositeModelsRequestRequestTypeDef = TypedDict(
    "ListAssetModelCompositeModelsRequestRequestTypeDef",
    {
        "assetModelId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "assetModelVersion": NotRequired[str],
    },
)
ListAssetModelPropertiesRequestRequestTypeDef = TypedDict(
    "ListAssetModelPropertiesRequestRequestTypeDef",
    {
        "assetModelId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[ListAssetModelPropertiesFilterType],
        "assetModelVersion": NotRequired[str],
    },
)
ListAssetModelsRequestRequestTypeDef = TypedDict(
    "ListAssetModelsRequestRequestTypeDef",
    {
        "assetModelTypes": NotRequired[Sequence[AssetModelTypeType]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "assetModelVersion": NotRequired[str],
    },
)
ListAssetPropertiesRequestRequestTypeDef = TypedDict(
    "ListAssetPropertiesRequestRequestTypeDef",
    {
        "assetId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[ListAssetPropertiesFilterType],
    },
)
ListAssetRelationshipsRequestRequestTypeDef = TypedDict(
    "ListAssetRelationshipsRequestRequestTypeDef",
    {
        "assetId": str,
        "traversalType": Literal["PATH_TO_ROOT"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssetsRequestRequestTypeDef = TypedDict(
    "ListAssetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "assetModelId": NotRequired[str],
        "filter": NotRequired[ListAssetsFilterType],
    },
)
ListAssociatedAssetsRequestRequestTypeDef = TypedDict(
    "ListAssociatedAssetsRequestRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": NotRequired[str],
        "traversalDirection": NotRequired[TraversalDirectionType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListBulkImportJobsRequestRequestTypeDef = TypedDict(
    "ListBulkImportJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[ListBulkImportJobsFilterType],
    },
)
ListCompositionRelationshipsRequestRequestTypeDef = TypedDict(
    "ListCompositionRelationshipsRequestRequestTypeDef",
    {
        "assetModelId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDashboardsRequestRequestTypeDef = TypedDict(
    "ListDashboardsRequestRequestTypeDef",
    {
        "projectId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListGatewaysRequestRequestTypeDef = TypedDict(
    "ListGatewaysRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListPortalsRequestRequestTypeDef = TypedDict(
    "ListPortalsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListProjectAssetsRequestRequestTypeDef = TypedDict(
    "ListProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "portalId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "description": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "lastUpdateDate": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListTimeSeriesRequestRequestTypeDef = TypedDict(
    "ListTimeSeriesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "assetId": NotRequired[str],
        "aliasPrefix": NotRequired[str],
        "timeSeriesType": NotRequired[ListTimeSeriesTypeType],
    },
)
TimeSeriesSummaryTypeDef = TypedDict(
    "TimeSeriesSummaryTypeDef",
    {
        "timeSeriesId": str,
        "dataType": PropertyDataTypeType,
        "timeSeriesCreationDate": datetime,
        "timeSeriesLastUpdateDate": datetime,
        "timeSeriesArn": str,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "alias": NotRequired[str],
        "dataTypeSpec": NotRequired[str],
    },
)
MetricProcessingConfigTypeDef = TypedDict(
    "MetricProcessingConfigTypeDef",
    {
        "computeLocation": ComputeLocationType,
    },
)
TumblingWindowTypeDef = TypedDict(
    "TumblingWindowTypeDef",
    {
        "interval": str,
        "offset": NotRequired[str],
    },
)
MonitorErrorDetailsTypeDef = TypedDict(
    "MonitorErrorDetailsTypeDef",
    {
        "code": NotRequired[MonitorErrorCodeType],
        "message": NotRequired[str],
    },
)
PortalResourceTypeDef = TypedDict(
    "PortalResourceTypeDef",
    {
        "id": str,
    },
)
ProjectResourceTypeDef = TypedDict(
    "ProjectResourceTypeDef",
    {
        "id": str,
    },
)
PutDefaultEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "PutDefaultEncryptionConfigurationRequestRequestTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyId": NotRequired[str],
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
UpdateAssetPropertyRequestRequestTypeDef = TypedDict(
    "UpdateAssetPropertyRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": NotRequired[str],
        "propertyNotificationState": NotRequired[PropertyNotificationStateType],
        "clientToken": NotRequired[str],
        "propertyUnit": NotRequired[str],
    },
)
UpdateAssetRequestRequestTypeDef = TypedDict(
    "UpdateAssetRequestRequestTypeDef",
    {
        "assetId": str,
        "assetName": str,
        "clientToken": NotRequired[str],
        "assetDescription": NotRequired[str],
        "assetExternalId": NotRequired[str],
    },
)
UpdateDashboardRequestRequestTypeDef = TypedDict(
    "UpdateDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
        "dashboardName": str,
        "dashboardDefinition": str,
        "dashboardDescription": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
UpdateGatewayCapabilityConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationRequestRequestTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
    },
)
UpdateGatewayRequestRequestTypeDef = TypedDict(
    "UpdateGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "projectId": str,
        "projectName": str,
        "projectDescription": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "actionId": NotRequired[str],
        "actionDefinitionId": NotRequired[str],
        "targetResource": NotRequired[TargetResourceTypeDef],
    },
)
ExecuteActionRequestRequestTypeDef = TypedDict(
    "ExecuteActionRequestRequestTypeDef",
    {
        "targetResource": TargetResourceTypeDef,
        "actionDefinitionId": str,
        "actionPayload": ActionPayloadTypeDef,
        "clientToken": NotRequired[str],
    },
)
AggregatedValueTypeDef = TypedDict(
    "AggregatedValueTypeDef",
    {
        "timestamp": datetime,
        "value": AggregatesTypeDef,
        "quality": NotRequired[QualityType],
    },
)
AssetCompositeModelSummaryTypeDef = TypedDict(
    "AssetCompositeModelSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "type": str,
        "description": str,
        "path": List[AssetCompositeModelPathSegmentTypeDef],
        "externalId": NotRequired[str],
    },
)
AssetRelationshipSummaryTypeDef = TypedDict(
    "AssetRelationshipSummaryTypeDef",
    {
        "relationshipType": Literal["HIERARCHY"],
        "hierarchyInfo": NotRequired[AssetHierarchyInfoTypeDef],
    },
)
AssetModelCompositeModelSummaryTypeDef = TypedDict(
    "AssetModelCompositeModelSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "type": str,
        "externalId": NotRequired[str],
        "description": NotRequired[str],
        "path": NotRequired[List[AssetModelCompositeModelPathSegmentTypeDef]],
    },
)
VariableValueOutputTypeDef = TypedDict(
    "VariableValueOutputTypeDef",
    {
        "propertyId": NotRequired[str],
        "hierarchyId": NotRequired[str],
        "propertyPath": NotRequired[List[AssetModelPropertyPathSegmentTypeDef]],
    },
)
VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "propertyId": NotRequired[str],
        "hierarchyId": NotRequired[str],
        "propertyPath": NotRequired[Sequence[AssetModelPropertyPathSegmentTypeDef]],
    },
)
AssetPropertySummaryTypeDef = TypedDict(
    "AssetPropertySummaryTypeDef",
    {
        "id": str,
        "alias": NotRequired[str],
        "unit": NotRequired[str],
        "notification": NotRequired[PropertyNotificationTypeDef],
        "assetCompositeModelId": NotRequired[str],
        "path": NotRequired[List[AssetPropertyPathSegmentTypeDef]],
        "externalId": NotRequired[str],
    },
)
AssetPropertyTypeDef = TypedDict(
    "AssetPropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": PropertyDataTypeType,
        "alias": NotRequired[str],
        "notification": NotRequired[PropertyNotificationTypeDef],
        "dataTypeSpec": NotRequired[str],
        "unit": NotRequired[str],
        "path": NotRequired[List[AssetPropertyPathSegmentTypeDef]],
        "externalId": NotRequired[str],
    },
)
BatchPutAssetPropertyErrorTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorTypeDef",
    {
        "errorCode": BatchPutAssetPropertyValueErrorCodeType,
        "errorMessage": str,
        "timestamps": List[TimeInNanosTypeDef],
    },
)
AssetPropertyValueTypeDef = TypedDict(
    "AssetPropertyValueTypeDef",
    {
        "value": VariantTypeDef,
        "timestamp": TimeInNanosTypeDef,
        "quality": NotRequired[QualityType],
    },
)
InterpolatedAssetPropertyValueTypeDef = TypedDict(
    "InterpolatedAssetPropertyValueTypeDef",
    {
        "timestamp": TimeInNanosTypeDef,
        "value": VariantTypeDef,
    },
)
BatchAssociateProjectAssetsResponseTypeDef = TypedDict(
    "BatchAssociateProjectAssetsResponseTypeDef",
    {
        "errors": List[AssetErrorDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisassociateProjectAssetsResponseTypeDef = TypedDict(
    "BatchDisassociateProjectAssetsResponseTypeDef",
    {
        "errors": List[AssetErrorDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessPolicyResponseTypeDef = TypedDict(
    "CreateAccessPolicyResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBulkImportJobResponseTypeDef = TypedDict(
    "CreateBulkImportJobResponseTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef",
    {
        "dashboardId": str,
        "dashboardArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGatewayResponseTypeDef = TypedDict(
    "CreateGatewayResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeActionResponseTypeDef = TypedDict(
    "DescribeActionResponseTypeDef",
    {
        "actionId": str,
        "targetResource": TargetResourceTypeDef,
        "actionDefinitionId": str,
        "actionPayload": ActionPayloadTypeDef,
        "executionTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDashboardResponseTypeDef = TypedDict(
    "DescribeDashboardResponseTypeDef",
    {
        "dashboardId": str,
        "dashboardArn": str,
        "dashboardName": str,
        "projectId": str,
        "dashboardDescription": str,
        "dashboardDefinition": str,
        "dashboardCreationDate": datetime,
        "dashboardLastUpdateDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGatewayCapabilityConfigurationResponseTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "projectName": str,
        "portalId": str,
        "projectDescription": str,
        "projectCreationDate": datetime,
        "projectLastUpdateDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTimeSeriesResponseTypeDef = TypedDict(
    "DescribeTimeSeriesResponseTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "alias": str,
        "timeSeriesId": str,
        "dataType": PropertyDataTypeType,
        "dataTypeSpec": str,
        "timeSeriesCreationDate": datetime,
        "timeSeriesLastUpdateDate": datetime,
        "timeSeriesArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteActionResponseTypeDef = TypedDict(
    "ExecuteActionResponseTypeDef",
    {
        "actionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectAssetsResponseTypeDef = TypedDict(
    "ListProjectAssetsResponseTypeDef",
    {
        "assetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGatewayCapabilityConfigurationResponseTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetAssetPropertyAggregatesEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesEntryTypeDef",
    {
        "entryId": str,
        "aggregateTypes": Sequence[AggregateTypeType],
        "resolution": str,
        "startDate": TimestampTypeDef,
        "endDate": TimestampTypeDef,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "qualities": NotRequired[Sequence[QualityType]],
        "timeOrdering": NotRequired[TimeOrderingType],
    },
)
BatchGetAssetPropertyValueHistoryEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistoryEntryTypeDef",
    {
        "entryId": str,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "startDate": NotRequired[TimestampTypeDef],
        "endDate": NotRequired[TimestampTypeDef],
        "qualities": NotRequired[Sequence[QualityType]],
        "timeOrdering": NotRequired[TimeOrderingType],
    },
)
GetAssetPropertyAggregatesRequestRequestTypeDef = TypedDict(
    "GetAssetPropertyAggregatesRequestRequestTypeDef",
    {
        "aggregateTypes": Sequence[AggregateTypeType],
        "resolution": str,
        "startDate": TimestampTypeDef,
        "endDate": TimestampTypeDef,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "qualities": NotRequired[Sequence[QualityType]],
        "timeOrdering": NotRequired[TimeOrderingType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetAssetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryRequestRequestTypeDef",
    {
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "startDate": NotRequired[TimestampTypeDef],
        "endDate": NotRequired[TimestampTypeDef],
        "qualities": NotRequired[Sequence[QualityType]],
        "timeOrdering": NotRequired[TimeOrderingType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
BatchGetAssetPropertyAggregatesSkippedEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesSkippedEntryTypeDef",
    {
        "entryId": str,
        "completionStatus": BatchEntryCompletionStatusType,
        "errorInfo": NotRequired[BatchGetAssetPropertyAggregatesErrorInfoTypeDef],
    },
)
BatchGetAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "BatchGetAssetPropertyValueRequestRequestTypeDef",
    {
        "entries": Sequence[BatchGetAssetPropertyValueEntryTypeDef],
        "nextToken": NotRequired[str],
    },
)
BatchGetAssetPropertyValueSkippedEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueSkippedEntryTypeDef",
    {
        "entryId": str,
        "completionStatus": BatchEntryCompletionStatusType,
        "errorInfo": NotRequired[BatchGetAssetPropertyValueErrorInfoTypeDef],
    },
)
BatchGetAssetPropertyValueHistorySkippedEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistorySkippedEntryTypeDef",
    {
        "entryId": str,
        "completionStatus": BatchEntryCompletionStatusType,
        "errorInfo": NotRequired[BatchGetAssetPropertyValueHistoryErrorInfoTypeDef],
    },
)
ImageFileTypeDef = TypedDict(
    "ImageFileTypeDef",
    {
        "data": BlobTypeDef,
        "type": Literal["PNG"],
    },
)
ColumnInfoTypeDef = TypedDict(
    "ColumnInfoTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[ColumnTypeTypeDef],
    },
)
CompositionDetailsTypeDef = TypedDict(
    "CompositionDetailsTypeDef",
    {
        "compositionRelationship": NotRequired[List[CompositionRelationshipItemTypeDef]],
    },
)
ListCompositionRelationshipsResponseTypeDef = TypedDict(
    "ListCompositionRelationshipsResponseTypeDef",
    {
        "compositionRelationshipSummaries": List[CompositionRelationshipSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigurationStatusTypeDef = TypedDict(
    "ConfigurationStatusTypeDef",
    {
        "state": ConfigurationStateType,
        "error": NotRequired[ConfigurationErrorDetailsTypeDef],
    },
)
FileFormatOutputTypeDef = TypedDict(
    "FileFormatOutputTypeDef",
    {
        "csv": NotRequired[CsvOutputTypeDef],
        "parquet": NotRequired[Dict[str, Any]],
    },
)
CsvUnionTypeDef = Union[CsvTypeDef, CsvOutputTypeDef]
MultiLayerStorageTypeDef = TypedDict(
    "MultiLayerStorageTypeDef",
    {
        "customerManagedS3Storage": CustomerManagedS3StorageTypeDef,
    },
)
ListDashboardsResponseTypeDef = TypedDict(
    "ListDashboardsResponseTypeDef",
    {
        "dashboardSummaries": List[DashboardSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RowPaginatorTypeDef = TypedDict(
    "RowPaginatorTypeDef",
    {
        "data": List[DatumPaginatorTypeDef],
    },
)
RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "data": List[DatumTypeDef],
    },
)
DescribeAssetModelRequestAssetModelActiveWaitTypeDef = TypedDict(
    "DescribeAssetModelRequestAssetModelActiveWaitTypeDef",
    {
        "assetModelId": str,
        "excludeProperties": NotRequired[bool],
        "assetModelVersion": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeAssetModelRequestAssetModelNotExistsWaitTypeDef = TypedDict(
    "DescribeAssetModelRequestAssetModelNotExistsWaitTypeDef",
    {
        "assetModelId": str,
        "excludeProperties": NotRequired[bool],
        "assetModelVersion": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeAssetRequestAssetActiveWaitTypeDef = TypedDict(
    "DescribeAssetRequestAssetActiveWaitTypeDef",
    {
        "assetId": str,
        "excludeProperties": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeAssetRequestAssetNotExistsWaitTypeDef = TypedDict(
    "DescribeAssetRequestAssetNotExistsWaitTypeDef",
    {
        "assetId": str,
        "excludeProperties": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribePortalRequestPortalActiveWaitTypeDef = TypedDict(
    "DescribePortalRequestPortalActiveWaitTypeDef",
    {
        "portalId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribePortalRequestPortalNotExistsWaitTypeDef = TypedDict(
    "DescribePortalRequestPortalNotExistsWaitTypeDef",
    {
        "portalId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
    },
)
ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
        "details": NotRequired[List[DetailedErrorTypeDef]],
    },
)
ExecuteQueryRequestExecuteQueryPaginateTypeDef = TypedDict(
    "ExecuteQueryRequestExecuteQueryPaginateTypeDef",
    {
        "queryStatement": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAssetPropertyAggregatesRequestGetAssetPropertyAggregatesPaginateTypeDef = TypedDict(
    "GetAssetPropertyAggregatesRequestGetAssetPropertyAggregatesPaginateTypeDef",
    {
        "aggregateTypes": Sequence[AggregateTypeType],
        "resolution": str,
        "startDate": TimestampTypeDef,
        "endDate": TimestampTypeDef,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "qualities": NotRequired[Sequence[QualityType]],
        "timeOrdering": NotRequired[TimeOrderingType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAssetPropertyValueHistoryRequestGetAssetPropertyValueHistoryPaginateTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryRequestGetAssetPropertyValueHistoryPaginateTypeDef",
    {
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "startDate": NotRequired[TimestampTypeDef],
        "endDate": NotRequired[TimestampTypeDef],
        "qualities": NotRequired[Sequence[QualityType]],
        "timeOrdering": NotRequired[TimeOrderingType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetInterpolatedAssetPropertyValuesRequestGetInterpolatedAssetPropertyValuesPaginateTypeDef = TypedDict(
    "GetInterpolatedAssetPropertyValuesRequestGetInterpolatedAssetPropertyValuesPaginateTypeDef",
    {
        "startTimeInSeconds": int,
        "endTimeInSeconds": int,
        "quality": QualityType,
        "intervalInSeconds": int,
        "type": str,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "startTimeOffsetInNanos": NotRequired[int],
        "endTimeOffsetInNanos": NotRequired[int],
        "intervalWindowInSeconds": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef = TypedDict(
    "ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef",
    {
        "identityType": NotRequired[IdentityTypeType],
        "identityId": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "iamArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListActionsRequestListActionsPaginateTypeDef = TypedDict(
    "ListActionsRequestListActionsPaginateTypeDef",
    {
        "targetResourceType": Literal["ASSET"],
        "targetResourceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetModelCompositeModelsRequestListAssetModelCompositeModelsPaginateTypeDef = TypedDict(
    "ListAssetModelCompositeModelsRequestListAssetModelCompositeModelsPaginateTypeDef",
    {
        "assetModelId": str,
        "assetModelVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetModelPropertiesRequestListAssetModelPropertiesPaginateTypeDef = TypedDict(
    "ListAssetModelPropertiesRequestListAssetModelPropertiesPaginateTypeDef",
    {
        "assetModelId": str,
        "filter": NotRequired[ListAssetModelPropertiesFilterType],
        "assetModelVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetModelsRequestListAssetModelsPaginateTypeDef = TypedDict(
    "ListAssetModelsRequestListAssetModelsPaginateTypeDef",
    {
        "assetModelTypes": NotRequired[Sequence[AssetModelTypeType]],
        "assetModelVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetPropertiesRequestListAssetPropertiesPaginateTypeDef = TypedDict(
    "ListAssetPropertiesRequestListAssetPropertiesPaginateTypeDef",
    {
        "assetId": str,
        "filter": NotRequired[ListAssetPropertiesFilterType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetRelationshipsRequestListAssetRelationshipsPaginateTypeDef = TypedDict(
    "ListAssetRelationshipsRequestListAssetRelationshipsPaginateTypeDef",
    {
        "assetId": str,
        "traversalType": Literal["PATH_TO_ROOT"],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetsRequestListAssetsPaginateTypeDef = TypedDict(
    "ListAssetsRequestListAssetsPaginateTypeDef",
    {
        "assetModelId": NotRequired[str],
        "filter": NotRequired[ListAssetsFilterType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssociatedAssetsRequestListAssociatedAssetsPaginateTypeDef = TypedDict(
    "ListAssociatedAssetsRequestListAssociatedAssetsPaginateTypeDef",
    {
        "assetId": str,
        "hierarchyId": NotRequired[str],
        "traversalDirection": NotRequired[TraversalDirectionType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBulkImportJobsRequestListBulkImportJobsPaginateTypeDef = TypedDict(
    "ListBulkImportJobsRequestListBulkImportJobsPaginateTypeDef",
    {
        "filter": NotRequired[ListBulkImportJobsFilterType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCompositionRelationshipsRequestListCompositionRelationshipsPaginateTypeDef = TypedDict(
    "ListCompositionRelationshipsRequestListCompositionRelationshipsPaginateTypeDef",
    {
        "assetModelId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDashboardsRequestListDashboardsPaginateTypeDef = TypedDict(
    "ListDashboardsRequestListDashboardsPaginateTypeDef",
    {
        "projectId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGatewaysRequestListGatewaysPaginateTypeDef = TypedDict(
    "ListGatewaysRequestListGatewaysPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPortalsRequestListPortalsPaginateTypeDef = TypedDict(
    "ListPortalsRequestListPortalsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectAssetsRequestListProjectAssetsPaginateTypeDef = TypedDict(
    "ListProjectAssetsRequestListProjectAssetsPaginateTypeDef",
    {
        "projectId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "portalId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTimeSeriesRequestListTimeSeriesPaginateTypeDef = TypedDict(
    "ListTimeSeriesRequestListTimeSeriesPaginateTypeDef",
    {
        "assetId": NotRequired[str],
        "aliasPrefix": NotRequired[str],
        "timeSeriesType": NotRequired[ListTimeSeriesTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
MeasurementProcessingConfigTypeDef = TypedDict(
    "MeasurementProcessingConfigTypeDef",
    {
        "forwardingConfig": ForwardingConfigTypeDef,
    },
)
TransformProcessingConfigTypeDef = TypedDict(
    "TransformProcessingConfigTypeDef",
    {
        "computeLocation": ComputeLocationType,
        "forwardingConfig": NotRequired[ForwardingConfigTypeDef],
    },
)
GatewayPlatformTypeDef = TypedDict(
    "GatewayPlatformTypeDef",
    {
        "greengrass": NotRequired[GreengrassTypeDef],
        "greengrassV2": NotRequired[GreengrassV2TypeDef],
        "siemensIE": NotRequired[SiemensIETypeDef],
    },
)
IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "user": NotRequired[UserIdentityTypeDef],
        "group": NotRequired[GroupIdentityTypeDef],
        "iamUser": NotRequired[IAMUserIdentityTypeDef],
        "iamRole": NotRequired[IAMRoleIdentityTypeDef],
    },
)
ListBulkImportJobsResponseTypeDef = TypedDict(
    "ListBulkImportJobsResponseTypeDef",
    {
        "jobSummaries": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "projectSummaries": List[ProjectSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTimeSeriesResponseTypeDef = TypedDict(
    "ListTimeSeriesResponseTypeDef",
    {
        "TimeSeriesSummaries": List[TimeSeriesSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricWindowTypeDef = TypedDict(
    "MetricWindowTypeDef",
    {
        "tumbling": NotRequired[TumblingWindowTypeDef],
    },
)
PortalStatusTypeDef = TypedDict(
    "PortalStatusTypeDef",
    {
        "state": PortalStateType,
        "error": NotRequired[MonitorErrorDetailsTypeDef],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "portal": NotRequired[PortalResourceTypeDef],
        "project": NotRequired[ProjectResourceTypeDef],
    },
)
ListActionsResponseTypeDef = TypedDict(
    "ListActionsResponseTypeDef",
    {
        "actionSummaries": List[ActionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetAssetPropertyAggregatesSuccessEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesSuccessEntryTypeDef",
    {
        "entryId": str,
        "aggregatedValues": List[AggregatedValueTypeDef],
    },
)
GetAssetPropertyAggregatesResponseTypeDef = TypedDict(
    "GetAssetPropertyAggregatesResponseTypeDef",
    {
        "aggregatedValues": List[AggregatedValueTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetRelationshipsResponseTypeDef = TypedDict(
    "ListAssetRelationshipsResponseTypeDef",
    {
        "assetRelationshipSummaries": List[AssetRelationshipSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetModelCompositeModelsResponseTypeDef = TypedDict(
    "ListAssetModelCompositeModelsResponseTypeDef",
    {
        "assetModelCompositeModelSummaries": List[AssetModelCompositeModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExpressionVariableOutputTypeDef = TypedDict(
    "ExpressionVariableOutputTypeDef",
    {
        "name": str,
        "value": VariableValueOutputTypeDef,
    },
)
VariableValueUnionTypeDef = Union[VariableValueTypeDef, VariableValueOutputTypeDef]
ListAssetPropertiesResponseTypeDef = TypedDict(
    "ListAssetPropertiesResponseTypeDef",
    {
        "assetPropertySummaries": List[AssetPropertySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetCompositeModelTypeDef = TypedDict(
    "AssetCompositeModelTypeDef",
    {
        "name": str,
        "type": str,
        "properties": List[AssetPropertyTypeDef],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
DescribeAssetCompositeModelResponseTypeDef = TypedDict(
    "DescribeAssetCompositeModelResponseTypeDef",
    {
        "assetId": str,
        "assetCompositeModelId": str,
        "assetCompositeModelExternalId": str,
        "assetCompositeModelPath": List[AssetCompositeModelPathSegmentTypeDef],
        "assetCompositeModelName": str,
        "assetCompositeModelDescription": str,
        "assetCompositeModelType": str,
        "assetCompositeModelProperties": List[AssetPropertyTypeDef],
        "assetCompositeModelSummaries": List[AssetCompositeModelSummaryTypeDef],
        "actionDefinitions": List[ActionDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutAssetPropertyErrorEntryTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorEntryTypeDef",
    {
        "entryId": str,
        "errors": List[BatchPutAssetPropertyErrorTypeDef],
    },
)
BatchGetAssetPropertyValueHistorySuccessEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistorySuccessEntryTypeDef",
    {
        "entryId": str,
        "assetPropertyValueHistory": List[AssetPropertyValueTypeDef],
    },
)
BatchGetAssetPropertyValueSuccessEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueSuccessEntryTypeDef",
    {
        "entryId": str,
        "assetPropertyValue": NotRequired[AssetPropertyValueTypeDef],
    },
)
GetAssetPropertyValueHistoryResponseTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryResponseTypeDef",
    {
        "assetPropertyValueHistory": List[AssetPropertyValueTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssetPropertyValueResponseTypeDef = TypedDict(
    "GetAssetPropertyValueResponseTypeDef",
    {
        "propertyValue": AssetPropertyValueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAssetPropertyValueEntryTypeDef = TypedDict(
    "PutAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
        "propertyValues": Sequence[AssetPropertyValueTypeDef],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
    },
)
GetInterpolatedAssetPropertyValuesResponseTypeDef = TypedDict(
    "GetInterpolatedAssetPropertyValuesResponseTypeDef",
    {
        "interpolatedAssetPropertyValues": List[InterpolatedAssetPropertyValueTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetAssetPropertyAggregatesRequestRequestTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesRequestRequestTypeDef",
    {
        "entries": Sequence[BatchGetAssetPropertyAggregatesEntryTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
BatchGetAssetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistoryRequestRequestTypeDef",
    {
        "entries": Sequence[BatchGetAssetPropertyValueHistoryEntryTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
CreatePortalRequestRequestTypeDef = TypedDict(
    "CreatePortalRequestRequestTypeDef",
    {
        "portalName": str,
        "portalContactEmail": str,
        "roleArn": str,
        "portalDescription": NotRequired[str],
        "clientToken": NotRequired[str],
        "portalLogoImageFile": NotRequired[ImageFileTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "portalAuthMode": NotRequired[AuthModeType],
        "notificationSenderEmail": NotRequired[str],
        "alarms": NotRequired[AlarmsTypeDef],
    },
)
ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "id": NotRequired[str],
        "file": NotRequired[ImageFileTypeDef],
    },
)
DescribeDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyArn": str,
        "configurationStatus": ConfigurationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyArn": str,
        "configurationStatus": ConfigurationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobConfigurationOutputTypeDef = TypedDict(
    "JobConfigurationOutputTypeDef",
    {
        "fileFormat": FileFormatOutputTypeDef,
    },
)
FileFormatTypeDef = TypedDict(
    "FileFormatTypeDef",
    {
        "csv": NotRequired[CsvUnionTypeDef],
        "parquet": NotRequired[Mapping[str, Any]],
    },
)
DescribeStorageConfigurationResponseTypeDef = TypedDict(
    "DescribeStorageConfigurationResponseTypeDef",
    {
        "storageType": StorageTypeType,
        "multiLayerStorage": MultiLayerStorageTypeDef,
        "disassociatedDataStorage": DisassociatedDataStorageStateType,
        "retentionPeriod": RetentionPeriodTypeDef,
        "configurationStatus": ConfigurationStatusTypeDef,
        "lastUpdateDate": datetime,
        "warmTier": WarmTierStateType,
        "warmTierRetentionPeriod": WarmTierRetentionPeriodTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutStorageConfigurationRequestRequestTypeDef = TypedDict(
    "PutStorageConfigurationRequestRequestTypeDef",
    {
        "storageType": StorageTypeType,
        "multiLayerStorage": NotRequired[MultiLayerStorageTypeDef],
        "disassociatedDataStorage": NotRequired[DisassociatedDataStorageStateType],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "warmTier": NotRequired[WarmTierStateType],
        "warmTierRetentionPeriod": NotRequired[WarmTierRetentionPeriodTypeDef],
    },
)
PutStorageConfigurationResponseTypeDef = TypedDict(
    "PutStorageConfigurationResponseTypeDef",
    {
        "storageType": StorageTypeType,
        "multiLayerStorage": MultiLayerStorageTypeDef,
        "disassociatedDataStorage": DisassociatedDataStorageStateType,
        "retentionPeriod": RetentionPeriodTypeDef,
        "configurationStatus": ConfigurationStatusTypeDef,
        "warmTier": WarmTierStateType,
        "warmTierRetentionPeriod": WarmTierRetentionPeriodTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteQueryResponsePaginatorTypeDef = TypedDict(
    "ExecuteQueryResponsePaginatorTypeDef",
    {
        "columns": List[ColumnInfoTypeDef],
        "rows": List[RowPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteQueryResponseTypeDef = TypedDict(
    "ExecuteQueryResponseTypeDef",
    {
        "columns": List[ColumnInfoTypeDef],
        "rows": List[RowTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetModelStatusTypeDef = TypedDict(
    "AssetModelStatusTypeDef",
    {
        "state": AssetModelStateType,
        "error": NotRequired[ErrorDetailsTypeDef],
    },
)
AssetStatusTypeDef = TypedDict(
    "AssetStatusTypeDef",
    {
        "state": AssetStateType,
        "error": NotRequired[ErrorDetailsTypeDef],
    },
)
MeasurementTypeDef = TypedDict(
    "MeasurementTypeDef",
    {
        "processingConfig": NotRequired[MeasurementProcessingConfigTypeDef],
    },
)
CreateGatewayRequestRequestTypeDef = TypedDict(
    "CreateGatewayRequestRequestTypeDef",
    {
        "gatewayName": str,
        "gatewayPlatform": GatewayPlatformTypeDef,
        "tags": NotRequired[Mapping[str, str]],
    },
)
DescribeGatewayResponseTypeDef = TypedDict(
    "DescribeGatewayResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "gatewayArn": str,
        "gatewayPlatform": GatewayPlatformTypeDef,
        "gatewayCapabilitySummaries": List[GatewayCapabilitySummaryTypeDef],
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GatewaySummaryTypeDef = TypedDict(
    "GatewaySummaryTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "gatewayPlatform": NotRequired[GatewayPlatformTypeDef],
        "gatewayCapabilitySummaries": NotRequired[List[GatewayCapabilitySummaryTypeDef]],
    },
)
CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalStartUrl": str,
        "portalStatus": PortalStatusTypeDef,
        "ssoApplicationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePortalResponseTypeDef = TypedDict(
    "DeletePortalResponseTypeDef",
    {
        "portalStatus": PortalStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePortalResponseTypeDef = TypedDict(
    "DescribePortalResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalName": str,
        "portalDescription": str,
        "portalClientId": str,
        "portalStartUrl": str,
        "portalContactEmail": str,
        "portalStatus": PortalStatusTypeDef,
        "portalCreationDate": datetime,
        "portalLastUpdateDate": datetime,
        "portalLogoImageLocation": ImageLocationTypeDef,
        "roleArn": str,
        "portalAuthMode": AuthModeType,
        "notificationSenderEmail": str,
        "alarms": AlarmsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PortalSummaryTypeDef = TypedDict(
    "PortalSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "startUrl": str,
        "status": PortalStatusTypeDef,
        "description": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "lastUpdateDate": NotRequired[datetime],
        "roleArn": NotRequired[str],
    },
)
UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef",
    {
        "portalStatus": PortalStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AccessPolicySummaryTypeDef = TypedDict(
    "AccessPolicySummaryTypeDef",
    {
        "id": str,
        "identity": IdentityTypeDef,
        "resource": ResourceTypeDef,
        "permission": PermissionType,
        "creationDate": NotRequired[datetime],
        "lastUpdateDate": NotRequired[datetime],
    },
)
CreateAccessPolicyRequestRequestTypeDef = TypedDict(
    "CreateAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyIdentity": IdentityTypeDef,
        "accessPolicyResource": ResourceTypeDef,
        "accessPolicyPermission": PermissionType,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DescribeAccessPolicyResponseTypeDef = TypedDict(
    "DescribeAccessPolicyResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "accessPolicyIdentity": IdentityTypeDef,
        "accessPolicyResource": ResourceTypeDef,
        "accessPolicyPermission": PermissionType,
        "accessPolicyCreationDate": datetime,
        "accessPolicyLastUpdateDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccessPolicyRequestRequestTypeDef = TypedDict(
    "UpdateAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyIdentity": IdentityTypeDef,
        "accessPolicyResource": ResourceTypeDef,
        "accessPolicyPermission": PermissionType,
        "clientToken": NotRequired[str],
    },
)
BatchGetAssetPropertyAggregatesResponseTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesResponseTypeDef",
    {
        "errorEntries": List[BatchGetAssetPropertyAggregatesErrorEntryTypeDef],
        "successEntries": List[BatchGetAssetPropertyAggregatesSuccessEntryTypeDef],
        "skippedEntries": List[BatchGetAssetPropertyAggregatesSkippedEntryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricOutputTypeDef = TypedDict(
    "MetricOutputTypeDef",
    {
        "expression": str,
        "variables": List[ExpressionVariableOutputTypeDef],
        "window": MetricWindowTypeDef,
        "processingConfig": NotRequired[MetricProcessingConfigTypeDef],
    },
)
TransformOutputTypeDef = TypedDict(
    "TransformOutputTypeDef",
    {
        "expression": str,
        "variables": List[ExpressionVariableOutputTypeDef],
        "processingConfig": NotRequired[TransformProcessingConfigTypeDef],
    },
)
ExpressionVariableTypeDef = TypedDict(
    "ExpressionVariableTypeDef",
    {
        "name": str,
        "value": VariableValueUnionTypeDef,
    },
)
BatchPutAssetPropertyValueResponseTypeDef = TypedDict(
    "BatchPutAssetPropertyValueResponseTypeDef",
    {
        "errorEntries": List[BatchPutAssetPropertyErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetAssetPropertyValueHistoryResponseTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistoryResponseTypeDef",
    {
        "errorEntries": List[BatchGetAssetPropertyValueHistoryErrorEntryTypeDef],
        "successEntries": List[BatchGetAssetPropertyValueHistorySuccessEntryTypeDef],
        "skippedEntries": List[BatchGetAssetPropertyValueHistorySkippedEntryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetAssetPropertyValueResponseTypeDef = TypedDict(
    "BatchGetAssetPropertyValueResponseTypeDef",
    {
        "errorEntries": List[BatchGetAssetPropertyValueErrorEntryTypeDef],
        "successEntries": List[BatchGetAssetPropertyValueSuccessEntryTypeDef],
        "skippedEntries": List[BatchGetAssetPropertyValueSkippedEntryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "BatchPutAssetPropertyValueRequestRequestTypeDef",
    {
        "entries": Sequence[PutAssetPropertyValueEntryTypeDef],
    },
)
UpdatePortalRequestRequestTypeDef = TypedDict(
    "UpdatePortalRequestRequestTypeDef",
    {
        "portalId": str,
        "portalName": str,
        "portalContactEmail": str,
        "roleArn": str,
        "portalDescription": NotRequired[str],
        "portalLogoImage": NotRequired[ImageTypeDef],
        "clientToken": NotRequired[str],
        "notificationSenderEmail": NotRequired[str],
        "alarms": NotRequired[AlarmsTypeDef],
    },
)
DescribeBulkImportJobResponseTypeDef = TypedDict(
    "DescribeBulkImportJobResponseTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "jobRoleArn": str,
        "files": List[FileTypeDef],
        "errorReportLocation": ErrorReportLocationTypeDef,
        "jobConfiguration": JobConfigurationOutputTypeDef,
        "jobCreationDate": datetime,
        "jobLastUpdateDate": datetime,
        "adaptiveIngestion": bool,
        "deleteFilesAfterImport": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FileFormatUnionTypeDef = Union[FileFormatTypeDef, FileFormatOutputTypeDef]
AssetModelSummaryTypeDef = TypedDict(
    "AssetModelSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": AssetModelStatusTypeDef,
        "externalId": NotRequired[str],
        "assetModelType": NotRequired[AssetModelTypeType],
        "version": NotRequired[str],
    },
)
CreateAssetModelCompositeModelResponseTypeDef = TypedDict(
    "CreateAssetModelCompositeModelResponseTypeDef",
    {
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelPath": List[AssetModelCompositeModelPathSegmentTypeDef],
        "assetModelStatus": AssetModelStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssetModelResponseTypeDef = TypedDict(
    "CreateAssetModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelArn": str,
        "assetModelStatus": AssetModelStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAssetModelCompositeModelResponseTypeDef = TypedDict(
    "DeleteAssetModelCompositeModelResponseTypeDef",
    {
        "assetModelStatus": AssetModelStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAssetModelResponseTypeDef = TypedDict(
    "DeleteAssetModelResponseTypeDef",
    {
        "assetModelStatus": AssetModelStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssetModelCompositeModelResponseTypeDef = TypedDict(
    "UpdateAssetModelCompositeModelResponseTypeDef",
    {
        "assetModelCompositeModelPath": List[AssetModelCompositeModelPathSegmentTypeDef],
        "assetModelStatus": AssetModelStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssetModelResponseTypeDef = TypedDict(
    "UpdateAssetModelResponseTypeDef",
    {
        "assetModelStatus": AssetModelStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetSummaryTypeDef = TypedDict(
    "AssetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": AssetStatusTypeDef,
        "hierarchies": List[AssetHierarchyTypeDef],
        "description": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
AssociatedAssetsSummaryTypeDef = TypedDict(
    "AssociatedAssetsSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": AssetStatusTypeDef,
        "hierarchies": List[AssetHierarchyTypeDef],
        "description": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetStatus": AssetStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAssetResponseTypeDef = TypedDict(
    "DeleteAssetResponseTypeDef",
    {
        "assetStatus": AssetStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAssetResponseTypeDef = TypedDict(
    "DescribeAssetResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperties": List[AssetPropertyTypeDef],
        "assetHierarchies": List[AssetHierarchyTypeDef],
        "assetCompositeModels": List[AssetCompositeModelTypeDef],
        "assetCreationDate": datetime,
        "assetLastUpdateDate": datetime,
        "assetStatus": AssetStatusTypeDef,
        "assetDescription": str,
        "assetCompositeModelSummaries": List[AssetCompositeModelSummaryTypeDef],
        "assetExternalId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssetResponseTypeDef = TypedDict(
    "UpdateAssetResponseTypeDef",
    {
        "assetStatus": AssetStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGatewaysResponseTypeDef = TypedDict(
    "ListGatewaysResponseTypeDef",
    {
        "gatewaySummaries": List[GatewaySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {
        "portalSummaries": List[PortalSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessPoliciesResponseTypeDef = TypedDict(
    "ListAccessPoliciesResponseTypeDef",
    {
        "accessPolicySummaries": List[AccessPolicySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PropertyTypeOutputTypeDef = TypedDict(
    "PropertyTypeOutputTypeDef",
    {
        "attribute": NotRequired[AttributeTypeDef],
        "measurement": NotRequired[MeasurementTypeDef],
        "transform": NotRequired[TransformOutputTypeDef],
        "metric": NotRequired[MetricOutputTypeDef],
    },
)
ExpressionVariableUnionTypeDef = Union[ExpressionVariableTypeDef, ExpressionVariableOutputTypeDef]
JobConfigurationTypeDef = TypedDict(
    "JobConfigurationTypeDef",
    {
        "fileFormat": FileFormatUnionTypeDef,
    },
)
ListAssetModelsResponseTypeDef = TypedDict(
    "ListAssetModelsResponseTypeDef",
    {
        "assetModelSummaries": List[AssetModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {
        "assetSummaries": List[AssetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssociatedAssetsResponseTypeDef = TypedDict(
    "ListAssociatedAssetsResponseTypeDef",
    {
        "assetSummaries": List[AssociatedAssetsSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetModelPropertyOutputTypeDef = TypedDict(
    "AssetModelPropertyOutputTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": PropertyTypeOutputTypeDef,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
        "dataTypeSpec": NotRequired[str],
        "unit": NotRequired[str],
        "path": NotRequired[List[AssetModelPropertyPathSegmentTypeDef]],
    },
)
AssetModelPropertySummaryTypeDef = TypedDict(
    "AssetModelPropertySummaryTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": PropertyTypeOutputTypeDef,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
        "dataTypeSpec": NotRequired[str],
        "unit": NotRequired[str],
        "assetModelCompositeModelId": NotRequired[str],
        "path": NotRequired[List[AssetModelPropertyPathSegmentTypeDef]],
    },
)
PropertyTypeDef = TypedDict(
    "PropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": PropertyDataTypeType,
        "alias": NotRequired[str],
        "notification": NotRequired[PropertyNotificationTypeDef],
        "unit": NotRequired[str],
        "type": NotRequired[PropertyTypeOutputTypeDef],
        "path": NotRequired[List[AssetPropertyPathSegmentTypeDef]],
        "externalId": NotRequired[str],
    },
)
MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "expression": str,
        "variables": Sequence[ExpressionVariableUnionTypeDef],
        "window": MetricWindowTypeDef,
        "processingConfig": NotRequired[MetricProcessingConfigTypeDef],
    },
)
TransformTypeDef = TypedDict(
    "TransformTypeDef",
    {
        "expression": str,
        "variables": Sequence[ExpressionVariableUnionTypeDef],
        "processingConfig": NotRequired[TransformProcessingConfigTypeDef],
    },
)
CreateBulkImportJobRequestRequestTypeDef = TypedDict(
    "CreateBulkImportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "jobRoleArn": str,
        "files": Sequence[FileTypeDef],
        "errorReportLocation": ErrorReportLocationTypeDef,
        "jobConfiguration": JobConfigurationTypeDef,
        "adaptiveIngestion": NotRequired[bool],
        "deleteFilesAfterImport": NotRequired[bool],
    },
)
AssetModelCompositeModelOutputTypeDef = TypedDict(
    "AssetModelCompositeModelOutputTypeDef",
    {
        "name": str,
        "type": str,
        "description": NotRequired[str],
        "properties": NotRequired[List[AssetModelPropertyOutputTypeDef]],
        "id": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
DescribeAssetModelCompositeModelResponseTypeDef = TypedDict(
    "DescribeAssetModelCompositeModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelExternalId": str,
        "assetModelCompositeModelPath": List[AssetModelCompositeModelPathSegmentTypeDef],
        "assetModelCompositeModelName": str,
        "assetModelCompositeModelDescription": str,
        "assetModelCompositeModelType": str,
        "assetModelCompositeModelProperties": List[AssetModelPropertyOutputTypeDef],
        "compositionDetails": CompositionDetailsTypeDef,
        "assetModelCompositeModelSummaries": List[AssetModelCompositeModelSummaryTypeDef],
        "actionDefinitions": List[ActionDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetModelPropertiesResponseTypeDef = TypedDict(
    "ListAssetModelPropertiesResponseTypeDef",
    {
        "assetModelPropertySummaries": List[AssetModelPropertySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CompositeModelPropertyTypeDef = TypedDict(
    "CompositeModelPropertyTypeDef",
    {
        "name": str,
        "type": str,
        "assetProperty": PropertyTypeDef,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
MetricUnionTypeDef = Union[MetricTypeDef, MetricOutputTypeDef]
TransformUnionTypeDef = Union[TransformTypeDef, TransformOutputTypeDef]
DescribeAssetModelResponseTypeDef = TypedDict(
    "DescribeAssetModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelExternalId": str,
        "assetModelArn": str,
        "assetModelName": str,
        "assetModelType": AssetModelTypeType,
        "assetModelDescription": str,
        "assetModelProperties": List[AssetModelPropertyOutputTypeDef],
        "assetModelHierarchies": List[AssetModelHierarchyTypeDef],
        "assetModelCompositeModels": List[AssetModelCompositeModelOutputTypeDef],
        "assetModelCompositeModelSummaries": List[AssetModelCompositeModelSummaryTypeDef],
        "assetModelCreationDate": datetime,
        "assetModelLastUpdateDate": datetime,
        "assetModelStatus": AssetModelStatusTypeDef,
        "assetModelVersion": str,
        "eTag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAssetPropertyResponseTypeDef = TypedDict(
    "DescribeAssetPropertyResponseTypeDef",
    {
        "assetId": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperty": PropertyTypeDef,
        "compositeModel": CompositeModelPropertyTypeDef,
        "assetExternalId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PropertyTypeTypeDef = TypedDict(
    "PropertyTypeTypeDef",
    {
        "attribute": NotRequired[AttributeTypeDef],
        "measurement": NotRequired[MeasurementTypeDef],
        "transform": NotRequired[TransformUnionTypeDef],
        "metric": NotRequired[MetricUnionTypeDef],
    },
)
PropertyTypeUnionTypeDef = Union[PropertyTypeTypeDef, PropertyTypeOutputTypeDef]
AssetModelPropertyDefinitionTypeDef = TypedDict(
    "AssetModelPropertyDefinitionTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": PropertyTypeUnionTypeDef,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
        "dataTypeSpec": NotRequired[str],
        "unit": NotRequired[str],
    },
)
AssetModelPropertyTypeDef = TypedDict(
    "AssetModelPropertyTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": PropertyTypeUnionTypeDef,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
        "dataTypeSpec": NotRequired[str],
        "unit": NotRequired[str],
        "path": NotRequired[Sequence[AssetModelPropertyPathSegmentTypeDef]],
    },
)
AssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "AssetModelCompositeModelDefinitionTypeDef",
    {
        "name": str,
        "type": str,
        "id": NotRequired[str],
        "externalId": NotRequired[str],
        "description": NotRequired[str],
        "properties": NotRequired[Sequence[AssetModelPropertyDefinitionTypeDef]],
    },
)
CreateAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "CreateAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelName": str,
        "assetModelCompositeModelType": str,
        "assetModelCompositeModelExternalId": NotRequired[str],
        "parentAssetModelCompositeModelId": NotRequired[str],
        "assetModelCompositeModelId": NotRequired[str],
        "assetModelCompositeModelDescription": NotRequired[str],
        "clientToken": NotRequired[str],
        "composedAssetModelId": NotRequired[str],
        "assetModelCompositeModelProperties": NotRequired[
            Sequence[AssetModelPropertyDefinitionTypeDef]
        ],
        "ifMatch": NotRequired[str],
        "ifNoneMatch": NotRequired[str],
        "matchForVersionType": NotRequired[AssetModelVersionTypeType],
    },
)
AssetModelPropertyUnionTypeDef = Union[AssetModelPropertyTypeDef, AssetModelPropertyOutputTypeDef]
UpdateAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "UpdateAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelName": str,
        "assetModelCompositeModelExternalId": NotRequired[str],
        "assetModelCompositeModelDescription": NotRequired[str],
        "clientToken": NotRequired[str],
        "assetModelCompositeModelProperties": NotRequired[Sequence[AssetModelPropertyTypeDef]],
        "ifMatch": NotRequired[str],
        "ifNoneMatch": NotRequired[str],
        "matchForVersionType": NotRequired[AssetModelVersionTypeType],
    },
)
CreateAssetModelRequestRequestTypeDef = TypedDict(
    "CreateAssetModelRequestRequestTypeDef",
    {
        "assetModelName": str,
        "assetModelType": NotRequired[AssetModelTypeType],
        "assetModelId": NotRequired[str],
        "assetModelExternalId": NotRequired[str],
        "assetModelDescription": NotRequired[str],
        "assetModelProperties": NotRequired[Sequence[AssetModelPropertyDefinitionTypeDef]],
        "assetModelHierarchies": NotRequired[Sequence[AssetModelHierarchyDefinitionTypeDef]],
        "assetModelCompositeModels": NotRequired[
            Sequence[AssetModelCompositeModelDefinitionTypeDef]
        ],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
AssetModelCompositeModelTypeDef = TypedDict(
    "AssetModelCompositeModelTypeDef",
    {
        "name": str,
        "type": str,
        "description": NotRequired[str],
        "properties": NotRequired[Sequence[AssetModelPropertyUnionTypeDef]],
        "id": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
AssetModelCompositeModelUnionTypeDef = Union[
    AssetModelCompositeModelTypeDef, AssetModelCompositeModelOutputTypeDef
]
UpdateAssetModelRequestRequestTypeDef = TypedDict(
    "UpdateAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelName": str,
        "assetModelExternalId": NotRequired[str],
        "assetModelDescription": NotRequired[str],
        "assetModelProperties": NotRequired[Sequence[AssetModelPropertyUnionTypeDef]],
        "assetModelHierarchies": NotRequired[Sequence[AssetModelHierarchyTypeDef]],
        "assetModelCompositeModels": NotRequired[Sequence[AssetModelCompositeModelUnionTypeDef]],
        "clientToken": NotRequired[str],
        "ifMatch": NotRequired[str],
        "ifNoneMatch": NotRequired[str],
        "matchForVersionType": NotRequired[AssetModelVersionTypeType],
    },
)
