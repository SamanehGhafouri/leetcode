"""
You are given a 0-indexed integer array nums. In one operation, you may do the following:

Choose two integers in nums that are equal.
Remove both integers from nums, forming a pair.
The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are
formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.
"""

from typing import List


def number_of_pairs(nums: List[int]) -> List[int]:
    dict_numbers = {}

    for i in nums:
        if i not in dict_numbers:
            dict_numbers[i] = 1
        else:
            dict_numbers[i] += 1

    count_pairs = 0
    count_leftovers = 0
    result = []
    for k, v in dict_numbers.items():

        if v % 2 != 0:
            count_pairs += v // 2
            count_leftovers += v % 2
        else:
            count_pairs += v // 2
    result.append(count_pairs)
    result.append(count_leftovers)
    return result


if __name__ == '__main__':
    nums_arr = [1, 3, 2, 1, 3, 2, 2]
    print(number_of_pairs(nums_arr))
