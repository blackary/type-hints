from typing import Callable

import numpy as np
import pandas as pd

# Callable[[list_of_argument_types], return_type]


def apply_transform(
    df: pd.DataFrame, transform: Callable[[pd.DataFrame], None]
) -> None:
    transform(df)


def fetch_data(fetcher: Callable[..., pd.DataFrame], **kwargs) -> pd.DataFrame:
    return fetcher(**kwargs)


def create_grid(
    arg1: int, arg2: int, grid_fn: Callable[[int, int], np.ndarray]
) -> np.ndarray:
    return grid_fn(arg1, arg2)
