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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4s_mut_g1/e4s_mut_g1_0.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4s-g1-08

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. . . | . 5 . | . . 7
. 2 4 | . . . | . 9 .
1 . 7 | 3 . 6 | . . .
---------------------
. 5 . | 6 . . | . . .
. . . | 2 4 . | . . .
. . . | 8 . . | 1 3 6
---------------------
6 7 . | . . . | . 8 5
. . 9 | . . 4 | . . .
8 . . | . . . | 3 . .

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
Solver mistakes: R1C1 (wrote 0, correct 9); R1C2 (wrote 0, correct 6); R1C3 (wrote 0, correct 3); R1C4 (wrote 0, correct 4); R1C6 (wrote 0, correct 2); R1C7 (wrote 0, correct 8); R1C8 (wrote 0, correct 1); R2C1 (wrote 0, correct 5); R2C4 (wrote 0, correct 7); R2C5 (wrote 0, correct 1); R2C6 (wrote 0, correct 8); R2C7 (wrote 0, correct 6); R2C9 (wrote 0, correct 3); R3C2 (wrote 0, correct 8); R3C4 (wrote 0, correct 3); R3C5 (wrote 3, correct 9); R3C7 (wrote 0, correct 2); R3C8 (wrote 0, correct 5); R3C9 (wrote 0, correct 4); R4C1 (wrote 0, correct 7); R4C3 (wrote 0, correct 8); R4C5 (wrote 0, correct 3); R4C6 (wrote 0, correct 1); R4C7 (wrote 0, correct 9); R4C8 (wrote 0, correct 4); R4C9 (wrote 0, correct 2); R5C1 (wrote 0, correct 3); R5C2 (wrote 0, correct 1); R5C3 (wrote 0, correct 6); R5C6 (wrote 0, correct 9)

## Puzzle e4s-g1-06

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
8 . 6 | . 1 9 | . . .
4 1 . | . . 7 | . . .
. . . | . 8 2 | . . 1
---------------------
. . 3 | . . . | 4 . .
. . 8 | . . . | 5 7 .
. . . | . 7 . | 8 2 .
---------------------
7 3 . | . . 8 | . . 4
. . . | . 4 . | . 3 5
9 . . | . . 5 | . 6 .

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
Solver mistakes: R1C2 (wrote 0, correct 2); R1C4 (wrote 0, correct 4); R1C7 (wrote 0, correct 3); R1C8 (wrote 0, correct 5); R1C9 (wrote 0, correct 7); R2C3 (wrote 0, correct 9); R2C4 (wrote 0, correct 3); R2C5 (wrote 0, correct 5); R2C7 (wrote 0, correct 6); R2C8 (wrote 0, correct 8); R2C9 (wrote 0, correct 2); R3C1 (wrote 0, correct 3); R3C2 (wrote 0, correct 5); R3C3 (wrote 0, correct 7); R3C4 (wrote 0, correct 6); R3C7 (wrote 0, correct 9); R3C8 (wrote 0, correct 4); R4C1 (wrote 0, correct 5); R4C2 (wrote 0, correct 7); R4C4 (wrote 0, correct 8); R4C5 (wrote 0, correct 2); R4C6 (wrote 0, correct 6); R4C8 (wrote 0, correct 1); R4C9 (wrote 0, correct 9); R5C1 (wrote 0, correct 2); R5C2 (wrote 0, correct 6); R5C4 (wrote 0, correct 1); R5C5 (wrote 0, correct 9); R5C6 (wrote 0, correct 4); R5C9 (wrote 0, correct 3)

## Puzzle e4s-g1-10

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
9 . 4 | . . . | 2 . .
. . 5 | 7 . . | . 8 .
1 . . | . . . | . . 9
---------------------
7 . . | . . . | . 6 .
. 4 . | 8 . . | . . .
2 8 6 | 5 . 7 | . 1 .
---------------------
. 6 7 | 9 . . | . 2 8
. . . | . 2 . | 6 . .
. 1 . | . 7 5 | . . .

