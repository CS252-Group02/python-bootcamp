"""Course timetable grouping utilities."""


def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day of the week and sort course codes alphabetically."""
    result: dict[str, list[str]] = {}

    for course, day in schedule:
        result.setdefault(day, []).append(course)

    for courses in result.values():
        courses.sort()

    return result
