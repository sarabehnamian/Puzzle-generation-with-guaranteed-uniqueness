# Task: make fair Sudoku puzzles harder for language-model solvers

Each 9x9 Sudoku below has a known unique solution. A language-model solver attempted it; its mistakes
are listed. Propose 2 variants of each puzzle that you expect to be HARDER for a language-model
solver while staying solvable by step-by-step logic (no guessing).

You edit puzzles with operations on the given digits (the digit placed is always the solution digit):
- {"op": "remove", "cell": "RrCc"}            remove a given
- {"op": "add", "cell": "RrCc"}               add a given
- {"op": "move", "from": "RrCc", "to": "RrCc"}  move a given to another cell
Use 1 to 6 operations per variant. A program will add givens back if the result has more than one
solution and will reject variants that need guessing, so focus on what makes the logic harder to
follow (for example: fewer givens, givens spread so that no row/column/box is nearly complete,
removing givens that make singles easy).

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4s_mut_g3\e4s_mut_g3_1.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4s-g3-06

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
8 . 6 | . 1 9 | . . .
4 1 . | . . 7 | . . .
. . . | . . 2 | 9 . .
---------------------
. . 3 | . . . | 4 . .
. . 8 | . . 4 | 5 . .
1 9 . | . . . | 8 . .
---------------------
7 . . | . 6 8 | . . 4
. . . | . . . | . 3 5
9 4 . | . 3 . | . 6 .

Solution:
826419357
419357682
357682941
573826419
268194573
194573826
735268194
682941735
941735268
Solver mistakes: R2C8 (wrote 2, correct 8); R2C9 (wrote 8, correct 2); R4C2 (wrote 3, correct 7); R4C3 (wrote 8, correct 3); R4C4 (wrote 2, correct 8); R4C5 (wrote 6, correct 2); R4C6 (wrote 4, correct 6); R4C7 (wrote 7, correct 4); R9C9 (wrote 2, correct 8)

## Puzzle e4s-g3-04

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
8 . 6 | . 1 . | . . .
4 1 . | . . 7 | . 8 .
. . . | . 8 2 | 9 . .
---------------------
. . 3 | . . . | 4 . .
. . 8 | . . 4 | 5 7 .
. . . | 5 . 3 | 8 . .
---------------------
7 . . | 2 . 8 | . . 4
. . . | . . 1 | . . 5
9 . . | . 3 . | 2 . .

Solution:
826419357
419357682
357682941
573826419
268194573
194573826
735268194
682941735
941735268
Solver mistakes: R2C8 (wrote 2, correct 8); R2C9 (wrote 8, correct 2); R3C5 (wrote 2, correct 8); R3C6 (wrote 8, correct 2); R8C3 (wrote 9, correct 2); R8C4 (wrote 4, correct 9); R8C5 (wrote 1, correct 4); R8C6 (wrote 5, correct 1); R8C9 (wrote 6, correct 5); R9C6 (wrote 6, correct 5); R9C7 (wrote 5, correct 2); R9C8 (wrote 2, correct 6)

## Puzzle e4s-g3-00

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
6 . . | . 7 . | . 3 .
. . 8 | . 6 5 | . 7 .
. 4 9 | 8 . . | . . 5
---------------------
8 3 . | . 1 6 | . . 7
. . 2 | . 8 . | . . .
. 6 4 | . 9 . | 5 . .
---------------------
. . 7 | . . . | 6 . .
. 9 3 | . 5 . | . 4 .
. . . | 7 4 1 | . . 9

Solution:
651974832
328165974
749832165
835416297
972583416
164297583
417329658
293658741
586741329
Solver mistakes: R4C4 (wrote 1, correct 4); R4C5 (wrote 6, correct 1); R4C6 (wrote 4, correct 6); R4C8 (wrote 7, correct 9); R4C9 (wrote 9, correct 7); R7C5 (wrote 6, correct 2); R7C6 (wrote 5, correct 9); R7C7 (wrote 9, correct 6); R7C8 (wrote 2, correct 5)
