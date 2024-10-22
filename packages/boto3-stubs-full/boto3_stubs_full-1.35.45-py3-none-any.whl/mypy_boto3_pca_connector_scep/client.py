"""
Type annotations for pca-connector-scep service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pca_connector_scep.client import PrivateCAConnectorforSCEPClient

    session = Session()
    client: PrivateCAConnectorforSCEPClient = session.client("pca-connector-scep")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListChallengeMetadataPaginator, ListConnectorsPaginator
from .type_defs import (
    CreateChallengeRequestRequestTypeDef,
    CreateChallengeResponseTypeDef,
    CreateConnectorRequestRequestTypeDef,
    CreateConnectorResponseTypeDef,
    DeleteChallengeRequestRequestTypeDef,
    DeleteConnectorRequestRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetChallengeMetadataRequestRequestTypeDef,
    GetChallengeMetadataResponseTypeDef,
    GetChallengePasswordRequestRequestTypeDef,
    GetChallengePasswordResponseTypeDef,
    GetConnectorRequestRequestTypeDef,
    GetConnectorResponseTypeDef,
    ListChallengeMetadataRequestRequestTypeDef,
    ListChallengeMetadataResponseTypeDef,
    ListConnectorsRequestRequestTypeDef,
    ListConnectorsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("PrivateCAConnectorforSCEPClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class PrivateCAConnectorforSCEPClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PrivateCAConnectorforSCEPClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#close)
        """

    def create_challenge(
        self, **kwargs: Unpack[CreateChallengeRequestRequestTypeDef]
    ) -> CreateChallengeResponseTypeDef:
        """
        For general-purpose connectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.create_challenge)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#create_challenge)
        """

    def create_connector(
        self, **kwargs: Unpack[CreateConnectorRequestRequestTypeDef]
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates a SCEP connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.create_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#create_connector)
        """

    def delete_challenge(
        self, **kwargs: Unpack[DeleteChallengeRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified
        [Challenge](https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Challenge.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.delete_challenge)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#delete_challenge)
        """

    def delete_connector(
        self, **kwargs: Unpack[DeleteConnectorRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified
        [Connector](https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Connector.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.delete_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#delete_connector)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#generate_presigned_url)
        """

    def get_challenge_metadata(
        self, **kwargs: Unpack[GetChallengeMetadataRequestRequestTypeDef]
    ) -> GetChallengeMetadataResponseTypeDef:
        """
        Retrieves the metadata for the specified
        [Challenge](https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Challenge.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.get_challenge_metadata)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_challenge_metadata)
        """

    def get_challenge_password(
        self, **kwargs: Unpack[GetChallengePasswordRequestRequestTypeDef]
    ) -> GetChallengePasswordResponseTypeDef:
        """
        Retrieves the challenge password for the specified
        [Challenge](https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Challenge.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.get_challenge_password)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_challenge_password)
        """

    def get_connector(
        self, **kwargs: Unpack[GetConnectorRequestRequestTypeDef]
    ) -> GetConnectorResponseTypeDef:
        """
        Retrieves details about the specified
        [Connector](https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Connector.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.get_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_connector)
        """

    def list_challenge_metadata(
        self, **kwargs: Unpack[ListChallengeMetadataRequestRequestTypeDef]
    ) -> ListChallengeMetadataResponseTypeDef:
        """
        Retrieves the challenge metadata for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.list_challenge_metadata)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#list_challenge_metadata)
        """

    def list_connectors(
        self, **kwargs: Unpack[ListConnectorsRequestRequestTypeDef]
    ) -> ListConnectorsResponseTypeDef:
        """
        Lists the connectors belonging to your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.list_connectors)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#list_connectors)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#list_tags_for_resource)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes one or more tags from your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_challenge_metadata"]
    ) -> ListChallengeMetadataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_connectors"]) -> ListConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_paginator)
        """
