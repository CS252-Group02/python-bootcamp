from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A task model representing a study or project task."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate importance bounds between 1 and 5 inclusive."""
        if not (isinstance(self.importance, int) and 1 <= self.importance <= 5):
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Calculate number of days remaining until the deadline (never below 0)."""
        delta = (self.deadline - today).days
        return max(0, delta)
