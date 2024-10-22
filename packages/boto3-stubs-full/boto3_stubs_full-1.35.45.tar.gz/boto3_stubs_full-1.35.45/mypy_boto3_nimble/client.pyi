"""
Type annotations for nimble service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_nimble.client import NimbleStudioClient

    session = Session()
    client: NimbleStudioClient = session.client("nimble")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListEulaAcceptancesPaginator,
    ListEulasPaginator,
    ListLaunchProfileMembersPaginator,
    ListLaunchProfilesPaginator,
    ListStreamingImagesPaginator,
    ListStreamingSessionBackupsPaginator,
    ListStreamingSessionsPaginator,
    ListStudioComponentsPaginator,
    ListStudioMembersPaginator,
    ListStudiosPaginator,
)
from .type_defs import (
    AcceptEulasRequestRequestTypeDef,
    AcceptEulasResponseTypeDef,
    CreateLaunchProfileRequestRequestTypeDef,
    CreateLaunchProfileResponseTypeDef,
    CreateStreamingImageRequestRequestTypeDef,
    CreateStreamingImageResponseTypeDef,
    CreateStreamingSessionRequestRequestTypeDef,
    CreateStreamingSessionResponseTypeDef,
    CreateStreamingSessionStreamRequestRequestTypeDef,
    CreateStreamingSessionStreamResponseTypeDef,
    CreateStudioComponentRequestRequestTypeDef,
    CreateStudioComponentResponseTypeDef,
    CreateStudioRequestRequestTypeDef,
    CreateStudioResponseTypeDef,
    DeleteLaunchProfileMemberRequestRequestTypeDef,
    DeleteLaunchProfileRequestRequestTypeDef,
    DeleteLaunchProfileResponseTypeDef,
    DeleteStreamingImageRequestRequestTypeDef,
    DeleteStreamingImageResponseTypeDef,
    DeleteStreamingSessionRequestRequestTypeDef,
    DeleteStreamingSessionResponseTypeDef,
    DeleteStudioComponentRequestRequestTypeDef,
    DeleteStudioComponentResponseTypeDef,
    DeleteStudioMemberRequestRequestTypeDef,
    DeleteStudioRequestRequestTypeDef,
    DeleteStudioResponseTypeDef,
    GetEulaRequestRequestTypeDef,
    GetEulaResponseTypeDef,
    GetLaunchProfileDetailsRequestRequestTypeDef,
    GetLaunchProfileDetailsResponseTypeDef,
    GetLaunchProfileInitializationRequestRequestTypeDef,
    GetLaunchProfileInitializationResponseTypeDef,
    GetLaunchProfileMemberRequestRequestTypeDef,
    GetLaunchProfileMemberResponseTypeDef,
    GetLaunchProfileRequestRequestTypeDef,
    GetLaunchProfileResponseTypeDef,
    GetStreamingImageRequestRequestTypeDef,
    GetStreamingImageResponseTypeDef,
    GetStreamingSessionBackupRequestRequestTypeDef,
    GetStreamingSessionBackupResponseTypeDef,
    GetStreamingSessionRequestRequestTypeDef,
    GetStreamingSessionResponseTypeDef,
    GetStreamingSessionStreamRequestRequestTypeDef,
    GetStreamingSessionStreamResponseTypeDef,
    GetStudioComponentRequestRequestTypeDef,
    GetStudioComponentResponseTypeDef,
    GetStudioMemberRequestRequestTypeDef,
    GetStudioMemberResponseTypeDef,
    GetStudioRequestRequestTypeDef,
    GetStudioResponseTypeDef,
    ListEulaAcceptancesRequestRequestTypeDef,
    ListEulaAcceptancesResponseTypeDef,
    ListEulasRequestRequestTypeDef,
    ListEulasResponseTypeDef,
    ListLaunchProfileMembersRequestRequestTypeDef,
    ListLaunchProfileMembersResponseTypeDef,
    ListLaunchProfilesRequestRequestTypeDef,
    ListLaunchProfilesResponseTypeDef,
    ListStreamingImagesRequestRequestTypeDef,
    ListStreamingImagesResponseTypeDef,
    ListStreamingSessionBackupsRequestRequestTypeDef,
    ListStreamingSessionBackupsResponseTypeDef,
    ListStreamingSessionsRequestRequestTypeDef,
    ListStreamingSessionsResponseTypeDef,
    ListStudioComponentsRequestRequestTypeDef,
    ListStudioComponentsResponseTypeDef,
    ListStudioMembersRequestRequestTypeDef,
    ListStudioMembersResponseTypeDef,
    ListStudiosRequestRequestTypeDef,
    ListStudiosResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutLaunchProfileMembersRequestRequestTypeDef,
    PutStudioMembersRequestRequestTypeDef,
    StartStreamingSessionRequestRequestTypeDef,
    StartStreamingSessionResponseTypeDef,
    StartStudioSSOConfigurationRepairRequestRequestTypeDef,
    StartStudioSSOConfigurationRepairResponseTypeDef,
    StopStreamingSessionRequestRequestTypeDef,
    StopStreamingSessionResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateLaunchProfileMemberRequestRequestTypeDef,
    UpdateLaunchProfileMemberResponseTypeDef,
    UpdateLaunchProfileRequestRequestTypeDef,
    UpdateLaunchProfileResponseTypeDef,
    UpdateStreamingImageRequestRequestTypeDef,
    UpdateStreamingImageResponseTypeDef,
    UpdateStudioComponentRequestRequestTypeDef,
    UpdateStudioComponentResponseTypeDef,
    UpdateStudioRequestRequestTypeDef,
    UpdateStudioResponseTypeDef,
)
from .waiter import (
    LaunchProfileDeletedWaiter,
    LaunchProfileReadyWaiter,
    StreamingImageDeletedWaiter,
    StreamingImageReadyWaiter,
    StreamingSessionDeletedWaiter,
    StreamingSessionReadyWaiter,
    StreamingSessionStoppedWaiter,
    StreamingSessionStreamReadyWaiter,
    StudioComponentDeletedWaiter,
    StudioComponentReadyWaiter,
    StudioDeletedWaiter,
    StudioReadyWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("NimbleStudioClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NimbleStudioClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NimbleStudioClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#exceptions)
        """

    def accept_eulas(
        self, **kwargs: Unpack[AcceptEulasRequestRequestTypeDef]
    ) -> AcceptEulasResponseTypeDef:
        """
        Accept EULAs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.accept_eulas)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#accept_eulas)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#close)
        """

    def create_launch_profile(
        self, **kwargs: Unpack[CreateLaunchProfileRequestRequestTypeDef]
    ) -> CreateLaunchProfileResponseTypeDef:
        """
        Create a launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_launch_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#create_launch_profile)
        """

    def create_streaming_image(
        self, **kwargs: Unpack[CreateStreamingImageRequestRequestTypeDef]
    ) -> CreateStreamingImageResponseTypeDef:
        """
        Creates a streaming image resource in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_streaming_image)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#create_streaming_image)
        """

    def create_streaming_session(
        self, **kwargs: Unpack[CreateStreamingSessionRequestRequestTypeDef]
    ) -> CreateStreamingSessionResponseTypeDef:
        """
        Creates a streaming session in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#create_streaming_session)
        """

    def create_streaming_session_stream(
        self, **kwargs: Unpack[CreateStreamingSessionStreamRequestRequestTypeDef]
    ) -> CreateStreamingSessionStreamResponseTypeDef:
        """
        Creates a streaming session stream for a streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session_stream)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#create_streaming_session_stream)
        """

    def create_studio(
        self, **kwargs: Unpack[CreateStudioRequestRequestTypeDef]
    ) -> CreateStudioResponseTypeDef:
        """
        Create a new studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_studio)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#create_studio)
        """

    def create_studio_component(
        self, **kwargs: Unpack[CreateStudioComponentRequestRequestTypeDef]
    ) -> CreateStudioComponentResponseTypeDef:
        """
        Creates a studio component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_studio_component)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#create_studio_component)
        """

    def delete_launch_profile(
        self, **kwargs: Unpack[DeleteLaunchProfileRequestRequestTypeDef]
    ) -> DeleteLaunchProfileResponseTypeDef:
        """
        Permanently delete a launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#delete_launch_profile)
        """

    def delete_launch_profile_member(
        self, **kwargs: Unpack[DeleteLaunchProfileMemberRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a user from launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile_member)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#delete_launch_profile_member)
        """

    def delete_streaming_image(
        self, **kwargs: Unpack[DeleteStreamingImageRequestRequestTypeDef]
    ) -> DeleteStreamingImageResponseTypeDef:
        """
        Delete streaming image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_image)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#delete_streaming_image)
        """

    def delete_streaming_session(
        self, **kwargs: Unpack[DeleteStreamingSessionRequestRequestTypeDef]
    ) -> DeleteStreamingSessionResponseTypeDef:
        """
        Deletes streaming session resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#delete_streaming_session)
        """

    def delete_studio(
        self, **kwargs: Unpack[DeleteStudioRequestRequestTypeDef]
    ) -> DeleteStudioResponseTypeDef:
        """
        Delete a studio resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_studio)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#delete_studio)
        """

    def delete_studio_component(
        self, **kwargs: Unpack[DeleteStudioComponentRequestRequestTypeDef]
    ) -> DeleteStudioComponentResponseTypeDef:
        """
        Deletes a studio component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_studio_component)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#delete_studio_component)
        """

    def delete_studio_member(
        self, **kwargs: Unpack[DeleteStudioMemberRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a user from studio membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_studio_member)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#delete_studio_member)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#generate_presigned_url)
        """

    def get_eula(self, **kwargs: Unpack[GetEulaRequestRequestTypeDef]) -> GetEulaResponseTypeDef:
        """
        Get EULA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_eula)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_eula)
        """

    def get_launch_profile(
        self, **kwargs: Unpack[GetLaunchProfileRequestRequestTypeDef]
    ) -> GetLaunchProfileResponseTypeDef:
        """
        Get a launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_launch_profile)
        """

    def get_launch_profile_details(
        self, **kwargs: Unpack[GetLaunchProfileDetailsRequestRequestTypeDef]
    ) -> GetLaunchProfileDetailsResponseTypeDef:
        """
        Launch profile details include the launch profile resource and summary
        information of resources that are used by, or available to, the launch
        profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_details)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_launch_profile_details)
        """

    def get_launch_profile_initialization(
        self, **kwargs: Unpack[GetLaunchProfileInitializationRequestRequestTypeDef]
    ) -> GetLaunchProfileInitializationResponseTypeDef:
        """
        Get a launch profile initialization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_initialization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_launch_profile_initialization)
        """

    def get_launch_profile_member(
        self, **kwargs: Unpack[GetLaunchProfileMemberRequestRequestTypeDef]
    ) -> GetLaunchProfileMemberResponseTypeDef:
        """
        Get a user persona in launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_member)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_launch_profile_member)
        """

    def get_streaming_image(
        self, **kwargs: Unpack[GetStreamingImageRequestRequestTypeDef]
    ) -> GetStreamingImageResponseTypeDef:
        """
        Get streaming image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_streaming_image)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_streaming_image)
        """

    def get_streaming_session(
        self, **kwargs: Unpack[GetStreamingSessionRequestRequestTypeDef]
    ) -> GetStreamingSessionResponseTypeDef:
        """
        Gets StreamingSession resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_streaming_session)
        """

    def get_streaming_session_backup(
        self, **kwargs: Unpack[GetStreamingSessionBackupRequestRequestTypeDef]
    ) -> GetStreamingSessionBackupResponseTypeDef:
        """
        Gets `StreamingSessionBackup` resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session_backup)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_streaming_session_backup)
        """

    def get_streaming_session_stream(
        self, **kwargs: Unpack[GetStreamingSessionStreamRequestRequestTypeDef]
    ) -> GetStreamingSessionStreamResponseTypeDef:
        """
        Gets a StreamingSessionStream for a streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session_stream)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_streaming_session_stream)
        """

    def get_studio(
        self, **kwargs: Unpack[GetStudioRequestRequestTypeDef]
    ) -> GetStudioResponseTypeDef:
        """
        Get a studio resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_studio)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_studio)
        """

    def get_studio_component(
        self, **kwargs: Unpack[GetStudioComponentRequestRequestTypeDef]
    ) -> GetStudioComponentResponseTypeDef:
        """
        Gets a studio component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_studio_component)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_studio_component)
        """

    def get_studio_member(
        self, **kwargs: Unpack[GetStudioMemberRequestRequestTypeDef]
    ) -> GetStudioMemberResponseTypeDef:
        """
        Get a user's membership in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_studio_member)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_studio_member)
        """

    def list_eula_acceptances(
        self, **kwargs: Unpack[ListEulaAcceptancesRequestRequestTypeDef]
    ) -> ListEulaAcceptancesResponseTypeDef:
        """
        List EULA acceptances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_eula_acceptances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_eula_acceptances)
        """

    def list_eulas(
        self, **kwargs: Unpack[ListEulasRequestRequestTypeDef]
    ) -> ListEulasResponseTypeDef:
        """
        List EULAs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_eulas)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_eulas)
        """

    def list_launch_profile_members(
        self, **kwargs: Unpack[ListLaunchProfileMembersRequestRequestTypeDef]
    ) -> ListLaunchProfileMembersResponseTypeDef:
        """
        Get all users in a given launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_launch_profile_members)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_launch_profile_members)
        """

    def list_launch_profiles(
        self, **kwargs: Unpack[ListLaunchProfilesRequestRequestTypeDef]
    ) -> ListLaunchProfilesResponseTypeDef:
        """
        List all the launch profiles a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_launch_profiles)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_launch_profiles)
        """

    def list_streaming_images(
        self, **kwargs: Unpack[ListStreamingImagesRequestRequestTypeDef]
    ) -> ListStreamingImagesResponseTypeDef:
        """
        List the streaming image resources available to this studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_streaming_images)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_streaming_images)
        """

    def list_streaming_session_backups(
        self, **kwargs: Unpack[ListStreamingSessionBackupsRequestRequestTypeDef]
    ) -> ListStreamingSessionBackupsResponseTypeDef:
        """
        Lists the backups of a streaming session in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_streaming_session_backups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_streaming_session_backups)
        """

    def list_streaming_sessions(
        self, **kwargs: Unpack[ListStreamingSessionsRequestRequestTypeDef]
    ) -> ListStreamingSessionsResponseTypeDef:
        """
        Lists the streaming sessions in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_streaming_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_streaming_sessions)
        """

    def list_studio_components(
        self, **kwargs: Unpack[ListStudioComponentsRequestRequestTypeDef]
    ) -> ListStudioComponentsResponseTypeDef:
        """
        Lists the `StudioComponents` in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_studio_components)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_studio_components)
        """

    def list_studio_members(
        self, **kwargs: Unpack[ListStudioMembersRequestRequestTypeDef]
    ) -> ListStudioMembersResponseTypeDef:
        """
        Get all users in a given studio membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_studio_members)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_studio_members)
        """

    def list_studios(
        self, **kwargs: Unpack[ListStudiosRequestRequestTypeDef]
    ) -> ListStudiosResponseTypeDef:
        """
        List studios in your Amazon Web Services accounts in the requested Amazon Web
        Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_studios)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_studios)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets the tags for a resource, given its Amazon Resource Names (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#list_tags_for_resource)
        """

    def put_launch_profile_members(
        self, **kwargs: Unpack[PutLaunchProfileMembersRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Add/update users with given persona to launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.put_launch_profile_members)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#put_launch_profile_members)
        """

    def put_studio_members(
        self, **kwargs: Unpack[PutStudioMembersRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Add/update users with given persona to studio membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.put_studio_members)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#put_studio_members)
        """

    def start_streaming_session(
        self, **kwargs: Unpack[StartStreamingSessionRequestRequestTypeDef]
    ) -> StartStreamingSessionResponseTypeDef:
        """
        Transitions sessions from the `STOPPED` state into the `READY` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.start_streaming_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#start_streaming_session)
        """

    def start_studio_sso_configuration_repair(
        self, **kwargs: Unpack[StartStudioSSOConfigurationRepairRequestRequestTypeDef]
    ) -> StartStudioSSOConfigurationRepairResponseTypeDef:
        """
        Repairs the IAM Identity Center configuration for a given studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.start_studio_sso_configuration_repair)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#start_studio_sso_configuration_repair)
        """

    def stop_streaming_session(
        self, **kwargs: Unpack[StopStreamingSessionRequestRequestTypeDef]
    ) -> StopStreamingSessionResponseTypeDef:
        """
        Transitions sessions from the `READY` state into the `STOPPED` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.stop_streaming_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#stop_streaming_session)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates tags for a resource, given its ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#untag_resource)
        """

    def update_launch_profile(
        self, **kwargs: Unpack[UpdateLaunchProfileRequestRequestTypeDef]
    ) -> UpdateLaunchProfileResponseTypeDef:
        """
        Update a launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#update_launch_profile)
        """

    def update_launch_profile_member(
        self, **kwargs: Unpack[UpdateLaunchProfileMemberRequestRequestTypeDef]
    ) -> UpdateLaunchProfileMemberResponseTypeDef:
        """
        Update a user persona in launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile_member)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#update_launch_profile_member)
        """

    def update_streaming_image(
        self, **kwargs: Unpack[UpdateStreamingImageRequestRequestTypeDef]
    ) -> UpdateStreamingImageResponseTypeDef:
        """
        Update streaming image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_streaming_image)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#update_streaming_image)
        """

    def update_studio(
        self, **kwargs: Unpack[UpdateStudioRequestRequestTypeDef]
    ) -> UpdateStudioResponseTypeDef:
        """
        Update a Studio resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_studio)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#update_studio)
        """

    def update_studio_component(
        self, **kwargs: Unpack[UpdateStudioComponentRequestRequestTypeDef]
    ) -> UpdateStudioComponentResponseTypeDef:
        """
        Updates a studio component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_studio_component)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#update_studio_component)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_eula_acceptances"]
    ) -> ListEulaAcceptancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_eulas"]) -> ListEulasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_profile_members"]
    ) -> ListLaunchProfileMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_profiles"]
    ) -> ListLaunchProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_images"]
    ) -> ListStreamingImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_session_backups"]
    ) -> ListStreamingSessionBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_sessions"]
    ) -> ListStreamingSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_components"]
    ) -> ListStudioComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_members"]
    ) -> ListStudioMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_studios"]) -> ListStudiosPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_paginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["launch_profile_deleted"]
    ) -> LaunchProfileDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["launch_profile_ready"]) -> LaunchProfileReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_image_deleted"]
    ) -> StreamingImageDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_image_ready"]
    ) -> StreamingImageReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_session_deleted"]
    ) -> StreamingSessionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_session_ready"]
    ) -> StreamingSessionReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_session_stopped"]
    ) -> StreamingSessionStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_session_stream_ready"]
    ) -> StreamingSessionStreamReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["studio_component_deleted"]
    ) -> StudioComponentDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["studio_component_ready"]
    ) -> StudioComponentReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["studio_deleted"]) -> StudioDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["studio_ready"]) -> StudioReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/client/#get_waiter)
        """
