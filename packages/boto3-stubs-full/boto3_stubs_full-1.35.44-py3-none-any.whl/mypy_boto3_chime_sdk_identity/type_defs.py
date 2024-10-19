"""
Type annotations for chime-sdk-identity service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_identity.type_defs import IdentityTypeDef

    data: IdentityTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AllowMessagesType,
    AppInstanceUserEndpointTypeType,
    EndpointStatusReasonType,
    EndpointStatusType,
    StandardMessagesType,
    TargetedMessagesType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "IdentityTypeDef",
    "AppInstanceBotSummaryTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "EndpointStateTypeDef",
    "EndpointAttributesTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "ExpirationSettingsTypeDef",
    "CreateAppInstanceAdminRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    "DeleteAppInstanceBotRequestRequestTypeDef",
    "DeleteAppInstanceRequestRequestTypeDef",
    "DeleteAppInstanceUserRequestRequestTypeDef",
    "DeregisterAppInstanceUserEndpointRequestRequestTypeDef",
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    "DescribeAppInstanceBotRequestRequestTypeDef",
    "DescribeAppInstanceRequestRequestTypeDef",
    "DescribeAppInstanceUserEndpointRequestRequestTypeDef",
    "DescribeAppInstanceUserRequestRequestTypeDef",
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    "InvokedByTypeDef",
    "ListAppInstanceAdminsRequestRequestTypeDef",
    "ListAppInstanceBotsRequestRequestTypeDef",
    "ListAppInstanceUserEndpointsRequestRequestTypeDef",
    "ListAppInstanceUsersRequestRequestTypeDef",
    "ListAppInstancesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppInstanceRequestRequestTypeDef",
    "UpdateAppInstanceUserEndpointRequestRequestTypeDef",
    "UpdateAppInstanceUserRequestRequestTypeDef",
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "AppInstanceUserEndpointSummaryTypeDef",
    "AppInstanceUserEndpointTypeDef",
    "RegisterAppInstanceUserEndpointRequestRequestTypeDef",
    "AppInstanceUserTypeDef",
    "PutAppInstanceUserExpirationSettingsRequestRequestTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceBotResponseTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListAppInstanceBotsResponseTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesResponseTypeDef",
    "PutAppInstanceUserExpirationSettingsResponseTypeDef",
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    "UpdateAppInstanceBotResponseTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
    "CreateAppInstanceRequestRequestTypeDef",
    "CreateAppInstanceUserRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "LexConfigurationTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "ListAppInstanceUserEndpointsResponseTypeDef",
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "ConfigurationTypeDef",
    "AppInstanceBotTypeDef",
    "CreateAppInstanceBotRequestRequestTypeDef",
    "UpdateAppInstanceBotRequestRequestTypeDef",
    "DescribeAppInstanceBotResponseTypeDef",
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
AppInstanceBotSummaryTypeDef = TypedDict(
    "AppInstanceBotSummaryTypeDef",
    {
        "AppInstanceBotArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)
ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef",
    {
        "RetentionDays": NotRequired[int],
    },
)
AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef",
    {
        "AppInstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)
AppInstanceTypeDef = TypedDict(
    "AppInstanceTypeDef",
    {
        "AppInstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Metadata": NotRequired[str],
    },
)
EndpointStateTypeDef = TypedDict(
    "EndpointStateTypeDef",
    {
        "Status": EndpointStatusType,
        "StatusReason": NotRequired[EndpointStatusReasonType],
    },
)
EndpointAttributesTypeDef = TypedDict(
    "EndpointAttributesTypeDef",
    {
        "DeviceToken": str,
        "VoipDeviceToken": NotRequired[str],
    },
)
AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)
ExpirationSettingsTypeDef = TypedDict(
    "ExpirationSettingsTypeDef",
    {
        "ExpirationDays": int,
        "ExpirationCriterion": Literal["CREATED_TIMESTAMP"],
    },
)
CreateAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
DeleteAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)
DeleteAppInstanceBotRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
    },
)
DeleteAppInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
DeleteAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)
DeregisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "DeregisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)
DescribeAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)
DescribeAppInstanceBotRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
    },
)
DescribeAppInstanceRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
DescribeAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)
DescribeAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)
GetAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
InvokedByTypeDef = TypedDict(
    "InvokedByTypeDef",
    {
        "StandardMessages": StandardMessagesType,
        "TargetedMessages": TargetedMessagesType,
    },
)
ListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "ListAppInstanceAdminsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAppInstanceBotsRequestRequestTypeDef = TypedDict(
    "ListAppInstanceBotsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAppInstanceUserEndpointsRequestRequestTypeDef = TypedDict(
    "ListAppInstanceUserEndpointsRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "ListAppInstanceUsersRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAppInstancesRequestRequestTypeDef = TypedDict(
    "ListAppInstancesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAppInstanceRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
    },
)
UpdateAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "Name": NotRequired[str],
        "AllowMessages": NotRequired[AllowMessagesType],
    },
)
UpdateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
    },
)
AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef",
    {
        "Admin": NotRequired[IdentityTypeDef],
    },
)
AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {
        "Admin": NotRequired[IdentityTypeDef],
        "AppInstanceArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)
AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {
        "ChannelRetentionSettings": NotRequired[ChannelRetentionSettingsTypeDef],
    },
)
AppInstanceUserEndpointSummaryTypeDef = TypedDict(
    "AppInstanceUserEndpointSummaryTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[AppInstanceUserEndpointTypeType],
        "AllowMessages": NotRequired[AllowMessagesType],
        "EndpointState": NotRequired[EndpointStateTypeDef],
    },
)
AppInstanceUserEndpointTypeDef = TypedDict(
    "AppInstanceUserEndpointTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[AppInstanceUserEndpointTypeType],
        "ResourceArn": NotRequired[str],
        "EndpointAttributes": NotRequired[EndpointAttributesTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "AllowMessages": NotRequired[AllowMessagesType],
        "EndpointState": NotRequired[EndpointStateTypeDef],
    },
)
RegisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "RegisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Type": AppInstanceUserEndpointTypeType,
        "ResourceArn": str,
        "EndpointAttributes": EndpointAttributesTypeDef,
        "ClientRequestToken": str,
        "Name": NotRequired[str],
        "AllowMessages": NotRequired[AllowMessagesType],
    },
)
AppInstanceUserTypeDef = TypedDict(
    "AppInstanceUserTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "ExpirationSettings": NotRequired[ExpirationSettingsTypeDef],
    },
)
PutAppInstanceUserExpirationSettingsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceUserExpirationSettingsRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "ExpirationSettings": NotRequired[ExpirationSettingsTypeDef],
    },
)
CreateAppInstanceAdminResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": IdentityTypeDef,
        "AppInstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppInstanceBotResponseTypeDef = TypedDict(
    "CreateAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBotArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppInstanceResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppInstanceUserResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAppInstanceResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseTypeDef",
    {
        "AppInstance": AppInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppInstanceBotsResponseTypeDef = TypedDict(
    "ListAppInstanceBotsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceBots": List[AppInstanceBotSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAppInstanceUsersResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List[AppInstanceUserSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAppInstancesResponseTypeDef = TypedDict(
    "ListAppInstancesResponseTypeDef",
    {
        "AppInstances": List[AppInstanceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutAppInstanceUserExpirationSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceUserExpirationSettingsResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ExpirationSettings": ExpirationSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAppInstanceBotResponseTypeDef = TypedDict(
    "UpdateAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBotArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAppInstanceResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAppInstanceUserResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppInstanceRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUserId": str,
        "Name": str,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ExpirationSettings": NotRequired[ExpirationSettingsTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
LexConfigurationTypeDef = TypedDict(
    "LexConfigurationTypeDef",
    {
        "LexBotAliasArn": str,
        "LocaleId": str,
        "RespondsTo": NotRequired[Literal["STANDARD_MESSAGES"]],
        "InvokedBy": NotRequired[InvokedByTypeDef],
        "WelcomeIntent": NotRequired[str],
    },
)
ListAppInstanceAdminsResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List[AppInstanceAdminSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeAppInstanceAdminResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": AppInstanceAdminTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsTypeDef,
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsTypeDef,
    },
)
PutAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsTypeDef,
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppInstanceUserEndpointsResponseTypeDef = TypedDict(
    "ListAppInstanceUserEndpointsResponseTypeDef",
    {
        "AppInstanceUserEndpoints": List[AppInstanceUserEndpointSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserEndpoint": AppInstanceUserEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUser": AppInstanceUserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Lex": LexConfigurationTypeDef,
    },
)
AppInstanceBotTypeDef = TypedDict(
    "AppInstanceBotTypeDef",
    {
        "AppInstanceBotArn": NotRequired[str],
        "Name": NotRequired[str],
        "Configuration": NotRequired[ConfigurationTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Metadata": NotRequired[str],
    },
)
CreateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "ClientRequestToken": str,
        "Configuration": ConfigurationTypeDef,
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
        "Name": str,
        "Metadata": str,
        "Configuration": NotRequired[ConfigurationTypeDef],
    },
)
DescribeAppInstanceBotResponseTypeDef = TypedDict(
    "DescribeAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBot": AppInstanceBotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
