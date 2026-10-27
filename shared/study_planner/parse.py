import csv
from datetime import date
from os import PathLike

from shared.contract import Task


def parse_csv(path: str | PathLike[str]) -> list[Task]:
    """Parse tasks from a CSV file, raising ValueError if it has no tasks."""
    tasks: list[Task] = []

    with open(path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            tasks.append(
                Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            )

    if not tasks:
        raise ValueError("The task file is empty: no tasks found.")

    return tasks
