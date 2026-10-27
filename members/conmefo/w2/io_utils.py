"""Week 2 CSV and JSON helpers for tasks."""

import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read tasks from a CSV file, raising ValueError with the bad line number."""
    tasks: list[Task] = []
    with Path(path).open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"title", "importance", "effort_h", "deadline"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("line 1: missing required CSV columns")
        for row in reader:
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except (ValueError, TypeError) as exc:
                raise ValueError(f"line {reader.line_num}: {exc}") from exc
            tasks.append(task)
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Write tasks to a JSON file with ISO-formatted deadlines."""
    records: list[dict[str, object]] = []
    for task in tasks:
        record = asdict(task)
        record["deadline"] = task.deadline.isoformat()
        records.append(record)
    Path(path).write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
