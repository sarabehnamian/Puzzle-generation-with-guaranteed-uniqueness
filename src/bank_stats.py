"""Summarise the certified puzzle banks: level distribution, clue counts, timing-free metrics."""
import collections
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    out = {}
    for p in sorted((ROOT / "data" / "bank").glob("*.jsonl")):
        recs = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
        lv = collections.Counter(r["analysis"]["level"] for r in recs)
        out[p.stem] = {
            "n": len(recs),
            "levels": {str(k): lv[k] for k in sorted(lv)},
            "clues_mean": statistics.mean(r["analysis"]["n_clues"] for r in recs),
            "all_unique_sat": all(r["analysis"]["unique"] for r in recs),
            "all_unique_cpsat": all(r["analysis"]["cpsat_unique"] for r in recs),
        }
    prev = ROOT / "results" / "bank_stats.json"
    if prev.exists():   # keep entries for banks that were deleted after summarising
        old = json.loads(prev.read_text())
        for k, v in old.items():
            out.setdefault(k, v)
    prev.parent.mkdir(exist_ok=True)
    prev.write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
