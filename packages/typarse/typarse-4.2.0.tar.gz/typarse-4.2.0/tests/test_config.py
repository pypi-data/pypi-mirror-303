from typarse import BaseConfig
from typing import List, Tuple


def test_simple_config():
    class Config(BaseConfig):
        foo: int = 1
        bar: float = 2.0
        baz: str = "abc"

    assert Config.foo == 1
    assert Config.bar == 2.0
    assert Config.baz == "abc"


def test_update():
    class Config(BaseConfig):
        foo: int = 1
        bar: float = 2.0
        baz: str = "abc"

    config = {"foo": 5, "bar": 10.0, "baz": "qwe"}
    Config.update(config)

    assert Config.foo == 5
    assert Config.bar == 10.0
    assert Config.baz == "qwe"


def test_nested():
    class Config(BaseConfig):
        foo: int = 1

        class Bar(BaseConfig):
            foo: int = 5
            bar: str = "abc"

    assert Config.foo == 1
    assert Config.Bar.foo == 5
    assert Config.Bar.bar == "abc"


def test_nested_update():
    class Config(BaseConfig):
        foo: int = 1

        class Bar(BaseConfig):
            foo: int = 5
            bar: str = "abc"

    config = {"foo": 2, "Bar": {"foo": 10, "bar": "qwe"}}

    Config.update(config)

    assert Config.foo == 2
    assert Config.Bar.foo == 10
    assert Config.Bar.bar == "qwe"


def test_partial_update():
    class Config(BaseConfig):
        foo: int = 1
        bar: float = 2.0

        class Bar(BaseConfig):
            foo: str = "abc"
            bar: List[int] = [1, 2, 3]
            baz: int = 10

    config = {"foo": 5, "Bar": {"foo": "qwe", "bar": [5, 6, 7]}}

    Config.update(config)

    assert Config.foo == 5
    assert Config.bar == 2.0
    assert Config.Bar.foo == "qwe"
    assert Config.Bar.bar == [5, 6, 7]
    assert Config.Bar.baz == 10


def test_getitem():
    class Config(BaseConfig):
        foo: int = 1
        bar: float = 2.0

        class Bar(BaseConfig):
            foo: str = "abc"
            bar: List[int] = [1, 2, 3]
            baz: int = 10

    Config["bar"] = 3.0
    Config["Bar"]["baz"] = 20

    assert Config["foo"] == 1
    assert Config["bar"] == 3.0
    assert Config["Bar"]["foo"] == "abc"
    assert Config["Bar"]["bar"] == [1, 2, 3]
    assert Config["Bar"]["baz"] == 20


def test_config_update():
    class ConfigA(BaseConfig):
        foo: int = 1

        class Bar(BaseConfig):
            foo: int = 5

    class ConfigB(BaseConfig):
        foo: int = 2

        class Bar(BaseConfig):
            foo: int = 10

    ConfigA.update(ConfigB.to_dict())

    assert ConfigA.foo == 2
    assert ConfigA.Bar.foo == 10


def test_pickle():
    import pickle
    import os

    class Config(BaseConfig):
        foo: int = 1
        bar: float = 2.0

        class Bar(BaseConfig):
            foo: str = "abc"
            bar: List[int] = [1, 2, 3]
            baz: int = 10

    config = Config
    with open("test.pickle", "wb") as f:
        pickle.dump(Config.to_dict(), f)

    with open("test.pickle", "rb") as f:
        config_ = pickle.load(f)

    os.remove("test.pickle")

    assert config.foo == 1 == config_["foo"]
    assert config.bar == 2.0 == config_["bar"]
    assert config.Bar.foo == "abc" == config_["Bar"]["foo"]
    assert config.Bar.bar == [1, 2, 3] == config_["Bar"]["bar"]
    assert config.Bar.baz == 10 == config_["Bar"]["baz"]


def test_copy():
    class OptimizerKwargs(BaseConfig):
        lr: float = 1e-4
        betas: Tuple[float, float] = (0.9, 0.999)
        eps: float = 1e-7
        weight_decay: float = 0.0
        amsgrad: bool = False

    ConfigCopy: OptimizerKwargs = OptimizerKwargs.clone()

    ConfigCopy.update({"lr": 1e-1})

    assert ConfigCopy.lr == 1e-1
    assert OptimizerKwargs.lr == 1e-4

    OptimizerKwargs.update({"eps": 1e-1})

    assert ConfigCopy.lr == 1e-1
    assert OptimizerKwargs.lr == 1e-4
    assert ConfigCopy.eps == 1e-7
    assert OptimizerKwargs.eps == 1e-1


def test_empty_update():
    class Config(BaseConfig):
        foo: int = 1
        bar: float = 2.0
        baz: str = "abc"

    config = {"foo": None, "bar": 10.0, "baz": "qwe"}
    Config.update(config)

    assert Config.foo == 1
    assert Config.bar == 10.0
    assert Config.baz == "qwe"


def test_tuple_list_update():
    class Config(BaseConfig):
        foo: tuple[int, ...] = (1, 2, 3)

    config = {"foo": [4, 5, 6]}
    Config.update(config)

    assert Config.foo == (4, 5, 6)
    assert not Config.foo == [4, 5, 6]


def test_list_tuple_update():
    class Config(BaseConfig):
        foo: list[int] = [1, 2, 3]

    config = {"foo": (4, 5, 6)}
    Config.update(config)

    assert Config.foo == [4, 5, 6]
    assert not Config.foo == (4, 5, 6)