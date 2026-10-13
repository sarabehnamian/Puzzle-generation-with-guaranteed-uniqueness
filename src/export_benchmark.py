"""Build the benchmark release in benchmark/.

Items: the E3 evaluation set, plus extra certified puzzles drawn from the
banks (disjoint from E1/E3), plus evolved puzzles from E4 if present.  Every
item is re-certified (SAT and CP-SAT uniqueness), graded, and given minimal
unsatisfiable-core explanations for every non-given fact.
"""
import json
import random
import sys
from multiprocessing import Pool
from pathlib import Path

from .analyze import analyze
from .csp import CNF, ClueSolver
from .families import get
from .grading import mus_for_literal

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "configs" / "config.json").read_text())
OUT = ROOT / "benchmark"
EXTRA_PER_LEVEL = 10


def explain(spec):
    fam = get(spec["family"])
    csp, sol = fam.build_csp(spec)
    cnf = CNF(csp)
    cs = ClueSolver(cnf)
    ids = list(range(len(csp.clues)))
    given_vars = set()
    for c in csp.clues:
        if c.meta.get("type") == "given":
            given_vars.update(c.scope)
    out = []
    for v, x in enumerate(cnf.solution_lits(sol)):
        if v in given_vars:
            continue
        mus = mus_for_literal(cs, ids, x)
        out.append({"fact": f"{csp.names[v]} = {sol[v]}", "clues": [i + 1 for i in mus]})
    cs.delete()
    return out


def clue_list(spec):
    f = spec["family"]
    if f == "zebra":
        return [{"n": i + 1, "text": c["text"], "dsl": c["expr"]} for i, c in enumerate(spec["clues"])]
    return [dict(c, n=i + 1) for i, c in enumerate(spec["clues"])]


def build_item(args):
    pid, spec, source = args
    fam = get(spec["family"])
    a = analyze(spec, explain=True, with_redundancy=True)
    assert a["unique"] and a["cpsat_unique"], pid
    sizes = a.pop("mus_sizes")
    text = fam.render(spec)
    if spec["family"] == "zebra":
        text = fam.rules_text(spec) + "\n\n" + text
    return {
        "id": pid, "family": spec["family"], "source": source, "prompt": text,
        "answer_format": fam.ANSWER_FORMAT, "clues": clue_list(spec), "solution": spec["solution"],
        "level": a["level"],
        "certificate": {"unique_sat_minisat": a["unique"], "unique_cpsat": a["cpsat_unique"],
                        "solutions_found_after_blocking": 0},
        "metrics": {k: a[k] for k in ("n_clues", "conflicts_total", "decisions_total", "propagations_total",
                                      "mus_mean", "mus_max", "redundancy")} | {"closure_after_level": a["frac_after"]},
        "explanations": explain(spec), "spec": spec,
    }


def main():
    OUT.mkdir(exist_ok=True)
    items = []
    e3 = [json.loads(l) for l in (ROOT / "data/e3/puzzles.jsonl").read_text().splitlines() if l.strip()]
    used = {p["id"] for p in e3}
    for p in e3:
        items.append((p["id"], p["spec"], "e3-" + p["source"]))
    rng = random.Random(f"{CFG['seed']}-benchmark")
    for fam, bank in [("zebra", "zebra"), ("sudoku", "sudoku"), ("killer", "killer"), ("futoshiki", "futoshiki")]:
        recs = [json.loads(l) for l in (ROOT / "data/bank" / f"{bank}.jsonl").read_text().splitlines() if l.strip()]
        recs = [r for r in recs if r["id"] not in used and not (fam == "zebra" and int(r["id"].split("-")[-1]) < 200)]
        rng.shuffle(recs)
        by = {}
        for r in recs:
            by.setdefault(r["analysis"]["level"], []).append(r)
        for lev, rs in sorted(by.items()):
            for r in rs[:EXTRA_PER_LEVEL]:
                items.append((r["id"], r["spec"], "bank"))
    st = ROOT / "data" / CFG["e4"].get("run", "e4") / "state.json"
    if st.exists():
        s = json.loads(st.read_text())
        for p in s["pop"]:
            items.append((p["id"], p["spec"], "e4-evolved-final"))
    with Pool(4) as pool:
        built = pool.map(build_item, items, chunksize=2)
    with (OUT / "puzzles.jsonl").open("w") as f:
        for b in built:
            f.write(json.dumps(b) + "\n")
    import collections
    c = collections.Counter((b["family"], b["level"]) for b in built)
    summary = {"n_items": len(built), "by_family_level": {f"{k[0]}|L{k[1]}": v for k, v in sorted(c.items())}}
    (OUT / "summary.json").write_text(json.dumps(summary, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
