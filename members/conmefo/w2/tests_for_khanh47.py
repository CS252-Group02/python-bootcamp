"""Peer tests: python -m pytest -q members/conmefo/w2/tests_for_khanh47.py"""

import pytest

from members.khanh47.w1 import grades, rules, text_tools, timetable, translate


@pytest.mark.parametrize(
    "values, key, expected",
    [
        ([], 4, -1),
        ([4], 4, 0),
        ([4], 3, -1),
        ([-8, -3, 0, 7, 12], -8, 0),
        ([-8, -3, 0, 7, 12], 12, 4),
        ([-8, -3, 0, 7, 12], 5, -1),
    ],
)
def test_binary_search_boundaries_and_missing_keys(values, key, expected):
    original = values.copy()
    assert translate.binary_search(values, key) == expected
    assert values == original


def test_binary_search_duplicate_key_returns_a_matching_index():
    values = [1, 3, 3, 3, 8]
    index = translate.binary_search(values, 3)
    assert index in (1, 2, 3)


def test_summary_single_score_and_input_preservation():
    assert grades.summary([8.25]) == {
        "min": 8.25, "max": 8.25, "mean": 8.25, "median": 8.25,
    }
    scores = [9, 1, 5]
    grades.summary(scores)
    assert scores == [9, 1, 5]


def test_word_count_handles_mixed_whitespace_and_adjacent_punctuation():
    assert text_tools.word_count("Red;;BLUE\tred\nblue:red") == {
        "red": 3, "blue": 2,
    }


def test_top_k_larger_than_vocabulary_returns_all_words_ranked():
    assert text_tools.top_k("sun moon sun star sun moon", 10) == [
        ("sun", 3), ("moon", 2), ("star", 1),
    ]


@pytest.mark.parametrize("credits, gpa", [(119, 2.0), (120, 1.99), (119, 1.99)])
def test_thesis_rejects_each_unsatisfied_requirement(credits, gpa):
    assert not rules.can_register_thesis(credits, gpa)
    assert len(rules.missing(credits, gpa)) == (credits < 120) + (gpa < 2.0)


def test_timetable_keeps_repeated_entries_without_mutating_input():
    pairs = [("CS2", "Fri"), ("CS1", "Fri"), ("CS2", "Fri")]
    original = pairs.copy()
    assert timetable.by_day(pairs) == {"Fri": ["CS1", "CS2", "CS2"]}
    assert pairs == original
