import matplotlib

matplotlib.use("Agg")

import numpy as np
from ase import Atoms
from ase.optimize import BFGS

from agox import AGOX
from agox.acquisitors import MetaInformationAcquisitor
from agox.collectors import ParallelTemperingCollector
from agox.databases import Database
from agox.environments import Environment
from agox.evaluators import LocalOptimizationEvaluator
from agox.samplers import ParallelTemperingSampler
from agox.postprocessors import ParallelRelaxPostprocess
from agox.generators import RandomGenerator, RattleGenerator
from agox.models.descriptors.fingerprint import Fingerprint
from agox.models.GPR import GPR
from agox.models.GPR.kernels import RBF, Noise
from agox.models.GPR.kernels import Constant as C
from agox.models.GPR.priors import Repulsive
from agox.postprocessors import ParallelRelaxPostprocess
from agox.samplers import ParallelTemperingSampler

seed = 42
database_index = 0

sample_size = 10
rattle_amplitudes = np.linspace(0.1, 5, sample_size)

################################################################################
# Calculator
##############################################################################

from ase.calculators.emt import EMT

calc = EMT()

##############################################################################
# System & general settings:
##############################################################################

db_path = "db{}.db".format(database_index)
database = Database(filename=db_path, order=6)

template = Atoms("", cell=np.eye(3) * 12)
confinement_cell = np.eye(3) * 6
confinement_corner = np.array([3, 3, 3])
environment = Environment(
    template=template,
    symbols="Au12Ni2",
    confinement_cell=confinement_cell,
    confinement_corner=confinement_corner,
)

##############################################################################
# Search Settings:
##############################################################################

# Setup a ML model.
descriptor = Fingerprint(environment=environment)
beta = 0.01
k0 = C(beta, (beta, beta)) * RBF()
k1 = C(1 - beta, (1 - beta, 1 - beta)) * RBF()
kernel = C(5000, (1, 1e5)) * (k0 + k1) + Noise(0.01, (0.01, 0.01))
model = GPR(descriptor=descriptor, kernel=kernel, database=database, prior=Repulsive())

sampler = ParallelTemperingSampler(
    t_min=0.02, t_max=2, swap="down", sample_size=sample_size, order=3, model=model
)


# Setup the generators to be used, as a dictionary
generator_dict = {}
random_generator = RandomGenerator(contiguous=True,**environment.get_confinement())
generator_dict['random'] = random_generator
for i, t in enumerate(sampler.temperatures):
    generator_dict[t] = RattleGenerator(
        **environment.get_confinement(), 
        rattle_amplitude=rattle_amplitudes[i],
        n_rattle=len(environment.get_missing_indices())
        )

collector = ParallelTemperingCollector.from_sampler(
    sampler, environment, rattle_amplitudes)

# Allow the amplitudes to vary over the course of the calculation to normalise acceptance probability
for key, generator in generator_dict.items(): 
    collector.add_generator_update(key,generator,"rattle_amplitude")

# Local optimisation parameters
relaxer = ParallelRelaxPostprocess(
    model=model,
    constraints=environment.get_constraints(),
    optimizer_run_kwargs={"steps": 5, "fmax": 0.1},
    start_relax=0,
    optimizer=BFGS,
    order=2,
)

# With skip function we can choose conditions under which we will skip the evaluation step. 
# In this case, we only perform evaluation if the iteration number is odd.
def skip_function(self, candidate_list): 
    if  self.get_iteration_counter() % 2 != 0: 
        return False
    else: 
        return True

# We select by walker index i.e. those walkers with lowest index are selected first for evaluation.
acquisitor = MetaInformationAcquisitor(
    meta_key="walker_index", order=4, skip_function=skip_function
)

# Each iteration the lowest temperature walker/replica will be evaluated.
evaluator = LocalOptimizationEvaluator(
    calc,
    number_to_evaluate=1,
    optimizer_kwargs={"logfile": None},
    optimizer_run_kwargs={"fmax": 0.05, "steps": 0},
    constraints=environment.get_constraints(),
    order=5,
)

agox = AGOX(
    collector,
    relaxer,
    sampler,
    acquisitor,
    evaluator,
    database,
    seed=seed,
)

# ##############################################################################
# # Lets get the show running!
# ##############################################################################

agox.run(N_iterations=10)
