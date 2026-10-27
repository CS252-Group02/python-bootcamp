import argparse
import math
import sys
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan tonight's tasks from a CSV file")
    parser.add_argument("path", type=Path, help="path to the tasks CSV")
    parser.add_argument("--hours", type=float, required=True, help="hours available tonight")
    # Tonight's plan uses the user's local calendar date.
    today: date = date.today()  # noqa: DTZ011
    parser.add_argument("--today", type=date.fromisoformat, default=today,
                        help="today's date as YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    if not math.isfinite(args.hours) or args.hours < 0:
        parser.error("--hours must be a finite, non-negative number")

    try:
        tasks = load_tasks(args.path)
    except FileNotFoundError:
        print(f"File not found: {args.path}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"Cannot load tasks: {exc}", file=sys.stderr)
        return 1

    tasks = sorted(tasks, key=lambda task: (
        task.days_left(args.today), task.deadline, -task.importance,
    ))

    remaining_h: float = args.hours
    index: int = 1

    print(f"Tonight ({args.hours:.1f} h):")
    for task in tasks:
        if remaining_h <= 0:
            break

        allocated_h: float = min(task.effort_h, remaining_h)
        if allocated_h <= 0:
            continue

        print(f" {index}. {task.title:.<20} {allocated_h:.1f} h")
        remaining_h -= allocated_h
        index += 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
