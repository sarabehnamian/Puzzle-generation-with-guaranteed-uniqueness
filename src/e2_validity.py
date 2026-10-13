"""E2: validity of raw LLM-generated puzzles, with and without the solver loop.

Stages
  gen        LLM writes puzzles with an intended solution (no solver).
  enc        zebra only: dual encoding of the generated text (A, B), as in E1.
  repair1/2  LLM revises invalid puzzles given solver feedback.
  complete   programmatic completion (add/remove clues) -> certified puzzles.

A puzzle is *valid* if (i) it parses, (ii) it has exactly one solution,
(iii) that solution is the intended one, and (iv) it is fair (ladder level <= 3).
"""
from __future__ import annotations

import copy
import json
import random
import re
import sys
from pathlib import Path

from . import llm
from .csp import CNF, count_solutions
from .dsl import DSLError, ZebraSpace, norm
from .families import get
from .families import zebra as Z
from .grading import grade, mus_for_literal
from .prompts import ENCODER, GEN, REPAIR

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "configs" / "config.json").read_text())
OUT = ROOT / "results" / "e2"
FAMS = ["zebra", "sudoku", "killer", "futoshiki"]
SIZES = {"sudoku": (9, [3, 3]), "killer": (6, [2, 3]), "futoshiki": (5, None)}
CELL = re.compile(r"R(\d+)\s*C(\d+)", re.I)


