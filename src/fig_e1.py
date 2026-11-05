"""Figure: E1 faithfulness."""
import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from .figstyle import INK2, SERIES, TEXTWIDTH, legend_above, save, setup
from .stats import boot_mean

ROOT = Path(__file__).resolve().parents[1]
STYLES = ["plain", "hard", "paraphrase"]
STYLE_NAMES = {"plain": "Plain\ntemplates", "hard": "Hard\ntemplates", "paraphrase": "LLM\nparaphrase"}
ENCS = [("A", "Sonnet A"), ("B", "Sonnet B"), ("C", "Haiku C")]
PARTNER = {"A": "B", "B": "A", "C": "A"}
TITLE_PAD = 17  # room for the one-row legend between title and axes


def main():
    setup()
    R = [json.loads(l) for l in (ROOT / "results/e1/records.jsonl").read_text().splitlines() if l.strip()]
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.5), gridspec_kw={"width_ratios": [1, 1.05]})

    # a: error rate per text style and encoder
    ax = axes[0]
    w = 0.26
    for j, (e, name) in enumerate(ENCS):
        xs, ys, lo, hi = [], [], [], []
        for i, st in enumerate(STYLES):
            rs = [r for r in R if r["style"] == st]
            m, l, h = boot_mean([0 if r[e]["equiv_gt"] else 1 for r in rs])
            xs.append(i + (j - 1) * w)
            ys.append(100 * m)
            lo.append(100 * (m - l))
            hi.append(100 * (h - m))
        ax.bar(xs, ys, width=w - 0.04, color=SERIES[j], label=name)
        ax.errorbar(xs, ys, yerr=[lo, hi], fmt="none", ecolor=INK2, elinewidth=0.7, capsize=1.5)
    ax.set_xticks(range(3))
    ax.set_xticklabels([STYLE_NAMES[s] for s in STYLES])
    ax.set_ylabel("Puzzles with a wrong encoding (%)")
    ax.set_ylim(0, None)
    ax.set_title("a  Single-encoding error rate", pad=TITLE_PAD)
    legend_above(ax, ncol=3)
    ax.grid(axis="x", visible=False)
    ax.tick_params(axis="x", length=0)

    # b: how wrong encodings are caught
    ax = axes[1]
    cats = ["dual check", "uniqueness check only", "not caught"]
    cols = [SERIES[0], SERIES[2], "#b8b7b2"]
    labels, data = [], []
    for e, name in ENCS:
        p = PARTNER[e]
        pair = "".join(sorted(e + p))
        wrong = [r for r in R if not r[e]["equiv_gt"]]
        dual = sum(1 for r in wrong if not r[f"{pair}_equiv"])
        uniq = sum(1 for r in wrong if r[f"{pair}_equiv"] and r[e]["n_solutions"] != 1)
        labels.append(f"{name}\n(vs {dict(ENCS)[p]})")
        data.append([dual, uniq, len(wrong) - dual - uniq])
    data = np.array(data)
    left = np.zeros(len(data))
    for k in range(3):
        ax.barh(range(len(data)), data[:, k], left=left, color=cols[k], label=cats[k], height=0.55,
                edgecolor="white", linewidth=1)
        left += data[:, k]
    ax.set_yticks(range(len(data)))
    ax.set_yticklabels(labels)
    ax.tick_params(axis="y", length=0)
    ax.invert_yaxis()
    ax.set_xlabel("Wrong encodings, all styles (count)")
    ax.set_title("b  Which check catches them", pad=TITLE_PAD)
    ax.set_xlim(0, max(1, data.sum(axis=1).max()) * 1.08)
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    legend_above(ax, ncol=3, title=None)
    ax.grid(axis="y", visible=False)
    save(fig, "fig2_faithfulness")


if __name__ == "__main__":
    main()
