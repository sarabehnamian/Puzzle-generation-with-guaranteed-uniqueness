"""Figure: E4 evolution curves and held-out accuracy of initial vs final populations."""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .figstyle import INK2, MODEL_COLORS, MODEL_NAMES, SERIES, save, setup

ROOT = Path(__file__).resolve().parents[1]
RUNS = [("e4", "Zebra 5x4 (pilot)"), ("e4b", "Zebra 6x6"), ("e4s", "Sudoku 9x9")]
MODELS = ["haiku", "sonnet", "opus"]


def load(run):
    p = ROOT / "data" / run / "state.json"
    return json.loads(p.read_text()) if p.exists() else None


def main():
    setup()
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.6), gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axes[0]
    for k, (run, name) in enumerate(RUNS):
        st = load(run)
        if not st:
            continue
        H = st["history"]
        g = [h["gen"] for h in H]
        best = [max(h["fitness"]) for h in H]
        mean = [float(np.mean(h["fitness"])) for h in H]
        ax.plot(g, best, "-o", color=SERIES[k], ms=4, label=f"{name}: best")
        ax.plot(g, mean, "--", color=SERIES[k], lw=1.2, label=f"{name}: mean")
    ax.set_xlabel("generation")
    ax.set_ylabel("fitness (1 - mean Haiku cell accuracy)")
    ax.set_title("a  Fitness of the surviving population", loc="left")
    ax.set_ylim(-0.02, max(0.3, ax.get_ylim()[1]))
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.legend(loc="upper left", fontsize=6)

    ax = axes[1]
    w = 0.13
    groups = []
    for run, name in RUNS[1:]:
        p = ROOT / "results" / run / "heldout_summary.json"
        if p.exists():
            groups.append((name, json.loads(p.read_text())))
    for gi, (name, S) in enumerate(groups):
        for mi, m in enumerate(MODELS):
            for si, grp in enumerate(["initial", "final"]):
                r = S.get(f"{grp}|{m}")
                if not r:
                    continue
                x = gi + (mi - 1) * 2.2 * w + (si - 0.5) * w
                ax.bar(x, r["exact"], w * 0.92, color=MODEL_COLORS[m],
                       alpha=0.45 if grp == "initial" else 1.0,
                       hatch="///" if grp == "initial" else None, edgecolor="white", linewidth=0.5)
    ax.set_xticks(range(len(groups)), [g[0] for g in groups])
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("exact solutions (fraction)")
    ax.set_title("b  Held-out solvers: initial (hatched) vs final", loc="left")
    from matplotlib.patches import Patch
    handles = [Patch(color=MODEL_COLORS[m], label=MODEL_NAMES[m]) for m in MODELS]
    handles += [Patch(facecolor="#bbbbbb", hatch="///", edgecolor="white", label="initial"),
                Patch(facecolor="#555555", label="final")]
    ax.legend(handles=handles, loc="lower right", fontsize=6, ncol=2)
    for a in axes:
        a.tick_params(colors=INK2)
    fig.tight_layout()
    save(fig, "fig6_evolution")


if __name__ == "__main__":
    main()
