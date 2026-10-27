"""Aggregate route latency statistics."""

from collections import Counter, defaultdict
from collections.abc import Iterable
from math import ceil
from typing import TypedDict


class LogStats(TypedDict):
    """The summary returned by :func:`analyse`."""

    counts: Counter[str]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: Iterable[tuple[str, float]]) -> LogStats:
    """Return request counts, nearest-rank p95s, and the slowest route."""
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)
    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95 = {
        route: sorted(values)[ceil(len(values) * 0.95) - 1]
        for route, values in latencies.items()
    }
    slowest = max(p95, key=p95.get) if p95 else None
    return {"counts": counts, "p95": p95, "slowest": slowest}
