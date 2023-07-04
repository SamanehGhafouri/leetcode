"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of
the integer. The digits are ordered from most significant to least significant in left-to-right order. The large
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

from typing import List


def plus_one(digits: List[int]) -> List[int]:
    convert_to_str = "".join(str(i) for i in digits)
    add_one_int = int(convert_to_str) + 1
    list_str_add_one_int = list(str(add_one_int))
    result = [int(x) for x in list_str_add_one_int]
    return result


if __name__ == '__main__':
    d = [9, 9]
    print(plus_one(d))
