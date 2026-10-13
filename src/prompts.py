"""Prompt texts for every LLM role.  Kept in one place so the paper can quote them."""

ENCODER = """# Task: encode logic-grid puzzles as solver constraints

Translate each puzzle below into constraints in a small Python DSL. A program will check your
constraints with a SAT/SMT solver, so they must say exactly what each clue says - no more, no less.

The DSL:
- pos('value') is the house number (an integer from 1 to N) of the given value. Use the value names
  exactly as they appear in the puzzle header (case does not matter).
- The basic rules (every value is in exactly one house; values of the same category are in different
  houses) are added automatically. Do not encode them.
- Encode each numbered clue as ONE Python boolean expression using pos(...), integer constants,
  == != < <= > >= + -, and the functions Abs(x), And(a, b, ...), Or(a, b, ...), Not(a), Implies(a, b).
- Do not use Python's and/or/not/in, chained comparisons such as 1 < x < 3, or abs().

Examples (from other puzzles):
- "The baker keeps the parrot."            ->  pos('baker') == pos('parrot')
- "The violinist lives in the fourth house." ->  pos('violinist') == 4
- "The person who reads poetry lives next to the person who drinks lemonade."
                                            ->  Abs(pos('poetry') - pos('lemonade')) == 1

Output: write a single JSON object to the file {OUT} with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.
"""

SOLVER_HEAD = """# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file {OUT} with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.
"""

PARAPHRASE = """# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file {OUT} with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.
"""

GEN_COMMON = """Each puzzle must have EXACTLY ONE solution, and it must be solvable by pure logical deduction,
step by step, without guessing or trial and error. Aim for puzzles a keen human solver would enjoy:
not trivial, but fair. You cannot run code, so check your puzzles carefully in your head.

Output: write a single JSON object to the file {OUT} with this exact structure
"""

GEN = {
    "zebra": """# Task: write {K} new logic-grid (zebra) puzzles

Each puzzle has 5 houses in a row numbered 1-5 from left to right, and 4 categories (for example
colour, pet, drink, job - choose your own) with 5 values each. Every occupant has one value per
category. Write clues in natural English (same person, not the same person, house positions,
directly left/right of, next to, not next to, somewhere left/right of, exactly one house between,
either/or, and so on).
""" + GEN_COMMON + """{"puzzles": [{"id": "g1", "categories": {"<category>": ["<v1>", "<v2>", "<v3>", "<v4>", "<v5>"], ...},
  "clues": ["<clue 1>", "<clue 2>", ...],
  "solution": {"1": {"<category>": "<value>", ...}, "2": {...}, "3": {...}, "4": {...}, "5": {...}}}, ...]}
Use ids g1..g{K}. Value names must be unique across categories.
""",
    "sudoku": """# Task: write {K} new classic 9x9 Sudoku puzzles

Standard rules: each row, column and 3x3 box contains the digits 1-9 exactly once.
""" + GEN_COMMON + """{"puzzles": [{"id": "g1", "grid": ["<row 1: 9 chars, digits or '.' for empty>", ... 9 rows],
  "solution": ["<row 1: 9 digits>", ... 9 rows]}, ...]}
Use ids g1..g{K}.
""",
    "killer": """# Task: write {K} new 6x6 Killer Sudoku puzzles

Rules: fill a 6x6 grid with digits 1-6 so each row, column and 2x3 box (2 rows by 3 columns) contains
each digit once. Cages are groups of orthogonally connected cells with a given sum; digits in a cage
are all different. Cages do not have to cover the whole grid. You may add a few given digits if needed.
Cells are named RrCc (row r, column c, from 1).
""" + GEN_COMMON + """{"puzzles": [{"id": "g1", "cages": [{"cells": ["R1C1", "R1C2"], "sum": 7}, ...],
  "givens": ["<row 1: 6 chars, digits or '.'>", ... 6 rows],
  "solution": ["<row 1: 6 digits>", ... 6 rows]}, ...]}
Use ids g1..g{K}.
""",
    "futoshiki": """# Task: write {K} new 5x5 Futoshiki puzzles

Rules: fill a 5x5 grid with digits 1-5 so each row and column contains each digit once; inequality
signs between orthogonally adjacent cells must hold. Cells are named RrCc (row r, column c, from 1).
""" + GEN_COMMON + """{"puzzles": [{"id": "g1", "givens": ["<row 1: 5 chars, digits or '.'>", ... 5 rows],
  "inequalities": ["R1C1 < R1C2", "R2C3 > R3C3", ...],
  "solution": ["<row 1: 5 digits>", ... 5 rows]}, ...]}
Use ids g1..g{K}.
""",
}

