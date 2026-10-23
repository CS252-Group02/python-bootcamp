from datetime import date

from shared.contract import Task
from shared.study_planner.filter import filter_active, filter_by_deadline


def test_filter_active_removes_overdue() -> None:
    today = date(2026, 10, 25)
    tasks = [
        Task("Overdue Task", 5, 2.0, date(2026, 10, 20)),
        Task("Active Task", 4, 3.0, date(2026, 10, 26)),
        Task("Due Today Task", 3, 1.0, date(2026, 10, 25)),
    ]
    filtered = filter_active(tasks, today)
    assert [t.title for t in filtered] == ["Active Task", "Due Today Task"]


def test_filter_active_with_min_importance() -> None:
    today = date(2026, 10, 25)
    tasks = [
        Task("Low priority", 2, 1.0, date(2026, 10, 30)),
        Task("High priority", 5, 4.0, date(2026, 10, 30)),
        Task("Medium priority", 3, 2.0, date(2026, 10, 28)),
    ]
    filtered = filter_active(tasks, today, min_importance=3)
    assert [t.title for t in filtered] == ["High priority", "Medium priority"]


def test_filter_active_empty() -> None:
    today = date(2026, 10, 25)
    assert filter_active([], today) == []


def test_filter_by_deadline() -> None:
    cutoff = date(2026, 10, 27)
    tasks = [
        Task("Early", 4, 2.0, date(2026, 10, 26)),
        Task("On Cutoff", 5, 1.0, date(2026, 10, 27)),
        Task("Late", 3, 3.0, date(2026, 10, 28)),
    ]
    result = filter_by_deadline(tasks, cutoff)
    assert [t.title for t in result] == ["Early", "On Cutoff"]
