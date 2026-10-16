def word_count(text: str) -> dict[str, int]:
    punctuation = ".,?!;:"
    text = text.lower()
    for char in punctuation:
        text = text.replace(char, " ")
    
    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def top_k(text: str, k: int ) -> list[tuple[str,int]]:
    counts = word_count(str)

    items = list(counts.items())

    items.sort(key=lambda x: (-x[1], x[0]))

    return items[:k]
    