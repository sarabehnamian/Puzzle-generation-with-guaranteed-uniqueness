# Datasheet: certified logic-puzzle benchmark

Structure follows "Datasheets for Datasets" (Gebru et al., 2021).

## Motivation
A reasoning benchmark whose items are generated fresh, carry a solver certificate of a unique
answer, and carry a certified difficulty level. Anyone can regenerate new, never-published items
with the same code and a new seed, which avoids training-data contamination.

## Composition
`puzzles.jsonl`, one JSON object per puzzle (counts per family and level in `summary.json`):

| field | meaning |
|---|---|
| `id` | unique id (`<bank>-<index>`, `-L1aug` = redundant clues added to reach level 1, `e4s-...` = evolved) |
| `family` | `zebra`, `sudoku` (9x9), `killer` (6x6, 2x3 boxes), `futoshiki` (5x5) |
| `source` | `e3-minimal`, `e3-augmented`, `bank`, `e4-evolved-final` |
| `prompt` | the exact text shown to LLM solvers in this study |
| `answer_format` | expected answer JSON |
| `clues` | clue list; zebra clues include the ground-truth DSL expression |
| `solution` | the certified unique solution |
| `level` | difficulty ladder level L1-L5 (see paper, Sec. 2.2) |
| `certificate` | uniqueness proven by MiniSat (solve, block, re-solve = UNSAT) and independently by OR-tools CP-SAT |
| `metrics` | clue count, MiniSat decisions/conflicts/propagations, mean/max minimal-explanation size, clue redundancy, fraction of variables fixed after each ladder level |
| `explanations` | for every non-given fact, a minimal set of clue numbers that forces it (group-MUS) |
| `spec` | machine-readable puzzle definition used by `src/` |

All items except `-L1aug` and evolved ones are clue-minimal: removing any clue creates a second solution.

## Collection process
Solutions are drawn uniformly at random from each family's generator (seeded); clues come from
the true clue pool; uniqueness is reached and then the clue set is minimised in random order.
No human data and no LLM output is part of the puzzle content, except zebra text templates
written by the authors.

## Recommended use
Report exact-solution and cell accuracy; report results per level. For contamination-free
evaluation regenerate items with `python -m src.build_bank` and a new seed in `configs/config.json`.

## Known limitations
* Zebra clues are rendered from templates; one "hard" template ("at least one house separates")
  is ambiguous (see paper, E1). It does not occur in the plain-style zebra items released here.
* Sudoku items stop at L3: none of 9,500 random minimal Sudokus reached L4.
* Ladder levels depend on our CNF encoding at L1 (unit propagation); L2+ are encoding independent
  per constraint.

## Licence
Code and data: MIT (see repository LICENSE).
