"""E1: faithfulness of LLM encodings and dual-encoding verification.

prepare  -> task files for encoders A and B (independent calls, different batch order)
analyze  -> results/e1/records.jsonl and results/e1/summary.json
"""
from __future__ import annotations

import copy
import json
import random
import sys
from pathlib import Path

import z3

from . import llm
from .dsl import DSLError, ZebraSpace, names_in, norm
from .families import zebra as Z
from .prompts import ENCODER, PARAPHRASE

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "configs" / "config.json").read_text())
OUT = ROOT / "results" / "e1"


def load_bank(bank):
    p = ROOT / "data" / "bank" / f"{bank}.jsonl"
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def paraphrased():
    """{puzzle id: [clue texts]} from the paraphrase stage."""
    out = {}
    for rec in llm.manifest("e1_para"):
        res = llm.read_output(rec)
        if not isinstance(res, dict):
            continue
        for p in res.get("puzzles") or []:
            if isinstance(p, dict) and isinstance(p.get("clues"), list):
                out[str(p["id"])] = [str(c) for c in p["clues"]]
    return out


def e1_items(require_para=True):
    """All E1 items: dicts with id, style, spec (texts as shown to encoders), analysis."""
    items = []
    para = paraphrased() if require_para else {}
    for style, c in CFG["e1"]["styles"].items():
        bank = load_bank(c["bank"])[c["ids"][0]:c["ids"][1]]
        for b in bank:
            spec = copy.deepcopy(b["spec"])
            if style == "paraphrase":
                if require_para:
                    texts = para.get(b["id"])
                    if not texts or len(texts) != len(spec["clues"]):
                        continue   # paraphrase missing or misaligned -> excluded (counted in summary)
                    for cl, t in zip(spec["clues"], texts):
                        cl["template_text"] = cl["text"]
                        cl["text"] = t
            items.append({"id": f"{style}:{b['id']}", "style": style, "spec": spec, "analysis": b["analysis"]})
    return items


def puzzle_block(pid, spec):
    return f"## Puzzle {pid}\n\n{Z.render(spec)}\n"


def prepare_paraphrase():
    c = CFG["e1"]["styles"]["paraphrase"]
    bank = load_bank(c["bank"])[c["ids"][0]:c["ids"][1]]
    batch = CFG["e1"]["batch"]
    for b in range(0, len(bank), batch):
        chunk = bank[b:b + batch]
        blocks = "\n".join(puzzle_block(x["id"], x["spec"]) for x in chunk)
        llm.write_task("e1_para", f"e1_para_{b // batch:03d}", CFG["e1"]["paraphrase_model"], PARAPHRASE,
                       blocks, [x["id"] for x in chunk])


def prepare_encoders(encoders=None):
    items = e1_items()
    batch = CFG["e1"]["batch"]
    encs = CFG["e1"]["encoders"]
    for enc in encoders or encs:
        rng = random.Random(f"{CFG['seed']}-e1-{enc}")
        order = list(range(len(items)))
        rng.shuffle(order)       # independent batch composition per encoder; styles mixed
        stage = f"e1_enc{enc}"
        for b in range(0, len(order), batch):
            idx = order[b:b + batch]
            blocks = "\n".join(puzzle_block(items[i]["id"], items[i]["spec"]) for i in idx)
            llm.write_task(stage, f"{stage}_{b // batch:03d}", encs[enc], ENCODER, blocks,
                           [items[i]["id"] for i in idx])
    print("prepared", len(items), "items")


def collect(stage):
    out = {}
    for rec in llm.manifest(stage):
        res = llm.read_output(rec)
        if res is None:
            continue
        for p in (res.get("puzzles") or []) if isinstance(res, dict) else []:
            if isinstance(p, dict) and "id" in p:
                out[str(p["id"]).strip()] = p.get("constraints") or []
    # some encoders drop the "style:" prefix of the id; bank ids are unique across styles
    for k in list(out):
        if ":" not in k:
            for style in ("plain", "hard", "paraphrase"):
                out.setdefault(f"{style}:{k}", out[k])
    return out


# ------------------------------------------------------------------ taxonomy
def confusions(clue, n):
    """Plausible misreadings of a ground-truth clue, as (label, expr)."""
    t, a = clue["type"], clue["args"]
    E = lambda tt, aa: Z.expr_for(tt, aa, n)  # noqa: E731
    out = []
    if t == "left_of":
        out += [("direction flipped", E("left_of", [a[1], a[0]])),
                ("'directly' read as 'somewhere'", E("before", a)),
                ("'directly left' read as 'next to'", E("next_to", a))]
    if t == "before":
        out += [("direction flipped", E("before", [a[1], a[0]])),
                ("'somewhere' read as 'directly'", E("left_of", a)),
                ("'somewhere' read as 'directly'", E("left_of", [a[1], a[0]])),
                ("strict order read as non-strict", f'pos("{a[0]}") <= pos("{a[1]}")')]
    if t == "next_to":
        out += [("'next to' read as directional", E("left_of", a)),
                ("'next to' read as directional", E("left_of", [a[1], a[0]]))]
    if t == "not_next_to":
        out.append(("generator template ambiguity ('at least one house separates' read as distance >= 2)",
                    f'Abs(pos("{a[0]}") - pos("{a[1]}")) >= 2'))
    if t in ("at", "not_at") and n + 1 - a[1] != a[1]:
        out.append(("counting from the right read as counting from the left", E(t, [a[0], n + 1 - a[1]])))
    if t in ("not_same", "not_at", "not_next_to"):
        pos_t = {"not_same": "same", "not_at": "at", "not_next_to": "next_to"}[t]
        out.append(("negation dropped", E(pos_t, a)))
    if t in ("same", "at", "next_to"):
        neg_t = {"same": "not_same", "at": "not_at", "next_to": "not_next_to"}[t]
        out.append(("spurious negation", E(neg_t, a)))
    if t in ("at", "not_at"):
        k = a[1]
        for kk in (k - 1, k + 1):
            if 1 <= kk <= n and kk != k:
                out.append(("wrong house number/ordinal", E(t, [a[0], kk])))
    if t == "gap2":
        out += [("'one house between' misread", f'Abs(pos("{a[0]}") - pos("{a[1]}")) >= 2'),
                ("'one house between' misread", f'Abs(pos("{a[0]}") - pos("{a[1]}")) == 3'),
                ("'one house between' misread", f'Abs(pos("{a[0]}") - pos("{a[1]}")) != 1')]
    if t == "end":
        out += [("'one of the ends' read as one specific end", f'pos("{a[0]}") == 1'),
                ("'one of the ends' read as one specific end", f'pos("{a[0]}") == {n}')]
    if t == "or":
        out += [("either-or misread", E("same", [a[0], a[1]])),
                ("either-or misread", E("same", [a[0], a[2]]))]
    return out


