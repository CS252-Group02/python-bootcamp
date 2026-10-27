"""Command-line study-plan renderer."""

import argparse
import logging
import sys
from datetime import date
from pathlib import Path

from members.Slampanda.w2.io_utils import load_tasks

LOGGER = logging.getLogger(__name__)


def _iso_date(value: str) -> date:
    """Convert an ISO-8601 date or report an argparse-friendly error."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be YYYY-MM-DD") from exc


def _render_plan(path: Path, hours: float, today: date) -> str:
    """Load tasks using the W2 reader and render the available study time."""
    tasks = load_tasks(path)
    active_tasks = [task for task in tasks if task.deadline >= today]
    ordered_tasks = sorted(active_tasks, key=lambda task: task.deadline)

    remaining = hours
    lines = [f"Tonight ({hours:.1f} h):"]
    for number, task in enumerate(ordered_tasks, start=1):
        if remaining <= 0:
            break
        allocated = min(task.estimate, remaining)
        lines.append(f"{number}. {task.title} ...... {allocated:.1f} h")
        remaining -= allocated
    return "\n".join(lines)


def main() -> None:
    """Parse arguments, then load and print a study plan."""
    parser = argparse.ArgumentParser(description="Render a study plan from a CSV file.")
    parser.add_argument("file", type=Path, help="CSV file containing tasks")
    parser.add_argument("--hours", required=True, type=float, help="available study hours")
    parser.add_argument("--today", type=_iso_date, default=date.today(), help="YYYY-MM-DD")
    args = parser.parse_args()

    if not args.file.is_file():
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        raise SystemExit(1)
    if args.hours < 0:
        parser.error("--hours must be zero or greater")

    LOGGER.debug("Rendering plan from %s for %s", args.file, args.today)
    try:
        print(_render_plan(args.file, args.hours, args.today))
    except (OSError, ValueError) as exc:
        print(f"Error: could not read {args.file}: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
