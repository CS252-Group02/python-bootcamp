import csv
from datetime import date
from os import PathLike

from shared.contract import Task


def parse_csv(path: str | PathLike[str]) -> list[Task]:
    """Parse tasks from a CSV file."""
    tasks: list[Task] = []

    try:
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
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Task file not found: {path}") from error

    return tasks
