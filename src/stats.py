"""Small statistics helpers (seeded bootstrap)."""
import numpy as np

SEED = 20261013


def boot_mean(x, n_boot=2000, seed=SEED, alpha=0.05):
    x = np.asarray(x, dtype=float)
    if len(x) == 0:
        return float("nan"), float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(n_boot, len(x)))
    m = x[idx].mean(axis=1)
    return float(x.mean()), float(np.quantile(m, alpha / 2)), float(np.quantile(m, 1 - alpha / 2))


def boot_cluster(df, stat, cluster, n_boot=2000, seed=SEED, alpha=0.05):
    """Cluster bootstrap of an arbitrary statistic(df) -> float."""
    rng = np.random.default_rng(seed)
    groups = {k: g for k, g in df.groupby(cluster)}
    keys = list(groups)
    vals = []
    import pandas as pd
    for _ in range(n_boot):
        pick = rng.choice(len(keys), size=len(keys), replace=True)
        sample = pd.concat([groups[keys[i]] for i in pick], ignore_index=True)
        try:
            vals.append(stat(sample))
        except Exception:  # noqa: BLE001 - degenerate resample
            continue
    vals = np.array(vals, dtype=float)
    return float(stat(df)), float(np.nanquantile(vals, alpha / 2)), float(np.nanquantile(vals, 1 - alpha / 2))
