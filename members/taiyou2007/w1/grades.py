
def summary(scores: list[float]) -> dict[str, float]:
    """Return score statistics; reject empty input with ValueError."""
    if not scores:
        raise ValueError("Scores list cannot be empty")

    sorted_scores = sorted(scores)
    n = len(scores)

    minimum = min(scores)
    maximum = max(scores)
    mean = round(sum(scores) / n, 2)

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": round(median, 2)
    }
