"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to
visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
"""
from typing import List


def min_time_visit(points: List[List[int]]) -> int:
    total_time = 0
    for i in range(len(points) - 1):

        if abs(points[i + 1][0] - points[i][0]) > abs(points[i + 1][1] - points[i][1]):
            total_time += abs(points[i + 1][0] - points[i][0])
        else:
            total_time += abs(points[i + 1][1] - points[i][1])
    return total_time


if __name__ == '__main__':
    points_m = [[3, 2], [-2, 2]]
    print(min_time_visit(points_m))
