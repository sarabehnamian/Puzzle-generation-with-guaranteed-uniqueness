"""Einstein/zebra-style grid logic puzzles with natural-language clues.

Every clue carries a canonical DSL expression (see ``src/dsl.py``); the CSP
constraint of a clue is derived from that expression, so the expression is
the single source of truth for the ground-truth encoding.
"""
from __future__ import annotations

import itertools
import random

from ..csp import CSP, Constraint
from ..dsl import eval_concrete, names_in, norm

FAMILY = "zebra"

CATEGORIES = {
    "color": {
        "values": ["red", "green", "blue", "yellow", "white", "purple"],
        "np": ["the person in the {v} house", "the occupant of the {v} house", "whoever lives in the {v} house"],
        "vp": "lives in the {v} house", "neg": "does not live in the {v} house",
        "base": "live in the {v} house",
    },
    "nationality": {
        "values": ["Brit", "Swede", "Dane", "Norwegian", "German", "Spaniard"],
        "np": ["the {v}"],
        "vp": "is the {v}", "neg": "is not the {v}",
        "base": "be the {v}",
    },
    "pet": {
        "values": ["dog", "cat", "bird", "fish", "horse", "rabbit"],
        "np": ["the person who keeps the {v}", "the {v} owner", "the owner of the {v}"],
        "vp": "keeps the {v}", "neg": "does not keep the {v}",
        "base": "keep the {v}",
    },
    "drink": {
        "values": ["tea", "coffee", "milk", "water", "juice", "cocoa"],
        "np": ["the person who drinks {v}", "the {v} drinker"],
        "vp": "drinks {v}", "neg": "does not drink {v}",
        "base": "drink {v}",
    },
    "hobby": {
        "values": ["chess", "tennis", "painting", "hiking", "cooking", "golf"],
        "np": ["the person who enjoys {v}", "the {v} enthusiast"],
        "vp": "enjoys {v}", "neg": "does not enjoy {v}",
        "base": "enjoy {v}",
    },
    "job": {
        "values": ["teacher", "doctor", "baker", "pilot", "farmer", "lawyer"],
        "np": ["the {v}"],
        "vp": "works as the {v}", "neg": "is not the {v}",
        "base": "work as the {v}",
    },
}

ORD = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth"}

TYPE_WEIGHTS = {
    "same": 3.0, "not_same": 1.5, "at": 1.2, "not_at": 1.0, "left_of": 1.5,
    "next_to": 1.5, "not_next_to": 1.0, "before": 1.2, "gap2": 1.0, "end": 0.5, "or": 1.0,
}
# extra compound clue types used only in the "hard" text style
HARD_EXTRA_WEIGHTS = {"neither": 1.0, "between": 1.0}


def _cat_of(spec):
    return {norm(v): c for c, vals in spec["cats"].items() for v in vals}


def _orig(spec):
    return {norm(v): v for vals in spec["cats"].values() for v in vals}


def expr_for(ctype, args, n):
    q = [f'pos("{norm(a)}")' if isinstance(a, str) else a for a in args]
    if ctype == "same":
        return f"{q[0]} == {q[1]}"
    if ctype == "not_same":
        return f"{q[0]} != {q[1]}"
    if ctype == "at":
        return f"{q[0]} == {args[1]}"
    if ctype == "not_at":
        return f"{q[0]} != {args[1]}"
    if ctype == "left_of":
        return f"{q[0]} + 1 == {q[1]}"
    if ctype == "next_to":
        return f"Abs({q[0]} - {q[1]}) == 1"
    if ctype == "not_next_to":
        return f"Abs({q[0]} - {q[1]}) != 1"
    if ctype == "before":
        return f"{q[0]} < {q[1]}"
    if ctype == "gap2":
        return f"Abs({q[0]} - {q[1]}) == 2"
    if ctype == "end":
        return f"Or({q[0]} == 1, {q[0]} == {n})"
    if ctype == "or":
        return f"Or({q[0]} == {q[1]}, {q[0]} == {q[2]})"
    if ctype == "neither":
        return f"And({q[0]} != {q[2]}, {q[1]} != {q[2]})"
    if ctype == "between":
        return f"Or(And({q[0]} < {q[2]}, {q[2]} < {q[1]}), And({q[1]} < {q[2]}, {q[2]} < {q[0]}))"
    raise ValueError(ctype)


# --------------------------------------------------------------------------
# natural-language rendering
# --------------------------------------------------------------------------

def _np(spec, v, rng):
    c = _cat_of(spec)[norm(v)]
    return rng.choice(CATEGORIES[c]["np"]).format(v=_orig(spec)[norm(v)])


