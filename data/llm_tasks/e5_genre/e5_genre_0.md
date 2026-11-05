# Task: invent new logic-puzzle genres

Invent 6 NEW pencil-and-paper logic puzzle genres on small grids. They should not be standard
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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e5_genre\e5_genre_0.out.json with this structure
{"genres": [{"name": "<name>", "rules_text": "<rules a human solver would read, 2-5 sentences>",
             "clue_text": "<how clues are shown to the solver>", "code": "<python source>"}, ...]}


