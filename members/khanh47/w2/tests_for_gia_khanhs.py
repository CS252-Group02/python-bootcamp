from members.gia_khanhs.w1 import grades, rules, text_tools, timetable, translate


def test_summary_rounds_statistics_and_handles_unsorted_scores():
    assert grades.summary([10, 2, 6]) == {
        "min": 2,
        "max": 10,
        "mean": 6,
        "median": 6,
    }


def test_word_count_normalizes_case_and_punctuation():
    assert text_tools.word_count("PyTest, pytest! PYTHON.") == {
        "pytest": 2,
        "python": 1,
    }


def test_word_count_returns_empty_mapping_for_punctuation_only_input():
    assert text_tools.word_count("... !!! ???") == {}


def test_top_k_returns_no_results_when_k_is_zero():
    assert text_tools.top_k("one two", 0) == []


def test_missing_reports_each_unsatisfied_requirement():
    missing = rules.missing(118, 1.5)
    assert missing[0] == "need 2 more credits"
    assert len(missing) == 2


def test_by_day_sorts_courses_within_each_day():
    assert timetable.by_day(
        [("ZOO100", "Mon"), ("BIO100", "Mon"), ("MAT100", "Tue")]
    ) == {"Mon": ["BIO100", "ZOO100"], "Tue": ["MAT100"]}


def test_run_length_encode_preserves_unicode_and_empty_input():
    assert translate.run_length_encode("ää🙂🙂a") == [("ä", 2), ("🙂", 2), ("a", 1)]
    assert translate.run_length_encode("") == []
