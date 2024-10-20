"""


"""

from typing import Tuple, Union

import pandas as pd
from IPython.core.display import display, HTML
from io import StringIO

from dfhelper.package_utils.utils_assert import (assert_dfs_nonempty,
                                                 validate_choice)
from dfhelper.package_utils.utils_transform_df import (truncate_dataframe_text,
                                                       prepare_dataframe_titles)


def df_view(*dfs: pd.DataFrame,
            titles: Tuple = (),
            number_rows: int = 5,
            display_all_lines: bool = False,
            orientation: str = 'vert',
            truncate_text: bool = False,
            method_truncate_text_col: Union[str, None] = None,
            max_length_text_col: int = 50,
            show_titles: bool = True,
            title_alignment: str = 'left') -> None:
    """
    Displays multiple pandas DataFrames as HTML tables in a Jupyter Notebook with several customizable options.

    This function allows you to render one or more pandas DataFrames in Jupyter Notebooks. You can specify
    titles for each DataFrame, control the number of rows displayed, choose the orientation, and truncate
    text within the DataFrame columns if needed.

    Parameters:
    dfs (*dfs: pd.DataFrame): One or more pandas DataFrames to be displayed.
    titles (Tuple): An optional tuple for titles corresponding to each DataFrame. If not provided, default
                    titles like "Dataframe 1", "Dataframe 2", etc., are generated.
    number_rows (int): Number of rows to display for each DataFrame. Defaults to 5. Ignored if display_all_lines is True
    display_all_lines (bool): If True, all rows of each DataFrame are displayed, overriding number_rows.
                              Defaults to False.
    orientation (str): Layout orientation of the DataFrames ('vert' for vertical, 'hor' for horizontal).
                       Defaults to 'vert'.
    truncate_text (bool): If True, text in DataFrame columns will be truncated to a specified length. Defaults to True.
    method_truncate_text_col (Union[str, None]): Method for truncating text ('characters' or 'words'). Defaults to None,
                                                 which treats it as 'characters'.
    max_length_text_col (int): Maximum number of characters or words for text before truncation.
                               Defaults to 50 characters.
    show_titles (bool): Controls the display of headings. By default, they are displayed.
    title_alignment (str): Controls the position of the headers. Acceptable values: left, right, center.
                           Defaults to 'left'

    Returns:
    None: Displays the HTML output directly in the Jupyter Notebook.

    Notes:
    - The function performs validation to ensure that DataFrames are not empty.
    - It checks the valid choices for orientation and method of truncation.
    - Internally, it calls a utility function `truncate_dataframe_text` for handling text truncation.

    Example Use:
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({'A': range(5), 'B': range(5, 10)})
    >>> df2 = pd.DataFrame({'X': ['long text data']*5, 'Y': range(15, 20)})
    >>> df_view(df1, df2, titles=('First DataFrame', 'Second DataFrame'), number_rows=3, orientation='hor')
    This will display the first 3 rows of each DataFrame side by side, with titles and truncated text where applicable.
    """
    assert_dfs_nonempty(dfs)
    validate_choice('orientation', ['vert', 'hor'], orientation)
    validate_choice('title_alignment', ['left', 'centr', 'right'], title_alignment)

    titles = prepare_dataframe_titles(dfs, titles)

    if display_all_lines:
        number_rows = max(len(df) for df in dfs)

    if truncate_text:
        validate_choice('method_truncate_text_col',
                        [None, 'characters', 'words'],
                        method_truncate_text_col)
        method_truncate = method_truncate_text_col if method_truncate_text_col else 'characters'
        dfs = truncate_dataframe_text(*dfs, max_length=max_length_text_col, method=method_truncate)

    html_output = []
    for title, df in zip(titles, dfs):
        df_html = df.head(number_rows).to_html()
        if show_titles:
            if title_alignment == 'center':
                html_output.append(f"<h1 style='text-align: center;'>{title}</h1>{df_html}")
            elif title_alignment == 'right':
                html_output.append(f"<h1 style='text-align: right;'>{title}</h1>{df_html}")
            else:
                html_output.append(f"<h1 style='text-align: left;'>{title}</h1>{df_html}")
        else:
            html_output.append(df_html)

    if orientation == 'hor':
        combined_html = "<table><tr>" + "".join(f"<td>{fragment}</td>"
                                                for fragment in html_output) + "</tr></table>"
    else:
        combined_html = "<br><br>".join(html_output)
    display(HTML(combined_html))


