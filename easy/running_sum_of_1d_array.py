"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
from typing import List


def running_sum(nums: List[int]) -> List[int]:
    accumulator = 0
    new_nums = []
    for i in nums:
        new_nums.append(i + accumulator)
        accumulator += i
    return new_nums


if __name__ == '__main__':

    nums_one = [1, 2, 3, 4]
    print(running_sum(nums_one))