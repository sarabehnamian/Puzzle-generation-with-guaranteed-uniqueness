"""Shared matplotlib style for all figures (colour-blind-safe, validated palette)."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# categorical slots 1-3 of the reference palette validate under all-pairs CVD checks
MODEL_COLORS = {"haiku": "#2a78d6", "sonnet": "#eb6834", "opus": "#1baf7a"}
MODEL_NAMES = {"haiku": "Haiku 5.5", "sonnet": "Sonnet 5.5", "opus": "Opus 5.5"}
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
INK = "#0b0b0b"
INK2 = "#52514e"
GRID = "#d9d8d4"
FAMILY_NAMES = {"zebra": "Zebra (NL)", "sudoku": "Sudoku 9x9", "killer": "Killer 6x6", "futoshiki": "Futoshiki 5x5"}


# figures are drawn at their printed size (A4, 2 cm margins => \textwidth = 17 cm), so the
# LaTeX source includes them with width=\textwidth and no font gets scaled down
TEXTWIDTH = 6.69


def setup():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 7.5,
        "axes.titlesize": 8,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.titlepad": 6,
        "axes.labelsize": 7.5,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "legend.handlelength": 1.4,
        "legend.columnspacing": 1.2,
        "legend.borderaxespad": 0.2,
        "figure.constrained_layout.use": True,
        "figure.constrained_layout.h_pad": 0.04,
        "figure.constrained_layout.w_pad": 0.06,
        "axes.edgecolor": INK2,
        "axes.labelcolor": INK,
        "xtick.color": INK2,
        "ytick.color": INK2,
        "text.color": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.5,
        "axes.axisbelow": True,
        "lines.linewidth": 2,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.03,
        "savefig.dpi": 600,
        "pdf.fonttype": 42,
        "legend.frameon": False,
    })


def legend_above(ax, handles=None, ncol=4, **kw):
    """Legend in one row just above the axes, outside the data area."""
    args = (handles,) if handles is not None else ()
    return ax.legend(*args, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=ncol, frameon=False, **kw)


def fig_legend(fig, handles, ncol, **kw):
    """One shared legend row at the top of the figure, above all panels."""
    return fig.legend(handles=handles, loc="outside upper center", ncol=ncol, frameon=False, **kw)


def save(fig, name):
    from pathlib import Path
    out = Path(__file__).resolve().parents[1] / "figures"
    out.mkdir(exist_ok=True)
    fig.savefig(out / f"{name}.pdf")
    fig.savefig(out / f"{name}.png")
    plt.close(fig)
