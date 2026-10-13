"""Figure: gallery of certified puzzles (one per family) and an invented genre."""
import json
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt

from .figstyle import INK, INK2, SERIES, save, setup

ROOT = Path(__file__).resolve().parents[1]


def pick(family, level):
    for l in (ROOT / "data/e3/puzzles.jsonl").read_text().splitlines():
        p = json.loads(l)
        if p["family"] == family and p["analysis"]["level"] == level and p["source"] == "minimal":
            return p
    raise KeyError(family)


def grid_lines(ax, n, box=None, lw_thin=0.5, lw_thick=1.4):
    for i in range(n + 1):
        thick = box and (i % box[0] == 0)
        ax.plot([0, n], [i, i], color=INK, lw=lw_thick if (thick or i in (0, n)) else lw_thin)
        thick = box and (i % box[1] == 0)
        ax.plot([i, i], [0, n], color=INK, lw=lw_thick if (thick or i in (0, n)) else lw_thin)
    ax.set_xlim(-0.2, n + 0.2)
    ax.set_ylim(n + 0.2, -0.2)
    ax.set_aspect("equal")
    ax.axis("off")


def draw_sudoku(ax, p):
    s = p["spec"]
    grid_lines(ax, 9, (3, 3))
    for c in s["clues"]:
        r, cc = c["cell"]
        ax.text(cc + 0.5, r + 0.55, str(c["value"]), ha="center", va="center", fontsize=6.5, color=INK)


def draw_killer(ax, p):
    s = p["spec"]
    n = 6
    grid_lines(ax, n, (2, 3), lw_thin=0.3)
    cols = ["#e8f0fb", "#fde9df", "#e2f5ee", "#fdf2d9"]
    cage_of = {}
    cages = [c for c in s["clues"] if c["type"] == "cage"]
    for k, c in enumerate(cages):
        for r, cc in c["cells"]:
            cage_of[(r, cc)] = k
    e = 0.09
    for k, c in enumerate(cages):
        for r, cc in c["cells"]:
            ax.add_patch(plt.Rectangle((cc, r), 1, 1, color=cols[k % 4], zorder=0, lw=0))
            if cage_of.get((r - 1, cc)) != k:
                ax.plot([cc + e, cc + 1 - e], [r + e, r + e], color=INK2, lw=0.7, ls=(0, (2, 1.2)))
            if cage_of.get((r + 1, cc)) != k:
                ax.plot([cc + e, cc + 1 - e], [r + 1 - e, r + 1 - e], color=INK2, lw=0.7, ls=(0, (2, 1.2)))
            if cage_of.get((r, cc - 1)) != k:
                ax.plot([cc + e, cc + e], [r + e, r + 1 - e], color=INK2, lw=0.7, ls=(0, (2, 1.2)))
            if cage_of.get((r, cc + 1)) != k:
                ax.plot([cc + 1 - e, cc + 1 - e], [r + e, r + 1 - e], color=INK2, lw=0.7, ls=(0, (2, 1.2)))
        r, cc = min(c["cells"])
        ax.text(cc + 0.14, r + 0.3, str(c["sum"]), fontsize=5.5, color=INK)
    for c in s["clues"]:
        if c["type"] == "given":
            r, cc = c["cell"]
            ax.text(cc + 0.5, r + 0.6, str(c["value"]), ha="center", va="center", fontsize=8)


def draw_futoshiki(ax, p):
    s = p["spec"]
    n = 5
    for r in range(n):
        for c in range(n):
            ax.add_patch(plt.Rectangle((c * 1.4, r * 1.4), 1, 1, fill=False, color=INK, lw=0.8))
    for c in s["clues"]:
        if c["type"] == "given":
            r, cc = c["cell"]
            ax.text(cc * 1.4 + 0.5, r * 1.4 + 0.55, str(c["value"]), ha="center", va="center", fontsize=8)
        else:
            (r1, c1), (r2, c2) = c["a"], c["b"]
            if r1 == r2:
                x = min(c1, c2) * 1.4 + 1.2
                sym = "<" if c1 < c2 else ">"
                ax.text(x, r1 * 1.4 + 0.55, sym, ha="center", va="center", fontsize=8, color=SERIES[0])
            else:
                y = min(r1, r2) * 1.4 + 1.2
                sym = "∧" if r1 < r2 else "∨"
                ax.text(c1 * 1.4 + 0.5, y, sym, ha="center", va="center", fontsize=8, color=SERIES[0])
    ax.set_xlim(-0.2, n * 1.4)
    ax.set_ylim(n * 1.4, -0.2)
    ax.set_aspect("equal")
    ax.axis("off")


def draw_text(ax, lines, size=5.4):
    ax.axis("off")
    ax.text(0, 1, "\n".join(lines), va="top", fontsize=size, family="DejaVu Sans Mono", color=INK, linespacing=1.3)


def main():
    setup()
    fig = plt.figure(figsize=(7.2, 5.6))
    specs = [("a  Zebra, L3", pick("zebra", 3)), ("b  Sudoku, L3", pick("sudoku", 3)),
             ("c  Killer, L4", pick("killer", 4)), ("d  Futoshiki, L3", pick("futoshiki", 3))]
    pos = [[0.0, 0.5, 0.48, 0.46], [0.52, 0.53, 0.22, 0.40], [0.77, 0.53, 0.22, 0.40], [0.58, 0.05, 0.26, 0.35]]
    for (title, p), ps in zip(specs, pos):
        ax = fig.add_axes(ps)
        fam = p["family"]
        if fam == "zebra":
            s = p["spec"]
            lines = [f"{c}: {', '.join(v)}" for c, v in s["cats"].items()] + [""]
            for i, c in enumerate(s["clues"], 1):
                for k, w in enumerate(textwrap.wrap(c["text"], 62)):
                    lines.append((f"{i:>2}. " if k == 0 else "    ") + w)
            draw_text(ax, lines)
        elif fam == "sudoku":
            draw_sudoku(ax, p)
        elif fam == "killer":
            draw_killer(ax, p)
        else:
            draw_futoshiki(ax, p)
        fig.text(ps[0], ps[1] + ps[3] + 0.01, title + f" ({p['analysis']['n_clues']} clues)",
                 fontsize=7.5, weight="bold")
    # invented genre
    G = json.loads((ROOT / "results/e5/genres.json").read_text())
    g = [x for x in G if x["name"] == "Median Line Latin"][0]
    inst = sorted([i for i in g["instances"] if i.get("status") == "ok"], key=lambda i: -i["level"])[0]
    ax = fig.add_axes([0.0, 0.03, 0.48, 0.40])
    lines = textwrap.wrap(g["rules_text"], 66) + [""] + [f"- {c['text']}" for c in inst["clues"]]
    draw_text(ax, lines, 5.6)
    fig.text(0.0, 0.445, f"e  LLM-invented genre “{g['name']}”, L{inst['level']} ({inst['n_clues']} clues)",
             fontsize=7.5, weight="bold")
    save(fig, "fig7_gallery")


if __name__ == "__main__":
    main()
