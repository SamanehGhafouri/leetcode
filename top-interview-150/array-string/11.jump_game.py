"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
from typing import List


def can_jump(nums: List[int]) -> bool:
    if len(nums) == 0:
        return False
    if len(nums) == 1:
        return True
    im_here = nums[0]
    if im_here == 0:
        return False
    if im_here >= len(nums) - 1:
        return True

    for i in range(1, len(nums)):
        im_here -= 1
        if i != len(nums) - 1 and im_here == 0 and nums[i] == 0:
            return False
        if im_here <= nums[i] and i != len(nums):
            im_here = nums[i]
    return True


if __name__ == '__main__':
    items = [
        ([1, 1, 0, 1], False),
        ([1, 1, 1, 0], True),
        ([1, 1, 0, 1], False),
        ([4, 0, 3, 4, 1, 4, 2, 1], True),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1], True),
        ([1, 0, 1, 0], False),
        ([1, 1, 1, 1], True),
        ([], False),
        ([2, 5, 0, 0], True)
    ]
    for item in items:
        print(can_jump(item[0]) == item[1], item[0], item[1])
