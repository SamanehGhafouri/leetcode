"""
Given a zero-based permutation nums (0-indexed),
build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
"""
from typing import List


class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(0, len(nums)):
            new_list.append(nums[nums[i]])
        return new_list


if __name__ == '__main__':

    pr = Solution()
    result = pr.buildArray([0, 2, 1, 5, 3, 4])
    print(result)
