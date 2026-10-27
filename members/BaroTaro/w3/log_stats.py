"""Chat log analysis utilities for latency profiling and route statistics."""

import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, int | float]]) -> dict[str, Any]:
    """Analyse route latencies from a list of (route, latency_ms) pairs.

    Returns:
        dict containing:
        - 'counts': number of requests per route (dict[str, int])
        - 'p95': 95th percentile latency per route (dict[str, int | float])
        - 'slowest': route with the highest p95 latency (str | None)
    """
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}

    counts = dict(Counter(route for route, _ in pairs))
    latencies_by_route: dict[str, list[int | float]] = defaultdict(list)

    for route, latency in pairs:
        latencies_by_route[route].append(latency)

    p95: dict[str, int | float] = {}
    for route, lats in latencies_by_route.items():
        sorted_lats = sorted(lats)
        n = len(sorted_lats)
        # 95th percentile using nearest-rank method
        idx = max(0, math.ceil(0.95 * n) - 1)
        p95[route] = sorted_lats[idx]

    slowest = max(p95, key=lambda route: p95[route]) if p95 else None

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
