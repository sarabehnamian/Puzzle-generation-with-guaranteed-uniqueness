# Task: write 10 new logic-grid (zebra) puzzles

Each puzzle has 5 houses in a row numbered 1-5 from left to right, and 4 categories (for example
colour, pet, drink, job - choose your own) with 5 values each. Every occupant has one value per
category. Write clues in natural English (same person, not the same person, house positions,
directly left/right of, next to, not next to, somewhere left/right of, exactly one house between,
either/or, and so on).
Each puzzle must have EXACTLY ONE solution, and it must be solvable by pure logical deduction,
step by step, without guessing or trial and error. Aim for puzzles a keen human solver would enjoy:
not trivial, but fair. You cannot run code, so check your puzzles carefully in your head.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_gen\e2_gen_zebra_2.out.json with this exact structure
{"puzzles": [{"id": "g1", "categories": {"<category>": ["<v1>", "<v2>", "<v3>", "<v4>", "<v5>"], ...},
  "clues": ["<clue 1>", "<clue 2>", ...],
  "solution": {"1": {"<category>": "<value>", ...}, "2": {...}, "3": {...}, "4": {...}, "5": {...}}}, ...]}
Use ids g1..g10. Value names must be unique across categories.


