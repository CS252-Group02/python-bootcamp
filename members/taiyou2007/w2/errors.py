from .models import Task


class InfeasiblePlan(Exception):
    """Report the required and available hours for an infeasible plan."""
    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the time budget and total required effort."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__()

    def __str__(self) -> str:
        """Describe the shortfall in study hours."""
        return (
            f"Infeasible plan: {self.needed_h} hours needed, "
            f"but only {self.available_h} hours available."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when total effort exceeds available hours."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
