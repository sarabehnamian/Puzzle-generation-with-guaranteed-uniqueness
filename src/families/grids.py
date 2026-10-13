"""Grid families: classic Sudoku, Killer Sudoku and Futoshiki."""
from __future__ import annotations

import random

from ..csp import CSP, Constraint


def cell_name(r, c):
    return f"R{r + 1}C{c + 1}"


def latin_rules(csp, n, box=None):
    for r in range(n):
        csp.add_rule(Constraint("alldiff", tuple(r * n + c for c in range(n)), meta={"row": r}))
    for c in range(n):
        csp.add_rule(Constraint("alldiff", tuple(r * n + c for r in range(n)), meta={"col": c}))
    if box:
        br, bc = box
        for r0 in range(0, n, br):
            for c0 in range(0, n, bc):
                csp.add_rule(Constraint("alldiff", tuple((r0 + i) * n + c0 + j
                                                         for i in range(br) for j in range(bc)),
                                        meta={"box": [r0, c0]}))


def base_csp(n):
    return CSP([cell_name(r, c) for r in range(n) for c in range(n)],
               [list(range(1, n + 1))] * (n * n))


def given_constraint(clue, n):
    r, c = clue["cell"]
    v = clue["value"]
    return Constraint("table", (r * n + c,), lambda x, _v=v: x == _v, meta={"type": "given"})


def grid_text(n, givens, box=None):
    g = [["."] * n for _ in range(n)]
    for cl in givens:
        r, c = cl["cell"]
        g[r][c] = str(cl["value"])
    lines = []
    for r in range(n):
        row = ""
        for c in range(n):
            row += g[r][c]
            if box and (c + 1) % box[1] == 0 and c + 1 < n:
                row += " |"
            row += " " if c + 1 < n else ""
        lines.append(row.rstrip())
        if box and (r + 1) % box[0] == 0 and r + 1 < n:
            lines.append("-" * len(lines[-1]))
    return "\n".join(lines)


