"""Custom exceptions for study planner feasibility."""

from typing import Any


class InfeasiblePlan(Exception):
    """Raised when available study hours are insufficient for tasks."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Initialize exception with required and available hours."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(needed_h, available_h)

    def __str__(self) -> str:
        """Return formatted error message."""
        return (
            f"Plan requires {self.needed_h:g} hours, "
            f"but only {self.available_h:g} hours are available"
        )


def check_feasible(tasks: list[Any], available_h: float) -> None:
    """Verify that total task effort does not exceed available hours."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
