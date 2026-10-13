"""Audit which tools each LLM worker actually called.

Reads the subagent transcripts (JSONL, kept outside the repository) and, for
every call in the ledger that we can match by its task-file path, lists the
tool calls made.  Writes results/tool_audit.json.
Usage: python -m src.tool_audit <transcript_dir>
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK_RE = re.compile(r"llm_tasks/([\w-]+)/([\w-]+)\.md")


def main(tdir):
    found = {}
    for f in sorted(Path(tdir).glob("*.output")):
        calls, cid = [], None
        for line in f.read_text(errors="ignore").splitlines():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            m = d.get("message")
            c = m.get("content") if isinstance(m, dict) else None
            if isinstance(c, str) and cid is None:
                mm = TASK_RE.search(c)
                if mm:
                    cid = mm.group(2)
            if isinstance(c, list):
                for b in c:
                    if not isinstance(b, dict):
                        continue
                    if b.get("type") == "text" and cid is None:
                        mm = TASK_RE.search(b.get("text", ""))
                        if mm:
                            cid = mm.group(2)
                    if b.get("type") == "tool_use":
                        calls.append(b["name"])
        if cid:
            found[cid] = calls
    L = [json.loads(l) for l in (ROOT / "results" / "ledger.jsonl").read_text().splitlines() if l.strip()]
    allowed = {"Read", "Write", "SubagentHandback"}
    rows, names = [], Counter()
    for r in L:
        calls = found.get(r["call_id"])
        if calls is None:
            continue
        names.update(calls)
        other = [c for c in calls if c not in allowed]
        rows.append({"call_id": r["call_id"], "ledger_tool_uses": r["tool_uses"], "tools": dict(Counter(calls)),
                     "forbidden": other})
    out = {"n_ledger": len(L), "n_matched": len(rows), "tool_counts": dict(names),
           "n_with_forbidden_tool": sum(1 for r in rows if r["forbidden"]),
           "n_ledger_over_3": sum(1 for r in L if r["tool_uses"] > 3),
           "over_3_explained": [r for r in rows if r["ledger_tool_uses"] > 3]}
    (ROOT / "results" / "tool_audit.json").write_text(json.dumps(out, indent=1))
    print(json.dumps({k: v for k, v in out.items() if k != "over_3_explained"}, indent=1))
    for r in out["over_3_explained"]:
        print(r)


if __name__ == "__main__":
    main(sys.argv[1])
