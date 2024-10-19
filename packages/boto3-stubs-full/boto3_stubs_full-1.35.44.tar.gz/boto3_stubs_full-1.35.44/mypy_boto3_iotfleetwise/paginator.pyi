"""
Type annotations for iotfleetwise service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iotfleetwise.client import IoTFleetWiseClient
    from mypy_boto3_iotfleetwise.paginator import (
        GetVehicleStatusPaginator,
        ListCampaignsPaginator,
        ListDecoderManifestNetworkInterfacesPaginator,
        ListDecoderManifestSignalsPaginator,
        ListDecoderManifestsPaginator,
        ListFleetsPaginator,
        ListFleetsForVehiclePaginator,
        ListModelManifestNodesPaginator,
        ListModelManifestsPaginator,
        ListSignalCatalogNodesPaginator,
        ListSignalCatalogsPaginator,
        ListVehiclesPaginator,
        ListVehiclesInFleetPaginator,
    )

    session = Session()
    client: IoTFleetWiseClient = session.client("iotfleetwise")

    get_vehicle_status_paginator: GetVehicleStatusPaginator = client.get_paginator("get_vehicle_status")
    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    list_decoder_manifest_network_interfaces_paginator: ListDecoderManifestNetworkInterfacesPaginator = client.get_paginator("list_decoder_manifest_network_interfaces")
    list_decoder_manifest_signals_paginator: ListDecoderManifestSignalsPaginator = client.get_paginator("list_decoder_manifest_signals")
    list_decoder_manifests_paginator: ListDecoderManifestsPaginator = client.get_paginator("list_decoder_manifests")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    list_fleets_for_vehicle_paginator: ListFleetsForVehiclePaginator = client.get_paginator("list_fleets_for_vehicle")
    list_model_manifest_nodes_paginator: ListModelManifestNodesPaginator = client.get_paginator("list_model_manifest_nodes")
    list_model_manifests_paginator: ListModelManifestsPaginator = client.get_paginator("list_model_manifests")
    list_signal_catalog_nodes_paginator: ListSignalCatalogNodesPaginator = client.get_paginator("list_signal_catalog_nodes")
    list_signal_catalogs_paginator: ListSignalCatalogsPaginator = client.get_paginator("list_signal_catalogs")
    list_vehicles_paginator: ListVehiclesPaginator = client.get_paginator("list_vehicles")
    list_vehicles_in_fleet_paginator: ListVehiclesInFleetPaginator = client.get_paginator("list_vehicles_in_fleet")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef,
    GetVehicleStatusResponseTypeDef,
    ListCampaignsRequestListCampaignsPaginateTypeDef,
    ListCampaignsResponseTypeDef,
    ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef,
    ListDecoderManifestNetworkInterfacesResponseTypeDef,
    ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef,
    ListDecoderManifestSignalsResponsePaginatorTypeDef,
    ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef,
    ListDecoderManifestsResponseTypeDef,
    ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef,
    ListFleetsForVehicleResponseTypeDef,
    ListFleetsRequestListFleetsPaginateTypeDef,
    ListFleetsResponseTypeDef,
    ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef,
    ListModelManifestNodesResponseTypeDef,
    ListModelManifestsRequestListModelManifestsPaginateTypeDef,
    ListModelManifestsResponseTypeDef,
    ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef,
    ListSignalCatalogNodesResponseTypeDef,
    ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef,
    ListSignalCatalogsResponseTypeDef,
    ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef,
    ListVehiclesInFleetResponseTypeDef,
    ListVehiclesRequestListVehiclesPaginateTypeDef,
    ListVehiclesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetVehicleStatusPaginator",
    "ListCampaignsPaginator",
    "ListDecoderManifestNetworkInterfacesPaginator",
    "ListDecoderManifestSignalsPaginator",
    "ListDecoderManifestsPaginator",
    "ListFleetsPaginator",
    "ListFleetsForVehiclePaginator",
    "ListModelManifestNodesPaginator",
    "ListModelManifestsPaginator",
    "ListSignalCatalogNodesPaginator",
    "ListSignalCatalogsPaginator",
    "ListVehiclesPaginator",
    "ListVehiclesInFleetPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class GetVehicleStatusPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.GetVehicleStatus)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#getvehiclestatuspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef]
    ) -> _PageIterator[GetVehicleStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.GetVehicleStatus.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#getvehiclestatuspaginator)
        """

class ListCampaignsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListCampaigns)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listcampaignspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListCampaignsRequestListCampaignsPaginateTypeDef]
    ) -> _PageIterator[ListCampaignsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListCampaigns.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listcampaignspaginator)
        """

class ListDecoderManifestNetworkInterfacesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestNetworkInterfaces)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listdecodermanifestnetworkinterfacespaginator)
    """
    def paginate(
        self,
        **kwargs: Unpack[
            ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef
        ],
    ) -> _PageIterator[ListDecoderManifestNetworkInterfacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestNetworkInterfaces.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listdecodermanifestnetworkinterfacespaginator)
        """

class ListDecoderManifestSignalsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestSignals)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listdecodermanifestsignalspaginator)
    """
    def paginate(
        self,
        **kwargs: Unpack[
            ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef
        ],
    ) -> _PageIterator[ListDecoderManifestSignalsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifestSignals.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listdecodermanifestsignalspaginator)
        """

class ListDecoderManifestsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifests)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listdecodermanifestspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef]
    ) -> _PageIterator[ListDecoderManifestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListDecoderManifests.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listdecodermanifestspaginator)
        """

class ListFleetsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleets)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listfleetspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListFleetsRequestListFleetsPaginateTypeDef]
    ) -> _PageIterator[ListFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleets.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listfleetspaginator)
        """

class ListFleetsForVehiclePaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleetsForVehicle)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listfleetsforvehiclepaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef]
    ) -> _PageIterator[ListFleetsForVehicleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListFleetsForVehicle.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listfleetsforvehiclepaginator)
        """

class ListModelManifestNodesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifestNodes)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listmodelmanifestnodespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef]
    ) -> _PageIterator[ListModelManifestNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifestNodes.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listmodelmanifestnodespaginator)
        """

class ListModelManifestsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifests)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listmodelmanifestspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListModelManifestsRequestListModelManifestsPaginateTypeDef]
    ) -> _PageIterator[ListModelManifestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListModelManifests.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listmodelmanifestspaginator)
        """

class ListSignalCatalogNodesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogNodes)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listsignalcatalognodespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef]
    ) -> _PageIterator[ListSignalCatalogNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogNodes.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listsignalcatalognodespaginator)
        """

class ListSignalCatalogsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogs)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listsignalcatalogspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef]
    ) -> _PageIterator[ListSignalCatalogsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListSignalCatalogs.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listsignalcatalogspaginator)
        """

class ListVehiclesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehicles)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listvehiclespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListVehiclesRequestListVehiclesPaginateTypeDef]
    ) -> _PageIterator[ListVehiclesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehicles.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listvehiclespaginator)
        """

class ListVehiclesInFleetPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehiclesInFleet)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listvehiclesinfleetpaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef]
    ) -> _PageIterator[ListVehiclesInFleetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Paginator.ListVehiclesInFleet.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/paginators/#listvehiclesinfleetpaginator)
        """
