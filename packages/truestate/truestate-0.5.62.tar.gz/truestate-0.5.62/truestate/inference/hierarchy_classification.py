import logging

import pydantic

from truestate.artifacts.classification import Category
from truestate.client import get_client
from truestate.exceptions import APIError

class HierarchyCategorisationResponse(pydantic.BaseModel):
    """
    A response model for the hierarchy classification endpoint.
    """

    text: str
    categories: dict[str, str]


def hierarchy_classification(text: str, hierarchy: Category) -> dict:
    
    client = get_client()

    data = hierarchy.dict()

    status_code, response = client.post(
        "/inference/hierarchy-classification",
        data={"text": text, "classification_class": data["classification_classes"]},
    )

    if status_code not in {200, 201}:
        raise APIError(f"API request failed with status code {status_code}: {response}")

    logging.debug(response)

    return HierarchyCategorisationResponse(**response).model_dump()
