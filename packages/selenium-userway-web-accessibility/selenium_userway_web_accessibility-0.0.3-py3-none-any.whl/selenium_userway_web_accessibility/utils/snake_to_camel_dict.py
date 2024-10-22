from typing import Any

from humps import camel


def snake_to_camel_dict(dictionary: dict[str, Any]) -> dict[str, Any]:
    return {camel.case(k): v for k, v in dictionary.items()}