def random_box_solution(rng: random.Random, n, box):
    br, bc = box
    base = [[(bc * (r % br) + r // br + c) % n for c in range(n)] for r in range(n)]
    digits = list(range(1, n + 1))
    rng.shuffle(digits)
    # permute rows within bands and bands; columns within stacks and stacks
    bands = list(range(n // br))
    rng.shuffle(bands)
    rows = [b * br + i for b in bands for i in rng.sample(range(br), br)]
    stacks = list(range(n // bc))
    rng.shuffle(stacks)
    cols = [s * bc + j for s in stacks for j in rng.sample(range(bc), bc)]
    grid = [[digits[base[r][c]] for c in cols] for r in rows]
    if br == bc and rng.random() < 0.5:
        grid = [list(x) for x in zip(*grid)]
    return grid


def random_latin(rng: random.Random, n):
    grid = [[0] * n for _ in range(n)]

    def fill(k):
        if k == n * n:
            return True
        r, c = divmod(k, n)
        vals = list(range(1, n + 1))
        rng.shuffle(vals)
        for v in vals:
            if v in grid[r] or any(grid[i][c] == v for i in range(r)):
                continue
            grid[r][c] = v
            if fill(k + 1):
                return True
            grid[r][c] = 0
        return False

    fill(0)
    return grid


def flat(grid):
    return [v for row in grid for v in row]


def parse_grid_answer(n, ans):
    rows = None
    if isinstance(ans, dict):
        rows = ans.get("grid")
    elif isinstance(ans, list):
        rows = ans
    if not isinstance(rows, list):
        return None
    out = []
    for row in rows:
        if isinstance(row, str):
            digits = [int(ch) for ch in row if ch.isdigit()]
        elif isinstance(row, list):
            digits = []
            for x in row:
                try:
                    digits.append(int(x))
                except (TypeError, ValueError):
                    digits.append(0)
        else:
            digits = []
        out.append((digits + [0] * n)[:n])
    out = (out + [[0] * n] * n)[:n]
    return out


def score_grid(spec, ans):
    n = spec["n"]
    sol = spec["solution"]
    got = parse_grid_answer(n, ans)
    given = {tuple(cl["cell"]) for cl in spec["clues"] if cl["type"] == "given"}
    cells = [(r, c) for r in range(n) for c in range(n) if (r, c) not in given]
    if got is None:
        return {"cell_acc": 0.0, "exact": False}
    corr = sum(1 for r, c in cells if got[r][c] == sol[r][c])
    allok = all(got[r][c] == sol[r][c] for r in range(n) for c in range(n))
    return {"cell_acc": corr / max(1, len(cells)), "exact": allok}


def givens_first_order(rng, pool):
    """Try removing given digits first (shuffled), then the other clues (shuffled)."""
    giv = [i for i, c in enumerate(pool) if c["type"] == "given"]
    oth = [i for i, c in enumerate(pool) if c["type"] != "given"]
    rng.shuffle(giv)
    rng.shuffle(oth)
    return giv + oth


GRID_ANSWER = '{"grid": ["<row 1 digits>", "<row 2 digits>", ...]} -- each row as a string of digits, no separators.'


# ==========================================================================
class Sudoku:
    FAMILY = "sudoku"
    ANSWER_FORMAT = GRID_ANSWER

    @staticmethod
    def rules_text(spec):
        n, (br, bc) = spec["n"], spec["box"]
        return (f"Classic Sudoku on a {n}x{n} grid. Fill every cell with a digit 1-{n} so that each row, "
                f"each column and each {br}x{bc} box contains every digit exactly once.")

    @staticmethod
    def build_csp(spec):
        n = spec["n"]
        csp = base_csp(n)
        latin_rules(csp, n, spec["box"])
        for cl in spec["clues"]:
            csp.add_clue(given_constraint(cl, n))
        return csp, flat(spec["solution"]) if spec.get("solution") else None

    @staticmethod
    def random_spec(rng, n=9, box=(3, 3)):
        sol = random_box_solution(rng, n, box)
        return {"family": "sudoku", "n": n, "box": list(box), "solution": sol}

    @staticmethod
    def clue_pool(rng, spec):
        n = spec["n"]
        return [{"type": "given", "cell": [r, c], "value": spec["solution"][r][c]}
                for r in range(n) for c in range(n)]

    @staticmethod
    def removal_order(rng, pool):
        idx = list(range(len(pool)))
        rng.shuffle(idx)
        return idx

    @staticmethod
    def render(spec):
        return Sudoku.rules_text(spec) + "\n\nGrid ('.' = empty):\n" + grid_text(spec["n"], spec["clues"], spec["box"])

    score = staticmethod(score_grid)


# ==========================================================================
def cage_constraint(clue, n):
    cells = tuple(r * n + c for r, c in clue["cells"])
    s = clue["sum"]
    return Constraint("table", cells,
                      lambda *v, _s=s: sum(v) == _s and len(set(v)) == len(v),
                      meta={"type": "cage"})


class Killer:
    FAMILY = "killer"
    ANSWER_FORMAT = GRID_ANSWER

    @staticmethod
    def rules_text(spec):
        n, (br, bc) = spec["n"], spec["box"]
        return (f"Killer Sudoku on a {n}x{n} grid. Fill every cell with a digit 1-{n} so that each row, "
                f"each column and each {br}x{bc} box contains every digit exactly once. Each cage lists "
                f"its cells and their sum; digits inside a cage are all different.")

    @staticmethod
    def build_csp(spec):
        n = spec["n"]
        csp = base_csp(n)
        latin_rules(csp, n, spec["box"])
        for cl in spec["clues"]:
            csp.add_clue(cage_constraint(cl, n) if cl["type"] == "cage" else given_constraint(cl, n))
        return csp, flat(spec["solution"]) if spec.get("solution") else None

    @staticmethod
    def random_spec(rng, n=6, box=(2, 3)):
        sol = random_box_solution(rng, n, box)
        return {"family": "killer", "n": n, "box": list(box), "solution": sol}

    @staticmethod
    def clue_pool(rng, spec):
        n = spec["n"]
        sol = spec["solution"]
        free = {(r, c) for r in range(n) for c in range(n)}
        cages = []
        while free:
            start = rng.choice(sorted(free))
            target = rng.choices([1, 2, 3, 4], [0.05, 0.4, 0.35, 0.2])[0]
            cage = [start]
            free.discard(start)
            while len(cage) < target:
                nb = [(r + dr, c + dc) for r, c in cage for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0))
                      if (r + dr, c + dc) in free and sol[r + dr][c + dc] not in [sol[a][b] for a, b in cage]]
                if not nb:
                    break
                nxt = rng.choice(sorted(set(nb)))
                cage.append(nxt)
                free.discard(nxt)
            cages.append({"type": "cage", "cells": [list(x) for x in sorted(cage)],
                          "sum": sum(sol[r][c] for r, c in cage)})
        givens = [{"type": "given", "cell": [r, c], "value": sol[r][c]} for r in range(n) for c in range(n)]
        return cages + givens

    removal_order = staticmethod(lambda rng, pool: givens_first_order(rng, pool))

    @staticmethod
    def render(spec):
        n = spec["n"]
        cages = [c for c in spec["clues"] if c["type"] == "cage"]
        givens = [c for c in spec["clues"] if c["type"] == "given"]
        lines = [Killer.rules_text(spec), ""]
        if givens:
            lines += ["Given digits ('.' = empty):", grid_text(n, givens, spec["box"]), ""]
        else:
            lines += ["There are no given digits.", ""]
        lines.append("Cages (cells not listed in any cage have no sum constraint):")
        for i, c in enumerate(cages):
            cells = ", ".join(cell_name(r, cc) for r, cc in c["cells"])
            lines.append(f"- cage {i + 1}: {cells} -> sum {c['sum']}")
        return "\n".join(lines)

    score = staticmethod(score_grid)


# ==========================================================================
def lt_constraint(clue, n):
    a = clue["a"][0] * n + clue["a"][1]
    b = clue["b"][0] * n + clue["b"][1]
    return Constraint("table", (a, b), lambda x, y: x < y, meta={"type": "lt"})


class Futoshiki:
    FAMILY = "futoshiki"
    ANSWER_FORMAT = GRID_ANSWER

    @staticmethod
    def rules_text(spec):
        n = spec["n"]
        return (f"Futoshiki on a {n}x{n} grid. Fill every cell with a digit 1-{n} so that each row and "
                f"each column contains every digit exactly once, and every listed inequality between "
                f"cells holds. Cells are named RrCc (row r, column c).")

    @staticmethod
    def build_csp(spec):
        n = spec["n"]
        csp = base_csp(n)
        latin_rules(csp, n, None)
        for cl in spec["clues"]:
            csp.add_clue(lt_constraint(cl, n) if cl["type"] == "lt" else given_constraint(cl, n))
        return csp, flat(spec["solution"]) if spec.get("solution") else None

    @staticmethod
    def random_spec(rng, n=5):
        return {"family": "futoshiki", "n": n, "solution": random_latin(rng, n)}

    @staticmethod
    def clue_pool(rng, spec):
        n = spec["n"]
        sol = spec["solution"]
        out = []
        for r in range(n):
            for c in range(n):
                for dr, dc in ((0, 1), (1, 0)):
                    r2, c2 = r + dr, c + dc
                    if r2 < n and c2 < n:
                        a, b = [r, c], [r2, c2]
                        if sol[r][c] > sol[r2][c2]:
                            a, b = b, a
                        out.append({"type": "lt", "a": a, "b": b})
        out += [{"type": "given", "cell": [r, c], "value": sol[r][c]} for r in range(n) for c in range(n)]
        return out

    removal_order = staticmethod(lambda rng, pool: givens_first_order(rng, pool))

    @staticmethod
    def render(spec):
        n = spec["n"]
        givens = [c for c in spec["clues"] if c["type"] == "given"]
        lts = [c for c in spec["clues"] if c["type"] == "lt"]
        lines = [Futoshiki.rules_text(spec), ""]
        if givens:
            lines += ["Given digits ('.' = empty):", grid_text(n, givens), ""]
        else:
            lines += ["There are no given digits.", ""]
        lines.append("Inequalities:")
        for c in lts:
            lines.append(f"- {cell_name(*c['a'])} < {cell_name(*c['b'])}")
        return "\n".join(lines)

    score = staticmethod(score_grid)
