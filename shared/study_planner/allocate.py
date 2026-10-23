"""Greedy allocation of a study-hour budget to already ordered tasks."""

from math import isfinite

from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Fill tasks in input order, allowing a partial final block.

    The caller supplies priority order. Zero-effort tasks are skipped, and
    neither tasks nor their effort estimates are modified. Negative or
    non-finite budgets and effort estimates raise ValueError.
    """
    if not isfinite(hours) or hours < 0:
        raise ValueError("hours must be finite and non-negative")
    for task in tasks:
        if not isfinite(task.effort_h) or task.effort_h < 0:
            raise ValueError("task effort_h must be finite and non-negative")

    blocks = []
    remaining = hours
    for task in tasks:
        if remaining <= 0:
            break
        allocated = min(task.effort_h, remaining)
        if allocated > 0:
            blocks.append(Block(task=task, hours=allocated))
            remaining -= allocated
    return blocks
