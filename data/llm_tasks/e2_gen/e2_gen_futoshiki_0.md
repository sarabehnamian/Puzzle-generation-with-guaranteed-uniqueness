# Task: write 10 new 5x5 Futoshiki puzzles

Rules: fill a 5x5 grid with digits 1-5 so each row and column contains each digit once; inequality
signs between orthogonally adjacent cells must hold. Cells are named RrCc (row r, column c, from 1).
Each puzzle must have EXACTLY ONE solution, and it must be solvable by pure logical deduction,
step by step, without guessing or trial and error. Aim for puzzles a keen human solver would enjoy:
not trivial, but fair. You cannot run code, so check your puzzles carefully in your head.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_gen/e2_gen_futoshiki_0.out.json with this exact structure
{"puzzles": [{"id": "g1", "givens": ["<row 1: 5 chars, digits or '.'>", ... 5 rows],
  "inequalities": ["R1C1 < R1C2", "R2C3 > R3C3", ...],
  "solution": ["<row 1: 5 digits>", ... 5 rows]}, ...]}
Use ids g1..g10.


