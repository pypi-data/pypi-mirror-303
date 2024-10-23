"""
Type annotations for managedblockchain-query service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/type_defs/)

Usage::

    ```python
    from mypy_boto3_managedblockchain_query.type_defs import AddressIdentifierFilterTypeDef

    data: AddressIdentifierFilterTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ConfirmationStatusType,
    ErrorTypeType,
    ExecutionStatusType,
    QueryNetworkType,
    QueryTokenStandardType,
    QueryTransactionEventTypeType,
    SortOrderType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AddressIdentifierFilterTypeDef",
    "ContractIdentifierTypeDef",
    "BlockchainInstantOutputTypeDef",
    "OwnerIdentifierTypeDef",
    "TokenIdentifierTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "ConfirmationStatusFilterTypeDef",
    "ContractFilterTypeDef",
    "ContractMetadataTypeDef",
    "GetTransactionInputRequestTypeDef",
    "TransactionTypeDef",
    "PaginatorConfigTypeDef",
    "ListFilteredTransactionEventsSortTypeDef",
    "VoutFilterTypeDef",
    "OwnerFilterTypeDef",
    "TokenFilterTypeDef",
    "ListTransactionEventsInputRequestTypeDef",
    "ListTransactionsSortTypeDef",
    "TransactionOutputItemTypeDef",
    "AssetContractTypeDef",
    "GetAssetContractInputRequestTypeDef",
    "TransactionEventTypeDef",
    "BatchGetTokenBalanceErrorItemTypeDef",
    "BatchGetTokenBalanceOutputItemTypeDef",
    "TokenBalanceTypeDef",
    "GetTokenBalanceOutputTypeDef",
    "BlockchainInstantTypeDef",
    "ListAssetContractsInputRequestTypeDef",
    "GetAssetContractOutputTypeDef",
    "GetTransactionOutputTypeDef",
    "ListAssetContractsInputListAssetContractsPaginateTypeDef",
    "ListTransactionEventsInputListTransactionEventsPaginateTypeDef",
    "ListTokenBalancesInputListTokenBalancesPaginateTypeDef",
    "ListTokenBalancesInputRequestTypeDef",
    "ListTransactionsOutputTypeDef",
    "ListAssetContractsOutputTypeDef",
    "ListFilteredTransactionEventsOutputTypeDef",
    "ListTransactionEventsOutputTypeDef",
    "BatchGetTokenBalanceOutputTypeDef",
    "ListTokenBalancesOutputTypeDef",
    "BlockchainInstantUnionTypeDef",
    "GetTokenBalanceInputRequestTypeDef",
    "ListTransactionsInputListTransactionsPaginateTypeDef",
    "ListTransactionsInputRequestTypeDef",
    "TimeFilterTypeDef",
    "BatchGetTokenBalanceInputItemTypeDef",
    "ListFilteredTransactionEventsInputListFilteredTransactionEventsPaginateTypeDef",
    "ListFilteredTransactionEventsInputRequestTypeDef",
    "BatchGetTokenBalanceInputRequestTypeDef",
)

AddressIdentifierFilterTypeDef = TypedDict(
    "AddressIdentifierFilterTypeDef",
    {
        "transactionEventToAddress": Sequence[str],
    },
)
ContractIdentifierTypeDef = TypedDict(
    "ContractIdentifierTypeDef",
    {
        "network": QueryNetworkType,
        "contractAddress": str,
    },
)
BlockchainInstantOutputTypeDef = TypedDict(
    "BlockchainInstantOutputTypeDef",
    {
        "time": NotRequired[datetime],
    },
)
OwnerIdentifierTypeDef = TypedDict(
    "OwnerIdentifierTypeDef",
    {
        "address": str,
    },
)
TokenIdentifierTypeDef = TypedDict(
    "TokenIdentifierTypeDef",
    {
        "network": QueryNetworkType,
        "contractAddress": NotRequired[str],
        "tokenId": NotRequired[str],
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
TimestampTypeDef = Union[datetime, str]
ConfirmationStatusFilterTypeDef = TypedDict(
    "ConfirmationStatusFilterTypeDef",
    {
        "include": Sequence[ConfirmationStatusType],
    },
)
ContractFilterTypeDef = TypedDict(
    "ContractFilterTypeDef",
    {
        "network": QueryNetworkType,
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
    },
)
ContractMetadataTypeDef = TypedDict(
    "ContractMetadataTypeDef",
    {
        "name": NotRequired[str],
        "symbol": NotRequired[str],
        "decimals": NotRequired[int],
    },
)
GetTransactionInputRequestTypeDef = TypedDict(
    "GetTransactionInputRequestTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": NotRequired[str],
        "transactionId": NotRequired[str],
    },
)
TransactionTypeDef = TypedDict(
    "TransactionTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "transactionTimestamp": datetime,
        "transactionIndex": int,
        "numberOfTransactions": int,
        "to": str,
        "blockHash": NotRequired[str],
        "blockNumber": NotRequired[str],
        "from": NotRequired[str],
        "contractAddress": NotRequired[str],
        "gasUsed": NotRequired[str],
        "cumulativeGasUsed": NotRequired[str],
        "effectiveGasPrice": NotRequired[str],
        "signatureV": NotRequired[int],
        "signatureR": NotRequired[str],
        "signatureS": NotRequired[str],
        "transactionFee": NotRequired[str],
        "transactionId": NotRequired[str],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
        "executionStatus": NotRequired[ExecutionStatusType],
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
ListFilteredTransactionEventsSortTypeDef = TypedDict(
    "ListFilteredTransactionEventsSortTypeDef",
    {
        "sortBy": NotRequired[Literal["blockchainInstant"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
VoutFilterTypeDef = TypedDict(
    "VoutFilterTypeDef",
    {
        "voutSpent": bool,
    },
)
OwnerFilterTypeDef = TypedDict(
    "OwnerFilterTypeDef",
    {
        "address": str,
    },
)
TokenFilterTypeDef = TypedDict(
    "TokenFilterTypeDef",
    {
        "network": QueryNetworkType,
        "contractAddress": NotRequired[str],
        "tokenId": NotRequired[str],
    },
)
ListTransactionEventsInputRequestTypeDef = TypedDict(
    "ListTransactionEventsInputRequestTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": NotRequired[str],
        "transactionId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTransactionsSortTypeDef = TypedDict(
    "ListTransactionsSortTypeDef",
    {
        "sortBy": NotRequired[Literal["TRANSACTION_TIMESTAMP"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
TransactionOutputItemTypeDef = TypedDict(
    "TransactionOutputItemTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
        "transactionTimestamp": datetime,
        "transactionId": NotRequired[str],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
    },
)
AssetContractTypeDef = TypedDict(
    "AssetContractTypeDef",
    {
        "contractIdentifier": ContractIdentifierTypeDef,
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
    },
)
GetAssetContractInputRequestTypeDef = TypedDict(
    "GetAssetContractInputRequestTypeDef",
    {
        "contractIdentifier": ContractIdentifierTypeDef,
    },
)
TransactionEventTypeDef = TypedDict(
    "TransactionEventTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "eventType": QueryTransactionEventTypeType,
        "from": NotRequired[str],
        "to": NotRequired[str],
        "value": NotRequired[str],
        "contractAddress": NotRequired[str],
        "tokenId": NotRequired[str],
        "transactionId": NotRequired[str],
        "voutIndex": NotRequired[int],
        "voutSpent": NotRequired[bool],
        "spentVoutTransactionId": NotRequired[str],
        "spentVoutTransactionHash": NotRequired[str],
        "spentVoutIndex": NotRequired[int],
        "blockchainInstant": NotRequired[BlockchainInstantOutputTypeDef],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
    },
)
BatchGetTokenBalanceErrorItemTypeDef = TypedDict(
    "BatchGetTokenBalanceErrorItemTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "errorType": ErrorTypeType,
        "tokenIdentifier": NotRequired[TokenIdentifierTypeDef],
        "ownerIdentifier": NotRequired[OwnerIdentifierTypeDef],
        "atBlockchainInstant": NotRequired[BlockchainInstantOutputTypeDef],
    },
)
BatchGetTokenBalanceOutputItemTypeDef = TypedDict(
    "BatchGetTokenBalanceOutputItemTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": BlockchainInstantOutputTypeDef,
        "ownerIdentifier": NotRequired[OwnerIdentifierTypeDef],
        "tokenIdentifier": NotRequired[TokenIdentifierTypeDef],
        "lastUpdatedTime": NotRequired[BlockchainInstantOutputTypeDef],
    },
)
TokenBalanceTypeDef = TypedDict(
    "TokenBalanceTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": BlockchainInstantOutputTypeDef,
        "ownerIdentifier": NotRequired[OwnerIdentifierTypeDef],
        "tokenIdentifier": NotRequired[TokenIdentifierTypeDef],
        "lastUpdatedTime": NotRequired[BlockchainInstantOutputTypeDef],
    },
)
GetTokenBalanceOutputTypeDef = TypedDict(
    "GetTokenBalanceOutputTypeDef",
    {
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "tokenIdentifier": TokenIdentifierTypeDef,
        "balance": str,
        "atBlockchainInstant": BlockchainInstantOutputTypeDef,
        "lastUpdatedTime": BlockchainInstantOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BlockchainInstantTypeDef = TypedDict(
    "BlockchainInstantTypeDef",
    {
        "time": NotRequired[TimestampTypeDef],
    },
)
ListAssetContractsInputRequestTypeDef = TypedDict(
    "ListAssetContractsInputRequestTypeDef",
    {
        "contractFilter": ContractFilterTypeDef,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetAssetContractOutputTypeDef = TypedDict(
    "GetAssetContractOutputTypeDef",
    {
        "contractIdentifier": ContractIdentifierTypeDef,
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
        "metadata": ContractMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransactionOutputTypeDef = TypedDict(
    "GetTransactionOutputTypeDef",
    {
        "transaction": TransactionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetContractsInputListAssetContractsPaginateTypeDef = TypedDict(
    "ListAssetContractsInputListAssetContractsPaginateTypeDef",
    {
        "contractFilter": ContractFilterTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTransactionEventsInputListTransactionEventsPaginateTypeDef = TypedDict(
    "ListTransactionEventsInputListTransactionEventsPaginateTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": NotRequired[str],
        "transactionId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTokenBalancesInputListTokenBalancesPaginateTypeDef = TypedDict(
    "ListTokenBalancesInputListTokenBalancesPaginateTypeDef",
    {
        "tokenFilter": TokenFilterTypeDef,
        "ownerFilter": NotRequired[OwnerFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTokenBalancesInputRequestTypeDef = TypedDict(
    "ListTokenBalancesInputRequestTypeDef",
    {
        "tokenFilter": TokenFilterTypeDef,
        "ownerFilter": NotRequired[OwnerFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTransactionsOutputTypeDef = TypedDict(
    "ListTransactionsOutputTypeDef",
    {
        "transactions": List[TransactionOutputItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetContractsOutputTypeDef = TypedDict(
    "ListAssetContractsOutputTypeDef",
    {
        "contracts": List[AssetContractTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFilteredTransactionEventsOutputTypeDef = TypedDict(
    "ListFilteredTransactionEventsOutputTypeDef",
    {
        "events": List[TransactionEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTransactionEventsOutputTypeDef = TypedDict(
    "ListTransactionEventsOutputTypeDef",
    {
        "events": List[TransactionEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetTokenBalanceOutputTypeDef = TypedDict(
    "BatchGetTokenBalanceOutputTypeDef",
    {
        "tokenBalances": List[BatchGetTokenBalanceOutputItemTypeDef],
        "errors": List[BatchGetTokenBalanceErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTokenBalancesOutputTypeDef = TypedDict(
    "ListTokenBalancesOutputTypeDef",
    {
        "tokenBalances": List[TokenBalanceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BlockchainInstantUnionTypeDef = Union[BlockchainInstantTypeDef, BlockchainInstantOutputTypeDef]
GetTokenBalanceInputRequestTypeDef = TypedDict(
    "GetTokenBalanceInputRequestTypeDef",
    {
        "tokenIdentifier": TokenIdentifierTypeDef,
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "atBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
    },
)
ListTransactionsInputListTransactionsPaginateTypeDef = TypedDict(
    "ListTransactionsInputListTransactionsPaginateTypeDef",
    {
        "address": str,
        "network": QueryNetworkType,
        "fromBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
        "toBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
        "sort": NotRequired[ListTransactionsSortTypeDef],
        "confirmationStatusFilter": NotRequired[ConfirmationStatusFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTransactionsInputRequestTypeDef = TypedDict(
    "ListTransactionsInputRequestTypeDef",
    {
        "address": str,
        "network": QueryNetworkType,
        "fromBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
        "toBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
        "sort": NotRequired[ListTransactionsSortTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "confirmationStatusFilter": NotRequired[ConfirmationStatusFilterTypeDef],
    },
)
TimeFilterTypeDef = TypedDict(
    "TimeFilterTypeDef",
    {
        "from": NotRequired[BlockchainInstantTypeDef],
        "to": NotRequired[BlockchainInstantTypeDef],
    },
)
BatchGetTokenBalanceInputItemTypeDef = TypedDict(
    "BatchGetTokenBalanceInputItemTypeDef",
    {
        "tokenIdentifier": TokenIdentifierTypeDef,
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "atBlockchainInstant": NotRequired[BlockchainInstantUnionTypeDef],
    },
)
ListFilteredTransactionEventsInputListFilteredTransactionEventsPaginateTypeDef = TypedDict(
    "ListFilteredTransactionEventsInputListFilteredTransactionEventsPaginateTypeDef",
    {
        "network": str,
        "addressIdentifierFilter": AddressIdentifierFilterTypeDef,
        "timeFilter": NotRequired[TimeFilterTypeDef],
        "voutFilter": NotRequired[VoutFilterTypeDef],
        "confirmationStatusFilter": NotRequired[ConfirmationStatusFilterTypeDef],
        "sort": NotRequired[ListFilteredTransactionEventsSortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFilteredTransactionEventsInputRequestTypeDef = TypedDict(
    "ListFilteredTransactionEventsInputRequestTypeDef",
    {
        "network": str,
        "addressIdentifierFilter": AddressIdentifierFilterTypeDef,
        "timeFilter": NotRequired[TimeFilterTypeDef],
        "voutFilter": NotRequired[VoutFilterTypeDef],
        "confirmationStatusFilter": NotRequired[ConfirmationStatusFilterTypeDef],
        "sort": NotRequired[ListFilteredTransactionEventsSortTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
BatchGetTokenBalanceInputRequestTypeDef = TypedDict(
    "BatchGetTokenBalanceInputRequestTypeDef",
    {
        "getTokenBalanceInputs": NotRequired[Sequence[BatchGetTokenBalanceInputItemTypeDef]],
    },
)
