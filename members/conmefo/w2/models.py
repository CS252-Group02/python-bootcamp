"""Week 2 task model."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with an importance from 1 to 5."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Reject importance values outside 1-5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")

    def days_left(self, today: date) -> int:
        """Return whole days until the deadline, never below zero."""
        return max(0, (self.deadline - today).days)
