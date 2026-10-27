"""Log statistics and latency analysis utilities."""
import math
from collections import Counter, defaultdict


def analyse(
    pairs: list[tuple[str, float]],
) -> dict[str, Counter[str] | dict[str, float] | str | None]:
    """Analyse chat log pairs and compute route counts, p95 latencies, and slowest route."""
    counts: Counter[str] = Counter()
    grouped: dict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        grouped[route].append(latency)

    p95: dict[str, float] = {}
    for route, latencies in grouped.items():
        sorted_latencies = sorted(latencies)
        # Nearest-rank method: index ceil(0.95 * N) - 1
        idx = math.ceil(0.95 * len(sorted_latencies)) - 1
        p95[route] = sorted_latencies[idx]

    slowest: str | None = None
    if p95:
        slowest = max(p95, key=lambda k: p95[k])

    return {"counts": counts, "p95": p95, "slowest": slowest}
