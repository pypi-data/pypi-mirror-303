import logging
import typing

from truestate.client import get_client
from truestate.exceptions import APIError


def route(text: str, strategy: dict, threshold: float = 0.5) -> typing.Any:
    """Routes text to downstream functions based on the consistency of the text with the provided strategy."""

    choices = [key for key in strategy.keys() if key != "__default__"]

    client = get_client()

    status_code, response = client.post(
        "/inference/entity-match",
        data={"text": text, "categories": choices},
    )

    logging.debug(response)

    if status_code not in {200, 201}:
        raise APIError(f"API request failed with status code {status_code}: {response}")

    else:
        results = response["results"]

        key = max(results, key=results.get)
        value = results[key]

        if value >= threshold or "__default__" not in strategy:
            return strategy[key](text)
        else:
            return strategy["__default__"](text)
