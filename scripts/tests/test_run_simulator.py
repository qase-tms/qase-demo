"""
Smoke tests for the run-result generation helpers in run_simulator.py.

Run with:
  python -m pytest scripts/tests/test_run_simulator.py -v
  # or without pytest:
  python scripts/tests/test_run_simulator.py
"""

from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from run_simulator import (  # noqa: E402
    STATUS_FAILED,
    STATUS_PASSED,
    _generate_run_results,
)


# ---------------------------------------------------------------------------
# Fixtures (plain builders, no YAML / network required)
# ---------------------------------------------------------------------------

def _profile() -> dict:
    return {
        "duration_buckets_ms": {
            "fast": [200, 800],
            "medium": [800, 2500],
            "slow": [2500, 6000],
        },
        "worker_range": [3, 5],
        "gap_frequency": 0.2,
        "idle_gap_ms": [2000, 7000],
    }


def _templates() -> dict:
    return {
        "auto_step_actions": ["Do A", "Do B", "Do C"],
        "manual_step_actions": ["Check A", "Check B", "Check C"],
        "result_comments": ["ok"],
    }


def _case_contexts(n: int = 60, weak_suite_title: str = "04 Checkout") -> list[dict]:
    ctx = []
    for i in range(n):
        # Mix a minority of weak-suite cases in with healthy ones.
        suite = weak_suite_title if i % 5 == 0 else "02 Catalog"
        ctx.append(
            {
                "qase_case_id": 1000 + i,
                "root_suite_title": suite,
                "params": None,
            }
        )
    return ctx


def _run(fail_bias: float = 0.0, force_green: bool = False, seed: int = 7):
    return _generate_run_results(
        rng=random.Random(seed),
        case_contexts=_case_contexts(),
        weak_suite_title="04 Checkout",
        force_green=force_green,
        fail_bias=fail_bias,
        profile=_profile(),
        templates=_templates(),
        attachment_hashes=[],
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_high_fail_bias_produces_failure_majority() -> None:
    _, audit = _run(fail_bias=0.68)
    assert audit["failed"] > audit["passed"], audit
    # Heavy failure target: at least ~55% of results should fail.
    assert audit["failed"] >= audit["total"] * 0.55, audit


def test_high_fail_bias_marks_some_defects() -> None:
    _, audit = _run(fail_bias=0.68)
    assert audit["defect"] >= 1, audit


def test_force_green_still_all_passed() -> None:
    entries, audit = _run(force_green=True)
    assert audit["failed"] == 0, audit
    assert audit["passed"] == audit["total"], audit
    assert all(e["status"] == STATUS_PASSED for e in entries)


def test_default_bias_is_pass_dominant() -> None:
    _, audit = _run()  # fail_bias defaults to 0.0
    assert audit["passed"] > audit["failed"], audit


def _has_failed_status(entries: list[dict]) -> bool:
    return any(e["status"] == STATUS_FAILED for e in entries)


if __name__ == "__main__":
    tests = [
        test_high_fail_bias_produces_failure_majority,
        test_high_fail_bias_marks_some_defects,
        test_force_green_still_all_passed,
        test_default_bias_is_pass_dominant,
    ]
    passed = failed = 0
    for fn in tests:
        try:
            fn()
            print(f"  PASS  {fn.__name__}")
            passed += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL  {fn.__name__}: {exc}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed out of {len(tests)} tests.")
    sys.exit(0 if failed == 0 else 1)
