"""
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones,
and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should
be selected.

Return an array containing the index of the row, and the number of ones in it.
"""
from typing import List


def row_max_ones(mat: List[List[int]]) -> List[int]:
    indx, max_ones = (0, sum(mat[0]))
    for i, li in enumerate(mat):
        if max_ones < sum(li):
            indx, max_ones = i, sum(li)
    return [indx, max_ones]


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 1]]
    print(row_max_ones(mat))
