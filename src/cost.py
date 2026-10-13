"""Token and cost accounting from results/ledger.jsonl.

Each subagent call reports only its total token count.  We estimate cost with
an explicit, conservative split: the fixed per-call context of the subagent
harness (measured at ~50k tokens from a trivial call) is billed as uncached
input, the task file as input, and the rest as output.  Real billing with
prompt caching would be lower.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICE = {  # USD per million tokens (input, output), first-party list prices
    "haiku": (0.10, 0.50), "sonnet": (2.00, 10.00), "opus": (4.00, 20.00),
}
OVERHEAD = 50_000


def estimate(rec):
    tin, tout = PRICE[rec["model"]]
    task_tokens = 0
    tp = ROOT / "data" / "llm_tasks" / rec["stage"] / f"{rec['call_id']}.md"
    if tp.exists():
        task_tokens = len(tp.read_text()) // 4
    inp = min(rec["subagent_tokens"], OVERHEAD + task_tokens)
    out = max(0, rec["subagent_tokens"] - inp)
    return inp, out, (inp * tin + out * tout) / 1e6


def summary():
    L = [json.loads(l) for l in (ROOT / "results" / "ledger.jsonl").read_text().splitlines() if l.strip()]
    by_stage = defaultdict(lambda: {"calls": 0, "tokens": 0, "usd": 0.0})
    by_model = defaultdict(lambda: {"calls": 0, "tokens": 0, "usd": 0.0})
    for r in L:
        _, _, usd = estimate(r)
        exp = r["stage"].split("_")[0]
        exp = "probe" if exp.startswith("probe") else ("e4" if exp.startswith("e4") else exp)
        for d, k in ((by_stage, exp), (by_model, r["model"])):
            d[k]["calls"] += 1
            d[k]["tokens"] += r["subagent_tokens"]
            d[k]["usd"] += usd
    tot = {"calls": len(L), "tokens": sum(r["subagent_tokens"] for r in L),
           "usd": sum(estimate(r)[2] for r in L),
           "tool_use_violations": sum(1 for r in L if r["tool_uses"] > 3)}
    out = {"total": tot, "by_experiment": by_stage, "by_model": by_model,
           "assumptions": {"prices_per_mtok": PRICE, "fixed_overhead_tokens_as_input": OVERHEAD}}
    (ROOT / "results" / "cost_summary.json").write_text(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    print(json.dumps(summary(), indent=1))
