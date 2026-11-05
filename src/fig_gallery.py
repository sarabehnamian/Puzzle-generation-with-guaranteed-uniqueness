"""Figure: gallery of certified puzzles (one per family) and an invented genre."""
import json
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt

from .figstyle import INK, INK2, SERIES, TEXTWIDTH, save, setup

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
        ax.text(cc + 0.5, r + 0.55, str(c["value"]), ha="center", va="center", fontsize=7, color=INK)


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
    """Cells of side 0.72 on a pitch of 1, so the inequality signs sit in the gaps between cells."""
    s = p["spec"]
    n, side = 5, 0.72
    for r in range(n):
        for c in range(n):
            ax.add_patch(plt.Rectangle((c, r), side, side, fill=False, edgecolor=INK, lw=0.9))
    mid = side + (1 - side) / 2
    for c in s["clues"]:
        if c["type"] == "given":
            r, cc = c["cell"]
            ax.text(cc + side / 2, r + side / 2, str(c["value"]), ha="center", va="center", fontsize=8)
        else:
            (r1, c1), (r2, c2) = c["a"], c["b"]
            if r1 == r2:
                sym = "<" if c1 < c2 else ">"
                ax.text(min(c1, c2) + mid, r1 + side / 2, sym, ha="center", va="center", fontsize=7.5,
                        color=SERIES[0])
            else:
                sym = "∧" if r1 < r2 else "∨"
                ax.text(c1 + side / 2, min(r1, r2) + mid, sym, ha="center", va="center", fontsize=7.5,
                        color=SERIES[0])
    ax.set_xlim(-0.15, n - 1 + side + 0.15)
    ax.set_ylim(n - 1 + side + 0.15, -0.15)
    ax.set_aspect("equal")
    ax.axis("off")


def draw_text(ax, lines, size=5.6):
    ax.axis("off")
    ax.text(0, 1, "\n".join(lines), va="top", ha="left", fontsize=size, family="DejaVu Sans Mono", color=INK,
            linespacing=1.35, transform=ax.transAxes)


def zebra_lines(p, width=60):
    s = p["spec"]
    lines = [f"{c}: {', '.join(v)}" for c, v in s["cats"].items()] + [""]
    for i, c in enumerate(s["clues"], 1):
        for k, w in enumerate(textwrap.wrap(c["text"], width - 4)):
            lines.append((f"{i:>2}. " if k == 0 else "    ") + w)
    return lines


def genre_and_instance():
    """The genre chosen for E5 (results/e5/solve_items.json) and its deepest certified instance."""
    G = json.loads((ROOT / "results/e5/genres.json").read_text(encoding="utf-8"))
    items = ROOT / "results/e5/solve_items.json"
    if items.exists():
        name = json.loads(items.read_text(encoding="utf-8"))["genre"]
    else:
        from .e5_genres import pick_genre
        name = pick_genre(G)
    g = [x for x in G if x["name"] == name][0]
    inst = sorted([i for i in g["instances"] if i.get("status") == "ok"], key=lambda i: -i["level"])[0]
    return g, inst


def main():
    setup()
    plt.rcParams["figure.constrained_layout.use"] = False
    fig = plt.figure(figsize=(TEXTWIDTH, 5.3))
    top, bottom = fig.subfigures(2, 1, height_ratios=[1.25, 1], hspace=0.02)
    # top row: the two puzzles that are text
    ta, tb = top.subplots(1, 2, gridspec_kw={"wspace": 0.08})
    top.subplots_adjust(left=0.0, right=1.0, top=0.93, bottom=0.0)
    za = pick("zebra", 3)
    draw_text(ta, zebra_lines(za))
    ta.set_title(f"a  Zebra, L3 ({za['analysis']['n_clues']} clues)")
    g, inst = genre_and_instance()
    lines = textwrap.wrap(g["rules_text"], 60) + [""] + \
        [w for c in inst["clues"] for w in textwrap.wrap(f"- {c['text']}", 60, subsequent_indent="  ")]
    draw_text(tb, lines)
    tb.set_title(f"b  LLM-invented genre “{g['name']}”, L{inst['level']} ({inst['n_clues']} clues)")
    # bottom row: the three grid puzzles at equal size
    axs = bottom.subplots(1, 3, gridspec_kw={"wspace": 0.18})
    bottom.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.02)
    for ax, (letter, fam, lev, draw) in zip(axs, [("c", "sudoku", 3, draw_sudoku), ("d", "killer", 4, draw_killer),
                                                  ("e", "futoshiki", 3, draw_futoshiki)]):
        p = pick(fam, lev)
        draw(ax, p)
        ax.set_title(f"{letter}  {fam.capitalize()}, L{lev} ({p['analysis']['n_clues']} clues)")
    save(fig, "fig7_gallery")


if __name__ == "__main__":
    main()
