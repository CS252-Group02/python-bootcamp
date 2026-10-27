"""Test the shared planner from a sample CSV through rendered output."""

from datetime import date
from pathlib import Path

import pytest

from shared.study_planner.allocate import allocate
from shared.study_planner.errors import InfeasiblePlan
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

SAMPLE = Path(__file__).resolve().parents[1] / "samples" / "study_planner_e2e.csv"
TODAY = date(2026, 10, 26)


@pytest.mark.parametrize(
    ("hours", "expected_output"),
    [
        pytest.param(
            2.0,
            "Study plan:\n"
            "- Assignment: 1.50 h\n"
            "- DS exam: 0.50 h\n"
            "Total: 2.00 h",
            id="partial-plan",
        ),
        pytest.param(
            10.0,
            "Study plan:\n"
            "- Assignment: 1.50 h\n"
            "- DS exam: 6.00 h\n"
            "- Reading: 2.00 h\n"
            "Total: 9.50 h",
            id="all-tasks-fit",
        ),
    ],
)
def test_csv_to_rendered_plan(hours: float, expected_output: str) -> None:
    """Parse, prioritise, allocate, and render real tasks without mocks."""
    tasks = parse_csv(SAMPLE)
    prioritised = prioritise(tasks, TODAY)
    blocks = allocate(prioritised, hours)
    output = render(blocks)

    # The CSV is deliberately unordered, so the pipeline must reorder it.
    assert [task.title for task in prioritised] == ["Assignment", "DS exam", "Reading"]
    assert sum(block.hours for block in blocks) <= hours
    assert all(0 < block.hours <= block.task.effort_h for block in blocks)
    assert output == expected_output


def test_csv_with_zero_hours_is_infeasible() -> None:
    """A zero-hour budget stops the pipeline with InfeasiblePlan."""
    prioritised = prioritise(parse_csv(SAMPLE), TODAY)

    with pytest.raises(InfeasiblePlan):
        allocate(prioritised, 0.0)
