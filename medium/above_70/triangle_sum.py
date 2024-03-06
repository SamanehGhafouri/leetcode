"""
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums
of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes
modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.
"""
from typing import List


def triangle_sum(nums: List[int]) -> int:
    l = len(nums)
    while l != 1:
        for i in range(len(nums) - 1):
            sum_nums = nums[i] + nums[i + 1]
            if sum_nums >= 10:
                sum_nums %= 10
            nums[i] = sum_nums
        nums.pop()
        l -= 1
    return nums[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(triangle_sum(nums))
