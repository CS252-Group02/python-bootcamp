def summary(scores: list[float]) -> dict[str, float]:
    """Return basic statistics for a non-empty list of scores."""
    if not scores:
        raise ValueError("scores must not be empty")
    ordered = sorted(scores)
    n = len(ordered)
    mean = round(sum(ordered) / n, 2)
    mid = n // 2
    if n % 2 == 1:
        median = round(float(ordered[mid]), 2)
    else:
        median = round((ordered[mid - 1] + ordered[mid]) / 2, 2)
    return {"min": ordered[0], "max": ordered[-1], "mean": mean, "median": median}
