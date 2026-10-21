def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Error")
    sortScore = sorted(scores)
    n = len(scores)
    average = sum(scores) / n
    mid = n//2
    if n%2 == 1 : 
        median = sortScore[mid]
    else:
        median = (sortScore[mid - 1] + sortScore[mid]) / 2
    return {"min": min(scores), "max": max(scores), "mean": round(average, 2), "median": round(median, 2)}