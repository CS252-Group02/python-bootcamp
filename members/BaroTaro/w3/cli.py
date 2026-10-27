"""Command-line study planner tool."""

import argparse
import sys
from datetime import date
from pathlib import Path

from members.BaroTaro.w2.io_utils import load_tasks
from members.BaroTaro.w2.models import Task


def schedule_tasks(
    tasks: list[Task], hours: float, today: date
) -> list[tuple[Task, float]]:
    """Prioritise tasks and allocate available study hours."""
    # Higher urgency = importance / max(days_left, 1)
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (t.importance / max(t.days_left(today), 1), t.importance),
        reverse=True,
    )

    allocated: list[tuple[Task, float]] = []
    remaining = hours
    for task in sorted_tasks:
        if remaining <= 0:
            break
        alloc_h = min(remaining, task.effort_h)
        allocated.append((task, alloc_h))
        remaining -= alloc_h

    return allocated


def main(argv: list[str] | None = None) -> int:
    """Entry point for the study planner CLI."""
    parser = argparse.ArgumentParser(
        description="Schedule study tasks based on urgency and available hours."
    )
    parser.add_argument("csv_file", type=str, help="Path to CSV tasks file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Total hours available"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date in YYYY-MM-DD format (default: today)",
    )

    args = parser.parse_args(argv)

    csv_path = Path(args.csv_file)
    if not csv_path.is_file():
        sys.stderr.write(f"Error: file not found: {args.csv_file}\n")
        return 1

    if args.today:
        try:
            today_date = date.fromisoformat(args.today)
        except ValueError as err:
            sys.stderr.write(f"Error: invalid date format for --today: {err}\n")
            return 1
    else:
        today_date = date.today()

    try:
        tasks = load_tasks(str(csv_path))
    except (OSError, ValueError) as err:
        sys.stderr.write(f"Error loading tasks: {err}\n")
        return 1

    allocated = schedule_tasks(tasks, args.hours, today_date)

    print(f"Tonight ({args.hours:.1f} h):")
    for idx, (task, alloc_h) in enumerate(allocated, start=1):
        prefix = f" {idx}. {task.title} "
        dotted = prefix.ljust(21, ".")
        print(f"{dotted} {alloc_h:.1f} h")

    return 0


if __name__ == "__main__":
    sys.exit(main())
