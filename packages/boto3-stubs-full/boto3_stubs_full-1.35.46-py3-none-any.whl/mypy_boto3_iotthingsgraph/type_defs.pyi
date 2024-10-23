"""
Type annotations for iotthingsgraph service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotthingsgraph.type_defs import AssociateEntityToThingRequestRequestTypeDef

    data: AssociateEntityToThingRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    DeploymentTargetType,
    EntityFilterNameType,
    EntityTypeType,
    FlowExecutionEventTypeType,
    FlowExecutionStatusType,
    NamespaceDeletionStatusType,
    SystemInstanceDeploymentStatusType,
    SystemInstanceFilterNameType,
    UploadStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssociateEntityToThingRequestRequestTypeDef",
    "DefinitionDocumentTypeDef",
    "FlowTemplateSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "MetricsConfigurationTypeDef",
    "TagTypeDef",
    "SystemInstanceSummaryTypeDef",
    "SystemTemplateSummaryTypeDef",
    "DeleteFlowTemplateRequestRequestTypeDef",
    "DeleteSystemInstanceRequestRequestTypeDef",
    "DeleteSystemTemplateRequestRequestTypeDef",
    "DependencyRevisionTypeDef",
    "DeploySystemInstanceRequestRequestTypeDef",
    "DeprecateFlowTemplateRequestRequestTypeDef",
    "DeprecateSystemTemplateRequestRequestTypeDef",
    "DescribeNamespaceRequestRequestTypeDef",
    "DissociateEntityFromThingRequestRequestTypeDef",
    "EntityFilterTypeDef",
    "FlowExecutionMessageTypeDef",
    "FlowExecutionSummaryTypeDef",
    "FlowTemplateFilterTypeDef",
    "GetEntitiesRequestRequestTypeDef",
    "GetFlowTemplateRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetFlowTemplateRevisionsRequestRequestTypeDef",
    "GetSystemInstanceRequestRequestTypeDef",
    "GetSystemTemplateRequestRequestTypeDef",
    "GetSystemTemplateRevisionsRequestRequestTypeDef",
    "GetUploadStatusRequestRequestTypeDef",
    "ListFlowExecutionMessagesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TimestampTypeDef",
    "SystemInstanceFilterTypeDef",
    "SystemTemplateFilterTypeDef",
    "SearchThingsRequestRequestTypeDef",
    "ThingTypeDef",
    "UndeploySystemInstanceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateFlowTemplateRequestRequestTypeDef",
    "CreateSystemTemplateRequestRequestTypeDef",
    "EntityDescriptionTypeDef",
    "UpdateFlowTemplateRequestRequestTypeDef",
    "UpdateSystemTemplateRequestRequestTypeDef",
    "UploadEntityDefinitionsRequestRequestTypeDef",
    "FlowTemplateDescriptionTypeDef",
    "CreateFlowTemplateResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "GetFlowTemplateRevisionsResponseTypeDef",
    "GetNamespaceDeletionStatusResponseTypeDef",
    "GetUploadStatusResponseTypeDef",
    "SearchFlowTemplatesResponseTypeDef",
    "UpdateFlowTemplateResponseTypeDef",
    "UploadEntityDefinitionsResponseTypeDef",
    "CreateSystemInstanceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateSystemInstanceResponseTypeDef",
    "DeploySystemInstanceResponseTypeDef",
    "SearchSystemInstancesResponseTypeDef",
    "UndeploySystemInstanceResponseTypeDef",
    "CreateSystemTemplateResponseTypeDef",
    "GetSystemTemplateRevisionsResponseTypeDef",
    "SearchSystemTemplatesResponseTypeDef",
    "SystemTemplateDescriptionTypeDef",
    "UpdateSystemTemplateResponseTypeDef",
    "SystemInstanceDescriptionTypeDef",
    "SearchEntitiesRequestRequestTypeDef",
    "ListFlowExecutionMessagesResponseTypeDef",
    "SearchFlowExecutionsResponseTypeDef",
    "SearchFlowTemplatesRequestRequestTypeDef",
    "GetFlowTemplateRevisionsRequestGetFlowTemplateRevisionsPaginateTypeDef",
    "GetSystemTemplateRevisionsRequestGetSystemTemplateRevisionsPaginateTypeDef",
    "ListFlowExecutionMessagesRequestListFlowExecutionMessagesPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "SearchEntitiesRequestSearchEntitiesPaginateTypeDef",
    "SearchFlowTemplatesRequestSearchFlowTemplatesPaginateTypeDef",
    "SearchThingsRequestSearchThingsPaginateTypeDef",
    "SearchFlowExecutionsRequestRequestTypeDef",
    "SearchFlowExecutionsRequestSearchFlowExecutionsPaginateTypeDef",
    "SearchSystemInstancesRequestRequestTypeDef",
    "SearchSystemInstancesRequestSearchSystemInstancesPaginateTypeDef",
    "SearchSystemTemplatesRequestRequestTypeDef",
    "SearchSystemTemplatesRequestSearchSystemTemplatesPaginateTypeDef",
    "SearchThingsResponseTypeDef",
    "GetEntitiesResponseTypeDef",
    "SearchEntitiesResponseTypeDef",
    "GetFlowTemplateResponseTypeDef",
    "GetSystemTemplateResponseTypeDef",
    "GetSystemInstanceResponseTypeDef",
)

AssociateEntityToThingRequestRequestTypeDef = TypedDict(
    "AssociateEntityToThingRequestRequestTypeDef",
    {
        "thingName": str,
        "entityId": str,
        "namespaceVersion": NotRequired[int],
    },
)
DefinitionDocumentTypeDef = TypedDict(
    "DefinitionDocumentTypeDef",
    {
        "language": Literal["GRAPHQL"],
        "text": str,
    },
)
FlowTemplateSummaryTypeDef = TypedDict(
    "FlowTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "revisionNumber": NotRequired[int],
        "createdAt": NotRequired[datetime],
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
MetricsConfigurationTypeDef = TypedDict(
    "MetricsConfigurationTypeDef",
    {
        "cloudMetricEnabled": NotRequired[bool],
        "metricRuleRoleArn": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
SystemInstanceSummaryTypeDef = TypedDict(
    "SystemInstanceSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[SystemInstanceDeploymentStatusType],
        "target": NotRequired[DeploymentTargetType],
        "greengrassGroupName": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "greengrassGroupId": NotRequired[str],
        "greengrassGroupVersionId": NotRequired[str],
    },
)
SystemTemplateSummaryTypeDef = TypedDict(
    "SystemTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "revisionNumber": NotRequired[int],
        "createdAt": NotRequired[datetime],
    },
)
DeleteFlowTemplateRequestRequestTypeDef = TypedDict(
    "DeleteFlowTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteSystemInstanceRequestRequestTypeDef = TypedDict(
    "DeleteSystemInstanceRequestRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)
DeleteSystemTemplateRequestRequestTypeDef = TypedDict(
    "DeleteSystemTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
DependencyRevisionTypeDef = TypedDict(
    "DependencyRevisionTypeDef",
    {
        "id": NotRequired[str],
        "revisionNumber": NotRequired[int],
    },
)
DeploySystemInstanceRequestRequestTypeDef = TypedDict(
    "DeploySystemInstanceRequestRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)
DeprecateFlowTemplateRequestRequestTypeDef = TypedDict(
    "DeprecateFlowTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeprecateSystemTemplateRequestRequestTypeDef = TypedDict(
    "DeprecateSystemTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
DescribeNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeNamespaceRequestRequestTypeDef",
    {
        "namespaceName": NotRequired[str],
    },
)
DissociateEntityFromThingRequestRequestTypeDef = TypedDict(
    "DissociateEntityFromThingRequestRequestTypeDef",
    {
        "thingName": str,
        "entityType": EntityTypeType,
    },
)
EntityFilterTypeDef = TypedDict(
    "EntityFilterTypeDef",
    {
        "name": NotRequired[EntityFilterNameType],
        "value": NotRequired[Sequence[str]],
    },
)
FlowExecutionMessageTypeDef = TypedDict(
    "FlowExecutionMessageTypeDef",
    {
        "messageId": NotRequired[str],
        "eventType": NotRequired[FlowExecutionEventTypeType],
        "timestamp": NotRequired[datetime],
        "payload": NotRequired[str],
    },
)
FlowExecutionSummaryTypeDef = TypedDict(
    "FlowExecutionSummaryTypeDef",
    {
        "flowExecutionId": NotRequired[str],
        "status": NotRequired[FlowExecutionStatusType],
        "systemInstanceId": NotRequired[str],
        "flowTemplateId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
FlowTemplateFilterTypeDef = TypedDict(
    "FlowTemplateFilterTypeDef",
    {
        "name": Literal["DEVICE_MODEL_ID"],
        "value": Sequence[str],
    },
)
GetEntitiesRequestRequestTypeDef = TypedDict(
    "GetEntitiesRequestRequestTypeDef",
    {
        "ids": Sequence[str],
        "namespaceVersion": NotRequired[int],
    },
)
GetFlowTemplateRequestRequestTypeDef = TypedDict(
    "GetFlowTemplateRequestRequestTypeDef",
    {
        "id": str,
        "revisionNumber": NotRequired[int],
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
GetFlowTemplateRevisionsRequestRequestTypeDef = TypedDict(
    "GetFlowTemplateRevisionsRequestRequestTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetSystemInstanceRequestRequestTypeDef = TypedDict(
    "GetSystemInstanceRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetSystemTemplateRequestRequestTypeDef = TypedDict(
    "GetSystemTemplateRequestRequestTypeDef",
    {
        "id": str,
        "revisionNumber": NotRequired[int],
    },
)
GetSystemTemplateRevisionsRequestRequestTypeDef = TypedDict(
    "GetSystemTemplateRevisionsRequestRequestTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetUploadStatusRequestRequestTypeDef = TypedDict(
    "GetUploadStatusRequestRequestTypeDef",
    {
        "uploadId": str,
    },
)
ListFlowExecutionMessagesRequestRequestTypeDef = TypedDict(
    "ListFlowExecutionMessagesRequestRequestTypeDef",
    {
        "flowExecutionId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
SystemInstanceFilterTypeDef = TypedDict(
    "SystemInstanceFilterTypeDef",
    {
        "name": NotRequired[SystemInstanceFilterNameType],
        "value": NotRequired[Sequence[str]],
    },
)
SystemTemplateFilterTypeDef = TypedDict(
    "SystemTemplateFilterTypeDef",
    {
        "name": Literal["FLOW_TEMPLATE_ID"],
        "value": Sequence[str],
    },
)
SearchThingsRequestRequestTypeDef = TypedDict(
    "SearchThingsRequestRequestTypeDef",
    {
        "entityId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "namespaceVersion": NotRequired[int],
    },
)
ThingTypeDef = TypedDict(
    "ThingTypeDef",
    {
        "thingArn": NotRequired[str],
        "thingName": NotRequired[str],
    },
)
UndeploySystemInstanceRequestRequestTypeDef = TypedDict(
    "UndeploySystemInstanceRequestRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
CreateFlowTemplateRequestRequestTypeDef = TypedDict(
    "CreateFlowTemplateRequestRequestTypeDef",
    {
        "definition": DefinitionDocumentTypeDef,
        "compatibleNamespaceVersion": NotRequired[int],
    },
)
CreateSystemTemplateRequestRequestTypeDef = TypedDict(
    "CreateSystemTemplateRequestRequestTypeDef",
    {
        "definition": DefinitionDocumentTypeDef,
        "compatibleNamespaceVersion": NotRequired[int],
    },
)
EntityDescriptionTypeDef = TypedDict(
    "EntityDescriptionTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "type": NotRequired[EntityTypeType],
        "createdAt": NotRequired[datetime],
        "definition": NotRequired[DefinitionDocumentTypeDef],
    },
)
UpdateFlowTemplateRequestRequestTypeDef = TypedDict(
    "UpdateFlowTemplateRequestRequestTypeDef",
    {
        "id": str,
        "definition": DefinitionDocumentTypeDef,
        "compatibleNamespaceVersion": NotRequired[int],
    },
)
UpdateSystemTemplateRequestRequestTypeDef = TypedDict(
    "UpdateSystemTemplateRequestRequestTypeDef",
    {
        "id": str,
        "definition": DefinitionDocumentTypeDef,
        "compatibleNamespaceVersion": NotRequired[int],
    },
)
UploadEntityDefinitionsRequestRequestTypeDef = TypedDict(
    "UploadEntityDefinitionsRequestRequestTypeDef",
    {
        "document": NotRequired[DefinitionDocumentTypeDef],
        "syncWithPublicNamespace": NotRequired[bool],
        "deprecateExistingEntities": NotRequired[bool],
    },
)
FlowTemplateDescriptionTypeDef = TypedDict(
    "FlowTemplateDescriptionTypeDef",
    {
        "summary": NotRequired[FlowTemplateSummaryTypeDef],
        "definition": NotRequired[DefinitionDocumentTypeDef],
        "validatedNamespaceVersion": NotRequired[int],
    },
)
CreateFlowTemplateResponseTypeDef = TypedDict(
    "CreateFlowTemplateResponseTypeDef",
    {
        "summary": FlowTemplateSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "trackingNamespaceName": str,
        "trackingNamespaceVersion": int,
        "namespaceVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFlowTemplateRevisionsResponseTypeDef = TypedDict(
    "GetFlowTemplateRevisionsResponseTypeDef",
    {
        "summaries": List[FlowTemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNamespaceDeletionStatusResponseTypeDef = TypedDict(
    "GetNamespaceDeletionStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "status": NamespaceDeletionStatusType,
        "errorCode": Literal["VALIDATION_FAILED"],
        "errorMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUploadStatusResponseTypeDef = TypedDict(
    "GetUploadStatusResponseTypeDef",
    {
        "uploadId": str,
        "uploadStatus": UploadStatusType,
        "namespaceArn": str,
        "namespaceName": str,
        "namespaceVersion": int,
        "failureReason": List[str],
        "createdDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchFlowTemplatesResponseTypeDef = TypedDict(
    "SearchFlowTemplatesResponseTypeDef",
    {
        "summaries": List[FlowTemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFlowTemplateResponseTypeDef = TypedDict(
    "UpdateFlowTemplateResponseTypeDef",
    {
        "summary": FlowTemplateSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadEntityDefinitionsResponseTypeDef = TypedDict(
    "UploadEntityDefinitionsResponseTypeDef",
    {
        "uploadId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSystemInstanceRequestRequestTypeDef = TypedDict(
    "CreateSystemInstanceRequestRequestTypeDef",
    {
        "definition": DefinitionDocumentTypeDef,
        "target": DeploymentTargetType,
        "tags": NotRequired[Sequence[TagTypeDef]],
        "greengrassGroupName": NotRequired[str],
        "s3BucketName": NotRequired[str],
        "metricsConfiguration": NotRequired[MetricsConfigurationTypeDef],
        "flowActionsRoleArn": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateSystemInstanceResponseTypeDef = TypedDict(
    "CreateSystemInstanceResponseTypeDef",
    {
        "summary": SystemInstanceSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploySystemInstanceResponseTypeDef = TypedDict(
    "DeploySystemInstanceResponseTypeDef",
    {
        "summary": SystemInstanceSummaryTypeDef,
        "greengrassDeploymentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchSystemInstancesResponseTypeDef = TypedDict(
    "SearchSystemInstancesResponseTypeDef",
    {
        "summaries": List[SystemInstanceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UndeploySystemInstanceResponseTypeDef = TypedDict(
    "UndeploySystemInstanceResponseTypeDef",
    {
        "summary": SystemInstanceSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSystemTemplateResponseTypeDef = TypedDict(
    "CreateSystemTemplateResponseTypeDef",
    {
        "summary": SystemTemplateSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSystemTemplateRevisionsResponseTypeDef = TypedDict(
    "GetSystemTemplateRevisionsResponseTypeDef",
    {
        "summaries": List[SystemTemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchSystemTemplatesResponseTypeDef = TypedDict(
    "SearchSystemTemplatesResponseTypeDef",
    {
        "summaries": List[SystemTemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SystemTemplateDescriptionTypeDef = TypedDict(
    "SystemTemplateDescriptionTypeDef",
    {
        "summary": NotRequired[SystemTemplateSummaryTypeDef],
        "definition": NotRequired[DefinitionDocumentTypeDef],
        "validatedNamespaceVersion": NotRequired[int],
    },
)
UpdateSystemTemplateResponseTypeDef = TypedDict(
    "UpdateSystemTemplateResponseTypeDef",
    {
        "summary": SystemTemplateSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SystemInstanceDescriptionTypeDef = TypedDict(
    "SystemInstanceDescriptionTypeDef",
    {
        "summary": NotRequired[SystemInstanceSummaryTypeDef],
        "definition": NotRequired[DefinitionDocumentTypeDef],
        "s3BucketName": NotRequired[str],
        "metricsConfiguration": NotRequired[MetricsConfigurationTypeDef],
        "validatedNamespaceVersion": NotRequired[int],
        "validatedDependencyRevisions": NotRequired[List[DependencyRevisionTypeDef]],
        "flowActionsRoleArn": NotRequired[str],
    },
)
SearchEntitiesRequestRequestTypeDef = TypedDict(
    "SearchEntitiesRequestRequestTypeDef",
    {
        "entityTypes": Sequence[EntityTypeType],
        "filters": NotRequired[Sequence[EntityFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "namespaceVersion": NotRequired[int],
    },
)
ListFlowExecutionMessagesResponseTypeDef = TypedDict(
    "ListFlowExecutionMessagesResponseTypeDef",
    {
        "messages": List[FlowExecutionMessageTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchFlowExecutionsResponseTypeDef = TypedDict(
    "SearchFlowExecutionsResponseTypeDef",
    {
        "summaries": List[FlowExecutionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchFlowTemplatesRequestRequestTypeDef = TypedDict(
    "SearchFlowTemplatesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[FlowTemplateFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetFlowTemplateRevisionsRequestGetFlowTemplateRevisionsPaginateTypeDef = TypedDict(
    "GetFlowTemplateRevisionsRequestGetFlowTemplateRevisionsPaginateTypeDef",
    {
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSystemTemplateRevisionsRequestGetSystemTemplateRevisionsPaginateTypeDef = TypedDict(
    "GetSystemTemplateRevisionsRequestGetSystemTemplateRevisionsPaginateTypeDef",
    {
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFlowExecutionMessagesRequestListFlowExecutionMessagesPaginateTypeDef = TypedDict(
    "ListFlowExecutionMessagesRequestListFlowExecutionMessagesPaginateTypeDef",
    {
        "flowExecutionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "resourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchEntitiesRequestSearchEntitiesPaginateTypeDef = TypedDict(
    "SearchEntitiesRequestSearchEntitiesPaginateTypeDef",
    {
        "entityTypes": Sequence[EntityTypeType],
        "filters": NotRequired[Sequence[EntityFilterTypeDef]],
        "namespaceVersion": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchFlowTemplatesRequestSearchFlowTemplatesPaginateTypeDef = TypedDict(
    "SearchFlowTemplatesRequestSearchFlowTemplatesPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[FlowTemplateFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchThingsRequestSearchThingsPaginateTypeDef = TypedDict(
    "SearchThingsRequestSearchThingsPaginateTypeDef",
    {
        "entityId": str,
        "namespaceVersion": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchFlowExecutionsRequestRequestTypeDef = TypedDict(
    "SearchFlowExecutionsRequestRequestTypeDef",
    {
        "systemInstanceId": str,
        "flowExecutionId": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SearchFlowExecutionsRequestSearchFlowExecutionsPaginateTypeDef = TypedDict(
    "SearchFlowExecutionsRequestSearchFlowExecutionsPaginateTypeDef",
    {
        "systemInstanceId": str,
        "flowExecutionId": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchSystemInstancesRequestRequestTypeDef = TypedDict(
    "SearchSystemInstancesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[SystemInstanceFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SearchSystemInstancesRequestSearchSystemInstancesPaginateTypeDef = TypedDict(
    "SearchSystemInstancesRequestSearchSystemInstancesPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[SystemInstanceFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchSystemTemplatesRequestRequestTypeDef = TypedDict(
    "SearchSystemTemplatesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[SystemTemplateFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SearchSystemTemplatesRequestSearchSystemTemplatesPaginateTypeDef = TypedDict(
    "SearchSystemTemplatesRequestSearchSystemTemplatesPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[SystemTemplateFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchThingsResponseTypeDef = TypedDict(
    "SearchThingsResponseTypeDef",
    {
        "things": List[ThingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEntitiesResponseTypeDef = TypedDict(
    "GetEntitiesResponseTypeDef",
    {
        "descriptions": List[EntityDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchEntitiesResponseTypeDef = TypedDict(
    "SearchEntitiesResponseTypeDef",
    {
        "descriptions": List[EntityDescriptionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFlowTemplateResponseTypeDef = TypedDict(
    "GetFlowTemplateResponseTypeDef",
    {
        "description": FlowTemplateDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSystemTemplateResponseTypeDef = TypedDict(
    "GetSystemTemplateResponseTypeDef",
    {
        "description": SystemTemplateDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSystemInstanceResponseTypeDef = TypedDict(
    "GetSystemInstanceResponseTypeDef",
    {
        "description": SystemInstanceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
