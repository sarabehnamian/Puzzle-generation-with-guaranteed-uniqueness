"""Generic LLM-solving stage: write solver task files and score the answers."""
from __future__ import annotations

import random

from . import llm
from .families import get
from .prompts import SOLVER_HEAD


def puzzle_block(pid, spec):
    fam = get(spec["family"])
    text = fam.render(spec)
    if spec["family"] == "zebra":
        text = fam.rules_text(spec) + "\n\n" + text
    return f"## Puzzle {pid}\n\n{text}\n\nAnswer format for this puzzle: {fam.ANSWER_FORMAT}\n"


def make_tasks(stage, items, model, batch, seed, prefix=None):
    """items: list of (pid, spec).  Batches are shuffled but identical across models."""
    order = list(range(len(items)))
    random.Random(seed).shuffle(order)
    prefix = prefix or stage
    recs = []
    for b in range(0, len(order), batch):
        idx = order[b:b + batch]
        blocks = "\n".join(puzzle_block(items[i][0], items[i][1]) for i in idx)
        recs.append(llm.write_task(stage, f"{prefix}_{model}_{b // batch:03d}", model, SOLVER_HEAD, blocks,
                                   [items[i][0] for i in idx]))
    return recs


def collect(stage):
    """Return {(pid, model): answer} for every finished call of a stage."""
    out = {}
    for rec in llm.manifest(stage):
        res = llm.read_output(rec)
        if not isinstance(res, dict):
            continue
        answers = res.get("answers") or []
        got = {}
        for a in answers:
            if isinstance(a, dict) and "id" in a:
                got[str(a["id"])] = a.get("answer")
        for pid in rec["items"]:
            out[(pid, rec["model"])] = got.get(pid, None)
    return out


def score_all(stage, specs):
    """specs: {pid: spec}.  Returns list of score records."""
    rows = []
    for (pid, model), ans in collect(stage).items():
        if pid not in specs:
            continue
        spec = specs[pid]
        fam = get(spec["family"])
        if ans is None:
            s = {"cell_acc": 0.0, "exact": False}
        else:
            try:
                s = fam.score(spec, ans)
            except Exception:  # noqa: BLE001 - malformed answers score zero
                s = {"cell_acc": 0.0, "exact": False}
        rows.append({"id": pid, "model": model, "answered": ans is not None, **s})
    return rows
