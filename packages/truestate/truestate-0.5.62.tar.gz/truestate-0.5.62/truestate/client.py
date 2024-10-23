import json
import os
from typing import Any
from enum import Enum

import requests

from pydantic import BaseModel
from truestate.artifacts.classification import ClassHierarchy

from truestate.artifacts.manager import ArtifactsManager
from truestate.datasets.manager import DatasetManager
from truestate.models.manager import ModelsManager
from truestate.secrets.manager import SecretManager
from truestate.workflows.manager import WorkflowManager


DEFAULT_URL = os.environ.get("TRUESTATE_HOST", "https://api.truestate.io")

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        if isinstance(obj, ClassHierarchy):
            return obj.dict()
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        return super().default(obj)


class Client:
    def __init__(
        self, api_key: str = None, organisation_id: str = None, base_url: str = None
    ):
        if api_key is None:
            api_key = os.environ.get("TRUESTATE_API_KEY")

        if api_key is None:
            raise ValueError(
                "Please ensure you set your API key as an environment variable, e.g. export TRUESTATE_API_KEY='your_api_key'"
            )

        if organisation_id is None:
            organisation_id = os.environ.get("TRUESTATE_ORGANISATION")

        if organisation_id is None:
            raise ValueError(
                "organisation not specified. Please ensure you enter your organisation_id, e.g. ts = Client(api_key, organisation='org_1234567890abcdef')"
            )

        if base_url is None:
            base_url = DEFAULT_URL

        self.organisation_id = organisation_id
        self.base_url = base_url
        self.headers = {
            "accept": "application/json",
            "Current-Org-Id": f"{organisation_id}",
            "Api-key": f"{api_key}",
        }
        self.workflows = WorkflowManager(self)
        self.datasets = DatasetManager(self)
        self.models = ModelsManager(self)
        self.secrets = SecretManager(self)
        self.artifacts = ArtifactsManager(self)

    def get(self, url: str) -> Any:
        print(url, self.headers)
        response = requests.get(self.base_url + url, headers=self.headers)

        if response.status_code == 401:
            raise Exception(
                "Unauthorized. Please check your API key is correct and valid for the supplied organisation_id"
            )

        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text

    def post(self, url: str, data: Any) -> Any:
        print(url, self.headers)
        response = requests.post(
            self.base_url + url,
            headers=self.headers,
            data=json.dumps(data, cls=CustomJSONEncoder, indent=2),
        )

        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text

    def put(self, url: str, data: Any) -> Any:
        response = requests.put(
            self.base_url + url,
            headers=self.headers,
            data=json.dumps(data, cls=CustomJSONEncoder, indent=2),
        )
        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text

    def patch(self, url: str, data: Any) -> Any:
        response = requests.patch(
            self.base_url + url,
            headers=self.headers,
            data=json.dumps(data, cls=CustomJSONEncoder, indent=2),
        )
        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text

    def delete(self, url: str) -> Any:
        response = requests.delete(self.base_url + url, headers=self.headers)
        try:
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            return response.status_code, response.text


def get_client(
    api_key: str = None, organisation_id: str = None, base_url: str = None
) -> Client:
    return Client(api_key, organisation_id, base_url)
