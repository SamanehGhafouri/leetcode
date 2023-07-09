"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


def rotate_array_in_place(nums: List[int], k: int):
    k = k % len(nums)
    nums.reverse()

    # un-reverse the left portion of nums
    i, j = 0, k - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1

    # un-reverse the right portion of nums
    i, j = k, len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1

    return nums


def rotate_array_with_extra_memory(nums: List[int], k: int):
    k = k % len(nums)
    fall_off = len(nums) - k
    copy_nums = nums[fall_off:] + nums[:fall_off]
    for i in range(len(nums)):
        nums[i] = copy_nums[i]
    return nums


if __name__ == '__main__':
    data = [
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, [6, 7, 8, 1, 2, 3, 4, 5]),
        ([1], 1, [1]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5, 6, 7], 2, [6, 7, 1, 2, 3, 4, 5]),
        ([1, 2], 5, [2, 1]),
        ([1, 2, 3], 5, [2, 3, 1])
    ]
    for nums, k, expected in data:
        actual = rotate_array_in_place(nums, k)
        print(actual == expected, actual, expected)
