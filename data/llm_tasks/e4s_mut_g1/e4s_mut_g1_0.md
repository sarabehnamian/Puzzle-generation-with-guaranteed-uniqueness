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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4s_mut_g1\e4s_mut_g1_0.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4s-g1-05

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
6 . . | . 7 . | . 3 .
. . 8 | . 6 5 | . 7 .
. 4 9 | 8 . . | . . 5
---------------------
8 3 . | . 1 . | . . 7
. . 2 | . 8 3 | . . .
. . 4 | . 9 . | 5 . .
---------------------
. . 7 | . . . | . . .
2 9 3 | . 5 . | . . .
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
Solver mistakes: no answer given

## Puzzle e4s-g0-05

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
8 . 6 | . 1 . | . . .
4 1 . | . . 7 | . . .
. . . | . 8 2 | 9 . .
---------------------
. . 3 | . . . | 4 . .
. . 8 | . . 4 | 5 . .
. . . | . 7 . | 8 . .
---------------------
7 . . | . . 8 | . . 4
. . . | . . . | . 3 .
9 . . | . 3 . | . 6 .

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
Solver mistakes: R2C8 (wrote 2, correct 8); R2C9 (wrote 8, correct 2); R5C1 (wrote 8, correct 2); R5C2 (wrote 2, correct 6); R5C3 (wrote 6, correct 8); R5C6 (wrote 5, correct 4); R5C7 (wrote 7, correct 5); R5C8 (wrote 3, correct 7); R5C9 (wrote 4, correct 3); R8C3 (wrote 9, correct 2); R8C4 (wrote 4, correct 9); R8C5 (wrote 1, correct 4); R8C6 (wrote 3, correct 1); R8C7 (wrote 5, correct 7); R8C8 (wrote 7, correct 3); R8C9 (wrote 3, correct 5)

## Puzzle e4s-g1-01

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
8 . 6 | . 1 . | . . 7
4 1 . | . . 7 | . . .
. . . | . 8 2 | 9 . .
---------------------
. . 3 | . . . | 4 . .
. 6 8 | . 9 4 | 5 7 .
. . . | 5 . 3 | 8 . .
---------------------
7 . . | 2 . 8 | . . 4
. . . | . . . | . . .
9 . . | . 3 . | 2 6 8

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
Solver mistakes: R2C3 (wrote 5, correct 9); R2C5 (wrote 7, correct 5); R2C6 (wrote 5, correct 7); R2C8 (wrote 9, correct 8); R4C6 (wrote 4, correct 6); R4C7 (wrote 6, correct 4); R8C3 (wrote 9, correct 2); R8C4 (wrote 4, correct 9); R8C5 (wrote 1, correct 4); R8C6 (wrote 5, correct 1)

## Puzzle e4s-g1-09

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. . 5 | . . . | . 7 8
8 6 . | . . . | . . .
2 . . | 8 . . | 4 5 1
---------------------
. 3 . | . 7 . | . . 4
. . 1 | . 5 . | . . .
. . . | 9 . 8 | . . .
---------------------
7 . 4 | . 2 . | . 6 .
5 . . | 3 . 6 | . . .
. 8 . | 7 . . | 2 9 .

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
Solver mistakes: R4C3 (wrote 6, correct 8); R4C4 (wrote 7, correct 6); R4C5 (wrote 1, correct 7); R4C6 (wrote 5, correct 1); R4C7 (wrote 2, correct 5); R4C8 (wrote 8, correct 2); R7C3 (wrote 5, correct 4); R7C4 (wrote 2, correct 5); R7C5 (wrote 9, correct 2); R7C6 (wrote 6, correct 9)

## Puzzle e4s-g1-10

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
4 6 . | 2 1 . | . 5 .
2 . 1 | . . . | 9 . .
. . 8 | . 6 4 | . . .
---------------------
6 9 4 | . . 1 | 5 . .
. . . | 4 . 6 | . 3 1
. . 2 | . . 8 | . . .
---------------------
1 . . | . 5 7 | . . 4
. . . | . . . | 8 . .
. 7 . | . . . | 3 . .

Solution:
469213758
231785946
758964123
694321587
587496231
312578469
123857694
946132875
875649312
Solver mistakes: R1C6 (wrote 5, correct 3); R1C7 (wrote 3, correct 7); R1C8 (wrote 7, correct 5); R7C6 (wrote 6, correct 7); R7C7 (wrote 7, correct 6); R9C2 (wrote 5, correct 7); R9C3 (wrote 7, correct 5); R9C4 (wrote 4, correct 6); R9C5 (wrote 6, correct 4)
