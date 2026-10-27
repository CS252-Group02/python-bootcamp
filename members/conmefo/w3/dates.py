"""Parse human-friendly due dates."""

import re
from datetime import date, timedelta

WEEKDAYS = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")


def _weekday_index(name: str) -> int | None:
    """Return 0-6 for a full or three-letter weekday name, otherwise None."""
    for index, weekday in enumerate(WEEKDAYS):
        if name in (weekday, weekday[:3]):
            return index
    return None


def parse_due(text: str, today: date) -> date:
    """Turn an ISO date, "tomorrow", "in N days" or a weekday into a date.

    A weekday means its next occurrence, so today's weekday is a week ahead.
    """
    cleaned = text.strip().lower()

    try:
        return date.fromisoformat(cleaned)
    except ValueError:
        pass

    if cleaned == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in (\d+) days?", cleaned)
    if match:
        return today + timedelta(days=int(match.group(1)))

    target = _weekday_index(cleaned)
    if target is not None:
        days_ahead = (target - today.weekday() - 1) % 7 + 1
        return today + timedelta(days=days_ahead)

    raise ValueError(f"cannot parse due date: {text!r}")
