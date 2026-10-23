import csv
import json
from datetime import date

from .models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []

    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
                tasks.append(task)
            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(
                    f"Invalid row at line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    data = []

    for task in tasks:
        data.append({
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        })

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)