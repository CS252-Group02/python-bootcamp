def binary_search(a: list[int], key: int) -> int:
    """Return index of key in sorted list a, or -1 if absent."""
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
