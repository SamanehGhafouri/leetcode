"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other
elements in row i and column j are 0 (rows and columns are 0-indexed).
"""
from typing import List


def num_special_positions(mat: List[List[int]]) -> int:
    count = 0
    for r in mat:
        if sum(r) == 1:
            indx = r.index(1)
            c = 0
            for row in mat:
                if row[indx] == 1:
                    c += 1
            if c == 1:
                count += 1
    return count


if __name__ == '__main__':
    # mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    # mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # mat = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    mat = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 1, 1, 0, 0, 0, 0]]
    print(num_special_positions(mat))
