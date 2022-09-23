"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
[[1,2,3,4],
[5,1,2,3],
[9,5,1,2]]
"""
from typing import List


def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    for ri in range(1, len(matrix)):
        for ci in range(1, len(matrix[0])):
            if matrix[ri][ci] != matrix[ri - 1][ci - 1]:
                return False
    return True


if __name__ == '__main__':
    m = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(is_toeplitz_matrix(m))
