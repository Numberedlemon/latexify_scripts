"""
File: latexify_table.py

Author: James Hunt
Date and Time Created: 4/16/2024 @ 5:20 PM BST

Description: This module contains a function to convert a pandas DataFrame into a LaTeX table.

Function: latexify_table
    Description: Converts a pandas DataFrame into a LaTeX table format.
    Parameters:
        - df (pandas.DataFrame): The DataFrame to be converted.
        - filename (str): Optional. The filename to save the LaTeX table. If not provided, the table will be printed.
        - caption (str): Optional. The caption for the LaTeX table.
        - label (str): Optional. The label for referencing the table in LaTeX.
        - **kwargs: Additional keyword arguments to be passed to DataFrame.to_latex().

Returns:
    - If filename is provided, None. Otherwise, returns the LaTeX table as a string.

Last edited by: James Hunt
Last edited on: 4/16/2024 @ 5:29 PM BST

Changelog:
    > 4/16/2024 @ 5:29 PM BST [James Hunt]: Created latexify_table.py
"""

def latexify_table(df,label,caption,file_path = "./", **kwargs):
    """
    Generates a LaTeX2e .tex file containing a tabulated DataFrame. Supports labelling, captioning, and custom filepaths for export.

    Args:
        Parameters:
        - df (pandas.DataFrame): The DataFrame to be converted.
        - file_path (str): Optional. The file path to save the LaTeX table. This must be a folder, and not a file. If not provided, defaults to "./output.tex". 
        - caption (str): Optional. The caption for the LaTeX table.
        - label (str): Optional. The label for referencing the table in LaTeX.
        - **kwargs: Additional keyword arguments to be passed to DataFrame.to_latex().
    """
    
    column_format = 'p{1.7cm}' * len(df.columns)
    
    latex_table = df.to_latex(df, label = label, caption = caption, column_format = column_format, **kwargs)
    
    with open(file_path + "/output.tex", 'w') as f:
        f.write(latex_table)
    
        f.close()