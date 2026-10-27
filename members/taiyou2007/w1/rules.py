
def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether both thesis registration thresholds are met."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Describe unmet credit and GPA requirements."""
    reasons = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append(f"need {2.0 - gpa:.2f} more GPA")

    return reasons

