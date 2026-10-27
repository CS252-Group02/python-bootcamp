"""CLI entry point for running the Week 2 package."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load sample tasks and print them to console."""
    sample_path = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    for task in load_tasks(str(sample_path)):
        print(task)


if __name__ == "__main__":
    main()
