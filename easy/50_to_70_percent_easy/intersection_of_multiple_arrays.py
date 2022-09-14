"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
return the list of integers that are present in each array of nums sorted in ascending order.
"""
from typing import List


def intersection(nums: List[List[int]]) -> List[int]:
    stack = [set(nums[0])]

    for i in range(1, len(nums)):
        stack.append(set(nums[i]).intersection(stack.pop()))
    return sorted(list(stack.pop()))


if __name__ == '__main__':
    arr = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    # arr = [[1, 2, 3], [4, 5, 6]]
    print(intersection(arr))
