"""Drive one experiment end to end through the Messages API.

Runs the README command order for the chosen experiment; after every command,
the experiment's own stages that have pending calls are sent to the API
(src.llm.run_api).  Experiments only touch their own stage prefix, so several
can run at once in separate processes.

    python -m src.rerun_api e1|e2|e3|e4b|e4s|e5
"""
import json
import os
import subprocess
import sys

from . import llm

PY = sys.executable
ENV = {**os.environ, "PYTHONUTF8": "1"}  # Windows defaults to cp1252 otherwise
PREFIX = {"e1": "e1_", "e2": "e2_", "e3": "e3_", "e4b": "e4b_", "e4s": "e4s_", "e5": "e5_"}


def sh(*args):
    print(">>", " ".join(args), flush=True)
    r = subprocess.run([PY, "-m", *args], capture_output=True, text=True, encoding="utf-8", env=ENV)
    print(r.stdout[-3000:], r.stderr[-3000:], flush=True)
    if r.returncode:
        raise SystemExit(f"command failed: {args}")
    return r.stdout


def flush(exp):
    """Send this experiment's pending calls to the API until none is pending."""
    for attempt in range(3):
        stages = [d.name for d in llm.TASKS.iterdir()
                  if d.is_dir() and d.name.startswith(PREFIX[exp]) and llm.pending(d.name)]
        if not stages:
            return
        for s in stages:
            llm.run_api(s)
    raise SystemExit(f"{exp}: stages still pending after 3 rounds")


def step(exp, *args):
    out = sh(*args)
    flush(exp)
    return out


def evolve(exp, run_arg):
    state = llm.ROOT / "data" / exp / "state.json"
    for _ in range(40):
        step(exp, "src.e4_evolution", run_arg)
        if state.exists() and json.loads(state.read_text())["phase"] == "done":
            break
    else:
        raise SystemExit("evolution did not finish")
    step(exp, "src.e4_evolution", run_arg, "heldout")   # writes held-out tasks, runs them
    sh("src.e4_evolution", run_arg, "heldout")          # scores


PLANS = {
    "e1": lambda: [step("e1", "src.e1_faithfulness", "prepare_paraphrase"),
                   step("e1", "src.e1_faithfulness", "prepare_encoders"),
                   sh("src.e1_faithfulness", "analyze"), sh("src.analysis_e1")],
    "e2": lambda: [step("e2", "src.e2_validity", "prepare_gen"), step("e2", "src.e2_validity", "prepare_enc"),
                   step("e2", "src.e2_validity", "prepare_repair1"), sh("src.e2_validity", "summarize")],
    "e3": lambda: [step("e3", "src.e3_difficulty", "prepare"), sh("src.e3_difficulty", "score"),
                   sh("src.analysis_e3")],
    "e4b": lambda: evolve("e4b", "e4"),
    "e4s": lambda: evolve("e4s", "e4s"),
    "e5": lambda: [step("e5", "src.e5_genres", "prepare"), step("e5", "src.e5_genres", "run"),
                   step("e5", "src.e5_genres", "prepare_solve"), sh("src.e5_genres", "score_solve")],
}

if __name__ == "__main__":
    assert sys.flags.utf8_mode, "run with PYTHONUTF8=1 (or python -X utf8)"
    PLANS[sys.argv[1]]()
    print("DONE", sys.argv[1])
