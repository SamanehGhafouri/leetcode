"""
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also
given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if
it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
"""
from typing import List


def nearest_valid_point(x: int, y: int, points: List[List[int]]) -> int:
    smallest_manhattan_d = 99999
    index = -1
    for i in range(len(points)):
        if points[i][0] == x or points[i][1] == y:
            if abs(x - points[i][0]) + abs(y - points[i][1]) < smallest_manhattan_d:
                smallest_manhattan_d = abs(x - points[i][0]) + abs(y - points[i][1])
                index = i
    return index


if __name__ == '__main__':
    x = 3
    y = 4
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    print(nearest_valid_point(x, y, points))
