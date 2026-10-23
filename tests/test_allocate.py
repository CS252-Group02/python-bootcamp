from dataclasses import asdict
from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.allocate import allocate


def task(title, effort_h):
    return Task(title, 3, effort_h, date(2026, 10, 30))


def test_allocation_follows_input_order_and_partially_fills_last_task():
    tasks = [task("first", 2), task("second", 4), task("third", 1)]
    assert allocate(tasks, 3.5) == [Block(tasks[0], 2), Block(tasks[1], 1.5)]


def test_exact_budget_completes_all_tasks():
    tasks = [task("first", 2), task("second", 1)]
    assert allocate(tasks, 3) == [Block(tasks[0], 2), Block(tasks[1], 1)]


def test_excess_budget_does_not_overallocate():
    tasks = [task("first", 1.5)]
    assert allocate(tasks, 10) == [Block(tasks[0], 1.5)]


def test_empty_tasks_and_zero_budget():
    assert allocate([], 5) == []
    assert allocate([task("first", 2)], 0) == []


def test_zero_effort_tasks_are_skipped():
    tasks = [task("done", 0), task("next", 2)]
    assert allocate(tasks, 1) == [Block(tasks[1], 1)]


def test_input_is_not_modified_and_blocks_reference_original_tasks():
    tasks = [task("first", 2), task("second", 4)]
    before = [asdict(item) for item in tasks]
    blocks = allocate(tasks, 1)
    assert [asdict(item) for item in tasks] == before
    assert blocks[0].task is tasks[0]


@pytest.mark.parametrize("hours", [-1, float("nan"), float("inf"), -float("inf")])
def test_invalid_budget_is_rejected(hours):
    with pytest.raises(ValueError, match="hours"):
        allocate([], hours)


@pytest.mark.parametrize("effort", [-1, float("nan"), float("inf"), -float("inf")])
def test_invalid_effort_is_rejected_even_after_budget_would_run_out(effort):
    with pytest.raises(ValueError, match="effort_h"):
        allocate([task("valid", 2), task("invalid", effort)], 1)
