from json import JSONDecodeError

from truestate.client import get_client
from truestate.exceptions import APIError


def search(query: str, id: str, num_results: int = 10) -> list[dict]:
    if num_results < 1 or num_results > 1000:
        raise ValueError("num_results must be between 1 and 1000")

    client = get_client()

    status_code, response = client.post(
        "/data/embedding_search",
        data={"sentence": query, "dataset_id": id, "top_k": num_results},
    )

    if status_code not in {200, 201}:
        raise APIError(f"API request failed with status code {status_code}: {response}")

    try:
        result = response.json()
        return result
    except JSONDecodeError:
        raise JSONDecodeError(f"Error: {response.text}")
