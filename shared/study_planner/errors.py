"""Exceptions and validation shared by the study-planner command."""

from collections.abc import Iterable

from shared.contract import Task


class InfeasiblePlan(ValueError):
    """Raised when a planner is asked to allocate an impossible amount of time."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Plan infeasible: needed {needed_h:g} h, "
            f"but only {available_h:g} h available."
        )


def require_positive_hours(hours: float) -> None:
    """Reject a non-positive time budget using the shared planner exception."""
    if hours <= 0:
        raise InfeasiblePlan(needed_h=0, available_h=hours)


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Raise if all supplied tasks cannot fit in ``available_h`` hours.

    This helper is intentionally opt-in: the regular planner may create a
    partial plan when its time budget is smaller than the full task list.
    """
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
