"""Academic rule verification utilities."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check if student satisfies requirements to register thesis."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of missing requirements for registering thesis."""
    reasons: list[str] = []

    if credits < 120:
        credit_reason = f"need {120 - credits} more credits"
        reasons.append(credit_reason)
    if gpa < 2.0:
        diff = round(2.0 - gpa)
        gpa_reason = f"need {diff} higher GPA"
        reasons.append(gpa_reason)

    return reasons
