import os
from importlib.resources import files

import numpy as np
import pytest
from ase.io import read

from agox.candidates import StandardCandidate
from agox.environments.environment import Environment

from typing import Tuple, List


def pytest_addoption(parser):
    parser.addoption("--rtol", type=float, default=1e-05)
    parser.addoption("--atol", type=float, default=1e-08)
    parser.addoption("--create_mode", default=False, action="store_true")


@pytest.fixture
def cmd_options(request):
    return {
        "tolerance": {"rtol": request.config.getoption("rtol"), "atol": request.config.getoption("atol")},
        "create_mode": request.config.getoption("create_mode"),
    }


@pytest.fixture(scope="module", autouse=True)
def ray_fix():
    import ray
    from agox.utils.ray import reset_ray_pool

    if ray.is_initialized():
        reset_ray_pool()
    yield


def pytest_sessionstart(session):
    from agox.utils.ray import ray_startup

    ray_startup(cpu_count=2, memory=None, tmp_dir=None, include_dashboard=False, max_grace_period=0.0)


test_folder_path = os.path.join(files("agox"), "test/")
test_data_dicts = [
    {"path": "datasets/AgO-dataset.traj", "remove": 6, "name": "AgO"},
    {"path": "datasets/B12-dataset.traj", "remove": 12, "name": "B12"},
    {"path": "datasets/C30-dataset.traj", "remove": 30, "name": "C30"},
]

for dictionary in test_data_dicts:
    dictionary['path'] = os.path.join(test_folder_path, dictionary['path'])

@pytest.fixture(params=test_data_dicts)
def environment_and_dataset(request: pytest.FixtureRequest) -> Tuple[Environment, List[StandardCandidate]]:
    atoms = read(request.param["path"])
    cell = atoms.get_cell()
    corner = np.array([0, 0, 0])
    remove = request.param["remove"]
    numbers = atoms.get_atomic_numbers()[len(atoms) - remove :]

    template = read(request.param["path"])
    del template[len(template) - remove : len(template)]
    environment = Environment(template=template, numbers=numbers, confinement_cell=cell, confinement_corner=corner)

    data = read(request.param["path"], ":")
    candidates = [StandardCandidate.from_atoms(template, a) for a in data]

    return environment, candidates
