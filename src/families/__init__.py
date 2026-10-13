"""Uniform access to the puzzle families."""
from . import zebra as _z
from .grids import Futoshiki, Killer, Sudoku


class Zebra:
    FAMILY = "zebra"
    START = "empty"          # build up clues until unique, then minimise
    ANSWER_FORMAT = _z.ANSWER_FORMAT

    @staticmethod
    def rules_text(spec):
        return _z.RULES_TEXT

    build_csp = staticmethod(_z.build_csp)
    render = staticmethod(_z.render)
    score = staticmethod(_z.score)

    @staticmethod
    def random_spec(rng, n=5, k=4, style="plain"):
        cats, pos = _z.random_solution(rng, n, k)
        return {"family": "zebra", "n": n, "cats": cats, "solution": pos, "style": style}

    @staticmethod
    def clue_pool(rng, spec):
        return _z.clue_pool(rng, spec, hard=spec.get("style") == "hard")

    @staticmethod
    def removal_order(rng, pool):
        idx = list(range(len(pool)))
        rng.shuffle(idx)
        return idx

    @staticmethod
    def finalize(rng, spec):
        rng.shuffle(spec["clues"])
        _z.make_texts(spec, rng, spec.get("style", "plain"))


for _F in (Sudoku, Killer, Futoshiki):
    _F.START = "full"
    _F.finalize = staticmethod(lambda rng, spec: None)

FAMILIES = {"zebra": Zebra, "sudoku": Sudoku, "killer": Killer, "futoshiki": Futoshiki}


def get(name):
    return FAMILIES[name]
