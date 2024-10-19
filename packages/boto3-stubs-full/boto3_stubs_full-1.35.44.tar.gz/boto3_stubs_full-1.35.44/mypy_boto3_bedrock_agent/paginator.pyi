"""
Type annotations for bedrock-agent service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock_agent.client import AgentsforBedrockClient
    from mypy_boto3_bedrock_agent.paginator import (
        ListAgentActionGroupsPaginator,
        ListAgentAliasesPaginator,
        ListAgentKnowledgeBasesPaginator,
        ListAgentVersionsPaginator,
        ListAgentsPaginator,
        ListDataSourcesPaginator,
        ListFlowAliasesPaginator,
        ListFlowVersionsPaginator,
        ListFlowsPaginator,
        ListIngestionJobsPaginator,
        ListKnowledgeBasesPaginator,
        ListPromptsPaginator,
    )

    session = Session()
    client: AgentsforBedrockClient = session.client("bedrock-agent")

    list_agent_action_groups_paginator: ListAgentActionGroupsPaginator = client.get_paginator("list_agent_action_groups")
    list_agent_aliases_paginator: ListAgentAliasesPaginator = client.get_paginator("list_agent_aliases")
    list_agent_knowledge_bases_paginator: ListAgentKnowledgeBasesPaginator = client.get_paginator("list_agent_knowledge_bases")
    list_agent_versions_paginator: ListAgentVersionsPaginator = client.get_paginator("list_agent_versions")
    list_agents_paginator: ListAgentsPaginator = client.get_paginator("list_agents")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_flow_aliases_paginator: ListFlowAliasesPaginator = client.get_paginator("list_flow_aliases")
    list_flow_versions_paginator: ListFlowVersionsPaginator = client.get_paginator("list_flow_versions")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
    list_ingestion_jobs_paginator: ListIngestionJobsPaginator = client.get_paginator("list_ingestion_jobs")
    list_knowledge_bases_paginator: ListKnowledgeBasesPaginator = client.get_paginator("list_knowledge_bases")
    list_prompts_paginator: ListPromptsPaginator = client.get_paginator("list_prompts")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAgentActionGroupsRequestListAgentActionGroupsPaginateTypeDef,
    ListAgentActionGroupsResponseTypeDef,
    ListAgentAliasesRequestListAgentAliasesPaginateTypeDef,
    ListAgentAliasesResponseTypeDef,
    ListAgentKnowledgeBasesRequestListAgentKnowledgeBasesPaginateTypeDef,
    ListAgentKnowledgeBasesResponseTypeDef,
    ListAgentsRequestListAgentsPaginateTypeDef,
    ListAgentsResponseTypeDef,
    ListAgentVersionsRequestListAgentVersionsPaginateTypeDef,
    ListAgentVersionsResponseTypeDef,
    ListDataSourcesRequestListDataSourcesPaginateTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFlowAliasesRequestListFlowAliasesPaginateTypeDef,
    ListFlowAliasesResponseTypeDef,
    ListFlowsRequestListFlowsPaginateTypeDef,
    ListFlowsResponseTypeDef,
    ListFlowVersionsRequestListFlowVersionsPaginateTypeDef,
    ListFlowVersionsResponseTypeDef,
    ListIngestionJobsRequestListIngestionJobsPaginateTypeDef,
    ListIngestionJobsResponseTypeDef,
    ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListPromptsRequestListPromptsPaginateTypeDef,
    ListPromptsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAgentActionGroupsPaginator",
    "ListAgentAliasesPaginator",
    "ListAgentKnowledgeBasesPaginator",
    "ListAgentVersionsPaginator",
    "ListAgentsPaginator",
    "ListDataSourcesPaginator",
    "ListFlowAliasesPaginator",
    "ListFlowVersionsPaginator",
    "ListFlowsPaginator",
    "ListIngestionJobsPaginator",
    "ListKnowledgeBasesPaginator",
    "ListPromptsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListAgentActionGroupsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentActionGroups)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentactiongroupspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAgentActionGroupsRequestListAgentActionGroupsPaginateTypeDef]
    ) -> _PageIterator[ListAgentActionGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentActionGroups.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentactiongroupspaginator)
        """

class ListAgentAliasesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentAliases)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentaliasespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAgentAliasesRequestListAgentAliasesPaginateTypeDef]
    ) -> _PageIterator[ListAgentAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentAliases.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentaliasespaginator)
        """

class ListAgentKnowledgeBasesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentKnowledgeBases)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentknowledgebasespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAgentKnowledgeBasesRequestListAgentKnowledgeBasesPaginateTypeDef]
    ) -> _PageIterator[ListAgentKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentKnowledgeBases.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentknowledgebasespaginator)
        """

class ListAgentVersionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentVersions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentversionspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAgentVersionsRequestListAgentVersionsPaginateTypeDef]
    ) -> _PageIterator[ListAgentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentVersions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentversionspaginator)
        """

class ListAgentsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgents)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAgentsRequestListAgentsPaginateTypeDef]
    ) -> _PageIterator[ListAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgents.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentspaginator)
        """

class ListDataSourcesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListDataSources)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listdatasourcespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListDataSourcesRequestListDataSourcesPaginateTypeDef]
    ) -> _PageIterator[ListDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListDataSources.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listdatasourcespaginator)
        """

class ListFlowAliasesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListFlowAliases)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowaliasespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListFlowAliasesRequestListFlowAliasesPaginateTypeDef]
    ) -> _PageIterator[ListFlowAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListFlowAliases.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowaliasespaginator)
        """

class ListFlowVersionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListFlowVersions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowversionspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListFlowVersionsRequestListFlowVersionsPaginateTypeDef]
    ) -> _PageIterator[ListFlowVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListFlowVersions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowversionspaginator)
        """

class ListFlowsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListFlows)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListFlowsRequestListFlowsPaginateTypeDef]
    ) -> _PageIterator[ListFlowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListFlows.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowspaginator)
        """

class ListIngestionJobsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListIngestionJobs)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listingestionjobspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListIngestionJobsRequestListIngestionJobsPaginateTypeDef]
    ) -> _PageIterator[ListIngestionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListIngestionJobs.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listingestionjobspaginator)
        """

class ListKnowledgeBasesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListKnowledgeBases)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listknowledgebasespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef]
    ) -> _PageIterator[ListKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListKnowledgeBases.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listknowledgebasespaginator)
        """

class ListPromptsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListPrompts)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listpromptspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListPromptsRequestListPromptsPaginateTypeDef]
    ) -> _PageIterator[ListPromptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListPrompts.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listpromptspaginator)
        """
