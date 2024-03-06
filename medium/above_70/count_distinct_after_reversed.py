"""
You are given an array nums consisting of positive integers.

You have to take each integer in the array, reverse its digits, and add it to the end of the array.
You should apply this operation to the original integers in nums.

Return the number of distinct integers in the final array.
"""
from typing import List


def count_distinct_integers(nums: List[int]) -> int:
    set_nums_plus_distinct_int = set(nums)
    for n in nums:
        reversed_digits = int(str(n)[::-1])
        if reversed_digits not in set_nums_plus_distinct_int:
            set_nums_plus_distinct_int.add(reversed_digits)
    return len(set_nums_plus_distinct_int)


if __name__ == '__main__':
    n = [1, 13, 10, 12, 31]
    print(count_distinct_integers(n))
