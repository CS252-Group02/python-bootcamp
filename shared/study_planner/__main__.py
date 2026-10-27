"""CLI entrypoint for the shared study planner package."""

import argparse
import sys
from datetime import date
from os import PathLike

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def run_pipeline(csv_path: str | PathLike[str], hours: float, today: date) -> str:
    """Execute the study planner pipeline end-to-end and return rendered plan."""
    tasks = parse_csv(csv_path)
    prioritised = prioritise(tasks, today)
    blocks = allocate(prioritised, hours)
    return render(blocks)


def main(argv: list[str] | None = None) -> int:
    """Parse command-line arguments and run the study planner."""
    parser = argparse.ArgumentParser(
        prog="python -m shared.study_planner",
        description="Generate an allocated study plan from a CSV file of tasks.",
    )
    parser.add_argument("csv_path", type=str, help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Available study hours"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date (YYYY-MM-DD), defaults to today",
    )

    args = parser.parse_args(argv)

    today = date.fromisoformat(args.today) if args.today else date.today()
    plan_output = run_pipeline(args.csv_path, args.hours, today)
    print(plan_output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
