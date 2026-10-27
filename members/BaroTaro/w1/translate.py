"""Algorithmic translations from C++ to Python."""


def gcd(a: int, b: int) -> int:
    """Compute greatest common divisor of a and b using Euclidean algorithm."""
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a
