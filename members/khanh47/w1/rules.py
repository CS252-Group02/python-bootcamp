def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether the credit and GPA requirements are met."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """List the thesis registration requirements that are not met."""
    reasons: list[str] = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append("need higher gpa (minimum 2.0)")
    return reasons
