from typarse import BaseParser
from typing import List, Optional


class Parser(BaseParser):
    nums: List[int] = [1, 2, 3]

    _abbrev = {"nums": "n"}

    _help = {
        "nums": "List of numbers to sum",
    }


args = Parser()

print(sum(args.nums))
