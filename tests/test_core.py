import random

import pytest

from src.csp import CNF, CSP, Constraint, count_solutions, is_unique
from src.dsl import ZebraSpace, eval_concrete
from src.families import get
from src.generate import generate
from src.grading import grade, explanation_sizes, redundancy
from src.analyze import analyze

# ---------------------------------------------------------------- zebra
EINSTEIN = {
    "family": "zebra", "n": 5,
    "cats": {
        "color": ["red", "green", "white", "yellow", "blue"],
        "nationality": ["Brit", "Swede", "Dane", "Norwegian", "German"],
        "drink": ["tea", "coffee", "milk", "beer", "water"],
        "smoke": ["pallmall", "dunhill", "blends", "bluemaster", "prince"],
        "pet": ["dogs", "birds", "cats", "horse", "fish"],
    },
    "clues": [{"expr": e} for e in [
        'pos("brit") == pos("red")',
        'pos("swede") == pos("dogs")',
        'pos("dane") == pos("tea")',
        'pos("green") + 1 == pos("white")',
        'pos("green") == pos("coffee")',
        'pos("pallmall") == pos("birds")',
        'pos("yellow") == pos("dunhill")',
        'pos("milk") == 3',
        'pos("norwegian") == 1',
        'Abs(pos("blends") - pos("cats")) == 1',
        'Abs(pos("horse") - pos("dunhill")) == 1',
        'pos("bluemaster") == pos("beer")',
        'pos("german") == pos("prince")',
        'Abs(pos("norwegian") - pos("blue")) == 1',
        'Abs(pos("blends") - pos("water")) == 1',
    ]],
}
EINSTEIN_SOL = {"yellow": 1, "blue": 2, "red": 3, "green": 4, "white": 5,
                "norwegian": 1, "dane": 2, "brit": 3, "german": 4, "swede": 5,
                "water": 1, "tea": 2, "milk": 3, "coffee": 4, "beer": 5,
                "dunhill": 1, "blends": 2, "pallmall": 3, "prince": 4, "bluemaster": 5,
                "cats": 1, "horse": 2, "birds": 3, "fish": 4, "dogs": 5}


def test_einstein_unique_and_correct():
    fam = get("zebra")
    csp, _ = fam.build_csp(EINSTEIN)
    cnf = CNF(csp)
    sols = count_solutions(cnf, limit=3)
    assert len(sols) == 1
    got = dict(zip(csp.names, sols[0]))
    assert got == EINSTEIN_SOL
    g = grade(cnf)
    assert 1 <= g.level <= 5


def test_einstein_z3_matches_cnf():
    sp = ZebraSpace(5, EINSTEIN["cats"])
    f = sp.formula([c["expr"] for c in EINSTEIN["clues"]])
    sols = sp.solutions(f, limit=3)
    assert len(sols) == 1 and sols[0] == EINSTEIN_SOL


def test_dsl_equivalence():
    sp = ZebraSpace(5, EINSTEIN["cats"])
    left = sp.formula(['pos("green") + 1 == pos("white")'])
    left2 = sp.formula(['pos("white") - pos("green") == 1'])
    flipped = sp.formula(['pos("white") + 1 == pos("green")'])
    nxt = sp.formula(['Or(pos("white") - pos("green") == 1, pos("green") - pos("white") == 1)'])
    nxt2 = sp.formula(['Abs(pos("green") - pos("white")) == 1'])
    assert sp.equivalent(left, left2) is True
    assert sp.equivalent(left, flipped) is False
    assert sp.equivalent(nxt, nxt2) is True
    assert sp.equivalent(left, nxt) is False
    assert eval_concrete('Abs(pos("a") - pos("b")) == 1', {"a": 2, "b": 3})


def test_dsl_rejects_unknown_and_unsafe():
    from src.dsl import DSLError
    with pytest.raises(DSLError):
        eval_concrete('pos("zzz") == 1', {"a": 1})
    with pytest.raises(DSLError):
        eval_concrete('__import__("os")', {"a": 1})


# ---------------------------------------------------------------- sudoku
WIKI = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
        "7...2...6", ".6....28.", "...419..5", "....8..79"]
WIKI_SOL = ["534678912", "672195348", "198342567", "859761423", "426853791",
            "713924856", "961537284", "287419635", "345286179"]


def _sudoku_spec(rows, sol):
    clues = [{"type": "given", "cell": [r, c], "value": int(ch)}
             for r, row in enumerate(rows) for c, ch in enumerate(row) if ch != "."]
    return {"family": "sudoku", "n": 9, "box": [3, 3], "clues": clues,
            "solution": [[int(ch) for ch in row] for row in sol]}


def test_sudoku_known():
    spec = _sudoku_spec(WIKI, WIKI_SOL)
    a = analyze(spec, explain=False)
    assert a["unique"] and a["matches_intended"]
    assert a["level"] <= 2   # this textbook example falls to singles / simple elimination


def test_sudoku_nonunique():
    rows = list(WIKI)
    rows[0] = "........."
    rows[1] = "........."
    spec = _sudoku_spec(rows, WIKI_SOL)
    fam = get("sudoku")
    csp, _ = fam.build_csp(spec)
    assert not is_unique(CNF(csp))


