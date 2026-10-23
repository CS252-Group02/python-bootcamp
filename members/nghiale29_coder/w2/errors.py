from .models import Task


class InfeasiblePlan(Exception):
    """Exception raised when required study hours exceed available hours."""

    def __init__(self, needed_h: float, available_h: float, message: str | None = None) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        if message is None:
            message = (
                f"Plan is infeasible: requires {needed_h} hours, but only {available_h} hours are available."
            )
        super().__init__(message)


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Validate that available hours can accommodate total task effort hours."""
    needed_h = sum(t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
