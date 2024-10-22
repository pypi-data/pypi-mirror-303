"""
Type annotations for devicefarm service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_devicefarm.client import DeviceFarmClient

    session = Session()
    client: DeviceFarmClient = session.client("devicefarm")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    GetOfferingStatusPaginator,
    ListArtifactsPaginator,
    ListDeviceInstancesPaginator,
    ListDevicePoolsPaginator,
    ListDevicesPaginator,
    ListInstanceProfilesPaginator,
    ListJobsPaginator,
    ListNetworkProfilesPaginator,
    ListOfferingPromotionsPaginator,
    ListOfferingsPaginator,
    ListOfferingTransactionsPaginator,
    ListProjectsPaginator,
    ListRemoteAccessSessionsPaginator,
    ListRunsPaginator,
    ListSamplesPaginator,
    ListSuitesPaginator,
    ListTestsPaginator,
    ListUniqueProblemsPaginator,
    ListUploadsPaginator,
    ListVPCEConfigurationsPaginator,
)
from .type_defs import (
    CreateDevicePoolRequestRequestTypeDef,
    CreateDevicePoolResultTypeDef,
    CreateInstanceProfileRequestRequestTypeDef,
    CreateInstanceProfileResultTypeDef,
    CreateNetworkProfileRequestRequestTypeDef,
    CreateNetworkProfileResultTypeDef,
    CreateProjectRequestRequestTypeDef,
    CreateProjectResultTypeDef,
    CreateRemoteAccessSessionRequestRequestTypeDef,
    CreateRemoteAccessSessionResultTypeDef,
    CreateTestGridProjectRequestRequestTypeDef,
    CreateTestGridProjectResultTypeDef,
    CreateTestGridUrlRequestRequestTypeDef,
    CreateTestGridUrlResultTypeDef,
    CreateUploadRequestRequestTypeDef,
    CreateUploadResultTypeDef,
    CreateVPCEConfigurationRequestRequestTypeDef,
    CreateVPCEConfigurationResultTypeDef,
    DeleteDevicePoolRequestRequestTypeDef,
    DeleteInstanceProfileRequestRequestTypeDef,
    DeleteNetworkProfileRequestRequestTypeDef,
    DeleteProjectRequestRequestTypeDef,
    DeleteRemoteAccessSessionRequestRequestTypeDef,
    DeleteRunRequestRequestTypeDef,
    DeleteTestGridProjectRequestRequestTypeDef,
    DeleteUploadRequestRequestTypeDef,
    DeleteVPCEConfigurationRequestRequestTypeDef,
    GetAccountSettingsResultTypeDef,
    GetDeviceInstanceRequestRequestTypeDef,
    GetDeviceInstanceResultTypeDef,
    GetDevicePoolCompatibilityRequestRequestTypeDef,
    GetDevicePoolCompatibilityResultTypeDef,
    GetDevicePoolRequestRequestTypeDef,
    GetDevicePoolResultTypeDef,
    GetDeviceRequestRequestTypeDef,
    GetDeviceResultTypeDef,
    GetInstanceProfileRequestRequestTypeDef,
    GetInstanceProfileResultTypeDef,
    GetJobRequestRequestTypeDef,
    GetJobResultTypeDef,
    GetNetworkProfileRequestRequestTypeDef,
    GetNetworkProfileResultTypeDef,
    GetOfferingStatusRequestRequestTypeDef,
    GetOfferingStatusResultTypeDef,
    GetProjectRequestRequestTypeDef,
    GetProjectResultTypeDef,
    GetRemoteAccessSessionRequestRequestTypeDef,
    GetRemoteAccessSessionResultTypeDef,
    GetRunRequestRequestTypeDef,
    GetRunResultTypeDef,
    GetSuiteRequestRequestTypeDef,
    GetSuiteResultTypeDef,
    GetTestGridProjectRequestRequestTypeDef,
    GetTestGridProjectResultTypeDef,
    GetTestGridSessionRequestRequestTypeDef,
    GetTestGridSessionResultTypeDef,
    GetTestRequestRequestTypeDef,
    GetTestResultTypeDef,
    GetUploadRequestRequestTypeDef,
    GetUploadResultTypeDef,
    GetVPCEConfigurationRequestRequestTypeDef,
    GetVPCEConfigurationResultTypeDef,
    InstallToRemoteAccessSessionRequestRequestTypeDef,
    InstallToRemoteAccessSessionResultTypeDef,
    ListArtifactsRequestRequestTypeDef,
    ListArtifactsResultTypeDef,
    ListDeviceInstancesRequestRequestTypeDef,
    ListDeviceInstancesResultTypeDef,
    ListDevicePoolsRequestRequestTypeDef,
    ListDevicePoolsResultTypeDef,
    ListDevicesRequestRequestTypeDef,
    ListDevicesResultTypeDef,
    ListInstanceProfilesRequestRequestTypeDef,
    ListInstanceProfilesResultTypeDef,
    ListJobsRequestRequestTypeDef,
    ListJobsResultTypeDef,
    ListNetworkProfilesRequestRequestTypeDef,
    ListNetworkProfilesResultTypeDef,
    ListOfferingPromotionsRequestRequestTypeDef,
    ListOfferingPromotionsResultTypeDef,
    ListOfferingsRequestRequestTypeDef,
    ListOfferingsResultTypeDef,
    ListOfferingTransactionsRequestRequestTypeDef,
    ListOfferingTransactionsResultTypeDef,
    ListProjectsRequestRequestTypeDef,
    ListProjectsResultTypeDef,
    ListRemoteAccessSessionsRequestRequestTypeDef,
    ListRemoteAccessSessionsResultTypeDef,
    ListRunsRequestRequestTypeDef,
    ListRunsResultTypeDef,
    ListSamplesRequestRequestTypeDef,
    ListSamplesResultTypeDef,
    ListSuitesRequestRequestTypeDef,
    ListSuitesResultTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestGridProjectsRequestRequestTypeDef,
    ListTestGridProjectsResultTypeDef,
    ListTestGridSessionActionsRequestRequestTypeDef,
    ListTestGridSessionActionsResultTypeDef,
    ListTestGridSessionArtifactsRequestRequestTypeDef,
    ListTestGridSessionArtifactsResultTypeDef,
    ListTestGridSessionsRequestRequestTypeDef,
    ListTestGridSessionsResultTypeDef,
    ListTestsRequestRequestTypeDef,
    ListTestsResultTypeDef,
    ListUniqueProblemsRequestRequestTypeDef,
    ListUniqueProblemsResultTypeDef,
    ListUploadsRequestRequestTypeDef,
    ListUploadsResultTypeDef,
    ListVPCEConfigurationsRequestRequestTypeDef,
    ListVPCEConfigurationsResultTypeDef,
    PurchaseOfferingRequestRequestTypeDef,
    PurchaseOfferingResultTypeDef,
    RenewOfferingRequestRequestTypeDef,
    RenewOfferingResultTypeDef,
    ScheduleRunRequestRequestTypeDef,
    ScheduleRunResultTypeDef,
    StopJobRequestRequestTypeDef,
    StopJobResultTypeDef,
    StopRemoteAccessSessionRequestRequestTypeDef,
    StopRemoteAccessSessionResultTypeDef,
    StopRunRequestRequestTypeDef,
    StopRunResultTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateDeviceInstanceRequestRequestTypeDef,
    UpdateDeviceInstanceResultTypeDef,
    UpdateDevicePoolRequestRequestTypeDef,
    UpdateDevicePoolResultTypeDef,
    UpdateInstanceProfileRequestRequestTypeDef,
    UpdateInstanceProfileResultTypeDef,
    UpdateNetworkProfileRequestRequestTypeDef,
    UpdateNetworkProfileResultTypeDef,
    UpdateProjectRequestRequestTypeDef,
    UpdateProjectResultTypeDef,
    UpdateTestGridProjectRequestRequestTypeDef,
    UpdateTestGridProjectResultTypeDef,
    UpdateUploadRequestRequestTypeDef,
    UpdateUploadResultTypeDef,
    UpdateVPCEConfigurationRequestRequestTypeDef,
    UpdateVPCEConfigurationResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("DeviceFarmClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ArgumentException: Type[BotocoreClientError]
    CannotDeleteException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotEligibleException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceAccountException: Type[BotocoreClientError]
    TagOperationException: Type[BotocoreClientError]
    TagPolicyException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class DeviceFarmClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DeviceFarmClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#close)
        """

    def create_device_pool(
        self, **kwargs: Unpack[CreateDevicePoolRequestRequestTypeDef]
    ) -> CreateDevicePoolResultTypeDef:
        """
        Creates a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_device_pool)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_device_pool)
        """

    def create_instance_profile(
        self, **kwargs: Unpack[CreateInstanceProfileRequestRequestTypeDef]
    ) -> CreateInstanceProfileResultTypeDef:
        """
        Creates a profile that can be applied to one or more private fleet device
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_instance_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_instance_profile)
        """

    def create_network_profile(
        self, **kwargs: Unpack[CreateNetworkProfileRequestRequestTypeDef]
    ) -> CreateNetworkProfileResultTypeDef:
        """
        Creates a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_network_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_network_profile)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectRequestRequestTypeDef]
    ) -> CreateProjectResultTypeDef:
        """
        Creates a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_project)
        """

    def create_remote_access_session(
        self, **kwargs: Unpack[CreateRemoteAccessSessionRequestRequestTypeDef]
    ) -> CreateRemoteAccessSessionResultTypeDef:
        """
        Specifies and starts a remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_remote_access_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_remote_access_session)
        """

    def create_test_grid_project(
        self, **kwargs: Unpack[CreateTestGridProjectRequestRequestTypeDef]
    ) -> CreateTestGridProjectResultTypeDef:
        """
        Creates a Selenium testing project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_test_grid_project)
        """

    def create_test_grid_url(
        self, **kwargs: Unpack[CreateTestGridUrlRequestRequestTypeDef]
    ) -> CreateTestGridUrlResultTypeDef:
        """
        Creates a signed, short-term URL that can be passed to a Selenium
        `RemoteWebDriver`
        constructor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_test_grid_url)
        """

    def create_upload(
        self, **kwargs: Unpack[CreateUploadRequestRequestTypeDef]
    ) -> CreateUploadResultTypeDef:
        """
        Uploads an app or test scripts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_upload)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_upload)
        """

    def create_vpce_configuration(
        self, **kwargs: Unpack[CreateVPCEConfigurationRequestRequestTypeDef]
    ) -> CreateVPCEConfigurationResultTypeDef:
        """
        Creates a configuration record in Device Farm for your Amazon Virtual Private
        Cloud (VPC)
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_vpce_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_vpce_configuration)
        """

    def delete_device_pool(
        self, **kwargs: Unpack[DeleteDevicePoolRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a device pool given the pool ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_device_pool)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_device_pool)
        """

    def delete_instance_profile(
        self, **kwargs: Unpack[DeleteInstanceProfileRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a profile that can be applied to one or more private device instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_instance_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_instance_profile)
        """

    def delete_network_profile(
        self, **kwargs: Unpack[DeleteNetworkProfileRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_network_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_network_profile)
        """

    def delete_project(
        self, **kwargs: Unpack[DeleteProjectRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an AWS Device Farm project, given the project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_project)
        """

    def delete_remote_access_session(
        self, **kwargs: Unpack[DeleteRemoteAccessSessionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a completed remote access session and its results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_remote_access_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_remote_access_session)
        """

    def delete_run(self, **kwargs: Unpack[DeleteRunRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the run, given the run ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_run)
        """

    def delete_test_grid_project(
        self, **kwargs: Unpack[DeleteTestGridProjectRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Selenium testing project and all content generated under it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_test_grid_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_test_grid_project)
        """

    def delete_upload(self, **kwargs: Unpack[DeleteUploadRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an upload given the upload ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_upload)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_upload)
        """

    def delete_vpce_configuration(
        self, **kwargs: Unpack[DeleteVPCEConfigurationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a configuration for your Amazon Virtual Private Cloud (VPC) endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_vpce_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_vpce_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#generate_presigned_url)
        """

    def get_account_settings(self) -> GetAccountSettingsResultTypeDef:
        """
        Returns the number of unmetered iOS or unmetered Android devices that have been
        purchased by the
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_account_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_account_settings)
        """

    def get_device(
        self, **kwargs: Unpack[GetDeviceRequestRequestTypeDef]
    ) -> GetDeviceResultTypeDef:
        """
        Gets information about a unique device type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_device)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_device)
        """

    def get_device_instance(
        self, **kwargs: Unpack[GetDeviceInstanceRequestRequestTypeDef]
    ) -> GetDeviceInstanceResultTypeDef:
        """
        Returns information about a device instance that belongs to a private device
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_device_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_device_instance)
        """

    def get_device_pool(
        self, **kwargs: Unpack[GetDevicePoolRequestRequestTypeDef]
    ) -> GetDevicePoolResultTypeDef:
        """
        Gets information about a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_device_pool)
        """

    def get_device_pool_compatibility(
        self, **kwargs: Unpack[GetDevicePoolCompatibilityRequestRequestTypeDef]
    ) -> GetDevicePoolCompatibilityResultTypeDef:
        """
        Gets information about compatibility with a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool_compatibility)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_device_pool_compatibility)
        """

    def get_instance_profile(
        self, **kwargs: Unpack[GetInstanceProfileRequestRequestTypeDef]
    ) -> GetInstanceProfileResultTypeDef:
        """
        Returns information about the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_instance_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_instance_profile)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestRequestTypeDef]) -> GetJobResultTypeDef:
        """
        Gets information about a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_job)
        """

    def get_network_profile(
        self, **kwargs: Unpack[GetNetworkProfileRequestRequestTypeDef]
    ) -> GetNetworkProfileResultTypeDef:
        """
        Returns information about a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_network_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_network_profile)
        """

    def get_offering_status(
        self, **kwargs: Unpack[GetOfferingStatusRequestRequestTypeDef]
    ) -> GetOfferingStatusResultTypeDef:
        """
        Gets the current status and future status of all offerings purchased by an AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_offering_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_offering_status)
        """

    def get_project(
        self, **kwargs: Unpack[GetProjectRequestRequestTypeDef]
    ) -> GetProjectResultTypeDef:
        """
        Gets information about a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_project)
        """

    def get_remote_access_session(
        self, **kwargs: Unpack[GetRemoteAccessSessionRequestRequestTypeDef]
    ) -> GetRemoteAccessSessionResultTypeDef:
        """
        Returns a link to a currently running remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_remote_access_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_remote_access_session)
        """

    def get_run(self, **kwargs: Unpack[GetRunRequestRequestTypeDef]) -> GetRunResultTypeDef:
        """
        Gets information about a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_run)
        """

    def get_suite(self, **kwargs: Unpack[GetSuiteRequestRequestTypeDef]) -> GetSuiteResultTypeDef:
        """
        Gets information about a suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_suite)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_suite)
        """

    def get_test(self, **kwargs: Unpack[GetTestRequestRequestTypeDef]) -> GetTestResultTypeDef:
        """
        Gets information about a test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_test)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_test)
        """

    def get_test_grid_project(
        self, **kwargs: Unpack[GetTestGridProjectRequestRequestTypeDef]
    ) -> GetTestGridProjectResultTypeDef:
        """
        Retrieves information about a Selenium testing project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_test_grid_project)
        """

    def get_test_grid_session(
        self, **kwargs: Unpack[GetTestGridSessionRequestRequestTypeDef]
    ) -> GetTestGridSessionResultTypeDef:
        """
        A session is an instance of a browser created through a `RemoteWebDriver` with
        the URL from
        CreateTestGridUrlResult$url.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_test_grid_session)
        """

    def get_upload(
        self, **kwargs: Unpack[GetUploadRequestRequestTypeDef]
    ) -> GetUploadResultTypeDef:
        """
        Gets information about an upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_upload)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_upload)
        """

    def get_vpce_configuration(
        self, **kwargs: Unpack[GetVPCEConfigurationRequestRequestTypeDef]
    ) -> GetVPCEConfigurationResultTypeDef:
        """
        Returns information about the configuration settings for your Amazon Virtual
        Private Cloud (VPC)
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_vpce_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_vpce_configuration)
        """

    def install_to_remote_access_session(
        self, **kwargs: Unpack[InstallToRemoteAccessSessionRequestRequestTypeDef]
    ) -> InstallToRemoteAccessSessionResultTypeDef:
        """
        Installs an application to the device in a remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.install_to_remote_access_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#install_to_remote_access_session)
        """

    def list_artifacts(
        self, **kwargs: Unpack[ListArtifactsRequestRequestTypeDef]
    ) -> ListArtifactsResultTypeDef:
        """
        Gets information about artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_artifacts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_artifacts)
        """

    def list_device_instances(
        self, **kwargs: Unpack[ListDeviceInstancesRequestRequestTypeDef]
    ) -> ListDeviceInstancesResultTypeDef:
        """
        Returns information about the private device instances associated with one or
        more AWS
        accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_device_instances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_device_instances)
        """

    def list_device_pools(
        self, **kwargs: Unpack[ListDevicePoolsRequestRequestTypeDef]
    ) -> ListDevicePoolsResultTypeDef:
        """
        Gets information about device pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_device_pools)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_device_pools)
        """

    def list_devices(
        self, **kwargs: Unpack[ListDevicesRequestRequestTypeDef]
    ) -> ListDevicesResultTypeDef:
        """
        Gets information about unique device types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_devices)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_devices)
        """

    def list_instance_profiles(
        self, **kwargs: Unpack[ListInstanceProfilesRequestRequestTypeDef]
    ) -> ListInstanceProfilesResultTypeDef:
        """
        Returns information about all the instance profiles in an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_instance_profiles)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_instance_profiles)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestRequestTypeDef]) -> ListJobsResultTypeDef:
        """
        Gets information about jobs for a given test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_jobs)
        """

    def list_network_profiles(
        self, **kwargs: Unpack[ListNetworkProfilesRequestRequestTypeDef]
    ) -> ListNetworkProfilesResultTypeDef:
        """
        Returns the list of available network profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_network_profiles)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_network_profiles)
        """

    def list_offering_promotions(
        self, **kwargs: Unpack[ListOfferingPromotionsRequestRequestTypeDef]
    ) -> ListOfferingPromotionsResultTypeDef:
        """
        Returns a list of offering promotions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_promotions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_offering_promotions)
        """

    def list_offering_transactions(
        self, **kwargs: Unpack[ListOfferingTransactionsRequestRequestTypeDef]
    ) -> ListOfferingTransactionsResultTypeDef:
        """
        Returns a list of all historical purchases, renewals, and system renewal
        transactions for an AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_transactions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_offering_transactions)
        """

    def list_offerings(
        self, **kwargs: Unpack[ListOfferingsRequestRequestTypeDef]
    ) -> ListOfferingsResultTypeDef:
        """
        Returns a list of products or offerings that the user can manage through the
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_offerings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_offerings)
        """

    def list_projects(
        self, **kwargs: Unpack[ListProjectsRequestRequestTypeDef]
    ) -> ListProjectsResultTypeDef:
        """
        Gets information about projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_projects)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_projects)
        """

    def list_remote_access_sessions(
        self, **kwargs: Unpack[ListRemoteAccessSessionsRequestRequestTypeDef]
    ) -> ListRemoteAccessSessionsResultTypeDef:
        """
        Returns a list of all currently running remote access sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_remote_access_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_remote_access_sessions)
        """

    def list_runs(self, **kwargs: Unpack[ListRunsRequestRequestTypeDef]) -> ListRunsResultTypeDef:
        """
        Gets information about runs, given an AWS Device Farm project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_runs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_runs)
        """

    def list_samples(
        self, **kwargs: Unpack[ListSamplesRequestRequestTypeDef]
    ) -> ListSamplesResultTypeDef:
        """
        Gets information about samples, given an AWS Device Farm job ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_samples)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_samples)
        """

    def list_suites(
        self, **kwargs: Unpack[ListSuitesRequestRequestTypeDef]
    ) -> ListSuitesResultTypeDef:
        """
        Gets information about test suites for a given job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_suites)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_suites)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags for an AWS Device Farm resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_tags_for_resource)
        """

    def list_test_grid_projects(
        self, **kwargs: Unpack[ListTestGridProjectsRequestRequestTypeDef]
    ) -> ListTestGridProjectsResultTypeDef:
        """
        Gets a list of all Selenium testing projects in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_projects)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_test_grid_projects)
        """

    def list_test_grid_session_actions(
        self, **kwargs: Unpack[ListTestGridSessionActionsRequestRequestTypeDef]
    ) -> ListTestGridSessionActionsResultTypeDef:
        """
        Returns a list of the actions taken in a  TestGridSession.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_actions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_test_grid_session_actions)
        """

    def list_test_grid_session_artifacts(
        self, **kwargs: Unpack[ListTestGridSessionArtifactsRequestRequestTypeDef]
    ) -> ListTestGridSessionArtifactsResultTypeDef:
        """
        Retrieves a list of artifacts created during the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_artifacts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_test_grid_session_artifacts)
        """

    def list_test_grid_sessions(
        self, **kwargs: Unpack[ListTestGridSessionsRequestRequestTypeDef]
    ) -> ListTestGridSessionsResultTypeDef:
        """
        Retrieves a list of sessions for a  TestGridProject.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_test_grid_sessions)
        """

    def list_tests(
        self, **kwargs: Unpack[ListTestsRequestRequestTypeDef]
    ) -> ListTestsResultTypeDef:
        """
        Gets information about tests in a given test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_tests)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_tests)
        """

    def list_unique_problems(
        self, **kwargs: Unpack[ListUniqueProblemsRequestRequestTypeDef]
    ) -> ListUniqueProblemsResultTypeDef:
        """
        Gets information about unique problems, such as exceptions or crashes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_unique_problems)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_unique_problems)
        """

    def list_uploads(
        self, **kwargs: Unpack[ListUploadsRequestRequestTypeDef]
    ) -> ListUploadsResultTypeDef:
        """
        Gets information about uploads, given an AWS Device Farm project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_uploads)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_uploads)
        """

    def list_vpce_configurations(
        self, **kwargs: Unpack[ListVPCEConfigurationsRequestRequestTypeDef]
    ) -> ListVPCEConfigurationsResultTypeDef:
        """
        Returns information about all Amazon Virtual Private Cloud (VPC) endpoint
        configurations in the AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_vpce_configurations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_vpce_configurations)
        """

    def purchase_offering(
        self, **kwargs: Unpack[PurchaseOfferingRequestRequestTypeDef]
    ) -> PurchaseOfferingResultTypeDef:
        """
        Immediately purchases offerings for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.purchase_offering)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#purchase_offering)
        """

    def renew_offering(
        self, **kwargs: Unpack[RenewOfferingRequestRequestTypeDef]
    ) -> RenewOfferingResultTypeDef:
        """
        Explicitly sets the quantity of devices to renew for an offering, starting from
        the `effectiveDate` of the next
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.renew_offering)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#renew_offering)
        """

    def schedule_run(
        self, **kwargs: Unpack[ScheduleRunRequestRequestTypeDef]
    ) -> ScheduleRunResultTypeDef:
        """
        Schedules a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.schedule_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#schedule_run)
        """

    def stop_job(self, **kwargs: Unpack[StopJobRequestRequestTypeDef]) -> StopJobResultTypeDef:
        """
        Initiates a stop request for the current job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.stop_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#stop_job)
        """

    def stop_remote_access_session(
        self, **kwargs: Unpack[StopRemoteAccessSessionRequestRequestTypeDef]
    ) -> StopRemoteAccessSessionResultTypeDef:
        """
        Ends a specified remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.stop_remote_access_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#stop_remote_access_session)
        """

    def stop_run(self, **kwargs: Unpack[StopRunRequestRequestTypeDef]) -> StopRunResultTypeDef:
        """
        Initiates a stop request for the current test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.stop_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#stop_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#untag_resource)
        """

    def update_device_instance(
        self, **kwargs: Unpack[UpdateDeviceInstanceRequestRequestTypeDef]
    ) -> UpdateDeviceInstanceResultTypeDef:
        """
        Updates information about a private device instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_device_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_device_instance)
        """

    def update_device_pool(
        self, **kwargs: Unpack[UpdateDevicePoolRequestRequestTypeDef]
    ) -> UpdateDevicePoolResultTypeDef:
        """
        Modifies the name, description, and rules in a device pool given the attributes
        and the pool
        ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_device_pool)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_device_pool)
        """

    def update_instance_profile(
        self, **kwargs: Unpack[UpdateInstanceProfileRequestRequestTypeDef]
    ) -> UpdateInstanceProfileResultTypeDef:
        """
        Updates information about an existing private device instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_instance_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_instance_profile)
        """

    def update_network_profile(
        self, **kwargs: Unpack[UpdateNetworkProfileRequestRequestTypeDef]
    ) -> UpdateNetworkProfileResultTypeDef:
        """
        Updates the network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_network_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_network_profile)
        """

    def update_project(
        self, **kwargs: Unpack[UpdateProjectRequestRequestTypeDef]
    ) -> UpdateProjectResultTypeDef:
        """
        Modifies the specified project name, given the project ARN and a new name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_project)
        """

    def update_test_grid_project(
        self, **kwargs: Unpack[UpdateTestGridProjectRequestRequestTypeDef]
    ) -> UpdateTestGridProjectResultTypeDef:
        """
        Change details of a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_test_grid_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_test_grid_project)
        """

    def update_upload(
        self, **kwargs: Unpack[UpdateUploadRequestRequestTypeDef]
    ) -> UpdateUploadResultTypeDef:
        """
        Updates an uploaded test spec.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_upload)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_upload)
        """

    def update_vpce_configuration(
        self, **kwargs: Unpack[UpdateVPCEConfigurationRequestRequestTypeDef]
    ) -> UpdateVPCEConfigurationResultTypeDef:
        """
        Updates information about an Amazon Virtual Private Cloud (VPC) endpoint
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_vpce_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_vpce_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_offering_status"]
    ) -> GetOfferingStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_artifacts"]) -> ListArtifactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_instances"]
    ) -> ListDeviceInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_pools"]
    ) -> ListDevicePoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles"]
    ) -> ListInstanceProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_network_profiles"]
    ) -> ListNetworkProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_offering_promotions"]
    ) -> ListOfferingPromotionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_offering_transactions"]
    ) -> ListOfferingTransactionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_remote_access_sessions"]
    ) -> ListRemoteAccessSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_runs"]) -> ListRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_samples"]) -> ListSamplesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_suites"]) -> ListSuitesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tests"]) -> ListTestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_unique_problems"]
    ) -> ListUniqueProblemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_uploads"]) -> ListUploadsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_vpce_configurations"]
    ) -> ListVPCEConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """
