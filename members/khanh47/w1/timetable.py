def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course names by day and sort each day's courses."""
    grouped: dict[str, list[str]] = {}
    for course, day in pairs:
        grouped.setdefault(day, []).append(course)
    return {day: sorted(courses) for day, courses in grouped.items()}
