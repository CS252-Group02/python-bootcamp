# Study Planner

## Overview

The Study Planner reads tasks from a CSV file, ranks them by importance and
deadline, and assigns study time within an available hours budget. It prints a
readable plan to the terminal.

## Project Structure

Paths below are relative to the repository root:

| File | Responsibility |
| --- | --- |
| `shared/contract.py` | Defines `Task` (title, importance, effort, deadline) and `Block` (task and allocated hours). |
| `shared/study_planner/__main__.py` | Parses CLI arguments and connects the four pipeline stages. |
| `shared/study_planner/parse.py` | Reads a UTF-8 CSV file into tasks. |
| `shared/study_planner/prioritise.py` | Sorts tasks by priority. |
| `shared/study_planner/allocate.py` | Greedily assigns hours to tasks in priority order. |
| `shared/study_planner/render.py` | Formats study blocks and total hours as text. |
| `samples/tasks.csv` | Provides sample input for the CLI. |
| `tests/test_study_planner_e2e.py` | Tests the four-stage pipeline using `samples/study_planner_e2e.csv`. |

## Requirements & Setup

Use Python 3.10 or newer, as the code uses union type syntax (`str | None`).
The repository CI uses Python 3.12. The planner itself uses only the Python
standard library.

From the repository root, optionally create and activate a virtual environment
(commands below use a Unix-like shell):

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the repository's development dependencies to run tests or lint checks:

```bash
python -m pip install -r requirements.txt
```

`requirements.txt` lists `pytest` and `ruff`.

## CSV Input Format

Use a UTF-8 CSV file with a header containing these column names:

| Column | Type | Meaning |
| --- | --- | --- |
| `title` | String | Task name displayed in the plan. |
| `importance` | Integer, 1–5 | Importance rating; higher values increase priority. |
| `effort_h` | Float | Estimated hours needed to complete the task. |
| `deadline` | ISO date (`YYYY-MM-DD`) | Due date used to calculate urgency. |

For example, `samples/tasks.csv` contains:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

Supply positive, finite effort values and a finite, non-negative hours budget.
The implementation validates the importance range but does not validate effort
or budget ranges. Missing columns, invalid numbers or dates, and file errors
raise exceptions; the CLI does not convert these into friendly error messages.

## Usage

Run the module from the repository root:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
```

| Argument | Required? | Description |
| --- | --- | --- |
| `csv_path` | Yes | Positional path to the task CSV file. |
| `--hours HOURS` | Yes | Available study hours, parsed as a float. |
| `--today TODAY` | No | Reference date in `YYYY-MM-DD` format; defaults to the local current date. |
| `-h`, `--help` | No | Shows CLI help and exits. |

To use the current date, omit `--today`:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2
```

## How It Works

The CLI runs `parse_csv → prioritise → allocate → render`:

1. **Parse:** Convert CSV rows into `Task` objects.
2. **Prioritise:** Sort by `importance / (days_left + 0.1)`, highest first.
   Days remaining are clamped to zero, so overdue tasks and tasks due today
   both use zero days left. Equal scores preserve CSV order.
3. **Allocate:** Assign each task the smaller of its estimated effort and the
   remaining budget. Stop when the budget is exhausted. A task can receive a
   partial allocation; unused hours remain if all tasks fit.
4. **Render:** Convert the allocated blocks into terminal output.

The CLI does not filter out overdue tasks or split blocks into calendar slots.

## Output Format

The reference command above prints:

```text
Study plan:
- Assignment: 1.50 h
- DS exam: 0.50 h
Total: 2.00 h
```

Each block shows a task title and its allocated hours, in priority order. Hours
and their total are displayed to two decimal places. The output is printed to
standard output; no plan file is created.

When no blocks are allocated (for example, with `--hours 0`), the output is:

```text
Study plan:
No study blocks.
Total: 0.00 h
```

## Testing

After installing `requirements.txt`, run the existing pipeline tests from the
repository root:

```bash
python -m pytest -q tests/test_study_planner_e2e.py
```

These cover partial allocation, a budget large enough for all tasks, and zero
hours. They call the four stages directly rather than invoking the CLI.

The prioritisation module also contains a test that can be run explicitly:

```bash
python -m pytest -q shared/study_planner/prioritise.py
```
