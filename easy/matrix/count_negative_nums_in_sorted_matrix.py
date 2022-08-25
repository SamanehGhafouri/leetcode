"""
Given a m x n matrix grid which is sorted in non-increasing
order both row-wise and column-wise, return the number of negative numbers in grid.
"""
from typing import List


def count_negatives(grid: List[List[int]]) -> int:
    count = 0
    for li in grid:
        for j in reversed(li):
            if j < 0:
                count += 1
            else:
                break
    return count


if __name__ == '__main__':
    matrix = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(count_negatives(matrix))
