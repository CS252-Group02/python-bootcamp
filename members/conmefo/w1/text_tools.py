def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    for punctuation in ".,!?;:":
        text = text.replace(punctuation, " ")

    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []

    counts = word_count(text)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:k]
