import argparse
from datetime import date
from pathlib import Path

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

    for task in tasks:
        print(task)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
