import typing

import pydantic

from truestate.datasets.dataset import Dataset
from truestate.datasets.types import DatasetConfig
from truestate.jobs.job import Job
from truestate.jobs.types import JobType
from truestate.models.model import Model
from truestate.models.types import ModelConfig


class TextClassificationConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    num_train_epochs: int = 10


class ClassificationTrainingConfig(pydantic.BaseModel):
    job_type: typing.Literal[JobType.ClassificationTraining] = (
        JobType.ClassificationTraining
    )
    text_column_name: str
    label_column_name: str
    input_dataset: DatasetConfig
    output_model: ModelConfig
    classification_config: TextClassificationConfig


class TrainTextClassifier(Job):
    def __init__(
        self,
        name: str,
        description: str,
        input_dataset: Dataset | str,
        output_model: Model | str,
        text_column_name: str,
        label_column_name: str,
        classification_config: TextClassificationConfig | dict = None,
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
            JobType.ClassificationTraining,
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

        if not text_column_name or len(text_column_name) == 0:
            raise ValueError(
                "Please define a text column name for your classifier training job"
            )

        self.text_column_name = text_column_name

        if not label_column_name or len(label_column_name) == 0:
            raise ValueError(
                "Please define a label column name for your classifier training job"
            )

        self.label_column_name = label_column_name

        if not classification_config:
            self.classification_config = TextClassificationConfig()
        elif isinstance(classification_config, TextClassificationConfig):
            self.classification_config = classification_config
        elif isinstance(classification_config, dict):
            self.classification_config = TextClassificationConfig(
                **classification_config
            )
        else:
            raise ValueError(
                "classifiction_config must be either a TextClassificationConfig or dict"
            )

    def params(self) -> dict:
        params = ClassificationTrainingConfig(
            text_column_name=self.text_column_name,
            label_column_name=self.label_column_name,
            input_dataset=self._parse_data(self.input_dataset),
            output_model=self._parse_model(self.output_model),
            classification_config=self.classification_config,
        )

        return params.model_dump()

    def _parse_input(self) -> dict:
        return self._parse_data(self.input)

    def _parse_outputs(self) -> dict:
        return self._parse_model(self.output)

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


class ClassificationInferenceConfig(pydantic.BaseModel):
    job_type: typing.Literal[JobType.ClassificationInference] = (
        JobType.ClassificationInference
    )
    inference_column_name: str
    output_column_name: str
    n_inference_choices: int
    inference_batch_size: int
    input_model: ModelConfig
    input_dataset: DatasetConfig
    output_dataset: DatasetConfig


class ApplyTextClassifier(Job):
    def __init__(
        self,
        name: str,
        description: str,
        input_model: Model | str,
        input_dataset: Dataset | str,
        output_dataset: Dataset | str,
        inference_column_name: str,
        output_column_name: str,
        n_inference_choices: int = 1,
        inference_batch_size: int = 32,
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
            JobType.ClassificationInference,
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
        self.n_inference_choices = n_inference_choices
        self.inference_batch_size = inference_batch_size

    def params(self) -> dict:
        params = ClassificationInferenceConfig(
            inference_column_name=self.inference_column_name,
            output_column_name=self.output_column_name,
            n_inference_choices=self.n_inference_choices,
            inference_batch_size=self.inference_batch_size,
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
