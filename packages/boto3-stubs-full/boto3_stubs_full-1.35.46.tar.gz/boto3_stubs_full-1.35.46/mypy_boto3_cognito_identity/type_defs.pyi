"""
Type annotations for cognito-identity service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/type_defs/)

Usage::

    ```python
    from mypy_boto3_cognito_identity.type_defs import CognitoIdentityProviderTypeDef

    data: CognitoIdentityProviderTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AmbiguousRoleResolutionTypeType,
    ErrorCodeType,
    MappingRuleMatchTypeType,
    RoleMappingTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CognitoIdentityProviderTypeDef",
    "CredentialsTypeDef",
    "DeleteIdentitiesInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UnprocessedIdentityIdTypeDef",
    "DeleteIdentityPoolInputRequestTypeDef",
    "DescribeIdentityInputRequestTypeDef",
    "DescribeIdentityPoolInputRequestTypeDef",
    "GetCredentialsForIdentityInputRequestTypeDef",
    "GetIdInputRequestTypeDef",
    "GetIdentityPoolRolesInputRequestTypeDef",
    "GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    "GetOpenIdTokenInputRequestTypeDef",
    "GetPrincipalTagAttributeMapInputRequestTypeDef",
    "IdentityDescriptionTypeDef",
    "IdentityPoolShortDescriptionTypeDef",
    "ListIdentitiesInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListIdentityPoolsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "LookupDeveloperIdentityInputRequestTypeDef",
    "MappingRuleTypeDef",
    "MergeDeveloperIdentitiesInputRequestTypeDef",
    "SetPrincipalTagAttributeMapInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UnlinkDeveloperIdentityInputRequestTypeDef",
    "UnlinkIdentityInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "CreateIdentityPoolInputRequestTypeDef",
    "IdentityPoolRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCredentialsForIdentityResponseTypeDef",
    "GetIdResponseTypeDef",
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "GetOpenIdTokenResponseTypeDef",
    "GetPrincipalTagAttributeMapResponseTypeDef",
    "IdentityDescriptionResponseTypeDef",
    "IdentityPoolTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LookupDeveloperIdentityResponseTypeDef",
    "MergeDeveloperIdentitiesResponseTypeDef",
    "SetPrincipalTagAttributeMapResponseTypeDef",
    "DeleteIdentitiesResponseTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoolsResponseTypeDef",
    "ListIdentityPoolsInputListIdentityPoolsPaginateTypeDef",
    "RulesConfigurationTypeOutputTypeDef",
    "RulesConfigurationTypeTypeDef",
    "RoleMappingOutputTypeDef",
    "RulesConfigurationTypeUnionTypeDef",
    "GetIdentityPoolRolesResponseTypeDef",
    "RoleMappingTypeDef",
    "RoleMappingUnionTypeDef",
    "SetIdentityPoolRolesInputRequestTypeDef",
)

CognitoIdentityProviderTypeDef = TypedDict(
    "CognitoIdentityProviderTypeDef",
    {
        "ProviderName": NotRequired[str],
        "ClientId": NotRequired[str],
        "ServerSideTokenCheck": NotRequired[bool],
    },
)
CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": NotRequired[str],
        "SecretKey": NotRequired[str],
        "SessionToken": NotRequired[str],
        "Expiration": NotRequired[datetime],
    },
)
DeleteIdentitiesInputRequestTypeDef = TypedDict(
    "DeleteIdentitiesInputRequestTypeDef",
    {
        "IdentityIdsToDelete": Sequence[str],
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
UnprocessedIdentityIdTypeDef = TypedDict(
    "UnprocessedIdentityIdTypeDef",
    {
        "IdentityId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
    },
)
DeleteIdentityPoolInputRequestTypeDef = TypedDict(
    "DeleteIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
DescribeIdentityInputRequestTypeDef = TypedDict(
    "DescribeIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
    },
)
DescribeIdentityPoolInputRequestTypeDef = TypedDict(
    "DescribeIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
GetCredentialsForIdentityInputRequestTypeDef = TypedDict(
    "GetCredentialsForIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "Logins": NotRequired[Mapping[str, str]],
        "CustomRoleArn": NotRequired[str],
    },
)
GetIdInputRequestTypeDef = TypedDict(
    "GetIdInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "AccountId": NotRequired[str],
        "Logins": NotRequired[Mapping[str, str]],
    },
)
GetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "GetIdentityPoolRolesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef = TypedDict(
    "GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Logins": Mapping[str, str],
        "IdentityId": NotRequired[str],
        "PrincipalTags": NotRequired[Mapping[str, str]],
        "TokenDuration": NotRequired[int],
    },
)
GetOpenIdTokenInputRequestTypeDef = TypedDict(
    "GetOpenIdTokenInputRequestTypeDef",
    {
        "IdentityId": str,
        "Logins": NotRequired[Mapping[str, str]],
    },
)
GetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
    },
)
IdentityDescriptionTypeDef = TypedDict(
    "IdentityDescriptionTypeDef",
    {
        "IdentityId": NotRequired[str],
        "Logins": NotRequired[List[str]],
        "CreationDate": NotRequired[datetime],
        "LastModifiedDate": NotRequired[datetime],
    },
)
IdentityPoolShortDescriptionTypeDef = TypedDict(
    "IdentityPoolShortDescriptionTypeDef",
    {
        "IdentityPoolId": NotRequired[str],
        "IdentityPoolName": NotRequired[str],
    },
)
ListIdentitiesInputRequestTypeDef = TypedDict(
    "ListIdentitiesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "MaxResults": int,
        "NextToken": NotRequired[str],
        "HideDisabled": NotRequired[bool],
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
ListIdentityPoolsInputRequestTypeDef = TypedDict(
    "ListIdentityPoolsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
LookupDeveloperIdentityInputRequestTypeDef = TypedDict(
    "LookupDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": NotRequired[str],
        "DeveloperUserIdentifier": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MappingRuleTypeDef = TypedDict(
    "MappingRuleTypeDef",
    {
        "Claim": str,
        "MatchType": MappingRuleMatchTypeType,
        "Value": str,
        "RoleARN": str,
    },
)
MergeDeveloperIdentitiesInputRequestTypeDef = TypedDict(
    "MergeDeveloperIdentitiesInputRequestTypeDef",
    {
        "SourceUserIdentifier": str,
        "DestinationUserIdentifier": str,
        "DeveloperProviderName": str,
        "IdentityPoolId": str,
    },
)
SetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "SetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": NotRequired[bool],
        "PrincipalTags": NotRequired[Mapping[str, str]],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UnlinkDeveloperIdentityInputRequestTypeDef = TypedDict(
    "UnlinkDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "DeveloperProviderName": str,
        "DeveloperUserIdentifier": str,
    },
)
UnlinkIdentityInputRequestTypeDef = TypedDict(
    "UnlinkIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "Logins": Mapping[str, str],
        "LoginsToRemove": Sequence[str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
CreateIdentityPoolInputRequestTypeDef = TypedDict(
    "CreateIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": NotRequired[bool],
        "SupportedLoginProviders": NotRequired[Mapping[str, str]],
        "DeveloperProviderName": NotRequired[str],
        "OpenIdConnectProviderARNs": NotRequired[Sequence[str]],
        "CognitoIdentityProviders": NotRequired[Sequence[CognitoIdentityProviderTypeDef]],
        "SamlProviderARNs": NotRequired[Sequence[str]],
        "IdentityPoolTags": NotRequired[Mapping[str, str]],
    },
)
IdentityPoolRequestTypeDef = TypedDict(
    "IdentityPoolRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": NotRequired[bool],
        "SupportedLoginProviders": NotRequired[Mapping[str, str]],
        "DeveloperProviderName": NotRequired[str],
        "OpenIdConnectProviderARNs": NotRequired[Sequence[str]],
        "CognitoIdentityProviders": NotRequired[Sequence[CognitoIdentityProviderTypeDef]],
        "SamlProviderARNs": NotRequired[Sequence[str]],
        "IdentityPoolTags": NotRequired[Mapping[str, str]],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCredentialsForIdentityResponseTypeDef = TypedDict(
    "GetCredentialsForIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Credentials": CredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdResponseTypeDef = TypedDict(
    "GetIdResponseTypeDef",
    {
        "IdentityId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOpenIdTokenForDeveloperIdentityResponseTypeDef = TypedDict(
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOpenIdTokenResponseTypeDef = TypedDict(
    "GetOpenIdTokenResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IdentityDescriptionResponseTypeDef = TypedDict(
    "IdentityDescriptionResponseTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IdentityPoolTypeDef = TypedDict(
    "IdentityPoolTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[CognitoIdentityProviderTypeDef],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LookupDeveloperIdentityResponseTypeDef = TypedDict(
    "LookupDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifierList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MergeDeveloperIdentitiesResponseTypeDef = TypedDict(
    "MergeDeveloperIdentitiesResponseTypeDef",
    {
        "IdentityId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "SetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIdentitiesResponseTypeDef = TypedDict(
    "DeleteIdentitiesResponseTypeDef",
    {
        "UnprocessedIdentityIds": List[UnprocessedIdentityIdTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdentitiesResponseTypeDef = TypedDict(
    "ListIdentitiesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List[IdentityDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIdentityPoolsResponseTypeDef = TypedDict(
    "ListIdentityPoolsResponseTypeDef",
    {
        "IdentityPools": List[IdentityPoolShortDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIdentityPoolsInputListIdentityPoolsPaginateTypeDef = TypedDict(
    "ListIdentityPoolsInputListIdentityPoolsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
RulesConfigurationTypeOutputTypeDef = TypedDict(
    "RulesConfigurationTypeOutputTypeDef",
    {
        "Rules": List[MappingRuleTypeDef],
    },
)
RulesConfigurationTypeTypeDef = TypedDict(
    "RulesConfigurationTypeTypeDef",
    {
        "Rules": Sequence[MappingRuleTypeDef],
    },
)
RoleMappingOutputTypeDef = TypedDict(
    "RoleMappingOutputTypeDef",
    {
        "Type": RoleMappingTypeType,
        "AmbiguousRoleResolution": NotRequired[AmbiguousRoleResolutionTypeType],
        "RulesConfiguration": NotRequired[RulesConfigurationTypeOutputTypeDef],
    },
)
RulesConfigurationTypeUnionTypeDef = Union[
    RulesConfigurationTypeTypeDef, RulesConfigurationTypeOutputTypeDef
]
GetIdentityPoolRolesResponseTypeDef = TypedDict(
    "GetIdentityPoolRolesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[str, RoleMappingOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RoleMappingTypeDef = TypedDict(
    "RoleMappingTypeDef",
    {
        "Type": RoleMappingTypeType,
        "AmbiguousRoleResolution": NotRequired[AmbiguousRoleResolutionTypeType],
        "RulesConfiguration": NotRequired[RulesConfigurationTypeUnionTypeDef],
    },
)
RoleMappingUnionTypeDef = Union[RoleMappingTypeDef, RoleMappingOutputTypeDef]
SetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "SetIdentityPoolRolesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Mapping[str, str],
        "RoleMappings": NotRequired[Mapping[str, RoleMappingUnionTypeDef]],
    },
)
