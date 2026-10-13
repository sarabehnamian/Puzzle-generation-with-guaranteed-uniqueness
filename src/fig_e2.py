"""Figure: E2 validity / redundancy / difficulty of LLM-written puzzles."""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .figstyle import FAMILY_NAMES, INK2, save, setup

ROOT = Path(__file__).resolve().parents[1]
FAMS = ["zebra", "sudoku", "killer", "futoshiki"]
LEVEL_COLORS = ["#c9dcf5", "#7fb0ea", "#2a78d6", "#18457d", "#0b0b0b"]


def main():
    setup()
    S = json.loads((ROOT / "results/e2/summary.json").read_text())["by_family"]
    B = json.loads((ROOT / "results/bank_stats.json").read_text())
    R = [json.loads(l) for l in (ROOT / "results/e2/records.jsonl").read_text().splitlines() if l.strip()]
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.7), gridspec_kw={"width_ratios": [1.5, 1]})
    ax = axes[0]
    x = 0
    ticks, labels = [], []
    for fam in FAMS:
        dists = [("LLM", S[fam]["levels"]), ("min", S[fam]["levels_after_min"]),
                 ("gen", B[fam]["levels"])]
        for name, d in dists:
            tot = sum(int(d.get(str(l), 0)) for l in range(1, 6))
            bottom = 0
            for l in range(1, 6):
                v = 100 * int(d.get(str(l), 0)) / tot
                ax.bar(x, v, bottom=bottom, color=LEVEL_COLORS[l - 1], width=0.8, edgecolor="white", linewidth=0.8,
                       label=f"L{l}" if (fam == "zebra" and name == "LLM") else None)
                bottom += v
            ticks.append(x)
            labels.append(name)
            x += 1
        ax.text(x - 2, -15, FAMILY_NAMES[fam], ha="center", va="top", fontsize=7)
        x += 0.6
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels, fontsize=6.5)
    ax.set_ylabel("Puzzles (%)")
    ax.set_ylim(0, 100)
    ax.set_title("a  Ladder level of LLM-written vs pipeline puzzles", loc="left")
    ax.legend(ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.24), handlelength=1, columnspacing=1.2)
    ax.grid(axis="x", visible=False)
    ax = axes[1]
    for i, fam in enumerate(FAMS):
        rs = [r for r in R if r["family"] == fam and r.get("n_clues_min")]
        red = [100 * r["redundancy"] for r in rs]
        jitter = np.random.default_rng(i).uniform(-0.18, 0.18, len(red))
        ax.scatter(np.full(len(red), i) + jitter, red, s=9, color="#2a78d6", alpha=0.6, linewidths=0)
        ax.hlines(np.mean(red), i - 0.3, i + 0.3, color="#0b0b0b", lw=1.5)
    ax.set_xticks(range(4))
    ax.set_xticklabels([FAMILY_NAMES[f].split(" ")[0] for f in FAMS])
    ax.set_ylabel("Clues removable one at a time (%)")
    ax.set_ylim(-3, 103)
    ax.set_title("b  Redundancy of LLM-written puzzles", loc="left")
    ax.text(3.45, 2, "pipeline puzzles: 0% by construction", fontsize=6, color=INK2, ha="right")
    ax.grid(axis="x", visible=False)
    fig.tight_layout()
    save(fig, "fig3_validity")


if __name__ == "__main__":
    main()
