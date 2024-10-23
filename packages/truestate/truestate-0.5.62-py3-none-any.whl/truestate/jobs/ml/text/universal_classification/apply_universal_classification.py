import typing

import pydantic

from truestate.datasets.dataset import Dataset
from truestate.datasets.types import DatasetConfig
from truestate.jobs.job import Job
from truestate.jobs.types import JobType


class ApplyUniversalClassificationParameters(pydantic.BaseModel):
    job_type: typing.Literal[JobType.ZeroShot] = JobType.ZeroShot
    column_name: str
    input_dataset: DatasetConfig
    output_dataset: DatasetConfig
    entities: list[str]


class ApplyUniversalClassification(Job):
    def __init__(
        self,
        inputs: Dataset | str,
        outputs: Dataset | str,
        column_name: str,
        criteria=list[str],
        name=None,
        description=None,
    ) -> None:
        if name is None:
            raise ValueError(
                "Please define a name for your universal classification job"
            )
        if description is None:
            raise ValueError(
                "Please define a description for your universal classification job"
            )

        super().__init__(self.job_type, name, description, inputs, outputs)
        self.column_name = column_name

        if (
            isinstance(criteria, list)
            and len(criteria) > 1
            and all(isinstance(i, str) for i in criteria)
        ):
            self.criteria = criteria
        else:
            raise ValueError(
                "Please provide a list of strings for the classification classes"
            )

    def params(self) -> dict:
        params = ApplyUniversalClassificationParameters(
            job_type=self.job_type,
            input_dataset=self._parse_inputs(),
            output_dataset=self._parse_outputs(),
            column_name=self.column_name,
            entities=self.criteria,
        )

        return params.dict()

    def _parse_inputs(self) -> dict:
        return self._parse_data(self.inputs)

    def _parse_outputs(self) -> dict:
        return self._parse_data(self.outputs)

    def _parse_data(self, data: typing.Union[str, Dataset]) -> dict:
        # unified function for parsing inputs or outputs
        # io is either a Dataset, List[Dataset] or Dict[str, Dataset]

        if isinstance(data, str):
            return Dataset(name=data).dict()

        elif isinstance(data, Dataset):
            return data.dict()

        else:
            raise ValueError(
                f"Invalid input type : {type(data)}, expected Dataset or str"
            )
