from typing import overload

import numpy as np


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


halve(6)[0]
halve(np.array([6]))[0]