def _vp(spec, v, neg=False):
    c = _cat_of(spec)[norm(v)]
    return CATEGORIES[c]["neg" if neg else "vp"].format(v=_orig(spec)[norm(v)])


def _cap(s):
    return s[0].upper() + s[1:]


def render_clue(spec, clue, rng):
    t, a = clue["type"], clue["args"]
    n = spec["n"]
    if t == "same":
        x, y = (a[0], a[1]) if rng.random() < 0.5 else (a[1], a[0])
        return _cap(f"{_np(spec, x, rng)} {_vp(spec, y)}.")
    if t == "not_same":
        x, y = (a[0], a[1]) if rng.random() < 0.5 else (a[1], a[0])
        opts = [f"{_np(spec, x, rng)} {_vp(spec, y, neg=True)}.",
                f"{_np(spec, x, rng)} and {_np(spec, y, rng)} are different people."]
        return _cap(rng.choice(opts))
    if t == "at":
        k = a[1]
        opts = [f"{_np(spec, a[0], rng)} lives in house {k}.",
                f"{_np(spec, a[0], rng)} lives in the {ORD[k]} house."]
        if k == 1:
            opts.append(f"{_np(spec, a[0], rng)} lives in the leftmost house.")
        if k == n:
            opts.append(f"{_np(spec, a[0], rng)} lives in the last house.")
        if n % 2 == 1 and k == (n + 1) // 2:
            opts.append(f"{_np(spec, a[0], rng)} lives in the middle house.")
        return _cap(rng.choice(opts))
    if t == "not_at":
        k = a[1]
        opts = [f"{_np(spec, a[0], rng)} does not live in house {k}.",
                f"{_np(spec, a[0], rng)} does not live in the {ORD[k]} house."]
        return _cap(rng.choice(opts))
    if t == "left_of":
        opts = [f"{_np(spec, a[0], rng)} lives directly to the left of {_np(spec, a[1], rng)}.",
                f"{_np(spec, a[1], rng)} lives immediately to the right of {_np(spec, a[0], rng)}.",
                f"{_np(spec, a[0], rng)} lives in the house just left of the one where {_np(spec, a[1], rng)} lives."]
        return _cap(rng.choice(opts))
    if t == "next_to":
        opts = [f"{_np(spec, a[0], rng)} lives next to {_np(spec, a[1], rng)}.",
                f"{_np(spec, a[0], rng)} and {_np(spec, a[1], rng)} are neighbours.",
                f"{_np(spec, a[0], rng)} and {_np(spec, a[1], rng)} live in adjacent houses."]
        return _cap(rng.choice(opts))
    if t == "not_next_to":
        opts = [f"{_np(spec, a[0], rng)} does not live next to {_np(spec, a[1], rng)}.",
                f"{_np(spec, a[0], rng)} and {_np(spec, a[1], rng)} are not neighbours."]
        return _cap(rng.choice(opts))
    if t == "before":
        opts = [f"{_np(spec, a[0], rng)} lives somewhere to the left of {_np(spec, a[1], rng)}.",
                f"{_np(spec, a[1], rng)} lives somewhere to the right of {_np(spec, a[0], rng)}.",
                f"{_np(spec, a[0], rng)} lives in a lower-numbered house than {_np(spec, a[1], rng)}."]
        return _cap(rng.choice(opts))
    if t == "gap2":
        opts = [f"There is exactly one house between {_np(spec, a[0], rng)} and {_np(spec, a[1], rng)}.",
                f"{_np(spec, a[0], rng)} and {_np(spec, a[1], rng)} live two houses apart."]
        return _cap(rng.choice(opts))
    if t == "end":
        opts = [f"{_np(spec, a[0], rng)} lives in one of the two end houses.",
                f"{_np(spec, a[0], rng)} lives at one end of the row."]
        return _cap(rng.choice(opts))
    if t == "or":
        return _cap(f"{_np(spec, a[0], rng)} either {_vp(spec, a[1])} or {_vp(spec, a[2])}.")
    raise ValueError(t)


def _base(spec, v):
    c = _cat_of(spec)[norm(v)]
    return CATEGORIES[c]["base"].format(v=_orig(spec)[norm(v)])


def _from_right(n, k):
    j = n + 1 - k
    return "rightmost" if j == 1 else f"{ORD[j]} house from the right"


