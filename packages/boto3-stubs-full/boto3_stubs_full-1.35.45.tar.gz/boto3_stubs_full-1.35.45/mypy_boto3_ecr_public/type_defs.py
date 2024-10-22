"""
Type annotations for ecr-public service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/type_defs/)

Usage::

    ```python
    from mypy_boto3_ecr_public.type_defs import AuthorizationDataTypeDef

    data: AuthorizationDataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ImageFailureCodeType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    RegistryAliasStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AuthorizationDataTypeDef",
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "ResponseMetadataTypeDef",
    "ImageIdentifierTypeDef",
    "BlobTypeDef",
    "CompleteLayerUploadRequestRequestTypeDef",
    "TagTypeDef",
    "RepositoryCatalogDataTypeDef",
    "RepositoryTypeDef",
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeImageTagsRequestRequestTypeDef",
    "ImageDetailTypeDef",
    "DescribeRegistriesRequestRequestTypeDef",
    "DescribeRepositoriesRequestRequestTypeDef",
    "RegistryCatalogDataTypeDef",
    "GetRepositoryCatalogDataRequestRequestTypeDef",
    "GetRepositoryPolicyRequestRequestTypeDef",
    "ReferencedImageDetailTypeDef",
    "InitiateLayerUploadRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutImageRequestRequestTypeDef",
    "PutRegistryCatalogDataRequestRequestTypeDef",
    "RegistryAliasTypeDef",
    "SetRepositoryPolicyRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "UploadLayerPartResponseTypeDef",
    "BatchDeleteImageRequestRequestTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "ImageFailureTypeDef",
    "ImageTypeDef",
    "RepositoryCatalogDataInputTypeDef",
    "UploadLayerPartRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "GetRepositoryCatalogDataResponseTypeDef",
    "PutRepositoryCatalogDataResponseTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "DescribeImageTagsRequestDescribeImageTagsPaginateTypeDef",
    "DescribeImagesRequestDescribeImagesPaginateTypeDef",
    "DescribeRegistriesRequestDescribeRegistriesPaginateTypeDef",
    "DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef",
    "DescribeImagesResponseTypeDef",
    "GetRegistryCatalogDataResponseTypeDef",
    "PutRegistryCatalogDataResponseTypeDef",
    "ImageTagDetailTypeDef",
    "RegistryTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "PutImageResponseTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "PutRepositoryCatalogDataRequestRequestTypeDef",
    "DescribeImageTagsResponseTypeDef",
    "DescribeRegistriesResponseTypeDef",
)

AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": NotRequired[str],
        "expiresAt": NotRequired[datetime],
    },
)
BatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigests": Sequence[str],
        "registryId": NotRequired[str],
    },
)
LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": NotRequired[str],
        "failureCode": NotRequired[LayerFailureCodeType],
        "failureReason": NotRequired[str],
    },
)
LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": NotRequired[str],
        "layerAvailability": NotRequired[LayerAvailabilityType],
        "layerSize": NotRequired[int],
        "mediaType": NotRequired[str],
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
ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef",
    {
        "imageDigest": NotRequired[str],
        "imageTag": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "CompleteLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "layerDigests": Sequence[str],
        "registryId": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
RepositoryCatalogDataTypeDef = TypedDict(
    "RepositoryCatalogDataTypeDef",
    {
        "description": NotRequired[str],
        "architectures": NotRequired[List[str]],
        "operatingSystems": NotRequired[List[str]],
        "logoUrl": NotRequired[str],
        "aboutText": NotRequired[str],
        "usageText": NotRequired[str],
        "marketplaceCertified": NotRequired[bool],
    },
)
RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": NotRequired[str],
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "repositoryUri": NotRequired[str],
        "createdAt": NotRequired[datetime],
    },
)
DeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
DeleteRepositoryRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "force": NotRequired[bool],
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
DescribeImageTagsRequestRequestTypeDef = TypedDict(
    "DescribeImageTagsRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "imageDigest": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "imageSizeInBytes": NotRequired[int],
        "imagePushedAt": NotRequired[datetime],
        "imageManifestMediaType": NotRequired[str],
        "artifactMediaType": NotRequired[str],
    },
)
DescribeRegistriesRequestRequestTypeDef = TypedDict(
    "DescribeRegistriesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeRepositoriesRequestRequestTypeDef = TypedDict(
    "DescribeRepositoriesRequestRequestTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryNames": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RegistryCatalogDataTypeDef = TypedDict(
    "RegistryCatalogDataTypeDef",
    {
        "displayName": NotRequired[str],
    },
)
GetRepositoryCatalogDataRequestRequestTypeDef = TypedDict(
    "GetRepositoryCatalogDataRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
GetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "GetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
ReferencedImageDetailTypeDef = TypedDict(
    "ReferencedImageDetailTypeDef",
    {
        "imageDigest": NotRequired[str],
        "imageSizeInBytes": NotRequired[int],
        "imagePushedAt": NotRequired[datetime],
        "imageManifestMediaType": NotRequired[str],
        "artifactMediaType": NotRequired[str],
    },
)
InitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "InitiateLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
PutImageRequestRequestTypeDef = TypedDict(
    "PutImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageManifest": str,
        "registryId": NotRequired[str],
        "imageManifestMediaType": NotRequired[str],
        "imageTag": NotRequired[str],
        "imageDigest": NotRequired[str],
    },
)
PutRegistryCatalogDataRequestRequestTypeDef = TypedDict(
    "PutRegistryCatalogDataRequestRequestTypeDef",
    {
        "displayName": NotRequired[str],
    },
)
RegistryAliasTypeDef = TypedDict(
    "RegistryAliasTypeDef",
    {
        "name": str,
        "status": RegistryAliasStatusType,
        "primaryRegistryAlias": bool,
        "defaultRegistryAlias": bool,
    },
)
SetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "SetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "policyText": str,
        "registryId": NotRequired[str],
        "force": NotRequired[bool],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List[LayerTypeDef],
        "failures": List[LayerFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": AuthorizationDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteImageRequestRequestTypeDef = TypedDict(
    "BatchDeleteImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
        "registryId": NotRequired[str],
    },
)
DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence[ImageIdentifierTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ImageFailureTypeDef = TypedDict(
    "ImageFailureTypeDef",
    {
        "imageId": NotRequired[ImageIdentifierTypeDef],
        "failureCode": NotRequired[ImageFailureCodeType],
        "failureReason": NotRequired[str],
    },
)
ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "imageId": NotRequired[ImageIdentifierTypeDef],
        "imageManifest": NotRequired[str],
        "imageManifestMediaType": NotRequired[str],
    },
)
RepositoryCatalogDataInputTypeDef = TypedDict(
    "RepositoryCatalogDataInputTypeDef",
    {
        "description": NotRequired[str],
        "architectures": NotRequired[Sequence[str]],
        "operatingSystems": NotRequired[Sequence[str]],
        "logoImageBlob": NotRequired[BlobTypeDef],
        "aboutText": NotRequired[str],
        "usageText": NotRequired[str],
    },
)
UploadLayerPartRequestRequestTypeDef = TypedDict(
    "UploadLayerPartRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "partFirstByte": int,
        "partLastByte": int,
        "layerPartBlob": BlobTypeDef,
        "registryId": NotRequired[str],
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
GetRepositoryCatalogDataResponseTypeDef = TypedDict(
    "GetRepositoryCatalogDataResponseTypeDef",
    {
        "catalogData": RepositoryCatalogDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRepositoryCatalogDataResponseTypeDef = TypedDict(
    "PutRepositoryCatalogDataResponseTypeDef",
    {
        "catalogData": RepositoryCatalogDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef",
    {
        "repository": RepositoryTypeDef,
        "catalogData": RepositoryCatalogDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef",
    {
        "repository": RepositoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List[RepositoryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeImageTagsRequestDescribeImageTagsPaginateTypeDef = TypedDict(
    "DescribeImageTagsRequestDescribeImageTagsPaginateTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeImagesRequestDescribeImagesPaginateTypeDef = TypedDict(
    "DescribeImagesRequestDescribeImagesPaginateTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence[ImageIdentifierTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegistriesRequestDescribeRegistriesPaginateTypeDef = TypedDict(
    "DescribeRegistriesRequestDescribeRegistriesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef = TypedDict(
    "DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {
        "imageDetails": List[ImageDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegistryCatalogDataResponseTypeDef = TypedDict(
    "GetRegistryCatalogDataResponseTypeDef",
    {
        "registryCatalogData": RegistryCatalogDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRegistryCatalogDataResponseTypeDef = TypedDict(
    "PutRegistryCatalogDataResponseTypeDef",
    {
        "registryCatalogData": RegistryCatalogDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageTagDetailTypeDef = TypedDict(
    "ImageTagDetailTypeDef",
    {
        "imageTag": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "imageDetail": NotRequired[ReferencedImageDetailTypeDef],
    },
)
RegistryTypeDef = TypedDict(
    "RegistryTypeDef",
    {
        "registryId": str,
        "registryArn": str,
        "registryUri": str,
        "verified": bool,
        "aliases": List[RegistryAliasTypeDef],
    },
)
BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {
        "imageIds": List[ImageIdentifierTypeDef],
        "failures": List[ImageFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef",
    {
        "image": ImageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRepositoryRequestRequestTypeDef = TypedDict(
    "CreateRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "catalogData": NotRequired[RepositoryCatalogDataInputTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PutRepositoryCatalogDataRequestRequestTypeDef = TypedDict(
    "PutRepositoryCatalogDataRequestRequestTypeDef",
    {
        "repositoryName": str,
        "catalogData": RepositoryCatalogDataInputTypeDef,
        "registryId": NotRequired[str],
    },
)
DescribeImageTagsResponseTypeDef = TypedDict(
    "DescribeImageTagsResponseTypeDef",
    {
        "imageTagDetails": List[ImageTagDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRegistriesResponseTypeDef = TypedDict(
    "DescribeRegistriesResponseTypeDef",
    {
        "registries": List[RegistryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
