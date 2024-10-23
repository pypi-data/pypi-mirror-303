import typing

import pydantic

from truestate.datasets.dataset import Dataset
from truestate.datasets.types import DatasetConfig
from truestate.jobs.job import Job
from truestate.jobs.types import JobType


class EmbeddingConfig(pydantic.BaseModel):
    job_type: typing.Literal[JobType.ApplyEmbeddings] = JobType.ApplyEmbeddings
    column_name: str
    input_dataset: DatasetConfig
    output_dataset: DatasetConfig


class ApplyEmbedding(Job):
    def __init__(
        self,
        name: str,
        description: str,
        input_dataset: Dataset | str,
        output_dataset: Dataset | str,
        inference_column_name: str,
    ) -> None:
        if name is None:
            raise ValueError("Please define a name for your data transform job")

        if description is None:
            raise ValueError("Please define a description for your data transform job")

        super().__init__(
            job_type=JobType.ApplyEmbeddings,
            name=name,
            description=description,
            inputs=input_dataset,
            outputs=output_dataset,
        )

        self.column_name = inference_column_name

    def params(self) -> dict:
        params = EmbeddingConfig(
            column_name=self.column_name,
            input_dataset=self._parse_data(self.inputs),
            output_dataset=self._parse_data(self.outputs),
        )

        return params.model_dump()

    def _parse_data(self, data: typing.Union[str, Dataset]) -> dict:
        if isinstance(data, str):
            return Dataset(name=data).dict()

        elif isinstance(data, Dataset):
            return data.dict()

        else:
            raise ValueError(
                f"Invalid input type : {type(data)}, expected Dataset or str"
            )
