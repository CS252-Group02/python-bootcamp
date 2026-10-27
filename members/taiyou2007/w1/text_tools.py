def word_count(text: str) -> dict[str, int]:
    """Count lowercase words, treating common punctuation as separators."""
    text = text.lower()

    for char in ".,!?;:":
        text = text.replace(char, " ")

    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Slice words ranked by descending count and alphabetical ties."""
    counts = word_count(text)

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:k]


        