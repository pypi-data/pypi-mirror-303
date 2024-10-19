"""
Type annotations for securitylake service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/type_defs/)

Usage::

    ```python
    from mypy_boto3_securitylake.type_defs import AwsIdentityTypeDef

    data: AwsIdentityTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AccessTypeType,
    AwsLogSourceNameType,
    DataLakeStatusType,
    HttpMethodType,
    SourceCollectionStatusType,
    SubscriberStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AwsIdentityTypeDef",
    "AwsLogSourceConfigurationTypeDef",
    "AwsLogSourceResourceTypeDef",
    "ResponseMetadataTypeDef",
    "CreateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    "TagTypeDef",
    "CustomLogSourceAttributesTypeDef",
    "CustomLogSourceCrawlerConfigurationTypeDef",
    "CustomLogSourceProviderTypeDef",
    "DataLakeEncryptionConfigurationTypeDef",
    "DataLakeExceptionTypeDef",
    "DataLakeLifecycleExpirationTypeDef",
    "DataLakeLifecycleTransitionTypeDef",
    "DataLakeReplicationConfigurationOutputTypeDef",
    "DataLakeReplicationConfigurationTypeDef",
    "DataLakeSourceStatusTypeDef",
    "DataLakeUpdateExceptionTypeDef",
    "DeleteCustomLogSourceRequestRequestTypeDef",
    "DeleteDataLakeRequestRequestTypeDef",
    "DeleteSubscriberNotificationRequestRequestTypeDef",
    "DeleteSubscriberRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetDataLakeSourcesRequestRequestTypeDef",
    "GetSubscriberRequestRequestTypeDef",
    "HttpsNotificationConfigurationTypeDef",
    "ListDataLakeExceptionsRequestRequestTypeDef",
    "ListDataLakesRequestRequestTypeDef",
    "ListSubscribersRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    "CreateAwsLogSourceRequestRequestTypeDef",
    "DeleteAwsLogSourceRequestRequestTypeDef",
    "DataLakeAutoEnableNewAccountConfigurationOutputTypeDef",
    "DataLakeAutoEnableNewAccountConfigurationTypeDef",
    "CreateAwsLogSourceResponseTypeDef",
    "CreateSubscriberNotificationResponseTypeDef",
    "DeleteAwsLogSourceResponseTypeDef",
    "GetDataLakeExceptionSubscriptionResponseTypeDef",
    "UpdateSubscriberNotificationResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CustomLogSourceConfigurationTypeDef",
    "CustomLogSourceResourceTypeDef",
    "ListDataLakeExceptionsResponseTypeDef",
    "DataLakeLifecycleConfigurationOutputTypeDef",
    "DataLakeLifecycleConfigurationTypeDef",
    "DataLakeReplicationConfigurationUnionTypeDef",
    "DataLakeSourceTypeDef",
    "DataLakeUpdateStatusTypeDef",
    "GetDataLakeSourcesRequestGetDataLakeSourcesPaginateTypeDef",
    "ListDataLakeExceptionsRequestListDataLakeExceptionsPaginateTypeDef",
    "ListSubscribersRequestListSubscribersPaginateTypeDef",
    "NotificationConfigurationTypeDef",
    "GetDataLakeOrganizationConfigurationResponseTypeDef",
    "DataLakeAutoEnableNewAccountConfigurationUnionTypeDef",
    "DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef",
    "CreateCustomLogSourceRequestRequestTypeDef",
    "CreateCustomLogSourceResponseTypeDef",
    "LogSourceResourceTypeDef",
    "DataLakeLifecycleConfigurationUnionTypeDef",
    "GetDataLakeSourcesResponseTypeDef",
    "DataLakeResourceTypeDef",
    "CreateSubscriberNotificationRequestRequestTypeDef",
    "UpdateSubscriberNotificationRequestRequestTypeDef",
    "CreateDataLakeOrganizationConfigurationRequestRequestTypeDef",
    "CreateSubscriberRequestRequestTypeDef",
    "ListLogSourcesRequestListLogSourcesPaginateTypeDef",
    "ListLogSourcesRequestRequestTypeDef",
    "LogSourceTypeDef",
    "SubscriberResourceTypeDef",
    "UpdateSubscriberRequestRequestTypeDef",
    "DataLakeConfigurationTypeDef",
    "CreateDataLakeResponseTypeDef",
    "ListDataLakesResponseTypeDef",
    "UpdateDataLakeResponseTypeDef",
    "ListLogSourcesResponseTypeDef",
    "CreateSubscriberResponseTypeDef",
    "GetSubscriberResponseTypeDef",
    "ListSubscribersResponseTypeDef",
    "UpdateSubscriberResponseTypeDef",
    "CreateDataLakeRequestRequestTypeDef",
    "UpdateDataLakeRequestRequestTypeDef",
)

AwsIdentityTypeDef = TypedDict(
    "AwsIdentityTypeDef",
    {
        "externalId": str,
        "principal": str,
    },
)
AwsLogSourceConfigurationTypeDef = TypedDict(
    "AwsLogSourceConfigurationTypeDef",
    {
        "regions": Sequence[str],
        "sourceName": AwsLogSourceNameType,
        "accounts": NotRequired[Sequence[str]],
        "sourceVersion": NotRequired[str],
    },
)
AwsLogSourceResourceTypeDef = TypedDict(
    "AwsLogSourceResourceTypeDef",
    {
        "sourceName": NotRequired[AwsLogSourceNameType],
        "sourceVersion": NotRequired[str],
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
CreateDataLakeExceptionSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    {
        "notificationEndpoint": str,
        "subscriptionProtocol": str,
        "exceptionTimeToLive": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
CustomLogSourceAttributesTypeDef = TypedDict(
    "CustomLogSourceAttributesTypeDef",
    {
        "crawlerArn": NotRequired[str],
        "databaseArn": NotRequired[str],
        "tableArn": NotRequired[str],
    },
)
CustomLogSourceCrawlerConfigurationTypeDef = TypedDict(
    "CustomLogSourceCrawlerConfigurationTypeDef",
    {
        "roleArn": str,
    },
)
CustomLogSourceProviderTypeDef = TypedDict(
    "CustomLogSourceProviderTypeDef",
    {
        "location": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
DataLakeEncryptionConfigurationTypeDef = TypedDict(
    "DataLakeEncryptionConfigurationTypeDef",
    {
        "kmsKeyId": NotRequired[str],
    },
)
DataLakeExceptionTypeDef = TypedDict(
    "DataLakeExceptionTypeDef",
    {
        "exception": NotRequired[str],
        "region": NotRequired[str],
        "remediation": NotRequired[str],
        "timestamp": NotRequired[datetime],
    },
)
DataLakeLifecycleExpirationTypeDef = TypedDict(
    "DataLakeLifecycleExpirationTypeDef",
    {
        "days": NotRequired[int],
    },
)
DataLakeLifecycleTransitionTypeDef = TypedDict(
    "DataLakeLifecycleTransitionTypeDef",
    {
        "days": NotRequired[int],
        "storageClass": NotRequired[str],
    },
)
DataLakeReplicationConfigurationOutputTypeDef = TypedDict(
    "DataLakeReplicationConfigurationOutputTypeDef",
    {
        "regions": NotRequired[List[str]],
        "roleArn": NotRequired[str],
    },
)
DataLakeReplicationConfigurationTypeDef = TypedDict(
    "DataLakeReplicationConfigurationTypeDef",
    {
        "regions": NotRequired[Sequence[str]],
        "roleArn": NotRequired[str],
    },
)
DataLakeSourceStatusTypeDef = TypedDict(
    "DataLakeSourceStatusTypeDef",
    {
        "resource": NotRequired[str],
        "status": NotRequired[SourceCollectionStatusType],
    },
)
DataLakeUpdateExceptionTypeDef = TypedDict(
    "DataLakeUpdateExceptionTypeDef",
    {
        "code": NotRequired[str],
        "reason": NotRequired[str],
    },
)
DeleteCustomLogSourceRequestRequestTypeDef = TypedDict(
    "DeleteCustomLogSourceRequestRequestTypeDef",
    {
        "sourceName": str,
        "sourceVersion": NotRequired[str],
    },
)
DeleteDataLakeRequestRequestTypeDef = TypedDict(
    "DeleteDataLakeRequestRequestTypeDef",
    {
        "regions": Sequence[str],
    },
)
DeleteSubscriberNotificationRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberNotificationRequestRequestTypeDef",
    {
        "subscriberId": str,
    },
)
DeleteSubscriberRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberRequestRequestTypeDef",
    {
        "subscriberId": str,
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
GetDataLakeSourcesRequestRequestTypeDef = TypedDict(
    "GetDataLakeSourcesRequestRequestTypeDef",
    {
        "accounts": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetSubscriberRequestRequestTypeDef = TypedDict(
    "GetSubscriberRequestRequestTypeDef",
    {
        "subscriberId": str,
    },
)
HttpsNotificationConfigurationTypeDef = TypedDict(
    "HttpsNotificationConfigurationTypeDef",
    {
        "endpoint": str,
        "targetRoleArn": str,
        "authorizationApiKeyName": NotRequired[str],
        "authorizationApiKeyValue": NotRequired[str],
        "httpMethod": NotRequired[HttpMethodType],
    },
)
ListDataLakeExceptionsRequestRequestTypeDef = TypedDict(
    "ListDataLakeExceptionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "regions": NotRequired[Sequence[str]],
    },
)
ListDataLakesRequestRequestTypeDef = TypedDict(
    "ListDataLakesRequestRequestTypeDef",
    {
        "regions": NotRequired[Sequence[str]],
    },
)
ListSubscribersRequestRequestTypeDef = TypedDict(
    "ListSubscribersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef = TypedDict(
    "RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef",
    {
        "accountId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateDataLakeExceptionSubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    {
        "notificationEndpoint": str,
        "subscriptionProtocol": str,
        "exceptionTimeToLive": NotRequired[int],
    },
)
CreateAwsLogSourceRequestRequestTypeDef = TypedDict(
    "CreateAwsLogSourceRequestRequestTypeDef",
    {
        "sources": Sequence[AwsLogSourceConfigurationTypeDef],
    },
)
DeleteAwsLogSourceRequestRequestTypeDef = TypedDict(
    "DeleteAwsLogSourceRequestRequestTypeDef",
    {
        "sources": Sequence[AwsLogSourceConfigurationTypeDef],
    },
)
DataLakeAutoEnableNewAccountConfigurationOutputTypeDef = TypedDict(
    "DataLakeAutoEnableNewAccountConfigurationOutputTypeDef",
    {
        "region": str,
        "sources": List[AwsLogSourceResourceTypeDef],
    },
)
DataLakeAutoEnableNewAccountConfigurationTypeDef = TypedDict(
    "DataLakeAutoEnableNewAccountConfigurationTypeDef",
    {
        "region": str,
        "sources": Sequence[AwsLogSourceResourceTypeDef],
    },
)
CreateAwsLogSourceResponseTypeDef = TypedDict(
    "CreateAwsLogSourceResponseTypeDef",
    {
        "failed": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriberNotificationResponseTypeDef = TypedDict(
    "CreateSubscriberNotificationResponseTypeDef",
    {
        "subscriberEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAwsLogSourceResponseTypeDef = TypedDict(
    "DeleteAwsLogSourceResponseTypeDef",
    {
        "failed": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataLakeExceptionSubscriptionResponseTypeDef = TypedDict(
    "GetDataLakeExceptionSubscriptionResponseTypeDef",
    {
        "exceptionTimeToLive": int,
        "notificationEndpoint": str,
        "subscriptionProtocol": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSubscriberNotificationResponseTypeDef = TypedDict(
    "UpdateSubscriberNotificationResponseTypeDef",
    {
        "subscriberEndpoint": str,
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
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CustomLogSourceConfigurationTypeDef = TypedDict(
    "CustomLogSourceConfigurationTypeDef",
    {
        "crawlerConfiguration": CustomLogSourceCrawlerConfigurationTypeDef,
        "providerIdentity": AwsIdentityTypeDef,
    },
)
CustomLogSourceResourceTypeDef = TypedDict(
    "CustomLogSourceResourceTypeDef",
    {
        "attributes": NotRequired[CustomLogSourceAttributesTypeDef],
        "provider": NotRequired[CustomLogSourceProviderTypeDef],
        "sourceName": NotRequired[str],
        "sourceVersion": NotRequired[str],
    },
)
ListDataLakeExceptionsResponseTypeDef = TypedDict(
    "ListDataLakeExceptionsResponseTypeDef",
    {
        "exceptions": List[DataLakeExceptionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataLakeLifecycleConfigurationOutputTypeDef = TypedDict(
    "DataLakeLifecycleConfigurationOutputTypeDef",
    {
        "expiration": NotRequired[DataLakeLifecycleExpirationTypeDef],
        "transitions": NotRequired[List[DataLakeLifecycleTransitionTypeDef]],
    },
)
DataLakeLifecycleConfigurationTypeDef = TypedDict(
    "DataLakeLifecycleConfigurationTypeDef",
    {
        "expiration": NotRequired[DataLakeLifecycleExpirationTypeDef],
        "transitions": NotRequired[Sequence[DataLakeLifecycleTransitionTypeDef]],
    },
)
DataLakeReplicationConfigurationUnionTypeDef = Union[
    DataLakeReplicationConfigurationTypeDef, DataLakeReplicationConfigurationOutputTypeDef
]
DataLakeSourceTypeDef = TypedDict(
    "DataLakeSourceTypeDef",
    {
        "account": NotRequired[str],
        "eventClasses": NotRequired[List[str]],
        "sourceName": NotRequired[str],
        "sourceStatuses": NotRequired[List[DataLakeSourceStatusTypeDef]],
    },
)
DataLakeUpdateStatusTypeDef = TypedDict(
    "DataLakeUpdateStatusTypeDef",
    {
        "exception": NotRequired[DataLakeUpdateExceptionTypeDef],
        "requestId": NotRequired[str],
        "status": NotRequired[DataLakeStatusType],
    },
)
GetDataLakeSourcesRequestGetDataLakeSourcesPaginateTypeDef = TypedDict(
    "GetDataLakeSourcesRequestGetDataLakeSourcesPaginateTypeDef",
    {
        "accounts": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataLakeExceptionsRequestListDataLakeExceptionsPaginateTypeDef = TypedDict(
    "ListDataLakeExceptionsRequestListDataLakeExceptionsPaginateTypeDef",
    {
        "regions": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscribersRequestListSubscribersPaginateTypeDef = TypedDict(
    "ListSubscribersRequestListSubscribersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "httpsNotificationConfiguration": NotRequired[HttpsNotificationConfigurationTypeDef],
        "sqsNotificationConfiguration": NotRequired[Mapping[str, Any]],
    },
)
GetDataLakeOrganizationConfigurationResponseTypeDef = TypedDict(
    "GetDataLakeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnableNewAccount": List[DataLakeAutoEnableNewAccountConfigurationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataLakeAutoEnableNewAccountConfigurationUnionTypeDef = Union[
    DataLakeAutoEnableNewAccountConfigurationTypeDef,
    DataLakeAutoEnableNewAccountConfigurationOutputTypeDef,
]
DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnableNewAccount": NotRequired[
            Sequence[DataLakeAutoEnableNewAccountConfigurationTypeDef]
        ],
    },
)
CreateCustomLogSourceRequestRequestTypeDef = TypedDict(
    "CreateCustomLogSourceRequestRequestTypeDef",
    {
        "configuration": CustomLogSourceConfigurationTypeDef,
        "sourceName": str,
        "eventClasses": NotRequired[Sequence[str]],
        "sourceVersion": NotRequired[str],
    },
)
CreateCustomLogSourceResponseTypeDef = TypedDict(
    "CreateCustomLogSourceResponseTypeDef",
    {
        "source": CustomLogSourceResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LogSourceResourceTypeDef = TypedDict(
    "LogSourceResourceTypeDef",
    {
        "awsLogSource": NotRequired[AwsLogSourceResourceTypeDef],
        "customLogSource": NotRequired[CustomLogSourceResourceTypeDef],
    },
)
DataLakeLifecycleConfigurationUnionTypeDef = Union[
    DataLakeLifecycleConfigurationTypeDef, DataLakeLifecycleConfigurationOutputTypeDef
]
GetDataLakeSourcesResponseTypeDef = TypedDict(
    "GetDataLakeSourcesResponseTypeDef",
    {
        "dataLakeArn": str,
        "dataLakeSources": List[DataLakeSourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataLakeResourceTypeDef = TypedDict(
    "DataLakeResourceTypeDef",
    {
        "dataLakeArn": str,
        "region": str,
        "createStatus": NotRequired[DataLakeStatusType],
        "encryptionConfiguration": NotRequired[DataLakeEncryptionConfigurationTypeDef],
        "lifecycleConfiguration": NotRequired[DataLakeLifecycleConfigurationOutputTypeDef],
        "replicationConfiguration": NotRequired[DataLakeReplicationConfigurationOutputTypeDef],
        "s3BucketArn": NotRequired[str],
        "updateStatus": NotRequired[DataLakeUpdateStatusTypeDef],
    },
)
CreateSubscriberNotificationRequestRequestTypeDef = TypedDict(
    "CreateSubscriberNotificationRequestRequestTypeDef",
    {
        "configuration": NotificationConfigurationTypeDef,
        "subscriberId": str,
    },
)
UpdateSubscriberNotificationRequestRequestTypeDef = TypedDict(
    "UpdateSubscriberNotificationRequestRequestTypeDef",
    {
        "configuration": NotificationConfigurationTypeDef,
        "subscriberId": str,
    },
)
CreateDataLakeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "CreateDataLakeOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnableNewAccount": NotRequired[
            Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef]
        ],
    },
)
CreateSubscriberRequestRequestTypeDef = TypedDict(
    "CreateSubscriberRequestRequestTypeDef",
    {
        "sources": Sequence[LogSourceResourceTypeDef],
        "subscriberIdentity": AwsIdentityTypeDef,
        "subscriberName": str,
        "accessTypes": NotRequired[Sequence[AccessTypeType]],
        "subscriberDescription": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListLogSourcesRequestListLogSourcesPaginateTypeDef = TypedDict(
    "ListLogSourcesRequestListLogSourcesPaginateTypeDef",
    {
        "accounts": NotRequired[Sequence[str]],
        "regions": NotRequired[Sequence[str]],
        "sources": NotRequired[Sequence[LogSourceResourceTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLogSourcesRequestRequestTypeDef = TypedDict(
    "ListLogSourcesRequestRequestTypeDef",
    {
        "accounts": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "regions": NotRequired[Sequence[str]],
        "sources": NotRequired[Sequence[LogSourceResourceTypeDef]],
    },
)
LogSourceTypeDef = TypedDict(
    "LogSourceTypeDef",
    {
        "account": NotRequired[str],
        "region": NotRequired[str],
        "sources": NotRequired[List[LogSourceResourceTypeDef]],
    },
)
SubscriberResourceTypeDef = TypedDict(
    "SubscriberResourceTypeDef",
    {
        "sources": List[LogSourceResourceTypeDef],
        "subscriberArn": str,
        "subscriberId": str,
        "subscriberIdentity": AwsIdentityTypeDef,
        "subscriberName": str,
        "accessTypes": NotRequired[List[AccessTypeType]],
        "createdAt": NotRequired[datetime],
        "resourceShareArn": NotRequired[str],
        "resourceShareName": NotRequired[str],
        "roleArn": NotRequired[str],
        "s3BucketArn": NotRequired[str],
        "subscriberDescription": NotRequired[str],
        "subscriberEndpoint": NotRequired[str],
        "subscriberStatus": NotRequired[SubscriberStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
UpdateSubscriberRequestRequestTypeDef = TypedDict(
    "UpdateSubscriberRequestRequestTypeDef",
    {
        "subscriberId": str,
        "sources": NotRequired[Sequence[LogSourceResourceTypeDef]],
        "subscriberDescription": NotRequired[str],
        "subscriberIdentity": NotRequired[AwsIdentityTypeDef],
        "subscriberName": NotRequired[str],
    },
)
DataLakeConfigurationTypeDef = TypedDict(
    "DataLakeConfigurationTypeDef",
    {
        "region": str,
        "encryptionConfiguration": NotRequired[DataLakeEncryptionConfigurationTypeDef],
        "lifecycleConfiguration": NotRequired[DataLakeLifecycleConfigurationUnionTypeDef],
        "replicationConfiguration": NotRequired[DataLakeReplicationConfigurationUnionTypeDef],
    },
)
CreateDataLakeResponseTypeDef = TypedDict(
    "CreateDataLakeResponseTypeDef",
    {
        "dataLakes": List[DataLakeResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataLakesResponseTypeDef = TypedDict(
    "ListDataLakesResponseTypeDef",
    {
        "dataLakes": List[DataLakeResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataLakeResponseTypeDef = TypedDict(
    "UpdateDataLakeResponseTypeDef",
    {
        "dataLakes": List[DataLakeResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLogSourcesResponseTypeDef = TypedDict(
    "ListLogSourcesResponseTypeDef",
    {
        "nextToken": str,
        "sources": List[LogSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriberResponseTypeDef = TypedDict(
    "CreateSubscriberResponseTypeDef",
    {
        "subscriber": SubscriberResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriberResponseTypeDef = TypedDict(
    "GetSubscriberResponseTypeDef",
    {
        "subscriber": SubscriberResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscribersResponseTypeDef = TypedDict(
    "ListSubscribersResponseTypeDef",
    {
        "nextToken": str,
        "subscribers": List[SubscriberResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSubscriberResponseTypeDef = TypedDict(
    "UpdateSubscriberResponseTypeDef",
    {
        "subscriber": SubscriberResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataLakeRequestRequestTypeDef = TypedDict(
    "CreateDataLakeRequestRequestTypeDef",
    {
        "configurations": Sequence[DataLakeConfigurationTypeDef],
        "metaStoreManagerRoleArn": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateDataLakeRequestRequestTypeDef = TypedDict(
    "UpdateDataLakeRequestRequestTypeDef",
    {
        "configurations": Sequence[DataLakeConfigurationTypeDef],
        "metaStoreManagerRoleArn": NotRequired[str],
    },
)
