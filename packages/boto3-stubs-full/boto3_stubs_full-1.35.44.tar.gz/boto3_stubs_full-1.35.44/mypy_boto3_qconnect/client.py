"""
Type annotations for qconnect service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qconnect.client import QConnectClient

    session = Session()
    client: QConnectClient = session.client("qconnect")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAIAgentsPaginator,
    ListAIAgentVersionsPaginator,
    ListAIPromptsPaginator,
    ListAIPromptVersionsPaginator,
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
from .type_defs import (
    CreateAIAgentRequestRequestTypeDef,
    CreateAIAgentResponseTypeDef,
    CreateAIAgentVersionRequestRequestTypeDef,
    CreateAIAgentVersionResponseTypeDef,
    CreateAIPromptRequestRequestTypeDef,
    CreateAIPromptResponseTypeDef,
    CreateAIPromptVersionRequestRequestTypeDef,
    CreateAIPromptVersionResponseTypeDef,
    CreateAssistantAssociationRequestRequestTypeDef,
    CreateAssistantAssociationResponseTypeDef,
    CreateAssistantRequestRequestTypeDef,
    CreateAssistantResponseTypeDef,
    CreateContentAssociationRequestRequestTypeDef,
    CreateContentAssociationResponseTypeDef,
    CreateContentRequestRequestTypeDef,
    CreateContentResponseTypeDef,
    CreateKnowledgeBaseRequestRequestTypeDef,
    CreateKnowledgeBaseResponseTypeDef,
    CreateQuickResponseRequestRequestTypeDef,
    CreateQuickResponseResponseTypeDef,
    CreateSessionRequestRequestTypeDef,
    CreateSessionResponseTypeDef,
    DeleteAIAgentRequestRequestTypeDef,
    DeleteAIAgentVersionRequestRequestTypeDef,
    DeleteAIPromptRequestRequestTypeDef,
    DeleteAIPromptVersionRequestRequestTypeDef,
    DeleteAssistantAssociationRequestRequestTypeDef,
    DeleteAssistantRequestRequestTypeDef,
    DeleteContentAssociationRequestRequestTypeDef,
    DeleteContentRequestRequestTypeDef,
    DeleteImportJobRequestRequestTypeDef,
    DeleteKnowledgeBaseRequestRequestTypeDef,
    DeleteQuickResponseRequestRequestTypeDef,
    GetAIAgentRequestRequestTypeDef,
    GetAIAgentResponseTypeDef,
    GetAIPromptRequestRequestTypeDef,
    GetAIPromptResponseTypeDef,
    GetAssistantAssociationRequestRequestTypeDef,
    GetAssistantAssociationResponseTypeDef,
    GetAssistantRequestRequestTypeDef,
    GetAssistantResponseTypeDef,
    GetContentAssociationRequestRequestTypeDef,
    GetContentAssociationResponseTypeDef,
    GetContentRequestRequestTypeDef,
    GetContentResponseTypeDef,
    GetContentSummaryRequestRequestTypeDef,
    GetContentSummaryResponseTypeDef,
    GetImportJobRequestRequestTypeDef,
    GetImportJobResponseTypeDef,
    GetKnowledgeBaseRequestRequestTypeDef,
    GetKnowledgeBaseResponseTypeDef,
    GetQuickResponseRequestRequestTypeDef,
    GetQuickResponseResponseTypeDef,
    GetRecommendationsRequestRequestTypeDef,
    GetRecommendationsResponseTypeDef,
    GetSessionRequestRequestTypeDef,
    GetSessionResponseTypeDef,
    ListAIAgentsRequestRequestTypeDef,
    ListAIAgentsResponseTypeDef,
    ListAIAgentVersionsRequestRequestTypeDef,
    ListAIAgentVersionsResponseTypeDef,
    ListAIPromptsRequestRequestTypeDef,
    ListAIPromptsResponseTypeDef,
    ListAIPromptVersionsRequestRequestTypeDef,
    ListAIPromptVersionsResponseTypeDef,
    ListAssistantAssociationsRequestRequestTypeDef,
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsRequestRequestTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentAssociationsRequestRequestTypeDef,
    ListContentAssociationsResponseTypeDef,
    ListContentsRequestRequestTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsRequestRequestTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesRequestRequestTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListQuickResponsesRequestRequestTypeDef,
    ListQuickResponsesResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    NotifyRecommendationsReceivedRequestRequestTypeDef,
    NotifyRecommendationsReceivedResponseTypeDef,
    PutFeedbackRequestRequestTypeDef,
    PutFeedbackResponseTypeDef,
    QueryAssistantRequestRequestTypeDef,
    QueryAssistantResponseTypeDef,
    RemoveAssistantAIAgentRequestRequestTypeDef,
    RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef,
    SearchContentRequestRequestTypeDef,
    SearchContentResponseTypeDef,
    SearchQuickResponsesRequestRequestTypeDef,
    SearchQuickResponsesResponseTypeDef,
    SearchSessionsRequestRequestTypeDef,
    SearchSessionsResponseTypeDef,
    StartContentUploadRequestRequestTypeDef,
    StartContentUploadResponseTypeDef,
    StartImportJobRequestRequestTypeDef,
    StartImportJobResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAIAgentRequestRequestTypeDef,
    UpdateAIAgentResponseTypeDef,
    UpdateAIPromptRequestRequestTypeDef,
    UpdateAIPromptResponseTypeDef,
    UpdateAssistantAIAgentRequestRequestTypeDef,
    UpdateAssistantAIAgentResponseTypeDef,
    UpdateContentRequestRequestTypeDef,
    UpdateContentResponseTypeDef,
    UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef,
    UpdateKnowledgeBaseTemplateUriResponseTypeDef,
    UpdateQuickResponseRequestRequestTypeDef,
    UpdateQuickResponseResponseTypeDef,
    UpdateSessionDataRequestRequestTypeDef,
    UpdateSessionDataResponseTypeDef,
    UpdateSessionRequestRequestTypeDef,
    UpdateSessionResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("QConnectClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class QConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#close)
        """

    def create_ai_agent(
        self, **kwargs: Unpack[CreateAIAgentRequestRequestTypeDef]
    ) -> CreateAIAgentResponseTypeDef:
        """
        Creates an Amazon Q in Connect AI Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_ai_agent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_agent)
        """

    def create_ai_agent_version(
        self, **kwargs: Unpack[CreateAIAgentVersionRequestRequestTypeDef]
    ) -> CreateAIAgentVersionResponseTypeDef:
        """
        Creates and Amazon Q in Connect AI Agent version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_ai_agent_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_agent_version)
        """

    def create_ai_prompt(
        self, **kwargs: Unpack[CreateAIPromptRequestRequestTypeDef]
    ) -> CreateAIPromptResponseTypeDef:
        """
        Creates an Amazon Q in Connect AI Prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_ai_prompt)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_prompt)
        """

    def create_ai_prompt_version(
        self, **kwargs: Unpack[CreateAIPromptVersionRequestRequestTypeDef]
    ) -> CreateAIPromptVersionResponseTypeDef:
        """
        Creates an Amazon Q in Connect AI Prompt version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_ai_prompt_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_ai_prompt_version)
        """

    def create_assistant(
        self, **kwargs: Unpack[CreateAssistantRequestRequestTypeDef]
    ) -> CreateAssistantResponseTypeDef:
        """
        Creates an Amazon Q in Connect assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_assistant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_assistant)
        """

    def create_assistant_association(
        self, **kwargs: Unpack[CreateAssistantAssociationRequestRequestTypeDef]
    ) -> CreateAssistantAssociationResponseTypeDef:
        """
        Creates an association between an Amazon Q in Connect assistant and another
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_assistant_association)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_assistant_association)
        """

    def create_content(
        self, **kwargs: Unpack[CreateContentRequestRequestTypeDef]
    ) -> CreateContentResponseTypeDef:
        """
        Creates Amazon Q in Connect content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_content)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_content)
        """

    def create_content_association(
        self, **kwargs: Unpack[CreateContentAssociationRequestRequestTypeDef]
    ) -> CreateContentAssociationResponseTypeDef:
        """
        Creates an association between a content resource in a knowledge base and
        [step-by-step
        guides](https://docs.aws.amazon.com/connect/latest/adminguide/step-by-step-guided-experiences.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_content_association)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_content_association)
        """

    def create_knowledge_base(
        self, **kwargs: Unpack[CreateKnowledgeBaseRequestRequestTypeDef]
    ) -> CreateKnowledgeBaseResponseTypeDef:
        """
        Creates a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_knowledge_base)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_knowledge_base)
        """

    def create_quick_response(
        self, **kwargs: Unpack[CreateQuickResponseRequestRequestTypeDef]
    ) -> CreateQuickResponseResponseTypeDef:
        """
        Creates an Amazon Q in Connect quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_quick_response)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_quick_response)
        """

    def create_session(
        self, **kwargs: Unpack[CreateSessionRequestRequestTypeDef]
    ) -> CreateSessionResponseTypeDef:
        """
        Creates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#create_session)
        """

    def delete_ai_agent(
        self, **kwargs: Unpack[DeleteAIAgentRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q in Connect AI Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_ai_agent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_agent)
        """

    def delete_ai_agent_version(
        self, **kwargs: Unpack[DeleteAIAgentVersionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q in Connect AI Agent Version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_ai_agent_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_agent_version)
        """

    def delete_ai_prompt(
        self, **kwargs: Unpack[DeleteAIPromptRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q in Connect AI Prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_ai_prompt)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_prompt)
        """

    def delete_ai_prompt_version(
        self, **kwargs: Unpack[DeleteAIPromptVersionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete and Amazon Q in Connect AI Prompt version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_ai_prompt_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_ai_prompt_version)
        """

    def delete_assistant(
        self, **kwargs: Unpack[DeleteAssistantRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_assistant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_assistant)
        """

    def delete_assistant_association(
        self, **kwargs: Unpack[DeleteAssistantAssociationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_assistant_association)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_assistant_association)
        """

    def delete_content(
        self, **kwargs: Unpack[DeleteContentRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_content)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_content)
        """

    def delete_content_association(
        self, **kwargs: Unpack[DeleteContentAssociationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the content association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_content_association)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_content_association)
        """

    def delete_import_job(
        self, **kwargs: Unpack[DeleteImportJobRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the quick response import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_import_job)
        """

    def delete_knowledge_base(
        self, **kwargs: Unpack[DeleteKnowledgeBaseRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_knowledge_base)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_knowledge_base)
        """

    def delete_quick_response(
        self, **kwargs: Unpack[DeleteQuickResponseRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_quick_response)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#delete_quick_response)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#generate_presigned_url)
        """

    def get_ai_agent(
        self, **kwargs: Unpack[GetAIAgentRequestRequestTypeDef]
    ) -> GetAIAgentResponseTypeDef:
        """
        Gets an Amazon Q in Connect AI Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_ai_agent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_ai_agent)
        """

    def get_ai_prompt(
        self, **kwargs: Unpack[GetAIPromptRequestRequestTypeDef]
    ) -> GetAIPromptResponseTypeDef:
        """
        Gets and Amazon Q in Connect AI Prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_ai_prompt)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_ai_prompt)
        """

    def get_assistant(
        self, **kwargs: Unpack[GetAssistantRequestRequestTypeDef]
    ) -> GetAssistantResponseTypeDef:
        """
        Retrieves information about an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_assistant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_assistant)
        """

    def get_assistant_association(
        self, **kwargs: Unpack[GetAssistantAssociationRequestRequestTypeDef]
    ) -> GetAssistantAssociationResponseTypeDef:
        """
        Retrieves information about an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_assistant_association)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_assistant_association)
        """

    def get_content(
        self, **kwargs: Unpack[GetContentRequestRequestTypeDef]
    ) -> GetContentResponseTypeDef:
        """
        Retrieves content, including a pre-signed URL to download the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_content)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_content)
        """

    def get_content_association(
        self, **kwargs: Unpack[GetContentAssociationRequestRequestTypeDef]
    ) -> GetContentAssociationResponseTypeDef:
        """
        Returns the content association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_content_association)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_content_association)
        """

    def get_content_summary(
        self, **kwargs: Unpack[GetContentSummaryRequestRequestTypeDef]
    ) -> GetContentSummaryResponseTypeDef:
        """
        Retrieves summary information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_content_summary)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_content_summary)
        """

    def get_import_job(
        self, **kwargs: Unpack[GetImportJobRequestRequestTypeDef]
    ) -> GetImportJobResponseTypeDef:
        """
        Retrieves the started import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_import_job)
        """

    def get_knowledge_base(
        self, **kwargs: Unpack[GetKnowledgeBaseRequestRequestTypeDef]
    ) -> GetKnowledgeBaseResponseTypeDef:
        """
        Retrieves information about the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_knowledge_base)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_knowledge_base)
        """

    def get_quick_response(
        self, **kwargs: Unpack[GetQuickResponseRequestRequestTypeDef]
    ) -> GetQuickResponseResponseTypeDef:
        """
        Retrieves the quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_quick_response)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_quick_response)
        """

    def get_recommendations(
        self, **kwargs: Unpack[GetRecommendationsRequestRequestTypeDef]
    ) -> GetRecommendationsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_recommendations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_recommendations)
        """

    def get_session(
        self, **kwargs: Unpack[GetSessionRequestRequestTypeDef]
    ) -> GetSessionResponseTypeDef:
        """
        Retrieves information for a specified session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_session)
        """

    def list_ai_agent_versions(
        self, **kwargs: Unpack[ListAIAgentVersionsRequestRequestTypeDef]
    ) -> ListAIAgentVersionsResponseTypeDef:
        """
        List AI Agent versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_ai_agent_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_agent_versions)
        """

    def list_ai_agents(
        self, **kwargs: Unpack[ListAIAgentsRequestRequestTypeDef]
    ) -> ListAIAgentsResponseTypeDef:
        """
        Lists AI Agents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_ai_agents)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_agents)
        """

    def list_ai_prompt_versions(
        self, **kwargs: Unpack[ListAIPromptVersionsRequestRequestTypeDef]
    ) -> ListAIPromptVersionsResponseTypeDef:
        """
        Lists AI Prompt versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_ai_prompt_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_prompt_versions)
        """

    def list_ai_prompts(
        self, **kwargs: Unpack[ListAIPromptsRequestRequestTypeDef]
    ) -> ListAIPromptsResponseTypeDef:
        """
        Lists the AI Prompts available on the Amazon Q in Connect assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_ai_prompts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_ai_prompts)
        """

    def list_assistant_associations(
        self, **kwargs: Unpack[ListAssistantAssociationsRequestRequestTypeDef]
    ) -> ListAssistantAssociationsResponseTypeDef:
        """
        Lists information about assistant associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_assistant_associations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_assistant_associations)
        """

    def list_assistants(
        self, **kwargs: Unpack[ListAssistantsRequestRequestTypeDef]
    ) -> ListAssistantsResponseTypeDef:
        """
        Lists information about assistants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_assistants)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_assistants)
        """

    def list_content_associations(
        self, **kwargs: Unpack[ListContentAssociationsRequestRequestTypeDef]
    ) -> ListContentAssociationsResponseTypeDef:
        """
        Lists the content associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_content_associations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_content_associations)
        """

    def list_contents(
        self, **kwargs: Unpack[ListContentsRequestRequestTypeDef]
    ) -> ListContentsResponseTypeDef:
        """
        Lists the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_contents)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_contents)
        """

    def list_import_jobs(
        self, **kwargs: Unpack[ListImportJobsRequestRequestTypeDef]
    ) -> ListImportJobsResponseTypeDef:
        """
        Lists information about import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_import_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_import_jobs)
        """

    def list_knowledge_bases(
        self, **kwargs: Unpack[ListKnowledgeBasesRequestRequestTypeDef]
    ) -> ListKnowledgeBasesResponseTypeDef:
        """
        Lists the knowledge bases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_knowledge_bases)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_knowledge_bases)
        """

    def list_quick_responses(
        self, **kwargs: Unpack[ListQuickResponsesRequestRequestTypeDef]
    ) -> ListQuickResponsesResponseTypeDef:
        """
        Lists information about quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_quick_responses)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_quick_responses)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#list_tags_for_resource)
        """

    def notify_recommendations_received(
        self, **kwargs: Unpack[NotifyRecommendationsReceivedRequestRequestTypeDef]
    ) -> NotifyRecommendationsReceivedResponseTypeDef:
        """
        Removes the specified recommendations from the specified assistant's queue of
        newly available
        recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.notify_recommendations_received)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#notify_recommendations_received)
        """

    def put_feedback(
        self, **kwargs: Unpack[PutFeedbackRequestRequestTypeDef]
    ) -> PutFeedbackResponseTypeDef:
        """
        Provides feedback against the specified assistant for the specified target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.put_feedback)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#put_feedback)
        """

    def query_assistant(
        self, **kwargs: Unpack[QueryAssistantRequestRequestTypeDef]
    ) -> QueryAssistantResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.query_assistant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#query_assistant)
        """

    def remove_assistant_ai_agent(
        self, **kwargs: Unpack[RemoveAssistantAIAgentRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the AI Agent that is set for use by defafult on an Amazon Q in Connect
        Assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.remove_assistant_ai_agent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#remove_assistant_ai_agent)
        """

    def remove_knowledge_base_template_uri(
        self, **kwargs: Unpack[RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a URI template from a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.remove_knowledge_base_template_uri)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#remove_knowledge_base_template_uri)
        """

    def search_content(
        self, **kwargs: Unpack[SearchContentRequestRequestTypeDef]
    ) -> SearchContentResponseTypeDef:
        """
        Searches for content in a specified knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.search_content)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#search_content)
        """

    def search_quick_responses(
        self, **kwargs: Unpack[SearchQuickResponsesRequestRequestTypeDef]
    ) -> SearchQuickResponsesResponseTypeDef:
        """
        Searches existing Amazon Q in Connect quick responses in an Amazon Q in Connect
        knowledge
        base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.search_quick_responses)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#search_quick_responses)
        """

    def search_sessions(
        self, **kwargs: Unpack[SearchSessionsRequestRequestTypeDef]
    ) -> SearchSessionsResponseTypeDef:
        """
        Searches for sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.search_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#search_sessions)
        """

    def start_content_upload(
        self, **kwargs: Unpack[StartContentUploadRequestRequestTypeDef]
    ) -> StartContentUploadResponseTypeDef:
        """
        Get a URL to upload content to a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.start_content_upload)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#start_content_upload)
        """

    def start_import_job(
        self, **kwargs: Unpack[StartImportJobRequestRequestTypeDef]
    ) -> StartImportJobResponseTypeDef:
        """
        Start an asynchronous job to import Amazon Q in Connect resources from an
        uploaded source
        file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.start_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#start_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#untag_resource)
        """

    def update_ai_agent(
        self, **kwargs: Unpack[UpdateAIAgentRequestRequestTypeDef]
    ) -> UpdateAIAgentResponseTypeDef:
        """
        Updates an AI Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_ai_agent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_ai_agent)
        """

    def update_ai_prompt(
        self, **kwargs: Unpack[UpdateAIPromptRequestRequestTypeDef]
    ) -> UpdateAIPromptResponseTypeDef:
        """
        Updates an AI Prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_ai_prompt)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_ai_prompt)
        """

    def update_assistant_ai_agent(
        self, **kwargs: Unpack[UpdateAssistantAIAgentRequestRequestTypeDef]
    ) -> UpdateAssistantAIAgentResponseTypeDef:
        """
        Updates the AI Agent that is set for use by defafult on an Amazon Q in Connect
        Assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_assistant_ai_agent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_assistant_ai_agent)
        """

    def update_content(
        self, **kwargs: Unpack[UpdateContentRequestRequestTypeDef]
    ) -> UpdateContentResponseTypeDef:
        """
        Updates information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_content)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_content)
        """

    def update_knowledge_base_template_uri(
        self, **kwargs: Unpack[UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef]
    ) -> UpdateKnowledgeBaseTemplateUriResponseTypeDef:
        """
        Updates the template URI of a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_knowledge_base_template_uri)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_knowledge_base_template_uri)
        """

    def update_quick_response(
        self, **kwargs: Unpack[UpdateQuickResponseRequestRequestTypeDef]
    ) -> UpdateQuickResponseResponseTypeDef:
        """
        Updates an existing Amazon Q in Connect quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_quick_response)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_quick_response)
        """

    def update_session(
        self, **kwargs: Unpack[UpdateSessionRequestRequestTypeDef]
    ) -> UpdateSessionResponseTypeDef:
        """
        Updates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_session)
        """

    def update_session_data(
        self, **kwargs: Unpack[UpdateSessionDataRequestRequestTypeDef]
    ) -> UpdateSessionDataResponseTypeDef:
        """
        Updates the data stored on an Amazon Q in Connect Session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_session_data)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#update_session_data)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ai_agent_versions"]
    ) -> ListAIAgentVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ai_agents"]) -> ListAIAgentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ai_prompt_versions"]
    ) -> ListAIPromptVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ai_prompts"]) -> ListAIPromptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assistant_associations"]
    ) -> ListAssistantAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_assistants"]) -> ListAssistantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_content_associations"]
    ) -> ListContentAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_contents"]) -> ListContentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_import_jobs"]) -> ListImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_knowledge_bases"]
    ) -> ListKnowledgeBasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_quick_responses"]
    ) -> ListQuickResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["query_assistant"]) -> QueryAssistantPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_content"]) -> SearchContentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_quick_responses"]
    ) -> SearchQuickResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_sessions"]) -> SearchSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/client/#get_paginator)
        """
