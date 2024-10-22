"""
Type annotations for robomaker service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_robomaker.client import RoboMakerClient

    session = Session()
    client: RoboMakerClient = session.client("robomaker")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListDeploymentJobsPaginator,
    ListFleetsPaginator,
    ListRobotApplicationsPaginator,
    ListRobotsPaginator,
    ListSimulationApplicationsPaginator,
    ListSimulationJobBatchesPaginator,
    ListSimulationJobsPaginator,
    ListWorldExportJobsPaginator,
    ListWorldGenerationJobsPaginator,
    ListWorldsPaginator,
    ListWorldTemplatesPaginator,
)
from .type_defs import (
    BatchDeleteWorldsRequestRequestTypeDef,
    BatchDeleteWorldsResponseTypeDef,
    BatchDescribeSimulationJobRequestRequestTypeDef,
    BatchDescribeSimulationJobResponseTypeDef,
    CancelDeploymentJobRequestRequestTypeDef,
    CancelSimulationJobBatchRequestRequestTypeDef,
    CancelSimulationJobRequestRequestTypeDef,
    CancelWorldExportJobRequestRequestTypeDef,
    CancelWorldGenerationJobRequestRequestTypeDef,
    CreateDeploymentJobRequestRequestTypeDef,
    CreateDeploymentJobResponseTypeDef,
    CreateFleetRequestRequestTypeDef,
    CreateFleetResponseTypeDef,
    CreateRobotApplicationRequestRequestTypeDef,
    CreateRobotApplicationResponseTypeDef,
    CreateRobotApplicationVersionRequestRequestTypeDef,
    CreateRobotApplicationVersionResponseTypeDef,
    CreateRobotRequestRequestTypeDef,
    CreateRobotResponseTypeDef,
    CreateSimulationApplicationRequestRequestTypeDef,
    CreateSimulationApplicationResponseTypeDef,
    CreateSimulationApplicationVersionRequestRequestTypeDef,
    CreateSimulationApplicationVersionResponseTypeDef,
    CreateSimulationJobRequestRequestTypeDef,
    CreateSimulationJobResponseTypeDef,
    CreateWorldExportJobRequestRequestTypeDef,
    CreateWorldExportJobResponseTypeDef,
    CreateWorldGenerationJobRequestRequestTypeDef,
    CreateWorldGenerationJobResponseTypeDef,
    CreateWorldTemplateRequestRequestTypeDef,
    CreateWorldTemplateResponseTypeDef,
    DeleteFleetRequestRequestTypeDef,
    DeleteRobotApplicationRequestRequestTypeDef,
    DeleteRobotRequestRequestTypeDef,
    DeleteSimulationApplicationRequestRequestTypeDef,
    DeleteWorldTemplateRequestRequestTypeDef,
    DeregisterRobotRequestRequestTypeDef,
    DeregisterRobotResponseTypeDef,
    DescribeDeploymentJobRequestRequestTypeDef,
    DescribeDeploymentJobResponseTypeDef,
    DescribeFleetRequestRequestTypeDef,
    DescribeFleetResponseTypeDef,
    DescribeRobotApplicationRequestRequestTypeDef,
    DescribeRobotApplicationResponseTypeDef,
    DescribeRobotRequestRequestTypeDef,
    DescribeRobotResponseTypeDef,
    DescribeSimulationApplicationRequestRequestTypeDef,
    DescribeSimulationApplicationResponseTypeDef,
    DescribeSimulationJobBatchRequestRequestTypeDef,
    DescribeSimulationJobBatchResponseTypeDef,
    DescribeSimulationJobRequestRequestTypeDef,
    DescribeSimulationJobResponseTypeDef,
    DescribeWorldExportJobRequestRequestTypeDef,
    DescribeWorldExportJobResponseTypeDef,
    DescribeWorldGenerationJobRequestRequestTypeDef,
    DescribeWorldGenerationJobResponseTypeDef,
    DescribeWorldRequestRequestTypeDef,
    DescribeWorldResponseTypeDef,
    DescribeWorldTemplateRequestRequestTypeDef,
    DescribeWorldTemplateResponseTypeDef,
    GetWorldTemplateBodyRequestRequestTypeDef,
    GetWorldTemplateBodyResponseTypeDef,
    ListDeploymentJobsRequestRequestTypeDef,
    ListDeploymentJobsResponseTypeDef,
    ListFleetsRequestRequestTypeDef,
    ListFleetsResponseTypeDef,
    ListRobotApplicationsRequestRequestTypeDef,
    ListRobotApplicationsResponseTypeDef,
    ListRobotsRequestRequestTypeDef,
    ListRobotsResponseTypeDef,
    ListSimulationApplicationsRequestRequestTypeDef,
    ListSimulationApplicationsResponseTypeDef,
    ListSimulationJobBatchesRequestRequestTypeDef,
    ListSimulationJobBatchesResponseTypeDef,
    ListSimulationJobsRequestRequestTypeDef,
    ListSimulationJobsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorldExportJobsRequestRequestTypeDef,
    ListWorldExportJobsResponseTypeDef,
    ListWorldGenerationJobsRequestRequestTypeDef,
    ListWorldGenerationJobsResponseTypeDef,
    ListWorldsRequestRequestTypeDef,
    ListWorldsResponseTypeDef,
    ListWorldTemplatesRequestRequestTypeDef,
    ListWorldTemplatesResponseTypeDef,
    RegisterRobotRequestRequestTypeDef,
    RegisterRobotResponseTypeDef,
    RestartSimulationJobRequestRequestTypeDef,
    StartSimulationJobBatchRequestRequestTypeDef,
    StartSimulationJobBatchResponseTypeDef,
    SyncDeploymentJobRequestRequestTypeDef,
    SyncDeploymentJobResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateRobotApplicationRequestRequestTypeDef,
    UpdateRobotApplicationResponseTypeDef,
    UpdateSimulationApplicationRequestRequestTypeDef,
    UpdateSimulationApplicationResponseTypeDef,
    UpdateWorldTemplateRequestRequestTypeDef,
    UpdateWorldTemplateResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("RoboMakerClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentDeploymentException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class RoboMakerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RoboMakerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#exceptions)
        """

    def batch_delete_worlds(
        self, **kwargs: Unpack[BatchDeleteWorldsRequestRequestTypeDef]
    ) -> BatchDeleteWorldsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.batch_delete_worlds)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#batch_delete_worlds)
        """

    def batch_describe_simulation_job(
        self, **kwargs: Unpack[BatchDescribeSimulationJobRequestRequestTypeDef]
    ) -> BatchDescribeSimulationJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.batch_describe_simulation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#batch_describe_simulation_job)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#can_paginate)
        """

    def cancel_deployment_job(
        self, **kwargs: Unpack[CancelDeploymentJobRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_deployment_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_deployment_job)
        """

    def cancel_simulation_job(
        self, **kwargs: Unpack[CancelSimulationJobRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_simulation_job)
        """

    def cancel_simulation_job_batch(
        self, **kwargs: Unpack[CancelSimulationJobBatchRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job_batch)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_simulation_job_batch)
        """

    def cancel_world_export_job(
        self, **kwargs: Unpack[CancelWorldExportJobRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_world_export_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_world_export_job)
        """

    def cancel_world_generation_job(
        self, **kwargs: Unpack[CancelWorldGenerationJobRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_world_generation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_world_generation_job)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#close)
        """

    def create_deployment_job(
        self, **kwargs: Unpack[CreateDeploymentJobRequestRequestTypeDef]
    ) -> CreateDeploymentJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_deployment_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_deployment_job)
        """

    def create_fleet(
        self, **kwargs: Unpack[CreateFleetRequestRequestTypeDef]
    ) -> CreateFleetResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_fleet)
        """

    def create_robot(
        self, **kwargs: Unpack[CreateRobotRequestRequestTypeDef]
    ) -> CreateRobotResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_robot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_robot)
        """

    def create_robot_application(
        self, **kwargs: Unpack[CreateRobotApplicationRequestRequestTypeDef]
    ) -> CreateRobotApplicationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_robot_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_robot_application)
        """

    def create_robot_application_version(
        self, **kwargs: Unpack[CreateRobotApplicationVersionRequestRequestTypeDef]
    ) -> CreateRobotApplicationVersionResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_robot_application_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_robot_application_version)
        """

    def create_simulation_application(
        self, **kwargs: Unpack[CreateSimulationApplicationRequestRequestTypeDef]
    ) -> CreateSimulationApplicationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_simulation_application)
        """

    def create_simulation_application_version(
        self, **kwargs: Unpack[CreateSimulationApplicationVersionRequestRequestTypeDef]
    ) -> CreateSimulationApplicationVersionResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_simulation_application_version)
        """

    def create_simulation_job(
        self, **kwargs: Unpack[CreateSimulationJobRequestRequestTypeDef]
    ) -> CreateSimulationJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_simulation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_simulation_job)
        """

    def create_world_export_job(
        self, **kwargs: Unpack[CreateWorldExportJobRequestRequestTypeDef]
    ) -> CreateWorldExportJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_world_export_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_world_export_job)
        """

    def create_world_generation_job(
        self, **kwargs: Unpack[CreateWorldGenerationJobRequestRequestTypeDef]
    ) -> CreateWorldGenerationJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_world_generation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_world_generation_job)
        """

    def create_world_template(
        self, **kwargs: Unpack[CreateWorldTemplateRequestRequestTypeDef]
    ) -> CreateWorldTemplateResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_world_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_world_template)
        """

    def delete_fleet(self, **kwargs: Unpack[DeleteFleetRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_fleet)
        """

    def delete_robot(self, **kwargs: Unpack[DeleteRobotRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_robot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_robot)
        """

    def delete_robot_application(
        self, **kwargs: Unpack[DeleteRobotApplicationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_robot_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_robot_application)
        """

    def delete_simulation_application(
        self, **kwargs: Unpack[DeleteSimulationApplicationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_simulation_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_simulation_application)
        """

    def delete_world_template(
        self, **kwargs: Unpack[DeleteWorldTemplateRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_world_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_world_template)
        """

    def deregister_robot(
        self, **kwargs: Unpack[DeregisterRobotRequestRequestTypeDef]
    ) -> DeregisterRobotResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.deregister_robot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#deregister_robot)
        """

    def describe_deployment_job(
        self, **kwargs: Unpack[DescribeDeploymentJobRequestRequestTypeDef]
    ) -> DescribeDeploymentJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_deployment_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_deployment_job)
        """

    def describe_fleet(
        self, **kwargs: Unpack[DescribeFleetRequestRequestTypeDef]
    ) -> DescribeFleetResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_fleet)
        """

    def describe_robot(
        self, **kwargs: Unpack[DescribeRobotRequestRequestTypeDef]
    ) -> DescribeRobotResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_robot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_robot)
        """

    def describe_robot_application(
        self, **kwargs: Unpack[DescribeRobotApplicationRequestRequestTypeDef]
    ) -> DescribeRobotApplicationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_robot_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_robot_application)
        """

    def describe_simulation_application(
        self, **kwargs: Unpack[DescribeSimulationApplicationRequestRequestTypeDef]
    ) -> DescribeSimulationApplicationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_simulation_application)
        """

    def describe_simulation_job(
        self, **kwargs: Unpack[DescribeSimulationJobRequestRequestTypeDef]
    ) -> DescribeSimulationJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_simulation_job)
        """

    def describe_simulation_job_batch(
        self, **kwargs: Unpack[DescribeSimulationJobBatchRequestRequestTypeDef]
    ) -> DescribeSimulationJobBatchResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job_batch)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_simulation_job_batch)
        """

    def describe_world(
        self, **kwargs: Unpack[DescribeWorldRequestRequestTypeDef]
    ) -> DescribeWorldResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_world)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_world)
        """

    def describe_world_export_job(
        self, **kwargs: Unpack[DescribeWorldExportJobRequestRequestTypeDef]
    ) -> DescribeWorldExportJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_world_export_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_world_export_job)
        """

    def describe_world_generation_job(
        self, **kwargs: Unpack[DescribeWorldGenerationJobRequestRequestTypeDef]
    ) -> DescribeWorldGenerationJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_world_generation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_world_generation_job)
        """

    def describe_world_template(
        self, **kwargs: Unpack[DescribeWorldTemplateRequestRequestTypeDef]
    ) -> DescribeWorldTemplateResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_world_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_world_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#generate_presigned_url)
        """

    def get_world_template_body(
        self, **kwargs: Unpack[GetWorldTemplateBodyRequestRequestTypeDef]
    ) -> GetWorldTemplateBodyResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_world_template_body)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_world_template_body)
        """

    def list_deployment_jobs(
        self, **kwargs: Unpack[ListDeploymentJobsRequestRequestTypeDef]
    ) -> ListDeploymentJobsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_deployment_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_deployment_jobs)
        """

    def list_fleets(
        self, **kwargs: Unpack[ListFleetsRequestRequestTypeDef]
    ) -> ListFleetsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_fleets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_fleets)
        """

    def list_robot_applications(
        self, **kwargs: Unpack[ListRobotApplicationsRequestRequestTypeDef]
    ) -> ListRobotApplicationsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_robot_applications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_robot_applications)
        """

    def list_robots(
        self, **kwargs: Unpack[ListRobotsRequestRequestTypeDef]
    ) -> ListRobotsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_robots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_robots)
        """

    def list_simulation_applications(
        self, **kwargs: Unpack[ListSimulationApplicationsRequestRequestTypeDef]
    ) -> ListSimulationApplicationsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_simulation_applications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_simulation_applications)
        """

    def list_simulation_job_batches(
        self, **kwargs: Unpack[ListSimulationJobBatchesRequestRequestTypeDef]
    ) -> ListSimulationJobBatchesResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_simulation_job_batches)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_simulation_job_batches)
        """

    def list_simulation_jobs(
        self, **kwargs: Unpack[ListSimulationJobsRequestRequestTypeDef]
    ) -> ListSimulationJobsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_simulation_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_simulation_jobs)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_tags_for_resource)
        """

    def list_world_export_jobs(
        self, **kwargs: Unpack[ListWorldExportJobsRequestRequestTypeDef]
    ) -> ListWorldExportJobsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_world_export_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_world_export_jobs)
        """

    def list_world_generation_jobs(
        self, **kwargs: Unpack[ListWorldGenerationJobsRequestRequestTypeDef]
    ) -> ListWorldGenerationJobsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_world_generation_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_world_generation_jobs)
        """

    def list_world_templates(
        self, **kwargs: Unpack[ListWorldTemplatesRequestRequestTypeDef]
    ) -> ListWorldTemplatesResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_world_templates)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_world_templates)
        """

    def list_worlds(
        self, **kwargs: Unpack[ListWorldsRequestRequestTypeDef]
    ) -> ListWorldsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_worlds)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_worlds)
        """

    def register_robot(
        self, **kwargs: Unpack[RegisterRobotRequestRequestTypeDef]
    ) -> RegisterRobotResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.register_robot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#register_robot)
        """

    def restart_simulation_job(
        self, **kwargs: Unpack[RestartSimulationJobRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.restart_simulation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#restart_simulation_job)
        """

    def start_simulation_job_batch(
        self, **kwargs: Unpack[StartSimulationJobBatchRequestRequestTypeDef]
    ) -> StartSimulationJobBatchResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.start_simulation_job_batch)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#start_simulation_job_batch)
        """

    def sync_deployment_job(
        self, **kwargs: Unpack[SyncDeploymentJobRequestRequestTypeDef]
    ) -> SyncDeploymentJobResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.sync_deployment_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#sync_deployment_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#untag_resource)
        """

    def update_robot_application(
        self, **kwargs: Unpack[UpdateRobotApplicationRequestRequestTypeDef]
    ) -> UpdateRobotApplicationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.update_robot_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#update_robot_application)
        """

    def update_simulation_application(
        self, **kwargs: Unpack[UpdateSimulationApplicationRequestRequestTypeDef]
    ) -> UpdateSimulationApplicationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.update_simulation_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#update_simulation_application)
        """

    def update_world_template(
        self, **kwargs: Unpack[UpdateWorldTemplateRequestRequestTypeDef]
    ) -> UpdateWorldTemplateResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.update_world_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#update_world_template)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_jobs"]
    ) -> ListDeploymentJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_robot_applications"]
    ) -> ListRobotApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_robots"]) -> ListRobotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_applications"]
    ) -> ListSimulationApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_job_batches"]
    ) -> ListSimulationJobBatchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_jobs"]
    ) -> ListSimulationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_export_jobs"]
    ) -> ListWorldExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_generation_jobs"]
    ) -> ListWorldGenerationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_templates"]
    ) -> ListWorldTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_worlds"]) -> ListWorldsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """
