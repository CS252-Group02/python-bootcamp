from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load sample tasks CSV and print summary."""
    sample_csv = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    tasks = load_tasks(sample_csv)
    print(f"Loaded {len(tasks)} tasks from {sample_csv.name}:")
    for idx, t in enumerate(tasks, start=1):
        print(f"  {idx}. {t.title} [Importance: {t.importance}, Effort: {t.effort_h}h, Deadline: {t.deadline}]")


if __name__ == "__main__":
    main()
