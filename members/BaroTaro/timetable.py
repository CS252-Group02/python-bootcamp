def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:

    result: dict[str, list[str]] = {}

    for course, day in schedule:
        result.setdefault(day, []).append(course)

    for day in result:
        result[day].sort()

    return result