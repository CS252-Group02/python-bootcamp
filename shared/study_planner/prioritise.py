from datetime import date
from ..contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    priority_and_task = [(task.importance / (task.days_left(today) + 0.1), task)
                         for task in tasks]

    priority_and_task = sorted(priority_and_task, key=lambda p_t: p_t[0], reverse=True)

    prioritised = [p_t[1]
                   for p_t in priority_and_task]
    return prioritised
    


def test_prioritise():
    today = date(2026, 10, 23)
    important = Task("Important", 5, 1, date(2026, 10, 28))
    less_important = Task("Less important", 1, 1, date(2026, 10, 28))
    urgent = Task("Urgent", 2, 1, date(2026, 10, 24))
    due_today = Task("Due today", 1, 1, today)
    overdue = Task("Overdue", 3, 1, date(2026, 10, 22))
    tied = Task("Tied", 5, 2, date(2026, 10, 28))

    tasks = [less_important, important, urgent, due_today, overdue]
    original = tasks.copy()
    assert prioritise(tasks, today) == [
        overdue, due_today, urgent, important, less_important,
    ]
    assert tasks == original
    assert prioritise([important, tied], today) == [important, tied]
    assert prioritise([tied, important], today) == [tied, important]
    assert prioritise([due_today], today) == [due_today]
    assert prioritise([], today) == []
