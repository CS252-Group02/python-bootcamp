from members.Slampanda.w1 import grades, rules, text_tools, timetable, translate


def test_summary_handles_unsorted_scores():
    assert grades.summary([10, 2, 7, 5]) == {
        "min": 2,
        "max": 10,
        "mean": 6,
        "median": 6,
    }


def test_word_count_handles_mixed_case_and_whitespace():
    assert text_tools.word_count("  Python\npython\tTEST! ") == {
        "python": 2,
        "test": 1,
    }


def test_top_k_zero_returns_no_words():
    # Edge case not covered by the instructor tests.
    assert text_tools.top_k("one two two", 0) == []


def test_thesis_requirements_at_exact_boundaries():
    assert rules.can_register_thesis(120, 2.0)
    assert rules.missing(120, 2.0) == []


def test_by_day_groups_and_sorts_courses():
    assert timetable.by_day(
        [
            ("CSC200", "Mon"),
            ("CSC100", "Mon"),
            ("MTH100", "Wed"),
            ("ENG100", "Mon"),
        ]
    ) == {
        "Mon": ["CSC100", "CSC200", "ENG100"],
        "Wed": ["MTH100"],
    }


def test_transpose_single_row_matrix():
    assert translate.transpose([[1, 2, 3]]) == [[1], [2], [3]]