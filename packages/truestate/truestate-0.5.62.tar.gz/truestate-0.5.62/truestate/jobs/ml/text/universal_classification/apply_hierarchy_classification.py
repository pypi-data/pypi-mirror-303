import typing

import pydantic

from truestate.artifacts.classification import ClassHierarchy
from truestate.client import get_client
from truestate.datasets.dataset import Dataset
from truestate.jobs.job import Job
from truestate.jobs.types import JobType


class ApplyHierarchyClassificationParameters(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)
    job_type: str
    input_dataset: dict
    output_dataset: dict
    column_name: str
    classification_classes: str


class ApplyHierarchyClassification(Job):
    def __init__(
        self,
        input_dataset: typing.Union[Dataset, str],
        output_dataset: typing.Union[Dataset, str],
        column_name: str,
        hierarchy=ClassHierarchy,
        name=None,
        description=None,
    ) -> None:
        if name is None:
            raise ValueError(
                "Please define a name for your zero-shot classification job"
            )
        if description is None:
            raise ValueError(
                "Please define a description for your zero-shot classification job"
            )

        super().__init__(
            JobType.ZeroShot, name, description, input_dataset, output_dataset
        )
        self.column_name = column_name
        self.hierarchy_reference = self._initialise_classification_classes(hierarchy)

    def _initialise_classification_classes(self, classification_classes):
        
        if isinstance(classification_classes, str):
            return classification_classes
        
        elif isinstance(classification_classes, ClassHierarchy):
            client = get_client()
            client.artifacts.sync(classification_classes)
            return classification_classes.name

        else:
            raise ValueError(f"Invalid classification classes type, expected str or ClassHierarchy object: {type(classification_classes)}")

    def params(self) -> dict:
        params = ApplyHierarchyClassificationParameters(
            job_type=self.job_type,
            input_dataset=self._parse_inputs(),
            output_dataset=self._parse_outputs(),
            column_name=self.column_name,
            classification_classes=self.hierarchy_reference,
        )

        return params.model_dump()

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
