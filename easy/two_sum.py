"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:

        num_seen = {}

        for index, value in enumerate(nums):

            remaining = target - nums[index]

            if remaining in num_seen:
                return [index, num_seen[remaining]]
            num_seen[value] = index


if __name__ == '__main__':
    final = Solution()
    lis = [2, 7, 11, 15]
    t = 9
    print(final.two_sum(lis, t))




