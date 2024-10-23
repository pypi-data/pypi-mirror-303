import typing

import pydantic

from truestate.datasets.dataset import Dataset
from truestate.datasets.types import DatasetConfig
from truestate.jobs.job import Job
from truestate.jobs.types import JobType
from truestate.models.model import Model
from truestate.models.types import ModelConfig


class PreferenceTrainingConfig(pydantic.BaseModel):
    job_type: typing.Literal[JobType.PreferenceTraining] = JobType.PreferenceTraining
    input_dataset: DatasetConfig
    output_model: ModelConfig


class TrainTextPreferenceModel(Job):
    def __init__(
        self,
        name: str,
        description: str,
        input_dataset: Dataset | str,
        output_model: Model | str,
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
            JobType.PreferenceTraining,
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

    def params(self) -> dict:
        params = PreferenceTrainingConfig(
            input_dataset=self._parse_data(self.input_dataset),
            output_model=self._parse_model(self.output_model),
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


class PreferenceInferenceConfig(pydantic.BaseModel):
    job_type: typing.Literal[JobType.PreferenceInference] = JobType.PreferenceInference
    inference_column_name: str
    output_column_name: str
    input_model: ModelConfig
    input_dataset: DatasetConfig
    output_dataset: DatasetConfig


class ApplyTextPreferenceModel(Job):
    def __init__(
        self,
        name: str,
        description: str,
        input_model: Model | str,
        input_dataset: Dataset | str,
        output_dataset: Dataset | str,
        inference_column_name: str,
        output_column_name: str,
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
            JobType.PreferenceInference,
            name,
            description,
            [input_model, input_dataset],
            output_dataset,
        )

        if not input_model:
            raise ValueError(
                "Please define an input model for your classifier training job"
            )

        self.input_model = input_model

        if not input_dataset:
            raise ValueError(
                "Please define an input dataset for your classifier training job"
            )

        self.input_dataset = input_dataset

        if not output_dataset:
            raise ValueError(
                "Please define an output dataset for your classifier training job"
            )

        self.output_dataset = output_dataset

        if not inference_column_name or len(inference_column_name) == 0:
            raise ValueError(
                "Please define an inference column name for your classifier training job"
            )

        self.inference_column_name = inference_column_name

        if not output_column_name or len(output_column_name) == 0:
            raise ValueError(
                "Please define an output column name for your classifier training job"
            )

        self.output_column_name = output_column_name

    def params(self) -> dict:
        params = PreferenceInferenceConfig(
            inference_column_name=self.inference_column_name,
            output_column_name=self.output_column_name,
            input_model=self._parse_model(self.input_model),
            input_dataset=self._parse_data(self.input_dataset),
            output_dataset=self._parse_data(self.output_dataset),
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
