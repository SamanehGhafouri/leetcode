"""
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.
"""
from typing import List


def minimum_operations(nums: List[int]) -> int:
    set_nums = set(nums)
    if len(nums) == 1 and 0 in set_nums:
        return 0
    elif 0 in set_nums:
        set_nums.remove(0)
        return len(set_nums)
    else:
        return len(set_nums)


if __name__ == '__main__':
    li = [1, 0, 6, 3]
    print(minimum_operations(li))
