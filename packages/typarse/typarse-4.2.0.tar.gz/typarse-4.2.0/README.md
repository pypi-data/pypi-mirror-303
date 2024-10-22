# Typarse

This is a small project born out of my frustration with simple argument parsing in Python.

Not only do I have to instantiate some object whose name I can never remember, then I get way too many 
function parameters to get them right... It's a mess. And I don't even need half the features.

So this is an attempt at streamlining this process while simultaneously promoting some better type safety, by using the
magic of Python type hints! 

Really all the magic here is happening in the BaseParser class. You just need to subclass it, add a few typed parameters,
perhaps with some extra information in dictionaries... and you're done! For examples, just look at, well, examples.

## Supported types

First of all, all the basic types supported by argparse are also supported here. Things like: `str`, `int`, `float`. `bool`s are automatically interpreted as flags, False by default. Each type can be wrapped in a `List` to support reading them like `--list 1 2 3 4`. Each type can also be made `Optional` which makes it, well, optinal.


## Simple illustrative example

```python
from typarse import BaseParser
from typing import List


class Parser(BaseParser):
    nums: List[int]
    square: bool
    default: int = 0

    _abbrev = {
        "nums": "n",
        "square": "s",
        "default": "d"
    }

    _help = {
        "nums": "List of numbers to sum",
        "square": "Whether the result should be squared",
        "default": "Initial value, added to the sum"
    }



args = Parser()

print(args.default + sum(args.nums) ** (1+args.square))
```

# Functionality 2: Config

In the spirit of the library, I added a config management component. 
Similarly to parsing, you can define a config using type annotations on a class -- also in a nested manner.

Example:
```python
from typarse import BaseConfig
from typing import List 

class Config(BaseConfig):
    rate: float = 0.1
    amount: float = 0.01
    limit: float = 1.
    class PolicyConfig(BaseConfig):
        layers: List[int] = [32, 32, 32]
        activation: str = "relu"

config = {
    "rate": 0.5,
    "PolicyConfig": {
        "layers": [64, 64]
    }
}

```

# Installation

It's on PyPi so install it with `pip install typarse`, `poetry add typarse` or whatever you want. If you want to install it from the source, it's pure Python so I'm sure you can figure it out.
