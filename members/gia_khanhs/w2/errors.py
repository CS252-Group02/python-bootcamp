from dataclasses import dataclass

from .models import Task


@dataclass
class InfeasiblePlan(Exception):
    """Report the hours required and available for an infeasible plan."""

    needed_h: float
    available_h: float

    def __str__(self) -> str:
        """Describe why the tasks cannot fit into the available hours."""
        return f"Tasks require {self.needed_h} hours, but only {self.available_h} hours are available"

def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if total task effort exceeds available hours."""
    total_h = 0
    for task in tasks:
        total_h += task.effort_h

    if total_h > available_h:
        raise InfeasiblePlan(total_h, available_h)
