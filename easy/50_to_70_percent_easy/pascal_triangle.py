"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
1
11
121
1331
14641
"""
from typing import List


def generate(num_rows: int) -> List[List[int]]:
    arr = [[0 for _ in range(i)] for i in range(1, num_rows + 1)]

    for row in range(num_rows):
        for i in range(row + 1):
            if i == 0 or i == row:
                arr[row][i] = 1
            else:
                arr[row][i] = arr[row - 1][i - 1] + arr[row - 1][i]
    return arr


if __name__ == '__main__':
    n_rows = 5
    print(generate(n_rows))
