import csv
import json
from dataclasses import asdict
from datetime import date

from .models import Task


def load_tasks(path) -> list[Task]:
    tasks: list[Task] = []

    with path.open("r", newline = "") as file:
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

def save_json(tasks, path):
    data = []
    for task in tasks:
        task_dict = asdict(task)
        task_dict["deadline"] = task.deadline.isoformat()
        data.append(task_dict)
    with path.open("w") as file:
        json.dump(data, file)
