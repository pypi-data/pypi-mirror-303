from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union

import numpy as np

from agox.analysis.search_data import SearchCollection, SearchData


class PropertyData(ABC):
    def __init__(self, data: Any, name: str) -> None:
        self.data = data
        self.name = name


class ArrayPropertyData(PropertyData):
    def __init__(self, data: np.ndarray, name: str, shape: Tuple[str], array_axis: Tuple[np.ndarray]) -> None:
        """
        Multidimensional array property data.

        E.g. for energy this is a 2D array with shape (Restarts, Iterations) and each entry is the energy of the configuration.

        Parameters
        ----------
        property_name : str
            Name of the property
        property_shape : Tuple[str]
            Shape of the property, e.g ('Restarts', 'Iterations') for a 2D array
        """
        super().__init__(data=data, name=name)
        self.shape = shape
        self.axis = array_axis


class ListPropertyData(PropertyData):
    def __init__(self, data: List[Any], name: str, shape: Tuple[str], list_axis: Tuple[Any]) -> None:
        """
        Parameters
        ----------
        property_name : str
            Name of the property
        """
        super().__init__(data=data, name=name)
        self.shape = shape
        self.axis = list_axis

    def __repr__(self) -> str:
        return f"{self.name}:\n{self.shape}"


class Property(ABC):
    @abstractmethod
    def compute(self, search_data: SearchData) -> PropertyData:
        pass

    def __call__(self, search_data: SearchData) -> PropertyData:
        return self.compute(search_data)

    def get_minimum(self, searches: Union[SearchCollection, List[SearchData]]) -> float:
        min_value = np.inf
        for search in searches:
            prop = self(search)
            if isinstance(prop, ArrayPropertyData):
                min_value = min(min_value, np.nanmin(prop.data))
            else:
                raise ValueError(f"Property {prop} is not an ArrayPropertyData")

        return min_value
