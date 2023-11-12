"""
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums.
If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums.
If there is no such element, rightSum[i] = 0.
Return the array answer.
"""
from typing import List


def left_right_difference(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        right_sum = sum(nums[i + 1:])
        left_sum = sum(nums[:i])
        result.append(abs(right_sum - left_sum))
    return result


if __name__ == '__main__':
    nums = [10, 4, 8, 3]
    print(left_right_difference(nums))
