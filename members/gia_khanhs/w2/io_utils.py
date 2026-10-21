import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def tasks_by_reader(reader) -> list[Task]:
    tasks = []
    next(reader)

    id: int = 1

    for row in reader:
        id += 1

        numeric_row = row
        try:
            numeric_row[1] = int(row[1])
            numeric_row[2] = float(row[2])
            numeric_row[3] = date.fromisoformat(row[3])
        except ValueError:
            raise ValueError(f"value error in line {id}")

        tasks.append(Task(*numeric_row))

    return tasks


def load_tasks(path: Path) -> list[Task]:
    tasks = None

    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        tasks = tasks_by_reader(reader) 

    return tasks


def save_json(tasks: list[Task], path: Path):
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