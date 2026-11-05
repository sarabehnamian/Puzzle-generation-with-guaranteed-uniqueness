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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4s_mut_g1\e4s_mut_g1_1.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4s-g0-06

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. . . | . . . | . . 7
. 2 4 | . . . | . 9 .
1 . . | 3 . 6 | 2 . .
---------------------
. 5 . | 6 . . | . . .
. . . | 2 4 . | . . .
. . . | 8 . . | 1 3 6
---------------------
6 . . | . . . | . 8 .
. . 9 | . . 4 | . . .
8 . . | 1 . . | 3 . .

Solution:
963452817
524718693
187396254
758631942
316249578
492875136
671923485
239584761
845167329
Solver mistakes: R2C3 (wrote 1, correct 4); R2C4 (wrote 8, correct 7); R2C5 (wrote 7, correct 1); R2C6 (wrote 1, correct 8)

## Puzzle e4s-g1-03

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. . . | . 5 . | . . 7
5 2 4 | . . . | . 9 .
1 . . | 3 . 6 | 2 . .
---------------------
. 5 . | . . . | . . .
. . . | 2 4 . | . . .
. . . | 8 . . | 1 3 6
---------------------
6 7 . | . . . | 4 8 .
. . 9 | . . 4 | 7 6 .
. 4 . | 1 . . | 3 . .

Solution:
963452817
524718693
187396254
758631942
316249578
492875136
671923485
239584761
845167329
Solver mistakes: R2C3 (wrote 7, correct 4); R2C4 (wrote 1, correct 7); R2C5 (wrote 8, correct 1); R2C6 (wrote 6, correct 8); R2C7 (wrote 9, correct 6); R2C8 (wrote 3, correct 9); R2C9 (wrote 0, correct 3)

## Puzzle e4s-g1-08

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. . . | . . . | . 7 8
. 6 . | . . 5 | . . .
2 . . | 8 . . | 4 5 1
---------------------
. 3 . | . 7 . | . . 4
. . 1 | . 5 . | . 8 9
. . . | 9 . 8 | . . .
---------------------
7 . . | . . 9 | . 6 .
. . . | 3 8 6 | . . .
. . . | 7 . . | 2 . .

Solution:
145293678
867145932
293867451
938671524
671452389
452938716
714529863
529386147
386714295
Solver mistakes: R4C3 (wrote 6, correct 8); R4C4 (wrote 7, correct 6); R4C5 (wrote 1, correct 7); R4C6 (wrote 8, correct 1); R9C8 (wrote 5, correct 9); R9C9 (wrote 9, correct 5)
