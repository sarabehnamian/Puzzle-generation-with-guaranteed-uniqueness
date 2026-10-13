"""Certified generation: build a clue pool, reach uniqueness, minimise."""
from __future__ import annotations

import random

from .csp import CNF, ClueSolver
from .families import get


def complete_to_unique(cnf: CNF, solution, start_ids, pool_ids, rng: random.Random):
    """Add clues true in ``solution`` until it is the only solution.

    Each step picks a random pool clue that rules out the current
    counter-example solution, so the loop is guaranteed to terminate.
    """
    cs = ClueSolver(cnf)
    try:
        guard = cs.block_guard(solution)
        chosen = list(start_ids)
        remaining = [p for p in pool_ids if p not in chosen]
        rng.shuffle(remaining)
        while cs.solve(chosen, extra=[guard]):
            other = cs.model_labels()
            dist = [p for p in remaining if not cnf.csp.check(other, clue_ids=[p])]
            if not dist:
                return None
            pick = rng.choice(dist)
            chosen.append(pick)
            remaining.remove(pick)
        return chosen
    finally:
        cs.delete()


def minimize(cnf: CNF, solution, ids, order):
    """Remove clues (in ``order``) whenever the solution stays unique."""
    cs = ClueSolver(cnf)
    try:
        guard = cs.block_guard(solution)
        cur = set(ids)
        assert not cs.solve(sorted(cur), extra=[guard]), "start set is not unique"
        for c in order:
            if c not in cur:
                continue
            trial = cur - {c}
            if not cs.solve(sorted(trial), extra=[guard]):
                cur = trial
        return sorted(cur)
    finally:
        cs.delete()


def generate(family: str, rng: random.Random, params: dict, minimal=True):
    fam = get(family)
    spec = fam.random_spec(rng, **params)
    pool = fam.clue_pool(rng, spec)
    pspec = dict(spec, clues=pool)
    csp, sol = fam.build_csp(pspec)
    cnf = CNF(csp)
    all_ids = list(range(len(pool)))
    if fam.START == "empty":
        ids = complete_to_unique(cnf, sol, [], all_ids, rng)
        if ids is None:
            return None
    else:
        ids = all_ids
    if minimal:
        order = [i for i in fam.removal_order(rng, pool) if i in set(ids)]
        ids = minimize(cnf, sol, ids, order)
    spec["clues"] = [pool[i] for i in ids]
    fam.finalize(rng, spec)
    return spec
