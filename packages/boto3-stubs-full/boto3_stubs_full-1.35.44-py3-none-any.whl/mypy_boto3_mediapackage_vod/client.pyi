"""
Type annotations for mediapackage-vod service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackage_vod.client import MediaPackageVodClient

    session = Session()
    client: MediaPackageVodClient = session.client("mediapackage-vod")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAssetsPaginator,
    ListPackagingConfigurationsPaginator,
    ListPackagingGroupsPaginator,
)
from .type_defs import (
    ConfigureLogsRequestRequestTypeDef,
    ConfigureLogsResponseTypeDef,
    CreateAssetRequestRequestTypeDef,
    CreateAssetResponseTypeDef,
    CreatePackagingConfigurationRequestRequestTypeDef,
    CreatePackagingConfigurationResponseTypeDef,
    CreatePackagingGroupRequestRequestTypeDef,
    CreatePackagingGroupResponseTypeDef,
    DeleteAssetRequestRequestTypeDef,
    DeletePackagingConfigurationRequestRequestTypeDef,
    DeletePackagingGroupRequestRequestTypeDef,
    DescribeAssetRequestRequestTypeDef,
    DescribeAssetResponseTypeDef,
    DescribePackagingConfigurationRequestRequestTypeDef,
    DescribePackagingConfigurationResponseTypeDef,
    DescribePackagingGroupRequestRequestTypeDef,
    DescribePackagingGroupResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ListAssetsRequestRequestTypeDef,
    ListAssetsResponseTypeDef,
    ListPackagingConfigurationsRequestRequestTypeDef,
    ListPackagingConfigurationsResponseTypeDef,
    ListPackagingGroupsRequestRequestTypeDef,
    ListPackagingGroupsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdatePackagingGroupRequestRequestTypeDef,
    UpdatePackagingGroupResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MediaPackageVodClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]

class MediaPackageVodClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaPackageVodClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#close)
        """

    def configure_logs(
        self, **kwargs: Unpack[ConfigureLogsRequestRequestTypeDef]
    ) -> ConfigureLogsResponseTypeDef:
        """
        Changes the packaging group's properities to configure log subscription See
        also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/ConfigureLogs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.configure_logs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#configure_logs)
        """

    def create_asset(
        self, **kwargs: Unpack[CreateAssetRequestRequestTypeDef]
    ) -> CreateAssetResponseTypeDef:
        """
        Creates a new MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_asset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#create_asset)
        """

    def create_packaging_configuration(
        self, **kwargs: Unpack[CreatePackagingConfigurationRequestRequestTypeDef]
    ) -> CreatePackagingConfigurationResponseTypeDef:
        """
        Creates a new MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#create_packaging_configuration)
        """

    def create_packaging_group(
        self, **kwargs: Unpack[CreatePackagingGroupRequestRequestTypeDef]
    ) -> CreatePackagingGroupResponseTypeDef:
        """
        Creates a new MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#create_packaging_group)
        """

    def delete_asset(self, **kwargs: Unpack[DeleteAssetRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an existing MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_asset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#delete_asset)
        """

    def delete_packaging_configuration(
        self, **kwargs: Unpack[DeletePackagingConfigurationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#delete_packaging_configuration)
        """

    def delete_packaging_group(
        self, **kwargs: Unpack[DeletePackagingGroupRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#delete_packaging_group)
        """

    def describe_asset(
        self, **kwargs: Unpack[DescribeAssetRequestRequestTypeDef]
    ) -> DescribeAssetResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD Asset resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_asset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#describe_asset)
        """

    def describe_packaging_configuration(
        self, **kwargs: Unpack[DescribePackagingConfigurationRequestRequestTypeDef]
    ) -> DescribePackagingConfigurationResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD PackagingConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#describe_packaging_configuration)
        """

    def describe_packaging_group(
        self, **kwargs: Unpack[DescribePackagingGroupRequestRequestTypeDef]
    ) -> DescribePackagingGroupResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD PackagingGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#describe_packaging_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#generate_presigned_url)
        """

    def list_assets(
        self, **kwargs: Unpack[ListAssetsRequestRequestTypeDef]
    ) -> ListAssetsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD Asset resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_assets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#list_assets)
        """

    def list_packaging_configurations(
        self, **kwargs: Unpack[ListPackagingConfigurationsRequestRequestTypeDef]
    ) -> ListPackagingConfigurationsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD PackagingConfiguration resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_configurations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#list_packaging_configurations)
        """

    def list_packaging_groups(
        self, **kwargs: Unpack[ListPackagingGroupsRequestRequestTypeDef]
    ) -> ListPackagingGroupsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD PackagingGroup resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#list_packaging_groups)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags assigned to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#list_tags_for_resource)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#untag_resource)
        """

    def update_packaging_group(
        self, **kwargs: Unpack[UpdatePackagingGroupRequestRequestTypeDef]
    ) -> UpdatePackagingGroupResponseTypeDef:
        """
        Updates a specific packaging group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.update_packaging_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#update_packaging_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_assets"]) -> ListAssetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_configurations"]
    ) -> ListPackagingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_groups"]
    ) -> ListPackagingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/client/#get_paginator)
        """
