"""E3: difficulty ladder vs solver metrics vs LLM accuracy.

select   -> data/e3/puzzles.jsonl (stratified by family x level, full metrics)
prepare  -> solver task files for every model
score    -> results/e3/scores.jsonl
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

from .analyze import analyze
from .augment import augment_to_level
from .solve_stage import make_tasks, score_all

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "configs" / "config.json").read_text())
DATA = ROOT / "data" / "e3"
OUT = ROOT / "results" / "e3"

BANKS = {"zebra": ["zebra"], "sudoku": ["sudoku", "sudoku_x"], "killer": ["killer"], "futoshiki": ["futoshiki"]}
EXCLUDE_PREFIX = {"zebra": 200}   # zebra-00000..00199 are used in E1


def load(bank):
    p = ROOT / "data" / "bank" / f"{bank}.jsonl"
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def select():
    k = CFG["e3"]["per_level_per_family"]
    rng = random.Random(f"{CFG['seed']}-e3")
    DATA.mkdir(parents=True, exist_ok=True)
    out = []
    for fam, banks in BANKS.items():
        recs = []
        for b in banks:
            recs += load(b)
        lo = EXCLUDE_PREFIX.get(fam, 0)
        recs = [r for r in recs if int(r["id"].split("-")[-1]) >= lo or not r["id"].startswith(fam + "-")]
        rng.shuffle(recs)
        by = {}
        for r in recs:
            by.setdefault(r["analysis"]["level"], []).append(r)
        for lev in range(1, 6):
            chosen = by.get(lev, [])[:k]
            for r in chosen:
                out.append({"id": r["id"], "family": fam, "spec": r["spec"], "source": "minimal"})
            if lev == 1 and len(chosen) < k:
                # minimal puzzles of this family rarely sit at L1: add redundant true clues
                donors = by.get(2, [])[k:] + by.get(3, [])[k:]
                made = 0
                for d in donors:
                    if made >= k - len(chosen):
                        break
                    s = augment_to_level(d["spec"], 1, random.Random(f"{CFG['seed']}-aug-{d['id']}"))
                    if s is not None:
                        out.append({"id": d["id"] + "-L1aug", "family": fam, "spec": s, "source": "augmented"})
                        made += 1
    with (DATA / "puzzles.jsonl").open("w") as f:
        for i, it in enumerate(out):
            a = analyze(it["spec"], explain=True, with_redundancy=True)
            a.pop("mus_sizes", None)
            assert a["unique"] and a["cpsat_unique"], it["id"]
            it["analysis"] = a
            f.write(json.dumps(it) + "\n")
            print(i, it["id"], a["level"], flush=True)
    return out


def items():
    return [json.loads(l) for l in (DATA / "puzzles.jsonl").read_text().splitlines() if l.strip()]


def prepare(models=None):
    its = items()
    pairs = [(it["id"], it["spec"]) for it in its]
    for m in models or CFG["e3"]["solver_models"]:
        for fam in BANKS:
            sub = [p for p, it in zip(pairs, its) if it["family"] == fam]
            make_tasks("e3_solve", sub, m, CFG["e3"]["batch"], f"{CFG['seed']}-e3-{fam}", prefix=f"e3_{fam}")


def score():
    its = items()
    specs = {it["id"]: it["spec"] for it in its}
    rows = score_all("e3_solve", specs)
    meta = {it["id"]: it for it in its}
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "scores.jsonl").open("w") as f:
        for r in rows:
            it = meta[r["id"]]
            r.update({"family": it["family"], "level": it["analysis"]["level"], "source": it["source"]})
            f.write(json.dumps(r) + "\n")
    print("scored", len(rows))


if __name__ == "__main__":
    {"select": select, "prepare": prepare, "score": score}[sys.argv[1]]()
