"""
There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical
square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the
building located in the block at row r and column c.

A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance.
The skyline from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings by any amount
(the amount can be different per building). The height of a 0-height building can also be increased. However,
increasing the height of a building should not affect the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline
from any cardinal direction.
"""
from typing import List


def max_increase_keeping_skyline(grid: List[List[int]]) -> int:
    li_max_row = []
    li_max_col = []
    for i in range(len(grid)):
        li_max_row.append(max(grid[i]))
        col_nums = []
        for j in range(len(grid[i])):
            col_nums.append(grid[j][i])
        li_max_col.append(max(col_nums))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            min_row_col = min(li_max_row[i], li_max_col[j])
            diff = min_row_col - grid[i][j]
            count += diff
    return count


if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(max_increase_keeping_skyline(grid))
