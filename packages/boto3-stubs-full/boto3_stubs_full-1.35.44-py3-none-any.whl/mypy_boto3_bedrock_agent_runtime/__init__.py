"""
Main interface for bedrock-agent-runtime service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_agent_runtime import (
        AgentsforBedrockRuntimeClient,
        Client,
        GetAgentMemoryPaginator,
        RetrievePaginator,
    )

    session = Session()
    client: AgentsforBedrockRuntimeClient = session.client("bedrock-agent-runtime")

    get_agent_memory_paginator: GetAgentMemoryPaginator = client.get_paginator("get_agent_memory")
    retrieve_paginator: RetrievePaginator = client.get_paginator("retrieve")
    ```
"""

from .client import AgentsforBedrockRuntimeClient
from .paginator import GetAgentMemoryPaginator, RetrievePaginator

Client = AgentsforBedrockRuntimeClient


__all__ = (
    "AgentsforBedrockRuntimeClient",
    "Client",
    "GetAgentMemoryPaginator",
    "RetrievePaginator",
)
