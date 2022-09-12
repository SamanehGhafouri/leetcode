"""
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file
line in non-decreasing order by height. Let this ordering be represented by the integer array expected where
expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students
are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].
"""
from typing import List


def height_checker(heights: List[int]) -> int:
    not_in_order = 0
    sorted_height = sorted(heights)
    for i, j in zip(heights, sorted_height):
        if i != j:
            not_in_order += 1
    return not_in_order


if __name__ == '__main__':
    li_heights = [1, 2, 3, 4, 5]
    print(height_checker(li_heights))
