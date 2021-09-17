import json
from pathlib import Path
from typing import Dict, Union, cast, overload

import numpy as np
import numpy.typing as npt


@overload
def halve(value: int) -> float:
    pass


@overload
def halve(value: float) -> float:
    pass


@overload
def halve(value: np.ndarray) -> np.ndarray:
    pass


def halve(value):
    return value / 2


class A:
    def get_thing(self) -> "B":
        ...


class B:
    ...


halve(6)[0]  # what does mypy say?
halve(np.array([6]))[0]


def load_json(path: str) -> Union[dict, list]:
    with open(path) as f:
        return json.load(f)


data = load_json("model_options.json")
data.items()

data = cast(dict, load_json("model_options.json"))
data.items()

events = cast(list, load_json("events.json"))
events.reverse()

reveal_locals()

reveal_type(events)
