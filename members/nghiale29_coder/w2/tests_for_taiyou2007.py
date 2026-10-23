import pytest

from members.taiyou2007.w1.grades import summary
from members.taiyou2007.w1.rules import can_register_thesis, missing
from members.taiyou2007.w1.text_tools import top_k, word_count
from members.taiyou2007.w1.timetable import by_day


def test_taiyou2007_summary_single_element() -> None:
    """Test summary with a single score."""
    res = summary([9.0])
    assert res == {"min": 9.0, "max": 9.0, "mean": 9.0, "median": 9.0}


def test_taiyou2007_summary_empty_raises_value_error() -> None:
    """Edge case: empty score list must raise ValueError."""
    with pytest.raises(ValueError):
        summary([])


def test_taiyou2007_word_count_punctuation_and_case() -> None:
    """Verify word_count ignores standard punctuation marks and normalizes case."""
    text = "Hello, world! HELLO... Python; world?"
    counts = word_count(text)
    assert counts["hello"] == 2
    assert counts["world"] == 2
    assert counts["python"] == 1


def test_taiyou2007_top_k_tie_breaking() -> None:
    """Edge case: top_k with equal counts must break ties alphabetically."""
    text = "banana apple cherry apple banana cherry date"
    # apple: 2, banana: 2, cherry: 2, date: 1
    # top 3 should be sorted by count (2) then alphabetically: apple, banana, cherry
    result = top_k(text, 3)
    assert result == [("apple", 2), ("banana", 2), ("cherry", 2)]


def test_taiyou2007_rules_boundary_and_missing() -> None:
    """Test boundary conditions for thesis registration and missing requirements."""
    # Exactly at boundary: 120 credits, 2.0 GPA
    assert can_register_thesis(120, 2.0) is True
    assert missing(120, 2.0) == []

    # Just below boundary
    assert can_register_thesis(119, 1.99) is False
    reasons = missing(119, 1.99)
    assert len(reasons) == 2


def test_taiyou2007_timetable_grouping() -> None:
    """Test timetable grouping and course sorting by day."""
    pairs = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    grouped = by_day(pairs)
    assert grouped["Mon"] == ["CSC10001", "CSC10014"]
    assert grouped["Tue"] == ["MTH00003"]
