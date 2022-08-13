"""
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example,
if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.
"""

from typing import List


def count_good_rectangles(rectangles: List[List[int]]) -> int:
    square_counts = {}
    for rectangle in rectangles:

        min_length = min(rectangle)
        if min_length in square_counts:
            square_counts[min_length] += 1
        else:
            square_counts[min_length] = 1
    maxi = max(square_counts)
    return square_counts[maxi]


if __name__ == '__main__':
    arr_rect = [[5, 8], [3, 9], [3, 12]]
    print(count_good_rectangles(arr_rect))
