import argparse
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise

from ..w2.io_utils import load_tasks


def main() -> int:
    """Run the study planner for a task CSV and available study hours."""
    parser = argparse.ArgumentParser(description="Plan study time from a task CSV.")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()

    try:
        tasks = load_tasks(args.csv_path)
    except FileNotFoundError:
        parser.exit(1, f"Error: file not found: {args.csv_path}\n")

    blocks = allocate(prioritise(tasks, args.today), args.hours)
    print(f"Tonight ({args.hours:.1f} h):")
    for index, block in enumerate(blocks, start=1):
        print(f"  {index}. {block.task.title} ...... {block.hours:g} h")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
