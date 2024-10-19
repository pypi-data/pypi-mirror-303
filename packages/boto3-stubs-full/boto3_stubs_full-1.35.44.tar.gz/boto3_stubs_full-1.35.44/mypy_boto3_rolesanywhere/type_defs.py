"""
Type annotations for rolesanywhere service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/type_defs/)

Usage::

    ```python
    from mypy_boto3_rolesanywhere.type_defs import MappingRuleTypeDef

    data: MappingRuleTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import CertificateFieldType, NotificationEventType, TrustAnchorTypeType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "MappingRuleTypeDef",
    "BlobTypeDef",
    "TagTypeDef",
    "NotificationSettingTypeDef",
    "CredentialSummaryTypeDef",
    "CrlDetailTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteAttributeMappingRequestRequestTypeDef",
    "InstancePropertyTypeDef",
    "PaginatorConfigTypeDef",
    "ListRequestRequestTypeDef",
    "SubjectSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NotificationSettingDetailTypeDef",
    "NotificationSettingKeyTypeDef",
    "ScalarCrlRequestRequestTypeDef",
    "ScalarProfileRequestRequestTypeDef",
    "ScalarSubjectRequestRequestTypeDef",
    "ScalarTrustAnchorRequestRequestTypeDef",
    "SourceDataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "AttributeMappingTypeDef",
    "PutAttributeMappingRequestRequestTypeDef",
    "UpdateCrlRequestRequestTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "ImportCrlRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "PutNotificationSettingsRequestRequestTypeDef",
    "CrlDetailResponseTypeDef",
    "ListCrlsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SubjectDetailTypeDef",
    "ListRequestListCrlsPaginateTypeDef",
    "ListRequestListProfilesPaginateTypeDef",
    "ListRequestListSubjectsPaginateTypeDef",
    "ListRequestListTrustAnchorsPaginateTypeDef",
    "ListSubjectsResponseTypeDef",
    "ResetNotificationSettingsRequestRequestTypeDef",
    "SourceTypeDef",
    "ProfileDetailTypeDef",
    "SubjectDetailResponseTypeDef",
    "CreateTrustAnchorRequestRequestTypeDef",
    "TrustAnchorDetailTypeDef",
    "UpdateTrustAnchorRequestRequestTypeDef",
    "DeleteAttributeMappingResponseTypeDef",
    "ListProfilesResponseTypeDef",
    "ProfileDetailResponseTypeDef",
    "PutAttributeMappingResponseTypeDef",
    "ListTrustAnchorsResponseTypeDef",
    "PutNotificationSettingsResponseTypeDef",
    "ResetNotificationSettingsResponseTypeDef",
    "TrustAnchorDetailResponseTypeDef",
)

MappingRuleTypeDef = TypedDict(
    "MappingRuleTypeDef",
    {
        "specifier": str,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
NotificationSettingTypeDef = TypedDict(
    "NotificationSettingTypeDef",
    {
        "enabled": bool,
        "event": NotificationEventType,
        "channel": NotRequired[Literal["ALL"]],
        "threshold": NotRequired[int],
    },
)
CredentialSummaryTypeDef = TypedDict(
    "CredentialSummaryTypeDef",
    {
        "enabled": NotRequired[bool],
        "failed": NotRequired[bool],
        "issuer": NotRequired[str],
        "seenAt": NotRequired[datetime],
        "serialNumber": NotRequired[str],
        "x509CertificateData": NotRequired[str],
    },
)
CrlDetailTypeDef = TypedDict(
    "CrlDetailTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "crlArn": NotRequired[str],
        "crlData": NotRequired[bytes],
        "crlId": NotRequired[str],
        "enabled": NotRequired[bool],
        "name": NotRequired[str],
        "trustAnchorArn": NotRequired[str],
        "updatedAt": NotRequired[datetime],
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
DeleteAttributeMappingRequestRequestTypeDef = TypedDict(
    "DeleteAttributeMappingRequestRequestTypeDef",
    {
        "certificateField": CertificateFieldType,
        "profileId": str,
        "specifiers": NotRequired[Sequence[str]],
    },
)
InstancePropertyTypeDef = TypedDict(
    "InstancePropertyTypeDef",
    {
        "failed": NotRequired[bool],
        "properties": NotRequired[Dict[str, str]],
        "seenAt": NotRequired[datetime],
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
ListRequestRequestTypeDef = TypedDict(
    "ListRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "pageSize": NotRequired[int],
    },
)
SubjectSummaryTypeDef = TypedDict(
    "SubjectSummaryTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "enabled": NotRequired[bool],
        "lastSeenAt": NotRequired[datetime],
        "subjectArn": NotRequired[str],
        "subjectId": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "x509Subject": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
NotificationSettingDetailTypeDef = TypedDict(
    "NotificationSettingDetailTypeDef",
    {
        "enabled": bool,
        "event": NotificationEventType,
        "channel": NotRequired[Literal["ALL"]],
        "configuredBy": NotRequired[str],
        "threshold": NotRequired[int],
    },
)
NotificationSettingKeyTypeDef = TypedDict(
    "NotificationSettingKeyTypeDef",
    {
        "event": NotificationEventType,
        "channel": NotRequired[Literal["ALL"]],
    },
)
ScalarCrlRequestRequestTypeDef = TypedDict(
    "ScalarCrlRequestRequestTypeDef",
    {
        "crlId": str,
    },
)
ScalarProfileRequestRequestTypeDef = TypedDict(
    "ScalarProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)
ScalarSubjectRequestRequestTypeDef = TypedDict(
    "ScalarSubjectRequestRequestTypeDef",
    {
        "subjectId": str,
    },
)
ScalarTrustAnchorRequestRequestTypeDef = TypedDict(
    "ScalarTrustAnchorRequestRequestTypeDef",
    {
        "trustAnchorId": str,
    },
)
SourceDataTypeDef = TypedDict(
    "SourceDataTypeDef",
    {
        "acmPcaArn": NotRequired[str],
        "x509CertificateData": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateProfileRequestRequestTypeDef = TypedDict(
    "UpdateProfileRequestRequestTypeDef",
    {
        "profileId": str,
        "acceptRoleSessionName": NotRequired[bool],
        "durationSeconds": NotRequired[int],
        "managedPolicyArns": NotRequired[Sequence[str]],
        "name": NotRequired[str],
        "roleArns": NotRequired[Sequence[str]],
        "sessionPolicy": NotRequired[str],
    },
)
AttributeMappingTypeDef = TypedDict(
    "AttributeMappingTypeDef",
    {
        "certificateField": NotRequired[CertificateFieldType],
        "mappingRules": NotRequired[List[MappingRuleTypeDef]],
    },
)
PutAttributeMappingRequestRequestTypeDef = TypedDict(
    "PutAttributeMappingRequestRequestTypeDef",
    {
        "certificateField": CertificateFieldType,
        "mappingRules": Sequence[MappingRuleTypeDef],
        "profileId": str,
    },
)
UpdateCrlRequestRequestTypeDef = TypedDict(
    "UpdateCrlRequestRequestTypeDef",
    {
        "crlId": str,
        "crlData": NotRequired[BlobTypeDef],
        "name": NotRequired[str],
    },
)
CreateProfileRequestRequestTypeDef = TypedDict(
    "CreateProfileRequestRequestTypeDef",
    {
        "name": str,
        "roleArns": Sequence[str],
        "acceptRoleSessionName": NotRequired[bool],
        "durationSeconds": NotRequired[int],
        "enabled": NotRequired[bool],
        "managedPolicyArns": NotRequired[Sequence[str]],
        "requireInstanceProperties": NotRequired[bool],
        "sessionPolicy": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ImportCrlRequestRequestTypeDef = TypedDict(
    "ImportCrlRequestRequestTypeDef",
    {
        "crlData": BlobTypeDef,
        "name": str,
        "trustAnchorArn": str,
        "enabled": NotRequired[bool],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
PutNotificationSettingsRequestRequestTypeDef = TypedDict(
    "PutNotificationSettingsRequestRequestTypeDef",
    {
        "notificationSettings": Sequence[NotificationSettingTypeDef],
        "trustAnchorId": str,
    },
)
CrlDetailResponseTypeDef = TypedDict(
    "CrlDetailResponseTypeDef",
    {
        "crl": CrlDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCrlsResponseTypeDef = TypedDict(
    "ListCrlsResponseTypeDef",
    {
        "crls": List[CrlDetailTypeDef],
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
SubjectDetailTypeDef = TypedDict(
    "SubjectDetailTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "credentials": NotRequired[List[CredentialSummaryTypeDef]],
        "enabled": NotRequired[bool],
        "instanceProperties": NotRequired[List[InstancePropertyTypeDef]],
        "lastSeenAt": NotRequired[datetime],
        "subjectArn": NotRequired[str],
        "subjectId": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "x509Subject": NotRequired[str],
    },
)
ListRequestListCrlsPaginateTypeDef = TypedDict(
    "ListRequestListCrlsPaginateTypeDef",
    {
        "pageSize": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRequestListProfilesPaginateTypeDef = TypedDict(
    "ListRequestListProfilesPaginateTypeDef",
    {
        "pageSize": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRequestListSubjectsPaginateTypeDef = TypedDict(
    "ListRequestListSubjectsPaginateTypeDef",
    {
        "pageSize": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRequestListTrustAnchorsPaginateTypeDef = TypedDict(
    "ListRequestListTrustAnchorsPaginateTypeDef",
    {
        "pageSize": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubjectsResponseTypeDef = TypedDict(
    "ListSubjectsResponseTypeDef",
    {
        "nextToken": str,
        "subjects": List[SubjectSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetNotificationSettingsRequestRequestTypeDef = TypedDict(
    "ResetNotificationSettingsRequestRequestTypeDef",
    {
        "notificationSettingKeys": Sequence[NotificationSettingKeyTypeDef],
        "trustAnchorId": str,
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "sourceData": NotRequired[SourceDataTypeDef],
        "sourceType": NotRequired[TrustAnchorTypeType],
    },
)
ProfileDetailTypeDef = TypedDict(
    "ProfileDetailTypeDef",
    {
        "acceptRoleSessionName": NotRequired[bool],
        "attributeMappings": NotRequired[List[AttributeMappingTypeDef]],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "durationSeconds": NotRequired[int],
        "enabled": NotRequired[bool],
        "managedPolicyArns": NotRequired[List[str]],
        "name": NotRequired[str],
        "profileArn": NotRequired[str],
        "profileId": NotRequired[str],
        "requireInstanceProperties": NotRequired[bool],
        "roleArns": NotRequired[List[str]],
        "sessionPolicy": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
SubjectDetailResponseTypeDef = TypedDict(
    "SubjectDetailResponseTypeDef",
    {
        "subject": SubjectDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrustAnchorRequestRequestTypeDef = TypedDict(
    "CreateTrustAnchorRequestRequestTypeDef",
    {
        "name": str,
        "source": SourceTypeDef,
        "enabled": NotRequired[bool],
        "notificationSettings": NotRequired[Sequence[NotificationSettingTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TrustAnchorDetailTypeDef = TypedDict(
    "TrustAnchorDetailTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "enabled": NotRequired[bool],
        "name": NotRequired[str],
        "notificationSettings": NotRequired[List[NotificationSettingDetailTypeDef]],
        "source": NotRequired[SourceTypeDef],
        "trustAnchorArn": NotRequired[str],
        "trustAnchorId": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
UpdateTrustAnchorRequestRequestTypeDef = TypedDict(
    "UpdateTrustAnchorRequestRequestTypeDef",
    {
        "trustAnchorId": str,
        "name": NotRequired[str],
        "source": NotRequired[SourceTypeDef],
    },
)
DeleteAttributeMappingResponseTypeDef = TypedDict(
    "DeleteAttributeMappingResponseTypeDef",
    {
        "profile": ProfileDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "nextToken": str,
        "profiles": List[ProfileDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProfileDetailResponseTypeDef = TypedDict(
    "ProfileDetailResponseTypeDef",
    {
        "profile": ProfileDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAttributeMappingResponseTypeDef = TypedDict(
    "PutAttributeMappingResponseTypeDef",
    {
        "profile": ProfileDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrustAnchorsResponseTypeDef = TypedDict(
    "ListTrustAnchorsResponseTypeDef",
    {
        "nextToken": str,
        "trustAnchors": List[TrustAnchorDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutNotificationSettingsResponseTypeDef = TypedDict(
    "PutNotificationSettingsResponseTypeDef",
    {
        "trustAnchor": TrustAnchorDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetNotificationSettingsResponseTypeDef = TypedDict(
    "ResetNotificationSettingsResponseTypeDef",
    {
        "trustAnchor": TrustAnchorDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TrustAnchorDetailResponseTypeDef = TypedDict(
    "TrustAnchorDetailResponseTypeDef",
    {
        "trustAnchor": TrustAnchorDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
