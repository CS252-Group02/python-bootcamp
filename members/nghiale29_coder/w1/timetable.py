"""W1-5: Group a course timetable by day of week."""


def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by the day they are scheduled.

    Args:
        schedule: A list of ``(course_code, day)`` tuples,
                  e.g. ``[("CSC10014", "Mon"), ("CSC10001", "Mon")]``.

    Returns:
        A dict mapping each day to an alphabetically sorted list of course codes.
        Returns an empty dict if *schedule* is empty.
    """
    result: dict[str, list[str]] = {}
    for course, day in schedule:
        result.setdefault(day, []).append(course)
    return {day: sorted(courses) for day, courses in result.items()}
