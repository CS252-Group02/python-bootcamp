import csv
import json
from dataclasses import asdict, is_dataclass
from datetime import date
from pathlib import Path


try:
    from .models import Task
except (ImportError, ValueError):
    try:
        from w2.models import Task
    except ImportError:
        from models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks: list[Task] = []

    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)
        for line_num, row in enumerate(reader, start=2):
            if not row or not any(field.strip() for field in row):
                continue

            try:
                if len(row) != 4:
                    raise ValueError(f"Expected 4 columns, got {len(row)}")

                title = row[0].strip()
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())
                task = Task(title, importance, effort_h, deadline)
                tasks.append(task)

            except Exception as exc:
                raise ValueError(f"Invalid row at line {line_num}: {exc}") from exc
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    data = []
    for t in tasks:
        if is_dataclass(t):
            item = asdict(t)
        else:
            item = dict(t.__dict__)

        if isinstance(item.get("deadline"), date):
            item["deadline"] = item["deadline"].isoformat()

        data.append(item)

    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
