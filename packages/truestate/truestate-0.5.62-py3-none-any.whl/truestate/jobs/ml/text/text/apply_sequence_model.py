import typing
from enum import Enum
import pydantic

from truestate.datasets.dataset import Dataset
from truestate.datasets.types import DatasetConfig
from truestate.jobs.job import Job
from truestate.jobs.types import JobType


class BulkPromptBaseModelType(str, Enum):
    Meta_llama_3_2_1b_instruct = "meta_llama_3_2_1b_instruct"
    Meta_llama_3_2_3b_instruct = "meta_llama_3_2_3b_instruct"
    Phi_3_mini_4k_instruct = "Phi_3_mini_4k_instruct"

class LLMBatchInferenceConfig(pydantic.BaseModel):
    job_type: typing.Literal[JobType.BulkPrompt] = JobType.BulkPrompt
    prompt: str
    input_dataset: DatasetConfig
    output_dataset: DatasetConfig
    base_model_type: BulkPromptBaseModelType | None = BulkPromptBaseModelType.Meta_llama_3_2_3b_instruct

class LLMBatchInference(Job):
    def __init__(
        self,
        name: str,
        description: str,
        input_dataset: Dataset | str,
        output_dataset: Dataset | str,
        prompt: str,
    ) -> None:
        if name is None:
            raise ValueError("Please define a name for your data transform job")

        if description is None:
            raise ValueError("Please define a description for your data transform job")

        super().__init__(
            job_type=JobType.BulkPrompt,
            name=name,
            description=description,
            inputs=input_dataset,
            outputs=output_dataset,
        )
        self.prompt = prompt

    def params(self) -> dict:
        params = LLMBatchInferenceConfig(
            job_type=self.job_type,
            prompt=self.prompt,
            input_dataset=self._parse_data(self.inputs),
            output_dataset=self._parse_data(self.outputs),
        )

        return params.model_dump()

    def _parse_data(self, data: str | Dataset) -> dict:
        if isinstance(data, str):
            return Dataset(name=data).dict()

        elif isinstance(data, Dataset):
            return data.dict()

        else:
            raise ValueError(
                f"Invalid input type : {type(data)}, expected Dataset or str"
            )
