from datetime import date
from pathlib import Path

import pytest

from shared.contract import Task
from shared.study_planner.parse import parse_csv


@pytest.mark.parametrize(
    "content",
    ["", "\n\n", "title,importance,effort_h,deadline\n"],
    ids=["empty-file", "blank-lines", "header-only"],
)
def test_parse_csv_rejects_files_without_tasks(tmp_path: Path, content: str) -> None:
    path = tmp_path / "tasks.csv"
    path.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError, match="The task file is empty: no tasks found\\."):
        parse_csv(path)


def test_parse_csv_reads_tasks(tmp_path: Path) -> None:
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\nAssignment,4,1.5,2026-10-27\n",
        encoding="utf-8",
    )

    assert parse_csv(path) == [Task("Assignment", 4, 1.5, date(2026, 10, 27))]


def test_parse_csv_preserves_missing_file_error(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        parse_csv(tmp_path / "missing.csv")
