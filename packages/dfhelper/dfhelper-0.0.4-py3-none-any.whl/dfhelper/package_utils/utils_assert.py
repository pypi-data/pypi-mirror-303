"""

"""
from typing import Sequence, List, Any
import inspect

import pandas as pd


def assert_dfs_nonempty(*dfs) -> None:
    if len(dfs) < 1:
        raise ValueError("At least one DataFrame must be provided.")


def assert_matching_lengths(var1: Sequence, var2: Sequence) -> None:
    frame = inspect.currentframe().f_back
    var_names = {id(v): name for name, v in frame.f_locals.items()}
    name1 = var_names.get(id(var1), 'first argument')
    name2 = var_names.get(id(var2), 'second argument')

    if len(var1) != 0 and len(var1) != len(var2):
        raise ValueError(f"The number of items in {name1} must match the number of items in {name2}.")


def validate_choice(variable_name: str,
                    valid_choices: List[Any],
                    given_value: Any) -> None:
    if given_value not in valid_choices:
        valid_str = ", ".join(str(choice) for choice in valid_choices)
        raise ValueError(f"The value '{given_value}' for '{variable_name}' is invalid. "
                         f"Expected one of: {valid_str}.")