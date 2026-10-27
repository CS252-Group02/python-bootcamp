"""Allocate a finite time budget across prioritised tasks."""

from shared.contract import Block, Task
from shared.study_planner.errors import require_positive_hours


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Allocate up to ``hours`` in task order, allowing a final partial task."""
    require_positive_hours(hours)
    block_list: list[Block] = []
    for task in tasks:
        if hours <= 0:
            break
        using_hour = min(hours, task.effort_h)
        block_list.append(Block(task, using_hour))
        hours -= using_hour
    return block_list
