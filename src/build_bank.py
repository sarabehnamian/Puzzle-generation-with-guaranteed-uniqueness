"""Stage 0: certified puzzle bank (no LLM).  Output: data/bank/<family>.jsonl"""
from __future__ import annotations

import json
import random
import sys
from multiprocessing import Pool
from pathlib import Path

from .analyze import analyze
from .generate import generate

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "configs" / "config.json").read_text())


def _one(args):
    bank, family, i, params, seed = args
    rng = random.Random(f"{seed}-{bank}-{i}")
    spec = generate(family, rng, params)
    a = analyze(spec, explain=False)
    a.pop("mus_sizes", None)
    return {"id": f"{bank}-{i:05d}", "spec": spec, "analysis": a}


def build(bank, n=None, procs=4):
    c = CFG["bank"][bank]
    family = c.get("family", bank)
    n = n or c["n_puzzles"]
    out = ROOT / "data" / "bank" / f"{bank}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if out.exists():
        done = {json.loads(l)["id"] for l in out.read_text().splitlines() if l.strip()}
    todo = [(bank, family, i, c["params"], CFG["seed"]) for i in range(n) if f"{bank}-{i:05d}" not in done]
    with Pool(procs) as p, out.open("a") as f:
        for rec in p.imap(_one, todo, chunksize=4):
            f.write(json.dumps(rec) + "\n")
            f.flush()
    print(bank, "done", len(todo), "new")


if __name__ == "__main__":
    for fam in sys.argv[1:] or list(CFG["bank"]):
        build(fam)
