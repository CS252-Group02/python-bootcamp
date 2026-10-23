from shared.contract import Task


def split_large_tasks(tasks: list[Task], max_hours: float = 2.0) -> list[Task]:
    """Chia các task có effort_h > max_hours thành nhiều sub-task nhỏ hơn.

    Ví dụ: Task 5h với max_hours=2.0 -> Task Part 1 (2h), Part 2 (2h), Part 3
    (1h).
    """
    result: list[Task] = []

    for task in tasks:
        if task.effort_h <= max_hours:
            result.append(task)
            continue

        remaining = task.effort_h
        part_idx = 1
        while remaining > 0:
            current_effort = min(remaining, max_hours)
            sub_task = Task(
                title=f"{task.title} (Part {part_idx})",
                importance=task.importance,
                effort_h=current_effort,
                deadline=task.deadline,
            )
            result.append(sub_task)
            remaining -= current_effort
            part_idx += 1

    return result