REPAIR = """# Task: repair logic puzzles using solver feedback

You wrote the puzzles below. A solver checked each one and found a problem, described under
"Solver feedback". Revise each puzzle so that it has exactly one solution, that solution is the one
you state, and it can be solved by logical deduction without guessing. Change as little as needed
(you may add, remove or edit clues/givens, and you may change the intended solution).

Output: write a single JSON object to the file {OUT} with this structure
{"puzzles": [<revised puzzle in exactly the same JSON format as the original, same id>, ...]}

The puzzles follow.
"""

MUTATE = """# Task: make fair logic puzzles harder for language-model solvers

Each puzzle below is a 5-house logic-grid puzzle with a known unique solution. A language-model
solver attempted it; its mistakes are listed. Propose {C} variants of each puzzle that you expect to
be HARDER for a language-model solver, while staying solvable by pure step-by-step deduction.

You edit puzzles with operations on the formal clue list:
- {"op": "remove", "clue": <clue number>}
- {"op": "add", "clue": {"type": <type>, "args": [...]}}
- {"op": "replace", "clue": <clue number>, "with": {"type": <type>, "args": [...]}}
Use 1 to 4 operations per variant. Clue types (a, b, c are value names; k is a house number):
  same(a,b)        a and b belong to the same person
  not_same(a,b)    a and b belong to different people
  at(a,k)          a is in house k            not_at(a,k)     a is not in house k
  left_of(a,b)     a is directly left of b    next_to(a,b)    a and b are neighbours
  not_next_to(a,b) a and b are not neighbours (they may share a house)
  before(a,b)      a is somewhere left of b   gap2(a,b)       exactly one house between a and b
  end(a)           a is in house 1 or house 5
  or(a,b,c)        a is with b or with c (b and c from the same category)
Every clue you add must be TRUE of the stated solution. A program will apply your edits, add a clue
if the result is no longer unique, and reject variants that need guessing, so focus on what makes the
deduction harder to follow (for example: fewer direct position clues, longer chains of inference,
negative and relative clues, information spread across many clues).

Output: write a single JSON object to the file {OUT} with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with {C} variants per puzzle.

The puzzles follow.
"""

GENRE = """# Task: invent new logic-puzzle genres

Invent {K} NEW pencil-and-paper logic puzzle genres on small grids. They should not be standard
genres (not Sudoku, Killer, Futoshiki, KenKen, Kakuro, Nonogram, Skyscrapers, ...); invent new
rules or new kinds of clues. A program will compile each genre, generate instances, check that
unique-solution instances exist, and measure how deep the required deduction is.

Write each genre as Python source using ONLY this API (no imports):

    GRID = (R, C, D)          # rows, columns, digits 1..D   (R, C <= 6, D <= 6)

    def rules(g):             # global rules every solution must satisfy
        # g.R, g.C, g.D are the sizes; cells are (row, col) pairs, 0-based
        g.alldiff(cells)                      # digits in these cells all different
        g.table(cells, check)                 # check(*digits) -> bool, e.g. lambda a, b: a + b != 7

    def clues(sol):           # sol[r][c] = digit of a solution grid
        # return a list of candidate clues that are TRUE of sol; the program picks a
        # minimal subset that makes the solution unique
        return [{"cells": [(r, c), ...], "check": "lambda a, b: a < b",
                 "text": "R1C1 < R1C2"}, ...]

"check" in clues is a STRING holding a Python lambda over the digits of the listed cells (in order);
it may use + - * // % == != < <= > >= and/or/not, abs, min, max, sum, len, set, sorted, all, any.
Keep clue scopes small (at most 4 cells). Make sure solutions to rules(g) exist.

Output: write a single JSON object to the file {OUT} with this structure
{"genres": [{"name": "<name>", "rules_text": "<rules a human solver would read, 2-5 sentences>",
             "clue_text": "<how clues are shown to the solver>", "code": "<python source>"}, ...]}
"""

MUTATE_SUDOKU = """# Task: make fair Sudoku puzzles harder for language-model solvers

Each 9x9 Sudoku below has a known unique solution. A language-model solver attempted it; its mistakes
are listed. Propose {C} variants of each puzzle that you expect to be HARDER for a language-model
solver while staying solvable by step-by-step logic (no guessing).

You edit puzzles with operations on the given digits (the digit placed is always the solution digit):
- {"op": "remove", "cell": "RrCc"}            remove a given
- {"op": "add", "cell": "RrCc"}               add a given
- {"op": "move", "from": "RrCc", "to": "RrCc"}  move a given to another cell
Use 1 to 6 operations per variant. A program will add givens back if the result has more than one
solution and will reject variants that need guessing, so focus on what makes the logic harder to
follow (for example: fewer givens, givens spread so that no row/column/box is nearly complete,
removing givens that make singles easy).

Output: write a single JSON object to the file {OUT} with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with {C} variants per puzzle.

The puzzles follow.
"""
