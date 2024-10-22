"""
Type annotations for migrationhuborchestrator service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_migrationhuborchestrator.client import MigrationHubOrchestratorClient

    session = Session()
    client: MigrationHubOrchestratorClient = session.client("migrationhuborchestrator")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListPluginsPaginator,
    ListTemplatesPaginator,
    ListTemplateStepGroupsPaginator,
    ListTemplateStepsPaginator,
    ListWorkflowsPaginator,
    ListWorkflowStepGroupsPaginator,
    ListWorkflowStepsPaginator,
)
from .type_defs import (
    CreateMigrationWorkflowRequestRequestTypeDef,
    CreateMigrationWorkflowResponseTypeDef,
    CreateTemplateRequestRequestTypeDef,
    CreateTemplateResponseTypeDef,
    CreateWorkflowStepGroupRequestRequestTypeDef,
    CreateWorkflowStepGroupResponseTypeDef,
    CreateWorkflowStepRequestRequestTypeDef,
    CreateWorkflowStepResponseTypeDef,
    DeleteMigrationWorkflowRequestRequestTypeDef,
    DeleteMigrationWorkflowResponseTypeDef,
    DeleteTemplateRequestRequestTypeDef,
    DeleteWorkflowStepGroupRequestRequestTypeDef,
    DeleteWorkflowStepRequestRequestTypeDef,
    GetMigrationWorkflowRequestRequestTypeDef,
    GetMigrationWorkflowResponseTypeDef,
    GetMigrationWorkflowTemplateRequestRequestTypeDef,
    GetMigrationWorkflowTemplateResponseTypeDef,
    GetTemplateStepGroupRequestRequestTypeDef,
    GetTemplateStepGroupResponseTypeDef,
    GetTemplateStepRequestRequestTypeDef,
    GetTemplateStepResponseTypeDef,
    GetWorkflowStepGroupRequestRequestTypeDef,
    GetWorkflowStepGroupResponseTypeDef,
    GetWorkflowStepRequestRequestTypeDef,
    GetWorkflowStepResponseTypeDef,
    ListMigrationWorkflowsRequestRequestTypeDef,
    ListMigrationWorkflowsResponseTypeDef,
    ListMigrationWorkflowTemplatesRequestRequestTypeDef,
    ListMigrationWorkflowTemplatesResponseTypeDef,
    ListPluginsRequestRequestTypeDef,
    ListPluginsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateStepGroupsRequestRequestTypeDef,
    ListTemplateStepGroupsResponseTypeDef,
    ListTemplateStepsRequestRequestTypeDef,
    ListTemplateStepsResponseTypeDef,
    ListWorkflowStepGroupsRequestRequestTypeDef,
    ListWorkflowStepGroupsResponseTypeDef,
    ListWorkflowStepsRequestRequestTypeDef,
    ListWorkflowStepsResponseTypeDef,
    RetryWorkflowStepRequestRequestTypeDef,
    RetryWorkflowStepResponseTypeDef,
    StartMigrationWorkflowRequestRequestTypeDef,
    StartMigrationWorkflowResponseTypeDef,
    StopMigrationWorkflowRequestRequestTypeDef,
    StopMigrationWorkflowResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateMigrationWorkflowRequestRequestTypeDef,
    UpdateMigrationWorkflowResponseTypeDef,
    UpdateTemplateRequestRequestTypeDef,
    UpdateTemplateResponseTypeDef,
    UpdateWorkflowStepGroupRequestRequestTypeDef,
    UpdateWorkflowStepGroupResponseTypeDef,
    UpdateWorkflowStepRequestRequestTypeDef,
    UpdateWorkflowStepResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("MigrationHubOrchestratorClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class MigrationHubOrchestratorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MigrationHubOrchestratorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#close)
        """

    def create_template(
        self, **kwargs: Unpack[CreateTemplateRequestRequestTypeDef]
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates a migration workflow template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#create_template)
        """

    def create_workflow(
        self, **kwargs: Unpack[CreateMigrationWorkflowRequestRequestTypeDef]
    ) -> CreateMigrationWorkflowResponseTypeDef:
        """
        Create a workflow to orchestrate your migrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#create_workflow)
        """

    def create_workflow_step(
        self, **kwargs: Unpack[CreateWorkflowStepRequestRequestTypeDef]
    ) -> CreateWorkflowStepResponseTypeDef:
        """
        Create a step in the migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow_step)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#create_workflow_step)
        """

    def create_workflow_step_group(
        self, **kwargs: Unpack[CreateWorkflowStepGroupRequestRequestTypeDef]
    ) -> CreateWorkflowStepGroupResponseTypeDef:
        """
        Create a step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow_step_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#create_workflow_step_group)
        """

    def delete_template(
        self, **kwargs: Unpack[DeleteTemplateRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a migration workflow template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#delete_template)
        """

    def delete_workflow(
        self, **kwargs: Unpack[DeleteMigrationWorkflowRequestRequestTypeDef]
    ) -> DeleteMigrationWorkflowResponseTypeDef:
        """
        Delete a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#delete_workflow)
        """

    def delete_workflow_step(
        self, **kwargs: Unpack[DeleteWorkflowStepRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow_step)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#delete_workflow_step)
        """

    def delete_workflow_step_group(
        self, **kwargs: Unpack[DeleteWorkflowStepGroupRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow_step_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#delete_workflow_step_group)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#generate_presigned_url)
        """

    def get_template(
        self, **kwargs: Unpack[GetMigrationWorkflowTemplateRequestRequestTypeDef]
    ) -> GetMigrationWorkflowTemplateResponseTypeDef:
        """
        Get the template you want to use for creating a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_template)
        """

    def get_template_step(
        self, **kwargs: Unpack[GetTemplateStepRequestRequestTypeDef]
    ) -> GetTemplateStepResponseTypeDef:
        """
        Get a specific step in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template_step)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_template_step)
        """

    def get_template_step_group(
        self, **kwargs: Unpack[GetTemplateStepGroupRequestRequestTypeDef]
    ) -> GetTemplateStepGroupResponseTypeDef:
        """
        Get a step group in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template_step_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_template_step_group)
        """

    def get_workflow(
        self, **kwargs: Unpack[GetMigrationWorkflowRequestRequestTypeDef]
    ) -> GetMigrationWorkflowResponseTypeDef:
        """
        Get migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_workflow)
        """

    def get_workflow_step(
        self, **kwargs: Unpack[GetWorkflowStepRequestRequestTypeDef]
    ) -> GetWorkflowStepResponseTypeDef:
        """
        Get a step in the migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow_step)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_workflow_step)
        """

    def get_workflow_step_group(
        self, **kwargs: Unpack[GetWorkflowStepGroupRequestRequestTypeDef]
    ) -> GetWorkflowStepGroupResponseTypeDef:
        """
        Get the step group of a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow_step_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_workflow_step_group)
        """

    def list_plugins(
        self, **kwargs: Unpack[ListPluginsRequestRequestTypeDef]
    ) -> ListPluginsResponseTypeDef:
        """
        List AWS Migration Hub Orchestrator plugins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_plugins)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_plugins)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags added to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_tags_for_resource)
        """

    def list_template_step_groups(
        self, **kwargs: Unpack[ListTemplateStepGroupsRequestRequestTypeDef]
    ) -> ListTemplateStepGroupsResponseTypeDef:
        """
        List the step groups in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_template_step_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_template_step_groups)
        """

    def list_template_steps(
        self, **kwargs: Unpack[ListTemplateStepsRequestRequestTypeDef]
    ) -> ListTemplateStepsResponseTypeDef:
        """
        List the steps in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_template_steps)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_template_steps)
        """

    def list_templates(
        self, **kwargs: Unpack[ListMigrationWorkflowTemplatesRequestRequestTypeDef]
    ) -> ListMigrationWorkflowTemplatesResponseTypeDef:
        """
        List the templates available in Migration Hub Orchestrator to create a
        migration
        workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_templates)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_templates)
        """

    def list_workflow_step_groups(
        self, **kwargs: Unpack[ListWorkflowStepGroupsRequestRequestTypeDef]
    ) -> ListWorkflowStepGroupsResponseTypeDef:
        """
        List the step groups in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflow_step_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_workflow_step_groups)
        """

    def list_workflow_steps(
        self, **kwargs: Unpack[ListWorkflowStepsRequestRequestTypeDef]
    ) -> ListWorkflowStepsResponseTypeDef:
        """
        List the steps in a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflow_steps)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_workflow_steps)
        """

    def list_workflows(
        self, **kwargs: Unpack[ListMigrationWorkflowsRequestRequestTypeDef]
    ) -> ListMigrationWorkflowsResponseTypeDef:
        """
        List the migration workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflows)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_workflows)
        """

    def retry_workflow_step(
        self, **kwargs: Unpack[RetryWorkflowStepRequestRequestTypeDef]
    ) -> RetryWorkflowStepResponseTypeDef:
        """
        Retry a failed step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.retry_workflow_step)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#retry_workflow_step)
        """

    def start_workflow(
        self, **kwargs: Unpack[StartMigrationWorkflowRequestRequestTypeDef]
    ) -> StartMigrationWorkflowResponseTypeDef:
        """
        Start a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.start_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#start_workflow)
        """

    def stop_workflow(
        self, **kwargs: Unpack[StopMigrationWorkflowRequestRequestTypeDef]
    ) -> StopMigrationWorkflowResponseTypeDef:
        """
        Stop an ongoing migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.stop_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#stop_workflow)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Tag a resource by specifying its Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#untag_resource)
        """

    def update_template(
        self, **kwargs: Unpack[UpdateTemplateRequestRequestTypeDef]
    ) -> UpdateTemplateResponseTypeDef:
        """
        Updates a migration workflow template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#update_template)
        """

    def update_workflow(
        self, **kwargs: Unpack[UpdateMigrationWorkflowRequestRequestTypeDef]
    ) -> UpdateMigrationWorkflowResponseTypeDef:
        """
        Update a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#update_workflow)
        """

    def update_workflow_step(
        self, **kwargs: Unpack[UpdateWorkflowStepRequestRequestTypeDef]
    ) -> UpdateWorkflowStepResponseTypeDef:
        """
        Update a step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow_step)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#update_workflow_step)
        """

    def update_workflow_step_group(
        self, **kwargs: Unpack[UpdateWorkflowStepGroupRequestRequestTypeDef]
    ) -> UpdateWorkflowStepGroupResponseTypeDef:
        """
        Update the step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow_step_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#update_workflow_step_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_plugins"]) -> ListPluginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_step_groups"]
    ) -> ListTemplateStepGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_steps"]
    ) -> ListTemplateStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_step_groups"]
    ) -> ListWorkflowStepGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_steps"]
    ) -> ListWorkflowStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workflows"]) -> ListWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """
