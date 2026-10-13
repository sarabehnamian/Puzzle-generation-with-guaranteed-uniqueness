"""E4: evolutionary search for fair-but-hard zebra puzzles.

(mu + lambda) evolution.  Fitness = 1 - mean cell accuracy of the training
solver (Haiku) over all of an individual's evaluations (survivors are
re-evaluated every generation, so lucky single evaluations are averaged out).
Mutation = LLM (Sonnet) edit proposals on the formal clue list; every child is
repaired to uniqueness and rejected unless it is fair (ladder level <= 3).

Run ``python -m src.e4_evolution step`` repeatedly; it advances the state as
far as the available LLM outputs allow and writes any new task files.
"""
from __future__ import annotations

import copy
import json
import random
import sys
from pathlib import Path

from . import llm
from .csp import CNF
from .dsl import norm
from .families import zebra as Z
from .generate import complete_to_unique, generate
from .grading import grade
from .prompts import MUTATE
from .solve_stage import collect, make_tasks

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "configs" / "config.json").read_text())
E4 = CFG["e4"]
DATA = ROOT / "data" / "e4"
STATE = DATA / "state.json"
TYPES = set(Z.TYPE_WEIGHTS)


def load():
    return json.loads(STATE.read_text()) if STATE.exists() else None


def save(st):
    DATA.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, indent=1))


def certify(spec):
    from .families import get
    from .csp import count_solutions
    csp, sol = get("zebra").build_csp(spec)
    cnf = CNF(csp)
    sols = count_solutions(cnf, limit=2)
    if len(sols) != 1:
        return None
    return grade(cnf).level


def init():
    rng = random.Random(f"{CFG['seed']}-e4-init")
    pop = []
    i = 0
    while len(pop) < E4["population"]:
        spec = generate("zebra", rng, {"n": 5, "k": 4})
        i += 1
        lev = certify(spec)
        if lev == 3:
            pop.append({"id": f"evo-g0-{len(pop):02d}", "spec": spec, "born": 0, "parent": None,
                        "level": lev, "evals": []})
    st = {"gen": 0, "phase": "eval", "pop": pop, "all": {p["id"]: p for p in pop}, "history": []}
    save(st)
    return st


def fitness(ind):
    if not ind["evals"]:
        return None
    return 1 - sum(ind["evals"]) / len(ind["evals"])


# ------------------------------------------------------------------ mutation
def _valid_clue(spec, c):
    if not isinstance(c, dict) or c.get("type") not in TYPES:
        return None
    args = list(c.get("args") or [])
    vals = {norm(v) for vs in spec["cats"].values() for v in vs}
    out = []
    for a in args:
        if isinstance(a, (int, float)) or (isinstance(a, str) and a.strip().isdigit()):
            out.append(int(a))
        elif isinstance(a, str) and norm(a) in vals:
            out.append(norm(a))
        else:
            return None
    t = c["type"]
    arity = {"at": 2, "not_at": 2, "end": 1, "or": 3}.get(t, 2)
    if len(out) != arity:
        return None
    if t in ("at", "not_at") and not (isinstance(out[1], int) and 1 <= out[1] <= spec["n"]):
        return None
    if t not in ("at", "not_at") and not all(isinstance(x, str) for x in out):
        return None
    try:
        expr = Z.expr_for(t, out, spec["n"])
    except Exception:  # noqa: BLE001
        return None
    from .dsl import eval_concrete
    if not eval_concrete(expr, spec["solution"]):
        return None   # false in the solution
    return {"type": t, "args": out, "expr": expr}


def apply_ops(parent_spec, ops, rng):
    spec = copy.deepcopy(parent_spec)
    clues = list(spec["clues"])
    removed = set()
    n_ok = 0
    for op in ops or []:
        if not isinstance(op, dict):
            continue
        kind = op.get("op")
        try:
            if kind == "remove":
                removed.add(int(op["clue"]) - 1)
                n_ok += 1
            elif kind == "add":
                c = _valid_clue(spec, op.get("clue"))
                if c:
                    clues.append(c)
                    n_ok += 1
            elif kind == "replace":
                j = int(op["clue"]) - 1
                c = _valid_clue(spec, op.get("with"))
                if c and 0 <= j < len(parent_spec["clues"]):
                    removed.add(j)
                    clues.append(c)
                    n_ok += 1
        except (KeyError, ValueError, TypeError):
            continue
    spec["clues"] = [c for j, c in enumerate(clues) if j not in removed]
    return spec, n_ok


def repair_and_check(spec, rng):
    """Restore uniqueness with random true clues; return (spec, level, n_added) or None."""
    from .families import get
    pool = Z.clue_pool(rng, spec)
    full = dict(spec, clues=spec["clues"] + pool)
    csp, sol = get("zebra").build_csp(full)
    cnf = CNF(csp)
    k = len(spec["clues"])
    ids = complete_to_unique(cnf, sol, list(range(k)), list(range(len(full["clues"]))), rng)
    if ids is None:
        return None
    added = [full["clues"][i] for i in ids if i >= k]
    spec = dict(spec, clues=spec["clues"] + added)
    lev = certify(spec)
    if lev is None or lev > E4["max_level"]:
        return None
    rng.shuffle(spec["clues"])
    for c in spec["clues"]:
        c["text"] = Z.render_clue(spec, c, rng)
    return spec, lev, len(added)


def mutation_block(ind, answers):
    spec = ind["spec"]
    lines = [f"## Puzzle {ind['id']}", "", Z.header(spec), "", "Formal clues (with their English text):"]
    for i, c in enumerate(spec["clues"], 1):
        lines.append(f"{i}. {c['type']}({', '.join(str(a) for a in c['args'])})   \"{c['text']}\"")
    sol = spec["solution"]
    by = {}
    for v, h in sol.items():
        by.setdefault(h, []).append(v)
    lines.append("")
    lines.append("Solution: " + "; ".join(f"house {h}: {', '.join(sorted(by[h]))}" for h in sorted(by)))
    wrong = []
    for ans in answers:
        got = Z.parse_answer(spec, ans) if ans else {}
        wrong += [f"{v} (put in house {got.get(v, '?')}, correct {h})" for v, h in sol.items() if got.get(v) != h]
    lines.append("Solver mistakes: " + ("; ".join(sorted(set(wrong))) if wrong else "none - the solver got it fully right"))
    lines.append(f"Solver cell accuracy so far: {1 - fitness(ind):.2f}" if ind["evals"] else "")
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ state machine
def step():
    st = load() or init()
    g = st["gen"]
    if st["phase"] == "eval":
        stage = f"e4_eval_g{g}"
        if not llm.manifest(stage):
            items = [(p["id"], p["spec"]) for p in st["pop"]]
            make_tasks(stage, items, E4["train_solver"], 5, f"{CFG['seed']}-e4-{g}")
            print("wrote eval tasks", stage)
            save(st)
            return
        if llm.pending(stage):
            print("waiting for", stage, len(llm.pending(stage)))
            return
        got = collect(stage)
        for p in st["pop"]:
            ans = got.get((p["id"], E4["train_solver"]))
            s = Z.score(p["spec"], ans) if ans is not None else {"cell_acc": 0.0}
            p["evals"].append(s["cell_acc"])
            p.setdefault("answers", {})[str(g)] = ans
            st["all"][p["id"]] = p
        # (mu + lambda) selection
        st["pop"].sort(key=lambda p: (-fitness(p), len(p["spec"]["clues"])))
        st["pop"] = st["pop"][:E4["population"]]
        fits = [fitness(p) for p in st["pop"]]
        st["history"].append({"gen": g, "fitness": fits, "ids": [p["id"] for p in st["pop"]],
                              "n_evals": [len(p["evals"]) for p in st["pop"]]})
        if g >= E4["generations"]:
            st["phase"] = "done"
            save(st)
            print("evolution finished")
            return
        st["phase"] = "mutate"
        save(st)
    if st["phase"] == "mutate":
        stage = f"e4_mut_g{g}"
        if not llm.manifest(stage):
            C = E4["children_per_parent"]
            per_call = 5
            for b in range(0, len(st["pop"]), per_call):
                chunk = st["pop"][b:b + per_call]
                blocks = "\n".join(mutation_block(p, [p["answers"][str(g)]]) for p in chunk)
                llm.write_task(stage, f"{stage}_{b // per_call}", E4["mutator_model"],
                               MUTATE.replace("{C}", str(C)), blocks, [p["id"] for p in chunk])
            print("wrote mutation tasks", stage)
            return
        if llm.pending(stage):
            print("waiting for", stage)
            return
        rng = random.Random(f"{CFG['seed']}-e4-children-{g}")
        parents = {p["id"]: p for p in st["pop"]}
        kids = []
        log = []
        for rec in llm.manifest(stage):
            res = llm.read_output(rec) or {}
            for v in (res.get("variants") or []) if isinstance(res, dict) else []:
                par = parents.get(str(v.get("parent")))
                if par is None:
                    continue
                spec, n_ok = apply_ops(par["spec"], v.get("ops"), rng)
                out = repair_and_check(spec, rng) if n_ok else None
                entry = {"parent": par["id"], "n_ops_applied": n_ok, "accepted": out is not None,
                         "idea": v.get("idea")}
                if out:
                    cs, lev, added = out
                    kid = {"id": f"evo-g{g + 1}-{len(kids):02d}", "spec": cs, "born": g + 1,
                           "parent": par["id"], "level": lev, "evals": [], "repair_added": added,
                           "idea": v.get("idea")}
                    kids.append(kid)
                    entry["child"] = kid["id"]
                log.append(entry)
        st["history"][-1]["mutation_log"] = log
        st["pop"] = st["pop"] + kids
        for k in kids:
            st["all"][k["id"]] = k
        st["gen"] = g + 1
        st["phase"] = "eval"
        save(st)
        print(f"gen {g + 1}: {len(kids)} children accepted of {len(log)} proposals")
        step()


if __name__ == "__main__":
    step()
