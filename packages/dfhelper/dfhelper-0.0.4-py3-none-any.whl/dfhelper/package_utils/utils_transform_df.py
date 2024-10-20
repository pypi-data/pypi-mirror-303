"""

"""

import pandas as pd
from typing import Tuple
from dfhelper.package_utils.utils_assert import (validate_choice,
                                                 assert_matching_lengths)


def truncate_text(text: str, max_length: int, method: str = 'characters') -> str:
    if isinstance(text, str):
        if method == 'characters':
            if len(text) > max_length:
                return text[:max_length] + "..."
        elif method == 'words':
            words = text.split()
            if len(words) > max_length:
                return ' '.join(words[:max_length]) + "..."
    return text


def truncate_dataframe_text(*dfs,
                            max_length: int,
                            method: str = 'characters') -> Tuple[pd.DataFrame, ...]:
    validate_choice('method', ['characters', 'words'], method)

    output_dfs = []
    for df in dfs:
        df = df.copy()
        truncated_df = df.applymap(lambda x: truncate_text(x, max_length, method)
                                   if isinstance(x, str) else x)
        output_dfs.append(truncated_df)

    return tuple(output_dfs)


def prepare_dataframe_titles(dfs: Tuple[pd.DataFrame, ...],
                             titles: Tuple[str, ...]) -> Tuple[str, ...]:
    if len(titles) > 0:
        assert_matching_lengths(dfs, titles)
    else:
        titles = tuple(f"Dataframe {i+1}" for i in range(len(dfs)))
    return titles
