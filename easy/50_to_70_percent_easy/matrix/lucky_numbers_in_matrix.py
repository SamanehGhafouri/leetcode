"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
"""
from typing import List


def lucky_numbers(matrix: List[List[int]]) -> List[int]:
    max_columns = set()
    min_rows = set()
    for li in matrix:
        min_rows.add(min(li))

    A = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            A[c][r] = matrix[r][c]

    for li in A:
        max_columns.add(max(li))

    intersect = min_rows.intersection(max_columns)
    if len(intersect) == 0:
        return []
    return list(intersect)


if __name__ == '__main__':
    m = [[7, 8], [1, 2]]
    print(lucky_numbers(m))
