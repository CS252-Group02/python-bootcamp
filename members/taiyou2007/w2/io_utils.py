
import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read tasks from CSV, reporting invalid data with its line number."""
    tasks = []
    required = ["title", "importance", "effort_h", "deadline"]

    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None or (
            len(reader.fieldnames) != len(required)
            or set(reader.fieldnames) != set(required)
        ):
            raise ValueError("Line 1: invalid CSV header")

        for row in reader:
            line_num = reader.line_num

            try:
                if None in row or any(row[k] is None for k in required):
                    raise ValueError("missing or extra columns")

                if not row["title"].strip():
                    raise ValueError("empty title")

                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"])
                )

                tasks.append(task)

            except (ValueError, TypeError) as e:
                raise ValueError(f"line {line_num}: {e}") from e

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Write tasks as UTF-8 JSON with ISO-formatted deadlines."""
    data = []

    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
