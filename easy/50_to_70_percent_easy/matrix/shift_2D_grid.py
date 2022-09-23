"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""
from typing import List


def shift_grid(grid: List[List[int]], k: int) -> List[List[int]]:
    if k == len(grid[0]) * len(grid):
        return grid
    q = []
    for row in grid:
        for col in row:
            q.append(col)

    for _ in range(k):
        q.insert(0, q[-1])
        q.pop()

    result = []
    while q:
        result.append(q[:len(grid[0])])
        q = q[len(grid[0]):]
    return result


if __name__ == '__main__':
    g = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k = 4
    print(shift_grid(g, k))
