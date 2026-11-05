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
    task.write_text(body, encoding="utf-8")
    rec = {"stage": stage, "call_id": call_id, "model": model, "items": item_ids,
           "task": str(task.relative_to(ROOT)), "out": str(out.relative_to(ROOT))}
    man = d / "manifest.jsonl"
    existing = {}
    if man.exists():
        for line in man.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            existing[r["call_id"]] = r
    existing[call_id] = rec
    man.write_text("".join(json.dumps(r) + "\n" for r in existing.values()), encoding="utf-8")
    return rec


def manifest(stage):
    man = task_dir(stage) / "manifest.jsonl"
    if not man.exists():
        return []
    return [json.loads(l) for l in man.read_text(encoding="utf-8").splitlines() if l.strip()]


def read_output(rec):
    p = ROOT / rec["out"]
    if not p.exists():
        return None
    txt = p.read_text(encoding="utf-8").strip()
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
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    return rec


def ledger():
    if not LEDGER.exists():
        return []
    return [json.loads(l) for l in LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()]


API_EFFORT = "high"        # same effort for every model (Haiku/Opus default to medium, Sonnet to high)
API_MAX_TOKENS = 128000    # model maximum; streamed, so no HTTP timeout risk
API_WORKERS = 8
API_NOTE = ("\n\n(Return only the JSON object described above as your whole reply, "
            "with no text before or after it.)")


def _api_call(client, stage, rec):  # pragma: no cover - needs ANTHROPIC_API_KEY
    import re
    text = (ROOT / rec["task"]).read_text(encoding="utf-8")
    # the task files were written for file-writing subagents; through the API the JSON is the reply
    text = re.sub(r"write a single JSON object to the file \S+", "reply with a single JSON object", text)
    text += API_NOTE
    t0 = time.time()
    with client.messages.stream(model=MODELS[rec["model"]], max_tokens=API_MAX_TOKENS,
                                thinking={"type": "adaptive"},
                                output_config={"effort": API_EFFORT},
                                messages=[{"role": "user", "content": text}]) as s:
        msg = s.get_final_message()
    ms = int((time.time() - t0) * 1000)
    out = "".join(b.text for b in msg.content if b.type == "text")
    u = msg.usage
    rec_l = {"stage": stage, "call_id": rec["call_id"], "model": rec["model"], "model_id": msg.model,
             "api": True, "input_tokens": u.input_tokens, "output_tokens": u.output_tokens,
             "cache_read_input_tokens": u.cache_read_input_tokens or 0,
             "cache_creation_input_tokens": u.cache_creation_input_tokens or 0,
             "subagent_tokens": u.input_tokens + u.output_tokens, "tool_uses": 0,
             "duration_ms": ms, "stop_reason": msg.stop_reason, "message_id": msg.id,
             "effort": API_EFFORT, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
    if msg.stop_reason == "refusal":
        # keep the raw text for inspection but do not write the output file, so the call stays pending
        (ROOT / rec["out"]).with_suffix(".refusal.txt").write_text(out, encoding="utf-8")
    else:
        # max_tokens at the model's output limit counts as "no answer": whatever text exists is kept
        # (usually none, which the collectors record as a parse error, i.e. graded wrong)
        (ROOT / rec["out"]).write_text(out, encoding="utf-8")
    return rec_l


def run_api(stage, workers=API_WORKERS, limit=None):  # pragma: no cover - needs ANTHROPIC_API_KEY
    """Run every pending call of ``stage`` through the Messages API, in parallel.

    Resumable like the subagent protocol: a call whose output file exists is skipped.
    Calls that end in a refusal or hit max_tokens are logged and left pending.
    """
    import threading
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import anthropic
    client = anthropic.Anthropic(max_retries=8)
    todo = pending(stage)[:limit] if limit else pending(stage)
    lock = threading.Lock()
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    fails = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_api_call, client, stage, r): r for r in todo}
        for f in as_completed(futs):
            r = futs[f]
            try:
                L = f.result()
            except Exception as e:  # noqa: BLE001 - one bad call must not stop the stage
                fails += 1
                print(f"FAIL {r['call_id']}: {type(e).__name__}: {e}", flush=True)
                continue
            with lock, LEDGER.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(L) + "\n")
            print(f"{L['call_id']:<28} {L['model']:<6} in={L['input_tokens']:>6} out={L['output_tokens']:>6} "
                  f"{L['duration_ms'] / 1000:5.0f}s {L['stop_reason']}", flush=True)
    print(f"{stage}: {len(todo) - fails} done, {fails} failed, {len(pending(stage))} still pending")


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
    elif cmd == "api":
        # run all pending calls of a stage through the Messages API (needs ANTHROPIC_API_KEY)
        # api <stage> [limit]
        run_api(sys.argv[2], limit=int(sys.argv[3]) if len(sys.argv) > 3 else None)
    elif cmd == "total":
        L = ledger()
        print(len(L), "calls,", sum(r["subagent_tokens"] for r in L), "tokens")
