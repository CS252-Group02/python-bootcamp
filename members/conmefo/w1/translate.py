def primes_up_to(n: int) -> list[int]:
    """Use a Python boolean list instead of C++ vector<bool> for the sieve."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    candidate = 2
    while candidate * candidate <= n:
        if is_prime[candidate]:
            for multiple in range(candidate * candidate, n + 1, candidate):
                is_prime[multiple] = False
        candidate += 1

    return [number for number in range(2, n + 1) if is_prime[number]]
