from dataclasses import dataclass

from .models import Task


@dataclass
class InfeasiblePlan(Exception):
    """Describe a study plan that needs more hours than are available."""

    needed_h: float
    available_h: float

    def __str__(self) -> str:
        """Return a readable explanation of the infeasible plan."""
        return f"Plan requires {self.needed_h} hours, but only {self.available_h} hours are available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when the tasks exceed the available hours."""
    needed_h = sum(task.effort_h for task in tasks)
    if (needed_h > available_h):
        raise InfeasiblePlan(needed_h, available_h)
