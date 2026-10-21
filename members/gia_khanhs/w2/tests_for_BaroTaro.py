"""
python -m pytest -q members/gia_khanhs/w2/tests_for_BaroTaro.py
"""

import pytest

from members.BaroTaro.w1 import grades, rules, text_tools, timetable, translate


def test_summary_even_number_of_scores():
    assert grades.summary([7.5, 9, 6, 8]) == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_empty_scores_raise_value_error():
    with pytest.raises(ValueError):
        grades.summary([])


def test_word_count_ignores_case_and_punctuation():
    assert text_tools.word_count("Git is fun. Git is fast!") == {
        "git": 2, "is": 2, "fun": 1, "fast": 1,
    }


def test_word_count_punctuation_only():
    assert text_tools.word_count(".,?!;: \t\n") == {} # edge case


def test_top_k_breaks_frequency_ties_alphabetically():
    assert text_tools.top_k("pear apple pear banana apple banana", 2) == [
        ("apple", 2), ("banana", 2),
    ]


def test_thesis_requires_both_credit_and_gpa_thresholds():
    assert rules.can_register_thesis(120, 2.0)
    assert not rules.can_register_thesis(119, 3.0)
    assert not rules.can_register_thesis(130, 1.99)
    assert rules.missing(118, 3.0) == ["need 2 more credits"]
    assert rules.missing(120, 2.0) == []


def test_gcd_common_factor():
    assert translate.gcd(54, 24) == 6


def test_gcd_zero_and_negative_operands():
    assert translate.gcd(0, 12) == 12 # edge case
    assert translate.gcd(12, 0) == 12
    assert translate.gcd(0, 0) == 0
    assert translate.gcd(-54, 24) == 6


def test_by_day_groups_courses_and_sorts_each_day():
    schedule = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    assert timetable.by_day(schedule) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }
    assert timetable.by_day([]) == {}
