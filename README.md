# python-bootcamp

CI checks the PR author's member folder on opened, updated, and reopened pull
requests. It runs Ruff, checks for conflict markers, runs the assigned W1-4
translation test, and runs all week 2 and week 3 tests.

Week 3 checks `w3/dates.py`, `w3/log_stats.py`, and `w3/cli.py` for every member.
Missing or unfinished week 3 homework fails CI.

Run week 3 tests from the repository root (replace `YOUR_MEMBER_FOLDER`):

```bash
python -m pytest -q tests/test_w3.py --member YOUR_MEMBER_FOLDER
```
