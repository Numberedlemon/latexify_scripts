"""
File: plot_2d.py

Author: James Hunt
Date and Time Created: 4/16/2024 @ 8:44 PM BST

Description: This module contains a function to create a 2D plot in a consistent style using matplotlib.

Requirements:
    - matplotlib (3.8.3 or later)
    
Function: plot_2d
    Description: Creates a 2D plot of one or more arrays in a consistent style.
    Parameters:
        - x (numpy.Array): Array for the x-axis of the plot.
        - y (list, numpy.Array): list of arrays for plotting against the x-axis. Can be one array or many.
        - x_label (str): String for the x-axis label.
        - y_label (str): String for the y-axis label.
        - title (str): Optional. Title of the plot. Defaults to an empty string.
        - x_units (str): Optional. Units of the x-axis. Defaults to an empty string.
        - y_units (str): Optional. Units of the y-axis. Defaults to an empty string.
        - save_fig (bool): Optional. Save the figure? Defaults to False
        - show_fig (bool): Optional. Show the figure in a matplotlib window? Defaults to False.
        - file_path (str): Optional. If save_fig is True, this is the relative folder to save the file to. Defaults to the current working directory.
        - file_name (str): Optional. If save_fig is True, this is the file name. Defaults to "output.pdf"
        - use_latex (bool): Optional. Use LaTeX rendering for units to show properly? Defaults to False.

Returns:
    - If show_fig is True, a matplotlib plot Object. If show_fig is false, none.

Last edited by: James Hunt
Last edited on: 4/16/2024 @ 8:44 PM BST

Changelog:
    > 4/16/2024 @ 8:44 PM BST [James Hunt]: Created plot_2d.py

"""

import matplotlib.pyplot as plt

def plot_2d(x, y, x_label, y_label, title = "", x_units = "", y_units = "", save_fig = False, show_fig = False, file_path = ".", file_name = "output.pdf", use_latex = False):
    """Generates a 2D plot of n arrays using matplotlib using a consistent style.

    Args:
        - x (numpy.Array): Array for the x-axis of the plot.
        - y (list, numpy.Array): list of arrays for plotting against the x-axis. Can be one array or many.
        - x_label (str): String for the x-axis label.
        - y_label (str): String for the y-axis label.
        - title (str): Optional. Title of the plot. Defaults to an empty string.
        - x_units (str): Optional. Units of the x-axis. Defaults to an empty string.
        - y_units (str): Optional. Units of the y-axis. Defaults to an empty string.
        - save_fig (bool): Optional. Save the figure? Defaults to False
        - show_fig (bool): Optional. Show the figure in a matplotlib window? Defaults to False.
        - file_path (str): Optional. If save_fig is True, this is the relative folder to save the file to. Defaults to the current working directory.
        - file_name (str): Optional. If save_fig is True, this is the file name. Defaults to "output.pdf"
        - use_latex (bool): Optional. Use LaTeX rendering for units to show properly? Defaults to False.
    """
    
    if use_latex == True:
        plt.rcParams.update({
        "text.usetex": True
        })
    
    full_path = "/".join([file_path, file_name])
    
    plt.figure()
    
    if x_units:
        plt.xlabel(x_label + r" [$\mathrm{x_units}$]")
    else:
        plt.xlabel(x_label)
        
    if y_units:
        plt.ylabel(y_label + r" [$\mathrm{y_units}$]")
    else:
        plt.ylabel(y_label)
    
    if title: 
        plt.title(title)
    
    for y_i in y:
        plt.scatter(x,y_i)
    
    if show_fig != False:
        plt.show()
    else:
        pass
    
    if save_fig != False:
        save_fig(full_path, format = "pdf")
    else:
        pass