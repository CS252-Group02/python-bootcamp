from pathlib import Path

from .io_utils import load_tasks

SAMPLE_TASKS = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> None:
    """Load and print the sample tasks."""
    for task in load_tasks(SAMPLE_TASKS):
        print(task)

if __name__ == "__main__":
    main()
