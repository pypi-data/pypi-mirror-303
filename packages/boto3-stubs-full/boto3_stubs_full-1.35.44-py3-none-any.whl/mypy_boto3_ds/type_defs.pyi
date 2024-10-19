"""
Type annotations for ds service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/type_defs/)

Usage::

    ```python
    from mypy_boto3_ds.type_defs import AcceptSharedDirectoryRequestRequestTypeDef

    data: AcceptSharedDirectoryRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    CertificateStateType,
    CertificateTypeType,
    ClientAuthenticationStatusType,
    ClientAuthenticationTypeType,
    DataAccessStatusType,
    DirectoryConfigurationStatusType,
    DirectoryEditionType,
    DirectorySizeType,
    DirectoryStageType,
    DirectoryTypeType,
    DomainControllerStatusType,
    IpRouteStatusMsgType,
    LDAPSStatusType,
    OSVersionType,
    RadiusAuthenticationProtocolType,
    RadiusStatusType,
    RegionTypeType,
    SchemaExtensionStatusType,
    SelectiveAuthType,
    ShareMethodType,
    ShareStatusType,
    SnapshotStatusType,
    SnapshotTypeType,
    TopicStatusType,
    TrustDirectionType,
    TrustStateType,
    TrustTypeType,
    UpdateStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptSharedDirectoryRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SharedDirectoryTypeDef",
    "IpRouteTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "TagTypeDef",
    "AttributeTypeDef",
    "CancelSchemaExtensionRequestRequestTypeDef",
    "CertificateInfoTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ClientAuthenticationSettingInfoTypeDef",
    "ConditionalForwarderTypeDef",
    "DirectoryConnectSettingsTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "CreateConditionalForwarderRequestRequestTypeDef",
    "CreateLogSubscriptionRequestRequestTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateTrustRequestRequestTypeDef",
    "DeleteConditionalForwarderRequestRequestTypeDef",
    "DeleteDirectoryRequestRequestTypeDef",
    "DeleteLogSubscriptionRequestRequestTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteTrustRequestRequestTypeDef",
    "DeregisterCertificateRequestRequestTypeDef",
    "DeregisterEventTopicRequestRequestTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeClientAuthenticationSettingsRequestRequestTypeDef",
    "DescribeConditionalForwardersRequestRequestTypeDef",
    "DescribeDirectoriesRequestRequestTypeDef",
    "DescribeDirectoryDataAccessRequestRequestTypeDef",
    "DescribeDomainControllersRequestRequestTypeDef",
    "DomainControllerTypeDef",
    "DescribeEventTopicsRequestRequestTypeDef",
    "EventTopicTypeDef",
    "DescribeLDAPSSettingsRequestRequestTypeDef",
    "LDAPSSettingInfoTypeDef",
    "DescribeRegionsRequestRequestTypeDef",
    "DescribeSettingsRequestRequestTypeDef",
    "SettingEntryTypeDef",
    "DescribeSharedDirectoriesRequestRequestTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "SnapshotTypeDef",
    "DescribeTrustsRequestRequestTypeDef",
    "TrustTypeDef",
    "DescribeUpdateDirectoryRequestRequestTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "RadiusSettingsOutputTypeDef",
    "RegionsInfoTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectoryVpcSettingsOutputTypeDef",
    "DisableClientAuthenticationRequestRequestTypeDef",
    "DisableDirectoryDataAccessRequestRequestTypeDef",
    "DisableLDAPSRequestRequestTypeDef",
    "DisableRadiusRequestRequestTypeDef",
    "DisableSsoRequestRequestTypeDef",
    "EnableClientAuthenticationRequestRequestTypeDef",
    "EnableDirectoryDataAccessRequestRequestTypeDef",
    "EnableLDAPSRequestRequestTypeDef",
    "RadiusSettingsTypeDef",
    "EnableSsoRequestRequestTypeDef",
    "GetSnapshotLimitsRequestRequestTypeDef",
    "SnapshotLimitsTypeDef",
    "IpRouteInfoTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListIpRoutesRequestRequestTypeDef",
    "ListLogSubscriptionsRequestRequestTypeDef",
    "LogSubscriptionTypeDef",
    "ListSchemaExtensionsRequestRequestTypeDef",
    "SchemaExtensionInfoTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "OSUpdateSettingsTypeDef",
    "RegisterEventTopicRequestRequestTypeDef",
    "RejectSharedDirectoryRequestRequestTypeDef",
    "RemoveIpRoutesRequestRequestTypeDef",
    "RemoveRegionRequestRequestTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "ResetUserPasswordRequestRequestTypeDef",
    "RestoreFromSnapshotRequestRequestTypeDef",
    "SettingTypeDef",
    "ShareTargetTypeDef",
    "StartSchemaExtensionRequestRequestTypeDef",
    "UnshareTargetTypeDef",
    "UpdateConditionalForwarderRequestRequestTypeDef",
    "UpdateNumberOfDomainControllersRequestRequestTypeDef",
    "UpdateTrustRequestRequestTypeDef",
    "VerifyTrustRequestRequestTypeDef",
    "ConnectDirectoryResultTypeDef",
    "CreateAliasResultTypeDef",
    "CreateDirectoryResultTypeDef",
    "CreateMicrosoftADResultTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateTrustResultTypeDef",
    "DeleteDirectoryResultTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteTrustResultTypeDef",
    "DescribeDirectoryDataAccessResultTypeDef",
    "RegisterCertificateResultTypeDef",
    "RejectSharedDirectoryResultTypeDef",
    "ShareDirectoryResultTypeDef",
    "StartSchemaExtensionResultTypeDef",
    "UnshareDirectoryResultTypeDef",
    "UpdateSettingsResultTypeDef",
    "UpdateTrustResultTypeDef",
    "VerifyTrustResultTypeDef",
    "AcceptSharedDirectoryResultTypeDef",
    "DescribeSharedDirectoriesResultTypeDef",
    "AddIpRoutesRequestRequestTypeDef",
    "AddRegionRequestRequestTypeDef",
    "AddTagsToResourceRequestRequestTypeDef",
    "CreateDirectoryRequestRequestTypeDef",
    "CreateMicrosoftADRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "ComputerTypeDef",
    "CreateComputerRequestRequestTypeDef",
    "ListCertificatesResultTypeDef",
    "CertificateTypeDef",
    "RegisterCertificateRequestRequestTypeDef",
    "DescribeClientAuthenticationSettingsResultTypeDef",
    "DescribeConditionalForwardersResultTypeDef",
    "ConnectDirectoryRequestRequestTypeDef",
    "DescribeClientAuthenticationSettingsRequestDescribeClientAuthenticationSettingsPaginateTypeDef",
    "DescribeDirectoriesRequestDescribeDirectoriesPaginateTypeDef",
    "DescribeDomainControllersRequestDescribeDomainControllersPaginateTypeDef",
    "DescribeLDAPSSettingsRequestDescribeLDAPSSettingsPaginateTypeDef",
    "DescribeRegionsRequestDescribeRegionsPaginateTypeDef",
    "DescribeSharedDirectoriesRequestDescribeSharedDirectoriesPaginateTypeDef",
    "DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef",
    "DescribeTrustsRequestDescribeTrustsPaginateTypeDef",
    "DescribeUpdateDirectoryRequestDescribeUpdateDirectoryPaginateTypeDef",
    "ListCertificatesRequestListCertificatesPaginateTypeDef",
    "ListIpRoutesRequestListIpRoutesPaginateTypeDef",
    "ListLogSubscriptionsRequestListLogSubscriptionsPaginateTypeDef",
    "ListSchemaExtensionsRequestListSchemaExtensionsPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "DescribeDomainControllersResultTypeDef",
    "DescribeEventTopicsResultTypeDef",
    "DescribeLDAPSSettingsResultTypeDef",
    "DescribeSettingsResultTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeTrustsResultTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "GetDirectoryLimitsResultTypeDef",
    "RegionDescriptionTypeDef",
    "EnableRadiusRequestRequestTypeDef",
    "UpdateRadiusRequestRequestTypeDef",
    "GetSnapshotLimitsResultTypeDef",
    "ListIpRoutesResultTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "UpdateDirectorySetupRequestRequestTypeDef",
    "UpdateValueTypeDef",
    "UpdateSettingsRequestRequestTypeDef",
    "ShareDirectoryRequestRequestTypeDef",
    "UnshareDirectoryRequestRequestTypeDef",
    "CreateComputerResultTypeDef",
    "DescribeCertificateResultTypeDef",
    "DirectoryDescriptionTypeDef",
    "DescribeRegionsResultTypeDef",
    "UpdateInfoEntryTypeDef",
    "DescribeDirectoriesResultTypeDef",
    "DescribeUpdateDirectoryResultTypeDef",
)

AcceptSharedDirectoryRequestRequestTypeDef = TypedDict(
    "AcceptSharedDirectoryRequestRequestTypeDef",
    {
        "SharedDirectoryId": str,
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
SharedDirectoryTypeDef = TypedDict(
    "SharedDirectoryTypeDef",
    {
        "OwnerAccountId": NotRequired[str],
        "OwnerDirectoryId": NotRequired[str],
        "ShareMethod": NotRequired[ShareMethodType],
        "SharedAccountId": NotRequired[str],
        "SharedDirectoryId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
        "ShareNotes": NotRequired[str],
        "CreatedDateTime": NotRequired[datetime],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)
IpRouteTypeDef = TypedDict(
    "IpRouteTypeDef",
    {
        "CidrIp": NotRequired[str],
        "Description": NotRequired[str],
    },
)
DirectoryVpcSettingsTypeDef = TypedDict(
    "DirectoryVpcSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": Sequence[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
CancelSchemaExtensionRequestRequestTypeDef = TypedDict(
    "CancelSchemaExtensionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
    },
)
CertificateInfoTypeDef = TypedDict(
    "CertificateInfoTypeDef",
    {
        "CertificateId": NotRequired[str],
        "CommonName": NotRequired[str],
        "State": NotRequired[CertificateStateType],
        "ExpiryDateTime": NotRequired[datetime],
        "Type": NotRequired[CertificateTypeType],
    },
)
ClientCertAuthSettingsTypeDef = TypedDict(
    "ClientCertAuthSettingsTypeDef",
    {
        "OCSPUrl": NotRequired[str],
    },
)
ClientAuthenticationSettingInfoTypeDef = TypedDict(
    "ClientAuthenticationSettingInfoTypeDef",
    {
        "Type": NotRequired[ClientAuthenticationTypeType],
        "Status": NotRequired[ClientAuthenticationStatusType],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)
ConditionalForwarderTypeDef = TypedDict(
    "ConditionalForwarderTypeDef",
    {
        "RemoteDomainName": NotRequired[str],
        "DnsIpAddrs": NotRequired[List[str]],
        "ReplicationScope": NotRequired[Literal["Domain"]],
    },
)
DirectoryConnectSettingsTypeDef = TypedDict(
    "DirectoryConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": Sequence[str],
        "CustomerDnsIps": Sequence[str],
        "CustomerUserName": str,
    },
)
CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
    },
)
CreateConditionalForwarderRequestRequestTypeDef = TypedDict(
    "CreateConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "DnsIpAddrs": Sequence[str],
    },
)
CreateLogSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateLogSubscriptionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "LogGroupName": str,
    },
)
CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Name": NotRequired[str],
    },
)
CreateTrustRequestRequestTypeDef = TypedDict(
    "CreateTrustRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "TrustPassword": str,
        "TrustDirection": TrustDirectionType,
        "TrustType": NotRequired[TrustTypeType],
        "ConditionalForwarderIpAddrs": NotRequired[Sequence[str]],
        "SelectiveAuth": NotRequired[SelectiveAuthType],
    },
)
DeleteConditionalForwarderRequestRequestTypeDef = TypedDict(
    "DeleteConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
    },
)
DeleteDirectoryRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
DeleteLogSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteLogSubscriptionRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
DeleteTrustRequestRequestTypeDef = TypedDict(
    "DeleteTrustRequestRequestTypeDef",
    {
        "TrustId": str,
        "DeleteAssociatedConditionalForwarder": NotRequired[bool],
    },
)
DeregisterCertificateRequestRequestTypeDef = TypedDict(
    "DeregisterCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateId": str,
    },
)
DeregisterEventTopicRequestRequestTypeDef = TypedDict(
    "DeregisterEventTopicRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
    },
)
DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateId": str,
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
DescribeClientAuthenticationSettingsRequestRequestTypeDef = TypedDict(
    "DescribeClientAuthenticationSettingsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[ClientAuthenticationTypeType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeConditionalForwardersRequestRequestTypeDef = TypedDict(
    "DescribeConditionalForwardersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainNames": NotRequired[Sequence[str]],
    },
)
DescribeDirectoriesRequestRequestTypeDef = TypedDict(
    "DescribeDirectoriesRequestRequestTypeDef",
    {
        "DirectoryIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeDirectoryDataAccessRequestRequestTypeDef = TypedDict(
    "DescribeDirectoryDataAccessRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
DescribeDomainControllersRequestRequestTypeDef = TypedDict(
    "DescribeDomainControllersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DomainControllerTypeDef = TypedDict(
    "DomainControllerTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "DomainControllerId": NotRequired[str],
        "DnsIpAddr": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "Status": NotRequired[DomainControllerStatusType],
        "StatusReason": NotRequired[str],
        "LaunchTime": NotRequired[datetime],
        "StatusLastUpdatedDateTime": NotRequired[datetime],
    },
)
DescribeEventTopicsRequestRequestTypeDef = TypedDict(
    "DescribeEventTopicsRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TopicNames": NotRequired[Sequence[str]],
    },
)
EventTopicTypeDef = TypedDict(
    "EventTopicTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TopicName": NotRequired[str],
        "TopicArn": NotRequired[str],
        "CreatedDateTime": NotRequired[datetime],
        "Status": NotRequired[TopicStatusType],
    },
)
DescribeLDAPSSettingsRequestRequestTypeDef = TypedDict(
    "DescribeLDAPSSettingsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[Literal["Client"]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
LDAPSSettingInfoTypeDef = TypedDict(
    "LDAPSSettingInfoTypeDef",
    {
        "LDAPSStatus": NotRequired[LDAPSStatusType],
        "LDAPSStatusReason": NotRequired[str],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)
DescribeRegionsRequestRequestTypeDef = TypedDict(
    "DescribeRegionsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RegionName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
DescribeSettingsRequestRequestTypeDef = TypedDict(
    "DescribeSettingsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Status": NotRequired[DirectoryConfigurationStatusType],
        "NextToken": NotRequired[str],
    },
)
SettingEntryTypeDef = TypedDict(
    "SettingEntryTypeDef",
    {
        "Type": NotRequired[str],
        "Name": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "AppliedValue": NotRequired[str],
        "RequestedValue": NotRequired[str],
        "RequestStatus": NotRequired[DirectoryConfigurationStatusType],
        "RequestDetailedStatus": NotRequired[Dict[str, DirectoryConfigurationStatusType]],
        "RequestStatusMessage": NotRequired[str],
        "LastUpdatedDateTime": NotRequired[datetime],
        "LastRequestedDateTime": NotRequired[datetime],
        "DataType": NotRequired[str],
    },
)
DescribeSharedDirectoriesRequestRequestTypeDef = TypedDict(
    "DescribeSharedDirectoriesRequestRequestTypeDef",
    {
        "OwnerDirectoryId": str,
        "SharedDirectoryIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SnapshotIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Type": NotRequired[SnapshotTypeType],
        "Name": NotRequired[str],
        "Status": NotRequired[SnapshotStatusType],
        "StartTime": NotRequired[datetime],
    },
)
DescribeTrustsRequestRequestTypeDef = TypedDict(
    "DescribeTrustsRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TrustIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
TrustTypeDef = TypedDict(
    "TrustTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TrustId": NotRequired[str],
        "RemoteDomainName": NotRequired[str],
        "TrustType": NotRequired[TrustTypeType],
        "TrustDirection": NotRequired[TrustDirectionType],
        "TrustState": NotRequired[TrustStateType],
        "CreatedDateTime": NotRequired[datetime],
        "LastUpdatedDateTime": NotRequired[datetime],
        "StateLastUpdatedDateTime": NotRequired[datetime],
        "TrustStateReason": NotRequired[str],
        "SelectiveAuth": NotRequired[SelectiveAuthType],
    },
)
DescribeUpdateDirectoryRequestRequestTypeDef = TypedDict(
    "DescribeUpdateDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UpdateType": Literal["OS"],
        "RegionName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
DirectoryConnectSettingsDescriptionTypeDef = TypedDict(
    "DirectoryConnectSettingsDescriptionTypeDef",
    {
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "CustomerUserName": NotRequired[str],
        "SecurityGroupId": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
        "ConnectIps": NotRequired[List[str]],
    },
)
DirectoryVpcSettingsDescriptionTypeDef = TypedDict(
    "DirectoryVpcSettingsDescriptionTypeDef",
    {
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "SecurityGroupId": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
    },
)
RadiusSettingsOutputTypeDef = TypedDict(
    "RadiusSettingsOutputTypeDef",
    {
        "RadiusServers": NotRequired[List[str]],
        "RadiusPort": NotRequired[int],
        "RadiusTimeout": NotRequired[int],
        "RadiusRetries": NotRequired[int],
        "SharedSecret": NotRequired[str],
        "AuthenticationProtocol": NotRequired[RadiusAuthenticationProtocolType],
        "DisplayLabel": NotRequired[str],
        "UseSameUsername": NotRequired[bool],
    },
)
RegionsInfoTypeDef = TypedDict(
    "RegionsInfoTypeDef",
    {
        "PrimaryRegion": NotRequired[str],
        "AdditionalRegions": NotRequired[List[str]],
    },
)
DirectoryLimitsTypeDef = TypedDict(
    "DirectoryLimitsTypeDef",
    {
        "CloudOnlyDirectoriesLimit": NotRequired[int],
        "CloudOnlyDirectoriesCurrentCount": NotRequired[int],
        "CloudOnlyDirectoriesLimitReached": NotRequired[bool],
        "CloudOnlyMicrosoftADLimit": NotRequired[int],
        "CloudOnlyMicrosoftADCurrentCount": NotRequired[int],
        "CloudOnlyMicrosoftADLimitReached": NotRequired[bool],
        "ConnectedDirectoriesLimit": NotRequired[int],
        "ConnectedDirectoriesCurrentCount": NotRequired[int],
        "ConnectedDirectoriesLimitReached": NotRequired[bool],
    },
)
DirectoryVpcSettingsOutputTypeDef = TypedDict(
    "DirectoryVpcSettingsOutputTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
    },
)
DisableClientAuthenticationRequestRequestTypeDef = TypedDict(
    "DisableClientAuthenticationRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": ClientAuthenticationTypeType,
    },
)
DisableDirectoryDataAccessRequestRequestTypeDef = TypedDict(
    "DisableDirectoryDataAccessRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
DisableLDAPSRequestRequestTypeDef = TypedDict(
    "DisableLDAPSRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)
DisableRadiusRequestRequestTypeDef = TypedDict(
    "DisableRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
DisableSsoRequestRequestTypeDef = TypedDict(
    "DisableSsoRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": NotRequired[str],
        "Password": NotRequired[str],
    },
)
EnableClientAuthenticationRequestRequestTypeDef = TypedDict(
    "EnableClientAuthenticationRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": ClientAuthenticationTypeType,
    },
)
EnableDirectoryDataAccessRequestRequestTypeDef = TypedDict(
    "EnableDirectoryDataAccessRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
EnableLDAPSRequestRequestTypeDef = TypedDict(
    "EnableLDAPSRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)
RadiusSettingsTypeDef = TypedDict(
    "RadiusSettingsTypeDef",
    {
        "RadiusServers": NotRequired[Sequence[str]],
        "RadiusPort": NotRequired[int],
        "RadiusTimeout": NotRequired[int],
        "RadiusRetries": NotRequired[int],
        "SharedSecret": NotRequired[str],
        "AuthenticationProtocol": NotRequired[RadiusAuthenticationProtocolType],
        "DisplayLabel": NotRequired[str],
        "UseSameUsername": NotRequired[bool],
    },
)
EnableSsoRequestRequestTypeDef = TypedDict(
    "EnableSsoRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": NotRequired[str],
        "Password": NotRequired[str],
    },
)
GetSnapshotLimitsRequestRequestTypeDef = TypedDict(
    "GetSnapshotLimitsRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
SnapshotLimitsTypeDef = TypedDict(
    "SnapshotLimitsTypeDef",
    {
        "ManualSnapshotsLimit": NotRequired[int],
        "ManualSnapshotsCurrentCount": NotRequired[int],
        "ManualSnapshotsLimitReached": NotRequired[bool],
    },
)
IpRouteInfoTypeDef = TypedDict(
    "IpRouteInfoTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "CidrIp": NotRequired[str],
        "IpRouteStatusMsg": NotRequired[IpRouteStatusMsgType],
        "AddedDateTime": NotRequired[datetime],
        "IpRouteStatusReason": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ListCertificatesRequestRequestTypeDef = TypedDict(
    "ListCertificatesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListIpRoutesRequestRequestTypeDef = TypedDict(
    "ListIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListLogSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListLogSubscriptionsRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
LogSubscriptionTypeDef = TypedDict(
    "LogSubscriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "LogGroupName": NotRequired[str],
        "SubscriptionCreatedDateTime": NotRequired[datetime],
    },
)
ListSchemaExtensionsRequestRequestTypeDef = TypedDict(
    "ListSchemaExtensionsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
SchemaExtensionInfoTypeDef = TypedDict(
    "SchemaExtensionInfoTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SchemaExtensionId": NotRequired[str],
        "Description": NotRequired[str],
        "SchemaExtensionStatus": NotRequired[SchemaExtensionStatusType],
        "SchemaExtensionStatusReason": NotRequired[str],
        "StartDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
OSUpdateSettingsTypeDef = TypedDict(
    "OSUpdateSettingsTypeDef",
    {
        "OSVersion": NotRequired[OSVersionType],
    },
)
RegisterEventTopicRequestRequestTypeDef = TypedDict(
    "RegisterEventTopicRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
    },
)
RejectSharedDirectoryRequestRequestTypeDef = TypedDict(
    "RejectSharedDirectoryRequestRequestTypeDef",
    {
        "SharedDirectoryId": str,
    },
)
RemoveIpRoutesRequestRequestTypeDef = TypedDict(
    "RemoveIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CidrIps": Sequence[str],
    },
)
RemoveRegionRequestRequestTypeDef = TypedDict(
    "RemoveRegionRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)
ResetUserPasswordRequestRequestTypeDef = TypedDict(
    "ResetUserPasswordRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "NewPassword": str,
    },
)
RestoreFromSnapshotRequestRequestTypeDef = TypedDict(
    "RestoreFromSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
SettingTypeDef = TypedDict(
    "SettingTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
ShareTargetTypeDef = TypedDict(
    "ShareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)
StartSchemaExtensionRequestRequestTypeDef = TypedDict(
    "StartSchemaExtensionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CreateSnapshotBeforeSchemaExtension": bool,
        "LdifContent": str,
        "Description": str,
    },
)
UnshareTargetTypeDef = TypedDict(
    "UnshareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)
UpdateConditionalForwarderRequestRequestTypeDef = TypedDict(
    "UpdateConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "DnsIpAddrs": Sequence[str],
    },
)
UpdateNumberOfDomainControllersRequestRequestTypeDef = TypedDict(
    "UpdateNumberOfDomainControllersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "DesiredNumber": int,
    },
)
UpdateTrustRequestRequestTypeDef = TypedDict(
    "UpdateTrustRequestRequestTypeDef",
    {
        "TrustId": str,
        "SelectiveAuth": NotRequired[SelectiveAuthType],
    },
)
VerifyTrustRequestRequestTypeDef = TypedDict(
    "VerifyTrustRequestRequestTypeDef",
    {
        "TrustId": str,
    },
)
ConnectDirectoryResultTypeDef = TypedDict(
    "ConnectDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAliasResultTypeDef = TypedDict(
    "CreateAliasResultTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDirectoryResultTypeDef = TypedDict(
    "CreateDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMicrosoftADResultTypeDef = TypedDict(
    "CreateMicrosoftADResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrustResultTypeDef = TypedDict(
    "CreateTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDirectoryResultTypeDef = TypedDict(
    "DeleteDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTrustResultTypeDef = TypedDict(
    "DeleteTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDirectoryDataAccessResultTypeDef = TypedDict(
    "DescribeDirectoryDataAccessResultTypeDef",
    {
        "DataAccessStatus": DataAccessStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterCertificateResultTypeDef = TypedDict(
    "RegisterCertificateResultTypeDef",
    {
        "CertificateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectSharedDirectoryResultTypeDef = TypedDict(
    "RejectSharedDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ShareDirectoryResultTypeDef = TypedDict(
    "ShareDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSchemaExtensionResultTypeDef = TypedDict(
    "StartSchemaExtensionResultTypeDef",
    {
        "SchemaExtensionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnshareDirectoryResultTypeDef = TypedDict(
    "UnshareDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSettingsResultTypeDef = TypedDict(
    "UpdateSettingsResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrustResultTypeDef = TypedDict(
    "UpdateTrustResultTypeDef",
    {
        "RequestId": str,
        "TrustId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyTrustResultTypeDef = TypedDict(
    "VerifyTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptSharedDirectoryResultTypeDef = TypedDict(
    "AcceptSharedDirectoryResultTypeDef",
    {
        "SharedDirectory": SharedDirectoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSharedDirectoriesResultTypeDef = TypedDict(
    "DescribeSharedDirectoriesResultTypeDef",
    {
        "SharedDirectories": List[SharedDirectoryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AddIpRoutesRequestRequestTypeDef = TypedDict(
    "AddIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "IpRoutes": Sequence[IpRouteTypeDef],
        "UpdateSecurityGroupForDirectoryControllers": NotRequired[bool],
    },
)
AddRegionRequestRequestTypeDef = TypedDict(
    "AddRegionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RegionName": str,
        "VPCSettings": DirectoryVpcSettingsTypeDef,
    },
)
AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateDirectoryRequestRequestTypeDef = TypedDict(
    "CreateDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "Size": DirectorySizeType,
        "ShortName": NotRequired[str],
        "Description": NotRequired[str],
        "VpcSettings": NotRequired[DirectoryVpcSettingsTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateMicrosoftADRequestRequestTypeDef = TypedDict(
    "CreateMicrosoftADRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "VpcSettings": DirectoryVpcSettingsTypeDef,
        "ShortName": NotRequired[str],
        "Description": NotRequired[str],
        "Edition": NotRequired[DirectoryEditionType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ComputerTypeDef = TypedDict(
    "ComputerTypeDef",
    {
        "ComputerId": NotRequired[str],
        "ComputerName": NotRequired[str],
        "ComputerAttributes": NotRequired[List[AttributeTypeDef]],
    },
)
CreateComputerRequestRequestTypeDef = TypedDict(
    "CreateComputerRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "ComputerName": str,
        "Password": str,
        "OrganizationalUnitDistinguishedName": NotRequired[str],
        "ComputerAttributes": NotRequired[Sequence[AttributeTypeDef]],
    },
)
ListCertificatesResultTypeDef = TypedDict(
    "ListCertificatesResultTypeDef",
    {
        "CertificatesInfo": List[CertificateInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateId": NotRequired[str],
        "State": NotRequired[CertificateStateType],
        "StateReason": NotRequired[str],
        "CommonName": NotRequired[str],
        "RegisteredDateTime": NotRequired[datetime],
        "ExpiryDateTime": NotRequired[datetime],
        "Type": NotRequired[CertificateTypeType],
        "ClientCertAuthSettings": NotRequired[ClientCertAuthSettingsTypeDef],
    },
)
RegisterCertificateRequestRequestTypeDef = TypedDict(
    "RegisterCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateData": str,
        "Type": NotRequired[CertificateTypeType],
        "ClientCertAuthSettings": NotRequired[ClientCertAuthSettingsTypeDef],
    },
)
DescribeClientAuthenticationSettingsResultTypeDef = TypedDict(
    "DescribeClientAuthenticationSettingsResultTypeDef",
    {
        "ClientAuthenticationSettingsInfo": List[ClientAuthenticationSettingInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeConditionalForwardersResultTypeDef = TypedDict(
    "DescribeConditionalForwardersResultTypeDef",
    {
        "ConditionalForwarders": List[ConditionalForwarderTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectDirectoryRequestRequestTypeDef = TypedDict(
    "ConnectDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "Size": DirectorySizeType,
        "ConnectSettings": DirectoryConnectSettingsTypeDef,
        "ShortName": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeClientAuthenticationSettingsRequestDescribeClientAuthenticationSettingsPaginateTypeDef = TypedDict(
    "DescribeClientAuthenticationSettingsRequestDescribeClientAuthenticationSettingsPaginateTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[ClientAuthenticationTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDirectoriesRequestDescribeDirectoriesPaginateTypeDef = TypedDict(
    "DescribeDirectoriesRequestDescribeDirectoriesPaginateTypeDef",
    {
        "DirectoryIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDomainControllersRequestDescribeDomainControllersPaginateTypeDef = TypedDict(
    "DescribeDomainControllersRequestDescribeDomainControllersPaginateTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLDAPSSettingsRequestDescribeLDAPSSettingsPaginateTypeDef = TypedDict(
    "DescribeLDAPSSettingsRequestDescribeLDAPSSettingsPaginateTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[Literal["Client"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegionsRequestDescribeRegionsPaginateTypeDef = TypedDict(
    "DescribeRegionsRequestDescribeRegionsPaginateTypeDef",
    {
        "DirectoryId": str,
        "RegionName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSharedDirectoriesRequestDescribeSharedDirectoriesPaginateTypeDef = TypedDict(
    "DescribeSharedDirectoriesRequestDescribeSharedDirectoriesPaginateTypeDef",
    {
        "OwnerDirectoryId": str,
        "SharedDirectoryIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef = TypedDict(
    "DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SnapshotIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTrustsRequestDescribeTrustsPaginateTypeDef = TypedDict(
    "DescribeTrustsRequestDescribeTrustsPaginateTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TrustIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeUpdateDirectoryRequestDescribeUpdateDirectoryPaginateTypeDef = TypedDict(
    "DescribeUpdateDirectoryRequestDescribeUpdateDirectoryPaginateTypeDef",
    {
        "DirectoryId": str,
        "UpdateType": Literal["OS"],
        "RegionName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCertificatesRequestListCertificatesPaginateTypeDef = TypedDict(
    "ListCertificatesRequestListCertificatesPaginateTypeDef",
    {
        "DirectoryId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIpRoutesRequestListIpRoutesPaginateTypeDef = TypedDict(
    "ListIpRoutesRequestListIpRoutesPaginateTypeDef",
    {
        "DirectoryId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLogSubscriptionsRequestListLogSubscriptionsPaginateTypeDef = TypedDict(
    "ListLogSubscriptionsRequestListLogSubscriptionsPaginateTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemaExtensionsRequestListSchemaExtensionsPaginateTypeDef = TypedDict(
    "ListSchemaExtensionsRequestListSchemaExtensionsPaginateTypeDef",
    {
        "DirectoryId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDomainControllersResultTypeDef = TypedDict(
    "DescribeDomainControllersResultTypeDef",
    {
        "DomainControllers": List[DomainControllerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeEventTopicsResultTypeDef = TypedDict(
    "DescribeEventTopicsResultTypeDef",
    {
        "EventTopics": List[EventTopicTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLDAPSSettingsResultTypeDef = TypedDict(
    "DescribeLDAPSSettingsResultTypeDef",
    {
        "LDAPSSettingsInfo": List[LDAPSSettingInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeSettingsResultTypeDef = TypedDict(
    "DescribeSettingsResultTypeDef",
    {
        "DirectoryId": str,
        "SettingEntries": List[SettingEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {
        "Snapshots": List[SnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeTrustsResultTypeDef = TypedDict(
    "DescribeTrustsResultTypeDef",
    {
        "Trusts": List[TrustTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
OwnerDirectoryDescriptionTypeDef = TypedDict(
    "OwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "AccountId": NotRequired[str],
        "DnsIpAddrs": NotRequired[List[str]],
        "VpcSettings": NotRequired[DirectoryVpcSettingsDescriptionTypeDef],
        "RadiusSettings": NotRequired[RadiusSettingsOutputTypeDef],
        "RadiusStatus": NotRequired[RadiusStatusType],
    },
)
GetDirectoryLimitsResultTypeDef = TypedDict(
    "GetDirectoryLimitsResultTypeDef",
    {
        "DirectoryLimits": DirectoryLimitsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegionDescriptionTypeDef = TypedDict(
    "RegionDescriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "RegionName": NotRequired[str],
        "RegionType": NotRequired[RegionTypeType],
        "Status": NotRequired[DirectoryStageType],
        "VpcSettings": NotRequired[DirectoryVpcSettingsOutputTypeDef],
        "DesiredNumberOfDomainControllers": NotRequired[int],
        "LaunchTime": NotRequired[datetime],
        "StatusLastUpdatedDateTime": NotRequired[datetime],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)
EnableRadiusRequestRequestTypeDef = TypedDict(
    "EnableRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RadiusSettings": RadiusSettingsTypeDef,
    },
)
UpdateRadiusRequestRequestTypeDef = TypedDict(
    "UpdateRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RadiusSettings": RadiusSettingsTypeDef,
    },
)
GetSnapshotLimitsResultTypeDef = TypedDict(
    "GetSnapshotLimitsResultTypeDef",
    {
        "SnapshotLimits": SnapshotLimitsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIpRoutesResultTypeDef = TypedDict(
    "ListIpRoutesResultTypeDef",
    {
        "IpRoutesInfo": List[IpRouteInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLogSubscriptionsResultTypeDef = TypedDict(
    "ListLogSubscriptionsResultTypeDef",
    {
        "LogSubscriptions": List[LogSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSchemaExtensionsResultTypeDef = TypedDict(
    "ListSchemaExtensionsResultTypeDef",
    {
        "SchemaExtensionsInfo": List[SchemaExtensionInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateDirectorySetupRequestRequestTypeDef = TypedDict(
    "UpdateDirectorySetupRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UpdateType": Literal["OS"],
        "OSUpdateSettings": NotRequired[OSUpdateSettingsTypeDef],
        "CreateSnapshotBeforeUpdate": NotRequired[bool],
    },
)
UpdateValueTypeDef = TypedDict(
    "UpdateValueTypeDef",
    {
        "OSUpdateSettings": NotRequired[OSUpdateSettingsTypeDef],
    },
)
UpdateSettingsRequestRequestTypeDef = TypedDict(
    "UpdateSettingsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Settings": Sequence[SettingTypeDef],
    },
)
ShareDirectoryRequestRequestTypeDef = TypedDict(
    "ShareDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "ShareTarget": ShareTargetTypeDef,
        "ShareMethod": ShareMethodType,
        "ShareNotes": NotRequired[str],
    },
)
UnshareDirectoryRequestRequestTypeDef = TypedDict(
    "UnshareDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UnshareTarget": UnshareTargetTypeDef,
    },
)
CreateComputerResultTypeDef = TypedDict(
    "CreateComputerResultTypeDef",
    {
        "Computer": ComputerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCertificateResultTypeDef = TypedDict(
    "DescribeCertificateResultTypeDef",
    {
        "Certificate": CertificateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DirectoryDescriptionTypeDef = TypedDict(
    "DirectoryDescriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "Name": NotRequired[str],
        "ShortName": NotRequired[str],
        "Size": NotRequired[DirectorySizeType],
        "Edition": NotRequired[DirectoryEditionType],
        "Alias": NotRequired[str],
        "AccessUrl": NotRequired[str],
        "Description": NotRequired[str],
        "DnsIpAddrs": NotRequired[List[str]],
        "Stage": NotRequired[DirectoryStageType],
        "ShareStatus": NotRequired[ShareStatusType],
        "ShareMethod": NotRequired[ShareMethodType],
        "ShareNotes": NotRequired[str],
        "LaunchTime": NotRequired[datetime],
        "StageLastUpdatedDateTime": NotRequired[datetime],
        "Type": NotRequired[DirectoryTypeType],
        "VpcSettings": NotRequired[DirectoryVpcSettingsDescriptionTypeDef],
        "ConnectSettings": NotRequired[DirectoryConnectSettingsDescriptionTypeDef],
        "RadiusSettings": NotRequired[RadiusSettingsOutputTypeDef],
        "RadiusStatus": NotRequired[RadiusStatusType],
        "StageReason": NotRequired[str],
        "SsoEnabled": NotRequired[bool],
        "DesiredNumberOfDomainControllers": NotRequired[int],
        "OwnerDirectoryDescription": NotRequired[OwnerDirectoryDescriptionTypeDef],
        "RegionsInfo": NotRequired[RegionsInfoTypeDef],
        "OsVersion": NotRequired[OSVersionType],
    },
)
DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {
        "RegionsDescription": List[RegionDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateInfoEntryTypeDef = TypedDict(
    "UpdateInfoEntryTypeDef",
    {
        "Region": NotRequired[str],
        "Status": NotRequired[UpdateStatusType],
        "StatusReason": NotRequired[str],
        "InitiatedBy": NotRequired[str],
        "NewValue": NotRequired[UpdateValueTypeDef],
        "PreviousValue": NotRequired[UpdateValueTypeDef],
        "StartTime": NotRequired[datetime],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)
DescribeDirectoriesResultTypeDef = TypedDict(
    "DescribeDirectoriesResultTypeDef",
    {
        "DirectoryDescriptions": List[DirectoryDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeUpdateDirectoryResultTypeDef = TypedDict(
    "DescribeUpdateDirectoryResultTypeDef",
    {
        "UpdateActivities": List[UpdateInfoEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
