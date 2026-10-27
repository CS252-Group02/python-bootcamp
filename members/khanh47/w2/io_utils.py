import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: Path) -> list[Task]:
    """Load study tasks from a CSV file."""
    tasks: list[Task] = []

    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for linenum, row in enumerate(reader, start=2):
            try:
                task = Task(
                    row["title"],
                    int(row["importance"]),
                    float(row["effort_h"]),
                    date.fromisoformat(row["deadline"])
                )
                tasks.append(task)
            except ValueError as e:
                raise ValueError(f"Invalid data at line {linenum}: {e}") from e
    return tasks

def save_json(tasks: list[Task], path: Path) -> None:
    """Save study tasks as a JSON list."""
    data = []
    for task in tasks:
        task_dict = asdict(task)
        task_dict["deadline"] = task.deadline.isoformat()
        data.append(task_dict)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
