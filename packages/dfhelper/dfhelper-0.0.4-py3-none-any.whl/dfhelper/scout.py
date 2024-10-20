"""

"""

from typing import Tuple
import pandas as pd

from dfhelper.package_utils.utils_assert import (assert_dfs_nonempty,
                                                 validate_choice)
from dfhelper.package_utils.utils_transform_df import prepare_dataframe_titles
from dfhelper.viz import df_view


def summarize_df(df: pd.DataFrame):
    """
    Generates a summary report for a given DataFrame.

    This function computes various statistics for each column in the input DataFrame,
    including missing values, zeros, duplicates, and unique values. It also calculates
    the percentage of these values relative to the total number of rows in the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.

    Returns:
    pd.DataFrame: A summary DataFrame containing statistics for each column.
                  The summary includes:
                  - Column name
                  - Column type
                  - Total rows
                  - Missing Values and their percentage
                  - Zero Values and their percentage
                  - Duplicate Values within the column and their percentage
                  - Complete Duplicate Rows across all columns and their percentage
                  - Unique Values count
    """
    analysis_data = []
    total_rows = len(df)
    complete_duplicate_count = df.duplicated().sum()

    for col in df.columns:
        missing_count = df[col].isnull().sum()
        zero_count = (df[col] == 0).sum()
        duplicate_count = df[col].duplicated().sum()
        unique_count = df[col].nunique()

        analysis_data.append({
            'Column name': col,
            'Column type': df[col].dtype,
            'Total rows': total_rows,
            'Missing Values': missing_count,
            'Missing %': (missing_count / total_rows) * 100,
            'Zero Values': zero_count,
            'Zero %': (zero_count / total_rows) * 100,
            'Duplicate Values': duplicate_count,
            'Duplicate %': (duplicate_count / total_rows) * 100,
            'Complete Duplicate Rows': complete_duplicate_count,
            'Complete Duplicate Rows %': (complete_duplicate_count / total_rows) * 100,
            'Unique Values': unique_count,
        })

    analysis_df = pd.DataFrame(analysis_data,
                               columns=['Column name', 'Column type', 'Total rows',
                                        'Missing Values', 'Missing %',
                                        'Zero Values', 'Zero %',
                                        'Duplicate Values', 'Duplicate %',
                                        'Complete Duplicate Rows', 'Complete Duplicate Rows %',
                                        'Unique Values'])

    return analysis_df


def summarize_dfs(*dfs: pd.DataFrame,
                  titles: Tuple = (),
                  display_html: bool = True,
                  orientation: str = 'vert',
                  show_titles: bool = True,
                  title_alignment: str = 'left') -> Tuple[pd.DataFrame, ...]:
    """Analyzes and summarizes multiple DataFrames, optionally displaying the results in HTML format.

    This function takes one or more DataFrames and performs a summary analysis on each of them,
    including statistics for missing values, zero counts, duplicates, and unique values.
    The results can be displayed in HTML format with specified orientation and titles.

    Parameters:
    dfs (pd.DataFrame): One or more pandas DataFrames to be summarized.
    titles (Tuple): Optional titles for each DataFrame when displayed in HTML. Defaults to an empty tuple.
    display_html (bool): Whether to display the summary in HTML format with the specified orientation. Defaults to True.
    orientation (str): Orientation of the HTML display, either 'vert' for vertical or 'hor' for horizontal.
                       Defaults to 'vert'.
    show_titles (bool): Controls the display of headings. By default, they are displayed.
    title_alignment (str): Controls the position of the headers. Acceptable values: left, right, center.
                           Defaults to 'left'

    Returns:
    Tuple[pd.DataFrame, ...]: A tuple of pandas DataFrames, each containing the summary statistics
                              of the input DataFrames.
                              The summary includes:
                              - Column name
                              - Column type
                              - Total rows
                              - Missing Values and their percentage
                              - Zero Values and their percentage
                              - Duplicate Values within the column and their percentage
                              - Complete Duplicate Rows across all columns and their percentage
                              - Unique Values count"""
    assert_dfs_nonempty(dfs)
    titles = prepare_dataframe_titles(dfs, titles)
    validate_choice('orientation', ['vert', 'hor'], orientation)

    dfs = [summarize_df(df) for df in dfs]

    if display_html:
        df_view(*dfs,
                titles=titles,
                orientation=orientation,
                show_titles=show_titles,
                title_alignment=title_alignment)

    return tuple(dfs)
