"""Task filtering utilities for study planner."""
from datetime import date

from shared.contract import Task


def filter_active(tasks: list[Task], today: date, min_importance: int = 1) -> list[Task]:
    """Filter out overdue tasks and tasks below the minimum importance threshold.

    Args:
        tasks: List of Task objects.
        today: Reference date for deadline evaluation.
        min_importance: Minimum importance level (1 to 5) to include. Defaults to 1.

    Returns:
        List of tasks that are active (deadline >= today) and have importance >= min_importance.
    """
    return [
        t for t in tasks
        if t.deadline >= today and t.importance >= min_importance
    ]


def filter_by_deadline(tasks: list[Task], max_date: date) -> list[Task]:
    """Filter tasks due on or before a given maximum date.

    Args:
        tasks: List of Task objects.
        max_date: The cutoff date (inclusive).

    Returns:
        List of tasks with deadline <= max_date.
    """
    return [t for t in tasks if t.deadline <= max_date]
