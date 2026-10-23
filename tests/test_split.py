from datetime import date
from shared.contract import Task
from shared.study_planner.split import split_large_tasks


def test_split_large_tasks():
    t_small = Task("Review", 3, 1.5, date(2026, 10, 30))
    t_large = Task("DS Exam", 5, 5.0, date(2026, 10, 30))

    result = split_large_tasks([t_small, t_large], max_hours=2.0)
    assert len(result) == 4
    assert result[0].title == "Review"
    assert result[1].title == "DS Exam (Part 1)"
    assert result[1].effort_h == 2.0
    assert result[3].title == "DS Exam (Part 3)"
    assert result[3].effort_h == 1.0