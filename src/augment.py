"""Add redundant (true) clues to a certified puzzle until it reaches a target level."""
from __future__ import annotations

import copy
import random

from .csp import CNF
from .families import get
from .grading import grade


def _key(c):
    return repr(sorted((k, str(v)) for k, v in c.items() if k != "text"))


def augment_to_level(spec, target, rng: random.Random, max_add=200):
    fam = get(spec["family"])
    spec = copy.deepcopy(spec)
    have = {_key(c) for c in spec["clues"]}
    pool = [c for c in fam.clue_pool(rng, spec) if _key(c) not in have]
    rng.shuffle(pool)
    added = 0
    while True:
        csp, _ = fam.build_csp(spec)
        if grade(CNF(csp)).level <= target:
            break
        if not pool or added >= max_add:
            return None
        c = pool.pop()
        if spec["family"] == "zebra":
            from .families import zebra as Z
            c["text"] = Z.render_clue(spec, c, rng)
        spec["clues"].append(c)
        added += 1
    if spec["family"] == "zebra":
        rng.shuffle(spec["clues"])
    spec["augmented"] = added
    return spec
