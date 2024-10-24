import numpy as np
from ase import Atoms
from ase.atoms import symbols2numbers
from ase.symbols import Symbols

from agox.environments.ABC_environment import EnvironmentBaseClass


class Environment(EnvironmentBaseClass):
    """
    Environment class for the generation of candidates with a single stoichoimetry.

    Parameters
    ----------
    template : Atoms
        The template structure to use.
    numbers : list, optional
        List of atomic numbers to add to the template, by default None.
    symbols : list, optional
        List of atomic symbols to add to the template, by default None.
    print_report : bool, optional
        If True, a report is printed, by default True.

    """

    def __init__(self, template, numbers=None, symbols=None, print_report=True, **kwargs):
        super().__init__(**kwargs)

        # Both numbers and symbols cannot be specified:
        assert (numbers is not None) is not (symbols is not None)  # XOR

        if numbers is not None:
            self._numbers = numbers
        elif symbols is not None:
            self._numbers = symbols2numbers(symbols)

        if type(template) is Atoms:
            template = self.convert_to_candidate_object(template)
        self._template = template

        if self.confinement_cell is None:
            self.confinement_cell = self._template.get_cell()
            self.confinement_corner = np.array([0, 0, 0])

        if print_report:
            self.environment_report()

    def get_template(self):
        return self._template.copy()

    def set_template(self, template):
        self._template = template

    def set_numbers(self, numbers):
        self._numbers = numbers

    def get_numbers(self):
        return self._numbers.copy()

    def get_missing_types(self):
        return np.sort(np.unique(self.get_numbers()))

    def get_all_types(self):
        return list(set(list(self._template.numbers) + list(self.get_numbers())))

    def get_identifier(self):
        return self.__hash__()

    def get_missing_indices(self):
        return np.arange(len(self._template), len(self._template) + len(self._numbers))

    def get_all_numbers(self):
        all_numbers = np.append(self.get_numbers(), self._template.get_atomic_numbers())
        return all_numbers

    def get_all_species(self):
        return list(Symbols(self.get_all_types()).species())

    def get_species(self):
        return list(np.unique(self.get_all_species()))

    def get_atoms(self):
        atoms = self.get_template()
        atoms += Atoms(self.get_numbers())
        return atoms

    def match(self, candidate):
        cand_numbers = candidate.get_atomic_numbers()
        env_numbers = self.get_all_numbers()

        stoi_match = (
            np.sort(cand_numbers) == np.sort(env_numbers)
        ).all()  # Not very efficient, but does it matter? Should pobably only use this function for debugging.
        template_match = (candidate.positions[0 : len(candidate.template)] == self._template.positions).all()
        return stoi_match * template_match

    def __hash__(self):
        feature = (
            tuple(self.get_numbers())
            + tuple(self._template.get_atomic_numbers())
            + tuple(self._template.get_positions().flatten().tolist())
        )
        return hash(feature)

    def environment_report(self) -> None:
        self.writer.write_panel(str(self), "Environment report")

    def __str__(self) -> str:
        string = ""
        tab = "    "
        string += "Atoms in search:\n"

        missing_numbers = self.get_numbers()
        for number in np.unique(missing_numbers):
            symbols_object = Symbols([number])
            specie = symbols_object.species().pop()
            count = np.count_nonzero(missing_numbers == number)
            string += f"{tab}{specie} = {count}\n"

        total_symbols = Symbols(self.get_all_numbers())
        string += f"Template formula: {self._template.get_chemical_formula()}\n"
        string += f"Full formula: {total_symbols.get_chemical_formula()}\n"

        string += "Cell:\n"
        for cell_vec in self._template.get_cell():
            string += tab + "{:4.2f} {:4.2f} {:4.2f}\n".format(*cell_vec)
        
        string += "Periodicity:\n"
        string += tab + "{} {} {}\n".format(*self._template.pbc)

        string += f"Box constraint: {self.use_box_constraint}\n"
        
        if self.use_box_constraint:
            assert self.confinement_cell is not None
            assert self.confinement_corner is not None
            string += "Confinement corner\n"
            string += tab + "{:4.2f} {:4.2f} {:4.2f}\n".format(*self.confinement_corner)
            string += "Confinement cell:\n"
            for i, cell_vec in enumerate(self.confinement_cell):
                string += tab + "{:4.2f} {:4.2f} {:4.2f}".format(*cell_vec)
                if i != 2:
                    string += "\n"
        return string
        

