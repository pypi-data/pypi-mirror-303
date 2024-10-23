"""
Type annotations for clouddirectory service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/type_defs/)

Usage::

    ```python
    from mypy_boto3_clouddirectory.type_defs import ObjectReferenceTypeDef

    data: ObjectReferenceTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    BatchReadExceptionTypeType,
    ConsistencyLevelType,
    DirectoryStateType,
    FacetAttributeTypeType,
    FacetStyleType,
    ObjectTypeType,
    RangeModeType,
    RequiredAttributeBehaviorType,
    RuleTypeType,
    UpdateActionTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ObjectReferenceTypeDef",
    "SchemaFacetTypeDef",
    "ApplySchemaRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "AttributeKeyTypeDef",
    "TypedAttributeValueOutputTypeDef",
    "BatchAttachObjectResponseTypeDef",
    "BatchAttachToIndexResponseTypeDef",
    "BatchCreateIndexResponseTypeDef",
    "BatchCreateObjectResponseTypeDef",
    "BatchDetachFromIndexResponseTypeDef",
    "BatchDetachObjectResponseTypeDef",
    "BatchListObjectChildrenResponseTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    "BatchListObjectPoliciesResponseTypeDef",
    "BatchListPolicyAttachmentsResponseTypeDef",
    "BatchReadExceptionTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "BlobTypeDef",
    "CreateDirectoryRequestRequestTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "DeleteDirectoryRequestRequestTypeDef",
    "DeleteFacetRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    "DirectoryTypeDef",
    "DisableDirectoryRequestRequestTypeDef",
    "EnableDirectoryRequestRequestTypeDef",
    "RuleOutputTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetTypeDef",
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    "GetDirectoryRequestRequestTypeDef",
    "GetFacetRequestRequestTypeDef",
    "GetSchemaAsJsonRequestRequestTypeDef",
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAppliedSchemaArnsRequestRequestTypeDef",
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    "ListDirectoriesRequestRequestTypeDef",
    "ListFacetAttributesRequestRequestTypeDef",
    "ListFacetNamesRequestRequestTypeDef",
    "ListManagedSchemaArnsRequestRequestTypeDef",
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListTypedLinkFacetAttributesRequestRequestTypeDef",
    "ListTypedLinkFacetNamesRequestRequestTypeDef",
    "PolicyAttachmentTypeDef",
    "PublishSchemaRequestRequestTypeDef",
    "PutSchemaFromJsonRequestRequestTypeDef",
    "RuleTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSchemaRequestRequestTypeDef",
    "UpgradeAppliedSchemaRequestRequestTypeDef",
    "UpgradePublishedSchemaRequestRequestTypeDef",
    "AttachObjectRequestRequestTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "AttachToIndexRequestRequestTypeDef",
    "BatchAttachObjectTypeDef",
    "BatchAttachPolicyTypeDef",
    "BatchAttachToIndexTypeDef",
    "BatchDeleteObjectTypeDef",
    "BatchDetachFromIndexTypeDef",
    "BatchDetachObjectTypeDef",
    "BatchDetachPolicyTypeDef",
    "BatchGetObjectInformationTypeDef",
    "BatchListAttachedIndicesTypeDef",
    "BatchListObjectChildrenTypeDef",
    "BatchListObjectParentPathsTypeDef",
    "BatchListObjectParentsTypeDef",
    "BatchListObjectPoliciesTypeDef",
    "BatchListPolicyAttachmentsTypeDef",
    "BatchLookupPolicyTypeDef",
    "DeleteObjectRequestRequestTypeDef",
    "DetachFromIndexRequestRequestTypeDef",
    "DetachObjectRequestRequestTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "GetObjectInformationRequestRequestTypeDef",
    "ListAttachedIndicesRequestRequestTypeDef",
    "ListObjectChildrenRequestRequestTypeDef",
    "ListObjectParentPathsRequestRequestTypeDef",
    "ListObjectParentsRequestRequestTypeDef",
    "ListObjectPoliciesRequestRequestTypeDef",
    "ListPolicyAttachmentsRequestRequestTypeDef",
    "LookupPolicyRequestRequestTypeDef",
    "BatchGetObjectAttributesTypeDef",
    "BatchGetObjectInformationResponseTypeDef",
    "BatchListObjectAttributesTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "GetObjectAttributesRequestRequestTypeDef",
    "ListObjectAttributesRequestRequestTypeDef",
    "RemoveFacetFromObjectRequestRequestTypeDef",
    "ApplySchemaResponseTypeDef",
    "AttachObjectResponseTypeDef",
    "AttachToIndexResponseTypeDef",
    "CreateDirectoryResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateObjectResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "DeleteDirectoryResponseTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DetachFromIndexResponseTypeDef",
    "DetachObjectResponseTypeDef",
    "DisableDirectoryResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableDirectoryResponseTypeDef",
    "GetAppliedSchemaVersionResponseTypeDef",
    "GetObjectInformationResponseTypeDef",
    "GetSchemaAsJsonResponseTypeDef",
    "GetTypedLinkFacetInformationResponseTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "ListFacetNamesResponseTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectChildrenResponseTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "PublishSchemaResponseTypeDef",
    "PutSchemaFromJsonResponseTypeDef",
    "UpdateObjectAttributesResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpgradeAppliedSchemaResponseTypeDef",
    "UpgradePublishedSchemaResponseTypeDef",
    "BatchCreateIndexTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "AttributeKeyAndValueOutputTypeDef",
    "AttributeNameAndValueOutputTypeDef",
    "BatchListObjectParentPathsResponseTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "BatchListObjectParentsResponseTypeDef",
    "ListObjectParentsResponseTypeDef",
    "GetDirectoryResponseTypeDef",
    "ListDirectoriesResponseTypeDef",
    "FacetAttributeDefinitionOutputTypeDef",
    "TypedLinkAttributeDefinitionOutputTypeDef",
    "GetFacetResponseTypeDef",
    "ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef",
    "ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef",
    "ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef",
    "ListDirectoriesRequestListDirectoriesPaginateTypeDef",
    "ListFacetAttributesRequestListFacetAttributesPaginateTypeDef",
    "ListFacetNamesRequestListFacetNamesPaginateTypeDef",
    "ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef",
    "ListObjectAttributesRequestListObjectAttributesPaginateTypeDef",
    "ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef",
    "ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef",
    "ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef",
    "ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef",
    "ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef",
    "LookupPolicyRequestLookupPolicyPaginateTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "PolicyToPathTypeDef",
    "RuleUnionTypeDef",
    "TypedAttributeValueTypeDef",
    "BatchGetLinkAttributesResponseTypeDef",
    "BatchGetObjectAttributesResponseTypeDef",
    "BatchListObjectAttributesResponseTypeDef",
    "GetLinkAttributesResponseTypeDef",
    "GetObjectAttributesResponseTypeDef",
    "IndexAttachmentTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "TypedLinkSpecifierOutputTypeDef",
    "FacetAttributeOutputTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "BatchLookupPolicyResponseTypeDef",
    "LookupPolicyResponseTypeDef",
    "TypedAttributeValueUnionTypeDef",
    "BatchListAttachedIndicesResponseTypeDef",
    "BatchListIndexResponseTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListIndexResponseTypeDef",
    "AttachTypedLinkResponseTypeDef",
    "BatchAttachTypedLinkResponseTypeDef",
    "BatchListIncomingTypedLinksResponseTypeDef",
    "BatchListOutgoingTypedLinksResponseTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "AttributeKeyAndValueTypeDef",
    "AttributeNameAndValueTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "LinkAttributeActionTypeDef",
    "ObjectAttributeActionTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "BatchReadSuccessfulResponseTypeDef",
    "AttributeKeyAndValueUnionTypeDef",
    "BatchAddFacetToObjectTypeDef",
    "CreateObjectRequestRequestTypeDef",
    "AttributeNameAndValueUnionTypeDef",
    "FacetAttributeDefinitionUnionTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ObjectAttributeUpdateTypeDef",
    "ObjectAttributeRangeTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "TypedLinkAttributeDefinitionUnionTypeDef",
    "BatchWriteResponseTypeDef",
    "BatchReadOperationResponseTypeDef",
    "AddFacetToObjectRequestRequestTypeDef",
    "BatchCreateObjectTypeDef",
    "AttachTypedLinkRequestRequestTypeDef",
    "BatchAttachTypedLinkTypeDef",
    "TypedLinkSpecifierTypeDef",
    "FacetAttributeTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "UpdateObjectAttributesRequestRequestTypeDef",
    "BatchListIndexTypeDef",
    "ListIndexRequestListIndexPaginateTypeDef",
    "ListIndexRequestRequestTypeDef",
    "BatchListIncomingTypedLinksTypeDef",
    "BatchListOutgoingTypedLinksTypeDef",
    "ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef",
    "ListIncomingTypedLinksRequestRequestTypeDef",
    "ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef",
    "ListOutgoingTypedLinksRequestRequestTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "BatchReadResponseTypeDef",
    "DetachTypedLinkRequestRequestTypeDef",
    "GetLinkAttributesRequestRequestTypeDef",
    "TypedLinkSpecifierUnionTypeDef",
    "UpdateLinkAttributesRequestRequestTypeDef",
    "FacetAttributeUnionTypeDef",
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    "CreateTypedLinkFacetRequestRequestTypeDef",
    "BatchDetachTypedLinkTypeDef",
    "BatchGetLinkAttributesTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "CreateFacetRequestRequestTypeDef",
    "FacetAttributeUpdateTypeDef",
    "BatchReadOperationTypeDef",
    "BatchWriteOperationTypeDef",
    "UpdateFacetRequestRequestTypeDef",
    "BatchReadRequestRequestTypeDef",
    "BatchWriteRequestRequestTypeDef",
)

ObjectReferenceTypeDef = TypedDict(
    "ObjectReferenceTypeDef",
    {
        "Selector": NotRequired[str],
    },
)
SchemaFacetTypeDef = TypedDict(
    "SchemaFacetTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "FacetName": NotRequired[str],
    },
)
ApplySchemaRequestRequestTypeDef = TypedDict(
    "ApplySchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
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
TypedLinkSchemaAndFacetNameTypeDef = TypedDict(
    "TypedLinkSchemaAndFacetNameTypeDef",
    {
        "SchemaArn": str,
        "TypedLinkName": str,
    },
)
AttributeKeyTypeDef = TypedDict(
    "AttributeKeyTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
        "Name": str,
    },
)
TypedAttributeValueOutputTypeDef = TypedDict(
    "TypedAttributeValueOutputTypeDef",
    {
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[bytes],
        "BooleanValue": NotRequired[bool],
        "NumberValue": NotRequired[str],
        "DatetimeValue": NotRequired[datetime],
    },
)
BatchAttachObjectResponseTypeDef = TypedDict(
    "BatchAttachObjectResponseTypeDef",
    {
        "attachedObjectIdentifier": NotRequired[str],
    },
)
BatchAttachToIndexResponseTypeDef = TypedDict(
    "BatchAttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": NotRequired[str],
    },
)
BatchCreateIndexResponseTypeDef = TypedDict(
    "BatchCreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)
BatchCreateObjectResponseTypeDef = TypedDict(
    "BatchCreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)
BatchDetachFromIndexResponseTypeDef = TypedDict(
    "BatchDetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": NotRequired[str],
    },
)
BatchDetachObjectResponseTypeDef = TypedDict(
    "BatchDetachObjectResponseTypeDef",
    {
        "detachedObjectIdentifier": NotRequired[str],
    },
)
BatchListObjectChildrenResponseTypeDef = TypedDict(
    "BatchListObjectChildrenResponseTypeDef",
    {
        "Children": NotRequired[Dict[str, str]],
        "NextToken": NotRequired[str],
    },
)
PathToObjectIdentifiersTypeDef = TypedDict(
    "PathToObjectIdentifiersTypeDef",
    {
        "Path": NotRequired[str],
        "ObjectIdentifiers": NotRequired[List[str]],
    },
)
ObjectIdentifierAndLinkNameTupleTypeDef = TypedDict(
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
        "LinkName": NotRequired[str],
    },
)
BatchListObjectPoliciesResponseTypeDef = TypedDict(
    "BatchListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": NotRequired[List[str]],
        "NextToken": NotRequired[str],
    },
)
BatchListPolicyAttachmentsResponseTypeDef = TypedDict(
    "BatchListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": NotRequired[List[str]],
        "NextToken": NotRequired[str],
    },
)
BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef",
    {
        "Type": NotRequired[BatchReadExceptionTypeType],
        "Message": NotRequired[str],
    },
)
BatchUpdateObjectAttributesResponseTypeDef = TypedDict(
    "BatchUpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CreateDirectoryRequestRequestTypeDef = TypedDict(
    "CreateDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "SchemaArn": str,
    },
)
CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteDirectoryRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
DeleteFacetRequestRequestTypeDef = TypedDict(
    "DeleteFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
DeleteTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
DirectoryTypeDef = TypedDict(
    "DirectoryTypeDef",
    {
        "Name": NotRequired[str],
        "DirectoryArn": NotRequired[str],
        "State": NotRequired[DirectoryStateType],
        "CreationDateTime": NotRequired[datetime],
    },
)
DisableDirectoryRequestRequestTypeDef = TypedDict(
    "DisableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
EnableDirectoryRequestRequestTypeDef = TypedDict(
    "EnableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "Type": NotRequired[RuleTypeType],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
FacetAttributeReferenceTypeDef = TypedDict(
    "FacetAttributeReferenceTypeDef",
    {
        "TargetFacetName": str,
        "TargetAttributeName": str,
    },
)
FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "Name": NotRequired[str],
        "ObjectType": NotRequired[ObjectTypeType],
        "FacetStyle": NotRequired[FacetStyleType],
    },
)
GetAppliedSchemaVersionRequestRequestTypeDef = TypedDict(
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
GetDirectoryRequestRequestTypeDef = TypedDict(
    "GetDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
GetFacetRequestRequestTypeDef = TypedDict(
    "GetFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
GetSchemaAsJsonRequestRequestTypeDef = TypedDict(
    "GetSchemaAsJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
GetTypedLinkFacetInformationRequestRequestTypeDef = TypedDict(
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
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
ListAppliedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListAppliedSchemaArnsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDevelopmentSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDirectoriesRequestRequestTypeDef = TypedDict(
    "ListDirectoriesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "state": NotRequired[DirectoryStateType],
    },
)
ListFacetAttributesRequestRequestTypeDef = TypedDict(
    "ListFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFacetNamesRequestRequestTypeDef = TypedDict(
    "ListFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListManagedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPublishedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ListTypedLinkFacetAttributesRequestRequestTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTypedLinkFacetNamesRequestRequestTypeDef = TypedDict(
    "ListTypedLinkFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PolicyAttachmentTypeDef = TypedDict(
    "PolicyAttachmentTypeDef",
    {
        "PolicyId": NotRequired[str],
        "ObjectIdentifier": NotRequired[str],
        "PolicyType": NotRequired[str],
    },
)
PublishSchemaRequestRequestTypeDef = TypedDict(
    "PublishSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "Version": str,
        "MinorVersion": NotRequired[str],
        "Name": NotRequired[str],
    },
)
PutSchemaFromJsonRequestRequestTypeDef = TypedDict(
    "PutSchemaFromJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Document": str,
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": NotRequired[RuleTypeType],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
TimestampTypeDef = Union[datetime, str]
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateSchemaRequestRequestTypeDef = TypedDict(
    "UpdateSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
UpgradeAppliedSchemaRequestRequestTypeDef = TypedDict(
    "UpgradeAppliedSchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
        "DryRun": NotRequired[bool],
    },
)
UpgradePublishedSchemaRequestRequestTypeDef = TypedDict(
    "UpgradePublishedSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "PublishedSchemaArn": str,
        "MinorVersion": str,
        "DryRun": NotRequired[bool],
    },
)
AttachObjectRequestRequestTypeDef = TypedDict(
    "AttachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": ObjectReferenceTypeDef,
        "ChildReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)
AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
AttachToIndexRequestRequestTypeDef = TypedDict(
    "AttachToIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
BatchAttachObjectTypeDef = TypedDict(
    "BatchAttachObjectTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "ChildReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)
BatchAttachPolicyTypeDef = TypedDict(
    "BatchAttachPolicyTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchAttachToIndexTypeDef = TypedDict(
    "BatchAttachToIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
BatchDeleteObjectTypeDef = TypedDict(
    "BatchDeleteObjectTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchDetachFromIndexTypeDef = TypedDict(
    "BatchDetachFromIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
BatchDetachObjectTypeDef = TypedDict(
    "BatchDetachObjectTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": NotRequired[str],
    },
)
BatchDetachPolicyTypeDef = TypedDict(
    "BatchDetachPolicyTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchGetObjectInformationTypeDef = TypedDict(
    "BatchGetObjectInformationTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchListAttachedIndicesTypeDef = TypedDict(
    "BatchListAttachedIndicesTypeDef",
    {
        "TargetReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListObjectChildrenTypeDef = TypedDict(
    "BatchListObjectChildrenTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListObjectParentPathsTypeDef = TypedDict(
    "BatchListObjectParentPathsTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListObjectParentsTypeDef = TypedDict(
    "BatchListObjectParentsTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListObjectPoliciesTypeDef = TypedDict(
    "BatchListObjectPoliciesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListPolicyAttachmentsTypeDef = TypedDict(
    "BatchListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchLookupPolicyTypeDef = TypedDict(
    "BatchLookupPolicyTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
DetachFromIndexRequestRequestTypeDef = TypedDict(
    "DetachFromIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
DetachObjectRequestRequestTypeDef = TypedDict(
    "DetachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)
DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
GetObjectInformationRequestRequestTypeDef = TypedDict(
    "GetObjectInformationRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListAttachedIndicesRequestRequestTypeDef = TypedDict(
    "ListAttachedIndicesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListObjectChildrenRequestRequestTypeDef = TypedDict(
    "ListObjectChildrenRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListObjectParentPathsRequestRequestTypeDef = TypedDict(
    "ListObjectParentPathsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListObjectParentsRequestRequestTypeDef = TypedDict(
    "ListObjectParentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "IncludeAllLinksToEachParent": NotRequired[bool],
    },
)
ListObjectPoliciesRequestRequestTypeDef = TypedDict(
    "ListObjectPoliciesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListPolicyAttachmentsRequestRequestTypeDef = TypedDict(
    "ListPolicyAttachmentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
LookupPolicyRequestRequestTypeDef = TypedDict(
    "LookupPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchGetObjectAttributesTypeDef = TypedDict(
    "BatchGetObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "SchemaFacet": SchemaFacetTypeDef,
        "AttributeNames": Sequence[str],
    },
)
BatchGetObjectInformationResponseTypeDef = TypedDict(
    "BatchGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": NotRequired[List[SchemaFacetTypeDef]],
        "ObjectIdentifier": NotRequired[str],
    },
)
BatchListObjectAttributesTypeDef = TypedDict(
    "BatchListObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "FacetFilter": NotRequired[SchemaFacetTypeDef],
    },
)
BatchRemoveFacetFromObjectTypeDef = TypedDict(
    "BatchRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
GetObjectAttributesRequestRequestTypeDef = TypedDict(
    "GetObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "SchemaFacet": SchemaFacetTypeDef,
        "AttributeNames": Sequence[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListObjectAttributesRequestRequestTypeDef = TypedDict(
    "ListObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "FacetFilter": NotRequired[SchemaFacetTypeDef],
    },
)
RemoveFacetFromObjectRequestRequestTypeDef = TypedDict(
    "RemoveFacetFromObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
ApplySchemaResponseTypeDef = TypedDict(
    "ApplySchemaResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachObjectResponseTypeDef = TypedDict(
    "AttachObjectResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachToIndexResponseTypeDef = TypedDict(
    "AttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDirectoryResponseTypeDef = TypedDict(
    "CreateDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "Name": str,
        "ObjectIdentifier": str,
        "AppliedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateObjectResponseTypeDef = TypedDict(
    "CreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDirectoryResponseTypeDef = TypedDict(
    "DeleteDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachFromIndexResponseTypeDef = TypedDict(
    "DetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachObjectResponseTypeDef = TypedDict(
    "DetachObjectResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableDirectoryResponseTypeDef = TypedDict(
    "DisableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableDirectoryResponseTypeDef = TypedDict(
    "EnableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "GetAppliedSchemaVersionResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetObjectInformationResponseTypeDef = TypedDict(
    "GetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List[SchemaFacetTypeDef],
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaAsJsonResponseTypeDef = TypedDict(
    "GetSchemaAsJsonResponseTypeDef",
    {
        "Name": str,
        "Document": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "GetTypedLinkFacetInformationResponseTypeDef",
    {
        "IdentityAttributeOrder": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "ListAppliedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFacetNamesResponseTypeDef = TypedDict(
    "ListFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListManagedSchemaArnsResponseTypeDef = TypedDict(
    "ListManagedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListObjectChildrenResponseTypeDef = TypedDict(
    "ListObjectChildrenResponseTypeDef",
    {
        "Children": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListObjectPoliciesResponseTypeDef = TypedDict(
    "ListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPolicyAttachmentsResponseTypeDef = TypedDict(
    "ListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "ListPublishedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PublishSchemaResponseTypeDef = TypedDict(
    "PublishSchemaResponseTypeDef",
    {
        "PublishedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSchemaFromJsonResponseTypeDef = TypedDict(
    "PutSchemaFromJsonResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateObjectAttributesResponseTypeDef = TypedDict(
    "UpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "UpgradeAppliedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpgradePublishedSchemaResponseTypeDef = TypedDict(
    "UpgradePublishedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreateIndexTypeDef = TypedDict(
    "BatchCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": Sequence[AttributeKeyTypeDef],
        "IsUnique": bool,
        "ParentReference": NotRequired[ObjectReferenceTypeDef],
        "LinkName": NotRequired[str],
        "BatchReferenceName": NotRequired[str],
    },
)
CreateIndexRequestRequestTypeDef = TypedDict(
    "CreateIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "OrderedIndexedAttributeList": Sequence[AttributeKeyTypeDef],
        "IsUnique": bool,
        "ParentReference": NotRequired[ObjectReferenceTypeDef],
        "LinkName": NotRequired[str],
    },
)
AttributeKeyAndValueOutputTypeDef = TypedDict(
    "AttributeKeyAndValueOutputTypeDef",
    {
        "Key": AttributeKeyTypeDef,
        "Value": TypedAttributeValueOutputTypeDef,
    },
)
AttributeNameAndValueOutputTypeDef = TypedDict(
    "AttributeNameAndValueOutputTypeDef",
    {
        "AttributeName": str,
        "Value": TypedAttributeValueOutputTypeDef,
    },
)
BatchListObjectParentPathsResponseTypeDef = TypedDict(
    "BatchListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": NotRequired[List[PathToObjectIdentifiersTypeDef]],
        "NextToken": NotRequired[str],
    },
)
ListObjectParentPathsResponseTypeDef = TypedDict(
    "ListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[PathToObjectIdentifiersTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchListObjectParentsResponseTypeDef = TypedDict(
    "BatchListObjectParentsResponseTypeDef",
    {
        "ParentLinks": NotRequired[List[ObjectIdentifierAndLinkNameTupleTypeDef]],
        "NextToken": NotRequired[str],
    },
)
ListObjectParentsResponseTypeDef = TypedDict(
    "ListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "ParentLinks": List[ObjectIdentifierAndLinkNameTupleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDirectoryResponseTypeDef = TypedDict(
    "GetDirectoryResponseTypeDef",
    {
        "Directory": DirectoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDirectoriesResponseTypeDef = TypedDict(
    "ListDirectoriesResponseTypeDef",
    {
        "Directories": List[DirectoryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FacetAttributeDefinitionOutputTypeDef = TypedDict(
    "FacetAttributeDefinitionOutputTypeDef",
    {
        "Type": FacetAttributeTypeType,
        "DefaultValue": NotRequired[TypedAttributeValueOutputTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Dict[str, RuleOutputTypeDef]],
    },
)
TypedLinkAttributeDefinitionOutputTypeDef = TypedDict(
    "TypedLinkAttributeDefinitionOutputTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
        "DefaultValue": NotRequired[TypedAttributeValueOutputTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Dict[str, RuleOutputTypeDef]],
    },
)
GetFacetResponseTypeDef = TypedDict(
    "GetFacetResponseTypeDef",
    {
        "Facet": FacetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef = TypedDict(
    "ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef",
    {
        "DirectoryArn": str,
        "SchemaArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef = TypedDict(
    "ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDirectoriesRequestListDirectoriesPaginateTypeDef = TypedDict(
    "ListDirectoriesRequestListDirectoriesPaginateTypeDef",
    {
        "state": NotRequired[DirectoryStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFacetAttributesRequestListFacetAttributesPaginateTypeDef = TypedDict(
    "ListFacetAttributesRequestListFacetAttributesPaginateTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFacetNamesRequestListFacetNamesPaginateTypeDef = TypedDict(
    "ListFacetNamesRequestListFacetNamesPaginateTypeDef",
    {
        "SchemaArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListObjectAttributesRequestListObjectAttributesPaginateTypeDef = TypedDict(
    "ListObjectAttributesRequestListObjectAttributesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "FacetFilter": NotRequired[SchemaFacetTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef = TypedDict(
    "ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef = TypedDict(
    "ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef = TypedDict(
    "ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef = TypedDict(
    "ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef",
    {
        "SchemaArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LookupPolicyRequestLookupPolicyPaginateTypeDef = TypedDict(
    "LookupPolicyRequestLookupPolicyPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
PolicyToPathTypeDef = TypedDict(
    "PolicyToPathTypeDef",
    {
        "Path": NotRequired[str],
        "Policies": NotRequired[List[PolicyAttachmentTypeDef]],
    },
)
RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]
TypedAttributeValueTypeDef = TypedDict(
    "TypedAttributeValueTypeDef",
    {
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[BlobTypeDef],
        "BooleanValue": NotRequired[bool],
        "NumberValue": NotRequired[str],
        "DatetimeValue": NotRequired[TimestampTypeDef],
    },
)
BatchGetLinkAttributesResponseTypeDef = TypedDict(
    "BatchGetLinkAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List[AttributeKeyAndValueOutputTypeDef]],
    },
)
BatchGetObjectAttributesResponseTypeDef = TypedDict(
    "BatchGetObjectAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List[AttributeKeyAndValueOutputTypeDef]],
    },
)
BatchListObjectAttributesResponseTypeDef = TypedDict(
    "BatchListObjectAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List[AttributeKeyAndValueOutputTypeDef]],
        "NextToken": NotRequired[str],
    },
)
GetLinkAttributesResponseTypeDef = TypedDict(
    "GetLinkAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetObjectAttributesResponseTypeDef = TypedDict(
    "GetObjectAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IndexAttachmentTypeDef = TypedDict(
    "IndexAttachmentTypeDef",
    {
        "IndexedAttributes": NotRequired[List[AttributeKeyAndValueOutputTypeDef]],
        "ObjectIdentifier": NotRequired[str],
    },
)
ListObjectAttributesResponseTypeDef = TypedDict(
    "ListObjectAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TypedLinkSpecifierOutputTypeDef = TypedDict(
    "TypedLinkSpecifierOutputTypeDef",
    {
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "IdentityAttributeValues": List[AttributeNameAndValueOutputTypeDef],
    },
)
FacetAttributeOutputTypeDef = TypedDict(
    "FacetAttributeOutputTypeDef",
    {
        "Name": str,
        "AttributeDefinition": NotRequired[FacetAttributeDefinitionOutputTypeDef],
        "AttributeReference": NotRequired[FacetAttributeReferenceTypeDef],
        "RequiredBehavior": NotRequired[RequiredAttributeBehaviorType],
    },
)
ListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponseTypeDef",
    {
        "Attributes": List[TypedLinkAttributeDefinitionOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchLookupPolicyResponseTypeDef = TypedDict(
    "BatchLookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": NotRequired[List[PolicyToPathTypeDef]],
        "NextToken": NotRequired[str],
    },
)
LookupPolicyResponseTypeDef = TypedDict(
    "LookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List[PolicyToPathTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TypedAttributeValueUnionTypeDef = Union[
    TypedAttributeValueTypeDef, TypedAttributeValueOutputTypeDef
]
BatchListAttachedIndicesResponseTypeDef = TypedDict(
    "BatchListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": NotRequired[List[IndexAttachmentTypeDef]],
        "NextToken": NotRequired[str],
    },
)
BatchListIndexResponseTypeDef = TypedDict(
    "BatchListIndexResponseTypeDef",
    {
        "IndexAttachments": NotRequired[List[IndexAttachmentTypeDef]],
        "NextToken": NotRequired[str],
    },
)
ListAttachedIndicesResponseTypeDef = TypedDict(
    "ListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIndexResponseTypeDef = TypedDict(
    "ListIndexResponseTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AttachTypedLinkResponseTypeDef = TypedDict(
    "AttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchAttachTypedLinkResponseTypeDef = TypedDict(
    "BatchAttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": NotRequired[TypedLinkSpecifierOutputTypeDef],
    },
)
BatchListIncomingTypedLinksResponseTypeDef = TypedDict(
    "BatchListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": NotRequired[List[TypedLinkSpecifierOutputTypeDef]],
        "NextToken": NotRequired[str],
    },
)
BatchListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": NotRequired[List[TypedLinkSpecifierOutputTypeDef]],
        "NextToken": NotRequired[str],
    },
)
ListIncomingTypedLinksResponseTypeDef = TypedDict(
    "ListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List[TypedLinkSpecifierOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List[TypedLinkSpecifierOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFacetAttributesResponseTypeDef = TypedDict(
    "ListFacetAttributesResponseTypeDef",
    {
        "Attributes": List[FacetAttributeOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AttributeKeyAndValueTypeDef = TypedDict(
    "AttributeKeyAndValueTypeDef",
    {
        "Key": AttributeKeyTypeDef,
        "Value": TypedAttributeValueUnionTypeDef,
    },
)
AttributeNameAndValueTypeDef = TypedDict(
    "AttributeNameAndValueTypeDef",
    {
        "AttributeName": str,
        "Value": TypedAttributeValueUnionTypeDef,
    },
)
FacetAttributeDefinitionTypeDef = TypedDict(
    "FacetAttributeDefinitionTypeDef",
    {
        "Type": FacetAttributeTypeType,
        "DefaultValue": NotRequired[TypedAttributeValueUnionTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Mapping[str, RuleUnionTypeDef]],
    },
)
LinkAttributeActionTypeDef = TypedDict(
    "LinkAttributeActionTypeDef",
    {
        "AttributeActionType": NotRequired[UpdateActionTypeType],
        "AttributeUpdateValue": NotRequired[TypedAttributeValueUnionTypeDef],
    },
)
ObjectAttributeActionTypeDef = TypedDict(
    "ObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": NotRequired[UpdateActionTypeType],
        "ObjectAttributeUpdateValue": NotRequired[TypedAttributeValueUnionTypeDef],
    },
)
TypedAttributeValueRangeTypeDef = TypedDict(
    "TypedAttributeValueRangeTypeDef",
    {
        "StartMode": RangeModeType,
        "EndMode": RangeModeType,
        "StartValue": NotRequired[TypedAttributeValueUnionTypeDef],
        "EndValue": NotRequired[TypedAttributeValueUnionTypeDef],
    },
)
TypedLinkAttributeDefinitionTypeDef = TypedDict(
    "TypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
        "DefaultValue": NotRequired[TypedAttributeValueUnionTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Mapping[str, RuleUnionTypeDef]],
    },
)
BatchWriteOperationResponseTypeDef = TypedDict(
    "BatchWriteOperationResponseTypeDef",
    {
        "CreateObject": NotRequired[BatchCreateObjectResponseTypeDef],
        "AttachObject": NotRequired[BatchAttachObjectResponseTypeDef],
        "DetachObject": NotRequired[BatchDetachObjectResponseTypeDef],
        "UpdateObjectAttributes": NotRequired[BatchUpdateObjectAttributesResponseTypeDef],
        "DeleteObject": NotRequired[Dict[str, Any]],
        "AddFacetToObject": NotRequired[Dict[str, Any]],
        "RemoveFacetFromObject": NotRequired[Dict[str, Any]],
        "AttachPolicy": NotRequired[Dict[str, Any]],
        "DetachPolicy": NotRequired[Dict[str, Any]],
        "CreateIndex": NotRequired[BatchCreateIndexResponseTypeDef],
        "AttachToIndex": NotRequired[BatchAttachToIndexResponseTypeDef],
        "DetachFromIndex": NotRequired[BatchDetachFromIndexResponseTypeDef],
        "AttachTypedLink": NotRequired[BatchAttachTypedLinkResponseTypeDef],
        "DetachTypedLink": NotRequired[Dict[str, Any]],
        "UpdateLinkAttributes": NotRequired[Dict[str, Any]],
    },
)
BatchReadSuccessfulResponseTypeDef = TypedDict(
    "BatchReadSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": NotRequired[BatchListObjectAttributesResponseTypeDef],
        "ListObjectChildren": NotRequired[BatchListObjectChildrenResponseTypeDef],
        "GetObjectInformation": NotRequired[BatchGetObjectInformationResponseTypeDef],
        "GetObjectAttributes": NotRequired[BatchGetObjectAttributesResponseTypeDef],
        "ListAttachedIndices": NotRequired[BatchListAttachedIndicesResponseTypeDef],
        "ListObjectParentPaths": NotRequired[BatchListObjectParentPathsResponseTypeDef],
        "ListObjectPolicies": NotRequired[BatchListObjectPoliciesResponseTypeDef],
        "ListPolicyAttachments": NotRequired[BatchListPolicyAttachmentsResponseTypeDef],
        "LookupPolicy": NotRequired[BatchLookupPolicyResponseTypeDef],
        "ListIndex": NotRequired[BatchListIndexResponseTypeDef],
        "ListOutgoingTypedLinks": NotRequired[BatchListOutgoingTypedLinksResponseTypeDef],
        "ListIncomingTypedLinks": NotRequired[BatchListIncomingTypedLinksResponseTypeDef],
        "GetLinkAttributes": NotRequired[BatchGetLinkAttributesResponseTypeDef],
        "ListObjectParents": NotRequired[BatchListObjectParentsResponseTypeDef],
    },
)
AttributeKeyAndValueUnionTypeDef = Union[
    AttributeKeyAndValueTypeDef, AttributeKeyAndValueOutputTypeDef
]
BatchAddFacetToObjectTypeDef = TypedDict(
    "BatchAddFacetToObjectTypeDef",
    {
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectAttributeList": Sequence[AttributeKeyAndValueTypeDef],
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
CreateObjectRequestRequestTypeDef = TypedDict(
    "CreateObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacets": Sequence[SchemaFacetTypeDef],
        "ObjectAttributeList": NotRequired[Sequence[AttributeKeyAndValueTypeDef]],
        "ParentReference": NotRequired[ObjectReferenceTypeDef],
        "LinkName": NotRequired[str],
    },
)
AttributeNameAndValueUnionTypeDef = Union[
    AttributeNameAndValueTypeDef, AttributeNameAndValueOutputTypeDef
]
FacetAttributeDefinitionUnionTypeDef = Union[
    FacetAttributeDefinitionTypeDef, FacetAttributeDefinitionOutputTypeDef
]
LinkAttributeUpdateTypeDef = TypedDict(
    "LinkAttributeUpdateTypeDef",
    {
        "AttributeKey": NotRequired[AttributeKeyTypeDef],
        "AttributeAction": NotRequired[LinkAttributeActionTypeDef],
    },
)
ObjectAttributeUpdateTypeDef = TypedDict(
    "ObjectAttributeUpdateTypeDef",
    {
        "ObjectAttributeKey": NotRequired[AttributeKeyTypeDef],
        "ObjectAttributeAction": NotRequired[ObjectAttributeActionTypeDef],
    },
)
ObjectAttributeRangeTypeDef = TypedDict(
    "ObjectAttributeRangeTypeDef",
    {
        "AttributeKey": NotRequired[AttributeKeyTypeDef],
        "Range": NotRequired[TypedAttributeValueRangeTypeDef],
    },
)
TypedLinkAttributeRangeTypeDef = TypedDict(
    "TypedLinkAttributeRangeTypeDef",
    {
        "Range": TypedAttributeValueRangeTypeDef,
        "AttributeName": NotRequired[str],
    },
)
TypedLinkAttributeDefinitionUnionTypeDef = Union[
    TypedLinkAttributeDefinitionTypeDef, TypedLinkAttributeDefinitionOutputTypeDef
]
BatchWriteResponseTypeDef = TypedDict(
    "BatchWriteResponseTypeDef",
    {
        "Responses": List[BatchWriteOperationResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchReadOperationResponseTypeDef = TypedDict(
    "BatchReadOperationResponseTypeDef",
    {
        "SuccessfulResponse": NotRequired[BatchReadSuccessfulResponseTypeDef],
        "ExceptionResponse": NotRequired[BatchReadExceptionTypeDef],
    },
)
AddFacetToObjectRequestRequestTypeDef = TypedDict(
    "AddFacetToObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
        "ObjectAttributeList": NotRequired[Sequence[AttributeKeyAndValueUnionTypeDef]],
    },
)
BatchCreateObjectTypeDef = TypedDict(
    "BatchCreateObjectTypeDef",
    {
        "SchemaFacet": Sequence[SchemaFacetTypeDef],
        "ObjectAttributeList": Sequence[AttributeKeyAndValueUnionTypeDef],
        "ParentReference": NotRequired[ObjectReferenceTypeDef],
        "LinkName": NotRequired[str],
        "BatchReferenceName": NotRequired[str],
    },
)
AttachTypedLinkRequestRequestTypeDef = TypedDict(
    "AttachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "Attributes": Sequence[AttributeNameAndValueUnionTypeDef],
    },
)
BatchAttachTypedLinkTypeDef = TypedDict(
    "BatchAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "Attributes": Sequence[AttributeNameAndValueUnionTypeDef],
    },
)
TypedLinkSpecifierTypeDef = TypedDict(
    "TypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "IdentityAttributeValues": Sequence[AttributeNameAndValueUnionTypeDef],
    },
)
FacetAttributeTypeDef = TypedDict(
    "FacetAttributeTypeDef",
    {
        "Name": str,
        "AttributeDefinition": NotRequired[FacetAttributeDefinitionUnionTypeDef],
        "AttributeReference": NotRequired[FacetAttributeReferenceTypeDef],
        "RequiredBehavior": NotRequired[RequiredAttributeBehaviorType],
    },
)
BatchUpdateObjectAttributesTypeDef = TypedDict(
    "BatchUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "AttributeUpdates": Sequence[ObjectAttributeUpdateTypeDef],
    },
)
UpdateObjectAttributesRequestRequestTypeDef = TypedDict(
    "UpdateObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "AttributeUpdates": Sequence[ObjectAttributeUpdateTypeDef],
    },
)
BatchListIndexTypeDef = TypedDict(
    "BatchListIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
        "RangesOnIndexedValues": NotRequired[Sequence[ObjectAttributeRangeTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListIndexRequestListIndexPaginateTypeDef = TypedDict(
    "ListIndexRequestListIndexPaginateTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "RangesOnIndexedValues": NotRequired[Sequence[ObjectAttributeRangeTypeDef]],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIndexRequestRequestTypeDef = TypedDict(
    "ListIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "RangesOnIndexedValues": NotRequired[Sequence[ObjectAttributeRangeTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
BatchListIncomingTypedLinksTypeDef = TypedDict(
    "BatchListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListOutgoingTypedLinksTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef = TypedDict(
    "ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIncomingTypedLinksRequestRequestTypeDef = TypedDict(
    "ListIncomingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef = TypedDict(
    "ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOutgoingTypedLinksRequestRequestTypeDef = TypedDict(
    "ListOutgoingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
TypedLinkFacetAttributeUpdateTypeDef = TypedDict(
    "TypedLinkFacetAttributeUpdateTypeDef",
    {
        "Attribute": TypedLinkAttributeDefinitionUnionTypeDef,
        "Action": UpdateActionTypeType,
    },
)
TypedLinkFacetTypeDef = TypedDict(
    "TypedLinkFacetTypeDef",
    {
        "Name": str,
        "Attributes": Sequence[TypedLinkAttributeDefinitionUnionTypeDef],
        "IdentityAttributeOrder": Sequence[str],
    },
)
BatchReadResponseTypeDef = TypedDict(
    "BatchReadResponseTypeDef",
    {
        "Responses": List[BatchReadOperationResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachTypedLinkRequestRequestTypeDef = TypedDict(
    "DetachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
    },
)
GetLinkAttributesRequestRequestTypeDef = TypedDict(
    "GetLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeNames": Sequence[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
TypedLinkSpecifierUnionTypeDef = Union[TypedLinkSpecifierTypeDef, TypedLinkSpecifierOutputTypeDef]
UpdateLinkAttributesRequestRequestTypeDef = TypedDict(
    "UpdateLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeUpdates": Sequence[LinkAttributeUpdateTypeDef],
    },
)
FacetAttributeUnionTypeDef = Union[FacetAttributeTypeDef, FacetAttributeOutputTypeDef]
UpdateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": Sequence[TypedLinkFacetAttributeUpdateTypeDef],
        "IdentityAttributeOrder": Sequence[str],
    },
)
CreateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "CreateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Facet": TypedLinkFacetTypeDef,
    },
)
BatchDetachTypedLinkTypeDef = TypedDict(
    "BatchDetachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierUnionTypeDef,
    },
)
BatchGetLinkAttributesTypeDef = TypedDict(
    "BatchGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierUnionTypeDef,
        "AttributeNames": Sequence[str],
    },
)
BatchUpdateLinkAttributesTypeDef = TypedDict(
    "BatchUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierUnionTypeDef,
        "AttributeUpdates": Sequence[LinkAttributeUpdateTypeDef],
    },
)
CreateFacetRequestRequestTypeDef = TypedDict(
    "CreateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "Attributes": NotRequired[Sequence[FacetAttributeUnionTypeDef]],
        "ObjectType": NotRequired[ObjectTypeType],
        "FacetStyle": NotRequired[FacetStyleType],
    },
)
FacetAttributeUpdateTypeDef = TypedDict(
    "FacetAttributeUpdateTypeDef",
    {
        "Attribute": NotRequired[FacetAttributeUnionTypeDef],
        "Action": NotRequired[UpdateActionTypeType],
    },
)
BatchReadOperationTypeDef = TypedDict(
    "BatchReadOperationTypeDef",
    {
        "ListObjectAttributes": NotRequired[BatchListObjectAttributesTypeDef],
        "ListObjectChildren": NotRequired[BatchListObjectChildrenTypeDef],
        "ListAttachedIndices": NotRequired[BatchListAttachedIndicesTypeDef],
        "ListObjectParentPaths": NotRequired[BatchListObjectParentPathsTypeDef],
        "GetObjectInformation": NotRequired[BatchGetObjectInformationTypeDef],
        "GetObjectAttributes": NotRequired[BatchGetObjectAttributesTypeDef],
        "ListObjectParents": NotRequired[BatchListObjectParentsTypeDef],
        "ListObjectPolicies": NotRequired[BatchListObjectPoliciesTypeDef],
        "ListPolicyAttachments": NotRequired[BatchListPolicyAttachmentsTypeDef],
        "LookupPolicy": NotRequired[BatchLookupPolicyTypeDef],
        "ListIndex": NotRequired[BatchListIndexTypeDef],
        "ListOutgoingTypedLinks": NotRequired[BatchListOutgoingTypedLinksTypeDef],
        "ListIncomingTypedLinks": NotRequired[BatchListIncomingTypedLinksTypeDef],
        "GetLinkAttributes": NotRequired[BatchGetLinkAttributesTypeDef],
    },
)
BatchWriteOperationTypeDef = TypedDict(
    "BatchWriteOperationTypeDef",
    {
        "CreateObject": NotRequired[BatchCreateObjectTypeDef],
        "AttachObject": NotRequired[BatchAttachObjectTypeDef],
        "DetachObject": NotRequired[BatchDetachObjectTypeDef],
        "UpdateObjectAttributes": NotRequired[BatchUpdateObjectAttributesTypeDef],
        "DeleteObject": NotRequired[BatchDeleteObjectTypeDef],
        "AddFacetToObject": NotRequired[BatchAddFacetToObjectTypeDef],
        "RemoveFacetFromObject": NotRequired[BatchRemoveFacetFromObjectTypeDef],
        "AttachPolicy": NotRequired[BatchAttachPolicyTypeDef],
        "DetachPolicy": NotRequired[BatchDetachPolicyTypeDef],
        "CreateIndex": NotRequired[BatchCreateIndexTypeDef],
        "AttachToIndex": NotRequired[BatchAttachToIndexTypeDef],
        "DetachFromIndex": NotRequired[BatchDetachFromIndexTypeDef],
        "AttachTypedLink": NotRequired[BatchAttachTypedLinkTypeDef],
        "DetachTypedLink": NotRequired[BatchDetachTypedLinkTypeDef],
        "UpdateLinkAttributes": NotRequired[BatchUpdateLinkAttributesTypeDef],
    },
)
UpdateFacetRequestRequestTypeDef = TypedDict(
    "UpdateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": NotRequired[Sequence[FacetAttributeUpdateTypeDef]],
        "ObjectType": NotRequired[ObjectTypeType],
    },
)
BatchReadRequestRequestTypeDef = TypedDict(
    "BatchReadRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": Sequence[BatchReadOperationTypeDef],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
BatchWriteRequestRequestTypeDef = TypedDict(
    "BatchWriteRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": Sequence[BatchWriteOperationTypeDef],
    },
)
