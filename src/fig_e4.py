"""Figure: E4 evolution curves and held-out accuracy of initial vs final populations."""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from .figstyle import INK2, MODEL_COLORS, MODEL_NAMES, SERIES, TEXTWIDTH, save, setup

ROOT = Path(__file__).resolve().parents[1]
RUNS = [("e4", "Zebra 5x4 (pilot)"), ("e4b", "Zebra 6x6"), ("e4s", "Sudoku 9x9")]
# the abandoned 5x4 pilot was not rerun through the API (still subagent data), so it is not drawn
SHOW = {"e4b", "e4s"}
MODELS = ["haiku", "sonnet", "opus"]
TITLE_PAD = 26  # room for two legend rows between title and axes


def load(run):
    p = ROOT / "data" / run / "state.json"
    return json.loads(p.read_text()) if p.exists() else None


def main():
    setup()
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.7), gridspec_kw={"width_ratios": [1, 1.1]})

    # a: fitness per generation; colour = run, solid = best, dashed = mean
    ax = axes[0]
    run_handles = []
    for k, (run, name) in enumerate(RUNS):
        if run not in SHOW:
            continue  # colour index k is kept, so each run keeps its colour
        st = load(run)
        if not st:
            continue
        H = st["history"]
        g = [h["gen"] for h in H]
        ax.plot(g, [max(h["fitness"]) for h in H], "-o", color=SERIES[k], ms=3, lw=1.4)
        ax.plot(g, [float(np.mean(h["fitness"])) for h in H], "--", color=SERIES[k], lw=1.0)
        run_handles.append(Line2D([], [], color=SERIES[k], lw=2, label=name))
    style_handles = [Line2D([], [], color=INK2, lw=1.4, marker="o", ms=3, label="best"),
                     Line2D([], [], color=INK2, lw=1.0, ls="--", label="mean")]
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness (1 $-$ Haiku cell accuracy)")
    ax.set_title("a  Fitness of the population", pad=TITLE_PAD)
    ax.set_ylim(-0.02, max(0.3, ax.get_ylim()[1]))
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    leg = ax.legend(handles=run_handles, loc="lower left", bbox_to_anchor=(0, 1.075), ncol=3, frameon=False)
    ax.add_artist(leg)
    ax.legend(handles=style_handles, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, frameon=False)

    # b: held-out exact-solution rate, initial (light, hatched) vs final (solid) population
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
                x = gi + (mi - 1) * 2.4 * w + (si - 0.5) * w
                ax.bar(x, 100 * r["exact"], w * 0.9, color=MODEL_COLORS[m],
                       alpha=0.4 if grp == "initial" else 1.0,
                       hatch="////" if grp == "initial" else None, edgecolor="white", linewidth=0.4)
    ax.set_xticks(range(len(groups)), [g[0] for g in groups])
    ax.tick_params(axis="x", length=0)
    ax.set_xlim(-0.6, len(groups) - 0.4)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Exactly solved (%)")
    ax.set_title("b  Fresh solver calls", pad=TITLE_PAD)
    ax.grid(axis="x", visible=False)
    model_handles = [Patch(color=MODEL_COLORS[m], label=MODEL_NAMES[m]) for m in MODELS]
    pop_handles = [Patch(facecolor="#bdbcb8", hatch="////", edgecolor="white", label="initial population"),
                   Patch(facecolor="#52514e", label="final population")]
    leg = ax.legend(handles=model_handles, loc="lower left", bbox_to_anchor=(0, 1.075), ncol=3, frameon=False)
    ax.add_artist(leg)
    ax.legend(handles=pop_handles, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, frameon=False)
    save(fig, "fig6_evolution")


if __name__ == "__main__":
    main()
