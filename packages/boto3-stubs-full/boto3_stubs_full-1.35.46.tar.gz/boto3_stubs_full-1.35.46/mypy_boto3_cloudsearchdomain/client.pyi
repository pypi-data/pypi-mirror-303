"""
Type annotations for cloudsearchdomain service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudsearchdomain.client import CloudSearchDomainClient

    session = Session()
    client: CloudSearchDomainClient = session.client("cloudsearchdomain")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    SearchRequestRequestTypeDef,
    SearchResponseTypeDef,
    SuggestRequestRequestTypeDef,
    SuggestResponseTypeDef,
    UploadDocumentsRequestRequestTypeDef,
    UploadDocumentsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("CloudSearchDomainClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    DocumentServiceException: Type[BotocoreClientError]
    SearchException: Type[BotocoreClientError]

class CloudSearchDomainClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudSearchDomainClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#generate_presigned_url)
        """

    def search(self, **kwargs: Unpack[SearchRequestRequestTypeDef]) -> SearchResponseTypeDef:
        """
        Retrieves a list of documents that match the specified search criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.search)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#search)
        """

    def suggest(self, **kwargs: Unpack[SuggestRequestRequestTypeDef]) -> SuggestResponseTypeDef:
        """
        Retrieves autocomplete suggestions for a partial query string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.suggest)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#suggest)
        """

    def upload_documents(
        self, **kwargs: Unpack[UploadDocumentsRequestRequestTypeDef]
    ) -> UploadDocumentsResponseTypeDef:
        """
        Posts a batch of documents to a search domain for indexing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.upload_documents)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#upload_documents)
        """
