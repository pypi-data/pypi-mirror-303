"""
Type annotations for connectcases service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/type_defs/)

Usage::

    ```python
    from mypy_boto3_connectcases.type_defs import AuditEventFieldValueUnionTypeDef

    data: AuditEventFieldValueUnionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AuditEventTypeType,
    DomainStatusType,
    FieldNamespaceType,
    FieldTypeType,
    OrderType,
    RelatedItemTypeType,
    TemplateStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AuditEventFieldValueUnionTypeDef",
    "UserUnionTypeDef",
    "FieldIdentifierTypeDef",
    "FieldErrorTypeDef",
    "GetFieldResponseTypeDef",
    "ResponseMetadataTypeDef",
    "FieldOptionTypeDef",
    "FieldOptionErrorTypeDef",
    "CaseSummaryTypeDef",
    "CommentContentTypeDef",
    "ContactContentTypeDef",
    "ContactFilterTypeDef",
    "ContactTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateFieldRequestRequestTypeDef",
    "LayoutConfigurationTypeDef",
    "RequiredFieldTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteFieldRequestRequestTypeDef",
    "DeleteLayoutRequestRequestTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DomainSummaryTypeDef",
    "RelatedItemEventIncludedDataTypeDef",
    "FieldItemTypeDef",
    "FieldSummaryTypeDef",
    "FieldValueUnionOutputTypeDef",
    "FieldValueUnionTypeDef",
    "FileContentTypeDef",
    "FileFilterTypeDef",
    "GetCaseAuditEventsRequestRequestTypeDef",
    "GetCaseEventConfigurationRequestRequestTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetLayoutRequestRequestTypeDef",
    "GetTemplateRequestRequestTypeDef",
    "LayoutSummaryTypeDef",
    "ListCasesForContactRequestRequestTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListFieldOptionsRequestRequestTypeDef",
    "ListFieldsRequestRequestTypeDef",
    "ListLayoutsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "TemplateSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "SortTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFieldRequestRequestTypeDef",
    "AuditEventFieldTypeDef",
    "AuditEventPerformedByTypeDef",
    "BatchGetFieldRequestRequestTypeDef",
    "CaseEventIncludedDataOutputTypeDef",
    "CaseEventIncludedDataTypeDef",
    "GetCaseRequestRequestTypeDef",
    "BatchGetFieldResponseTypeDef",
    "CreateCaseResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateFieldResponseTypeDef",
    "CreateLayoutResponseTypeDef",
    "CreateRelatedItemResponseTypeDef",
    "CreateTemplateResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDomainResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "BatchPutFieldOptionsRequestRequestTypeDef",
    "ListFieldOptionsResponseTypeDef",
    "BatchPutFieldOptionsResponseTypeDef",
    "ListCasesForContactResponseTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "GetTemplateResponseTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "FieldGroupOutputTypeDef",
    "FieldGroupTypeDef",
    "ListFieldsResponseTypeDef",
    "FieldValueOutputTypeDef",
    "FieldValueUnionUnionTypeDef",
    "RelatedItemContentTypeDef",
    "RelatedItemInputContentTypeDef",
    "RelatedItemTypeFilterTypeDef",
    "ListLayoutsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "AuditEventTypeDef",
    "EventIncludedDataOutputTypeDef",
    "CaseEventIncludedDataUnionTypeDef",
    "SectionOutputTypeDef",
    "FieldGroupUnionTypeDef",
    "GetCaseResponseTypeDef",
    "SearchCasesResponseItemTypeDef",
    "FieldValueTypeDef",
    "SearchRelatedItemsResponseItemTypeDef",
    "CreateRelatedItemRequestRequestTypeDef",
    "SearchRelatedItemsRequestRequestTypeDef",
    "SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef",
    "GetCaseAuditEventsResponseTypeDef",
    "EventBridgeConfigurationOutputTypeDef",
    "EventIncludedDataTypeDef",
    "LayoutSectionsOutputTypeDef",
    "SectionTypeDef",
    "SearchCasesResponseTypeDef",
    "FieldValueExtraUnionTypeDef",
    "UpdateCaseRequestRequestTypeDef",
    "SearchRelatedItemsResponseTypeDef",
    "GetCaseEventConfigurationResponseTypeDef",
    "EventIncludedDataUnionTypeDef",
    "BasicLayoutOutputTypeDef",
    "SectionUnionTypeDef",
    "CreateCaseRequestRequestTypeDef",
    "FieldFilterTypeDef",
    "EventBridgeConfigurationTypeDef",
    "LayoutContentOutputTypeDef",
    "LayoutSectionsTypeDef",
    "CaseFilterPaginatorTypeDef",
    "CaseFilterTypeDef",
    "PutCaseEventConfigurationRequestRequestTypeDef",
    "GetLayoutResponseTypeDef",
    "LayoutSectionsUnionTypeDef",
    "SearchCasesRequestSearchCasesPaginateTypeDef",
    "SearchCasesRequestRequestTypeDef",
    "BasicLayoutTypeDef",
    "BasicLayoutUnionTypeDef",
    "LayoutContentTypeDef",
    "CreateLayoutRequestRequestTypeDef",
    "UpdateLayoutRequestRequestTypeDef",
)

AuditEventFieldValueUnionTypeDef = TypedDict(
    "AuditEventFieldValueUnionTypeDef",
    {
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "emptyValue": NotRequired[Dict[str, Any]],
        "stringValue": NotRequired[str],
        "userArnValue": NotRequired[str],
    },
)
UserUnionTypeDef = TypedDict(
    "UserUnionTypeDef",
    {
        "userArn": NotRequired[str],
    },
)
FieldIdentifierTypeDef = TypedDict(
    "FieldIdentifierTypeDef",
    {
        "id": str,
    },
)
FieldErrorTypeDef = TypedDict(
    "FieldErrorTypeDef",
    {
        "errorCode": str,
        "id": str,
        "message": NotRequired[str],
    },
)
GetFieldResponseTypeDef = TypedDict(
    "GetFieldResponseTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "name": str,
        "namespace": FieldNamespaceType,
        "type": FieldTypeType,
        "createdTime": NotRequired[datetime],
        "deleted": NotRequired[bool],
        "description": NotRequired[str],
        "lastModifiedTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
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
FieldOptionTypeDef = TypedDict(
    "FieldOptionTypeDef",
    {
        "active": bool,
        "name": str,
        "value": str,
    },
)
FieldOptionErrorTypeDef = TypedDict(
    "FieldOptionErrorTypeDef",
    {
        "errorCode": str,
        "message": str,
        "value": str,
    },
)
CaseSummaryTypeDef = TypedDict(
    "CaseSummaryTypeDef",
    {
        "caseId": str,
        "templateId": str,
    },
)
CommentContentTypeDef = TypedDict(
    "CommentContentTypeDef",
    {
        "body": str,
        "contentType": Literal["Text/Plain"],
    },
)
ContactContentTypeDef = TypedDict(
    "ContactContentTypeDef",
    {
        "channel": str,
        "connectedToSystemTime": datetime,
        "contactArn": str,
    },
)
ContactFilterTypeDef = TypedDict(
    "ContactFilterTypeDef",
    {
        "channel": NotRequired[Sequence[str]],
        "contactArn": NotRequired[str],
    },
)
ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "contactArn": str,
    },
)
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "name": str,
    },
)
CreateFieldRequestRequestTypeDef = TypedDict(
    "CreateFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "name": str,
        "type": FieldTypeType,
        "description": NotRequired[str],
    },
)
LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "defaultLayout": NotRequired[str],
    },
)
RequiredFieldTypeDef = TypedDict(
    "RequiredFieldTypeDef",
    {
        "fieldId": str,
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
DeleteFieldRequestRequestTypeDef = TypedDict(
    "DeleteFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
    },
)
DeleteLayoutRequestRequestTypeDef = TypedDict(
    "DeleteLayoutRequestRequestTypeDef",
    {
        "domainId": str,
        "layoutId": str,
    },
)
DeleteTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "templateId": str,
    },
)
DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "domainArn": str,
        "domainId": str,
        "name": str,
    },
)
RelatedItemEventIncludedDataTypeDef = TypedDict(
    "RelatedItemEventIncludedDataTypeDef",
    {
        "includeContent": bool,
    },
)
FieldItemTypeDef = TypedDict(
    "FieldItemTypeDef",
    {
        "id": str,
    },
)
FieldSummaryTypeDef = TypedDict(
    "FieldSummaryTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "name": str,
        "namespace": FieldNamespaceType,
        "type": FieldTypeType,
    },
)
FieldValueUnionOutputTypeDef = TypedDict(
    "FieldValueUnionOutputTypeDef",
    {
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "emptyValue": NotRequired[Dict[str, Any]],
        "stringValue": NotRequired[str],
        "userArnValue": NotRequired[str],
    },
)
FieldValueUnionTypeDef = TypedDict(
    "FieldValueUnionTypeDef",
    {
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "emptyValue": NotRequired[Mapping[str, Any]],
        "stringValue": NotRequired[str],
        "userArnValue": NotRequired[str],
    },
)
FileContentTypeDef = TypedDict(
    "FileContentTypeDef",
    {
        "fileArn": str,
    },
)
FileFilterTypeDef = TypedDict(
    "FileFilterTypeDef",
    {
        "fileArn": NotRequired[str],
    },
)
GetCaseAuditEventsRequestRequestTypeDef = TypedDict(
    "GetCaseAuditEventsRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetCaseEventConfigurationRequestRequestTypeDef = TypedDict(
    "GetCaseEventConfigurationRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
GetLayoutRequestRequestTypeDef = TypedDict(
    "GetLayoutRequestRequestTypeDef",
    {
        "domainId": str,
        "layoutId": str,
    },
)
GetTemplateRequestRequestTypeDef = TypedDict(
    "GetTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "templateId": str,
    },
)
LayoutSummaryTypeDef = TypedDict(
    "LayoutSummaryTypeDef",
    {
        "layoutArn": str,
        "layoutId": str,
        "name": str,
    },
)
ListCasesForContactRequestRequestTypeDef = TypedDict(
    "ListCasesForContactRequestRequestTypeDef",
    {
        "contactArn": str,
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListFieldOptionsRequestRequestTypeDef = TypedDict(
    "ListFieldOptionsRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
ListFieldsRequestRequestTypeDef = TypedDict(
    "ListFieldsRequestRequestTypeDef",
    {
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLayoutsRequestRequestTypeDef = TypedDict(
    "ListLayoutsRequestRequestTypeDef",
    {
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "arn": str,
    },
)
ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[Sequence[TemplateStatusType]],
    },
)
TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "name": str,
        "status": TemplateStatusType,
        "templateArn": str,
        "templateId": str,
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
SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "fieldId": str,
        "sortOrder": OrderType,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateFieldRequestRequestTypeDef = TypedDict(
    "UpdateFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
        "description": NotRequired[str],
        "name": NotRequired[str],
    },
)
AuditEventFieldTypeDef = TypedDict(
    "AuditEventFieldTypeDef",
    {
        "eventFieldId": str,
        "newValue": AuditEventFieldValueUnionTypeDef,
        "oldValue": NotRequired[AuditEventFieldValueUnionTypeDef],
    },
)
AuditEventPerformedByTypeDef = TypedDict(
    "AuditEventPerformedByTypeDef",
    {
        "iamPrincipalArn": str,
        "user": NotRequired[UserUnionTypeDef],
    },
)
BatchGetFieldRequestRequestTypeDef = TypedDict(
    "BatchGetFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "fields": Sequence[FieldIdentifierTypeDef],
    },
)
CaseEventIncludedDataOutputTypeDef = TypedDict(
    "CaseEventIncludedDataOutputTypeDef",
    {
        "fields": List[FieldIdentifierTypeDef],
    },
)
CaseEventIncludedDataTypeDef = TypedDict(
    "CaseEventIncludedDataTypeDef",
    {
        "fields": Sequence[FieldIdentifierTypeDef],
    },
)
GetCaseRequestRequestTypeDef = TypedDict(
    "GetCaseRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "fields": Sequence[FieldIdentifierTypeDef],
        "nextToken": NotRequired[str],
    },
)
BatchGetFieldResponseTypeDef = TypedDict(
    "BatchGetFieldResponseTypeDef",
    {
        "errors": List[FieldErrorTypeDef],
        "fields": List[GetFieldResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCaseResponseTypeDef = TypedDict(
    "CreateCaseResponseTypeDef",
    {
        "caseArn": str,
        "caseId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "domainArn": str,
        "domainId": str,
        "domainStatus": DomainStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFieldResponseTypeDef = TypedDict(
    "CreateFieldResponseTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLayoutResponseTypeDef = TypedDict(
    "CreateLayoutResponseTypeDef",
    {
        "layoutArn": str,
        "layoutId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRelatedItemResponseTypeDef = TypedDict(
    "CreateRelatedItemResponseTypeDef",
    {
        "relatedItemArn": str,
        "relatedItemId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainResponseTypeDef = TypedDict(
    "GetDomainResponseTypeDef",
    {
        "createdTime": datetime,
        "domainArn": str,
        "domainId": str,
        "domainStatus": DomainStatusType,
        "name": str,
        "tags": Dict[str, str],
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
BatchPutFieldOptionsRequestRequestTypeDef = TypedDict(
    "BatchPutFieldOptionsRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
        "options": Sequence[FieldOptionTypeDef],
    },
)
ListFieldOptionsResponseTypeDef = TypedDict(
    "ListFieldOptionsResponseTypeDef",
    {
        "nextToken": str,
        "options": List[FieldOptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutFieldOptionsResponseTypeDef = TypedDict(
    "BatchPutFieldOptionsResponseTypeDef",
    {
        "errors": List[FieldOptionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCasesForContactResponseTypeDef = TypedDict(
    "ListCasesForContactResponseTypeDef",
    {
        "cases": List[CaseSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTemplateRequestRequestTypeDef = TypedDict(
    "CreateTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "name": str,
        "description": NotRequired[str],
        "layoutConfiguration": NotRequired[LayoutConfigurationTypeDef],
        "requiredFields": NotRequired[Sequence[RequiredFieldTypeDef]],
        "status": NotRequired[TemplateStatusType],
    },
)
GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "createdTime": datetime,
        "deleted": bool,
        "description": str,
        "lastModifiedTime": datetime,
        "layoutConfiguration": LayoutConfigurationTypeDef,
        "name": str,
        "requiredFields": List[RequiredFieldTypeDef],
        "status": TemplateStatusType,
        "tags": Dict[str, str],
        "templateArn": str,
        "templateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTemplateRequestRequestTypeDef = TypedDict(
    "UpdateTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "templateId": str,
        "description": NotRequired[str],
        "layoutConfiguration": NotRequired[LayoutConfigurationTypeDef],
        "name": NotRequired[str],
        "requiredFields": NotRequired[Sequence[RequiredFieldTypeDef]],
        "status": NotRequired[TemplateStatusType],
    },
)
ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "domains": List[DomainSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FieldGroupOutputTypeDef = TypedDict(
    "FieldGroupOutputTypeDef",
    {
        "fields": List[FieldItemTypeDef],
        "name": NotRequired[str],
    },
)
FieldGroupTypeDef = TypedDict(
    "FieldGroupTypeDef",
    {
        "fields": Sequence[FieldItemTypeDef],
        "name": NotRequired[str],
    },
)
ListFieldsResponseTypeDef = TypedDict(
    "ListFieldsResponseTypeDef",
    {
        "fields": List[FieldSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FieldValueOutputTypeDef = TypedDict(
    "FieldValueOutputTypeDef",
    {
        "id": str,
        "value": FieldValueUnionOutputTypeDef,
    },
)
FieldValueUnionUnionTypeDef = Union[FieldValueUnionTypeDef, FieldValueUnionOutputTypeDef]
RelatedItemContentTypeDef = TypedDict(
    "RelatedItemContentTypeDef",
    {
        "comment": NotRequired[CommentContentTypeDef],
        "contact": NotRequired[ContactContentTypeDef],
        "file": NotRequired[FileContentTypeDef],
    },
)
RelatedItemInputContentTypeDef = TypedDict(
    "RelatedItemInputContentTypeDef",
    {
        "comment": NotRequired[CommentContentTypeDef],
        "contact": NotRequired[ContactTypeDef],
        "file": NotRequired[FileContentTypeDef],
    },
)
RelatedItemTypeFilterTypeDef = TypedDict(
    "RelatedItemTypeFilterTypeDef",
    {
        "comment": NotRequired[Mapping[str, Any]],
        "contact": NotRequired[ContactFilterTypeDef],
        "file": NotRequired[FileFilterTypeDef],
    },
)
ListLayoutsResponseTypeDef = TypedDict(
    "ListLayoutsResponseTypeDef",
    {
        "layouts": List[LayoutSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "templates": List[TemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuditEventTypeDef = TypedDict(
    "AuditEventTypeDef",
    {
        "eventId": str,
        "fields": List[AuditEventFieldTypeDef],
        "performedTime": datetime,
        "type": AuditEventTypeType,
        "performedBy": NotRequired[AuditEventPerformedByTypeDef],
        "relatedItemType": NotRequired[RelatedItemTypeType],
    },
)
EventIncludedDataOutputTypeDef = TypedDict(
    "EventIncludedDataOutputTypeDef",
    {
        "caseData": NotRequired[CaseEventIncludedDataOutputTypeDef],
        "relatedItemData": NotRequired[RelatedItemEventIncludedDataTypeDef],
    },
)
CaseEventIncludedDataUnionTypeDef = Union[
    CaseEventIncludedDataTypeDef, CaseEventIncludedDataOutputTypeDef
]
SectionOutputTypeDef = TypedDict(
    "SectionOutputTypeDef",
    {
        "fieldGroup": NotRequired[FieldGroupOutputTypeDef],
    },
)
FieldGroupUnionTypeDef = Union[FieldGroupTypeDef, FieldGroupOutputTypeDef]
GetCaseResponseTypeDef = TypedDict(
    "GetCaseResponseTypeDef",
    {
        "fields": List[FieldValueOutputTypeDef],
        "nextToken": str,
        "tags": Dict[str, str],
        "templateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchCasesResponseItemTypeDef = TypedDict(
    "SearchCasesResponseItemTypeDef",
    {
        "caseId": str,
        "fields": List[FieldValueOutputTypeDef],
        "templateId": str,
        "tags": NotRequired[Dict[str, str]],
    },
)
FieldValueTypeDef = TypedDict(
    "FieldValueTypeDef",
    {
        "id": str,
        "value": FieldValueUnionUnionTypeDef,
    },
)
SearchRelatedItemsResponseItemTypeDef = TypedDict(
    "SearchRelatedItemsResponseItemTypeDef",
    {
        "associationTime": datetime,
        "content": RelatedItemContentTypeDef,
        "relatedItemId": str,
        "type": RelatedItemTypeType,
        "performedBy": NotRequired[UserUnionTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateRelatedItemRequestRequestTypeDef = TypedDict(
    "CreateRelatedItemRequestRequestTypeDef",
    {
        "caseId": str,
        "content": RelatedItemInputContentTypeDef,
        "domainId": str,
        "type": RelatedItemTypeType,
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)
SearchRelatedItemsRequestRequestTypeDef = TypedDict(
    "SearchRelatedItemsRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "filters": NotRequired[Sequence[RelatedItemTypeFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef = TypedDict(
    "SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "filters": NotRequired[Sequence[RelatedItemTypeFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCaseAuditEventsResponseTypeDef = TypedDict(
    "GetCaseAuditEventsResponseTypeDef",
    {
        "auditEvents": List[AuditEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventBridgeConfigurationOutputTypeDef = TypedDict(
    "EventBridgeConfigurationOutputTypeDef",
    {
        "enabled": bool,
        "includedData": NotRequired[EventIncludedDataOutputTypeDef],
    },
)
EventIncludedDataTypeDef = TypedDict(
    "EventIncludedDataTypeDef",
    {
        "caseData": NotRequired[CaseEventIncludedDataUnionTypeDef],
        "relatedItemData": NotRequired[RelatedItemEventIncludedDataTypeDef],
    },
)
LayoutSectionsOutputTypeDef = TypedDict(
    "LayoutSectionsOutputTypeDef",
    {
        "sections": NotRequired[List[SectionOutputTypeDef]],
    },
)
SectionTypeDef = TypedDict(
    "SectionTypeDef",
    {
        "fieldGroup": NotRequired[FieldGroupUnionTypeDef],
    },
)
SearchCasesResponseTypeDef = TypedDict(
    "SearchCasesResponseTypeDef",
    {
        "cases": List[SearchCasesResponseItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FieldValueExtraUnionTypeDef = Union[FieldValueTypeDef, FieldValueOutputTypeDef]
UpdateCaseRequestRequestTypeDef = TypedDict(
    "UpdateCaseRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "fields": Sequence[FieldValueTypeDef],
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)
SearchRelatedItemsResponseTypeDef = TypedDict(
    "SearchRelatedItemsResponseTypeDef",
    {
        "nextToken": str,
        "relatedItems": List[SearchRelatedItemsResponseItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCaseEventConfigurationResponseTypeDef = TypedDict(
    "GetCaseEventConfigurationResponseTypeDef",
    {
        "eventBridge": EventBridgeConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventIncludedDataUnionTypeDef = Union[EventIncludedDataTypeDef, EventIncludedDataOutputTypeDef]
BasicLayoutOutputTypeDef = TypedDict(
    "BasicLayoutOutputTypeDef",
    {
        "moreInfo": NotRequired[LayoutSectionsOutputTypeDef],
        "topPanel": NotRequired[LayoutSectionsOutputTypeDef],
    },
)
SectionUnionTypeDef = Union[SectionTypeDef, SectionOutputTypeDef]
CreateCaseRequestRequestTypeDef = TypedDict(
    "CreateCaseRequestRequestTypeDef",
    {
        "domainId": str,
        "fields": Sequence[FieldValueExtraUnionTypeDef],
        "templateId": str,
        "clientToken": NotRequired[str],
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)
FieldFilterTypeDef = TypedDict(
    "FieldFilterTypeDef",
    {
        "contains": NotRequired[FieldValueExtraUnionTypeDef],
        "equalTo": NotRequired[FieldValueExtraUnionTypeDef],
        "greaterThan": NotRequired[FieldValueExtraUnionTypeDef],
        "greaterThanOrEqualTo": NotRequired[FieldValueExtraUnionTypeDef],
        "lessThan": NotRequired[FieldValueExtraUnionTypeDef],
        "lessThanOrEqualTo": NotRequired[FieldValueExtraUnionTypeDef],
    },
)
EventBridgeConfigurationTypeDef = TypedDict(
    "EventBridgeConfigurationTypeDef",
    {
        "enabled": bool,
        "includedData": NotRequired[EventIncludedDataUnionTypeDef],
    },
)
LayoutContentOutputTypeDef = TypedDict(
    "LayoutContentOutputTypeDef",
    {
        "basic": NotRequired[BasicLayoutOutputTypeDef],
    },
)
LayoutSectionsTypeDef = TypedDict(
    "LayoutSectionsTypeDef",
    {
        "sections": NotRequired[Sequence[SectionUnionTypeDef]],
    },
)
CaseFilterPaginatorTypeDef = TypedDict(
    "CaseFilterPaginatorTypeDef",
    {
        "andAll": NotRequired[Sequence[Mapping[str, Any]]],
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Mapping[str, Any]],
        "orAll": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
CaseFilterTypeDef = TypedDict(
    "CaseFilterTypeDef",
    {
        "andAll": NotRequired[Sequence[Mapping[str, Any]]],
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Mapping[str, Any]],
        "orAll": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
PutCaseEventConfigurationRequestRequestTypeDef = TypedDict(
    "PutCaseEventConfigurationRequestRequestTypeDef",
    {
        "domainId": str,
        "eventBridge": EventBridgeConfigurationTypeDef,
    },
)
GetLayoutResponseTypeDef = TypedDict(
    "GetLayoutResponseTypeDef",
    {
        "content": LayoutContentOutputTypeDef,
        "createdTime": datetime,
        "deleted": bool,
        "lastModifiedTime": datetime,
        "layoutArn": str,
        "layoutId": str,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LayoutSectionsUnionTypeDef = Union[LayoutSectionsTypeDef, LayoutSectionsOutputTypeDef]
SearchCasesRequestSearchCasesPaginateTypeDef = TypedDict(
    "SearchCasesRequestSearchCasesPaginateTypeDef",
    {
        "domainId": str,
        "fields": NotRequired[Sequence[FieldIdentifierTypeDef]],
        "filter": NotRequired[CaseFilterPaginatorTypeDef],
        "searchTerm": NotRequired[str],
        "sorts": NotRequired[Sequence[SortTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchCasesRequestRequestTypeDef = TypedDict(
    "SearchCasesRequestRequestTypeDef",
    {
        "domainId": str,
        "fields": NotRequired[Sequence[FieldIdentifierTypeDef]],
        "filter": NotRequired[CaseFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchTerm": NotRequired[str],
        "sorts": NotRequired[Sequence[SortTypeDef]],
    },
)
BasicLayoutTypeDef = TypedDict(
    "BasicLayoutTypeDef",
    {
        "moreInfo": NotRequired[LayoutSectionsUnionTypeDef],
        "topPanel": NotRequired[LayoutSectionsUnionTypeDef],
    },
)
BasicLayoutUnionTypeDef = Union[BasicLayoutTypeDef, BasicLayoutOutputTypeDef]
LayoutContentTypeDef = TypedDict(
    "LayoutContentTypeDef",
    {
        "basic": NotRequired[BasicLayoutUnionTypeDef],
    },
)
CreateLayoutRequestRequestTypeDef = TypedDict(
    "CreateLayoutRequestRequestTypeDef",
    {
        "content": LayoutContentTypeDef,
        "domainId": str,
        "name": str,
    },
)
UpdateLayoutRequestRequestTypeDef = TypedDict(
    "UpdateLayoutRequestRequestTypeDef",
    {
        "domainId": str,
        "layoutId": str,
        "content": NotRequired[LayoutContentTypeDef],
        "name": NotRequired[str],
    },
)
