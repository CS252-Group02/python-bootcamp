# AI-use log

## 2026-10-27 — T-W3: empty task file handling

- AI assistant: Codex.
- Assistance: added a clear English ValueError when the shared CSV parser finds
  no tasks, including empty files, blank lines, and header-only files; added
  regression tests for empty input, valid input, and missing files.
- Verification: all 10 shared planner tests passed; Ruff passed on the changed
  Python files, and git diff --check passed.
- Member review: the member must read and understand the implementation before
  submitting it. The future shared CLI should catch ValueError, display its
  message, and exit with status 1.

## conmefo — individual Python W2

- AI assistant: coding assistant in pi.
- Assistance: generated the Task model, CSV/JSON helpers, feasibility exception,
  package entry point, and original peer tests for khanh47's W1 code; created
  the branch, commit, and pull request at the member's request.
- Verification performed by the assistant: Ruff on `members/conmefo`, the three
  instructor W2 tests, peer tests, required W1 translation test, and a package
  execution smoke test. All passed (18 pytest cases).
- Member review: the member still needs to read and understand the generated
  implementation; automated checks are not a substitute for personal review.

## conmefo — individual Python W3

- AI assistant: Claude Code.
- Assistance: wrote W3-1 `parse_due`, W3-2 `analyse`, and the W3-3 study planner
  CLI in `members/conmefo/w3/`; for W3-4 added type hints and docstrings to the
  member's W1 and W2 code and removed a leftover `print` call from `grades.py`.
- Verification performed by the assistant: Ruff on `members/conmefo`, the
  instructor W1-4, W2 and W3 tests, and the member's W2 peer tests. All passed.
- Member review: the member still needs to read and understand the generated
  code; automated checks are not a substitute for personal review.
