import re
import typing

from truestate.datasets.dataset import Dataset
from truestate.jobs.data.types import AliasDataset, DataTransformConfig
from truestate.jobs.job import Job
from truestate.jobs.types import JobType


class DataTransform(Job):
    def __init__(
        self,
        input_datasets: typing.Union[
            Dataset, typing.List[Dataset], typing.Dict[str, Dataset]
        ],
        output_datasets: typing.Union[
            Dataset, typing.List[Dataset], typing.Dict[str, Dataset]
        ],
        query: str,
        name=None,
        description=None,
    ) -> None:
        if not name or len(name) == 0:
            raise ValueError("Please define a name for your data transform job")

        if not description or len(description) == 0:
            raise ValueError("Please define a description for your data transform job")

        super().__init__(
            JobType.DataTransform, name, description, input_datasets, output_datasets
        )

        if not query or len(query) == 0:
            raise ValueError("Please define a query for your data transform job")
        else:
            self.query = query

        self._validate_alias_uniqueness()

    def params(self) -> dict:
        params = DataTransformConfig(
            input_datasets=self._parse_inputs(),
            output_datasets=self._parse_outputs(),
            query=self.query,
        )

        return params.model_dump()

    def _parse_inputs(self) -> typing.List[AliasDataset]:
        return self._parse_data(self.inputs)

    def _parse_outputs(self) -> typing.List[AliasDataset]:
        return self._parse_data(self.outputs)

    def _parse_data(
        self,
        data: typing.Union[
            str, Dataset, typing.List[Dataset], typing.Dict[str, Dataset]
        ],
    ) -> typing.List[AliasDataset]:
        # unified function for parsing inputs or outputs
        # io is either a Dataset, List[Dataset] or Dict[str, Dataset]

        if isinstance(data, str):
            return [
                AliasDataset(
                    alias=self._validate_alias_name(data),
                    dataset=Dataset(name=data).dict(),
                )
            ]

        elif isinstance(data, Dataset):
            return [
                AliasDataset(
                    alias=self._validate_alias_name(data.name), dataset=data.dict()
                )
            ]

        elif isinstance(data, typing.List):
            aliases = []
            for item in data:
                if isinstance(item, Dataset):
                    aliases.append(
                        AliasDataset(
                            alias=self._validate_alias_name(item.name),
                            dataset=item.dict(),
                        )
                    )
                elif isinstance(item, str):
                    aliases.append(
                        AliasDataset(
                            alias=self._validate_alias_name(item),
                            dataset=Dataset(name=item).dict(),
                        )
                    )
                else:
                    raise ValueError(
                        f"Invalid input type in list : {type(item)}, expected Dataset or str"
                    )

            return aliases

        elif isinstance(data, typing.Dict):
            aliases = []
            for k, v in data.items():
                if isinstance(v, Dataset):
                    aliases.append(
                        AliasDataset(
                            alias=self._validate_alias_name(k), dataset=v.dict()
                        )
                    )
                elif isinstance(v, str):
                    aliases.append(
                        AliasDataset(
                            alias=self._validate_alias_name(k),
                            dataset=Dataset(name=v).dict(),
                        )
                    )
                else:
                    raise ValueError(
                        f"Invalid input type in dictionary : {type(item)}, expected Dataset or str"
                    )

            return aliases

        else:
            raise ValueError(
                f"Invalid input type : {type(data)}, expected Dataset, List[Dataset] or Dict[str, Dataset]"
            )

    def _validate_alias_name(self, alias_name: str) -> bool:
        pattern = r"^[a-zA-Z][a-zA-Z0-9_]*$"
        if bool(re.match(pattern, alias_name)):
            return alias_name
        else:
            raise Exception(
                f"Creating alias from string '{alias_name}' for DataTransform {self.name} failed. Must only contain letters, numbers or underscores and begin with a letter."
            )

    def _validate_alias_uniqueness(self):
        inputs = self._parse_inputs()
        outputs = self._parse_outputs()

        aliases = [alias.alias for alias in inputs + outputs]

        if len(aliases) != len(set(aliases)):
            raise ValueError(
                f"DataTransform {self.name} has duplicate aliases. Aliases must be unique."
            )
