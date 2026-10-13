"""Certify and measure one puzzle spec: uniqueness, ladder level, solver metrics."""
from __future__ import annotations

import statistics

from .csp import CNF, count_solutions, cpsat_count
from .families import get
from .grading import cdcl_stats, explanation_sizes, grade, redundancy


def certify(spec):
    fam = get(spec["family"])
    csp, sol = fam.build_csp(spec)
    cnf = CNF(csp)
    sols = count_solutions(cnf, limit=2)
    out = {"n_solutions": len(sols) if len(sols) < 2 else ">=2", "unique": len(sols) == 1,
           "cpsat_unique": cpsat_count(csp, limit=2) == 1}
    if sol is not None:
        out["intended_ok"] = csp.check(sol)
        out["matches_intended"] = len(sols) == 1 and sols[0] == sol
    return out, cnf, sols


def analyze(spec, explain=True, with_redundancy=False):
    fam = get(spec["family"])
    cert, cnf, sols = certify(spec)
    res = dict(cert)
    if not cert["unique"]:
        return res
    sol = sols[0]
    g = grade(cnf)
    res.update({
        "level": g.level,
        "counts": g.counts,
        "frac_after": {str(k): v for k, v in g.frac_after.items()},
        "probes": g.probes,
        "n_clues": len(spec["clues"]),
    })
    res.update(cdcl_stats(cnf))
    if explain:
        skip = set()
        for j, c in enumerate(cnf.csp.clues):
            if c.meta.get("type") == "given":
                skip.update(c.scope)
        sizes = explanation_sizes(cnf, list(range(len(cnf.csp.clues))), sol, skip_vars=skip)
        vals = list(sizes.values()) or [0]
        res["mus_mean"] = statistics.mean(vals)
        res["mus_max"] = max(vals)
        res["mus_sizes"] = sizes
    if with_redundancy:
        res["redundancy"] = redundancy(cnf, list(range(len(cnf.csp.clues))))
    return res
