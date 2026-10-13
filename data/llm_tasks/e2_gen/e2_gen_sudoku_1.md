# Task: write 10 new classic 9x9 Sudoku puzzles

Standard rules: each row, column and 3x3 box contains the digits 1-9 exactly once.
Each puzzle must have EXACTLY ONE solution, and it must be solvable by pure logical deduction,
step by step, without guessing or trial and error. Aim for puzzles a keen human solver would enjoy:
not trivial, but fair. You cannot run code, so check your puzzles carefully in your head.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_gen/e2_gen_sudoku_1.out.json with this exact structure
{"puzzles": [{"id": "g1", "grid": ["<row 1: 9 chars, digits or '.' for empty>", ... 9 rows],
  "solution": ["<row 1: 9 digits>", ... 9 rows]}, ...]}
Use ids g1..g10.


