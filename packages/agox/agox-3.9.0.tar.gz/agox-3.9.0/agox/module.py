import functools
from typing import Any, Dict, List
from uuid import uuid4

from agox.writer import Writer


class Module:
    """
    Base class for all modules.

    Modules are the building blocks of the AGOX framework. They are used to define the
    different types of operations that are performed during a global optimization
    algorithm.

    Parameters:
    -----------
    use_cache : bool
        If True, the module will use a cache to store the results of the methods.
    """

    kwargs = ["surname"]

    def __init__(self, use_cache: bool = False, surname: bool = None) -> None:
        self.writer = Writer()
        self.surname = surname if surname is not None else ""

        self.use_cache = use_cache
        self.cache_key = str(uuid4())
        self.ray_key = str(uuid4())
        self.self_synchronizing = False
        self.dynamic_attributes = []  # Attributes that can be added and removed.

    def get_dynamic_attributes(self) -> Dict:
        return {key: self.__dict__.get(key, None) for key in self.dynamic_attributes}

    def add_dynamic_attribute(self, attribute_name: str) -> None:
        self.dynamic_attributes.append(attribute_name)

    def remove_dynamic_attribute(self, attribute_name: str) -> None:
        assert attribute_name in self.__dict__.keys()
        assert attribute_name in self.dynamic_attributes
        del self.dynamic_attributes[self.dynamic_attributes.index(attribute_name)]

    @property
    def dynamic_state(self) -> bool:
        state = len(self.dynamic_attributes) > 0
        return state

    @property
    def __name__(self) -> str:
        """
        Defines the name.
        """
        if len(self.dynamic_attributes) > 0:
            last = "Dynamic"
        else:
            last = ""
        return self.name + self.surname + last

    def find_submodules(self, in_key: str = None, only_dynamic: bool =False) -> Dict:
        if in_key is None:
            in_key = []

        submodules = {}
        for key, value in self.__dict__.items():
            if issubclass(value.__class__, Module):
                key = in_key + [key]
                if only_dynamic:
                    if value.dynamic_state:
                        submodules[tuple(key)] = value
                else:
                    submodules[tuple(key)] = value
                submodules.update(value.find_submodules(in_key=key, only_dynamic=only_dynamic))

        return submodules

    def set_for_submodule(self, submodule_keys: List, value: Any) -> None:
        reference = self
        for key in submodule_keys[0:-1]:
            reference = self.__dict__[key]
        reference.__dict__[submodule_keys[-1]] = value

    @classmethod
    def reset_cache_key(clc, func) -> Any:
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs) -> Any:
            self.cache_key = str(uuid4())
            return func(self, *args, **kwargs)

        return wrapper