def test_sudoku_score():
    spec = _sudoku_spec(WIKI, WIKI_SOL)
    fam = get("sudoku")
    assert fam.score(spec, {"grid": WIKI_SOL})["exact"]
    bad = list(WIKI_SOL)
    bad[0] = "534678921"
    s = fam.score(spec, {"grid": bad})
    assert not s["exact"] and s["cell_acc"] < 1


# ---------------------------------------------------------------- ladder
def _tiny(domains, preds):
    names = [f"v{i}" for i in range(len(domains))]
    csp = CSP(names, domains)
    for scope, p in preds:
        csp.add_clue(Constraint("table", tuple(scope), p))
    return CNF(csp)


def test_ladder_L1():
    # one empty cell in a 4x4 latin square with givens -> unit propagation
    csp = CSP([f"c{i}" for i in range(4)], [[1, 2, 3, 4]] * 4)
    csp.add_rule(Constraint("alldiff", (0, 1, 2, 3)))
    for i, v in enumerate([1, 2, 3]):
        csp.add_clue(Constraint("table", (i,), lambda x, _v=v: x == _v))
    assert grade(CNF(csp)).level == 1


def test_ladder_L2():
    # a, b, c in houses 1..3; a directly left of b, b directly left of c
    csp = CSP(["a", "b", "c"], [[1, 2, 3]] * 3)
    csp.add_rule(Constraint("alldiff", (0, 1, 2)))
    csp.add_clue(Constraint("table", (0, 1), lambda a, b: a + 1 == b))
    csp.add_clue(Constraint("table", (1, 2), lambda b, c: b + 1 == c))
    cnf = CNF(csp)
    assert is_unique(cnf)
    assert grade(cnf).level == 2


def test_ladder_L3():
    cnf = _tiny([[1, 2], [1, 2, 3]], [
        ((0, 1), lambda x, y: x == 2 or y == 1),
        ((0, 1), lambda x, y: x == 2 or y == 2),
        ((0, 1), lambda x, y: x == 1 or y == 3),
    ])
    assert is_unique(cnf)
    assert grade(cnf).level == 3


def test_ladder_L4():
    cnf = _tiny([[1, 2]] * 3, [
        ((0, 1, 2), lambda x, y, z: x == 2 or y == 2 or z == 1),
        ((0, 1, 2), lambda x, y, z: x == 2 or y == 2 or z == 2),
        ((0, 1, 2), lambda x, y, z: x == 2 or y == 1 or z == 1),
        ((0, 1, 2), lambda x, y, z: x == 2 or y == 1 or z == 2),
        ((0, 1, 2), lambda x, y, z: x == 1 or (y == 1 and z == 2)),
    ])
    assert is_unique(cnf)
    assert grade(cnf).level == 4


def test_ladder_L5():
    import itertools
    preds = []
    for t in itertools.product([1, 2], repeat=3):
        preds.append(((0, 1, 2, 3), lambda a, b, c, d, _t=t: a == 2 or (b, c, d) != _t))
    preds.append(((0, 1, 2, 3), lambda a, b, c, d: a == 1 or (b, c, d) == (1, 1, 1)))
    cnf = _tiny([[1, 2]] * 4, preds)
    assert is_unique(cnf)
    assert grade(cnf).level == 5


def test_ladder_monotone_on_generated():
    rng = random.Random(0)
    for fam in ["zebra", "futoshiki", "killer"]:
        for _ in range(3):
            spec = generate(fam, rng, {})
            csp, sol = get(fam).build_csp(spec)
            cnf = CNF(csp)
            g = grade(cnf)
            fr = [g.frac_after[k] for k in range(1, 6)]
            assert fr == sorted(fr)
            if g.level <= 4:
                assert fr[g.level - 1] == 1.0


def test_generated_puzzles_are_minimal_and_unique():
    rng = random.Random(3)
    for fam in ["zebra", "sudoku", "killer", "futoshiki"]:
        spec = generate(fam, rng, {})
        csp, sol = get(fam).build_csp(spec)
        cnf = CNF(csp)
        sols = count_solutions(cnf, limit=2)
        assert len(sols) == 1 and sols[0] == sol
        assert redundancy(cnf, list(range(len(csp.clues)))) == 0.0


def test_explanations_bounded():
    rng = random.Random(5)
    spec = generate("zebra", rng, {})
    csp, sol = get("zebra").build_csp(spec)
    cnf = CNF(csp)
    sizes = explanation_sizes(cnf, list(range(len(csp.clues))), sol)
    assert all(1 <= s <= len(csp.clues) for s in sizes.values())


def test_zebra_score_roundtrip():
    rng = random.Random(9)
    spec = generate("zebra", rng, {})
    ans = {}
    for c, vals in spec["cats"].items():
        for v in vals:
            ans.setdefault(str(spec["solution"][v.lower()]), {})[c] = v
    s = get("zebra").score(spec, ans)
    assert s["exact"] and s["cell_acc"] == 1.0