# ------------------------------------------------------------------ prepare
def prepare_gen():
    per = CFG["e2"]["per_family"]
    k = CFG["e2"]["batch"]
    for fam in FAMS:
        for b in range(per[fam] // k):
            instr = GEN[fam].replace("{K}", str(k))
            llm.write_task("e2_gen", f"e2_gen_{fam}_{b}", CFG["e2"]["generator_model"], instr, "",
                           [f"{fam}/{b}/g{i + 1}" for i in range(k)])


def raw_puzzles(stage="e2_gen"):
    """{uid: raw dict} with uid = family/batch/id."""
    out = {}
    for rec in llm.manifest(stage):
        res = llm.read_output(rec)
        if not isinstance(res, dict):
            continue
        prefix = rec["call_id"].split("_")
        fam = prefix[2]
        b = prefix[3]
        for p in res.get("puzzles") or []:
            if isinstance(p, dict) and "id" in p:
                uid = p.get("_uid") or f"{fam}/{b}/{p['id']}"
                out[uid] = p
    return out


# ------------------------------------------------------------------ parsing
def _grid(rows, n, blanks_ok):
    if not isinstance(rows, list) or len(rows) != n:
        raise ValueError("bad grid shape")
    g = []
    for row in rows:
        row = str(row).replace(" ", "").replace("|", "")
        if len(row) != n:
            raise ValueError("bad row length")
        out = []
        for ch in row:
            if ch.isdigit() and 1 <= int(ch) <= n:
                out.append(int(ch))
            elif blanks_ok and ch in ".0_-x*":
                out.append(0)
            else:
                raise ValueError(f"bad char {ch!r}")
        g.append(out)
    return g


def _cell(s, n):
    m = CELL.search(str(s))
    if not m:
        raise ValueError(f"bad cell {s!r}")
    r, c = int(m.group(1)) - 1, int(m.group(2)) - 1
    if not (0 <= r < n and 0 <= c < n):
        raise ValueError("cell out of range")
    return [r, c]


def to_spec(fam, raw, encoding=None):
    """Raw LLM puzzle -> family spec with intended solution.  Raises on malformed input."""
    if fam == "zebra":
        cats = raw["categories"]
        if not isinstance(cats, dict) or len(cats) < 2:
            raise ValueError("bad categories")
        n = len(next(iter(cats.values())))
        if any(len(v) != n for v in cats.values()):
            raise ValueError("unequal category sizes")
        names = [norm(v) for vals in cats.values() for v in vals]
        if len(set(names)) != len(names):
            raise ValueError("duplicate value names")
        sol = {}
        for h, row in raw["solution"].items():
            for c, v in row.items():
                sol[norm(str(v))] = int(re.sub(r"\D", "", str(h)))
        if set(sol) != set(names):
            raise ValueError("solution does not cover all values")
        clues = [{"text": t} for t in raw["clues"]]
        spec = {"family": "zebra", "n": n, "cats": {c: [str(v) for v in vals] for c, vals in cats.items()},
                "solution": sol, "clues": clues}
        if encoding is not None:
            for c, e in zip(spec["clues"], encoding):
                c["expr"] = e
        return spec
    n, box = SIZES[fam]
    sol = _grid(raw["solution"], n, False)
    spec = {"family": fam, "n": n, "solution": sol, "clues": []}
    if box:
        spec["box"] = box
    if fam == "sudoku":
        g = _grid(raw["grid"], n, True)
    else:
        g = _grid(raw["givens"], n, True) if raw.get("givens") else [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if g[r][c]:
                spec["clues"].append({"type": "given", "cell": [r, c], "value": g[r][c]})
    if fam == "killer":
        for cage in raw["cages"]:
            cells = [_cell(x, n) for x in cage["cells"]]
            spec["clues"].append({"type": "cage", "cells": cells, "sum": int(cage["sum"])})
    if fam == "futoshiki":
        for s in raw["inequalities"]:
            s = str(s)
            if "<" in s:
                a, b = s.split("<", 1)
                spec["clues"].append({"type": "lt", "a": _cell(a, n), "b": _cell(b, n)})
            elif ">" in s:
                a, b = s.split(">", 1)
                spec["clues"].append({"type": "lt", "a": _cell(b, n), "b": _cell(a, n)})
            else:
                raise ValueError("bad inequality")
    return spec


# ------------------------------------------------------------------ checking
def check(spec):
    """Validity verdict plus solver feedback text for the repair prompt."""
    fam = get(spec["family"])
    try:
        csp, sol = fam.build_csp(spec)
    except (DSLError, KeyError, ValueError) as e:
        return {"stage": "encode", "valid": False, "feedback": f"could not be encoded: {e}"}
    cnf = CNF(csp)
    res = {"n_clues": len(spec["clues"])}
    # which clues does the intended solution violate?
    viol = []
    rules_ok = True
    for c in csp.rules:
        vals = [sol[v] for v in c.scope]
        if len(set(vals)) != len(vals):
            rules_ok = False
    for j, c in enumerate(csp.clues):
        if not c.pred(*[sol[v] for v in c.scope]):
            viol.append(j)
    res["intended_rules_ok"] = rules_ok
    res["intended_violates"] = viol
    sols = count_solutions(cnf, limit=2)
    res["n_solutions"] = len(sols) if len(sols) < 2 else 2
    res["unique"] = len(sols) == 1
    res["matches_intended"] = res["unique"] and sols[0] == sol
    fb = []
    if not rules_ok:
        fb.append("Your stated solution breaks the basic rules of the puzzle (a repeated value).")
    if viol:
        fb.append("Your stated solution violates these clues: " + ", ".join(_clue_name(spec, j) for j in viol) + ".")
    if len(sols) == 0:
        # explain the contradiction with a minimal conflicting clue set
        from .csp import ClueSolver
        cs = ClueSolver(cnf)
        ids = list(range(len(csp.clues)))
        cs.solve(ids)
        core = sorted({j for j in ids if cs.sel[j] in set(cs.solver.get_core() or [])})
        cs.delete()
        fb.append("The puzzle has NO solution. These clues contradict each other: "
                  + ", ".join(_clue_name(spec, j) for j in core) + ".")
    elif len(sols) >= 2:
        other = sols[1] if sols[0] == sol else sols[0]
        fb.append("The puzzle has MORE THAN ONE solution. Another solution besides yours is:\n"
                  + _show(spec, csp, other))
    if res["unique"]:
        g = grade(cnf)
        res["level"] = g.level
        res["fair"] = g.level <= 3
        if not res["fair"]:
            fb.append(f"The puzzle cannot be solved without guessing or deep trial-and-error "
                      f"(difficulty level L{g.level}); add or change clues so it can be solved by "
                      f"direct deduction.")
    res["valid"] = bool(res["matches_intended"] and res.get("fair", False))
    res["feedback"] = " ".join(fb) if fb else "ok"
    return res


def _clue_name(spec, j):
    c = spec["clues"][j]
    if spec["family"] == "zebra":
        return f"clue {j + 1} (\"{c.get('text', '')}\")"
    if c["type"] == "given":
        return f"given digit {c['value']} at R{c['cell'][0] + 1}C{c['cell'][1] + 1}"
    if c["type"] == "cage":
        return "cage " + "+".join(f"R{r + 1}C{cc + 1}" for r, cc in c["cells"]) + f" = {c['sum']}"
    return f"R{c['a'][0] + 1}C{c['a'][1] + 1} < R{c['b'][0] + 1}C{c['b'][1] + 1}"


def _show(spec, csp, labels):
    if spec["family"] == "zebra":
        by = {}
        for name, h in zip(csp.names, labels):
            by.setdefault(h, []).append(name)
        return "; ".join(f"house {h}: " + ", ".join(sorted(by[h])) for h in sorted(by))
    n = spec["n"]
    return "\n".join("".join(str(labels[r * n + c]) for c in range(n)) for r in range(n))


# ------------------------------------------------------------------ zebra encoding
def prepare_enc(stage_in, stage_out, uids=None):
    raws = raw_puzzles(stage_in)
    zs = [(u, p) for u, p in sorted(raws.items()) if u.startswith("zebra/") and (uids is None or u in uids)]
    blocks = []
    ok = []
    for u, p in zs:
        try:
            spec = to_spec("zebra", p)
        except Exception:  # noqa: BLE001
            continue
        for i, c in enumerate(spec["clues"]):
            c["text"] = str(c["text"])
        blocks.append(f"## Puzzle {u}\n\n{Z.render(spec)}\n")
        ok.append(u)
    batch = 10
    for enc in ("A", "B"):
        order = list(range(len(ok)))
        random.Random(f"{CFG['seed']}-{stage_out}-{enc}").shuffle(order)
        for b in range(0, len(order), batch):
            idx = order[b:b + batch]
            llm.write_task(f"{stage_out}_enc{enc}", f"{stage_out}_enc{enc}_{b // batch:03d}", "sonnet", ENCODER,
                           "\n".join(blocks[i] for i in idx), [ok[i] for i in idx])


def encodings(stage):
    from .e1_faithfulness import collect
    return collect(stage)


def zebra_encoding(spec, encA, encB):
    """Return (exprs or None, status) after the dual-encoding check."""
    k = len(spec["clues"])

    def exprs(cons):
        by = {}
        for c in cons or []:
            try:
                by[int(c.get("clue"))] = str(c.get("expr"))
            except (TypeError, ValueError, AttributeError):
                pass
        return [by.get(i + 1) for i in range(k)]

    a, b = exprs(encA), exprs(encB)
    if None in a or None in b:
        return None, "encoding incomplete"
    sp = ZebraSpace(spec["n"], spec["cats"])
    try:
        fa, fb = sp.formula(a), sp.formula(b)
    except DSLError:
        return None, "encoding invalid"
    if sp.equivalent(fa, fb) is not True:
        return None, "encodings disagree"
    return a, "agreed"


# ------------------------------------------------------------------ evaluate a round
def evaluate(stage_gen, stage_enc=None):
    raws = raw_puzzles(stage_gen)
    encA = encodings(f"{stage_enc}_encA") if stage_enc else {}
    encB = encodings(f"{stage_enc}_encB") if stage_enc else {}
    rows = {}
    for uid, raw in sorted(raws.items()):
        fam = uid.split("/")[0]
        row = {"uid": uid, "family": fam}
        try:
            spec = to_spec(fam, raw)
        except Exception as e:  # noqa: BLE001
            row.update({"parsed": False, "valid": False, "feedback": f"malformed puzzle: {e}"})
            rows[uid] = row
            continue
        row["parsed"] = True
        if fam == "zebra":
            ex, status = zebra_encoding(spec, encA.get(uid), encB.get(uid))
            row["encoding"] = status
            if ex is None:
                row.update({"valid": False, "feedback": "(not checked: " + status + ")"})
                rows[uid] = row
                continue
            for c, e in zip(spec["clues"], ex):
                c["expr"] = e
        row.update(check(spec))
        row["spec"] = spec
        rows[uid] = row
    return rows


def prepare_repair(rows, stage_out):
    bad = [r for r in rows.values() if not r["valid"] and r.get("parsed")
           and not str(r.get("feedback", "")).startswith("(not checked")]
    raws = {}
    for st in ("e2_gen", "e2_repair1", "e2_repair2"):
        raws.update(raw_puzzles(st)) if llm.manifest(st) else None
    batch = 10
    by_fam = {}
    for r in bad:
        by_fam.setdefault(r["family"], []).append(r)
    for fam, rs in by_fam.items():
        for b in range(0, len(rs), batch):
            chunk = rs[b:b + batch]
            blocks = []
            for r in chunk:
                orig = dict(raws[r["uid"]])
                orig["_uid"] = r["uid"]
                blocks.append(f"## Puzzle {r['uid']}\n\nOriginal puzzle (JSON):\n{json.dumps(orig, indent=1)}\n\n"
                              f"Solver feedback: {r['feedback']}\n")
            llm.write_task(stage_out, f"{stage_out}_{fam}_{b // batch}", "sonnet",
                           REPAIR + "\nKeep the field \"_uid\" unchanged in each revised puzzle.\n",
                           "\n".join(blocks), [r["uid"] for r in chunk])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "prepare_gen":
        prepare_gen()
    elif cmd == "prepare_enc":            # dual encodings of the zebra puzzles
        prepare_enc("e2_gen", "e2_enc")
    elif cmd == "prepare_repair1":        # one round of solver feedback
        prepare_repair(evaluate("e2_gen", "e2_enc"), "e2_repair1")


# ------------------------------------------------------------------ summary
WIKI_MASK = "xx..x....x..xxx....xx....x.x...x...xx..x.x..xx...x...x.x....xx....xxx..x....x..xx"


def _mask(rows):
    return "".join("x" if ch.isdigit() and ch != "0" else "." for row in rows for ch in str(row))


def summarize():
    """Validity before/after each loop stage plus redundancy, level and duplication."""
    from .csp import CNF
    from .generate import minimize
    from .grading import grade, redundancy
    OUT.mkdir(parents=True, exist_ok=True)
    rows = evaluate("e2_gen", "e2_enc")
    repaired = {}
    for k, st, enc in (("repair1", "e2_repair1", "e2_rep1enc"),):
        if llm.manifest(st):
            repaired[k] = evaluate(st, enc if llm.manifest(f"{enc}_encA") else None)
    recs = []
    for uid, r in sorted(rows.items()):
        rec = {k: r.get(k) for k in ("uid", "family", "parsed", "valid", "unique", "matches_intended", "level",
                                     "fair", "n_solutions", "n_clues", "encoding", "feedback")}
        rec["intended_violates"] = len(r.get("intended_violates") or [])
        for k, rr in repaired.items():
            if uid in rr:
                rec[f"{k}_valid"] = rr[uid]["valid"]
        if r.get("unique"):
            spec = r["spec"]
            csp, _ = get(spec["family"]).build_csp(spec)
            cnf = CNF(csp)
            sol = count_solutions(cnf, limit=1)[0]   # the unique solution (may differ from the stated one)
            ids = list(range(len(csp.clues)))
            rec["redundancy"] = redundancy(cnf, ids)
            # the solver loop: minimise the LLM's puzzle in a fixed random order
            order = list(ids)
            random.Random(f"{CFG['seed']}-{uid}").shuffle(order)
            mini = minimize(cnf, sol, ids, order)
            rec["n_clues_min"] = len(mini)
            rec["level_min"] = grade(cnf, clue_ids=mini).level
        recs.append(rec)
    raws = raw_puzzles("e2_gen")
    dup = {}
    for fam in ("sudoku", "futoshiki"):
        key = "grid" if fam == "sudoku" else "givens"
        masks = [_mask(p.get(key) or []) for u, p in raws.items() if u.startswith(fam)]
        import collections
        c = collections.Counter(masks)
        dup[fam] = {"n": len(masks), "distinct_masks": len(c), "largest_mask_group": max(c.values()) if c else 0}
    sud = [p for u, p in raws.items() if u.startswith("sudoku")]
    dup["sudoku"]["wikipedia_mask"] = sum(_mask(p["grid"]) == WIKI_MASK for p in sud)
    dup["sudoku"]["wikipedia_identical"] = sum(
        [str(r) for r in p["grid"]] == ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
                                       "7...2...6", ".6....28.", "...419..5", "....8..79"] for p in sud)
    (OUT / "records.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs))
    summ = {"by_family": {}, "duplication": dup}
    import statistics as st
    for fam in FAMS:
        rs = [r for r in recs if r["family"] == fam]
        if not rs:
            continue
        ok = [r for r in rs if r.get("unique")]
        summ["by_family"][fam] = {
            "n": len(rs), "parsed": sum(bool(r["parsed"]) for r in rs),
            "unique": sum(bool(r.get("unique")) for r in rs),
            "matches_intended": sum(bool(r.get("matches_intended")) for r in rs),
            "valid_raw": sum(bool(r["valid"]) for r in rs),
            "valid_after_repair1": sum(bool(r["valid"] or r.get("repair1_valid")) for r in rs),
            "encoding_disputed": sum(1 for r in rs if r.get("encoding") not in (None, "agreed")),
            "levels": {str(l): sum(1 for r in ok if r.get("level") == l) for l in range(1, 6)},
            "levels_after_min": {str(l): sum(1 for r in ok if r.get("level_min") == l) for l in range(1, 6)},
            "redundancy_mean": st.mean([r["redundancy"] for r in ok]) if ok else None,
            "clues_mean": st.mean([r["n_clues"] for r in ok]) if ok else None,
            "clues_min_mean": st.mean([r["n_clues_min"] for r in ok]) if ok else None,
        }
    (OUT / "summary.json").write_text(json.dumps(summ, indent=1))
    return summ


if __name__ == "__main__" and sys.argv[1] == "summarize":
    print(json.dumps(summarize(), indent=1))
