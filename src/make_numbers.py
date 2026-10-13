"""Write paper/numbers.tex and paper/tables/*.tex from saved results.

Every number quoted in the manuscript comes from this file.
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "results"
PAPER = ROOT / "paper"
FAMS = ["zebra", "sudoku", "killer", "futoshiki"]
FNAME = {"zebra": "Zebra", "sudoku": "Sudoku", "killer": "Killer", "futoshiki": "Futoshiki"}
MODELS = ["haiku", "sonnet", "opus"]
MNAME = {"haiku": "Haiku", "sonnet": "Sonnet", "opus": "Opus"}

macros = {}


def J(p):
    return json.loads((R / p).read_text())


def put(name, val):
    assert name.isalpha(), name
    macros[name] = val


def pct(x, d=0):
    return f"{100 * x:.{d}f}"


def ci(t, d=0):
    return f"{pct(t[0], d)}\\% [{pct(t[1], d)}, {pct(t[2], d)}]"


def word(i):
    return "ABCDEFGHIJ"[i]


def main():
    # ---- cost / ledger -------------------------------------------------
    C = J("cost_summary.json")
    put("NCalls", f"{C['total']['calls']}")
    put("NViolations", f"{C['total']['tool_use_violations']}")
    put("TokensM", f"{C['total']['tokens'] / 1e6:.1f}")
    put("CostUSD", f"{C['total']['usd']:.0f}")
    for m in MODELS:
        d = C["by_model"].get(m, {"calls": 0, "usd": 0, "tokens": 0})
        put(f"Calls{MNAME[m]}", f"{d['calls']}")
        put(f"Cost{MNAME[m]}", f"{d['usd']:.0f}")
    for e, d in C["by_experiment"].items():
        tag = {"e1": "EOne", "e2": "ETwo", "e3": "EThree", "e4": "EFour", "e5": "EFive",
               "probe": "Probe", "pilot": "Pilot"}.get(e)
        if tag:
            put(f"Calls{tag}", f"{d['calls']}")
            put(f"Cost{tag}", f"{d['usd']:.1f}")
    TA = J("tool_audit.json")
    put("NAudited", f"{TA['n_matched']}")
    put("NForbidden", f"{TA['n_with_forbidden_tool']}")
    n_extra_write = sum(1 for r in TA["over_3_explained"] if not r["forbidden"])
    put("NExtraWrite", f"{n_extra_write}")
    put("NEditOwn", f"{sum(1 for r in TA['over_3_explained'] if r['forbidden'] == ['Edit'])}")

    # ---- banks ---------------------------------------------------------
    B = J("bank_stats.json")
    for k in ["zebra", "sudoku", "killer", "futoshiki", "zebra_hard", "sudoku_x"]:
        tag = {"zebra_hard": "ZebraHard", "sudoku_x": "SudokuX"}.get(k, FNAME.get(k))
        for l in range(1, 6):
            put(f"Bank{tag}L{word(l - 1)}", f"{B[k]['levels'].get(str(l), 0):,}".replace(",", "{,}"))
        put(f"Bank{tag}Clues", f"{B[k]['clues_mean']:.1f}")
    rows = []
    for k in FAMS:
        lv = B[k]["levels"]
        rows.append(f"{FNAME[k]} & {B[k]['n']:,} & " + " & ".join(str(lv.get(str(l), 0)) for l in range(1, 6))
                    + f" & {B[k]['clues_mean']:.1f} \\\\")
    k = "sudoku_x"
    lv = B[k]["levels"]
    rows.append(f"Sudoku (extra) & {B[k]['n']:,} & " + " & ".join(str(lv.get(str(l), 0)) for l in range(1, 6))
                + f" & {B[k]['clues_mean']:.1f} \\\\")
    k = "zebra_hard"
    lv = B[k]["levels"]
    rows.append(f"Zebra (hard text) & {B[k]['n']:,} & " + " & ".join(str(lv.get(str(l), 0)) for l in range(1, 6))
                + f" & {B[k]['clues_mean']:.1f} \\\\")
    table("bank", rows)

    # ---- E1 --------------------------------------------------------------
    E1 = J("e1/summary.json")
    put("EOneN", f"{E1['n_puzzles']}")
    rows = []
    for st, sname in [("plain", "Plain"), ("hard", "Hard"), ("paraphrase", "Para")]:
        S = E1["styles"][st]
        put(f"EOne{sname}N", f"{S['n']}")
        put(f"EOne{sname}Clues", f"{S['n_clues']:,}".replace(",", "{,}"))
        cells = []
        for enc in "ABC":
            e = S[enc]
            put(f"EOne{sname}Err{enc}", ci(e["puzzle_error"]))
            put(f"EOne{sname}ErrN{enc}", f"{round(e['puzzle_error'][0] * S['n'])}")
            put(f"EOne{sname}Clue{enc}", f"{e['clue_errors']}")
            cells.append(f"{round(e['puzzle_error'][0] * S['n'])} ({e['clue_errors']})")
        for pair in ["AB", "AC", "BC"]:
            p = S[pair]
            put(f"EOne{sname}Dis{pair}", ci(p["disagreement"]))
            put(f"EOne{sname}Det{pair}", f"{p['detected']}")
            put(f"EOne{sname}Miss{pair}", f"{p['undetected_shared_error']}")
            put(f"EOne{sname}With{pair}", f"{p['n_with_error']}")
            cells.append(f"{round(p['disagreement'][0] * S['n'])} ({p['detected']}/{p['n_with_error']})")
        rows.append(f"{ {'plain': 'Plain templates', 'hard': 'Hard templates', 'paraphrase': 'LLM paraphrase'}[st]} "
                    f"& {S['n']} & " + " & ".join(cells) + " \\\\")
    table("e1", rows)
    tax = Counter()
    for k, d in E1["taxonomy"].items():
        for cat, n in d.items():
            tax[cat] += n
    put("EOneTaxTooStrong", f"{tax.get('too strong (other)', 0)}")

    # ---- E2 --------------------------------------------------------------
    E2 = J("e2/summary.json")
    tot = {"n": 0, "valid_raw": 0, "valid_after_repair1": 0, "unique": 0, "matches_intended": 0}
    rows = []
    for f in FAMS:
        S = E2["by_family"][f]
        for k in tot:
            tot[k] += S[k]
        put(f"ETwo{FNAME[f]}N", f"{S['n']}")
        put(f"ETwo{FNAME[f]}Valid", f"{S['valid_raw']}")
        put(f"ETwo{FNAME[f]}Red", f"{S['redundancy_mean']:.2f}")
        put(f"ETwo{FNAME[f]}Clues", f"{S['clues_mean']:.1f}")
        put(f"ETwo{FNAME[f]}CluesMin", f"{S['clues_min_mean']:.1f}")
        lv = S["levels"]
        lm = S["levels_after_min"]
        rows.append(f"{FNAME[f]} & {S['n']} & {S['unique']} & {S['matches_intended']} & {S['valid_raw']} & "
                    f"{S['valid_after_repair1']} & " + "/".join(str(lv.get(str(l), 0)) for l in range(1, 4))
                    + " & " + "/".join(str(lm.get(str(l), 0)) for l in range(1, 4))
                    + f" & {S['redundancy_mean']:.2f} & {S['clues_mean']:.1f} $\\to$ {S['clues_min_mean']:.1f} \\\\")
        for l in range(1, 4):
            put(f"ETwo{FNAME[f]}L{word(l - 1)}", f"{lv.get(str(l), 0)}")
            put(f"ETwo{FNAME[f]}MinL{word(l - 1)}", f"{lm.get(str(l), 0)}")
    table("e2", rows)
    put("ETwoN", f"{tot['n']}")
    put("ETwoValid", f"{tot['valid_raw']}")
    put("ETwoValidRepair", f"{tot['valid_after_repair1']}")
    put("ETwoUnique", f"{tot['unique']}")
    put("ETwoMatch", f"{tot['matches_intended']}")
    D = E2["duplication"]["sudoku"]
    put("ETwoSudokuMasks", f"{D['distinct_masks']}")
    put("ETwoSudokuWikiMask", f"{D['wikipedia_mask']}")
    put("ETwoSudokuWikiSame", f"{D['wikipedia_identical']}")
    put("ETwoSudokuLargestGroup", f"{D['largest_mask_group']}")

    # ---- E3 --------------------------------------------------------------
    E3 = J("e3/summary.json")
    put("EThreeN", f"{E3['n_puzzles']}")
    put("EThreeScores", f"{E3['n_scores']}")
    rows = []
    for f in FAMS:
        cells = []
        for m in MODELS:
            a = next(x for x in E3["accuracy_by_family"] if x["family"] == f and x["model"] == m)
            put(f"EThree{FNAME[f]}{MNAME[m]}", pct(a["exact"]))
            put(f"EThree{FNAME[f]}{MNAME[m]}Cell", pct(a["cell"], 1))
            cells.append(f"{pct(a['exact'])} [{pct(a['exact_lo'])}, {pct(a['exact_hi'])}]")
        rows.append(f"{FNAME[f]} & " + " & ".join(cells) + " \\\\")
    table("e3acc", rows)
    for a in E3["accuracy"]:
        put(f"EThree{FNAME[a['family']]}{MNAME[a['model']]}L{word(a['level'] - 1)}", pct(a["exact"]))
        put(f"EThree{FNAME[a['family']]}{MNAME[a['model']]}LN{word(a['level'] - 1)}", f"{a['n']}")
    rows = []
    mets = [("conflicts", "MiniSat conflicts"), ("decisions", "MiniSat decisions"), ("mus_mean", "mean MUS size"),
            ("up_closure", "fixed by L1"), ("fl_steps", "probing steps"), ("n_clues", "number of clues")]
    for met, mname in mets:
        cells = []
        for f in FAMS:
            c = next(x for x in E3["metric_vs_level"] if x["family"] == f and x["metric"] == met)
            cells.append(f"{c['rho']:.2f} [{c['lo']:.2f}, {c['hi']:.2f}]")
            put(f"Rho{FNAME[f]}{''.join(w.capitalize() for w in met.split('_'))}".replace("_", ""), f"{c['rho']:.2f}")
        rows.append(f"{mname} & " + " & ".join(cells) + " \\\\")
    table("e3rho", rows)
    M = E3["models"]
    nc = M["logit_nonceiling"]
    put("LogitLevel", f"{nc['params']['level']:.2f}")
    put("LogitLevelLo", f"{nc['level_boot'][1]:.2f}")
    put("LogitLevelHi", f"{nc['level_boot'][2]:.2f}")
    put("LogitLevelP", f"{nc['pvalues']['level']:.2f}")
    put("LogitN", f"{nc['n']}")
    sh = M["logit_sudoku_haiku"]
    put("LogitSudokuLevel", f"{sh['params']['level']:.2f}")
    put("LogitSudokuLo", f"{sh['level_boot'][1]:.2f}")
    put("LogitSudokuHi", f"{sh['level_boot'][2]:.2f}")
    put("LogitSudokuP", f"{sh['pvalues']['level']:.2f}")
    put("AICMetrics", f"{M['metrics_only']['aic']:.1f}")
    put("AICMetricsLevel", f"{M['metrics_plus_level']['aic']:.1f}")
    put("LogitMLLevel", f"{M['metrics_plus_level']['params']['level']:.2f}")
    put("LogitMLLevelP", f"{M['metrics_plus_level']['pvalues']['level']:.2f}")
    put("LogitMLConfP", f"{M['metrics_plus_level']['pvalues']['log_conf']:.2f}")
    put("LogitMOConf", f"{M['metrics_only']['params']['log_conf']:.2f}")
    put("LogitMOConfP", f"{M['metrics_only']['pvalues']['log_conf']:.2f}")
    mx = M["mixed_cell"]
    put("MixedLevel", f"{mx['params']['level']:.3f}")
    put("MixedLevelSE", f"{mx['bse']['level']:.3f}")
    put("MixedLevelP", f"{mx['pvalues']['level']:.2f}")
    # puzzles per family / augmented
    P = [json.loads(l) for l in (ROOT / "data/e3/puzzles.jsonl").read_text().splitlines() if l.strip()]
    put("EThreeAug", f"{sum(1 for p in P if p['source'] != 'minimal')}")
    for f in FAMS:
        put(f"EThree{FNAME[f]}N", f"{sum(1 for p in P if p['family'] == f)}")
    S = [json.loads(l) for l in (R / "e3/scores.jsonl").read_text().splitlines() if l.strip()]
    put("EThreeUnanswered", f"{sum(1 for s in S if not s.get('answered', True))}")
    for f in FAMS:
        for m in MODELS:
            ss = [s for s in S if s["family"] == f and s["model"] == m]
            sa = [s for s in ss if s.get("answered", True)]
            put(f"EThree{FNAME[f]}{MNAME[m]}Unans", f"{len(ss) - len(sa)}")
            put(f"EThree{FNAME[f]}{MNAME[m]}Answered", pct(sum(s["exact"] for s in sa) / max(1, len(sa))))
            for l in range(1, 6):
                sl = [s for s in sa if s["level"] == l]
                if sl:
                    put(f"EThree{FNAME[f]}{MNAME[m]}AnsL{word(l - 1)}", f"{sum(s['exact'] for s in sl)}/{len(sl)}")
                    put(f"EThree{FNAME[f]}{MNAME[m]}UnansL{word(l - 1)}",
                        f"{sum(1 for s in ss if s['level'] == l and not s.get('answered', True))}")

    # ---- E4 --------------------------------------------------------------
    for run, tag in [("e4", "Pilot"), ("e4b", "Zebra"), ("e4s", "Sudoku")]:
        p = ROOT / "data" / run / "state.json"
        if not p.exists():
            continue
        st = json.loads(p.read_text())
        H = st["history"]
        if not H:
            continue
        put(f"EFour{tag}Indiv", f"{len(st['all'])}")
        put(f"EFour{tag}Gens", f"{len(H)}")
        put(f"EFour{tag}BestStart", f"{max(H[0]['fitness']):.2f}")
        put(f"EFour{tag}BestEnd", f"{max(H[-1]['fitness']):.2f}")
        put(f"EFour{tag}MeanStart", f"{sum(H[0]['fitness']) / len(H[0]['fitness']):.2f}")
        put(f"EFour{tag}MeanEnd", f"{sum(H[-1]['fitness']) / len(H[-1]['fitness']):.2f}")
        logs = [m for h in H for m in h.get("mutation_log", [])]
        put(f"EFour{tag}Proposals", f"{len(logs)}")
        put(f"EFour{tag}Accepted", f"{sum(m['accepted'] for m in logs)}")
        n_err = sum(1 for ind in st["all"].values() if any(e < 1 for e in ind.get("evals", [])))
        put(f"EFour{tag}WithError", f"{n_err}")
        n_ev = sum(len(ind.get("evals", [])) for ind in st["all"].values())
        put(f"EFour{tag}Evals", f"{n_ev}")
        lev = Counter(ind.get("level") for ind in st["all"].values())
        for l in range(1, 4):
            put(f"EFour{tag}L{word(l - 1)}", f"{lev.get(l, 0)}")
        hp = R / run / "heldout_summary.json"
        if hp.exists():
            Hs = json.loads(hp.read_text())
            for grp in ("initial", "final"):
                for m in MODELS:
                    d = Hs.get(f"{grp}|{m}")
                    if d:
                        put(f"EFour{tag}{grp.capitalize()}{MNAME[m]}", pct(d["exact"]))
                        put(f"EFour{tag}{grp.capitalize()}{MNAME[m]}Cell", pct(d["cell_acc"], 1))

    # ---- E5 --------------------------------------------------------------
    G = J("e5/genres.json")
    put("EFiveGenres", f"{len(G)}")
    rows = []
    n_ok_tot = 0
    for g in G:
        inst = [i for i in g.get("instances", []) if i.get("status") == "ok"]
        n_ok_tot += len(inst)
        lv = Counter(i["level"] for i in inst)
        mean_clues = sum(i["n_clues"] for i in inst) / max(1, len(inst))
        rows.append(f"{g['name']} & {len(inst)}/{len(g.get('instances', []))} & "
                    + " & ".join(str(lv.get(l, 0)) for l in range(1, 6)) + f" & {mean_clues:.1f} \\\\")
    table("e5", rows)
    put("EFiveInstances", f"{n_ok_tot}")
    SS = J("e5/solve_scores.json")
    put("EFiveSolveN", f"{len(SS)}")
    put("EFiveSolveExact", f"{sum(1 for s in SS if s['exact'])}")

    lines = ["% generated by src/make_numbers.py -- do not edit"]
    for k, v in sorted(macros.items()):
        lines.append(f"\\newcommand{{\\{k}}}{{{v}\\xspace}}")
    (PAPER / "numbers.tex").write_text("\n".join(lines) + "\n")
    print(f"wrote {len(macros)} macros")


def table(name, rows):
    d = PAPER / "tables"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{name}_rows.tex").write_text("% generated by src/make_numbers.py\n" + "\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
