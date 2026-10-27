"""Summarise chatbot latency logs per route."""

import math
from collections import defaultdict


def p95(latencies: list[float]) -> float:
    """Return the 95th percentile using the nearest-rank method."""
    ordered = sorted(latencies)
    rank = math.ceil(0.95 * len(ordered))
    return ordered[rank - 1]


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Count requests per route, find each route's p95 and the slowest route.

    ``pairs`` holds ``(route, latency_ms)`` tuples. The slowest route is the
    one with the highest p95; it is ``None`` when there are no pairs.
    """
    by_route: dict[str, list[float]] = defaultdict(list)
    for route, latency in pairs:
        by_route[route].append(latency)

    counts = {route: len(latencies) for route, latencies in by_route.items()}
    p95s = {route: p95(latencies) for route, latencies in by_route.items()}
    slowest = max(p95s, key=p95s.get) if p95s else None

    return {"counts": counts, "p95": p95s, "slowest": slowest}
