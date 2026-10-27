"""Text processing and word count analysis tools."""


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in text, ignoring punctuation and case."""
    punctuation = ".,?!;:"
    text = text.lower()

    for char in punctuation:
        text = text.replace(char, " ")

    words = text.split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k words sorted by frequency (descending), then alphabetically."""
    counts = word_count(text)
    items = list(counts.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:k]
