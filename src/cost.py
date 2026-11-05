"""Token and cost accounting.

``results/ledger.jsonl``: calls made through the Messages API (src.llm.run_api); each record
carries the exact input/output token counts reported by the API, so costs are exact at list price.

``results/ledger_subagent.jsonl``: the earlier run, made through Claude Code subagents that report
only a total token count per call.  Its cost is estimated as before: the fixed per-call harness
context (~50k tokens) and the task file billed as input, the rest as output.
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICE = {  # USD per million tokens (input, output), first-party list prices
    "haiku": (0.10, 0.50), "sonnet": (2.00, 10.00), "opus": (4.00, 20.00),
}
OVERHEAD = 50_000


def _read(name):
    p = ROOT / "results" / name
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.exists() else []


def _experiment(stage):
    exp = stage.split("_")[0]
    return "probe" if exp.startswith("probe") else ("e4" if exp.startswith("e4") else exp)


def api_cost(rec):
    tin, tout = PRICE[rec["model"]]
    return (rec["input_tokens"] * tin + rec["output_tokens"] * tout) / 1e6


def subagent_estimate(rec):
    tin, tout = PRICE[rec["model"]]
    tp = ROOT / "data" / "llm_tasks" / rec["stage"] / f"{rec['call_id']}.md"
    task_tokens = len(tp.read_text(encoding="utf-8")) // 4 if tp.exists() else 0
    inp = min(rec["subagent_tokens"], OVERHEAD + task_tokens)
    out = max(0, rec["subagent_tokens"] - inp)
    return (inp * tin + out * tout) / 1e6


def summary():
    L = _read("ledger.jsonl")
    by_exp = defaultdict(lambda: {"calls": 0, "input_tokens": 0, "output_tokens": 0, "tokens": 0, "usd": 0.0})
    by_model = defaultdict(lambda: {"calls": 0, "input_tokens": 0, "output_tokens": 0, "tokens": 0, "usd": 0.0})
    for r in L:
        for d in (by_exp[_experiment(r["stage"])], by_model[r["model"]]):
            d["calls"] += 1
            d["input_tokens"] += r["input_tokens"]
            d["output_tokens"] += r["output_tokens"]
            d["tokens"] += r["input_tokens"] + r["output_tokens"]
            d["usd"] += api_cost(r)
    stops = defaultdict(int)
    for r in L:
        stops[r.get("stop_reason")] += 1
    tot = {"calls": len(L), "tokens": sum(r["input_tokens"] + r["output_tokens"] for r in L),
           "input_tokens": sum(r["input_tokens"] for r in L), "output_tokens": sum(r["output_tokens"] for r in L),
           "usd": sum(api_cost(r) for r in L), "api_estimate_usd": sum(api_cost(r) for r in L),
           "tool_use_violations": 0, "stop_reasons": dict(stops),
           "effort": sorted({r.get("effort") for r in L if r.get("effort")})}
    # calls behind the final results: every call in the current task folders, priced by its last
    # ledger entry (discarded runs live in data/llm_tasks_archive/ and reuse some call ids)
    last = {(r["stage"], r["call_id"]): r for r in L}
    from . import llm
    final = [last[(rec["stage"], rec["call_id"])] for d in sorted(llm.TASKS.iterdir()) if d.is_dir()
             for rec in llm.manifest(d.name) if (rec["stage"], rec["call_id"]) in last]
    tot["final_calls"] = len(final)
    tot["final_usd"] = sum(api_cost(r) for r in final)
    tot["final_tokens"] = sum(r["input_tokens"] + r["output_tokens"] for r in final)
    tot["final_max_tokens"] = sum(r["stop_reason"] == "max_tokens" for r in final)
    S = _read("ledger_subagent.jsonl")
    sub = {"calls": len(S), "tokens": sum(r["subagent_tokens"] for r in S),
           "usd_estimate": sum(subagent_estimate(r) for r in S),
           "tool_use_violations": sum(1 for r in S if r["tool_uses"] > 3)}
    out = {"total": tot, "by_experiment": by_exp, "by_model": by_model, "subagent_run": sub,
           "assumptions": {"prices_per_mtok": PRICE, "api_costs": "exact token counts x list price, no batch discount",
                           "subagent_fixed_overhead_tokens_as_input": OVERHEAD}}
    (ROOT / "results" / "cost_summary.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    return out


if __name__ == "__main__":
    print(json.dumps(summary(), indent=1))
