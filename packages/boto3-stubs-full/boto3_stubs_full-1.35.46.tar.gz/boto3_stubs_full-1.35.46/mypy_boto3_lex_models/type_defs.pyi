"""
Type annotations for lex-models service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/type_defs/)

Usage::

    ```python
    from mypy_boto3_lex_models.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ChannelStatusType,
    ChannelTypeType,
    ContentTypeType,
    DestinationType,
    ExportStatusType,
    ExportTypeType,
    FulfillmentActivityTypeType,
    ImportStatusType,
    LocaleType,
    LogTypeType,
    MergeStrategyType,
    MigrationAlertTypeType,
    MigrationSortAttributeType,
    MigrationStatusType,
    MigrationStrategyType,
    ObfuscationSettingType,
    ProcessBehaviorType,
    ResourceTypeType,
    SlotConstraintType,
    SlotValueSelectionStrategyType,
    SortOrderType,
    StatusType,
    StatusTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "BotChannelAssociationTypeDef",
    "BotMetadataTypeDef",
    "BuiltinIntentMetadataTypeDef",
    "BuiltinIntentSlotTypeDef",
    "BuiltinSlotTypeMetadataTypeDef",
    "CodeHookTypeDef",
    "LogSettingsRequestTypeDef",
    "LogSettingsResponseTypeDef",
    "CreateBotVersionRequestRequestTypeDef",
    "IntentTypeDef",
    "ResponseMetadataTypeDef",
    "CreateIntentVersionRequestRequestTypeDef",
    "InputContextTypeDef",
    "KendraConfigurationTypeDef",
    "OutputContextTypeDef",
    "CreateSlotTypeVersionRequestRequestTypeDef",
    "EnumerationValueOutputTypeDef",
    "DeleteBotAliasRequestRequestTypeDef",
    "DeleteBotChannelAssociationRequestRequestTypeDef",
    "DeleteBotRequestRequestTypeDef",
    "DeleteBotVersionRequestRequestTypeDef",
    "DeleteIntentRequestRequestTypeDef",
    "DeleteIntentVersionRequestRequestTypeDef",
    "DeleteSlotTypeRequestRequestTypeDef",
    "DeleteSlotTypeVersionRequestRequestTypeDef",
    "DeleteUtterancesRequestRequestTypeDef",
    "EnumerationValueTypeDef",
    "GetBotAliasRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetBotAliasesRequestRequestTypeDef",
    "GetBotChannelAssociationRequestRequestTypeDef",
    "GetBotChannelAssociationsRequestRequestTypeDef",
    "GetBotRequestRequestTypeDef",
    "GetBotVersionsRequestRequestTypeDef",
    "GetBotsRequestRequestTypeDef",
    "GetBuiltinIntentRequestRequestTypeDef",
    "GetBuiltinIntentsRequestRequestTypeDef",
    "GetBuiltinSlotTypesRequestRequestTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetImportRequestRequestTypeDef",
    "GetIntentRequestRequestTypeDef",
    "GetIntentVersionsRequestRequestTypeDef",
    "IntentMetadataTypeDef",
    "GetIntentsRequestRequestTypeDef",
    "GetMigrationRequestRequestTypeDef",
    "MigrationAlertTypeDef",
    "GetMigrationsRequestRequestTypeDef",
    "MigrationSummaryTypeDef",
    "GetSlotTypeRequestRequestTypeDef",
    "GetSlotTypeVersionsRequestRequestTypeDef",
    "SlotTypeMetadataTypeDef",
    "GetSlotTypesRequestRequestTypeDef",
    "GetUtterancesViewRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "MessageTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotTypeRegexConfigurationTypeDef",
    "StartMigrationRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UtteranceDataTypeDef",
    "FulfillmentActivityTypeDef",
    "ConversationLogsRequestTypeDef",
    "ConversationLogsResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetBotChannelAssociationResponseTypeDef",
    "GetBotChannelAssociationsResponseTypeDef",
    "GetBotVersionsResponseTypeDef",
    "GetBotsResponseTypeDef",
    "GetBuiltinIntentResponseTypeDef",
    "GetBuiltinIntentsResponseTypeDef",
    "GetBuiltinSlotTypesResponseTypeDef",
    "GetExportResponseTypeDef",
    "GetImportResponseTypeDef",
    "StartMigrationResponseTypeDef",
    "EnumerationValueUnionTypeDef",
    "GetBotAliasesRequestGetBotAliasesPaginateTypeDef",
    "GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef",
    "GetBotVersionsRequestGetBotVersionsPaginateTypeDef",
    "GetBotsRequestGetBotsPaginateTypeDef",
    "GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef",
    "GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef",
    "GetIntentVersionsRequestGetIntentVersionsPaginateTypeDef",
    "GetIntentsRequestGetIntentsPaginateTypeDef",
    "GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef",
    "GetSlotTypesRequestGetSlotTypesPaginateTypeDef",
    "GetIntentVersionsResponseTypeDef",
    "GetIntentsResponseTypeDef",
    "GetMigrationResponseTypeDef",
    "GetMigrationsResponseTypeDef",
    "GetSlotTypeVersionsResponseTypeDef",
    "GetSlotTypesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartImportRequestRequestTypeDef",
    "StartImportResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "PromptOutputTypeDef",
    "PromptTypeDef",
    "StatementOutputTypeDef",
    "StatementTypeDef",
    "SlotDefaultValueSpecOutputTypeDef",
    "SlotDefaultValueSpecTypeDef",
    "SlotTypeConfigurationTypeDef",
    "UtteranceListTypeDef",
    "PutBotAliasRequestRequestTypeDef",
    "BotAliasMetadataTypeDef",
    "GetBotAliasResponseTypeDef",
    "PutBotAliasResponseTypeDef",
    "PromptUnionTypeDef",
    "CreateBotVersionResponseTypeDef",
    "FollowUpPromptOutputTypeDef",
    "GetBotResponseTypeDef",
    "PutBotResponseTypeDef",
    "PutBotRequestRequestTypeDef",
    "StatementUnionTypeDef",
    "SlotOutputTypeDef",
    "SlotDefaultValueSpecUnionTypeDef",
    "CreateSlotTypeVersionResponseTypeDef",
    "GetSlotTypeResponseTypeDef",
    "PutSlotTypeRequestRequestTypeDef",
    "PutSlotTypeResponseTypeDef",
    "GetUtterancesViewResponseTypeDef",
    "GetBotAliasesResponseTypeDef",
    "FollowUpPromptTypeDef",
    "CreateIntentVersionResponseTypeDef",
    "GetIntentResponseTypeDef",
    "PutIntentResponseTypeDef",
    "SlotTypeDef",
    "SlotUnionTypeDef",
    "PutIntentRequestRequestTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BotChannelAssociationTypeDef = TypedDict(
    "BotChannelAssociationTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "botAlias": NotRequired[str],
        "botName": NotRequired[str],
        "createdDate": NotRequired[datetime],
        "type": NotRequired[ChannelTypeType],
        "botConfiguration": NotRequired[Dict[str, str]],
        "status": NotRequired[ChannelStatusType],
        "failureReason": NotRequired[str],
    },
)
BotMetadataTypeDef = TypedDict(
    "BotMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[StatusType],
        "lastUpdatedDate": NotRequired[datetime],
        "createdDate": NotRequired[datetime],
        "version": NotRequired[str],
    },
)
BuiltinIntentMetadataTypeDef = TypedDict(
    "BuiltinIntentMetadataTypeDef",
    {
        "signature": NotRequired[str],
        "supportedLocales": NotRequired[List[LocaleType]],
    },
)
BuiltinIntentSlotTypeDef = TypedDict(
    "BuiltinIntentSlotTypeDef",
    {
        "name": NotRequired[str],
    },
)
BuiltinSlotTypeMetadataTypeDef = TypedDict(
    "BuiltinSlotTypeMetadataTypeDef",
    {
        "signature": NotRequired[str],
        "supportedLocales": NotRequired[List[LocaleType]],
    },
)
CodeHookTypeDef = TypedDict(
    "CodeHookTypeDef",
    {
        "uri": str,
        "messageVersion": str,
    },
)
LogSettingsRequestTypeDef = TypedDict(
    "LogSettingsRequestTypeDef",
    {
        "logType": LogTypeType,
        "destination": DestinationType,
        "resourceArn": str,
        "kmsKeyArn": NotRequired[str],
    },
)
LogSettingsResponseTypeDef = TypedDict(
    "LogSettingsResponseTypeDef",
    {
        "logType": NotRequired[LogTypeType],
        "destination": NotRequired[DestinationType],
        "kmsKeyArn": NotRequired[str],
        "resourceArn": NotRequired[str],
        "resourcePrefix": NotRequired[str],
    },
)
CreateBotVersionRequestRequestTypeDef = TypedDict(
    "CreateBotVersionRequestRequestTypeDef",
    {
        "name": str,
        "checksum": NotRequired[str],
    },
)
IntentTypeDef = TypedDict(
    "IntentTypeDef",
    {
        "intentName": str,
        "intentVersion": str,
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
CreateIntentVersionRequestRequestTypeDef = TypedDict(
    "CreateIntentVersionRequestRequestTypeDef",
    {
        "name": str,
        "checksum": NotRequired[str],
    },
)
InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)
KendraConfigurationTypeDef = TypedDict(
    "KendraConfigurationTypeDef",
    {
        "kendraIndex": str,
        "role": str,
        "queryFilterString": NotRequired[str],
    },
)
OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)
CreateSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "CreateSlotTypeVersionRequestRequestTypeDef",
    {
        "name": str,
        "checksum": NotRequired[str],
    },
)
EnumerationValueOutputTypeDef = TypedDict(
    "EnumerationValueOutputTypeDef",
    {
        "value": str,
        "synonyms": NotRequired[List[str]],
    },
)
DeleteBotAliasRequestRequestTypeDef = TypedDict(
    "DeleteBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)
DeleteBotChannelAssociationRequestRequestTypeDef = TypedDict(
    "DeleteBotChannelAssociationRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)
DeleteBotRequestRequestTypeDef = TypedDict(
    "DeleteBotRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteBotVersionRequestRequestTypeDef = TypedDict(
    "DeleteBotVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)
DeleteIntentRequestRequestTypeDef = TypedDict(
    "DeleteIntentRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteIntentVersionRequestRequestTypeDef = TypedDict(
    "DeleteIntentVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)
DeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)
DeleteUtterancesRequestRequestTypeDef = TypedDict(
    "DeleteUtterancesRequestRequestTypeDef",
    {
        "botName": str,
        "userId": str,
    },
)
EnumerationValueTypeDef = TypedDict(
    "EnumerationValueTypeDef",
    {
        "value": str,
        "synonyms": NotRequired[Sequence[str]],
    },
)
GetBotAliasRequestRequestTypeDef = TypedDict(
    "GetBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
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
GetBotAliasesRequestRequestTypeDef = TypedDict(
    "GetBotAliasesRequestRequestTypeDef",
    {
        "botName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)
GetBotChannelAssociationRequestRequestTypeDef = TypedDict(
    "GetBotChannelAssociationRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)
GetBotChannelAssociationsRequestRequestTypeDef = TypedDict(
    "GetBotChannelAssociationsRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)
GetBotRequestRequestTypeDef = TypedDict(
    "GetBotRequestRequestTypeDef",
    {
        "name": str,
        "versionOrAlias": str,
    },
)
GetBotVersionsRequestRequestTypeDef = TypedDict(
    "GetBotVersionsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetBotsRequestRequestTypeDef = TypedDict(
    "GetBotsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)
GetBuiltinIntentRequestRequestTypeDef = TypedDict(
    "GetBuiltinIntentRequestRequestTypeDef",
    {
        "signature": str,
    },
)
GetBuiltinIntentsRequestRequestTypeDef = TypedDict(
    "GetBuiltinIntentsRequestRequestTypeDef",
    {
        "locale": NotRequired[LocaleType],
        "signatureContains": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetBuiltinSlotTypesRequestRequestTypeDef = TypedDict(
    "GetBuiltinSlotTypesRequestRequestTypeDef",
    {
        "locale": NotRequired[LocaleType],
        "signatureContains": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetExportRequestRequestTypeDef = TypedDict(
    "GetExportRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
    },
)
GetImportRequestRequestTypeDef = TypedDict(
    "GetImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)
GetIntentRequestRequestTypeDef = TypedDict(
    "GetIntentRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)
GetIntentVersionsRequestRequestTypeDef = TypedDict(
    "GetIntentVersionsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
IntentMetadataTypeDef = TypedDict(
    "IntentMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedDate": NotRequired[datetime],
        "createdDate": NotRequired[datetime],
        "version": NotRequired[str],
    },
)
GetIntentsRequestRequestTypeDef = TypedDict(
    "GetIntentsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)
GetMigrationRequestRequestTypeDef = TypedDict(
    "GetMigrationRequestRequestTypeDef",
    {
        "migrationId": str,
    },
)
MigrationAlertTypeDef = TypedDict(
    "MigrationAlertTypeDef",
    {
        "type": NotRequired[MigrationAlertTypeType],
        "message": NotRequired[str],
        "details": NotRequired[List[str]],
        "referenceURLs": NotRequired[List[str]],
    },
)
GetMigrationsRequestRequestTypeDef = TypedDict(
    "GetMigrationsRequestRequestTypeDef",
    {
        "sortByAttribute": NotRequired[MigrationSortAttributeType],
        "sortByOrder": NotRequired[SortOrderType],
        "v1BotNameContains": NotRequired[str],
        "migrationStatusEquals": NotRequired[MigrationStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
MigrationSummaryTypeDef = TypedDict(
    "MigrationSummaryTypeDef",
    {
        "migrationId": NotRequired[str],
        "v1BotName": NotRequired[str],
        "v1BotVersion": NotRequired[str],
        "v1BotLocale": NotRequired[LocaleType],
        "v2BotId": NotRequired[str],
        "v2BotRole": NotRequired[str],
        "migrationStatus": NotRequired[MigrationStatusType],
        "migrationStrategy": NotRequired[MigrationStrategyType],
        "migrationTimestamp": NotRequired[datetime],
    },
)
GetSlotTypeRequestRequestTypeDef = TypedDict(
    "GetSlotTypeRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)
GetSlotTypeVersionsRequestRequestTypeDef = TypedDict(
    "GetSlotTypeVersionsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SlotTypeMetadataTypeDef = TypedDict(
    "SlotTypeMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedDate": NotRequired[datetime],
        "createdDate": NotRequired[datetime],
        "version": NotRequired[str],
    },
)
GetSlotTypesRequestRequestTypeDef = TypedDict(
    "GetSlotTypesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)
GetUtterancesViewRequestRequestTypeDef = TypedDict(
    "GetUtterancesViewRequestRequestTypeDef",
    {
        "botName": str,
        "botVersions": Sequence[str],
        "statusType": StatusTypeType,
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "contentType": ContentTypeType,
        "content": str,
        "groupNumber": NotRequired[int],
    },
)
SlotDefaultValueTypeDef = TypedDict(
    "SlotDefaultValueTypeDef",
    {
        "defaultValue": str,
    },
)
SlotTypeRegexConfigurationTypeDef = TypedDict(
    "SlotTypeRegexConfigurationTypeDef",
    {
        "pattern": str,
    },
)
StartMigrationRequestRequestTypeDef = TypedDict(
    "StartMigrationRequestRequestTypeDef",
    {
        "v1BotName": str,
        "v1BotVersion": str,
        "v2BotName": str,
        "v2BotRole": str,
        "migrationStrategy": MigrationStrategyType,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UtteranceDataTypeDef = TypedDict(
    "UtteranceDataTypeDef",
    {
        "utteranceString": NotRequired[str],
        "count": NotRequired[int],
        "distinctUsers": NotRequired[int],
        "firstUtteredDate": NotRequired[datetime],
        "lastUtteredDate": NotRequired[datetime],
    },
)
FulfillmentActivityTypeDef = TypedDict(
    "FulfillmentActivityTypeDef",
    {
        "type": FulfillmentActivityTypeType,
        "codeHook": NotRequired[CodeHookTypeDef],
    },
)
ConversationLogsRequestTypeDef = TypedDict(
    "ConversationLogsRequestTypeDef",
    {
        "logSettings": Sequence[LogSettingsRequestTypeDef],
        "iamRoleArn": str,
    },
)
ConversationLogsResponseTypeDef = TypedDict(
    "ConversationLogsResponseTypeDef",
    {
        "logSettings": NotRequired[List[LogSettingsResponseTypeDef]],
        "iamRoleArn": NotRequired[str],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBotChannelAssociationResponseTypeDef = TypedDict(
    "GetBotChannelAssociationResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelTypeType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatusType,
        "failureReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBotChannelAssociationsResponseTypeDef = TypedDict(
    "GetBotChannelAssociationsResponseTypeDef",
    {
        "botChannelAssociations": List[BotChannelAssociationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBotVersionsResponseTypeDef = TypedDict(
    "GetBotVersionsResponseTypeDef",
    {
        "bots": List[BotMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBotsResponseTypeDef = TypedDict(
    "GetBotsResponseTypeDef",
    {
        "bots": List[BotMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBuiltinIntentResponseTypeDef = TypedDict(
    "GetBuiltinIntentResponseTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
        "slots": List[BuiltinIntentSlotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBuiltinIntentsResponseTypeDef = TypedDict(
    "GetBuiltinIntentsResponseTypeDef",
    {
        "intents": List[BuiltinIntentMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBuiltinSlotTypesResponseTypeDef = TypedDict(
    "GetBuiltinSlotTypesResponseTypeDef",
    {
        "slotTypes": List[BuiltinSlotTypeMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExportResponseTypeDef = TypedDict(
    "GetExportResponseTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
        "exportStatus": ExportStatusType,
        "failureReason": str,
        "url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImportResponseTypeDef = TypedDict(
    "GetImportResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "failureReason": List[str],
        "createdDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMigrationResponseTypeDef = TypedDict(
    "StartMigrationResponseTypeDef",
    {
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationId": str,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnumerationValueUnionTypeDef = Union[EnumerationValueTypeDef, EnumerationValueOutputTypeDef]
GetBotAliasesRequestGetBotAliasesPaginateTypeDef = TypedDict(
    "GetBotAliasesRequestGetBotAliasesPaginateTypeDef",
    {
        "botName": str,
        "nameContains": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef = TypedDict(
    "GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "nameContains": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBotVersionsRequestGetBotVersionsPaginateTypeDef = TypedDict(
    "GetBotVersionsRequestGetBotVersionsPaginateTypeDef",
    {
        "name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBotsRequestGetBotsPaginateTypeDef = TypedDict(
    "GetBotsRequestGetBotsPaginateTypeDef",
    {
        "nameContains": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef = TypedDict(
    "GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef",
    {
        "locale": NotRequired[LocaleType],
        "signatureContains": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef = TypedDict(
    "GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef",
    {
        "locale": NotRequired[LocaleType],
        "signatureContains": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIntentVersionsRequestGetIntentVersionsPaginateTypeDef = TypedDict(
    "GetIntentVersionsRequestGetIntentVersionsPaginateTypeDef",
    {
        "name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIntentsRequestGetIntentsPaginateTypeDef = TypedDict(
    "GetIntentsRequestGetIntentsPaginateTypeDef",
    {
        "nameContains": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef = TypedDict(
    "GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef",
    {
        "name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSlotTypesRequestGetSlotTypesPaginateTypeDef = TypedDict(
    "GetSlotTypesRequestGetSlotTypesPaginateTypeDef",
    {
        "nameContains": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetIntentVersionsResponseTypeDef = TypedDict(
    "GetIntentVersionsResponseTypeDef",
    {
        "intents": List[IntentMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIntentsResponseTypeDef = TypedDict(
    "GetIntentsResponseTypeDef",
    {
        "intents": List[IntentMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMigrationResponseTypeDef = TypedDict(
    "GetMigrationResponseTypeDef",
    {
        "migrationId": str,
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationStatus": MigrationStatusType,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
        "alerts": List[MigrationAlertTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMigrationsResponseTypeDef = TypedDict(
    "GetMigrationsResponseTypeDef",
    {
        "migrationSummaries": List[MigrationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSlotTypeVersionsResponseTypeDef = TypedDict(
    "GetSlotTypeVersionsResponseTypeDef",
    {
        "slotTypes": List[SlotTypeMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSlotTypesResponseTypeDef = TypedDict(
    "GetSlotTypesResponseTypeDef",
    {
        "slotTypes": List[SlotTypeMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportRequestRequestTypeDef = TypedDict(
    "StartImportRequestRequestTypeDef",
    {
        "payload": BlobTypeDef,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "tags": List[TagTypeDef],
        "createdDate": datetime,
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
PromptOutputTypeDef = TypedDict(
    "PromptOutputTypeDef",
    {
        "messages": List[MessageTypeDef],
        "maxAttempts": int,
        "responseCard": NotRequired[str],
    },
)
PromptTypeDef = TypedDict(
    "PromptTypeDef",
    {
        "messages": Sequence[MessageTypeDef],
        "maxAttempts": int,
        "responseCard": NotRequired[str],
    },
)
StatementOutputTypeDef = TypedDict(
    "StatementOutputTypeDef",
    {
        "messages": List[MessageTypeDef],
        "responseCard": NotRequired[str],
    },
)
StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "messages": Sequence[MessageTypeDef],
        "responseCard": NotRequired[str],
    },
)
SlotDefaultValueSpecOutputTypeDef = TypedDict(
    "SlotDefaultValueSpecOutputTypeDef",
    {
        "defaultValueList": List[SlotDefaultValueTypeDef],
    },
)
SlotDefaultValueSpecTypeDef = TypedDict(
    "SlotDefaultValueSpecTypeDef",
    {
        "defaultValueList": Sequence[SlotDefaultValueTypeDef],
    },
)
SlotTypeConfigurationTypeDef = TypedDict(
    "SlotTypeConfigurationTypeDef",
    {
        "regexConfiguration": NotRequired[SlotTypeRegexConfigurationTypeDef],
    },
)
UtteranceListTypeDef = TypedDict(
    "UtteranceListTypeDef",
    {
        "botVersion": NotRequired[str],
        "utterances": NotRequired[List[UtteranceDataTypeDef]],
    },
)
PutBotAliasRequestRequestTypeDef = TypedDict(
    "PutBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botVersion": str,
        "botName": str,
        "description": NotRequired[str],
        "checksum": NotRequired[str],
        "conversationLogs": NotRequired[ConversationLogsRequestTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
BotAliasMetadataTypeDef = TypedDict(
    "BotAliasMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "botVersion": NotRequired[str],
        "botName": NotRequired[str],
        "lastUpdatedDate": NotRequired[datetime],
        "createdDate": NotRequired[datetime],
        "checksum": NotRequired[str],
        "conversationLogs": NotRequired[ConversationLogsResponseTypeDef],
    },
)
GetBotAliasResponseTypeDef = TypedDict(
    "GetBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ConversationLogsResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutBotAliasResponseTypeDef = TypedDict(
    "PutBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ConversationLogsResponseTypeDef,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PromptUnionTypeDef = Union[PromptTypeDef, PromptOutputTypeDef]
CreateBotVersionResponseTypeDef = TypedDict(
    "CreateBotVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[IntentTypeDef],
        "clarificationPrompt": PromptOutputTypeDef,
        "abortStatement": StatementOutputTypeDef,
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "enableModelImprovements": bool,
        "detectSentiment": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FollowUpPromptOutputTypeDef = TypedDict(
    "FollowUpPromptOutputTypeDef",
    {
        "prompt": PromptOutputTypeDef,
        "rejectionStatement": StatementOutputTypeDef,
    },
)
GetBotResponseTypeDef = TypedDict(
    "GetBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[IntentTypeDef],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": PromptOutputTypeDef,
        "abortStatement": StatementOutputTypeDef,
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "detectSentiment": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutBotResponseTypeDef = TypedDict(
    "PutBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[IntentTypeDef],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": PromptOutputTypeDef,
        "abortStatement": StatementOutputTypeDef,
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "createVersion": bool,
        "detectSentiment": bool,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutBotRequestRequestTypeDef = TypedDict(
    "PutBotRequestRequestTypeDef",
    {
        "name": str,
        "locale": LocaleType,
        "childDirected": bool,
        "description": NotRequired[str],
        "intents": NotRequired[Sequence[IntentTypeDef]],
        "enableModelImprovements": NotRequired[bool],
        "nluIntentConfidenceThreshold": NotRequired[float],
        "clarificationPrompt": NotRequired[PromptTypeDef],
        "abortStatement": NotRequired[StatementTypeDef],
        "idleSessionTTLInSeconds": NotRequired[int],
        "voiceId": NotRequired[str],
        "checksum": NotRequired[str],
        "processBehavior": NotRequired[ProcessBehaviorType],
        "detectSentiment": NotRequired[bool],
        "createVersion": NotRequired[bool],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StatementUnionTypeDef = Union[StatementTypeDef, StatementOutputTypeDef]
SlotOutputTypeDef = TypedDict(
    "SlotOutputTypeDef",
    {
        "name": str,
        "slotConstraint": SlotConstraintType,
        "description": NotRequired[str],
        "slotType": NotRequired[str],
        "slotTypeVersion": NotRequired[str],
        "valueElicitationPrompt": NotRequired[PromptOutputTypeDef],
        "priority": NotRequired[int],
        "sampleUtterances": NotRequired[List[str]],
        "responseCard": NotRequired[str],
        "obfuscationSetting": NotRequired[ObfuscationSettingType],
        "defaultValueSpec": NotRequired[SlotDefaultValueSpecOutputTypeDef],
    },
)
SlotDefaultValueSpecUnionTypeDef = Union[
    SlotDefaultValueSpecTypeDef, SlotDefaultValueSpecOutputTypeDef
]
CreateSlotTypeVersionResponseTypeDef = TypedDict(
    "CreateSlotTypeVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[EnumerationValueOutputTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[SlotTypeConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSlotTypeResponseTypeDef = TypedDict(
    "GetSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[EnumerationValueOutputTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[SlotTypeConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSlotTypeRequestRequestTypeDef = TypedDict(
    "PutSlotTypeRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "enumerationValues": NotRequired[Sequence[EnumerationValueUnionTypeDef]],
        "checksum": NotRequired[str],
        "valueSelectionStrategy": NotRequired[SlotValueSelectionStrategyType],
        "createVersion": NotRequired[bool],
        "parentSlotTypeSignature": NotRequired[str],
        "slotTypeConfigurations": NotRequired[Sequence[SlotTypeConfigurationTypeDef]],
    },
)
PutSlotTypeResponseTypeDef = TypedDict(
    "PutSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[EnumerationValueOutputTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[SlotTypeConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUtterancesViewResponseTypeDef = TypedDict(
    "GetUtterancesViewResponseTypeDef",
    {
        "botName": str,
        "utterances": List[UtteranceListTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBotAliasesResponseTypeDef = TypedDict(
    "GetBotAliasesResponseTypeDef",
    {
        "BotAliases": List[BotAliasMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FollowUpPromptTypeDef = TypedDict(
    "FollowUpPromptTypeDef",
    {
        "prompt": PromptUnionTypeDef,
        "rejectionStatement": StatementUnionTypeDef,
    },
)
CreateIntentVersionResponseTypeDef = TypedDict(
    "CreateIntentVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[SlotOutputTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": PromptOutputTypeDef,
        "rejectionStatement": StatementOutputTypeDef,
        "followUpPrompt": FollowUpPromptOutputTypeDef,
        "conclusionStatement": StatementOutputTypeDef,
        "dialogCodeHook": CodeHookTypeDef,
        "fulfillmentActivity": FulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": KendraConfigurationTypeDef,
        "inputContexts": List[InputContextTypeDef],
        "outputContexts": List[OutputContextTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIntentResponseTypeDef = TypedDict(
    "GetIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[SlotOutputTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": PromptOutputTypeDef,
        "rejectionStatement": StatementOutputTypeDef,
        "followUpPrompt": FollowUpPromptOutputTypeDef,
        "conclusionStatement": StatementOutputTypeDef,
        "dialogCodeHook": CodeHookTypeDef,
        "fulfillmentActivity": FulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": KendraConfigurationTypeDef,
        "inputContexts": List[InputContextTypeDef],
        "outputContexts": List[OutputContextTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutIntentResponseTypeDef = TypedDict(
    "PutIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[SlotOutputTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": PromptOutputTypeDef,
        "rejectionStatement": StatementOutputTypeDef,
        "followUpPrompt": FollowUpPromptOutputTypeDef,
        "conclusionStatement": StatementOutputTypeDef,
        "dialogCodeHook": CodeHookTypeDef,
        "fulfillmentActivity": FulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "createVersion": bool,
        "kendraConfiguration": KendraConfigurationTypeDef,
        "inputContexts": List[InputContextTypeDef],
        "outputContexts": List[OutputContextTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SlotTypeDef = TypedDict(
    "SlotTypeDef",
    {
        "name": str,
        "slotConstraint": SlotConstraintType,
        "description": NotRequired[str],
        "slotType": NotRequired[str],
        "slotTypeVersion": NotRequired[str],
        "valueElicitationPrompt": NotRequired[PromptUnionTypeDef],
        "priority": NotRequired[int],
        "sampleUtterances": NotRequired[Sequence[str]],
        "responseCard": NotRequired[str],
        "obfuscationSetting": NotRequired[ObfuscationSettingType],
        "defaultValueSpec": NotRequired[SlotDefaultValueSpecUnionTypeDef],
    },
)
SlotUnionTypeDef = Union[SlotTypeDef, SlotOutputTypeDef]
PutIntentRequestRequestTypeDef = TypedDict(
    "PutIntentRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "slots": NotRequired[Sequence[SlotUnionTypeDef]],
        "sampleUtterances": NotRequired[Sequence[str]],
        "confirmationPrompt": NotRequired[PromptTypeDef],
        "rejectionStatement": NotRequired[StatementTypeDef],
        "followUpPrompt": NotRequired[FollowUpPromptTypeDef],
        "conclusionStatement": NotRequired[StatementTypeDef],
        "dialogCodeHook": NotRequired[CodeHookTypeDef],
        "fulfillmentActivity": NotRequired[FulfillmentActivityTypeDef],
        "parentIntentSignature": NotRequired[str],
        "checksum": NotRequired[str],
        "createVersion": NotRequired[bool],
        "kendraConfiguration": NotRequired[KendraConfigurationTypeDef],
        "inputContexts": NotRequired[Sequence[InputContextTypeDef]],
        "outputContexts": NotRequired[Sequence[OutputContextTypeDef]],
    },
)
