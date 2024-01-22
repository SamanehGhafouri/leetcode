"""
There are n houses evenly lined up on the street, and each house is beautifully painted.
You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
"""

from typing import List


def max_distance(colors: List[int]) -> int:
    i = 0
    j = len(colors) - 1
    distance_left = 0
    while i < j:
        if colors[i] != colors[j]:
            distance_left = abs(i - j)
            break
        j -= 1

    i = 0
    j = len(colors) - 1
    distance_right = 0
    while i < j:
        if colors[i] != colors[j]:
            distance_right = abs(i - j)
            break
        i += 1
    return max(distance_right, distance_left)


if __name__ == '__main__':
    colors = [4, 4, 4, 11, 4, 4, 11, 4, 4, 4, 4, 4]
    print(max_distance(colors))