def render_clue_hard(spec, clue, rng):
    """Indirect phrasings: neighbour descriptions, counting from the right,
    negated orderings, conditionals and compound clues."""
    t, a = clue["type"], clue["args"]
    n = spec["n"]
    cat = _cat_of(spec)
    if t == "same":
        return _cap(f"{_np(spec, a[0], rng)} and {_np(spec, a[1], rng)} are one and the same person.")
    if t == "not_same":
        return _cap(f"{_np(spec, a[0], rng)} is not the same person as {_np(spec, a[1], rng)}.")
    if t in ("at", "not_at"):
        k = a[1]
        fr = _from_right(n, k)
        place = "the rightmost house" if fr == "rightmost" else f"the {fr}"
        if t == "at":
            opts = [f"{_np(spec, a[0], rng)} lives in {place}.",
                    f"Exactly {k - 1} house{'s' if k - 1 != 1 else ''} lie{'' if k - 1 != 1 else 's'} to the left of the home of {_np(spec, a[0], rng)}."]
            return _cap(rng.choice(opts))
        return _cap(f"{_np(spec, a[0], rng)} does not live in {place}.")
    if t == "left_of":
        opts = [f"The left-hand neighbour of {_np(spec, a[1], rng)} {_vp(spec, a[0])}.",
                f"The right-hand neighbour of {_np(spec, a[0], rng)} {_vp(spec, a[1])}."]
        return _cap(rng.choice(opts))
    if t == "next_to":
        x, y = (a[0], a[1]) if rng.random() < 0.5 else (a[1], a[0])
        return _cap(f"One of the neighbours of {_np(spec, x, rng)} {_vp(spec, y)}.")
    if t == "not_next_to":
        x, y = (a[0], a[1]) if rng.random() < 0.5 else (a[1], a[0])
        opts = [f"None of the neighbours of {_np(spec, x, rng)} {_vp(spec, y)}.",
                f"At least one house separates {_np(spec, x, rng)} from {_np(spec, y, rng)}."]
        return _cap(rng.choice(opts))
    if t == "before":
        if cat[norm(a[0])] == cat[norm(a[1])]:
            return _cap(f"{_np(spec, a[0], rng)} does not live to the right of {_np(spec, a[1], rng)}.")
        return _cap(f"{_np(spec, a[1], rng)} lives further to the right than {_np(spec, a[0], rng)}.")
    if t == "gap2":
        opts = [f"{_np(spec, a[0], rng)} lives two doors away from {_np(spec, a[1], rng)}.",
                f"Exactly one house separates {_np(spec, a[0], rng)} from {_np(spec, a[1], rng)}."]
        return _cap(rng.choice(opts))
    if t == "end":
        return _cap(f"{_np(spec, a[0], rng)} has only one neighbour.")
    if t == "or":
        return _cap(f"If {_np(spec, a[0], rng)} {_vp(spec, a[1], neg=True)}, then that person {_vp(spec, a[2])}.")
    if t == "neither":
        return _cap(f"Neither {_np(spec, a[0], rng)} nor {_np(spec, a[1], rng)} {_vp(spec, a[2])}.")
    if t == "between":
        return _cap(f"{_np(spec, a[2], rng)} lives somewhere between {_np(spec, a[0], rng)} and {_np(spec, a[1], rng)}.")
    raise ValueError(t)


def header(spec):
    n = spec["n"]
    lines = [f"There are {n} houses in a row, numbered 1 to {n} from left to right. "
             f"Each house has one occupant. Every occupant has exactly one value from each "
             f"category below, and no two occupants share a value within a category."]
    for c, vals in spec["cats"].items():
        lines.append(f"- {c}: " + ", ".join(vals))
    return "\n".join(lines)


def render(spec):
    out = [header(spec), "", "Clues:"]
    for i, c in enumerate(spec["clues"], 1):
        out.append(f"{i}. {c['text']}")
    return "\n".join(out)


ANSWER_FORMAT = ('{"1": {"<category>": "<value>", ...}, "2": {...}, ...} '
                 '-- one entry per house number, giving the value of every category.')

RULES_TEXT = ("Grid logic puzzle. Deduce which value of each category belongs to each house. "
              "Every value is used exactly once.")


# --------------------------------------------------------------------------
# CSP
# --------------------------------------------------------------------------

def clue_constraint(spec, clue, index):
    expr = clue["expr"]
    scope_names = names_in(expr)
    scope = tuple(index[nm] for nm in scope_names)

    def pred(*labs, _e=expr, _s=scope_names):
        return eval_concrete(_e, dict(zip(_s, labs)))

    return Constraint("table", scope, pred, meta={"type": clue.get("type"), "expr": expr})


