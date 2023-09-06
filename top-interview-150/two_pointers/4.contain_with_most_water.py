"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
from typing import List


def max_area(height: List[int]) -> int:
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        if height[i] <= height[j]:
            area = (height[i] * (j - i))
        elif height[i] > height[j]:
            area = (height[j] * (j - i))
        if area > max_area:
            max_area = area
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return max_area


if __name__ == '__main__':
    h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(h))
