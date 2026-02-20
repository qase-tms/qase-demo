"""
Smoke tests for deterministic helpers in jira_requirements.py.

Run with:
  python -m pytest scripts/tests/test_jira_requirements.py -v
  # or without pytest:
  python scripts/tests/test_jira_requirements.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from jira_requirements import (  # noqa: E402
    _all_two_letter_codes,
    _select_project_name,
    _story_slug,
    build_jira_state,
    select_project_key,
    validate_seed,
)


# ---------------------------------------------------------------------------
# select_project_key
# ---------------------------------------------------------------------------

def test_first_key_is_AA_when_nothing_exists() -> None:
    assert select_project_key(set()) == "AA"


def test_skips_occupied_keys() -> None:
    assert select_project_key({"AA"}) == "AB"
    assert select_project_key({"AA", "AB"}) == "AC"


def test_case_insensitive_key_check() -> None:
    assert select_project_key({"aa", "ab"}) == "AC"


def test_skips_many_keys_in_order() -> None:
    occupied = set(_all_two_letter_codes()[:10])   # AA–AJ
    result = select_project_key(occupied)
    assert result == "AK"


def test_all_codes_generated_once() -> None:
    codes = _all_two_letter_codes()
    assert len(codes) == 676
    assert codes[0] == "AA"
    assert codes[-1] == "ZZ"
    assert len(set(codes)) == 676


# ---------------------------------------------------------------------------
# _select_project_name
# ---------------------------------------------------------------------------

def test_unique_name_returned_as_is() -> None:
    assert _select_project_name("Alpha", ["Beta", "Gamma"]) == "Alpha"


def test_appends_2_on_first_collision() -> None:
    assert _select_project_name("Alpha", ["Alpha", "Beta"]) == "Alpha (2)"


def test_increments_suffix_past_occupied() -> None:
    existing = ["Alpha", "Alpha (2)", "Alpha (3)"]
    assert _select_project_name("Alpha", existing) == "Alpha (4)"


def test_name_comparison_is_case_insensitive() -> None:
    assert _select_project_name("alpha", ["ALPHA"]) == "alpha (2)"


def test_suffix_skips_non_contiguous_gap() -> None:
    existing = ["Alpha", "Alpha (2)", "Alpha (4)"]
    assert _select_project_name("Alpha", existing) == "Alpha (3)"


# ---------------------------------------------------------------------------
# _story_slug
# ---------------------------------------------------------------------------

def test_story_slug_namespacing() -> None:
    assert _story_slug("auth", 1) == "auth-1"
    assert _story_slug("checkout", 3) == "checkout-3"


# ---------------------------------------------------------------------------
# validate_seed
# ---------------------------------------------------------------------------

def test_validate_seed_passes_clean_input() -> None:
    seed = {
        "epics": [{"slug": "auth", "summary": "Auth epic"}],
        "stories": [{"epic": "auth", "summary": "A story"}],
    }
    validate_seed(seed)   # should not raise


def test_validate_seed_raises_on_duplicate_slug() -> None:
    seed = {
        "epics": [
            {"slug": "auth", "summary": "Epic A"},
            {"slug": "auth", "summary": "Epic B"},
        ],
        "stories": [],
    }
    try:
        validate_seed(seed)
        assert False, "Expected SystemExit"
    except SystemExit as exc:
        assert "Duplicate" in str(exc)


def test_validate_seed_raises_on_missing_epic_ref() -> None:
    seed = {
        "epics": [{"slug": "auth", "summary": "Auth"}],
        "stories": [{"epic": "search", "summary": "Unknown epic ref"}],
    }
    try:
        validate_seed(seed)
        assert False, "Expected SystemExit"
    except SystemExit as exc:
        assert "unknown epic slug" in str(exc).lower()


# ---------------------------------------------------------------------------
# build_jira_state
# ---------------------------------------------------------------------------

def test_build_jira_state_structure() -> None:
    project = {"name": "Test", "key": "AA", "id": 1}
    epic_slugs = ["auth", "cart"]
    created_epics = [
        {"key": "AA-1", "id": "100"},
        {"key": "AA-2", "id": "101"},
    ]
    stories_seed = [
        {"epic": "auth", "summary": "Sign up"},
        {"epic": "auth", "summary": "Log in"},
        {"epic": "cart", "summary": "Add item"},
    ]
    created_stories = [
        {"key": "AA-3", "id": "200"},
        {"key": "AA-4", "id": "201"},
        {"key": "AA-5", "id": "202"},
    ]

    state = build_jira_state(project, epic_slugs, created_epics, stories_seed, created_stories)

    assert state["project"] == project
    assert state["epics"]["auth"]["jira_key"] == "AA-1"
    assert state["epics"]["auth"]["issue_type"] == "Epic"
    assert state["epics"]["cart"]["jira_key"] == "AA-2"

    assert "auth-1" in state["stories"]
    assert "auth-2" in state["stories"]
    assert "cart-1" in state["stories"]
    assert state["stories"]["auth-1"]["epic_slug"] == "auth"
    assert state["stories"]["cart-1"]["jira_key"] == "AA-5"


# ---------------------------------------------------------------------------
# Plain runner (no pytest required)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    tests = [
        test_first_key_is_AA_when_nothing_exists,
        test_skips_occupied_keys,
        test_case_insensitive_key_check,
        test_skips_many_keys_in_order,
        test_all_codes_generated_once,
        test_unique_name_returned_as_is,
        test_appends_2_on_first_collision,
        test_increments_suffix_past_occupied,
        test_name_comparison_is_case_insensitive,
        test_suffix_skips_non_contiguous_gap,
        test_story_slug_namespacing,
        test_validate_seed_passes_clean_input,
        test_validate_seed_raises_on_duplicate_slug,
        test_validate_seed_raises_on_missing_epic_ref,
        test_build_jira_state_structure,
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
