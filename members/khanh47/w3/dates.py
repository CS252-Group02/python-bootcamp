import re
from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tues": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thur": 3,
    "thurs": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date or a supported relative date expression."""
    value = text.strip().lower()

    if value == "tomorrow":
        return today + timedelta(days=1)

    days_match = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if days_match:
        return today + timedelta(days=int(days_match.group(1)))

    if value in _WEEKDAYS:
        days_ahead = (_WEEKDAYS[value] - today.weekday()) % 7
        return today + timedelta(days=days_ahead or 7)

    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"unknown due date: {text}") from exc
