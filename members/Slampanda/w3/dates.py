"""Helpers for parsing the due-date formats accepted by the planner."""

import re
from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}
_IN_DAYS = re.compile(r"in (\d+) days?")


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date, relative date, or weekday after ``today``.

    A weekday always refers to its next occurrence, so ``"Tue"`` on a
    Tuesday is one week later.
    """
    value = text.strip().lower()
    if value == "tomorrow":
        return today + timedelta(days=1)

    if match := _IN_DAYS.fullmatch(value):
        return today + timedelta(days=int(match.group(1)))

    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    weekday = _WEEKDAYS.get(value)
    if weekday is not None:
        days_ahead = (weekday - today.weekday()) % 7 or 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: {text}")
