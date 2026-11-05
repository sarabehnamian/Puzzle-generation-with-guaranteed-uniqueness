# Task: write 10 new 6x6 Killer Sudoku puzzles

Rules: fill a 6x6 grid with digits 1-6 so each row, column and 2x3 box (2 rows by 3 columns) contains
each digit once. Cages are groups of orthogonally connected cells with a given sum; digits in a cage
are all different. Cages do not have to cover the whole grid. You may add a few given digits if needed.
Cells are named RrCc (row r, column c, from 1).
Each puzzle must have EXACTLY ONE solution, and it must be solvable by pure logical deduction,
step by step, without guessing or trial and error. Aim for puzzles a keen human solver would enjoy:
not trivial, but fair. You cannot run code, so check your puzzles carefully in your head.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_gen\e2_gen_killer_0.out.json with this exact structure
{"puzzles": [{"id": "g1", "cages": [{"cells": ["R1C1", "R1C2"], "sum": 7}, ...],
  "givens": ["<row 1: 6 chars, digits or '.'>", ... 6 rows],
  "solution": ["<row 1: 6 digits>", ... 6 rows]}, ...]}
Use ids g1..g10.


