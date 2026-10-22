from pathlib import Path
from .io_utils import load_tasks
from .models import Task


def main():
    repo_root = Path(__file__).resolve().parents[3]
    csv_path = repo_root / "samples" / "tasks.csv"
    tasks = load_tasks(csv_path)

    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()
