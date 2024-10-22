"""
Type annotations for gamelift service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_gamelift.client import GameLiftClient

    session = Session()
    client: GameLiftClient = session.client("gamelift")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeFleetAttributesPaginator,
    DescribeFleetCapacityPaginator,
    DescribeFleetEventsPaginator,
    DescribeFleetUtilizationPaginator,
    DescribeGameServerInstancesPaginator,
    DescribeGameSessionDetailsPaginator,
    DescribeGameSessionQueuesPaginator,
    DescribeGameSessionsPaginator,
    DescribeInstancesPaginator,
    DescribeMatchmakingConfigurationsPaginator,
    DescribeMatchmakingRuleSetsPaginator,
    DescribePlayerSessionsPaginator,
    DescribeScalingPoliciesPaginator,
    ListAliasesPaginator,
    ListBuildsPaginator,
    ListComputePaginator,
    ListContainerGroupDefinitionsPaginator,
    ListFleetsPaginator,
    ListGameServerGroupsPaginator,
    ListGameServersPaginator,
    ListLocationsPaginator,
    ListScriptsPaginator,
    SearchGameSessionsPaginator,
)
from .type_defs import (
    AcceptMatchInputRequestTypeDef,
    ClaimGameServerInputRequestTypeDef,
    ClaimGameServerOutputTypeDef,
    CreateAliasInputRequestTypeDef,
    CreateAliasOutputTypeDef,
    CreateBuildInputRequestTypeDef,
    CreateBuildOutputTypeDef,
    CreateContainerGroupDefinitionInputRequestTypeDef,
    CreateContainerGroupDefinitionOutputTypeDef,
    CreateFleetInputRequestTypeDef,
    CreateFleetLocationsInputRequestTypeDef,
    CreateFleetLocationsOutputTypeDef,
    CreateFleetOutputTypeDef,
    CreateGameServerGroupInputRequestTypeDef,
    CreateGameServerGroupOutputTypeDef,
    CreateGameSessionInputRequestTypeDef,
    CreateGameSessionOutputTypeDef,
    CreateGameSessionQueueInputRequestTypeDef,
    CreateGameSessionQueueOutputTypeDef,
    CreateLocationInputRequestTypeDef,
    CreateLocationOutputTypeDef,
    CreateMatchmakingConfigurationInputRequestTypeDef,
    CreateMatchmakingConfigurationOutputTypeDef,
    CreateMatchmakingRuleSetInputRequestTypeDef,
    CreateMatchmakingRuleSetOutputTypeDef,
    CreatePlayerSessionInputRequestTypeDef,
    CreatePlayerSessionOutputTypeDef,
    CreatePlayerSessionsInputRequestTypeDef,
    CreatePlayerSessionsOutputTypeDef,
    CreateScriptInputRequestTypeDef,
    CreateScriptOutputTypeDef,
    CreateVpcPeeringAuthorizationInputRequestTypeDef,
    CreateVpcPeeringAuthorizationOutputTypeDef,
    CreateVpcPeeringConnectionInputRequestTypeDef,
    DeleteAliasInputRequestTypeDef,
    DeleteBuildInputRequestTypeDef,
    DeleteContainerGroupDefinitionInputRequestTypeDef,
    DeleteFleetInputRequestTypeDef,
    DeleteFleetLocationsInputRequestTypeDef,
    DeleteFleetLocationsOutputTypeDef,
    DeleteGameServerGroupInputRequestTypeDef,
    DeleteGameServerGroupOutputTypeDef,
    DeleteGameSessionQueueInputRequestTypeDef,
    DeleteLocationInputRequestTypeDef,
    DeleteMatchmakingConfigurationInputRequestTypeDef,
    DeleteMatchmakingRuleSetInputRequestTypeDef,
    DeleteScalingPolicyInputRequestTypeDef,
    DeleteScriptInputRequestTypeDef,
    DeleteVpcPeeringAuthorizationInputRequestTypeDef,
    DeleteVpcPeeringConnectionInputRequestTypeDef,
    DeregisterComputeInputRequestTypeDef,
    DeregisterGameServerInputRequestTypeDef,
    DescribeAliasInputRequestTypeDef,
    DescribeAliasOutputTypeDef,
    DescribeBuildInputRequestTypeDef,
    DescribeBuildOutputTypeDef,
    DescribeComputeInputRequestTypeDef,
    DescribeComputeOutputTypeDef,
    DescribeContainerGroupDefinitionInputRequestTypeDef,
    DescribeContainerGroupDefinitionOutputTypeDef,
    DescribeEC2InstanceLimitsInputRequestTypeDef,
    DescribeEC2InstanceLimitsOutputTypeDef,
    DescribeFleetAttributesInputRequestTypeDef,
    DescribeFleetAttributesOutputTypeDef,
    DescribeFleetCapacityInputRequestTypeDef,
    DescribeFleetCapacityOutputTypeDef,
    DescribeFleetEventsInputRequestTypeDef,
    DescribeFleetEventsOutputTypeDef,
    DescribeFleetLocationAttributesInputRequestTypeDef,
    DescribeFleetLocationAttributesOutputTypeDef,
    DescribeFleetLocationCapacityInputRequestTypeDef,
    DescribeFleetLocationCapacityOutputTypeDef,
    DescribeFleetLocationUtilizationInputRequestTypeDef,
    DescribeFleetLocationUtilizationOutputTypeDef,
    DescribeFleetPortSettingsInputRequestTypeDef,
    DescribeFleetPortSettingsOutputTypeDef,
    DescribeFleetUtilizationInputRequestTypeDef,
    DescribeFleetUtilizationOutputTypeDef,
    DescribeGameServerGroupInputRequestTypeDef,
    DescribeGameServerGroupOutputTypeDef,
    DescribeGameServerInputRequestTypeDef,
    DescribeGameServerInstancesInputRequestTypeDef,
    DescribeGameServerInstancesOutputTypeDef,
    DescribeGameServerOutputTypeDef,
    DescribeGameSessionDetailsInputRequestTypeDef,
    DescribeGameSessionDetailsOutputTypeDef,
    DescribeGameSessionPlacementInputRequestTypeDef,
    DescribeGameSessionPlacementOutputTypeDef,
    DescribeGameSessionQueuesInputRequestTypeDef,
    DescribeGameSessionQueuesOutputTypeDef,
    DescribeGameSessionsInputRequestTypeDef,
    DescribeGameSessionsOutputTypeDef,
    DescribeInstancesInputRequestTypeDef,
    DescribeInstancesOutputTypeDef,
    DescribeMatchmakingConfigurationsInputRequestTypeDef,
    DescribeMatchmakingConfigurationsOutputTypeDef,
    DescribeMatchmakingInputRequestTypeDef,
    DescribeMatchmakingOutputTypeDef,
    DescribeMatchmakingRuleSetsInputRequestTypeDef,
    DescribeMatchmakingRuleSetsOutputTypeDef,
    DescribePlayerSessionsInputRequestTypeDef,
    DescribePlayerSessionsOutputTypeDef,
    DescribeRuntimeConfigurationInputRequestTypeDef,
    DescribeRuntimeConfigurationOutputTypeDef,
    DescribeScalingPoliciesInputRequestTypeDef,
    DescribeScalingPoliciesOutputTypeDef,
    DescribeScriptInputRequestTypeDef,
    DescribeScriptOutputTypeDef,
    DescribeVpcPeeringAuthorizationsOutputTypeDef,
    DescribeVpcPeeringConnectionsInputRequestTypeDef,
    DescribeVpcPeeringConnectionsOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetComputeAccessInputRequestTypeDef,
    GetComputeAccessOutputTypeDef,
    GetComputeAuthTokenInputRequestTypeDef,
    GetComputeAuthTokenOutputTypeDef,
    GetGameSessionLogUrlInputRequestTypeDef,
    GetGameSessionLogUrlOutputTypeDef,
    GetInstanceAccessInputRequestTypeDef,
    GetInstanceAccessOutputTypeDef,
    ListAliasesInputRequestTypeDef,
    ListAliasesOutputTypeDef,
    ListBuildsInputRequestTypeDef,
    ListBuildsOutputTypeDef,
    ListComputeInputRequestTypeDef,
    ListComputeOutputTypeDef,
    ListContainerGroupDefinitionsInputRequestTypeDef,
    ListContainerGroupDefinitionsOutputTypeDef,
    ListFleetsInputRequestTypeDef,
    ListFleetsOutputTypeDef,
    ListGameServerGroupsInputRequestTypeDef,
    ListGameServerGroupsOutputTypeDef,
    ListGameServersInputRequestTypeDef,
    ListGameServersOutputTypeDef,
    ListLocationsInputRequestTypeDef,
    ListLocationsOutputTypeDef,
    ListScriptsInputRequestTypeDef,
    ListScriptsOutputTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutScalingPolicyInputRequestTypeDef,
    PutScalingPolicyOutputTypeDef,
    RegisterComputeInputRequestTypeDef,
    RegisterComputeOutputTypeDef,
    RegisterGameServerInputRequestTypeDef,
    RegisterGameServerOutputTypeDef,
    RequestUploadCredentialsInputRequestTypeDef,
    RequestUploadCredentialsOutputTypeDef,
    ResolveAliasInputRequestTypeDef,
    ResolveAliasOutputTypeDef,
    ResumeGameServerGroupInputRequestTypeDef,
    ResumeGameServerGroupOutputTypeDef,
    SearchGameSessionsInputRequestTypeDef,
    SearchGameSessionsOutputTypeDef,
    StartFleetActionsInputRequestTypeDef,
    StartFleetActionsOutputTypeDef,
    StartGameSessionPlacementInputRequestTypeDef,
    StartGameSessionPlacementOutputTypeDef,
    StartMatchBackfillInputRequestTypeDef,
    StartMatchBackfillOutputTypeDef,
    StartMatchmakingInputRequestTypeDef,
    StartMatchmakingOutputTypeDef,
    StopFleetActionsInputRequestTypeDef,
    StopFleetActionsOutputTypeDef,
    StopGameSessionPlacementInputRequestTypeDef,
    StopGameSessionPlacementOutputTypeDef,
    StopMatchmakingInputRequestTypeDef,
    SuspendGameServerGroupInputRequestTypeDef,
    SuspendGameServerGroupOutputTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAliasInputRequestTypeDef,
    UpdateAliasOutputTypeDef,
    UpdateBuildInputRequestTypeDef,
    UpdateBuildOutputTypeDef,
    UpdateFleetAttributesInputRequestTypeDef,
    UpdateFleetAttributesOutputTypeDef,
    UpdateFleetCapacityInputRequestTypeDef,
    UpdateFleetCapacityOutputTypeDef,
    UpdateFleetPortSettingsInputRequestTypeDef,
    UpdateFleetPortSettingsOutputTypeDef,
    UpdateGameServerGroupInputRequestTypeDef,
    UpdateGameServerGroupOutputTypeDef,
    UpdateGameServerInputRequestTypeDef,
    UpdateGameServerOutputTypeDef,
    UpdateGameSessionInputRequestTypeDef,
    UpdateGameSessionOutputTypeDef,
    UpdateGameSessionQueueInputRequestTypeDef,
    UpdateGameSessionQueueOutputTypeDef,
    UpdateMatchmakingConfigurationInputRequestTypeDef,
    UpdateMatchmakingConfigurationOutputTypeDef,
    UpdateRuntimeConfigurationInputRequestTypeDef,
    UpdateRuntimeConfigurationOutputTypeDef,
    UpdateScriptInputRequestTypeDef,
    UpdateScriptOutputTypeDef,
    ValidateMatchmakingRuleSetInputRequestTypeDef,
    ValidateMatchmakingRuleSetOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("GameLiftClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    FleetCapacityExceededException: Type[BotocoreClientError]
    GameSessionFullException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidFleetStatusException: Type[BotocoreClientError]
    InvalidGameSessionStatusException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    NotReadyException: Type[BotocoreClientError]
    OutOfCapacityException: Type[BotocoreClientError]
    TaggingFailedException: Type[BotocoreClientError]
    TerminalRoutingStrategyException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnsupportedRegionException: Type[BotocoreClientError]


class GameLiftClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GameLiftClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#exceptions)
        """

    def accept_match(self, **kwargs: Unpack[AcceptMatchInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Registers a player's acceptance or rejection of a proposed FlexMatch match.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.accept_match)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#accept_match)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#can_paginate)
        """

    def claim_game_server(
        self, **kwargs: Unpack[ClaimGameServerInputRequestTypeDef]
    ) -> ClaimGameServerOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Locates an available game server and temporarily reserves it
        to host gameplay and
        players.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.claim_game_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#claim_game_server)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#close)
        """

    def create_alias(
        self, **kwargs: Unpack[CreateAliasInputRequestTypeDef]
    ) -> CreateAliasOutputTypeDef:
        """
        Creates an alias for a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_alias)
        """

    def create_build(
        self, **kwargs: Unpack[CreateBuildInputRequestTypeDef]
    ) -> CreateBuildOutputTypeDef:
        """
        Creates a new Amazon GameLift build resource for your game server binary files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_build)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_build)
        """

    def create_container_group_definition(
        self, **kwargs: Unpack[CreateContainerGroupDefinitionInputRequestTypeDef]
    ) -> CreateContainerGroupDefinitionOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift containers feature, which is
        currently in public preview.** Creates a `ContainerGroupDefinition` resource
        that describes a set of containers for hosting your game server with Amazon
        GameLift managed EC2
        hosting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_container_group_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_container_group_definition)
        """

    def create_fleet(
        self, **kwargs: Unpack[CreateFleetInputRequestTypeDef]
    ) -> CreateFleetOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Creates a fleet of compute
        resources to host your game
        servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_fleet)
        """

    def create_fleet_locations(
        self, **kwargs: Unpack[CreateFleetLocationsInputRequestTypeDef]
    ) -> CreateFleetLocationsOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Adds remote locations to an
        EC2 or container fleet and begins populating the new locations with
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_fleet_locations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_fleet_locations)
        """

    def create_game_server_group(
        self, **kwargs: Unpack[CreateGameServerGroupInputRequestTypeDef]
    ) -> CreateGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Creates a Amazon GameLift FleetIQ game server group for
        managing game hosting on a collection of Amazon Elastic Compute Cloud instances
        for game
        hosting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_game_server_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_game_server_group)
        """

    def create_game_session(
        self, **kwargs: Unpack[CreateGameSessionInputRequestTypeDef]
    ) -> CreateGameSessionOutputTypeDef:
        """
        Creates a multiplayer game session for players in a specific fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_game_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_game_session)
        """

    def create_game_session_queue(
        self, **kwargs: Unpack[CreateGameSessionQueueInputRequestTypeDef]
    ) -> CreateGameSessionQueueOutputTypeDef:
        """
        Creates a placement queue that processes requests for new game sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_game_session_queue)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_game_session_queue)
        """

    def create_location(
        self, **kwargs: Unpack[CreateLocationInputRequestTypeDef]
    ) -> CreateLocationOutputTypeDef:
        """
        Creates a custom location for use in an Anywhere fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_location)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_location)
        """

    def create_matchmaking_configuration(
        self, **kwargs: Unpack[CreateMatchmakingConfigurationInputRequestTypeDef]
    ) -> CreateMatchmakingConfigurationOutputTypeDef:
        """
        Defines a new matchmaking configuration for use with FlexMatch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_matchmaking_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_matchmaking_configuration)
        """

    def create_matchmaking_rule_set(
        self, **kwargs: Unpack[CreateMatchmakingRuleSetInputRequestTypeDef]
    ) -> CreateMatchmakingRuleSetOutputTypeDef:
        """
        Creates a new rule set for FlexMatch matchmaking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_matchmaking_rule_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_matchmaking_rule_set)
        """

    def create_player_session(
        self, **kwargs: Unpack[CreatePlayerSessionInputRequestTypeDef]
    ) -> CreatePlayerSessionOutputTypeDef:
        """
        Reserves an open player slot in a game session for a player.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_player_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_player_session)
        """

    def create_player_sessions(
        self, **kwargs: Unpack[CreatePlayerSessionsInputRequestTypeDef]
    ) -> CreatePlayerSessionsOutputTypeDef:
        """
        Reserves open slots in a game session for a group of players.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_player_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_player_sessions)
        """

    def create_script(
        self, **kwargs: Unpack[CreateScriptInputRequestTypeDef]
    ) -> CreateScriptOutputTypeDef:
        """
        Creates a new script record for your Realtime Servers script.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_script)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_script)
        """

    def create_vpc_peering_authorization(
        self, **kwargs: Unpack[CreateVpcPeeringAuthorizationInputRequestTypeDef]
    ) -> CreateVpcPeeringAuthorizationOutputTypeDef:
        """
        Requests authorization to create or delete a peer connection between the VPC
        for your Amazon GameLift fleet and a virtual private cloud (VPC) in your Amazon
        Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_authorization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_vpc_peering_authorization)
        """

    def create_vpc_peering_connection(
        self, **kwargs: Unpack[CreateVpcPeeringConnectionInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Establishes a VPC peering connection between a virtual private cloud (VPC) in
        an Amazon Web Services account with the VPC for your Amazon GameLift
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_connection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#create_vpc_peering_connection)
        """

    def delete_alias(
        self, **kwargs: Unpack[DeleteAliasInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_alias)
        """

    def delete_build(
        self, **kwargs: Unpack[DeleteBuildInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_build)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_build)
        """

    def delete_container_group_definition(
        self, **kwargs: Unpack[DeleteContainerGroupDefinitionInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        **This operation is used with the Amazon GameLift containers feature, which is
        currently in public preview.** Deletes a container group definition
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_container_group_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_container_group_definition)
        """

    def delete_fleet(
        self, **kwargs: Unpack[DeleteFleetInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes all resources and information related to a fleet and shuts down any
        currently running fleet instances, including those in remote
        locations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_fleet)
        """

    def delete_fleet_locations(
        self, **kwargs: Unpack[DeleteFleetLocationsInputRequestTypeDef]
    ) -> DeleteFleetLocationsOutputTypeDef:
        """
        Removes locations from a multi-location fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_fleet_locations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_fleet_locations)
        """

    def delete_game_server_group(
        self, **kwargs: Unpack[DeleteGameServerGroupInputRequestTypeDef]
    ) -> DeleteGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Terminates a game server group and permanently deletes the
        game server group
        record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_game_server_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_game_server_group)
        """

    def delete_game_session_queue(
        self, **kwargs: Unpack[DeleteGameSessionQueueInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a game session queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_game_session_queue)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_game_session_queue)
        """

    def delete_location(
        self, **kwargs: Unpack[DeleteLocationInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a custom location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_location)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_location)
        """

    def delete_matchmaking_configuration(
        self, **kwargs: Unpack[DeleteMatchmakingConfigurationInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Permanently removes a FlexMatch matchmaking configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_matchmaking_configuration)
        """

    def delete_matchmaking_rule_set(
        self, **kwargs: Unpack[DeleteMatchmakingRuleSetInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing matchmaking rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_rule_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_matchmaking_rule_set)
        """

    def delete_scaling_policy(
        self, **kwargs: Unpack[DeleteScalingPolicyInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a fleet scaling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_scaling_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_scaling_policy)
        """

    def delete_script(
        self, **kwargs: Unpack[DeleteScriptInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Realtime script.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_script)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_script)
        """

    def delete_vpc_peering_authorization(
        self, **kwargs: Unpack[DeleteVpcPeeringAuthorizationInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels a pending VPC peering authorization for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_authorization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_vpc_peering_authorization)
        """

    def delete_vpc_peering_connection(
        self, **kwargs: Unpack[DeleteVpcPeeringConnectionInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a VPC peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_connection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#delete_vpc_peering_connection)
        """

    def deregister_compute(
        self, **kwargs: Unpack[DeregisterComputeInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Removes a compute resource
        from an Amazon GameLift Anywhere fleet or container
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.deregister_compute)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#deregister_compute)
        """

    def deregister_game_server(
        self, **kwargs: Unpack[DeregisterGameServerInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Removes the game server from a game server
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.deregister_game_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#deregister_game_server)
        """

    def describe_alias(
        self, **kwargs: Unpack[DescribeAliasInputRequestTypeDef]
    ) -> DescribeAliasOutputTypeDef:
        """
        Retrieves properties for an alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_alias)
        """

    def describe_build(
        self, **kwargs: Unpack[DescribeBuildInputRequestTypeDef]
    ) -> DescribeBuildOutputTypeDef:
        """
        Retrieves properties for a custom game build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_build)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_build)
        """

    def describe_compute(
        self, **kwargs: Unpack[DescribeComputeInputRequestTypeDef]
    ) -> DescribeComputeOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Retrieves properties for a
        compute resource in an Amazon GameLift
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_compute)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_compute)
        """

    def describe_container_group_definition(
        self, **kwargs: Unpack[DescribeContainerGroupDefinitionInputRequestTypeDef]
    ) -> DescribeContainerGroupDefinitionOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift containers feature, which is
        currently in public preview.** Retrieves the properties of a container group
        definition, including all container definitions in the
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_container_group_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_container_group_definition)
        """

    def describe_ec2_instance_limits(
        self, **kwargs: Unpack[DescribeEC2InstanceLimitsInputRequestTypeDef]
    ) -> DescribeEC2InstanceLimitsOutputTypeDef:
        """
        Retrieves the instance limits and current utilization for an Amazon Web
        Services Region or
        location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_ec2_instance_limits)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_ec2_instance_limits)
        """

    def describe_fleet_attributes(
        self, **kwargs: Unpack[DescribeFleetAttributesInputRequestTypeDef]
    ) -> DescribeFleetAttributesOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Retrieves core fleet-wide
        properties for fleets in an Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_fleet_attributes)
        """

    def describe_fleet_capacity(
        self, **kwargs: Unpack[DescribeFleetCapacityInputRequestTypeDef]
    ) -> DescribeFleetCapacityOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Retrieves the resource
        capacity settings for one or more
        fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_capacity)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_fleet_capacity)
        """

    def describe_fleet_events(
        self, **kwargs: Unpack[DescribeFleetEventsInputRequestTypeDef]
    ) -> DescribeFleetEventsOutputTypeDef:
        """
        Retrieves entries from a fleet's event log.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_events)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_fleet_events)
        """

    def describe_fleet_location_attributes(
        self, **kwargs: Unpack[DescribeFleetLocationAttributesInputRequestTypeDef]
    ) -> DescribeFleetLocationAttributesOutputTypeDef:
        """
        Retrieves information on a fleet's remote locations, including life-cycle
        status and any suspended fleet
        activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_fleet_location_attributes)
        """

    def describe_fleet_location_capacity(
        self, **kwargs: Unpack[DescribeFleetLocationCapacityInputRequestTypeDef]
    ) -> DescribeFleetLocationCapacityOutputTypeDef:
        """
        Retrieves the resource capacity settings for a fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_capacity)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_fleet_location_capacity)
        """

    def describe_fleet_location_utilization(
        self, **kwargs: Unpack[DescribeFleetLocationUtilizationInputRequestTypeDef]
    ) -> DescribeFleetLocationUtilizationOutputTypeDef:
        """
        Retrieves current usage data for a fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_utilization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_fleet_location_utilization)
        """

    def describe_fleet_port_settings(
        self, **kwargs: Unpack[DescribeFleetPortSettingsInputRequestTypeDef]
    ) -> DescribeFleetPortSettingsOutputTypeDef:
        """
        Retrieves a fleet's inbound connection permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_port_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_fleet_port_settings)
        """

    def describe_fleet_utilization(
        self, **kwargs: Unpack[DescribeFleetUtilizationInputRequestTypeDef]
    ) -> DescribeFleetUtilizationOutputTypeDef:
        """
        Retrieves utilization statistics for one or more fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_fleet_utilization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_fleet_utilization)
        """

    def describe_game_server(
        self, **kwargs: Unpack[DescribeGameServerInputRequestTypeDef]
    ) -> DescribeGameServerOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Retrieves information for a registered game
        server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_game_server)
        """

    def describe_game_server_group(
        self, **kwargs: Unpack[DescribeGameServerGroupInputRequestTypeDef]
    ) -> DescribeGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Retrieves information on a game server
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_server_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_game_server_group)
        """

    def describe_game_server_instances(
        self, **kwargs: Unpack[DescribeGameServerInstancesInputRequestTypeDef]
    ) -> DescribeGameServerInstancesOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Retrieves status information about the Amazon EC2 instances
        associated with a Amazon GameLift FleetIQ game server
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_server_instances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_game_server_instances)
        """

    def describe_game_session_details(
        self, **kwargs: Unpack[DescribeGameSessionDetailsInputRequestTypeDef]
    ) -> DescribeGameSessionDetailsOutputTypeDef:
        """
        Retrieves additional game session properties, including the game session
        protection policy in force, a set of one or more game sessions in a specific
        fleet
        location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_session_details)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_game_session_details)
        """

    def describe_game_session_placement(
        self, **kwargs: Unpack[DescribeGameSessionPlacementInputRequestTypeDef]
    ) -> DescribeGameSessionPlacementOutputTypeDef:
        """
        Retrieves information, including current status, about a game session placement
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_session_placement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_game_session_placement)
        """

    def describe_game_session_queues(
        self, **kwargs: Unpack[DescribeGameSessionQueuesInputRequestTypeDef]
    ) -> DescribeGameSessionQueuesOutputTypeDef:
        """
        Retrieves the properties for one or more game session queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_session_queues)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_game_session_queues)
        """

    def describe_game_sessions(
        self, **kwargs: Unpack[DescribeGameSessionsInputRequestTypeDef]
    ) -> DescribeGameSessionsOutputTypeDef:
        """
        Retrieves a set of one or more game sessions in a specific fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_game_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_game_sessions)
        """

    def describe_instances(
        self, **kwargs: Unpack[DescribeInstancesInputRequestTypeDef]
    ) -> DescribeInstancesOutputTypeDef:
        """
        Retrieves information about the EC2 instances in an Amazon GameLift managed
        fleet, including instance ID, connection data, and
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_instances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_instances)
        """

    def describe_matchmaking(
        self, **kwargs: Unpack[DescribeMatchmakingInputRequestTypeDef]
    ) -> DescribeMatchmakingOutputTypeDef:
        """
        Retrieves one or more matchmaking tickets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_matchmaking)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_matchmaking)
        """

    def describe_matchmaking_configurations(
        self, **kwargs: Unpack[DescribeMatchmakingConfigurationsInputRequestTypeDef]
    ) -> DescribeMatchmakingConfigurationsOutputTypeDef:
        """
        Retrieves the details of FlexMatch matchmaking configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_configurations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_matchmaking_configurations)
        """

    def describe_matchmaking_rule_sets(
        self, **kwargs: Unpack[DescribeMatchmakingRuleSetsInputRequestTypeDef]
    ) -> DescribeMatchmakingRuleSetsOutputTypeDef:
        """
        Retrieves the details for FlexMatch matchmaking rule sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_rule_sets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_matchmaking_rule_sets)
        """

    def describe_player_sessions(
        self, **kwargs: Unpack[DescribePlayerSessionsInputRequestTypeDef]
    ) -> DescribePlayerSessionsOutputTypeDef:
        """
        Retrieves properties for one or more player sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_player_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_player_sessions)
        """

    def describe_runtime_configuration(
        self, **kwargs: Unpack[DescribeRuntimeConfigurationInputRequestTypeDef]
    ) -> DescribeRuntimeConfigurationOutputTypeDef:
        """
        Retrieves a fleet's runtime configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_runtime_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_runtime_configuration)
        """

    def describe_scaling_policies(
        self, **kwargs: Unpack[DescribeScalingPoliciesInputRequestTypeDef]
    ) -> DescribeScalingPoliciesOutputTypeDef:
        """
        Retrieves all scaling policies applied to a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_scaling_policies)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_scaling_policies)
        """

    def describe_script(
        self, **kwargs: Unpack[DescribeScriptInputRequestTypeDef]
    ) -> DescribeScriptOutputTypeDef:
        """
        Retrieves properties for a Realtime script.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_script)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_script)
        """

    def describe_vpc_peering_authorizations(self) -> DescribeVpcPeeringAuthorizationsOutputTypeDef:
        """
        Retrieves valid VPC peering authorizations that are pending for the Amazon Web
        Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_authorizations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_vpc_peering_authorizations)
        """

    def describe_vpc_peering_connections(
        self, **kwargs: Unpack[DescribeVpcPeeringConnectionsInputRequestTypeDef]
    ) -> DescribeVpcPeeringConnectionsOutputTypeDef:
        """
        Retrieves information on VPC peering connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_connections)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#describe_vpc_peering_connections)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#generate_presigned_url)
        """

    def get_compute_access(
        self, **kwargs: Unpack[GetComputeAccessInputRequestTypeDef]
    ) -> GetComputeAccessOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Requests authorization to
        remotely connect to a hosting resource in a Amazon GameLift managed
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_compute_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_compute_access)
        """

    def get_compute_auth_token(
        self, **kwargs: Unpack[GetComputeAuthTokenInputRequestTypeDef]
    ) -> GetComputeAuthTokenOutputTypeDef:
        """
        Requests an authentication token from Amazon GameLift for a compute resource in
        an Amazon GameLift Anywhere fleet or container
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_compute_auth_token)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_compute_auth_token)
        """

    def get_game_session_log_url(
        self, **kwargs: Unpack[GetGameSessionLogUrlInputRequestTypeDef]
    ) -> GetGameSessionLogUrlOutputTypeDef:
        """
        Retrieves the location of stored game session logs for a specified game session
        on Amazon GameLift managed
        fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_game_session_log_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_game_session_log_url)
        """

    def get_instance_access(
        self, **kwargs: Unpack[GetInstanceAccessInputRequestTypeDef]
    ) -> GetInstanceAccessOutputTypeDef:
        """
        Requests authorization to remotely connect to an instance in an Amazon GameLift
        managed
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_instance_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_instance_access)
        """

    def list_aliases(
        self, **kwargs: Unpack[ListAliasesInputRequestTypeDef]
    ) -> ListAliasesOutputTypeDef:
        """
        Retrieves all aliases for this Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_aliases)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_aliases)
        """

    def list_builds(
        self, **kwargs: Unpack[ListBuildsInputRequestTypeDef]
    ) -> ListBuildsOutputTypeDef:
        """
        Retrieves build resources for all builds associated with the Amazon Web
        Services account in
        use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_builds)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_builds)
        """

    def list_compute(
        self, **kwargs: Unpack[ListComputeInputRequestTypeDef]
    ) -> ListComputeOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Retrieves information on the
        compute resources in an Amazon GameLift
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_compute)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_compute)
        """

    def list_container_group_definitions(
        self, **kwargs: Unpack[ListContainerGroupDefinitionsInputRequestTypeDef]
    ) -> ListContainerGroupDefinitionsOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift containers feature, which is
        currently in public preview.** Retrieves all container group definitions for
        the Amazon Web Services account and Amazon Web Services Region that are
        currently in
        use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_container_group_definitions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_container_group_definitions)
        """

    def list_fleets(
        self, **kwargs: Unpack[ListFleetsInputRequestTypeDef]
    ) -> ListFleetsOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Retrieves a collection of
        fleet resources in an Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_fleets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_fleets)
        """

    def list_game_server_groups(
        self, **kwargs: Unpack[ListGameServerGroupsInputRequestTypeDef]
    ) -> ListGameServerGroupsOutputTypeDef:
        """
        Lists a game server groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_game_server_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_game_server_groups)
        """

    def list_game_servers(
        self, **kwargs: Unpack[ListGameServersInputRequestTypeDef]
    ) -> ListGameServersOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Retrieves information on all game servers that are currently
        active in a specified game server
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_game_servers)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_game_servers)
        """

    def list_locations(
        self, **kwargs: Unpack[ListLocationsInputRequestTypeDef]
    ) -> ListLocationsOutputTypeDef:
        """
        Lists all custom and Amazon Web Services locations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_locations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_locations)
        """

    def list_scripts(
        self, **kwargs: Unpack[ListScriptsInputRequestTypeDef]
    ) -> ListScriptsOutputTypeDef:
        """
        Retrieves script records for all Realtime scripts that are associated with the
        Amazon Web Services account in
        use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_scripts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_scripts)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves all tags assigned to a Amazon GameLift resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#list_tags_for_resource)
        """

    def put_scaling_policy(
        self, **kwargs: Unpack[PutScalingPolicyInputRequestTypeDef]
    ) -> PutScalingPolicyOutputTypeDef:
        """
        Creates or updates a scaling policy for a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.put_scaling_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#put_scaling_policy)
        """

    def register_compute(
        self, **kwargs: Unpack[RegisterComputeInputRequestTypeDef]
    ) -> RegisterComputeOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Registers a compute resource
        in an Amazon GameLift
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.register_compute)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#register_compute)
        """

    def register_game_server(
        self, **kwargs: Unpack[RegisterGameServerInputRequestTypeDef]
    ) -> RegisterGameServerOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Creates a new game server resource and notifies Amazon
        GameLift FleetIQ that the game server is ready to host gameplay and
        players.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.register_game_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#register_game_server)
        """

    def request_upload_credentials(
        self, **kwargs: Unpack[RequestUploadCredentialsInputRequestTypeDef]
    ) -> RequestUploadCredentialsOutputTypeDef:
        """
        Retrieves a fresh set of credentials for use when uploading a new set of game
        build files to Amazon GameLift's Amazon
        S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.request_upload_credentials)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#request_upload_credentials)
        """

    def resolve_alias(
        self, **kwargs: Unpack[ResolveAliasInputRequestTypeDef]
    ) -> ResolveAliasOutputTypeDef:
        """
        Attempts to retrieve a fleet ID that is associated with an alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.resolve_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#resolve_alias)
        """

    def resume_game_server_group(
        self, **kwargs: Unpack[ResumeGameServerGroupInputRequestTypeDef]
    ) -> ResumeGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Reinstates activity on a game server group after it has been
        suspended.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.resume_game_server_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#resume_game_server_group)
        """

    def search_game_sessions(
        self, **kwargs: Unpack[SearchGameSessionsInputRequestTypeDef]
    ) -> SearchGameSessionsOutputTypeDef:
        """
        Retrieves all active game sessions that match a set of search criteria and
        sorts them into a specified
        order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.search_game_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#search_game_sessions)
        """

    def start_fleet_actions(
        self, **kwargs: Unpack[StartFleetActionsInputRequestTypeDef]
    ) -> StartFleetActionsOutputTypeDef:
        """
        Resumes certain types of activity on fleet instances that were suspended with
        [StopFleetActions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.start_fleet_actions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#start_fleet_actions)
        """

    def start_game_session_placement(
        self, **kwargs: Unpack[StartGameSessionPlacementInputRequestTypeDef]
    ) -> StartGameSessionPlacementOutputTypeDef:
        """
        Places a request for a new game session in a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.start_game_session_placement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#start_game_session_placement)
        """

    def start_match_backfill(
        self, **kwargs: Unpack[StartMatchBackfillInputRequestTypeDef]
    ) -> StartMatchBackfillOutputTypeDef:
        """
        Finds new players to fill open slots in currently running game sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.start_match_backfill)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#start_match_backfill)
        """

    def start_matchmaking(
        self, **kwargs: Unpack[StartMatchmakingInputRequestTypeDef]
    ) -> StartMatchmakingOutputTypeDef:
        """
        Uses FlexMatch to create a game match for a group of players based on custom
        matchmaking
        rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.start_matchmaking)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#start_matchmaking)
        """

    def stop_fleet_actions(
        self, **kwargs: Unpack[StopFleetActionsInputRequestTypeDef]
    ) -> StopFleetActionsOutputTypeDef:
        """
        Suspends certain types of activity in a fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.stop_fleet_actions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#stop_fleet_actions)
        """

    def stop_game_session_placement(
        self, **kwargs: Unpack[StopGameSessionPlacementInputRequestTypeDef]
    ) -> StopGameSessionPlacementOutputTypeDef:
        """
        Cancels a game session placement that is in `PENDING` status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.stop_game_session_placement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#stop_game_session_placement)
        """

    def stop_matchmaking(
        self, **kwargs: Unpack[StopMatchmakingInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels a matchmaking ticket or match backfill ticket that is currently being
        processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.stop_matchmaking)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#stop_matchmaking)
        """

    def suspend_game_server_group(
        self, **kwargs: Unpack[SuspendGameServerGroupInputRequestTypeDef]
    ) -> SuspendGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Temporarily stops activity on a game server group without
        terminating instances or the game server
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.suspend_game_server_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#suspend_game_server_group)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns a tag to an Amazon GameLift resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a tag assigned to a Amazon GameLift resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#untag_resource)
        """

    def update_alias(
        self, **kwargs: Unpack[UpdateAliasInputRequestTypeDef]
    ) -> UpdateAliasOutputTypeDef:
        """
        Updates properties for an alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_alias)
        """

    def update_build(
        self, **kwargs: Unpack[UpdateBuildInputRequestTypeDef]
    ) -> UpdateBuildOutputTypeDef:
        """
        Updates metadata in a build resource, including the build name and version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_build)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_build)
        """

    def update_fleet_attributes(
        self, **kwargs: Unpack[UpdateFleetAttributesInputRequestTypeDef]
    ) -> UpdateFleetAttributesOutputTypeDef:
        """
        Updates a fleet's mutable attributes, such as game session protection and
        resource creation
        limits.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_fleet_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_fleet_attributes)
        """

    def update_fleet_capacity(
        self, **kwargs: Unpack[UpdateFleetCapacityInputRequestTypeDef]
    ) -> UpdateFleetCapacityOutputTypeDef:
        """
        **This operation has been expanded to use with the Amazon GameLift containers
        feature, which is currently in public preview.** Updates capacity settings for
        a managed EC2 fleet or container
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_fleet_capacity)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_fleet_capacity)
        """

    def update_fleet_port_settings(
        self, **kwargs: Unpack[UpdateFleetPortSettingsInputRequestTypeDef]
    ) -> UpdateFleetPortSettingsOutputTypeDef:
        """
        Updates permissions that allow inbound traffic to connect to game sessions in
        the
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_fleet_port_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_fleet_port_settings)
        """

    def update_game_server(
        self, **kwargs: Unpack[UpdateGameServerInputRequestTypeDef]
    ) -> UpdateGameServerOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Updates information about a registered game server to help
        Amazon GameLift FleetIQ track game server
        availability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_game_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_game_server)
        """

    def update_game_server_group(
        self, **kwargs: Unpack[UpdateGameServerGroupInputRequestTypeDef]
    ) -> UpdateGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Updates Amazon GameLift FleetIQ-specific properties for a game
        server
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_game_server_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_game_server_group)
        """

    def update_game_session(
        self, **kwargs: Unpack[UpdateGameSessionInputRequestTypeDef]
    ) -> UpdateGameSessionOutputTypeDef:
        """
        Updates the mutable properties of a game session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_game_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_game_session)
        """

    def update_game_session_queue(
        self, **kwargs: Unpack[UpdateGameSessionQueueInputRequestTypeDef]
    ) -> UpdateGameSessionQueueOutputTypeDef:
        """
        Updates the configuration of a game session queue, which determines how the
        queue processes new game session
        requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_game_session_queue)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_game_session_queue)
        """

    def update_matchmaking_configuration(
        self, **kwargs: Unpack[UpdateMatchmakingConfigurationInputRequestTypeDef]
    ) -> UpdateMatchmakingConfigurationOutputTypeDef:
        """
        Updates settings for a FlexMatch matchmaking configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_matchmaking_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_matchmaking_configuration)
        """

    def update_runtime_configuration(
        self, **kwargs: Unpack[UpdateRuntimeConfigurationInputRequestTypeDef]
    ) -> UpdateRuntimeConfigurationOutputTypeDef:
        """
        Updates the runtime configuration for the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_runtime_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_runtime_configuration)
        """

    def update_script(
        self, **kwargs: Unpack[UpdateScriptInputRequestTypeDef]
    ) -> UpdateScriptOutputTypeDef:
        """
        Updates Realtime script metadata and content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.update_script)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#update_script)
        """

    def validate_matchmaking_rule_set(
        self, **kwargs: Unpack[ValidateMatchmakingRuleSetInputRequestTypeDef]
    ) -> ValidateMatchmakingRuleSetOutputTypeDef:
        """
        Validates the syntax of a matchmaking rule or rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.validate_matchmaking_rule_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#validate_matchmaking_rule_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_attributes"]
    ) -> DescribeFleetAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_capacity"]
    ) -> DescribeFleetCapacityPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_events"]
    ) -> DescribeFleetEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_utilization"]
    ) -> DescribeFleetUtilizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_server_instances"]
    ) -> DescribeGameServerInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_session_details"]
    ) -> DescribeGameSessionDetailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_session_queues"]
    ) -> DescribeGameSessionQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_sessions"]
    ) -> DescribeGameSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> DescribeInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_matchmaking_configurations"]
    ) -> DescribeMatchmakingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_matchmaking_rule_sets"]
    ) -> DescribeMatchmakingRuleSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_player_sessions"]
    ) -> DescribePlayerSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> DescribeScalingPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_builds"]) -> ListBuildsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_compute"]) -> ListComputePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_container_group_definitions"]
    ) -> ListContainerGroupDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_game_server_groups"]
    ) -> ListGameServerGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_game_servers"]
    ) -> ListGameServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_locations"]) -> ListLocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_scripts"]) -> ListScriptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_game_sessions"]
    ) -> SearchGameSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html#GameLift.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client/#get_paginator)
        """
