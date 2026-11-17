# Extension: certified frontier banks at new sizes + fresh-seed eval protocol

This extension pushes the pipeline's certified generation to sizes beyond the released
benchmark, and adds fresh-seed banks for contamination-free evaluation. Every item is
re-certified unique by MiniSat and OR-Tools CP-SAT through the repo's own
src/export_benchmark.build_item machinery, is minimal (every clue necessary), and carries
its ladder level, solver metrics, and per-fact minimal-unsatisfiable-core explanations.

## Banks (config additions in configs/config.json; seeded and resumable)

| bank | size | n in release | note |
|---|---|---|---|
| zebra_fresh | 5x4 | 100 | fresh rng stream at the released size: contamination-free eval set |
| killer_fresh | 6x6 | 60 | fresh rng stream at the released size |
| zebra_f7 | 7 houses x 5 categories | 100 | NEW SIZE |
| futoshiki_f7 | 7x7 | 100 | NEW SIZE |
| sudoku_f12 | 12x12 (box 3x4) | 59 | NEW SIZE |
| killer_f9 | 9x9 (box 3x3, the classic size) | 17 | NEW SIZE |

n_items: 436

## Why

The paper names larger instances as the open axis: minimal puzzles rarely sit at L1, and top
ladder levels are rare at released sizes (no Sudoku above L3 in 9,500). Larger instances
shift the whole distribution upward, and the fresh-seed banks let models trained on the
released benchmark (or on curricula derived from it) be evaluated on instances that were
never in any training corpus - the pipeline's regenerability used as designed.

The bank is also published at https://huggingface.co/datasets/SZLHOLDINGS/certified-puzzles-frontier-bank-v1
(MIT, attribution Sara Behnamian). Generated on a 4-core laptop with the repo's pinned
requirements; no LLM calls are needed for any of this - generation, certification and
grading are pure solver code.

## Files
- data/puzzles.jsonl - the bank (same schema as benchmark/puzzles.jsonl)
- data/summary.json - per-family/level and per-bank counts
- data/manifest.json - provenance, banks_in_release and sha256
- data/skipped.json - items excluded at export (with reasons), when any

