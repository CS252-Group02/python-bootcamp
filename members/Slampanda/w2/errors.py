from collections.abc import Iterable
from typing import Any


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Plan infeasible: needed {needed_h}h, but only {available_h}h available."
        )

    def __str__(self) -> str:
        return f"Plan infeasible: needed {self.needed_h} hours, but only {self.available_h} hours available."

def check_feasible(tasks: Iterable[Any], available_h: float) -> None:
    needed_h = 0.0
    for t in tasks:
        hours = getattr(
            t, "estimate", getattr(t, "effort_h", getattr(t, "hours", 0.0))
        )
        needed_h += hours

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
