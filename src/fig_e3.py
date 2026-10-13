"""Figures: ladder vs solver metrics (fig4) and ladder vs LLM accuracy (fig5)."""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .analysis_e3 import load
from .figstyle import FAMILY_NAMES, INK2, MODEL_COLORS, MODEL_NAMES, SERIES, save, setup
from .stats import boot_mean

ROOT = Path(__file__).resolve().parents[1]
FAMS = ["zebra", "sudoku", "killer", "futoshiki"]


def fig_metrics(M):
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.4))
    metrics = [("conflicts", "MiniSat conflicts (find + prove unique)", True),
               ("mus_mean", "Mean clues per minimal explanation", False),
               ("up_closure", "Variables fixed by unit propagation (%)", False)]
    for ax, (m, label, logy) in zip(axes, metrics):
        for j, fam in enumerate(FAMS):
            g = M[M.family == fam]
            lv = sorted(g.level.unique())
            means, lo, hi = [], [], []
            for l in lv:
                vals = g[g.level == l][m].values * (100 if m == "up_closure" else 1)
                if logy:
                    vals = np.log10(vals + 1)
                mm, a, b = boot_mean(vals)
                means.append(mm), lo.append(mm - a), hi.append(b - mm)
            off = (j - 1.5) * 0.08
            ax.errorbar(np.array(lv) + off, means, yerr=[lo, hi], color=SERIES[j], marker="o", ms=3.5, lw=1.5,
                        capsize=1.5, label=FAMILY_NAMES[fam])
        ax.set_xlabel("Ladder level")
        ax.set_xticks(range(1, 6))
        ax.set_title(label, loc="left", fontsize=7.5)
        if logy:
            ax.set_ylabel("log10(conflicts + 1)")
    axes[0].legend(loc="upper left", fontsize=6)
    fig.tight_layout()
    save(fig, "fig4_ladder_metrics")


def fig_accuracy(D):
    fig, axes = plt.subplots(1, 4, figsize=(7.2, 2.3), sharey=True)
    for ax, fam in zip(axes, FAMS):
        g = D[D.family == fam]
        for k, mod in enumerate(["haiku", "sonnet", "opus"]):
            h = g[g.model == mod]
            if h.empty:
                continue
            lv = sorted(h.level.unique())
            means, lo, hi = [], [], []
            for l in lv:
                m, a, b = boot_mean(h[h.level == l]["exact"].values)
                means.append(100 * m), lo.append(100 * (m - a)), hi.append(100 * (b - m))
            off = (k - 1) * 0.1
            ax.errorbar(np.array(lv) + off, means, yerr=[lo, hi], color=MODEL_COLORS[mod], marker="o", ms=3.5,
                        lw=1.5, capsize=1.5, label=MODEL_NAMES[mod])
        ax.set_title(FAMILY_NAMES[fam], loc="left")
        ax.set_xticks(range(1, 6))
        ax.set_xlim(0.6, 5.4)
        ax.set_ylim(-5, 105)
        ax.set_xlabel("Ladder level")
    axes[0].set_ylabel("Exactly solved (%)")
    axes[-1].legend(loc="lower left", fontsize=6)
    fig.tight_layout()
    save(fig, "fig5_ladder_accuracy")


def main():
    setup()
    M, D = load()
    fig_metrics(M)
    fig_accuracy(D)


if __name__ == "__main__":
    main()
