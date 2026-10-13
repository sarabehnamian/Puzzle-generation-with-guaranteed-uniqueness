"""Finite-domain CSP core shared by all puzzle families.

A puzzle is a CSP with
  * variables, each with a finite list of domain labels,
  * rule constraints (the rules of the genre; never removed),
  * clue constraints (the givens of one instance; removable).

Every constraint is either ``alldiff`` over a scope or a ``table`` constraint
given by a Python predicate over the domain *labels* of its scope.  The CSP is
compiled to CNF with the direct encoding: one Boolean x[v][a] per
(variable, value) pair, exactly-one clauses per variable, at-most-one (and
at-least-one for permutation scopes) clauses for alldiff, and one
forbidden-tuple clause per disallowed tuple of a table constraint.
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from typing import Callable, Sequence

from pysat.solvers import Solver

SOLVER_NAME = "minisat22"


@dataclass
class Constraint:
    kind: str                      # 'alldiff' or 'table'
    scope: tuple                   # variable indices
    pred: Callable | None = None   # table: pred(*labels) -> bool
    meta: dict = field(default_factory=dict)


class CSP:
    def __init__(self, names: Sequence[str], domains: Sequence[Sequence]):
        self.names = list(names)
        self.domains = [list(d) for d in domains]
        self.index = {n: i for i, n in enumerate(self.names)}
        self.rules: list[Constraint] = []
        self.clues: list[Constraint] = []

    def add_rule(self, c: Constraint):
        self.rules.append(c)

    def add_clue(self, c: Constraint):
        self.clues.append(c)

    def check(self, labels: Sequence, clue_ids=None) -> bool:
        """Does a full assignment (list of labels) satisfy rules and clues?"""
        cl = self.clues if clue_ids is None else [self.clues[i] for i in clue_ids]
        for c in self.rules + cl:
            vals = [labels[v] for v in c.scope]
            if c.kind == "alldiff":
                if len(set(vals)) != len(vals):
                    return False
            elif not c.pred(*vals):
                return False
        return True


class CNF:
    """Direct CNF encoding of a CSP, with clauses grouped by constraint."""

    def __init__(self, csp: CSP):
        self.csp = csp
        self.nvars = 0
        self.lit = []
        for d in csp.domains:
            row = []
            for _ in d:
                self.nvars += 1
                row.append(self.nvars)
            self.lit.append(row)
        self.var_of = {}
        for v, row in enumerate(self.lit):
            for a, x in enumerate(row):
                self.var_of[x] = (v, a)
        # exactly-one per variable
        self.domain_clauses = []
        self.var_domain_clauses = []
        for v, row in enumerate(self.lit):
            cls = [list(row)] + [[-x, -y] for x, y in itertools.combinations(row, 2)]
            self.var_domain_clauses.append(cls)
            self.domain_clauses.extend(cls)
        self.rule_clauses = [self._compile(c) for c in csp.rules]
        self.clue_clauses = [self._compile(c) for c in csp.clues]

    def _compile(self, c: Constraint):
        doms = [self.csp.domains[v] for v in c.scope]
        if c.kind == "alldiff":
            cls = []
            labels = set(doms[0])
            for d in doms[1:]:
                labels &= set(d)
            permutation = all(len(d) == len(c.scope) and set(d) == set(doms[0]) for d in doms)
            for lab in labels:
                xs = [self.lit[v][self.csp.domains[v].index(lab)] for v in c.scope]
                cls.extend([[-x, -y] for x, y in itertools.combinations(xs, 2)])
                if permutation:
                    cls.append(list(xs))
            return cls
        cls = []
        for tup in itertools.product(*[range(len(d)) for d in doms]):
            labs = [doms[i][a] for i, a in enumerate(tup)]
            if not c.pred(*labs):
                cls.append([-self.lit[v][a] for v, a in zip(c.scope, tup)])
        # drop clauses subsumed by domain clauses (two literals of the same var)
        return cls

    # --- helpers -------------------------------------------------------
    def all_clauses(self, clue_ids=None):
        out = list(self.domain_clauses)
        for g in self.rule_clauses:
            out.extend(g)
        ids = range(len(self.clue_clauses)) if clue_ids is None else clue_ids
        for i in ids:
            out.extend(self.clue_clauses[i])
        return out

    def decode(self, model) -> list:
        pos = set(l for l in model if l > 0)
        labels = []
        for v, row in enumerate(self.lit):
            val = None
            for a, x in enumerate(row):
                if x in pos:
                    val = self.csp.domains[v][a]
            labels.append(val)
        return labels

    def solution_lits(self, labels) -> list:
        return [self.lit[v][self.csp.domains[v].index(lab)] for v, lab in enumerate(labels)]


class ClueSolver:
    """Incremental SAT solver in which every clue can be switched on or off.

    Clue j's clauses are guarded by selector s_j; a check activates the
    chosen clues through assumptions.  Used for uniqueness checks,
    minimisation and minimal-unsatisfiable-core explanations.
    """

    def __init__(self, cnf: CNF, name: str = SOLVER_NAME):
        self.cnf = cnf
        self.solver = Solver(name=name)
        top = cnf.nvars
        for cl in cnf.domain_clauses:
            self.solver.add_clause(cl)
        for g in cnf.rule_clauses:
            for cl in g:
                self.solver.add_clause(cl)
        self.sel = []
        for g in cnf.clue_clauses:
            top += 1
            self.sel.append(top)
            for cl in g:
                self.solver.add_clause(cl + [-top])
        self.top = top

    def new_var(self):
        self.top += 1
        return self.top

    def solve(self, clue_ids, extra=()):
        ok = self.solver.solve(assumptions=[self.sel[i] for i in clue_ids] + list(extra))
        return ok

    def model_labels(self):
        return self.cnf.decode(self.solver.get_model())

    def block_guard(self, labels):
        """Add a guarded clause excluding one solution; return its guard literal."""
        g = self.new_var()
        self.solver.add_clause([-x for x in self.cnf.solution_lits(labels)] + [-g])
        return g

    def delete(self):
        self.solver.delete()


def solve_once(cnf: CNF, clue_ids=None):
    with Solver(name=SOLVER_NAME, bootstrap_with=cnf.all_clauses(clue_ids)) as s:
        if s.solve():
            return cnf.decode(s.get_model())
    return None


def count_solutions(cnf: CNF, clue_ids=None, limit: int = 2):
    """Return up to ``limit`` distinct solutions (as label lists)."""
    sols = []
    with Solver(name=SOLVER_NAME, bootstrap_with=cnf.all_clauses(clue_ids)) as s:
        while len(sols) < limit and s.solve():
            lab = cnf.decode(s.get_model())
            sols.append(lab)
            s.add_clause([-x for x in cnf.solution_lits(lab)])
    return sols


def is_unique(cnf: CNF, clue_ids=None) -> bool:
    return len(count_solutions(cnf, clue_ids, 2)) == 1


def cpsat_count(csp: CSP, limit: int = 2, time_limit: float = 30.0):
    """Independent cross-check with OR-tools CP-SAT: number of solutions (capped)."""
    import itertools as it

    from ortools.sat.python import cp_model

    m = cp_model.CpModel()
    xs = [m.NewIntVar(0, len(d) - 1, f"x{i}") for i, d in enumerate(csp.domains)]
    for c in csp.rules + csp.clues:
        doms = [csp.domains[v] for v in c.scope]
        if c.kind == "alldiff":
            # compare labels, not indices
            labs = sorted(set().union(*map(set, doms)), key=str)
            ys = []
            for v in c.scope:
                y = m.NewIntVar(0, len(labs) - 1, "")
                m.AddElement(xs[v], [labs.index(l) for l in csp.domains[v]], y)
                ys.append(y)
            m.AddAllDifferent(ys)
        else:
            allowed = [tup for tup in it.product(*[range(len(d)) for d in doms])
                       if c.pred(*[doms[i][a] for i, a in enumerate(tup)])]
            m.AddAllowedAssignments([xs[v] for v in c.scope], allowed)

    class CB(cp_model.CpSolverSolutionCallback):
        def __init__(self):
            super().__init__()
            self.n = 0

        def on_solution_callback(self):
            self.n += 1
            if self.n >= limit:
                self.StopSearch()

    s = cp_model.CpSolver()
    s.parameters.enumerate_all_solutions = True
    s.parameters.max_time_in_seconds = time_limit
    s.parameters.num_workers = 1
    cb = CB()
    s.Solve(m, cb)
    return cb.n
