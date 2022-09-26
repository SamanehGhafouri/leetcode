"""
A square matrix is said to be an X-Matrix if both of the following conditions hold:

    * All the elements in the diagonals of the matrix are non-zero.
    * All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix,
return true if grid is an X-Matrix. Otherwise, return false.
"""
from typing import List


def check_x_matrix(grid: List[List[int]]) -> bool:
    n = len(grid)

    for i in range(n):
        for j in range(n):

            if i == j or i + j == n - 1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True


if __name__ == '__main__':
    g = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]
    print(check_x_matrix(g))
