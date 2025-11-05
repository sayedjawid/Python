import matplotlib.pyplot as plt
import pandas as pd

def _cat_for_plot(s, missing_label='missing'):
    if hasattr(s, 'astype'):
        s = s.astype('object')
    try:

        return s.fillna(missing_label)
    except Exception:
        return s

def _num_for_plot(s):
    try:
        return pd.to_numeric(s, errors='coerce').fillna(0)
    except Exception:
        return s 


def bar(ax, x, y, title, xlabel, ylabel, grid:bool=True):
    """Ritar ett stapeldiagram på ax-objektet"""
    x = _cat_for_plot(x)
    y = _num_for_plot(y)
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)   
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis='y')

    return ax


def line(ax, x, y, title, xlabel, ylabel, grid:bool=True):
    """Ritar ett stapeldiagram på ax-objektet"""
    
    y = _num_for_plot(y)
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)   
    ax.set_ylabel(ylabel)
    ax.grid(grid)

    return ax


def box_h(ax, values, title, xlabel, grid:bool=True):
    """Ritar ett stapeldiagram på ax-objektet"""
    values = _num_for_plot(values)
    ax.boxplot(values, vert=False)
    ax.set_title(title)
    ax.set_xlabel(xlabel)   
    ax.grid(grid, axis='x')

    return ax


