from typing import Any, Dict, Type
from inspect import isclass


class MetaConfig(type):
    """Takes care of printing the config like a dictionary"""

    def get_dict(cls) -> Dict:
        contents = dict(cls.__dict__)
        to_remove = ["__module__", "__annotations__", "__doc__"]
        for name in to_remove:
            try:
                contents.pop(name)
            except KeyError:
                continue

        return contents

    def __repr__(cls) -> str:
        return cls.get_dict().__repr__()

    def __str__(cls) -> str:
        return cls.get_dict().__str__()

    def get(self, key: str) -> Any:
        return getattr(self, key, None)

    def set(self, key: str, value: Any):
        """Set a single key's vale"""
        if hasattr(self, key):
            setattr(self, key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.set(key, value)

    # def __dict__(cls):
    #     return cls.get_dict()
    # def __getstate__(self, state):
    #     return self.get_dict()
    #
    # def __setstate__(self, state):
    #     for key, val in state.items():
    #         setattr(self, key, val)


class BaseConfig(metaclass=MetaConfig):

    # @classmethod
    # def set(cls, key: str, value: Any):
    #     """Set a single key's vale"""
    #     if hasattr(cls, key):
    #         setattr(cls, key, value)

    # @classmethod
    # def get(cls, key: str) -> Any:
    #     """Get the key's value, defaulting to None."""
    #     return getattr(cls, key, None)

    @classmethod
    def to_dict(cls) -> dict:
        """Converts the config to a dictionary, removing the built-ins"""
        contents = dict(cls.__dict__)
        to_remove = ["__module__", "__annotations__", "__doc__"]
        for name in to_remove:
            try:
                contents.pop(name)
            except KeyError:
                continue

        for key, value in contents.items():
            if isclass(value) and issubclass(value, BaseConfig):
                contents[key] = value.to_dict()

        return contents

    @classmethod
    def update(cls, config: dict):
        """Updates the config based on the values from a dictionary."""
        for key in config:
            value = config.get(key)
            d_value = cls.get(key)

            if isclass(d_value) and issubclass(d_value, BaseConfig):
                d_value.update(value)
            elif value is not None:
                cls.set(key, value)
            else:
                continue

    @classmethod
    def clone(cls):
        return type(cls.__name__, cls.__bases__, dict(cls.__dict__))

    @classmethod
    def __getstate__(cls, state):
        return cls.to_dict()

    @classmethod
    def __setstate__(cls, state):
        for key, val in state.items():
            setattr(cls, key, val)

    @classmethod
    def __dict__(cls):
        return cls.to_dict