def classify(space, gt_clue, gt_f, enc_expr, n):
    try:
        f = space.formula([enc_expr])
    except DSLError:
        return "invalid expression / unknown name"
    if space.equivalent(f, z3.BoolVal(True)) is True:
        return "vacuous (always true)"
    for label, e in confusions(gt_clue, n):
        if space.equivalent(f, space.formula([e])) is True:
            return label
    if set(names_in(enc_expr)) != set(names_in(gt_clue["expr"])):
        return "wrong entity"
    # implied by / implies the truth
    s1 = space.equivalent(z3.And(f, gt_f), gt_f)  # gt -> f  (f weaker)
    s2 = space.equivalent(z3.And(f, gt_f), f)     # f -> gt  (f stronger)
    if s1 and not s2:
        return "too weak (other)"
    if s2 and not s1:
        return "too strong (other)"
    return "other"


def analyze_puzzle(item, encs):
    spec = item["spec"]
    n = spec["n"]
    space = ZebraSpace(n, spec["cats"])
    gt_exprs = [c["expr"] for c in spec["clues"]]
    gt_f = space.formula(gt_exprs)
    gt_sol = {norm(k): v for k, v in spec["solution"].items()}
    rec = {"id": item["id"], "n_clues": len(gt_exprs), "level": item["analysis"]["level"],
           "clue_types": [c["type"] for c in spec["clues"]]}
    forms = {}
    for name, cons in encs.items():
        r = {"present": cons is not None}
        if cons is None:
            rec[name] = r
            forms[name] = None
            continue
        bynum = {}
        for c in cons:
            try:
                bynum[int(c.get("clue"))] = str(c.get("expr", ""))
            except (TypeError, ValueError, AttributeError):
                pass
        exprs = [bynum.get(i + 1) for i in range(len(gt_exprs))]
        r["n_missing"] = sum(e is None for e in exprs)
        clue_err = []
        parts = []
        valid = True
        for i, e in enumerate(exprs):
            if e is None:
                clue_err.append({"clue": i + 1, "type": spec["clues"][i]["type"], "cat": "missing",
                                 "enc": None, "gt": gt_exprs[i], "text": spec["clues"][i]["text"]})
                valid = False
                continue
            try:
                fi = space.formula([e])
            except DSLError:
                clue_err.append({"clue": i + 1, "type": spec["clues"][i]["type"],
                                 "cat": "invalid expression / unknown name", "enc": e, "gt": gt_exprs[i],
                                 "text": spec["clues"][i]["text"]})
                valid = False
                continue
            parts.append(fi)
            gi = space.formula([gt_exprs[i]])
            if space.equivalent(fi, gi) is not True:
                clue_err.append({"clue": i + 1, "type": spec["clues"][i]["type"],
                                 "cat": classify(space, spec["clues"][i], gi, e, n),
                                 "enc": e, "gt": gt_exprs[i], "text": spec["clues"][i]["text"]})
        r["valid"] = valid
        r["clue_errors"] = clue_err
        f = z3.And(*parts) if parts else z3.BoolVal(True)
        forms[name] = f if valid else None
        eq = space.equivalent(f, gt_f) if valid else False
        r["equiv_gt"] = bool(eq)
        sols = space.solutions(f, limit=2) if valid else []
        r["n_solutions"] = len(sols)
        r["answer_correct"] = len(sols) == 1 and sols[0] == gt_sol
        rec[name] = r
    names = sorted(forms)
    for i, x in enumerate(names):
        for y in names[i + 1:]:
            if forms[x] is not None and forms[y] is not None:
                eq = space.equivalent(forms[x], forms[y])
            else:
                eq = False   # an invalid encoding counts as a disagreement
            rec[f"{x}{y}_equiv"] = bool(eq)
    return rec


def analyze():
    items = e1_items()
    encs = {e: collect(f"e1_enc{e}") for e in CFG["e1"]["encoders"]}
    OUT.mkdir(parents=True, exist_ok=True)
    recs = []
    for it in items:
        if not all(it["id"] in encs[e] for e in encs):
            continue
        r = analyze_puzzle(it, {e: encs[e][it["id"]] for e in encs})
        r["style"] = it["style"]
        recs.append(r)
    with (OUT / "records.jsonl").open("w") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    print("analyzed", len(recs))
    return recs


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "prepare_paraphrase":
        prepare_paraphrase()
    elif cmd == "prepare_encoders":
        prepare_encoders()
    elif cmd == "analyze":
        analyze()
