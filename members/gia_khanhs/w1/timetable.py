from collections import defaultdict


def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort each day's course names."""
    res: dict[str, list[str]] = defaultdict(list[str])

    for course, day in timetable:
        res[day].append(course)

    for day, courses in res.items():
        res[day] = sorted(courses)

    return dict(res)
