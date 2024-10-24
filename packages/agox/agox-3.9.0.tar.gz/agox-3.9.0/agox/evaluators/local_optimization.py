import traceback
from uuid import uuid4

import numpy as np
from ase.calculators.singlepoint import SinglePointCalculator
from ase.constraints import FixAtoms
from ase.optimize.bfgs import BFGS


from .ABC_evaluator import EvaluatorBaseClass


class LocalOptimizationEvaluator(EvaluatorBaseClass):
    """
    Evaluator that performs a local optimization of a candidate using a ASE BFGS optimizer.

    Parameters:
    -----------
    calculator: ASE calculator
        The calculator to use for the evaluation.
    optimizer: ASE optimizer, optional
        The optimizer to use for the local optimization. Default is BFGS.
    optimizer_run_kwargs: dict, optional
        The keyword arguments to pass to the optimizer.run() method.
    optimizer_kwargs: dict, optional
        The keyword arguments to pass to the optimizer constructor.
    fix_template: bool, optional
        Whether to fix the template atoms during the optimization. Default is True.
    constraints: list, optional
        List of constraints to apply during the optimization.
    store_trajectory: bool, optional
        Whether to store the trajectory of the optimization. Default is True.
        If False only the last step is stored.
    """

    name = "LocalOptimizationEvaluator"

    def __init__(
        self,
        calculator,
        optimizer=BFGS,
        optimizer_run_kwargs={"fmax": 0.25, "steps": 200},
        optimizer_kwargs={"logfile": None},
        fix_template=True,
        constraints=[],
        store_trajectory=True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.calculator = calculator
        self.store_trajectory = store_trajectory

        # Optimizer stuff:
        self.optimizer = optimizer
        self.optimizer_kwargs = optimizer_kwargs
        self.optimizer_run_kwargs = optimizer_run_kwargs

        # Constraints:
        self.constraints = constraints
        self.fix_template = fix_template

        if self.name == "LocalOptimizationEvaluator":
            if optimizer_run_kwargs["steps"] == 0:
                print(
                    f"{self.name}: Running with steps = 0 is equivalent to SinglePointEvaluator, consider using that instead to simplify your runscript."
                )
                self.store_trajectory = False

    def evaluate_candidate(self, candidate):
        candidate.calc = self.calculator

        try:
            if self.optimizer_run_kwargs["steps"] > 0:
                self.apply_constraints(candidate)
                optimizer = self.optimizer(candidate, **self.optimizer_kwargs)

                # The observer here stores all the steps if 'store_trajectory' is True.
                optimizer.attach(self._observer, interval=1, candidate=candidate, steps=optimizer.get_number_of_steps)

                optimizer.run(**self.optimizer_run_kwargs)
                candidate.add_meta_information("relax_index", optimizer.get_number_of_steps())

                # If 'store_trajectory' is False we manually store the last step.
                if not self.store_trajectory:
                    self.evaluated_candidates.append(candidate)
            else:
                F = candidate.get_forces(apply_constraint=False)
                E = candidate.get_potential_energy(apply_constraint=False)
                self.evaluated_candidates.append(candidate)

        except Exception as e:
            self.writer("Energy calculation failed with exception: {}".format(e))
            traceback.print_exc()
            return False

        E = candidate.get_potential_energy(apply_constraint=False)
        F = candidate.get_forces(apply_constraint=False)
        self.writer(f"Final energy of candidate = {E:5.3f}")
        calc = SinglePointCalculator(candidate, energy=E, forces=F)
        candidate.calc = calc

        return True

    def _observer(self, candidate, steps):
        E = candidate.get_potential_energy(apply_constraint=False)
        F = candidate.get_forces(apply_constraint=False)

        traj_candidate = candidate.copy()
        calc = SinglePointCalculator(traj_candidate, energy=E, forces=F)
        traj_candidate.set_calculator(calc)
        traj_candidate.add_meta_information("relax_index", steps())
        traj_candidate.add_meta_information("final", False)
        if steps() > 0:
            traj_candidate.add_meta_information("uuid", str(uuid4()))
        self.writer(f"Step {steps()}: {E:.3f}")

        if self.store_trajectory:
            self.evaluated_candidates.append(traj_candidate)

        # self.add_to_cache(self.set_key, [traj_candidate], mode='a')

    def apply_constraints(self, candidate):
        constraints = [] + self.constraints
        if self.fix_template:
            constraints.append(self.get_template_constraint(candidate))

        for constraint in constraints:
            if hasattr(constraint, "reset"):
                constraint.reset()

        candidate.set_constraint(constraints)

    def get_template_constraint(self, candidate):
        return FixAtoms(indices=np.arange(len(candidate.template)))
