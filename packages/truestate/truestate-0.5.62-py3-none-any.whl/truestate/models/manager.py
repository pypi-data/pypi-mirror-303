import typing
import uuid

from truestate.models.types import ModelConfig


class ModelsManager:
    def __init__(self, client):
        self.client = client

    def get(self, id: uuid.UUID = None, name: str = None):
        if id is None and name is None:
            result = self.client.get("/models/")

            datasets = [
                ModelConfig(name=i["name"], description=i["description"])
                for i in result
            ]

            return datasets

        elif name is None:
            # look up by id
            result = self.client.get("/models/{id}/")

            if result.get("detail") == "Model not found":
                return None

            return ModelConfig(name=result["name"], description=result["description"])

        else:
            # look up by name
            result = self.client.get("/models/?name={name}")

            if len(result) == 0:
                return None

            elif len(result) > 1:
                raise Exception("Multiple models found with the same name")

            else:
                return ModelConfig(
                    name=result["name"], description=result["description"]
                )

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return self.get(*args, **kwargs)
