_PUNCT = ".,!?;:"

_TRANSLATE = str.maketrans({ch: " " for ch in _PUNCT})


def word_count(text: str) -> dict[str, int]:
    """Count lowercase words after replacing common punctuation."""
    counts: dict[str, int] = {}
    for word in text.lower().translate(_TRANSLATE).split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return up to k words ordered by count and then alphabetically."""
    counts = word_count(text)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:k]
