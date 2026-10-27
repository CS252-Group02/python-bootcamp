"""Date parsing utilities for due date strings."""
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a due date from string representation into a date object.

    Accepts ISO dates ('YYYY-MM-DD'), relative terms ('tomorrow', 'in N days', 'in 1 day'),
    and weekday names ('Mon', 'Monday', 'Fri', etc.) targeting the next occurrence.
    Raises ValueError for unrecognized formats.
    """
    cleaned = text.strip()

    # 1. ISO format YYYY-MM-DD
    try:
        return date.fromisoformat(cleaned)
    except ValueError:
        pass

    lowered = cleaned.lower()

    # 2. 'tomorrow'
    if lowered == "tomorrow":
        return today + timedelta(days=1)

    # 3. 'in N days' or 'in N day'
    tokens = lowered.split()
    if (
        len(tokens) == 3
        and tokens[0] == "in"
        and tokens[2] in ("day", "days")
        and tokens[1].isdigit()
    ):
        return today + timedelta(days=int(tokens[1]))

    # 4. Weekday names
    weekdays_short = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    weekdays_full = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    target_idx = None
    if lowered in weekdays_short:
        target_idx = weekdays_short.index(lowered)
    elif lowered in weekdays_full:
        target_idx = weekdays_full.index(lowered)

    if target_idx is not None:
        delta_days = (target_idx - today.weekday()) % 7
        if delta_days == 0:
            delta_days = 7  # Must be next occurrence, not today
        return today + timedelta(days=delta_days)

    raise ValueError(f"Unable to parse due date: {text}")
