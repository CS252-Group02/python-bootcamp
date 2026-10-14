import math


def summary(scores: list[float]) -> dict[str, float]:
    res: dict[str, float] = {}
    n: int = len(scores)

    if n == 0:
        raise ValueError("LOL SUMMARY WHAT FROM THIS KINDA LIST?")

    scores = sorted(scores)

    res["min"] = min(scores)
    res["max"] = max(scores)
    res["mean"] = sum(scores) / n
    res["median"] = scores[math.floor((n - 1) / 2)] + scores[math.ceil((n - 1) / 2)]
    res["median"] = res["median"] / 2

    for key, val in res.items():
        res[key] = round(val, 2)

    return res

print(summary([7.5, 9, 6, 8]))

# LOL