"""
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane.
Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered
at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are
considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
"""
from typing import List
import math


def count_points(points: list[List[int]], queries: List[List[int]]) -> List[int]:
    result = []
    for circle in queries:
        count_p = 0
        for point in points:
            if math.dist([circle[0], circle[1]], [point[0], point[1]]) <= circle[2]:
                count_p += 1
        result.append(count_p)
    return result


if __name__ == '__main__':
    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    print(count_points(points, queries))
