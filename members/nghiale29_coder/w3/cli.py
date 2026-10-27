"""Command-line tool to plan study tasks for tonight."""
import argparse
import sys
from datetime import UTC, date, datetime
from pathlib import Path

from members.nghiale29_coder.w2.io_utils import load_tasks


def main() -> int:
    """Run the study planner CLI."""
    parser = argparse.ArgumentParser(description="Plan tonight's tasks from a CSV file.")
    parser.add_argument("path", type=Path, help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Hours available tonight")

    default_today = datetime.now(tz=UTC).astimezone().date()
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=default_today,
        help="Today's date in YYYY-MM-DD format (default: today)",
    )

    args = parser.parse_args()

    if args.hours < 0:
        print("Hours must be non-negative.", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(args.path)
    except FileNotFoundError:
        print(f"File not found: {args.path}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"Error loading tasks: {exc}", file=sys.stderr)
        return 1

    # Prioritise tasks: earliest days_left, earliest deadline, highest importance
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (t.days_left(args.today), t.deadline, -t.importance),
    )

    remaining_hours = args.hours
    print(f"Tonight ({args.hours:.1f} h):")
    idx = 1
    for task in sorted_tasks:
        if remaining_hours <= 0:
            break
        allocated = min(task.effort_h, remaining_hours)
        if allocated <= 0:
            continue
        print(f" {idx}. {task.title:.<20} {allocated:.1f} h")
        remaining_hours -= allocated
        idx += 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
