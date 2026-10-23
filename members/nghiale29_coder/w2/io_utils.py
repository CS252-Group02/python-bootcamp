import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: Path | str) -> list[Task]:
    """Load tasks from a CSV file.

    Expected CSV header: title,importance,effort_h,deadline.
    Raises ValueError with line number if any row contains invalid data.
    """
    file_path = Path(path)
    tasks: list[Task] = []

    with file_path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            _ = next(reader)  # Read header (line 1)
        except StopIteration:
            return tasks

        for line_no, row in enumerate(reader, start=2):
            if not row:
                continue
            if len(row) != 4:
                raise ValueError(f"Invalid row at line {line_no}: expected 4 columns")
            title, raw_importance, raw_effort, raw_deadline = (col.strip() for col in row)
            try:
                importance = int(raw_importance)
                effort_h = float(raw_effort)
                deadline = date.fromisoformat(raw_deadline)
                task = Task(title=title, importance=importance, effort_h=effort_h, deadline=deadline)
            except Exception as exc:
                raise ValueError(f"Invalid row at line {line_no}: {exc}") from exc
            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: Path | str) -> None:
    """Save tasks to a JSON file with ISO formatted dates."""
    file_path = Path(path)
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
