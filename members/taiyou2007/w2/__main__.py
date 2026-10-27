from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load and print the repository sample tasks."""
    repo_root = Path(__file__).resolve().parents[3]
    sample_path = repo_root / "samples" / "tasks.csv"

    tasks = load_tasks(sample_path)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
