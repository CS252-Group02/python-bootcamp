"""Plan tonight's study time from a tasks CSV file."""

import argparse
import sys
from datetime import date

from ..w2.io_utils import load_tasks
from ..w2.models import Task


def plan(tasks: list[Task], hours: float, today: date) -> list[tuple[Task, float]]:
    """Give hours to the most urgent tasks first, splitting the last one if needed.

    Urgency is importance divided by days left (at least one day).
    """
    ranked = sorted(
        tasks,
        key=lambda task: (-task.importance / max(task.days_left(today), 1), task.deadline),
    )

    blocks = []
    remaining = hours
    for task in ranked:
        if remaining <= 0:
            break
        spent = min(remaining, task.effort_h)
        blocks.append((task, spent))
        remaining -= spent
    return blocks


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return the process exit code."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", help="tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="study hours available")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        metavar="YYYY-MM-DD",
        help="reference date (default: today)",
    )
    args = parser.parse_args(argv)

    try:
        tasks = load_tasks(args.csv_path)
    except FileNotFoundError:
        print(f"error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    blocks = plan(tasks, args.hours, args.today)
    width = max((len(task.title) for task, _ in blocks), default=0) + 4

    print(f"Tonight ({args.hours:.1f} h):")
    for number, (task, spent) in enumerate(blocks, start=1):
        print(f" {number}. {(task.title + ' ').ljust(width, '.')} {spent:.1f} h")
    return 0


if __name__ == "__main__":
    sys.exit(main())
