"""The position DSL used to encode grid-logic (zebra) clues.

An encoding is a list of Python expressions over ``pos("value")``, the house
number (1..N) of a value.  Allowed names: pos, Abs, And, Or, Not, Implies, If,
Xor, Distinct and integer literals.  The same expression can be evaluated in
two modes:

* concrete: ``pos`` returns Python ints and the logical helpers act on bools;
* symbolic: ``pos`` returns z3 integer variables, giving a z3 formula.

Example clue encodings::

    pos("tea") == pos("Swede")                 # the Swede drinks tea
    pos("green") + 1 == pos("white")           # green directly left of white
    Abs(pos("dog") - pos("milk")) == 1         # dog owner next to milk drinker
    pos("chess") < pos("cat")                  # somewhere to the left
"""
from __future__ import annotations

import re

import z3

POS_RE = re.compile(r"pos\(\s*[\"']([^\"']+)[\"']\s*\)")


class DSLError(Exception):
    pass


def norm(name: str) -> str:
    return name.strip().lower()


def names_in(expr: str):
    return sorted({norm(m) for m in POS_RE.findall(expr)})


def _flat(args):
    out = []
    for a in args:
        if isinstance(a, (list, tuple)):
            out.extend(_flat(a))
        else:
            out.append(a)
    return out


def _concrete_ns(posmap):
    def pos(name):
        k = norm(name)
        if k not in posmap:
            raise DSLError(f"unknown value {name!r}")
        return posmap[k]

    return {
        "pos": pos,
        "Abs": abs,
        "And": lambda *a: all(_flat(a)),
        "Or": lambda *a: any(_flat(a)),
        "Not": lambda a: not a,
        "Implies": lambda a, b: (not a) or b,
        "If": lambda c, a, b: a if c else b,
        "Xor": lambda a, b: bool(a) != bool(b),
        "Distinct": lambda *a: len(set(_flat(a))) == len(_flat(a)),
        "True": True,
        "False": False,
    }


def _symbolic_ns(varmap):
    def pos(name):
        k = norm(name)
        if k not in varmap:
            raise DSLError(f"unknown value {name!r}")
        return varmap[k]

    def _abs(x):
        return z3.If(x >= 0, x, -x)

    return {
        "pos": pos,
        "Abs": _abs,
        "And": lambda *a: z3.And(*_flat(a)),
        "Or": lambda *a: z3.Or(*_flat(a)),
        "Not": z3.Not,
        "Implies": z3.Implies,
        "If": z3.If,
        "Xor": z3.Xor,
        "Distinct": lambda *a: z3.Distinct(*_flat(a)),
        "True": True,
        "False": False,
    }


def _check_syntax(expr: str):
    if any(tok in expr for tok in ("__", "import", "lambda", "exec", "eval", "open", ";")):
        raise DSLError("forbidden token in expression")


def eval_concrete(expr: str, posmap: dict) -> bool:
    _check_syntax(expr)
    try:
        return bool(eval(expr, {"__builtins__": {}}, _concrete_ns(posmap)))
    except DSLError:
        raise
    except Exception as e:  # noqa: BLE001
        raise DSLError(f"cannot evaluate {expr!r}: {e}") from e


def eval_symbolic(expr: str, varmap: dict):
    _check_syntax(expr)
    try:
        out = eval(expr, {"__builtins__": {}}, _symbolic_ns(varmap))
    except DSLError:
        raise
    except Exception as e:  # noqa: BLE001
        raise DSLError(f"cannot evaluate {expr!r}: {e}") from e
    if isinstance(out, bool):
        out = z3.BoolVal(out)
    if not z3.is_bool(out):
        raise DSLError(f"expression is not a boolean constraint: {expr!r}")
    return out


class ZebraSpace:
    """Symbolic universe for one zebra puzzle: z3 position variables and rules."""

    def __init__(self, n: int, cats: dict):
        self.n = n
        self.cats = {c: [norm(v) for v in vals] for c, vals in cats.items()}
        self.vars = {}
        for c, vals in self.cats.items():
            for v in vals:
                self.vars[v] = z3.Int(f"p_{v}")
        base = []
        for v, x in self.vars.items():
            base += [x >= 1, x <= n]
        for c, vals in self.cats.items():
            base.append(z3.Distinct(*[self.vars[v] for v in vals]))
        self.base = z3.And(*base)

    def formula(self, exprs):
        return z3.And(*[eval_symbolic(e, self.vars) for e in exprs]) if exprs else z3.BoolVal(True)

    def equivalent(self, f, g, timeout_ms=20000):
        """True if base -> (f <-> g); None on timeout."""
        s = z3.Solver()
        s.set("timeout", timeout_ms)
        s.add(self.base, z3.Xor(f, g))
        r = s.check()
        if r == z3.unsat:
            return True
        if r == z3.sat:
            return False
        return None

    def solutions(self, f, limit=2):
        s = z3.Solver()
        s.add(self.base, f)
        out = []
        while len(out) < limit and s.check() == z3.sat:
            m = s.model()
            sol = {v: m.eval(x).as_long() for v, x in self.vars.items()}
            out.append(sol)
            s.add(z3.Or(*[x != sol[v] for v, x in self.vars.items()]))
        return out
