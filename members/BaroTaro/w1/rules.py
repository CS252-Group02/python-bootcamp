def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits, gpa) -> list[str]:
    reasons: list[str] = []

    if credits < 120 :
        credit_reason = f"need {120 - credits} more credits"
        reasons.append(credit_reason)
    if gpa < 2.0 :
        diff = round(2.0 - gpa)
        gpa_reason = f"need {diff} higher GPA"
        reasons.append(gpa_reason)
        
    return reasons