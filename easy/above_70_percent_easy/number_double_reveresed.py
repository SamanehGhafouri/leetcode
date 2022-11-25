"""
Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if
reversed2 equals num. Otherwise return false.
"""


def is_same_after_reversals(num: int) -> bool:
    return str(int(str(num)[::-1]))[::-1] == str(num)


if __name__ == '__main__':
    n = 1800
    print(is_same_after_reversals(n))
