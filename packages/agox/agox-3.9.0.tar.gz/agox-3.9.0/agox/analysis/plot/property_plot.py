from typing import List, Union

import numpy as np
from matplotlib.axes import Axes

from agox.analysis.property import Property
from agox.analysis.search_data import SearchCollection, SearchData


class PropertyPlotter:
    def __init__(self, searches: Union[SearchCollection, List[SearchData]], search_property: Property) -> None:
        """
        Plot an analysis property versus time for a list of searches. The property
        should be a scalar property, e.g. one number pr. iteration/time-step of a search.
        """
        self.searches = searches
        self.search_property = search_property

    def plot(self, ax: Axes) -> None:
        for search in self.searches:
            self.plot_search(ax, search)

        ax.set_xlim(0, None)
        ax.legend()

    def plot_search(self, ax: Axes, search: SearchData) -> None:
        # Gather stuff
        prop = self.search_property(search)
        values = prop.data
        time = prop.axis[1]
        min_energies = np.minimum.accumulate(values, axis=1)

        # Plot - mean
        (l1,) = ax.plot(time[0], values.mean(axis=0), linestyle="--", label=f"{search.get_label()}")
        (l2,) = ax.plot(time[0], min_energies.min(axis=0), color=l1.get_color())

        # Spread:
        values_max = values.max(axis=0)
        values_min = values.min(axis=0)

        ax.fill_between(time[0], values_max, values_min, alpha=0.2, color=l1.get_color())

        ax.set_xlabel(f"{prop.shape[1]}")
        ax.set_ylabel(f"{prop.name}")
