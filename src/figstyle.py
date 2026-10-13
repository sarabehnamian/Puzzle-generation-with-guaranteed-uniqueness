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


def setup():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 8,
        "axes.titlesize": 8.5,
        "axes.labelsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
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
        "savefig.dpi": 300,
        "pdf.fonttype": 42,
        "legend.frameon": False,
    })


def save(fig, name):
    from pathlib import Path
    out = Path(__file__).resolve().parents[1] / "figures"
    out.mkdir(exist_ok=True)
    fig.savefig(out / f"{name}.pdf")
    fig.savefig(out / f"{name}.png")
    plt.close(fig)
