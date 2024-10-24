import numpy as np
import ray

from agox.collectors.ABC_collector import CollectorBaseClass
from agox.samplers.fixed_sampler import FixedSampler
from agox.utils.ray import RayPoolUser


def remote_generate(generator, sampler, environment):
    return generator(sampler, environment)


class ParallelTemperingCollector(CollectorBaseClass, RayPoolUser):
    name = "ParallelTemperingCollector"

    """
    Parameters
    ----------
    num_candidates : dict or list
        If dict, it must have the form {0: [], 500: []} where the keys are the iteration numbers
        and the values are the number of candidates to generate for that iteration.
        If a list it must provide the number of candidates for each generator used. 
    """

    def __init__(self, generator_dict, **kwargs):
        # Get the kwargs that are relevant for RayPoolUser
        RayPoolUser.__init__(self)
        self.dynamic_generators = {}
        # Get all the generators from the generator_dict
        unique_generators = []
        for generator in generator_dict.values():
            if generator not in unique_generators:
                unique_generators.append(generator)

        # Figure out which unique generator each generator in the generator_dict corresponds to.
        self.mapping = {}
        for key, generator in generator_dict.items():
            self.mapping[key] = unique_generators.index(generator)

        # Give the rest to the CollectorBaseClass.
        CollectorBaseClass.__init__(self, unique_generators, **kwargs)

        self.generator_keys = []
        for generator in self.generators:
            key = self.pool_add_module(generator)
            self.generator_keys.append(key)

    def make_candidates(self):
        if len(self.dynamic_generators) != 0:
            self.update_generators()
        # We need to build the args and kwargs sent to the actors.

        # If sampler is empty and initialized, then use fallback generator
        if len(self.sampler) == 0 and self.sampler.initialized:
            number_of_candidates = self.get_number_of_candidates()
            fallback_generator = self.get_fallback_generator()
            generator_id = self.pool_add_module(fallback_generator)
            modules = [[generator_id]] * np.sum(number_of_candidates)
        else:
            if self.get_iteration_counter() == 1 or self.get_iteration_counter() is None:
                random_key = self.mapping["random"]
                modules = [[self.generator_keys[random_key]]] * self.sampler.sample_size
            else:
                # This specifies which module each actor of the pool will use.
                modules = []
                for temperature in self.sampler.temperatures:
                    modules += [[self.get_generator_key(temperature)]]

        environment_id = ray.put(self.environment)
        fixed_samplers = self.get_dummy_samplers()
        if len(fixed_samplers) == 0:
            sampler_ids = [ray.put(self.sampler)] * self.sampler.sample_size
        else:
            sampler_ids = [ray.put(sampler) for sampler in fixed_samplers]

        # The args and kwargs passed to the function - in this case the remote_generate
        # function defined above.
        args = [[sampler_id, environment_id] for sampler_id in sampler_ids]
        # kwargs = [{}] * np.sum(number_of_candidates)
        kwargs = [{} for _ in range(np.sum(self.sampler.sample_size))]

        # Generate in parallel using the pool.
        candidates = self.pool_map(remote_generate, modules, args, kwargs)

        # Flatten the output which is a list of lists.
        flat_candidates = []
        for cand_list in candidates:
            for cand in cand_list:
                flat_candidates.append(cand.copy())

        for i, cand in enumerate(flat_candidates):
            cand.add_meta_information("walker_index", i)

        return flat_candidates

    def get_dummy_samplers(self):
        sample = self.sampler.get_all_members()
        samplers = []
        for member in sample:
            sampler = FixedSampler(member)
            samplers.append(sampler)
        return samplers

    def get_number_of_candidates(self):
        return [self.sampler.sample_size]

    @classmethod
    def from_sampler(
        cls, sampler, environment, amplitudes, generator_dict=None, random_generator_kwargs=None, **kwargs
    ):
        from agox.generators import RandomGenerator, RattleGenerator

        # Generators to produce candidates structures

        if not len(amplitudes) == len(sampler.temperatures):
            raise ValueError("The number of amplitudes must match the number of temperatures in the sampler.")
        # Dict specificies how many candidates are created with and the dict-keys are iterations.
        N_atoms = len(environment.get_missing_indices())

        default_dict = {}
        if random_generator_kwargs is None:
            random_generator_kwargs = {}
        random_generator = RandomGenerator(**environment.get_confinement(), **random_generator_kwargs)
        default_dict["random"] = random_generator
        for i, t in enumerate(sampler.temperatures):
            default_dict[t] = RattleGenerator(
                **environment.get_confinement(), rattle_amplitude=amplitudes[i], n_rattle=N_atoms
            )
        if generator_dict is None:
            generator_dict = default_dict.copy()

        for key in default_dict.keys():
            if key not in generator_dict.keys():
                generator_dict[key] = default_dict[key]

        return cls(generator_dict, sampler=sampler, environment=environment, order=1, **kwargs)

    def add_generator_update(self, key, generator, attribute, correlated=False, min=0.5, max=1.5):
        if hasattr(generator, attribute):
            generator.add_dynamic_attribute(attribute)
            self.dynamic_generators[key] = (attribute, correlated, [min * key, max * key])

    def update_generators(self):
        for i, temperature in enumerate(self.sampler.temperatures):
            generator = self.get_generator(temperature)
            acceptance = self.sampler.get_acceptance_rate(i, start=-10)  # Acceptance rate over the last 10 iterations.

            if acceptance.size == 0:
                continue

            attribute = self.dynamic_generators[temperature][0]
            caps = self.dynamic_generators[temperature][2]
            cap_functions = [max, min]
            correlation_factors = [0.99, 1.01]
            if self.dynamic_generators[temperature][1] == False:
                pass
            else:
                correlation_factors.reverse()
                cap_functions.reverse()
                caps.reverse()

            # Rattle update amplitude
            if hasattr(generator, attribute):
                amplitude = getattr(generator, attribute)
                if acceptance < 0.5:
                    setattr(generator, attribute, cap_functions[0](caps[0], amplitude * correlation_factors[0]))
                else:
                    setattr(generator, attribute, cap_functions[1](caps[1], amplitude * correlation_factors[1]))

    def get_generator(self, temperature):
        return self.generators[self.mapping[temperature]]

    def get_generator_key(self, temperature):
        return self.generator_keys[self.mapping[temperature]]
