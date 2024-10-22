"""
Type annotations for snowball service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snowball/type_defs/)

Usage::

    ```python
    from mypy_boto3_snowball.type_defs import AddressTypeDef

    data: AddressTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AddressTypeType,
    ClusterStateType,
    DeviceServiceNameType,
    ImpactLevelType,
    JobStateType,
    JobTypeType,
    LongTermPricingTypeType,
    RemoteManagementType,
    ServiceNameType,
    ShipmentStateType,
    ShippingLabelStatusType,
    ShippingOptionType,
    SnowballCapacityType,
    SnowballTypeType,
    TransferOptionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AddressTypeDef",
    "CancelClusterRequestRequestTypeDef",
    "CancelJobRequestRequestTypeDef",
    "ClusterListEntryTypeDef",
    "NotificationOutputTypeDef",
    "CompatibleImageTypeDef",
    "ResponseMetadataTypeDef",
    "NotificationTypeDef",
    "JobListEntryTypeDef",
    "CreateLongTermPricingRequestRequestTypeDef",
    "CreateReturnShippingLabelRequestRequestTypeDef",
    "DataTransferTypeDef",
    "ServiceVersionTypeDef",
    "DescribeAddressRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAddressesRequestRequestTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeReturnShippingLabelRequestRequestTypeDef",
    "EKSOnDeviceServiceConfigurationTypeDef",
    "Ec2AmiResourceTypeDef",
    "EventTriggerDefinitionTypeDef",
    "GetJobManifestRequestRequestTypeDef",
    "GetJobUnlockCodeRequestRequestTypeDef",
    "GetSoftwareUpdatesRequestRequestTypeDef",
    "INDTaxDocumentsTypeDef",
    "JobLogsTypeDef",
    "PickupDetailsOutputTypeDef",
    "KeyRangeTypeDef",
    "ListClusterJobsRequestRequestTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListCompatibleImagesRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListLongTermPricingRequestRequestTypeDef",
    "LongTermPricingListEntryTypeDef",
    "ListPickupLocationsRequestRequestTypeDef",
    "NFSOnDeviceServiceConfigurationTypeDef",
    "S3OnDeviceServiceConfigurationTypeDef",
    "TGWOnDeviceServiceConfigurationTypeDef",
    "TimestampTypeDef",
    "TargetOnDeviceServiceTypeDef",
    "ShipmentTypeDef",
    "WirelessConnectionTypeDef",
    "UpdateJobShipmentStateRequestRequestTypeDef",
    "UpdateLongTermPricingRequestRequestTypeDef",
    "CreateAddressRequestRequestTypeDef",
    "CreateAddressResultTypeDef",
    "CreateJobResultTypeDef",
    "CreateLongTermPricingResultTypeDef",
    "CreateReturnShippingLabelResultTypeDef",
    "DescribeAddressResultTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeReturnShippingLabelResultTypeDef",
    "GetJobManifestResultTypeDef",
    "GetJobUnlockCodeResultTypeDef",
    "GetSnowballUsageResultTypeDef",
    "GetSoftwareUpdatesResultTypeDef",
    "ListClustersResultTypeDef",
    "ListCompatibleImagesResultTypeDef",
    "ListPickupLocationsResultTypeDef",
    "CreateClusterResultTypeDef",
    "ListClusterJobsResultTypeDef",
    "ListJobsResultTypeDef",
    "DependentServiceTypeDef",
    "DescribeAddressesRequestDescribeAddressesPaginateTypeDef",
    "ListClusterJobsRequestListClusterJobsPaginateTypeDef",
    "ListClustersRequestListClustersPaginateTypeDef",
    "ListCompatibleImagesRequestListCompatibleImagesPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListLongTermPricingRequestListLongTermPricingPaginateTypeDef",
    "LambdaResourceOutputTypeDef",
    "LambdaResourceTypeDef",
    "TaxDocumentsTypeDef",
    "ListLongTermPricingResultTypeDef",
    "OnDeviceServiceConfigurationTypeDef",
    "PickupDetailsTypeDef",
    "S3ResourceOutputTypeDef",
    "S3ResourceTypeDef",
    "ShippingDetailsTypeDef",
    "SnowconeDeviceConfigurationTypeDef",
    "ListServiceVersionsRequestRequestTypeDef",
    "ListServiceVersionsResultTypeDef",
    "LambdaResourceUnionTypeDef",
    "JobResourceOutputTypeDef",
    "S3ResourceUnionTypeDef",
    "DeviceConfigurationTypeDef",
    "ClusterMetadataTypeDef",
    "JobResourceTypeDef",
    "JobMetadataTypeDef",
    "DescribeClusterResultTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateJobRequestRequestTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "DescribeJobResultTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressId": NotRequired[str],
        "Name": NotRequired[str],
        "Company": NotRequired[str],
        "Street1": NotRequired[str],
        "Street2": NotRequired[str],
        "Street3": NotRequired[str],
        "City": NotRequired[str],
        "StateOrProvince": NotRequired[str],
        "PrefectureOrDistrict": NotRequired[str],
        "Landmark": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "IsRestricted": NotRequired[bool],
        "Type": NotRequired[AddressTypeType],
    },
)
CancelClusterRequestRequestTypeDef = TypedDict(
    "CancelClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
ClusterListEntryTypeDef = TypedDict(
    "ClusterListEntryTypeDef",
    {
        "ClusterId": NotRequired[str],
        "ClusterState": NotRequired[ClusterStateType],
        "CreationDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)
NotificationOutputTypeDef = TypedDict(
    "NotificationOutputTypeDef",
    {
        "SnsTopicARN": NotRequired[str],
        "JobStatesToNotify": NotRequired[List[JobStateType]],
        "NotifyAll": NotRequired[bool],
        "DevicePickupSnsTopicARN": NotRequired[str],
    },
)
CompatibleImageTypeDef = TypedDict(
    "CompatibleImageTypeDef",
    {
        "AmiId": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
        "HostId": NotRequired[str],
    },
)
NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "SnsTopicARN": NotRequired[str],
        "JobStatesToNotify": NotRequired[Sequence[JobStateType]],
        "NotifyAll": NotRequired[bool],
        "DevicePickupSnsTopicARN": NotRequired[str],
    },
)
JobListEntryTypeDef = TypedDict(
    "JobListEntryTypeDef",
    {
        "JobId": NotRequired[str],
        "JobState": NotRequired[JobStateType],
        "IsMaster": NotRequired[bool],
        "JobType": NotRequired[JobTypeType],
        "SnowballType": NotRequired[SnowballTypeType],
        "CreationDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)
CreateLongTermPricingRequestRequestTypeDef = TypedDict(
    "CreateLongTermPricingRequestRequestTypeDef",
    {
        "LongTermPricingType": LongTermPricingTypeType,
        "SnowballType": SnowballTypeType,
        "IsLongTermPricingAutoRenew": NotRequired[bool],
    },
)
CreateReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "CreateReturnShippingLabelRequestRequestTypeDef",
    {
        "JobId": str,
        "ShippingOption": NotRequired[ShippingOptionType],
    },
)
DataTransferTypeDef = TypedDict(
    "DataTransferTypeDef",
    {
        "BytesTransferred": NotRequired[int],
        "ObjectsTransferred": NotRequired[int],
        "TotalBytes": NotRequired[int],
        "TotalObjects": NotRequired[int],
    },
)
ServiceVersionTypeDef = TypedDict(
    "ServiceVersionTypeDef",
    {
        "Version": NotRequired[str],
    },
)
DescribeAddressRequestRequestTypeDef = TypedDict(
    "DescribeAddressRequestRequestTypeDef",
    {
        "AddressId": str,
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
DescribeAddressesRequestRequestTypeDef = TypedDict(
    "DescribeAddressesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "DescribeReturnShippingLabelRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
EKSOnDeviceServiceConfigurationTypeDef = TypedDict(
    "EKSOnDeviceServiceConfigurationTypeDef",
    {
        "KubernetesVersion": NotRequired[str],
        "EKSAnywhereVersion": NotRequired[str],
    },
)
Ec2AmiResourceTypeDef = TypedDict(
    "Ec2AmiResourceTypeDef",
    {
        "AmiId": str,
        "SnowballAmiId": NotRequired[str],
    },
)
EventTriggerDefinitionTypeDef = TypedDict(
    "EventTriggerDefinitionTypeDef",
    {
        "EventResourceARN": NotRequired[str],
    },
)
GetJobManifestRequestRequestTypeDef = TypedDict(
    "GetJobManifestRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
GetJobUnlockCodeRequestRequestTypeDef = TypedDict(
    "GetJobUnlockCodeRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
GetSoftwareUpdatesRequestRequestTypeDef = TypedDict(
    "GetSoftwareUpdatesRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
INDTaxDocumentsTypeDef = TypedDict(
    "INDTaxDocumentsTypeDef",
    {
        "GSTIN": NotRequired[str],
    },
)
JobLogsTypeDef = TypedDict(
    "JobLogsTypeDef",
    {
        "JobCompletionReportURI": NotRequired[str],
        "JobSuccessLogURI": NotRequired[str],
        "JobFailureLogURI": NotRequired[str],
    },
)
PickupDetailsOutputTypeDef = TypedDict(
    "PickupDetailsOutputTypeDef",
    {
        "Name": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Email": NotRequired[str],
        "IdentificationNumber": NotRequired[str],
        "IdentificationExpirationDate": NotRequired[datetime],
        "IdentificationIssuingOrg": NotRequired[str],
        "DevicePickupId": NotRequired[str],
    },
)
KeyRangeTypeDef = TypedDict(
    "KeyRangeTypeDef",
    {
        "BeginMarker": NotRequired[str],
        "EndMarker": NotRequired[str],
    },
)
ListClusterJobsRequestRequestTypeDef = TypedDict(
    "ListClusterJobsRequestRequestTypeDef",
    {
        "ClusterId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListCompatibleImagesRequestRequestTypeDef = TypedDict(
    "ListCompatibleImagesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLongTermPricingRequestRequestTypeDef = TypedDict(
    "ListLongTermPricingRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
LongTermPricingListEntryTypeDef = TypedDict(
    "LongTermPricingListEntryTypeDef",
    {
        "LongTermPricingId": NotRequired[str],
        "LongTermPricingEndDate": NotRequired[datetime],
        "LongTermPricingStartDate": NotRequired[datetime],
        "LongTermPricingType": NotRequired[LongTermPricingTypeType],
        "CurrentActiveJob": NotRequired[str],
        "ReplacementJob": NotRequired[str],
        "IsLongTermPricingAutoRenew": NotRequired[bool],
        "LongTermPricingStatus": NotRequired[str],
        "SnowballType": NotRequired[SnowballTypeType],
        "JobIds": NotRequired[List[str]],
    },
)
ListPickupLocationsRequestRequestTypeDef = TypedDict(
    "ListPickupLocationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NFSOnDeviceServiceConfigurationTypeDef = TypedDict(
    "NFSOnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": NotRequired[int],
        "StorageUnit": NotRequired[Literal["TB"]],
    },
)
S3OnDeviceServiceConfigurationTypeDef = TypedDict(
    "S3OnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": NotRequired[float],
        "StorageUnit": NotRequired[Literal["TB"]],
        "ServiceSize": NotRequired[int],
        "FaultTolerance": NotRequired[int],
    },
)
TGWOnDeviceServiceConfigurationTypeDef = TypedDict(
    "TGWOnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": NotRequired[int],
        "StorageUnit": NotRequired[Literal["TB"]],
    },
)
TimestampTypeDef = Union[datetime, str]
TargetOnDeviceServiceTypeDef = TypedDict(
    "TargetOnDeviceServiceTypeDef",
    {
        "ServiceName": NotRequired[DeviceServiceNameType],
        "TransferOption": NotRequired[TransferOptionType],
    },
)
ShipmentTypeDef = TypedDict(
    "ShipmentTypeDef",
    {
        "Status": NotRequired[str],
        "TrackingNumber": NotRequired[str],
    },
)
WirelessConnectionTypeDef = TypedDict(
    "WirelessConnectionTypeDef",
    {
        "IsWifiEnabled": NotRequired[bool],
    },
)
UpdateJobShipmentStateRequestRequestTypeDef = TypedDict(
    "UpdateJobShipmentStateRequestRequestTypeDef",
    {
        "JobId": str,
        "ShipmentState": ShipmentStateType,
    },
)
UpdateLongTermPricingRequestRequestTypeDef = TypedDict(
    "UpdateLongTermPricingRequestRequestTypeDef",
    {
        "LongTermPricingId": str,
        "ReplacementJob": NotRequired[str],
        "IsLongTermPricingAutoRenew": NotRequired[bool],
    },
)
CreateAddressRequestRequestTypeDef = TypedDict(
    "CreateAddressRequestRequestTypeDef",
    {
        "Address": AddressTypeDef,
    },
)
CreateAddressResultTypeDef = TypedDict(
    "CreateAddressResultTypeDef",
    {
        "AddressId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLongTermPricingResultTypeDef = TypedDict(
    "CreateLongTermPricingResultTypeDef",
    {
        "LongTermPricingId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReturnShippingLabelResultTypeDef = TypedDict(
    "CreateReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddressResultTypeDef = TypedDict(
    "DescribeAddressResultTypeDef",
    {
        "Address": AddressTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {
        "Addresses": List[AddressTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeReturnShippingLabelResultTypeDef = TypedDict(
    "DescribeReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ExpirationDate": datetime,
        "ReturnShippingLabelURI": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobManifestResultTypeDef = TypedDict(
    "GetJobManifestResultTypeDef",
    {
        "ManifestURI": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobUnlockCodeResultTypeDef = TypedDict(
    "GetJobUnlockCodeResultTypeDef",
    {
        "UnlockCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSnowballUsageResultTypeDef = TypedDict(
    "GetSnowballUsageResultTypeDef",
    {
        "SnowballLimit": int,
        "SnowballsInUse": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSoftwareUpdatesResultTypeDef = TypedDict(
    "GetSoftwareUpdatesResultTypeDef",
    {
        "UpdatesURI": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClustersResultTypeDef = TypedDict(
    "ListClustersResultTypeDef",
    {
        "ClusterListEntries": List[ClusterListEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCompatibleImagesResultTypeDef = TypedDict(
    "ListCompatibleImagesResultTypeDef",
    {
        "CompatibleImages": List[CompatibleImageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPickupLocationsResultTypeDef = TypedDict(
    "ListPickupLocationsResultTypeDef",
    {
        "Addresses": List[AddressTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef",
    {
        "ClusterId": str,
        "JobListEntries": List[JobListEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClusterJobsResultTypeDef = TypedDict(
    "ListClusterJobsResultTypeDef",
    {
        "JobListEntries": List[JobListEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "JobListEntries": List[JobListEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DependentServiceTypeDef = TypedDict(
    "DependentServiceTypeDef",
    {
        "ServiceName": NotRequired[ServiceNameType],
        "ServiceVersion": NotRequired[ServiceVersionTypeDef],
    },
)
DescribeAddressesRequestDescribeAddressesPaginateTypeDef = TypedDict(
    "DescribeAddressesRequestDescribeAddressesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClusterJobsRequestListClusterJobsPaginateTypeDef = TypedDict(
    "ListClusterJobsRequestListClusterJobsPaginateTypeDef",
    {
        "ClusterId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClustersRequestListClustersPaginateTypeDef = TypedDict(
    "ListClustersRequestListClustersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCompatibleImagesRequestListCompatibleImagesPaginateTypeDef = TypedDict(
    "ListCompatibleImagesRequestListCompatibleImagesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLongTermPricingRequestListLongTermPricingPaginateTypeDef = TypedDict(
    "ListLongTermPricingRequestListLongTermPricingPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LambdaResourceOutputTypeDef = TypedDict(
    "LambdaResourceOutputTypeDef",
    {
        "LambdaArn": NotRequired[str],
        "EventTriggers": NotRequired[List[EventTriggerDefinitionTypeDef]],
    },
)
LambdaResourceTypeDef = TypedDict(
    "LambdaResourceTypeDef",
    {
        "LambdaArn": NotRequired[str],
        "EventTriggers": NotRequired[Sequence[EventTriggerDefinitionTypeDef]],
    },
)
TaxDocumentsTypeDef = TypedDict(
    "TaxDocumentsTypeDef",
    {
        "IND": NotRequired[INDTaxDocumentsTypeDef],
    },
)
ListLongTermPricingResultTypeDef = TypedDict(
    "ListLongTermPricingResultTypeDef",
    {
        "LongTermPricingEntries": List[LongTermPricingListEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
OnDeviceServiceConfigurationTypeDef = TypedDict(
    "OnDeviceServiceConfigurationTypeDef",
    {
        "NFSOnDeviceService": NotRequired[NFSOnDeviceServiceConfigurationTypeDef],
        "TGWOnDeviceService": NotRequired[TGWOnDeviceServiceConfigurationTypeDef],
        "EKSOnDeviceService": NotRequired[EKSOnDeviceServiceConfigurationTypeDef],
        "S3OnDeviceService": NotRequired[S3OnDeviceServiceConfigurationTypeDef],
    },
)
PickupDetailsTypeDef = TypedDict(
    "PickupDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Email": NotRequired[str],
        "IdentificationNumber": NotRequired[str],
        "IdentificationExpirationDate": NotRequired[TimestampTypeDef],
        "IdentificationIssuingOrg": NotRequired[str],
        "DevicePickupId": NotRequired[str],
    },
)
S3ResourceOutputTypeDef = TypedDict(
    "S3ResourceOutputTypeDef",
    {
        "BucketArn": NotRequired[str],
        "KeyRange": NotRequired[KeyRangeTypeDef],
        "TargetOnDeviceServices": NotRequired[List[TargetOnDeviceServiceTypeDef]],
    },
)
S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef",
    {
        "BucketArn": NotRequired[str],
        "KeyRange": NotRequired[KeyRangeTypeDef],
        "TargetOnDeviceServices": NotRequired[Sequence[TargetOnDeviceServiceTypeDef]],
    },
)
ShippingDetailsTypeDef = TypedDict(
    "ShippingDetailsTypeDef",
    {
        "ShippingOption": NotRequired[ShippingOptionType],
        "InboundShipment": NotRequired[ShipmentTypeDef],
        "OutboundShipment": NotRequired[ShipmentTypeDef],
    },
)
SnowconeDeviceConfigurationTypeDef = TypedDict(
    "SnowconeDeviceConfigurationTypeDef",
    {
        "WirelessConnection": NotRequired[WirelessConnectionTypeDef],
    },
)
ListServiceVersionsRequestRequestTypeDef = TypedDict(
    "ListServiceVersionsRequestRequestTypeDef",
    {
        "ServiceName": ServiceNameType,
        "DependentServices": NotRequired[Sequence[DependentServiceTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListServiceVersionsResultTypeDef = TypedDict(
    "ListServiceVersionsResultTypeDef",
    {
        "ServiceVersions": List[ServiceVersionTypeDef],
        "ServiceName": ServiceNameType,
        "DependentServices": List[DependentServiceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LambdaResourceUnionTypeDef = Union[LambdaResourceTypeDef, LambdaResourceOutputTypeDef]
JobResourceOutputTypeDef = TypedDict(
    "JobResourceOutputTypeDef",
    {
        "S3Resources": NotRequired[List[S3ResourceOutputTypeDef]],
        "LambdaResources": NotRequired[List[LambdaResourceOutputTypeDef]],
        "Ec2AmiResources": NotRequired[List[Ec2AmiResourceTypeDef]],
    },
)
S3ResourceUnionTypeDef = Union[S3ResourceTypeDef, S3ResourceOutputTypeDef]
DeviceConfigurationTypeDef = TypedDict(
    "DeviceConfigurationTypeDef",
    {
        "SnowconeDeviceConfiguration": NotRequired[SnowconeDeviceConfigurationTypeDef],
    },
)
ClusterMetadataTypeDef = TypedDict(
    "ClusterMetadataTypeDef",
    {
        "ClusterId": NotRequired[str],
        "Description": NotRequired[str],
        "KmsKeyARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "ClusterState": NotRequired[ClusterStateType],
        "JobType": NotRequired[JobTypeType],
        "SnowballType": NotRequired[SnowballTypeType],
        "CreationDate": NotRequired[datetime],
        "Resources": NotRequired[JobResourceOutputTypeDef],
        "AddressId": NotRequired[str],
        "ShippingOption": NotRequired[ShippingOptionType],
        "Notification": NotRequired[NotificationOutputTypeDef],
        "ForwardingAddressId": NotRequired[str],
        "TaxDocuments": NotRequired[TaxDocumentsTypeDef],
        "OnDeviceServiceConfiguration": NotRequired[OnDeviceServiceConfigurationTypeDef],
    },
)
JobResourceTypeDef = TypedDict(
    "JobResourceTypeDef",
    {
        "S3Resources": NotRequired[Sequence[S3ResourceUnionTypeDef]],
        "LambdaResources": NotRequired[Sequence[LambdaResourceUnionTypeDef]],
        "Ec2AmiResources": NotRequired[Sequence[Ec2AmiResourceTypeDef]],
    },
)
JobMetadataTypeDef = TypedDict(
    "JobMetadataTypeDef",
    {
        "JobId": NotRequired[str],
        "JobState": NotRequired[JobStateType],
        "JobType": NotRequired[JobTypeType],
        "SnowballType": NotRequired[SnowballTypeType],
        "CreationDate": NotRequired[datetime],
        "Resources": NotRequired[JobResourceOutputTypeDef],
        "Description": NotRequired[str],
        "KmsKeyARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "AddressId": NotRequired[str],
        "ShippingDetails": NotRequired[ShippingDetailsTypeDef],
        "SnowballCapacityPreference": NotRequired[SnowballCapacityType],
        "Notification": NotRequired[NotificationOutputTypeDef],
        "DataTransferProgress": NotRequired[DataTransferTypeDef],
        "JobLogInfo": NotRequired[JobLogsTypeDef],
        "ClusterId": NotRequired[str],
        "ForwardingAddressId": NotRequired[str],
        "TaxDocuments": NotRequired[TaxDocumentsTypeDef],
        "DeviceConfiguration": NotRequired[DeviceConfigurationTypeDef],
        "RemoteManagement": NotRequired[RemoteManagementType],
        "LongTermPricingId": NotRequired[str],
        "OnDeviceServiceConfiguration": NotRequired[OnDeviceServiceConfigurationTypeDef],
        "ImpactLevel": NotRequired[ImpactLevelType],
        "PickupDetails": NotRequired[PickupDetailsOutputTypeDef],
        "SnowballId": NotRequired[str],
    },
)
DescribeClusterResultTypeDef = TypedDict(
    "DescribeClusterResultTypeDef",
    {
        "ClusterMetadata": ClusterMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "JobType": JobTypeType,
        "AddressId": str,
        "SnowballType": SnowballTypeType,
        "ShippingOption": ShippingOptionType,
        "Resources": NotRequired[JobResourceTypeDef],
        "OnDeviceServiceConfiguration": NotRequired[OnDeviceServiceConfigurationTypeDef],
        "Description": NotRequired[str],
        "KmsKeyARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "Notification": NotRequired[NotificationTypeDef],
        "ForwardingAddressId": NotRequired[str],
        "TaxDocuments": NotRequired[TaxDocumentsTypeDef],
        "RemoteManagement": NotRequired[RemoteManagementType],
        "InitialClusterSize": NotRequired[int],
        "ForceCreateJobs": NotRequired[bool],
        "LongTermPricingIds": NotRequired[Sequence[str]],
        "SnowballCapacityPreference": NotRequired[SnowballCapacityType],
    },
)
CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "JobType": NotRequired[JobTypeType],
        "Resources": NotRequired[JobResourceTypeDef],
        "OnDeviceServiceConfiguration": NotRequired[OnDeviceServiceConfigurationTypeDef],
        "Description": NotRequired[str],
        "AddressId": NotRequired[str],
        "KmsKeyARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "SnowballCapacityPreference": NotRequired[SnowballCapacityType],
        "ShippingOption": NotRequired[ShippingOptionType],
        "Notification": NotRequired[NotificationTypeDef],
        "ClusterId": NotRequired[str],
        "SnowballType": NotRequired[SnowballTypeType],
        "ForwardingAddressId": NotRequired[str],
        "TaxDocuments": NotRequired[TaxDocumentsTypeDef],
        "DeviceConfiguration": NotRequired[DeviceConfigurationTypeDef],
        "RemoteManagement": NotRequired[RemoteManagementType],
        "LongTermPricingId": NotRequired[str],
        "ImpactLevel": NotRequired[ImpactLevelType],
        "PickupDetails": NotRequired[PickupDetailsTypeDef],
    },
)
UpdateClusterRequestRequestTypeDef = TypedDict(
    "UpdateClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
        "RoleARN": NotRequired[str],
        "Description": NotRequired[str],
        "Resources": NotRequired[JobResourceTypeDef],
        "OnDeviceServiceConfiguration": NotRequired[OnDeviceServiceConfigurationTypeDef],
        "AddressId": NotRequired[str],
        "ShippingOption": NotRequired[ShippingOptionType],
        "Notification": NotRequired[NotificationTypeDef],
        "ForwardingAddressId": NotRequired[str],
    },
)
UpdateJobRequestRequestTypeDef = TypedDict(
    "UpdateJobRequestRequestTypeDef",
    {
        "JobId": str,
        "RoleARN": NotRequired[str],
        "Notification": NotRequired[NotificationTypeDef],
        "Resources": NotRequired[JobResourceTypeDef],
        "OnDeviceServiceConfiguration": NotRequired[OnDeviceServiceConfigurationTypeDef],
        "AddressId": NotRequired[str],
        "ShippingOption": NotRequired[ShippingOptionType],
        "Description": NotRequired[str],
        "SnowballCapacityPreference": NotRequired[SnowballCapacityType],
        "ForwardingAddressId": NotRequired[str],
        "PickupDetails": NotRequired[PickupDetailsTypeDef],
    },
)
DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "JobMetadata": JobMetadataTypeDef,
        "SubJobMetadata": List[JobMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
