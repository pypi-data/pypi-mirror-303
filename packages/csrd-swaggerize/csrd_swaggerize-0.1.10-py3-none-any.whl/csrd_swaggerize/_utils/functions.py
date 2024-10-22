from typing import List, Any


def init_params(params: List[Any]) -> List[Any]:
    if params is None:
        params = []
    return params


def init_responses(responses: dict = None):
    if responses is None:
        responses = {}
    return responses
