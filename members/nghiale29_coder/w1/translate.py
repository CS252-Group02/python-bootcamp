"""W1-4: Translate C++ Insertion Sort to Pythonic Python.

Original C++ algorithm (in-place):
    void insertionSort(vector<int>& arr) {
        for (int i = 1; i < arr.size(); i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
"""


def insertion_sort(arr: list) -> list:
    """Sort *arr* using insertion sort and return the sorted list.

    Differences from the C++ version:
    1. **Return instead of mutate**: The C++ version modifies the vector
       in-place via a reference parameter (``vector<int>&``). This Python
       version works on a copy and returns a new list, following the
       principle of least surprise — callers' original data is untouched.
    2. **No manual memory management**: C++ requires explicit index arithmetic
       to shift elements; Python's expressive slice assignment
       (``result.insert(j, key)``) makes the intent immediately clear.
    3. **Duck typing**: The function works on any list whose elements support
       ``<`` comparison (ints, floats, strings …) without template boilerplate.

    Args:
        arr: A list of comparable elements.

    Returns:
        A new list containing all elements of *arr* in ascending order.
    """
    result = list(arr)  # copy — do not mutate the caller's list
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result
