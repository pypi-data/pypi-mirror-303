from typarse import BaseParser
from typing import List, Optional


class Parser(BaseParser):
    directory: str
    identifier: str
    num_experiments: int = 5
    gammas: List[float]
    etas: Optional[List[float]]
    beta: bool

    gamma_range: bool
    eta_range: bool

    _abbrev = {
        "directory": "d",
        "identifier": "i",
        "num_experiments": "n",
        "gammas": "g",
        "etas": "e",
        "beta": "b",
        "gamma_range": "gr",
        "eta_range": "er",
    }

    _help = {
        "directory": "Directory of the tensorboard logs",
        "identifier": "Name of the experiment for tensorboard",
        "num_experiments": "How many random seeds to run",
        "gammas": "Values of gamma (or mu) to test",
        "etas": "If in beta mode, values of eta (1/beta) to test",
        "beta": "Whether to use beta-weighted discounting. In absence of eta values, the heuristic will be used",
        "gamma_range": "Whether the gamma values should be interpreted as in np.linspace(start, end, num)",
        "eta_range": "See gamma_range",
    }
