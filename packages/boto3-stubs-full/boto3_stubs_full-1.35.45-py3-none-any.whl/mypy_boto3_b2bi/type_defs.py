"""
Type annotations for b2bi service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/type_defs/)

Usage::

    ```python
    from mypy_boto3_b2bi.type_defs import CapabilitySummaryTypeDef

    data: CapabilitySummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    CapabilityDirectionType,
    ConversionSourceFormatType,
    FileFormatType,
    LoggingType,
    MappingTemplateLanguageType,
    MappingTypeType,
    TransformerJobStatusType,
    TransformerStatusType,
    X12TransactionSetType,
    X12VersionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "CapabilitySummaryTypeDef",
    "InputFileSourceTypeDef",
    "X12DetailsTypeDef",
    "S3LocationTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "MappingTypeDef",
    "DeleteCapabilityRequestRequestTypeDef",
    "DeletePartnershipRequestRequestTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteTransformerRequestRequestTypeDef",
    "GetCapabilityRequestRequestTypeDef",
    "GetPartnershipRequestRequestTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetTransformerJobRequestRequestTypeDef",
    "GetTransformerRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListCapabilitiesRequestRequestTypeDef",
    "ListPartnershipsRequestRequestTypeDef",
    "ListProfilesRequestRequestTypeDef",
    "ProfileSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTransformersRequestRequestTypeDef",
    "SampleDocumentKeysTypeDef",
    "TestMappingRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "X12DelimitersTypeDef",
    "X12FunctionalGroupHeadersTypeDef",
    "X12InterchangeControlHeadersTypeDef",
    "ConversionSourceTypeDef",
    "ConversionTargetFormatDetailsTypeDef",
    "EdiTypeTypeDef",
    "FormatOptionsTypeDef",
    "TemplateDetailsTypeDef",
    "OutputSampleFileSourceTypeDef",
    "StartTransformerJobRequestRequestTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateStarterMappingTemplateResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetProfileResponseTypeDef",
    "GetTransformerJobResponseTypeDef",
    "ListCapabilitiesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartTransformerJobResponseTypeDef",
    "TestConversionResponseTypeDef",
    "TestMappingResponseTypeDef",
    "TestParsingResponseTypeDef",
    "UpdateProfileResponseTypeDef",
    "ListCapabilitiesRequestListCapabilitiesPaginateTypeDef",
    "ListPartnershipsRequestListPartnershipsPaginateTypeDef",
    "ListProfilesRequestListProfilesPaginateTypeDef",
    "ListTransformersRequestListTransformersPaginateTypeDef",
    "ListProfilesResponseTypeDef",
    "SampleDocumentsOutputTypeDef",
    "SampleDocumentsTypeDef",
    "X12OutboundEdiHeadersTypeDef",
    "EdiConfigurationTypeDef",
    "TestParsingRequestRequestTypeDef",
    "InputConversionTypeDef",
    "OutputConversionTypeDef",
    "CreateStarterMappingTemplateRequestRequestTypeDef",
    "ConversionTargetTypeDef",
    "X12EnvelopeTypeDef",
    "CapabilityConfigurationTypeDef",
    "CreateTransformerRequestRequestTypeDef",
    "CreateTransformerResponseTypeDef",
    "GetTransformerResponseTypeDef",
    "TransformerSummaryTypeDef",
    "UpdateTransformerRequestRequestTypeDef",
    "UpdateTransformerResponseTypeDef",
    "TestConversionRequestRequestTypeDef",
    "OutboundEdiOptionsTypeDef",
    "CreateCapabilityRequestRequestTypeDef",
    "CreateCapabilityResponseTypeDef",
    "GetCapabilityResponseTypeDef",
    "UpdateCapabilityRequestRequestTypeDef",
    "UpdateCapabilityResponseTypeDef",
    "ListTransformersResponseTypeDef",
    "CapabilityOptionsTypeDef",
    "CreatePartnershipRequestRequestTypeDef",
    "CreatePartnershipResponseTypeDef",
    "GetPartnershipResponseTypeDef",
    "PartnershipSummaryTypeDef",
    "UpdatePartnershipRequestRequestTypeDef",
    "UpdatePartnershipResponseTypeDef",
    "ListPartnershipsResponseTypeDef",
)

CapabilitySummaryTypeDef = TypedDict(
    "CapabilitySummaryTypeDef",
    {
        "capabilityId": str,
        "name": str,
        "type": Literal["edi"],
        "createdAt": datetime,
        "modifiedAt": NotRequired[datetime],
    },
)
InputFileSourceTypeDef = TypedDict(
    "InputFileSourceTypeDef",
    {
        "fileContent": NotRequired[str],
    },
)
X12DetailsTypeDef = TypedDict(
    "X12DetailsTypeDef",
    {
        "transactionSet": NotRequired[X12TransactionSetType],
        "version": NotRequired[X12VersionType],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketName": NotRequired[str],
        "key": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
MappingTypeDef = TypedDict(
    "MappingTypeDef",
    {
        "templateLanguage": MappingTemplateLanguageType,
        "template": NotRequired[str],
    },
)
DeleteCapabilityRequestRequestTypeDef = TypedDict(
    "DeleteCapabilityRequestRequestTypeDef",
    {
        "capabilityId": str,
    },
)
DeletePartnershipRequestRequestTypeDef = TypedDict(
    "DeletePartnershipRequestRequestTypeDef",
    {
        "partnershipId": str,
    },
)
DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)
DeleteTransformerRequestRequestTypeDef = TypedDict(
    "DeleteTransformerRequestRequestTypeDef",
    {
        "transformerId": str,
    },
)
GetCapabilityRequestRequestTypeDef = TypedDict(
    "GetCapabilityRequestRequestTypeDef",
    {
        "capabilityId": str,
    },
)
GetPartnershipRequestRequestTypeDef = TypedDict(
    "GetPartnershipRequestRequestTypeDef",
    {
        "partnershipId": str,
    },
)
GetProfileRequestRequestTypeDef = TypedDict(
    "GetProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)
GetTransformerJobRequestRequestTypeDef = TypedDict(
    "GetTransformerJobRequestRequestTypeDef",
    {
        "transformerJobId": str,
        "transformerId": str,
    },
)
GetTransformerRequestRequestTypeDef = TypedDict(
    "GetTransformerRequestRequestTypeDef",
    {
        "transformerId": str,
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
ListCapabilitiesRequestRequestTypeDef = TypedDict(
    "ListCapabilitiesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListPartnershipsRequestRequestTypeDef = TypedDict(
    "ListPartnershipsRequestRequestTypeDef",
    {
        "profileId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListProfilesRequestRequestTypeDef = TypedDict(
    "ListProfilesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ProfileSummaryTypeDef = TypedDict(
    "ProfileSummaryTypeDef",
    {
        "profileId": str,
        "name": str,
        "businessName": str,
        "createdAt": datetime,
        "logging": NotRequired[LoggingType],
        "logGroupName": NotRequired[str],
        "modifiedAt": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
ListTransformersRequestRequestTypeDef = TypedDict(
    "ListTransformersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SampleDocumentKeysTypeDef = TypedDict(
    "SampleDocumentKeysTypeDef",
    {
        "input": NotRequired[str],
        "output": NotRequired[str],
    },
)
TestMappingRequestRequestTypeDef = TypedDict(
    "TestMappingRequestRequestTypeDef",
    {
        "inputFileContent": str,
        "mappingTemplate": str,
        "fileFormat": FileFormatType,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateProfileRequestRequestTypeDef = TypedDict(
    "UpdateProfileRequestRequestTypeDef",
    {
        "profileId": str,
        "name": NotRequired[str],
        "email": NotRequired[str],
        "phone": NotRequired[str],
        "businessName": NotRequired[str],
    },
)
X12DelimitersTypeDef = TypedDict(
    "X12DelimitersTypeDef",
    {
        "componentSeparator": NotRequired[str],
        "dataElementSeparator": NotRequired[str],
        "segmentTerminator": NotRequired[str],
    },
)
X12FunctionalGroupHeadersTypeDef = TypedDict(
    "X12FunctionalGroupHeadersTypeDef",
    {
        "applicationSenderCode": NotRequired[str],
        "applicationReceiverCode": NotRequired[str],
        "responsibleAgencyCode": NotRequired[str],
    },
)
X12InterchangeControlHeadersTypeDef = TypedDict(
    "X12InterchangeControlHeadersTypeDef",
    {
        "senderIdQualifier": NotRequired[str],
        "senderId": NotRequired[str],
        "receiverIdQualifier": NotRequired[str],
        "receiverId": NotRequired[str],
        "repetitionSeparator": NotRequired[str],
        "acknowledgmentRequestedCode": NotRequired[str],
        "usageIndicatorCode": NotRequired[str],
    },
)
ConversionSourceTypeDef = TypedDict(
    "ConversionSourceTypeDef",
    {
        "fileFormat": ConversionSourceFormatType,
        "inputFile": InputFileSourceTypeDef,
    },
)
ConversionTargetFormatDetailsTypeDef = TypedDict(
    "ConversionTargetFormatDetailsTypeDef",
    {
        "x12": NotRequired[X12DetailsTypeDef],
    },
)
EdiTypeTypeDef = TypedDict(
    "EdiTypeTypeDef",
    {
        "x12Details": NotRequired[X12DetailsTypeDef],
    },
)
FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "x12": NotRequired[X12DetailsTypeDef],
    },
)
TemplateDetailsTypeDef = TypedDict(
    "TemplateDetailsTypeDef",
    {
        "x12": NotRequired[X12DetailsTypeDef],
    },
)
OutputSampleFileSourceTypeDef = TypedDict(
    "OutputSampleFileSourceTypeDef",
    {
        "fileLocation": NotRequired[S3LocationTypeDef],
    },
)
StartTransformerJobRequestRequestTypeDef = TypedDict(
    "StartTransformerJobRequestRequestTypeDef",
    {
        "inputFile": S3LocationTypeDef,
        "outputLocation": S3LocationTypeDef,
        "transformerId": str,
        "clientToken": NotRequired[str],
    },
)
CreateProfileRequestRequestTypeDef = TypedDict(
    "CreateProfileRequestRequestTypeDef",
    {
        "name": str,
        "phone": str,
        "businessName": str,
        "logging": LoggingType,
        "email": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "profileId": str,
        "profileArn": str,
        "name": str,
        "businessName": str,
        "phone": str,
        "email": str,
        "logging": LoggingType,
        "logGroupName": str,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStarterMappingTemplateResponseTypeDef = TypedDict(
    "CreateStarterMappingTemplateResponseTypeDef",
    {
        "mappingTemplate": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "profileId": str,
        "profileArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "businessName": str,
        "logging": LoggingType,
        "logGroupName": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransformerJobResponseTypeDef = TypedDict(
    "GetTransformerJobResponseTypeDef",
    {
        "status": TransformerJobStatusType,
        "outputFiles": List[S3LocationTypeDef],
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCapabilitiesResponseTypeDef = TypedDict(
    "ListCapabilitiesResponseTypeDef",
    {
        "capabilities": List[CapabilitySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTransformerJobResponseTypeDef = TypedDict(
    "StartTransformerJobResponseTypeDef",
    {
        "transformerJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestConversionResponseTypeDef = TypedDict(
    "TestConversionResponseTypeDef",
    {
        "convertedFileContent": str,
        "validationMessages": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestMappingResponseTypeDef = TypedDict(
    "TestMappingResponseTypeDef",
    {
        "mappedFileContent": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestParsingResponseTypeDef = TypedDict(
    "TestParsingResponseTypeDef",
    {
        "parsedFileContent": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "profileId": str,
        "profileArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "businessName": str,
        "logging": LoggingType,
        "logGroupName": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCapabilitiesRequestListCapabilitiesPaginateTypeDef = TypedDict(
    "ListCapabilitiesRequestListCapabilitiesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPartnershipsRequestListPartnershipsPaginateTypeDef = TypedDict(
    "ListPartnershipsRequestListPartnershipsPaginateTypeDef",
    {
        "profileId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfilesRequestListProfilesPaginateTypeDef = TypedDict(
    "ListProfilesRequestListProfilesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTransformersRequestListTransformersPaginateTypeDef = TypedDict(
    "ListTransformersRequestListTransformersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "profiles": List[ProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SampleDocumentsOutputTypeDef = TypedDict(
    "SampleDocumentsOutputTypeDef",
    {
        "bucketName": str,
        "keys": List[SampleDocumentKeysTypeDef],
    },
)
SampleDocumentsTypeDef = TypedDict(
    "SampleDocumentsTypeDef",
    {
        "bucketName": str,
        "keys": Sequence[SampleDocumentKeysTypeDef],
    },
)
X12OutboundEdiHeadersTypeDef = TypedDict(
    "X12OutboundEdiHeadersTypeDef",
    {
        "interchangeControlHeaders": NotRequired[X12InterchangeControlHeadersTypeDef],
        "functionalGroupHeaders": NotRequired[X12FunctionalGroupHeadersTypeDef],
        "delimiters": NotRequired[X12DelimitersTypeDef],
        "validateEdi": NotRequired[bool],
    },
)
EdiConfigurationTypeDef = TypedDict(
    "EdiConfigurationTypeDef",
    {
        "type": EdiTypeTypeDef,
        "inputLocation": S3LocationTypeDef,
        "outputLocation": S3LocationTypeDef,
        "transformerId": str,
        "capabilityDirection": NotRequired[CapabilityDirectionType],
    },
)
TestParsingRequestRequestTypeDef = TypedDict(
    "TestParsingRequestRequestTypeDef",
    {
        "inputFile": S3LocationTypeDef,
        "fileFormat": FileFormatType,
        "ediType": EdiTypeTypeDef,
    },
)
InputConversionTypeDef = TypedDict(
    "InputConversionTypeDef",
    {
        "fromFormat": Literal["X12"],
        "formatOptions": NotRequired[FormatOptionsTypeDef],
    },
)
OutputConversionTypeDef = TypedDict(
    "OutputConversionTypeDef",
    {
        "toFormat": Literal["X12"],
        "formatOptions": NotRequired[FormatOptionsTypeDef],
    },
)
CreateStarterMappingTemplateRequestRequestTypeDef = TypedDict(
    "CreateStarterMappingTemplateRequestRequestTypeDef",
    {
        "mappingType": MappingTypeType,
        "templateDetails": TemplateDetailsTypeDef,
        "outputSampleLocation": NotRequired[S3LocationTypeDef],
    },
)
ConversionTargetTypeDef = TypedDict(
    "ConversionTargetTypeDef",
    {
        "fileFormat": Literal["X12"],
        "formatDetails": NotRequired[ConversionTargetFormatDetailsTypeDef],
        "outputSampleFile": NotRequired[OutputSampleFileSourceTypeDef],
    },
)
X12EnvelopeTypeDef = TypedDict(
    "X12EnvelopeTypeDef",
    {
        "common": NotRequired[X12OutboundEdiHeadersTypeDef],
    },
)
CapabilityConfigurationTypeDef = TypedDict(
    "CapabilityConfigurationTypeDef",
    {
        "edi": NotRequired[EdiConfigurationTypeDef],
    },
)
CreateTransformerRequestRequestTypeDef = TypedDict(
    "CreateTransformerRequestRequestTypeDef",
    {
        "name": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "fileFormat": NotRequired[FileFormatType],
        "mappingTemplate": NotRequired[str],
        "ediType": NotRequired[EdiTypeTypeDef],
        "sampleDocument": NotRequired[str],
        "inputConversion": NotRequired[InputConversionTypeDef],
        "mapping": NotRequired[MappingTypeDef],
        "outputConversion": NotRequired[OutputConversionTypeDef],
        "sampleDocuments": NotRequired[SampleDocumentsTypeDef],
    },
)
CreateTransformerResponseTypeDef = TypedDict(
    "CreateTransformerResponseTypeDef",
    {
        "transformerId": str,
        "transformerArn": str,
        "name": str,
        "status": TransformerStatusType,
        "createdAt": datetime,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "ediType": EdiTypeTypeDef,
        "sampleDocument": str,
        "inputConversion": InputConversionTypeDef,
        "mapping": MappingTypeDef,
        "outputConversion": OutputConversionTypeDef,
        "sampleDocuments": SampleDocumentsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransformerResponseTypeDef = TypedDict(
    "GetTransformerResponseTypeDef",
    {
        "transformerId": str,
        "transformerArn": str,
        "name": str,
        "status": TransformerStatusType,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "ediType": EdiTypeTypeDef,
        "sampleDocument": str,
        "inputConversion": InputConversionTypeDef,
        "mapping": MappingTypeDef,
        "outputConversion": OutputConversionTypeDef,
        "sampleDocuments": SampleDocumentsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransformerSummaryTypeDef = TypedDict(
    "TransformerSummaryTypeDef",
    {
        "transformerId": str,
        "name": str,
        "status": TransformerStatusType,
        "createdAt": datetime,
        "modifiedAt": NotRequired[datetime],
        "fileFormat": NotRequired[FileFormatType],
        "mappingTemplate": NotRequired[str],
        "ediType": NotRequired[EdiTypeTypeDef],
        "sampleDocument": NotRequired[str],
        "inputConversion": NotRequired[InputConversionTypeDef],
        "mapping": NotRequired[MappingTypeDef],
        "outputConversion": NotRequired[OutputConversionTypeDef],
        "sampleDocuments": NotRequired[SampleDocumentsOutputTypeDef],
    },
)
UpdateTransformerRequestRequestTypeDef = TypedDict(
    "UpdateTransformerRequestRequestTypeDef",
    {
        "transformerId": str,
        "name": NotRequired[str],
        "status": NotRequired[TransformerStatusType],
        "fileFormat": NotRequired[FileFormatType],
        "mappingTemplate": NotRequired[str],
        "ediType": NotRequired[EdiTypeTypeDef],
        "sampleDocument": NotRequired[str],
        "inputConversion": NotRequired[InputConversionTypeDef],
        "mapping": NotRequired[MappingTypeDef],
        "outputConversion": NotRequired[OutputConversionTypeDef],
        "sampleDocuments": NotRequired[SampleDocumentsTypeDef],
    },
)
UpdateTransformerResponseTypeDef = TypedDict(
    "UpdateTransformerResponseTypeDef",
    {
        "transformerId": str,
        "transformerArn": str,
        "name": str,
        "status": TransformerStatusType,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "ediType": EdiTypeTypeDef,
        "sampleDocument": str,
        "inputConversion": InputConversionTypeDef,
        "mapping": MappingTypeDef,
        "outputConversion": OutputConversionTypeDef,
        "sampleDocuments": SampleDocumentsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestConversionRequestRequestTypeDef = TypedDict(
    "TestConversionRequestRequestTypeDef",
    {
        "source": ConversionSourceTypeDef,
        "target": ConversionTargetTypeDef,
    },
)
OutboundEdiOptionsTypeDef = TypedDict(
    "OutboundEdiOptionsTypeDef",
    {
        "x12": NotRequired[X12EnvelopeTypeDef],
    },
)
CreateCapabilityRequestRequestTypeDef = TypedDict(
    "CreateCapabilityRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["edi"],
        "configuration": CapabilityConfigurationTypeDef,
        "instructionsDocuments": NotRequired[Sequence[S3LocationTypeDef]],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateCapabilityResponseTypeDef = TypedDict(
    "CreateCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": CapabilityConfigurationTypeDef,
        "instructionsDocuments": List[S3LocationTypeDef],
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCapabilityResponseTypeDef = TypedDict(
    "GetCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": CapabilityConfigurationTypeDef,
        "instructionsDocuments": List[S3LocationTypeDef],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCapabilityRequestRequestTypeDef = TypedDict(
    "UpdateCapabilityRequestRequestTypeDef",
    {
        "capabilityId": str,
        "name": NotRequired[str],
        "configuration": NotRequired[CapabilityConfigurationTypeDef],
        "instructionsDocuments": NotRequired[Sequence[S3LocationTypeDef]],
    },
)
UpdateCapabilityResponseTypeDef = TypedDict(
    "UpdateCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": CapabilityConfigurationTypeDef,
        "instructionsDocuments": List[S3LocationTypeDef],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTransformersResponseTypeDef = TypedDict(
    "ListTransformersResponseTypeDef",
    {
        "transformers": List[TransformerSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CapabilityOptionsTypeDef = TypedDict(
    "CapabilityOptionsTypeDef",
    {
        "outboundEdi": NotRequired[OutboundEdiOptionsTypeDef],
    },
)
CreatePartnershipRequestRequestTypeDef = TypedDict(
    "CreatePartnershipRequestRequestTypeDef",
    {
        "profileId": str,
        "name": str,
        "email": str,
        "capabilities": Sequence[str],
        "phone": NotRequired[str],
        "capabilityOptions": NotRequired[CapabilityOptionsTypeDef],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreatePartnershipResponseTypeDef = TypedDict(
    "CreatePartnershipResponseTypeDef",
    {
        "profileId": str,
        "partnershipId": str,
        "partnershipArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "capabilities": List[str],
        "capabilityOptions": CapabilityOptionsTypeDef,
        "tradingPartnerId": str,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPartnershipResponseTypeDef = TypedDict(
    "GetPartnershipResponseTypeDef",
    {
        "profileId": str,
        "partnershipId": str,
        "partnershipArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "capabilities": List[str],
        "capabilityOptions": CapabilityOptionsTypeDef,
        "tradingPartnerId": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PartnershipSummaryTypeDef = TypedDict(
    "PartnershipSummaryTypeDef",
    {
        "profileId": str,
        "partnershipId": str,
        "createdAt": datetime,
        "name": NotRequired[str],
        "capabilities": NotRequired[List[str]],
        "capabilityOptions": NotRequired[CapabilityOptionsTypeDef],
        "tradingPartnerId": NotRequired[str],
        "modifiedAt": NotRequired[datetime],
    },
)
UpdatePartnershipRequestRequestTypeDef = TypedDict(
    "UpdatePartnershipRequestRequestTypeDef",
    {
        "partnershipId": str,
        "name": NotRequired[str],
        "capabilities": NotRequired[Sequence[str]],
        "capabilityOptions": NotRequired[CapabilityOptionsTypeDef],
    },
)
UpdatePartnershipResponseTypeDef = TypedDict(
    "UpdatePartnershipResponseTypeDef",
    {
        "profileId": str,
        "partnershipId": str,
        "partnershipArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "capabilities": List[str],
        "capabilityOptions": CapabilityOptionsTypeDef,
        "tradingPartnerId": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPartnershipsResponseTypeDef = TypedDict(
    "ListPartnershipsResponseTypeDef",
    {
        "partnerships": List[PartnershipSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
