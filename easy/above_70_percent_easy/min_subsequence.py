"""
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum
of the non included elements in such subsequence.

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions,
return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by
erasing some (possibly zero) elements from the array.

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted
in non-increasing order.
"""
from typing import List


def min_subsequence(nums: List[int]) -> List[int]:
    nums.sort()
    sum_all_nums = sum(nums[::])
    greatest = []
    count = 0
    if len(nums) == 1:
        return nums
    if len(nums) == 2 and nums[0] == nums[1]:
        return nums

    for _ in range(1, len(nums)):
        diff = sum_all_nums - nums[-1]
        greatest.append(nums[-1])
        count += nums[-1]
        sum_all_nums -= nums[-1]
        nums.pop()
        if diff == count and len(nums) == 2:
            return nums
        if diff >= count:
            continue
        return greatest


if __name__ == '__main__':
    li = [4, 3, 10, 9, 8]
    print(min_subsequence(li))
