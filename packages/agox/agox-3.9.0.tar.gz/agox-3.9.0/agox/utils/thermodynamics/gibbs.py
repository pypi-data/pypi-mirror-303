import numpy as np

from agox.candidates import StandardCandidate
from agox.utils.thermodynamics import ThermodynamicsData


def gibbs_free_energy(
    candidate: StandardCandidate = None,
    numbers: np.array = None,
    total_energy: float = None,
    thermo_data: ThermodynamicsData = None,
) -> float:
    assert thermo_data is not None, "ThermodynamicsData object must be provided"

    if total_energy is None:
        total_energy = candidate.get_total_energy()
    if numbers is None:
        numbers = candidate.get_search_numbers()

    gibbs_energy = total_energy - thermo_data.template_energy

    for number in np.unique(numbers):
        reference = thermo_data.get_reference(number)
        chemical_potential = thermo_data.get_chemical_potential(number)
        n_atoms = len(np.where(numbers == number)[0])
        gibbs_energy -= n_atoms * (chemical_potential + reference)

    return gibbs_energy
