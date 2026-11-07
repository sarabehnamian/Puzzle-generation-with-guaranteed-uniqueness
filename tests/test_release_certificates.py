"""Release-integrity contract: re-prove released benchmark certificates.

The benchmark's central claim is that every released puzzle carries a solver
certificate of a unique answer (MiniSat, cross-checked with OR-tools CP-SAT).
This test re-proves that claim on a deterministic stratified sample of the
released `benchmark/puzzles.jsonl` with the repo's own certifier, so a change
that silently breaks uniqueness, encoding, or the intended-solution match fails
CI instead of surfacing in published numbers.

The full 242-puzzle re-certification runs as a scheduled job (see
.github/workflows/ci.yml); this test keeps every push fast (~1-2 min).
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.analyze import certify

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "benchmark" / "puzzles.jsonl"
STRIDE = 20  # deterministic stratified sample: every 20th puzzle, all families


def _sample():
    puzzles = [json.loads(line) for line in BANK.read_text().splitlines() if line.strip()]
    return puzzles[::STRIDE]


def test_release_file_exists_and_is_nonempty():
    assert BANK.is_file()
    puzzles = [json.loads(line) for line in BANK.read_text().splitlines() if line.strip()]
    assert len(puzzles) >= 200, f"expected the released bank, found {len(puzzles)}"


@pytest.mark.parametrize("puzzle", _sample(), ids=lambda p: p["id"])
def test_released_puzzle_certificate_still_holds(puzzle):
    cert, _cnf, _sols = certify(puzzle["spec"])
    assert cert["unique"] is True, f"{puzzle['id']}: MiniSat no longer proves uniqueness"
    assert cert["cpsat_unique"] is True, f"{puzzle['id']}: CP-SAT cross-check failed"
    assert cert["matches_intended"] is True, f"{puzzle['id']}: unique solution differs from the intended one"
