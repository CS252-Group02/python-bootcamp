"""W1-2: Word counter utilities for text analysis."""

import re
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in *text*.

    Words are lowercased and punctuation ``.,!?;:`` is stripped.

    Args:
        text: Input string to analyse.

    Returns:
        A dict mapping each word to its frequency.
    """
    cleaned = re.sub(r"[.,!?;:]", "", text).lower()
    words = cleaned.split()
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the *k* most frequent words in *text*.

    Ties are broken alphabetically (ascending).

    Args:
        text: Input string to analyse.
        k: Number of top entries to return.

    Returns:
        A list of ``(word, count)`` tuples sorted by count (desc), then word (asc).
    """
    counts = word_count(text)
    if not counts:
        return []
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]
