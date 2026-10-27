"""Grade statistics and calculation utilities."""


def summary(scores: list[float]) -> dict[str, float]:
    """Calculate min, max, mean, and median from a list of scores."""
    if not scores:
        raise ValueError("scores list cannot be empty")

    n = len(scores)
    sorted_scores = sorted(scores)

    mid = n // 2
    if n % 2 == 1:
        med = sorted_scores[mid]
    else:
        med = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(sum(scores) / n, 2),
        "median": round(med, 2),
    }
