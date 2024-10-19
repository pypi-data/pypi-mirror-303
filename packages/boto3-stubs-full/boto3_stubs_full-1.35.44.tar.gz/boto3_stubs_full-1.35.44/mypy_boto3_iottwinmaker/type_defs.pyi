"""
Type annotations for iottwinmaker service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/type_defs/)

Usage::

    ```python
    from mypy_boto3_iottwinmaker.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    ColumnTypeType,
    ComponentUpdateTypeType,
    DestinationTypeType,
    ErrorCodeType,
    MetadataTransferJobStateType,
    OrderByTimeType,
    OrderType,
    ParentEntityUpdateTypeType,
    PricingModeType,
    PricingTierType,
    PropertyGroupUpdateTypeType,
    PropertyUpdateTypeType,
    ScopeType,
    SourceTypeType,
    StateType,
    SyncJobStateType,
    SyncResourceStateType,
    SyncResourceTypeType,
    TypeType,
    UpdateReasonType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "BundleInformationTypeDef",
    "CancelMetadataTransferJobRequestRequestTypeDef",
    "MetadataTransferJobProgressTypeDef",
    "ColumnDescriptionTypeDef",
    "ComponentPropertyGroupRequestTypeDef",
    "ComponentPropertyGroupResponseTypeDef",
    "CompositeComponentTypeRequestTypeDef",
    "CompositeComponentTypeResponseTypeDef",
    "PropertyGroupRequestTypeDef",
    "CreateSceneRequestRequestTypeDef",
    "CreateSyncJobRequestRequestTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "LambdaFunctionTypeDef",
    "RelationshipTypeDef",
    "RelationshipValueTypeDef",
    "DeleteComponentTypeRequestRequestTypeDef",
    "DeleteEntityRequestRequestTypeDef",
    "DeleteSceneRequestRequestTypeDef",
    "DeleteSyncJobRequestRequestTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "IotTwinMakerDestinationConfigurationTypeDef",
    "S3DestinationConfigurationTypeDef",
    "EntityPropertyReferenceOutputTypeDef",
    "EntityPropertyReferenceTypeDef",
    "ErrorDetailsTypeDef",
    "ExecuteQueryRequestRequestTypeDef",
    "RowTypeDef",
    "FilterByAssetModelTypeDef",
    "FilterByAssetTypeDef",
    "FilterByComponentTypeTypeDef",
    "FilterByEntityTypeDef",
    "GetComponentTypeRequestRequestTypeDef",
    "PropertyGroupResponseTypeDef",
    "GetEntityRequestRequestTypeDef",
    "GetMetadataTransferJobRequestRequestTypeDef",
    "InterpolationParametersTypeDef",
    "TimestampTypeDef",
    "GetSceneRequestRequestTypeDef",
    "SceneErrorTypeDef",
    "GetSyncJobRequestRequestTypeDef",
    "GetWorkspaceRequestRequestTypeDef",
    "ListComponentTypesFilterTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListEntitiesFilterTypeDef",
    "ListMetadataTransferJobsFilterTypeDef",
    "ListPropertiesRequestRequestTypeDef",
    "ListScenesRequestRequestTypeDef",
    "SceneSummaryTypeDef",
    "ListSyncJobsRequestRequestTypeDef",
    "SyncResourceFilterTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "WorkspaceSummaryTypeDef",
    "OrderByTypeDef",
    "ParentEntityUpdateRequestTypeDef",
    "S3SourceConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePricingPlanRequestRequestTypeDef",
    "UpdateSceneRequestRequestTypeDef",
    "UpdateWorkspaceRequestRequestTypeDef",
    "CreateComponentTypeResponseTypeDef",
    "CreateEntityResponseTypeDef",
    "CreateSceneResponseTypeDef",
    "CreateSyncJobResponseTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteComponentTypeResponseTypeDef",
    "DeleteEntityResponseTypeDef",
    "DeleteSyncJobResponseTypeDef",
    "DeleteWorkspaceResponseTypeDef",
    "GetWorkspaceResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateComponentTypeResponseTypeDef",
    "UpdateEntityResponseTypeDef",
    "UpdateSceneResponseTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "PricingPlanTypeDef",
    "DataConnectorTypeDef",
    "DataValueOutputTypeDef",
    "DataValueTypeDef",
    "DestinationConfigurationTypeDef",
    "EntityPropertyReferenceUnionTypeDef",
    "MetadataTransferJobStatusTypeDef",
    "StatusTypeDef",
    "SyncJobStatusTypeDef",
    "SyncResourceStatusTypeDef",
    "ExecuteQueryResponseTypeDef",
    "IotSiteWiseSourceConfigurationFilterTypeDef",
    "IotTwinMakerSourceConfigurationFilterTypeDef",
    "GetSceneResponseTypeDef",
    "ListComponentTypesRequestRequestTypeDef",
    "ListEntitiesRequestRequestTypeDef",
    "ListMetadataTransferJobsRequestRequestTypeDef",
    "ListScenesResponseTypeDef",
    "ListSyncResourcesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "GetPricingPlanResponseTypeDef",
    "UpdatePricingPlanResponseTypeDef",
    "FunctionRequestTypeDef",
    "FunctionResponseTypeDef",
    "DataTypeOutputTypeDef",
    "PropertyLatestValueTypeDef",
    "PropertyValueOutputTypeDef",
    "DataValueUnionTypeDef",
    "CancelMetadataTransferJobResponseTypeDef",
    "CreateMetadataTransferJobResponseTypeDef",
    "MetadataTransferJobSummaryTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeSummaryTypeDef",
    "EntitySummaryTypeDef",
    "GetSyncJobResponseTypeDef",
    "SyncJobSummaryTypeDef",
    "SyncResourceSummaryTypeDef",
    "IotSiteWiseSourceConfigurationOutputTypeDef",
    "IotSiteWiseSourceConfigurationTypeDef",
    "IotTwinMakerSourceConfigurationOutputTypeDef",
    "IotTwinMakerSourceConfigurationTypeDef",
    "PropertyDefinitionResponseTypeDef",
    "GetPropertyValueResponseTypeDef",
    "PropertyValueEntryOutputTypeDef",
    "PropertyValueHistoryTypeDef",
    "DataTypeTypeDef",
    "PropertyFilterTypeDef",
    "PropertyValueTypeDef",
    "ListMetadataTransferJobsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "ListComponentTypesResponseTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListSyncJobsResponseTypeDef",
    "ListSyncResourcesResponseTypeDef",
    "IotSiteWiseSourceConfigurationUnionTypeDef",
    "SourceConfigurationOutputTypeDef",
    "IotTwinMakerSourceConfigurationUnionTypeDef",
    "GetComponentTypeResponseTypeDef",
    "PropertyResponseTypeDef",
    "PropertySummaryTypeDef",
    "BatchPutPropertyErrorTypeDef",
    "GetPropertyValueHistoryResponseTypeDef",
    "DataTypeUnionTypeDef",
    "GetPropertyValueHistoryRequestRequestTypeDef",
    "TabularConditionsTypeDef",
    "PropertyValueUnionTypeDef",
    "GetMetadataTransferJobResponseTypeDef",
    "SourceConfigurationTypeDef",
    "ComponentResponseTypeDef",
    "ListPropertiesResponseTypeDef",
    "BatchPutPropertyErrorEntryTypeDef",
    "PropertyDefinitionRequestTypeDef",
    "GetPropertyValueRequestRequestTypeDef",
    "PropertyValueEntryTypeDef",
    "SourceConfigurationUnionTypeDef",
    "GetEntityResponseTypeDef",
    "BatchPutPropertyValuesResponseTypeDef",
    "CreateComponentTypeRequestRequestTypeDef",
    "PropertyRequestTypeDef",
    "UpdateComponentTypeRequestRequestTypeDef",
    "PropertyValueEntryUnionTypeDef",
    "CreateMetadataTransferJobRequestRequestTypeDef",
    "ComponentRequestTypeDef",
    "ComponentUpdateRequestTypeDef",
    "CompositeComponentRequestTypeDef",
    "CompositeComponentUpdateRequestTypeDef",
    "BatchPutPropertyValuesRequestRequestTypeDef",
    "CreateEntityRequestRequestTypeDef",
    "UpdateEntityRequestRequestTypeDef",
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
BundleInformationTypeDef = TypedDict(
    "BundleInformationTypeDef",
    {
        "bundleNames": List[str],
        "pricingTier": NotRequired[PricingTierType],
    },
)
CancelMetadataTransferJobRequestRequestTypeDef = TypedDict(
    "CancelMetadataTransferJobRequestRequestTypeDef",
    {
        "metadataTransferJobId": str,
    },
)
MetadataTransferJobProgressTypeDef = TypedDict(
    "MetadataTransferJobProgressTypeDef",
    {
        "totalCount": NotRequired[int],
        "succeededCount": NotRequired[int],
        "skippedCount": NotRequired[int],
        "failedCount": NotRequired[int],
    },
)
ColumnDescriptionTypeDef = TypedDict(
    "ColumnDescriptionTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[ColumnTypeType],
    },
)
ComponentPropertyGroupRequestTypeDef = TypedDict(
    "ComponentPropertyGroupRequestTypeDef",
    {
        "groupType": NotRequired[Literal["TABULAR"]],
        "propertyNames": NotRequired[Sequence[str]],
        "updateType": NotRequired[PropertyGroupUpdateTypeType],
    },
)
ComponentPropertyGroupResponseTypeDef = TypedDict(
    "ComponentPropertyGroupResponseTypeDef",
    {
        "groupType": Literal["TABULAR"],
        "propertyNames": List[str],
        "isInherited": bool,
    },
)
CompositeComponentTypeRequestTypeDef = TypedDict(
    "CompositeComponentTypeRequestTypeDef",
    {
        "componentTypeId": NotRequired[str],
    },
)
CompositeComponentTypeResponseTypeDef = TypedDict(
    "CompositeComponentTypeResponseTypeDef",
    {
        "componentTypeId": NotRequired[str],
        "isInherited": NotRequired[bool],
    },
)
PropertyGroupRequestTypeDef = TypedDict(
    "PropertyGroupRequestTypeDef",
    {
        "groupType": NotRequired[Literal["TABULAR"]],
        "propertyNames": NotRequired[Sequence[str]],
    },
)
CreateSceneRequestRequestTypeDef = TypedDict(
    "CreateSceneRequestRequestTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
        "contentLocation": str,
        "description": NotRequired[str],
        "capabilities": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
        "sceneMetadata": NotRequired[Mapping[str, str]],
    },
)
CreateSyncJobRequestRequestTypeDef = TypedDict(
    "CreateSyncJobRequestRequestTypeDef",
    {
        "workspaceId": str,
        "syncSource": str,
        "syncRole": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateWorkspaceRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "description": NotRequired[str],
        "s3Location": NotRequired[str],
        "role": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
LambdaFunctionTypeDef = TypedDict(
    "LambdaFunctionTypeDef",
    {
        "arn": str,
    },
)
RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "targetComponentTypeId": NotRequired[str],
        "relationshipType": NotRequired[str],
    },
)
RelationshipValueTypeDef = TypedDict(
    "RelationshipValueTypeDef",
    {
        "targetEntityId": NotRequired[str],
        "targetComponentName": NotRequired[str],
    },
)
DeleteComponentTypeRequestRequestTypeDef = TypedDict(
    "DeleteComponentTypeRequestRequestTypeDef",
    {
        "workspaceId": str,
        "componentTypeId": str,
    },
)
DeleteEntityRequestRequestTypeDef = TypedDict(
    "DeleteEntityRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityId": str,
        "isRecursive": NotRequired[bool],
    },
)
DeleteSceneRequestRequestTypeDef = TypedDict(
    "DeleteSceneRequestRequestTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
    },
)
DeleteSyncJobRequestRequestTypeDef = TypedDict(
    "DeleteSyncJobRequestRequestTypeDef",
    {
        "workspaceId": str,
        "syncSource": str,
    },
)
DeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
IotTwinMakerDestinationConfigurationTypeDef = TypedDict(
    "IotTwinMakerDestinationConfigurationTypeDef",
    {
        "workspace": str,
    },
)
S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "location": str,
    },
)
EntityPropertyReferenceOutputTypeDef = TypedDict(
    "EntityPropertyReferenceOutputTypeDef",
    {
        "propertyName": str,
        "componentName": NotRequired[str],
        "componentPath": NotRequired[str],
        "externalIdProperty": NotRequired[Dict[str, str]],
        "entityId": NotRequired[str],
    },
)
EntityPropertyReferenceTypeDef = TypedDict(
    "EntityPropertyReferenceTypeDef",
    {
        "propertyName": str,
        "componentName": NotRequired[str],
        "componentPath": NotRequired[str],
        "externalIdProperty": NotRequired[Mapping[str, str]],
        "entityId": NotRequired[str],
    },
)
ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": NotRequired[ErrorCodeType],
        "message": NotRequired[str],
    },
)
ExecuteQueryRequestRequestTypeDef = TypedDict(
    "ExecuteQueryRequestRequestTypeDef",
    {
        "workspaceId": str,
        "queryStatement": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "rowData": NotRequired[List[Dict[str, Any]]],
    },
)
FilterByAssetModelTypeDef = TypedDict(
    "FilterByAssetModelTypeDef",
    {
        "assetModelId": NotRequired[str],
        "assetModelExternalId": NotRequired[str],
        "includeOffspring": NotRequired[bool],
        "includeAssets": NotRequired[bool],
    },
)
FilterByAssetTypeDef = TypedDict(
    "FilterByAssetTypeDef",
    {
        "assetId": NotRequired[str],
        "assetExternalId": NotRequired[str],
        "includeOffspring": NotRequired[bool],
        "includeAssetModel": NotRequired[bool],
    },
)
FilterByComponentTypeTypeDef = TypedDict(
    "FilterByComponentTypeTypeDef",
    {
        "componentTypeId": str,
    },
)
FilterByEntityTypeDef = TypedDict(
    "FilterByEntityTypeDef",
    {
        "entityId": str,
    },
)
GetComponentTypeRequestRequestTypeDef = TypedDict(
    "GetComponentTypeRequestRequestTypeDef",
    {
        "workspaceId": str,
        "componentTypeId": str,
    },
)
PropertyGroupResponseTypeDef = TypedDict(
    "PropertyGroupResponseTypeDef",
    {
        "groupType": Literal["TABULAR"],
        "propertyNames": List[str],
        "isInherited": bool,
    },
)
GetEntityRequestRequestTypeDef = TypedDict(
    "GetEntityRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityId": str,
    },
)
GetMetadataTransferJobRequestRequestTypeDef = TypedDict(
    "GetMetadataTransferJobRequestRequestTypeDef",
    {
        "metadataTransferJobId": str,
    },
)
InterpolationParametersTypeDef = TypedDict(
    "InterpolationParametersTypeDef",
    {
        "interpolationType": NotRequired[Literal["LINEAR"]],
        "intervalInSeconds": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
GetSceneRequestRequestTypeDef = TypedDict(
    "GetSceneRequestRequestTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
    },
)
SceneErrorTypeDef = TypedDict(
    "SceneErrorTypeDef",
    {
        "code": NotRequired[Literal["MATTERPORT_ERROR"]],
        "message": NotRequired[str],
    },
)
GetSyncJobRequestRequestTypeDef = TypedDict(
    "GetSyncJobRequestRequestTypeDef",
    {
        "syncSource": str,
        "workspaceId": NotRequired[str],
    },
)
GetWorkspaceRequestRequestTypeDef = TypedDict(
    "GetWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
ListComponentTypesFilterTypeDef = TypedDict(
    "ListComponentTypesFilterTypeDef",
    {
        "extendsFrom": NotRequired[str],
        "namespace": NotRequired[str],
        "isAbstract": NotRequired[bool],
    },
)
ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityId": str,
        "componentPath": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEntitiesFilterTypeDef = TypedDict(
    "ListEntitiesFilterTypeDef",
    {
        "parentEntityId": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
ListMetadataTransferJobsFilterTypeDef = TypedDict(
    "ListMetadataTransferJobsFilterTypeDef",
    {
        "workspaceId": NotRequired[str],
        "state": NotRequired[MetadataTransferJobStateType],
    },
)
ListPropertiesRequestRequestTypeDef = TypedDict(
    "ListPropertiesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityId": str,
        "componentName": NotRequired[str],
        "componentPath": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListScenesRequestRequestTypeDef = TypedDict(
    "ListScenesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SceneSummaryTypeDef = TypedDict(
    "SceneSummaryTypeDef",
    {
        "sceneId": str,
        "contentLocation": str,
        "arn": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "description": NotRequired[str],
    },
)
ListSyncJobsRequestRequestTypeDef = TypedDict(
    "ListSyncJobsRequestRequestTypeDef",
    {
        "workspaceId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SyncResourceFilterTypeDef = TypedDict(
    "SyncResourceFilterTypeDef",
    {
        "state": NotRequired[SyncResourceStateType],
        "resourceType": NotRequired[SyncResourceTypeType],
        "resourceId": NotRequired[str],
        "externalId": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
WorkspaceSummaryTypeDef = TypedDict(
    "WorkspaceSummaryTypeDef",
    {
        "workspaceId": str,
        "arn": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "description": NotRequired[str],
        "linkedServices": NotRequired[List[str]],
    },
)
OrderByTypeDef = TypedDict(
    "OrderByTypeDef",
    {
        "propertyName": str,
        "order": NotRequired[OrderType],
    },
)
ParentEntityUpdateRequestTypeDef = TypedDict(
    "ParentEntityUpdateRequestTypeDef",
    {
        "updateType": ParentEntityUpdateTypeType,
        "parentEntityId": NotRequired[str],
    },
)
S3SourceConfigurationTypeDef = TypedDict(
    "S3SourceConfigurationTypeDef",
    {
        "location": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)
UpdatePricingPlanRequestRequestTypeDef = TypedDict(
    "UpdatePricingPlanRequestRequestTypeDef",
    {
        "pricingMode": PricingModeType,
        "bundleNames": NotRequired[Sequence[str]],
    },
)
UpdateSceneRequestRequestTypeDef = TypedDict(
    "UpdateSceneRequestRequestTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
        "contentLocation": NotRequired[str],
        "description": NotRequired[str],
        "capabilities": NotRequired[Sequence[str]],
        "sceneMetadata": NotRequired[Mapping[str, str]],
    },
)
UpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "description": NotRequired[str],
        "role": NotRequired[str],
        "s3Location": NotRequired[str],
    },
)
CreateComponentTypeResponseTypeDef = TypedDict(
    "CreateComponentTypeResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "state": StateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEntityResponseTypeDef = TypedDict(
    "CreateEntityResponseTypeDef",
    {
        "entityId": str,
        "arn": str,
        "creationDateTime": datetime,
        "state": StateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSceneResponseTypeDef = TypedDict(
    "CreateSceneResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSyncJobResponseTypeDef = TypedDict(
    "CreateSyncJobResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "state": SyncJobStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteComponentTypeResponseTypeDef = TypedDict(
    "DeleteComponentTypeResponseTypeDef",
    {
        "state": StateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEntityResponseTypeDef = TypedDict(
    "DeleteEntityResponseTypeDef",
    {
        "state": StateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSyncJobResponseTypeDef = TypedDict(
    "DeleteSyncJobResponseTypeDef",
    {
        "state": SyncJobStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkspaceResponseTypeDef = TypedDict(
    "DeleteWorkspaceResponseTypeDef",
    {
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkspaceResponseTypeDef = TypedDict(
    "GetWorkspaceResponseTypeDef",
    {
        "workspaceId": str,
        "arn": str,
        "description": str,
        "linkedServices": List[str],
        "s3Location": str,
        "role": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateComponentTypeResponseTypeDef = TypedDict(
    "UpdateComponentTypeResponseTypeDef",
    {
        "workspaceId": str,
        "arn": str,
        "componentTypeId": str,
        "state": StateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEntityResponseTypeDef = TypedDict(
    "UpdateEntityResponseTypeDef",
    {
        "updateDateTime": datetime,
        "state": StateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSceneResponseTypeDef = TypedDict(
    "UpdateSceneResponseTypeDef",
    {
        "updateDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkspaceResponseTypeDef = TypedDict(
    "UpdateWorkspaceResponseTypeDef",
    {
        "updateDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PricingPlanTypeDef = TypedDict(
    "PricingPlanTypeDef",
    {
        "effectiveDateTime": datetime,
        "pricingMode": PricingModeType,
        "updateDateTime": datetime,
        "updateReason": UpdateReasonType,
        "billableEntityCount": NotRequired[int],
        "bundleInformation": NotRequired[BundleInformationTypeDef],
    },
)
DataConnectorTypeDef = TypedDict(
    "DataConnectorTypeDef",
    {
        "lambda": NotRequired[LambdaFunctionTypeDef],
        "isNative": NotRequired[bool],
    },
)
DataValueOutputTypeDef = TypedDict(
    "DataValueOutputTypeDef",
    {
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "integerValue": NotRequired[int],
        "longValue": NotRequired[int],
        "stringValue": NotRequired[str],
        "listValue": NotRequired[List[Dict[str, Any]]],
        "mapValue": NotRequired[Dict[str, Dict[str, Any]]],
        "relationshipValue": NotRequired[RelationshipValueTypeDef],
        "expression": NotRequired[str],
    },
)
DataValueTypeDef = TypedDict(
    "DataValueTypeDef",
    {
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "integerValue": NotRequired[int],
        "longValue": NotRequired[int],
        "stringValue": NotRequired[str],
        "listValue": NotRequired[Sequence[Mapping[str, Any]]],
        "mapValue": NotRequired[Mapping[str, Mapping[str, Any]]],
        "relationshipValue": NotRequired[RelationshipValueTypeDef],
        "expression": NotRequired[str],
    },
)
DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "type": DestinationTypeType,
        "s3Configuration": NotRequired[S3DestinationConfigurationTypeDef],
        "iotTwinMakerConfiguration": NotRequired[IotTwinMakerDestinationConfigurationTypeDef],
    },
)
EntityPropertyReferenceUnionTypeDef = Union[
    EntityPropertyReferenceTypeDef, EntityPropertyReferenceOutputTypeDef
]
MetadataTransferJobStatusTypeDef = TypedDict(
    "MetadataTransferJobStatusTypeDef",
    {
        "state": NotRequired[MetadataTransferJobStateType],
        "error": NotRequired[ErrorDetailsTypeDef],
        "queuedPosition": NotRequired[int],
    },
)
StatusTypeDef = TypedDict(
    "StatusTypeDef",
    {
        "state": NotRequired[StateType],
        "error": NotRequired[ErrorDetailsTypeDef],
    },
)
SyncJobStatusTypeDef = TypedDict(
    "SyncJobStatusTypeDef",
    {
        "state": NotRequired[SyncJobStateType],
        "error": NotRequired[ErrorDetailsTypeDef],
    },
)
SyncResourceStatusTypeDef = TypedDict(
    "SyncResourceStatusTypeDef",
    {
        "state": NotRequired[SyncResourceStateType],
        "error": NotRequired[ErrorDetailsTypeDef],
    },
)
ExecuteQueryResponseTypeDef = TypedDict(
    "ExecuteQueryResponseTypeDef",
    {
        "columnDescriptions": List[ColumnDescriptionTypeDef],
        "rows": List[RowTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IotSiteWiseSourceConfigurationFilterTypeDef = TypedDict(
    "IotSiteWiseSourceConfigurationFilterTypeDef",
    {
        "filterByAssetModel": NotRequired[FilterByAssetModelTypeDef],
        "filterByAsset": NotRequired[FilterByAssetTypeDef],
    },
)
IotTwinMakerSourceConfigurationFilterTypeDef = TypedDict(
    "IotTwinMakerSourceConfigurationFilterTypeDef",
    {
        "filterByComponentType": NotRequired[FilterByComponentTypeTypeDef],
        "filterByEntity": NotRequired[FilterByEntityTypeDef],
    },
)
GetSceneResponseTypeDef = TypedDict(
    "GetSceneResponseTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
        "contentLocation": str,
        "arn": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "description": str,
        "capabilities": List[str],
        "sceneMetadata": Dict[str, str],
        "generatedSceneMetadata": Dict[str, str],
        "error": SceneErrorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComponentTypesRequestRequestTypeDef = TypedDict(
    "ListComponentTypesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "filters": NotRequired[Sequence[ListComponentTypesFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListEntitiesRequestRequestTypeDef = TypedDict(
    "ListEntitiesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "filters": NotRequired[Sequence[ListEntitiesFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListMetadataTransferJobsRequestRequestTypeDef = TypedDict(
    "ListMetadataTransferJobsRequestRequestTypeDef",
    {
        "sourceType": SourceTypeType,
        "destinationType": DestinationTypeType,
        "filters": NotRequired[Sequence[ListMetadataTransferJobsFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListScenesResponseTypeDef = TypedDict(
    "ListScenesResponseTypeDef",
    {
        "sceneSummaries": List[SceneSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSyncResourcesRequestRequestTypeDef = TypedDict(
    "ListSyncResourcesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "syncSource": str,
        "filters": NotRequired[Sequence[SyncResourceFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "workspaceSummaries": List[WorkspaceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPricingPlanResponseTypeDef = TypedDict(
    "GetPricingPlanResponseTypeDef",
    {
        "currentPricingPlan": PricingPlanTypeDef,
        "pendingPricingPlan": PricingPlanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePricingPlanResponseTypeDef = TypedDict(
    "UpdatePricingPlanResponseTypeDef",
    {
        "currentPricingPlan": PricingPlanTypeDef,
        "pendingPricingPlan": PricingPlanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FunctionRequestTypeDef = TypedDict(
    "FunctionRequestTypeDef",
    {
        "requiredProperties": NotRequired[Sequence[str]],
        "scope": NotRequired[ScopeType],
        "implementedBy": NotRequired[DataConnectorTypeDef],
    },
)
FunctionResponseTypeDef = TypedDict(
    "FunctionResponseTypeDef",
    {
        "requiredProperties": NotRequired[List[str]],
        "scope": NotRequired[ScopeType],
        "implementedBy": NotRequired[DataConnectorTypeDef],
        "isInherited": NotRequired[bool],
    },
)
DataTypeOutputTypeDef = TypedDict(
    "DataTypeOutputTypeDef",
    {
        "type": TypeType,
        "nestedType": NotRequired[Dict[str, Any]],
        "allowedValues": NotRequired[List[DataValueOutputTypeDef]],
        "unitOfMeasure": NotRequired[str],
        "relationship": NotRequired[RelationshipTypeDef],
    },
)
PropertyLatestValueTypeDef = TypedDict(
    "PropertyLatestValueTypeDef",
    {
        "propertyReference": EntityPropertyReferenceOutputTypeDef,
        "propertyValue": NotRequired[DataValueOutputTypeDef],
    },
)
PropertyValueOutputTypeDef = TypedDict(
    "PropertyValueOutputTypeDef",
    {
        "value": DataValueOutputTypeDef,
        "timestamp": NotRequired[datetime],
        "time": NotRequired[str],
    },
)
DataValueUnionTypeDef = Union[DataValueTypeDef, DataValueOutputTypeDef]
CancelMetadataTransferJobResponseTypeDef = TypedDict(
    "CancelMetadataTransferJobResponseTypeDef",
    {
        "metadataTransferJobId": str,
        "arn": str,
        "updateDateTime": datetime,
        "status": MetadataTransferJobStatusTypeDef,
        "progress": MetadataTransferJobProgressTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMetadataTransferJobResponseTypeDef = TypedDict(
    "CreateMetadataTransferJobResponseTypeDef",
    {
        "metadataTransferJobId": str,
        "arn": str,
        "creationDateTime": datetime,
        "status": MetadataTransferJobStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetadataTransferJobSummaryTypeDef = TypedDict(
    "MetadataTransferJobSummaryTypeDef",
    {
        "metadataTransferJobId": str,
        "arn": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "status": MetadataTransferJobStatusTypeDef,
        "progress": NotRequired[MetadataTransferJobProgressTypeDef],
    },
)
ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "componentName": str,
        "componentTypeId": str,
        "status": StatusTypeDef,
        "definedIn": NotRequired[str],
        "description": NotRequired[str],
        "propertyGroups": NotRequired[Dict[str, ComponentPropertyGroupResponseTypeDef]],
        "syncSource": NotRequired[str],
        "componentPath": NotRequired[str],
    },
)
ComponentTypeSummaryTypeDef = TypedDict(
    "ComponentTypeSummaryTypeDef",
    {
        "arn": str,
        "componentTypeId": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "description": NotRequired[str],
        "status": NotRequired[StatusTypeDef],
        "componentTypeName": NotRequired[str],
    },
)
EntitySummaryTypeDef = TypedDict(
    "EntitySummaryTypeDef",
    {
        "entityId": str,
        "entityName": str,
        "arn": str,
        "status": StatusTypeDef,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "parentEntityId": NotRequired[str],
        "description": NotRequired[str],
        "hasChildEntities": NotRequired[bool],
    },
)
GetSyncJobResponseTypeDef = TypedDict(
    "GetSyncJobResponseTypeDef",
    {
        "arn": str,
        "workspaceId": str,
        "syncSource": str,
        "syncRole": str,
        "status": SyncJobStatusTypeDef,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SyncJobSummaryTypeDef = TypedDict(
    "SyncJobSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "workspaceId": NotRequired[str],
        "syncSource": NotRequired[str],
        "status": NotRequired[SyncJobStatusTypeDef],
        "creationDateTime": NotRequired[datetime],
        "updateDateTime": NotRequired[datetime],
    },
)
SyncResourceSummaryTypeDef = TypedDict(
    "SyncResourceSummaryTypeDef",
    {
        "resourceType": NotRequired[SyncResourceTypeType],
        "externalId": NotRequired[str],
        "resourceId": NotRequired[str],
        "status": NotRequired[SyncResourceStatusTypeDef],
        "updateDateTime": NotRequired[datetime],
    },
)
IotSiteWiseSourceConfigurationOutputTypeDef = TypedDict(
    "IotSiteWiseSourceConfigurationOutputTypeDef",
    {
        "filters": NotRequired[List[IotSiteWiseSourceConfigurationFilterTypeDef]],
    },
)
IotSiteWiseSourceConfigurationTypeDef = TypedDict(
    "IotSiteWiseSourceConfigurationTypeDef",
    {
        "filters": NotRequired[Sequence[IotSiteWiseSourceConfigurationFilterTypeDef]],
    },
)
IotTwinMakerSourceConfigurationOutputTypeDef = TypedDict(
    "IotTwinMakerSourceConfigurationOutputTypeDef",
    {
        "workspace": str,
        "filters": NotRequired[List[IotTwinMakerSourceConfigurationFilterTypeDef]],
    },
)
IotTwinMakerSourceConfigurationTypeDef = TypedDict(
    "IotTwinMakerSourceConfigurationTypeDef",
    {
        "workspace": str,
        "filters": NotRequired[Sequence[IotTwinMakerSourceConfigurationFilterTypeDef]],
    },
)
PropertyDefinitionResponseTypeDef = TypedDict(
    "PropertyDefinitionResponseTypeDef",
    {
        "dataType": DataTypeOutputTypeDef,
        "isTimeSeries": bool,
        "isRequiredInEntity": bool,
        "isExternalId": bool,
        "isStoredExternally": bool,
        "isImported": bool,
        "isFinal": bool,
        "isInherited": bool,
        "defaultValue": NotRequired[DataValueOutputTypeDef],
        "configuration": NotRequired[Dict[str, str]],
        "displayName": NotRequired[str],
    },
)
GetPropertyValueResponseTypeDef = TypedDict(
    "GetPropertyValueResponseTypeDef",
    {
        "propertyValues": Dict[str, PropertyLatestValueTypeDef],
        "nextToken": str,
        "tabularPropertyValues": List[List[Dict[str, DataValueOutputTypeDef]]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PropertyValueEntryOutputTypeDef = TypedDict(
    "PropertyValueEntryOutputTypeDef",
    {
        "entityPropertyReference": EntityPropertyReferenceOutputTypeDef,
        "propertyValues": NotRequired[List[PropertyValueOutputTypeDef]],
    },
)
PropertyValueHistoryTypeDef = TypedDict(
    "PropertyValueHistoryTypeDef",
    {
        "entityPropertyReference": EntityPropertyReferenceOutputTypeDef,
        "values": NotRequired[List[PropertyValueOutputTypeDef]],
    },
)
DataTypeTypeDef = TypedDict(
    "DataTypeTypeDef",
    {
        "type": TypeType,
        "nestedType": NotRequired[Mapping[str, Any]],
        "allowedValues": NotRequired[Sequence[DataValueUnionTypeDef]],
        "unitOfMeasure": NotRequired[str],
        "relationship": NotRequired[RelationshipTypeDef],
    },
)
PropertyFilterTypeDef = TypedDict(
    "PropertyFilterTypeDef",
    {
        "propertyName": NotRequired[str],
        "operator": NotRequired[str],
        "value": NotRequired[DataValueUnionTypeDef],
    },
)
PropertyValueTypeDef = TypedDict(
    "PropertyValueTypeDef",
    {
        "value": DataValueUnionTypeDef,
        "timestamp": NotRequired[TimestampTypeDef],
        "time": NotRequired[str],
    },
)
ListMetadataTransferJobsResponseTypeDef = TypedDict(
    "ListMetadataTransferJobsResponseTypeDef",
    {
        "metadataTransferJobSummaries": List[MetadataTransferJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "componentSummaries": List[ComponentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComponentTypesResponseTypeDef = TypedDict(
    "ListComponentTypesResponseTypeDef",
    {
        "workspaceId": str,
        "componentTypeSummaries": List[ComponentTypeSummaryTypeDef],
        "nextToken": str,
        "maxResults": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "entitySummaries": List[EntitySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSyncJobsResponseTypeDef = TypedDict(
    "ListSyncJobsResponseTypeDef",
    {
        "syncJobSummaries": List[SyncJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSyncResourcesResponseTypeDef = TypedDict(
    "ListSyncResourcesResponseTypeDef",
    {
        "syncResources": List[SyncResourceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IotSiteWiseSourceConfigurationUnionTypeDef = Union[
    IotSiteWiseSourceConfigurationTypeDef, IotSiteWiseSourceConfigurationOutputTypeDef
]
SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "type": SourceTypeType,
        "s3Configuration": NotRequired[S3SourceConfigurationTypeDef],
        "iotSiteWiseConfiguration": NotRequired[IotSiteWiseSourceConfigurationOutputTypeDef],
        "iotTwinMakerConfiguration": NotRequired[IotTwinMakerSourceConfigurationOutputTypeDef],
    },
)
IotTwinMakerSourceConfigurationUnionTypeDef = Union[
    IotTwinMakerSourceConfigurationTypeDef, IotTwinMakerSourceConfigurationOutputTypeDef
]
GetComponentTypeResponseTypeDef = TypedDict(
    "GetComponentTypeResponseTypeDef",
    {
        "workspaceId": str,
        "isSingleton": bool,
        "componentTypeId": str,
        "description": str,
        "propertyDefinitions": Dict[str, PropertyDefinitionResponseTypeDef],
        "extendsFrom": List[str],
        "functions": Dict[str, FunctionResponseTypeDef],
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "arn": str,
        "isAbstract": bool,
        "isSchemaInitialized": bool,
        "status": StatusTypeDef,
        "propertyGroups": Dict[str, PropertyGroupResponseTypeDef],
        "syncSource": str,
        "componentTypeName": str,
        "compositeComponentTypes": Dict[str, CompositeComponentTypeResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PropertyResponseTypeDef = TypedDict(
    "PropertyResponseTypeDef",
    {
        "definition": NotRequired[PropertyDefinitionResponseTypeDef],
        "value": NotRequired[DataValueOutputTypeDef],
        "areAllPropertyValuesReturned": NotRequired[bool],
    },
)
PropertySummaryTypeDef = TypedDict(
    "PropertySummaryTypeDef",
    {
        "propertyName": str,
        "definition": NotRequired[PropertyDefinitionResponseTypeDef],
        "value": NotRequired[DataValueOutputTypeDef],
        "areAllPropertyValuesReturned": NotRequired[bool],
    },
)
BatchPutPropertyErrorTypeDef = TypedDict(
    "BatchPutPropertyErrorTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "entry": PropertyValueEntryOutputTypeDef,
    },
)
GetPropertyValueHistoryResponseTypeDef = TypedDict(
    "GetPropertyValueHistoryResponseTypeDef",
    {
        "propertyValues": List[PropertyValueHistoryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataTypeUnionTypeDef = Union[DataTypeTypeDef, DataTypeOutputTypeDef]
GetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "GetPropertyValueHistoryRequestRequestTypeDef",
    {
        "workspaceId": str,
        "selectedProperties": Sequence[str],
        "entityId": NotRequired[str],
        "componentName": NotRequired[str],
        "componentPath": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "propertyFilters": NotRequired[Sequence[PropertyFilterTypeDef]],
        "startDateTime": NotRequired[TimestampTypeDef],
        "endDateTime": NotRequired[TimestampTypeDef],
        "interpolation": NotRequired[InterpolationParametersTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "orderByTime": NotRequired[OrderByTimeType],
        "startTime": NotRequired[str],
        "endTime": NotRequired[str],
    },
)
TabularConditionsTypeDef = TypedDict(
    "TabularConditionsTypeDef",
    {
        "orderBy": NotRequired[Sequence[OrderByTypeDef]],
        "propertyFilters": NotRequired[Sequence[PropertyFilterTypeDef]],
    },
)
PropertyValueUnionTypeDef = Union[PropertyValueTypeDef, PropertyValueOutputTypeDef]
GetMetadataTransferJobResponseTypeDef = TypedDict(
    "GetMetadataTransferJobResponseTypeDef",
    {
        "metadataTransferJobId": str,
        "arn": str,
        "description": str,
        "sources": List[SourceConfigurationOutputTypeDef],
        "destination": DestinationConfigurationTypeDef,
        "metadataTransferJobRole": str,
        "reportUrl": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "status": MetadataTransferJobStatusTypeDef,
        "progress": MetadataTransferJobProgressTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "type": SourceTypeType,
        "s3Configuration": NotRequired[S3SourceConfigurationTypeDef],
        "iotSiteWiseConfiguration": NotRequired[IotSiteWiseSourceConfigurationUnionTypeDef],
        "iotTwinMakerConfiguration": NotRequired[IotTwinMakerSourceConfigurationUnionTypeDef],
    },
)
ComponentResponseTypeDef = TypedDict(
    "ComponentResponseTypeDef",
    {
        "componentName": NotRequired[str],
        "description": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "status": NotRequired[StatusTypeDef],
        "definedIn": NotRequired[str],
        "properties": NotRequired[Dict[str, PropertyResponseTypeDef]],
        "propertyGroups": NotRequired[Dict[str, ComponentPropertyGroupResponseTypeDef]],
        "syncSource": NotRequired[str],
        "areAllPropertiesReturned": NotRequired[bool],
        "compositeComponents": NotRequired[Dict[str, ComponentSummaryTypeDef]],
        "areAllCompositeComponentsReturned": NotRequired[bool],
    },
)
ListPropertiesResponseTypeDef = TypedDict(
    "ListPropertiesResponseTypeDef",
    {
        "propertySummaries": List[PropertySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutPropertyErrorEntryTypeDef = TypedDict(
    "BatchPutPropertyErrorEntryTypeDef",
    {
        "errors": List[BatchPutPropertyErrorTypeDef],
    },
)
PropertyDefinitionRequestTypeDef = TypedDict(
    "PropertyDefinitionRequestTypeDef",
    {
        "dataType": NotRequired[DataTypeUnionTypeDef],
        "isRequiredInEntity": NotRequired[bool],
        "isExternalId": NotRequired[bool],
        "isStoredExternally": NotRequired[bool],
        "isTimeSeries": NotRequired[bool],
        "defaultValue": NotRequired[DataValueUnionTypeDef],
        "configuration": NotRequired[Mapping[str, str]],
        "displayName": NotRequired[str],
    },
)
GetPropertyValueRequestRequestTypeDef = TypedDict(
    "GetPropertyValueRequestRequestTypeDef",
    {
        "selectedProperties": Sequence[str],
        "workspaceId": str,
        "componentName": NotRequired[str],
        "componentPath": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "entityId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "propertyGroupName": NotRequired[str],
        "tabularConditions": NotRequired[TabularConditionsTypeDef],
    },
)
PropertyValueEntryTypeDef = TypedDict(
    "PropertyValueEntryTypeDef",
    {
        "entityPropertyReference": EntityPropertyReferenceUnionTypeDef,
        "propertyValues": NotRequired[Sequence[PropertyValueUnionTypeDef]],
    },
)
SourceConfigurationUnionTypeDef = Union[
    SourceConfigurationTypeDef, SourceConfigurationOutputTypeDef
]
GetEntityResponseTypeDef = TypedDict(
    "GetEntityResponseTypeDef",
    {
        "entityId": str,
        "entityName": str,
        "arn": str,
        "status": StatusTypeDef,
        "workspaceId": str,
        "description": str,
        "components": Dict[str, ComponentResponseTypeDef],
        "parentEntityId": str,
        "hasChildEntities": bool,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "syncSource": str,
        "areAllComponentsReturned": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutPropertyValuesResponseTypeDef = TypedDict(
    "BatchPutPropertyValuesResponseTypeDef",
    {
        "errorEntries": List[BatchPutPropertyErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateComponentTypeRequestRequestTypeDef = TypedDict(
    "CreateComponentTypeRequestRequestTypeDef",
    {
        "workspaceId": str,
        "componentTypeId": str,
        "isSingleton": NotRequired[bool],
        "description": NotRequired[str],
        "propertyDefinitions": NotRequired[Mapping[str, PropertyDefinitionRequestTypeDef]],
        "extendsFrom": NotRequired[Sequence[str]],
        "functions": NotRequired[Mapping[str, FunctionRequestTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "propertyGroups": NotRequired[Mapping[str, PropertyGroupRequestTypeDef]],
        "componentTypeName": NotRequired[str],
        "compositeComponentTypes": NotRequired[Mapping[str, CompositeComponentTypeRequestTypeDef]],
    },
)
PropertyRequestTypeDef = TypedDict(
    "PropertyRequestTypeDef",
    {
        "definition": NotRequired[PropertyDefinitionRequestTypeDef],
        "value": NotRequired[DataValueUnionTypeDef],
        "updateType": NotRequired[PropertyUpdateTypeType],
    },
)
UpdateComponentTypeRequestRequestTypeDef = TypedDict(
    "UpdateComponentTypeRequestRequestTypeDef",
    {
        "workspaceId": str,
        "componentTypeId": str,
        "isSingleton": NotRequired[bool],
        "description": NotRequired[str],
        "propertyDefinitions": NotRequired[Mapping[str, PropertyDefinitionRequestTypeDef]],
        "extendsFrom": NotRequired[Sequence[str]],
        "functions": NotRequired[Mapping[str, FunctionRequestTypeDef]],
        "propertyGroups": NotRequired[Mapping[str, PropertyGroupRequestTypeDef]],
        "componentTypeName": NotRequired[str],
        "compositeComponentTypes": NotRequired[Mapping[str, CompositeComponentTypeRequestTypeDef]],
    },
)
PropertyValueEntryUnionTypeDef = Union[PropertyValueEntryTypeDef, PropertyValueEntryOutputTypeDef]
CreateMetadataTransferJobRequestRequestTypeDef = TypedDict(
    "CreateMetadataTransferJobRequestRequestTypeDef",
    {
        "sources": Sequence[SourceConfigurationUnionTypeDef],
        "destination": DestinationConfigurationTypeDef,
        "metadataTransferJobId": NotRequired[str],
        "description": NotRequired[str],
    },
)
ComponentRequestTypeDef = TypedDict(
    "ComponentRequestTypeDef",
    {
        "description": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "properties": NotRequired[Mapping[str, PropertyRequestTypeDef]],
        "propertyGroups": NotRequired[Mapping[str, ComponentPropertyGroupRequestTypeDef]],
    },
)
ComponentUpdateRequestTypeDef = TypedDict(
    "ComponentUpdateRequestTypeDef",
    {
        "updateType": NotRequired[ComponentUpdateTypeType],
        "description": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "propertyUpdates": NotRequired[Mapping[str, PropertyRequestTypeDef]],
        "propertyGroupUpdates": NotRequired[Mapping[str, ComponentPropertyGroupRequestTypeDef]],
    },
)
CompositeComponentRequestTypeDef = TypedDict(
    "CompositeComponentRequestTypeDef",
    {
        "description": NotRequired[str],
        "properties": NotRequired[Mapping[str, PropertyRequestTypeDef]],
        "propertyGroups": NotRequired[Mapping[str, ComponentPropertyGroupRequestTypeDef]],
    },
)
CompositeComponentUpdateRequestTypeDef = TypedDict(
    "CompositeComponentUpdateRequestTypeDef",
    {
        "updateType": NotRequired[ComponentUpdateTypeType],
        "description": NotRequired[str],
        "propertyUpdates": NotRequired[Mapping[str, PropertyRequestTypeDef]],
        "propertyGroupUpdates": NotRequired[Mapping[str, ComponentPropertyGroupRequestTypeDef]],
    },
)
BatchPutPropertyValuesRequestRequestTypeDef = TypedDict(
    "BatchPutPropertyValuesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entries": Sequence[PropertyValueEntryUnionTypeDef],
    },
)
CreateEntityRequestRequestTypeDef = TypedDict(
    "CreateEntityRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityName": str,
        "entityId": NotRequired[str],
        "description": NotRequired[str],
        "components": NotRequired[Mapping[str, ComponentRequestTypeDef]],
        "compositeComponents": NotRequired[Mapping[str, CompositeComponentRequestTypeDef]],
        "parentEntityId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateEntityRequestRequestTypeDef = TypedDict(
    "UpdateEntityRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityId": str,
        "entityName": NotRequired[str],
        "description": NotRequired[str],
        "componentUpdates": NotRequired[Mapping[str, ComponentUpdateRequestTypeDef]],
        "compositeComponentUpdates": NotRequired[
            Mapping[str, CompositeComponentUpdateRequestTypeDef]
        ],
        "parentEntityUpdate": NotRequired[ParentEntityUpdateRequestTypeDef],
    },
)
