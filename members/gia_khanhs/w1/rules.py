def can_register_thesis(credits: int, gpa: float) -> bool:
    if credits >= 120 and gpa >= 2.0:
        return True

    return False

    raise NotImplemented

def  missing(credits, gpa) -> list[str]:
    missings: list[str] = []

    if not credits >= 120:
        missings.append(f"need {120 - credits} more credits")

    if not gpa >= 2.0:
        missings.append(f"yo u cannot do a thesis with a gpa of {gpa}, either improve it or register for Grab instead!")

    return missings

    raise NotImplemented