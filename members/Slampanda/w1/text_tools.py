def word_count(text: str) -> dict[str, int]:
    text_lower = text.lower()
    for punct in ".,!?;:":
        text_lower = text_lower.replace(punct, "")
    
    words = text_lower.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    def sort_key(item):
        word = item[0]
        count = item[1]
        return (-count, word)
    
    items = list(counts.items())
    items.sort(key=sort_key)
    return items[:k]
