"""W1-3: Thesis registration eligibility checker."""

CREDITS_REQUIRED = 120
GPA_REQUIRED = 2.0


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True if the student meets all thesis registration requirements.

    Args:
        credits: Total credits completed.
        gpa: Current GPA on a 4.0 scale.

    Returns:
        True if ``credits >= 120`` and ``gpa >= 2.0``, otherwise False.
    """
    return credits >= CREDITS_REQUIRED and gpa >= GPA_REQUIRED


def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of unmet requirements for thesis registration.

    Args:
        credits: Total credits completed.
        gpa: Current GPA on a 4.0 scale.

    Returns:
        A list of human-readable reason strings. Empty list means eligible.
    """
    reasons = []
    if credits < CREDITS_REQUIRED:
        shortfall = CREDITS_REQUIRED - credits
        reasons.append(f"need {shortfall} more credits")
    if gpa < GPA_REQUIRED:
        reasons.append(f"GPA too low (got {gpa}, need {GPA_REQUIRED})")
    return reasons
