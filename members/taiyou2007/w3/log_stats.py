"""Summarize request counts and latency by route."""

from collections import Counter, defaultdict
from typing import TypedDict


class LogStats(TypedDict):
    """Describe per-route counts, percentiles, and the slowest route."""

    counts: Counter[str]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: list[tuple[str, float]]) -> LogStats:
    """Return request counts, nearest-rank p95 latencies, and the slowest route.

    Ties for slowest use the route encountered first. Empty input returns
    empty counts and percentiles, with None as the slowest route.
    """
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95: dict[str, float] = {}
    for route, values in latencies.items():
        ordered = sorted(values)
        rank = (95 * len(ordered) + 99) // 100
        p95[route] = ordered[rank - 1]

    slowest = max(p95, key=p95.__getitem__, default=None)
    return {"counts": counts, "p95": p95, "slowest": slowest}
