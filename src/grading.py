"""Difficulty ladder and solver-side metrics.

Ladder (each engine contains all rules of the engines below it; the level of
a puzzle is the weakest engine whose fixpoint assigns every variable):

  L1  unit propagation on the direct CNF encoding (naked and hidden singles,
      direct use of a clue once its other side is known).
  L2  L1 + single-constraint elimination: generalised arc consistency on each
      rule or clue taken on its own (with the exactly-one domain constraints
      of its scope).  Covers elimination by one clue, naked/hidden subsets
      inside one row/category, cage combinations, etc.
  L3  L2 + failed-literal probing: tentatively place a candidate value, run
      unit propagation, and eliminate it if that yields a contradiction
      (one-step lookahead).
  L4  L2 + two-level lookahead: place a candidate, then run unit propagation
      plus failed-literal probing inside that hypothesis; eliminate the
      candidate if this yields a contradiction.
  L5  none of the above reaches the solution: some search/backtracking is
      needed (beyond two levels of lookahead).

All rules are sound and monotone, so their closure is unique and the ladder
can be computed in a single pass that switches on stronger rules only when
the weaker ones are exhausted.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from pysat.solvers import Solver

from .csp import CNF, ClueSolver, SOLVER_NAME


@dataclass
class GradeResult:
    level: int
    counts: dict = field(default_factory=dict)      # deductions per rule
    frac_after: dict = field(default_factory=dict)  # fraction of vars fixed after each level's fixpoint
    trace: list = field(default_factory=list)
    probes: dict = field(default_factory=dict)      # number of probe calls per rule


class Engine:
    def __init__(self, cnf: CNF, clue_ids=None, trace=False):
        self.cnf = cnf
        self.clue_ids = list(range(len(cnf.clue_clauses))) if clue_ids is None else list(clue_ids)
        # unit clauses are kept out of the solver and used as assumptions, so
        # that propagate() reports their consequences (MiniSat does not report
        # literals fixed at decision level 0)
        clauses = cnf.all_clauses(self.clue_ids)
        self.units = {cl[0] for cl in clauses if len(cl) == 1}
        self.main = Solver(name=SOLVER_NAME, bootstrap_with=[cl for cl in clauses if len(cl) > 1])
        csp = cnf.csp
        # groups for single-constraint reasoning: rules and active clues
        self.groups = []
        for i, c in enumerate(csp.rules):
            self.groups.append((("rule", i), c.scope, cnf.rule_clauses[i]))
        for j in self.clue_ids:
            c = csp.clues[j]
            self.groups.append((("clue", j), c.scope, cnf.clue_clauses[j]))
        self._gsolvers = {}
        self._gsnap = {}
        self.do_trace = trace
        self.trace = []
        self.counts = {"UP": 0, "GAC": 0, "FL1": 0, "FL2": 0}
        self.probes = {"GAC": 0, "FL1": 0, "FL2": 0}
        self.known = set()

    def close(self):
        self.main.delete()
        for s in self._gsolvers.values():
            s.delete()

    # --- basic propagation --------------------------------------------
    def up(self, lits):
        ok, out = self.main.propagate(assumptions=sorted(lits, key=abs))
        if not ok:
            return None
        return set(out) | set(lits)

    def _primary(self, lits):
        return {l for l in lits if abs(l) <= self.cnf.nvars}

    def assign(self, new, rule, info=None):
        before = self.known
        res = self.up(self.known | set(new))
        if res is None:
            raise RuntimeError("contradiction during sound propagation (bug or inconsistent puzzle)")
        res = self._primary(res)
        gained = res - before
        n_direct = len(set(new) - before)
        self.counts[rule] += n_direct
        self.counts["UP"] += max(0, len(gained) - n_direct)
        if self.do_trace:
            for l in sorted(set(new) - before, key=abs):
                self.trace.append({"rule": rule, "lit": l, "info": info.get(l) if info else None})
            for l in sorted(gained - set(new), key=abs):
                if l > 0:
                    self.trace.append({"rule": "UP", "lit": l, "info": None})
        self.known = res

    def complete(self):
        pos = {l for l in self.known if l > 0}
        return len(pos) == len(self.cnf.lit)

    def frac_fixed(self):
        return len({l for l in self.known if l > 0}) / len(self.cnf.lit)

    def candidates(self):
        """Positive literals not yet decided."""
        out = []
        for v, row in enumerate(self.cnf.lit):
            if any(x in self.known for x in row):
                continue
            for x in row:
                if -x not in self.known:
                    out.append(x)
        return out

    # --- L2: single-constraint GAC -------------------------------------
    def _gsolver(self, gi):
        if gi not in self._gsolvers:
            _, scope, cls = self.groups[gi]
            s = Solver(name=SOLVER_NAME)
            for v in scope:
                for cl in self.cnf.var_domain_clauses[v]:
                    s.add_clause(cl)
            for cl in cls:
                s.add_clause(cl)
            self._gsolvers[gi] = s
        return self._gsolvers[gi]

    def gac_sweep(self):
        new = set()
        info = {}
        for gi, (gid, scope, _) in enumerate(self.groups):
            scope_lits = [x for v in scope for x in self.cnf.lit[v]]
            ass = [l for x in scope_lits for l in (x, -x) if l in self.known]
            snap = frozenset(ass)
            if self._gsnap.get(gi) == snap:
                continue
            self._gsnap[gi] = snap
            s = self._gsolver(gi)
            for v in scope:
                row = self.cnf.lit[v]
                if any(x in self.known for x in row):
                    continue
                for x in row:
                    if -x in self.known or -x in new:
                        continue
                    self.probes["GAC"] += 1
                    if not s.solve(assumptions=ass + [x]):
                        new.add(-x)
                        info[-x] = gid
        if new:
            self.assign(new, "GAC", info)
        return bool(new)

    def gac_fixpoint(self):
        changed = False
        while not self.complete() and self.gac_sweep():
            changed = True
        return changed

    # --- L3: failed literals --------------------------------------------
    def fl_sweep(self):
        new = set()
        info = {}
        for x in self.candidates():
            self.probes["FL1"] += 1
            if self.up(self.known | {x}) is None:
                new.add(-x)
                info[-x] = x
        if new:
            self.assign(new, "FL1", info)
        return bool(new)

    # --- L4: two-level lookahead ----------------------------------------
    def _inner_conflict(self, x):
        k = self.up(self.known | {x})
        if k is None:
            return True
        k = self._primary(k)
        changed = True
        while changed:
            changed = False
            for v, row in enumerate(self.cnf.lit):
                if any(y in k for y in row):
                    continue
                for m in row:
                    if -m in k:
                        continue
                    if self.up(k | {m}) is None:
                        k2 = self.up(k | {-m})
                        if k2 is None:
                            return True
                        k = self._primary(k2)
                        changed = True
                        break
        return False

    def fl2_sweep(self):
        new = set()
        info = {}
        for x in self.candidates():
            self.probes["FL2"] += 1
            if self._inner_conflict(x):
                new.add(-x)
                info[-x] = x
                break  # apply immediately; cheaper rules are retried first
        if new:
            self.assign(new, "FL2", info)
        return bool(new)


def grade(cnf: CNF, clue_ids=None, trace=False, max_level=4) -> GradeResult:
    eng = Engine(cnf, clue_ids, trace=trace)
    try:
        start = eng.up(set(eng.units))
        if start is None:
            raise RuntimeError("puzzle is inconsistent")
        eng.known = eng._primary(start)
        eng.counts["UP"] += len([l for l in eng.known if l > 0])
        if eng.do_trace:
            for l in sorted(eng.known, key=abs):
                if l > 0:
                    eng.trace.append({"rule": "UP", "lit": l, "info": None})
        frac = {1: eng.frac_fixed()}
        level = 1
        if not eng.complete():
            level = 2
            eng.gac_fixpoint()
            frac[2] = eng.frac_fixed()
        if not eng.complete() and max_level >= 3:
            level = 3
            while not eng.complete():
                eng.gac_fixpoint()
                if eng.complete() or not eng.fl_sweep():
                    break
            frac[3] = eng.frac_fixed()
        if not eng.complete() and max_level >= 4:
            level = 4
            while not eng.complete():
                eng.gac_fixpoint()
                if eng.complete():
                    break
                if eng.fl_sweep():
                    continue
                if not eng.fl2_sweep():
                    break
            frac[4] = eng.frac_fixed()
        if not eng.complete():
            level = max_level + 1
        for k in range(1, 6):
            if k not in frac:
                frac[k] = frac[max(frac)] if k > max(frac) else frac[k]
        return GradeResult(level=level, counts=dict(eng.counts), frac_after=frac,
                           trace=eng.trace, probes=dict(eng.probes))
    finally:
        eng.close()


# ----------------------------------------------------------------------
# solver-side metrics
# ----------------------------------------------------------------------

def cdcl_stats(cnf: CNF, clue_ids=None):
    """MiniSat statistics for finding the solution and proving it unique."""
    with Solver(name=SOLVER_NAME, bootstrap_with=cnf.all_clauses(clue_ids)) as s:
        assert s.solve()
        st1 = dict(s.accum_stats())
        lab = cnf.decode(s.get_model())
        s.add_clause([-x for x in cnf.solution_lits(lab)])
        unique = not s.solve()
        st2 = dict(s.accum_stats())
    return {
        "decisions_find": st1.get("decisions", 0),
        "conflicts_find": st1.get("conflicts", 0),
        "decisions_total": st2.get("decisions", 0),
        "conflicts_total": st2.get("conflicts", 0),
        "propagations_total": st2.get("propagations", 0),
        "unique": unique,
    }


def mus_for_literal(cs: ClueSolver, clue_ids, lit):
    """Minimal set of clues that (with the rules) forces ``lit``.

    Deletion-based group-MUS over the clue selectors.  Returns a sorted list
    of clue indices.
    """
    sel_to_clue = {cs.sel[i]: i for i in clue_ids}
    assert not cs.solve(clue_ids, extra=[-lit])
    core = {sel_to_clue[s] for s in cs.solver.get_core() if s in sel_to_clue}
    for c in sorted(core):
        if c not in core:
            continue
        trial = sorted(core - {c})
        if not cs.solve(trial, extra=[-lit]):
            core = {sel_to_clue[s] for s in cs.solver.get_core() if s in sel_to_clue}
    core = sorted(core)
    return core


def explanation_sizes(cnf: CNF, clue_ids, solution, skip_vars=()):
    """MUS size (number of clues) needed to force each variable's value."""
    cs = ClueSolver(cnf)
    sizes = {}
    try:
        lits = cnf.solution_lits(solution)
        for v, x in enumerate(lits):
            if v in skip_vars:
                continue
            sizes[v] = len(mus_for_literal(cs, clue_ids, x))
    finally:
        cs.delete()
    return sizes


def redundancy(cnf: CNF, clue_ids):
    """Fraction of clues whose individual removal keeps the solution unique."""
    cs = ClueSolver(cnf)
    try:
        assert cs.solve(clue_ids)
        sol = cs.model_labels()
        g = cs.block_guard(sol)
        red = 0
        for c in clue_ids:
            rest = [i for i in clue_ids if i != c]
            if not cs.solve(rest, extra=[g]):
                red += 1
    finally:
        cs.delete()
    return red / max(1, len(clue_ids))
