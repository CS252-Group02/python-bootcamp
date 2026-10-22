from dataclasses import dataclass

@dataclass
class InfeasiblePlan(Exception):
    needed_h: float
    available_h: float

    def __str__(self):
        return(f"Plan requires {self.needed_h} hours, but only {self.available_h} hours are available.")

def check_feasible(tasks, available_h):
    needed_h = sum(task.effort_h for task in tasks)
    if (needed_h > available_h):
        raise InfeasiblePlan(needed_h, available_h)
