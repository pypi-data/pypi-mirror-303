import pickle
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

import numpy as np
from ase import Atoms

from agox.candidates import StandardCandidate
from agox.databases import Database


def read_database(path: Path, database_class: Database) -> List[StandardCandidate]:
    db = database_class(path)
    db.restore_to_memory()
    candidates = db.get_all_candidates()
    return candidates


@dataclass
class RestartData:
    path: Path
    candidates: List[Atoms]
    energies: np.array = None
    indices: np.array = None
    iterations: np.array = None
    identifier: str = None

    def __post_init__(self) -> None:
        self.n_candidates = len(self.candidates)
        self.indices = np.arange(self.n_candidates)
        self.iterations = np.array([candidate.get_meta_information("iteration") for candidate in self.candidates])
        if self.energies is None:
            self.energies = np.array([candidate.get_potential_energy() for candidate in self.candidates])

        if self.identifier is None:
            self.identifier = self.path.stem

    def __len__(self) -> int:
        return self.n_candidates


class SearchData:
    """
    A set of restarts with the same settings.

    Parameters
    ----------
    directory : Path
        The directory where the restarts are located.
    reload : bool
        Whether to reload the restarts from the database files.
    """

    def __init__(
        self, directory: Union[Path, str], reload: bool = False, pickle_name: str = "experiment.pckl", label: str = None
    ) -> None:
        self.directory = Path(directory)
        self.database_class = Database
        self.pickle_name = pickle_name
        self._label = label

        if reload or not (self.directory / self.pickle_name).exists():
            self.get_restarts()
        else:
            self.load()

    def get_label(self) -> str:
        if self._label is None:
            return self.directory.name
        return self._label

    def get_files(self, pattern: str = "*.db") -> List[Path]:
        return list(self.directory.glob(pattern))

    def get_restarts(self) -> List[RestartData]:
        if not hasattr(self, "restarts"):
            files = self.get_files()
            self.restarts = []
            for file in files:
                candidates = read_database(file, self.database_class)
                restart = RestartData(file, candidates)
                self.restarts.append(restart)
            self.save()

        return self.restarts

    def get_number_of_restarts(self) -> int:
        if not hasattr(self, "restarts"):
            self.get_restarts()
        return len(self.get_restarts())

    def get_all_energies(self, fill: Union[float, int, str] = np.nan) -> np.ndarray:
        restarts = self.get_restarts()

        # Determine size of array to return:
        N_restarts = len(restarts)
        N_max = max([len(restart) for restart in restarts])

        # Get all values:
        all_values = np.zeros((N_restarts, N_max))

        for i, restart in enumerate(restarts):
            all_values[i, : len(restart)] = restart.energies.copy()
            all_values[i, len(restart) :] = fill

        return all_values

    def get_all(self, attribute: str, fill: Union[float, int, str] = np.nan) -> np.ndarray:
        restarts = self.get_restarts()

        # Determine size of array to return:
        N_restarts = len(restarts)
        N_max = max([len(restart) for restart in restarts])

        # Get all values:
        all_values = np.zeros((N_restarts, N_max))

        for i, restart in enumerate(restarts):
            all_values[i, : len(restart)] = getattr(restart, attribute).copy()
            all_values[i, len(restart) :] = fill

        return all_values

    def get_all_identifiers(self) -> List[str]:
        return [restart.identifier for restart in self.get_restarts()]

    def get_all_candidates(self) -> List[List[StandardCandidate]]:
        return [restart.candidates for restart in self.get_restarts()]

    def get_candidate(self, restart_index: int, candidate_index: int) -> StandardCandidate:
        return deepcopy(self.get_restarts()[restart_index].candidates[candidate_index])

    def get_best_candidates(self) -> List[StandardCandidate]:
        restarts = self.get_restarts()
        best_candidates = []
        for restart in restarts:
            best_index = np.argmin(restart.energies)
            best_candidates.append(restart.candidates[best_index])
        return best_candidates

    def save(self) -> None:
        with open(self.directory / self.pickle_name, "wb") as f:
            pickle.dump(self.get_restarts(), f)

    def load(self) -> None:
        with open(self.directory / self.pickle_name, "rb") as f:
            self.restarts = pickle.load(f)

    def __str__(self) -> str:
        mu = "\u03bc"
        sigma = "\u03c3"
        smin = "\u2193"
        smax = "\u2191"

        energies = self.get_all("energies")
        iterations = self.get_all("iterations")
        repr_str = f"""SearchData for: {self.directory.resolve()}"""
        repr_str += f"\n\tNumber of restarts: {self.get_number_of_restarts()}"
        repr_str += f"\n\tEnergy: {smin} = {np.nanmin(energies):.3f} {mu} = {np.nanmean(energies):.3f} {smax} = {np.nanmax(energies):.3f} {sigma} = {np.nanstd(energies):.3f}"
        repr_str += f"\n\tNumber of candidates: {len(energies[~np.isnan(energies)])}"
        repr_str += f"\n\tNumber of iterations: {np.nanmean(np.nanmax(iterations, axis=1))}"

        return repr_str


class SearchCollection:
    def __init__(
        self, directories: Optional[List[Union[Path, str]]] = None, reload: bool = False, labels: List[str] = None
    ) -> None:
        """
        Parameters
        ----------
        directories : List[Union[Path, str]]
            List of directories each containing a search.
        """
        self.reload = reload
        self._directories = []
        self._searches = []

        if directories is not None:
            if labels is None:
                labels = [None for _ in directories]

            for directory, label in zip(directories, labels):
                self.add_directory(directory, label=label)

    def add_directory(self, directory: Union[Path, str], label: str = None) -> None:
        """
        Add a directory to the list of directories.

        Parameters
        ----------
        directory : Union[Path, str]
            Directory containing a search.
        """
        if isinstance(directory, str):
            directory = Path(directory)
        elif isinstance(directory, Path):
            pass
        else:
            raise TypeError(f"Directory must be a Path or a string but is {type(directory)}.")
        self._directories.append(directory)
        self._searches.append(SearchData(directory, reload=self.reload, label=label))

    def get_searches(self) -> List[SearchData]:
        """
        Load searches from the directories.

        Returns
        -------
        List[Search]
            List of searches.
        """
        return self._searches

    def __iter__(self):  # noqa
        self.index = 0
        return self

    def __next__(self):  # noqa
        try:
            output = self._searches[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return output

    def __getitem__(self, index: int) -> SearchData:
        return self._searches[index]

    def __len__(self):
        return len(self._searches)
