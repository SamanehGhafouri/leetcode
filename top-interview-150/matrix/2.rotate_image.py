"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(m))
