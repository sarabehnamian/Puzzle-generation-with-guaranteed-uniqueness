"""Figure 1: one puzzle, its two independent encodings, and its forced-deduction chain."""
import json
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt

from .csp import CNF, ClueSolver
from .e1_faithfulness import collect, e1_items
from .families import get
from .figstyle import INK, INK2, SERIES, save, setup
from .grading import Engine, grade, mus_for_literal

ROOT = Path(__file__).resolve().parents[1]
PID = "plain:zebra-00051"
RULE_NAME = {"UP": "L1", "GAC": "L2", "FL1": "L3", "FL2": "L4"}
RANK = {"L1": 1, "L2": 2, "L3": 3, "L4": 4}


def deduction_chain(spec):
    csp, sol = get("zebra").build_csp(spec)
    cnf = CNF(csp)
    g = grade(cnf, trace=True)
    cs = ClueSolver(cnf)
    ids = list(range(len(csp.clues)))
    chain, seen, phase = [], set(), "L1"
    for t in g.trace:
        if t["rule"] != "UP" and RANK[RULE_NAME[t["rule"]]] > RANK[phase]:
            phase = RULE_NAME[t["rule"]]
        lit = t["lit"]
        if lit <= 0 or lit in seen:
            continue
        seen.add(lit)
        v, a = cnf.var_of[lit]
        mus = mus_for_literal(cs, ids, lit)
        chain.append({"value": csp.names[v], "house": csp.domains[v][a], "phase": phase,
                      "clues": [i + 1 for i in mus]})
    cs.delete()
    return chain, g.level


def main():
    setup()
    item = [i for i in e1_items() if i["id"] == PID][0]
    spec = item["spec"]
    A = {c["clue"]: c["expr"] for c in collect("e1_encA")[PID]}
    B = {c["clue"]: c["expr"] for c in collect("e1_encB")[PID]}
    chain, level = deduction_chain(spec)
    (ROOT / "results" / "fig1_chain.json").write_text(json.dumps({"id": PID, "level": level, "chain": chain}, indent=1))
    fig = plt.figure(figsize=(7.2, 4.6))
    # panel a: puzzle text
    ax = fig.add_axes([0.0, 0.0, 0.36, 1.0])
    ax.axis("off")
    ax.text(0, 1.0, "a  Puzzle (natural language)", fontsize=8.5, weight="bold", va="top")
    lines = []
    for c, vals in spec["cats"].items():
        lines.append(f"{c}: {', '.join(vals)}")
    lines.append("")
    for i, c in enumerate(spec["clues"], 1):
        for k, w in enumerate(textwrap.wrap(c["text"], 52)):
            lines.append((f"{i:>2}. " if k == 0 else "    ") + w)
    ax.text(0, 0.94, "\n".join(lines), fontsize=5.6, family="DejaVu Sans Mono", va="top", color=INK,
            linespacing=1.35)
    # panel b: two encodings
    ax = fig.add_axes([0.37, 0.0, 0.33, 1.0])
    ax.axis("off")
    ax.text(0, 1.0, "b  Two independent encodings", fontsize=8.5, weight="bold", va="top")
    ax.text(0, 0.955, "A and B are separate Sonnet calls; z3 proves\n(A xor B) unsatisfiable, i.e. A and B are equivalent.",
            fontsize=6, va="top", color=INK2)
    y = 0.88
    for i in range(1, len(spec["clues"]) + 1):
        a = A[i].replace('"', "'")
        b = B[i].replace('"', "'")
        same = a.replace(" ", "").lower() == b.replace(" ", "").lower()
        ax.text(0, y, f"{i:>2}", fontsize=5.6, family="DejaVu Sans Mono", va="top", color=INK2)
        ax.text(0.06, y, "A: " + a, fontsize=5.3, family="DejaVu Sans Mono", va="top", color=SERIES[0])
        ax.text(0.06, y - 0.025, "B: " + (b if not same else "(identical up to case)"), fontsize=5.3,
                family="DejaVu Sans Mono", va="top", color=SERIES[1] if not same else INK2)
        y -= 0.062
    # panel c: deduction chain
    ax = fig.add_axes([0.73, 0.0, 0.27, 1.0])
    ax.axis("off")
    ax.text(0, 1.0, f"c  Forced deductions (ladder L{level})", fontsize=8.5, weight="bold", va="top")
    ax.text(0, 0.955, "facts in the order the ladder engine derives them;\nL = highest rule needed so far; {..} = minimal set\nof clues that forces the fact", fontsize=6,
            va="top", color=INK2)
    y = 0.85
    colors = {"L1": SERIES[2], "L2": SERIES[0], "L3": SERIES[1], "L4": "#6250d6"}
    for k, st in enumerate(chain, 1):
        ax.text(0, y, f"{k:>2}", fontsize=5.6, family="DejaVu Sans Mono", va="top", color=INK2)
        ax.text(0.09, y, f"{st['value']} = house {st['house']}", fontsize=5.8, va="top", color=INK)
        ax.text(0.58, y, st["phase"], fontsize=5.8, va="top", color=colors[st["phase"]], weight="bold")
        ax.text(0.70, y, "{" + ",".join(map(str, st["clues"])) + "}", fontsize=5.6, va="top", color=INK2)
        y -= 0.04
    save(fig, "fig1_example")


if __name__ == "__main__":
    main()
