"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
that are not part of the primary diagonal.
"""
from typing import List


def diagonal_sum(mat: List[List[int]]) -> int:
    total_sum = 0
    for i in range(len(mat)):
        total_sum += mat[i][i]
        if len(mat) % 2 != 0 and i != len(mat) // 2:
            total_sum += mat[i][-1 - i]
        if len(mat) % 2 == 0:
            total_sum += mat[i][-1 - i]
    return total_sum


if __name__ == '__main__':
    li_matrix = [[4, 6, 7], [2, 9, 4], [5, 5, 5]]
    print(diagonal_sum(li_matrix))
