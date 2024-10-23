"""
Type annotations for qapps service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/type_defs/)

Usage::

    ```python
    from mypy_boto3_qapps.type_defs import AssociateLibraryItemReviewInputRequestTypeDef

    data: AssociateLibraryItemReviewInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AppRequiredCapabilityType,
    AppStatusType,
    CardOutputSourceType,
    CardTypeType,
    DocumentScopeType,
    ExecutionStatusType,
    LibraryItemStatusType,
    PluginTypeType,
    SenderType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AssociateLibraryItemReviewInputRequestTypeDef",
    "AssociateQAppWithUserInputRequestTypeDef",
    "FileUploadCardInputTypeDef",
    "QPluginCardInputTypeDef",
    "TextInputCardInputTypeDef",
    "CardStatusTypeDef",
    "FileUploadCardTypeDef",
    "QPluginCardTypeDef",
    "TextInputCardTypeDef",
    "CardValueTypeDef",
    "CategoryTypeDef",
    "ConversationMessageTypeDef",
    "CreateLibraryItemInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteLibraryItemInputRequestTypeDef",
    "DeleteQAppInputRequestTypeDef",
    "DisassociateLibraryItemReviewInputRequestTypeDef",
    "DisassociateQAppFromUserInputRequestTypeDef",
    "DocumentAttributeValueOutputTypeDef",
    "TimestampTypeDef",
    "GetLibraryItemInputRequestTypeDef",
    "GetQAppInputRequestTypeDef",
    "GetQAppSessionInputRequestTypeDef",
    "ImportDocumentInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListLibraryItemsInputRequestTypeDef",
    "ListQAppsInputRequestTypeDef",
    "UserAppItemTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StopQAppSessionInputRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLibraryItemInputRequestTypeDef",
    "UpdateLibraryItemMetadataInputRequestTypeDef",
    "StartQAppSessionInputRequestTypeDef",
    "UpdateQAppSessionInputRequestTypeDef",
    "LibraryItemMemberTypeDef",
    "PredictQAppInputOptionsTypeDef",
    "CreateLibraryItemOutputTypeDef",
    "CreateQAppOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetLibraryItemOutputTypeDef",
    "GetQAppSessionOutputTypeDef",
    "ImportDocumentOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartQAppSessionOutputTypeDef",
    "UpdateLibraryItemOutputTypeDef",
    "UpdateQAppOutputTypeDef",
    "UpdateQAppSessionOutputTypeDef",
    "DocumentAttributeOutputTypeDef",
    "DocumentAttributeValueTypeDef",
    "ListLibraryItemsInputListLibraryItemsPaginateTypeDef",
    "ListQAppsInputListQAppsPaginateTypeDef",
    "ListQAppsOutputTypeDef",
    "ListLibraryItemsOutputTypeDef",
    "PredictQAppInputRequestTypeDef",
    "AttributeFilterOutputTypeDef",
    "DocumentAttributeValueUnionTypeDef",
    "QQueryCardInputOutputTypeDef",
    "QQueryCardTypeDef",
    "DocumentAttributeTypeDef",
    "CardInputOutputTypeDef",
    "CardTypeDef",
    "DocumentAttributeUnionTypeDef",
    "AppDefinitionInputOutputTypeDef",
    "AppDefinitionTypeDef",
    "AttributeFilterTypeDef",
    "PredictAppDefinitionTypeDef",
    "GetQAppOutputTypeDef",
    "AttributeFilterUnionTypeDef",
    "PredictQAppOutputTypeDef",
    "QQueryCardInputTypeDef",
    "QQueryCardInputUnionTypeDef",
    "CardInputTypeDef",
    "CardInputUnionTypeDef",
    "AppDefinitionInputTypeDef",
    "CreateQAppInputRequestTypeDef",
    "UpdateQAppInputRequestTypeDef",
)

AssociateLibraryItemReviewInputRequestTypeDef = TypedDict(
    "AssociateLibraryItemReviewInputRequestTypeDef",
    {
        "instanceId": str,
        "libraryItemId": str,
    },
)
AssociateQAppWithUserInputRequestTypeDef = TypedDict(
    "AssociateQAppWithUserInputRequestTypeDef",
    {
        "instanceId": str,
        "appId": str,
    },
)
FileUploadCardInputTypeDef = TypedDict(
    "FileUploadCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "filename": NotRequired[str],
        "fileId": NotRequired[str],
        "allowOverride": NotRequired[bool],
    },
)
QPluginCardInputTypeDef = TypedDict(
    "QPluginCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "prompt": str,
        "pluginId": str,
    },
)
TextInputCardInputTypeDef = TypedDict(
    "TextInputCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
    },
)
CardStatusTypeDef = TypedDict(
    "CardStatusTypeDef",
    {
        "currentState": ExecutionStatusType,
        "currentValue": str,
    },
)
FileUploadCardTypeDef = TypedDict(
    "FileUploadCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "filename": NotRequired[str],
        "fileId": NotRequired[str],
        "allowOverride": NotRequired[bool],
    },
)
QPluginCardTypeDef = TypedDict(
    "QPluginCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "prompt": str,
        "pluginType": PluginTypeType,
        "pluginId": str,
    },
)
TextInputCardTypeDef = TypedDict(
    "TextInputCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
    },
)
CardValueTypeDef = TypedDict(
    "CardValueTypeDef",
    {
        "cardId": str,
        "value": str,
    },
)
CategoryTypeDef = TypedDict(
    "CategoryTypeDef",
    {
        "id": str,
        "title": str,
    },
)
ConversationMessageTypeDef = TypedDict(
    "ConversationMessageTypeDef",
    {
        "body": str,
        "type": SenderType,
    },
)
CreateLibraryItemInputRequestTypeDef = TypedDict(
    "CreateLibraryItemInputRequestTypeDef",
    {
        "instanceId": str,
        "appId": str,
        "appVersion": int,
        "categories": Sequence[str],
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
DeleteLibraryItemInputRequestTypeDef = TypedDict(
    "DeleteLibraryItemInputRequestTypeDef",
    {
        "instanceId": str,
        "libraryItemId": str,
    },
)
DeleteQAppInputRequestTypeDef = TypedDict(
    "DeleteQAppInputRequestTypeDef",
    {
        "instanceId": str,
        "appId": str,
    },
)
DisassociateLibraryItemReviewInputRequestTypeDef = TypedDict(
    "DisassociateLibraryItemReviewInputRequestTypeDef",
    {
        "instanceId": str,
        "libraryItemId": str,
    },
)
DisassociateQAppFromUserInputRequestTypeDef = TypedDict(
    "DisassociateQAppFromUserInputRequestTypeDef",
    {
        "instanceId": str,
        "appId": str,
    },
)
DocumentAttributeValueOutputTypeDef = TypedDict(
    "DocumentAttributeValueOutputTypeDef",
    {
        "stringValue": NotRequired[str],
        "stringListValue": NotRequired[List[str]],
        "longValue": NotRequired[int],
        "dateValue": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]
GetLibraryItemInputRequestTypeDef = TypedDict(
    "GetLibraryItemInputRequestTypeDef",
    {
        "instanceId": str,
        "libraryItemId": str,
        "appId": NotRequired[str],
    },
)
GetQAppInputRequestTypeDef = TypedDict(
    "GetQAppInputRequestTypeDef",
    {
        "instanceId": str,
        "appId": str,
    },
)
GetQAppSessionInputRequestTypeDef = TypedDict(
    "GetQAppSessionInputRequestTypeDef",
    {
        "instanceId": str,
        "sessionId": str,
    },
)
ImportDocumentInputRequestTypeDef = TypedDict(
    "ImportDocumentInputRequestTypeDef",
    {
        "instanceId": str,
        "cardId": str,
        "appId": str,
        "fileContentsBase64": str,
        "fileName": str,
        "scope": DocumentScopeType,
        "sessionId": NotRequired[str],
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
ListLibraryItemsInputRequestTypeDef = TypedDict(
    "ListLibraryItemsInputRequestTypeDef",
    {
        "instanceId": str,
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
        "categoryId": NotRequired[str],
    },
)
ListQAppsInputRequestTypeDef = TypedDict(
    "ListQAppsInputRequestTypeDef",
    {
        "instanceId": str,
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
UserAppItemTypeDef = TypedDict(
    "UserAppItemTypeDef",
    {
        "appId": str,
        "appArn": str,
        "title": str,
        "createdAt": datetime,
        "description": NotRequired[str],
        "canEdit": NotRequired[bool],
        "status": NotRequired[str],
        "isVerified": NotRequired[bool],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)
StopQAppSessionInputRequestTypeDef = TypedDict(
    "StopQAppSessionInputRequestTypeDef",
    {
        "instanceId": str,
        "sessionId": str,
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
UpdateLibraryItemInputRequestTypeDef = TypedDict(
    "UpdateLibraryItemInputRequestTypeDef",
    {
        "instanceId": str,
        "libraryItemId": str,
        "status": NotRequired[LibraryItemStatusType],
        "categories": NotRequired[Sequence[str]],
    },
)
UpdateLibraryItemMetadataInputRequestTypeDef = TypedDict(
    "UpdateLibraryItemMetadataInputRequestTypeDef",
    {
        "instanceId": str,
        "libraryItemId": str,
        "isVerified": NotRequired[bool],
    },
)
StartQAppSessionInputRequestTypeDef = TypedDict(
    "StartQAppSessionInputRequestTypeDef",
    {
        "instanceId": str,
        "appId": str,
        "appVersion": int,
        "initialValues": NotRequired[Sequence[CardValueTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateQAppSessionInputRequestTypeDef = TypedDict(
    "UpdateQAppSessionInputRequestTypeDef",
    {
        "instanceId": str,
        "sessionId": str,
        "values": NotRequired[Sequence[CardValueTypeDef]],
    },
)
LibraryItemMemberTypeDef = TypedDict(
    "LibraryItemMemberTypeDef",
    {
        "libraryItemId": str,
        "appId": str,
        "appVersion": int,
        "categories": List[CategoryTypeDef],
        "status": str,
        "createdAt": datetime,
        "createdBy": str,
        "ratingCount": int,
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "isRatedByUser": NotRequired[bool],
        "userCount": NotRequired[int],
        "isVerified": NotRequired[bool],
    },
)
PredictQAppInputOptionsTypeDef = TypedDict(
    "PredictQAppInputOptionsTypeDef",
    {
        "conversation": NotRequired[Sequence[ConversationMessageTypeDef]],
        "problemStatement": NotRequired[str],
    },
)
CreateLibraryItemOutputTypeDef = TypedDict(
    "CreateLibraryItemOutputTypeDef",
    {
        "libraryItemId": str,
        "status": str,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ratingCount": int,
        "isVerified": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateQAppOutputTypeDef = TypedDict(
    "CreateQAppOutputTypeDef",
    {
        "appId": str,
        "appArn": str,
        "title": str,
        "description": str,
        "initialPrompt": str,
        "appVersion": int,
        "status": AppStatusType,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "requiredCapabilities": List[AppRequiredCapabilityType],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLibraryItemOutputTypeDef = TypedDict(
    "GetLibraryItemOutputTypeDef",
    {
        "libraryItemId": str,
        "appId": str,
        "appVersion": int,
        "categories": List[CategoryTypeDef],
        "status": str,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ratingCount": int,
        "isRatedByUser": bool,
        "userCount": int,
        "isVerified": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQAppSessionOutputTypeDef = TypedDict(
    "GetQAppSessionOutputTypeDef",
    {
        "sessionId": str,
        "sessionArn": str,
        "status": ExecutionStatusType,
        "cardStatus": Dict[str, CardStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportDocumentOutputTypeDef = TypedDict(
    "ImportDocumentOutputTypeDef",
    {
        "fileId": str,
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
StartQAppSessionOutputTypeDef = TypedDict(
    "StartQAppSessionOutputTypeDef",
    {
        "sessionId": str,
        "sessionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLibraryItemOutputTypeDef = TypedDict(
    "UpdateLibraryItemOutputTypeDef",
    {
        "libraryItemId": str,
        "appId": str,
        "appVersion": int,
        "categories": List[CategoryTypeDef],
        "status": str,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ratingCount": int,
        "isRatedByUser": bool,
        "userCount": int,
        "isVerified": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateQAppOutputTypeDef = TypedDict(
    "UpdateQAppOutputTypeDef",
    {
        "appId": str,
        "appArn": str,
        "title": str,
        "description": str,
        "initialPrompt": str,
        "appVersion": int,
        "status": AppStatusType,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "requiredCapabilities": List[AppRequiredCapabilityType],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateQAppSessionOutputTypeDef = TypedDict(
    "UpdateQAppSessionOutputTypeDef",
    {
        "sessionId": str,
        "sessionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentAttributeOutputTypeDef = TypedDict(
    "DocumentAttributeOutputTypeDef",
    {
        "name": str,
        "value": DocumentAttributeValueOutputTypeDef,
    },
)
DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "stringValue": NotRequired[str],
        "stringListValue": NotRequired[Sequence[str]],
        "longValue": NotRequired[int],
        "dateValue": NotRequired[TimestampTypeDef],
    },
)
ListLibraryItemsInputListLibraryItemsPaginateTypeDef = TypedDict(
    "ListLibraryItemsInputListLibraryItemsPaginateTypeDef",
    {
        "instanceId": str,
        "categoryId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQAppsInputListQAppsPaginateTypeDef = TypedDict(
    "ListQAppsInputListQAppsPaginateTypeDef",
    {
        "instanceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQAppsOutputTypeDef = TypedDict(
    "ListQAppsOutputTypeDef",
    {
        "apps": List[UserAppItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLibraryItemsOutputTypeDef = TypedDict(
    "ListLibraryItemsOutputTypeDef",
    {
        "libraryItems": List[LibraryItemMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PredictQAppInputRequestTypeDef = TypedDict(
    "PredictQAppInputRequestTypeDef",
    {
        "instanceId": str,
        "options": NotRequired[PredictQAppInputOptionsTypeDef],
    },
)
AttributeFilterOutputTypeDef = TypedDict(
    "AttributeFilterOutputTypeDef",
    {
        "andAllFilters": NotRequired[List[Dict[str, Any]]],
        "orAllFilters": NotRequired[List[Dict[str, Any]]],
        "notFilter": NotRequired[Dict[str, Any]],
        "equalsTo": NotRequired[DocumentAttributeOutputTypeDef],
        "containsAll": NotRequired[DocumentAttributeOutputTypeDef],
        "containsAny": NotRequired[DocumentAttributeOutputTypeDef],
        "greaterThan": NotRequired[DocumentAttributeOutputTypeDef],
        "greaterThanOrEquals": NotRequired[DocumentAttributeOutputTypeDef],
        "lessThan": NotRequired[DocumentAttributeOutputTypeDef],
        "lessThanOrEquals": NotRequired[DocumentAttributeOutputTypeDef],
    },
)
DocumentAttributeValueUnionTypeDef = Union[
    DocumentAttributeValueTypeDef, DocumentAttributeValueOutputTypeDef
]
QQueryCardInputOutputTypeDef = TypedDict(
    "QQueryCardInputOutputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "prompt": str,
        "outputSource": NotRequired[CardOutputSourceType],
        "attributeFilter": NotRequired[AttributeFilterOutputTypeDef],
    },
)
QQueryCardTypeDef = TypedDict(
    "QQueryCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "prompt": str,
        "outputSource": CardOutputSourceType,
        "attributeFilter": NotRequired[AttributeFilterOutputTypeDef],
    },
)
DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "name": str,
        "value": DocumentAttributeValueUnionTypeDef,
    },
)
CardInputOutputTypeDef = TypedDict(
    "CardInputOutputTypeDef",
    {
        "textInput": NotRequired[TextInputCardInputTypeDef],
        "qQuery": NotRequired[QQueryCardInputOutputTypeDef],
        "qPlugin": NotRequired[QPluginCardInputTypeDef],
        "fileUpload": NotRequired[FileUploadCardInputTypeDef],
    },
)
CardTypeDef = TypedDict(
    "CardTypeDef",
    {
        "textInput": NotRequired[TextInputCardTypeDef],
        "qQuery": NotRequired[QQueryCardTypeDef],
        "qPlugin": NotRequired[QPluginCardTypeDef],
        "fileUpload": NotRequired[FileUploadCardTypeDef],
    },
)
DocumentAttributeUnionTypeDef = Union[DocumentAttributeTypeDef, DocumentAttributeOutputTypeDef]
AppDefinitionInputOutputTypeDef = TypedDict(
    "AppDefinitionInputOutputTypeDef",
    {
        "cards": List[CardInputOutputTypeDef],
        "initialPrompt": NotRequired[str],
    },
)
AppDefinitionTypeDef = TypedDict(
    "AppDefinitionTypeDef",
    {
        "appDefinitionVersion": str,
        "cards": List[CardTypeDef],
        "canEdit": NotRequired[bool],
    },
)
AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "andAllFilters": NotRequired[Sequence[Mapping[str, Any]]],
        "orAllFilters": NotRequired[Sequence[Mapping[str, Any]]],
        "notFilter": NotRequired[Mapping[str, Any]],
        "equalsTo": NotRequired[DocumentAttributeUnionTypeDef],
        "containsAll": NotRequired[DocumentAttributeUnionTypeDef],
        "containsAny": NotRequired[DocumentAttributeUnionTypeDef],
        "greaterThan": NotRequired[DocumentAttributeUnionTypeDef],
        "greaterThanOrEquals": NotRequired[DocumentAttributeUnionTypeDef],
        "lessThan": NotRequired[DocumentAttributeUnionTypeDef],
        "lessThanOrEquals": NotRequired[DocumentAttributeUnionTypeDef],
    },
)
PredictAppDefinitionTypeDef = TypedDict(
    "PredictAppDefinitionTypeDef",
    {
        "title": str,
        "appDefinition": AppDefinitionInputOutputTypeDef,
        "description": NotRequired[str],
    },
)
GetQAppOutputTypeDef = TypedDict(
    "GetQAppOutputTypeDef",
    {
        "appId": str,
        "appArn": str,
        "title": str,
        "description": str,
        "initialPrompt": str,
        "appVersion": int,
        "status": AppStatusType,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "requiredCapabilities": List[AppRequiredCapabilityType],
        "appDefinition": AppDefinitionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttributeFilterUnionTypeDef = Union[AttributeFilterTypeDef, AttributeFilterOutputTypeDef]
PredictQAppOutputTypeDef = TypedDict(
    "PredictQAppOutputTypeDef",
    {
        "app": PredictAppDefinitionTypeDef,
        "problemStatement": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QQueryCardInputTypeDef = TypedDict(
    "QQueryCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "prompt": str,
        "outputSource": NotRequired[CardOutputSourceType],
        "attributeFilter": NotRequired[AttributeFilterUnionTypeDef],
    },
)
QQueryCardInputUnionTypeDef = Union[QQueryCardInputTypeDef, QQueryCardInputOutputTypeDef]
CardInputTypeDef = TypedDict(
    "CardInputTypeDef",
    {
        "textInput": NotRequired[TextInputCardInputTypeDef],
        "qQuery": NotRequired[QQueryCardInputUnionTypeDef],
        "qPlugin": NotRequired[QPluginCardInputTypeDef],
        "fileUpload": NotRequired[FileUploadCardInputTypeDef],
    },
)
CardInputUnionTypeDef = Union[CardInputTypeDef, CardInputOutputTypeDef]
AppDefinitionInputTypeDef = TypedDict(
    "AppDefinitionInputTypeDef",
    {
        "cards": Sequence[CardInputUnionTypeDef],
        "initialPrompt": NotRequired[str],
    },
)
CreateQAppInputRequestTypeDef = TypedDict(
    "CreateQAppInputRequestTypeDef",
    {
        "instanceId": str,
        "title": str,
        "appDefinition": AppDefinitionInputTypeDef,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateQAppInputRequestTypeDef = TypedDict(
    "UpdateQAppInputRequestTypeDef",
    {
        "instanceId": str,
        "appId": str,
        "title": NotRequired[str],
        "description": NotRequired[str],
        "appDefinition": NotRequired[AppDefinitionInputTypeDef],
    },
)
