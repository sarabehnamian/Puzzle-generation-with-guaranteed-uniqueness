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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4s_mut_g0/e4s_mut_g0_0.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4s-g0-00

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. 6 . | 2 . . | . 5 .
. . . | . . . | 9 . .
7 . 8 | . 6 4 | . . .
---------------------
. 9 4 | . . 1 | 5 . .
. . 7 | 4 . . | . 3 .
. . 2 | . . 8 | . . .
---------------------
1 . . | . 5 7 | . . 4
. . . | . . . | 8 . .
. . . | . . . | 3 1 .

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
Solver mistakes: R3C5 (wrote 4, correct 6); R3C6 (wrote 6, correct 4); R4C2 (wrote 4, correct 9); R4C3 (wrote 7, correct 4); R4C9 (wrote 1, correct 7); R7C6 (wrote 9, correct 7); R7C8 (wrote 7, correct 9); R9C5 (wrote 7, correct 4); R9C6 (wrote 4, correct 9)

## Puzzle e4s-g0-01

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. 9 . | 5 3 . | . . .
6 . . | . 9 . | 1 . .
. . 3 | . . . | 7 . .
---------------------
. . . | . . . | 6 2 .
. 1 . | . . 2 | . 9 .
. . 4 | 8 . . | . . .
---------------------
. . . | . . 7 | . . 3
. 8 7 | . 1 . | 2 . .
5 . . | . 6 . | . . .

Solution:
798531462
642798135
153426789
879153624
315642897
264879351
426987513
987315246
531264978
Solver mistakes: none - the solver got it fully right

## Puzzle e4s-g0-02

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. . 5 | . . . | . 7 8
. 6 . | . . 5 | . . .
2 . . | 8 . . | 4 . .
---------------------
. 3 . | . 7 . | . . 4
. . 1 | . 5 . | . 8 .
. . . | 9 . 8 | . . .
---------------------
7 . . | . . . | . . .
. . . | 3 8 6 | . . .
. . . | 7 . . | 2 9 .

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
Solver mistakes: none - the solver got it fully right

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
Solver mistakes: none - the solver got it fully right

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
Solver mistakes: none - the solver got it fully right
