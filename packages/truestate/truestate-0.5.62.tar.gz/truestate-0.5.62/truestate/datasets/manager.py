import typing
import uuid

from truestate.datasets.types import DatasetConfig


class DatasetManager:
    def __init__(self, client):
        self.client = client

    def get(self, id: uuid.UUID = None, name: str = None):
        if id is None and name is None:
            result = self.client.get("/datasets/")

            datasets = [
                DatasetConfig(name=i["name"], description=i["description"])
                for i in result
            ]

            return datasets

        elif name is None:
            # look up by id
            result = self.client.get("/datasets/{id}/")

            if result.get("detail") == "Dataset not found":
                return None

            return DatasetConfig(name=result["name"], description=result["description"])

        else:
            # look up by name
            result = self.client.get("/datasets/?name={name}")

            if len(result) == 0:
                return None

            elif len(result) > 1:
                raise Exception("Multiple datasets found with the same name")

            else:
                return DatasetConfig(
                    name=result["name"], description=result["description"]
                )

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return self.get(*args, **kwargs)
