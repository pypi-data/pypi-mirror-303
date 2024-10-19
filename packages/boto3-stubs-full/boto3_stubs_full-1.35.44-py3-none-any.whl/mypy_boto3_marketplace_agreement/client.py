"""
Type annotations for marketplace-agreement service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_agreement.client import AgreementServiceClient

    session = Session()
    client: AgreementServiceClient = session.client("marketplace-agreement")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    DescribeAgreementInputRequestTypeDef,
    DescribeAgreementOutputTypeDef,
    GetAgreementTermsInputRequestTypeDef,
    GetAgreementTermsOutputTypeDef,
    SearchAgreementsInputRequestTypeDef,
    SearchAgreementsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("AgreementServiceClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class AgreementServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AgreementServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#close)
        """

    def describe_agreement(
        self, **kwargs: Unpack[DescribeAgreementInputRequestTypeDef]
    ) -> DescribeAgreementOutputTypeDef:
        """
        Provides details about an agreement, such as the proposer, acceptor, start
        date, and end
        date.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client.describe_agreement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#describe_agreement)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#generate_presigned_url)
        """

    def get_agreement_terms(
        self, **kwargs: Unpack[GetAgreementTermsInputRequestTypeDef]
    ) -> GetAgreementTermsOutputTypeDef:
        """
        Obtains details about the terms in an agreement that you participated in as
        proposer or
        acceptor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client.get_agreement_terms)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#get_agreement_terms)
        """

    def search_agreements(
        self, **kwargs: Unpack[SearchAgreementsInputRequestTypeDef]
    ) -> SearchAgreementsOutputTypeDef:
        """
        Searches across all agreements that a proposer or an acceptor has in AWS
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-agreement.html#AgreementService.Client.search_agreements)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/client/#search_agreements)
        """
