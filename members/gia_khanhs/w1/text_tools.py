import string
from collections import defaultdict


def word_count(text: str) -> dict[str, int]:
    """Count lowercase words after removing punctuation."""
    res: dict[str, int] = defaultdict(int)

    text = "".join([char
            for char in text
            if char not in string.punctuation]).lower()

    for word in text.split():
        res[word] += 1

    return dict(res)

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, keeping encounter order for ties."""
    word_cnt_dict: dict[str, int] = word_count(text)
    word_cnt_list: list[tuple[str, int]] = [(key, val)
                                            for key, val in word_cnt_dict.items()]

    word_cnt_list = sorted(word_cnt_list, key=lambda word: word[1], reverse=True)

    return word_cnt_list[:k]
