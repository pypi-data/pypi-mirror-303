"""
Type annotations for bedrock-agent-runtime service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient
    from mypy_boto3_bedrock_agent_runtime.paginator import (
        GetAgentMemoryPaginator,
        RetrievePaginator,
    )

    session = Session()
    client: AgentsforBedrockRuntimeClient = session.client("bedrock-agent-runtime")

    get_agent_memory_paginator: GetAgentMemoryPaginator = client.get_paginator("get_agent_memory")
    retrieve_paginator: RetrievePaginator = client.get_paginator("retrieve")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetAgentMemoryRequestGetAgentMemoryPaginateTypeDef,
    GetAgentMemoryResponseTypeDef,
    RetrieveRequestRetrievePaginateTypeDef,
    RetrieveResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("GetAgentMemoryPaginator", "RetrievePaginator")

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class GetAgentMemoryPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.GetAgentMemory)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#getagentmemorypaginator)
    """
    def paginate(
        self, **kwargs: Unpack[GetAgentMemoryRequestGetAgentMemoryPaginateTypeDef]
    ) -> _PageIterator[GetAgentMemoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.GetAgentMemory.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#getagentmemorypaginator)
        """

class RetrievePaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.Retrieve)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#retrievepaginator)
    """
    def paginate(
        self, **kwargs: Unpack[RetrieveRequestRetrievePaginateTypeDef]
    ) -> _PageIterator[RetrieveResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.Retrieve.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#retrievepaginator)
        """
