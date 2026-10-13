"""E3 analysis: ladder level vs solver metrics vs LLM accuracy."""
import json
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats

from .stats import boot_cluster, boot_mean

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "e3"


def load():
    P = [json.loads(l) for l in (ROOT / "data" / "e3" / "puzzles.jsonl").read_text().splitlines() if l.strip()]
    meta = []
    for p in P:
        a = p["analysis"]
        meta.append({"id": p["id"], "family": p["family"], "level": a["level"], "source": p["source"],
                     "n_clues": a["n_clues"], "conflicts": a["conflicts_total"], "decisions": a["decisions_total"],
                     "propagations": a["propagations_total"], "mus_mean": a["mus_mean"], "mus_max": a["mus_max"],
                     "up_closure": a["frac_after"]["1"], "l2_closure": a["frac_after"]["2"],
                     "fl_steps": a["counts"]["FL1"] + a["counts"]["FL2"], "redundancy": a.get("redundancy", 0)})
    M = pd.DataFrame(meta)
    S = pd.DataFrame([json.loads(l) for l in (OUT / "scores.jsonl").read_text().splitlines() if l.strip()])
    D = S.merge(M.drop(columns=["family", "level", "source"]), on="id")
    D["exact"] = D["exact"].astype(int)
    return M, D


def main():
    M, D = load()
    res = {"n_puzzles": int(len(M)), "n_scores": int(len(D))}
    # accuracy table
    acc = []
    for (fam, lev, mod), g in D.groupby(["family", "level", "model"]):
        e = boot_mean(g["exact"])
        c = boot_mean(g["cell_acc"])
        acc.append({"family": fam, "level": int(lev), "model": mod, "n": int(len(g)),
                    "exact": e[0], "exact_lo": e[1], "exact_hi": e[2], "cell": c[0], "cell_lo": c[1], "cell_hi": c[2]})
    res["accuracy"] = acc
    tot = []
    for (fam, mod), g in D.groupby(["family", "model"]):
        e = boot_mean(g["exact"])
        tot.append({"family": fam, "model": mod, "n": int(len(g)), "exact": e[0], "exact_lo": e[1], "exact_hi": e[2],
                    "cell": float(g["cell_acc"].mean())})
    res["accuracy_by_family"] = tot
    # solver metrics vs level (Spearman, per family)
    cors = []
    for fam, g in M.groupby("family"):
        for metric in ["conflicts", "decisions", "mus_mean", "up_closure", "n_clues", "fl_steps"]:
            rho, p = stats.spearmanr(g["level"], g[metric])
            rng = np.random.default_rng(1)
            bs = []
            for _ in range(2000):
                s = g.sample(len(g), replace=True, random_state=int(rng.integers(1e9)))
                if s["level"].nunique() > 1 and s[metric].nunique() > 1:
                    bs.append(stats.spearmanr(s["level"], s[metric])[0])
            cors.append({"family": fam, "metric": metric, "rho": float(rho), "p": float(p),
                         "lo": float(np.quantile(bs, .025)), "hi": float(np.quantile(bs, .975)), "n": int(len(g))})
    res["metric_vs_level"] = cors
    # logistic regression with puzzle-cluster bootstrap for the level slope
    models = {}
    f_main = "exact ~ level + C(family) + C(model)"
    try:
        fit = smf.logit(f_main, D).fit(disp=0)
        models["logit_main"] = {"params": fit.params.to_dict(), "bse": fit.bse.to_dict(), "aic": fit.aic,
                                "llf": fit.llf, "n": int(fit.nobs)}

        def slope(df):
            return smf.logit(f_main, df).fit(disp=0).params["level"]
        est, lo, hi = boot_cluster(D, slope, "id", n_boot=500)
        models["logit_main"]["level_boot"] = [est, lo, hi]
    except Exception as e:  # noqa: BLE001
        models["logit_main"] = {"error": str(e)}
    # does the ladder add information beyond solver metrics?
    D2 = D.assign(log_conf=np.log1p(D["conflicts"]))
    for name, f in {"metrics_only": "exact ~ log_conf + mus_mean + n_clues + C(family) + C(model)",
                    "metrics_plus_level": "exact ~ level + log_conf + mus_mean + n_clues + C(family) + C(model)"}.items():
        try:
            fit = smf.logit(f, D2).fit(disp=0, maxiter=200)
            models[name] = {"params": fit.params.to_dict(), "pvalues": fit.pvalues.to_dict(), "aic": fit.aic, "llf": fit.llf}
        except Exception as e:  # noqa: BLE001
            models[name] = {"error": str(e)}
    # mixed model on cell accuracy (random intercept per puzzle)
    try:
        mm = smf.mixedlm("cell_acc ~ level + C(family) + C(model)", D, groups=D["id"]).fit()
        models["mixed_cell"] = {"params": mm.params.to_dict(), "bse": mm.bse.to_dict(),
                                "pvalues": mm.pvalues.to_dict()}
    except Exception as e:  # noqa: BLE001
        models["mixed_cell"] = {"error": str(e)}
    # per family x model logistic slope on level (where identifiable)
    slopes = []
    for (fam, mod), g in D.groupby(["family", "model"]):
        if g["exact"].nunique() < 2:
            slopes.append({"family": fam, "model": mod, "slope": None, "note": "no variation in outcome"})
            continue
        rho, p = stats.spearmanr(g["level"], g["cell_acc"])
        slopes.append({"family": fam, "model": mod, "spearman_level_cellacc": float(rho), "p": float(p)})
    res["per_family_model"] = slopes
    res["models"] = models
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "summary.json").write_text(json.dumps(res, indent=1, default=float))
    return res


if __name__ == "__main__":
    r = main()
    for a in r["accuracy_by_family"]:
        print(a)
    print(json.dumps(r["models"].get("logit_main", {}), indent=0, default=float)[:800])
