from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Print tasks loaded from the sample CSV file."""
    repo_root = Path(__file__).resolve().parents[3]
    csv_path = repo_root / "samples" / "tasks.csv"
    tasks = load_tasks(csv_path)

    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()
