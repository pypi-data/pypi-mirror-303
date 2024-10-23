import logging
from typing import List

from pydantic import BaseModel, Field

from truestate.client import get_client
from truestate.exceptions import APIError


class ClassificationResponse(BaseModel):
    text: str
    results: dict[str, float] = Field(
        ..., description="Mapping of categories to their match scores"
    )


def classify(text: str, choices: list[str]) -> dict:

    if len(choices) == 0:
        raise ValueError("Please provide at least one category to classify against")
    
    client = get_client()

    status_code, response = client.post(
        "/inference/entity-match",
        data={"text": text, "categories": choices},
    )

    if status_code not in {200, 201}:
        raise APIError(f"API request failed with status code {status_code}: {response}")

    logging.debug(response)

    result = ClassificationResponse.model_validate(response).model_dump()

    return {key: score for key, score in result["results"].items()}
