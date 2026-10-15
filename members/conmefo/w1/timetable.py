def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    grouped = {}
    for course, day in courses:
        grouped.setdefault(day, []).append(course)

    return {day: sorted(day_courses) for day, day_courses in grouped.items()}
