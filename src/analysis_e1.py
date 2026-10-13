"""E1 summary: single-encoding error, dual-encoding disagreement and detection, taxonomy."""
import collections
import json
from pathlib import Path

from .stats import boot_mean

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "e1"
ENC = {"A": "Sonnet (A)", "B": "Sonnet (B)", "C": "Haiku (C)"}


def main():
    R = [json.loads(l) for l in (OUT / "records.jsonl").read_text().splitlines() if l.strip()]
    S = {"n_puzzles": len(R), "styles": {}}
    for style in ["plain", "hard", "paraphrase", "all"]:
        rs = R if style == "all" else [r for r in R if r["style"] == style]
        d = {"n": len(rs), "n_clues": sum(r["n_clues"] for r in rs)}
        for e in ENC:
            wrong = [0 if r[e]["equiv_gt"] else 1 for r in rs]
            ans = [0 if r[e]["answer_correct"] else 1 for r in rs]
            clue_err = sum(len(r[e]["clue_errors"]) for r in rs)
            caught = [r for r in rs if not r[e]["equiv_gt"] and r[e]["n_solutions"] != 1]
            d[e] = {"puzzle_error": boot_mean(wrong), "answer_error": boot_mean(ans),
                    "clue_errors": clue_err, "clue_error_rate": clue_err / max(1, d["n_clues"]),
                    "invalid": sum(not r[e]["valid"] for r in rs),
                    "wrong_but_not_unique": len(caught)}
        for pair in ["AB", "AC", "BC"]:
            x, y = pair
            dis = [0 if r[f"{pair}_equiv"] else 1 for r in rs]
            either = [r for r in rs if not (r[x]["equiv_gt"] and r[y]["equiv_gt"])]
            det = [0 if r[f"{pair}_equiv"] else 1 for r in either]
            both_same_wrong = sum(1 for r in either if r[f"{pair}_equiv"])
            d[pair] = {"disagreement": boot_mean(dis), "n_with_error": len(either),
                       "detected": sum(det), "undetected_shared_error": both_same_wrong}
        S["styles"][style] = d
    # taxonomy (clue-level), per style and encoder, and per GT clue type
    tax = collections.defaultdict(collections.Counter)
    by_type = collections.defaultdict(lambda: [0, 0])
    for r in R:
        for e in ENC:
            for c in r[e]["clue_errors"]:
                tax[f"{r['style']}|{e}"][c["cat"]] += 1
        for t in r["clue_types"]:
            by_type[(r["style"], t)][1] += 3
        for e in ENC:
            for c in r[e]["clue_errors"]:
                by_type[(r["style"], c["type"])][0] += 1
    S["taxonomy"] = {k: dict(v) for k, v in tax.items()}
    S["error_rate_by_clue_type"] = {f"{s}|{t}": {"errors": v[0], "encodings": v[1]} for (s, t), v in by_type.items()}
    # examples for the audit
    ex = []
    for r in R:
        for e in ENC:
            for c in r[e]["clue_errors"]:
                ex.append({"puzzle": r["id"], "style": r["style"], "encoder": e, **c})
    (OUT / "error_examples.jsonl").write_text("".join(json.dumps(x) + "\n" for x in ex))
    (OUT / "summary.json").write_text(json.dumps(S, indent=1))
    return S


if __name__ == "__main__":
    s = main()
    for st, d in s["styles"].items():
        print(st, d["n"], {e: (round(d[e]["puzzle_error"][0], 3), d[e]["clue_errors"], d[e]["wrong_but_not_unique"]) for e in ENC},
              {p: (round(d[p]["disagreement"][0], 3), d[p]["n_with_error"], d[p]["detected"]) for p in ["AB", "AC", "BC"]})
    print(json.dumps(s["taxonomy"], indent=0))
