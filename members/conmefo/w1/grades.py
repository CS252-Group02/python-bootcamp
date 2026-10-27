"""Week 1 grade statistics."""


def summary(scores: list[float]) -> dict[str, float]:
    """Return the min, max, mean and median of the scores, rounded to 2 places."""
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    count = len(ordered)
    middle = count // 2

    if count % 2 == 0:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    else:
        median = ordered[middle]

    return {
        "min": ordered[0],
        "max": ordered[-1],
        "mean": round(sum(scores) / count, 2),
        "median": round(median, 2),
    }