Solution:
974381256
625749381
138256749
759413862
341862597
286597413
567934128
493128675
812675934
Solver mistakes: R1C2 (wrote 0, correct 7); R1C4 (wrote 0, correct 3); R1C5 (wrote 0, correct 8); R1C6 (wrote 0, correct 1); R1C8 (wrote 0, correct 5); R1C9 (wrote 0, correct 6); R2C1 (wrote 0, correct 6); R2C2 (wrote 0, correct 2); R2C5 (wrote 0, correct 4); R2C6 (wrote 0, correct 9); R2C7 (wrote 0, correct 3); R2C9 (wrote 0, correct 1); R3C2 (wrote 0, correct 3); R3C3 (wrote 0, correct 8); R3C4 (wrote 0, correct 2); R3C5 (wrote 0, correct 5); R3C6 (wrote 0, correct 6); R3C7 (wrote 0, correct 7); R3C8 (wrote 0, correct 4); R4C2 (wrote 0, correct 5); R4C3 (wrote 0, correct 9); R4C4 (wrote 0, correct 4); R4C5 (wrote 0, correct 1); R4C6 (wrote 0, correct 3); R4C7 (wrote 0, correct 8); R4C9 (wrote 0, correct 2); R5C1 (wrote 0, correct 3); R5C3 (wrote 0, correct 1); R5C5 (wrote 0, correct 6); R5C6 (wrote 0, correct 2)

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
Solver mistakes: R1C1 (wrote 0, correct 4); R1C3 (wrote 0, correct 9); R1C5 (wrote 0, correct 1); R1C6 (wrote 0, correct 3); R1C7 (wrote 0, correct 7); R1C9 (wrote 0, correct 8); R2C1 (wrote 0, correct 2); R2C2 (wrote 0, correct 3); R2C3 (wrote 0, correct 1); R2C4 (wrote 0, correct 7); R2C5 (wrote 0, correct 8); R2C6 (wrote 0, correct 5); R2C8 (wrote 0, correct 4); R2C9 (wrote 0, correct 6); R3C2 (wrote 0, correct 5); R3C4 (wrote 0, correct 9); R3C7 (wrote 0, correct 1); R3C8 (wrote 0, correct 2); R3C9 (wrote 0, correct 3); R4C1 (wrote 0, correct 6); R4C4 (wrote 0, correct 3); R4C5 (wrote 0, correct 2); R4C8 (wrote 0, correct 8); R4C9 (wrote 0, correct 7); R5C1 (wrote 0, correct 5); R5C2 (wrote 0, correct 8); R5C5 (wrote 0, correct 9); R5C6 (wrote 0, correct 6); R5C7 (wrote 0, correct 2); R5C9 (wrote 0, correct 1)

## Puzzle e4s-g1-04

Classic Sudoku on a 9x9 grid. Fill every cell with a digit 1-9 so that each row, each column and each 3x3 box contains every digit exactly once.

Grid ('.' = empty):
. . 5 | . . . | . 7 8
. 6 . | . . 5 | . . .
2 . . | 8 6 . | 4 . .
---------------------
. 3 . | . 7 . | 5 2 4
. . 1 | . 5 . | . 8 .
4 . . | 9 . 8 | . . .
---------------------
7 . . | . . . | . . .
. . . | 3 8 6 | 1 . .
. . . | 7 1 . | . 9 .

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
Solver mistakes: R4C3 (wrote 6, correct 8); R4C4 (wrote 7, correct 6); R4C5 (wrote 1, correct 7); R4C6 (wrote 5, correct 1); R4C7 (wrote 2, correct 5); R4C8 (wrote 4, correct 2); R4C9 (wrote 8, correct 4); R9C5 (wrote 4, correct 1); R9C6 (wrote 1, correct 4)
