from enum import Enum
from typing import Literal, Union
from uuid import UUID

import pydantic

from truestate.datasets.types import DatasetConfig
from truestate.jobs.types import JobType


class IntegrationSource(str, Enum):
    Salesforce = "salesforce"
    GoogleCloudStorage = "google-cloud-storage"
    AwsS3 = "aws-s3"
    AzureBlobStorage = "azure-blob-storage"


class SecretRuntimeParams(pydantic.BaseModel):
    id: UUID
    organisation_id: str
    name: str


class SalesforceQueryType(str, Enum):
    Soql = "soql"


class IntegrationFileType(str, Enum):
    Csv = "csv"
    Parquet = "parquet"


class SalesforceIntegrationParams(pydantic.BaseModel):
    source: Literal[IntegrationSource.Salesforce] = IntegrationSource.Salesforce
    domain: str
    query_type: SalesforceQueryType = SalesforceQueryType.Soql
    query: str


class GoogleCloudStorageIntegrationParams(pydantic.BaseModel):
    source: Literal[IntegrationSource.GoogleCloudStorage] = (
        IntegrationSource.GoogleCloudStorage
    )
    path: str
    filetype: IntegrationFileType


class AzureBlobStorageIntegrationParams(pydantic.BaseModel):
    source: Literal[IntegrationSource.AzureBlobStorage] = (
        IntegrationSource.AzureBlobStorage
    )
    path: str
    filetype: IntegrationFileType


class AwsS3IntegrationParams(pydantic.BaseModel):
    source: Literal[IntegrationSource.AwsS3] = IntegrationSource.AwsS3
    path: str
    filetype: IntegrationFileType


class IntegrationConfig(pydantic.BaseModel):
    job_type: Literal[JobType.Integration] = JobType.Integration
    integration_config: Union[
        SalesforceIntegrationParams,
        GoogleCloudStorageIntegrationParams,
        AzureBlobStorageIntegrationParams,
        AwsS3IntegrationParams,
    ] = pydantic.Field(..., discriminator="source")
    credential_secret: str
    input_dataset: DatasetConfig = None
    output_dataset: DatasetConfig = None
