"""Peer-review tests for conmefo's five Week 1 exercises (variant 4)."""

import pytest

from members.conmefo.w1 import grades, rules, text_tools, timetable, translate


@pytest.mark.parametrize(
    ("scores", "expected"),
    [
        ([9, 2, 2, 5, 2], {"min": 2, "max": 9, "mean": 4, "median": 2}),
        ([10, 0, 10, 0], {"min": 0, "max": 10, "mean": 5, "median": 5}),
        ([1.111, 2.222, 3.333],
         {"min": 1.111, "max": 3.333, "mean": 2.22, "median": 2.22}),
        ([0], {"min": 0, "max": 0, "mean": 0, "median": 0}),
    ],
)
def test_summary_handles_duplicates_rounding_and_preserves_input(
    scores: list[float], expected: dict[str, float],
) -> None:
    """Verify summary handles duplicates rounding and preserves input."""
    original = scores.copy()
    assert grades.summary(scores) == expected
    assert scores == original


def test_summary_rejects_empty_scores() -> None:
    """Verify summary rejects empty scores."""
    with pytest.raises(ValueError):
        grades.summary([])


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", {}),
        (" \t\n.,!?;:", {}),
        ("Alpha,beta!ALPHA?beta;gamma:ALPHA.",
         {"alpha": 3, "beta": 2, "gamma": 1}),
        ("One\ttwo\nONE   two", {"one": 2, "two": 2}),
    ],
)
def test_word_count_handles_empty_text_punctuation_and_whitespace(
    text: str, expected: dict[str, int],
) -> None:
    """Verify word count handles empty text punctuation and whitespace."""
    assert text_tools.word_count(text) == expected


@pytest.mark.parametrize(
    ("k", "expected"),
    [
        (-1, []),
        (0, []),
        (1, [("apple", 2)]),
        (2, [("apple", 2), ("zebra", 2)]),
        (10, [("apple", 2), ("zebra", 2), ("berry", 1), ("pear", 1)]),
    ],
)
def test_top_k_orders_by_frequency_then_alphabetically_and_limits_results(
    k: int, expected: list[tuple[str, int]],
) -> None:
    """Verify top k orders by frequency then alphabetically and limits results."""
    assert text_tools.top_k("zebra pear apple zebra berry apple", k) == expected


@pytest.mark.parametrize(
    ("credits", "gpa", "eligible", "reason_count"),
    [
        (119, 2.0, False, 1),
        (120, 1.99, False, 1),
        (119, 1.99, False, 2),
        (120, 2.0, True, 0),
        (121, 2.01, True, 0),
        (0, 0.0, False, 2),
    ],
)
def test_thesis_thresholds_and_missing_reasons_agree(
    credits: int, gpa: float, eligible: bool, reason_count: int,
) -> None:
    """Verify thesis thresholds and missing reasons agree."""
    assert rules.can_register_thesis(credits, gpa) is eligible
    reasons = rules.missing(credits, gpa)
    assert len(reasons) == reason_count
    assert all(isinstance(reason, str) and reason.strip() for reason in reasons)


def test_missing_reports_credit_deficit_at_the_boundary() -> None:
    """Verify missing reports credit deficit at the boundary."""
    assert rules.missing(119, 2.0) == ["need 1 more credits"]


def test_by_day_sorts_each_day_retains_duplicates_and_preserves_input() -> None:
    """Verify by day sorts each day retains duplicates and preserves input."""
    courses = [
        ("ZZZ200", "Tue"),
        ("CSC100", "Mon"),
        ("AAA100", "Tue"),
        ("CSC100", "Mon"),
        ("AAA100", "Mon"),
    ]
    original = courses.copy()
    assert timetable.by_day(courses) == {
        "Tue": ["AAA100", "ZZZ200"],
        "Mon": ["AAA100", "CSC100", "CSC100"],
    }
    assert courses == original


def test_by_day_returns_independent_results_for_empty_and_repeated_calls() -> None:
    """Verify by day returns independent results for empty and repeated calls."""
    assert timetable.by_day([]) == {}
    courses = [("CSC100", "Mon")]
    first = timetable.by_day(courses)
    first["Mon"].append("EXTRA")
    assert timetable.by_day(courses) == {"Mon": ["CSC100"]}
    assert courses == [("CSC100", "Mon")]


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (-5, []),
        (0, []),
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (4, [2, 3]),
        (9, [2, 3, 5, 7]),
        (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (29, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
    ],
)
def test_primes_up_to_includes_prime_endpoint_and_excludes_squares(
    n: int, expected: list[int],
) -> None:
    """Verify primes up to includes prime endpoint and excludes squares."""
    assert translate.primes_up_to(n) == expected


def test_primes_up_to_matches_trial_division_and_returns_sorted_unique_values() -> None:
    """Verify primes up to matches trial division and returns sorted unique values."""
    expected = [
        n for n in range(2, 201)
        if all(n % divisor for divisor in range(2, n))
    ]
    actual = translate.primes_up_to(200)
    assert actual == expected
    assert actual == sorted(set(actual))
