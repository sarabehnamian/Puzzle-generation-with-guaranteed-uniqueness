"""File-based protocol for LLM calls.

No API key was available in the environment where this study was run, so
every LLM call is executed by a fresh, isolated Claude Code subagent (no
shared context).  A pipeline stage writes one *task file* per call; the
orchestrator starts one subagent per task file with ``WORKER_PROMPT``; the
subagent reads the task, reasons without tools, and writes a JSON *output
file*.  The orchestrator then records the token usage reported for that call
in ``results/ledger.jsonl``.  Stages are resumable: a call whose output file
exists is never repeated.

With an API key the same task files can be run by ``run_api`` below (one
Messages API request per task; untested in this study).
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "data" / "llm_tasks"
LEDGER = ROOT / "results" / "ledger.jsonl"

MODELS = {"haiku": "claude-haiku-5-5", "sonnet": "claude-sonnet-5-5", "opus": "claude-opus-5-5"}

WORKER_PROMPT = (
    "You are one isolated call in a research pipeline. Rules: use ONLY the Read tool to read the task "
    "file, and the Write tool to write the single output file the task names. Do NOT run code, Bash, "
    "search, or use any other tool, and do not read any other file. Reason in your head. When finished, "
    'reply with one short line "done".\nTask file: {path}'
)


def task_dir(stage):
    d = TASKS / stage
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_task(stage, call_id, model, instructions, items, item_ids):
    d = task_dir(stage)
    task = d / f"{call_id}.md"
    out = d / f"{call_id}.out.json"
    body = instructions.replace("{OUT}", str(out)) + "\n\n" + items
    task.write_text(body)
    rec = {"stage": stage, "call_id": call_id, "model": model, "items": item_ids,
           "task": str(task.relative_to(ROOT)), "out": str(out.relative_to(ROOT))}
    man = d / "manifest.jsonl"
    existing = {}
    if man.exists():
        for line in man.read_text().splitlines():
            r = json.loads(line)
            existing[r["call_id"]] = r
    existing[call_id] = rec
    man.write_text("".join(json.dumps(r) + "\n" for r in existing.values()))
    return rec


def manifest(stage):
    man = task_dir(stage) / "manifest.jsonl"
    if not man.exists():
        return []
    return [json.loads(l) for l in man.read_text().splitlines() if l.strip()]


def read_output(rec):
    p = ROOT / rec["out"]
    if not p.exists():
        return None
    txt = p.read_text().strip()
    if txt.startswith("```"):
        txt = txt.strip("`")
        txt = txt[txt.index("\n") + 1:] if "\n" in txt else txt
    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        # tolerate trailing text after the JSON object
        try:
            return json.JSONDecoder().raw_decode(txt)[0]
        except json.JSONDecodeError:
            return {"_parse_error": True, "_raw": txt[:2000]}


def pending(stage):
    return [r for r in manifest(stage) if not (ROOT / r["out"]).exists()]


def log_usage(stage, call_id, tokens, tool_uses, duration_ms, model=None):
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    if model is None:
        model = {r["call_id"]: r["model"] for r in manifest(stage)}.get(call_id)
    rec = {"stage": stage, "call_id": call_id, "model": model, "model_id": MODELS.get(model, model),
           "subagent_tokens": int(tokens), "tool_uses": int(tool_uses), "duration_ms": int(duration_ms),
           "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
    with LEDGER.open("a") as f:
        f.write(json.dumps(rec) + "\n")
    return rec


def ledger():
    if not LEDGER.exists():
        return []
    return [json.loads(l) for l in LEDGER.read_text().splitlines() if l.strip()]


def run_api(stage, max_tokens=16000):  # pragma: no cover - needs ANTHROPIC_API_KEY
    import anthropic
    client = anthropic.Anthropic()
    for rec in pending(stage):
        text = (ROOT / rec["task"]).read_text()
        text += "\n\n(Return the JSON as your whole reply instead of writing a file.)"
        msg = client.messages.create(model=MODELS[rec["model"]], max_tokens=max_tokens,
                                     messages=[{"role": "user", "content": text}])
        out = "".join(b.text for b in msg.content if b.type == "text")
        (ROOT / rec["out"]).write_text(out)
        log_usage(stage, rec["call_id"], msg.usage.input_tokens + msg.usage.output_tokens, 0, 0, rec["model"])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "pending":
        for r in pending(sys.argv[2]):
            print(r["call_id"], r["model"], r["task"])
    elif cmd == "log":
        # log <stage> <call_id>:<tokens>:<tool_uses>:<ms> ...
        stage = sys.argv[2]
        for spec in sys.argv[3:]:
            cid, tok, tu, ms = spec.split(":")
            r = log_usage(stage, cid, tok, tu, ms)
            if int(tu) > 3:
                print("WARNING: tool_uses > 3 for", cid)
        print("logged", len(sys.argv) - 3)
    elif cmd == "total":
        L = ledger()
        print(len(L), "calls,", sum(r["subagent_tokens"] for r in L), "tokens")
