import json
from pathlib import Path
from typing import Dict, Union

import numpy as np
from ase.data import atomic_numbers

symbols = {n: s for s, n in atomic_numbers.items()}


class ThermodynamicsData:
    def __init__(self, references: Dict, chemical_potentials: Dict, template_energy: float = 0.0):
        self.references = references
        self.chemical_potentials = chemical_potentials
        self.template_energy = template_energy

    def set_chemical_potential(self, element: Union[str, int], value: float):
        element = self.convert_number_to_element(element)
        self.chemical_potentials[element] = value

    def get_chemical_potential(self, element: Union[str, int]) -> float:
        element = self.convert_number_to_element(element)
        return self.chemical_potentials[element]

    def set_reference(self, element: str, value: float):
        element = self.convert_number_to_element(element)
        self.references[element] = value

    def get_reference(self, element: Union[str, int]) -> float:
        element = self.convert_number_to_element(element)
        return self.references[element]

    def convert_number_to_element(self, element: Union[int, str]):
        if isinstance(element, (int, np.int64)):
            return symbols[element]
        return element

    @classmethod
    def from_file(cls, path: Union[str, Path]):
        if isinstance(path, str):
            path = Path(path)

        if not path.exists():
            raise FileNotFoundError(f"{path} does not exist")

        with open(path, "r") as f:
            data = json.load(f)

        return cls(
            references=data["references"],
            chemical_potentials=data["chemical_potentials"],
            template_energy=data.get("template_energy", 0.0),
        )

    def save(self, path: Union[str, Path]):
        if isinstance(path, str):
            path = Path(path)

        data = {
            "references": self.references,
            "chemical_potentials": self.chemical_potentials,
            "template_energy": self.template_energy,
        }

        if not path.exists():
            with open(path, "w") as f:
                json.dump(data, f, indent=4)
        else:
            raise FileExistsError(f"{path} already exists")
