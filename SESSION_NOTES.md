# Session notes: API rerun + new figures (2–3 Nov 2026)

Where things stand, so the work can continue from here.

## Status in one line
Everything has been rerun through the API, all figures are redrawn, and the paper text is rewritten.
**Nothing is committed yet.** Everything is on branch `api-rerun`; the original study is untouched on `main`.

## What was done
1. **Cloned** the repo and set up a venv at `.venv/` (the pinned versions in `requirements.txt` don't
   install on Python 3.11/Windows, so the packages were installed unpinned).
2. **Reran every LLM experiment (E1–E5) through the Messages API** (the original run used Claude Code
   subagents because there was no API key).
   - Models `claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5`; adaptive thinking, effort `high`,
     128k output limit, no refusal fallback.
   - **One puzzle per solving call** (your decision). With 4–5 puzzles per call, Haiku ran out of tokens
     and Sonnet guessed (Sonnet Sudoku 25% vs 88% with one puzzle per call).
   - **Cost:** 672 calls / **$38** behind the final results; **$63** in total including discarded runs.
3. **Bugs found and fixed**
   - `src/llm.py`: the API runner was untested → now parallel, streamed, retries, exact token logging.
   - `src/solve_stage.py`: single-puzzle replies without the JSON wrapper were scored as "no answer";
     this silently drove the first E4 run. Fixed, with a new test (17 tests pass).
   - `src/e5_genres.py`: genres that defined helper functions could not compile, and the genre name
     was hard-coded. Fixed; the genre is now chosen by a fixed rule (deepest instances).
   - Windows text encoding: always run with `PYTHONUTF8=1`.
4. **Figures (all 7) redrawn:** no text on the data, legends above the panels, drawn at the paper's real
   width (6.69 in), PNG at 600 dpi. The gallery (Fig 7) layout is reorganised; the E4 pilot is dropped
   from Fig 6. Shared style lives in `src/figstyle.py`.
5. **Paper text rewritten** to match the new results: abstract, intro, methods, all results sections
   (E4 Sudoku was "PENDING"), discussion, limitations, data availability, README.
   `paper/main.pdf` builds cleanly (12 pages).

## Main new results (what changed vs the original run)
- E1: Haiku 18% wrong on hard templates (it counts "from the right" from the left). One wrong
  encoding now passes both checks: `paraphrase:zebra-00148`, where Sonnet's paraphrase itself
  changed a clue ("two houses separate" for distance 2).
- E2: all 100 LLM-written puzzles valid; still easy and redundant.
- E3: Sudoku exact: Opus 100%, Sonnet 88%, Haiku 58%. Failures are near misses and don't follow
  the ladder level.
- E4: zebra: Haiku never fails (same as before). Sudoku: evolution found puzzles Haiku fails, but
  they are L1 (easy) and failed by a few cells.
- E5: all 6 genres compile; "Latin Windows" reaches L5; all models solve it.

## Where things are
- Run log of every call: `results/ledger.jsonl` (old subagent run: `results/ledger_subagent.jsonl`)
- Discarded runs (kept for reference): `data/llm_tasks_archive/{batched,parse_bug}/`,
  `data/archive_batched/`, `data/archive_parse_bug/`, `results/archive_batched/`, `results/archive_parse_bug/`
- Run logs: `logs/` (git-ignored)

## Still to do (your decisions)
1. **Read the rewritten paper** (`paper/main.pdf`) and adjust wording as you like.
2. `results/e1/audit.md` is the hand-written audit from the OLD run, now out of date (the paper no
   longer cites it): delete it or redo it.
3. Fix `requirements.txt` pins (they don't install on Python 3.11/Windows).
4. Optional: rerun the E4 pilot (Zebra 5x4, `data/e4`), which is still old subagent data. It's cheap.
5. **Commit** the work on `api-rerun`, then push it or open a PR.

## Useful commands
```bash
# rebuild everything from saved outputs (no API calls)
export PYTHONUTF8=1
.venv/Scripts/python -m pytest -q
for m in fig_example fig_e1 fig_e2 fig_e3 fig_e4 fig_gallery; do .venv/Scripts/python -m src.$m; done
.venv/Scripts/python -m src.cost && .venv/Scripts/python -m src.make_numbers
cd paper && latexmk -pdf main.tex

# rerun one experiment through the API (resumes; finished calls are never repeated)
PYTHONUTF8=1 .venv/Scripts/python -m src.rerun_api e3   # e1 e2 e3 e4b e4s e5
```
