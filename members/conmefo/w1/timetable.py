"""Week 1 timetable grouping."""


def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group (course, day) pairs by day, with each day's courses sorted."""
    grouped: dict[str, list[str]] = {}
    for course, day in courses:
        grouped.setdefault(day, []).append(course)

    return {day: sorted(day_courses) for day, day_courses in grouped.items()}
