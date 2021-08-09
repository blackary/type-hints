from pathlib import Path
from typing import Any, Optional, Union


def apply_model(model: Any):
    model.get_predictions([1, 2, 3])
    model.any_arbitrary_function("hi", False)  # no mypy error


def read_from_file_path(path: Union[Path, str]):
    if isinstance(path, str):  # inside this block, mypy knows this is a string
        ...
    elif isinstance(path, Path):
        ...


# These three have the same types specified in 3 different ways
def copy(directory: str, file: Union[str, None] = None):
    # Second parameter can be of type str or None
    ...


def copy2(directory: str, file: Optional[str] = None):
    # Optional[arg] == Union[arg, None]
    ...


def copy3(directory: str, file: str = None):
    # If you're defaulting a function argument to None, the
    # Optional is implied
    ...
