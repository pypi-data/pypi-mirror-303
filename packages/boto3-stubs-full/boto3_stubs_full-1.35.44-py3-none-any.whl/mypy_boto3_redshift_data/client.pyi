"""
Type annotations for redshift-data service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_redshift_data.client import RedshiftDataAPIServiceClient

    session = Session()
    client: RedshiftDataAPIServiceClient = session.client("redshift-data")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeTablePaginator,
    GetStatementResultPaginator,
    ListDatabasesPaginator,
    ListSchemasPaginator,
    ListStatementsPaginator,
    ListTablesPaginator,
)
from .type_defs import (
    BatchExecuteStatementInputRequestTypeDef,
    BatchExecuteStatementOutputTypeDef,
    CancelStatementRequestRequestTypeDef,
    CancelStatementResponseTypeDef,
    DescribeStatementRequestRequestTypeDef,
    DescribeStatementResponseTypeDef,
    DescribeTableRequestRequestTypeDef,
    DescribeTableResponseTypeDef,
    ExecuteStatementInputRequestTypeDef,
    ExecuteStatementOutputTypeDef,
    GetStatementResultRequestRequestTypeDef,
    GetStatementResultResponseTypeDef,
    ListDatabasesRequestRequestTypeDef,
    ListDatabasesResponseTypeDef,
    ListSchemasRequestRequestTypeDef,
    ListSchemasResponseTypeDef,
    ListStatementsRequestRequestTypeDef,
    ListStatementsResponseTypeDef,
    ListTablesRequestRequestTypeDef,
    ListTablesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("RedshiftDataAPIServiceClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ActiveSessionsExceededException: Type[BotocoreClientError]
    ActiveStatementsExceededException: Type[BotocoreClientError]
    BatchExecuteStatementException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DatabaseConnectionException: Type[BotocoreClientError]
    ExecuteStatementException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    QueryTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RedshiftDataAPIServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RedshiftDataAPIServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#exceptions)
        """

    def batch_execute_statement(
        self, **kwargs: Unpack[BatchExecuteStatementInputRequestTypeDef]
    ) -> BatchExecuteStatementOutputTypeDef:
        """
        Runs one or more SQL statements, which can be data manipulation language (DML)
        or data definition language
        (DDL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.batch_execute_statement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#batch_execute_statement)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#can_paginate)
        """

    def cancel_statement(
        self, **kwargs: Unpack[CancelStatementRequestRequestTypeDef]
    ) -> CancelStatementResponseTypeDef:
        """
        Cancels a running query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.cancel_statement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#cancel_statement)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#close)
        """

    def describe_statement(
        self, **kwargs: Unpack[DescribeStatementRequestRequestTypeDef]
    ) -> DescribeStatementResponseTypeDef:
        """
        Describes the details about a specific instance when a query was run by the
        Amazon Redshift Data
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_statement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#describe_statement)
        """

    def describe_table(
        self, **kwargs: Unpack[DescribeTableRequestRequestTypeDef]
    ) -> DescribeTableResponseTypeDef:
        """
        Describes the detailed information about a table from metadata in the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_table)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#describe_table)
        """

    def execute_statement(
        self, **kwargs: Unpack[ExecuteStatementInputRequestTypeDef]
    ) -> ExecuteStatementOutputTypeDef:
        """
        Runs an SQL statement, which can be data manipulation language (DML) or data
        definition language
        (DDL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.execute_statement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#execute_statement)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#generate_presigned_url)
        """

    def get_statement_result(
        self, **kwargs: Unpack[GetStatementResultRequestRequestTypeDef]
    ) -> GetStatementResultResponseTypeDef:
        """
        Fetches the temporarily cached result of an SQL statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_statement_result)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_statement_result)
        """

    def list_databases(
        self, **kwargs: Unpack[ListDatabasesRequestRequestTypeDef]
    ) -> ListDatabasesResponseTypeDef:
        """
        List the databases in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_databases)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#list_databases)
        """

    def list_schemas(
        self, **kwargs: Unpack[ListSchemasRequestRequestTypeDef]
    ) -> ListSchemasResponseTypeDef:
        """
        Lists the schemas in a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_schemas)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#list_schemas)
        """

    def list_statements(
        self, **kwargs: Unpack[ListStatementsRequestRequestTypeDef]
    ) -> ListStatementsResponseTypeDef:
        """
        List of SQL statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_statements)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#list_statements)
        """

    def list_tables(
        self, **kwargs: Unpack[ListTablesRequestRequestTypeDef]
    ) -> ListTablesResponseTypeDef:
        """
        List the tables in a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_tables)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#list_tables)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_table"]) -> DescribeTablePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_statement_result"]
    ) -> GetStatementResultPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_statements"]) -> ListStatementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """
