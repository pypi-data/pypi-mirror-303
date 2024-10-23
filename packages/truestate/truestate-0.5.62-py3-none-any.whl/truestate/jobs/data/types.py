import typing

import pydantic

from truestate.datasets.types import DatasetConfig
from truestate.jobs.types import JobType


class AliasDataset(pydantic.BaseModel):
    alias: str
    dataset: DatasetConfig


class DataTransformConfig(pydantic.BaseModel):
    job_type: typing.Literal[JobType.DataTransform] = JobType.DataTransform
    query_type: str = "sql"
    query: str
    input_datasets: list[AliasDataset]
    output_datasets: list[AliasDataset]
