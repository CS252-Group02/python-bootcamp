def transpose(matrix: list[list[float]]) -> list[list[float]]:
    """
    Difference from C++:
    In C++, nested vector indexing matrix[r][c] requires manually managing 
    container capacity or resize operations before assignment. In Python, we 
    can dynamically construct the transposed rows by creating temporary lists 
    and appending elements from each column, avoiding index-out-of-range errors 
    and memory management code.
    """
    if not matrix or not matrix[0]:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = []
    for col_index in range(num_cols):
        new_row = []
        for row_index in range(num_rows):
            new_row.append(matrix[row_index][col_index])

        result.append(new_row)
    return result