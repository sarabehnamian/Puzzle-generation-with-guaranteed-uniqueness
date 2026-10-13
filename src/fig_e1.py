"""Figure: E1 faithfulness."""
import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from .figstyle import INK2, SERIES, save, setup
from .stats import boot_mean

ROOT = Path(__file__).resolve().parents[1]
STYLES = ["plain", "hard", "paraphrase"]
STYLE_NAMES = {"plain": "Plain templates", "hard": "Hard templates", "paraphrase": "LLM paraphrase"}
ENCS = [("A", "Sonnet A"), ("B", "Sonnet B"), ("C", "Haiku C")]
PARTNER = {"A": "B", "B": "A", "C": "A"}


def main():
    setup()
    R = [json.loads(l) for l in (ROOT / "results/e1/records.jsonl").read_text().splitlines() if l.strip()]
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.6), gridspec_kw={"width_ratios": [1.25, 1]})
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
        ax.bar(xs, ys, width=w - 0.03, color=SERIES[j], label=name)
        for x, y in zip(xs, ys):
            if y == 0:
                ax.text(x, 0.2, "0", ha="center", va="bottom", fontsize=6.5, color=INK2)
        ax.errorbar(xs, ys, yerr=[lo, hi], fmt="none", ecolor=INK2, elinewidth=0.8, capsize=1.5)
    ax.set_xticks(range(3))
    ax.set_xticklabels([STYLE_NAMES[s] for s in STYLES])
    ax.set_ylabel("Puzzles with a wrong encoding (%)")
    ax.set_title("a  Single-encoding error rate (n = 100/100/99)", loc="left")
    ax.legend(loc="upper left")
    ax.grid(axis="x", visible=False)
    # panel b: how wrong encodings are caught
    ax = axes[1]
    cats = ["caught by dual check", "caught by uniqueness check only", "not caught"]
    cols = [SERIES[0], SERIES[2], "#b8b7b2"]
    labels, data = [], []
    for e, name in ENCS:
        p = PARTNER[e]
        pair = "".join(sorted(e + p))
        wrong = [r for r in R if not r[e]["equiv_gt"]]
        dual = sum(1 for r in wrong if not r[f"{pair}_equiv"])
        uniq = sum(1 for r in wrong if r[f"{pair}_equiv"] and r[e]["n_solutions"] != 1)
        miss = len(wrong) - dual - uniq
        labels.append(f"{name}\n(partner {dict(ENCS)[p]})")
        data.append([dual, uniq, miss])
    data = np.array(data)
    left = np.zeros(len(data))
    for k in range(3):
        ax.barh(range(len(data)), data[:, k], left=left, color=cols[k], label=cats[k], height=0.6,
                edgecolor="white", linewidth=1)
        for i, v in enumerate(data[:, k]):
            if v:
                ax.text(left[i] + v / 2, i, str(int(v)), ha="center", va="center", fontsize=7,
                        color="white" if k < 2 else "#0b0b0b")
        left += data[:, k]
    ax.set_yticks(range(len(data)))
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Puzzles with a wrong encoding (all styles)")
    ax.set_title("b  Which check flags the wrong encodings", loc="left")
    ax.set_xlim(0, 2 * data.sum(axis=1).max() + 2)
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.legend(loc="center right", handlelength=1.2)
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    save(fig, "fig2_faithfulness")


if __name__ == "__main__":
    main()
