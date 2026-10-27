def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether credits and GPA meet the thesis requirements."""
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    """List the thesis requirements the student has not met."""
    missings: list[str] = []

    if not credits >= 120:
        missings.append(f"need {120 - credits} more credits")

    if not gpa >= 2.0:
        missings.append(f"yo u cannot do a thesis with a gpa of {gpa}, either improve it or register for Grab instead!")

    return missings
