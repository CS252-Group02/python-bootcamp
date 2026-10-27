"""Build a study plan from a tasks CSV file."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise

from ..w2.io_utils import load_tasks


def _hours(text: str) -> float:
    """Require a finite, nonnegative time budget."""
    try:
        value = float(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("hours must be a number") from exc
    if not math.isfinite(value) or value < 0:
        raise argparse.ArgumentTypeError("hours must be finite and nonnegative")
    return value


def main() -> int:
    """Read tasks, prioritize them, and print blocks within the time budget."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="tasks CSV file")
    parser.add_argument("--hours", type=_hours, required=True, help="available study hours")
    parser.add_argument(
        "--today", type=date.fromisoformat, default=date.today(),
        metavar="YYYY-MM-DD", help="reference date (default: today)",
    )
    args = parser.parse_args()

    try:
        tasks = load_tasks(args.path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.path}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if any(not math.isfinite(task.effort_h) or task.effort_h < 0 for task in tasks):
        print("Error: task effort must be finite and nonnegative", file=sys.stderr)
        return 1

    shared_tasks = [
        Task(task.title, task.importance, task.effort_h, task.deadline)
        for task in tasks if task.effort_h > 0
    ]
    blocks = allocate(prioritise(shared_tasks, args.today), args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    width = max((len(block.task.title) for block in blocks), default=0) + 6
    for index, block in enumerate(blocks, start=1):
        title = f"{block.task.title} ".ljust(width, ".")
        print(f" {index}. {title} {block.hours:g} h")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
