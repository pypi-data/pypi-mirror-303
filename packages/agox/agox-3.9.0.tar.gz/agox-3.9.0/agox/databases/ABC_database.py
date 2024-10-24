from abc import ABC, abstractmethod

from ase import Atoms
from ase.calculators.singlepoint import SinglePointCalculator

from agox.observer import Observer, ObserverHandler
from agox.writer import Writer


class DatabaseBaseClass(ABC, ObserverHandler, Observer):
    """
    Base class for all databases.

    Databases are used to store, typically evaluated, candidates.

    Parameters
    ----------
    gets : dict
        Dictionary of get keys, e.g. {'get_key':'evaluated_candidates'}. Used to select
        from which entry in the agox.main.State cache the database should get candidates.
    order : int
        Order of the database, by default 6
    """

    def __init__(
        self,
        gets={"get_key": "evaluated_candidates"},
        sets={},
        order=6,
        surname="",
    ):
        Observer.__init__(self, gets=gets, sets=sets, order=order, surname=surname)
        ObserverHandler.__init__(self, handler_identifier="database", dispatch_method=self.store_in_database)
        self.candidates = []

        self.objects_to_assign = []

        self.add_observer_method(
            self.store_in_database, sets=self.sets[0], gets=self.gets[0], order=self.order[0], handler_identifier="AGOX"
        )

    ########################################################################################
    # Required methods
    ########################################################################################

    @abstractmethod
    def write(self, *args, **kwargs):  # pragma: no cover
        """
        Write stuff to database
        """

    @abstractmethod
    def store_candidate(self, candidate):  # pragma: no cover
        pass

    @abstractmethod
    def get_all_candidates(self):  # pragma: no cover
        pass

    @property
    @abstractmethod
    def name(self):  # pragma: no cover
        return NotImplementedError

    ########################################################################################
    # Default methods
    ########################################################################################

    def __len__(self):
        return len(self.candidates)

    @Observer.observer_method
    def store_in_database(self, state):
        evaluated_candidates = state.get_from_cache(self, self.get_key)
        anything_accepted = False
        for j, candidate in enumerate(evaluated_candidates):
            if candidate:
                self.store_candidate(candidate, accepted=True, write=True)
                anything_accepted = True

            elif candidate is None:
                dummy_candidate = self.candidate_instanstiator(template=Atoms())
                dummy_candidate.set_calculator(SinglePointCalculator(dummy_candidate, energy=float("nan")))

                # This will dispatch to observers if valid data has been added but the last candidate is None.
                self.store_candidate(candidate, accepted=False, write=True)

        if anything_accepted:
            self.dispatch_to_observers(database=self, state=state)
