"""Week 1 thesis registration rules."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True when a student has at least 120 credits and a GPA of 2.0."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """List what a student still needs before registering a thesis."""
    reasons: list[str] = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append(f"need GPA of at least 2.0 (current: {gpa:g})")
    return reasons
