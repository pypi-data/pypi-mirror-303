"""
Type annotations for mediapackagev2 service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackagev2.client import Mediapackagev2Client

    session = Session()
    client: Mediapackagev2Client = session.client("mediapackagev2")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListChannelGroupsPaginator,
    ListChannelsPaginator,
    ListOriginEndpointsPaginator,
)
from .type_defs import (
    CreateChannelGroupRequestRequestTypeDef,
    CreateChannelGroupResponseTypeDef,
    CreateChannelRequestRequestTypeDef,
    CreateChannelResponseTypeDef,
    CreateOriginEndpointRequestRequestTypeDef,
    CreateOriginEndpointResponseTypeDef,
    DeleteChannelGroupRequestRequestTypeDef,
    DeleteChannelPolicyRequestRequestTypeDef,
    DeleteChannelRequestRequestTypeDef,
    DeleteOriginEndpointPolicyRequestRequestTypeDef,
    DeleteOriginEndpointRequestRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetChannelGroupRequestRequestTypeDef,
    GetChannelGroupResponseTypeDef,
    GetChannelPolicyRequestRequestTypeDef,
    GetChannelPolicyResponseTypeDef,
    GetChannelRequestRequestTypeDef,
    GetChannelResponseTypeDef,
    GetOriginEndpointPolicyRequestRequestTypeDef,
    GetOriginEndpointPolicyResponseTypeDef,
    GetOriginEndpointRequestRequestTypeDef,
    GetOriginEndpointResponseTypeDef,
    ListChannelGroupsRequestRequestTypeDef,
    ListChannelGroupsResponseTypeDef,
    ListChannelsRequestRequestTypeDef,
    ListChannelsResponseTypeDef,
    ListOriginEndpointsRequestRequestTypeDef,
    ListOriginEndpointsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutChannelPolicyRequestRequestTypeDef,
    PutOriginEndpointPolicyRequestRequestTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateChannelGroupRequestRequestTypeDef,
    UpdateChannelGroupResponseTypeDef,
    UpdateChannelRequestRequestTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateOriginEndpointRequestRequestTypeDef,
    UpdateOriginEndpointResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("Mediapackagev2Client",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class Mediapackagev2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Mediapackagev2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#close)
        """

    def create_channel(
        self, **kwargs: Unpack[CreateChannelRequestRequestTypeDef]
    ) -> CreateChannelResponseTypeDef:
        """
        Create a channel to start receiving content streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.create_channel)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#create_channel)
        """

    def create_channel_group(
        self, **kwargs: Unpack[CreateChannelGroupRequestRequestTypeDef]
    ) -> CreateChannelGroupResponseTypeDef:
        """
        Create a channel group to group your channels and origin endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.create_channel_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#create_channel_group)
        """

    def create_origin_endpoint(
        self, **kwargs: Unpack[CreateOriginEndpointRequestRequestTypeDef]
    ) -> CreateOriginEndpointResponseTypeDef:
        """
        The endpoint is attached to a channel, and represents the output of the live
        content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.create_origin_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#create_origin_endpoint)
        """

    def delete_channel(
        self, **kwargs: Unpack[DeleteChannelRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a channel to stop AWS Elemental MediaPackage from receiving further
        content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.delete_channel)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_channel)
        """

    def delete_channel_group(
        self, **kwargs: Unpack[DeleteChannelGroupRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a channel group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.delete_channel_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_channel_group)
        """

    def delete_channel_policy(
        self, **kwargs: Unpack[DeleteChannelPolicyRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a channel policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.delete_channel_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_channel_policy)
        """

    def delete_origin_endpoint(
        self, **kwargs: Unpack[DeleteOriginEndpointRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Origin endpoints can serve content until they're deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.delete_origin_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_origin_endpoint)
        """

    def delete_origin_endpoint_policy(
        self, **kwargs: Unpack[DeleteOriginEndpointPolicyRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete an origin endpoint policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.delete_origin_endpoint_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#delete_origin_endpoint_policy)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#generate_presigned_url)
        """

    def get_channel(
        self, **kwargs: Unpack[GetChannelRequestRequestTypeDef]
    ) -> GetChannelResponseTypeDef:
        """
        Retrieves the specified channel that's configured in AWS Elemental
        MediaPackage, including the origin endpoints that are associated with
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.get_channel)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_channel)
        """

    def get_channel_group(
        self, **kwargs: Unpack[GetChannelGroupRequestRequestTypeDef]
    ) -> GetChannelGroupResponseTypeDef:
        """
        Retrieves the specified channel group that's configured in AWS Elemental
        MediaPackage, including the channels and origin endpoints that are associated
        with
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.get_channel_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_channel_group)
        """

    def get_channel_policy(
        self, **kwargs: Unpack[GetChannelPolicyRequestRequestTypeDef]
    ) -> GetChannelPolicyResponseTypeDef:
        """
        Retrieves the specified channel policy that's configured in AWS Elemental
        MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.get_channel_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_channel_policy)
        """

    def get_origin_endpoint(
        self, **kwargs: Unpack[GetOriginEndpointRequestRequestTypeDef]
    ) -> GetOriginEndpointResponseTypeDef:
        """
        Retrieves the specified origin endpoint that's configured in AWS Elemental
        MediaPackage to obtain its playback URL and to view the packaging settings that
        it's currently
        using.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.get_origin_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_origin_endpoint)
        """

    def get_origin_endpoint_policy(
        self, **kwargs: Unpack[GetOriginEndpointPolicyRequestRequestTypeDef]
    ) -> GetOriginEndpointPolicyResponseTypeDef:
        """
        Retrieves the specified origin endpoint policy that's configured in AWS
        Elemental
        MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.get_origin_endpoint_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_origin_endpoint_policy)
        """

    def list_channel_groups(
        self, **kwargs: Unpack[ListChannelGroupsRequestRequestTypeDef]
    ) -> ListChannelGroupsResponseTypeDef:
        """
        Retrieves all channel groups that are configured in AWS Elemental MediaPackage,
        including the channels and origin endpoints that are associated with
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.list_channel_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_channel_groups)
        """

    def list_channels(
        self, **kwargs: Unpack[ListChannelsRequestRequestTypeDef]
    ) -> ListChannelsResponseTypeDef:
        """
        Retrieves all channels in a specific channel group that are configured in AWS
        Elemental MediaPackage, including the origin endpoints that are associated with
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.list_channels)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_channels)
        """

    def list_origin_endpoints(
        self, **kwargs: Unpack[ListOriginEndpointsRequestRequestTypeDef]
    ) -> ListOriginEndpointsResponseTypeDef:
        """
        Retrieves all origin endpoints in a specific channel that are configured in AWS
        Elemental
        MediaPackage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.list_origin_endpoints)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_origin_endpoints)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#list_tags_for_resource)
        """

    def put_channel_policy(
        self, **kwargs: Unpack[PutChannelPolicyRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Attaches an IAM policy to the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.put_channel_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#put_channel_policy)
        """

    def put_origin_endpoint_policy(
        self, **kwargs: Unpack[PutOriginEndpointPolicyRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Attaches an IAM policy to the specified origin endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.put_origin_endpoint_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#put_origin_endpoint_policy)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns one of more tags (key-value pairs) to the specified MediaPackage
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#untag_resource)
        """

    def update_channel(
        self, **kwargs: Unpack[UpdateChannelRequestRequestTypeDef]
    ) -> UpdateChannelResponseTypeDef:
        """
        Update the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.update_channel)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#update_channel)
        """

    def update_channel_group(
        self, **kwargs: Unpack[UpdateChannelGroupRequestRequestTypeDef]
    ) -> UpdateChannelGroupResponseTypeDef:
        """
        Update the specified channel group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.update_channel_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#update_channel_group)
        """

    def update_origin_endpoint(
        self, **kwargs: Unpack[UpdateOriginEndpointRequestRequestTypeDef]
    ) -> UpdateOriginEndpointResponseTypeDef:
        """
        Update the specified origin endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.update_origin_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#update_origin_endpoint)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_channel_groups"]
    ) -> ListChannelGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_origin_endpoints"]
    ) -> ListOriginEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2.html#Mediapackagev2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/client/#get_paginator)
        """
