import sys
from pathlib import Path

import pytest

BOOTCAMP_ROOT = Path(__file__).resolve().parents[3]
if str(BOOTCAMP_ROOT) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP_ROOT))

from members.nghiale29_coder.w1.grades import summary
from members.nghiale29_coder.w1.rules import can_register_thesis, missing
from members.nghiale29_coder.w1.text_tools import top_k
from members.nghiale29_coder.w1.timetable import by_day
from members.nghiale29_coder.w1.translate import insertion_sort


def test_summary_rounds_even_median_and_mean():
    assert summary([1, 2, 3, 8]) == {
        "min": 1,
        "max": 8,
        "mean": 3.5,
        "median": 2.5,
    }


def test_summary_rejects_empty_scores():
    with pytest.raises(ValueError):
        summary([])


def test_top_k_breaks_equal_counts_alphabetically():
    assert top_k("zebra apple zebra apple mango", 2) == [
        ("apple", 2),
        ("zebra", 2),
    ]


def test_thesis_requirements_at_exact_boundaries():
    assert can_register_thesis(120, 2.0)
    assert missing(119, 1.99) == [
        "need 1 more credits",
        "GPA too low (got 1.99, need 2.0)",
    ]


def test_insertion_sort_keeps_duplicates_and_input_unchanged():
    values = [3, -1, 3, 0, -1]

    assert insertion_sort(values) == [-1, -1, 0, 3, 3]
    assert values == [3, -1, 3, 0, -1]


def test_by_day_sorts_each_day_without_reordering_days():
    schedule = [
        ("CSC20002", "Wed"),
        ("CSC10001", "Mon"),
        ("CSC10002", "Mon"),
    ]

    assert by_day(schedule) == {
        "Wed": ["CSC20002"],
        "Mon": ["CSC10001", "CSC10002"],
    }
