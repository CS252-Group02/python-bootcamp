"""Task data models and deadline calculation."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a scheduled task with priority, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate importance is within 1 to 5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return remaining days until deadline, minimum 0."""
        return max(0, (self.deadline - today).days)
