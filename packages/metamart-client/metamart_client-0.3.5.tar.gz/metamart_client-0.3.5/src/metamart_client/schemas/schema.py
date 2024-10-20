from pathlib import Path
from typing import Any, Dict, Iterable, Literal, Type, Union

import yaml
from metamart_schemas.schema import MetamartType, Schema


def validate_file(file: Union[str, Path]) -> Iterable[MetamartType]:
    """

    Args:
        file (Union[str, Path]):

    Returns:

    Raises:

    """
    with open(file) as f:
        for item in yaml.safe_load_all(f):
            yield Schema(entity=item).entity
