"""W1-1: Grade summary — returns statistics for a list of scores."""


def summary(scores: list[float]) -> dict:
    """Return min, max, mean, and median of *scores*.

    Args:
        scores: A non-empty list of numeric scores.

    Returns:
        A dict with keys ``min``, ``max``, ``mean``, and ``median``.
        ``mean`` and ``median`` are rounded to 2 decimal places.

    Raises:
        ValueError: If *scores* is empty.
    """
    if not scores:
        raise ValueError("scores list must not be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    minimum = sorted_scores[0]
    maximum = sorted_scores[-1]
    mean = round(sum(sorted_scores) / n, 2)

    mid = n // 2
    if n % 2 == 1:
        median = sorted_scores[mid]
    else:
        median = round((sorted_scores[mid - 1] + sorted_scores[mid]) / 2, 2)

    return {"min": minimum, "max": maximum, "mean": mean, "median": median}
