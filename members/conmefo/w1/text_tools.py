"""Week 1 word counting helpers."""


def word_count(text: str) -> dict[str, int]:
    """Count lowercase words in text, ignoring basic punctuation."""
    text = text.lower()
    for punctuation in ".,!?;:":
        text = text.replace(punctuation, " ")

    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, ties broken alphabetically."""
    if k <= 0:
        return []

    counts = word_count(text)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:k]
