"""
Visualization tools for the ``tsc`` module.
"""

try:
    import matplotlib.pyplot as plt
    from matplotlib.axis import Axis
    from matplotlib.figure import Figure
except ImportError as ie:  # pragma: no cover
    raise ImportError(
        "matplotlib not installed, but can be installed by running "
        "`pip install topological-signal-compression[extras]`"
    ) from ie
from typing import Optional, Tuple

import pandas as pd


def plot_persistence(
    pers_data: pd.DataFrame,
    bounds: Optional[Tuple[float, float]] = None,
    title: str = "Persistence Diagram",
    figsize: Tuple[float, float] = (6, 6),
    fig: Optional[Figure] = None,
    ax: Optional[Axis] = None,
    birth_death_line_kwargs: Optional[dict] = None,
    **scatter_kwargs,
) -> Tuple[Figure, Axis]:
    """
    Plot persistence diagram, as output by :py:func:`~tsc.__init__.signal_persistence()`, in ``matplotlib``.

    :param pers_data: dataframe of persistence information.
    :param bounds: (min, max) range for *both* x and y for final figure. Default ``None`` will infer shape by
        range of persistence values.
    :param title: title of resulting figure. Default "Persistence Diagram".
    :param figsize: (horizontal, vertical) dimensions of figure. Only called if ``fig`` and ``ax`` are both ``None``.
    :param fig: ``Figure`` instance onto which we will plot. If ``fig`` and ``ax`` are both ``None``, a new figure and
        axis will be created.
    :param ax: ``Axis`` instance onto which we will plot. If ``fig`` and ``ax`` are both ``None``, a new figure and
        axis will be created.
    :param birth_death_line_kwargs: keyword arguments for the ``plt.plot()`` call that plots the birth-death line (e.g.
        the 45 degree line). Default ``None`` just specifies ``c="black"``.
    :param scatter_kwargs: keyword arguments for the ``plt.scatter()`` call that plots the persistence values.
    :return: ``matplotlib`` ``Figure`` and ``Axis`` instance.
    """
    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    elif fig is not None and ax is not None:
        pass
    else:
        raise ValueError("`fig` and `ax` must both be `None` or not `None`")

    # build 45 degree line
    if birth_death_line_kwargs is None:
        birth_death_line_kwargs = {}
    birth_death_line_kwargs.setdefault("c", "black")
    if bounds is not None:
        ax.set_xlim(bounds[0], bounds[1])
        ax.set_ylim(bounds[0], bounds[1])
        ax.plot([0, bounds[1]], [0, bounds[1]], **birth_death_line_kwargs)
    else:
        max_death = pers_data.death.to_numpy().max()
        min_death = min(0, pers_data.death.to_numpy().min())
        min_birth = min(0, pers_data.birth.to_numpy().min())
        min_val = min(min_birth, min_death)
        ax.plot([min_val, max_death], [min_val, max_death], **birth_death_line_kwargs)

    if pers_data.shape[0] != 0:
        ax.scatter(pers_data.birth, pers_data.death, **scatter_kwargs)

    ax.set_xlabel("Birth")
    ax.set_ylabel("Death")

    ax.set_title(title)

    return fig, ax
