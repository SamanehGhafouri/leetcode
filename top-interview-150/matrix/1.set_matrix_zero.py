"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    set_zero_row_col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                set_zero_row_col.add((i, j))
    for item in set_zero_row_col:
        row = item[0]
        col = item[1]
        for i in range(len(matrix[0])):
            matrix[row][i] = 0
        for j in range(len(matrix)):
            matrix[j][col] = 0


if __name__ == '__main__':
    # m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    m = [[0, 1]]
    print(set_zeroes(m))