def df_info_view(*dfs: pd.DataFrame,
                 titles: Tuple = (),
                 orientation: str = 'hor',
                 show_titles: bool = True,
                 title_alignment: str = 'left',
                 color_line: str = 'green') -> None:
    """
    Displays the info summary of one or more pandas DataFrames in a Jupyter Notebook.

    The function renders DataFrame.info() outputs in an HTML format, allowing for both horizontal
    and vertical layout options for better visualization within notebooks. It supports custom
    titles for each DataFrame's info section and ensures data integrity with input validations.

    Parameters:
    dfs (*dfs: pd.DataFrame): One or more pandas DataFrames whose information you want to display.
        - These are the main data structures that contain data, from which summary information
          will be extracted and displayed.
    titles (Tuple): An optional tuple of strings that provide custom titles for each DataFrame.
        - Titles enhance readability and context for each DataFrame's information displayed.
        - If empty, default titles are generated like "Dataframe 1", "Dataframe 2", etc.
    orientation (str): Specifies the orientation of the displayed DataFrame infos.
        - Acceptable values are 'hor' for horizontal layout and 'vert' for vertical layout.
        - The default orientation is 'hor', which displays DataFrame infos side by side.
        - Orientation affects how the data is visually structured in the output.
    show_titles (bool): Controls the display of headings. By default, they are displayed.
    title_alignment (str): Controls the position of the headers. Acceptable values: left, right, center.
                           Defaults to 'left'
    color_line (str): The color of the dividing line

    Returns:
    None: The function returns no value. Instead, it directly renders HTML content in the Jupyter Notebook cell output.

    Notes:
    - Utilizes helper functions (not shown here) to perform input validation:
        - `assert_dfs_nonempty(dfs)`: Ensures that at least one DataFrame is provided.
        - `validate_choice('orientation', ['vert', 'hor'], orientation)`: Validates that the given orientation is
                                                                          either 'hor' or 'vert'.
        - `assert_matching_lengths(dfs, titles)`: Ensures that if titles are provided, their number
                                                  matches the number of DataFrames.
    - The function captures DataFrame.info() output into a buffer, converting it to a string for HTML formatting.
    - Employs HTML tables and styling to format output, distinguishing info sections clearly with borders and padding.

    Example Use:
    >>> df1 = pd.DataFrame({'A': range(5), 'B': range(5, 10)})
    >>> df2 = pd.DataFrame({'X': range(10, 15), 'Y': range(15, 20)})
    >>> df_info_view(df1, df2, titles=('First DataFrame', 'Second DataFrame'), orientation='vert')
    """
    assert_dfs_nonempty(dfs)
    validate_choice('orientation', ['vert', 'hor'], orientation)

    titles = prepare_dataframe_titles(dfs, titles)

    infos = []
    for title, df in zip(titles, dfs):
        buffer = StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        infos.append((title, info_str))

    html_content = "<table style='border-collapse: collapse;'>"

    if orientation == 'hor':
        html_content += "<tr>"
        for name, info in infos:
            title_html = (f"<h3 style='text-align: {title_alignment};'>{name}</h3>" if show_titles else "")
            html_content += (
                f"<td style='border-left: 1px solid {color_line}; border-right: 1px solid {color_line}; "
                "padding: 10px; vertical-align: top;'>"
                f"{title_html}"
                f"<pre>{info}</pre>"
                "</td>"
            )
        html_content += "</tr>"
    else:  # vertical orientation
        for name, info in infos:
            title_html = (f"<h3 style='text-align: {title_alignment};'>{name}</h3>" if show_titles else "")
            html_content += (
                f"<tr><td style='border-top: 1px solid {color_line}; border-bottom: 1px solid {color_line}; "
                "padding: 10px; vertical-align: top;'>"
                f"{title_html}"
                f"<pre>{info}</pre>"
                "</td></tr>"
            )

    html_content += "</table>"

    display(HTML(html_content))


def df_shape_view(*dfs: pd.DataFrame,
                  titles: Tuple = (),
                  show_titles: bool = True,
                  title_alignment: str = 'left') -> None:
    """Displays the shape (number of rows and columns) of multiple pandas DataFrames.

    This function provides a quick overview of the dimensions of one or more pandas DataFrames.
    Users can specify titles for each DataFrame, which enhances the interpretability of the output.

    Parameters:
    dfs (*dfs: pd.DataFrame): One or more pandas DataFrames whose shapes will be displayed.
    titles (Tuple): An optional tuple for titles corresponding to each DataFrame. If not provided,
                    default titles like "Dataframe 1", "Dataframe 2", etc., are generated.
    show_titles (bool): Controls the display of headings. By default, they are displayed.
    title_alignment (str): Controls the position of the headers. Acceptable values: left, right, center.
                           Defaults to 'left'

    Returns:
    None: Displays the shape information of the DataFrames directly in the Jupyter Notebook.

    Example Use:
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({'A': range(5), 'B': range(5, 10)})
    >>> df2 = pd.DataFrame({'X': ['text']*5, 'Y': range(15, 20)})
    >>> df_shape_view(df1, df2, titles=('First Data Frame', 'Second Data Frame'))
    This will display the shape of each DataFrame with the given titles.

    Notes:
    - Similar to df_view, this function uses the prepare_dataframe_titles helper function to manage titles.
    - It ensures that at least one DataFrame is provided before proceeding.
    """
    assert_dfs_nonempty(dfs)
    titles = prepare_dataframe_titles(dfs, titles)

    dfs_shape = []
    for df in dfs:
        shape = df.shape
        dfs_shape.append(pd.DataFrame({
            'rows': [shape[0]],
            'columns': [shape[1]]
        }))

    df_view(*dfs_shape,
            titles=titles,
            orientation='hor',
            show_titles=show_titles,
            title_alignment=title_alignment)
