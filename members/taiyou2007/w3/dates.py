"""Parse absolute and relative task deadlines."""

import re
from datetime import date, timedelta

_WEEKDAYS = (
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
)


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date, tomorrow, 'in N days', or a weekday after today.

    Weekday names accept full names and three-letter abbreviations.
    Raise ValueError for unrecognized text or an invalid calendar date.
    """
    text = text.strip().lower()

    if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", text):
        return date.fromisoformat(text)

    if text == "tomorrow":
        return today + timedelta(days=1)

    relative = re.fullmatch(r"in ([0-9]+) days?", text)
    if relative:
        return today + timedelta(days=int(relative.group(1)))

    for weekday, name in enumerate(_WEEKDAYS):
        if text in (name, name[:3]):
            days_ahead = (weekday - today.weekday()) % 7 or 7
            return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date: {text!r}")
