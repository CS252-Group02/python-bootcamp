import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Counter[str] | dict[str, float] | str | None]:
    """Return route counts, nearest-rank p95 values, and the slowest route."""
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)
    p95: dict[str, float] = {}

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    for route, values in latencies.items():
        values = sorted(values)
        # Nearest rank: the first value covering at least 95% of requests.
        index: int = math.ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    slowest = max(p95, key=lambda route: p95[route], default=None)

    return {"counts": counts, "p95": p95, "slowest": slowest}
