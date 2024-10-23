import typing

from truestate.datasets.dataset import Dataset
from truestate.jobs.integrations.types import (
    AwsS3IntegrationParams,
    AzureBlobStorageIntegrationParams,
    GoogleCloudStorageIntegrationParams,
    IntegrationConfig,
    IntegrationFileType,
    SalesforceIntegrationParams,
)
from truestate.jobs.job import Job
from truestate.jobs.types import JobType


class CloudStorageIntegration(Job):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        output: typing.Union[Dataset, str] = None,
        path: str = None,
        filetype: IntegrationFileType = None,
        secret_name: str = None,
    ) -> None:
        if name is None:
            raise ValueError("Please specify a name for your integration.")

        self.name = name

        if description is None:
            description = ""

        self.description = description

        if output is None:
            raise ValueError(f"Please specify an output for your integration: {name}")

        self.output = output

        if path is None:
            raise ValueError(f"Please specify a path for your integration: {name}")
        self.path = path

        if filetype is None:
            raise ValueError(
                f"Please specify a filetype for the integration {name}, can be csv or parquet"
            )

        self.filetype = filetype

        if secret_name is None:
            raise ValueError(
                f"Please specify a secret_name for your integration: {name}"
            )

        self.secret_name = secret_name

        super().__init__(
            JobType.Integration, name, description, inputs=None, outputs=output
        )

    @property
    def _params_model(self):
        raise NotImplementedError

    def _parse_output(self) -> dict:
        return self._parse_data(self.output)

    def _parse_data(self, data: typing.Union[str, Dataset]) -> dict:
        if isinstance(data, str):
            return Dataset(name=data).dict()

        elif isinstance(data, Dataset):
            return data.dict()

        else:
            raise ValueError(
                f"Invalid input type : {type(data)}, expected Dataset or str"
            )

    def params(self) -> dict:
        _params = IntegrationConfig(
            integration_config=self._params_model(
                path=self.path,
                filetype=self.filetype,
            ),
            credential_secret=self.secret_name,
            output_dataset=self._parse_output(),
        )

        return _params.model_dump()


class BlobStorageRead(CloudStorageIntegration):
    _params_model = AzureBlobStorageIntegrationParams


class GCSRead(CloudStorageIntegration):
    _params_model = GoogleCloudStorageIntegrationParams


class S3Read(CloudStorageIntegration):
    _params_model = AwsS3IntegrationParams


class SalesforceRead(Job):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        output: typing.Union[Dataset, str] = None,
        domain: str = None,
        query: str = None,
        secret_name: str = None,
    ) -> None:
        if name is None:
            raise ValueError("Please specify a name for your integration.")

        self.name = name

        if description is None:
            description = ""

        self.description = description

        if output is None:
            raise ValueError(f"Please specify an output for your integration: {name}")

        self.output = output

        if domain is None:
            raise ValueError(
                f"Please specify a domain for your Salesforce integration: {name}"
            )

        self.domain = domain

        if query is None:
            raise ValueError(
                f"Please specify a query for your Salesforce integration: {name}"
            )

        self.query = query

        if secret_name is None:
            raise ValueError(
                "Please specify a secret_name for your Salesforce integration: {name}"
            )

        self.secret_name = secret_name

        super().__init__(
            JobType.Integration, name, description, inputs=None, outputs=output
        )

    def params(self) -> dict:
        _params = IntegrationConfig(
            integration_config=SalesforceIntegrationParams(
                domain=self.domain,
                query=self.query,
            ),
            credential_secret=self.secret_name,
            output_dataset=self._parse_output(),
        )

        return _params.model_dump()

    def _parse_output(self) -> dict:
        return self._parse_data(self.output)

    def _parse_data(self, data: typing.Union[str, Dataset]) -> dict:
        if isinstance(data, str):
            return Dataset(name=data).dict()

        elif isinstance(data, Dataset):
            return data.dict()

        else:
            raise ValueError(
                f"Invalid input type : {type(data)}, expected Dataset or str"
            )
