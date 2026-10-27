from dataclasses import dataclass
from datetime import date


@dataclass
class Task: 
    """Represent a study task with its priority, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate the task's importance level."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int: 
        """Return non-negative days remaining until the deadline."""
        return max(0, (self.deadline - today).days)
