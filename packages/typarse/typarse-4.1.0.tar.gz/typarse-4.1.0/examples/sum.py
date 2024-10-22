from typarse import BaseParser
from typing import List, Optional


class Parser(BaseParser):
    nums: List[int]
    square: bool
    default: int = 0

    _abbrev = {"nums": "n", "square": "s", "default": "d"}

    _help = {
        "nums": "List of numbers to sum",
        "square": "Whether the result should be squared",
        "default": "Initial value, added to the sum",
    }


args = Parser()

print(args.default + sum(args.nums) ** (1 + args.square))
