import csv
import json
from collections.abc import Iterator
from datetime import date
from pathlib import Path

from .models import Task


def tasks_by_reader(reader: Iterator[list[str]]) -> list[Task]:
    """Parse CSV rows after the header, reporting invalid row numbers."""
    tasks: list[Task] = []
    next(reader)

    id: int = 1

    for row in reader:
        id += 1

        try:
            importance: int = int(row[1])
            effort_h: float = float(row[2])
            deadline: date = date.fromisoformat(row[3])
            task = Task(row[0], importance, effort_h, deadline)
        except ValueError as exc:
            raise ValueError(f"value error in line {id}") from exc

        tasks.append(task)

    return tasks


def load_tasks(path: Path) -> list[Task]:
    """Read tasks from a UTF-8 CSV file."""

    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        tasks = tasks_by_reader(reader) 

    return tasks


def save_json(tasks: list[Task], path: Path) -> None:
    """Save tasks as JSON with ISO-formatted deadline strings."""
    serialisable_tasks = [
        {   
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": str(task.deadline)
        }
        for task in tasks
    ]

    with open(path, mode='w', encoding='utf-8') as file:
        json.dump(serialisable_tasks, file)
