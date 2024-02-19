"""
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every
two consecutive elements is the same. More formally, a sequence s is arithmetic if and only
if s[i+1] - s[i] == s[1] - s[0] for all valid i.
For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic:

1, 1, 2, 5, 7
"""
from typing import List


def is_arithmetic(numbers: List[int]) -> bool:
    numbers.sort()
    diff = abs(numbers[1] - numbers[0])
    helper_num = numbers.pop() - diff
    while numbers:
        if numbers.pop() != helper_num:
            return False
        else:
            helper_num -= diff
    return True


def check_arithmetic_subarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    result = []
    for left, right in zip(l, r):
        result.append(is_arithmetic(nums[left:right + 1]))
    return result


if __name__ == '__main__':
    nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
    l = [0, 1, 6, 4, 8, 7]
    r = [4, 4, 9, 7, 9, 10]
    print(check_arithmetic_subarrays(nums, l, r))
