from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Store a task's importance, effort in hours, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Reject importance values outside the range 1 through 5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return days until the deadline, using zero for overdue tasks."""
        date_diff = self.deadline - today
        d_left = max(0, date_diff.days)

        return d_left
