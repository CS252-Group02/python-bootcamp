from collections import Counter, defaultdict
from collections.abc import Iterable
from math import ceil


def analyse(pairs: Iterable[tuple[str, float]]) -> dict[str, object]:
    """Count requests and calculate each route's nearest-rank p95 latency."""
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95 = {
        route: sorted(values)[ceil(0.95 * len(values)) - 1]
        for route, values in latencies.items()
    }
    slowest = max(p95, key=p95.get) if p95 else None

    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
