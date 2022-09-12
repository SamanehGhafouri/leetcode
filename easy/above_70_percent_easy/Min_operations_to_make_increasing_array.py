"""
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment
it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
An array of length 1 is trivially strictly increasing.
"""
from typing import List


def min_operations(nums: List[int]) -> int:
    count = 0
    for num in range(len(nums) - 1):

        if nums[num] >= nums[num + 1]:
            diff = abs(nums[num] - nums[num + 1])
            count += diff + 1
            nums[num + 1] = nums[num + 1] + diff + 1
    return count


if __name__ == '__main__':
    arr_nums = [1]
    print(min_operations(arr_nums))
