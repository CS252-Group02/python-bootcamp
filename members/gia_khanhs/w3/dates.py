from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    text = text.strip()

    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    text = text.lower()

    if text == "tomorrow":
        return today + timedelta(days=1)

    words: list[str] = text.split()
    if (len(words) == 3 and words[0] == "in"
            and words[2] in ["day", "days"] and words[1].isdecimal()):
        n_days: int = int(words[1])
        return today + timedelta(days=n_days)

    weekdays: list[str] = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    full_weekdays: list[str] = [
        "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
    ]

    if text in full_weekdays:
        text = weekdays[full_weekdays.index(text)]

    if text in weekdays:
        n_days = (weekdays.index(text) - today.weekday()) % 7
        if n_days == 0:
            n_days = 7

        return today + timedelta(days=n_days)

    raise ValueError(f"unknown due date: {text}")