def build_csp(spec):
    n = spec["n"]
    names = [norm(v) for vals in spec["cats"].values() for v in vals]
    csp = CSP(names, [list(range(1, n + 1))] * len(names))
    for c, vals in spec["cats"].items():
        csp.add_rule(Constraint("alldiff", tuple(csp.index[norm(v)] for v in vals), meta={"cat": c}))
    for clue in spec["clues"]:
        csp.add_clue(clue_constraint(spec, clue, csp.index))
    sol = None
    if spec.get("solution"):
        sol = [spec["solution"][nm] for nm in names]
    return csp, sol


def random_solution(rng: random.Random, n: int, k: int):
    cats = rng.sample(list(CATEGORIES), k)
    out_cats, pos = {}, {}
    for c in cats:
        vals = rng.sample(CATEGORIES[c]["values"], n)
        out_cats[c] = vals
        perm = list(range(1, n + 1))
        rng.shuffle(perm)
        for v, p in zip(vals, perm):
            pos[norm(v)] = p
    return out_cats, pos


def _true_clues(spec):
    n = spec["n"]
    pos = spec["solution"]
    cat = _cat_of(spec)
    vals = list(pos)
    out = {t: [] for t in list(TYPE_WEIGHTS) + list(HARD_EXTRA_WEIGHTS)}
    for a, b in itertools.permutations(vals, 2):
        diffcat = cat[a] != cat[b]
        pa, pb = pos[a], pos[b]
        if diffcat and a < b:
            (out["same"] if pa == pb else out["not_same"]).append((a, b))
        if pa + 1 == pb:
            out["left_of"].append((a, b))
        if a < b and abs(pa - pb) == 1:
            out["next_to"].append((a, b))
        if a < b and abs(pa - pb) > 1:
            out["not_next_to"].append((a, b))
        if pa < pb and pb - pa >= 2:
            out["before"].append((a, b))
        if a < b and abs(pa - pb) == 2:
            out["gap2"].append((a, b))
    for a in vals:
        out["at"].append((a, pos[a]))
        for k in range(1, n + 1):
            if k != pos[a]:
                out["not_at"].append((a, k))
        if pos[a] in (1, n):
            out["end"].append((a,))
    for a, b, c in itertools.permutations(vals, 3):
        pa, pb, pc = pos[a], pos[b], pos[c]
        if a < b and cat[c] not in (cat[a], cat[b]) and pa != pc and pb != pc and pa != pb:
            out["neither"].append((a, b, c))
        if a < b and min(pa, pb) < pc < max(pa, pb):
            out["between"].append((a, b, c))
    for a in vals:
        for c2 in spec["cats"]:
            if c2 == cat[a]:
                continue
            others = [norm(v) for v in spec["cats"][c2]]
            match = [v for v in others if pos[v] == pos[a]][0]
            for wrong in others:
                if wrong != match:
                    out["or"].append((a, match, wrong) if wrong > match else (a, wrong, match))
    return out


def clue_pool(rng: random.Random, spec, size=260, hard=False):
    true = _true_clues(spec)
    for t in true:
        rng.shuffle(true[t])
    tw = dict(TYPE_WEIGHTS, **(HARD_EXTRA_WEIGHTS if hard else {}))
    types = [t for t in tw if true[t]]
    weights = [tw[t] for t in types]
    pool, seen = [], set()
    tries = 0
    while len(pool) < size and tries < size * 20:
        tries += 1
        t = rng.choices(types, weights)[0]
        if not true[t]:
            continue
        args = true[t].pop()
        key = (t, args)
        if key in seen:
            continue
        seen.add(key)
        pool.append({"type": t, "args": list(args), "expr": expr_for(t, list(args), spec["n"])})
    return pool


def make_texts(spec, rng, style="plain"):
    f = render_clue_hard if style == "hard" else render_clue
    for c in spec["clues"]:
        c["text"] = f(spec, c, rng)


# --------------------------------------------------------------------------
# answers
# --------------------------------------------------------------------------

def parse_answer(spec, ans):
    """LLM answer -> {value: house}; missing entries are omitted."""
    out = {}
    if not isinstance(ans, dict):
        return out
    lower = {norm(v): v for vals in spec["cats"].values() for v in vals}
    for h, row in ans.items():
        try:
            house = int(str(h).strip().lower().replace("house", "").strip())
        except ValueError:
            continue
        if not isinstance(row, dict):
            continue
        for _, v in row.items():
            if isinstance(v, str) and norm(v) in lower:
                out[norm(v)] = house
    return out


def score(spec, ans):
    got = parse_answer(spec, ans)
    sol = spec["solution"]
    n_cells = len(sol)
    correct = sum(1 for v, p in sol.items() if got.get(v) == p)
    return {"cell_acc": correct / n_cells, "exact": correct == n_cells}
