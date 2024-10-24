import numpy as np

from agox.analysis.search_data import SearchData

from .property import ArrayPropertyData, Property


class EnergyProperty(Property):
    def __init__(self, time_axis: np.ndarray = None) -> None:
        """
        Get the energy of the system as a np.array of shape [restarts, iterations].
        """
        if time_axis is None:
            time_axis = "indices"

        if time_axis not in ["indices", "iterations"]:
            raise ValueError("time_axis must be one of ['indices', 'iterations']")

        self.time_axis = time_axis

    def compute(self, search_data: SearchData) -> np.array:
        """
        Get the energy of the system as a np.array of shape [restarts, iterations].
        """

        if self.time_axis == "indices":
            indices = search_data.get_all("indices", fill=np.nan)
        elif self.time_axis == "iterations":
            indices = search_data.get_all("iterations", fill=np.nan)

        energy = ArrayPropertyData(
            data=search_data.get_all("energies", fill=np.nan),
            name="Energy",
            shape=("Restarts", self.time_axis.capitalize()),
            array_axis=(search_data.get_all_identifiers(), indices),
        )

        return energy
