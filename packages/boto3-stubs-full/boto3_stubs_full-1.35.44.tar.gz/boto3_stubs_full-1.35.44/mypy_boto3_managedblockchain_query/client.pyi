"""
Type annotations for managedblockchain-query service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_managedblockchain_query.client import ManagedBlockchainQueryClient

    session = Session()
    client: ManagedBlockchainQueryClient = session.client("managedblockchain-query")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAssetContractsPaginator,
    ListFilteredTransactionEventsPaginator,
    ListTokenBalancesPaginator,
    ListTransactionEventsPaginator,
    ListTransactionsPaginator,
)
from .type_defs import (
    BatchGetTokenBalanceInputRequestTypeDef,
    BatchGetTokenBalanceOutputTypeDef,
    GetAssetContractInputRequestTypeDef,
    GetAssetContractOutputTypeDef,
    GetTokenBalanceInputRequestTypeDef,
    GetTokenBalanceOutputTypeDef,
    GetTransactionInputRequestTypeDef,
    GetTransactionOutputTypeDef,
    ListAssetContractsInputRequestTypeDef,
    ListAssetContractsOutputTypeDef,
    ListFilteredTransactionEventsInputRequestTypeDef,
    ListFilteredTransactionEventsOutputTypeDef,
    ListTokenBalancesInputRequestTypeDef,
    ListTokenBalancesOutputTypeDef,
    ListTransactionEventsInputRequestTypeDef,
    ListTransactionEventsOutputTypeDef,
    ListTransactionsInputRequestTypeDef,
    ListTransactionsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ManagedBlockchainQueryClient",)

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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ManagedBlockchainQueryClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ManagedBlockchainQueryClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#exceptions)
        """

    def batch_get_token_balance(
        self, **kwargs: Unpack[BatchGetTokenBalanceInputRequestTypeDef]
    ) -> BatchGetTokenBalanceOutputTypeDef:
        """
        Gets the token balance for a batch of tokens by using the
        `BatchGetTokenBalance` action for every token in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.batch_get_token_balance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#batch_get_token_balance)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#generate_presigned_url)
        """

    def get_asset_contract(
        self, **kwargs: Unpack[GetAssetContractInputRequestTypeDef]
    ) -> GetAssetContractOutputTypeDef:
        """
        Gets the information about a specific contract deployed on the blockchain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_asset_contract)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#get_asset_contract)
        """

    def get_token_balance(
        self, **kwargs: Unpack[GetTokenBalanceInputRequestTypeDef]
    ) -> GetTokenBalanceOutputTypeDef:
        """
        Gets the balance of a specific token, including native tokens, for a given
        address (wallet or contract) on the
        blockchain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_token_balance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#get_token_balance)
        """

    def get_transaction(
        self, **kwargs: Unpack[GetTransactionInputRequestTypeDef]
    ) -> GetTransactionOutputTypeDef:
        """
        Gets the details of a transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_transaction)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#get_transaction)
        """

    def list_asset_contracts(
        self, **kwargs: Unpack[ListAssetContractsInputRequestTypeDef]
    ) -> ListAssetContractsOutputTypeDef:
        """
        Lists all the contracts for a given contract type deployed by an address
        (either a contract address or a wallet
        address).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_asset_contracts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#list_asset_contracts)
        """

    def list_filtered_transaction_events(
        self, **kwargs: Unpack[ListFilteredTransactionEventsInputRequestTypeDef]
    ) -> ListFilteredTransactionEventsOutputTypeDef:
        """
        Lists all the transaction events for an address on the blockchain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_filtered_transaction_events)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#list_filtered_transaction_events)
        """

    def list_token_balances(
        self, **kwargs: Unpack[ListTokenBalancesInputRequestTypeDef]
    ) -> ListTokenBalancesOutputTypeDef:
        """
        This action returns the following for a given blockchain network: * Lists all
        token balances owned by an address (either a contract address or a wallet
        address).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_token_balances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#list_token_balances)
        """

    def list_transaction_events(
        self, **kwargs: Unpack[ListTransactionEventsInputRequestTypeDef]
    ) -> ListTransactionEventsOutputTypeDef:
        """
        Lists all the transaction events for a transaction .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_transaction_events)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#list_transaction_events)
        """

    def list_transactions(
        self, **kwargs: Unpack[ListTransactionsInputRequestTypeDef]
    ) -> ListTransactionsOutputTypeDef:
        """
        Lists all the transaction events for a transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_transactions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#list_transactions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_contracts"]
    ) -> ListAssetContractsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_filtered_transaction_events"]
    ) -> ListFilteredTransactionEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_token_balances"]
    ) -> ListTokenBalancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transaction_events"]
    ) -> ListTransactionEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transactions"]
    ) -> ListTransactionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client/#get_paginator)
        """
