from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    priority: int
    estimate: float
    deadline: date

    def __post_init__(self):
        if not (1 <= self.priority <= 5):
            raise ValueError(
                f"Priority must be between 1 and 5, got {self.priority}"
            )
        if self.estimate < 0:
            raise ValueError("Estimate cannot be negative")

    def days_left(self, today: date) -> int:
        remaining = (self.deadline - today).days
        return max(0, remaining)

    @property
    def name(self) -> str:
        return self.title
    
    @property
    def hours(self) -> float:
        return self.estimate