"""Date parsing utilities for deadlines and study plans."""

import re
from datetime import date, timedelta

WEEKDAYS: dict[str, int] = {
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
    """Parse a human-readable or ISO date string into a date object.

    Accepts:
    - ISO 8601 string: 'YYYY-MM-DD'
    - 'tomorrow' (case-insensitive)
    - 'in N days' / 'in N day'
    - Weekday names (e.g. 'Fri', 'Tue', 'Tuesday') mapping to the next occurrence.

    Raises:
        ValueError: If text cannot be parsed into a supported date.
    """
    cleaned = text.strip()
    lower = cleaned.lower()

    if not cleaned:
        raise ValueError("Date string cannot be empty")

    # 1. Try ISO date format YYYY-MM-DD
    try:
        return date.fromisoformat(cleaned)
    except ValueError:
        pass

    # 2. 'tomorrow'
    if lower == "tomorrow":
        return today + timedelta(days=1)

    # 3. 'in N day(s)'
    in_days_match = re.fullmatch(r"in\s+(\d+)\s+days?", lower)
    if in_days_match:
        days_offset = int(in_days_match.group(1))
        return today + timedelta(days=days_offset)

    # 4. Weekday name (strictly next occurrence, 1 to 7 days ahead)
    if lower in WEEKDAYS:
        target_weekday = WEEKDAYS[lower]
        days_ahead = (target_weekday - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown or unsupported date expression: {text!r}")
