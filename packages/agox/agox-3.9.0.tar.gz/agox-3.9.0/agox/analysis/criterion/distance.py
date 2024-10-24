from typing import Any, Tuple

import numpy as np
from scipy.spatial.distance import cdist

from agox.analysis.criterion.base_criterion import BaseCriterion
from agox.analysis.property.property import ListPropertyData


class DistanceCriterion(BaseCriterion):
    def __init__(self, threshold: float, comparate: Any) -> None:
        """
        Find the time at which the property first crosses below a threshold.

        Parameters
        ----------
        threshold : float
            Distance threshold to compare against the property data
        comparate : Any
            Data to compare against the property data, of the same type as the objects in property_data.data
        """
        self.threshold = threshold
        self.comparate = comparate

    def compute(self, property_data: ListPropertyData) -> Tuple[np.array, np.array]:
        """
        Parameters
        ----------
        property_data : ListPropertyData
            Property data to be analyzed
        """

        property_data = property_data.data
        times = []
        events = []

        for restart, data in enumerate(property_data):
            property_arr = np.array(data).squeeze().reshape(-1, self.comparate.shape[1])
            distances = cdist(property_arr, self.comparate)
            below_threshold = distances <= self.threshold
            if below_threshold.any():
                indices = np.argwhere(below_threshold).flatten()
                time = indices[0]
                event = 1
            else:
                time = len(property_arr)
                event = 0

            times.append(time)
            events.append(event)

        events = np.array(events)
        times = np.array(times)

        print(f"Distance criterion: {np.sum(events)} events found")
        print(events)

        return times, events
