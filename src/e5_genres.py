"""E5: LLM-invented puzzle genres, compiled and certified by the pipeline."""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

from pysat.solvers import Solver

from . import llm
from .csp import CNF, CSP, SOLVER_NAME, Constraint
from .generate import complete_to_unique, minimize
from .grading import grade
from .prompts import GENRE

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "configs" / "config.json").read_text())
OUT = ROOT / "results" / "e5"
SAFE = {"abs": abs, "min": min, "max": max, "sum": sum, "len": len, "set": set, "sorted": sorted,
        "all": all, "any": any, "range": range, "list": list, "tuple": tuple, "True": True,
        "False": False, "None": None, "enumerate": enumerate, "zip": zip, "int": int}


def _guard(src):
    for tok in ("import", "__", "open(", "exec", "eval", "globals", "locals", "getattr", "compile"):
        if tok in src:
            raise ValueError(f"forbidden token {tok!r}")


class G:
    def __init__(self, R, C, D):
        self.R, self.C, self.D = R, C, D
        self.cons = []

    def alldiff(self, cells):
        self.cons.append(("alldiff", [tuple(x) for x in cells], None))

    def table(self, cells, check):
        self.cons.append(("table", [tuple(x) for x in cells], check))


def load_genre(code):
    _guard(code)
    ns = dict(SAFE)
    exec(compile(code, "<genre>", "exec"), {"__builtins__": SAFE}, ns)  # noqa: S102
    R, C, D = ns["GRID"]
    assert 2 <= R <= 6 and 2 <= C <= 6 and 2 <= D <= 6
    return ns, (R, C, D)


def build(code, clue_list=None):
    ns, (R, C, D) = load_genre(code)
    g = G(R, C, D)
    ns["rules"](g)
    idx = lambda rc: rc[0] * C + rc[1]  # noqa: E731
    csp = CSP([f"R{r + 1}C{c + 1}" for r in range(R) for c in range(C)], [list(range(1, D + 1))] * (R * C))
    for kind, cells, chk in g.cons:
        if len(cells) > 8 and kind == "table":
            raise ValueError("table scope too large")
        csp.add_rule(Constraint(kind, tuple(idx(x) for x in cells), chk))
    for cl in clue_list or []:
        f = eval(cl["check"], {"__builtins__": SAFE}, {})  # noqa: S307
        csp.add_clue(Constraint("table", tuple(idx(tuple(x)) for x in cl["cells"]), f, meta={"text": cl.get("text")}))
    return ns, csp, (R, C, D)


def random_solution(csp, rng):
    cnf = CNF(csp)
    with Solver(name=SOLVER_NAME, bootstrap_with=cnf.all_clauses()) as s:
        if not s.solve():
            return None
        fixed = []
        order = list(range(len(csp.names)))
        rng.shuffle(order)
        for v in order:
            vals = list(range(len(csp.domains[v])))
            rng.shuffle(vals)
            for a in vals:
                if s.solve(assumptions=fixed + [cnf.lit[v][a]]):
                    fixed.append(cnf.lit[v][a])
                    break
        s.solve(assumptions=fixed)
        return cnf.decode(s.get_model())


def make_instance(code, rng):
    ns, csp, (R, C, D) = build(code)
    sol = random_solution(csp, rng)
    if sol is None:
        return {"status": "rules unsatisfiable"}
    grid = [[sol[r * C + c] for c in range(C)] for r in range(R)]
    pool = ns["clues"]([row[:] for row in grid])
    pool = [p for p in pool if isinstance(p, dict) and p.get("cells") and len(p["cells"]) <= 4][:400]
    if not pool:
        return {"status": "no clues"}
    _, pcsp, _ = build(code, pool)
    true_ids = [j for j, c in enumerate(pcsp.clues) if c.pred(*[sol[v] for v in c.scope])]
    if len(true_ids) < len(pool):
        frac_false = 1 - len(true_ids) / len(pool)
    else:
        frac_false = 0.0
    cnf = CNF(pcsp)
    ids = complete_to_unique(cnf, sol, [], true_ids, rng)
    if ids is None:
        return {"status": "clue pool cannot force uniqueness", "frac_false_clues": frac_false}
    order = list(ids)
    rng.shuffle(order)
    ids = minimize(cnf, sol, ids, order)
    g = grade(cnf, clue_ids=ids)
    return {"status": "ok", "grid": grid, "clues": [pool[j] for j in ids], "level": g.level,
            "n_clues": len(ids), "frac_false_clues": frac_false, "counts": g.counts}


def prepare():
    llm.write_task("e5_genre", "e5_genre_0", "sonnet", GENRE.replace("{K}", "6"), "", ["genres"])


def run(n_instances=12):
    OUT.mkdir(parents=True, exist_ok=True)
    rec = llm.manifest("e5_genre")[0]
    res = llm.read_output(rec)
    report = []
    for gi, gen in enumerate(res.get("genres", [])):
        rng = random.Random(f"{CFG['seed']}-e5-{gi}")
        entry = {"name": gen.get("name"), "rules_text": gen.get("rules_text"), "clue_text": gen.get("clue_text"),
                 "code": gen.get("code"), "instances": []}
        try:
            load_genre(gen["code"])
            for k in range(n_instances):
                entry["instances"].append(make_instance(gen["code"], rng))
            entry["compiled"] = True
        except Exception as e:  # noqa: BLE001
            entry["compiled"] = False
            entry["error"] = f"{type(e).__name__}: {e}"
        ok = [i for i in entry["instances"] if i.get("status") == "ok"]
        entry["n_ok"] = len(ok)
        entry["levels"] = sorted(i["level"] for i in ok)
        report.append(entry)
        print(entry["name"], entry.get("compiled"), entry.get("error", ""), entry["n_ok"], entry["levels"])
    (OUT / "genres.json").write_text(json.dumps(report, indent=1))


if __name__ == "__main__":
    {"prepare": prepare, "run": run}[sys.argv[1]]()
