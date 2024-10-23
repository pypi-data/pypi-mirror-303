"""
Type annotations for finspace-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_finspace_data.type_defs import AssociateUserToPermissionGroupRequestRequestTypeDef

    data: AssociateUserToPermissionGroupRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ApiAccessType,
    ApplicationPermissionType,
    ChangeTypeType,
    ColumnDataTypeType,
    DatasetKindType,
    DatasetStatusType,
    DataViewStatusType,
    ErrorCategoryType,
    ExportFileFormatType,
    IngestionStatusType,
    LocationTypeType,
    PermissionGroupMembershipStatusType,
    UserStatusType,
    UserTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AssociateUserToPermissionGroupRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AwsCredentialsTypeDef",
    "ChangesetErrorInfoTypeDef",
    "ColumnDefinitionTypeDef",
    "CreateChangesetRequestRequestTypeDef",
    "DataViewDestinationTypeParamsTypeDef",
    "DatasetOwnerInfoTypeDef",
    "CreatePermissionGroupRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CredentialsTypeDef",
    "DataViewDestinationTypeParamsOutputTypeDef",
    "DataViewErrorInfoTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeletePermissionGroupRequestRequestTypeDef",
    "DisableUserRequestRequestTypeDef",
    "DisassociateUserFromPermissionGroupRequestRequestTypeDef",
    "EnableUserRequestRequestTypeDef",
    "GetChangesetRequestRequestTypeDef",
    "GetDataViewRequestRequestTypeDef",
    "GetDatasetRequestRequestTypeDef",
    "GetExternalDataViewAccessDetailsRequestRequestTypeDef",
    "S3LocationTypeDef",
    "GetPermissionGroupRequestRequestTypeDef",
    "PermissionGroupTypeDef",
    "GetProgrammaticAccessCredentialsRequestRequestTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetWorkingLocationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListChangesetsRequestRequestTypeDef",
    "ListDataViewsRequestRequestTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListPermissionGroupsByUserRequestRequestTypeDef",
    "PermissionGroupByUserTypeDef",
    "ListPermissionGroupsRequestRequestTypeDef",
    "ListUsersByPermissionGroupRequestRequestTypeDef",
    "UserByPermissionGroupTypeDef",
    "ListUsersRequestRequestTypeDef",
    "UserTypeDef",
    "ResourcePermissionTypeDef",
    "ResetUserPasswordRequestRequestTypeDef",
    "UpdateChangesetRequestRequestTypeDef",
    "UpdatePermissionGroupRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "AssociateUserToPermissionGroupResponseTypeDef",
    "CreateChangesetResponseTypeDef",
    "CreateDataViewResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreatePermissionGroupResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeletePermissionGroupResponseTypeDef",
    "DisableUserResponseTypeDef",
    "DisassociateUserFromPermissionGroupResponseTypeDef",
    "EnableUserResponseTypeDef",
    "GetUserResponseTypeDef",
    "GetWorkingLocationResponseTypeDef",
    "ResetUserPasswordResponseTypeDef",
    "UpdateChangesetResponseTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdatePermissionGroupResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "ChangesetSummaryTypeDef",
    "GetChangesetResponseTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "CreateDataViewRequestRequestTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "DataViewSummaryTypeDef",
    "GetDataViewResponseTypeDef",
    "GetExternalDataViewAccessDetailsResponseTypeDef",
    "GetPermissionGroupResponseTypeDef",
    "ListPermissionGroupsResponseTypeDef",
    "ListChangesetsRequestListChangesetsPaginateTypeDef",
    "ListDataViewsRequestListDataViewsPaginateTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListPermissionGroupsByUserResponseTypeDef",
    "ListUsersByPermissionGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PermissionGroupParamsTypeDef",
    "ListChangesetsResponseTypeDef",
    "SchemaUnionOutputTypeDef",
    "SchemaDefinitionUnionTypeDef",
    "ListDataViewsResponseTypeDef",
    "DatasetTypeDef",
    "GetDatasetResponseTypeDef",
    "SchemaUnionTypeDef",
    "ListDatasetsResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
)

AssociateUserToPermissionGroupRequestRequestTypeDef = TypedDict(
    "AssociateUserToPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "userId": str,
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
AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "secretAccessKey": NotRequired[str],
        "sessionToken": NotRequired[str],
        "expiration": NotRequired[int],
    },
)
ChangesetErrorInfoTypeDef = TypedDict(
    "ChangesetErrorInfoTypeDef",
    {
        "errorMessage": NotRequired[str],
        "errorCategory": NotRequired[ErrorCategoryType],
    },
)
ColumnDefinitionTypeDef = TypedDict(
    "ColumnDefinitionTypeDef",
    {
        "dataType": NotRequired[ColumnDataTypeType],
        "columnName": NotRequired[str],
        "columnDescription": NotRequired[str],
    },
)
CreateChangesetRequestRequestTypeDef = TypedDict(
    "CreateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Mapping[str, str],
        "formatParams": Mapping[str, str],
        "clientToken": NotRequired[str],
    },
)
DataViewDestinationTypeParamsTypeDef = TypedDict(
    "DataViewDestinationTypeParamsTypeDef",
    {
        "destinationType": str,
        "s3DestinationExportFileFormat": NotRequired[ExportFileFormatType],
        "s3DestinationExportFileFormatOptions": NotRequired[Mapping[str, str]],
    },
)
DatasetOwnerInfoTypeDef = TypedDict(
    "DatasetOwnerInfoTypeDef",
    {
        "name": NotRequired[str],
        "phoneNumber": NotRequired[str],
        "email": NotRequired[str],
    },
)
CreatePermissionGroupRequestRequestTypeDef = TypedDict(
    "CreatePermissionGroupRequestRequestTypeDef",
    {
        "name": str,
        "applicationPermissions": Sequence[ApplicationPermissionType],
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "emailAddress": str,
        "type": UserTypeType,
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "secretAccessKey": NotRequired[str],
        "sessionToken": NotRequired[str],
    },
)
DataViewDestinationTypeParamsOutputTypeDef = TypedDict(
    "DataViewDestinationTypeParamsOutputTypeDef",
    {
        "destinationType": str,
        "s3DestinationExportFileFormat": NotRequired[ExportFileFormatType],
        "s3DestinationExportFileFormatOptions": NotRequired[Dict[str, str]],
    },
)
DataViewErrorInfoTypeDef = TypedDict(
    "DataViewErrorInfoTypeDef",
    {
        "errorMessage": NotRequired[str],
        "errorCategory": NotRequired[ErrorCategoryType],
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
        "clientToken": NotRequired[str],
    },
)
DeletePermissionGroupRequestRequestTypeDef = TypedDict(
    "DeletePermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "clientToken": NotRequired[str],
    },
)
DisableUserRequestRequestTypeDef = TypedDict(
    "DisableUserRequestRequestTypeDef",
    {
        "userId": str,
        "clientToken": NotRequired[str],
    },
)
DisassociateUserFromPermissionGroupRequestRequestTypeDef = TypedDict(
    "DisassociateUserFromPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "userId": str,
        "clientToken": NotRequired[str],
    },
)
EnableUserRequestRequestTypeDef = TypedDict(
    "EnableUserRequestRequestTypeDef",
    {
        "userId": str,
        "clientToken": NotRequired[str],
    },
)
GetChangesetRequestRequestTypeDef = TypedDict(
    "GetChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
    },
)
GetDataViewRequestRequestTypeDef = TypedDict(
    "GetDataViewRequestRequestTypeDef",
    {
        "dataViewId": str,
        "datasetId": str,
    },
)
GetDatasetRequestRequestTypeDef = TypedDict(
    "GetDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)
GetExternalDataViewAccessDetailsRequestRequestTypeDef = TypedDict(
    "GetExternalDataViewAccessDetailsRequestRequestTypeDef",
    {
        "dataViewId": str,
        "datasetId": str,
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
GetPermissionGroupRequestRequestTypeDef = TypedDict(
    "GetPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
    },
)
PermissionGroupTypeDef = TypedDict(
    "PermissionGroupTypeDef",
    {
        "permissionGroupId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "applicationPermissions": NotRequired[List[ApplicationPermissionType]],
        "createTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
        "membershipStatus": NotRequired[PermissionGroupMembershipStatusType],
    },
)
GetProgrammaticAccessCredentialsRequestRequestTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsRequestRequestTypeDef",
    {
        "environmentId": str,
        "durationInMinutes": NotRequired[int],
    },
)
GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)
GetWorkingLocationRequestRequestTypeDef = TypedDict(
    "GetWorkingLocationRequestRequestTypeDef",
    {
        "locationType": NotRequired[LocationTypeType],
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
ListChangesetsRequestRequestTypeDef = TypedDict(
    "ListChangesetsRequestRequestTypeDef",
    {
        "datasetId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDataViewsRequestRequestTypeDef = TypedDict(
    "ListDataViewsRequestRequestTypeDef",
    {
        "datasetId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListPermissionGroupsByUserRequestRequestTypeDef = TypedDict(
    "ListPermissionGroupsByUserRequestRequestTypeDef",
    {
        "userId": str,
        "maxResults": int,
        "nextToken": NotRequired[str],
    },
)
PermissionGroupByUserTypeDef = TypedDict(
    "PermissionGroupByUserTypeDef",
    {
        "permissionGroupId": NotRequired[str],
        "name": NotRequired[str],
        "membershipStatus": NotRequired[PermissionGroupMembershipStatusType],
    },
)
ListPermissionGroupsRequestRequestTypeDef = TypedDict(
    "ListPermissionGroupsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": NotRequired[str],
    },
)
ListUsersByPermissionGroupRequestRequestTypeDef = TypedDict(
    "ListUsersByPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "maxResults": int,
        "nextToken": NotRequired[str],
    },
)
UserByPermissionGroupTypeDef = TypedDict(
    "UserByPermissionGroupTypeDef",
    {
        "userId": NotRequired[str],
        "status": NotRequired[UserStatusType],
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "emailAddress": NotRequired[str],
        "type": NotRequired[UserTypeType],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "membershipStatus": NotRequired[PermissionGroupMembershipStatusType],
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": NotRequired[str],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "userId": NotRequired[str],
        "status": NotRequired[UserStatusType],
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "emailAddress": NotRequired[str],
        "type": NotRequired[UserTypeType],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "createTime": NotRequired[int],
        "lastEnabledTime": NotRequired[int],
        "lastDisabledTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
        "lastLoginTime": NotRequired[int],
    },
)
ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "permission": NotRequired[str],
    },
)
ResetUserPasswordRequestRequestTypeDef = TypedDict(
    "ResetUserPasswordRequestRequestTypeDef",
    {
        "userId": str,
        "clientToken": NotRequired[str],
    },
)
UpdateChangesetRequestRequestTypeDef = TypedDict(
    "UpdateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
        "sourceParams": Mapping[str, str],
        "formatParams": Mapping[str, str],
        "clientToken": NotRequired[str],
    },
)
UpdatePermissionGroupRequestRequestTypeDef = TypedDict(
    "UpdatePermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "applicationPermissions": NotRequired[Sequence[ApplicationPermissionType]],
        "clientToken": NotRequired[str],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "userId": str,
        "type": NotRequired[UserTypeType],
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
AssociateUserToPermissionGroupResponseTypeDef = TypedDict(
    "AssociateUserToPermissionGroupResponseTypeDef",
    {
        "statusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChangesetResponseTypeDef = TypedDict(
    "CreateChangesetResponseTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataViewResponseTypeDef = TypedDict(
    "CreateDataViewResponseTypeDef",
    {
        "datasetId": str,
        "dataViewId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePermissionGroupResponseTypeDef = TypedDict(
    "CreatePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePermissionGroupResponseTypeDef = TypedDict(
    "DeletePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableUserResponseTypeDef = TypedDict(
    "DisableUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateUserFromPermissionGroupResponseTypeDef = TypedDict(
    "DisassociateUserFromPermissionGroupResponseTypeDef",
    {
        "statusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableUserResponseTypeDef = TypedDict(
    "EnableUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "userId": str,
        "status": UserStatusType,
        "firstName": str,
        "lastName": str,
        "emailAddress": str,
        "type": UserTypeType,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "createTime": int,
        "lastEnabledTime": int,
        "lastDisabledTime": int,
        "lastModifiedTime": int,
        "lastLoginTime": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkingLocationResponseTypeDef = TypedDict(
    "GetWorkingLocationResponseTypeDef",
    {
        "s3Uri": str,
        "s3Path": str,
        "s3Bucket": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetUserPasswordResponseTypeDef = TypedDict(
    "ResetUserPasswordResponseTypeDef",
    {
        "userId": str,
        "temporaryPassword": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChangesetResponseTypeDef = TypedDict(
    "UpdateChangesetResponseTypeDef",
    {
        "changesetId": str,
        "datasetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePermissionGroupResponseTypeDef = TypedDict(
    "UpdatePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChangesetSummaryTypeDef = TypedDict(
    "ChangesetSummaryTypeDef",
    {
        "changesetId": NotRequired[str],
        "changesetArn": NotRequired[str],
        "datasetId": NotRequired[str],
        "changeType": NotRequired[ChangeTypeType],
        "sourceParams": NotRequired[Dict[str, str]],
        "formatParams": NotRequired[Dict[str, str]],
        "createTime": NotRequired[int],
        "status": NotRequired[IngestionStatusType],
        "errorInfo": NotRequired[ChangesetErrorInfoTypeDef],
        "activeUntilTimestamp": NotRequired[int],
        "activeFromTimestamp": NotRequired[int],
        "updatesChangesetId": NotRequired[str],
        "updatedByChangesetId": NotRequired[str],
    },
)
GetChangesetResponseTypeDef = TypedDict(
    "GetChangesetResponseTypeDef",
    {
        "changesetId": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Dict[str, str],
        "formatParams": Dict[str, str],
        "createTime": int,
        "status": IngestionStatusType,
        "errorInfo": ChangesetErrorInfoTypeDef,
        "activeUntilTimestamp": int,
        "activeFromTimestamp": int,
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SchemaDefinitionOutputTypeDef = TypedDict(
    "SchemaDefinitionOutputTypeDef",
    {
        "columns": NotRequired[List[ColumnDefinitionTypeDef]],
        "primaryKeyColumns": NotRequired[List[str]],
    },
)
SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": NotRequired[Sequence[ColumnDefinitionTypeDef]],
        "primaryKeyColumns": NotRequired[Sequence[str]],
    },
)
CreateDataViewRequestRequestTypeDef = TypedDict(
    "CreateDataViewRequestRequestTypeDef",
    {
        "datasetId": str,
        "destinationTypeParams": DataViewDestinationTypeParamsTypeDef,
        "clientToken": NotRequired[str],
        "autoUpdate": NotRequired[bool],
        "sortColumns": NotRequired[Sequence[str]],
        "partitionColumns": NotRequired[Sequence[str]],
        "asOfTimestamp": NotRequired[int],
    },
)
GetProgrammaticAccessCredentialsResponseTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    {
        "credentials": CredentialsTypeDef,
        "durationInMinutes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataViewSummaryTypeDef = TypedDict(
    "DataViewSummaryTypeDef",
    {
        "dataViewId": NotRequired[str],
        "dataViewArn": NotRequired[str],
        "datasetId": NotRequired[str],
        "asOfTimestamp": NotRequired[int],
        "partitionColumns": NotRequired[List[str]],
        "sortColumns": NotRequired[List[str]],
        "status": NotRequired[DataViewStatusType],
        "errorInfo": NotRequired[DataViewErrorInfoTypeDef],
        "destinationTypeProperties": NotRequired[DataViewDestinationTypeParamsOutputTypeDef],
        "autoUpdate": NotRequired[bool],
        "createTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
    },
)
GetDataViewResponseTypeDef = TypedDict(
    "GetDataViewResponseTypeDef",
    {
        "autoUpdate": bool,
        "partitionColumns": List[str],
        "datasetId": str,
        "asOfTimestamp": int,
        "errorInfo": DataViewErrorInfoTypeDef,
        "lastModifiedTime": int,
        "createTime": int,
        "sortColumns": List[str],
        "dataViewId": str,
        "dataViewArn": str,
        "destinationTypeParams": DataViewDestinationTypeParamsOutputTypeDef,
        "status": DataViewStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExternalDataViewAccessDetailsResponseTypeDef = TypedDict(
    "GetExternalDataViewAccessDetailsResponseTypeDef",
    {
        "credentials": AwsCredentialsTypeDef,
        "s3Location": S3LocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPermissionGroupResponseTypeDef = TypedDict(
    "GetPermissionGroupResponseTypeDef",
    {
        "permissionGroup": PermissionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionGroupsResponseTypeDef = TypedDict(
    "ListPermissionGroupsResponseTypeDef",
    {
        "permissionGroups": List[PermissionGroupTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChangesetsRequestListChangesetsPaginateTypeDef = TypedDict(
    "ListChangesetsRequestListChangesetsPaginateTypeDef",
    {
        "datasetId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataViewsRequestListDataViewsPaginateTypeDef = TypedDict(
    "ListDataViewsRequestListDataViewsPaginateTypeDef",
    {
        "datasetId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef = TypedDict(
    "ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPermissionGroupsByUserResponseTypeDef = TypedDict(
    "ListPermissionGroupsByUserResponseTypeDef",
    {
        "permissionGroups": List[PermissionGroupByUserTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUsersByPermissionGroupResponseTypeDef = TypedDict(
    "ListUsersByPermissionGroupResponseTypeDef",
    {
        "users": List[UserByPermissionGroupTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "users": List[UserTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PermissionGroupParamsTypeDef = TypedDict(
    "PermissionGroupParamsTypeDef",
    {
        "permissionGroupId": NotRequired[str],
        "datasetPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
ListChangesetsResponseTypeDef = TypedDict(
    "ListChangesetsResponseTypeDef",
    {
        "changesets": List[ChangesetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SchemaUnionOutputTypeDef = TypedDict(
    "SchemaUnionOutputTypeDef",
    {
        "tabularSchemaConfig": NotRequired[SchemaDefinitionOutputTypeDef],
    },
)
SchemaDefinitionUnionTypeDef = Union[SchemaDefinitionTypeDef, SchemaDefinitionOutputTypeDef]
ListDataViewsResponseTypeDef = TypedDict(
    "ListDataViewsResponseTypeDef",
    {
        "nextToken": str,
        "dataViews": List[DataViewSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "datasetId": NotRequired[str],
        "datasetArn": NotRequired[str],
        "datasetTitle": NotRequired[str],
        "kind": NotRequired[DatasetKindType],
        "datasetDescription": NotRequired[str],
        "ownerInfo": NotRequired[DatasetOwnerInfoTypeDef],
        "createTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
        "schemaDefinition": NotRequired[SchemaUnionOutputTypeDef],
        "alias": NotRequired[str],
    },
)
GetDatasetResponseTypeDef = TypedDict(
    "GetDatasetResponseTypeDef",
    {
        "datasetId": str,
        "datasetArn": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "datasetDescription": str,
        "createTime": int,
        "lastModifiedTime": int,
        "schemaDefinition": SchemaUnionOutputTypeDef,
        "alias": str,
        "status": DatasetStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SchemaUnionTypeDef = TypedDict(
    "SchemaUnionTypeDef",
    {
        "tabularSchemaConfig": NotRequired[SchemaDefinitionUnionTypeDef],
    },
)
ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasets": List[DatasetTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "datasetTitle": str,
        "kind": DatasetKindType,
        "permissionGroupParams": PermissionGroupParamsTypeDef,
        "clientToken": NotRequired[str],
        "datasetDescription": NotRequired[str],
        "ownerInfo": NotRequired[DatasetOwnerInfoTypeDef],
        "alias": NotRequired[str],
        "schemaDefinition": NotRequired[SchemaUnionTypeDef],
    },
)
UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "clientToken": NotRequired[str],
        "datasetDescription": NotRequired[str],
        "alias": NotRequired[str],
        "schemaDefinition": NotRequired[SchemaUnionTypeDef],
    },
)
