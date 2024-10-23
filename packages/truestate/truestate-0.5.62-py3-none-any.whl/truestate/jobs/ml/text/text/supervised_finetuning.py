import typing

import pydantic

from truestate.datasets.dataset import Dataset
from truestate.datasets.types import DatasetConfig
from truestate.jobs.job import Job
from truestate.jobs.types import JobType
from truestate.models.model import Model
from truestate.models.types import ModelConfig


class SFTHyperParameters(pydantic.BaseModel):
    max_steps: int


class SFTTrainingConfig(pydantic.BaseModel):
    job_type: typing.Literal[JobType.SFTTraining] = JobType.SFTTraining
    format_str: str
    input_dataset: DatasetConfig
    output_model: ModelConfig
    sft_config: SFTHyperParameters


class FineTuneLLM(Job):
    def __init__(
        self,
        name: str,
        description: str,
        input_dataset: Dataset | str,
        output_model: Model | str,
        column_name: str,
        hyperparameters: SFTHyperParameters = None,
    ) -> None:
        if not name or len(name) == 0:
            raise ValueError(
                "Please define a name for your text classifier training job"
            )

        if not description or len(description) == 0:
            raise ValueError(
                "Please define a description for your classifier training job"
            )

        super().__init__(
            JobType.SFTTraining,
            name,
            description,
            input_dataset,
            output_model,
        )

        if not input_dataset:
            raise ValueError(
                "Please define an input dataset for your classifier training job"
            )

        self.input_dataset = input_dataset

        if not output_model:
            raise ValueError(
                "Please define an output model for your classifier training job"
            )

        self.output_model = output_model

        self.format_str = "{%s}" % column_name

        if hyperparameters:
            self.hyperparameters = hyperparameters
        else:
            self.hyperparameters = SFTHyperParameters(max_steps=1000)

    def params(self) -> dict:
        params = SFTTrainingConfig(
            input_dataset=self._parse_data(self.input_dataset),
            output_model=self._parse_model(self.output_model),
            format_str=self.format_str,
            sft_config=self.hyperparameters,
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

    def _parse_model(self, model: typing.Union[str, Model]) -> dict:
        if isinstance(model, str):
            return Model(name=model).dict()

        elif isinstance(model, Model):
            return model.dict()

        else:
            raise ValueError(
                f"Invalid input type : {type(model)}, expected Model or str"
            )
