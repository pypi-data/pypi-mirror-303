"""
Type annotations for qconnect service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_qconnect.client import QConnectClient
    from mypy_boto3_qconnect.paginator import (
        ListAIAgentVersionsPaginator,
        ListAIAgentsPaginator,
        ListAIPromptVersionsPaginator,
        ListAIPromptsPaginator,
        ListAssistantAssociationsPaginator,
        ListAssistantsPaginator,
        ListContentAssociationsPaginator,
        ListContentsPaginator,
        ListImportJobsPaginator,
        ListKnowledgeBasesPaginator,
        ListQuickResponsesPaginator,
        QueryAssistantPaginator,
        SearchContentPaginator,
        SearchQuickResponsesPaginator,
        SearchSessionsPaginator,
    )

    session = Session()
    client: QConnectClient = session.client("qconnect")

    list_ai_agent_versions_paginator: ListAIAgentVersionsPaginator = client.get_paginator("list_ai_agent_versions")
    list_ai_agents_paginator: ListAIAgentsPaginator = client.get_paginator("list_ai_agents")
    list_ai_prompt_versions_paginator: ListAIPromptVersionsPaginator = client.get_paginator("list_ai_prompt_versions")
    list_ai_prompts_paginator: ListAIPromptsPaginator = client.get_paginator("list_ai_prompts")
    list_assistant_associations_paginator: ListAssistantAssociationsPaginator = client.get_paginator("list_assistant_associations")
    list_assistants_paginator: ListAssistantsPaginator = client.get_paginator("list_assistants")
    list_content_associations_paginator: ListContentAssociationsPaginator = client.get_paginator("list_content_associations")
    list_contents_paginator: ListContentsPaginator = client.get_paginator("list_contents")
    list_import_jobs_paginator: ListImportJobsPaginator = client.get_paginator("list_import_jobs")
    list_knowledge_bases_paginator: ListKnowledgeBasesPaginator = client.get_paginator("list_knowledge_bases")
    list_quick_responses_paginator: ListQuickResponsesPaginator = client.get_paginator("list_quick_responses")
    query_assistant_paginator: QueryAssistantPaginator = client.get_paginator("query_assistant")
    search_content_paginator: SearchContentPaginator = client.get_paginator("search_content")
    search_quick_responses_paginator: SearchQuickResponsesPaginator = client.get_paginator("search_quick_responses")
    search_sessions_paginator: SearchSessionsPaginator = client.get_paginator("search_sessions")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAIAgentsRequestListAIAgentsPaginateTypeDef,
    ListAIAgentsResponseTypeDef,
    ListAIAgentVersionsRequestListAIAgentVersionsPaginateTypeDef,
    ListAIAgentVersionsResponseTypeDef,
    ListAIPromptsRequestListAIPromptsPaginateTypeDef,
    ListAIPromptsResponseTypeDef,
    ListAIPromptVersionsRequestListAIPromptVersionsPaginateTypeDef,
    ListAIPromptVersionsResponseTypeDef,
    ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef,
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsRequestListAssistantsPaginateTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentAssociationsRequestListContentAssociationsPaginateTypeDef,
    ListContentAssociationsResponseTypeDef,
    ListContentsRequestListContentsPaginateTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsRequestListImportJobsPaginateTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListQuickResponsesRequestListQuickResponsesPaginateTypeDef,
    ListQuickResponsesResponseTypeDef,
    QueryAssistantRequestQueryAssistantPaginateTypeDef,
    QueryAssistantResponsePaginatorTypeDef,
    SearchContentRequestSearchContentPaginateTypeDef,
    SearchContentResponseTypeDef,
    SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef,
    SearchQuickResponsesResponseTypeDef,
    SearchSessionsRequestSearchSessionsPaginateTypeDef,
    SearchSessionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAIAgentVersionsPaginator",
    "ListAIAgentsPaginator",
    "ListAIPromptVersionsPaginator",
    "ListAIPromptsPaginator",
    "ListAssistantAssociationsPaginator",
    "ListAssistantsPaginator",
    "ListContentAssociationsPaginator",
    "ListContentsPaginator",
    "ListImportJobsPaginator",
    "ListKnowledgeBasesPaginator",
    "ListQuickResponsesPaginator",
    "QueryAssistantPaginator",
    "SearchContentPaginator",
    "SearchQuickResponsesPaginator",
    "SearchSessionsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListAIAgentVersionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAIAgentVersions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiagentversionspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAIAgentVersionsRequestListAIAgentVersionsPaginateTypeDef]
    ) -> _PageIterator[ListAIAgentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAIAgentVersions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiagentversionspaginator)
        """

class ListAIAgentsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAIAgents)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiagentspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAIAgentsRequestListAIAgentsPaginateTypeDef]
    ) -> _PageIterator[ListAIAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAIAgents.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiagentspaginator)
        """

class ListAIPromptVersionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAIPromptVersions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaipromptversionspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAIPromptVersionsRequestListAIPromptVersionsPaginateTypeDef]
    ) -> _PageIterator[ListAIPromptVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAIPromptVersions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaipromptversionspaginator)
        """

class ListAIPromptsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAIPrompts)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaipromptspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAIPromptsRequestListAIPromptsPaginateTypeDef]
    ) -> _PageIterator[ListAIPromptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAIPrompts.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaipromptspaginator)
        """

class ListAssistantAssociationsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAssistantAssociations)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listassistantassociationspaginator)
    """
    def paginate(
        self,
        **kwargs: Unpack[ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef],
    ) -> _PageIterator[ListAssistantAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAssistantAssociations.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listassistantassociationspaginator)
        """

class ListAssistantsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAssistants)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listassistantspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAssistantsRequestListAssistantsPaginateTypeDef]
    ) -> _PageIterator[ListAssistantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAssistants.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listassistantspaginator)
        """

class ListContentAssociationsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListContentAssociations)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listcontentassociationspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListContentAssociationsRequestListContentAssociationsPaginateTypeDef]
    ) -> _PageIterator[ListContentAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListContentAssociations.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listcontentassociationspaginator)
        """

class ListContentsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListContents)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listcontentspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListContentsRequestListContentsPaginateTypeDef]
    ) -> _PageIterator[ListContentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListContents.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listcontentspaginator)
        """

class ListImportJobsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListImportJobs)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listimportjobspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListImportJobsRequestListImportJobsPaginateTypeDef]
    ) -> _PageIterator[ListImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListImportJobs.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listimportjobspaginator)
        """

class ListKnowledgeBasesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListKnowledgeBases)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listknowledgebasespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef]
    ) -> _PageIterator[ListKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListKnowledgeBases.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listknowledgebasespaginator)
        """

class ListQuickResponsesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListQuickResponses)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listquickresponsespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListQuickResponsesRequestListQuickResponsesPaginateTypeDef]
    ) -> _PageIterator[ListQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListQuickResponses.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listquickresponsespaginator)
        """

class QueryAssistantPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.QueryAssistant)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#queryassistantpaginator)
    """
    def paginate(
        self, **kwargs: Unpack[QueryAssistantRequestQueryAssistantPaginateTypeDef]
    ) -> _PageIterator[QueryAssistantResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.QueryAssistant.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#queryassistantpaginator)
        """

class SearchContentPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchContent)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchcontentpaginator)
    """
    def paginate(
        self, **kwargs: Unpack[SearchContentRequestSearchContentPaginateTypeDef]
    ) -> _PageIterator[SearchContentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchContent.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchcontentpaginator)
        """

class SearchQuickResponsesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchQuickResponses)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchquickresponsespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef]
    ) -> _PageIterator[SearchQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchQuickResponses.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchquickresponsespaginator)
        """

class SearchSessionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchSessions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchsessionspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[SearchSessionsRequestSearchSessionsPaginateTypeDef]
    ) -> _PageIterator[SearchSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchSessions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchsessionspaginator)
        """
