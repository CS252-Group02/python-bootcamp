"""Print the sample tasks: python -m members.conmefo.w2."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load samples/tasks.csv and print each task."""
    repo_root = Path(__file__).resolve().parents[3]
    tasks = load_tasks(repo_root / "samples" / "tasks.csv")
    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
