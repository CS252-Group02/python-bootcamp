def insertion_sort(a: list[int]) -> list[int]:
    """
    Sort a list in ascending order using insertion sort.

    Difference from C++:
    Python uses list instead of std::vector<int>.
    Python also uses indentation instead of braces
    and does not require explicit variable types.

    The sorting is performed in-place.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a
