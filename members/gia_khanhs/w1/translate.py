"""MY VERY CUSTOM MADE EXERCISE (DEFO NOT BY ANY AI LOL): Return consecutive characters paired with their repetition counts."""


def run_length_encode(text: str) -> list[tuple[str, int]]:
    if not text:
        return []

    encoded: list[tuple[str, int]] = []
    current_character = text[0]
    count = 1

    for character in text[1:]:
        if character == current_character:
            count += 1
        else:
            encoded.append((current_character, count))
            current_character = character
            count = 1

    encoded.append((current_character, count))
    return encoded
